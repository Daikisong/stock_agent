from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring.semantic_self_repair import (
    FAILURE_CLASSES,
    MAX_ITERATIONS,
    PASS_STATUS,
    compile_semantic_scoring_self_repair_audit,
    render_semantic_scoring_self_repair_summary,
)


class SemanticScoringSelfRepairTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = compile_semantic_scoring_self_repair_audit(
            repo_root=cls.ROOT
        )

    def test_exact_twelve_code_repair_iterations_resolve_true_replays(self) -> None:
        self.assertEqual(self.audit["status"], PASS_STATUS)
        self.assertEqual(self.audit["max_iterations"], MAX_ITERATIONS)
        self.assertEqual(self.audit["iteration_count"], 12)
        self.assertEqual(self.audit["critical_count_sum"], 0)
        self.assertTrue(
            all(
                row["resolved_unresolved"] == "RESOLVED"
                for row in self.audit["iterations"]
            )
        )
        self.assertEqual(
            tuple(row["iteration"] for row in self.audit["iterations"]),
            tuple(range(1, 13)),
        )

    def test_every_iteration_has_goal_required_lineage_fields(self) -> None:
        required = {
            "iteration",
            "target",
            "failure_class",
            "root_cause_file_function_config",
            "before_metrics",
            "patch_commit",
            "focused_tests",
            "frozen_corpus_rerun",
            "live_production_rerun",
            "gold_comparison",
            "after_metrics",
            "resolved_unresolved",
        }
        for row in self.audit["iterations"]:
            with self.subTest(iteration=row["iteration"]):
                self.assertTrue(required <= set(row))
                self.assertIn(row["failure_class"], FAILURE_CLASSES)
                self.assertEqual(len(row["patch_commit"]), 40)
                self.assertTrue(row["root_cause_path_changed_by_commit"])
                self.assertFalse(row["failed_focused_tests"])

    def test_final_snapshot_is_frozen_live_gold_true_pass(self) -> None:
        snapshot = self.audit["final_replay_snapshot"]
        self.assertEqual(snapshot["frozen_critical_count_sum"], 0)
        self.assertEqual(snapshot["frozen_new_document_count"], 0)
        self.assertEqual(snapshot["live_status"], "LIVE_SEMANTIC_SCORING_PASS")
        self.assertEqual(snapshot["live_valid_target_count"], 2)
        self.assertEqual(snapshot["gold_critical_fact_recall"], 1.0)
        self.assertEqual(snapshot["gold_leakage_count"], 0)
        self.assertEqual(snapshot["search_critical_count_sum"], 0)
        self.assertEqual(snapshot["known_bad_case_count"], 35)
        self.assertEqual(
            set(snapshot["live_targets"]), {"005930", "000660"}
        )

    def test_forbidden_repairs_and_external_blockers_are_zero(self) -> None:
        self.assertTrue(
            all(value == 0 for value in self.audit["forbidden_actions"].values())
        )
        self.assertEqual(self.audit["external_provider_blockers"], [])
        self.assertEqual(
            self.audit["final_failure_status"]["EXTERNAL_PROVIDER_BLOCKER"],
            "NOT_OBSERVED",
        )

    def test_committed_audit_and_summary_are_recompiled(self) -> None:
        expected_audit = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_semantic_scoring_self_repair_audit.json"
            ).read_text(encoding="utf-8")
        )
        expected_summary = (
            self.ROOT
            / "docs/operational/e2r_semantic_scoring_self_repair_summary.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(self.audit, expected_audit)
        self.assertEqual(
            render_semantic_scoring_self_repair_summary(self.audit),
            expected_summary,
        )


if __name__ == "__main__":
    unittest.main()
