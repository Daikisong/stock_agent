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
from e2r.research_brain.researcher_mode import self_repair


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

    def test_live_canary_truth_matches_current_target_state(self) -> None:
        self.assertFalse(self.audit["production_readiness_authority"])
        by_target = {
            row["target_id"]: row
            for row in self.audit["live_canaries"]["targets"]
        }
        self.assertEqual(set(by_target), {"005930", "000660"})
        blockers = self.audit["canary_completion_blockers"]
        expected_complete = bool(by_target) and not blockers and all(
            row["production_research_complete"] for row in by_target.values()
        )
        self.assertEqual(self.audit["canary_goal_complete"], expected_complete)
        for target_id, row in by_target.items():
            self.assertEqual(
                row["status"] == "PRODUCTION_RESEARCH_COMPLETE",
                row["production_research_complete"],
            )
            pending_blocker = f"LIVE_RESEARCH_CHECKPOINT_PENDING:{target_id}"
            not_started_blocker = f"LIVE_RESEARCH_NOT_STARTED:{target_id}"
            self.assertEqual(
                pending_blocker in blockers,
                row["status"]
                not in {"LIVE_RESEARCH_NOT_STARTED", "PRODUCTION_RESEARCH_COMPLETE"},
            )
            self.assertEqual(
                not_started_blocker in blockers,
                row["status"] == "LIVE_RESEARCH_NOT_STARTED",
            )
        usage_limit = self.audit["live_canaries"]
        usage_target_ids = usage_limit["provider_usage_limit_target_ids"]
        self.assertEqual(
            usage_limit["provider_usage_limit_detected"],
            bool(usage_target_ids),
        )
        self.assertEqual(
            sorted(
                blocker.split(":", 1)[1]
                for blocker in blockers
                if blocker.startswith("CODEX_PROVIDER_USAGE_LIMIT:")
            ),
            sorted(usage_target_ids),
        )
        self.assertTrue(set(usage_target_ids).issubset(by_target))

    def test_usage_limit_audit_reads_current_leaf_and_never_embeds_reset_date(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "output" / "researcher_mode" / "case" / "009999"
            target.mkdir(parents=True)
            manifest_path = target / "target_run_manifest.json"
            manifest = {
                "target_id": "009999",
                "production_research_complete": False,
                "provider_response_cache": {
                    "provider_usage_limit_detected": True,
                    "provider_usage_limit_reset_hints": [
                        "Aug 3rd, 2031 7:09 PM"
                    ],
                },
            }
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            (target / "research_supervisor_review.json").write_text(
                json.dumps(
                    {
                        "status": "NEXT_RESEARCH_REQUIRED",
                        "error": (
                            "ERROR: You've hit your usage limit. "
                            "try again at Aug 3rd, 2031 7:09 PM."
                        ),
                    }
                ),
                encoding="utf-8",
            )
            audit = self_repair._audit_active_provider_usage_limits(
                root=root,
                target_items=((manifest_path, manifest),),
            )
        self.assertTrue(audit["detected"])
        self.assertEqual(audit["target_ids"], ["009999"])
        self.assertEqual(audit["reset_hints"], ["Aug 3rd, 2031 7:09 PM"])
        self.assertEqual(
            audit["evidence_paths"],
            [
                "output/researcher_mode/case/009999/"
                "target_run_manifest.json",
                "output/researcher_mode/case/009999/"
                "research_supervisor_review.json"
            ],
        )

    def test_completed_target_ignores_historical_usage_limit_text(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target"
            target.mkdir()
            manifest_path = target / "target_run_manifest.json"
            manifest = {
                "target_id": "009999",
                "production_research_complete": True,
            }
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            (target / "research_supervisor_review.json").write_text(
                "usage limit; try again at Jan 1st, 2030 1:00 AM",
                encoding="utf-8",
            )
            audit = self_repair._audit_active_provider_usage_limits(
                root=root,
                target_items=((manifest_path, manifest),),
            )
        self.assertFalse(audit["detected"])
        self.assertEqual(audit["target_ids"], [])
        self.assertEqual(audit["reset_hints"], [])

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
        if self.audit["canary_goal_complete"]:
            self.assertIn("선언의 canary gate는 통과했다", committed_summary)
            self.assertNotIn("선언은 허용되지 않는다", committed_summary)
        else:
            self.assertIn("선언은 허용되지 않는다", committed_summary)


if __name__ == "__main__":
    unittest.main()
