from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring.component_assessment import TERMINAL_FULL_SCORE_STATUSES


class SamsungHynixCanonicalDossierTests(unittest.TestCase):
    ROOT = Path("output/evidence_to_score/c06/2026-07-11")

    def test_both_mandatory_targets_have_organic_full_score_stagecourt(self) -> None:
        expected = {
            "005930": "SAMSUNG_CANONICAL_FULL_THESIS_PASS",
            "000660": "SK_HYNIX_CANONICAL_FULL_THESIS_PASS",
        }
        for target_id, status in expected.items():
            with self.subTest(target_id=target_id):
                root = self.ROOT / target_id
                audit = json.loads((root / "audit_summary.json").read_text())
                claims = self._rows(root / "accepted_current_claims.jsonl")
                impacts = self._rows(root / "claim_impacts_validated.jsonl")
                assessments = self._rows(root / "component_assessments.jsonl")
                score = json.loads((root / "component_score_vector.json").read_text())
                decision = json.loads((root / "atomic_stage_decision.json").read_text())
                self.assertEqual(audit["status"], status)
                self.assertEqual(audit["critical_count_sum"], 0)
                self.assertTrue(claims)
                self.assertTrue(impacts)
                self.assertTrue(all(row["evidence_origin"] == "ORGANIC_LIVE" for row in claims))
                self.assertTrue(all(row["status"] in TERMINAL_FULL_SCORE_STATUSES for row in assessments))
                self.assertEqual(len(assessments), 7)
                self.assertTrue(score["full_score_valid"])
                self.assertEqual(score["score_type"], "FULL_E2R_100")
                self.assertGreater(score["verified_supported_score"], 0)
                self.assertEqual(decision["decision_status"], "FINAL")
                self.assertNotEqual(decision["canonical_stage"], "0")

    @staticmethod
    def _rows(path: Path):
        return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


if __name__ == "__main__": unittest.main()
