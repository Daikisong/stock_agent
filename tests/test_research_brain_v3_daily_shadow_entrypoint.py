import unittest
from pathlib import Path

from research_brain_v2_test_helpers import load_json


class ResearchBrainV3DailyShadowEntrypointTests(unittest.TestCase):
    def test_entrypoint_outputs_exist(self):
        self.assertTrue(Path("src/e2r/cli/run_research_brain_v3_daily_shadow.py").exists())
        self.assertTrue(Path("docs/operational/research_brain_v3_daily_shadow_report.md").exists())
        self.assertTrue(Path("output/daily_watchlist/2026-06-29/e2r_daily_watchlist.json").exists())
        report = load_json("docs/operational/research_brain_v3_daily_watchlist_sample.json")
        self.assertGreaterEqual(report["summary"]["watchlist_item_count"], 30)


if __name__ == "__main__":
    unittest.main()
