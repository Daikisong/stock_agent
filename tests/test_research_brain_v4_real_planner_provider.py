import unittest

from e2r.research_brain.v4_planner_runtime import (
    build_v4_planner_prompt_payload,
    run_planner_provider_v4,
    validate_llm_planner_output_v4,
)
from research_brain_v4_test_helpers import RealStubPlannerProviderV4, load_v4_cards, sample_v4_event


class ResearchBrainV4RealPlannerProviderTests(unittest.TestCase):
    def test_prompt_excludes_score_stage_and_future_targets(self):
        payload = build_v4_planner_prompt_payload(
            events=(sample_v4_event(),),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id={},
        )
        runtime_payload = str(payload["events"])
        self.assertIn("forbidden_output_keys", payload)
        self.assertNotIn("expected stage", runtime_payload.lower())
        self.assertNotIn("target score threshold", runtime_payload.lower())
        self.assertNotIn("mfe", runtime_payload.lower())
        self.assertNotIn("mae", runtime_payload.lower())

    def test_real_provider_success_is_counted_without_fake_provider(self):
        event = sample_v4_event()
        runs = run_planner_provider_v4(
            provider=RealStubPlannerProviderV4(),
            events=(event,),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id={event.candidate_event_id: {}},
        )
        self.assertEqual(len(runs), 1)
        self.assertTrue(runs[0].real_provider_success)
        self.assertFalse(runs[0].fake_provider_used)

    def test_score_stage_key_rejected_by_validator(self):
        event = sample_v4_event()
        with self.assertRaises(ValueError):
            validate_llm_planner_output_v4(
                {
                    "top_k_archetype_hypotheses": [
                        {"archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "probability_or_score": 0.9, "reason": "x"}
                    ],
                    "positive_thesis": "x",
                    "counter_thesis": "x",
                    "must_verify_primitives": ["medium_term_revision_visibility"],
                    "green_blockers_to_close": [],
                    "red_team_checks": [],
                    "source_task_drafts": [],
                    "query_intents": [],
                    "do_not_promote_reasons": [],
                    "planner_self_check": {
                        "score_keys_present": False,
                        "stage_keys_present": False,
                        "future_outcome_used": False,
                    },
                    "score": 90,
                },
                event=event,
                memory_cards=load_v4_cards(),
            )


if __name__ == "__main__":
    unittest.main()
