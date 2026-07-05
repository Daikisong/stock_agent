"""Known-bad regression suite for Census v4 anti-overclaim gates."""

from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Callable, Mapping

from e2r.agentic.evidence_os import (
    AdjudicatedClaim,
    AppendOnlyEvidenceLedger,
    Directness,
    EvidenceAnchor,
    EvidenceContractV2,
    EvidenceDocument,
    GateExpression,
    InvestigationStatus,
    MappingStatus,
    Polarity,
    PrimitiveMappingProposal,
    PrimitiveStatus,
    RawAssertion,
    RelationToTarget,
    ScoreInterval,
    SemanticStatus,
    SourceType,
    SupportDirection,
    TargetScopeStatus,
    TemporalStatus,
    TransitionOverlay,
    VerificationStatus,
    derive_score_eligibility,
)
from e2r.agentic.primitive_aggregator import aggregate_primitive_states
from e2r.agentic.stage_court import StageCourtInput, decide_stage_court
from e2r.evidence.contract_semantic_classifier import classify_contract_event
from e2r.production.claim_extraction.contract_blind_extractor import (
    ContractBlindRawAssertionExtractor,
    ExtractionInput,
)

from .census_v4_auditor import audit_census_v4_leaf_artifacts


KNOWN_BAD_SCHEMA = "e2r_census_v4_known_bad_regression_report_v1"
MIN_KNOWN_BAD_CASE_COUNT = 10
REQUIRED_KNOWN_BAD_CASE_IDS = (
    "wrong_subject_audit_opinion_not_target_risk",
    "old_risk_resolved_not_current_hard_break",
    "non_revenue_contract_not_contract_quality",
    "trace_mismatch_guard",
    "trace_score_interval_guard",
    "trace_claim_set_guard",
    "source_proxy_score_guard",
    "evidence_url_pending_score_guard",
    "snippet_score_guard",
    "provider_failure_final_score_guard",
    "samsung_hynix_daily_event_not_full_thesis_or_4c",
)


def run_known_bad_regression(*, output_root: str | Path, target_gate: str) -> dict[str, Any]:
    root = Path(output_root)
    leaf = audit_census_v4_leaf_artifacts(root)
    critical = leaf.get("critical_counts") or {}
    cases = [
        _wrong_subject_audit_opinion_case(),
        _old_risk_resolved_not_current_hard_break_case(),
        _non_revenue_contract_case(),
        _mutated_leaf_critical_case(
            root,
            case_id="trace_mismatch_guard",
            critical_count_key="stage_trace_stage_mismatch_count",
            mutate=_mutate_stage_trace_stage_mismatch,
        ),
        _mutated_leaf_critical_case(
            root,
            case_id="trace_score_interval_guard",
            critical_count_key="stage_trace_score_interval_mismatch_count",
            mutate=_mutate_stage_trace_score_interval_mismatch,
        ),
        _mutated_leaf_critical_case(
            root,
            case_id="trace_claim_set_guard",
            critical_count_key="stage_trace_claim_set_mismatch_count",
            mutate=_mutate_stage_trace_claim_set_mismatch,
        ),
        _mutated_leaf_critical_case(
            root,
            case_id="source_proxy_score_guard",
            critical_count_key="source_proxy_to_score_count",
            mutate=_mutate_source_proxy_score_contribution,
        ),
        _mutated_leaf_critical_case(
            root,
            case_id="evidence_url_pending_score_guard",
            critical_count_key="evidence_url_pending_to_score_count",
            mutate=_mutate_evidence_url_pending_score_contribution,
        ),
        _mutated_leaf_critical_case(
            root,
            case_id="snippet_score_guard",
            critical_count_key="news_snippet_to_score_count",
            mutate=_mutate_snippet_score_contribution,
        ),
        _mutated_leaf_critical_case(
            root,
            case_id="provider_failure_final_score_guard",
            critical_count_key="provider_failed_final_score_count",
            mutate=_mutate_provider_failed_final_score,
        ),
        _samsung_hynix_daily_event_not_full_thesis_case(root),
    ]
    case_ids = {str(case.get("case_id") or "") for case in cases}
    missing_required_case_ids = sorted(set(REQUIRED_KNOWN_BAD_CASE_IDS) - case_ids)
    minimum_case_count_pass = len(cases) >= MIN_KNOWN_BAD_CASE_COUNT
    failed = [case for case in cases if case.get("status") != "PASS"]
    completion_eligible = not failed and not missing_required_case_ids and minimum_case_count_pass
    return {
        "schema_version": KNOWN_BAD_SCHEMA,
        "status": "PASS" if completion_eligible else "FAIL",
        "target_gate": target_gate,
        "completion_eligible": completion_eligible,
        "known_bad_required_before_goal_completion": True,
        "required_case_ids": list(REQUIRED_KNOWN_BAD_CASE_IDS),
        "missing_required_case_ids": missing_required_case_ids,
        "minimum_case_count_required": MIN_KNOWN_BAD_CASE_COUNT,
        "minimum_case_count_pass": minimum_case_count_pass,
        "case_count": len(cases),
        "passed_case_count": len(cases) - len(failed),
        "failed_case_count": len(failed),
        "cases": cases,
        "required_before_labels": [
            "KNOWN_BAD_REGRESSION_PASS",
            "MEANINGFUL_OPERATIONAL_STAGE_PASS",
            "READY_FOR_OPERATIONAL_STAGE_USE",
        ],
        "note": "Known-bad regression runs deterministic adversarial fixtures and leaf critical-count guards.",
    }


