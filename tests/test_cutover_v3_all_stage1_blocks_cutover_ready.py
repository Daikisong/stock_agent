import unittest

from e2r.production.cutover_v3 import _static_logic_audit_v3
from tests.cutover_v3_test_helpers import fake_a2, fake_provider_matrix, fake_rollup_metadata


class CutoverV3AllStage1BlocksCutoverReadyTests(unittest.TestCase):
    def test_all_stage1_without_low_signal_explanation_is_critical_if_ready(self):
        audit = _static_logic_audit_v3(
            provider_matrix=fake_provider_matrix(),
            multiday={"summary": {"status": "MULTIDAY_SHADOW_PASS"}},
            claim_audit={"summary": {"status": "CLAIM_EXTRACTOR_AUDIT_PASS", "unstructured_text_rule_score_count": 0}},
            stage_distribution={
                "summary": {
                    "status": "MEANINGFUL_STAGE_SPLIT_PASS",
                    "live_Stage2_or_higher_count": 0,
                    "documented_low_signal_market": False,
                    "score_without_claim_count": 0,
                }
            },
            trigger_policy={"summary": {"status": "TRIGGER_POLICY_ENFORCED", "market_anomaly_to_score_count": 0, "news_snippet_to_score_count": 0, "old_risk_without_current_open_to_score_count": 0}},
            sla={"summary": {"status": "SLA_PASS", "unbounded_fetch_config_count": 0}},
            a2=fake_a2(),
            census={"label": "READY_FOR_CENSUS_DESIGN"},
            metadata=fake_rollup_metadata(),
        )
        self.assertGreater(audit["summary"]["all_stage1_but_ready_count"], 0)


if __name__ == "__main__":
    unittest.main()
