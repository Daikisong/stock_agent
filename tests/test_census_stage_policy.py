import unittest

from e2r.census.baseline_scanner import BaselineScanResult
from e2r.census.depth_policy import CensusDepthPolicyConfig, decide_depths
from e2r.census.stage_status_builder import build_stage_status
from tests.census_test_helpers import instrument


class CensusStagePolicyTests(unittest.TestCase):
    def test_accepted_claim_and_claim_backed_score_can_stage(self):
        inst = instrument()
        scan = BaselineScanResult(symbol=inst.symbol, as_of_date="2026-07-01", recent_disclosure_count=1, trigger_priority_score=20)
        decision = decide_depths([inst], [scan], config=CensusDepthPolicyConfig(sector_sample_quota=0))[0]
        status = build_stage_status(
            instrument=inst,
            as_of_date="2026-07-01",
            scan=scan,
            depth_decision=decision,
            accepted_claims=({"claim_id": "CLM-1", "symbol": inst.symbol},),
            score_contributions=({"raw_points": 50.0, "support_claim_ids": ["CLM-1"]},),
        )
        self.assertEqual(status.verified_score, 50.0)
        self.assertEqual(status.base_stage.value, "Stage2-Actionable")
        self.assertEqual(status.orphan_score_count, 0)


if __name__ == "__main__":
    unittest.main()
