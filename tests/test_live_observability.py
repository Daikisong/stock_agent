from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import compile_live_observability


REPO_ROOT = Path(__file__).resolve().parents[1]


class LiveObservabilityTest(unittest.TestCase):
    def test_phase37_reports_cover_the_full_conversion_chain(self) -> None:
        funnel = json.loads(
            (REPO_ROOT / "docs/operational/e2r_live_conversion_funnel.json").read_text(
                encoding="utf-8"
            )
        )
        sla = json.loads(
            (REPO_ROOT / "docs/operational/e2r_live_runtime_sla.json").read_text(
                encoding="utf-8"
            )
        )
        providers = json.loads(
            (REPO_ROOT / "docs/operational/e2r_live_provider_performance.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertEqual(funnel["status"], "LIVE_CONVERSION_FUNNEL_PASS")
        self.assertEqual(funnel["critical_count_sum"], 0)
        self.assertEqual(set(funnel["stage_order"]), set(funnel["global_stage_counts"]))
        self.assertEqual(funnel["global_stage_counts"]["universe"], 2542)
        self.assertEqual(funnel["global_stage_counts"]["baseline_attempt"], 10168)
        for stage in funnel["stage_order"]:
            self.assertGreater(funnel["global_stage_counts"][stage], 0, stage)
        self.assertEqual(
            funnel["progress_policy"]["direct_original_gap_closure_count"], 1
        )
        self.assertEqual(
            funnel["progress_policy"]["source_task_shell_progress_credit"], 0
        )
        self.assertEqual(len(funnel["symbol_breakdown"]), 2542)
        self.assertEqual(len(funnel["candidate_breakdown"]), 419)
        samsung = next(
            row for row in funnel["symbol_breakdown"] if row["target_id"] == "005930"
        )
        self.assertEqual(samsung["stage_counts"]["accepted_claim"], 1)
        self.assertEqual(samsung["stage_counts"]["score_contribution"], 1)
        c06 = next(
            row for row in funnel["archetype_breakdown"]
            if row["archetype_id"] == "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
        )
        self.assertEqual(set(c06["stage_counts"]), set(funnel["stage_order"]))
        self.assertEqual(c06["stage_counts"]["primitive_closure"], 1)

        self.assertEqual(sla["status"], "LIVE_RUNTIME_SLA_OBSERVABILITY_PASS")
        self.assertEqual(sla["wall_clock_sla_status"], "UNKNOWN")
        self.assertEqual(
            sla["runtime_measurement_status"], "UPSTREAM_WALL_CLOCK_NOT_RECORDED"
        )
        self.assertTrue(sla["checkpoint"]["checkpoint_complete"])
        self.assertEqual(sla["determinism"]["variance_count"], 0)

        issuer_ir = next(
            row for row in providers["providers"] if row["provider"] == "IssuerIR"
        )
        self.assertEqual(issuer_ir["call_count"], 3)
        self.assertEqual(issuer_ir["failure_count"], 3)
        self.assertEqual(issuer_ir["success_rate"], 0.0)
        self.assertIn("CodexClaimExtractor", providers["unknown_call_count_providers"])

    def test_frozen_phase36_leaves_recompile_to_same_observability_counts(self) -> None:
        acceptance_input = (
            REPO_ROOT
            / "output/live_acceptance/2026-07-10/full/current_operation_input_manifest.json"
        )
        if not acceptance_input.exists():
            self.skipTest("ignored Phase 36 live acceptance leaves are not present")

        reports = compile_live_observability(
            config_path=REPO_ROOT / "configs/e2r_live_observability_v1.json"
        )

        funnel = reports["funnel"]
        self.assertEqual(funnel["critical_count_sum"], 0)
        self.assertEqual(funnel["rates"]["baseline_coverage"], 1.0)
        self.assertEqual(funnel["rates"]["direct_original_gap_closure_rate"], 0.1)
        self.assertEqual(
            funnel["hard_acceptance_counts"]["symbol_stage_projection_mismatch"],
            0,
        )


if __name__ == "__main__":
    unittest.main()
