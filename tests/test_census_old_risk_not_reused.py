import unittest

from e2r.census.census_ledger import evaluate_claim_reuse


class CensusOldRiskNotReusedTests(unittest.TestCase):
    def test_old_negative_risk_without_followup_not_reused(self):
        result = evaluate_claim_reuse({"claim_id": "RISK-1", "symbol": "005930", "as_of_date": "2020-01-01", "polarity": "NEGATIVE", "lifecycle": "CURRENT"}, symbol="005930", as_of_date="2026-07-01")
        self.assertEqual(result.reuse_status, "STALE_NEEDS_REFRESH")
        self.assertIn("followup", result.reason)


if __name__ == "__main__":
    unittest.main()