def _wrong_subject_audit_opinion_case() -> dict[str, Any]:
    extractor = ContractBlindRawAssertionExtractor()
    records = extractor.extract(
        ExtractionInput(
            target_entity_id="CORP_SAMSUNG_ELECTRONICS",
            target_aliases=("삼성전자",),
            as_of_date="2026-07-01",
            document_id="DOC-WORLDEX-AUDIT",
            anchor_id="ANC-WORLDEX-AUDIT",
            source_text="월덱스는 삼성전자와 거래 관계가 있으며 감사의견은 적정이다.",
        )
    )
    audit_records = [record for record in records if record.predicate == "audit_or_accounting_claim"]
    passed = len(audit_records) == 1 and audit_records[0].subject == "월덱스"
    return {
        "case_id": "wrong_subject_audit_opinion_not_target_risk",
        "status": "PASS" if passed else "FAIL",
        "expected": "audit/accounting claim subject is 월덱스, not 삼성전자",
        "observed_subjects": [record.subject for record in audit_records],
    }


def _non_revenue_contract_case() -> dict[str, Any]:
    buyback = classify_contract_event({"quote_text": "자기주식취득신탁계약체결결정"})
    pledge = classify_contract_event({"quote_text": "주식담보제공계약체결"})
    passed = not buyback.allowed_for_contract_quality and not pledge.allowed_for_contract_quality
    return {
        "case_id": "non_revenue_contract_not_contract_quality",
        "status": "PASS" if passed else "FAIL",
        "expected": "share buyback trust and pledge contracts cannot unlock contract_quality",
        "observed_classes": [buyback.event_class, pledge.event_class],
    }


def _old_risk_resolved_not_current_hard_break_case() -> dict[str, Any]:
    text = "Target issuer disclosed that the prior adverse audit opinion issue was fully resolved."
    document = EvidenceDocument.from_text(
        text=text,
        canonical_url="fixture://target-risk-resolved",
        source_type=SourceType.FILING,
        source_name="KnownBadLifecycleFixture",
        published_at=_date("2026-06-01"),
    )
    quote = "prior adverse audit opinion issue was fully resolved"
    anchor = EvidenceAnchor.text_span(document=document, document_text=text, exact_text=quote)
    raw = RawAssertion(
        raw_assertion_id="RAW-KNOWN-BAD-OLD-RISK-RESOLVED",
        anchor_id=anchor.anchor_id,
        subject_text="Target issuer",
        predicate="prior adverse audit opinion issue",
        object_text="fully resolved",
        polarity_proposal=Polarity.NEGATIVE,
        event_date_text="2026-06-01",
        exact_quote=quote,
    )
    claim = AdjudicatedClaim.from_raw(
        raw=raw,
        document=document,
        anchor=anchor,
        subject_entity_id="CORP_TARGET",
        target_entity_id="CORP_TARGET",
        relation_to_target=RelationToTarget.SELF,
        directness=Directness.DIRECT,
        verification_status=VerificationStatus.SEMANTIC_VERIFIED,
        target_scope_status=TargetScopeStatus.DIRECT,
        polarity=Polarity.NEGATIVE,
        temporal_status=TemporalStatus.RESOLVED,
        semantic_status=SemanticStatus.PASS_,
        investigation_status=InvestigationStatus.COMPLETE,
        event_date=_date("2026-06-01"),
    )
    contract = EvidenceContractV2(
        archetype_id="R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
        required_primitives=("accounting_trust_break",),
        green_gate=GateExpression.primitive("accounting_trust_break"),
    )
    mapping = PrimitiveMappingProposal.build(
        claim_id=claim.claim_id,
        archetype_id=contract.archetype_id,
        primitive_id="accounting_trust_break",
        support_direction=SupportDirection.SUPPORT,
        mapping_status=MappingStatus.ACCEPTED,
        rationale="Resolved historical accounting issue is lifecycle context, not current hard break.",
    )
    eligibility = derive_score_eligibility(
        document=document,
        anchor=anchor,
        claim=claim,
        mapping=mapping,
        as_of_date=_date("2026-07-01"),
        require_source_quorum=True,
        source_quorum_satisfied=True,
    )
    ledger = AppendOnlyEvidenceLedger()
    ledger.append_claim(claim)
    ledger.append_mapping(mapping)
    states = aggregate_primitive_states(ledger=ledger, contract=contract, as_of_date=_date("2026-07-01"))
    stage = decide_stage_court(
        StageCourtInput(
            score_interval=ScoreInterval(verified_score=91.0, potential_score_upper_bound=91.0),
            primitive_states=states,
            contract=contract,
            current_hard_break_claim_ids=(),
            has_prior_live_thesis=True,
        )
    )
    primitive = states["accounting_trust_break"]
    passed = (
        eligibility.eligible is False
        and "temporal_not_allowed:RESOLVED" in eligibility.reasons
        and primitive.status == PrimitiveStatus.RESOLVED
        and primitive.support_claim_ids == ()
        and stage.decision.transition_overlay == TransitionOverlay.NONE
        and all(not str(reason).startswith("current_hard_break_claims:") for reason in stage.reasons)
    )
    return {
        "case_id": "old_risk_resolved_not_current_hard_break",
        "status": "PASS" if passed else "FAIL",
        "expected": "resolved target accounting/trust risk is lifecycle context, not current score evidence or 4C hard break",
        "observed": {
            "score_eligible": eligibility.eligible,
            "eligibility_reasons": list(eligibility.reasons),
            "primitive_status": primitive.status.value,
            "support_claim_ids": list(primitive.support_claim_ids),
            "transition_overlay": stage.decision.transition_overlay.value,
            "stage_reasons": list(stage.reasons),
        },
    }


