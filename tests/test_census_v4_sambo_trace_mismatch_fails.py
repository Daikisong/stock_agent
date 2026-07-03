import unittest

from tests.census_v4_test_helpers import by_symbol, census_v4_artifacts


class CensusV4SamboTraceMismatchTests(unittest.TestCase):
    def test_sambo_representative_trace_matches_final_row(self):
        artifacts = census_v4_artifacts()
        row = by_symbol(artifacts["stage_rows"], "001470")
        atomic = {item["atomic_stage_decision_id"]: item for item in artifacts["atomic_rows"]}[row["atomic_stage_decision_id"]]
        self.assertEqual(row["base_stage"], "Stage2-Watch")
        self.assertEqual(row["canonical_stage"], "2")
        self.assertEqual(row["event_evidence_score"], 4.4)
        self.assertEqual(atomic["base_stage"], row["base_stage"])
        self.assertEqual(atomic["canonical_stage"], row["canonical_stage"])
        self.assertEqual(atomic["score_interval_lower"], row["score_interval_lower"])
        self.assertEqual(atomic["stagecourt_trace_id"], row["stagecourt_trace_id"])


if __name__ == "__main__":
    unittest.main()
