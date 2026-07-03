import unittest

from tests.census_v4_test_helpers import by_symbol, census_v4_artifacts


class CensusV4EventSeparationTests(unittest.TestCase):
    def test_assessment_event_is_not_candidate_or_score_evidence(self):
        artifacts = census_v4_artifacts()
        audit = artifacts["leaf_audit"]
        for key in (
            "missing_census_assessment_event_id_count",
            "assessment_event_score_evidence_allowed_count",
            "assessment_event_used_as_score_evidence_count",
            "candidate_event_ids_contain_assessment_event_count",
            "assessment_only_nonzero_score_count",
            "event_without_accepted_claim_nonzero_score_count",
            "score_contribution_without_accepted_claim_support_count",
            "no_current_catalyst_with_candidate_event_count",
            "score_eligible_candidate_without_accepted_claim_count",
            "atomic_candidate_event_is_assessment_count",
            "atomic_candidate_event_not_in_symbol_candidate_events_count",
        ):
            self.assertEqual(audit["critical_counts"][key], 0, key)

        for row in artifacts["stage_rows"]:
            self.assertTrue(row["census_assessment_event_id"].startswith("CAE-"))
            self.assertIs(row["census_assessment_event_score_evidence_allowed"], False)
            self.assertNotIn(row["census_assessment_event_id"], row["candidate_event_ids"])

    def test_atomic_decision_candidate_event_belongs_to_symbol_candidate_events(self):
        artifacts = census_v4_artifacts()
        stage_by_symbol = {row["symbol"]: row for row in artifacts["stage_rows"]}
        for row in artifacts["atomic_rows"]:
            event_id = row.get("candidate_event_id")
            if not event_id:
                continue
            stage = stage_by_symbol[row["symbol"]]
            self.assertNotEqual(event_id, stage["census_assessment_event_id"])
            self.assertIn(event_id, stage["candidate_event_ids"])

    def test_stage0_rows_are_assessment_only_no_current_catalyst(self):
        rows = census_v4_artifacts()["stage_rows"]
        stage0_rows = [row for row in rows if row["base_stage"] == "Stage0"]
        self.assertGreater(len(stage0_rows), 3000)
        for row in stage0_rows:
            self.assertEqual(row["candidate_event_scope"], "ASSESSMENT_ONLY")
            self.assertEqual(row["candidate_event_count"], 0)
            self.assertEqual(row["score_scale"], "NO_SCORE")
            self.assertIsNone(row["event_evidence_score"])
            self.assertEqual(row["stage_signal"], "NO_CURRENT_CATALYST")

    def test_samsung_hynix_keep_daily_candidate_events_separate_from_full_thesis(self):
        rows = census_v4_artifacts()["stage_rows"]
        for symbol in ("005930", "000660"):
            row = by_symbol(rows, symbol)
            self.assertEqual(row["candidate_event_scope"], "CANDIDATE_EVENTS_PRESENT")
            self.assertGreater(row["candidate_event_count"], 0)
            self.assertGreater(row["score_eligible_candidate_event_count"], 0)
            self.assertGreater(row["investigation_only_candidate_event_count"], 0)
            self.assertEqual(row["stage_scope"], "FULL_THESIS")
            self.assertEqual(row["score_scale"], "FULL_E2R_100")
            self.assertNotEqual(row["full_thesis_stage"], "FULL_THESIS_NOT_RUN")
            self.assertIsNotNone(row["full_e2r_verified_score"])
            self.assertIsNone(row["event_evidence_score"])
            self.assertIsNotNone(row["daily_event_evidence_score"])

    def test_blocked_contract_noise_keeps_candidate_but_not_score(self):
        rows = census_v4_artifacts()["stage_rows"]
        for symbol in ("473980", "043260"):
            row = by_symbol(rows, symbol)
            self.assertEqual(row["candidate_event_scope"], "CANDIDATE_EVENTS_PRESENT")
            self.assertGreater(row["candidate_event_count"], 0)
            self.assertGreater(row["score_eligible_candidate_event_count"], 0)
            self.assertEqual(row["semantic_guard_status"], "BLOCKED")
            self.assertEqual(row["score_scale"], "NO_SCORE")
            self.assertEqual(row["accepted_claim_ids"], [])
            self.assertGreater(len(row["blocked_claim_ids"]), 0)


if __name__ == "__main__":
    unittest.main()
