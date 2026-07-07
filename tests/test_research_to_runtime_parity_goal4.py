import json
import unittest
from pathlib import Path

from e2r.census.research_to_runtime_parity import build_research_to_runtime_parity_audit
from e2r.cli.run_research_to_runtime_parity_until_pass import main as parity_cli_main


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

    def test_score_path_pass_is_split_from_meaningful_full_thesis_pass(self) -> None:
        self.assertTrue(self.audit["production_full_e2r_score_path_pass"])
        self.assertFalse(self.audit["meaningful_full_thesis_evidence_pass"])
        self.assertFalse(self.audit["green_ready_full_thesis_pass"])
        self.assertFalse(self.audit["archetype_balanced_full_thesis_pass"])
        self.assertIn("PRODUCTION_FULL_E2R_SCORE_PATH_PASS", self.audit["completion_labels"])
        self.assertIn("MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE", self.audit["completion_labels"])
        self.assertIn("ARCHETYPE_BALANCED_FULL_THESIS_PASS_FALSE", self.audit["completion_labels"])
        self.assertIn("PRODUCTION_SCORE_PATH_IS_NOT_MEANINGFUL_FULL_THESIS_PASS", self.audit["blockers"])
        self.assertIn("REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS", self.audit["blockers"])
        self.assertIn("GREEN_GAP_ON_PROMOTED_ROWS", self.audit["blockers"])

    def test_partial_full_thesis_rows_do_not_satisfy_runtime_parity(self) -> None:
        self.assertEqual(self.audit["full_thesis_row_count"], 6)
        self.assertEqual(self.audit["distinct_full_thesis_archetype_count"], 6)
        self.assertEqual(
            self.audit["full_thesis_candidate_attempts_by_archetype"],
            {
                "C01_ORDER_BACKLOG_MARGIN_BRIDGE": 2,
                "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": 2,
                "C05_EPC_MEGA_CONTRACT_MARGIN_GAP": 3,
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY": 3,
                "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY": 1,
                "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE": 1,
                "C15_MATERIAL_SPREAD_SUPERCYCLE": 1,
                "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD": 1,
                "C24_BIO_TRIAL_DATA_EVENT_RISK": 1,
                "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE": 1,
                "C31_POLICY_SUBSIDY_LEGISLATION_EVENT": 3,
            },
        )
        self.assertEqual(
            self.audit["full_thesis_by_archetype"],
            {
                "C01_ORDER_BACKLOG_MARGIN_BRIDGE": 1,
                "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": 1,
                "C05_EPC_MEGA_CONTRACT_MARGIN_GAP": 1,
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY": 1,
                "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD": 1,
                "C24_BIO_TRIAL_DATA_EVENT_RISK": 1,
            },
        )
        self.assertEqual(self.audit["c05_full_thesis_share"], 0.166667)
        self.assertEqual(self.audit["required_positive_missing_full_thesis_row_rate"], 0.833333)
        self.assertEqual(self.audit["green_gap_full_thesis_row_rate"], 0.833333)
        self.assertNotIn("C05_FULL_THESIS_MONOCULTURE", self.audit["blockers"])
        self.assertIn("MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING", self.audit["blockers"])

        c05 = self.by_prefix["C05"]
        self.assertEqual(c05["runtime_parity_status"], "PRODUCTION_FULL_E2R_SCORE_PATH_ONLY")
        self.assertEqual(c05["runtime_full_thesis_row_count"], 1)
        self.assertEqual(c05["runtime_full_thesis_row_with_required_positive_missing_count"], 1)
        self.assertEqual(c05["runtime_full_thesis_row_with_green_gap_count"], 1)
        self.assertIn("FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP", c05["blocker_classes"])

    def test_mandatory_canaries_are_not_misreported_as_production_full_thesis(self) -> None:
        self.assertEqual(self.audit["mandatory_archetype_attempt_count"], 6)
        self.assertEqual(self.audit["mandatory_archetype_full_thesis_count"], 3)
        self.assertEqual(
            self.audit["mandatory_archetype_full_thesis_missing"],
            [
                "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
                "C15_MATERIAL_SPREAD_SUPERCYCLE",
                "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
            ],
        )

        c06 = self.by_prefix["C06"]
        self.assertEqual(c06["source_route_status"], "FULL_THESIS_SCORE_PATH_CLOSED")
        self.assertEqual(c06["runtime_full_thesis_row_count"], 1)
        self.assertEqual(c06["runtime_parity_status"], "PRODUCTION_FULL_E2R_SCORE_PATH_ONLY")
        self.assertEqual(c06["runtime_full_thesis_row_with_required_positive_missing_count"], 1)
        self.assertGreaterEqual(c06["runtime_planner_top1_count"], 1)
        self.assertIn("005930", c06["blocked_symbols"])
        self.assertIn("REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROW", c06["blocker_classes"])
        self.assertIn("GREEN_GAP_ON_PROMOTED_ROW", c06["blocker_classes"])

        for prefix in ("C08", "C15"):
            row = self.by_prefix[prefix]
            self.assertEqual(row["runtime_full_thesis_row_count"], 0, prefix)
            self.assertEqual(row["runtime_parity_status"], "FULL_THESIS_BLOCKED_BY_REQUIRED_OR_GREEN_GAP", prefix)
            self.assertGreater(row["runtime_source_task_execution_count"], 0, prefix)
            self.assertIn("MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW", row["blocker_classes"], prefix)
            self.assertIn("FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP", row["blocker_classes"], prefix)

        c24 = self.by_prefix["C24"]
        self.assertEqual(c24["runtime_full_thesis_row_count"], 1)
        self.assertEqual(c24["runtime_parity_status"], "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS")
        self.assertEqual(c24["blocker_classes"], [])

        c28 = self.by_prefix["C28"]
        self.assertEqual(c28["runtime_full_thesis_row_count"], 0)
        self.assertEqual(c28["runtime_parity_status"], "SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM")
        self.assertIn("MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW", c28["blocker_classes"])
        self.assertIn("PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM", c28["blocker_classes"])

        c17 = self.by_prefix["C17"]
        self.assertEqual(c17["runtime_full_thesis_row_count"], 1)
        self.assertEqual(c17["runtime_parity_status"], "PRODUCTION_FULL_E2R_SCORE_PATH_ONLY")
        self.assertIn("REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROW", c17["blocker_classes"])
        self.assertIn("GREEN_GAP_ON_PROMOTED_ROW", c17["blocker_classes"])

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
        self.assertEqual(v2["score_path_status"], "PRODUCTION_FULL_E2R_SCORE_PATH_PASS")
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
                "--fail-on-c05-monoculture",
                "true",
                "--fail-on-unknown-target-promoted",
                "true",
                "--fail-on-required-positive-missing-over-threshold",
                "true",
            ]
        )
        self.assertEqual(exit_code, 2)

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
        selected_prefixes = [row["archetype_id"].split("_", 1)[0] for row in selected[:6]]

        self.assertEqual(audit["status"], "BALANCED_FULL_THESIS_SELECTION_NOT_READY")
        self.assertFalse(audit["meaningful_pass_allowed"])
        self.assertEqual(selected_prefixes[:3], ["C08", "C15", "C28"])
        self.assertTrue({"C02", "C04", "C07"}.issubset(set(selected_prefixes[3:7])))
        self.assertIn("required_positive_missing_promoted_rows", audit["blockers"])

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
        self.assertGreaterEqual(audit["top1_archetype_counts"]["C29"], 5)
        self.assertEqual(audit["top1_archetype_counts"]["C06"], 3)
        self.assertGreaterEqual(audit["distinct_top1_archetype_count"], 31)
        self.assertLess(audit["c05_top1_share"], 0.1)
        self.assertEqual(audit["planner_output_score_stage_key_count"], 0)
        self.assertEqual(audit["blockers"], [])


if __name__ == "__main__":
    unittest.main()
