import unittest
from pathlib import Path

from research_brain_v2_test_helpers import load_json


class ResearchBrainV2DailyWatchlistTests(unittest.TestCase):
    def test_daily_watchlist_sample_contains_required_state_fields(self):
        report = load_json("docs/operational/research_brain_v2_daily_watchlist_sample.json")
        self.assertGreater(report["summary"]["watchlist_item_count"], 0)
        row = report["rows"][0]
        for key in (
            "candidate_event_id",
            "event_type",
            "primary_archetype",
            "accepted_claim_ids",
            "green_blockers",
            "red_team_checks",
            "follow_up_tasks",
            "source_task_status_summary",
        ):
            self.assertIn(key, row)

    def test_daily_watchlist_files_are_written_to_output(self):
        self.assertTrue(Path("output/daily_watchlist/2026-06-29/e2r_daily_watchlist.json").exists())
        self.assertTrue(Path("output/daily_watchlist/2026-06-29/e2r_daily_watchlist.md").exists())


if __name__ == "__main__":
    unittest.main()
