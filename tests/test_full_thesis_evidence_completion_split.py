import json
import unittest
from pathlib import Path


class FullThesisEvidenceCompletionSplitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = json.loads(Path("docs/operational/full_thesis_evidence_completion_audit_v2.json").read_text())

    def test_score_path_pass_is_not_meaningful_evidence_pass(self) -> None:
        self.assertEqual(self.audit["score_path_status"], "PRODUCTION_FULL_E2R_SCORE_PATH_PASS")
        self.assertEqual(self.audit["meaningful_evidence_status"], "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE")
        self.assertEqual(self.audit["green_ready_status"], "GREEN_READY_FULL_THESIS_PASS_FALSE")
        self.assertEqual(self.audit["archetype_balanced_status"], "ARCHETYPE_BALANCED_FULL_THESIS_PASS_FALSE")

    def test_required_positive_and_green_gaps_block_meaningful_pass(self) -> None:
        self.assertEqual(self.audit["full_thesis_row_count"], 6)
        self.assertEqual(self.audit["required_positive_missing_full_thesis_row_count"], 5)
        self.assertEqual(self.audit["green_gap_full_thesis_row_count"], 5)
        self.assertIn("REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS", self.audit["blockers"])
        self.assertIn("GREEN_GAP_ON_PROMOTED_ROWS", self.audit["blockers"])
        self.assertIn("MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING", self.audit["blockers"])


if __name__ == "__main__":
    unittest.main()
