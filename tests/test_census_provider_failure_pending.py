import unittest

from e2r.census.baseline_scanner import BaselineScanInputs, BaselineScanner
from e2r.census.depth_policy import CensusDepthPolicyConfig, decide_depths
from e2r.census.stage_status_builder import build_stage_status
from tests.census_test_helpers import instrument


class CensusProviderFailurePendingTests(unittest.TestCase):
    def test_provider_failure_becomes_pending_not_low_score(self):
        inst = instrument()
        scan = BaselineScanner(BaselineScanInputs(provider_failed_symbols={inst.symbol: ["KRX"]})).scan(inst, as_of_date="2026-07-01")
        decision = decide_depths([inst], [scan], config=CensusDepthPolicyConfig(sector_sample_quota=0))[0]
        status = build_stage_status(instrument=inst, as_of_date="2026-07-01", scan=scan, depth_decision=decision)
        self.assertEqual(status.census_status.value, "PENDING_PROVIDER")
        self.assertEqual(status.verified_score, None)
        self.assertNotIn(status.base_stage.value, {"Reject", "Red"})


if __name__ == "__main__":
    unittest.main()
