from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from e2r.research_brain.compiler import (
    compile_case_level_source_verification,
    compile_research_intelligence,
    load_historical_case_source_links,
    load_historical_provider_snapshots,
)
from e2r.research_brain.intelligence_schema import (
    CurrentEvidenceFact,
    PlannerSourceTaskDraft,
)
from e2r.research_brain.planning import (
    FixtureQuestionQueryProvider,
    LegacySourceTaskAdapterStatus,
    QuestionAcceptanceContract,
    QuestionQueryProvider,
    QuestionTaskPlanningStatus,
    SourceBudget,
    SourceRouteContract,
    adapt_legacy_source_task,
    audit_question_source_tasks,
    compile_question_task_context,
    plan_question_source_task,
    question_source_task_to_router_payload,
)
from e2r.research_brain.recipes import compile_evidence_recipe_os
from e2r.research_brain.schemas import SourceTask, SourceTaskType
from e2r.research_brain.source_task_bridge import source_task_to_router_payload


REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_FIXTURES = REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "corpus"
SOURCE_FIXTURES = (
    REPO_ROOT / "tests" / "fixtures" / "e2r_reconstruction" / "source_verification"
)


class QuestionSourceTaskTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
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
        cls.recipes = compile_evidence_recipe_os(
            cases,
            source_verifications=source_result.verifications,
        ).recipes
        cls.recipe = next(
            recipe
            for recipe in cls.recipes
            if recipe.primitive_id == "customer_preorder_or_allocation"
        )

    def _context(self, *, existing_queries=()):
        return compile_question_task_context(
            target_id="TARGET-000660",
            target_name="테스트기업",
            symbol="000660",
            target_aliases=("Test Company",),
            as_of_date="2025-03-31",
            current_facts=(
                CurrentEvidenceFact(
                    fact_id="FACT-1",
                    text="대상 회사는 고객 배정과 생산능력 제약을 현재 사실로 설명했다.",
                    observed_date="2025-03-20",
                    target_relation="DIRECT",
                    current_status="CURRENT",
                ),
            ),
            missing_information=("취소 조건과 계약 구속력을 직접 확인해야 한다.",),
            existing_queries=existing_queries,
        )

    def _draft(self, recipe=None, **updates):
        recipe = recipe or self.recipe
        values = {
            "draft_id": f"DRAFT:{recipe.recipe_id}",
            "recipe_id": recipe.recipe_id,
            "question_to_answer": recipe.question_to_answer,
            "why_material": "현재 메커니즘을 직접 증거와 반증 조건으로 닫아야 한다.",
            "query_intent": (
                "대상 회사의 기준일 이전 공식 문서에서 질문과 취소 조건을 함께 찾는다."
            ),
            "preferred_source_families": recipe.preferred_source_families[:3],
            "fallback_source_families": recipe.discovery_sources[:2],
            "max_queries": 3,
            "max_candidates": 20,
            "max_fetches": 5,
            "stop_condition": "직접 anchor와 counter check가 확인되면 중단한다.",
        }
        values.update(updates)
        return PlannerSourceTaskDraft(**values)

    def _provider(self, mutate=None, fail=False):
        def callback(payload):
            if fail:
                raise RuntimeError("query provider down")
            target = payload["target"]["target_name"]
            result = {
                "input_id": payload["input_id"],
                "literal_queries": [
                    f"{target} 2025 1Q 공식 공시 IR 고객 계약 취소 조건"
                ],
                "generation_rationale": (
                    "대상과 기준 분기를 명시하고 공식 문서의 계약 조건을 우선한다."
                ),
                "ambiguity_reasons": [],
                "abstain": False,
                "abstention_reason": "",
            }
            return mutate(result, payload) if mutate else result

        return FixtureQuestionQueryProvider(callback=callback)

    def _plan(self, *, recipe=None, draft=None, provider=None, context=None, test_mode=True):
        recipe = recipe or self.recipe
        task_type = (
            SourceTaskType.RED_TEAM.value
            if recipe.role in {"GUARD", "HARD_BREAK"}
            else SourceTaskType.POSITIVE_VERIFY.value
        )
        return plan_question_source_task(
            draft=draft or self._draft(recipe),
            recipe=recipe,
            context=context or self._context(),
            candidate_event_id="EVENT-1",
            task_type=task_type,
            provider=provider if provider is not None else self._provider(),
            test_mode=test_mode,
        )

    def test_valid_task_preserves_question_acceptance_source_and_stop_contracts(self) -> None:
        result = self._plan()
        self.assertEqual(result.status, QuestionTaskPlanningStatus.COMPLETE.value)
        task = result.task
        self.assertEqual(task.recipe_id, self.recipe.recipe_id)
        self.assertEqual(task.context_id, self._context().context_id)
        self.assertEqual(task.supporting_current_fact_ids, ("FACT-1",))
        self.assertTrue(task.missing_information)
        self.assertEqual(task.question_to_answer, self.recipe.question_to_answer)
        self.assertEqual(
            task.acceptance_contract.accepted_predicates,
            self.recipe.accepted_claim_predicates,
        )
        self.assertEqual(
            task.acceptance_contract.rejection_conditions,
            self.recipe.rejection_conditions,
        )
        self.assertEqual(
            task.source_route.preferred_document_types,
            self.recipe.preferred_document_types,
        )
        self.assertEqual(task.budget.max_queries, 3)
        self.assertTrue(task.stop_condition.resolution_conditions)
        self.assertTrue(task.stop_condition.exhaustion_conditions)
        self.assertTrue(task.query_intent.literal_queries)
        self.assertEqual(task.query_intent.generation_attempt_count, 1)
        self.assertTrue(task.test_only)
        self.assertFalse(task.production_execution_allowed)
        self.assertFalse(task.runtime_score_eligible)
        self.assertTrue(result.trace.prompt_hash)
        self.assertTrue(result.trace.response_hash)

    def test_query_prompt_uses_current_question_without_taxonomy_or_score_fields(self) -> None:
        captured = []

        def callback(payload):
            captured.append(payload)
            return {
                "input_id": payload["input_id"],
                "literal_queries": [
                    "테스트기업 2025 1Q 공식 공시 IR 고객 계약 취소 조건"
                ],
                "generation_rationale": "현재 질문과 공식 source route를 따른다.",
                "ambiguity_reasons": [],
                "abstain": False,
                "abstention_reason": "",
            }

        result = self._plan(
            provider=FixtureQuestionQueryProvider(callback=callback)
        )
        self.assertEqual(result.status, QuestionTaskPlanningStatus.COMPLETE.value)
        serialized = json.dumps(captured[0], ensure_ascii=False, sort_keys=True).lower()
        self.assertNotIn(self.recipe.archetype_id.lower(), serialized)
        self.assertNotIn(self.recipe.primitive_id.lower(), serialized)
        self.assertNotIn("source_primary", serialized)
        self.assertNotIn("target_score", serialized)
        self.assertNotIn("expected_stage", serialized)

    def test_fixture_task_cannot_enter_production_router(self) -> None:
        task = self._plan().task
        with self.assertRaisesRegex(ValueError, "test-only"):
            question_source_task_to_router_payload(task, production_mode=True)
        payload = question_source_task_to_router_payload(
            task,
            production_mode=False,
        )
        self.assertTrue(payload["canonical_question_task"])
        self.assertTrue(payload["official_first"])
        self.assertEqual(payload["query_intents"], list(task.query_intent.literal_queries))
        self.assertEqual(payload["max_fetches"], 5)

    def test_empty_contract_fields_and_generic_question_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "accepted_predicates"):
            QuestionAcceptanceContract(
                accepted_predicates=(),
                required_entities=("target",),
                required_values=("value",),
                required_units=("KRW",),
                required_time_scope=("as_of",),
                required_target_directness=("DIRECT",),
                required_current_lifecycle=("CURRENT",),
                counter_questions=("Is it cancelled?",),
                rejection_conditions=("Wrong subject",),
            )
        with self.assertRaisesRegex(ValueError, "rejection_conditions"):
            QuestionAcceptanceContract(
                accepted_predicates=self.recipe.accepted_claim_predicates,
                required_entities=self.recipe.required_entities,
                required_values=self.recipe.required_values,
                required_units=self.recipe.required_units,
                required_time_scope=self.recipe.required_time_scope,
                required_target_directness=self.recipe.required_target_directness,
                required_current_lifecycle=self.recipe.required_current_lifecycle,
                counter_questions=self.recipe.counter_questions,
                rejection_conditions=(),
            )
        generic = self._draft(question_to_answer="verify primitive gap evidence")
        with self.assertRaisesRegex(ValueError, "generic verify-primitive"):
            self._plan(draft=generic)
        generic_intent = self._draft(query_intent="verify primitive gap")
        with self.assertRaisesRegex(ValueError, "semantic query intent"):
            self._plan(draft=generic_intent)

    def test_official_first_and_bounded_budget_are_hard_contracts(self) -> None:
        with self.assertRaisesRegex(ValueError, "official-first"):
            SourceRouteContract(
                preferred_source_families=("NaverSearch", "DART"),
                fallback_source_families=("TrustedNewsSearch",),
                preferred_document_types=("filing",),
                preferred_sections=("cash flow",),
                discovery_source_families=("NaverSearch",),
                forbidden_source_families=("search_snippet",),
            )
        for kwargs in (
            {"max_queries": 0, "max_candidates": 20, "max_fetches": 5},
            {"max_queries": 11, "max_candidates": 20, "max_fetches": 5},
            {"max_queries": 3, "max_candidates": 101, "max_fetches": 5},
            {"max_queries": 3, "max_candidates": 20, "max_fetches": 21},
        ):
            with self.subTest(kwargs=kwargs):
                with self.assertRaisesRegex(ValueError, "bounded"):
                    SourceBudget(**kwargs)

    def test_guard_recipe_cannot_be_misrouted_as_positive_verification(self) -> None:
        guard = next(recipe for recipe in self.recipes if recipe.role == "GUARD")
        with self.assertRaisesRegex(ValueError, "defensive task type"):
            plan_question_source_task(
                draft=self._draft(guard),
                recipe=guard,
                context=self._context(),
                candidate_event_id="EVENT-GUARD",
                task_type=SourceTaskType.POSITIVE_VERIFY.value,
                provider=self._provider(),
                test_mode=True,
            )

    def test_invalid_llm_queries_become_pending_without_fallback(self) -> None:
        def query(value):
            def mutate(result, _payload):
                result["literal_queries"] = value
                return result

            return mutate

        invalid = {
            "future": ["테스트기업 2026 Q1 earnings report"],
            "primitive_copy": [
                f"테스트기업 2025 {self.recipe.primitive_id} official filing"
            ],
            "wrong_target": ["다른기업 2025 1Q 공식 공시 계약 조건"],
            "generic": ["verify primitive gap 테스트기업 2025"],
            "relative_time": ["테스트기업 latest official filing contract"],
            "missing_period": ["테스트기업 공식 공시 IR 계약 조건"],
            "score_leak": ["테스트기업 2025 target score=88 official filing"],
            "empty": [],
        }
        for label, queries in invalid.items():
            with self.subTest(label=label):
                result = self._plan(provider=self._provider(mutate=query(queries)))
                self.assertEqual(result.status, QuestionTaskPlanningStatus.PENDING.value)
                self.assertIsNone(result.task)
                self.assertEqual(
                    result.pending.reason_code,
                    "QUERY_VALIDATION_RETRY_EXHAUSTED",
                )
                self.assertEqual(result.pending.attempt_count, 3)
                self.assertEqual(len(result.traces), 3)

    def test_duplicate_or_already_executed_query_is_pending(self) -> None:
        duplicate_query = "테스트기업 2025 1Q 공식 공시 IR 고객 계약 취소 조건"

        def duplicate(result, _payload):
            result["literal_queries"] = [duplicate_query, duplicate_query]
            return result

        duplicate_result = self._plan(provider=self._provider(mutate=duplicate))
        self.assertEqual(
            duplicate_result.status,
            QuestionTaskPlanningStatus.PENDING.value,
        )
        existing_result = self._plan(
            context=self._context(existing_queries=(duplicate_query,))
        )
        self.assertEqual(existing_result.status, QuestionTaskPlanningStatus.PENDING.value)
        self.assertIn("already executed", existing_result.pending.reason_detail)

    def test_invalid_query_feedback_is_returned_to_llm_for_a_new_query(self) -> None:
        captured = []

        def callback(payload):
            captured.append(payload)
            query = (
                "테스트기업 2026 Q1 earnings report"
                if payload["query_generation_attempt"] == 1
                else "테스트기업 2025 1Q 공식 공시 IR 계약 취소 조건"
            )
            return {
                "input_id": payload["input_id"],
                "literal_queries": [query],
                "generation_rationale": "validator feedback를 반영해 기준 기간을 고쳤다.",
                "ambiguity_reasons": [],
                "abstain": False,
                "abstention_reason": "",
            }

        result = self._plan(
            provider=FixtureQuestionQueryProvider(callback=callback)
        )
        self.assertEqual(result.status, QuestionTaskPlanningStatus.COMPLETE.value)
        self.assertEqual(len(result.traces), 2)
        self.assertEqual(len(captured), 2)
        self.assertFalse(captured[0]["validation_feedback"])
        self.assertIn("future", captured[1]["validation_feedback"][0])
        self.assertIn(
            "테스트기업 2026 Q1 earnings report",
            captured[1]["rejected_queries"],
        )
        self.assertEqual(
            result.task.query_intent.literal_queries,
            ("테스트기업 2025 1Q 공식 공시 IR 계약 취소 조건",),
        )
        self.assertEqual(result.task.query_intent.generation_attempt_count, 2)
        self.assertTrue(result.task.query_intent.validation_feedback)
        self.assertEqual(
            result.task.query_intent.rejected_queries,
            ("테스트기업 2026 Q1 earnings report",),
        )

    def test_provider_missing_failure_fake_production_and_abstention_are_explicit(self) -> None:
        missing = plan_question_source_task(
            draft=self._draft(),
            recipe=self.recipe,
            context=self._context(),
            candidate_event_id="EVENT-1",
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            provider=None,
        )
        self.assertEqual(missing.status, QuestionTaskPlanningStatus.PENDING.value)
        self.assertEqual(missing.pending.reason_code, "QUERY_PROVIDER_NOT_CONFIGURED")
        failed = self._plan(provider=self._provider(fail=True))
        self.assertEqual(failed.status, QuestionTaskPlanningStatus.PENDING.value)
        fake_production = self._plan(provider=self._provider(), test_mode=False)
        self.assertEqual(
            fake_production.pending.reason_code,
            "FAKE_QUERY_PROVIDER_NOT_ALLOWED",
        )
        invalid_identity = self._plan(
            provider=QuestionQueryProvider(),
            test_mode=True,
        )
        self.assertEqual(
            invalid_identity.pending.reason_code,
            "INVALID_QUERY_PROVIDER_IDENTITY",
        )

        def abstain(result, _payload):
            result["literal_queries"] = []
            result["abstain"] = True
            result["abstention_reason"] = "No safe target-scoped query remains."
            return result

        abstained = self._plan(provider=self._provider(mutate=abstain))
        self.assertEqual(
            abstained.status,
            QuestionTaskPlanningStatus.ABSTAINED.value,
        )
        self.assertIsNone(abstained.task)
        self.assertTrue(abstained.abstention_reason)

    def test_invalid_returned_response_preserves_raw_response_hash(self) -> None:
        def inject(result, _payload):
            result["score"] = 99
            return result

        result = self._plan(provider=self._provider(mutate=inject))
        self.assertEqual(result.status, QuestionTaskPlanningStatus.PENDING.value)
        expected_payload = {
            "abstain": False,
            "abstention_reason": "",
            "ambiguity_reasons": [],
            "generation_rationale": (
                "대상과 기준 분기를 명시하고 공식 문서의 계약 조건을 우선한다."
            ),
            "input_id": result.input_id,
            "literal_queries": [
                "테스트기업 2025 1Q 공식 공시 IR 고객 계약 취소 조건"
            ],
            "score": 99,
        }
        raw = json.dumps(
            expected_payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        self.assertEqual(
            result.pending.response_hash,
            hashlib.sha256(raw.encode("utf-8")).hexdigest(),
        )

    def test_query_output_types_are_not_coerced(self) -> None:
        def string_boolean(result, _payload):
            result["abstain"] = "false"
            return result

        result = self._plan(provider=self._provider(mutate=string_boolean))
        self.assertEqual(result.status, QuestionTaskPlanningStatus.PENDING.value)
        self.assertIn("must be a boolean", result.pending.reason_detail)

    def test_legacy_task_requires_explicit_recipe_question_and_llm_intent(self) -> None:
        legacy = SourceTask(
            task_id="LEGACY-1",
            candidate_event_id="EVENT-1",
            symbol="000660",
            company_name="테스트기업",
            archetype_id=self.recipe.archetype_id,
            primitive_gap=self.recipe.primitive_id,
            task_type=SourceTaskType.POSITIVE_VERIFY.value,
            preferred_source_classes=("DART", "IR"),
            fallback_source_classes=("TrustedNews",),
        )
        invalid = adapt_legacy_source_task(legacy)
        self.assertEqual(
            invalid.status,
            LegacySourceTaskAdapterStatus.INVALID_LEGACY_TASK.value,
        )
        self.assertEqual(len(invalid.invalid.reason_codes), 4)
        self.assertFalse(invalid.invalid.production_execution_allowed)

        ready = adapt_legacy_source_task(
            legacy,
            recipe_id=self.recipe.recipe_id,
            question_to_answer=self.recipe.question_to_answer,
            why_material="이 질문이 현재 가설의 핵심 공백이다.",
            llm_query_intent="대상 공식 문서에서 직접 조건을 확인한다.",
        )
        self.assertEqual(
            ready.status,
            LegacySourceTaskAdapterStatus.READY_FOR_QUERY_GENERATION.value,
        )
        self.assertEqual(ready.draft.recipe_id, self.recipe.recipe_id)
        with self.assertRaisesRegex(ValueError, "INVALID_LEGACY_TASK"):
            source_task_to_router_payload(legacy)
        diagnostic = source_task_to_router_payload(
            legacy,
            allow_legacy_diagnostic=True,
        )
        self.assertFalse(diagnostic["canonical_execution_allowed"])
        self.assertTrue(diagnostic["legacy_diagnostic_only"])

    def test_all_executable_recipes_compile_to_complete_question_tasks(self) -> None:
        tasks = []
        for recipe in self.recipes:
            result = self._plan(recipe=recipe)
            self.assertEqual(
                result.status,
                QuestionTaskPlanningStatus.COMPLETE.value,
                recipe.recipe_id,
            )
            tasks.append(result.task)
        audit = audit_question_source_tasks(tasks)
        self.assertEqual(audit["status"], "QUESTION_SOURCE_TASK_CONTRACT_PASS")
        self.assertEqual(audit["task_count"], 31)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(audit["fixture_query_provider_task_count"], 31)
        self.assertEqual(audit["real_query_provider_task_count"], 0)
        self.assertEqual(audit["production_execution_allowed_count"], 0)
        self.assertEqual(
            audit["result_hash"],
            "2b20637db04e9517295a0ddd8361cd2ec5956d6c921a8121be7f3d73c62bfa3e",
        )
        self.assertFalse(audit["production_runtime_ready"])

    def test_context_identity_covers_existing_queries(self) -> None:
        first = self._context()
        second = self._context(existing_queries=("테스트기업 2025 1Q 공식 공시",))
        self.assertNotEqual(first.context_id, second.context_id)


if __name__ == "__main__":
    unittest.main()
