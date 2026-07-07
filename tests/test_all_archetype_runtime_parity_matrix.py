import json
import tempfile
import unittest
from pathlib import Path

from e2r.census.all_archetype_runtime_status_matrix import write_all_archetype_runtime_status_matrix
from e2r.census.full_thesis_candidate_selector import build_balanced_full_thesis_candidate_selection_audit
from e2r.census.research_to_runtime_parity import build_research_to_runtime_parity_audit


class AllArchetypeRuntimeParityMatrixArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        docs = Path("docs/operational")
        cls.parity = build_research_to_runtime_parity_audit(repo_root=Path(".").resolve(), as_of_date="2026-07-05")
        cls.contract_ids = [
            row["archetype_id"]
            for row in json.loads(
                (Path("configs") / "e2r_agentic_evidence_contracts_v2.json").read_text(encoding="utf-8")
            )["contracts"]
        ]
        cls.cards = json.loads((docs / "research_runtime_memory_cards_v2.json").read_text(encoding="utf-8"))
        cls.routes = json.loads((docs / "research_source_route_recovery_matrix.json").read_text(encoding="utf-8"))
        cls.inventory = json.loads((docs / "research_reverse_case_inventory.json").read_text(encoding="utf-8"))
        cls.selection = build_balanced_full_thesis_candidate_selection_audit(cls.parity)

    def test_writer_emits_goal4_runtime_parity_aliases(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports = write_all_archetype_runtime_status_matrix(
                parity_audit=self.parity,
                memory_cards=self.cards,
                source_routes=self.routes,
                candidate_selection=self.selection,
                research_inventory=self.inventory,
                docs_dir=temp_dir,
            )
            parity_path = reports["parity_json_path"]
            summary_path = reports["parity_summary_path"]
            self.assertTrue(parity_path.exists())
            self.assertEqual(parity_path.name, "all_archetype_runtime_parity_matrix.json")
            self.assertTrue(summary_path.exists())
            self.assertEqual(summary_path.name, "all_archetype_runtime_parity_summary.md")

            matrix = json.loads(parity_path.read_text(encoding="utf-8"))
            self.assertEqual(matrix["registry_contract_count"], len(self.contract_ids))
            self.assertEqual(len(matrix["rows"]), len(self.contract_ids))
            self.assertEqual(set(matrix["registry_archetype_ids"]), set(self.contract_ids))
            self.assertEqual(set(matrix["matrix_row_archetype_ids"]), set(self.contract_ids))
            self.assertEqual(matrix["missing_parity_source_row_count"], 0)
            self.assertEqual(matrix["duplicate_parity_source_row_count"], 0)
            self.assertEqual(matrix["extra_parity_source_row_count"], 0)
            self.assertTrue(matrix["all_registered_archetypes_have_exactly_one_runtime_status_row"])
            self.assertIn("runtime_status_counts", matrix)
            self.assertIn("primary_blocker_class_counts", matrix)
            self.assertIn("goal4_hard_failure_counts", matrix)
            self.assertFalse(matrix["goal4_hard_failures_clear"])
            self.assertEqual(matrix["source_proxy_to_score_count"], 0)
            self.assertEqual(matrix["not_attempted_without_reason_count"], 0)
            self.assertEqual(matrix["url_backed_case_exists_without_runtime_execution_count"], 1)
            self.assertEqual(
                matrix["url_backed_case_exists_without_runtime_execution_archetype_ids"],
                ["C24_BIO_TRIAL_DATA_EVENT_RISK"],
            )
            self.assertIn(
                "REPLAY_ACCEPTED_CLAIM_ONLY_NOT_PRODUCTION_EXECUTED",
                matrix["url_backed_replay_obligation_status_counts"],
            )

            required_row_fields = {
                "archetype_id",
                "large_sector_id",
                "exists_in_registry",
                "parity_source_row_present",
                "research_case_count",
                "url_backed_case_count",
                "source_proxy_case_count",
                "evidence_url_pending_count",
                "positive_case_count",
                "counterexample_case_count",
                "guard_case_count",
                "runtime_candidate_attempt_count",
                "runtime_planner_attempt_count",
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
                "claim_failure_mode_counts",
                "claim_failure_top_modes",
                "claim_failure_primary_mode",
                "claim_failure_repair_hint",
                "claim_mapping_rejected_samples",
                "url_backed_replay_obligation_status",
                "url_backed_replay_obligation_unmet",
                "source_proxy_to_score_count",
                "runtime_accepted_claim_count",
                "runtime_score_contribution_count",
                "runtime_stagecourt_trace_count",
                "runtime_full_thesis_row_count",
                "runtime_status",
                "primary_blocker_class",
                "blocker_detail",
                "required_positive_missing_rate",
                "green_gap_rate",
                "source_route_ready",
                "source_route_gaps",
                "memory_card_ready",
                "followup_task_count",
                "source_repair_task_count",
            }
            for row in matrix["rows"]:
                self.assertTrue(required_row_fields.issubset(row), row["archetype_id"])
                self.assertTrue(row["exists_in_registry"])

            summary = summary_path.read_text(encoding="utf-8")
            self.assertIn("goal4", summary)
            self.assertIn("SOURCE_REPAIR_REQUIRED", summary)

    def test_goal4_canary_rows_explain_runtime_blocker_not_fake_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            matrix = write_all_archetype_runtime_status_matrix(
                parity_audit=self.parity,
                memory_cards=self.cards,
                source_routes=self.routes,
                candidate_selection=self.selection,
                research_inventory=self.inventory,
                docs_dir=temp_dir,
            )["matrix"]
        by_prefix = {row["archetype_prefix"]: row for row in matrix["rows"]}

        c05 = by_prefix["C05"]
        self.assertEqual(c05["runtime_status"], "SCORE_PATH_CLOSED_WITH_THESIS_GAPS")
        self.assertEqual(c05["primary_blocker_class"], "REQUIRED_POSITIVE_MISSING")
        self.assertEqual(c05["runtime_full_thesis_row_count"], 1)
        self.assertEqual(c05["runtime_full_thesis_row_with_required_positive_missing_count"], 1)
        self.assertEqual(c05["runtime_full_thesis_row_with_green_gap_count"], 1)
        self.assertGreater(c05["runtime_stagecourt_trace_count"], 0)

        c08 = by_prefix["C08"]
        self.assertEqual(c08["runtime_status"], "SCORE_PATH_CLOSED_WITH_THESIS_GAPS")
        self.assertEqual(c08["primary_blocker_class"], "REQUIRED_POSITIVE_MISSING")
        self.assertGreater(c08["research_case_count"], 0)
        self.assertGreater(c08["runtime_source_task_count"], 0)
        self.assertGreater(c08["source_task_execution_log_count"], 0)
        self.assertGreater(c08["source_task_any_accepted_claim_count"], 0)
        self.assertEqual(c08["runtime_full_thesis_row_count"], 1)
        self.assertEqual(c08["runtime_full_thesis_row_with_required_positive_missing_count"], 1)
        self.assertEqual(c08["runtime_full_thesis_row_with_green_gap_count"], 1)
        self.assertEqual(
            c08["next_required_action"],
            "CLOSE_REQUIRED_POSITIVE_AND_GREEN_GAPS_BEFORE_MEANINGFUL_PASS",
        )

        c24 = by_prefix["C24"]
        self.assertEqual(c24["runtime_status"], "PLANNING_ONLY")
        self.assertEqual(c24["primary_blocker_class"], "SOURCE_TASK_NOT_CREATED")
        self.assertEqual(c24["url_backed_replay_obligation_status"], "REPLAY_ACCEPTED_CLAIM_ONLY_NOT_PRODUCTION_EXECUTED")
        self.assertTrue(c24["url_backed_replay_obligation_unmet"])
        self.assertEqual(c24["runtime_source_task_count"], 0)
        self.assertEqual(c24["source_task_execution_log_count"], 0)
        self.assertEqual(c24["runtime_full_thesis_row_count"], 0)
        self.assertEqual(c24["source_task_any_accepted_claim_count"], 0)
        self.assertEqual(
            c24["next_required_action"],
            "TURN_PLANNER_ATTEMPT_INTO_BOUNDED_SOURCE_TASKS",
        )


if __name__ == "__main__":
    unittest.main()
