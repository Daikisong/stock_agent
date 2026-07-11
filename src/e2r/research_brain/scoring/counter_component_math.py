"""Source-backed support/counter/resolution component-math audit."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)

from .claim_impact_ledger import ClaimImpactProposal, ValidatedClaimImpact
from .component_assessment import ComponentAssessmentBuilder
from .component_scorer import ResearchCalibratedComponentScorer
from .full_score_validity import FullScoreValidityEvidenceV2
from .impact_validator import ImpactValidator


ARCHETYPE_ID = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
TARGET_ID = "TARGET-C06-COUNTER-CANARY"


@dataclass(frozen=True)
class _ImpactSpec:
    impact_id: str
    claim_id: str
    mapping_id: str
    primitive_id: str
    component_id: str
    subcriterion_id: str
    question_family_id: str
    direction: str
    support_type: str
    strength_band: str = "STRONG"
    completeness_band: str = "SUBSTANTIAL"
    counter_claim_ids: tuple[str, ...] = ()


def audit_counter_component_math() -> Mapping[str, Any]:
    scenarios = {
        "open_qualification_counter": _run_scenario(
            (
                _qualification_support("OPEN-SUPPORT"),
                _qualification_counter("OPEN-COUNTER"),
            )
        ),
        "bounded_asp_counter": _run_scenario(
            (
                _asp_support("ASP-SUPPORT"),
                _asp_counter("ASP-COUNTER"),
            )
        ),
        "resolved_qualification_counter": _run_scenario(
            (
                _qualification_support("RESOLVED-SUPPORT"),
                _qualification_counter("RESOLVED-COUNTER"),
                _qualification_resolution(
                    "RESOLUTION",
                    counter_claim_id="CLM-RESOLVED-COUNTER",
                ),
            )
        ),
        "unlinked_resolution_keeps_counter_open": _run_scenario(
            (
                _qualification_support("UNLINKED-SUPPORT"),
                _qualification_counter("UNLINKED-COUNTER"),
                _qualification_resolution(
                    "UNLINKED-RESOLUTION",
                    counter_claim_id="CLM-DIFFERENT-COUNTER",
                ),
            )
        ),
        "capacity_support_and_scarcity_counter": _run_scenario(
            (
                _capacity_effect(
                    suffix="CAPACITY-SUPPORT",
                    component_id="capital_allocation",
                    subcriterion_id="C06_CAP_CAPACITY_RESPONSE",
                    direction="SUPPORT",
                    support_type="DIRECT_FORWARD",
                ),
                _capacity_effect(
                    suffix="SCARCITY-COUNTER",
                    component_id="bottleneck_pricing",
                    subcriterion_id="C06_BOT_SUPPLY_RESPONSE",
                    direction="COUNTER",
                    support_type="RISK_OPEN",
                ),
            )
        ),
        "same_component_distinct_subcriterion_counter": _run_scenario(
            (
                _capacity_constraint_support("SCARCITY-SUPPORT"),
                _capacity_effect(
                    suffix="SUPPLY-OPEN-COUNTER",
                    component_id="bottleneck_pricing",
                    subcriterion_id="C06_BOT_SUPPLY_RESPONSE",
                    direction="COUNTER",
                    support_type="RISK_OPEN",
                ),
            )
        ),
    }
    hard_names = (
        "counter_impact_ignored_count",
        "support_counter_same_component_unreconciled_count",
        "risk_open_zero_effect_count",
        "risk_resolved_still_penalized_count",
    )
    critical = {
        name: sum(
            int(row["assessment_audit"]["critical_counts"][name])
            for row in scenarios.values()
        )
        for name in hard_names
    }
    critical_sum = sum(critical.values())
    audit = {
        "schema_version": "e2r_counter_component_audit_v1",
        "status": (
            "COUNTER_COMPONENT_MATH_PASS"
            if critical_sum == 0
            else "COUNTER_COMPONENT_MATH_FAIL"
        ),
        "archetype_id": ARCHETYPE_ID,
        "scenario_count": len(scenarios),
        "scenarios": scenarios,
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
    }
    return json.loads(json.dumps(audit, ensure_ascii=False))


def _run_scenario(specs: Sequence[_ImpactSpec]) -> Mapping[str, Any]:
    claims: dict[str, Mapping[str, Any]] = {}
    provenance_by_claim: dict[str, Mapping[str, Any]] = {}
    decisions: dict[str, Mapping[str, Any]] = {}
    validated_rows = []
    for spec in specs:
        existing = claims.get(spec.claim_id)
        mapping_ids = list(existing.get("mapping_ids") or ()) if existing else []
        mapping_ids.append(spec.mapping_id)
        claims[spec.claim_id] = {
            "claim_id": spec.claim_id,
            "target_id": TARGET_ID,
            "accepted": True,
            "mapping_ids": list(dict.fromkeys(mapping_ids)),
            "economic_fact_key": f"FACT-{spec.claim_id}",
            "exact_quote": f"Current source-backed fact for {spec.claim_id}",
        }
        provenance_by_claim[spec.claim_id] = {
            "claim_id": spec.claim_id,
            "mapping_ids": claims[spec.claim_id]["mapping_ids"],
            "document_id": f"DOC-{spec.claim_id}",
            "source_url": f"https://issuer.example/{spec.claim_id.casefold()}",
            "content_sha256": (spec.claim_id.encode().hex() + "0" * 64)[:64],
            "source_proxy_only": False,
            "directness": "DIRECT",
            "temporal_status": "CURRENT",
        }
        eligibility_id = f"ELIG-{spec.claim_id}"
        decisions[eligibility_id] = {
            "eligibility_decision_id": eligibility_id,
            "claim_id": spec.claim_id,
            "component_scoring_eligibility": True,
        }
        proposal = ClaimImpactProposal(
            impact_id=f"IMPACT-{spec.impact_id}",
            claim_id=spec.claim_id,
            mapping_id=spec.mapping_id,
            target_id=TARGET_ID,
            archetype_id=ARCHETYPE_ID,
            primitive_id=spec.primitive_id,
            component_id=spec.component_id,
            direction=spec.direction,
            support_type=spec.support_type,
            strength_band=spec.strength_band,
            completeness_band=spec.completeness_band,
            causal_distance="DIRECT",
            temporal_scope="CURRENT",
            source_family="ISSUER_OFFICIAL",
            evidence_family_id=f"FAMILY-{spec.claim_id}",
            confidence=0.9,
            rationale="The current source supports only this bounded effect.",
            unsupported_aspects=("No stronger effect is inferred.",),
            counter_claim_ids=spec.counter_claim_ids,
            question_family_id=spec.question_family_id,
            component_subcriterion_id=spec.subcriterion_id,
            mechanism_scope_match=True,
        )
        validated_rows.append(
            ValidatedClaimImpact(
                proposal=proposal,
                scope_validation={
                    "status": "MECHANISM_SCOPE_PASS",
                    "scope_match": True,
                    "scope": {
                        "issuer_id": TARGET_ID,
                        "business_segment": "MEMORY",
                        "product_family": "HBM",
                        "economic_mechanism": _mechanism(spec),
                    },
                },
                eligibility_decision_id=eligibility_id,
            )
        )
    validation = ImpactValidator().validate(
        impacts=tuple(validated_rows),
        claim_provenance=tuple(provenance_by_claim.values()),
        claim_eligibility_decisions=tuple(decisions.values()),
        accepted_current_claims=tuple(claims.values()),
    )
    if validation.status != "IMPACT_CREDIT_CAP_PASS":
        raise ValueError("counter component audit impact validation failed")
    contract = load_archetype_scoring_contract(ARCHETYPE_ID)
    active_components = {spec.component_id for spec in specs}
    terminal_evidence = {
        component_id: {
            "status": "VERIFIED_ABSENT_AFTER_SEARCH",
            "search_exhaustion_proof": ["COUNTER-CANARY-EXHAUSTED"],
        }
        for component_id in contract.component_weights
        if component_id not in active_components
    }
    assessment = ComponentAssessmentBuilder().build(
        contract=contract,
        impacts=validation.impacts,
        terminal_evidence=terminal_evidence,
    )
    score = ResearchCalibratedComponentScorer().score(
        contract=contract,
        impacts=validation.impacts,
        assessments=assessment.assessments,
        validity_evidence=FullScoreValidityEvidenceV2(
            schema_totality_status="SCORING_SCHEMA_TOTALITY_PASS",
            scoring_schema_critical_count=0,
            silent_zero_default_count=0,
            positive_impact_zeroed_by_missing_cap_count=0,
            counter_impact_zeroed_by_missing_cap_count=0,
            mechanism_scope_failure_count=0,
            question_component_reconciliation_critical_count=0,
            unresolved_contradiction_count=sum(
                row.status == "CONTRADICTED_OPEN"
                for row in assessment.assessments
            ),
            pending_state_count=sum(
                row.status
                in {
                    "UNKNOWN_UNINVESTIGATED",
                    "SOURCE_PENDING",
                    "PROVIDER_PENDING",
                    "BUDGET_PENDING",
                }
                for row in assessment.assessments
            ),
            absence_without_adequacy_count=0,
            gold_critical_fact_miss_count=0,
            cross_business_question_closure_count=0,
            same_fact_duplicate_credit_count=0,
            same_document_duplicate_credit_count=0,
            source_audit_ids=("CONTROLLED-COUNTER-COMPONENT-CANARY",),
        ),
    )
    active_assessments = tuple(
        row
        for row in assessment.assessments
        if row.component_id in active_components
    )
    active_subcriteria = tuple(
        row
        for row in assessment.subcriterion_scores
        if row.support_impact_ids
        or row.counter_impact_ids
        or row.resolution_impact_ids
    )
    return {
        "validation_status": validation.status,
        "assessment_status": assessment.status,
        "full_score_valid": score.full_score_valid,
        "verified_supported_score": score.verified_supported_score,
        "material_nonterminal_components": list(
            assessment.material_nonterminal_components
        ),
        "active_component_assessments": [
            row.to_dict() for row in active_assessments
        ],
        "active_subcriterion_scores": [
            row.to_dict() for row in active_subcriteria
        ],
        "assessment_audit": assessment.audit,
    }


def _qualification_support(suffix: str) -> _ImpactSpec:
    return _ImpactSpec(
        impact_id=suffix,
        claim_id=f"CLM-{suffix}",
        mapping_id=f"MAP-{suffix}",
        primitive_id="qualification_state",
        component_id="earnings_visibility",
        subcriterion_id="C06_VIS_QUALIFICATION",
        question_family_id="qualification_pass_lag_reopen",
        direction="SUPPORT",
        support_type="DIRECT_ACTUAL",
    )


def _qualification_counter(suffix: str) -> _ImpactSpec:
    return _ImpactSpec(
        impact_id=suffix,
        claim_id=f"CLM-{suffix}",
        mapping_id=f"MAP-{suffix}",
        primitive_id="qualification_state",
        component_id="earnings_visibility",
        subcriterion_id="C06_VIS_QUALIFICATION",
        question_family_id="qualification_pass_lag_reopen",
        direction="COUNTER",
        support_type="RISK_OPEN",
    )


def _qualification_resolution(
    suffix: str, *, counter_claim_id: str
) -> _ImpactSpec:
    return _ImpactSpec(
        impact_id=suffix,
        claim_id=f"CLM-{suffix}",
        mapping_id=f"MAP-{suffix}",
        primitive_id="qualification_state",
        component_id="earnings_visibility",
        subcriterion_id="C06_VIS_QUALIFICATION",
        question_family_id="qualification_pass_lag_reopen",
        direction="RESOLUTION",
        support_type="RISK_RESOLVED",
        strength_band="VERY_STRONG",
        completeness_band="COMPLETE_FOR_PRIMITIVE",
        counter_claim_ids=(counter_claim_id,),
    )


def _asp_support(suffix: str) -> _ImpactSpec:
    return _ImpactSpec(
        impact_id=suffix,
        claim_id=f"CLM-{suffix}",
        mapping_id=f"MAP-{suffix}",
        primitive_id="memory_price_increase_mentioned",
        component_id="bottleneck_pricing",
        subcriterion_id="C06_BOT_REALIZED_ASP",
        question_family_id="asp_pricing_actual",
        direction="SUPPORT",
        support_type="DIRECT_ACTUAL",
    )


def _asp_counter(suffix: str) -> _ImpactSpec:
    return _ImpactSpec(
        impact_id=suffix,
        claim_id=f"CLM-{suffix}",
        mapping_id=f"MAP-{suffix}",
        primitive_id="memory_price_increase_mentioned",
        component_id="bottleneck_pricing",
        subcriterion_id="C06_BOT_REALIZED_ASP",
        question_family_id="asp_pricing_actual",
        direction="COUNTER",
        support_type="RISK_OPEN",
        strength_band="MODERATE",
    )


def _capacity_effect(
    *,
    suffix: str,
    component_id: str,
    subcriterion_id: str,
    direction: str,
    support_type: str,
) -> _ImpactSpec:
    return _ImpactSpec(
        impact_id=suffix,
        claim_id="CLM-CAPACITY-DUAL-EFFECT",
        mapping_id=f"MAP-{suffix}",
        primitive_id="capacity_supply_response",
        component_id=component_id,
        subcriterion_id=subcriterion_id,
        question_family_id="capex_supply_oversupply",
        direction=direction,
        support_type=support_type,
    )


def _capacity_constraint_support(suffix: str) -> _ImpactSpec:
    return _ImpactSpec(
        impact_id=suffix,
        claim_id=f"CLM-{suffix}",
        mapping_id=f"MAP-{suffix}",
        primitive_id="hbm_capacity_constraint",
        component_id="bottleneck_pricing",
        subcriterion_id="C06_BOT_CAPACITY_CONSTRAINT",
        question_family_id="capacity_constraint_presold_status",
        direction="SUPPORT",
        support_type="DIRECT_FORWARD",
    )


def _mechanism(spec: _ImpactSpec) -> str:
    if spec.primitive_id == "qualification_state":
        return "QUALIFICATION_EXECUTION"
    if spec.primitive_id == "memory_price_increase_mentioned":
        return "PRICING_POWER"
    return "SUPPLY_RESPONSE"


__all__ = ["audit_counter_component_math"]
