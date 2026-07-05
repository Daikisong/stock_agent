import json
import unittest
from pathlib import Path


class RequiredPositiveMissingBlocksMeaningfulPassTests(unittest.TestCase):
    def test_required_positive_missing_rate_above_threshold_blocks_meaningful(self) -> None:
        audit = json.loads(Path("docs/operational/meaningful_full_thesis_production_acceptance.json").read_text())
        self.assertEqual(audit["required_positive_missing_rate"], 1.0)
        self.assertIn("required_positive_missing_rate_above_30_percent", audit["hard_fails"])
        self.assertFalse(audit["meaningful_pass_allowed"])


if __name__ == "__main__":
    unittest.main()
