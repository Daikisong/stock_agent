import json
import unittest
from pathlib import Path


class NonEconomicMechanismC05RequiresReviewTests(unittest.TestCase):
    def test_c05_context_bias_is_not_current_planner_blocker(self) -> None:
        audit = json.loads(Path("docs/operational/planner_bias_and_archetype_routing_audit.json").read_text())
        self.assertEqual(audit["status"], "PLANNER_ARCHETYPE_ROUTING_BIAS_PASS")
        self.assertEqual(audit["c05_top1_count"], 3)
        self.assertLess(audit["c05_top1_share"], 0.1)
        self.assertEqual(audit["blockers"], [])


if __name__ == "__main__":
    unittest.main()
