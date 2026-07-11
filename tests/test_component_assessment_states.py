from __future__ import annotations

import unittest

from e2r.research_brain.runtime.scoring_contracts import load_archetype_scoring_contract
from e2r.research_brain.scoring import ClaimImpactProposal, ComponentAssessmentBuilder, ImpactValidator, ValidatedClaimImpact


def supported_impact():
    proposal=ClaimImpactProposal(impact_id="I1",claim_id="C1",mapping_id="M1",target_id="005930",archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",primitive_id="memory_price_increase_mentioned",component_id="bottleneck_pricing",direction="SUPPORT",support_type="DIRECT_ACTUAL",strength_band="STRONG",completeness_band="SUBSTANTIAL",causal_distance="DIRECT",temporal_scope="CURRENT",source_family="ISSUER_OFFICIAL",evidence_family_id="F1",confidence=.9,rationale="realized ASP supports pricing",unsupported_aspects=("allocation not shown",))
    return ImpactValidator().validate(impacts=(ValidatedClaimImpact(proposal),),claim_provenance=({"claim_id":"C1","mapping_ids":["M1"],"source_proxy_only":False,"directness":"DIRECT","temporal_status":"CURRENT"},)).impacts[0]


class ComponentAssessmentStateTests(unittest.TestCase):
    def setUp(self): self.contract=load_archetype_scoring_contract("C06_HBM_MEMORY_CUSTOMER_CAPACITY")

    def test_partial_component_score_is_preserved_while_other_components_unknown(self):
        result=ComponentAssessmentBuilder().build(contract=self.contract,impacts=(supported_impact(),))
        pricing=next(a for a in result.assessments if a.component_id=="bottleneck_pricing")
        self.assertEqual(pricing.status,"VERIFIED_PARTIAL_SUPPORT")
        self.assertEqual(pricing.verified_points,11.4)
        self.assertIn("earnings_visibility",result.material_nonterminal_components)

    def test_evaluated_absent_allows_terminal_full_thesis_assessment(self):
        evidence={key:{"status":"VERIFIED_ABSENT_AFTER_SEARCH","search_exhaustion_proof":["TASK-EXHAUSTED"]} for key in self.contract.component_weights if key!="bottleneck_pricing"}
        result=ComponentAssessmentBuilder().build(contract=self.contract,impacts=(supported_impact(),),terminal_evidence=evidence)
        self.assertEqual(result.material_nonterminal_components,())
        self.assertEqual(result.audit["terminal_component_count"],7)
        self.assertEqual(result.audit["verified_supported_points"],11.4)

    def test_unknown_and_provider_pending_block_finalization(self):
        unknown=ComponentAssessmentBuilder().build(contract=self.contract,impacts=())
        self.assertEqual(len(unknown.material_nonterminal_components),7)
        provider=ComponentAssessmentBuilder().build(contract=self.contract,impacts=(),terminal_evidence={"earnings_visibility":{"status":"PROVIDER_PENDING"}})
        self.assertIn("earnings_visibility",provider.material_nonterminal_components)

    def test_absence_without_search_proof_is_rejected(self):
        with self.assertRaisesRegex(ValueError,"search exhaustion proof"):
            ComponentAssessmentBuilder().build(contract=self.contract,impacts=(),terminal_evidence={"earnings_visibility":{"status":"VERIFIED_ABSENT_AFTER_SEARCH"}})


if __name__=="__main__": unittest.main()
