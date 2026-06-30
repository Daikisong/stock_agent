import unittest

from e2r.census.census_event import build_census_assessment_event
from e2r.census.depth_policy import CensusDepthPolicyConfig, decide_depths
from e2r.census.baseline_scanner import BaselineScanner
from e2r.census.stage_status_builder import build_stage_status
from tests.census_test_helpers import instrument


class CensusAssessmentEventTests(unittest.TestCase):
    def test_census_assessment_event_alone_produces_no_score(self):
        inst = instrument()
        event = build_census_assessment_event(inst, as_of_date="2026-07-01")
        scan = BaselineScanner().scan(inst, as_of_date="2026-07-01")
        decision = decide_depths([inst], [scan], config=CensusDepthPolicyConfig(sector_sample_quota=0))[0]
        status = build_stage_status(instrument=inst, as_of_date="2026-07-01", scan=scan, depth_decision=decision)
        self.assertFalse(event.score_evidence_eligible)
        self.assertEqual(status.verified_score, None)
        self.assertEqual(status.score_contribution_count, 0)
        self.assertEqual(status.base_stage.value, "Stage0")
        self.assertEqual(status.investigation_status.value, "NO_CURRENT_CATALYST")


if __name__ == "__main__":
    unittest.main()
