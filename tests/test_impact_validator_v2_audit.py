from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring import (
    audit_impact_validator_v2,
    compile_fact_document_dedupe_audit,
)


class ImpactValidatorV2AuditTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_frozen_corpus_replay_matches_committed_validator_audit(self) -> None:
        actual = audit_impact_validator_v2(repo_root=self.ROOT)
        expected = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_impact_validator_v2_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, expected)
        self.assertEqual(actual["status"], "STRICT_IMPACT_VALIDATOR_V2_PASS")
        self.assertEqual(actual["critical_count_sum"], 0)

    def test_fact_document_dedupe_audit_has_no_duplicate_credit(self) -> None:
        impact = audit_impact_validator_v2(repo_root=self.ROOT)
        actual = compile_fact_document_dedupe_audit(impact)
        expected = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_fact_document_dedupe_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, expected)
        self.assertEqual(actual["critical_count_sum"], 0)
        self.assertGreater(
            sum(
                row["suppressed_same_document_duplicate_count"]
                for row in actual["targets"].values()
            ),
            0,
        )


if __name__ == "__main__":
    unittest.main()
