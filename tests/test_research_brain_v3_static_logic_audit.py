import unittest

from research_brain_v2_test_helpers import load_json


class ResearchBrainV3StaticLogicAuditTests(unittest.TestCase):
    def test_critical_static_logic_counts_are_zero(self):
        audit = load_json("docs/operational/research_brain_v3_static_logic_audit.json")
        summary = audit["summary"]
        self.assertEqual(summary["critical_count_sum"], 0)
        self.assertTrue(summary["critical_audit_pass"])
        self.assertEqual(summary["cheap_scan_total_score_used_as_verified_score_count"], 0)
        self.assertEqual(summary["source_proxy_to_score_count"], 0)


if __name__ == "__main__":
    unittest.main()
