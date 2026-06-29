import unittest

from research_brain_v2_test_helpers import load_json


class ResearchBrainV3WatchlistUsesRealScorerTests(unittest.TestCase):
    def test_verified_score_requires_claim_and_score_contribution(self):
        report = load_json("docs/operational/research_brain_v3_daily_watchlist_sample.json")
        self.assertGreaterEqual(report["summary"]["real_deterministic_scorer_used_count"], 3)
        for row in report["rows"]:
            if row["verified_score"] is None:
                continue
            self.assertTrue(row["accepted_claim_ids"])
            self.assertTrue(row["score_contribution_ids"])
            self.assertTrue(row["stage_court_trace"])


if __name__ == "__main__":
    unittest.main()
