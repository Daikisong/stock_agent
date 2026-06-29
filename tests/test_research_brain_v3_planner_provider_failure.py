import unittest

from e2r.research_brain.v2_schemas import CandidateEventV2
from e2r.research_brain.v3_llm_planner_provider import run_planner_provider_v3
from research_brain_v2_test_helpers import load_v2_cards


class ResearchBrainV3PlannerProviderFailureTests(unittest.TestCase):
    def test_missing_provider_becomes_provider_failure_run(self):
        event = CandidateEventV2(
            candidate_event_id="ev",
            symbol="005930",
            company_name="삼성전자",
            event_date="2026-06-29",
            detected_at="2026-06-29",
            source_family="DART",
            source_id="fixture",
            event_type="operating_event",
            event_summary="planner unavailable test",
        )
        run = run_planner_provider_v3(provider=None, event=event, memory_cards=load_v2_cards())
        self.assertTrue(run.provider_failed)
        self.assertEqual(run.provider_name, "none")
        self.assertFalse(run.fake_provider_used)


if __name__ == "__main__":
    unittest.main()
