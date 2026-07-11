from __future__ import annotations

import unittest

from e2r.research_brain.scoring import ClaimImpactProposal, ImpactValidator, ValidatedClaimImpact

SCOPE={"status":"MECHANISM_SCOPE_PASS","scope_match":True,"scope":{"issuer_id":"005930","business_segment":"MEMORY","product_family":"HBM","economic_mechanism":"ACTUAL_EARNINGS_CONVERSION"}}

def impact(i: str, component: str, *, source="ISSUER_OFFICIAL", support="DIRECT_ACTUAL", primitive="memory_price_increase_mentioned", strength="STRONG", completeness="SUBSTANTIAL"):
    return ValidatedClaimImpact(ClaimImpactProposal(
        impact_id=i,claim_id="CLM-1",mapping_id="MAP-1",target_id="005930",archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",primitive_id=primitive,component_id=component,direction="SUPPORT",support_type=support,strength_band=strength,completeness_band=completeness,causal_distance="DIRECT",temporal_scope="CURRENT",source_family=source,evidence_family_id=i,confidence=.9,rationale="bounded direct impact",unsupported_aspects=("other components remain unsupported",)
    ),scope_validation=SCOPE,eligibility_decision_id="ELIG-1")


PROVENANCE=({"claim_id":"CLM-1","mapping_ids":["MAP-1"],"source_proxy_only":False,"directness":"DIRECT","temporal_status":"CURRENT"},)
ELIGIBILITY=({"eligibility_decision_id":"ELIG-1","claim_id":"CLM-1","component_scoring_eligibility":True},)


class ImpactCreditCapsTests(unittest.TestCase):
    def test_band_fraction_is_deterministic(self):
        result=ImpactValidator().validate(impacts=(impact("I1","bottleneck_pricing"),),claim_provenance=PROVENANCE,claim_eligibility_decisions=ELIGIBILITY)
        self.assertEqual(result.status,"IMPACT_CREDIT_CAP_PASS")
        self.assertEqual(result.impacts[0].raw_credit_fraction,.6)
        self.assertEqual(result.impacts[0].validated_credit_fraction,.6)

    def test_claim_total_credit_budget_scales_many_components(self):
        result=ImpactValidator().validate(impacts=(impact("I1","bottleneck_pricing",strength="VERY_STRONG",completeness="COMPLETE_FOR_PRIMITIVE"),impact("I2","eps_fcf_explosion",primitive="actual_earnings_conversion",strength="VERY_STRONG",completeness="COMPLETE_FOR_PRIMITIVE")),claim_provenance=PROVENANCE,claim_eligibility_decisions=ELIGIBILITY)
        self.assertAlmostEqual(sum(i.validated_credit_fraction for i in result.impacts),1.0,places=6)
        self.assertTrue(all(i.claim_budget_scaled for i in result.impacts))

    def test_discovery_only_cannot_receive_credit(self):
        result=ImpactValidator().validate(impacts=(impact("I1","bottleneck_pricing",source="DISCOVERY_ONLY",support="DISCOVERY_ONLY"),),claim_provenance=PROVENANCE,claim_eligibility_decisions=ELIGIBILITY)
        self.assertEqual(result.impacts[0].validated_credit_fraction,0.0)

    def test_rubric_edge_violation_is_rejected(self):
        result=ImpactValidator().validate(impacts=(impact("I1","market_mispricing"),),claim_provenance=PROVENANCE,claim_eligibility_decisions=ELIGIBILITY)
        self.assertEqual(result.status,"IMPACT_CREDIT_CAP_FAIL")
        self.assertEqual(result.audit["critical_counts"]["rubric_edge_violation_count"],1)


if __name__=="__main__": unittest.main()
