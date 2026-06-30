import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3ResolvedOldRiskZeroTests(unittest.TestCase):
    def test_old_risk_without_current_open_does_not_score(self):
        self.assertEqual(census_v3_artifacts()["leaf_audit"]["critical_counts"]["old_risk_without_current_open_to_score_count"], 0)


if __name__ == "__main__":
    unittest.main()
