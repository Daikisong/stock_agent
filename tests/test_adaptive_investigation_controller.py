from __future__ import annotations

import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

from e2r.agentic.evidence_os import Polarity, SupportDirection
from e2r.research_brain.runtime.adaptive_investigation_controller import (
    AdaptiveInvestigationController,
    AdaptiveInvestigationInput,
    AdaptiveInvestigationStatus,
    FixtureInvestigationPlannerProvider,
    InvestigationFailureReason,
    InvestigationRoundStatus,
    audit_adaptive_investigation_results,
    build_codex_investigation_planner_provider,
    normalize_investigation_failure,
)
from e2r.research_brain.runtime.source_acquisition import (
    AcquisitionStatus,
    BudgetUsage,
)
from e2r.research_brain.runtime.systemic_failure_cluster import (
    CodeRepairHistoryEntry,
    CodeRepairResult,
    audit_systemic_repair_ledger,
    build_systemic_repair_ledger,
    with_code_repair_history,
    write_systemic_repair_ledger,
)
from tests import test_contract_blind_claim_compiler as phase9_tests


class AdaptiveInvestigationControllerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        phase9_tests.ContractBlindClaimCompilerTest.setUpClass()
        cls.phase9 = phase9_tests.ContractBlindClaimCompilerTest(
            methodName="test_contract_blind_input_and_direct_task_satisfaction"
        )
        cls.task = phase9_tests.ContractBlindClaimCompilerTest.task

    def _input(
        self,
        *,
        acquisition,
        compilation,
        previous_rounds=(),
        cumulative_usage=None,
        round_limit=3,
    ):
        return AdaptiveInvestigationInput(
            task=self.task,
            acquisition=acquisition,
            compilation=compilation,
            target_aliases=("Test Company",),
            cumulative_usage=cumulative_usage or acquisition.usage,
            previous_rounds=tuple(previous_rounds),
            round_limit=round_limit,
        )

    def _provider(self, *, captured=None, query_factory=None):
        def callback(payload):
            if captured is not None:
                captured.append(payload)
            reason = payload["failure"]["reason"]
            failed_sources = tuple(
                payload["failure"].get("failed_source_families") or ()
            )
            query = (
                query_factory(payload)
                if query_factory is not None
                else f"테스트기업 2025 1Q 공식 원문 추가 검증 {reason}"
            )
            preferred = next(
                item
                for item in ("IssuerIR", "DART", "KIND", "KRX", "NaverSearch")
                if item not in failed_sources
            )
            return {
                "input_id": payload["input_id"],
                "failure_reason": reason,
                "literal_queries": [query],
                "changed_dimensions": payload["required_changed_dimensions"],
                "source_constraints": {
                    "prefer": [preferred],
                    "exclude": list(
                        failed_sources
                        or (payload["source_route"]["preferred_source_families"][0],)
                    ),
                    "required_changes": [
                        "use a different bounded provider/source path"
                    ],
                },
                "document_constraints": {
                    "required_document_types": ["filing"],
                    "required_sections": ["direct claim and counter conditions"],
                    "freshness_or_date_constraints": [
                        "published and available on or before 2025-03-31"
                    ],
                    "required_provenance": [
                        "full original source with content hash and exact anchor"
                    ],
                },
                "target_constraints": {
                    "required_subjects": ["테스트기업"],
                    "required_directness": ["DIRECT"],
                    "excluded_subjects": ["industry-only or customer-only subject"],
                },
                "rationale": f"change constraints for {reason}",
                "abstain": False,
                "abstention_reason": "",
            }

        return FixtureInvestigationPlannerProvider(callback=callback)

    def _failure_inputs(self):
        direct_acq = self.phase9._acquisition(candidate_id="PHASE10-DIRECT")
        direct = self.phase9._compile(acquisition=direct_acq)

        wrong_acq = self.phase9._acquisition(
            candidate_id="PHASE10-WRONG",
            text=self.phase9._text(other_subject=True),
        )
        wrong = self.phase9._compile(
            acquisition=wrong_acq,
            extractor=self.phase9._extractor(subject="다른기업"),
        )

        stale_acq = self.phase9._acquisition(
            candidate_id="PHASE10-STALE",
            text=self.phase9._text(old_period=True),
        )
        stale = self.phase9._compile(
            acquisition=stale_acq,
            extractor=self.phase9._extractor(
                polarity=Polarity.NEGATIVE,
                event_date="2020-01-01",
                effective_period="2020-01-01 to 2020-12-31",
            ),
            mapper=self.phase9._mapper(direction=SupportDirection.COUNTER),
        )

        reroute_acq = self.phase9._acquisition(candidate_id="PHASE10-REROUTE")
        reroute = self.phase9._compile(
            acquisition=reroute_acq,
            mapper=self.phase9._mapper(recipe=self.phase9.reroute_recipe),
        )

        mapping_acq = self.phase9._acquisition(candidate_id="PHASE10-MAPPING")
        mapping = self.phase9._compile(
            acquisition=mapping_acq,
            mapper=self.phase9._mapper(complete_fields=False),
        )

        generic_acq = self.phase9._acquisition(candidate_id="PHASE10-GENERIC")
        generic = self.phase9._compile(
            acquisition=generic_acq,
            mapper=self.phase9._mapper(empty=True),
        )

        contradiction_acq = self.phase9._acquisition(
            candidate_id="PHASE10-CONTRADICTION"
        )
        contradiction = self.phase9._compile(
            acquisition=contradiction_acq,
            extractor=self.phase9._extractor(polarity=Polarity.NEGATIVE),
            mapper=self.phase9._mapper(direction=SupportDirection.COUNTER),
        )

        provider_acq = self.phase9._provider_failed_acquisition()
        provider = self.phase9._compile(acquisition=provider_acq)

        exhausted_acq = self.phase9._source_exhausted_acquisition()
        exhausted = self.phase9._compile(acquisition=exhausted_acq)

        no_document_acq = replace(
            exhausted_acq,
            acquisition_id=f"NO-DOCUMENT-{exhausted_acq.acquisition_id}",
            status=AcquisitionStatus.NO_EVIDENCE.value,
            source_gaps=(),
            stop_reason="connectors_returned_no_candidates",
        )
        no_document = self.phase9._compile(acquisition=no_document_acq)

        return {
            "RESOLVED": self._input(
                acquisition=direct_acq,
                compilation=direct,
            ),
            InvestigationFailureReason.NO_DOCUMENT_FOUND.value: self._input(
                acquisition=no_document_acq,
                compilation=no_document,
            ),
            InvestigationFailureReason.WRONG_SUBJECT.value: self._input(
                acquisition=wrong_acq,
                compilation=wrong,
            ),
            InvestigationFailureReason.STALE_ONLY.value: self._input(
                acquisition=stale_acq,
                compilation=stale,
            ),
            InvestigationFailureReason.GENERIC_CONTEXT_ONLY.value: self._input(
                acquisition=generic_acq,
                compilation=generic,
            ),
            InvestigationFailureReason.REROUTED_PRIMITIVE.value: self._input(
                acquisition=reroute_acq,
                compilation=reroute,
            ),
            InvestigationFailureReason.MAPPING_REJECTED.value: self._input(
                acquisition=mapping_acq,
                compilation=mapping,
            ),
            InvestigationFailureReason.CONTRADICTION_OPEN.value: self._input(
                acquisition=contradiction_acq,
                compilation=contradiction,
            ),
            InvestigationFailureReason.PROVIDER_FAILED.value: self._input(
                acquisition=provider_acq,
                compilation=provider,
            ),
            InvestigationFailureReason.SOURCE_EXHAUSTED.value: self._input(
                acquisition=exhausted_acq,
                compilation=exhausted,
            ),
        }

    def test_every_runtime_failure_normalizes_to_exact_taxonomy(self) -> None:
        inputs_by_reason = self._failure_inputs()
        self.assertIsNone(
            normalize_investigation_failure(inputs_by_reason.pop("RESOLVED"))
        )
        self.assertEqual(
            set(inputs_by_reason),
            {reason.value for reason in InvestigationFailureReason},
        )
        for expected, inputs in inputs_by_reason.items():
            with self.subTest(expected=expected):
                failure = normalize_investigation_failure(inputs)
                self.assertIsNotNone(failure)
                self.assertEqual(failure.reason, expected)
                self.assertTrue(failure.detail)
                self.assertEqual(failure.task_id, self.task.task_id)
                if expected == InvestigationFailureReason.PROVIDER_FAILED.value:
                    self.assertIn(
                        self.task.source_route.preferred_source_families[0],
                        failure.failed_source_families,
                    )

    def test_cumulative_budget_usage_cannot_under_report_acquisition(self) -> None:
        inputs = self._failure_inputs()[InvestigationFailureReason.WRONG_SUBJECT.value]
        with self.assertRaisesRegex(ValueError, "cannot under-report"):
            self._input(
                acquisition=inputs.acquisition,
                compilation=inputs.compilation,
                cumulative_usage=BudgetUsage(),
            )

    def test_valid_llm_abstention_is_pending_with_provider_trace(self) -> None:
        inputs = self._failure_inputs()[InvestigationFailureReason.WRONG_SUBJECT.value]

        def abstains(payload):
            return {
                "input_id": payload["input_id"],
                "failure_reason": payload["failure"]["reason"],
                "literal_queries": [],
                "changed_dimensions": [],
                "source_constraints": {
                    "prefer": [],
                    "exclude": [],
                    "required_changes": [],
                },
                "document_constraints": {
                    "required_document_types": [],
                    "required_sections": [],
                    "freshness_or_date_constraints": [],
                    "required_provenance": [],
                },
                "target_constraints": {
                    "required_subjects": [],
                    "required_directness": [],
                    "excluded_subjects": [],
                },
                "rationale": "현재 bounded 조건으로는 안전한 다음 query를 만들 수 없다",
                "abstain": True,
                "abstention_reason": "direct source route needs operator review",
            }

        result = AdaptiveInvestigationController(
            provider=FixtureInvestigationPlannerProvider(callback=abstains),
            test_mode=True,
        ).plan_next(inputs)
        self.assertEqual(result.status, AdaptiveInvestigationStatus.PENDING.value)
        self.assertTrue(
            result.current_round.pending_reason.startswith(
                "INVESTIGATION_LLM_ABSTAINED:"
            )
        )
        self.assertEqual(len(result.current_round.traces), 1)
        self.assertIsNone(result.current_round.traces[0].validation_error)
        self.assertFalse(result.score_valid)

    def test_real_codex_provider_builder_reuses_canonical_transport(self) -> None:
        with patch.dict("os.environ", {}, clear=True):
            provider = build_codex_investigation_planner_provider(
                working_directory=Path.cwd(),
                load_env=False,
            )
        self.assertTrue(provider.real_provider)
        self.assertFalse(provider.fake_provider)
        self.assertEqual(provider.transport.working_directory, Path.cwd())
        self.assertEqual(provider.transport.sandbox, "read-only")
        self.assertEqual(provider.transport.approval_policy, "never")

    def test_each_failure_plans_a_distinct_bounded_constraint_change(self) -> None:
        results = {}
        inputs_by_reason = self._failure_inputs()
        inputs_by_reason.pop("RESOLVED")
        for reason, inputs in inputs_by_reason.items():
            with self.subTest(reason=reason):
                result = AdaptiveInvestigationController(
                    provider=self._provider(),
                    test_mode=True,
                ).plan_next(inputs)
                self.assertEqual(
                    result.status,
                    AdaptiveInvestigationStatus.ACTION_PLANNED.value,
                )
                action = result.current_round.action
                self.assertIsNotNone(action)
                self.assertEqual(action.failure_reason, reason)
                self.assertTrue(action.literal_queries)
                self.assertLessEqual(
                    len(action.literal_queries),
                    action.budget.max_queries,
                )
                self.assertTrue(action.source_constraints.prefer)
                self.assertFalse(
                    set(action.source_constraints.prefer).intersection(
                        action.source_constraints.exclude
                    )
                )
                if "SOURCE" in action.changed_dimensions:
                    failed_sources = set(
                        result.current_round.failure.failed_source_families
                    )
                    if failed_sources:
                        self.assertTrue(
                            any(
                                source not in failed_sources
                                for source in action.source_constraints.prefer
                            ),
                            action.failure_reason,
                        )
                self.assertTrue(action.document_constraints.required_sections)
                self.assertIn("테스트기업", action.target_constraints.required_subjects)
                self.assertFalse(action.deterministic_query_synthesis)
                self.assertTrue(action.material_gap_open)
                self.assertFalse(action.score_valid)
                self.assertFalse(action.coding_agent_repair)
                results[reason] = result
        rerouted = results[InvestigationFailureReason.REROUTED_PRIMITIVE.value]
        feedback = rerouted.current_round.action.rerouted_feedback
        self.assertIsNotNone(feedback)
        self.assertTrue(feedback.accepted_claim_ids)
        self.assertTrue(feedback.mapped_primitive_ids)
        self.assertEqual(feedback.original_primitive_id, self.task.primitive_id)
        self.assertTrue(feedback.sources_to_avoid_repeating)
        sample = results[InvestigationFailureReason.WRONG_SUBJECT.value]
        with self.assertRaisesRegex(ValueError, "failure task mismatch"):
            replace(sample.current_round, task_id="ANOTHER-TASK")

    def test_identical_query_is_rejected_and_feedback_returns_to_llm(self) -> None:
        captured = []
        original_query = self.task.query_intent.literal_queries[0]
        inputs = self._failure_inputs()[InvestigationFailureReason.WRONG_SUBJECT.value]
        result = AdaptiveInvestigationController(
            provider=self._provider(
                captured=captured,
                query_factory=lambda _payload: original_query,
            ),
            test_mode=True,
        ).plan_next(inputs)
        self.assertEqual(result.status, AdaptiveInvestigationStatus.PENDING.value)
        self.assertEqual(
            result.current_round.pending_reason,
            "INVESTIGATION_VALIDATION_RETRY_EXHAUSTED",
        )
        self.assertIsNone(result.current_round.action)
        self.assertEqual(len(result.current_round.traces), 3)
        self.assertEqual(len(captured), 3)
        self.assertFalse(captured[0]["validation_feedback"])
        self.assertTrue(captured[1]["validation_feedback"])
        self.assertIn(original_query, captured[1]["rejected_queries"])
        self.assertFalse(result.score_valid)

        valid_provider = self._provider()

        def contradictory_source(payload):
            response = dict(valid_provider.callback(payload))
            constraints = dict(response["source_constraints"])
            constraints["prefer"] = [constraints["exclude"][0]]
            response["source_constraints"] = constraints
            return response

        source_result = AdaptiveInvestigationController(
            provider=FixtureInvestigationPlannerProvider(
                callback=contradictory_source
            ),
            test_mode=True,
            max_provider_attempts=1,
        ).plan_next(inputs)
        self.assertEqual(
            source_result.current_round.pending_reason,
            "INVESTIGATION_VALIDATION_RETRY_EXHAUSTED",
        )
        self.assertIn(
            "both preferred and excluded",
            source_result.current_round.traces[0].validation_error,
        )

        def future_document_constraint(payload):
            response = dict(valid_provider.callback(payload))
            constraints = dict(response["document_constraints"])
            constraints["freshness_or_date_constraints"] = [
                "published on or before 2026-01-01"
            ]
            response["document_constraints"] = constraints
            return response

        future_result = AdaptiveInvestigationController(
            provider=FixtureInvestigationPlannerProvider(
                callback=future_document_constraint
            ),
            test_mode=True,
            max_provider_attempts=1,
        ).plan_next(inputs)
        self.assertEqual(
            future_result.current_round.pending_reason,
            "INVESTIGATION_VALIDATION_RETRY_EXHAUSTED",
        )
        self.assertIn(
            "future reporting year",
            future_result.current_round.traces[0].validation_error,
        )

    def test_resolved_task_never_retries_without_failure_reason(self) -> None:
        calls = []
        resolved = self._failure_inputs()["RESOLVED"]
        result = AdaptiveInvestigationController(
            provider=self._provider(captured=calls),
            test_mode=True,
        ).plan_next(resolved)
        self.assertEqual(result.status, AdaptiveInvestigationStatus.RESOLVED.value)
        self.assertEqual(result.current_round.status, InvestigationRoundStatus.RESOLVED.value)
        self.assertIsNone(result.current_round.failure)
        self.assertIsNone(result.current_round.action)
        self.assertEqual(calls, [])
        self.assertFalse(result.self_repair_claimed)
        with self.assertRaisesRegex(ValueError, "cannot keep a gap or forge a score"):
            replace(result.current_round, material_gap_open=True)
        with self.assertRaisesRegex(ValueError, "cannot forge score finalization"):
            replace(result, score_valid=True)

    def test_round_budget_and_provider_limits_become_pending(self) -> None:
        inputs = self._failure_inputs()[InvestigationFailureReason.WRONG_SUBJECT.value]
        with self.assertRaisesRegex(ValueError, "test_mode must be boolean"):
            AdaptiveInvestigationController(
                provider=self._provider(),
                test_mode="true",
            )
        planned = AdaptiveInvestigationController(
            provider=self._provider(),
            test_mode=True,
        ).plan_next(inputs)
        round_limited = AdaptiveInvestigationController(
            provider=self._provider(),
            test_mode=True,
        ).plan_next(
            self._input(
                acquisition=inputs.acquisition,
                compilation=inputs.compilation,
                previous_rounds=(planned.current_round,),
                round_limit=1,
            )
        )
        self.assertEqual(round_limited.status, AdaptiveInvestigationStatus.PENDING.value)
        self.assertEqual(
            round_limited.current_round.pending_reason,
            "ROUND_LIMIT_REACHED",
        )

        budget_exhausted = AdaptiveInvestigationController(
            provider=self._provider(),
            test_mode=True,
        ).plan_next(
            self._input(
                acquisition=inputs.acquisition,
                compilation=inputs.compilation,
                cumulative_usage=BudgetUsage(
                    queries=self.task.budget.max_queries,
                    candidates=self.task.budget.max_candidates,
                    fetches=self.task.budget.max_fetches,
                ),
            )
        )
        self.assertEqual(
            budget_exhausted.current_round.pending_reason,
            "INVESTIGATION_BUDGET_EXHAUSTED",
        )
        missing_provider = AdaptiveInvestigationController(
            provider=None,
            test_mode=False,
        ).plan_next(inputs)
        self.assertEqual(
            missing_provider.current_round.pending_reason,
            "INVESTIGATION_PROVIDER_NOT_CONFIGURED",
        )

        def raises(_payload):
            raise RuntimeError("provider unavailable")

        provider_failed = AdaptiveInvestigationController(
            provider=FixtureInvestigationPlannerProvider(callback=raises),
            test_mode=True,
        ).plan_next(inputs)
        self.assertTrue(
            provider_failed.current_round.pending_reason.startswith(
                "INVESTIGATION_PROVIDER_ERROR:RuntimeError"
            )
        )
        self.assertEqual(len(provider_failed.current_round.traces), 1)
        self.assertTrue(
            provider_failed.current_round.traces[0].validation_error.startswith(
                "INVESTIGATION_PROVIDER_ERROR:RuntimeError"
            )
        )
        for result in (
            round_limited,
            budget_exhausted,
            missing_provider,
            provider_failed,
        ):
            self.assertTrue(result.material_gap_open)
            self.assertFalse(result.score_valid)
            self.assertFalse(result.score_finalization_allowed)
            self.assertFalse(result.self_repair_claimed)

    def test_systemic_cluster_and_code_repair_history_are_separate(self) -> None:
        inputs = self._failure_inputs()[InvestigationFailureReason.WRONG_SUBJECT.value]
        first = AdaptiveInvestigationController(
            provider=self._provider(),
            test_mode=True,
        ).plan_next(inputs).current_round
        second_task_id = f"{first.task_id}:SECOND-TARGET"
        second_failure = replace(
            first.failure,
            failure_id=f"{first.failure.failure_id}:SECOND",
            task_id=second_task_id,
        )
        second_action = replace(
            first.action,
            action_id=f"{first.action.action_id}:SECOND",
            task_id=second_task_id,
        )
        second = replace(
            first,
            round_id=f"{first.round_id}:SECOND",
            task_id=second_task_id,
            failure=second_failure,
            action=second_action,
        )
        ledger = build_systemic_repair_ledger(rounds=(first, second))
        self.assertEqual(len(ledger.clusters), 1)
        cluster = ledger.clusters[0]
        self.assertEqual(cluster.distinct_task_count, 2)
        self.assertTrue(cluster.systemic_code_repair_candidate)
        self.assertFalse(cluster.runtime_query_retry_is_code_repair)
        history = CodeRepairHistoryEntry.build(
            cluster=cluster,
            commit_sha="TEST-FIXTURE-COMMIT",
            changed_files=("runtime/adaptive_investigation_controller.py",),
            verification_tests=("tests.test_adaptive_investigation_controller",),
            result=CodeRepairResult.VERIFIED,
            result_detail="fixture proves systemic repair ledger separation",
            repaired_by="coding-agent-fixture",
            test_only=True,
        )
        ledger = with_code_repair_history(ledger, (history,))
        audit = audit_systemic_repair_ledger(ledger)
        self.assertEqual(audit["status"], "SYSTEMIC_REPAIR_SEPARATION_PASS")
        self.assertEqual(audit["cluster_count"], 1)
        self.assertEqual(audit["code_repair_history_count"], 1)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(
            audit["result_hash"],
            "3588710cea478e0eebfa43548b60528e57fb252eeb25050441e096ab5e6bf03d",
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = write_systemic_repair_ledger(
                Path(tmp) / "systemic_repair.json",
                ledger,
            )
            payload = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(payload["ledger_id"], ledger.ledger_id)
        self.assertFalse(history.runtime_investigation_action)
        with self.assertRaisesRegex(ValueError, "requires a git commit SHA"):
            CodeRepairHistoryEntry.build(
                cluster=cluster,
                commit_sha="NOT-A-REAL-COMMIT",
                changed_files=("runtime/adaptive_investigation_controller.py",),
                verification_tests=("tests.test_adaptive_investigation_controller",),
                result=CodeRepairResult.VERIFIED,
                result_detail="fixture provenance cannot count as production repair",
                repaired_by="coding-agent",
                test_only=False,
            )

    def test_adaptive_audit_has_zero_critical_violations(self) -> None:
        inputs_by_reason = self._failure_inputs()
        resolved_input = inputs_by_reason.pop("RESOLVED")
        results = [
            AdaptiveInvestigationController(
                provider=self._provider(),
                test_mode=True,
            ).plan_next(inputs)
            for inputs in inputs_by_reason.values()
        ]
        results.append(
            AdaptiveInvestigationController(
                provider=self._provider(),
                test_mode=True,
            ).plan_next(resolved_input)
        )
        audit = audit_adaptive_investigation_results(
            results,
            tasks_by_id={self.task.task_id: self.task},
        )
        self.assertEqual(audit["status"], "ADAPTIVE_EVIDENCE_CLOSURE_PASS")
        self.assertEqual(audit["result_count"], 10)
        self.assertEqual(audit["planned_action_count"], 9)
        self.assertEqual(audit["resolved_round_count"], 1)
        self.assertEqual(audit["rerouted_feedback_action_count"], 1)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(all(value == 0 for value in audit["critical_counts"].values()))
        self.assertEqual(
            audit["result_hash"],
            "53f997ca1e88e4836e612683854ece9b9c14386b7495c8fce48e22033850fd5a",
        )
        self.assertFalse(audit["production_runtime_ready"])


if __name__ == "__main__":
    unittest.main()
