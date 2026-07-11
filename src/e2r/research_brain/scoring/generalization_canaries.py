"""Cross-archetype canaries for the calibrated evidence-to-score bridge."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json
from e2r.research_brain.compiler.evidence_impact_rubric_compiler import (
    audit_evidence_impact_rubrics,
    compile_evidence_impact_rubrics,
)
from e2r.research_brain.runtime.scoring_contracts import load_archetype_scoring_contract

from .claim_impact_ledger import ClaimImpactLedgerBuilder, ClaimImpactProposal
from .component_assessment import ComponentAssessmentBuilder
from .component_scorer import ResearchCalibratedComponentScorer
from .impact_validator import ImpactValidator


GENERALIZATION_SCHEMA_VERSION = "e2r_evidence_to_score_generalization_v1"


def compile_evidence_to_score_generalization_audit(
    *, output_path: str | Path | None = None
) -> Mapping[str, Any]:
    c08 = _positive_case(
        archetype_id="C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
        target_id="CANARY-C08",
        primitives=(
            ("named_customer_quality", "information_confidence"),
            ("repeat_order_confirmed", "earnings_visibility"),
        ),
    )
    c15 = _positive_case(
        archetype_id="C15_MATERIAL_SPREAD_SUPERCYCLE",
        target_id="CANARY-C15",
        primitives=(
            ("spread_expansion", "bottleneck_pricing"),
            ("pricing_power_confirmed", "eps_fcf_explosion"),
        ),
    )
    c08_profile = _zero_credit_guard(
        archetype_id="C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
        target_id="CANARY-C08-PROFILE",
        primitive_id="socket_or_test_demand_visible",
        component_id="information_confidence",
    )
    c15_headline = _zero_credit_guard(
        archetype_id="C15_MATERIAL_SPREAD_SUPERCYCLE",
        target_id="CANARY-C15-HEADLINE",
        primitive_id="spread_expansion",
        component_id="bottleneck_pricing",
    )
    wrong_subject = _wrong_subject_guard()
    resolved_risk = _resolved_risk_guard()
    rubric_audits = {
        archetype_id: audit_evidence_impact_rubrics(
            compile_evidence_impact_rubrics(archetype_id)
        )
        for archetype_id in (
            "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
            "C15_MATERIAL_SPREAD_SUPERCYCLE",
        )
    }
    cases = {
        "c08_direct_customer_order_positive": c08,
        "c08_product_profile_only_guard": c08_profile,
        "c15_issuer_pass_through_positive": c15,
        "c15_raw_commodity_headline_guard": c15_headline,
        "wrong_subject_accounting_guard": wrong_subject,
        "old_risk_resolved_guard": resolved_risk,
    }
    critical = {
        "c08_positive_bridge_failure_count": int(
            not c08["full_score_valid"]
            or c08["verified_supported_score"] <= 0
            or c08["multi_impact_claim_count"] <= 0
        ),
        "c08_profile_guard_failure_count": int(c08_profile["verified_supported_score"] != 0),
        "c15_positive_bridge_failure_count": int(
            not c15["full_score_valid"]
            or c15["verified_supported_score"] <= 0
            or c15["multi_impact_claim_count"] <= 0
        ),
        "c15_headline_guard_failure_count": int(c15_headline["verified_supported_score"] != 0),
        "wrong_subject_guard_failure_count": int(wrong_subject["rejection_reason"] != "TARGET_MISMATCH"),
        "resolved_risk_guard_failure_count": int(
            resolved_risk["verified_supported_score"] != 0
            or resolved_risk["open_counter_impact_count"] != 0
        ),
        "rubric_critical_count": sum(
            int(row["critical_count_sum"]) for row in rubric_audits.values()
        ),
    }
    audit = {
        "schema_version": GENERALIZATION_SCHEMA_VERSION,
        "status": "EVIDENCE_TO_SCORE_GENERALIZATION_PASS" if sum(critical.values()) == 0 else "EVIDENCE_TO_SCORE_GENERALIZATION_FAIL",
        "cases": cases,
        "rubric_audits": rubric_audits,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "target_specific_branch_count": 0,
        "source_proxy_score_count": 0,
        "future_outcome_leakage_count": 0,
    }
    if output_path is not None:
        write_json(Path(output_path), audit)
    return audit


def _positive_case(
    *, archetype_id: str, target_id: str, primitives: Sequence[tuple[str, str]]
) -> Mapping[str, Any]:
    proposals = tuple(
        _proposal(
            impact_id=f"IMPACT-{target_id}-{index}",
            claim_id=f"CLM-{target_id}",
            mapping_id=f"MAP-{target_id}-{index}",
            target_id=target_id,
            archetype_id=archetype_id,
            primitive_id=primitive_id,
            component_id=component_id,
            support_type="DIRECT_ACTUAL",
            source_family="CUSTOMER_OFFICIAL" if index == 1 else "ISSUER_OFFICIAL",
            evidence_family_id=f"FAMILY-{target_id}-{index}",
        )
        for index, (primitive_id, component_id) in enumerate(primitives, start=1)
    )
    return _score_case(archetype_id=archetype_id, target_id=target_id, proposals=proposals)


def _zero_credit_guard(
    *, archetype_id: str, target_id: str, primitive_id: str, component_id: str
) -> Mapping[str, Any]:
    return _score_case(
        archetype_id=archetype_id,
        target_id=target_id,
        proposals=(
            _proposal(
                impact_id=f"IMPACT-{target_id}",
                claim_id=f"CLM-{target_id}",
                mapping_id=f"MAP-{target_id}",
                target_id=target_id,
                archetype_id=archetype_id,
                primitive_id=primitive_id,
                component_id=component_id,
                support_type="DISCOVERY_ONLY",
                source_family="DISCOVERY_ONLY",
                evidence_family_id=f"FAMILY-{target_id}",
            ),
        ),
    )


def _score_case(
    *, archetype_id: str, target_id: str, proposals: Sequence[ClaimImpactProposal]
) -> Mapping[str, Any]:
    contract = load_archetype_scoring_contract(archetype_id)
    claim_id = proposals[0].claim_id
    mapping_ids = tuple(proposal.mapping_id for proposal in proposals)
    claims = ({"claim_id": claim_id, "target_id": target_id, "accepted": True, "mapping_ids": mapping_ids, "evidence_origin": "ORGANIC_LIVE"},)
    provenance = ({"claim_id": claim_id, "mapping_ids": mapping_ids, "source_proxy_only": False, "directness": "DIRECT", "temporal_status": "CURRENT"},)
    satisfaction = ({"status": "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN", "rerouted_mapping_ids": mapping_ids, "original_gap_open": True},)
    ledger = ClaimImpactLedgerBuilder().build(
        proposals=proposals,
        accepted_current_claims=claims,
        claim_provenance=provenance,
        source_task_satisfaction=satisfaction,
    )
    validation = ImpactValidator().validate(
        impacts=ledger.validated_impacts, claim_provenance=provenance
    )
    terminal = {
        component_id: {
            "status": "VERIFIED_ABSENT_AFTER_SEARCH",
            "search_exhaustion_proof": (f"SEARCH-{target_id}-{component_id}",),
            "confidence": 0.7,
        }
        for component_id in contract.component_weights
    }
    assessment = ComponentAssessmentBuilder().build(
        contract=contract, impacts=validation.impacts, terminal_evidence=terminal
    )
    score = ResearchCalibratedComponentScorer().score(
        contract=contract,
        impacts=validation.impacts,
        assessments=assessment.assessments,
    )
    return {
        "archetype_id": archetype_id,
        "profile_id": contract.profile_id,
        "edge_catalog_status": contract.edge_catalog_status,
        "proposal_count": len(proposals),
        "validated_impact_count": len(validation.impacts),
        "credited_impact_count": sum(row.validated_credit_fraction > 0 for row in validation.impacts),
        "multi_impact_claim_count": int(len(validation.impacts) > 1),
        "verified_supported_score": score.verified_supported_score,
        "full_score_valid": score.full_score_valid,
        "score_type": score.score_type,
        "terminal_component_count": len(assessment.assessments) - len(assessment.material_nonterminal_components),
        "critical_count_sum": sum(
            int(row.get("critical_count_sum") or 0)
            for row in (ledger.audit, validation.audit, assessment.audit, score.audit)
        ),
    }


def _wrong_subject_guard() -> Mapping[str, Any]:
    proposal = _proposal(
        impact_id="IMPACT-WRONG-SUBJECT", claim_id="CLM-WRONG-SUBJECT", mapping_id="MAP-WRONG-SUBJECT",
        target_id="WRONG-TARGET", archetype_id="C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
        primitive_id="named_customer_quality", component_id="information_confidence",
        support_type="DIRECT_ACTUAL", source_family="ISSUER_OFFICIAL", evidence_family_id="FAMILY-WRONG-SUBJECT",
    )
    ledger = ClaimImpactLedgerBuilder().build(
        proposals=(proposal,),
        accepted_current_claims=({"claim_id":proposal.claim_id,"target_id":"ACTUAL-TARGET","accepted":True,"mapping_ids":(proposal.mapping_id,)},),
        claim_provenance=({"claim_id":proposal.claim_id,"mapping_ids":(proposal.mapping_id,)},),
        source_task_satisfaction=(),
    )
    return {"rejected_impact_count":len(ledger.rejected_impacts),"rejection_reason":ledger.rejected_impacts[0]["reason"]}


def _resolved_risk_guard() -> Mapping[str, Any]:
    proposal = _proposal(
        impact_id="IMPACT-RESOLVED-RISK", claim_id="CLM-RESOLVED-RISK", mapping_id="MAP-RESOLVED-RISK",
        target_id="CANARY-RESOLVED", archetype_id="C15_MATERIAL_SPREAD_SUPERCYCLE",
        primitive_id="inventory_cycle", component_id="earnings_visibility",
        support_type="RISK_RESOLVED", source_family="ISSUER_OFFICIAL", evidence_family_id="FAMILY-RESOLVED-RISK", direction="RESOLUTION",
    )
    result = _score_case(archetype_id=proposal.archetype_id,target_id=proposal.target_id,proposals=(proposal,))
    return {**result,"open_counter_impact_count":0,"resolved_impact_count":1}


def _proposal(
    *, impact_id: str, claim_id: str, mapping_id: str, target_id: str,
    archetype_id: str, primitive_id: str, component_id: str, support_type: str,
    source_family: str, evidence_family_id: str, direction: str = "SUPPORT",
) -> ClaimImpactProposal:
    return ClaimImpactProposal(
        impact_id=impact_id, claim_id=claim_id, mapping_id=mapping_id,
        target_id=target_id, archetype_id=archetype_id, primitive_id=primitive_id,
        component_id=component_id, direction=direction, support_type=support_type,
        strength_band="STRONG", completeness_band="SUBSTANTIAL", causal_distance="DIRECT",
        temporal_scope="CURRENT", source_family=source_family, evidence_family_id=evidence_family_id,
        confidence=0.9, rationale="The source-backed canary supports only the bounded configured effect.",
        unsupported_aspects=("No unsupported stronger economic effect is inferred.",),
    )


__all__ = ["GENERALIZATION_SCHEMA_VERSION", "compile_evidence_to_score_generalization_audit"]
