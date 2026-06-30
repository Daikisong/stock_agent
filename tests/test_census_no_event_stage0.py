import unittest

from e2r.census.baseline_scanner import BaselineScanner
from e2r.census.depth_policy import CensusDepthPolicyConfig, decide_depths
from e2r.census.stage_status_builder import build_stage_status
from tests.census_test_helpers import instrument


class CensusNoEventStage0Tests(unittest.TestCase):
    def test_no_current_event_becomes_stage0(self):
        inst = instrument()
        scan = BaselineScanner().scan(inst, as_of_date="2026-07-01")
        decision = decide_depths([inst], [scan], config=CensusDepthPolicyConfig(sector_sample_quota=0))[0]
        status = build_stage_status(instrument=inst, as_of_date="2026-07-01", scan=scan, depth_decision=decision)
        self.assertEqual(status.base_stage.value, "Stage0")
        self.assertEqual(status.score_valid_status.value, "NO_CURRENT_EVENT")


if __name__ == "__main__":
    unittest.main()
