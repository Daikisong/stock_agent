from __future__ import annotations

import unittest

from e2r.research_brain.runtime.scoring_contracts import load_archetype_scoring_contract
from e2r.research_brain.scoring import ComponentAssessmentBuilder, ResearchCalibratedComponentScorer
from tests.test_component_assessment_states import supported_impact


class ResearchCalibratedComponentScorerTests(unittest.TestCase):
    def setUp(self):
        self.contract=load_archetype_scoring_contract("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.impact=supported_impact()

    def test_verified_score_survives_with_provisional_interval(self):
        assessments=ComponentAssessmentBuilder().build(contract=self.contract,impacts=(self.impact,)).assessments
        score=ResearchCalibratedComponentScorer().score(contract=self.contract,impacts=(self.impact,),assessments=assessments)
        self.assertEqual(score.verified_supported_score,3.0)
        self.assertEqual((score.provisional_score_lower,score.provisional_score_upper),(3.0,84.0))
        self.assertFalse(score.full_score_valid); self.assertIsNone(score.full_e2r_score)
        self.assertEqual(score.score_type,"VERIFIED_COMPONENT_PARTIAL")

    def test_evaluated_absent_components_allow_full_e2r_score(self):
        evidence={key:{"status":"VERIFIED_ABSENT_AFTER_SEARCH","search_exhaustion_proof":["TASK-EXHAUSTED"]} for key in self.contract.component_weights if key!="bottleneck_pricing"}
        assessments=ComponentAssessmentBuilder().build(contract=self.contract,impacts=(self.impact,),terminal_evidence=evidence).assessments
        score=ResearchCalibratedComponentScorer().score(contract=self.contract,impacts=(self.impact,),assessments=assessments)
        self.assertTrue(score.full_score_valid); self.assertEqual(score.full_e2r_score,3.0)
        self.assertEqual(score.score_type,"FULL_E2R_100")
        self.assertEqual(sum(score.component_score_vector.values()),score.full_e2r_score)

    def test_component_vector_uses_c06_calibrated_maxima(self):
        assessments=ComponentAssessmentBuilder().build(contract=self.contract,impacts=(self.impact,)).assessments
        score=ResearchCalibratedComponentScorer().score(contract=self.contract,impacts=(self.impact,),assessments=assessments)
        self.assertEqual(score.profile_id,"e2r_2_2_archetype_weight_runtime")
        self.assertEqual(score.audit["critical_counts"]["balanced_point_score_count"],0)
        self.assertEqual(set(score.component_score_vector),set(self.contract.component_weights))


if __name__=="__main__": unittest.main()
