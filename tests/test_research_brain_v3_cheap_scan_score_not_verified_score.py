import unittest

from research_brain_v2_test_helpers import load_json


class ResearchBrainV3CheapScanScoreNotVerifiedTests(unittest.TestCase):
    def test_cheap_scan_not_used_as_verified_score(self):
        report = load_json("docs/operational/research_brain_v3_daily_watchlist_sample.json")
        self.assertEqual(report["summary"]["cheap_scan_total_score_as_verified_score_count"], 0)
        for row in report["rows"]:
            if row["verified_score"] is None:
                continue
            self.assertIn("trigger_priority_score", row)
            self.assertNotEqual(row["operator_notes"], "cheap_scan_total_score used as verified_score")


if __name__ == "__main__":
    unittest.main()