def _samsung_hynix_daily_event_not_full_thesis_case(root: Path) -> dict[str, Any]:
    rows = {str(row.get("symbol") or "").zfill(6): row for row in _read_jsonl(root / "census_stage_status.jsonl")}
    observed = {}
    passed = True
    for symbol in ("005930", "000660"):
        row = rows.get(symbol) or {}
        observed[symbol] = {
            "base_stage": row.get("base_stage"),
            "canonical_stage": row.get("canonical_stage"),
            "stage_scope": row.get("stage_scope"),
            "score_scale": row.get("score_scale"),
            "event_evidence_score": row.get("event_evidence_score"),
            "daily_event_evidence_score": row.get("daily_event_evidence_score"),
            "full_thesis_stage": row.get("full_thesis_stage"),
            "verified_score": row.get("verified_score"),
            "full_e2r_verified_score": row.get("full_e2r_verified_score"),
        }
        full_thesis_ran = row.get("stage_scope") == "FULL_THESIS"
        if full_thesis_ran:
            if row.get("score_scale") != "FULL_E2R_100":
                passed = False
            if row.get("event_evidence_score") is not None:
                passed = False
            if row.get("daily_event_evidence_score") is None:
                passed = False
            if row.get("verified_score") is None or row.get("full_e2r_verified_score") is None:
                passed = False
            if row.get("full_thesis_stage") in {None, "", "FULL_THESIS_NOT_RUN"}:
                passed = False
        elif row.get("full_thesis_stage") != "FULL_THESIS_NOT_RUN":
            passed = False
        if not full_thesis_ran and (row.get("verified_score") is not None or row.get("full_e2r_verified_score") is not None):
            passed = False
        if row.get("canonical_stage") in {"4A", "4B", "4C"}:
            passed = False
    return {
        "case_id": "samsung_hynix_daily_event_not_full_thesis_or_4c",
        "status": "PASS" if passed else "FAIL",
        "expected": "Samsung/Hynix separate daily event score from full thesis score and never become 4C from daily-event evidence",
        "observed": observed,
    }


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if text:
                rows.append(json.loads(text))
    return rows


def _mutated_leaf_critical_case(
    root: Path,
    *,
    case_id: str,
    critical_count_key: str,
    mutate: Callable[[Path, Path], str],
) -> dict[str, Any]:
    with TemporaryDirectory() as tmp:
        mutated_root = Path(tmp) / case_id
        mutated_root.mkdir(parents=True, exist_ok=True)
        mutation_note = mutate(root, mutated_root)
        audit = audit_census_v4_leaf_artifacts(mutated_root)
    value = int((audit.get("critical_counts") or {}).get(critical_count_key) or 0)
    passed = value > 0
    return {
        "case_id": case_id,
        "status": "PASS" if passed else "FAIL",
        "fixture_type": "mutated_leaf_artifact",
        "critical_count_key": critical_count_key,
        "expected": f"mutated fixture must raise {critical_count_key}",
        "observed_count": value,
        "mutation_note": mutation_note,
    }


