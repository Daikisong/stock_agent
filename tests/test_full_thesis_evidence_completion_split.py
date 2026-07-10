import json
import unittest
from pathlib import Path


class FullThesisEvidenceCompletionSplitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = json.loads(Path("docs/operational/full_thesis_evidence_completion_audit_v2.json").read_text())

    def test_score_path_stays_pending_without_a_full_thesis_row(self) -> None:
        self.assertEqual(self.audit["score_path_status"], "PRODUCTION_FULL_E2R_SCORE_PATH_PENDING")
        self.assertEqual(self.audit["meaningful_evidence_status"], "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE")
        self.assertEqual(self.audit["green_ready_status"], "GREEN_READY_FULL_THESIS_PASS_FALSE")
        self.assertEqual(self.audit["archetype_balanced_status"], "ARCHETYPE_BALANCED_FULL_THESIS_PASS_FALSE")

    def test_zero_promoted_rows_do_not_invent_required_or_green_gaps(self) -> None:
        self.assertEqual(self.audit["full_thesis_row_count"], 0)
        self.assertEqual(self.audit["required_positive_missing_full_thesis_row_count"], 0)
        self.assertEqual(self.audit["green_gap_full_thesis_row_count"], 0)
        self.assertIn("FULL_THESIS_ARCHETYPE_DIVERSITY_BELOW_MINIMUM", self.audit["blockers"])
        self.assertNotIn("REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS", self.audit["blockers"])
        self.assertNotIn("GREEN_GAP_ON_PROMOTED_ROWS", self.audit["blockers"])
        self.assertIn("MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING", self.audit["blockers"])


if __name__ == "__main__":
    unittest.main()
