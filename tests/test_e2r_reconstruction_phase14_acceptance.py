from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime import (
    CONVERSION_FUNNEL_AUDIT_SCHEMA_VERSION,
    CONVERSION_FUNNEL_SCHEMA_VERSION,
    FunnelMetricScope,
    FunnelStage,
)
from tests import test_conversion_funnel_observability as funnel_fixture


class E2RReconstructionPhase14AcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.acceptance = json.loads(
            (
                cls.repo_root
                / "e2r_reconstruction_phase14_acceptance.json"
            ).read_text(encoding="utf-8")
        )
        fixture_class = funnel_fixture.ConversionFunnelObservabilityTest
        if not hasattr(fixture_class, "result"):
            fixture_class.setUpClass()
        cls.result = fixture_class.result

    def test_phase_status_schema_and_stage_chain_are_frozen(self) -> None:
        self.assertEqual(self.acceptance["phase"], 14)
        self.assertEqual(
            self.acceptance["status"],
            "CONVERSION_FUNNEL_OBSERVABILITY_PASS",
        )
        self.assertFalse(self.acceptance["production_runtime_ready"])
        self.assertEqual(
            CONVERSION_FUNNEL_SCHEMA_VERSION,
            "e2r_conversion_funnel_v1",
        )
        self.assertEqual(
            CONVERSION_FUNNEL_AUDIT_SCHEMA_VERSION,
            "e2r_conversion_funnel_audit_v1",
        )
        self.assertEqual(
            set(self.acceptance["canonical_funnel_stages"]),
            {"CANDIDATE", *(item.value for item in FunnelStage)},
        )

    def test_frozen_leaf_and_metric_hashes_match_recomputed_result(self) -> None:
        frozen = self.acceptance["frozen_funnel_run"]
        self.assertEqual(self.result.run_id, frozen["run_id"])
        self.assertEqual(self.result.as_of_date, frozen["as_of_date"])
        self.assertEqual(len(self.result.candidates), frozen["candidate_count"])
        self.assertEqual(
            len(self.result.stage_leaves),
            frozen["stage_leaf_count"],
        )
        self.assertEqual(
            len(self.result.metric_rows),
            frozen["metric_row_count"],
        )
        self.assertEqual(self.result.audit["result_hash"], frozen["leaf_hash"])
        self.assertEqual(self.result.audit["metric_hash"], frozen["metric_hash"])
        actual_stage_counts = {
            stage.value: sum(
                item.stage == stage.value for item in self.result.stage_leaves
            )
            for stage in FunnelStage
        }
        self.assertEqual(actual_stage_counts, self.acceptance["stage_counts"])

    def test_primary_progress_is_direct_gap_closure_not_shell_or_claim_total(self) -> None:
        metric = next(
            item
            for item in self.result.metric_rows
            if item.scope_type == FunnelMetricScope.GLOBAL.value
        )
        frozen = self.acceptance["conversion_metrics"]
        self.assertEqual(metric.source_task_count, frozen["source_task_shell_count"])
        self.assertEqual(metric.original_gap_count, frozen["original_gap_count"])
        self.assertEqual(metric.accepted_claim_count, 3)
        self.assertEqual(
            metric.direct_original_gap_closure_count,
            frozen["direct_original_gap_closure_count"],
        )
        self.assertEqual(
            metric.meaningful_progress_count,
            frozen["meaningful_progress_count"],
        )
        self.assertEqual(metric.task_shell_progress_credit_count, 0)
        self.assertEqual(metric.relevant_document_rate, 0.8)
        self.assertEqual(metric.accepted_claim_rate, 0.75)
        self.assertEqual(metric.direct_original_gap_closure_rate, 0.2)
        self.assertLess(
            metric.direct_original_gap_closure_count,
            metric.accepted_claim_count,
        )

    def test_terminal_pending_archetype_and_usage_metrics_are_explicit(self) -> None:
        global_metric = next(
            item
            for item in self.result.metric_rows
            if item.scope_type == FunnelMetricScope.GLOBAL.value
        )
        self.assertEqual(
            global_metric.terminal_outcome_counts,
            self.acceptance["terminal_outcomes"],
        )
        self.assertEqual(
            global_metric.pending_reason_counts,
            self.acceptance["pending_reason_counts"],
        )
        self.assertEqual(global_metric.cost_usd, 0.55)
        self.assertEqual(global_metric.runtime_seconds, 28.0)
        self.assertEqual(global_metric.query_usage_count, 5)
        self.assertEqual(global_metric.result_usage_count, 5)
        self.assertEqual(global_metric.fetch_usage_count, 5)
        scope_counts = {
            scope.value: sum(
                item.scope_type == scope.value for item in self.result.metric_rows
            )
            for scope in FunnelMetricScope
        }
        self.assertEqual(
            scope_counts,
            {"GLOBAL": 1, "CANDIDATE": 5, "ARCHETYPE": 6},
        )

    def test_canonical_integration_and_known_bad_contract_are_recorded(self) -> None:
        integration = self.acceptance["canonical_phase_integration"]
        self.assertTrue(
            all(
                value
                for key, value in integration.items()
                if key not in {"production_acceptance_credit"}
            )
        )
        self.assertFalse(integration["production_acceptance_credit"])
        self.assertTrue(all(self.acceptance["lineage_contract"].values()))
        self.assertTrue(all(self.acceptance["known_bad_detection"].values()))
        self.assertTrue(
            all(value == 0 for value in self.acceptance["hard_acceptance"].values())
        )

    def test_independent_audit_report_and_production_boundary_are_explicit(self) -> None:
        audit = self.acceptance["integrity_audit"]
        self.assertEqual(audit["status"], "CONVERSION_FUNNEL_OBSERVABILITY_PASS")
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(
            audit["critical_check_count"],
            len(self.result.audit["critical_counts"]),
        )
        self.assertTrue(
            all(value == 0 for value in self.result.audit["critical_counts"].values())
        )
        self.assertFalse(self.result.production_runtime_ready)

        report = (
            self.repo_root
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase14_conversion_funnel.md"
        ).read_text(encoding="utf-8")
        self.assertIn("CONVERSION_FUNNEL_OBSERVABILITY_PASS", report)
        self.assertIn("SourceTask shell의 progress credit은 항상 0", report)
        self.assertIn("direct original-gap closure", report)
        self.assertIn("rerouted claim", report)
        self.assertIn("production_runtime_ready=false", report)
        self.assertIn("Phase 15", report)


if __name__ == "__main__":
    unittest.main()
