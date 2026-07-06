import unittest
from dataclasses import replace

from e2r.research_brain.v4_planner_runtime import (
    PLANNER_BATCH_OUTPUT_SCHEMA,
    build_v4_planner_prompt_payload,
    run_planner_provider_v4,
    validate_llm_planner_output_v4,
)
from e2r.research_brain.v3_llm_planner_provider import PlannerProviderUnavailable
from tests.research_brain_v4_test_helpers import RealStubPlannerProviderV4, load_v4_cards, sample_v4_event


class BatchTimeoutThenSingleSuccessProvider(RealStubPlannerProviderV4):
    def __init__(self):
        self.call_sizes = []

    def plan_many(self, *, events, memory_cards, existing_evidence_by_event_id=None):
        self.call_sizes.append(len(events))
        if len(events) > 1:
            raise PlannerProviderUnavailable("codex_cli_timeout")
        return super().plan_many(
            events=events,
            memory_cards=memory_cards,
            existing_evidence_by_event_id=existing_evidence_by_event_id,
        )


class ResearchBrainV4RealPlannerProviderTests(unittest.TestCase):
    def test_planner_batch_schema_requires_every_declared_object_property_for_strict_provider(self):
        plan_schema = PLANNER_BATCH_OUTPUT_SCHEMA["properties"]["plans"]["items"]
        self.assertEqual(set(plan_schema["properties"]), set(plan_schema["required"]))
        draft_schema = plan_schema["properties"]["source_task_drafts"]["items"]
        self.assertEqual(set(draft_schema["properties"]), set(draft_schema["required"]))
        self.assertIn("query_intents", draft_schema["required"])

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

    def test_prompt_allowed_primitives_are_canonical_not_alias_or_score_component(self):
        payload = build_v4_planner_prompt_payload(
            events=(sample_v4_event(),),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id={},
        )
        options = payload["events"][0]["allowed_archetype_options"]
        c06_option = next(
            option
            for option in options
            if option["archetype_id"] == "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
        )
        allowed = set(c06_option["allowed_primitives"])

        self.assertIn("hbm_capacity_pre_sold", allowed)
        self.assertIn("cash_or_revision_conversion", allowed)
        self.assertNotIn("ASP increase", allowed)
        self.assertNotIn("eps_fcf_explosion", allowed)

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
        self.assertTrue(runs[0].planner_run_id)
        self.assertTrue(runs[0].prompt_hash)
        self.assertTrue(runs[0].response_hash)
        self.assertTrue(runs[0].raw_prompt_path)
        self.assertTrue(runs[0].raw_response_path)
        self.assertIsNotNone(runs[0].prompt_payload)
        self.assertIsNotNone(runs[0].response_payload)
        exported = runs[0].to_dict()
        self.assertIn("prompt_hash", exported)
        self.assertIn("response_hash", exported)
        self.assertNotIn("prompt_payload", exported)
        self.assertNotIn("response_payload", exported)

    def test_batch_timeout_retries_each_candidate_instead_of_failing_whole_batch(self):
        first = sample_v4_event(symbol="005930", company_name="삼성전자")
        second = sample_v4_event(symbol="000660", company_name="SK하이닉스")
        provider = BatchTimeoutThenSingleSuccessProvider()

        runs = run_planner_provider_v4(
            provider=provider,
            events=(first, second),
            memory_cards=load_v4_cards(),
            existing_evidence_by_event_id={},
        )

        self.assertEqual(provider.call_sizes, [2, 1, 1])
        self.assertEqual(len(runs), 2)
        self.assertTrue(all(run.real_provider_success for run in runs))
        self.assertEqual([run.event.symbol for run in runs], ["005930", "000660"])
        self.assertTrue(all(run.provider_error is None for run in runs))

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

    def test_r13_redteam_reason_code_is_explicit_primary_signal(self):
        event = replace(
            sample_v4_event(symbol="", company_name=""),
            event_type="all_archetype_runtime_parity_follow_up_seed",
            event_summary=(
                "planner input only. archetype_id=R13_CROSS_ARCHETYPE_4B_4C_REDTEAM; "
                "primitive_gap=contract_visibility"
            ),
            raw_reason_codes=(
                "GOAL4_RUNTIME_PARITY_FOLLOW_UP",
                "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
            ),
        )

        output = validate_llm_planner_output_v4(
            {
                "top_k_archetype_hypotheses": [
                    {
                        "archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
                        "probability_or_score": 0.9,
                        "reason": "explicit R13 redteam follow-up seed",
                    }
                ],
                "positive_thesis": "redteam overlay follow-up only",
                "counter_thesis": "not a production score finalization",
                "must_verify_primitives": ["contract_visibility"],
                "green_blockers_to_close": ["source quorum"],
                "red_team_checks": ["wrong subject"],
                "source_task_drafts": [
                    {
                        "task_id": "TASK-R13-REDTEAM",
                        "primitive_gap": "contract_visibility",
                        "task_type": "guard_verify",
                        "preferred_source_classes": ["DART"],
                        "fallback_source_classes": ["IssuerOfficial"],
                        "forbidden_source_classes": ["unbounded_general_search"],
                        "date_window": {"end": "2026-07-05", "lookback_days": 730},
                        "max_queries": 1,
                        "max_candidates": 5,
                        "max_fetches": 1,
                        "stop_condition": {"accepted_claim_count": 1},
                        "query_intents": ["R13 redteam current source-backed follow-up"],
                        "llm_query_allowed": True,
                        "general_search_allowed": False,
                        "reason_from_memory": "explicit redteam overlay follow-up",
                    }
                ],
                "query_intents": ["R13 redteam current source-backed follow-up"],
                "do_not_promote_reasons": ["overlay only"],
                "planner_self_check": {
                    "score_keys_present": False,
                    "stage_keys_present": False,
                    "future_outcome_used": False,
                },
            },
            event=event,
            memory_cards=load_v4_cards(),
        )

        self.assertEqual(output.top_k_archetype_hypotheses[0]["archetype_id"], "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM")

    def test_source_task_primitive_outside_primary_contract_is_quarantined(self):
        event = sample_v4_event(symbol="003090", company_name="대웅")
        output = validate_llm_planner_output_v4(
            {
                "top_k_archetype_hypotheses": [
                    {
                        "archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
                        "probability_or_score": 0.9,
                        "reason": "facility event closest to C29",
                    }
                ],
                "positive_thesis": "시설투자 일정 확인",
                "counter_thesis": "일정 변경만으로 volume growth를 인정하지 않는다.",
                "must_verify_primitives": ["implementation_timeline", "volume_growth_visible"],
                "green_blockers_to_close": [],
                "red_team_checks": [],
                "source_task_drafts": [
                    {
                        "task_id": "TASK-BAD-PRIMITIVE",
                        "primitive_gap": "implementation_timeline",
                        "task_type": "positive_verify",
                        "preferred_source_classes": ["DART"],
                        "fallback_source_classes": ["IssuerOfficial"],
                        "forbidden_source_classes": ["unbounded_general_search"],
                        "date_window": {"end": "2026-06-29", "lookback_days": 30},
                        "max_queries": 1,
                        "max_candidates": 5,
                        "max_fetches": 1,
                        "stop_condition": {"accepted_claim_count": 1},
                        "llm_query_allowed": True,
                        "general_search_allowed": False,
                        "reason_from_memory": "unit invalid primitive",
                    },
                    {
                        "task_id": "TASK-GOOD-PRIMITIVE",
                        "primitive_gap": "volume_growth_visible",
                        "task_type": "positive_verify",
                        "preferred_source_classes": ["DART"],
                        "fallback_source_classes": ["IssuerOfficial"],
                        "forbidden_source_classes": ["unbounded_general_search"],
                        "date_window": {"end": "2026-06-29", "lookback_days": 30},
                        "max_queries": 1,
                        "max_candidates": 5,
                        "max_fetches": 1,
                        "stop_condition": {"accepted_claim_count": 1},
                        "llm_query_allowed": True,
                        "general_search_allowed": False,
                        "reason_from_memory": "unit valid primitive",
                    },
                ],
                "query_intents": ["대웅 신규시설투자 일정"],
                "do_not_promote_reasons": [],
                "planner_self_check": {
                    "score_keys_present": False,
                    "stage_keys_present": False,
                    "future_outcome_used": False,
                },
            },
            event=event,
            memory_cards=load_v4_cards(),
        )

        self.assertEqual(output.must_verify_primitives, ("volume_growth_visible",))
        self.assertEqual(len(output.source_task_drafts), 1)
        self.assertEqual(output.source_task_drafts[0]["primitive_gap"], "volume_growth_visible")


if __name__ == "__main__":
    unittest.main()
