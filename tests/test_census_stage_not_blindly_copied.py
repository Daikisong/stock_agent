import unittest

from e2r.census.baseline_scanner import BaselineScanResult
from e2r.census.depth_policy import CensusDepthPolicyConfig, decide_depths
from e2r.census.stage_status_builder import build_stage_status
from tests.census_test_helpers import instrument


class CensusStageNotBlindlyCopiedTests(unittest.TestCase):
    def test_existing_stage_without_current_claim_does_not_copy_green(self):
        inst = instrument()
        scan = BaselineScanResult(symbol=inst.symbol, as_of_date="2026-07-01", existing_stage="Stage3-Green")
        decision = decide_depths([inst], [scan], config=CensusDepthPolicyConfig(sector_sample_quota=0))[0]
        status = build_stage_status(instrument=inst, as_of_date="2026-07-01", scan=scan, depth_decision=decision)
        self.assertNotEqual(status.base_stage.value, "Stage3-Green")


if __name__ == "__main__":
    unittest.main()
