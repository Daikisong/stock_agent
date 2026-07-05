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
        cls.by_id = {row["archetype_id"]: row for row in cls.audit["rows"]}
        cls.by_prefix = {row["archetype_id"].split("_", 1)[0]: row for row in cls.audit["rows"]}

    def test_matrix_has_one_runtime_parity_row_for_every_registered_contract(self) -> None:
        contracts = json.loads(
            (self.repo_root / "configs" / "e2r_agentic_evidence_contracts_v2.json").read_text(encoding="utf-8")
        )["contracts"]
        contract_ids = [row["archetype_id"] for row in contracts]

        self.assertEqual(self.audit["schema_version"], "e2r_research_to_runtime_parity_matrix_v1")
        self.assertEqual(self.audit["registry_archetype_count"], 36)
        self.assertEqual(self.audit["parity_row_count"], 36)
        self.assertEqual(set(self.by_id), set(contract_ids))
        self.assertEqual(self.audit["missing_registry_archetype_ids"], [])

    def test_score_path_pass_is_split_from_meaningful_full_thesis_pass(self) -> None:
        self.assertTrue(self.audit["production_full_e2r_score_path_pass"])
        self.assertFalse(self.audit["meaningful_full_thesis_evidence_pass"])
        self.assertFalse(self.audit["green_ready_full_thesis_pass"])
        self.assertFalse(self.audit["archetype_balanced_full_thesis_pass"])
        self.assertIn("PRODUCTION_FULL_E2R_SCORE_PATH_PASS", self.audit["completion_labels"])
        self.assertIn("MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE", self.audit["completion_labels"])
        self.assertIn("PRODUCTION_SCORE_PATH_IS_NOT_MEANINGFUL_FULL_THESIS_PASS", self.audit["blockers"])

    def test_c05_only_full_thesis_rows_do_not_satisfy_runtime_parity(self) -> None:
        self.assertEqual(self.audit["full_thesis_row_count"], 10)
        self.assertEqual(self.audit["distinct_full_thesis_archetype_count"], 1)
        self.assertEqual(self.audit["full_thesis_by_archetype"], {"C05_EPC_MEGA_CONTRACT_MARGIN_GAP": 10})
        self.assertEqual(self.audit["c05_full_thesis_share"], 1.0)
        self.assertEqual(self.audit["required_positive_missing_full_thesis_row_rate"], 1.0)
        self.assertEqual(self.audit["green_gap_full_thesis_row_rate"], 1.0)
        self.assertIn("C05_FULL_THESIS_MONOCULTURE", self.audit["blockers"])
        self.assertIn("FULL_THESIS_ARCHETYPE_DIVERSITY_BELOW_MINIMUM", self.audit["blockers"])

        c05 = self.by_prefix["C05"]
        self.assertEqual(c05["runtime_parity_status"], "PRODUCTION_FULL_E2R_SCORE_PATH_ONLY")
        self.assertEqual(c05["runtime_full_thesis_row_count"], 10)
        self.assertEqual(c05["runtime_full_thesis_row_with_required_positive_missing_count"], 10)
        self.assertIn("REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROW", c05["blocker_classes"])

    def test_mandatory_canaries_are_not_misreported_as_production_full_thesis(self) -> None:
        self.assertEqual(self.audit["mandatory_archetype_attempt_count"], 1)
        self.assertEqual(self.audit["mandatory_archetype_full_thesis_count"], 0)

        c06 = self.by_prefix["C06"]
        self.assertEqual(c06["source_route_status"], "BLOCKED_FULL_THESIS_CANDIDATE")
        self.assertEqual(c06["runtime_full_thesis_row_count"], 0)
        self.assertGreaterEqual(c06["runtime_planner_top1_count"], 1)
        self.assertIn("005930", c06["blocked_symbols"])
        self.assertIn("000660", c06["planner_top1_symbols_sample"])
        self.assertIn("MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW", c06["blocker_classes"])

        for prefix in ("C08", "C15", "C17", "C24", "C28"):
            row = self.by_prefix[prefix]
            self.assertEqual(row["runtime_full_thesis_row_count"], 0, prefix)
            self.assertEqual(row["runtime_parity_status"], "RESEARCH_REPLAY_READY_BUT_NOT_RUNTIME_PROVEN", prefix)
            self.assertIn("SOURCE_BACKED_REPLAY_NOT_CONNECTED_TO_RUNTIME", row["blocker_classes"])
            self.assertIn("MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW", row["blocker_classes"])

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
        self.assertEqual(v2["required_positive_missing_full_thesis_row_count"], 10)

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
        self.assertEqual(selected_prefixes, ["C06", "C08", "C15", "C17", "C24", "C28"])
        self.assertIn("c05_share_over_balanced_selection_limit", audit["blockers"])
        self.assertIn("target_archetype_unknown_promoted", audit["blockers"])
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

        self.assertEqual(audit["status"], "PLANNER_ARCHETYPE_ROUTING_BIAS_NOT_READY")
        self.assertEqual(audit["top1_archetype_counts"], {"C01": 2, "C05": 29, "C06": 2, "C29": 2})
        self.assertEqual(audit["distinct_top1_archetype_count"], 4)
        self.assertGreater(audit["c05_top1_share"], 0.8)
        self.assertEqual(audit["planner_output_score_stage_key_count"], 0)
        self.assertIn("planner_top1_c05_share_over_limit", audit["blockers"])
        self.assertIn("mandatory_archetypes_not_planner_attempted", audit["blockers"])


if __name__ == "__main__":
    unittest.main()
