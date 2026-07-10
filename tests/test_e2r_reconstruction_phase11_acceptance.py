from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.replay import HISTORICAL_REPLAY_PARITY_SCHEMA_VERSION
from e2r.research_brain.runtime import (
    CURRENT_OPERATION_SCHEMA_VERSION,
    RUN_MODE_MARKER_SCHEMA_VERSION,
    CanonicalRunMode,
    CurrentDeepOutcome,
)


class E2RReconstructionPhase11AcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.acceptance = json.loads(
            (cls.repo_root / "e2r_reconstruction_phase11_acceptance.json").read_text(
                encoding="utf-8"
            )
        )

    def test_status_is_phase_scoped_and_not_production_ready(self) -> None:
        self.assertEqual(self.acceptance["phase"], 11)
        self.assertEqual(
            self.acceptance["status"],
            "HISTORICAL_CURRENT_MODE_SEPARATION_PASS",
        )
        self.assertFalse(self.acceptance["production_runtime_ready"])
        self.assertEqual(
            HISTORICAL_REPLAY_PARITY_SCHEMA_VERSION,
            "e2r_historical_replay_parity_v1",
        )
        self.assertEqual(CURRENT_OPERATION_SCHEMA_VERSION, "e2r_current_operation_mode_v1")
        self.assertEqual(RUN_MODE_MARKER_SCHEMA_VERSION, "e2r_run_mode_marker_v1")

    def test_historical_registry_thresholds_and_hash_are_frozen(self) -> None:
        replay = self.acceptance["historical_replay"]
        self.assertEqual(replay["status"], "HISTORICAL_REPLAY_PARITY_PASS")
        self.assertEqual(replay["mode"], CanonicalRunMode.HISTORICAL_REPLAY.value)
        self.assertEqual(replay["registry_archetype_count"], 36)
        self.assertEqual(replay["registry_covered_archetype_count"], 36)
        self.assertEqual(replay["registry_coverage_rate"], 1.0)
        self.assertGreaterEqual(replay["top3_accuracy"], 0.95)
        self.assertGreaterEqual(replay["top1_accuracy"], 0.85)
        self.assertGreaterEqual(replay["mapping_precision"], 0.95)
        self.assertGreaterEqual(replay["positive_recall"], 0.90)
        self.assertGreaterEqual(replay["guard_accuracy"], 0.95)
        self.assertEqual(replay["guard_probe_count"], 5)
        self.assertEqual(replay["guard_probe_kind_count"], 5)
        self.assertEqual(replay["guard_probe_pass_rate"], 1.0)
        self.assertEqual(
            set(replay["guard_probe_counts"]),
            {
                "POSITIVE",
                "COUNTER_GUARD",
                "WRONG_SUBJECT",
                "OLD_RISK",
                "SOURCE_MISSING",
            },
        )
        self.assertEqual(replay["critical_count_sum"], 0)
        self.assertEqual(
            replay["leaf_hash"],
            "236ae82327e773a2062a18ab0a409a0dc2688a476818f60154d404ddc08b899d",
        )
        self.assertFalse(replay["production_runtime_ready"])
        full = self.acceptance["full_registry_compile_reverification"]
        self.assertEqual(full["historical_case_count"], 10920)
        self.assertEqual(full["registry_archetype_coverage_count"], 36)
        self.assertEqual(full["top3_archetype_hit_rate"], 1.0)
        self.assertEqual(full["critical_count_sum"], 0)
        self.assertEqual(
            full["result_hash"],
            "96d947b64fd66a708facc2cd69a484a8f02159d85f603dbfde688aabd784d3da",
        )

    def test_historical_source_and_prompt_safety_are_explicit(self) -> None:
        replay = self.acceptance["historical_replay"]
        contract = self.acceptance["historical_contract"]
        self.assertEqual(
            replay["url_backed_archetype_count"]
            + replay["exact_source_blocker_archetype_count"],
            36,
        )
        self.assertEqual(replay["source_proxy_score_credit_count"], 0)
        self.assertEqual(replay["future_leakage_count"], 0)
        self.assertEqual(replay["current_watchlist_eligible_count"], 0)
        self.assertTrue(contract["expected_archetype_stage_outcome_evaluator_only"])
        self.assertTrue(
            contract["benchmark_request_id_is_evidence_hash_not_expected_label"]
        )
        self.assertTrue(contract["single_frozen_as_of_required"])
        self.assertTrue(contract["not_attempted_requires_exact_reason"])
        self.assertTrue(contract["source_proxy_never_scores"])

    def test_current_mode_is_selective_and_every_deep_candidate_terminates(self) -> None:
        current = self.acceptance["current_operation"]
        contract = self.acceptance["current_contract"]
        self.assertEqual(
            current["status"],
            "CURRENT_OPERATION_MODE_SEPARATION_PASS",
        )
        self.assertEqual(current["mode"], CanonicalRunMode.CURRENT_OPERATION.value)
        self.assertLess(
            current["materialized_current_archetype_count"],
            current["canonical_registry_archetype_count"],
        )
        self.assertEqual(
            set(current["deep_outcome_counts"]),
            {item.value for item in CurrentDeepOutcome},
        )
        self.assertTrue(all(current["deep_outcome_counts"].values()))
        self.assertEqual(
            current["selected_deep_candidate_count"],
            current["deep_terminal_outcome_count"],
        )
        self.assertLessEqual(
            current["selected_deep_candidate_count"],
            current["max_deep_candidates"],
        )
        self.assertEqual(current["archetype_quota_count"], 0)
        self.assertEqual(current["forced_archetype_materialization_count"], 0)
        self.assertEqual(current["historical_replay_input_count"], 0)
        self.assertEqual(current["trigger_score_evidence_count"], 0)
        self.assertTrue(contract["missing_current_archetype_row_allowed"])
        self.assertTrue(contract["score_claim_requires_current_open_source_backed"])
        self.assertEqual(
            current["leaf_hash"],
            "e6142d30f5360fb61b3fa519123e64539cd0cb4b0051ceac8c7ac4f80ed72fd1",
        )
        self.assertFalse(current["production_runtime_ready"])

    def test_independent_mode_separation_audit_has_no_critical_gap(self) -> None:
        audit = self.acceptance["mode_separation_audit"]
        self.assertEqual(
            audit["status"],
            "HISTORICAL_CURRENT_MODE_SEPARATION_PASS",
        )
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(all(value == 0 for value in audit["critical_counts"].values()))
        self.assertEqual(
            audit["result_hash"],
            "702400d8e940a96ba194bb930fbb5409b11ad273693d1f584288c4d97cbc4836",
        )
        self.assertFalse(audit["production_runtime_ready"])
        output_contract = self.acceptance["output_contract"]
        self.assertTrue(
            output_contract["historical_planner_and_evaluator_artifacts_separate"]
        )

    def test_report_explains_blockers_selectivity_and_fixture_boundary(self) -> None:
        report = (
            self.repo_root
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase11_historical_current_separation.md"
        ).read_text(encoding="utf-8")
        self.assertIn("HISTORICAL_CURRENT_MODE_SEPARATION_PASS", report)
        self.assertIn("36/36", report)
        self.assertIn("exact blocker", report)
        self.assertIn("답안지", report)
        self.assertIn("archetype", report)
        self.assertIn("PROVIDER_PENDING", report)
        self.assertIn("production_runtime_ready=false", report)


if __name__ == "__main__":
    unittest.main()
