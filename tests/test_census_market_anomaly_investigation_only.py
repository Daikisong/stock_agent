import unittest

from e2r.census.baseline_scanner import BaselineScanInputs, BaselineScanner
from e2r.census.depth_policy import CensusDepthPolicyConfig, decide_depths
from e2r.census.stage_status_builder import build_stage_status
from tests.census_test_helpers import instrument


class CensusMarketAnomalyInvestigationOnlyTests(unittest.TestCase):
    def test_market_anomaly_does_not_create_verified_score(self):
        inst = instrument()
        scan = BaselineScanner(BaselineScanInputs(price_anomaly_symbols={inst.symbol: 2})).scan(inst, as_of_date="2026-07-01")
        decision = decide_depths([inst], [scan], config=CensusDepthPolicyConfig(sector_sample_quota=0))[0]
        status = build_stage_status(instrument=inst, as_of_date="2026-07-01", scan=scan, depth_decision=decision)
        self.assertEqual(status.verified_score, None)
        self.assertEqual(status.base_stage.value, "Stage1")
        self.assertIn("INVESTIGATE", status.next_actions)


if __name__ == "__main__":
    unittest.main()
