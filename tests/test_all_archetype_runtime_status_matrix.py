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
        cls.selection = build_balanced_full_thesis_candidate_selection_audit(cls.parity)
        cls.matrix = build_all_archetype_runtime_status_matrix(
            parity_audit=cls.parity,
            memory_cards=cls.cards,
            source_routes=cls.routes,
            candidate_selection=cls.selection,
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
            "next_required_action",
            "status_reason_ko",
        }
        for row in self.matrix["rows"]:
            self.assertTrue(required.issubset(row), row["archetype_id"])
            for key in required:
                self.assertTrue(row[key], (row["archetype_id"], key))

    def test_c05_score_path_is_not_meaningful_runtime_parity(self) -> None:
        c05 = self.by_prefix["C05"]
        self.assertEqual(c05["runtime_attempt_status"], "PRODUCTION_FULL_THESIS_ATTEMPTED")
        self.assertEqual(c05["accepted_claim_status"], "PRODUCTION_SCORE_PATH_HAS_ACCEPTED_CLAIMS")
        self.assertEqual(c05["full_thesis_status"], "SCORE_PATH_ONLY_WITH_REQUIRED_OR_GREEN_GAPS")
        self.assertEqual(c05["runtime_parity_proof_status"], "NOT_PROVEN_SCORE_PATH_ONLY")
        self.assertEqual(c05["runtime_full_thesis_row_count"], 2)
        self.assertEqual(c05["runtime_full_thesis_row_with_required_positive_missing_count"], 2)
        self.assertEqual(c05["runtime_full_thesis_row_with_green_gap_count"], 2)

    def test_c06_has_runtime_evidence_but_is_blocked_not_smoke_promoted(self) -> None:
        c06 = self.by_prefix["C06"]
        self.assertEqual(c06["runtime_attempt_status"], "PRODUCTION_FULL_THESIS_ATTEMPTED")
        self.assertEqual(c06["runtime_source_route_execution_status"], "SOURCE_TASK_EXECUTED_WITH_ACCEPTED_CLAIMS")
        self.assertEqual(c06["accepted_claim_status"], "PRODUCTION_SCORE_PATH_HAS_ACCEPTED_CLAIMS")
        self.assertEqual(c06["full_thesis_status"], "SCORE_PATH_ONLY_WITH_REQUIRED_OR_GREEN_GAPS")
        self.assertEqual(c06["runtime_parity_proof_status"], "NOT_PROVEN_SCORE_PATH_ONLY")
        self.assertEqual(c06["runtime_full_thesis_row_count"], 1)
        self.assertEqual(c06["runtime_full_thesis_row_with_required_positive_missing_count"], 1)
        self.assertEqual(c06["runtime_full_thesis_row_with_green_gap_count"], 1)
        self.assertIn("005930", c06["blocked_symbols"])

    def test_c08_and_other_canaries_are_replay_ready_but_not_runtime_attempted(self) -> None:
        source_attempted_prefixes = ("C08", "C15", "C24", "C28")
        for prefix in source_attempted_prefixes:
            row = self.by_prefix[prefix]
            self.assertEqual(row["runtime_attempt_status"], "SOURCE_TASK_EXECUTED", prefix)
            self.assertEqual(row["runtime_source_route_execution_status"], "SOURCE_TASK_EXECUTED_NO_ACCEPTED_CLAIMS", prefix)
            self.assertEqual(row["accepted_claim_status"], "REPLAY_ACCEPTED_CLAIM_ONLY", prefix)
            self.assertEqual(row["full_thesis_status"], "NO_PRODUCTION_FULL_THESIS_ROW", prefix)
            self.assertEqual(row["runtime_parity_proof_status"], "NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM", prefix)
            self.assertEqual(
                row["next_required_action"],
                "REPLAN_SOURCE_TASKS_WITH_RESEARCH_MEMORY_AND_REQUIRE_ANCHORS",
                prefix,
            )
        c17 = self.by_prefix["C17"]
        self.assertEqual(c17["runtime_attempt_status"], "PLANNER_ATTEMPTED_ONLY")
        self.assertEqual(c17["runtime_source_route_execution_status"], "ROUTE_RECOVERED_NOT_EXECUTED")
        self.assertEqual(c17["accepted_claim_status"], "REPLAY_ACCEPTED_CLAIM_ONLY")
        self.assertEqual(c17["full_thesis_status"], "NO_PRODUCTION_FULL_THESIS_ROW")
        self.assertEqual(c17["runtime_parity_proof_status"], "NOT_PROVEN_PLANNER_ONLY")
        self.assertEqual(c17["next_required_action"], "TURN_PLANNER_ATTEMPT_INTO_BOUNDED_SOURCE_TASKS")

    def test_source_executed_without_accepted_claim_is_not_collapsed_into_planner_only(self) -> None:
        c29 = self.by_prefix["C29"]
        self.assertEqual(c29["runtime_attempt_status"], "SOURCE_TASK_EXECUTED")
        self.assertEqual(c29["runtime_source_route_execution_status"], "SOURCE_TASK_EXECUTED_NO_ACCEPTED_CLAIMS")
        self.assertEqual(c29["accepted_claim_status"], "NO_ACCEPTED_CLAIM")
        self.assertEqual(c29["runtime_parity_proof_status"], "NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM")


if __name__ == "__main__":
    unittest.main()
