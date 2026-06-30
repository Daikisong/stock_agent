import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3MemoryHintNeverScoreTests(unittest.TestCase):
    def test_memory_hint_events_exist_but_do_not_score(self):
        hints = [row for row in census_v3_artifacts()["events"] if row["event_category"] == "ResearchMemoryHintEvent"]
        self.assertGreater(len(hints), 0)
        self.assertTrue(all(not row["score_evidence_allowed"] for row in hints))


if __name__ == "__main__":
    unittest.main()
