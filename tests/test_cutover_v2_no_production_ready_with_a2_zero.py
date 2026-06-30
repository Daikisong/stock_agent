import unittest

from e2r.production.cutover_v2 import _static_logic_audit_v2


class CutoverV2NoProductionReadyWithA2ZeroTests(unittest.TestCase):
    def test_a2_zero_is_blocker(self):
        audit = _static_logic_audit_v2(
            source_report={"summary": {"live_connector_alias_to_snapshot_count": 0, "source_task_accepted_without_provider_fetch_count": 0, "provider_failed_final_score_count": 0}},
            provider_matrix={"summary": {"provider_blocker_count": 0}},
            a2={"report": {"summary": {"A2_REAL_REPLAY_VERIFIED_count": 0, "source_proxy_to_A2_count": 0}}},
            claim_extraction={"report": {"summary": {"status": "LLM_EXTRACTION_PASS"}}},
            stage_distribution={"summary": {"Stage2_or_higher_count": 5}},
            trigger_policy={"summary": {"market_only_events_to_score_count": 0}},
            census={"label": "NOT_READY_FOR_CENSUS"},
            base={"sla_report": {"summary": {"unbounded_fetch_config_count": 0}}},
        )
        self.assertIn("A2_REAL_REPLAY_VERIFIED_count below 30", audit["summary"]["production_blockers"])


if __name__ == "__main__":
    unittest.main()
