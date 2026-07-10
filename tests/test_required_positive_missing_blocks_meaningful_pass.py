import json
import unittest
from pathlib import Path


class RequiredPositiveMissingBlocksMeaningfulPassTests(unittest.TestCase):
    def test_no_promoted_row_does_not_invent_required_positive_gap(self) -> None:
        audit = json.loads(Path("docs/operational/meaningful_full_thesis_production_acceptance.json").read_text())
        self.assertEqual(audit["required_positive_missing_row_count"], 0)
        self.assertEqual(audit["required_positive_missing_rate"], 0.0)
        self.assertNotIn("required_positive_missing_any_promoted_row", audit["hard_fails"])
        self.assertFalse(audit["meaningful_pass_allowed"])


if __name__ == "__main__":
    unittest.main()
