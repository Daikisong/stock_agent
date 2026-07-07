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
        cls.case_inventory = json.loads(
            (cls.docs / "research_reverse_case_inventory.json").read_text(encoding="utf-8")
        )
        cls.plan = build_all_archetype_next_runtime_attempt_plan(
            status_matrix=cls.status,
            memory_cards=cls.cards,
            case_inventory=cls.case_inventory,
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
        self.assertGreater(self.plan["source_task_count"], self.plan["plan_row_count"])
        self.assertEqual(self.plan["source_task_count"], self.plan["seed_event_count"])

    def test_all_source_tasks_are_planner_input_only_not_score_input(self) -> None:
        self.assertTrue(self.plan["all_tasks_score_blocked_before_execution"])
        self.assertTrue(self.plan["all_tasks_require_llm_query_generation"])
        self.assertTrue(self.plan["all_tasks_have_no_hardcoded_queries"])
        self.assertTrue(self.plan["all_tasks_have_finite_budget"])
        self.assertTrue(self.plan["all_tasks_have_success_condition"])
        self.assertTrue(self.plan["all_tasks_have_expected_claim_schema"])
        self.assertTrue(self.plan["all_tasks_have_fallback_if_not_found"])
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
            self.assertIn("planner_failure_feedback", task)
            self.assertFalse(task["planner_failure_feedback"]["score_evidence_allowed_from_previous_rejected_claims"])
            self.assertFalse(task["planner_failure_feedback"]["score_evidence_allowed_from_previous_seed_failures"])
            self.assertIn("previous_seed_materialization_primary_failure_axis", task["planner_failure_feedback"])
            self.assertIn("previous_seed_materialization_top_failure_axes", task["planner_failure_feedback"])
            self.assertIn("accepted Evidence OS claim", task["success_condition"])
            self.assertIn(task["primitive_gap"], task["success_condition"])
            self.assertIn(
                task["fallback_if_not_found"],
                {"PENDING_SOURCE", "PENDING_MATERIAL_GAP", "SOURCE_REPAIR_REQUIRED", "TARGET_MATERIALIZATION_REQUIRED"},
            )
            schema = task["expected_claim_schema"]
            self.assertEqual(schema["schema_version"], "e2r_expected_runtime_parity_claim_v1")
            self.assertEqual(schema["archetype_id"], task["archetype_id"])
            self.assertEqual(schema["primitive_id"], task["primitive_gap"])
            self.assertEqual(schema["target_scope_status"], "DIRECT")
            self.assertEqual(schema["temporal_status"], "CURRENT_OR_AS_OF_VALID")
            self.assertEqual(schema["anchor_status"], "VERIFIED_SOURCE_ANCHOR")
            self.assertEqual(schema["mapping_status"], "ACCEPTED")
            self.assertTrue(schema["score_forbidden_until_claim_accepted"])
            self.assertIn("source_proxy_only", schema["forbidden_source_classes"])

    def test_seed_events_are_visible_to_census_v4_seed_runtime_audit(self) -> None:
        for event in self.plan["seed_events"][:10]:
            self.assertEqual(event["seed_role"], "planner_input_only")
            self.assertEqual(event["structured_payload"]["seed_role"], "planner_input_only")
            self.assertEqual(event["source_family"], "AllArchetypeRuntimeParityFollowUp")
            self.assertEqual(event["event_type"], "all_archetype_runtime_parity_follow_up_seed")
            self.assertIn("success_condition", event["structured_payload"])
            self.assertIn("expected_claim_schema", event["structured_payload"])
            self.assertIn("fallback_if_not_found", event["structured_payload"])
            self.assertEqual(
                event["structured_payload"]["expected_claim_schema"]["primitive_id"],
                event["structured_payload"]["primitive_gap"],
            )

    def test_attempt_types_reflect_current_runtime_failure_modes(self) -> None:
        self.assertEqual(self.by_prefix["C05"]["attempt_type"], "PROMOTED_SCORE_PATH_GAP_CLOSURE")
        self.assertEqual(self.by_prefix["C06"]["attempt_type"], "PROMOTED_SCORE_PATH_GAP_CLOSURE")
        self.assertEqual(self.by_prefix["C08"]["attempt_type"], "PROMOTED_SCORE_PATH_GAP_CLOSURE")
        self.assertEqual(self.by_prefix["C24"]["attempt_type"], "PLANNER_TO_SOURCE_TASK_MATERIALIZATION")
        self.assertEqual(self.by_prefix["C29"]["attempt_type"], "SOURCE_EXECUTION_REPAIR")

    def test_replay_only_archetypes_are_materialized_as_research_memory_target_candidates(self) -> None:
        expected_symbols = {
            "C08": "058470",
            "C15": "001390",
            "C17": "011170",
            "C28": "012510",
        }
        for prefix, expected_symbol in expected_symbols.items():
            row = self.by_prefix[prefix]
            self.assertEqual(row["target_symbol_mode"], "SYMBOL_SPECIFIC", prefix)
            self.assertEqual(row["target_symbols"], [expected_symbol], prefix)
            self.assertFalse(row["requires_target_materialization_before_scoring"], prefix)
            self.assertTrue(row["requires_current_source_confirmation_before_scoring"], prefix)
            self.assertFalse(row["score_allowed_before_execution"], prefix)
            self.assertEqual(row["target_materialization_candidates"], [], prefix)

        self.assertEqual(self.plan["target_symbol_mode_counts"]["SYMBOL_SPECIFIC"], 32)
        self.assertEqual(self.plan["target_symbol_mode_counts"]["ARCHETYPE_LEVEL_DISCOVERY"], 3)
        self.assertEqual(self.plan["target_materialization_required_task_count"], 9)

    def test_c01_to_c32_all_have_symbol_specific_next_attempts(self) -> None:
        unresolved_c_rows = [
            row
            for row in self.plan["plan_rows"]
            if row["archetype_prefix"].startswith("C")
            and row["requires_target_materialization_before_scoring"]
        ]
        self.assertEqual(unresolved_c_rows, [])

    def test_research_memory_candidates_remain_planner_inputs_not_score_evidence(self) -> None:
        symbol_specific_tasks = [
            task
            for task in self.plan["source_tasks"]
            if task["target_symbol_mode"] == "SYMBOL_SPECIFIC"
        ]
        self.assertEqual(len(symbol_specific_tasks), 96)
        for task in symbol_specific_tasks[:20]:
            self.assertIsNone(task["target_materialization_candidate"])
            self.assertTrue(task["symbol"])
            self.assertTrue(task["requires_current_source_confirmation_before_scoring"])
            self.assertFalse(task["requires_target_materialization_before_scoring"])
            self.assertFalse(task["score_allowed_before_execution"])
            self.assertIn("verify current, direct target-company evidence", task["query_intents"][0])

    def test_previous_claim_failure_feedback_is_carried_into_next_source_tasks(self) -> None:
        self.assertGreater(self.plan["source_route_repair_task_count"], 0)
        self.assertIn(
            "TIGHTEN_TARGET_ENTITY_FILTER_OR_RELATION_ADJUDICATION",
            self.plan["source_route_repair_hint_counts"],
        )
        self.assertIn(
            "REPLAN_SOURCE_TASK_TO_MATCH_PRIMITIVE_FAMILY",
            self.plan["source_route_repair_hint_counts"],
        )

        redteam_row = next(
            row
            for row in self.plan["plan_rows"]
            if row["archetype_id"] == "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM"
        )
        self.assertEqual(
            redteam_row["previous_claim_failure_primary_mode"],
            "TARGET_SCOPE_NOT_DIRECT",
        )
        self.assertEqual(
            redteam_row["previous_claim_failure_repair_hint"],
            "TIGHTEN_TARGET_ENTITY_FILTER_OR_RELATION_ADJUDICATION",
        )
        self.assertIn(
            "ASK_LLM_FOR_DIRECT_TARGET_COMPANY_SOURCE",
            redteam_row["source_route_repair_actions"],
        )

        redteam_task = next(
            task
            for task in self.plan["source_tasks"]
            if task["archetype_id"] == "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM"
        )
        self.assertTrue(redteam_task["source_route_repair_required"])
        self.assertIn(
            "direct target-company scope",
            " ".join(redteam_task["query_intents"]),
        )
        self.assertEqual(
            redteam_task["planner_failure_feedback"]["previous_claim_failure_primary_mode"],
            "TARGET_SCOPE_NOT_DIRECT",
        )
        self.assertFalse(
            redteam_task["planner_failure_feedback"]["score_evidence_allowed_from_previous_rejected_claims"]
        )

    def test_seed_materialization_failure_feedback_is_carried_into_next_source_tasks(self) -> None:
        self.assertGreater(self.plan["seed_materialization_repair_task_count"], 0)
        self.assertIn(
            "PRIMITIVE_GAP_UNSATISFIED",
            self.plan["seed_materialization_primary_failure_axis_counts"],
        )
        self.assertIn(
            "FIND_PRIMITIVE_SPECIFIC_CLAIM_NOT_GENERIC_CONTEXT",
            self.plan["seed_materialization_repair_hint_counts"],
        )

        c02_row = self.by_prefix["C02"]
        self.assertEqual(
            c02_row["previous_seed_materialization_primary_failure_axis"],
            "PRIMITIVE_GAP_UNSATISFIED",
        )
        self.assertEqual(
            c02_row["previous_seed_materialization_repair_hint"],
            "FIND_PRIMITIVE_SPECIFIC_CLAIM_NOT_GENERIC_CONTEXT",
        )
        self.assertTrue(c02_row["seed_materialization_repair_required"])
        self.assertIn(
            "ASK_LLM_FOR_PRIMITIVE_SPECIFIC_SOURCE_SECTION",
            c02_row["seed_materialization_repair_actions"],
        )

        c02_task = next(task for task in self.plan["source_tasks"] if task["archetype_id"] == c02_row["archetype_id"])
        self.assertIn(
            "generic disclosure, status check, or adjacent business context is not enough",
            " ".join(c02_task["query_intents"]),
        )
        self.assertEqual(
            c02_task["planner_failure_feedback"]["previous_seed_materialization_primary_failure_axis"],
            "PRIMITIVE_GAP_UNSATISFIED",
        )
        self.assertFalse(
            c02_task["planner_failure_feedback"]["score_evidence_allowed_from_previous_seed_failures"]
        )

    def test_signal_family_mismatch_feedback_reaches_seed_payload(self) -> None:
        mismatch_task = next(
            task
            for task in self.plan["source_tasks"]
            if task["archetype_id"] == "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW"
        )
        self.assertEqual(
            mismatch_task["previous_claim_failure_primary_mode"],
            "ROUTE_SIGNAL_FAMILY_MISMATCH",
        )
        self.assertIn(
            "ASK_LLM_TO_MATCH_SOURCE_FAMILY_TO_PRIMITIVE_FAMILY",
            mismatch_task["source_route_repair_actions"],
        )
        self.assertIn(
            "source task must match the primitive family",
            " ".join(mismatch_task["query_intents"]),
        )

        mismatch_seed = next(
            event
            for event in self.plan["seed_events"]
            if event["target_archetype"] == "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW"
        )
        self.assertIn("ROUTE_SIGNAL_FAMILY_MISMATCH", mismatch_seed["raw_reason_codes"])
        self.assertEqual(
            mismatch_seed["structured_payload"]["previous_claim_failure_repair_hint"],
            "REPLAN_SOURCE_TASK_TO_MATCH_PRIMITIVE_FAMILY",
        )
        self.assertTrue(mismatch_seed["structured_payload"]["source_route_repair_required"])


if __name__ == "__main__":
    unittest.main()
