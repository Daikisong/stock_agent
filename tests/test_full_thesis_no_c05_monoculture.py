import json
import unittest
from pathlib import Path


class FullThesisNoC05MonocultureTests(unittest.TestCase):
    def test_c05_share_is_not_current_blocker_but_diversity_gap_remains(self) -> None:
        audit = json.loads(Path("docs/operational/full_thesis_candidate_selection_audit_v2.json").read_text())
        self.assertEqual(audit["current_c05_full_thesis_share"], 0.0)
        self.assertEqual(audit["current_full_thesis_row_count"], 1)
        self.assertEqual(audit["current_distinct_full_thesis_archetype_count"], 1)
        self.assertNotIn("c05_share_over_balanced_selection_limit", audit["blockers"])
        self.assertIn("full_thesis_archetype_count_below_meaningful_minimum", audit["blockers"])
        self.assertIn("required_positive_missing_promoted_rows", audit["blockers"])
        self.assertFalse(audit["meaningful_pass_allowed"])


if __name__ == "__main__":
    unittest.main()
