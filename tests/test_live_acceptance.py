from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import run_full_live_acceptance


REPO_ROOT = Path(__file__).resolve().parents[1]


class FullLiveAcceptanceTest(unittest.TestCase):
    def test_operational_report_proves_all_phase36_minimums(self) -> None:
        report = json.loads(
            (REPO_ROOT / "docs/operational/e2r_live_acceptance_report.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertEqual(report["status"], "FULL_LIVE_ACCEPTANCE_PASS")
        self.assertEqual(report["critical_count_sum"], 0)
        evidence = report["current_census_evidence"]
        self.assertGreater(evidence["eligible_universe_count"], 1000)
        self.assertEqual(
            evidence["baseline_lane_count"],
            evidence["required_baseline_lane_count"],
        )
        for key in (
            "trigger_count",
            "selected_l3_count",
            "selected_l4_count",
            "real_planner_call_count",
            "source_task_count",
            "real_fresh_fetched_document_count",
            "accepted_current_claim_count",
            "claim_provenance_count",
            "atomic_decision_count",
        ):
            self.assertGreater(evidence[key], 0, key)
        self.assertEqual(report["determinism"]["variance_count"], 0)
        self.assertEqual(
            report["determinism"]["first_leaf_hash"],
            report["determinism"]["second_leaf_hash"],
        )
        claim = report["accepted_claim_proof"]
        self.assertEqual(claim["score_type"], "NO_SCORE")
        self.assertFalse(claim["score_valid"])
        self.assertEqual(claim["canonical_stage"], "0")
        self.assertTrue(claim["material_gap_ids"])

    def test_frozen_live_inputs_recompile_with_zero_variance(self) -> None:
        probe = REPO_ROOT / "output/live_acceptance/2026-07-10/claim_probe_samsung_q1"
        census = REPO_ROOT / "output/census/live_2026-07-10/current_operation_input_manifest.json"
        if not probe.exists() or not census.exists():
            self.skipTest("ignored authorized live leaves are not present")

        result = run_full_live_acceptance(
            config_path=REPO_ROOT / "configs/e2r_live_acceptance_v1.json"
        )

        self.assertEqual(result.status, "FULL_LIVE_ACCEPTANCE_PASS")
        self.assertEqual(result.report["critical_count_sum"], 0)
        self.assertEqual(result.report["determinism"]["variance_count"], 0)
        samsung = next(
            item
            for item in result.current_result.atomic_decisions
            if item.target_id == "005930"
        )
        self.assertEqual(samsung.accepted_claim_ids, ("CLM-94438945025662847395",))
        self.assertEqual(samsung.score_type, "NO_SCORE")
        self.assertEqual(samsung.canonical_stage, "0")


if __name__ == "__main__":
    unittest.main()
