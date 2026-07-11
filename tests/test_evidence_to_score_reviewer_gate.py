from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring.evidence_to_score_reviewer_gate import (
    PASS_STATUS,
    compile_evidence_to_score_reviewer_gate,
)


class EvidenceToScoreReviewerGateTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_reviewers_a_through_g_independently_pass_leaf_checks(self) -> None:
        audit = compile_evidence_to_score_reviewer_gate(repo_root=self.ROOT)
        self.assertEqual(audit["status"], PASS_STATUS)
        self.assertEqual(set(audit["reviewers"]), set("ABCDEFG"))
        self.assertEqual(audit["critical_count_sum"], 0)
        for reviewer_id, row in audit["reviewers"].items():
            self.assertEqual(row["status"], f"REVIEWER_{reviewer_id}_PASS")
            self.assertGreater(len(row["leaf_paths"]), 0)
            self.assertEqual(set(row["leaf_paths"]), set(row["leaf_sha256"]))

    def test_operational_reviewer_gate_is_recomputed_from_leaves(self) -> None:
        expected = compile_evidence_to_score_reviewer_gate(repo_root=self.ROOT)
        artifact = json.loads(
            (self.ROOT / "docs/operational/e2r_evidence_to_score_reviewer_gate.json").read_text(encoding="utf-8")
        )
        self.assertEqual(artifact, expected)


if __name__ == "__main__":
    unittest.main()
