from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime import (
    INVESTIGATION_ACTION_OUTPUT_SCHEMA,
    ConstraintDimension,
    InvestigationFailureReason,
    SystemicClusterStatus,
    build_codex_investigation_planner_provider,
)


class E2RReconstructionPhase10AcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.acceptance = json.loads(
            (cls.repo_root / "e2r_reconstruction_phase10_acceptance.json").read_text(
                encoding="utf-8"
            )
        )

    def test_status_is_phase_scoped_and_not_runtime_ready(self) -> None:
        self.assertEqual(self.acceptance["phase"], 10)
        self.assertEqual(
            self.acceptance["status"],
            "ADAPTIVE_EVIDENCE_CLOSURE_PASS",
        )
        self.assertFalse(self.acceptance["production_runtime_ready"])
        self.assertEqual(INVESTIGATION_ACTION_OUTPUT_SCHEMA["type"], "object")
        self.assertEqual(SystemicClusterStatus.OPEN.value, "OPEN")
        self.assertTrue(callable(build_codex_investigation_planner_provider))

    def test_all_failure_reasons_and_constraint_dimensions_are_frozen(self) -> None:
        taxonomy = self.acceptance["failure_taxonomy"]
        self.assertEqual(
            set(taxonomy),
            {reason.value for reason in InvestigationFailureReason},
        )
        self.assertTrue(all(taxonomy.values()))
        valid_dimensions = {item.value for item in ConstraintDimension}
        transitions = self.acceptance["failure_transition_dimensions"]
        self.assertEqual(set(transitions), set(taxonomy))
        for reason, dimensions in transitions.items():
            self.assertTrue(dimensions, reason)
            self.assertTrue(set(dimensions).issubset(valid_dimensions), reason)
            self.assertIn("QUERY", dimensions, reason)

    def test_query_generation_has_no_deterministic_fallback(self) -> None:
        policy = self.acceptance["query_policy"]
        self.assertTrue(policy["llm_generates_literal_query"])
        self.assertFalse(policy["deterministic_query_synthesis"])
        self.assertTrue(policy["no_deterministic_fallback_after_retry"])
        self.assertTrue(policy["executed_query_duplicate_rejected"])
        self.assertTrue(policy["rejected_query_duplicate_rejected"])
        self.assertTrue(policy["previous_round_query_duplicate_rejected"])
        self.assertTrue(policy["validation_feedback_returned_to_llm"])

    def test_adaptive_audit_has_zero_critical_gaps_and_frozen_hash(self) -> None:
        audit = self.acceptance["adaptive_investigation_audit"]
        self.assertEqual(audit["status"], "ADAPTIVE_EVIDENCE_CLOSURE_PASS")
        self.assertEqual(audit["result_count"], 10)
        self.assertEqual(audit["planned_action_count"], 9)
        self.assertEqual(audit["rerouted_feedback_action_count"], 1)
        self.assertEqual(audit["critical_counts"]["unknown_task_identity"], 0)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(all(value == 0 for value in audit["critical_counts"].values()))
        self.assertEqual(
            audit["result_hash"],
            "53f997ca1e88e4836e612683854ece9b9c14386b7495c8fce48e22033850fd5a",
        )
        self.assertFalse(audit["production_runtime_ready"])

    def test_pending_and_material_gap_contract_never_finalize_score(self) -> None:
        runtime = self.acceptance["runtime_contract"]
        self.assertTrue(runtime["round_failure_action_leaf_identity_enforced"])
        self.assertTrue(runtime["round_limit_becomes_pending"])
        self.assertTrue(runtime["budget_exhaustion_becomes_pending"])
        self.assertTrue(runtime["cumulative_budget_underreport_rejected"])
        self.assertTrue(runtime["provider_failure_becomes_pending"])
        self.assertTrue(runtime["provider_exception_preserves_provider_trace"])
        self.assertTrue(runtime["provider_failed_official_route_is_excluded"])
        self.assertTrue(runtime["preferred_and_excluded_sources_are_disjoint"])
        self.assertTrue(runtime["source_dimension_requires_actual_new_route"])
        self.assertTrue(runtime["future_document_time_constraint_rejected"])
        self.assertTrue(runtime["stale_only_requires_explicit_reporting_period"])
        self.assertTrue(runtime["llm_abstention_becomes_pending"])
        self.assertTrue(runtime["llm_abstention_preserves_provider_trace"])
        self.assertTrue(runtime["canonical_codex_provider_builder_available"])
        self.assertTrue(runtime["canonical_runtime_exports_available"])
        self.assertTrue(runtime["test_mode_requires_boolean_identity"])
        self.assertTrue(runtime["unresolved_material_gap_score_valid_false"])
        self.assertTrue(
            runtime["unresolved_material_gap_score_finalization_allowed_false"]
        )
        self.assertTrue(
            runtime["resolved_controller_state_cannot_forge_score_finalization"]
        )
        self.assertFalse(runtime["runtime_investigation_self_repair_label_allowed"])
        verification = self.acceptance["verification"]
        self.assertEqual(verification["phase0_through_phase10_targeted_test_count"], 190)
        self.assertEqual(verification["phase8_through_phase10_contract_test_count"], 64)
        self.assertEqual(verification["full_suite_test_count"], 5495)
        self.assertEqual(verification["full_suite_failure_count"], 18)
        self.assertEqual(verification["new_failure_count"], 0)

    def test_systemic_cluster_and_code_history_are_separate(self) -> None:
        separation = self.acceptance["systemic_repair_separation"]
        self.assertTrue(separation["multiple_distinct_tasks_required_for_cluster"])
        self.assertFalse(separation["single_task_runtime_retry_is_systemic_repair"])
        self.assertTrue(
            separation["production_code_repair_history_requires_git_commit_sha"]
        )
        self.assertFalse(separation["code_repair_history_is_runtime_action"])
        self.assertTrue(separation["fixture_code_repair_history_test_only"])
        self.assertFalse(separation["production_code_repair_observed"])
        audit = self.acceptance["systemic_repair_audit"]
        self.assertEqual(audit["status"], "SYSTEMIC_REPAIR_SEPARATION_PASS")
        self.assertEqual(audit["cluster_count"], 1)
        self.assertEqual(audit["code_repair_history_count"], 1)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(
            audit["result_hash"],
            "3588710cea478e0eebfa43548b60528e57fb252eeb25050441e096ab5e6bf03d",
        )

    def test_report_explains_failure_examples_and_fixture_boundary(self) -> None:
        report = (
            self.repo_root
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase10_adaptive_investigation.md"
        ).read_text(encoding="utf-8")
        self.assertIn("ADAPTIVE_EVIDENCE_CLOSURE_PASS", report)
        self.assertIn("production_runtime_ready=false", report)
        self.assertIn("REROUTED_PRIMITIVE", report)
        self.assertIn("동일 query", report)
        self.assertIn("score_valid=false", report)
        self.assertIn("fixture LLM", report)
        self.assertIn("self-repair", report)


if __name__ == "__main__":
    unittest.main()
