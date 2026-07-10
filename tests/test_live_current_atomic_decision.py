from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import CurrentAtomicDecisionBuilder


class LiveCurrentAtomicDecisionTest(unittest.TestCase):
    def test_claimless_material_gaps_are_atomic_no_score_stage_zero(self) -> None:
        satisfaction = tuple(
            {
                "source_task_id": f"TASK-{index}",
                "target_id": "000001",
                "primitive_id": primitive,
            }
            for index, primitive in enumerate(("p1", "p2", "p3"), 1)
        )
        gaps = tuple(
            {
                "source_task_id": f"TASK-{index}",
                "terminal_status": "SOURCE_PENDING",
            }
            for index in range(1, 4)
        )

        result = CurrentAtomicDecisionBuilder().build(
            as_of_date="2026-07-10",
            source_task_satisfaction=satisfaction,
            gap_status_rows=gaps,
            accepted_current_claims=(),
        )

        decision = result.decisions[0]
        self.assertEqual(decision.score_type, "NO_SCORE")
        self.assertIsNone(decision.score_value)
        self.assertFalse(decision.score_valid)
        self.assertEqual(decision.canonical_stage, "0")
        self.assertEqual(decision.decision_status, "PENDING")
        self.assertEqual(result.audit["critical_count_sum"], 0)

    def test_live_operational_atomic_audit_has_no_claimless_score(self) -> None:
        path = (
            Path(__file__).resolve().parents[1]
            / "docs"
            / "operational"
            / "e2r_live_atomic_score_audit.json"
        )
        audit = json.loads(path.read_text(encoding="utf-8"))

        self.assertEqual(audit["status"], "PHASE_30_ACCEPTED")
        self.assertEqual(audit["no_score_count"], 3)
        self.assertEqual(audit["stage_zero_pending_count"], 3)
        self.assertEqual(audit["score_valid_true_count"], 0)
        self.assertEqual(sum(audit["critical_counts"].values()), 0)


if __name__ == "__main__":
    unittest.main()
