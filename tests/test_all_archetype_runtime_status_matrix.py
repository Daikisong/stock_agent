import json
import unittest
from pathlib import Path

from e2r.census.all_archetype_runtime_status_matrix import build_all_archetype_runtime_status_matrix
from e2r.census.full_thesis_candidate_selector import build_balanced_full_thesis_candidate_selection_audit
from e2r.census.research_to_runtime_parity import build_research_to_runtime_parity_audit


class AllArchetypeRuntimeStatusMatrixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.docs = Path("docs/operational")
        cls.parity = build_research_to_runtime_parity_audit(repo_root=Path(".").resolve(), as_of_date="2026-07-05")
        cls.cards = json.loads((cls.docs / "research_runtime_memory_cards_v2.json").read_text(encoding="utf-8"))
        cls.routes = json.loads((cls.docs / "research_source_route_recovery_matrix.json").read_text(encoding="utf-8"))
        cls.inventory = json.loads((cls.docs / "research_reverse_case_inventory.json").read_text(encoding="utf-8"))
        cls.selection = build_balanced_full_thesis_candidate_selection_audit(cls.parity)
        cls.matrix = build_all_archetype_runtime_status_matrix(
            parity_audit=cls.parity,
            memory_cards=cls.cards,
            source_routes=cls.routes,
            candidate_selection=cls.selection,
            research_inventory=cls.inventory,
        )
        cls.by_prefix = {row["archetype_prefix"]: row for row in cls.matrix["rows"]}

    def test_matrix_covers_c01_to_c32_plus_four_r13_contracts(self) -> None:
        self.assertEqual(self.matrix["schema_version"], "e2r_all_archetype_runtime_status_matrix_v1")
        self.assertEqual(self.matrix["registry_contract_count"], 36)
        self.assertEqual(self.matrix["c01_to_c32_contract_count"], 32)
        self.assertEqual(self.matrix["r13_cross_archetype_contract_count"], 4)
        self.assertTrue(self.matrix["all_contracts_have_runtime_status_axes"])
        self.assertTrue(self.matrix["all_contracts_have_memory_card"])
        self.assertTrue(self.matrix["all_contracts_have_source_route_patterns"])

    def test_every_row_has_attempt_source_claim_and_full_thesis_status(self) -> None:
        required = {
            "runtime_attempt_status",
            "source_route_recovery_status",
            "runtime_source_route_execution_status",
            "accepted_claim_status",
            "full_thesis_status",
            "runtime_parity_proof_status",
            "runtime_status",
            "primary_blocker_class",
            "blocker_detail",
            "next_required_action",
            "status_reason_ko",
            "research_case_count",
            "url_backed_case_count",
            "runtime_source_task_count",
            "runtime_source_task_executed_count",
            "source_task_execution_log_count",
            "source_task_no_accepted_claim_execution_count",
            "source_task_direct_accepted_claim_count",
            "source_task_rerouted_accepted_claim_count",
            "source_task_any_accepted_claim_count",
            "source_task_rejected_claim_count",
            "source_task_failure_axis_counts",
            "source_task_top_failure_axes",
            "source_task_status_counts",
            "source_task_stop_reason_counts",
            "source_task_provider_error_counts",
            "source_task_not_eligible_reason_counts",
            "source_task_top_unsatisfied_primitives",
            "claim_mapping_trace_log_count",
            "claim_mapping_accepted_trace_count",
            "claim_mapping_rejected_trace_count",
            "claim_mapping_rejection_reason_counts",
            "claim_mapping_top_rejection_reasons",
            "claim_mapping_rejected_samples",
            "runtime_planner_attempt_count",
            "source_route_ready",
            "memory_card_ready",
        }
        for row in self.matrix["rows"]:
            self.assertTrue(required.issubset(row), row["archetype_id"])
            for key in required:
                if key in {"source_route_ready", "memory_card_ready"}:
                    self.assertIsInstance(row[key], bool, (row["archetype_id"], key))
                elif key.endswith("_count"):
                    self.assertIsInstance(row[key], int, (row["archetype_id"], key))
                elif key.endswith("_counts"):
                    self.assertIsInstance(row[key], dict, (row["archetype_id"], key))
                elif key.startswith("source_task_top_"):
                    self.assertIsInstance(row[key], list, (row["archetype_id"], key))
                elif key.startswith("claim_mapping_top_") or key == "claim_mapping_rejected_samples":
                    self.assertIsInstance(row[key], list, (row["archetype_id"], key))
                else:
                    self.assertTrue(row[key], (row["archetype_id"], key))

    def test_c05_score_path_is_not_meaningful_runtime_parity(self) -> None:
        c05 = self.by_prefix["C05"]
        self.assertEqual(c05["runtime_attempt_status"], "PRODUCTION_FULL_THESIS_ATTEMPTED")
        self.assertEqual(c05["accepted_claim_status"], "PRODUCTION_SCORE_PATH_HAS_ACCEPTED_CLAIMS")
        self.assertEqual(c05["full_thesis_status"], "SCORE_PATH_ONLY_WITH_REQUIRED_OR_GREEN_GAPS")
        self.assertEqual(c05["runtime_parity_proof_status"], "NOT_PROVEN_SCORE_PATH_ONLY")
        self.assertEqual(c05["runtime_status"], "SCORE_PATH_CLOSED_WITH_THESIS_GAPS")
        self.assertEqual(c05["primary_blocker_class"], "REQUIRED_POSITIVE_MISSING")
        self.assertEqual(c05["runtime_full_thesis_row_count"], 1)
        self.assertEqual(c05["runtime_full_thesis_row_with_required_positive_missing_count"], 1)
        self.assertEqual(c05["runtime_full_thesis_row_with_green_gap_count"], 1)
        self.assertEqual(c05["required_positive_missing_rate"], 1.0)
        self.assertEqual(c05["green_gap_rate"], 1.0)
        self.assertGreater(c05["research_case_count"], 0)
        self.assertGreater(c05["url_backed_case_count"], 0)

    def test_c06_has_runtime_evidence_but_is_blocked_not_smoke_promoted(self) -> None:
        c06 = self.by_prefix["C06"]
        self.assertEqual(c06["runtime_attempt_status"], "PRODUCTION_FULL_THESIS_ATTEMPTED")
        self.assertEqual(c06["runtime_source_route_execution_status"], "SOURCE_TASK_EXECUTED_WITH_ACCEPTED_CLAIMS")
        self.assertEqual(c06["accepted_claim_status"], "PRODUCTION_SCORE_PATH_HAS_ACCEPTED_CLAIMS")
        self.assertEqual(c06["full_thesis_status"], "SCORE_PATH_ONLY_WITH_REQUIRED_OR_GREEN_GAPS")
        self.assertEqual(c06["runtime_parity_proof_status"], "NOT_PROVEN_SCORE_PATH_ONLY")
        self.assertEqual(c06["runtime_status"], "SCORE_PATH_CLOSED_WITH_THESIS_GAPS")
        self.assertEqual(c06["primary_blocker_class"], "REQUIRED_POSITIVE_MISSING")
        self.assertEqual(c06["runtime_full_thesis_row_count"], 1)
        self.assertEqual(c06["runtime_full_thesis_row_with_required_positive_missing_count"], 1)
        self.assertEqual(c06["runtime_full_thesis_row_with_green_gap_count"], 1)
        self.assertIn("005930", c06["blocked_symbols"])

    def test_c08_and_other_canaries_require_target_materialization_before_source_proof(self) -> None:
        targetless_shell_prefixes = ("C08", "C15", "C24", "C28")
        for prefix in targetless_shell_prefixes:
            row = self.by_prefix[prefix]
            self.assertEqual(row["runtime_attempt_status"], "SOURCE_TASK_EXECUTED", prefix)
            self.assertEqual(row["runtime_source_route_execution_status"], "SOURCE_TASK_EXECUTED_NO_ACCEPTED_CLAIMS", prefix)
            self.assertEqual(row["accepted_claim_status"], "REPLAY_ACCEPTED_CLAIM_ONLY", prefix)
            self.assertEqual(row["full_thesis_status"], "NO_PRODUCTION_FULL_THESIS_ROW", prefix)
            self.assertEqual(row["runtime_parity_proof_status"], "NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM", prefix)
            self.assertEqual(row["runtime_status"], "SOURCE_REPAIR_REQUIRED", prefix)
            self.assertEqual(row["primary_blocker_class"], "ACCEPTED_CLAIM_NOT_CREATED", prefix)
            self.assertGreater(row["runtime_source_task_execution_count"], 0, prefix)
            self.assertGreater(row["source_task_execution_log_count"], 0, prefix)
            self.assertEqual(
                row["source_task_no_accepted_claim_execution_count"],
                row["source_task_execution_log_count"],
                prefix,
            )
            self.assertIn("NO_ACCEPTED_CLAIM", row["source_task_failure_axis_counts"], prefix)
            self.assertIn("NO_SCORE_ELIGIBLE_REAL_CLAIM", row["source_task_failure_axis_counts"], prefix)
            self.assertIn("PRIMITIVE_MAPPING_REJECTED", row["source_task_failure_axis_counts"], prefix)
            self.assertGreater(row["claim_mapping_trace_log_count"], 0, prefix)
            self.assertEqual(row["claim_mapping_accepted_trace_count"], 0, prefix)
            self.assertGreater(row["claim_mapping_rejected_trace_count"], 0, prefix)
            self.assertIn("primitive_mapping_rejected", row["claim_mapping_rejection_reason_counts"], prefix)
            self.assertTrue(row["claim_mapping_rejected_samples"], prefix)
            sample = row["claim_mapping_rejected_samples"][0]
            self.assertIn("source_url", sample, prefix)
            self.assertIn("quote_excerpt", sample, prefix)
            self.assertIn("rejection_reasons", sample, prefix)
            self.assertEqual(row["targetless_source_task_execution_count"], 0, prefix)
            self.assertEqual(
                row["next_required_action"],
                "REPLAN_SOURCE_TASKS_WITH_RESEARCH_MEMORY_AND_REQUIRE_ANCHORS",
                prefix,
            )
        c17 = self.by_prefix["C17"]
        self.assertEqual(c17["runtime_attempt_status"], "SOURCE_TASK_EXECUTED")
        self.assertEqual(c17["runtime_source_route_execution_status"], "SOURCE_TASK_EXECUTED_NO_ACCEPTED_CLAIMS")
        self.assertEqual(c17["accepted_claim_status"], "REPLAY_ACCEPTED_CLAIM_ONLY")
        self.assertEqual(c17["full_thesis_status"], "NO_PRODUCTION_FULL_THESIS_ROW")
        self.assertEqual(c17["runtime_parity_proof_status"], "NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM")
        self.assertEqual(c17["runtime_status"], "SOURCE_REPAIR_REQUIRED")
        self.assertEqual(c17["primary_blocker_class"], "ACCEPTED_CLAIM_NOT_CREATED")
        self.assertEqual(c17["source_task_any_accepted_claim_count"], 0)
        self.assertGreater(c17["source_task_failure_axis_counts"]["NO_ACCEPTED_CLAIM"], 0)
        self.assertGreater(c17["claim_mapping_rejected_trace_count"], 0)
        self.assertTrue(c17["claim_mapping_rejected_samples"])
        self.assertEqual(
            c17["next_required_action"],
            "REPLAN_SOURCE_TASKS_WITH_RESEARCH_MEMORY_AND_REQUIRE_ANCHORS",
        )

    def test_source_executed_without_accepted_claim_is_not_collapsed_into_planner_only(self) -> None:
        c29 = self.by_prefix["C29"]
        self.assertEqual(c29["runtime_attempt_status"], "SOURCE_TASK_EXECUTED")
        self.assertEqual(c29["runtime_source_route_execution_status"], "SOURCE_TASK_EXECUTED_NO_ACCEPTED_CLAIMS")
        self.assertEqual(c29["accepted_claim_status"], "NO_ACCEPTED_CLAIM")
        self.assertEqual(c29["runtime_parity_proof_status"], "NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM")


if __name__ == "__main__":
    unittest.main()
