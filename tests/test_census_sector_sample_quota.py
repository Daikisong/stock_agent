import unittest

from e2r.census.baseline_scanner import BaselineScanResult
from e2r.census.depth_policy import CensusDepthPolicyConfig, decide_depths
from tests.census_test_helpers import instrument


class CensusSectorSampleQuotaTests(unittest.TestCase):
    def test_sector_sample_promotes_one_per_sector(self):
        instruments = [instrument("000001", sector="A"), instrument("000002", sector="B")]
        scans = [BaselineScanResult(symbol=row.symbol, as_of_date="2026-07-01") for row in instruments]
        decisions = decide_depths(instruments, scans, config=CensusDepthPolicyConfig(max_deep_symbols=0, sector_sample_quota=1))
        self.assertEqual(sum(1 for row in decisions if row.reason == "sector_random_audit_quota"), 2)


if __name__ == "__main__":
    unittest.main()
