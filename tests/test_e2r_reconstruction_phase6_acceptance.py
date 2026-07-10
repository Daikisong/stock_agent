from __future__ import annotations

import json
import unittest
from pathlib import Path


class E2RReconstructionPhase6AcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.acceptance = json.loads(
            (cls.repo_root / "e2r_reconstruction_phase6_acceptance.json").read_text(
                encoding="utf-8"
            )
        )

    def test_status_is_phase_scoped_and_not_runtime_ready(self) -> None:
        self.assertEqual(self.acceptance["phase"], 6)
        self.assertEqual(
            self.acceptance["status"],
            "TWO_PASS_PLANNER_PHASE_CONTRACT_PASS",
        )
        self.assertFalse(self.acceptance["production_runtime_ready"])

    def test_two_pass_contract_has_blind_and_balanced_boundaries(self) -> None:
        implementation = self.acceptance["implementation"]
        self.assertEqual(implementation["pass_a"], "BLIND_HYPOTHESIS")
        self.assertEqual(implementation["pass_b"], "MEMORY_CRITIQUE")
        self.assertIn("source_primary", implementation["pass_a_forbidden_inputs"])
        self.assertIn("historical outcome", implementation["pass_a_forbidden_inputs"])
        self.assertEqual(len(implementation["balanced_memory_roles"]), 6)
        self.assertTrue(implementation["strict_json_type_validation"])
        self.assertTrue(implementation["target_directness_validation"])
        self.assertTrue(implementation["sector_plausibility_validation"])
        self.assertFalse(implementation["sector_context_forwarded_to_pass_a"])

    def test_blind_benchmark_exceeds_goal_thresholds(self) -> None:
        benchmark = self.acceptance["blind_benchmark"]
        self.assertEqual(benchmark["benchmark_count"], 61)
        self.assertEqual(benchmark["archetype_benchmark_count"], 60)
        self.assertGreaterEqual(benchmark["top3_hit_rate"], 0.95)
        self.assertGreaterEqual(benchmark["top1_hit_rate"], 0.85)
        self.assertGreater(benchmark["abstention_count"], 0)
        self.assertEqual(benchmark["critical_guard_misroute_count"], 0)
        self.assertEqual(benchmark["impossible_archetype_assignment_count"], 0)
        self.assertTrue(benchmark["fake_provider"])
        self.assertFalse(benchmark["production_acceptance_credit"])
        self.assertEqual(
            benchmark["result_hash"],
            "97212312ba0ebc70089a3e3e8e7c16368de53fbbe960e735630a70603c2b0044",
        )

    def test_provider_failure_is_pending_and_cannot_finalize(self) -> None:
        contract = self.acceptance["provider_pending_contract"]
        self.assertTrue(contract["missing_provider_becomes_pending"])
        self.assertTrue(contract["provider_failure_becomes_pending"])
        self.assertTrue(contract["invalid_provider_output_becomes_pending"])
        self.assertTrue(contract["pending_preserves_prompt_hash"])
        self.assertTrue(contract["returned_invalid_response_preserves_raw_response_hash"])
        self.assertFalse(contract["pending_can_finalize_score_or_stage"])

    def test_real_smoke_is_reported_as_pending_without_acceptance_credit(self) -> None:
        smoke = self.acceptance["real_provider_smoke"]
        self.assertTrue(smoke["executed"])
        self.assertTrue(smoke["real_pass_a_completion_observed"])
        self.assertFalse(smoke["real_pass_b_completion_observed"])
        self.assertEqual(smoke["final_status"], "PLANNER_PENDING")
        self.assertEqual(smoke["failed_pass"], "MEMORY_CRITIQUE")
        self.assertFalse(smoke["production_acceptance_credit"])

    def test_every_hard_acceptance_count_is_zero(self) -> None:
        hard = self.acceptance["hard_acceptance"]
        for key, value in hard.items():
            if key.endswith("_count") or key == "critical_count_sum":
                self.assertEqual(value, 0, key)

    def test_phase6_operational_report_is_explicit_about_limits(self) -> None:
        report = (
            self.repo_root
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase6_two_pass_research_brain.md"
        ).read_text(encoding="utf-8")
        self.assertIn("TWO_PASS_PLANNER_PHASE_CONTRACT_PASS", report)
        self.assertIn("60/60", report)
        self.assertIn("57/60", report)
        self.assertIn("PlannerPending", report)
        self.assertIn("production_runtime_ready=false", report)
        self.assertIn("실제 LLM 성능", report)


if __name__ == "__main__":
    unittest.main()
