from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import CurrentOperationRunnerInputBuilder


REPO_ROOT = Path(__file__).resolve().parents[1]


class CurrentOperationInputBuilderTest(unittest.TestCase):
    def test_real_live_leaves_build_full_valid_production_manifest(self) -> None:
        live_root = REPO_ROOT / "output/live_materialization/2026-07-10"
        if not (live_root / "current_operation_input_manifest.json").exists():
            self.skipTest("ignored live materialization artifacts are not present")
        inputs, audit = CurrentOperationRunnerInputBuilder().build_from_live_root(
            as_of_date="2026-07-10",
            live_root=live_root,
            run_profile=REPO_ROOT / "configs/e2r_production_daily_v1.json",
        )

        self.assertGreater(len(inputs.universe), 1000)
        self.assertEqual(len(inputs.baseline_lanes), len(inputs.universe) * 4)
        self.assertFalse(inputs.config.test_mode)
        self.assertTrue(inputs.config.require_claim_provenance)
        self.assertEqual(len(inputs.deep_executions), inputs.config.max_deep_candidates)
        self.assertEqual(audit["critical_count_sum"], 0)

    def test_operational_audit_proves_authorized_cli_no_longer_needs_manual_manifest(self) -> None:
        path = REPO_ROOT / "docs/operational/e2r_current_operation_input_builder_audit.json"
        audit = json.loads(path.read_text(encoding="utf-8"))

        self.assertEqual(audit["status"], "PHASE_31_ACCEPTED")
        self.assertEqual(audit["evaluator_critical_count_sum"], 0)
        self.assertEqual(sum(audit["critical_counts"].values()), 0)
        self.assertFalse(audit["safety"]["user_manual_manifest_required"])


if __name__ == "__main__":
    unittest.main()
