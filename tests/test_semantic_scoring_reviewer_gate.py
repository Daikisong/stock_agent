from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring.semantic_scoring_reviewer_gate import (
    FAIL_STATUS,
    PASS_STATUS,
    REVIEWER_SCOPES,
    compile_semantic_scoring_reviewer_gate,
    evaluate_semantic_scoring_reviewer_gate,
)


class SemanticScoringReviewerGateTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = compile_semantic_scoring_reviewer_gate(
            repo_root=cls.ROOT
        )

    def test_reviewers_a_through_h_independently_pass_direct_leaf_checks(self) -> None:
        self.assertEqual(self.audit["status"], PASS_STATUS)
        self.assertEqual(self.audit["reviewer_count"], 8)
        self.assertEqual(set(self.audit["reviewers"]), set("ABCDEFGH"))
        self.assertEqual(self.audit["critical_count_sum"], 0)
        for reviewer_id, scope in REVIEWER_SCOPES.items():
            with self.subTest(reviewer_id=reviewer_id):
                row = self.audit["reviewers"][reviewer_id]
                self.assertEqual(row["scope"], scope)
                self.assertEqual(row["status"], f"REVIEWER_{reviewer_id}_PASS")
                self.assertTrue(row["direct_leaf_reread"])
                self.assertGreater(len(row["direct_leaf_paths"]), 0)
                self.assertEqual(
                    set(row["direct_leaf_paths"]),
                    set(row["direct_leaf_sha256"]),
                )
                self.assertEqual(row["report_generator_counter_ids"], [])

    def test_private_counter_namespaces_are_not_shared(self) -> None:
        independence = self.audit["counter_independence"]
        self.assertEqual(independence["shared_report_generator_counter_count"], 0)
        self.assertEqual(independence["unique_counter_namespace_count"], 8)
        self.assertEqual(
            len(set(independence["counter_namespaces"])),
            len(independence["counter_namespaces"]),
        )

    def test_one_critical_in_any_reviewer_forces_gate_fail(self) -> None:
        for reviewer_id in "ABCDEFGH":
            with self.subTest(reviewer_id=reviewer_id):
                mutated = copy.deepcopy(self.audit["reviewers"])
                first_key = next(iter(mutated[reviewer_id]["critical_counts"]))
                mutated[reviewer_id]["critical_counts"][first_key] = 1
                verdict = evaluate_semantic_scoring_reviewer_gate(mutated)
                self.assertEqual(verdict["status"], FAIL_STATUS)
                self.assertGreater(verdict["critical_count_sum"], 0)

    def test_committed_operational_gate_is_recompiled(self) -> None:
        expected = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_semantic_scoring_reviewer_gate.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(self.audit, expected)


if __name__ == "__main__":
    unittest.main()
