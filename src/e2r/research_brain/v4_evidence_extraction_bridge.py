"""Real document to Evidence OS bridge for Research Brain v4."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
import re
from typing import Any, Callable, Mapping, Sequence
from urllib.parse import urlsplit

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
    SourceType,
    SupportDirection,
    TargetScopeStatus,
    TemporalStatus,
    VerificationStatus,
    derive_score_eligibility,
)
from e2r.production.claim_extraction import (
    ExtractionInput,
    ExtractorProviderResult,
    LLMContractBlindRawAssertionExtractor,
    RawAssertionRecord,
    adjudicate_entity_temporal_scope,
    map_claim_to_primitive,
    validate_anchor,
)
from e2r.research_brain.schemas import SourceTask, deterministic_id
from e2r.research_brain.v2_schemas import CandidateEventV2
from e2r.research_brain.v4_schemas import SourceTaskExecutionStatusV4, SourceTaskExecutionV4
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
from e2r.sources.report_search import is_verified_report_original_url


@dataclass(frozen=True)
class ExtractionSignal:
    signal_id: str
    predicate: str
    quote: str
    polarity: Polarity
    supported_primitives: tuple[str, ...]
    extraction_method: str
    polarity_source: str
    event_date: date | None = None


@dataclass(frozen=True)
class EvidenceOSExecutionBundleV4:
    ledger: AppendOnlyEvidenceLedger
    executions: tuple[SourceTaskExecutionV4, ...]
    documents: Mapping[str, EvidenceDocument]
    anchors: Mapping[str, EvidenceAnchor]
    document_text_by_id: Mapping[str, str]
    extraction_audit: Mapping[str, Any]
    raw_assertions: Mapping[str, RawAssertion] = field(default_factory=dict)
    web_search_tasks: tuple[Mapping[str, Any], ...] = ()
    web_search_results: tuple[Mapping[str, Any], ...] = ()
    web_fetched_documents: tuple[Mapping[str, Any], ...] = ()
    web_rejected_documents: tuple[Mapping[str, Any], ...] = ()
    claim_extractor_runs: tuple[Mapping[str, Any], ...] = ()
    raw_assertion_rejections: tuple[Mapping[str, Any], ...] = ()


def execute_source_tasks_with_evidence_os_v4(
    *,
    event: CandidateEventV2,
    tasks: Sequence[SourceTask],
    contract: EvidenceContractV2,
    as_of_date: date,
    source_runner: SourceAcquisitionRunnerV4 | None = None,
    claim_extractor: LLMContractBlindRawAssertionExtractor | None = None,
    runtime_budget_exhausted: Callable[[], bool] | None = None,
) -> EvidenceOSExecutionBundleV4:
    runner = source_runner or SourceAcquisitionRunnerV4()
    extractor = claim_extractor or LLMContractBlindRawAssertionExtractor()
    ledger = AppendOnlyEvidenceLedger()
    executions: list[SourceTaskExecutionV4] = []
    documents: dict[str, EvidenceDocument] = {}
    anchors: dict[str, EvidenceAnchor] = {}
    document_text_by_id: dict[str, str] = {}
    raw_assertions: dict[str, RawAssertion] = {}
    web_search_tasks: list[Mapping[str, Any]] = []
    web_search_results: list[Mapping[str, Any]] = []
    web_fetched_documents: list[Mapping[str, Any]] = []
    web_rejected_documents: list[Mapping[str, Any]] = []
    claim_extractor_runs: list[Mapping[str, Any]] = []
    raw_assertion_rejections: list[Mapping[str, Any]] = []
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
        "llm_claim_extractor_attempt_count": 0,
        "llm_claim_extractor_success_count": 0,
        "llm_claim_extractor_provider_error_count": 0,
        "llm_claim_extractor_non_llm_provider_count": 0,
        "unstructured_text_to_raw_assertion_count": 0,
        "anchor_validation_rejected_count": 0,
        "post_extraction_web_rejected_document_count": 0,
        "source_task_score_admissibility_rejected_count": 0,
        "runtime_budget_skipped_source_task_count": 0,
        "runtime_budget_stopped_document_extraction_count": 0,
    }
    for task in tasks:
        if runtime_budget_exhausted is not None and runtime_budget_exhausted():
            audit_counts["runtime_budget_skipped_source_task_count"] += 1
            executions.append(_runtime_budget_skipped_execution(event=event, task=task))
            continue
        result = runner.acquire(event=event, task=task, as_of_date=as_of_date)
        for document in result.documents:
            documents[document.document_id] = document
        for anchor in result.anchors:
            anchors[anchor.anchor_id] = anchor
        document_text_by_id.update(dict(result.document_text_by_id))
        web_search_tasks.extend(result.web_search_tasks)
        web_search_results.extend(result.web_search_results)
        web_fetched_documents.extend(result.web_fetched_documents)
        web_rejected_documents.extend(result.web_rejected_documents)
        if result.status in {"REJECTED_BY_POLICY", "PROVIDER_FAILED", "NO_EVIDENCE_FOUND", "BUDGET_EXHAUSTED"}:
            executions.append(
                SourceTaskExecutionV4(
                    task_id=task.task_id,
                    source_task=task.to_dict(),
                    status=_execution_status_for_acquisition(result.status),
                    **_source_task_execution_identity(
                        event=event,
                        task=task,
                        source_class=result.source_class,
                        provider_name=result.provider_name,
                    ),
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
            acquisition_source_class=result.source_class,
            acquisition_provider_name=result.provider_name,
            raw_assertions=raw_assertions,
            web_fetched_by_document_id={
                str(row.get("document_id") or ""): row
                for row in result.web_fetched_documents
                if str(row.get("document_id") or "").strip()
            },
            post_extraction_web_rejected_documents=web_rejected_documents,
            claim_extractor_runs=claim_extractor_runs,
            raw_assertion_rejections=raw_assertion_rejections,
            claim_extractor=extractor,
            runtime_budget_exhausted=runtime_budget_exhausted,
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
        raw_assertions=raw_assertions,
        web_search_tasks=tuple(web_search_tasks),
        web_search_results=tuple(web_search_results),
        web_fetched_documents=tuple(web_fetched_documents),
        web_rejected_documents=tuple(web_rejected_documents),
        claim_extractor_runs=tuple(claim_extractor_runs),
        raw_assertion_rejections=tuple(raw_assertion_rejections),
    )


def _runtime_budget_skipped_execution(*, event: CandidateEventV2, task: SourceTask) -> SourceTaskExecutionV4:
    reason = "source_task_skipped_after_runtime_budget_exhausted"
    return SourceTaskExecutionV4(
        task_id=task.task_id,
        source_task=task.to_dict(),
        status=SourceTaskExecutionStatusV4.BUDGET_EXHAUSTED.value,
        **_source_task_execution_identity(
            event=event,
            task=task,
            source_class="runtime_budget",
            provider_name="research_brain_v4_runtime_budget",
        ),
        not_eligible_reasons=(reason,),
        primitive_gap_unsatisfied_ids=(task.primitive_gap,) if task.primitive_gap else (),
        provider_errors=(reason,),
        budget_used={"queries": 0, "candidates": 0, "fetches": 0},
        stop_reason=reason,
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
    acquisition_source_class: str,
    acquisition_provider_name: str,
    raw_assertions: dict[str, RawAssertion],
    web_fetched_by_document_id: Mapping[str, Mapping[str, Any]],
    post_extraction_web_rejected_documents: list[Mapping[str, Any]] | None,
    claim_extractor_runs: list[Mapping[str, Any]],
    raw_assertion_rejections: list[Mapping[str, Any]],
    claim_extractor: LLMContractBlindRawAssertionExtractor,
    runtime_budget_exhausted: Callable[[], bool] | None = None,
) -> SourceTaskExecutionV4:
    accepted: list[str] = []
    direct_accepted: list[str] = []
    rerouted_accepted: list[str] = []
    accepted_primitives: list[str] = []
    rejected: list[str] = []
    assertion_ids: list[str] = []
    adjudicated_ids: list[str] = []
    anchor_ids: list[str] = []
    not_eligible: list[str] = []
    extractor_provider_errors: list[str] = []
    runtime_budget_errors: list[str] = []
    runtime_budget_stopped = False
    for document in documents:
        if runtime_budget_exhausted is not None and runtime_budget_exhausted():
            runtime_budget_stopped = True
            reason = "source_task_document_extraction_stopped_after_runtime_budget_exhausted"
            runtime_budget_errors.append(reason)
            not_eligible.append(reason)
            audit_counts["runtime_budget_stopped_document_extraction_count"] += 1
            break
        document_assertion_ids: list[str] = []
        document_adjudicated_ids: list[str] = []
        document_accepted_ids: list[str] = []
        document_rejected_ids: list[str] = []
        document_not_eligible: list[str] = []
        document_provider_error_start = len(extractor_provider_errors)
        anchor = anchors_by_document.get(document.document_id)
        if anchor is None:
            audit_counts["quote_anchor_missing_rejected_count"] += 1
            document_not_eligible.append("anchor_missing")
            _append_post_extraction_web_rejection_if_needed(
                event=event,
                task=task,
                as_of_date=as_of_date,
                document=document,
                anchor=None,
                web_fetched_by_document_id=web_fetched_by_document_id,
                post_extraction_web_rejected_documents=post_extraction_web_rejected_documents,
                audit_counts=audit_counts,
                document_assertion_ids=document_assertion_ids,
                document_rejected_ids=document_rejected_ids,
                document_not_eligible=document_not_eligible,
                document_provider_errors=(),
            )
            continue
        anchor_ids.append(anchor.anchor_id)
        document_text = document_text_by_id.get(document.document_id, anchor.exact_text)
        target_aliases = _target_aliases(event, source_context=web_fetched_by_document_id.get(document.document_id))
        source_task_score_reasons = _source_task_score_admissibility_reasons(
            task=task,
            document=document,
            acquisition_source_class=acquisition_source_class,
            acquisition_provider_name=acquisition_provider_name,
            provider_errors=provider_errors,
        )
        if source_task_score_reasons:
            audit_counts["source_task_score_admissibility_rejected_count"] += 1
            document_not_eligible.extend(source_task_score_reasons)
        signals = _extract_signals(document=document, anchor=anchor, document_text=document_text)
        if signals:
            pass
        else:
            if runtime_budget_exhausted is not None and runtime_budget_exhausted():
                runtime_budget_stopped = True
                reason = "claim_extraction_skipped_after_runtime_budget_exhausted"
                runtime_budget_errors.append(reason)
                not_eligible.append(reason)
                document_not_eligible.append(reason)
                audit_counts["runtime_budget_stopped_document_extraction_count"] += 1
                _append_post_extraction_web_rejection_if_needed(
                    event=event,
                    task=task,
                    as_of_date=as_of_date,
                    document=document,
                    anchor=anchor,
                    web_fetched_by_document_id=web_fetched_by_document_id,
                    post_extraction_web_rejected_documents=post_extraction_web_rejected_documents,
                    audit_counts=audit_counts,
                    document_assertion_ids=document_assertion_ids,
                    document_rejected_ids=document_rejected_ids,
                    document_not_eligible=document_not_eligible,
                    document_provider_errors=(reason,),
                    document_adjudicated_ids=document_adjudicated_ids,
                    document_accepted_ids=document_accepted_ids,
                )
                break
            records = _extract_unstructured_records(
                event=event,
                document=document,
                anchor=anchor,
                document_text=document_text,
                as_of_date=as_of_date,
                claim_extractor=claim_extractor,
                claim_extractor_runs=claim_extractor_runs,
                audit_counts=audit_counts,
                extractor_provider_errors=extractor_provider_errors,
                target_aliases=target_aliases,
            )
            if records:
                for record in records:
                    anchor_validation = validate_anchor(
                        exact_quote=record.exact_quote,
                        document_text=document_text,
                        locator=anchor.locator,
                        anchor_type=anchor.anchor_type.value,
                    )
                    if not anchor_validation.valid:
                        audit_counts["anchor_validation_rejected_count"] += 1
                        not_eligible.append(f"anchor_validation:{anchor_validation.reason}")
                        document_assertion_ids.append(record.raw_assertion_id)
                        _append_raw_assertion_rejection(
                            rows=raw_assertion_rejections,
                            event=event,
                            task=task,
                            as_of_date=as_of_date,
                            document=document,
                            anchor=anchor,
                            raw_assertion_id=record.raw_assertion_id,
                            adjudicated_claim_id=None,
                            mapping=None,
                            claim=None,
                            rejection_stage="anchor_validation",
                            rejection_reason=f"anchor_validation:{anchor_validation.reason}",
                            not_eligible_reasons=(f"anchor_validation:{anchor_validation.reason}",),
                            mapping_rationale=None,
                        )
                        continue
                    raw = _raw_assertion_from_record(record=record, anchor=anchor)
                    raw_assertions[raw.raw_assertion_id] = raw
                    assertion_ids.append(raw.raw_assertion_id)
                    document_assertion_ids.append(raw.raw_assertion_id)
                    audit_counts["real_document_to_raw_assertion_count"] += 1
                    audit_counts["unstructured_text_to_raw_assertion_count"] += 1
                    claim = _adjudicated_claim_from_record(
                        event=event,
                        document=document,
                        anchor=anchor,
                        raw=raw,
                        record=record,
                        as_of_date=as_of_date,
                        target_aliases=target_aliases,
                    )
                    adjudicated_ids.append(claim.claim_id)
                    document_adjudicated_ids.append(claim.claim_id)
                    audit_counts["raw_assertion_to_adjudicated_claim_count"] += 1
                    ledger.append_claim(claim)
                    mapping_decision = map_claim_to_primitive(
                        record,
                        adjudicate_entity_temporal_scope(
                            record,
                            target_aliases=target_aliases,
                            as_of_date=as_of_date,
                            source_published_at=document.published_date(),
                        ),
                        allowed_primitives=tuple(sorted(_contract_primitive_ids(contract))),
                    )
                    mapped_primitive = mapping_decision.primitive_id or task.primitive_gap
                    mapping = PrimitiveMappingProposal.build(
                        claim_id=claim.claim_id,
                        archetype_id=contract.archetype_id,
                        primitive_id=mapped_primitive,
                        support_direction=_support_direction_from_text(mapping_decision.support_direction),
                        mapping_status=_mapping_status_from_text(mapping_decision.mapping_status),
                        rationale=f"contract_blind_extractor:{mapping_decision.rationale}",
                        contract_rule_id=mapped_primitive,
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
                    score_reasons = tuple(dict.fromkeys((*eligibility.reasons, *source_task_score_reasons)))
                    if not score_reasons and eligibility.eligible and mapping.mapping_status == MappingStatus.ACCEPTED:
                        ledger.append_mapping(mapping)
                        accepted.append(claim.claim_id)
                        document_accepted_ids.append(claim.claim_id)
                        accepted_primitives.append(mapped_primitive)
                        if mapped_primitive == task.primitive_gap:
                            direct_accepted.append(claim.claim_id)
                        else:
                            rerouted_accepted.append(claim.claim_id)
                        audit_counts["adjudicated_claim_to_accepted_claim_count"] += 1
                    else:
                        rejected.append(claim.claim_id)
                        document_rejected_ids.append(claim.claim_id)
                        if claim.target_scope_status != TargetScopeStatus.DIRECT:
                            audit_counts["wrong_subject_rejected_count"] += 1
                        rejection_reasons = _eligibility_reasons_with_mapping_rationale(
                            score_reasons,
                            mapping_decision.rationale,
                        )
                        not_eligible.extend(rejection_reasons)
                        document_not_eligible.extend(rejection_reasons)
                        _append_raw_assertion_rejection(
                            rows=raw_assertion_rejections,
                            event=event,
                            task=task,
                            as_of_date=as_of_date,
                            document=document,
                            anchor=anchor,
                            raw_assertion_id=raw.raw_assertion_id,
                            adjudicated_claim_id=claim.claim_id,
                            mapping=mapping,
                            claim=claim,
                            rejection_stage="score_eligibility",
                            rejection_reason=_raw_assertion_rejection_reason(rejection_reasons),
                            not_eligible_reasons=rejection_reasons,
                            mapping_rationale=mapping_decision.rationale,
                        )
                        ledger.append_mapping(
                            PrimitiveMappingProposal.build(
                                claim_id=claim.claim_id,
                                archetype_id=contract.archetype_id,
                                primitive_id=task.primitive_gap,
                                support_direction=SupportDirection.NEUTRAL,
                                mapping_status=MappingStatus.REJECTED,
                                rationale=";".join(rejection_reasons),
                                contract_rule_id=task.primitive_gap,
                            )
                        )
                _append_post_extraction_web_rejection_if_needed(
                    event=event,
                    task=task,
                    as_of_date=as_of_date,
                    document=document,
                    anchor=anchor,
                    web_fetched_by_document_id=web_fetched_by_document_id,
                    post_extraction_web_rejected_documents=post_extraction_web_rejected_documents,
                    audit_counts=audit_counts,
                    document_assertion_ids=document_assertion_ids,
                    document_rejected_ids=document_rejected_ids,
                    document_not_eligible=document_not_eligible,
                    document_provider_errors=tuple(extractor_provider_errors[document_provider_error_start:]),
                    document_adjudicated_ids=document_adjudicated_ids,
                    document_accepted_ids=document_accepted_ids,
                )
                continue
            audit_counts["mention_only_count"] += 1
        for signal in signals:
            raw = _raw_assertion_from_signal(signal=signal, anchor=anchor, event=event)
            raw_assertions[raw.raw_assertion_id] = raw
            assertion_ids.append(raw.raw_assertion_id)
            document_assertion_ids.append(raw.raw_assertion_id)
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
            document_adjudicated_ids.append(claim.claim_id)
            audit_counts["raw_assertion_to_adjudicated_claim_count"] += 1
            ledger.append_claim(claim)
            support_direction = _support_direction_for_signal(signal)
            mapped_primitive = _mapped_primitive_for_signal(
                signal=signal,
                task_primitive_gap=task.primitive_gap,
                contract=contract,
            )
            mapping_status = MappingStatus.ACCEPTED if support_direction != SupportDirection.NEUTRAL and mapped_primitive else MappingStatus.REJECTED
            mapping = PrimitiveMappingProposal.build(
                claim_id=claim.claim_id,
                archetype_id=contract.archetype_id,
                primitive_id=mapped_primitive or task.primitive_gap,
                support_direction=support_direction,
                mapping_status=mapping_status,
                rationale=f"v4_signal:{signal.signal_id}",
                contract_rule_id=mapped_primitive or task.primitive_gap,
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
            score_reasons = tuple(dict.fromkeys((*eligibility.reasons, *source_task_score_reasons)))
            if not score_reasons and eligibility.eligible and mapping.mapping_status == MappingStatus.ACCEPTED:
                ledger.append_mapping(mapping)
                accepted.append(claim.claim_id)
                document_accepted_ids.append(claim.claim_id)
                accepted_primitives.append(mapping.primitive_id)
                if mapping.primitive_id == task.primitive_gap:
                    direct_accepted.append(claim.claim_id)
                else:
                    rerouted_accepted.append(claim.claim_id)
                audit_counts["adjudicated_claim_to_accepted_claim_count"] += 1
            else:
                rejected.append(claim.claim_id)
                document_rejected_ids.append(claim.claim_id)
                if claim.target_scope_status != TargetScopeStatus.DIRECT:
                    audit_counts["wrong_subject_rejected_count"] += 1
                rejection_reasons = _eligibility_reasons_with_mapping_rationale(
                    score_reasons,
                    mapping.rationale,
                )
                not_eligible.extend(rejection_reasons)
                document_not_eligible.extend(rejection_reasons)
                _append_raw_assertion_rejection(
                    rows=raw_assertion_rejections,
                    event=event,
                    task=task,
                    as_of_date=as_of_date,
                    document=document,
                    anchor=anchor,
                    raw_assertion_id=raw.raw_assertion_id,
                    adjudicated_claim_id=claim.claim_id,
                    mapping=mapping,
                    claim=claim,
                    rejection_stage="score_eligibility",
                    rejection_reason=_raw_assertion_rejection_reason(rejection_reasons),
                    not_eligible_reasons=rejection_reasons,
                    mapping_rationale=mapping.rationale,
                )
                ledger.append_mapping(
                    PrimitiveMappingProposal.build(
                        claim_id=claim.claim_id,
                        archetype_id=contract.archetype_id,
                        primitive_id=task.primitive_gap,
                        support_direction=SupportDirection.SUPPORT,
                        mapping_status=MappingStatus.REJECTED,
                        rationale=";".join(rejection_reasons),
                        contract_rule_id=task.primitive_gap,
                    )
                )
        _append_post_extraction_web_rejection_if_needed(
            event=event,
            task=task,
            as_of_date=as_of_date,
            document=document,
            anchor=anchor,
            web_fetched_by_document_id=web_fetched_by_document_id,
            post_extraction_web_rejected_documents=post_extraction_web_rejected_documents,
            audit_counts=audit_counts,
            document_assertion_ids=document_assertion_ids,
            document_rejected_ids=document_rejected_ids,
            document_not_eligible=document_not_eligible,
            document_provider_errors=tuple(extractor_provider_errors[document_provider_error_start:]),
            document_adjudicated_ids=document_adjudicated_ids,
            document_accepted_ids=document_accepted_ids,
        )
    accepted_unique = tuple(dict.fromkeys(accepted))
    direct_unique = tuple(dict.fromkeys(direct_accepted))
    rerouted_unique = tuple(dict.fromkeys(rerouted_accepted))
    accepted_primitive_unique = tuple(dict.fromkeys(accepted_primitives))
    satisfies_source_task = bool(direct_unique)
    satisfaction_type = (
        "DIRECT_ACCEPTED_CLAIM"
        if direct_unique
        else "REROUTED_ACCEPTED_CLAIM"
        if rerouted_unique
        else "PROVIDER_FAILED"
        if extractor_provider_errors
        else "BUDGET_EXHAUSTED"
        if runtime_budget_stopped
        else "NO_EVIDENCE_FOUND"
    )
    status = (
        SourceTaskExecutionStatusV4.EVIDENCE_OS_ACCEPTED.value
        if accepted_unique
        else SourceTaskExecutionStatusV4.BUDGET_EXHAUSTED.value
        if runtime_budget_stopped
        else SourceTaskExecutionStatusV4.PROVIDER_FAILED.value
        if extractor_provider_errors
        else SourceTaskExecutionStatusV4.NO_EVIDENCE_FOUND.value
    )
    return SourceTaskExecutionV4(
        task_id=task.task_id,
        source_task=task.to_dict(),
        status=status,
        **_source_task_execution_identity(
            event=event,
            task=task,
            source_class=acquisition_source_class,
            provider_name=acquisition_provider_name,
        ),
        fetched_document_ids=tuple(document.document_id for document in documents),
        document_urls=tuple(document.canonical_url or "" for document in documents),
        document_hashes=tuple(document.content_hash for document in documents),
        evidence_anchor_ids=tuple(anchor_ids),
        raw_assertion_ids=tuple(assertion_ids),
        adjudicated_claim_ids=tuple(adjudicated_ids),
        accepted_claim_ids=accepted_unique,
        rejected_claim_ids=tuple(dict.fromkeys(rejected)),
        not_eligible_reasons=tuple(dict.fromkeys(not_eligible)),
        satisfies_source_task=satisfies_source_task,
        satisfaction_type=satisfaction_type,
        direct_accepted_claim_ids=direct_unique,
        rerouted_accepted_claim_ids=rerouted_unique,
        # Score support is assigned only after the score contribution ledger is
        # built. Accepted claims can be useful evidence without contributing
        # points, so exporting all accepted claims here would make source-task
        # satisfaction audits overclaim the score chain.
        score_claim_ids=(),
        accepted_primitive_ids=accepted_primitive_unique,
        primitive_gap_satisfied_ids=(task.primitive_gap,) if satisfies_source_task else (),
        primitive_gap_unsatisfied_ids=() if satisfies_source_task else ((task.primitive_gap,) if task.primitive_gap else ()),
        provider_errors=tuple(dict.fromkeys((*provider_errors, *extractor_provider_errors, *runtime_budget_errors))),
        budget_used=dict(budget_used),
        stop_reason=(
            stop_reason
            if direct_unique
            else "rerouted_claim_accepted_original_gap_unsatisfied"
            if rerouted_unique
            else "source_task_extraction_stopped_after_runtime_budget_exhausted"
            if runtime_budget_stopped
            else "claim_extractor_provider_failed"
            if extractor_provider_errors
            else "no_score_eligible_real_claim"
        ),
    )


def _source_task_execution_identity(
    *,
    event: CandidateEventV2,
    task: SourceTask,
    source_class: str,
    provider_name: str,
) -> dict[str, Any]:
    preferred = tuple(str(item) for item in task.preferred_source_classes)
    fallback = tuple(str(item) for item in task.fallback_source_classes)
    forbidden = tuple(str(item) for item in task.forbidden_source_classes)
    requested = tuple(dict.fromkeys((*preferred, *fallback)))
    return {
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "archetype_id": task.archetype_id,
        "primitive_gap": task.primitive_gap,
        "source_class": str(source_class or (requested[0] if requested else "")),
        "provider_name": str(provider_name or ""),
        "source_task_origin": "research_brain_v4_attempt",
        "preferred_source_classes": preferred,
        "fallback_source_classes": fallback,
        "forbidden_source_classes": forbidden,
        "requested_source_classes": requested,
    }


def _source_task_score_admissibility_reasons(
    *,
    task: SourceTask,
    document: EvidenceDocument,
    acquisition_source_class: str,
    acquisition_provider_name: str,
    provider_errors: Sequence[str],
) -> tuple[str, ...]:
    reasons: list[str] = []
    document_type = _document_source_type(document)
    source_class = _document_score_source_class(
        task=task,
        document_type=document_type,
        acquisition_source_class=acquisition_source_class,
    )
    if _document_has_verified_issuer_original_lineage(document) and document_type in {SourceType.NEWS, SourceType.IR}:
        requested = _requested_source_classes(task)
        if "CompanyNewsroom" in requested:
            source_class = "CompanyNewsroom"
        elif "IssuerOfficial" in requested:
            source_class = "IssuerOfficial"
    full_official_source_allowed = document_type == SourceType.FILING and source_class in {
        "DART",
        "KIND",
        "KRX",
        "IssuerOfficial",
    }
    verified_issuer_original_allowed = (
        _document_has_verified_issuer_original_lineage(document)
        and source_class in {"CompanyNewsroom", "IssuerOfficial", "IR"}
        and document_type in {SourceType.NEWS, SourceType.IR}
    )
    verified_report_original_allowed = (
        _document_has_verified_report_original_lineage(document)
        and source_class in {"BrokerReportPublicPDF", "ReportPDF"}
        and document_type == SourceType.RESEARCH_REPORT
    )
    stored_report_snapshot_allowed = (
        _provider_is_stored_real_source_snapshot(acquisition_provider_name)
        and source_class in {"BrokerReportPublicPDF", "ReportPDF"}
        and document_type == SourceType.RESEARCH_REPORT
        and is_verified_report_original_url(str(document.canonical_url or ""))
    )
    for error in provider_errors:
        lowered = str(error).lower()
        if (
            "general search is not a score source" in lowered
            and not full_official_source_allowed
            and not verified_issuer_original_allowed
            and not verified_report_original_allowed
        ):
            reasons.append("source_task_provider_error_score_block:general_search_not_score_source")
        if "trusted_news_provider_not_configured" in lowered and source_class == "TrustedNews":
            reasons.append("source_task_provider_error_score_block:trusted_news_provider_not_configured")
    allowed = _allowed_document_source_types_for_source_class(source_class)
    if allowed and document_type not in allowed:
        reasons.append(f"source_class_document_type_mismatch:{source_class}:{document_type.value}")
    if (
        _provider_is_general_web_search(acquisition_provider_name)
        and source_class in {"BrokerReportPublicPDF", "ReportPDF"}
        and not verified_report_original_allowed
    ):
        reasons.append(f"source_provider_document_type_mismatch:{source_class}:general_web_search_provider")
    if (
        _provider_is_stored_real_source_snapshot(acquisition_provider_name)
        and source_class in {"BrokerReportPublicPDF", "ReportPDF"}
        and document_type == SourceType.RESEARCH_REPORT
        and not stored_report_snapshot_allowed
    ):
        reasons.append(f"source_lineage_unverified_original:{source_class}:stored_report_snapshot_provider")
    if (
        _provider_is_general_web_search(acquisition_provider_name)
        and document_type == SourceType.NEWS
        and source_class in {
        "CompanyNewsroom",
        "IndustryMedia",
        "NaverSearch",
        "News",
        "TrustedNews",
        }
        and not verified_issuer_original_allowed
    ):
        reasons.append(f"source_provider_document_type_mismatch:{source_class}:general_web_search_provider")
    source_lineage_reason = _source_lineage_score_admissibility_reason(
        document_type=document_type,
        source_class=source_class,
        acquisition_provider_name=acquisition_provider_name,
        full_official_source_allowed=full_official_source_allowed,
        verified_issuer_original_allowed=verified_issuer_original_allowed,
        verified_report_original_allowed=verified_report_original_allowed,
    )
    if source_lineage_reason:
        reasons.append(source_lineage_reason)
    return tuple(dict.fromkeys(reasons))


def _source_lineage_score_admissibility_reason(
    *,
    document_type: SourceType,
    source_class: str,
    acquisition_provider_name: str,
    full_official_source_allowed: bool,
    verified_issuer_original_allowed: bool = False,
    verified_report_original_allowed: bool = False,
) -> str | None:
    if not _provider_is_general_web_search(acquisition_provider_name):
        return None
    if full_official_source_allowed:
        return None
    if verified_issuer_original_allowed:
        return None
    if verified_report_original_allowed:
        return None
    if document_type not in {SourceType.NEWS, SourceType.RESEARCH_REPORT, SourceType.IR}:
        return None
    if source_class not in {
        "BrokerReportPublicPDF",
        "CompanyNewsroom",
        "IndustryMedia",
        "IR",
        "NaverSearch",
        "News",
        "ReportPDF",
        "TrustedNews",
    }:
        return None
    return f"source_lineage_unverified_original:{source_class}:general_web_search_provider"


def _provider_is_stored_real_source_snapshot(provider_name: str) -> bool:
    return str(provider_name or "").strip() == "stored_real_source_snapshot_provider"


def _document_score_source_class(
    *,
    task: SourceTask,
    document_type: SourceType,
    acquisition_source_class: str,
) -> str:
    source_class = str(acquisition_source_class or "").strip()
    allowed = _allowed_document_source_types_for_source_class(source_class)
    if allowed and document_type in allowed:
        return source_class
    if source_class not in {"DART", "KIND", "KRX", "IssuerOfficial", "IR", "Official"}:
        return source_class
    requested = tuple(dict.fromkeys(str(item).strip() for item in (*task.preferred_source_classes, *task.fallback_source_classes)))
    for candidate in requested:
        candidate_allowed = _allowed_document_source_types_for_source_class(candidate)
        if candidate_allowed and document_type in candidate_allowed:
            return candidate
    return source_class


def _requested_source_classes(task: SourceTask) -> tuple[str, ...]:
    return tuple(dict.fromkeys(str(item).strip() for item in (*task.preferred_source_classes, *task.fallback_source_classes)))


def _document_has_verified_issuer_original_lineage(document: EvidenceDocument) -> bool:
    lineage = str(document.source_lineage_id or "")
    marker = "verified_issuer_original:issuer_official_domain:"
    if marker not in lineage:
        return False
    suffix = lineage.split(marker, 1)[1]
    parts = suffix.split(":")
    if len(parts) < 2:
        return False
    homepage_host = _normalized_host(parts[0])
    result_host = _normalized_host(parts[1])
    canonical_host = _normalized_host(str(document.canonical_url or ""))
    if not homepage_host or not result_host or not canonical_host:
        return False
    if canonical_host != result_host:
        return False
    return result_host == homepage_host or result_host.endswith(f".{homepage_host}")


def _document_has_verified_report_original_lineage(document: EvidenceDocument) -> bool:
    lineage = str(document.source_lineage_id or "")
    marker = "verified_report_original:broker_report_domain:"
    if marker not in lineage:
        return False
    suffix = lineage.split(marker, 1)[1]
    result_host = _normalized_host(suffix.split(":", 1)[0])
    canonical_url = str(document.canonical_url or "")
    canonical_host = _normalized_host(canonical_url)
    if not result_host or not canonical_host:
        return False
    if canonical_host != result_host:
        return False
    return is_verified_report_original_url(canonical_url)


def _normalized_host(url_or_host: str) -> str:
    value = str(url_or_host or "").strip()
    if not value:
        return ""
    try:
        host = (urlsplit(value if "://" in value else f"https://{value}").hostname or "").lower()
    except ValueError:
        return ""
    if host.startswith("www."):
        host = host[4:]
    return host.strip(".")


def _allowed_document_source_types_for_source_class(source_class: str) -> frozenset[SourceType]:
    mapping = {
        "DART": frozenset({SourceType.FILING}),
        "KIND": frozenset({SourceType.FILING}),
        "KRX": frozenset({SourceType.FILING}),
        "CompanyGuide": frozenset({SourceType.API}),
        "TrustedNews": frozenset({SourceType.NEWS}),
        "IndustryMedia": frozenset({SourceType.NEWS}),
        "ReportPDF": frozenset({SourceType.RESEARCH_REPORT}),
        "BrokerReportPublicPDF": frozenset({SourceType.RESEARCH_REPORT}),
        "IR": frozenset({SourceType.IR}),
        "IssuerOfficial": frozenset({SourceType.IR, SourceType.FILING}),
        "CompanyNewsroom": frozenset({SourceType.IR, SourceType.NEWS}),
    }
    return mapping.get(str(source_class).strip(), frozenset())


def _document_source_type(document: EvidenceDocument) -> SourceType:
    value = document.source_type
    if isinstance(value, SourceType):
        return value
    try:
        return SourceType(str(value))
    except ValueError:
        return SourceType.OTHER


def _provider_is_general_web_search(provider_name: str) -> bool:
    lowered = str(provider_name or "").lower()
    return "openapi.naver.com" in lowered or "naver" in lowered or "generalweb" in lowered or "web_search" in lowered


def _append_post_extraction_web_rejection_if_needed(
    *,
    event: CandidateEventV2,
    task: SourceTask,
    as_of_date: date,
    document: EvidenceDocument,
    anchor: EvidenceAnchor | None,
    web_fetched_by_document_id: Mapping[str, Mapping[str, Any]],
    post_extraction_web_rejected_documents: list[Mapping[str, Any]] | None,
    audit_counts: dict[str, int],
    document_assertion_ids: Sequence[str],
    document_rejected_ids: Sequence[str],
    document_not_eligible: Sequence[str],
    document_provider_errors: Sequence[str],
    document_adjudicated_ids: Sequence[str] = (),
    document_accepted_ids: Sequence[str] = (),
) -> None:
    if post_extraction_web_rejected_documents is None:
        return
    web_fetch_row = web_fetched_by_document_id.get(document.document_id)
    if not web_fetch_row:
        return
    if document_accepted_ids:
        return
    reason = _post_extraction_web_rejection_reason(
        document_assertion_ids=document_assertion_ids,
        document_rejected_ids=document_rejected_ids,
        document_provider_errors=document_provider_errors,
        document_not_eligible=document_not_eligible,
    )
    rejected_ids = tuple(dict.fromkeys(str(item) for item in document_rejected_ids if str(item).strip()))
    assertion_ids = tuple(dict.fromkeys(str(item) for item in document_assertion_ids if str(item).strip()))
    not_eligible = tuple(dict.fromkeys(str(item) for item in document_not_eligible if str(item).strip()))
    row = {
        "schema_version": "e2r_research_brain_v4_web_rejected_document_v1",
        "web_rejected_id": deterministic_id(
            "WEBREJECT",
            (
                "post_extraction_evidence_os",
                task.task_id,
                document.document_id,
                reason,
                rejected_ids,
                assertion_ids,
                not_eligible,
            ),
        ),
        "web_result_id": web_fetch_row.get("web_result_id"),
        "web_fetch_id": web_fetch_row.get("web_fetch_id"),
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": task.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "query": web_fetch_row.get("query"),
        "provider_name": web_fetch_row.get("provider_name") or document.source_name,
        "as_of_date": as_of_date.isoformat(),
        "status": "REJECTED",
        "url": document.canonical_url,
        "title": web_fetch_row.get("title"),
        "published_at": document.published_date().isoformat() if document.published_date() else web_fetch_row.get("published_at"),
        "rejection_phase": "post_extraction_evidence_os",
        "rejection_reason": reason,
        "document_id": document.document_id,
        "anchor_id": anchor.anchor_id if anchor else None,
        "document_hash": document.content_hash,
        "raw_assertion_ids": list(assertion_ids),
        "adjudicated_claim_ids": list(dict.fromkeys(str(item) for item in document_adjudicated_ids if str(item).strip())),
        "rejected_claim_ids": list(rejected_ids),
        "accepted_claim_ids": [],
        "not_eligible_reasons": list(not_eligible),
        "provider_errors": list(dict.fromkeys(str(item) for item in document_provider_errors if str(item).strip())),
        "primitive_gap": task.primitive_gap,
        "source_task_primitive_gap": task.primitive_gap,
        "task_type": task.task_type,
        "snippet_score_forbidden": True,
        "source_origin": "research_brain_v4_attempt",
        "brain_web_origin": "research_brain_v4_attempt",
    }
    if any(existing.get("web_rejected_id") == row["web_rejected_id"] for existing in post_extraction_web_rejected_documents):
        return
    post_extraction_web_rejected_documents.append(row)
    audit_counts["post_extraction_web_rejected_document_count"] += 1


def _post_extraction_web_rejection_reason(
    *,
    document_assertion_ids: Sequence[str],
    document_rejected_ids: Sequence[str],
    document_provider_errors: Sequence[str],
    document_not_eligible: Sequence[str],
) -> str:
    if document_provider_errors:
        return "post_extraction_claim_extractor_provider_failed"
    if document_rejected_ids:
        return "post_extraction_no_score_eligible_claim"
    if document_assertion_ids:
        return "post_extraction_no_accepted_mapping"
    if any(str(reason).startswith("anchor") for reason in document_not_eligible):
        return "post_extraction_anchor_missing_or_invalid"
    return "post_extraction_no_extractable_claim"


def _append_raw_assertion_rejection(
    *,
    rows: list[Mapping[str, Any]],
    event: CandidateEventV2,
    task: SourceTask,
    as_of_date: date,
    document: EvidenceDocument,
    anchor: EvidenceAnchor | None,
    raw_assertion_id: str,
    adjudicated_claim_id: str | None,
    mapping: PrimitiveMappingProposal | None,
    claim: AdjudicatedClaim | None,
    rejection_stage: str,
    rejection_reason: str,
    not_eligible_reasons: Sequence[str],
    mapping_rationale: str | None,
) -> None:
    clean_reasons = tuple(dict.fromkeys(str(reason) for reason in not_eligible_reasons if str(reason).strip()))
    row = {
        "schema_version": "e2r_research_brain_v4_raw_assertion_rejection_v1",
        "raw_assertion_rejection_id": deterministic_id(
            "RAWREJECT",
            (
                task.task_id,
                document.document_id,
                anchor.anchor_id if anchor else None,
                raw_assertion_id,
                adjudicated_claim_id,
                rejection_stage,
                rejection_reason,
                clean_reasons,
            ),
        ),
        "raw_assertion_id": raw_assertion_id,
        "adjudicated_claim_id": adjudicated_claim_id,
        "claim_id": adjudicated_claim_id,
        "mapping_id": getattr(mapping, "mapping_id", None),
        "task_id": task.task_id,
        "source_task_id": task.task_id,
        "candidate_event_id": task.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "archetype_id": task.archetype_id,
        "primitive_gap": task.primitive_gap,
        "source_task_primitive_gap": task.primitive_gap,
        "document_id": document.document_id,
        "anchor_id": anchor.anchor_id if anchor else None,
        "source_url": document.canonical_url,
        "source_provider": document.source_name,
        "document_hash": document.content_hash,
        "as_of_date": as_of_date.isoformat(),
        "published_at": document.published_date().isoformat() if document.published_date() else None,
        "rejection_stage": rejection_stage,
        "rejection_reason": rejection_reason,
        "not_eligible_reasons": list(clean_reasons),
        "target_scope_status": _enum_value(getattr(claim, "target_scope_status", None)),
        "temporal_status": _enum_value(getattr(claim, "temporal_status", None)),
        "polarity": _enum_value(getattr(claim, "polarity", None)),
        "verification_status": _enum_value(getattr(claim, "verification_status", None)),
        "semantic_status": _enum_value(getattr(claim, "semantic_status", None)),
        "directness": _enum_value(getattr(claim, "directness", None)),
        "relation_to_target": _enum_value(getattr(claim, "relation_to_target", None)),
        "mapping_status": _enum_value(getattr(mapping, "mapping_status", None)),
        "mapped_primitive_id": getattr(mapping, "primitive_id", None),
        "support_direction": _enum_value(getattr(mapping, "support_direction", None)),
        "mapping_rationale": mapping_rationale,
        "accepted_claim_id_if_any": None,
        "score_eligible": False,
        "source_origin": "research_brain_v4_attempt",
        "brain_web_origin": "research_brain_v4_attempt",
    }
    if any(existing.get("raw_assertion_rejection_id") == row["raw_assertion_rejection_id"] for existing in rows):
        return
    rows.append(row)


def _raw_assertion_rejection_reason(reasons: Sequence[str]) -> str:
    reason_texts = [str(reason) for reason in reasons if str(reason).strip()]
    if any(reason.startswith("anchor") for reason in reason_texts):
        return "anchor_validation_failed"
    if any(reason.startswith("target_scope_not_allowed") or reason.startswith("target_not_direct") for reason in reason_texts):
        return "target_scope_or_directness_rejected"
    if any(reason.startswith("temporal_not_allowed") for reason in reason_texts):
        return "temporal_status_rejected"
    if any(reason.startswith("future_") for reason in reason_texts):
        return "future_leakage_rejected"
    if any(reason.startswith("mapping_not_accepted") or reason.startswith("primitive_mapping_rejected") for reason in reason_texts):
        return "primitive_mapping_rejected"
    if any(reason.startswith("semantic_") for reason in reason_texts):
        return "semantic_verification_rejected"
    if any(reason.startswith("source_proxy") or reason.startswith("document_score_block") for reason in reason_texts):
        return "source_not_score_eligible"
    return "score_eligibility_rejected"


def _enum_value(value: Any) -> Any:
    return getattr(value, "value", value)


def _eligibility_reasons_with_mapping_rationale(
    eligibility_reasons: Sequence[str],
    mapping_rationale: str,
) -> tuple[str, ...]:
    reasons = [str(reason) for reason in eligibility_reasons if str(reason).strip()]
    clean_rationale = str(mapping_rationale or "").strip()
    if clean_rationale and any(reason.startswith("mapping_not_accepted:") for reason in reasons):
        reasons.append(f"primitive_mapping_rejected:{clean_rationale}")
    if not reasons:
        reasons.append(clean_rationale or "mapping_rejected")
    return tuple(dict.fromkeys(reasons))


def _extract_unstructured_records(
    *,
    event: CandidateEventV2,
    document: EvidenceDocument,
    anchor: EvidenceAnchor,
    document_text: str,
    as_of_date: date,
    claim_extractor: LLMContractBlindRawAssertionExtractor,
    claim_extractor_runs: list[Mapping[str, Any]],
    audit_counts: dict[str, int],
    extractor_provider_errors: list[str],
    target_aliases: Sequence[str],
) -> tuple[RawAssertionRecord, ...]:
    if not _should_run_unstructured_extractor(anchor=anchor, document_text=document_text):
        return ()
    request = ExtractionInput(
        target_entity_id=f"TICKER:{event.symbol}",
        target_aliases=tuple(target_aliases),
        as_of_date=as_of_date.isoformat(),
        document_id=document.document_id,
        anchor_id=anchor.anchor_id,
        source_text=document_text,
        source_metadata={
            "canonical_url": document.canonical_url,
            "source_type": document.source_type.value,
            "source_name": document.source_name,
            "published_at": document.published_date().isoformat() if document.published_date() else None,
            "anchor_type": anchor.anchor_type.value,
        },
        extra_context={},
    )
    result = claim_extractor.extract_with_metadata(request)
    claim_extractor_runs.append(
        _claim_extractor_run_row(
            event=event,
            document=document,
            anchor=anchor,
            request=request,
            result=result,
            as_of_date=as_of_date,
        )
    )
    audit_counts["llm_claim_extractor_attempt_count"] += 1
    if result.provider_error:
        audit_counts["llm_claim_extractor_provider_error_count"] += 1
        extractor_provider_errors.append(f"claim_extractor_provider_error:{result.provider_error}")
    elif result.raw_assertions:
        audit_counts["llm_claim_extractor_success_count"] += 1
    if result.provider_mode != "llm":
        audit_counts["llm_claim_extractor_non_llm_provider_count"] += 1
    return tuple(result.raw_assertions)


def _should_run_unstructured_extractor(*, anchor: EvidenceAnchor, document_text: str) -> bool:
    if anchor.anchor_type != AnchorType.TEXT_SPAN:
        return False
    return bool(_visible_text(document_text or anchor.exact_text))


def _claim_extractor_run_row(
    *,
    event: CandidateEventV2,
    document: EvidenceDocument,
    anchor: EvidenceAnchor,
    request: ExtractionInput,
    result: ExtractorProviderResult,
    as_of_date: date,
) -> dict[str, Any]:
    input_context_keys = sorted(request.extra_context.keys())
    forbidden_context_seen = [
        key
        for key in input_context_keys
        if key.lower()
        in {
            "score",
            "stage",
            "verified_score",
            "current_score_eligible",
            "hard_break",
            "primitive_gap",
            "missing_primitive",
            "score_gap_context",
        }
    ]
    run_id = deterministic_id(
        "EXT-RUN",
        (
            event.candidate_event_id,
            document.document_id,
            anchor.anchor_id,
            result.provider_name,
            result.prompt_hash or "",
            result.response_hash or "",
        ),
    )
    raw_prompt_path = f"claim_extractor_raw/prompts/{run_id}.json" if result.prompt_hash and result.raw_prompt_payload is not None else None
    raw_response_path = f"claim_extractor_raw/responses/{run_id}.json" if result.response_hash and result.raw_response_payload is not None else None
    return {
        "schema_version": "e2r_research_brain_v4_claim_extractor_run_v1",
        "claim_extractor_run_id": run_id,
        "extractor_run_id": run_id,
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "document_id": document.document_id,
        "anchor_id": anchor.anchor_id,
        "as_of_date": as_of_date.isoformat(),
        "provider_name": result.provider_name,
        "provider_mode": result.provider_mode,
        "model": result.model,
        "prompt_hash": result.prompt_hash,
        "initial_prompt_hash": result.initial_prompt_hash,
        "retry_prompt_hash": result.retry_prompt_hash,
        "response_hash": result.response_hash,
        "raw_prompt_path": raw_prompt_path,
        "raw_response_path": raw_response_path,
        "_raw_prompt_payload": {
            "schema_version": "e2r_research_brain_v4_claim_extractor_prompt_artifact_v1",
            "claim_extractor_run_id": run_id,
            "candidate_event_id": event.candidate_event_id,
            "symbol": event.symbol,
            "provider_name": result.provider_name,
            "model": result.model,
            "prompt_hash": result.prompt_hash,
            "prompt_payload": result.raw_prompt_payload,
        }
        if raw_prompt_path
        else None,
        "_raw_response_payload": {
            "schema_version": "e2r_research_brain_v4_claim_extractor_response_artifact_v1",
            "claim_extractor_run_id": run_id,
            "candidate_event_id": event.candidate_event_id,
            "symbol": event.symbol,
            "provider_name": result.provider_name,
            "model": result.model,
            "response_hash": result.response_hash,
            "response_payload": result.raw_response_payload,
        }
        if raw_response_path
        else None,
        "latency_ms": result.latency_ms,
        "timeout_seconds": result.timeout_seconds,
        "attempt_count": result.attempt_count,
        "timeout_retry_attempted": result.timeout_retry_attempted,
        "prompt_text_chars": result.prompt_text_chars,
        "prompt_text_compacted": result.prompt_text_compacted,
        "prompt_text_limit": result.prompt_text_limit,
        "status": "PROVIDER_FAILED" if result.provider_error else "SUCCESS",
        "provider_error": result.provider_error,
        "input_context_keys": input_context_keys,
        "forbidden_context_seen": forbidden_context_seen,
        "raw_assertion_ids": [record.raw_assertion_id for record in result.raw_assertions],
        "raw_assertion_count": len(result.raw_assertions),
        "source_origin": "research_brain_v4_attempt",
        "brain_web_origin": "research_brain_v4_attempt",
    }


def _raw_assertion_from_record(*, record: RawAssertionRecord, anchor: EvidenceAnchor) -> RawAssertion:
    return RawAssertion(
        raw_assertion_id=record.raw_assertion_id,
        anchor_id=anchor.anchor_id,
        subject_text=record.subject,
        predicate=record.predicate,
        object_text=record.object_text,
        value=record.object_text,
        polarity_proposal=_polarity_from_text(record.polarity_proposal),
        modality=record.modality,
        certainty="contract_blind_extracted",
        event_date_text=record.event_date,
        exact_quote=record.exact_quote,
        related_entity_texts=tuple(dict.fromkeys((record.subject, *record.related_entities))),
        extractor_model="research_brain_v4_contract_blind_extractor",
        extractor_prompt_hash="contract_blind_unstructured_v1",
    )


def _adjudicated_claim_from_record(
    *,
    event: CandidateEventV2,
    document: EvidenceDocument,
    anchor: EvidenceAnchor,
    raw: RawAssertion,
    record: RawAssertionRecord,
    as_of_date: date,
    target_aliases: Sequence[str],
) -> AdjudicatedClaim:
    adjudication = adjudicate_entity_temporal_scope(
        record,
        target_aliases=tuple(target_aliases),
        as_of_date=as_of_date,
        source_published_at=document.published_date(),
    )
    direct = adjudication.target_scope_status == "DIRECT" and adjudication.directness == "DIRECT"
    event_date = _parse_iso_date(record.event_date) or document.published_date()
    effective_start, effective_end = _effective_period_from_text(record.exact_quote or record.object_text)
    return AdjudicatedClaim.from_raw(
        raw=raw,
        document=document,
        anchor=anchor,
        subject_entity_id=f"TICKER:{event.symbol}" if direct else f"UNRESOLVED:{record.subject}",
        target_entity_id=f"TICKER:{event.symbol}",
        relation_to_target=RelationToTarget.SELF if direct else RelationToTarget.UNRELATED,
        directness=Directness.DIRECT if direct else Directness.NOT_TARGET_SCOPED,
        verification_status=VerificationStatus.SEMANTIC_VERIFIED if anchor.anchor_verified else VerificationStatus.UNVERIFIED,
        target_scope_status=TargetScopeStatus.DIRECT if direct else TargetScopeStatus.UNRELATED,
        polarity=_polarity_from_text(adjudication.polarity),
        temporal_status=_temporal_status_from_text(adjudication.temporal_status),
        semantic_status=SemanticStatus.PASS_ if adjudication.semantic_status == "PASS" else SemanticStatus.REJECTED,
        investigation_status=InvestigationStatus.COMPLETE if direct else InvestigationStatus.FOLLOWUP_REQUIRED,
        event_date=event_date,
        effective_start=effective_start,
        effective_end=effective_end,
        adjudication_rationale="contract-blind unstructured extraction followed by deterministic target/temporal adjudication",
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
    if not row:
        return ()
    signals: list[ExtractionSignal] = []
    source_date = document.published_date()

    def add(
        signal_id: str,
        predicate: str,
        primitives: Sequence[str],
        *,
        polarity: Polarity,
        polarity_source: str,
    ) -> None:
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
                extraction_method="structured_api_record",
                polarity_source=polarity_source,
                event_date=source_date,
            )
        )

    if _has_current_consensus_visibility(row):
        add(
            "structured_consensus_visibility_current",
            "current analyst consensus table includes EPS target price and provider count",
            ("medium_term_revision_visibility",),
            polarity=Polarity.POSITIVE,
            polarity_source="structured_consensus_visibility_current_not_revision_delta",
        )

    for key, value in row.items():
        if value in (None, ""):
            continue
        primitives = _field_to_primitives(str(key), value)
        if primitives:
            polarity, polarity_source = _structured_field_polarity(str(key), value)
            add(
                f"structured_field_{'_'.join(primitives[:3])}",
                f"structured field {key} is present",
                primitives,
                polarity=polarity,
                polarity_source=polarity_source,
            )
    return tuple(dict((signal.signal_id, signal) for signal in signals).values())


def _has_current_consensus_visibility(row: Mapping[str, Any]) -> bool:
    lowered = {str(key).lower(): value for key, value in row.items()}
    has_date = bool(lowered.get("consensus_as_of_date"))
    has_estimate = lowered.get("target_prc") not in (None, "") or lowered.get("eps") not in (None, "")
    providers = _numeric_value(lowered.get("consensus_provider_count"))
    return has_date and has_estimate and providers is not None and providers > 0


def _structured_field_polarity(key: str, value: Any) -> tuple[Polarity, str]:
    text = f"{key} {value}".lower()
    lowered = key.lower()
    if lowered in {
        "contract_amount_to_prior_sales",
        "contract_duration_months",
        "order_backlog_to_sales",
        "rpo_to_sales",
        "facility_investment_amount",
        "facility_investment_to_market_cap",
    }:
        try:
            if float(str(value).replace(",", "").strip()) > 0:
                return Polarity.POSITIVE, "structured_numeric_positive_official_bridge"
        except ValueError:
            pass
    if lowered in {"expected_completion_date", "contract_start", "contract_end"} and str(value).strip():
        return Polarity.POSITIVE, "structured_date_positive_execution_timeline"
    if any(token in text for token in ("하향", "감소", "축소", "down", "lower", "cut", "negative")):
        return Polarity.NEGATIVE, "structured_field_negative_value"
    if any(token in text for token in ("상향", "증가", "확대", "up", "raise", "positive")):
        return Polarity.POSITIVE, "structured_field_positive_value"
    return Polarity.NORMAL, "structured_field_presence_only_not_score_positive"


def _numeric_value(value: Any) -> float | None:
    try:
        return float(str(value).replace(",", "").strip())
    except (TypeError, ValueError):
        return None


def _support_direction_for_signal(signal: ExtractionSignal) -> SupportDirection:
    if signal.polarity == Polarity.POSITIVE:
        return SupportDirection.SUPPORT
    if signal.polarity == Polarity.NEGATIVE:
        return SupportDirection.COUNTER
    return SupportDirection.NEUTRAL


def _mapped_primitive_for_signal(
    *,
    signal: ExtractionSignal,
    task_primitive_gap: str,
    contract: EvidenceContractV2,
) -> str | None:
    contract_primitives = _contract_primitive_ids(contract)
    if task_primitive_gap in signal.supported_primitives and task_primitive_gap in contract_primitives:
        return task_primitive_gap
    for primitive_id in signal.supported_primitives:
        if primitive_id in contract_primitives:
            return primitive_id
    return None


def _field_to_primitives(key: str, value: Any) -> tuple[str, ...]:
    lowered = key.lower()
    mapping = {
        "eps_action_typ_nm": ("medium_term_revision_visibility", "cycle_to_revenue_bridge", "order_to_revenue_bridge"),
        "prc_action_typ_nm": ("medium_term_revision_visibility", "cycle_to_revenue_bridge", "order_to_revenue_bridge"),
        "recomm_action_typ_nm": ("medium_term_revision_visibility",),
        "target_prc": ("medium_term_revision_visibility",),
        "eps": ("medium_term_revision_visibility",),
        "report_type": ("contract_quality", "revenue_visibility_contract", "export_contract"),
        "contract_amount_to_prior_sales": (
            "contract_quality",
            "contract_amount_to_prior_sales",
            "revenue_visibility_contract",
            "export_contract",
        ),
        "contract_duration_months": ("delivery_schedule", "contract_duration_months", "contract_quality"),
        "contract_start": ("implementation_timeline", "delivery_schedule"),
        "contract_end": ("implementation_timeline", "delivery_schedule"),
        "order_backlog_to_sales": ("order_backlog_to_sales", "revenue_visibility_contract", "equipment_order_backlog"),
        "rpo_to_sales": ("rpo_to_sales", "revenue_visibility_contract", "retention_or_renewal"),
        "backlog_yoy_pct": ("order_backlog_to_sales", "equipment_order_backlog"),
        "record_backlog": ("order_backlog_to_sales", "revenue_visibility_contract"),
        "prepayment_exists": ("contract_quality", "revenue_visibility_contract"),
        "non_cancellable": ("contract_quality",),
        "op_yoy_pct": ("opm_expansion_pctp", "cycle_to_revenue_bridge", "order_to_revenue_bridge"),
        "opm_expansion_pctp": ("opm_expansion_pctp", "margin_bridge_visible", "realized_margin"),
        "fcf_quality_score": ("fcf_quality_score", "direct_company_cash_route"),
        "pricing_power_confirmed": ("pricing_power_confirmed", "spread_expansion"),
        "capa_utilization_pct": ("utilization_rate", "capacity_constraint", "hbm_capacity_constraint"),
        "capa_expansion_pct": ("utilization_rate", "capacity_precommitted", "capacity_constraint"),
        "facility_investment_amount": ("capacity_expansion", "implementation_timeline"),
        "facility_investment_to_market_cap": ("capacity_expansion", "implementation_timeline"),
        "expected_completion_date": ("implementation_timeline", "capacity_expansion"),
        "capacity_constraint": ("capacity_constraint", "hbm_capacity_constraint", "supply_demand_tightness"),
        "capacity_precommitted": ("capacity_precommitted", "hbm_capacity_pre_sold"),
        "lead_time_months": ("lead_time_extended", "capacity_constraint"),
        "asp_yoy_pct": ("memory_price_increase_mentioned", "pricing_power_confirmed", "spread_expansion"),
        "high_margin_mix_pct": ("margin_bridge_visible", "realized_margin"),
    }
    if lowered not in mapping or str(value).strip().lower() in {"0", "false", "none", "없음"}:
        return ()
    if lowered == "report_type" and not _explicit_contract_disclosure(value):
        return ()
    return tuple(dict.fromkeys(mapping[lowered]))


def _explicit_contract_disclosure(value: Any) -> bool:
    text = str(value)
    return any(token in text for token in ("단일판매", "공급계약", "계약체결", "수주", "신규시설투자"))


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
        extractor_model=f"research_brain_v4_{signal.extraction_method}",
        extractor_prompt_hash=f"contract_blind_{signal.extraction_method}_v2",
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
    effective_start, effective_end = _effective_period_from_text(signal.quote)
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
        effective_start=effective_start,
        effective_end=effective_end,
        adjudication_rationale="v4 separated extraction/adjudication from real source anchor",
    )


def _temporal_status(*, signal: ExtractionSignal, document: EvidenceDocument, as_of_date: date) -> TemporalStatus:
    published = document.published_date()
    if published and published > as_of_date:
        return TemporalStatus.UNKNOWN
    if published and (as_of_date - published).days > 540 and not _contains_future_contract(signal.quote, as_of_date):
        return TemporalStatus.HISTORICAL
    return TemporalStatus.CURRENT


def _target_aliases(event: CandidateEventV2, *, source_context: Mapping[str, Any] | None = None) -> tuple[str, ...]:
    symbol = str(event.symbol or "").zfill(6)
    company = str(event.company_name or "").strip()
    aliases = [company, symbol]
    if company and symbol:
        aliases.extend((f"{company}({symbol})", f"{company} ({symbol})"))
    aliases.extend(_source_title_target_aliases(symbol=symbol, source_context=source_context))
    return tuple(dict.fromkeys(alias for alias in aliases if alias))


def _source_title_target_aliases(*, symbol: str, source_context: Mapping[str, Any] | None) -> tuple[str, ...]:
    if not source_context:
        return ()
    title = str(source_context.get("title") or "").strip()
    if not title or not symbol or symbol not in title:
        return ()
    title_before_symbol = title[: title.find(symbol)]
    title_before_symbol = re.sub(r"[\[(]\s*$", "", title_before_symbol).strip()
    segments = [segment.strip(" \t-:|/()[]") for segment in re.split(r"\s[|:–—-]\s", title_before_symbol) if segment.strip()]
    if not segments:
        return ()
    candidate = segments[-1]
    aliases = [candidate, *_company_alias_without_english_suffix(candidate)]
    return tuple(dict.fromkeys(alias for alias in aliases if _looks_like_source_title_company_alias(alias)))


def _company_alias_without_english_suffix(value: str) -> tuple[str, ...]:
    stripped = re.sub(
        r"\b(?:co|corp|corporation|inc|ltd|limited|plc|sa|ag)\b\.?",
        "",
        str(value or ""),
        flags=re.IGNORECASE,
    )
    stripped = re.sub(r"\s+", " ", stripped).strip(" ,.-")
    return (stripped,) if stripped and stripped != value else ()


def _looks_like_source_title_company_alias(value: str) -> bool:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(text) < 2 or len(text) > 80:
        return False
    if not re.search(r"[A-Za-z]", text):
        return False
    lowered = text.casefold()
    blocked = {
        "research report",
        "stock report",
        "company report",
        "equity research",
        "daily report",
        "market report",
        "mirae asset securities",
    }
    return lowered not in blocked


def _polarity_from_text(value: str | Polarity | None) -> Polarity:
    if isinstance(value, Polarity):
        return value
    try:
        return Polarity(str(value or "MIXED").upper())
    except ValueError:
        return Polarity.MIXED


def _support_direction_from_text(value: str | SupportDirection | None) -> SupportDirection:
    if isinstance(value, SupportDirection):
        return value
    try:
        return SupportDirection(str(value or "NEUTRAL").upper())
    except ValueError:
        return SupportDirection.NEUTRAL


def _mapping_status_from_text(value: str | MappingStatus | None) -> MappingStatus:
    if isinstance(value, MappingStatus):
        return value
    try:
        return MappingStatus(str(value or "REJECTED").upper())
    except ValueError:
        return MappingStatus.REJECTED


def _temporal_status_from_text(value: str | TemporalStatus | None) -> TemporalStatus:
    if isinstance(value, TemporalStatus):
        return value
    try:
        return TemporalStatus(str(value or "UNKNOWN").upper())
    except ValueError:
        return TemporalStatus.UNKNOWN


def _parse_iso_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def _contains_future_contract(text: str, as_of_date: date) -> bool:
    years = [int(year) for year in re.findall(r"\b(20[2-4][0-9])\b", text)]
    return any(year >= as_of_date.year for year in years)


def _effective_period_from_text(text: str) -> tuple[date | None, date | None]:
    patterns = (
        r"(20\d{2})[-./년 ]+(\d{1,2})[-./월 ]+(\d{1,2})\s*(?:일)?\s*(?:~|부터|[-–])\s*(20\d{2})[-./년 ]+(\d{1,2})[-./월 ]+(\d{1,2})",
        r"계약기간\s*(20\d{2})[-./년 ]+(\d{1,2})[-./월 ]+(\d{1,2})\s*(?:일)?\s*(?:~|부터|[-–])\s*(20\d{2})[-./년 ]+(\d{1,2})[-./월 ]+(\d{1,2})",
    )
    for pattern in patterns:
        match = re.search(pattern, text)
        if not match:
            continue
        start = _date_from_match_groups(match.groups()[:3])
        end = _date_from_match_groups(match.groups()[3:6])
        if start is not None or end is not None:
            return start, end
    return None, None


def _date_from_match_groups(groups: tuple[str, str, str] | Sequence[str]) -> date | None:
    try:
        year, month, day = (int(groups[0]), int(groups[1]), int(groups[2]))
        return date(year, month, day)
    except (TypeError, ValueError, IndexError):
        return None


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
