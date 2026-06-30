import unittest

from e2r.census.census_ledger import evaluate_claim_reuse


class CensusClaimReuseLifecycleTests(unittest.TestCase):
    def test_current_claim_reused(self):
        result = evaluate_claim_reuse({"claim_id": "CLM-1", "symbol": "005930", "as_of_date": "2026-06-20", "lifecycle": "CURRENT"}, symbol="005930", as_of_date="2026-07-01")
        self.assertEqual(result.reuse_status, "REUSED_CURRENT")


if __name__ == "__main__":
    unittest.main()
