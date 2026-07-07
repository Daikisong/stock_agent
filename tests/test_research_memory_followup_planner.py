import json
import unittest
from pathlib import Path


class ResearchMemoryFollowupPlannerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = json.loads(Path("docs/operational/research_memory_followup_task_audit.json").read_text(encoding="utf-8"))

    def test_every_blocked_candidate_has_memory_followup_task(self) -> None:
        self.assertEqual(self.audit["schema_version"], "e2r_research_memory_followup_task_audit_v1")
        self.assertEqual(self.audit["blocked_candidate_count"], 13)
        self.assertEqual(self.audit["task_count"], 38)
        self.assertEqual(
            self.audit["tasks_by_archetype"],
            {
                "C01_ORDER_BACKLOG_MARGIN_BRIDGE": 5,
                "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": 2,
                "C05_EPC_MEGA_CONTRACT_MARGIN_GAP": 3,
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY": 5,
                "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY": 2,
                "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE": 10,
                "C15_MATERIAL_SPREAD_SUPERCYCLE": 4,
                "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE": 4,
                "C31_POLICY_SUBSIDY_LEGISLATION_EVENT": 3,
            },
        )
        self.assertTrue(self.audit["all_tasks_use_memory_card_or_route"])

    def test_c06_followups_include_allocation_and_presold_routes(self) -> None:
        c06_tasks = [task for task in self.audit["tasks"] if task["archetype_id"].startswith("C06_")]
        primitives = {task["missing_primitive"] for task in c06_tasks}
        self.assertIn("customer_preorder_or_allocation", primitives)
        self.assertIn("hbm_capacity_constraint", primitives)
        self.assertIn("hbm_capacity_pre_sold", primitives)
        self.assertIn("medium_term_revision_visibility", primitives)
        self.assertIn("memory_price_increase_mentioned", primitives)
        for task in c06_tasks:
            self.assertIn("snippet_only_score", task["disallowed_sources"])
            self.assertTrue(task["source_route_priority"])
            self.assertEqual(task["fallback_if_not_found"], "PENDING_SOURCE")


if __name__ == "__main__":
    unittest.main()
