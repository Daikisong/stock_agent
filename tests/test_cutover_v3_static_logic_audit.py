import unittest

from e2r.production.cutover_v3 import _completion_labels_v3, _static_logic_audit_v3
from tests.cutover_v3_test_helpers import fake_a2, fake_provider_matrix


class CutoverV3StaticLogicAuditTests(unittest.TestCase):
    def test_static_audit_zero_counts_allows_cutover_ready_label(self):
        static = _static_logic_audit_v3(
            provider_matrix=fake_provider_matrix(),
            multiday={"summary": {"status": "MULTIDAY_SHADOW_PASS"}},
            claim_audit={"summary": {"status": "CLAIM_EXTRACTOR_AUDIT_PASS", "unstructured_text_rule_score_count": 0}},
            stage_distribution={"summary": {"status": "MEANINGFUL_STAGE_SPLIT_PASS", "live_Stage2_or_higher_count": 10, "score_without_claim_count": 0}},
            trigger_policy={"summary": {"status": "TRIGGER_POLICY_ENFORCED", "market_anomaly_to_score_count": 0, "news_snippet_to_score_count": 0, "old_risk_without_current_open_to_score_count": 0}},
            sla={"summary": {"status": "SLA_PASS", "unbounded_fetch_config_count": 0}},
            a2=fake_a2(),
            census={"label": "READY_FOR_CENSUS_DESIGN"},
        )
        self.assertEqual(static["summary"]["critical_count_sum"], 0)
        labels = _completion_labels_v3(
            provider_matrix=fake_provider_matrix(),
            multiday={"summary": {"status": "MULTIDAY_SHADOW_PASS"}},
            claim_audit={"summary": {"status": "CLAIM_EXTRACTOR_AUDIT_PASS"}},
            stage_distribution={"summary": {"status": "MEANINGFUL_STAGE_SPLIT_PASS"}},
            trigger_policy={"summary": {"status": "TRIGGER_POLICY_ENFORCED"}},
            operator_digest={"summary": {"status": "OPERATOR_DIGEST_PASS"}},
            sla={"summary": {"status": "SLA_PASS"}},
            static=static,
            a2=fake_a2(),
            final_cutover_approved=False,
        )
        self.assertIn("CUTOVER_READY", labels)
        self.assertNotIn("PRODUCTION_READY", labels)


if __name__ == "__main__":
    unittest.main()
