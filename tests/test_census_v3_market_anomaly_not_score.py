import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3MarketAnomalyNotScoreTests(unittest.TestCase):
    def test_market_anomaly_to_score_count_zero(self):
        self.assertEqual(census_v3_artifacts()["leaf_audit"]["critical_counts"]["market_anomaly_to_score_count"], 0)


if __name__ == "__main__":
    unittest.main()
