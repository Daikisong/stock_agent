import unittest

from e2r.research_brain.v2_schemas import CandidateEventV2
from e2r.research_brain.v3_llm_planner_provider import (
    FixturePlannerProvider,
    PlannerProviderRejected,
    build_v3_planner_prompt_payload,
    validate_llm_planner_output_v3,
)
from research_brain_v2_test_helpers import load_v2_cards


class ResearchBrainV3RealPlannerProviderTests(unittest.TestCase):
    def test_prompt_excludes_score_stage_targets(self):
        event = CandidateEventV2(
            candidate_event_id="ev",
            symbol="000660",
            company_name="SK하이닉스",
            event_date="2026-06-29",
            detected_at="2026-06-29",
            source_family="DART",
            source_id="fixture",
            event_type="operating_event",
            event_summary="HBM capacity sold out customer allocation",
            issuer_directness="DIRECT",
        )
        payload = build_v3_planner_prompt_payload(event=event, memory_cards=load_v2_cards()[:3])
        self.assertIn("forbidden_output_keys", payload)
        runtime_payload = str(payload["candidate_event"]) + str(payload["archetype_memory_cards"])
        self.assertNotIn("expected stage", runtime_payload.lower())
        self.assertNotIn("score threshold", runtime_payload.lower())

    def test_fixture_provider_output_validates_without_score_stage(self):
        cards = load_v2_cards()
        event = CandidateEventV2(
            candidate_event_id="ev",
            symbol="000660",
            company_name="SK하이닉스",
            event_date="2026-06-29",
            detected_at="2026-06-29",
            source_family="DART",
            source_id="fixture",
            event_type="operating_event",
            event_summary="HBM 매출 비중 확대 capacity sold out customer allocation",
            raw_reason_codes=("HBM_REVENUE_MIX",),
            issuer_directness="DIRECT",
        )
        output = FixturePlannerProvider().plan(event, cards)
        self.assertTrue(output.top_k_archetype_hypotheses)
        self.assertFalse(output.planner_self_check["score_keys_present"])

    def test_score_key_rejected(self):
        cards = load_v2_cards()
        event = CandidateEventV2(
            candidate_event_id="ev",
            symbol="000660",
            company_name="SK하이닉스",
            event_date="2026-06-29",
            detected_at="2026-06-29",
            source_family="DART",
            source_id="fixture",
            event_type="operating_event",
            event_summary="HBM capacity",
        )
        with self.assertRaises(ValueError):
            validate_llm_planner_output_v3(
                {
                    "top_k_archetype_hypotheses": [{"archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY"}],
                    "score": 90,
                    "planner_self_check": {},
                },
                event=event,
                memory_cards=cards,
            )


if __name__ == "__main__":
    unittest.main()
