import unittest

from e2r.census.watchlist_seed_exporter import export_watchlist_seed


class CensusWatchlistSeedExportTests(unittest.TestCase):
    def test_exports_only_trackable_seed_without_recommendation_language(self):
        seed = export_watchlist_seed(
            [
                {"symbol": "005930", "company_name": "삼성전자", "base_stage": "Stage2-Actionable", "score_valid_status": "FINAL", "next_actions": ["DAILY_TRIGGER_TRACK"]},
                {"symbol": "000001", "company_name": "무사건", "base_stage": "Stage0", "score_valid_status": "NO_CURRENT_EVENT", "next_actions": ["IGNORE"]},
            ],
            as_of_date="2026-07-01",
        )
        self.assertEqual(seed["seed_count"], 1)
        self.assertNotIn("매수", str(seed))
        self.assertNotIn("매도", str(seed))


if __name__ == "__main__":
    unittest.main()
