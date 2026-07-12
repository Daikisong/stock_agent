from __future__ import annotations

import unittest

from e2r.research_brain.scoring import (
    ClaimImpactProposal,
    ComponentAssessmentBuilder,
    ImpactValidator,
    ValidatedClaimImpact,
)
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)


class PartialBridgeNonzeroPolicyTests(unittest.TestCase):
    def test_partial_bridge_has_research_backed_nonzero_cap(self) -> None:
        proposal = ClaimImpactProposal(
            impact_id="IMPACT-PARTIAL",
            claim_id="CLM-PARTIAL",
            mapping_id="MAP-PARTIAL",
            target_id="000660",
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_id="shipment_or_revenue_mix",
            component_id="earnings_visibility",
            direction="SUPPORT",
            support_type="PARTIAL_BRIDGE",
            strength_band="MODERATE",
            completeness_band="PARTIAL",
            causal_distance="ONE_HOP",
            temporal_scope="CURRENT",
            source_family="ISSUER_OFFICIAL",
            evidence_family_id="DOC-PARTIAL",
            confidence=0.8,
            rationale="HBM revenue mix는 earnings visibility에 bounded bridge다.",
            unsupported_aspects=("고객별 확약 물량은 확인되지 않았다.",),
        )
        result = ImpactValidator().validate(
            impacts=(ValidatedClaimImpact(proposal, scope_validation={"status":"MECHANISM_SCOPE_PASS","scope_match":True,"scope":{"issuer_id":"000660","business_segment":"MEMORY","product_family":"HBM","economic_mechanism":"SHIPMENT_REVENUE_MIX"}}, eligibility_decision_id="ELIG-PARTIAL"),),
            claim_provenance=(
                {
                    "claim_id": "CLM-PARTIAL",
                    "mapping_ids": ["MAP-PARTIAL"],
                    "source_proxy_only": False,
                    "directness": "DIRECT",
                    "temporal_status": "CURRENT",
                },
            ),
            claim_eligibility_decisions=(
                {
                    "eligibility_decision_id": "ELIG-PARTIAL",
                    "claim_id": "CLM-PARTIAL",
                    "component_scoring_eligibility": True,
                },
            ),
        )
        self.assertEqual(result.status, "IMPACT_CREDIT_CAP_PASS")
        self.assertEqual(result.impacts[0].support_type_cap, 0.6)
        self.assertGreater(result.impacts[0].validated_credit_fraction, 0.0)

    def test_neutral_partial_bridge_survives_component_subcriterion_schema(self) -> None:
        proposal = ClaimImpactProposal(
            impact_id="IMPACT-NEUTRAL-PARTIAL",
            claim_id="CLM-NEUTRAL-PARTIAL",
            mapping_id="MAP-NEUTRAL-PARTIAL",
            target_id="000660",
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_id="shipment_or_revenue_mix",
            component_id="earnings_visibility",
            direction="NEUTRAL",
            support_type="PARTIAL_BRIDGE",
            strength_band="MODERATE",
            completeness_band="PARTIAL",
            causal_distance="ONE_HOP",
            temporal_scope="CURRENT",
            source_family="ISSUER_OFFICIAL",
            evidence_family_id="DOC-NEUTRAL-PARTIAL",
            confidence=0.8,
            rationale="부분적인 출하 증거는 bounded visibility bridge다.",
            unsupported_aspects=("고객별 확약 물량은 확인되지 않았다.",),
            question_family_id="shipment_mass_production_generation",
            component_subcriterion_id="C06_VIS_SHIPMENT_REVENUE_MIX",
        )
        validation = ImpactValidator().validate(
            impacts=(ValidatedClaimImpact(proposal, scope_validation={"status":"MECHANISM_SCOPE_PASS","scope_match":True,"scope":{"issuer_id":"000660","business_segment":"MEMORY","product_family":"HBM","economic_mechanism":"SHIPMENT_REVENUE_MIX"}}, eligibility_decision_id="ELIG-NEUTRAL-PARTIAL"),),
            claim_provenance=(
                {
                    "claim_id": proposal.claim_id,
                    "mapping_ids": [proposal.mapping_id],
                    "source_proxy_only": False,
                    "directness": "DIRECT",
                    "temporal_status": "CURRENT",
                },
            ),
            claim_eligibility_decisions=(
                {
                    "eligibility_decision_id": "ELIG-NEUTRAL-PARTIAL",
                    "claim_id": proposal.claim_id,
                    "component_scoring_eligibility": True,
                },
            ),
        )
        contract = load_archetype_scoring_contract(proposal.archetype_id)
        assessment = ComponentAssessmentBuilder().build(
            contract=contract,
            impacts=validation.impacts,
            terminal_evidence={
                component_id: {
                    "status": "VERIFIED_ABSENT_AFTER_SEARCH",
                    "search_exhaustion_proof": ["SEARCH-EXHAUSTED"],
                }
                for component_id in contract.component_weights
                if component_id != proposal.component_id
            },
        )

        row = next(
            item
            for item in assessment.assessments
            if item.component_id == proposal.component_id
        )
        self.assertEqual(assessment.audit["critical_count_sum"], 0)
        self.assertIn(proposal.impact_id, row.support_impact_ids)
        self.assertGreater(row.verified_points, 0.0)


if __name__ == "__main__":
    unittest.main()
