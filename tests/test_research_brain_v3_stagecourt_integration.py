import unittest

from research_brain_v2_test_helpers import load_json


class ResearchBrainV3StageCourtIntegrationTests(unittest.TestCase):
    def test_stagecourt_trace_present_for_scored_items(self):
        report = load_json("docs/operational/research_brain_v3_daily_watchlist_sample.json")
        self.assertEqual(
            report["summary"]["stagecourt_trace_count"],
            report["summary"]["real_deterministic_scorer_used_count"],
        )
        for row in report["rows"]:
            if row["verified_score"] is not None:
                self.assertIn(row["base_stage"], {"0", "1", "2", "2-Actionable", "3-Yellow", "3-Green", "3-Red"})


if __name__ == "__main__":
    unittest.main()
