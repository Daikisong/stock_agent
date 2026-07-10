from __future__ import annotations

import json
import unittest
from pathlib import Path


class E2RReconstructionPhase7AcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.acceptance = json.loads(
            (cls.repo_root / "e2r_reconstruction_phase7_acceptance.json").read_text(
                encoding="utf-8"
            )
        )

    def test_status_is_phase_scoped_and_not_runtime_ready(self) -> None:
        self.assertEqual(self.acceptance["phase"], 7)
        self.assertEqual(
            self.acceptance["status"],
            "QUESTION_SOURCE_TASK_CONTRACT_PASS",
        )
        self.assertFalse(self.acceptance["production_runtime_ready"])

    def test_every_goal_contract_field_is_present(self) -> None:
        required = self.acceptance["required_contract"]
        self.assertTrue(required)
        self.assertTrue(all(required.values()))

    def test_all_executable_recipes_have_zero_critical_task_gaps(self) -> None:
        audit = self.acceptance["recipe_task_audit"]
        self.assertEqual(audit["task_count"], 31)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(all(value == 0 for value in audit["critical_counts"].values()))
        self.assertEqual(audit["fixture_query_provider_task_count"], 31)
        self.assertEqual(audit["real_query_provider_task_count"], 0)
        self.assertEqual(audit["production_execution_allowed_count"], 0)
        self.assertFalse(audit["production_acceptance_credit"])
        self.assertEqual(
            audit["result_hash"],
            "2b20637db04e9517295a0ddd8361cd2ec5956d6c921a8121be7f3d73c62bfa3e",
        )

    def test_literal_query_is_llm_generated_and_deterministically_validated(self) -> None:
        policy = self.acceptance["literal_query_policy"]
        self.assertFalse(policy["deterministic_query_synthesis"])
        for key, value in policy.items():
            if key != "deterministic_query_synthesis":
                self.assertTrue(value, key)

    def test_incomplete_legacy_task_cannot_enter_canonical_production(self) -> None:
        migration = self.acceptance["legacy_migration"]
        self.assertTrue(migration["legacy_reader_preserved"])
        self.assertTrue(migration["missing_recipe_becomes_invalid_legacy_task"])
        self.assertTrue(migration["missing_question_becomes_invalid_legacy_task"])
        self.assertFalse(migration["legacy_canonical_production_routing_allowed"])
        self.assertTrue(migration["diagnostic_reader_allowed"])

    def test_every_hard_acceptance_count_is_zero(self) -> None:
        hard = self.acceptance["hard_acceptance"]
        for key, value in hard.items():
            if key.endswith("_count") or key == "critical_count_sum":
                self.assertEqual(value, 0, key)

    def test_operational_report_explains_fixture_limit(self) -> None:
        report = (
            self.repo_root
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase7_question_source_task.md"
        ).read_text(encoding="utf-8")
        self.assertIn("QUESTION_SOURCE_TASK_CONTRACT_PASS", report)
        self.assertIn("INVALID_LEGACY_TASK", report)
        self.assertIn("deterministic 코드는 literal query를 만들지 않는다", report)
        self.assertIn("31개", report)
        self.assertIn("production_runtime_ready=false", report)


if __name__ == "__main__":
    unittest.main()
