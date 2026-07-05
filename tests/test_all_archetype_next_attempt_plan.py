import json
import unittest
from pathlib import Path

from e2r.census.all_archetype_next_attempt_planner import build_all_archetype_next_runtime_attempt_plan


class AllArchetypeNextAttemptPlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.docs = Path("docs/operational")
        cls.status = json.loads(
            (cls.docs / "all_archetype_runtime_status_matrix_2026-07-05.json").read_text(encoding="utf-8")
        )
        cls.cards = json.loads((cls.docs / "research_runtime_memory_cards_v2.json").read_text(encoding="utf-8"))
        cls.plan = build_all_archetype_next_runtime_attempt_plan(
            status_matrix=cls.status,
            memory_cards=cls.cards,
        )
        cls.by_prefix = {row["archetype_prefix"]: row for row in cls.plan["plan_rows"]}

    def test_every_unproven_archetype_has_next_attempt_row(self) -> None:
        unproven = [
            row
            for row in self.status["rows"]
            if row["runtime_parity_proof_status"] != "RUNTIME_PARITY_PROVEN"
        ]
        self.assertEqual(self.plan["schema_version"], "e2r_all_archetype_next_runtime_attempt_plan_v1")
        self.assertEqual(self.plan["plan_row_count"], len(unproven))
        self.assertEqual(self.plan["plan_row_count"], 36)
        self.assertGreater(self.plan["source_task_count"], self.plan["plan_row_count"])
        self.assertEqual(self.plan["source_task_count"], self.plan["seed_event_count"])

    def test_all_source_tasks_are_planner_input_only_not_score_input(self) -> None:
        self.assertTrue(self.plan["all_tasks_score_blocked_before_execution"])
        self.assertTrue(self.plan["all_tasks_require_llm_query_generation"])
        self.assertTrue(self.plan["all_tasks_have_no_hardcoded_queries"])
        self.assertTrue(self.plan["all_tasks_have_finite_budget"])
        for task in self.plan["source_tasks"]:
            self.assertFalse(task["score_allowed_before_execution"])
            self.assertFalse(task["stage_promotion_allowed_before_execution"])
            self.assertTrue(task["llm_query_required"])
            self.assertEqual(task["hardcoded_queries"], [])
            self.assertEqual(task["hardcoded_query_count"], 0)
            self.assertIsNotNone(task["max_queries"])
            self.assertIsNotNone(task["max_candidates"])
            self.assertIsNotNone(task["max_fetches"])
            self.assertIn("snippet_only_score", task["forbidden_source_classes"])
            self.assertIn("source_proxy_only", task["forbidden_source_classes"])

    def test_seed_events_are_visible_to_census_v4_seed_runtime_audit(self) -> None:
        for event in self.plan["seed_events"][:10]:
            self.assertEqual(event["seed_role"], "planner_input_only")
            self.assertEqual(event["structured_payload"]["seed_role"], "planner_input_only")
            self.assertEqual(event["source_family"], "AllArchetypeRuntimeParityFollowUp")
            self.assertEqual(event["event_type"], "all_archetype_runtime_parity_follow_up_seed")

    def test_attempt_types_reflect_current_runtime_failure_modes(self) -> None:
        self.assertEqual(self.by_prefix["C05"]["attempt_type"], "PROMOTED_SCORE_PATH_GAP_CLOSURE")
        self.assertEqual(self.by_prefix["C06"]["attempt_type"], "BLOCKED_CANDIDATE_GAP_CLOSURE")
        self.assertEqual(self.by_prefix["C29"]["attempt_type"], "SOURCE_EXECUTION_REPAIR")
        self.assertEqual(self.by_prefix["C08"]["attempt_type"], "REPLAY_TO_PRODUCTION_RUNTIME_ATTEMPT")
        self.assertEqual(self.by_prefix["C24"]["attempt_type"], "REPLAY_TO_PRODUCTION_RUNTIME_ATTEMPT")

    def test_replay_only_archetypes_are_archetype_level_discovery_not_fake_symbol_scores(self) -> None:
        for prefix in ("C08", "C15", "C17", "C24", "C28"):
            row = self.by_prefix[prefix]
            self.assertEqual(row["target_symbol_mode"], "ARCHETYPE_LEVEL_DISCOVERY", prefix)
            self.assertEqual(row["target_symbols"], [], prefix)
            self.assertFalse(row["score_allowed_before_execution"], prefix)


if __name__ == "__main__":
    unittest.main()
