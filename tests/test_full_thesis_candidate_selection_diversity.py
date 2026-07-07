import json
import unittest
from pathlib import Path


class FullThesisCandidateSelectionDiversityTests(unittest.TestCase):
    def test_candidate_selection_audit_requires_diverse_next_attempts(self) -> None:
        audit = json.loads(Path("docs/operational/full_thesis_candidate_selection_audit_v2.json").read_text())
        self.assertEqual(audit["status"], "BALANCED_FULL_THESIS_SELECTION_NOT_READY")
        selected_prefixes = [row["archetype_id"].split("_", 1)[0] for row in audit["next_required_archetype_attempts"][:7]]
        self.assertEqual(selected_prefixes[:3], ["C08", "C15", "C28"])
        self.assertTrue({"C02", "C04", "C07"}.issubset(set(selected_prefixes[3:7])))
        self.assertEqual(audit["current_full_thesis_row_count"], 6)
        self.assertEqual(audit["current_distinct_full_thesis_archetype_count"], 6)
        self.assertEqual(audit["current_c05_full_thesis_share"], 0.166667)
        self.assertIn("required_positive_missing_promoted_rows", audit["blockers"])


if __name__ == "__main__":
    unittest.main()
