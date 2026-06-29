import unittest

from e2r.research_brain.v2_production_orchestrator import build_readiness_verdict
from research_brain_v2_test_helpers import load_json


class ResearchBrainV2ProductionOrchestratorTests(unittest.TestCase):
    def test_generated_discovery_dry_run_is_not_targeted_smoke_and_has_30_events(self):
        report = load_json("docs/operational/research_brain_v2_candidate_event_dry_run.json")
        self.assertFalse(report["summary"]["targeted_smoke_only"])
        self.assertGreaterEqual(report["summary"]["candidate_event_count"], 30)

    def test_candidate_count_below_30_cannot_be_shadow_ready_without_gap(self):
        verdict = build_readiness_verdict(
            evidence_os_ready=True,
            router_matrix={"summary": {"mandatory_six_top1_pass": True, "top3_accuracy": 1.0, "r13_overroute_count": 0}},
            candidate_dry_run={"summary": {"candidate_event_count": 8}},
            source_task_audit={
                "summary": {
                    "executed_source_task_count": 20,
                    "accepted_claim_count": 5,
                    "deterministic_stage_output_count": 3,
                    "source_task_execution_audit_pass": True,
                }
            },
            watchlist_report={"summary": {"watchlist_item_count": 8}},
            provider_status={"fake_provider_used": False, "real_provider_available": False},
            frozen_daily_run_count=1,
        )
        self.assertNotEqual(verdict["summary"]["production_verdict"], "READY_FOR_SHADOW_DAILY_RUN")


if __name__ == "__main__":
    unittest.main()
