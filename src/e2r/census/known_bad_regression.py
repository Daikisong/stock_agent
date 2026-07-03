"""Known-bad regression suite for Census v4 anti-overclaim gates."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

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


def run_known_bad_regression(*, output_root: str | Path, target_gate: str) -> dict[str, Any]:
    root = Path(output_root)
    leaf = audit_census_v4_leaf_artifacts(root)
    critical = leaf.get("critical_counts") or {}
    cases = [
        _wrong_subject_audit_opinion_case(),
        _old_risk_resolved_not_current_hard_break_case(),
        _non_revenue_contract_case(),
        _critical_zero_case("trace_mismatch_guard", critical, "stage_trace_stage_mismatch_count"),
        _critical_zero_case("trace_score_interval_guard", critical, "stage_trace_score_interval_mismatch_count"),
        _critical_zero_case("trace_claim_set_guard", critical, "stage_trace_claim_set_mismatch_count"),
        _critical_zero_case("source_proxy_score_guard", critical, "source_proxy_to_score_count"),
        _critical_zero_case("evidence_url_pending_score_guard", critical, "evidence_url_pending_to_score_count"),
        _critical_zero_case("snippet_score_guard", critical, "news_snippet_to_score_count"),
        _critical_zero_case("provider_failure_final_score_guard", critical, "provider_failed_final_score_count"),
        _samsung_hynix_daily_event_not_full_thesis_case(root),
    ]
    failed = [case for case in cases if case.get("status") != "PASS"]
    return {
        "schema_version": KNOWN_BAD_SCHEMA,
        "status": "PASS" if not failed else "FAIL",
        "target_gate": target_gate,
        "completion_eligible": not failed,
        "known_bad_required_before_goal_completion": True,
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


def _critical_zero_case(case_id: str, critical: Mapping[str, Any], key: str) -> dict[str, Any]:
    value = int(critical.get(key) or 0)
    return {
        "case_id": case_id,
        "status": "PASS" if value == 0 else "FAIL",
        "critical_count_key": key,
        "observed_count": value,
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


def _date(value: str):
    from datetime import date

    return date.fromisoformat(value)


__all__ = ["KNOWN_BAD_SCHEMA", "run_known_bad_regression"]
