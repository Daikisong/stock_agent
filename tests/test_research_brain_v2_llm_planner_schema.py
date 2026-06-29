import unittest

from e2r.research_brain.v2_llm_planner import build_planner_prompt_payload, validate_llm_planner_output_v2
from e2r.research_brain.v2_schemas import CandidateEventV2
from research_brain_v2_test_helpers import load_v2_cards


class ResearchBrainV2LLMPlannerSchemaTests(unittest.TestCase):
    def test_planner_output_rejects_score_stage_and_eligibility_keys(self):
        payload = {
            "top_k_archetype_hypotheses": [{"archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "rank": 1}],
            "positive_thesis": "x",
            "counter_thesis": "y",
            "must_verify_primitives": [],
            "green_blockers_to_close": [],
            "red_team_checks": [],
            "source_task_drafts": [],
            "query_intents": [],
            "do_not_promote_reasons": [],
            "planner_self_check": {"score_keys_present": False, "stage_keys_present": False, "future_outcome_used": False},
            "score": 99,
        }
        with self.assertRaises(ValueError):
            validate_llm_planner_output_v2(payload)

    def test_valid_planner_output_schema_accepts_archetype_hypotheses_only(self):
        output = validate_llm_planner_output_v2(
            {
                "top_k_archetype_hypotheses": [{"archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "rank": 1}],
                "positive_thesis": "verify HBM allocation",
                "counter_thesis": "guard against sympathy only",
                "must_verify_primitives": ["capacity_allocation"],
                "green_blockers_to_close": [],
                "red_team_checks": [],
                "source_task_drafts": [],
                "query_intents": [],
                "do_not_promote_reasons": [],
                "planner_self_check": {"score_keys_present": False, "stage_keys_present": False, "future_outcome_used": False},
            }
        )
        self.assertEqual(output.top_k_archetype_hypotheses[0]["archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")

    def test_planner_prompt_payload_has_no_score_or_stage_targets(self):
        event = CandidateEventV2(
            candidate_event_id="evt",
            symbol="000660",
            company_name="SK하이닉스",
            event_date="2026-06-29",
            detected_at="2026-06-29",
            source_family="DART",
            source_id="fixture",
            event_type="supply_contract",
        )
        payload = build_planner_prompt_payload(event=event, cards=load_v2_cards()[:2])
        text = str(payload)
        self.assertIn("forbidden_output_keys", payload)
        self.assertNotIn("verified_score", text)
        self.assertNotIn("base_stage", text)


if __name__ == "__main__":
    unittest.main()
