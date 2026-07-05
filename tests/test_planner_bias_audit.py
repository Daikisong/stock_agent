import json
import unittest
from pathlib import Path


class PlannerBiasAuditTests(unittest.TestCase):
    def test_planner_bias_audit_uses_stable_goal4_filename(self) -> None:
        audit = json.loads(Path("docs/operational/planner_bias_and_archetype_routing_audit.json").read_text())
        self.assertEqual(audit["status"], "PLANNER_ARCHETYPE_ROUTING_BIAS_NOT_READY")
        self.assertEqual(audit["top1_archetype_counts"], {"C01": 2, "C05": 29, "C06": 2, "C29": 2})
        self.assertIn("planner_top1_c05_share_over_limit", audit["blockers"])
        self.assertIn("target_unknown_rows_promoted_after_planner", audit["blockers"])


if __name__ == "__main__":
    unittest.main()
