from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class E2RReconstructionPhase4AcceptanceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.path = REPO_ROOT / "e2r_reconstruction_phase4_acceptance.json"
        self.payload = json.loads(self.path.read_text(encoding="utf-8"))

    def test_status_is_compiler_scoped_and_not_runtime_ready(self) -> None:
        self.assertEqual(self.payload["phase"], 4)
        self.assertEqual(self.payload["status"], "EVIDENCE_RECIPE_OS_COMPILER_PASS")
        self.assertFalse(self.payload["production_runtime_ready"])
        self.assertNotIn("MEANINGFUL_E2R_RUNTIME_READY", self.path.read_text())

    def test_all_contract_pairs_are_explicitly_covered(self) -> None:
        registry = self.payload["contract_registry"]
        self.assertEqual(registry["contract_count"], 36)
        self.assertEqual(registry["required_primitive_pair_count"], 189)
        self.assertEqual(registry["covered_pair_count"], 189)
        self.assertEqual(registry["pair_coverage_rate"], 1.0)

    def test_executable_and_unsupported_counts_are_honest(self) -> None:
        executable = self.payload["executable_semantic_recipes"]
        unsupported = self.payload["explicit_unsupported"]
        self.assertEqual(executable["recipe_count"], 31)
        self.assertEqual(executable["supported_archetype_count"], 6)
        self.assertEqual(unsupported["count"], 158)
        self.assertTrue(unsupported["planning_only"])
        self.assertFalse(unsupported["runtime_route_available"])
        self.assertEqual(executable["recipe_count"] + unsupported["count"], 189)

    def test_hard_acceptance_counts_are_all_zero(self) -> None:
        for key, value in self.payload["hard_acceptance"].items():
            self.assertEqual(value, 0, key)

    def test_literal_query_generation_is_not_owned_by_recipe_code(self) -> None:
        self.assertEqual(
            self.payload["routing_strategy"],
            "EXACT_ARCHETYPE_PRIMITIVE_SEMANTIC_DEFINITION_LOOKUP",
        )
        self.assertIn("LLM planner", self.payload["literal_query_generation_owner"])

    def test_phase4_operational_report_exists(self) -> None:
        report = (
            REPO_ROOT
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase4_evidence_recipe_os.md"
        )
        text = report.read_text(encoding="utf-8")
        self.assertIn("EVIDENCE_RECIPE_OS_COMPILER_PASS", text)
        self.assertIn("UNSUPPORTED_PENDING_SEMANTIC_RECIPE", text)
        self.assertIn("Phase 5", text)


if __name__ == "__main__":
    unittest.main()
