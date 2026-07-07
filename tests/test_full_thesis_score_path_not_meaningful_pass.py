import json
import unittest
from pathlib import Path

from e2r.census.census_runner_v4 import _full_thesis_goal4_semantic_split


class FullThesisScorePathNotMeaningfulPassTests(unittest.TestCase):
    def test_legacy_full_thesis_production_pass_is_reclassified(self) -> None:
        old = json.loads(Path("docs/operational/census_mode_v4_full_thesis_production_audit.json").read_text())
        new = json.loads(Path("docs/operational/full_thesis_evidence_completion_audit_v2.json").read_text())
        self.assertEqual(old["status"], "PENDING_FULL_THESIS_PRODUCTION")
        self.assertEqual(new["score_path_status"], "PRODUCTION_FULL_E2R_SCORE_PATH_PASS")
        self.assertEqual(new["meaningful_evidence_status"], "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE")
        self.assertEqual(new["archetype_balanced_status"], "ARCHETYPE_BALANCED_FULL_THESIS_PASS_FALSE")

    def test_goal4_semantic_split_separates_score_path_from_meaningful_evidence(self) -> None:
        split = _full_thesis_goal4_semantic_split(
            {
                "production_mode_requested": True,
                "production_full_thesis_row_count": 7,
                "production_full_thesis_row_with_required_positive_missing_primitives_count": 7,
                "production_full_thesis_row_with_green_gap_primitives_count": 7,
                "production_green_stage_row_with_green_gap_count": 0,
                "completion_eligible": False,
                "verdict": "PENDING_FULL_THESIS_PRODUCTION",
            }
        )

        self.assertEqual(split["score_path_label"], "PRODUCTION_FULL_E2R_SCORE_PATH_PASS")
        self.assertEqual(split["meaningful_label"], "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE")
        self.assertTrue(split["production_full_e2r_score_path_pass"])
        self.assertFalse(split["meaningful_full_thesis_evidence_pass"])
        self.assertTrue(split["score_path_only_not_meaningful"])
        self.assertIn("production_score_path_is_not_meaningful_full_thesis_pass", split["blockers"])
        self.assertIn("required_positive_missing_on_promoted_rows", split["blockers"])
        self.assertIn("green_gap_on_promoted_rows", split["blockers"])


if __name__ == "__main__":
    unittest.main()
