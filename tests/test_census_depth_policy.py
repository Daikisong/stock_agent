import unittest

from e2r.census.baseline_scanner import BaselineScanResult
from e2r.census.depth_policy import CensusDepthPolicyConfig, decide_depths
from tests.census_test_helpers import instrument


class CensusDepthPolicyTests(unittest.TestCase):
    def test_every_symbol_gets_depth_and_deep_is_bounded(self):
        instruments = [instrument(f"{idx:06d}", sector="S") for idx in range(1, 6)]
        scans = [
            BaselineScanResult(symbol=row.symbol, as_of_date="2026-07-01", recent_disclosure_count=5, trigger_priority_score=50)
            for row in instruments
        ]
        decisions = decide_depths(instruments, scans, config=CensusDepthPolicyConfig(max_deep_symbols=2, sector_sample_quota=0))
        self.assertEqual(len(decisions), 5)
        self.assertEqual(sum(1 for row in decisions if row.recommended_depth.value == "L3_RESEARCH_BRAIN_TRIAGE"), 2)


if __name__ == "__main__":
    unittest.main()
