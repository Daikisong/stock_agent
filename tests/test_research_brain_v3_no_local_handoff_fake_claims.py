import unittest

from research_brain_v2_test_helpers import load_json


class ResearchBrainV3NoLocalHandoffFakeClaimsTests(unittest.TestCase):
    def test_no_local_handoff_or_deterministic_fake_claims(self):
        audit = load_json("docs/operational/research_brain_v3_source_task_execution_audit.json")
        summary = audit["summary"]
        self.assertEqual(summary["local_handoff_fake_claim_count"], 0)
        self.assertEqual(summary["deterministic_fake_accepted_claim_count"], 0)


if __name__ == "__main__":
    unittest.main()
