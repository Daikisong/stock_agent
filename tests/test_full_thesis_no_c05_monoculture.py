import json
import unittest
from pathlib import Path


class FullThesisNoC05MonocultureTests(unittest.TestCase):
    def test_c05_candidate_share_over_limit_is_blocker(self) -> None:
        audit = json.loads(Path("docs/operational/full_thesis_candidate_selection_audit_v2.json").read_text())
        self.assertEqual(audit["current_c05_full_thesis_share"], 0.666667)
        self.assertIn("c05_share_over_balanced_selection_limit", audit["blockers"])
        self.assertFalse(audit["meaningful_pass_allowed"])


if __name__ == "__main__":
    unittest.main()
