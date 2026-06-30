import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3NoRecentCutoffStageDropTests(unittest.TestCase):
    def test_recent_cutoff_misuse_count_zero(self):
        self.assertEqual(census_v3_artifacts()["leaf_audit"]["critical_counts"]["recent_lookback_used_as_stage_cutoff_count"], 0)


if __name__ == "__main__":
    unittest.main()
