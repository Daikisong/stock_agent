from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.compiler import (
    compile_case_level_source_verification,
    compile_research_intelligence,
    load_historical_case_source_links,
    load_historical_provider_snapshots,
)
from e2r.research_brain.planning import FixtureTwoPassPlannerProvider
from e2r.research_brain.recipes import compile_evidence_recipe_os
from e2r.research_brain.retrieval import compile_semantic_memory_graph
from e2r.research_brain.runtime.live_materialization import (
    BrainPlannerConfig,
    CandidateEvent,
    CurrentBrainPlannerRunner,
    CurrentStateBootstrapper,
    LiveDepth,
    LiveDepthDecision,
    LiveUniverseRow,
    TriggerSignal,
    TriggerType,
    load_planner_run_rows,
    write_brain_planner_run,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_FIXTURES = REPO_ROOT / "tests/fixtures/e2r_reconstruction/corpus"
SOURCE_FIXTURES = REPO_ROOT / "tests/fixtures/e2r_reconstruction/source_verification"


def _universe() -> LiveUniverseRow:
    return LiveUniverseRow(
        symbol="005930",
        company_name="삼성전자",
        market="KOSPI",
        security_group="주권",
        stock_certificate_type="보통주",
        sector_type="",
        listing_date="1975-06-11",
        listing_status="LISTED",
        source_effective_date="2026-07-09",
        source_url="https://data-dbg.krx.co.kr/svc/apis/sto/stk_isu_base_info",
        source_document_id="KRX-UNIVERSE-005930",
        source_content_hash="a" * 64,
        source_request_id="KRX-REQUEST",
        source_mode="LIVE_OFFICIAL_API",
        eligible=True,
        exclusion_reason=None,
        raw_fields={},
    )


def _signal() -> TriggerSignal:
    return TriggerSignal(
        trigger_signal_id="TRIG-005930-OFFICIAL",
        target_id="005930",
        target_name="삼성전자",
        trigger_type=TriggerType.OFFICIAL.value,
        source_event_id="DART-RCEPT-20260710000001",
        effective_date="2026-07-10",
        detected_at="2026-07-10",
        source_refs=("DART-RCEPT-20260710000001",),
        provider_names=("OpenDART",),
        subject_direct=True,
        lifecycle_status="REQUIRES_CURRENT_LIFECYCLE_ADJUDICATION",
        investigation_required=True,
        score_evidence_eligible=False,
        headline_or_snippet_only=False,
        payload={
            "report_name": "단일판매ㆍ공급계약체결",
            "receipt_no": "20260710000001",
        },
    )


def _candidate(signal: TriggerSignal) -> CandidateEvent:
    return CandidateEvent(
        candidate_event_id="CAND-005930",
        target_id="005930",
        target_name="삼성전자",
        as_of_date="2026-07-10",
        latest_effective_date="2026-07-10",
        trigger_types=(signal.trigger_type,),
        trigger_signal_ids=(signal.trigger_signal_id,),
        source_refs=signal.source_refs,
        investigation_required=True,
        active_thesis_present=False,
        score_evidence_eligible=False,
        summary="공식 공시 검증 필요",
    )


def _decision(candidate: CandidateEvent) -> LiveDepthDecision:
    return LiveDepthDecision(
        depth_decision_id="DEPTH-005930",
        target_id="005930",
        target_name="삼성전자",
        as_of_date="2026-07-10",
        completed_depths=(
            LiveDepth.L0_UNIVERSE.value,
            LiveDepth.L1_BASELINE.value,
            LiveDepth.L2_OFFICIAL_LIGHT.value,
            LiveDepth.L3_RESEARCH_BRAIN.value,
        ),
        maximum_depth=LiveDepth.L3_RESEARCH_BRAIN.value,
        candidate_event_id=candidate.candidate_event_id,
        trigger_signal_ids=candidate.trigger_signal_ids,
        priority_score=55.0,
        selected_for_official_light=True,
        selected_for_deep=True,
        selected_for_brain=True,
        acquisition_eligible=True,
        selection_reasons=("TRIGGER_OFFICIAL",),
        not_selected_reason=None,
        source_task_budget={"max_tasks": 4, "max_fetches": 6, "max_retries": 1},
        llm_budget={"max_calls": 2},
        general_web_budget={"max_fetches": 1},
    )


class LiveBrainPlannerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mandatory = compile_research_intelligence(
            [CORPUS_FIXTURES / "golden_mandatory_cases.md"],
            repo_root=REPO_ROOT,
        )
        source_cases = compile_research_intelligence(
            [SOURCE_FIXTURES / "golden_source_cases.jsonl"],
            repo_root=REPO_ROOT,
        )
        cases = (*mandatory.cases, *source_cases.cases)
        source_result = compile_case_level_source_verification(
            cases,
            snapshots=load_historical_provider_snapshots(
                SOURCE_FIXTURES / "provider_snapshots.jsonl"
            ),
            case_source_links=load_historical_case_source_links(
                SOURCE_FIXTURES / "case_source_links.jsonl"
            ),
            repo_root=REPO_ROOT,
        )
        recipes = compile_evidence_recipe_os(
            cases,
            source_verifications=source_result.verifications,
        )
        cls.memory = compile_semantic_memory_graph(
            cases,
            recipes.recipes,
            source_verifications=source_result.verifications,
        ).index

    def setUp(self):
        self.member = _universe()
        self.signal = _signal()
        self.candidate = _candidate(self.signal)
        self.decision = _decision(self.candidate)
        self.state = CurrentStateBootstrapper().bootstrap(
            as_of_date="2026-07-10",
            universe=(self.member,),
        ).records

    def _provider(self, *, mutate_a=None, fail_a=False):
        def pass_a(payload):
            if fail_a:
                raise RuntimeError("fixture planner unavailable")
            source = payload["input"]
            fact = source["current_facts"][0]
            result = {
                "input_id": source["input_id"],
                "hypotheses": [
                    {
                        "hypothesis_id": "H1",
                        "rank": 1,
                        "mechanism_summary": fact["text"],
                        "strength": "MEDIUM",
                        "supporting_fact_ids": [fact["fact_id"]],
                        "contradicting_fact_ids": [],
                        "must_verify_questions": ["직접 원문이 경제적 전환을 확인하는가?"],
                    }
                ],
                "ambiguity_reasons": [],
                "abstain": False,
                "abstention_reason": "",
            }
            return mutate_a(result) if mutate_a else result

        def pass_b(payload):
            source = payload["input"]
            fact = source["current_facts"][0]
            memory = source["balanced_memory"]
            ranked = memory["ranked_archetypes"][:3]
            direct = [
                item for item in memory["memory_items"] if item["role"] == "DIRECT_RECIPE"
            ]
            hypotheses = []
            for rank, item in enumerate(ranked, start=1):
                recipe_ids = [
                    row["recipe_id"]
                    for row in direct
                    if row["archetype_id"] == item["archetype_id"]
                ][:1]
                hypotheses.append(
                    {
                        "archetype_id": item["archetype_id"],
                        "rank": rank,
                        "reason": "현재 사실과 균형 메모리의 경제적 메커니즘이 연결된다.",
                        "supporting_fact_ids": [fact["fact_id"]],
                        "contradicting_fact_ids": [],
                        "recipe_ids": recipe_ids,
                    }
                )
            direct_recipe = next(
                (
                    item
                    for item in direct
                    if hypotheses and item["recipe_id"] in hypotheses[0]["recipe_ids"]
                ),
                None,
            )
            abstain = direct_recipe is None
            drafts = []
            if direct_recipe:
                content = direct_recipe["content"]
                drafts.append(
                    {
                        "draft_id": "D1",
                        "recipe_id": direct_recipe["recipe_id"],
                        "question_to_answer": content["question_to_answer"],
                        "why_material": "leading mechanism의 direct current 확인이 필요하다.",
                        "query_intent": "대상 회사의 공식 자료에서 질문을 직접 확인한다.",
                        "preferred_source_families": content["preferred_source_families"],
                        "fallback_source_families": content["discovery_sources"],
                        "max_queries": 3,
                        "max_candidates": 20,
                        "max_fetches": 5,
                        "stop_condition": "direct anchored claim과 counter 확인 후 중단",
                    }
                )
            return {
                "input_id": source["input_id"],
                "top_k_archetypes": hypotheses,
                "supporting_current_fact_ids": [fact["fact_id"]],
                "contradicting_current_fact_ids": [],
                "positive_thesis": "현재 사실이 leading mechanism 조사 가설을 연다.",
                "counter_thesis": "취소, stale lifecycle 또는 wrong subject이면 가설이 깨진다.",
                "must_verify_questions": ["대상 회사의 direct current 원문이 질문을 충족하는가?"],
                "red_team_questions": ["공시가 취소·정정·종료되었거나 다른 주체의 사실인가?"],
                "source_task_drafts": drafts,
                "do_not_promote_reasons": ["direct evidence와 counter 확인이 남아 있다."],
                "ambiguity_reasons": ["실행 가능한 recipe 없음"] if abstain else [],
                "abstain": abstain,
                "abstention_reason": "실행 가능한 recipe 없음" if abstain else "",
            }

        return FixtureTwoPassPlannerProvider(pass_a=pass_a, pass_b=pass_b)

    def _run(self, provider, *, test_mode=True):
        return CurrentBrainPlannerRunner().run(
            BrainPlannerConfig(
                as_of_date="2026-07-10",
                max_brain_candidates=1,
                max_llm_calls_per_candidate=2,
                test_mode=test_mode,
            ),
            depth_decisions=(self.decision,),
            candidate_events=(self.candidate,),
            trigger_signals=(self.signal,),
            baseline_lanes=(),
            current_state=self.state,
            provider=provider,
            memory_index=self.memory,
        )

    def test_live_operational_audit_records_real_two_pass_calls_and_safe_pending(self):
        audit = json.loads(
            (
                REPO_ROOT / "docs/operational/e2r_live_brain_planner_audit.json"
            ).read_text(encoding="utf-8")
        )

        self.assertEqual(audit["status"], "CURRENT_BRAIN_PLANNER_PASS")
        self.assertGreater(audit["selected_L3_count"], 0)
        self.assertEqual(audit["planner_run_count"], audit["selected_L3_count"])
        self.assertGreater(audit["planner_call_count"], 0)
        self.assertGreater(audit["real_planner_success_count"], 0)
        self.assertEqual(
            audit["planner_pending_count"], audit["exact_llm_blocker_count"]
        )
        self.assertGreater(audit["source_task_draft_count"], 0)
        self.assertEqual(audit["planner_score_stage_key_count"], 0)
        self.assertEqual(audit["future_outcome_prompt_leak_count"], 0)
        self.assertEqual(audit["provider_failure_final_score_count"], 0)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(audit["hard_acceptance_pass"])

    def test_canonical_two_pass_runner_records_plans_prompts_and_responses(self):
        result = self._run(self._provider())

        self.assertEqual(result.status, "CURRENT_BRAIN_PLANNER_FAIL")
        self.assertEqual(len(result.planner_runs), 1)
        self.assertEqual(result.planner_runs[0].terminal_status, "COMPLETE")
        self.assertTrue(result.planner_runs[0].provider_fake)
        self.assertEqual(result.audit["real_planner_success_count"], 0)
        self.assertEqual(result.audit["planner_call_count"], 2)
        self.assertEqual(result.audit["planner_score_stage_key_count"], 0)
        self.assertEqual(result.audit["future_outcome_prompt_leak_count"], 0)
        self.assertEqual(result.audit["provider_failure_final_score_count"], 0)

    def test_provider_failure_is_exact_pending_not_low_score(self):
        result = self._run(self._provider(fail_a=True))

        self.assertEqual(result.planner_runs[0].terminal_status, "PENDING")
        self.assertIsNotNone(result.planner_runs[0].plan.pending)
        self.assertEqual(result.audit["exact_llm_blocker_count"], 1)
        self.assertEqual(result.audit["provider_failure_final_score_count"], 0)

    def test_fake_provider_is_rejected_outside_test_mode(self):
        result = self._run(self._provider(), test_mode=False)

        self.assertEqual(result.status, "CURRENT_BRAIN_PLANNER_FAIL")
        self.assertEqual(result.planner_runs[0].terminal_status, "PENDING")
        self.assertEqual(result.audit["planner_call_count"], 0)

    def test_score_or_stage_provider_key_is_detected_and_rejected(self):
        def inject(payload):
            return {**payload, "score": 99}

        result = self._run(self._provider(mutate_a=inject))

        self.assertEqual(result.status, "CURRENT_BRAIN_PLANNER_FAIL")
        self.assertEqual(result.planner_runs[0].terminal_status, "PENDING")
        self.assertGreater(result.audit["planner_score_stage_key_count"], 0)

    def test_writer_emits_planner_prompt_response_validation_and_memory(self):
        result = self._run(self._provider())
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_brain_planner_run(result, output_root=tmp)
            rows = load_planner_run_rows(paths["runs"])
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["target_id"], "005930")
            self.assertEqual(
                {path.name for path in paths.values()},
                {
                    "planner_runs.jsonl",
                    "llm_prompts.jsonl",
                    "llm_responses.jsonl",
                    "planner_validation.json",
                    "planner_memory_metadata.json",
                },
            )


if __name__ == "__main__":
    unittest.main()
