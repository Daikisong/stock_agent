import unittest

from e2r.production.cutover_v2 import _trigger_policy_audit


class CutoverV2TriggerTaxonomyPolicyTests(unittest.TestCase):
    def test_market_anomaly_is_investigation_only(self):
        audit = _trigger_policy_audit()
        self.assertEqual(audit["summary"]["status"], "TRIGGER_POLICY_PASS")
        self.assertEqual(audit["summary"]["market_only_events_to_score_count"], 0)


if __name__ == "__main__":
    unittest.main()
