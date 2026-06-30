import unittest

from e2r.production.cutover_v2 import _static_logic_audit_v2


class CutoverV2NoForcedSubjectPolarityTemporalTests(unittest.TestCase):
    def test_forced_subject_polarity_temporal_are_critical_if_nonzero(self):
        audit = _static_logic_audit_v2(
            source_report={"summary": {"live_connector_alias_to_snapshot_count": 0, "source_task_accepted_without_provider_fetch_count": 0, "provider_failed_final_score_count": 0}},
            provider_matrix={"summary": {"provider_blocker_count": 0}},
            a2={"report": {"summary": {"A2_REAL_REPLAY_VERIFIED_count": 30, "source_proxy_to_A2_count": 0}}},
            claim_extraction={"report": {"summary": {"status": "LLM_EXTRACTION_PASS", "forced_target_subject_count": 1, "forced_positive_polarity_count": 0, "forced_current_temporal_count": 0}}},
            stage_distribution={"summary": {"Stage2_or_higher_count": 5}},
            trigger_policy={"summary": {"market_only_events_to_score_count": 0}},
            census={"label": "READY_FOR_CENSUS_DESIGN"},
            base={"sla_report": {"summary": {"unbounded_fetch_config_count": 0}}},
        )
        self.assertGreater(audit["summary"]["critical_count_sum"], 0)


if __name__ == "__main__":
    unittest.main()
