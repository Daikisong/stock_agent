from __future__ import annotations

import json
import unittest
from dataclasses import replace
from pathlib import Path

from e2r.research_brain.intelligence_schema import AcceptedClaimPredicate, EvidenceRecipe
from e2r.research_brain.planning import FixtureQuestionQueryProvider
from e2r.research_brain.runtime.live_materialization import (
    CurrentQuestionSourceTaskMaterializer,
    SourceTaskMaterializationConfig,
)


class LiveSourceTaskMaterializerTest(unittest.TestCase):
    def test_live_operational_audit_records_real_question_tasks(self) -> None:
        audit_path = (
            Path(__file__).resolve().parents[1]
            / "docs"
            / "operational"
            / "e2r_live_source_task_audit.json"
        )
        audit = json.loads(audit_path.read_text(encoding="utf-8"))

        self.assertEqual(audit["status"], "PHASE_26_ACCEPTED")
        self.assertEqual(audit["materialized_source_task_count"], 9)
        self.assertEqual(audit["real_query_provider_task_count"], 9)
        self.assertEqual(audit["real_query_generation_call_count"], 9)
        self.assertEqual(sum(audit["critical_counts"].values()), 0)
        self.assertFalse(audit["safety"]["deterministic_literal_query_fallback_present"])
        self.assertFalse(audit["safety"]["official_fetch_claimed_before_execution"])

    def test_llm_literal_query_becomes_bounded_daily_task(self) -> None:
        provider = FixtureQuestionQueryProvider(
            callback=lambda payload: {
                "input_id": payload["input_id"],
                "literal_queries": [
                    "테스트회사 2026년 1분기 공식 IR 계약 갱신 기간 현금흐름"
                ],
                "generation_rationale": "회사와 보고기간을 직접 한정했다.",
                "ambiguity_reasons": [],
                "abstain": False,
                "abstention_reason": "",
            }
        )
        result = CurrentQuestionSourceTaskMaterializer().materialize(
            SourceTaskMaterializationConfig(
                as_of_date="2026-07-10",
                max_source_tasks_per_candidate=3,
                test_mode=True,
            ),
            planner_runs=(_planner_run(),),
            trigger_signals=(_trigger_signal(),),
            recipes=(_recipe(),),
            provider=provider,
        )

        self.assertEqual(result.status, "CURRENT_SOURCE_TASK_PASS")
        self.assertEqual(len(result.source_tasks), 1)
        task = result.source_tasks[0]
        self.assertEqual(task.recipe_id, "ERECIPE-TEST")
        self.assertEqual(task.source_class, "DART")
        self.assertEqual(
            task.literal_queries,
            ("테스트회사 2026년 1분기 공식 IR 계약 갱신 기간 현금흐름",),
        )
        self.assertFalse(task.official_first_attempted)
        self.assertFalse(task.allows_general_web)
        self.assertTrue(task.accepted_predicates)
        self.assertTrue(task.resolution_conditions)
        self.assertEqual(result.audit["critical_count_sum"], 0)

    def test_non_official_first_draft_is_rejected(self) -> None:
        run = _planner_run()
        draft = run["plan"]["critique_output"]["source_task_drafts"][0]
        draft["preferred_source_families"] = ["TrustedNews"]
        provider = FixtureQuestionQueryProvider(
            callback=lambda payload: {
                "input_id": payload["input_id"],
                "literal_queries": ["테스트회사 2026년 1분기 계약 갱신 공식 발표"],
                "generation_rationale": "대상과 기간을 한정했다.",
                "ambiguity_reasons": [],
                "abstain": False,
                "abstention_reason": "",
            }
        )

        with self.assertRaisesRegex(ValueError, "official-first"):
            CurrentQuestionSourceTaskMaterializer().materialize(
                SourceTaskMaterializationConfig(
                    as_of_date="2026-07-10",
                    max_source_tasks_per_candidate=3,
                    test_mode=True,
                ),
                planner_runs=(run,),
                trigger_signals=(_trigger_signal(),),
                recipes=(_recipe(),),
                provider=provider,
            )

    def test_short_economic_acronym_is_not_mistaken_for_internal_label(self) -> None:
        run = _planner_run()
        draft = run["plan"]["critique_output"]["source_task_drafts"][0]
        draft["question_to_answer"] = "테스트회사가 정의된 NRR을 현재 직접 보고했는가?"
        draft["query_intent"] = "공식 자료에서 NRR 정의와 측정 기간을 확인한다."
        provider = FixtureQuestionQueryProvider(
            callback=lambda payload: {
                "input_id": payload["input_id"],
                "literal_queries": ["테스트회사 2026년 1분기 NRR 정의 공식 IR"],
                "generation_rationale": "경제 지표와 기간을 직접 명시했다.",
                "ambiguity_reasons": [],
                "abstain": False,
                "abstention_reason": "",
            }
        )

        result = CurrentQuestionSourceTaskMaterializer().materialize(
            SourceTaskMaterializationConfig(
                as_of_date="2026-07-10",
                max_source_tasks_per_candidate=3,
                test_mode=True,
            ),
            planner_runs=(run,),
            trigger_signals=(_trigger_signal(),),
            recipes=(replace(_recipe(), primitive_id="nrr"),),
            provider=provider,
        )

        self.assertEqual(result.status, "CURRENT_SOURCE_TASK_PASS")
        self.assertIn("NRR", result.source_tasks[0].literal_queries[0])


