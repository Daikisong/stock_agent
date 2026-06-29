import unittest
from pathlib import Path

from research_brain_v2_test_helpers import load_json


class ResearchBrainV2EvidenceOSIntegrationTests(unittest.TestCase):
    def test_evidence_os_v2_ready_status_is_preserved(self):
        text = Path("docs/operational/evidence_os_v2_acceptance_report.md").read_text(encoding="utf-8")
        self.assertIn("verdict: READY", text)

    def test_source_proxy_to_score_and_future_leakage_are_zero(self):
        source_quality = load_json("docs/operational/research_brain_v2_source_quality_reclassification.json")
        self.assertEqual(source_quality["summary"]["source_proxy_to_score_count"], 0)
        acceptance = Path("docs/operational/research_brain_v2_acceptance_report.md").read_text(encoding="utf-8")
        self.assertIn("source_proxy_to_score count: 0", acceptance)

    def test_a2_replay_sample_audit_passes(self):
        audit = load_json("docs/operational/research_brain_v2_a2_replay_sample_audit.json")
        self.assertTrue(audit["summary"]["audit_pass"])
        self.assertEqual(audit["summary"]["A2_replay_sample_pass_count"], 200)


if __name__ == "__main__":
    unittest.main()
