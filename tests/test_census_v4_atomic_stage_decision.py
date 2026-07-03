import unittest

from tests.census_v4_test_helpers import census_v4_artifacts


class CensusV4AtomicStageDecisionTests(unittest.TestCase):
    def test_leaf_audit_has_no_atomic_mismatch(self):
        audit = census_v4_artifacts()["leaf_audit"]
        self.assertEqual(audit["critical_counts"]["stage_trace_stage_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_trace_scope_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_trace_score_scope_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_trace_score_interval_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_trace_score_status_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_trace_claim_set_mismatch_count"], 0)
        self.assertEqual(audit["critical_counts"]["stage_trace_contribution_set_mismatch_count"], 0)

    def test_every_scored_row_points_to_atomic_decision(self):
        for row in census_v4_artifacts()["stage_rows"]:
            if row["score_scale"] != "NO_SCORE":
                self.assertTrue(row["atomic_stage_decision_id"])
                self.assertTrue(row["stagecourt_trace_id"])
                self.assertTrue(row["accepted_claim_ids"])
                self.assertTrue(row["score_contribution_ids"])

    def test_atomic_decision_carries_stage_and_score_scope(self):
        for row in census_v4_artifacts()["atomic_rows"]:
            self.assertIn(row["stage_scope"], {"CENSUS_EVENT_BOARD", "FULL_THESIS"})
            if row["stage_scope"] == "FULL_THESIS":
                self.assertEqual(row["score_scope"], "FULL_E2R_100")
            else:
                self.assertIn(row["score_scope"], {"NO_SCORE", "EVENT_WEIGHTED_PARTIAL"})


if __name__ == "__main__":
    unittest.main()
