import json
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from e2r.census.research_to_runtime_parity import build_research_to_runtime_parity_audit
from e2r.cli.run_research_to_runtime_parity_until_pass import (
    _run_next_runtime_attempt,
    main as parity_cli_main,
)


class ResearchToRuntimeParityGoal4Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(".").resolve()
        cls.audit = build_research_to_runtime_parity_audit(repo_root=cls.repo_root, as_of_date="2026-07-05")
        cls.contract_ids = [
            row["archetype_id"]
            for row in json.loads(
                (cls.repo_root / "configs" / "e2r_agentic_evidence_contracts_v2.json").read_text(encoding="utf-8")
            )["contracts"]
        ]
        cls.by_id = {row["archetype_id"]: row for row in cls.audit["rows"]}
        cls.by_prefix = {row["archetype_id"].split("_", 1)[0]: row for row in cls.audit["rows"]}

    def test_matrix_has_one_runtime_parity_row_for_every_registered_contract(self) -> None:
        self.assertEqual(self.audit["schema_version"], "e2r_research_to_runtime_parity_matrix_v1")
        self.assertEqual(self.audit["registry_archetype_count"], len(self.contract_ids))
        self.assertEqual(self.audit["parity_row_count"], len(self.contract_ids))
        self.assertEqual(self.audit["registry_archetype_ids"], self.contract_ids)
        self.assertEqual(set(self.by_id), set(self.contract_ids))
        self.assertEqual(self.audit["missing_registry_archetype_ids"], [])

    def test_score_path_stays_pending_without_full_thesis_rows(self) -> None:
        self.assertFalse(self.audit["production_full_e2r_score_path_pass"])
        self.assertFalse(self.audit["meaningful_full_thesis_evidence_pass"])
        self.assertFalse(self.audit["green_ready_full_thesis_pass"])
        self.assertFalse(self.audit["archetype_balanced_full_thesis_pass"])
        self.assertIn("PRODUCTION_FULL_E2R_SCORE_PATH_PENDING", self.audit["completion_labels"])
        self.assertIn("MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE", self.audit["completion_labels"])
        self.assertIn("ARCHETYPE_BALANCED_FULL_THESIS_PASS_FALSE", self.audit["completion_labels"])
        self.assertNotIn("PRODUCTION_SCORE_PATH_IS_NOT_MEANINGFUL_FULL_THESIS_PASS", self.audit["blockers"])
        self.assertNotIn("REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS", self.audit["blockers"])
        self.assertNotIn("GREEN_GAP_ON_PROMOTED_ROWS", self.audit["blockers"])
        self.assertIn("FULL_THESIS_ARCHETYPE_DIVERSITY_BELOW_MINIMUM", self.audit["blockers"])
        self.assertIn("MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING", self.audit["blockers"])

    def test_no_full_thesis_rows_do_not_satisfy_runtime_parity(self) -> None:
        self.assertEqual(self.audit["full_thesis_row_count"], 0)
        self.assertEqual(self.audit["distinct_full_thesis_archetype_count"], 0)
        self.assertEqual(
            self.audit["full_thesis_candidate_attempts_by_archetype"],
            {
                "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": 1,
                "C05_EPC_MEGA_CONTRACT_MARGIN_GAP": 1,
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY": 1,
            },
        )
        self.assertEqual(self.audit["full_thesis_by_archetype"], {})
        self.assertEqual(self.audit["c05_full_thesis_share"], 0.0)
        self.assertEqual(self.audit["required_positive_missing_full_thesis_row_rate"], 0.0)
        self.assertEqual(self.audit["green_gap_full_thesis_row_rate"], 0.0)
        self.assertNotIn("C05_FULL_THESIS_MONOCULTURE", self.audit["blockers"])
        self.assertIn("FULL_THESIS_ARCHETYPE_DIVERSITY_BELOW_MINIMUM", self.audit["blockers"])
        self.assertIn("MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING", self.audit["blockers"])

        c05 = self.by_prefix["C05"]
        self.assertEqual(c05["runtime_parity_status"], "FULL_THESIS_BLOCKED_BY_REQUIRED_OR_GREEN_GAP")
        self.assertEqual(c05["source_route_status"], "BLOCKED_FULL_THESIS_CANDIDATE")
        self.assertEqual(c05["runtime_full_thesis_row_count"], 0)
        self.assertEqual(c05["runtime_full_thesis_row_with_required_positive_missing_count"], 0)
        self.assertEqual(c05["runtime_full_thesis_row_with_green_gap_count"], 0)
        self.assertGreater(c05["runtime_accepted_claim_count"], 0)
        self.assertIn("FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP", c05["blocker_classes"])

    def test_mandatory_canaries_are_not_misreported_as_production_full_thesis(self) -> None:
        self.assertEqual(self.audit["mandatory_archetype_attempt_count"], 6)
        self.assertEqual(self.audit["mandatory_archetype_full_thesis_count"], 0)
        self.assertEqual(
            self.audit["mandatory_archetype_full_thesis_missing"],
            [
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
                "C15_MATERIAL_SPREAD_SUPERCYCLE",
                "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
                "C24_BIO_TRIAL_DATA_EVENT_RISK",
                "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
            ],
        )

        c06 = self.by_prefix["C06"]
        self.assertEqual(c06["source_route_status"], "BLOCKED_FULL_THESIS_CANDIDATE")
        self.assertEqual(c06["runtime_full_thesis_row_count"], 0)
        self.assertEqual(c06["runtime_parity_status"], "FULL_THESIS_BLOCKED_BY_REQUIRED_OR_GREEN_GAP")
        self.assertEqual(c06["runtime_full_thesis_row_with_required_positive_missing_count"], 0)
        self.assertGreaterEqual(c06["runtime_planner_top1_count"], 1)
        self.assertIn("005930", c06["blocked_symbols"])
        self.assertIn("MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW", c06["blocker_classes"])
        self.assertIn("FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP", c06["blocker_classes"])

        c08 = self.by_prefix["C08"]
        self.assertEqual(c08["runtime_full_thesis_row_count"], 0)
        self.assertEqual(c08["runtime_parity_status"], "SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM")
        self.assertGreater(c08["runtime_source_task_execution_count"], 0)
        self.assertEqual(c08["runtime_accepted_claim_count"], 0)
        self.assertIn("MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW", c08["blocker_classes"])
        self.assertIn("PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM", c08["blocker_classes"])

        c15 = self.by_prefix["C15"]
        self.assertEqual(c15["runtime_full_thesis_row_count"], 0)
        self.assertEqual(c15["runtime_parity_status"], "ACCEPTED_CLAIM_PRESENT_BUT_FULL_THESIS_NOT_CLOSED")
        self.assertGreater(c15["runtime_accepted_claim_count"], 0)
        self.assertIn("MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW", c15["blocker_classes"])
        self.assertNotIn("PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM", c15["blocker_classes"])

        c24 = self.by_prefix["C24"]
        self.assertEqual(c24["runtime_full_thesis_row_count"], 0)
        self.assertEqual(c24["runtime_parity_status"], "ACCEPTED_CLAIM_PRESENT_BUT_FULL_THESIS_NOT_CLOSED")
        self.assertEqual(c24["runtime_full_thesis_row_with_required_positive_missing_count"], 0)
        self.assertEqual(c24["runtime_full_thesis_row_with_green_gap_count"], 0)
        self.assertGreater(c24["runtime_source_task_execution_count"], 0)
        self.assertGreater(c24["runtime_accepted_claim_count"], 0)
        self.assertIn("MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW", c24["blocker_classes"])

        c28 = self.by_prefix["C28"]
        self.assertEqual(c28["runtime_full_thesis_row_count"], 0)
        self.assertEqual(c28["runtime_parity_status"], "SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM")
        self.assertGreater(c28["runtime_source_task_execution_count"], 0)
        self.assertEqual(c28["runtime_accepted_claim_count"], 0)
        self.assertIn("MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW", c28["blocker_classes"])
        self.assertIn("PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM", c28["blocker_classes"])

        c17 = self.by_prefix["C17"]
        self.assertEqual(c17["runtime_full_thesis_row_count"], 0)
        self.assertEqual(c17["runtime_parity_status"], "ACCEPTED_CLAIM_PRESENT_BUT_FULL_THESIS_NOT_CLOSED")
        self.assertGreater(c17["runtime_accepted_claim_count"], 0)
        self.assertIn("MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW", c17["blocker_classes"])
        self.assertNotIn("REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROW", c17["blocker_classes"])
        self.assertNotIn("GREEN_GAP_ON_PROMOTED_ROW", c17["blocker_classes"])

    def test_split_label_v2_audit_is_written_and_matches_matrix(self) -> None:
        matrix = json.loads(
            (self.repo_root / "docs" / "operational" / "research_to_runtime_parity_matrix_2026-07-05.json").read_text(
                encoding="utf-8"
            )
        )
        v2 = json.loads(
            (
                self.repo_root
                / "docs"
                / "operational"
                / "census_mode_v4_full_thesis_evidence_completion_audit_v2.json"
            ).read_text(encoding="utf-8")
        )

        self.assertEqual(matrix["final_status"], "MEANINGFUL_RUNTIME_PARITY_NOT_READY")
        self.assertEqual(v2["score_path_status"], "PRODUCTION_FULL_E2R_SCORE_PATH_PENDING")
        self.assertEqual(v2["meaningful_evidence_status"], "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE")
        self.assertEqual(v2["distinct_full_thesis_archetype_count"], matrix["distinct_full_thesis_archetype_count"])
        self.assertEqual(
            v2["required_positive_missing_full_thesis_row_count"],
            matrix["required_positive_missing_full_thesis_row_count"],
        )
        self.assertEqual(v2["green_gap_full_thesis_row_count"], matrix["green_gap_full_thesis_row_count"])

    def test_cli_fail_flags_return_failure_for_current_c05_monoculture(self) -> None:
        exit_code = parity_cli_main(
            [
                "--as-of-date",
                "2026-07-05",
                "--allow-legacy-diagnostic",
                "--fail-on-c05-monoculture",
                "true",
                "--fail-on-unknown-target-promoted",
                "true",
                "--fail-on-required-positive-missing-over-threshold",
                "true",
            ]
        )
        self.assertNotEqual(exit_code, 0)

    def test_cli_max_iterations_above_one_executes_next_runtime_manifest(self) -> None:
        def fake_paths(*, ready: bool) -> dict:
            audit = {
                "final_status": "MEANINGFUL_RUNTIME_PARITY_READY" if ready else "MEANINGFUL_RUNTIME_PARITY_NOT_READY",
                "completion_labels": ["MEANINGFUL_FULL_THESIS_EVIDENCE_PASS"]
                if ready
                else ["MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE"],
                "blockers": [] if ready else ["REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS"],
                "rows": [],
                "meaningful_full_thesis_evidence_pass": ready,
                "archetype_balanced_full_thesis_pass": ready,
                "full_thesis_row_count": 7 if ready else 6,
                "distinct_full_thesis_archetype_count": 7 if ready else 6,
                "mandatory_archetype_full_thesis_missing": [] if ready else ["C15_MATERIAL_SPREAD_SUPERCYCLE"],
                "required_positive_missing_full_thesis_row_rate": 0.0 if ready else 1.0,
                "green_gap_full_thesis_row_rate": 0.0 if ready else 1.0,
                "as_of_date": "2026-07-05",
                "output_root": "output/current",
            }
            return {
                "audit": audit,
                "matrix_path": Path("docs/operational/fake_matrix.json"),
                "summary_path": Path("docs/operational/fake_summary.md"),
                "root_cause_path": Path("docs/operational/fake_root.md"),
                "v2_audit_path": Path("docs/operational/fake_v2.json"),
                "candidate_selection_audit": {"status": "PASS"},
                "planner_bias_audit": {"status": "PASS"},
                "research_reverse_bundle": {
                    "inventory": {"record_count": 1001},
                    "cards": {"card_count": 36},
                },
                "source_route_reports": {"source_route_matrix": {"pattern_count": 36}},
                "all_status_reports": {
                    "json_path": Path("docs/operational/fake_status.json"),
                    "matrix": {"registry_contract_count": 36},
                },
                "next_attempt_reports": {
                    "json_path": Path("docs/operational/fake_next.json"),
                    "plan": {"plan_row_count": 36, "source_task_count": 111},
                },
                "execution_manifest_reports": {
                    "json_path": Path("docs/operational/fake_manifest.json"),
                    "manifest": {
                        "seed_event_count": 111,
                        "run_command_argv": [
                            "python",
                            "-m",
                            "e2r.cli.run_e2r_census_v4_until_pass",
                            "--as-of-date",
                            "2026-07-05",
                            "--output-root",
                            "output/old",
                        ],
                        "census_v4_config_kwargs": {
                            "as_of_date": "2026-07-05",
                            "brain_runtime_budget_seconds": 1.0,
                        },
                    },
                },
                "followup_audit": {"task_count": 28},
                "replay_reports": {
                    "replay_matrix": {
                        "accepted_claim_replay_count": 3,
                        "source_proxy_repair_task_count": 18,
                    }
                },
                "meaningful_acceptance": {
                    "meaningful_status": "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS"
                    if ready
                    else "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE"
                },
                "acceptance_report_path": Path("docs/operational/fake_acceptance.md"),
                "readiness_verdict_path": Path("docs/operational/fake_verdict.md"),
            }

        with patch(
            "e2r.cli.run_research_to_runtime_parity_until_pass.write_research_to_runtime_parity_artifacts",
            side_effect=[fake_paths(ready=False), fake_paths(ready=True)],
        ) as write_mock, patch(
            "e2r.cli.run_research_to_runtime_parity_until_pass._run_next_runtime_attempt",
            return_value={
                "iteration": 1,
                "output_root": "output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01",
                "returncode": 1,
                "argv": ["python", "-m", "e2r.cli.run_e2r_census_v4_until_pass"],
                "stdout_tail": "NOT_READY",
                "stderr_tail": "",
                "partial_run_invalid": False,
                "partial_run_invalid_path": "",
            },
        ) as run_mock:
            exit_code = parity_cli_main(
                [
                    "--as-of-date",
                    "2026-07-05",
                    "--max-iterations",
                    "2",
                    "--allow-legacy-diagnostic",
                ]
            )

        self.assertEqual(exit_code, 0)
        self.assertEqual(write_mock.call_count, 2)
        run_mock.assert_called_once()

    def test_cli_stops_after_one_unready_runtime_without_repeated_attempt_flag(self) -> None:
        def fake_paths() -> dict:
            audit = {
                "final_status": "MEANINGFUL_RUNTIME_PARITY_NOT_READY",
                "completion_labels": ["MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE"],
                "blockers": ["REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS"],
                "rows": [],
                "meaningful_full_thesis_evidence_pass": False,
                "archetype_balanced_full_thesis_pass": False,
                "full_thesis_row_count": 6,
                "distinct_full_thesis_archetype_count": 6,
                "mandatory_archetype_full_thesis_missing": ["C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY"],
                "required_positive_missing_full_thesis_row_rate": 0.833333,
                "green_gap_full_thesis_row_rate": 0.833333,
                "as_of_date": "2026-07-05",
                "output_root": "output/current",
            }
            return {
                "audit": audit,
                "matrix_path": Path("docs/operational/fake_matrix.json"),
                "summary_path": Path("docs/operational/fake_summary.md"),
                "root_cause_path": Path("docs/operational/fake_root.md"),
                "v2_audit_path": Path("docs/operational/fake_v2.json"),
                "candidate_selection_audit": {"status": "NOT_READY"},
                "planner_bias_audit": {"status": "PASS"},
                "research_reverse_bundle": {"inventory": {"record_count": 1001}, "cards": {"card_count": 36}},
                "source_route_reports": {"source_route_matrix": {"pattern_count": 36}},
                "all_status_reports": {
                    "json_path": Path("docs/operational/fake_status.json"),
                    "matrix": {"registry_contract_count": 36},
                },
                "next_attempt_reports": {
                    "json_path": Path("docs/operational/fake_next.json"),
                    "plan": {"plan_row_count": 36, "source_task_count": 111},
                },
                "execution_manifest_reports": {
                    "json_path": Path("docs/operational/fake_manifest.json"),
                    "manifest": {
                        "seed_event_count": 111,
                        "run_command_argv": ["python", "-m", "e2r.cli.run_e2r_census_v4_until_pass"],
                    },
                },
                "followup_audit": {"task_count": 28},
                "replay_reports": {
                    "replay_matrix": {"accepted_claim_replay_count": 3, "source_proxy_repair_task_count": 18}
                },
                "meaningful_acceptance": {"meaningful_status": "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE"},
                "acceptance_report_path": Path("docs/operational/fake_acceptance.md"),
                "readiness_verdict_path": Path("docs/operational/fake_verdict.md"),
            }

        with patch(
            "e2r.cli.run_research_to_runtime_parity_until_pass.write_research_to_runtime_parity_artifacts",
            side_effect=[fake_paths(), fake_paths(), fake_paths()],
        ) as write_mock, patch(
            "e2r.cli.run_research_to_runtime_parity_until_pass._run_next_runtime_attempt",
            return_value={
                "iteration": 1,
                "output_root": "output/census_v4/attempt-01",
                "returncode": 1,
                "argv": ["python", "-m", "e2r.cli.run_e2r_census_v4_until_pass"],
                "stdout_tail": "NOT_READY",
                "stderr_tail": "",
                "partial_run_invalid": False,
                "partial_run_invalid_path": "",
            },
        ) as run_mock, patch("sys.stdout", new_callable=io.StringIO) as stdout:
            exit_code = parity_cli_main(
                [
                    "--as-of-date",
                    "2026-07-05",
                    "--max-iterations",
                    "3",
                    "--allow-legacy-diagnostic",
                ]
            )

        payload = json.loads(stdout.getvalue())
        self.assertEqual(exit_code, 1)
        self.assertEqual(write_mock.call_count, 2)
        run_mock.assert_called_once()
        self.assertEqual(payload["self_repair_iteration_count"], 1)
        self.assertEqual(
            payload["self_repair_stop_reason"],
            "SELF_REPAIR_REQUIRES_CODE_OR_SOURCE_ROUTE_REPAIR_AFTER_RUNTIME_ATTEMPT",
        )

    def test_runtime_attempt_keyboard_interrupt_marks_partial_output_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir, patch(
            "e2r.cli.run_research_to_runtime_parity_until_pass._self_repair_output_root",
            return_value=str(Path(tmpdir) / "attempt"),
        ), patch(
            "e2r.cli.run_research_to_runtime_parity_until_pass.subprocess.run",
            side_effect=KeyboardInterrupt(),
        ):
            execution = _run_next_runtime_attempt(
                repo_root=self.repo_root,
                manifest={"run_command_argv": ["python", "-m", "e2r.cli.run_e2r_census_v4_until_pass"]},
                as_of_date="2026-07-05",
                iteration=1,
            )

            marker_path = Path(execution["partial_run_invalid_path"])
            marker = json.loads(marker_path.read_text(encoding="utf-8"))

        self.assertEqual(execution["returncode"], 130)
        self.assertTrue(execution["partial_run_invalid"])
        self.assertEqual(marker["verdict"], "INVALID_PARTIAL_OUTPUT")
        self.assertFalse(marker["readiness_evidence_allowed"])
        self.assertFalse(marker["score_or_stage_evidence_allowed"])
        self.assertFalse(marker["full_thesis_promotion_allowed"])

    def test_balanced_candidate_selection_audit_prioritizes_missing_canaries(self) -> None:
        audit = json.loads(
            (
                self.repo_root
                / "docs"
                / "operational"
                / "balanced_full_thesis_candidate_selection_audit_2026-07-05.json"
            ).read_text(encoding="utf-8")
        )
        selected = audit["next_required_archetype_attempts"]
        selected_prefixes = [row["archetype_id"].split("_", 1)[0] for row in selected[:12]]

        self.assertEqual(audit["status"], "BALANCED_FULL_THESIS_SELECTION_NOT_READY")
        self.assertFalse(audit["meaningful_pass_allowed"])
        self.assertEqual(selected_prefixes[:6], ["C06", "C08", "C15", "C17", "C24", "C28"])
        self.assertTrue({"C01", "C02", "C03", "C04", "C05", "C07"}.issubset(set(selected_prefixes[6:12])))
        self.assertNotIn("required_positive_missing_promoted_rows", audit["blockers"])
        self.assertIn("full_thesis_archetype_count_below_meaningful_minimum", audit["blockers"])

    def test_planner_bias_audit_catches_c05_routing_concentration(self) -> None:
        audit = json.loads(
            (
                self.repo_root
                / "docs"
                / "operational"
                / "planner_bias_and_archetype_routing_audit_2026-07-05.json"
            ).read_text(encoding="utf-8")
        )

        self.assertEqual(audit["status"], "PLANNER_ARCHETYPE_ROUTING_BIAS_PASS")
        self.assertEqual(audit["top1_archetype_counts"]["C05"], 3)
        self.assertEqual(audit["top1_archetype_counts"]["C29"], 3)
        self.assertEqual(audit["top1_archetype_counts"]["C06"], 3)
        self.assertGreaterEqual(audit["distinct_top1_archetype_count"], 31)
        self.assertLess(audit["c05_top1_share"], 0.1)
        self.assertEqual(audit["planner_output_score_stage_key_count"], 0)
        self.assertEqual(audit["blockers"], [])


if __name__ == "__main__":
    unittest.main()
