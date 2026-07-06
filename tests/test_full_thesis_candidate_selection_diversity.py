import json
import unittest
from pathlib import Path


class FullThesisCandidateSelectionDiversityTests(unittest.TestCase):
    def test_candidate_selection_audit_requires_diverse_next_attempts(self) -> None:
        audit = json.loads(Path("docs/operational/full_thesis_candidate_selection_audit_v2.json").read_text())
        self.assertEqual(audit["status"], "BALANCED_FULL_THESIS_SELECTION_NOT_READY")
        selected_prefixes = [row["archetype_id"].split("_", 1)[0] for row in audit["next_required_archetype_attempts"][:6]]
        self.assertEqual(selected_prefixes[:5], ["C08", "C15", "C17", "C24", "C28"])
        self.assertIn(selected_prefixes[5], {"C22", "R13"})
        self.assertEqual(audit["current_full_thesis_row_count"], 4)
        self.assertEqual(audit["current_distinct_full_thesis_archetype_count"], 4)
        self.assertEqual(audit["current_c05_full_thesis_share"], 0.25)
        self.assertIn("required_positive_missing_promoted_rows", audit["blockers"])


if __name__ == "__main__":
    unittest.main()
