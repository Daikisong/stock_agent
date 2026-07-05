import json
import unittest
from pathlib import Path


class FullThesisScorePathNotMeaningfulPassTests(unittest.TestCase):
    def test_legacy_full_thesis_production_pass_is_reclassified(self) -> None:
        old = json.loads(Path("docs/operational/census_mode_v4_full_thesis_production_audit.json").read_text())
        new = json.loads(Path("docs/operational/full_thesis_evidence_completion_audit_v2.json").read_text())
        self.assertEqual(old["status"], "PENDING_FULL_THESIS_PRODUCTION")
        self.assertEqual(new["score_path_status"], "PRODUCTION_FULL_E2R_SCORE_PATH_PENDING")
        self.assertEqual(new["meaningful_evidence_status"], "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE")


if __name__ == "__main__":
    unittest.main()