def _mutate_stage_trace_stage_mismatch(source_root: Path, target_root: Path) -> str:
    stage_rows, atomic_rows = _first_stage_atomic_pair(source_root)
    stage_rows[0]["base_stage"] = "Stage3-Green" if stage_rows[0].get("base_stage") != "Stage3-Green" else "Stage0"
    _write_jsonl(target_root / "census_stage_status.jsonl", stage_rows[:1])
    _write_jsonl(target_root / "atomic_stage_decisions.jsonl", atomic_rows)
    return "changed stage row base_stage while leaving atomic decision unchanged"


def _mutate_stage_trace_score_interval_mismatch(source_root: Path, target_root: Path) -> str:
    stage_rows, atomic_rows = _first_stage_atomic_pair(source_root)
    stage_rows[0]["score_interval_lower"] = float(stage_rows[0].get("score_interval_lower") or 0.0) + 7.0
    _write_jsonl(target_root / "census_stage_status.jsonl", stage_rows[:1])
    _write_jsonl(target_root / "atomic_stage_decisions.jsonl", atomic_rows)
    return "changed stage row score interval lower while leaving atomic decision unchanged"


def _mutate_stage_trace_claim_set_mismatch(source_root: Path, target_root: Path) -> str:
    stage_rows, atomic_rows = _first_stage_atomic_pair(source_root)
    claims = list(stage_rows[0].get("accepted_claim_ids") or [])
    claims.append("CLM-KNOWN-BAD-MISSING")
    stage_rows[0]["accepted_claim_ids"] = claims
    _write_jsonl(target_root / "census_stage_status.jsonl", stage_rows[:1])
    _write_jsonl(target_root / "atomic_stage_decisions.jsonl", atomic_rows)
    return "added an extra stage row accepted claim absent from atomic decision"


def _mutate_source_proxy_score_contribution(source_root: Path, target_root: Path) -> str:
    rows = _read_jsonl(source_root / "score_contributions.jsonl")
    if not rows:
        raise ValueError("score_contributions.jsonl has no rows for known-bad mutation")
    rows[0]["source_proxy_only"] = True
    _write_jsonl(target_root / "score_contributions.jsonl", rows[:1])
    return "marked a score contribution as source_proxy_only"


def _mutate_evidence_url_pending_score_contribution(source_root: Path, target_root: Path) -> str:
    rows = _read_jsonl(source_root / "score_contributions.jsonl")
    if not rows:
        raise ValueError("score_contributions.jsonl has no rows for known-bad mutation")
    rows[0]["evidence_url_pending"] = True
    _write_jsonl(target_root / "score_contributions.jsonl", rows[:1])
    return "marked a score contribution as evidence_url_pending"


def _mutate_snippet_score_contribution(source_root: Path, target_root: Path) -> str:
    rows = _read_jsonl(source_root / "score_contributions.jsonl")
    if not rows:
        raise ValueError("score_contributions.jsonl has no rows for known-bad mutation")
    rows[0]["source_type"] = "snippet"
    _write_jsonl(target_root / "score_contributions.jsonl", rows[:1])
    return "changed a score contribution source_type to snippet"


def _mutate_provider_failed_final_score(source_root: Path, target_root: Path) -> str:
    rows = _read_jsonl(source_root / "census_stage_status.jsonl")
    if not rows:
        raise ValueError("census_stage_status.jsonl has no rows for known-bad mutation")
    row = dict(rows[0])
    row["census_status"] = "PENDING_PROVIDER"
    row["score_scale"] = "FULL_E2R_100"
    row["verified_score"] = row.get("verified_score") if row.get("verified_score") is not None else 1.0
    _write_jsonl(target_root / "census_stage_status.jsonl", [row])
    return "gave a provider-pending stage row a score scale and verified score"


def _first_stage_atomic_pair(source_root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    stage_rows = _read_jsonl(source_root / "census_stage_status.jsonl")
    atomic_rows = _read_jsonl(source_root / "atomic_stage_decisions.jsonl")
    atomic_by_id = {str(row.get("atomic_stage_decision_id") or ""): row for row in atomic_rows}
    for row in stage_rows:
        atomic_id = str(row.get("atomic_stage_decision_id") or "")
        if atomic_id and atomic_id in atomic_by_id:
            return [dict(row)], [dict(atomic_by_id[atomic_id])]
    raise ValueError("no stage row with atomic_stage_decision_id found for known-bad mutation")


def _write_jsonl(path: Path, rows: list[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(dict(row), ensure_ascii=False, sort_keys=True) + "\n")


def _date(value: str):
    from datetime import date

    return date.fromisoformat(value)


__all__ = ["KNOWN_BAD_SCHEMA", "run_known_bad_regression"]
