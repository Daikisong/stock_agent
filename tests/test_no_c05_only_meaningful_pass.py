import json
import unittest
from pathlib import Path


class NoC05OnlyMeaningfulPassTests(unittest.TestCase):
    def test_partial_score_path_rows_are_still_hard_fail(self) -> None:
        audit = json.loads(Path("docs/operational/meaningful_full_thesis_production_acceptance.json").read_text())
        self.assertEqual(audit["distinct_full_thesis_archetype_count"], 1)
        self.assertEqual(audit["c05_full_thesis_share"], 0.0)
        self.assertEqual(audit["archetype_balanced_status"], "ARCHETYPE_BALANCED_FULL_THESIS_PASS_FALSE")
        self.assertIn("distinct_full_thesis_archetype_count_below_3", audit["hard_fails"])
        self.assertNotIn("c05_share_above_50_percent", audit["hard_fails"])
        self.assertIn("mandatory_archetype_full_thesis_missing", audit["hard_fails"])
        self.assertIn("required_positive_missing_any_promoted_row", audit["hard_fails"])
        self.assertIn("green_gap_any_promoted_row", audit["hard_fails"])
        self.assertIn("balanced_candidate_selection_not_pass", audit["hard_fails"])


if __name__ == "__main__":
    unittest.main()
