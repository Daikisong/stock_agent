import json
import unittest
from pathlib import Path


class NoC05OnlyMeaningfulPassTests(unittest.TestCase):
    def test_c05_dominated_promoted_rows_are_hard_fail(self) -> None:
        audit = json.loads(Path("docs/operational/meaningful_full_thesis_production_acceptance.json").read_text())
        self.assertEqual(audit["distinct_full_thesis_archetype_count"], 4)
        self.assertEqual(audit["c05_full_thesis_share"], 0.25)
        self.assertNotIn("distinct_full_thesis_archetype_count_below_3", audit["hard_fails"])
        self.assertNotIn("c05_share_above_50_percent", audit["hard_fails"])
        self.assertIn("required_positive_missing_rate_above_30_percent", audit["hard_fails"])


if __name__ == "__main__":
    unittest.main()
