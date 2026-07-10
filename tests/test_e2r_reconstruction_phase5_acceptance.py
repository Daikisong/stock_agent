from __future__ import annotations

import json
import unittest
from pathlib import Path


class E2RReconstructionPhase5AcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.acceptance = json.loads(
            (cls.repo_root / "e2r_reconstruction_phase5_acceptance.json").read_text(
                encoding="utf-8"
            )
        )

    def test_status_is_phase_scoped_and_not_runtime_ready(self) -> None:
        self.assertEqual(self.acceptance["phase"], 5)
        self.assertEqual(
            self.acceptance["status"],
            "SEMANTIC_MEMORY_RETRIEVAL_COMPILER_PASS",
        )
        self.assertFalse(self.acceptance["production_runtime_ready"])

    def test_full_registry_graph_preserves_every_required_type(self) -> None:
        graph = self.acceptance["full_registry_graph"]
        self.assertEqual(graph["historical_case_count"], 10920)
        self.assertEqual(graph["source_verification_count"], 14201)
        self.assertEqual(graph["node_count"], 25532)
        self.assertEqual(graph["edge_count"], 44221)
        self.assertEqual(
            set(graph["node_count_by_type"]),
            {
                "ARCHETYPE",
                "CASE",
                "COUNTER",
                "HARD_BREAK",
                "POSITIVE",
                "PRIMITIVE",
                "RECIPE",
                "SOURCE",
                "SOURCE_FAILURE",
                "SOURCE_SUCCESS",
            },
        )
        self.assertEqual(
            set(graph["edge_count_by_type"]),
            {
                "BEST_FOUND_IN",
                "CAPS",
                "COUNTERS",
                "FAILED_IN",
                "REQUIRES",
                "SAME_MECHANISM",
                "SUPERSEDES",
                "SUPPORTS",
                "WRONG_SUBJECT_EXAMPLE",
            },
        )

    def test_blind_retrieval_exceeds_goal_thresholds(self) -> None:
        retrieval = self.acceptance["blind_retrieval"]
        self.assertEqual(retrieval["benchmark_count"], 61)
        self.assertEqual(retrieval["registry_archetype_coverage_count"], 36)
        self.assertEqual(retrieval["archetype_benchmark_count"], 60)
        self.assertEqual(retrieval["recipe_benchmark_count"], 31)
        self.assertGreaterEqual(retrieval["top3_archetype_hit_rate"], 0.95)
        self.assertGreaterEqual(retrieval["required_recipe_hit_rate"], 0.95)
        self.assertGreaterEqual(retrieval["positive_guard_pair_rate"], 0.90)
        self.assertTrue(retrieval["archetype_exclusion_reason"])
        self.assertTrue(retrieval["recipe_exclusion_reason"])

    def test_ranking_does_not_use_name_count_degree_order_or_outcome(self) -> None:
        policy = self.acceptance["ranking_policy"]
        self.assertFalse(policy["company_name_routing"])
        self.assertFalse(policy["node_count_weight"])
        self.assertFalse(policy["edge_degree_weight"])
        self.assertFalse(policy["input_order_weight"])
        self.assertFalse(policy["historical_outcome_weight"])
        self.assertTrue(policy["as_of_date_filter"])

    def test_every_hard_acceptance_count_is_zero(self) -> None:
        hard = self.acceptance["hard_acceptance"]
        self.assertEqual(hard["critical_count_sum"], 0)
        for key, value in hard.items():
            if key.endswith("_count") or key == "critical_count_sum":
                self.assertEqual(value, 0, key)

    def test_phase5_operational_report_exists(self) -> None:
        path = (
            self.repo_root
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase5_semantic_memory_retrieval.md"
        )
        text = path.read_text(encoding="utf-8")
        self.assertIn("SEMANTIC_MEMORY_RETRIEVAL_COMPILER_PASS", text)
        self.assertIn("60/60", text)
        self.assertIn("31/31", text)
        self.assertIn("planner-hidden", text)
        self.assertIn("Phase 6", text)


if __name__ == "__main__":
    unittest.main()