def _planner_run() -> dict:
    return {
        "target_id": "000001",
        "target_name": "테스트회사",
        "as_of_date": "2026-07-10",
        "candidate_event_id": "CAND-TEST",
        "trigger_signal_ids": ["TRIG-TEST"],
        "plan": {
            "critique_output": {
                "source_task_drafts": [
                    {
                        "draft_id": "DRAFT-TEST",
                        "recipe_id": "ERECIPE-TEST",
                        "question_to_answer": (
                            "테스트회사의 현재 계약 갱신이 기간과 현금흐름으로 확인되는가?"
                        ),
                        "why_material": "계약 발표와 실제 경제 효과를 구분해야 한다.",
                        "query_intent": (
                            "대상 회사의 공식 문서에서 계약 갱신 기간과 현금흐름을 확인한다."
                        ),
                        "preferred_source_families": ["DART", "IssuerIR"],
                        "fallback_source_families": ["TrustedNews"],
                        "max_queries": 2,
                        "max_candidates": 8,
                        "max_fetches": 4,
                        "stop_condition": (
                            "계약 기간과 현금흐름을 공식 원문에서 확인하면 중단한다."
                        ),
                    }
                ]
            }
        },
    }


def _trigger_signal() -> dict:
    return {
        "trigger_signal_id": "TRIG-TEST",
        "target_id": "000001",
        "target_name": "테스트회사",
        "trigger_type": "OFFICIAL",
        "effective_date": "2026-07-09",
        "payload": {"report_name": "단일판매·공급계약체결"},
    }


def _recipe() -> EvidenceRecipe:
    predicate = AcceptedClaimPredicate(
        predicate_id="PRED-TEST",
        semantic_test="대상 회사 계약의 기간과 경제 효과가 직접 확인된다.",
        required_subject_relation="DIRECT",
        required_fields=("source_id", "exact_anchor", "contract_period"),
        allowed_polarities=("POSITIVE", "NEGATIVE"),
        temporal_test="as_of_date 이전 문서만 허용한다.",
        lifecycle_test="최신 미취소 계약이어야 한다.",
    )
    return EvidenceRecipe(
        recipe_id="ERECIPE-TEST",
        archetype_id="C01_TEST",
        primitive_id="contract_economic_bridge",
        role="POSITIVE",
        economic_mechanism="계약이 기간과 현금흐름으로 이어지는지를 확인한다.",
        question_to_answer="계약 갱신이 직접 경제 효과로 이어지는가?",
        accepted_claim_predicates=(predicate,),
        required_entities=("대상 회사", "계약 상대방"),
        required_values=("계약 기간", "계약 금액"),
        required_units=("원", "개월"),
        required_time_scope=("공시일", "계약 기간"),
        required_target_directness=("DIRECT",),
        required_current_lifecycle=("OPEN", "not cancelled"),
        preferred_source_families=("DART", "IssuerIR", "TrustedNews"),
        preferred_document_types=("filing", "investor_presentation"),
        preferred_sections=("계약 내용", "현금흐름"),
        discovery_sources=("DART", "IssuerIR", "TrustedNews"),
        forbidden_score_sources=("search_snippet",),
        positive_examples=("기간과 금액이 명시된 직접 계약",),
        counterexamples=("구속력 없는 업무협약",),
        wrong_subject_examples=("고객사가 아닌 동종사 계약",),
        source_success_examples=("공시 원문과 정확한 계약 표",),
        source_failure_examples=("검색 결과 제목만 존재",),
        rejection_conditions=("대상 회사가 계약 주체가 아님",),
        counter_questions=("계약이 취소 또는 축소됐는가?",),
        supersession_questions=("더 최신 정정공시가 있는가?",),
        query_intent_constraints=("회사와 보고기간을 명시한다.",),
        stop_conditions=("직접 원문으로 성공 또는 반증되면 중단",),
        source_exhaustion_conditions=("공식 후보를 예산 안에서 소진",),
        supporting_case_ids=("CASE-TEST",),
        supporting_source_verification_ids=(),
        supporting_source_failure_verification_ids=(),
        planning_only_source_proxy_case_ids=(),
        freshness_max_age_days=365,
        freshness_supersession_rule="correction_or_cancellation",
    )


if __name__ == "__main__":
    unittest.main()
