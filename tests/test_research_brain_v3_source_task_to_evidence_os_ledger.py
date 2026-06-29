import unittest

from research_brain_v2_test_helpers import load_json


class ResearchBrainV3SourceTaskLedgerTests(unittest.TestCase):
    def test_source_task_accepted_count_matches_evidence_os_count(self):
        audit = load_json("docs/operational/research_brain_v3_source_task_execution_audit.json")
        summary = audit["summary"]
        self.assertEqual(summary["accepted_claim_count"], summary["evidence_os_accepted_claim_count"])
        self.assertTrue(summary["source_task_accepted_claim_count_matches_ledger"])
        self.assertGreater(summary["accepted_claim_count"], 0)


if __name__ == "__main__":
    unittest.main()
