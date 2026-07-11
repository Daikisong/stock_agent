from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import CurrentAtomicDecisionBuilder


class LiveCurrentAtomicDecisionTest(unittest.TestCase):
    def test_direct_live_claim_with_provenance_enters_pending_atomic_decision(self) -> None:
        text = "삼성전자는 2026년 1분기 메모리 ASP가 상승했다고 공식 발표했다."
        content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        satisfaction = tuple(
            {
                "source_task_id": f"TASK-{index}",
                "target_id": "005930",
                "primitive_id": primitive,
                "status": (
                    "DIRECT_TASK_SATISFIED" if index == 5 else "SOURCE_EXHAUSTED"
                ),
                "original_gap_open": index != 5,
                "accepted_claim_ids": (["CLM-LIVE"] if index == 5 else []),
                "accepted_mapping_ids": (["MAP-LIVE"] if index == 5 else []),
            }
            for index, primitive in enumerate(
                (
                    "customer_preorder_or_allocation",
                    "revenue_visibility_contract",
                    "hbm_capacity_constraint",
                    "hbm_capacity_pre_sold",
                    "memory_price_increase_mentioned",
                    "medium_term_revision_visibility",
                ),
                1,
            )
        )
        accepted = ({
            "claim_id": "CLM-LIVE",
            "target_id": "005930",
            "accepted": True,
            "directness": "DIRECT",
            "temporal_status": "CURRENT",
            "semantic_status": "PASS",
            "mapping_ids": ["MAP-LIVE"],
        },)
        provenance = ({
            "claim_id": "CLM-LIVE",
            "target_id": "005930",
            "available_date": "2026-04-30",
            "content_sha256": content_hash,
            "source_ids": ["FETCH-LIVE", "issuer-newsroom:live"],
            "anchor_ids": ["ANCH-LIVE"],
            "mapping_ids": ["MAP-LIVE"],
            "directness": "DIRECT",
            "temporal_status": "CURRENT",
            "mapping_status": "ACCEPTED",
            "fetched": True,
            "anchor_verified": True,
            "source_proxy_only": False,
        },)

        result = CurrentAtomicDecisionBuilder().build(
            as_of_date="2026-07-10",
            source_task_satisfaction=satisfaction,
            gap_status_rows=(),
            accepted_current_claims=accepted,
            claim_provenance=provenance,
            controlled_probe=True,
        )

        decision = result.decisions[0]
        self.assertEqual(len(result.claims), 1)
        self.assertEqual(decision.accepted_claim_ids, ("CLM-LIVE",))
        self.assertEqual(decision.score_type, "NO_SCORE")
        self.assertEqual(decision.canonical_stage, "0")
        self.assertFalse(decision.score_valid)
        self.assertGreater(decision.raw_reference_score, 0)
        self.assertEqual(
            sum(item.state == "PRESENT_CURRENT" for item in result.primitive_states),
            1,
        )

        with self.assertRaisesRegex(ValueError, "lacks provenance"):
            CurrentAtomicDecisionBuilder().build(
                as_of_date="2026-07-10",
                source_task_satisfaction=satisfaction,
                gap_status_rows=(),
                accepted_current_claims=accepted,
                controlled_probe=True,
            )

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
            controlled_probe=True,
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
