import unittest

from e2r.production.cutover_v2 import _trigger_policy_audit


class CutoverV2TriggerTaxonomyPolicyTests(unittest.TestCase):
    def test_market_anomaly_is_investigation_only(self):
        audit = _trigger_policy_audit()
        self.assertEqual(audit["summary"]["status"], "TRIGGER_POLICY_PASS")
        self.assertEqual(audit["summary"]["market_only_events_to_score_count"], 0)

    def test_candidate_events_must_carry_trigger_policy(self):
        audit = _trigger_policy_audit(
            base={
                "output_artifacts": {
                    "candidate_events": [
                        {"candidate_event_id": "CE-1", "trigger_category": "Official Positive Trigger", "score_eligibility_policy": "accepted_claim_required"},
                        {"candidate_event_id": "CE-2"},
                    ]
                }
            }
        )
        self.assertEqual(audit["summary"]["candidate_events_missing_trigger_category_count"], 1)
        self.assertEqual(audit["summary"]["status"], "TRIGGER_POLICY_NOT_COMPLETE")


if __name__ == "__main__":
    unittest.main()
