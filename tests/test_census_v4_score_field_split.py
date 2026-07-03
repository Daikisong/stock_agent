import unittest

from tests.census_v4_test_helpers import by_symbol, census_v4_artifacts


class CensusV4ScoreFieldSplitTests(unittest.TestCase):
    def test_event_scores_are_not_verified_scores(self):
        artifacts = census_v4_artifacts()
        audit = artifacts["leaf_audit"]
        summary = artifacts["stage_summary"]
        self.assertEqual(audit["critical_counts"]["verified_score_not_full_e2r_count"], 0)
        self.assertGreater(audit["metrics"]["event_evidence_score_present_count"], 0)
        self.assertEqual(audit["metrics"]["full_e2r_verified_score_present_count"], 2)
        self.assertEqual(summary["verified_score_present_count"], 2)
        self.assertEqual(summary["full_e2r_verified_score_count"], 2)
        self.assertEqual(summary["full_thesis_stage_distribution"]["FULL_THESIS_NOT_RUN"], len(artifacts["stage_rows"]) - 2)
        for row in artifacts["stage_rows"]:
            if row["score_scale"] == "FULL_E2R_100":
                self.assertIsNotNone(row["verified_score"])
            else:
                self.assertIsNone(row["verified_score"])
            if row["event_evidence_score"] is not None:
                self.assertEqual(row["score_scale"], "EVENT_WEIGHTED_PARTIAL")

    def test_samsung_hynix_daily_event_is_separate_from_full_thesis(self):
        rows = census_v4_artifacts()["stage_rows"]
        for symbol in ("005930", "000660"):
            row = by_symbol(rows, symbol)
            self.assertIsNotNone(row["daily_event_evidence_score"])
            self.assertIsNone(row["event_evidence_score"])
            self.assertEqual(row["stage_scope"], "FULL_THESIS")
            self.assertEqual(row["score_scale"], "FULL_E2R_100")
            self.assertNotEqual(row["full_thesis_stage"], "FULL_THESIS_NOT_RUN")
            self.assertIsNotNone(row["full_thesis_verified_score"])
            self.assertGreater(len(row["daily_event_claim_ids"]), 0)
            self.assertGreater(len(row["full_thesis_accepted_claim_ids"]), 0)


if __name__ == "__main__":
    unittest.main()
