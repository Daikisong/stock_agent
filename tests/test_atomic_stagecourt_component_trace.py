from __future__ import annotations

import unittest

from e2r.research_brain.runtime.scoring_contracts import load_archetype_scoring_contract
from e2r.research_brain.scoring import AtomicStageCourtV2, ComponentAssessmentBuilder, ResearchCalibratedComponentScorer
from tests.test_component_assessment_states import supported_impact
from tests.full_score_validity_fixture import (
    passing_full_score_validity_evidence,
)


class AtomicStageCourtComponentTraceTests(unittest.TestCase):
    def setUp(self):
        self.contract=load_archetype_scoring_contract("C06_HBM_MEMORY_CUSTOMER_CAPACITY"); self.impact=supported_impact()

    def _score(self,terminal=False):
        evidence={}
        if terminal:evidence={key:{"status":"VERIFIED_ABSENT_AFTER_SEARCH","search_exhaustion_proof":["TASK-EXHAUSTED"]} for key in self.contract.component_weights if key!="bottleneck_pricing"}
        assessments=ComponentAssessmentBuilder().build(contract=self.contract,impacts=(self.impact,),terminal_evidence=evidence).assessments
        score=ResearchCalibratedComponentScorer().score(
            contract=self.contract,
            impacts=(self.impact,),
            assessments=assessments,
            validity_evidence=passing_full_score_validity_evidence(),
        )
        return assessments,score

    def test_pending_preserves_verified_score_and_does_not_finalize_stage(self):
        assessments,score=self._score(False)
        decision=AtomicStageCourtV2().decide(target_id="005930",as_of_date="2026-07-11",contract=self.contract,score=score,assessments=assessments,impacts=(self.impact,),accepted_claim_ids=("C1",))
        self.assertEqual(decision.canonical_stage,"0"); self.assertEqual(decision.decision_status,"PENDING_MATERIAL_COMPONENTS")
        self.assertEqual(decision.verified_supported_score,3.0); self.assertFalse(decision.full_score_valid)

    def test_final_score_runs_existing_deterministic_stage_classifier(self):
        assessments,score=self._score(True)
        decision=AtomicStageCourtV2().decide(target_id="005930",as_of_date="2026-07-11",contract=self.contract,score=score,assessments=assessments,impacts=(self.impact,),accepted_claim_ids=("C1",))
        self.assertEqual(decision.decision_status,"FINAL"); self.assertTrue(decision.full_score_valid)
        self.assertEqual(decision.score_type,"FULL_E2R_100"); self.assertIn(decision.canonical_stage,{"0","1","2","3-Green","3-Yellow","3-Red","4A","4B","4C","5"})
        self.assertEqual(decision.claim_impact_ids,("I1",)); self.assertEqual(len(decision.component_assessment_ids),7)

    def test_score_impact_lineage_mismatch_is_rejected(self):
        assessments,score=self._score(True)
        with self.assertRaisesRegex(ValueError,"unaccepted claim"):
            AtomicStageCourtV2().decide(target_id="005930",as_of_date="2026-07-11",contract=self.contract,score=score,assessments=assessments,impacts=(self.impact,),accepted_claim_ids=())

    def test_hard_break_requires_current_direct_open_counter(self):
        assessments,score=self._score(True)
        with self.assertRaisesRegex(ValueError,"current direct OPEN"):
            AtomicStageCourtV2().decide(target_id="005930",as_of_date="2026-07-11",contract=self.contract,score=score,assessments=assessments,impacts=(self.impact,),accepted_claim_ids=("C1",),risk_overlay={"hard_break_claim_ids":["RISK-1"],"current_direct_open_counter_claim_ids":[]})

    def test_accepted_claim_is_not_implicitly_a_high_quality_event(self):
        assessments,score=self._score(True)
        decision=AtomicStageCourtV2().decide(target_id="005930",as_of_date="2026-07-11",contract=self.contract,score=score,assessments=assessments,impacts=(self.impact,),accepted_claim_ids=("C1",))
        self.assertEqual(decision.stage_event_claim_ids,())

    def test_only_explicit_event_eligible_claim_enters_event_plane(self):
        assessments,score=self._score(True)
        decision=AtomicStageCourtV2().decide(target_id="005930",as_of_date="2026-07-11",contract=self.contract,score=score,assessments=assessments,impacts=(self.impact,),accepted_claim_ids=("C1",),claim_eligibility_decisions=({"claim_id":"C1","stage_event_eligibility":True,"event_quality_contract_status":"HIGH_QUALITY_EVENT_PASS"},))
        self.assertEqual(decision.stage_event_claim_ids,("C1",))
        self.assertEqual(decision.event_overlay["status"],"EVENT_OVERLAY_ACTIVE")

    def test_event_eligibility_boolean_without_quality_contract_is_not_event(self):
        assessments,score=self._score(True)
        decision=AtomicStageCourtV2().decide(target_id="005930",as_of_date="2026-07-11",contract=self.contract,score=score,assessments=assessments,impacts=(self.impact,),accepted_claim_ids=("C1",),claim_eligibility_decisions=({"claim_id":"C1","stage_event_eligibility":True},))
        self.assertEqual(decision.stage_event_claim_ids,())
        self.assertEqual(decision.event_overlay["status"],"NO_EVENT_OVERLAY")


if __name__=="__main__": unittest.main()
