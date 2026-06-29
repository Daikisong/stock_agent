import unittest
from pathlib import Path

from research_brain_v2_test_helpers import load_json


class ResearchBrainV3SectorCoverageRequirementsTests(unittest.TestCase):
    def test_candidate_event_count_or_gap_is_recorded(self):
        watchlist = load_json("docs/operational/research_brain_v3_daily_watchlist_sample.json")
        self.assertGreaterEqual(watchlist["summary"]["watchlist_item_count"], 30)
        shadow_text = Path("docs/operational/research_brain_v3_daily_shadow_report.md").read_text(encoding="utf-8")
        self.assertIn("candidate_event_count", shadow_text)


if __name__ == "__main__":
    unittest.main()
