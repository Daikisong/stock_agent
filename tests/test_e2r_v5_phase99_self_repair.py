from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.researcher_mode.self_repair import (
    PARITY_FAILURE_CLASSES,
    PHASE99_PASS,
    PUBLIC_RESEARCH_ROUTES,
    REPAIR_CLUSTER_SPECS,
    SELF_REPAIR_LOOP_ORDER,
    compile_phase99_self_repair_audit,
    plan_alternate_public_routes,
    render_phase99_self_repair_summary,
    validate_llm_repair_queries,
)


class E2RV5Phase99SelfRepairTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = compile_phase99_self_repair_audit(cls.ROOT)

    def test_exact_twelve_failure_clusters_pass_focused_and_clean_rerun(self) -> None:
        self.assertEqual(len(PARITY_FAILURE_CLASSES), 12)
        self.assertEqual(len(REPAIR_CLUSTER_SPECS), 12)
        self.assertEqual(
            tuple(spec.failure_class for spec in REPAIR_CLUSTER_SPECS),
            PARITY_FAILURE_CLASSES,
        )
        self.assertEqual(self.audit["status"], PHASE99_PASS)
        self.assertEqual(self.audit["critical_count_sum"], 0)
        self.assertEqual(self.audit["self_repair_loop_order"], list(SELF_REPAIR_LOOP_ORDER))
        self.assertFalse(self.audit["fixed_iteration_cap_used"])
        self.assertTrue(
            all(
                row["focused_test_status"] == "PASS"
                and row["clean_rerun_status"] == "PASS"
                and row["final_status"] == "VERIFIED_REPAIRED"
                for row in self.audit["repair_clusters"]
            )
        )

    def test_clean_rerun_has_zero_same_evidence_variance(self) -> None:
        focused = self.audit["focused_test_run"]
        clean = self.audit["clean_rerun"]
        self.assertEqual(focused["test_count"], clean["test_count"])
        self.assertEqual(focused["passed_count"], clean["passed_count"])
        self.assertEqual(focused["outcome_hash"], clean["outcome_hash"])
        self.assertEqual(clean["same_evidence_replay_variance"], 0)

    def test_duplicate_query_returns_failure_context_to_llm_without_fallback(self) -> None:
        result = validate_llm_repair_queries(
            executed_queries=("Example issuer 2026Q2 earnings call allocation",),
            suggested_queries=(
                "  example   issuer 2026q2 EARNINGS call allocation ",
            ),
        )
        self.assertEqual(result.status, "RETRY_LLM_REQUIRED")
        self.assertEqual(result.accepted_queries, ())
        self.assertIn(
            "IDENTICAL_OR_NORMALIZED_DUPLICATE_QUERY",
            result.rejection_reasons,
        )
        self.assertEqual(result.query_generation_authority, "LLM_RESEARCH_SUPERVISOR")
        self.assertFalse(result.deterministic_query_synthesis)
        self.assertNotIn("suggested_queries", result.score_gap_context)

    def test_novel_llm_query_is_validated_verbatim_but_gold_origin_is_rejected(
        self,
    ) -> None:
        query = "Example issuer 2026Q2 filed capacity commissioning schedule"
        accepted = validate_llm_repair_queries(
            executed_queries=("Example issuer annual report capacity",),
            suggested_queries=(query,),
        )
        self.assertEqual(accepted.status, "ACCEPTED")
        self.assertEqual(accepted.accepted_queries, (query,))

        rejected = validate_llm_repair_queries(
            executed_queries=(),
            suggested_queries=("Gold expected source URL for target",),
            provenance_by_query={
                "Gold expected source URL for target": "GOLD_BENCHMARK",
            },
        )
        self.assertEqual(rejected.status, "RETRY_LLM_REQUIRED")
        self.assertIn(
            "GOLD_QUERY_OR_PROVENANCE_FORBIDDEN",
            rejected.rejection_reasons,
        )

    def test_provider_failure_tries_another_public_route_then_exactly_blocks(
        self,
    ) -> None:
        alternate = plan_alternate_public_routes(
            failed_route="ISSUER_IR",
            attempted_routes=("DART", "ISSUER_IR"),
        )
        self.assertEqual(alternate.status, "ALTERNATE_PUBLIC_ROUTE_REQUIRED")
        self.assertTrue(alternate.remaining_public_routes)
        self.assertNotIn("DART", alternate.remaining_public_routes)
        self.assertIsNone(alternate.deterministic_literal_query)
        self.assertFalse(alternate.canary_goal_complete)

        exhausted = plan_alternate_public_routes(
            failed_route="GENERAL_WEB_FALLBACK",
            attempted_routes=PUBLIC_RESEARCH_ROUTES,
        )
        self.assertEqual(exhausted.status, "ALL_PUBLIC_ROUTES_EXHAUSTED")
        self.assertEqual(exhausted.remaining_public_routes, ())
        self.assertEqual(
            exhausted.exact_blocker,
            "ALL_PUBLIC_ROUTES_EXHAUSTED:GENERAL_WEB_FALLBACK",
        )
        self.assertFalse(exhausted.canary_goal_complete)

    def test_live_canary_truth_stays_pending_despite_internal_pass(self) -> None:
        self.assertFalse(self.audit["production_readiness_authority"])
        self.assertFalse(self.audit["canary_goal_complete"])
        by_target = {
            row["target_id"]: row
            for row in self.audit["live_canaries"]["targets"]
        }
        self.assertEqual(by_target["005930"]["status"], "RESEARCH_CHECKPOINT_PENDING")
        self.assertEqual(by_target["000660"]["status"], "LIVE_RESEARCH_NOT_STARTED")
        blockers = self.audit["canary_completion_blockers"]
        self.assertIn("LIVE_RESEARCH_CHECKPOINT_PENDING:005930", blockers)
        self.assertIn("LIVE_RESEARCH_NOT_STARTED:000660", blockers)
        self.assertIn(
            "CODEX_PROVIDER_USAGE_LIMIT_UNTIL_2026-07-20T03:58:00+09:00",
            blockers,
        )

    def test_missing_live_manifests_are_exact_pending_not_fake_completion(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            audit = compile_phase99_self_repair_audit(directory)
        self.assertFalse(audit["canary_goal_complete"])
        self.assertEqual(audit["live_canaries"]["targets"], [])
        self.assertIn(
            "LIVE_CANARY_TARGET_REGISTRY_MISSING_OR_EMPTY",
            audit["canary_completion_blockers"],
        )

    def test_committed_audit_and_required_summary_are_reproducible(self) -> None:
        committed_audit = json.loads(
            (
                self.ROOT / "docs/operational/e2r_v5_self_repair_audit.json"
            ).read_text(encoding="utf-8")
        )
        committed_summary = (
            self.ROOT / "docs/operational/e2r_v5_self_repair_summary.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(committed_audit, self.audit)
        self.assertEqual(
            committed_summary,
            render_phase99_self_repair_summary(self.audit),
        )
        self.assertIn("MEANINGFUL_E2R_RESEARCHER_PARITY_READY", committed_summary)
        self.assertIn("선언은 허용되지 않는다", committed_summary)


if __name__ == "__main__":
    unittest.main()
