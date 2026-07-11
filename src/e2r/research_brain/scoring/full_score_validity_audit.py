"""Source-backed canaries for the semantic full-score validity v2 gate."""

from __future__ import annotations

import json
from dataclasses import replace
from typing import Any, Mapping

from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)

from .claim_impact_ledger import ClaimImpactProposal, ValidatedClaimImpact
from .component_assessment import ComponentAssessmentBuilder
from .component_scorer import ResearchCalibratedComponentScorer
from .full_score_validity import FullScoreValidityEvidenceV2
from .impact_validator import ImpactValidator


ARCHETYPE_ID = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
TARGET_ID = "TARGET-FULL-SCORE-VALIDITY"


def audit_full_score_validity_v2() -> Mapping[str, Any]:
    contract = load_archetype_scoring_contract(ARCHETYPE_ID)
    impact = _validated_impact()
    assessment = ComponentAssessmentBuilder().build(
        contract=contract,
        impacts=(impact,),
        terminal_evidence={
            component_id: {
                "status": "VERIFIED_ABSENT_AFTER_SEARCH",
                "search_exhaustion_proof": [
                    f"VALIDITY-CANARY-{component_id}"
                ],
            }
            for component_id in contract.component_weights
            if component_id != impact.component_id
        },
    )
    scorer = ResearchCalibratedComponentScorer()
    passing_evidence = _passing_evidence()
    baseline = scorer.score(
        contract=contract,
        impacts=(impact,),
        assessments=assessment.assessments,
        validity_evidence=passing_evidence,
    )
    mutations = {
        "scoring_schema_not_total": {
            "schema_totality_status": "SCORING_SCHEMA_TOTALITY_FAIL"
        },
        "silent_zero_default": {"silent_zero_default_count": 1},
        "positive_missing_cap": {
            "positive_impact_zeroed_by_missing_cap_count": 1
        },
        "counter_missing_cap": {
            "counter_impact_zeroed_by_missing_cap_count": 1
        },
        "mechanism_scope_failure": {"mechanism_scope_failure_count": 1},
        "question_component_reconciliation_failure": {
            "question_component_reconciliation_critical_count": 1
        },
        "unresolved_contradiction": {
            "unresolved_contradiction_count": 1
        },
        "provider_source_budget_pending": {"pending_state_count": 1},
        "absence_without_adequacy": {
            "absence_without_adequacy_count": 1
        },
        "gold_critical_fact_miss": {
            "gold_critical_fact_miss_count": 1
        },
        "cross_business_question_closure": {
            "cross_business_question_closure_count": 1
        },
        "same_fact_duplicate_credit": {
            "same_fact_duplicate_credit_count": 1
        },
        "same_document_duplicate_credit": {
            "same_document_duplicate_credit_count": 1
        },
    }
    cases = {}
    for case_id, changes in mutations.items():
        result = scorer.score(
            contract=contract,
            impacts=(impact,),
            assessments=assessment.assessments,
            validity_evidence=replace(passing_evidence, **changes),
        )
        cases[case_id] = _score_case(result)
    missing_evidence = scorer.score(
        contract=contract,
        impacts=(impact,),
        assessments=assessment.assessments,
    )
    critical = {
        "valid_baseline_rejected_count": int(
            not baseline.full_score_valid
            or baseline.full_e2r_score is None
            or baseline.score_type != "FULL_E2R_100"
        ),
        "semantic_failure_allowed_full_score_count": sum(
            row["full_score_valid"] or row["full_e2r_score"] is not None
            for row in cases.values()
        ),
        "invalid_score_reference_lost_count": sum(
            row["verified_supported_score"]
            != baseline.verified_supported_score
            or row["provisional_score_lower"]
            != baseline.provisional_score_lower
            or row["provisional_score_upper"]
            != baseline.provisional_score_upper
            for row in cases.values()
        ),
        "missing_validity_evidence_allowed_full_score_count": int(
            missing_evidence.full_score_valid
            or missing_evidence.full_e2r_score is not None
        ),
        "required_gate_case_missing_count": max(0, 13 - len(cases)),
    }
    critical_sum = sum(critical.values())
    audit = {
        "schema_version": "e2r_full_score_validity_v2_audit_v1",
        "status": (
            "FULL_SCORE_VALIDITY_V2_AUDIT_PASS"
            if critical_sum == 0
            else "FULL_SCORE_VALIDITY_V2_AUDIT_FAIL"
        ),
        "archetype_id": ARCHETYPE_ID,
        "baseline": _score_case(baseline),
        "failure_cases": cases,
        "missing_evidence_case": _score_case(missing_evidence),
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
    }
    return json.loads(json.dumps(audit, ensure_ascii=False))


def _score_case(result: Any) -> Mapping[str, Any]:
    validity = result.audit["full_score_validity"]
    return {
        "full_score_valid": result.full_score_valid,
        "score_type": result.score_type,
        "full_e2r_score": result.full_e2r_score,
        "verified_supported_score": result.verified_supported_score,
        "provisional_score_lower": result.provisional_score_lower,
        "provisional_score_upper": result.provisional_score_upper,
        "validity_status": validity["status"],
        "blocking_reasons": validity["blocking_reasons"],
        "validity_critical_count_sum": validity["critical_count_sum"],
    }


def _passing_evidence() -> FullScoreValidityEvidenceV2:
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
        source_audit_ids=("CONTROLLED-FULL-SCORE-VALIDITY-CANARY",),
    )


def _validated_impact():
    proposal = ClaimImpactProposal(
        impact_id="IMPACT-FULL-SCORE-VALIDITY",
        claim_id="CLM-FULL-SCORE-VALIDITY",
        mapping_id="MAP-FULL-SCORE-VALIDITY",
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
        evidence_family_id="FAMILY-FULL-SCORE-VALIDITY",
        confidence=0.9,
        rationale="The current issuer source supports realized pricing only.",
        unsupported_aspects=("No unsupported stronger effect is inferred.",),
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
                eligibility_decision_id="ELIG-FULL-SCORE-VALIDITY",
            ),
        ),
        claim_provenance=(
            {
                "claim_id": proposal.claim_id,
                "mapping_ids": [proposal.mapping_id],
                "document_id": "DOC-FULL-SCORE-VALIDITY",
                "source_url": "https://issuer.example/full-score-validity",
                "source_proxy_only": False,
                "directness": "DIRECT",
                "temporal_status": "CURRENT",
            },
        ),
        claim_eligibility_decisions=(
            {
                "eligibility_decision_id": "ELIG-FULL-SCORE-VALIDITY",
                "claim_id": proposal.claim_id,
                "component_scoring_eligibility": True,
            },
        ),
        accepted_current_claims=(
            {
                "claim_id": proposal.claim_id,
                "target_id": TARGET_ID,
                "accepted": True,
                "mapping_ids": [proposal.mapping_id],
                "economic_fact_key": "FACT-FULL-SCORE-VALIDITY",
            },
        ),
    )
    if validation.status != "IMPACT_CREDIT_CAP_PASS":
        raise ValueError("full score validity canary impact validation failed")
    return validation.impacts[0]


__all__ = ["audit_full_score_validity_v2"]
