import json
import unittest
from pathlib import Path


class PlannerBiasAuditTests(unittest.TestCase):
    def test_planner_bias_audit_uses_stable_goal4_filename(self) -> None:
        audit = json.loads(Path("docs/operational/planner_bias_and_archetype_routing_audit.json").read_text())
        self.assertEqual(audit["status"], "PLANNER_ARCHETYPE_ROUTING_BIAS_PASS")
        self.assertEqual(audit["top1_archetype_counts"]["C05"], 5)
        self.assertEqual(audit["top1_archetype_counts"]["C29"], 5)
        self.assertEqual(audit["top1_archetype_counts"]["C06"], 3)
        self.assertEqual(audit["distinct_top1_archetype_count"], 32)
        self.assertLess(audit["c05_top1_share"], 0.1)
        self.assertEqual(audit["blockers"], [])


if __name__ == "__main__":
    unittest.main()
