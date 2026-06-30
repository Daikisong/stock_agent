import unittest

from e2r.census.baseline_scanner import BaselineScanResult
from e2r.census.depth_policy import CensusDepthPolicyConfig, decide_depths
from e2r.census.stage_status_builder import build_stage_status
from tests.census_test_helpers import instrument


class CensusNoClaimNoScoreTests(unittest.TestCase):
    def test_nonzero_score_without_claim_is_invalid(self):
        inst = instrument()
        scan = BaselineScanResult(symbol=inst.symbol, as_of_date="2026-07-01", recent_disclosure_count=1)
        decision = decide_depths([inst], [scan], config=CensusDepthPolicyConfig(sector_sample_quota=0))[0]
        status = build_stage_status(
            instrument=inst,
            as_of_date="2026-07-01",
            scan=scan,
            depth_decision=decision,
            accepted_claims=(),
            score_contributions=({"raw_points": 5.0, "support_claim_ids": []},),
        )
        self.assertEqual(status.score_valid_status.value, "INVALID_EVIDENCE")
        self.assertGreater(status.orphan_score_count, 0)


if __name__ == "__main__":
    unittest.main()
