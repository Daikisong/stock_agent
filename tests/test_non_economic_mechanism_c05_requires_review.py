import json
import unittest
from pathlib import Path


class NonEconomicMechanismC05RequiresReviewTests(unittest.TestCase):
    def test_c05_context_bias_requires_review_before_meaningful_pass(self) -> None:
        audit = json.loads(Path("docs/operational/planner_bias_and_archetype_routing_audit.json").read_text())
        self.assertEqual(audit["c05_top1_count"], 29)
        self.assertGreater(audit["c05_top1_share"], 0.35)
        self.assertIn("source_primary_context_survived_into_promotion", audit["blockers"])


if __name__ == "__main__":
    unittest.main()
