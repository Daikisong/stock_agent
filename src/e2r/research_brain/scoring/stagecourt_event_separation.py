"""Audit full-thesis Stage and daily event-overlay separation."""

from __future__ import annotations

import json
from typing import Any, Mapping

from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)

from .atomic_stagecourt_v2 import (
    AtomicStageCourtV2,
    EventOverlayInput,
    FullThesisStageInput,
    RiskOverlayInput,
)
from .claim_impact_ledger import ClaimImpactProposal, ValidatedClaimImpact
from .component_assessment import ComponentAssessmentBuilder
from .component_scorer import ResearchCalibratedComponentScorer
from .full_score_validity import FullScoreValidityEvidenceV2
from .impact_validator import ImpactValidator


ARCHETYPE_ID = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
TARGET_ID = "TARGET-STAGE-EVENT-SEPARATION"


def audit_stagecourt_event_separation() -> Mapping[str, Any]:
    contract = load_archetype_scoring_contract(ARCHETYPE_ID)
    impact = _validated_support_impact()
    terminal = {
        component_id: {
            "status": "VERIFIED_ABSENT_AFTER_SEARCH",
            "search_exhaustion_proof": ["STAGE-EVENT-CANARY-EXHAUSTED"],
        }
        for component_id in contract.component_weights
        if component_id != "bottleneck_pricing"
    }
    assessment = ComponentAssessmentBuilder().build(
        contract=contract,
        impacts=(impact,),
        terminal_evidence=terminal,
    )
    score = ResearchCalibratedComponentScorer().score(
        contract=contract,
        impacts=(impact,),
        assessments=assessment.assessments,
        validity_evidence=_canary_validity_evidence(),
    )
    court = AtomicStageCourtV2()

    def stage_input(claim_ids: tuple[str, ...]) -> FullThesisStageInput:
        return FullThesisStageInput(
            target_id=TARGET_ID,
            as_of_date="2026-07-11",
            contract=contract,
            score=score,
            assessments=assessment.assessments,
            impacts=(impact,),
            accepted_claim_ids=claim_ids,
        )

    no_event = court.decide_full_thesis(
        full_thesis_input=stage_input(("CLM-STAGE-SUPPORT",)),
        event_overlay_input=EventOverlayInput(),
        risk_overlay_input=RiskOverlayInput(),
    )
    more_generic_claims = court.decide_full_thesis(
        full_thesis_input=stage_input(
            (
                "CLM-STAGE-SUPPORT",
                "CLM-GENERIC-2",
                "CLM-GENERIC-3",
            )
        ),
        event_overlay_input=EventOverlayInput(),
        risk_overlay_input=RiskOverlayInput(),
    )
    explicit_event = court.decide_full_thesis(
        full_thesis_input=stage_input(("CLM-STAGE-SUPPORT",)),
        event_overlay_input=EventOverlayInput(
            event_quality_contract_status="HIGH_QUALITY_EVENT_PASS",
            event_claim_ids=("CLM-STAGE-SUPPORT",),
            event_type="EARNINGS_RELEASE_WATCH",
            event_rationale="Explicit bounded event-quality contract passed.",
            source_evidence_ids=("DOC-STAGE-SUPPORT",),
        ),
        risk_overlay_input=RiskOverlayInput(),
    )
    generic_boolean = court.decide(
        target_id=TARGET_ID,
        as_of_date="2026-07-11",
        contract=contract,
        score=score,
        assessments=assessment.assessments,
        impacts=(impact,),
        accepted_claim_ids=("CLM-STAGE-SUPPORT",),
        claim_eligibility_decisions=(
            {
                "claim_id": "CLM-STAGE-SUPPORT",
                "stage_event_eligibility": True,
            },
        ),
    )
    critical = {
        "claim_count_event_boost_count": int(
            no_event.canonical_stage != more_generic_claims.canonical_stage
            or more_generic_claims.canonical_stage == "1"
        ),
        "generic_claim_high_quality_event_count": int(
            generic_boolean.event_overlay.get("status")
            == "EVENT_OVERLAY_ACTIVE"
            or bool(generic_boolean.stage_event_claim_ids)
        ),
        "full_thesis_event_score_injection_count": int(
            no_event.canonical_stage != explicit_event.canonical_stage
            or any(
                "company-level event" in reason.casefold()
                for reason in explicit_event.stage_reason
            )
        ),
        "explicit_event_overlay_missing_count": int(
            explicit_event.event_overlay.get("status")
            != "EVENT_OVERLAY_ACTIVE"
            or explicit_event.event_overlay.get("stage_signal")
            != "EVENT_WATCH"
        ),
    }
    critical_sum = sum(critical.values())
    audit = {
        "schema_version": "e2r_stagecourt_event_separation_audit_v1",
        "status": (
            "STAGECOURT_EVENT_SEPARATION_PASS"
            if critical_sum == 0
            else "STAGECOURT_EVENT_SEPARATION_FAIL"
        ),
        "archetype_id": ARCHETYPE_ID,
        "no_event_decision": no_event.to_dict(),
        "more_generic_claims_decision": more_generic_claims.to_dict(),
        "explicit_event_decision": explicit_event.to_dict(),
        "generic_boolean_decision": generic_boolean.to_dict(),
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
    }
    return json.loads(json.dumps(audit, ensure_ascii=False))


