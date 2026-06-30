import unittest

from e2r.production.cutover_v2 import _trigger_taxonomy


class MarketAnomalyNotScoreEvidenceTests(unittest.TestCase):
    def test_market_anomaly_policy_is_investigation_only(self):
        taxonomy = _trigger_taxonomy()
        market = [row for row in taxonomy["categories"] if row["trigger_category"] == "Market Anomaly Trigger"][0]
        self.assertEqual(market["score_eligibility_policy"], "investigation_only_never_score")


if __name__ == "__main__":
    unittest.main()
