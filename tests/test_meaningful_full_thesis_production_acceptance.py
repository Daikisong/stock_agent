import json
import unittest
from pathlib import Path


class MeaningfulFullThesisProductionAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = json.loads(Path("docs/operational/meaningful_full_thesis_production_acceptance.json").read_text())

    def test_meaningful_acceptance_is_not_ready_for_incomplete_score_path_rows(self) -> None:
        self.assertEqual(self.audit["schema_version"], "e2r_meaningful_full_thesis_production_acceptance_v1")
        self.assertEqual(self.audit["score_path_status"], "PRODUCTION_FULL_E2R_SCORE_PATH_PASS")
        self.assertEqual(self.audit["meaningful_status"], "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE")
        self.assertEqual(self.audit["archetype_balanced_status"], "ARCHETYPE_BALANCED_FULL_THESIS_PASS")
        self.assertEqual(self.audit["candidate_selection_status"], "BALANCED_FULL_THESIS_SELECTION_NOT_READY")
        self.assertFalse(self.audit["meaningful_pass_allowed"])
        self.assertNotIn("c05_share_above_50_percent", self.audit["hard_fails"])
        self.assertIn("mandatory_archetype_full_thesis_missing", self.audit["hard_fails"])
        self.assertIn("required_positive_missing_any_promoted_row", self.audit["hard_fails"])
        self.assertIn("green_gap_any_promoted_row", self.audit["hard_fails"])
        self.assertIn("balanced_candidate_selection_not_pass", self.audit["hard_fails"])
        self.assertNotIn("planner_bias_audit_not_pass", self.audit["hard_fails"])

    def test_replay_does_not_leak_into_production_score(self) -> None:
        self.assertEqual(self.audit["research_replay_production_score_leak_count"], 0)
        self.assertGreater(self.audit["source_proxy_repair_task_count"], 0)


if __name__ == "__main__":
    unittest.main()
