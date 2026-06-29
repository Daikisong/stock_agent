import unittest

from research_brain_v2_test_helpers import load_json


class ResearchBrainV3RawEventRoutingTests(unittest.TestCase):
    def test_raw_fixture_acceptance_thresholds(self):
        matrix = load_json("docs/operational/research_brain_v3_raw_event_router_matrix.json")
        summary = matrix["summary"]
        self.assertGreaterEqual(summary["top1_accuracy"], 0.85)
        self.assertGreaterEqual(summary["top3_accuracy"], 0.98)
        self.assertTrue(summary["mandatory_six_top1_pass"])
        self.assertEqual(summary["r13_overroute_count"], 0)


if __name__ == "__main__":
    unittest.main()
