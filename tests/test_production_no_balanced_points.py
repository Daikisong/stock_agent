from __future__ import annotations

import ast
import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import CurrentAtomicDecisionBuilder


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "src/e2r/research_brain/runtime/live_materialization/current_atomic_decision.py"


class ProductionNoBalancedPointsTests(unittest.TestCase):
    def test_legacy_builder_rejects_implicit_production_use(self) -> None:
        with self.assertRaisesRegex(ValueError, "controlled-probe-only"):
            CurrentAtomicDecisionBuilder().build(
                as_of_date="2026-07-11",
                source_task_satisfaction=(),
                gap_status_rows=(),
                accepted_current_claims=(),
            )

    def test_balanced_points_function_is_absent(self) -> None:
        tree = ast.parse(MODULE.read_text())
        function_names = {
            node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
        }
        self.assertNotIn("_balanced_points", function_names)
        self.assertIn("_controlled_probe_points_test_only", function_names)

    def test_only_controlled_probe_callers_use_legacy_builder(self) -> None:
        production_callers = []
        for path in (ROOT / "src/e2r").rglob("*.py"):
            if path == MODULE:
                continue
            text = path.read_text()
            if "CurrentAtomicDecisionBuilder().build(" not in text:
                continue
            if path.name != "live_acceptance.py" or "controlled_probe=True" not in text:
                production_callers.append(str(path.relative_to(ROOT)))
        self.assertEqual(production_callers, [])

    def test_static_lockout_audit_has_zero_critical_counts(self) -> None:
        audit = json.loads(
            (ROOT / "docs/operational/e2r_legacy_scoring_lockout_audit.json").read_text()
        )
        self.assertEqual(audit["status"], "LEGACY_SCORING_PATH_LOCKOUT_PASS")
        self.assertEqual(sum(audit["critical_counts"].values()), 0)
        self.assertFalse(audit["controlled_probe_path"]["readiness_eligible"])


if __name__ == "__main__":
    unittest.main()
