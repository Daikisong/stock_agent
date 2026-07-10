from __future__ import annotations

import json
import unittest
from collections import Counter
from pathlib import Path

from e2r.research_brain.runtime import (
    CURRENT_OPERATION_RUNNER_AUDIT_SCHEMA_VERSION,
    CURRENT_OPERATION_RUNNER_SCHEMA_VERSION,
    AtomicScoreType,
    CensusDepthLevel,
    CurrentDeepOutcome,
    CurrentTriggerType,
    DailyBaselineLaneType,
)
from tests import test_current_operation_runner as current_runner_fixture


class E2RReconstructionPhase13AcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.acceptance = json.loads(
            (
                cls.repo_root
                / "e2r_reconstruction_phase13_acceptance.json"
            ).read_text(encoding="utf-8")
        )
        fixture_class = current_runner_fixture.CurrentOperationRunnerTest
        if not hasattr(fixture_class, "result"):
            fixture_class.setUpClass()
        cls.result = fixture_class.result

    def test_phase_status_schema_and_daily_pipeline_are_frozen(self) -> None:
        self.assertEqual(self.acceptance["phase"], 13)
        self.assertEqual(
            self.acceptance["status"],
            "CURRENT_OPERATIONAL_BRAIN_PASS",
        )
        self.assertFalse(self.acceptance["production_runtime_ready"])
        self.assertEqual(
            CURRENT_OPERATION_RUNNER_SCHEMA_VERSION,
            "e2r_current_operation_runner_v1",
        )
        self.assertEqual(
            CURRENT_OPERATION_RUNNER_AUDIT_SCHEMA_VERSION,
            "e2r_current_operation_runner_audit_v1",
        )
        self.assertTrue(
            all(self.acceptance["canonical_daily_pipeline"].values())
        )

    def test_frozen_run_matches_full_universe_leaf_artifacts(self) -> None:
        frozen = self.acceptance["frozen_daily_run"]
        result = self.result
        self.assertEqual(result.run_id, frozen["run_id"])
        self.assertEqual(result.as_of_date, frozen["as_of_date"])
        self.assertEqual(len(result.universe), frozen["full_universe_count"])
        self.assertEqual(
            len(result.baseline_lanes),
            frozen["baseline_lane_count"],
        )
        self.assertEqual(
            len(result.source_timelines),
            frozen["source_timeline_count"],
        )
        self.assertEqual(
            len(result.thesis_states),
            frozen["last_effective_thesis_count"],
        )
        self.assertEqual(
            len(result.stage_statuses),
            frozen["census_stage_status_count"],
        )
        self.assertEqual(result.audit["result_hash"], frozen["leaf_hash"])

    def test_baseline_depth_and_all_trigger_families_never_use_quota(self) -> None:
        baseline = self.acceptance["baseline_contract"]
        self.assertEqual(
            set(baseline["required_lanes"]),
            {item.value for item in DailyBaselineLaneType},
        )
        self.assertFalse(baseline["baseline_is_score_evidence"])

        expected_depths = self.acceptance["depth_policy"]
        actual_depths = {
            depth.value: sum(
                depth.value in item.completed_depths
                for item in self.result.depth_decisions
            )
            for depth in CensusDepthLevel
        }
        self.assertEqual(
            actual_depths,
            {item.value: expected_depths[item.value] for item in CensusDepthLevel},
        )
        self.assertFalse(expected_depths["selection_uses_archetype_quota"])
        self.assertFalse(expected_depths["selection_uses_recent_stage_cutoff"])

        triggers = self.acceptance["daily_trigger_contract"]
        self.assertEqual(
            set(triggers["trigger_family_counts"]),
            {item.value for item in CurrentTriggerType},
        )
        self.assertEqual(triggers["trigger_used_as_score_evidence_count"], 0)
        self.assertEqual(triggers["market_news_used_as_score_evidence_count"], 0)

    def test_source_tasks_are_bounded_and_each_deep_candidate_terminates(self) -> None:
        tasks = self.acceptance["bounded_source_tasks"]
        self.assertEqual(len(self.result.source_tasks), tasks["task_leaf_count"])
        self.assertTrue(
            all(
                item.max_queries > 0
                and item.max_candidates > 0
                and item.max_fetches > 0
                and item.max_retries >= 0
                and item.stop_condition == "stop_on_resolution"
                for item in self.result.source_tasks
            )
        )
        refs = tuple(
            task_id
            for execution in self.result.deep_executions
            for task_id in execution.source_task_ids
        )
        self.assertCountEqual(
            refs,
            (item.task_id for item in self.result.source_tasks),
        )
        self.assertEqual(
            Counter(item.outcome for item in self.result.deep_executions),
            Counter(self.acceptance["terminal_outcomes"]),
        )
        self.assertEqual(
            set(self.acceptance["terminal_outcomes"]),
            {item.value for item in CurrentDeepOutcome},
        )

    def test_atomic_status_open_thesis_and_watchlist_safety_are_preserved(self) -> None:
        projection = self.acceptance["atomic_status_projection"]
        self.assertEqual(
            Counter(item.canonical_stage for item in self.result.stage_statuses),
            Counter(projection["stage_counts"]),
        )
        self.assertEqual(
            Counter(item.score_type for item in self.result.stage_statuses),
            Counter(projection["score_type_counts"]),
        )
        self.assertEqual(projection["pending_finalized_score_count"], 0)
        self.assertEqual(
            sum(
                item.score_type == AtomicScoreType.FULL_E2R_100.value
                for item in self.result.stage_statuses
            ),
            1,
        )

        thesis = self.acceptance["last_effective_thesis_contract"]
        self.assertTrue(thesis["old_open_claim_preserved_as_of_2026_06_30"])
        self.assertEqual(thesis["recent_cutoff_stage_drop_count"], 0)
        self.assertTrue(
            any(
                claim.observed_date == thesis["oldest_open_claim_observed_date"]
                and claim.current_open
                for claim in self.result.claims
            )
        )
        watchlist = self.acceptance["watchlist_contract"]
        self.assertEqual(len(self.result.watchlist), watchlist["row_count"])
        self.assertEqual(watchlist["direct_investment_recommendation_count"], 0)
        required_fields = {
            "score_type",
            "confidence",
            "claim_ids",
            "missing_conditions",
            "gap_ids",
            "next_action",
        }
        self.assertTrue(
            all(
                required_fields.issubset(item.to_dict())
                for item in self.result.watchlist
            )
        )

    def test_independent_audit_report_and_production_boundary_are_explicit(self) -> None:
        audit = self.acceptance["integrity_audit"]
        self.assertEqual(audit["status"], "BOUNDED_DAILY_CENSUS_PASS")
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(
            audit["critical_check_count"],
            len(self.result.audit["critical_counts"]),
        )
        self.assertTrue(
            all(value == 0 for value in self.result.audit["critical_counts"].values())
        )
        self.assertTrue(all(self.acceptance["known_bad_detection"].values()))
        self.assertTrue(
            all(value == 0 for value in self.acceptance["hard_acceptance"].values())
        )
        boundary = self.acceptance["production_boundary"]
        self.assertTrue(boundary["production_bounded_contract_ready"])
        self.assertFalse(boundary["live_execution_observed"])
        self.assertFalse(boundary["production_runtime_ready"])

        report = (
            self.repo_root
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase13_bounded_daily_census.md"
        ).read_text(encoding="utf-8")
        self.assertIn("CURRENT_OPERATIONAL_BRAIN_PASS", report)
        self.assertIn("stop_on_resolution", report)
        self.assertIn("current OPEN", report)
        self.assertIn("trigger는 “더 조사할 이유”", report)
        self.assertIn("production_runtime_ready=false", report)
        self.assertIn("Phase 14", report)


if __name__ == "__main__":
    unittest.main()
