from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring.evidence_to_score_known_bad import (
    CASES,
    PASS_STATUS,
    compile_evidence_to_score_known_bad_audit,
)


class EvidenceToScoreKnownBadTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_exact_35_goal_mutations_are_detected(self) -> None:
        audit = compile_evidence_to_score_known_bad_audit()
        self.assertEqual([case.case_id for case in CASES], [f"KB-{i:02d}" for i in range(1, 36)])
        self.assertEqual(audit["status"], PASS_STATUS)
        self.assertEqual(audit["case_count"], 35)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(all(row["status"] == "PASS" for row in audit["cases"]))

    def test_operational_audit_is_recomputed_from_real_detectors(self) -> None:
        expected = compile_evidence_to_score_known_bad_audit()
        artifact = json.loads(
            (self.ROOT / "docs/operational/e2r_semantic_scoring_known_bad_audit.json").read_text(encoding="utf-8")
        )
        self.assertEqual(artifact, expected)


if __name__ == "__main__":
    unittest.main()