def _validated_support_impact():
    proposal = ClaimImpactProposal(
        impact_id="IMPACT-STAGE-SUPPORT",
        claim_id="CLM-STAGE-SUPPORT",
        mapping_id="MAP-STAGE-SUPPORT",
        target_id=TARGET_ID,
        archetype_id=ARCHETYPE_ID,
        primitive_id="memory_price_increase_mentioned",
        component_id="bottleneck_pricing",
        direction="SUPPORT",
        support_type="DIRECT_ACTUAL",
        strength_band="STRONG",
        completeness_band="SUBSTANTIAL",
        causal_distance="DIRECT",
        temporal_scope="CURRENT",
        source_family="ISSUER_OFFICIAL",
        evidence_family_id="FAMILY-STAGE-SUPPORT",
        confidence=0.9,
        rationale="Current realized ASP evidence supports the bounded subcriterion.",
        unsupported_aspects=("No event quality is inferred from this claim.",),
        question_family_id="asp_pricing_actual",
        component_subcriterion_id="C06_BOT_REALIZED_ASP",
        mechanism_scope_match=True,
    )
    validation = ImpactValidator().validate(
        impacts=(
            ValidatedClaimImpact(
                proposal=proposal,
                scope_validation={
                    "status": "MECHANISM_SCOPE_PASS",
                    "scope_match": True,
                    "scope": {
                        "issuer_id": TARGET_ID,
                        "business_segment": "MEMORY",
                        "product_family": "HBM",
                        "economic_mechanism": "PRICING_POWER",
                    },
                },
                eligibility_decision_id="ELIG-STAGE-SUPPORT",
            ),
        ),
        claim_provenance=(
            {
                "claim_id": "CLM-STAGE-SUPPORT",
                "mapping_ids": ["MAP-STAGE-SUPPORT"],
                "document_id": "DOC-STAGE-SUPPORT",
                "source_url": "https://issuer.example/stage-support",
                "source_proxy_only": False,
                "directness": "DIRECT",
                "temporal_status": "CURRENT",
            },
        ),
        claim_eligibility_decisions=(
            {
                "eligibility_decision_id": "ELIG-STAGE-SUPPORT",
                "claim_id": "CLM-STAGE-SUPPORT",
                "component_scoring_eligibility": True,
            },
        ),
        accepted_current_claims=(
            {
                "claim_id": "CLM-STAGE-SUPPORT",
                "target_id": TARGET_ID,
                "accepted": True,
                "mapping_ids": ["MAP-STAGE-SUPPORT"],
                "economic_fact_key": "FACT-STAGE-SUPPORT",
            },
        ),
    )
    if validation.status != "IMPACT_CREDIT_CAP_PASS":
        raise ValueError("stage event separation canary validation failed")
    return validation.impacts[0]


def _canary_validity_evidence() -> FullScoreValidityEvidenceV2:
    return FullScoreValidityEvidenceV2(
        schema_totality_status="SCORING_SCHEMA_TOTALITY_PASS",
        scoring_schema_critical_count=0,
        silent_zero_default_count=0,
        positive_impact_zeroed_by_missing_cap_count=0,
        counter_impact_zeroed_by_missing_cap_count=0,
        mechanism_scope_failure_count=0,
        question_component_reconciliation_critical_count=0,
        unresolved_contradiction_count=0,
        pending_state_count=0,
        absence_without_adequacy_count=0,
        gold_critical_fact_miss_count=0,
        cross_business_question_closure_count=0,
        same_fact_duplicate_credit_count=0,
        same_document_duplicate_credit_count=0,
        source_audit_ids=("CONTROLLED-STAGE-EVENT-CANARY",),
    )


__all__ = ["audit_stagecourt_event_separation"]
