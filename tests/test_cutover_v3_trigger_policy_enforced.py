import unittest

from e2r.production.cutover_v3 import _trigger_policy_audit_v3
from tests.cutover_v3_test_helpers import fake_v3_base


class CutoverV3TriggerPolicyEnforcedTests(unittest.TestCase):
    def test_every_candidate_event_carries_trigger_policy_fields(self):
        report = _trigger_policy_audit_v3(base_bundles=[fake_v3_base()])
        self.assertEqual(report["summary"]["status"], "TRIGGER_POLICY_ENFORCED")
        self.assertEqual(report["summary"]["candidate_events_missing_trigger_category_count"], 0)
        self.assertEqual(report["summary"]["candidate_events_missing_allowed_source_families_count"], 0)


if __name__ == "__main__":
    unittest.main()
