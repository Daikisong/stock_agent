import unittest

from research_brain_v2_test_helpers import load_json


class ResearchBrainV3FrozenDailyRunsTests(unittest.TestCase):
    def test_five_day_frozen_runs_are_stable(self):
        report = load_json("docs/operational/research_brain_v3_frozen_daily_runs.json")
        self.assertEqual(report["summary"]["frozen_daily_run_count"], 5)
        self.assertEqual(report["summary"]["max_repeat_variance_count"], 0)
        self.assertTrue(report["summary"]["no_score_stage_variance"])


if __name__ == "__main__":
    unittest.main()
