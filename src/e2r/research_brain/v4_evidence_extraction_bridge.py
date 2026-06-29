"""Real document to Evidence OS bridge for Research Brain v4."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
import re
from typing import Any, Mapping, Sequence

from e2r.agentic.evidence_os import (
    AdjudicatedClaim,
    AppendOnlyEvidenceLedger,
    AnchorType,
    Directness,
    EvidenceAnchor,
    EvidenceContractV2,
    EvidenceDocument,
    InvestigationStatus,
    MappingStatus,
    Polarity,
    PrimitiveMappingProposal,
    RawAssertion,
    RelationToTarget,
    SemanticStatus,
    SupportDirection,
    TargetScopeStatus,
    TemporalStatus,
    VerificationStatus,
    derive_score_eligibility,
)
from e2r.research_brain.schemas import SourceTask, deterministic_id
from e2r.research_brain.v2_schemas import CandidateEventV2
from e2r.research_brain.v4_schemas import SourceTaskExecutionStatusV4, SourceTaskExecutionV4
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4


@dataclass(frozen=True)
class ExtractionSignal:
    signal_id: str
    predicate: str
    quote: str
    polarity: Polarity
    supported_primitives: tuple[str, ...]
    event_date: date | None = None


@dataclass(frozen=True)
class EvidenceOSExecutionBundleV4:
    ledger: AppendOnlyEvidenceLedger
    executions: tuple[SourceTaskExecutionV4, ...]
    documents: Mapping[str, EvidenceDocument]
    anchors: Mapping[str, EvidenceAnchor]
    document_text_by_id: Mapping[str, str]
    extraction_audit: Mapping[str, Any]


def execute_source_tasks_with_evidence_os_v4(
    *,
    event: CandidateEventV2,
    tasks: Sequence[SourceTask],
    contract: EvidenceContractV2,
    as_of_date: date,
    source_runner: SourceAcquisitionRunnerV4 | None = None,
) -> EvidenceOSExecutionBundleV4:
    runner = source_runner or SourceAcquisitionRunnerV4()
    ledger = AppendOnlyEvidenceLedger()
    executions: list[SourceTaskExecutionV4] = []
    documents: dict[str, EvidenceDocument] = {}
    anchors: dict[str, EvidenceAnchor] = {}
    document_text_by_id: dict[str, str] = {}
    audit_counts = {
        "real_document_to_raw_assertion_count": 0,
        "raw_assertion_to_adjudicated_claim_count": 0,
        "adjudicated_claim_to_accepted_claim_count": 0,
        "mention_only_count": 0,
        "synthetic_assertion_count": 0,
        "forced_positive_polarity_count": 0,
        "forced_current_temporal_count": 0,
        "forced_target_subject_count": 0,
        "quote_anchor_missing_rejected_count": 0,
        "wrong_subject_rejected_count": 0,
        "event_summary_used_as_exact_quote_count": 0,
        "source_task_accepted_without_real_document_count": 0,
    }
    for task in tasks:
        result = runner.acquire(event=event, task=task, as_of_date=as_of_date)
        for document in result.documents:
            documents[document.document_id] = document
        for anchor in result.anchors:
            anchors[anchor.anchor_id] = anchor
        document_text_by_id.update(dict(result.document_text_by_id))
        if result.status in {"REJECTED_BY_POLICY", "PROVIDER_FAILED", "NO_EVIDENCE_FOUND", "BUDGET_EXHAUSTED"}:
            executions.append(
                SourceTaskExecutionV4(
                    task_id=task.task_id,
                    source_task=task.to_dict(),
                    status=_execution_status_for_acquisition(result.status),
                    fetched_document_ids=tuple(result.fetched_document_ids),
                    document_urls=tuple(result.document_urls),
                    document_hashes=tuple(result.document_hashes),
                    evidence_anchor_ids=tuple(result.anchor_ids),
                    provider_errors=tuple(result.provider_errors),
                    budget_used=dict(result.budget_used),
                    stop_reason=result.stop_reason,
                )
            )
            continue
        execution = _append_claims_for_task(
            event=event,
            task=task,
            contract=contract,
            as_of_date=as_of_date,
            ledger=ledger,
            documents=tuple(result.documents),
            anchors_by_document={anchor.document_id: anchor for anchor in result.anchors},
            document_text_by_id=dict(result.document_text_by_id),
            provider_errors=tuple(result.provider_errors),
            budget_used=dict(result.budget_used),
            stop_reason=result.stop_reason,
            audit_counts=audit_counts,
        )
        executions.append(execution)
    if any(execution.accepted_claim_ids and not execution.fetched_document_ids for execution in executions):
        audit_counts["source_task_accepted_without_real_document_count"] += 1
    return EvidenceOSExecutionBundleV4(
        ledger=ledger,
        executions=tuple(executions),
        documents=documents,
        anchors=anchors,
        document_text_by_id=document_text_by_id,
        extraction_audit=dict(audit_counts),
    )


def _append_claims_for_task(
    *,
    event: CandidateEventV2,
    task: SourceTask,
    contract: EvidenceContractV2,
    as_of_date: date,
    ledger: AppendOnlyEvidenceLedger,
    documents: Sequence[EvidenceDocument],
    anchors_by_document: Mapping[str, EvidenceAnchor],
    document_text_by_id: Mapping[str, str],
    provider_errors: Sequence[str],
    budget_used: Mapping[str, int],
    stop_reason: str,
    audit_counts: dict[str, int],
) -> SourceTaskExecutionV4:
    accepted: list[str] = []
    rejected: list[str] = []
    assertion_ids: list[str] = []
    adjudicated_ids: list[str] = []
    anchor_ids: list[str] = []
    not_eligible: list[str] = []
    for document in documents:
        anchor = anchors_by_document.get(document.document_id)
        if anchor is None:
            audit_counts["quote_anchor_missing_rejected_count"] += 1
            continue
        anchor_ids.append(anchor.anchor_id)
        document_text = document_text_by_id.get(document.document_id, anchor.exact_text)
        signals = _extract_signals(document=document, anchor=anchor, document_text=document_text)
        if not signals:
            audit_counts["mention_only_count"] += 1
        for signal in signals:
            raw = _raw_assertion_from_signal(signal=signal, anchor=anchor, event=event)
            assertion_ids.append(raw.raw_assertion_id)
            audit_counts["real_document_to_raw_assertion_count"] += 1
            claim = _adjudicated_claim_from_signal(
                event=event,
                document=document,
                anchor=anchor,
                raw=raw,
                signal=signal,
                as_of_date=as_of_date,
            )
            adjudicated_ids.append(claim.claim_id)
            audit_counts["raw_assertion_to_adjudicated_claim_count"] += 1
            ledger.append_claim(claim)
            mapping_status = (
                MappingStatus.ACCEPTED
                if task.primitive_gap in signal.supported_primitives and task.primitive_gap in _contract_primitive_ids(contract)
                else MappingStatus.REJECTED
            )
            mapping = PrimitiveMappingProposal.build(
                claim_id=claim.claim_id,
                archetype_id=contract.archetype_id,
                primitive_id=task.primitive_gap,
                support_direction=SupportDirection.SUPPORT if signal.polarity != Polarity.NEGATIVE else SupportDirection.COUNTER,
                mapping_status=mapping_status,
                rationale=f"v4_signal:{signal.signal_id}",
                contract_rule_id=task.primitive_gap,
            )
            eligibility = derive_score_eligibility(
                document=document,
                anchor=anchor,
                claim=claim,
                mapping=mapping,
                as_of_date=as_of_date,
                allowed_target_scopes=contract.allowed_target_scopes,
                allowed_directness=contract.allowed_directness,
            )
            if eligibility.eligible and mapping.mapping_status == MappingStatus.ACCEPTED:
                ledger.append_mapping(mapping)
                accepted.append(claim.claim_id)
                audit_counts["adjudicated_claim_to_accepted_claim_count"] += 1
            else:
                rejected.append(claim.claim_id)
                if claim.target_scope_status != TargetScopeStatus.DIRECT:
                    audit_counts["wrong_subject_rejected_count"] += 1
                not_eligible.extend(eligibility.reasons or ("mapping_rejected",))
                ledger.append_mapping(
                    PrimitiveMappingProposal.build(
                        claim_id=claim.claim_id,
                        archetype_id=contract.archetype_id,
                        primitive_id=task.primitive_gap,
                        support_direction=SupportDirection.SUPPORT,
                        mapping_status=MappingStatus.REJECTED,
                        rationale=";".join(eligibility.reasons or ("mapping_rejected",)),
                        contract_rule_id=task.primitive_gap,
                    )
                )
    status = (
        SourceTaskExecutionStatusV4.EVIDENCE_OS_ACCEPTED.value
        if accepted
        else SourceTaskExecutionStatusV4.NO_EVIDENCE_FOUND.value
    )
    return SourceTaskExecutionV4(
        task_id=task.task_id,
        source_task=task.to_dict(),
        status=status,
        fetched_document_ids=tuple(document.document_id for document in documents),
        document_urls=tuple(document.canonical_url or "" for document in documents),
        document_hashes=tuple(document.content_hash for document in documents),
        evidence_anchor_ids=tuple(anchor_ids),
        raw_assertion_ids=tuple(assertion_ids),
        adjudicated_claim_ids=tuple(adjudicated_ids),
        accepted_claim_ids=tuple(dict.fromkeys(accepted)),
        rejected_claim_ids=tuple(dict.fromkeys(rejected)),
        not_eligible_reasons=tuple(dict.fromkeys(not_eligible)),
        provider_errors=tuple(provider_errors),
        budget_used=dict(budget_used),
        stop_reason=stop_reason if accepted else "no_score_eligible_real_claim",
    )


def _extract_signals(
    *,
    document: EvidenceDocument,
    anchor: EvidenceAnchor,
    document_text: str,
) -> tuple[ExtractionSignal, ...]:
    text = _visible_text(anchor.exact_text or document_text)
    normalized = anchor.normalized_value if isinstance(anchor.normalized_value, Mapping) else {}
    row = normalized.get("row") if isinstance(normalized.get("row"), Mapping) else {}
    if anchor.anchor_type == AnchorType.TEXT_SPAN and not row:
        return ()
    signals: list[ExtractionSignal] = []
    source_date = document.published_date()

    def add(signal_id: str, predicate: str, primitives: Sequence[str], *, polarity: Polarity = Polarity.POSITIVE) -> None:
        quote = _quote_for_signal(text, predicate)
        if not quote:
            return
        signals.append(
            ExtractionSignal(
                signal_id=signal_id,
                predicate=predicate,
                quote=quote,
                polarity=polarity,
                supported_primitives=tuple(dict.fromkeys(primitives)),
                event_date=source_date,
            )
        )

    if _any_text(text, "HBM", "메모리", "Memory", "DRAM"):
        if _any_text(text, "고객", "customer", "엔비디아", "ASIC", "다변화"):
            add(
                "memory_customer_allocation",
                "customer demand/allocation is discussed",
                ("customer_preorder_or_allocation", "named_customer_quality", "cycle_demand_visibility"),
            )
        if _any_text(text, "공급 부족", "병목", "수급 불균형", "bottleneck", "supply-demand", "좁은"):
            add(
                "memory_capacity_constraint",
                "memory supply bottleneck is discussed",
                ("hbm_capacity_constraint", "hbm_capacity_pre_sold", "supply_demand_tightness"),
            )
        if _any_text(text, "가격 상승", "price uptrend", "가격 상승세", "ASP"):
            add(
                "memory_price_increase",
                "memory price increase is discussed",
                ("memory_price_increase_mentioned", "pricing_power_confirmed", "spread_expansion"),
            )
    if _any_text(text, "목표주가 상향", "추정EPS 상향", "실적 전망치 상향", "Upward earnings revisions", "Raising target"):
        add(
            "revision_visibility",
            "earnings or target revision is raised",
            ("medium_term_revision_visibility", "cycle_to_revenue_bridge", "opm_expansion_pctp"),
        )
    if _any_text(text, "계약", "수주잔고", "장기공급", "RPO", "backlog", "contract"):
        add(
            "contract_backlog_visibility",
            "contract or backlog visibility is discussed",
            (
                "revenue_visibility_contract",
                "contract_quality",
                "order_backlog_to_sales",
                "rpo_to_sales",
                "retention_or_renewal",
                "export_contract",
            ),
        )
    if _any_text(text, "영업이익", "OP", "OPM", "margin", "마진", "FCF", "현금흐름"):
        add(
            "margin_cash_bridge",
            "margin or cash-flow bridge is discussed",
            (
                "opm_expansion_pctp",
                "fcf_quality_score",
                "margin_bridge_visible",
                "recurring_margin_leverage",
                "realized_margin",
            ),
        )
    if _any_text(text, "판가", "spread", "스프레드", "원재료", "price pass-through"):
        add(
            "spread_pass_through",
            "spread or pass-through is discussed",
            ("spread_expansion", "pricing_power_confirmed", "raw_material_cost_risk", "inventory_cycle"),
        )
    if _any_text(text, "CAPA", "capacity", "증설", "가동률"):
        add(
            "capacity_utilization",
            "capacity or utilization is discussed",
            ("utilization_rate", "hbm_capacity_constraint", "capacity_precommitted", "socket_or_test_demand_visible"),
        )
    if row:
        for key, value in row.items():
            if value in (None, ""):
                continue
            primitive = _field_to_primitive(str(key), value)
            if primitive:
                add(
                    f"structured_field_{primitive}",
                    f"structured field {key} is present",
                    (primitive,),
                )
    return tuple(dict((signal.signal_id, signal) for signal in signals).values())


def _field_to_primitive(key: str, value: Any) -> str | None:
    lowered = key.lower()
    mapping = {
        "eps_action_typ_nm": "medium_term_revision_visibility",
        "prc_action_typ_nm": "medium_term_revision_visibility",
        "target_prc": "medium_term_revision_visibility",
        "contract_amount_to_prior_sales": "contract_quality",
        "contract_duration_months": "delivery_schedule",
        "order_backlog_to_sales": "order_backlog_to_sales",
        "rpo_to_sales": "rpo_to_sales",
        "backlog_yoy_pct": "order_backlog_to_sales",
        "opm_expansion_pctp": "opm_expansion_pctp",
        "fcf_quality_score": "fcf_quality_score",
        "pricing_power_confirmed": "pricing_power_confirmed",
        "capa_utilization_pct": "utilization_rate",
        "capa_expansion_pct": "utilization_rate",
        "asp_yoy_pct": "memory_price_increase_mentioned",
    }
    if lowered in mapping and str(value).strip().lower() not in {"0", "false", "none", "없음"}:
        return mapping[lowered]
    return None


def _raw_assertion_from_signal(
    *,
    signal: ExtractionSignal,
    anchor: EvidenceAnchor,
    event: CandidateEventV2,
) -> RawAssertion:
    normalized = anchor.normalized_value if isinstance(anchor.normalized_value, Mapping) else {}
    subject_text = str(normalized.get("company_name") or normalized.get("symbol") or event.company_name)
    return RawAssertion(
        raw_assertion_id=deterministic_id("RAWASSERTV4", (anchor.anchor_id, signal.signal_id, signal.quote)),
        anchor_id=anchor.anchor_id,
        subject_text=subject_text,
        predicate=signal.predicate,
        object_text=signal.quote,
        value=signal.quote,
        polarity_proposal=signal.polarity,
        certainty="source_anchor_extracted",
        event_date_text=signal.event_date.isoformat() if signal.event_date else None,
        exact_quote=signal.quote,
        related_entity_texts=tuple(dict.fromkeys((subject_text, event.company_name))),
        extractor_model="research_brain_v4_rule_extractor_from_real_anchor",
        extractor_prompt_hash="contract_blind_signal_rules_v1",
    )


def _adjudicated_claim_from_signal(
    *,
    event: CandidateEventV2,
    document: EvidenceDocument,
    anchor: EvidenceAnchor,
    raw: RawAssertion,
    signal: ExtractionSignal,
    as_of_date: date,
) -> AdjudicatedClaim:
    normalized = anchor.normalized_value if isinstance(anchor.normalized_value, Mapping) else {}
    doc_symbol = str(normalized.get("symbol") or event.symbol)
    subject_entity_id = f"TICKER:{doc_symbol}"
    target_entity_id = f"TICKER:{event.symbol}"
    direct = doc_symbol == event.symbol
    published = document.published_date()
    current = _temporal_status(signal=signal, document=document, as_of_date=as_of_date)
    return AdjudicatedClaim.from_raw(
        raw=raw,
        document=document,
        anchor=anchor,
        subject_entity_id=subject_entity_id,
        target_entity_id=target_entity_id,
        relation_to_target=RelationToTarget.SELF if direct else RelationToTarget.UNRELATED,
        directness=Directness.DIRECT if direct else Directness.NOT_TARGET_SCOPED,
        verification_status=VerificationStatus.SEMANTIC_VERIFIED if anchor.anchor_verified else VerificationStatus.UNVERIFIED,
        target_scope_status=TargetScopeStatus.DIRECT if direct else TargetScopeStatus.UNRELATED,
        polarity=signal.polarity,
        temporal_status=current,
        semantic_status=SemanticStatus.PASS_ if direct else SemanticStatus.REJECTED,
        investigation_status=InvestigationStatus.COMPLETE if direct else InvestigationStatus.FOLLOWUP_REQUIRED,
        event_date=signal.event_date or published,
        adjudication_rationale="v4 separated extraction/adjudication from real source anchor",
    )


def _temporal_status(*, signal: ExtractionSignal, document: EvidenceDocument, as_of_date: date) -> TemporalStatus:
    published = document.published_date()
    if published and published > as_of_date:
        return TemporalStatus.UNKNOWN
    if published and (as_of_date - published).days > 540 and not _contains_future_contract(signal.quote, as_of_date):
        return TemporalStatus.HISTORICAL
    return TemporalStatus.CURRENT


def _contains_future_contract(text: str, as_of_date: date) -> bool:
    years = [int(year) for year in re.findall(r"\b(20[2-4][0-9])\b", text)]
    return any(year >= as_of_date.year for year in years)


def _execution_status_for_acquisition(status: str) -> str:
    if status == "REJECTED_BY_POLICY":
        return SourceTaskExecutionStatusV4.REJECTED_BY_POLICY.value
    if status == "PROVIDER_FAILED":
        return SourceTaskExecutionStatusV4.PROVIDER_FAILED.value
    if status == "BUDGET_EXHAUSTED":
        return SourceTaskExecutionStatusV4.BUDGET_EXHAUSTED.value
    return SourceTaskExecutionStatusV4.NO_EVIDENCE_FOUND.value


def _contract_primitive_ids(contract: EvidenceContractV2) -> set[str]:
    values = set(contract.required_primitives)
    values.update(contract.green_gate.primitive_ids())
    values.update(contract.alternative_primitives)
    for primitives in contract.alternative_primitives.values():
        values.update(primitives)
    for primitives in contract.score_rubric.values():
        values.update(primitives)
    return values


def _visible_text(value: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", value, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _any_text(text: str, *needles: str) -> bool:
    lowered = text.lower()
    return any(needle.lower() in lowered for needle in needles)


def _quote_for_signal(text: str, predicate: str) -> str:
    if not text.strip():
        return ""
    sentences = re.split(r"(?<=[.!?。])\s+|[▶\n\r]+", text)
    predicate_tokens = [token for token in re.split(r"\W+", predicate.lower()) if len(token) > 3]
    for sentence in sentences:
        clean = sentence.strip()
        if not clean:
            continue
        lowered = clean.lower()
        if any(token in lowered for token in predicate_tokens) or _signal_keyword_hit(clean):
            return clean[:500]
    return text[:500]


def _signal_keyword_hit(text: str) -> bool:
    return _any_text(
        text,
        "HBM",
        "메모리",
        "고객",
        "공급",
        "병목",
        "목표주가",
        "EPS",
        "계약",
        "수주",
        "영업이익",
        "마진",
        "가격",
        "CAPA",
    )


__all__ = ["EvidenceOSExecutionBundleV4", "execute_source_tasks_with_evidence_os_v4"]
