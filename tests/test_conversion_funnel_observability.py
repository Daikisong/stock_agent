from __future__ import annotations

import unittest
from copy import deepcopy
from dataclasses import replace
from pathlib import Path
from tempfile import TemporaryDirectory

from e2r.research_brain.runtime.atomic_score_stage import (
    AtomicPrimitiveAssessment,
    AtomicPrimitiveStatus,
    AtomicScoreRule,
    AtomicScoringInput,
    AtomicScoringScope,
    AtomicScoreType,
    adapt_claim_ledger_event_to_atomic_claim,
    decide_atomic_score_stage,
)
from e2r.research_brain.runtime.conversion_funnel import (
    FunnelCandidate,
    FunnelLeafStatus,
    FunnelMetricScope,
    FunnelStage,
    FunnelStageLeaf,
    FunnelUsageRecord,
    ConversionFunnelInput,
    audit_conversion_funnel,
    compile_conversion_funnel,
    original_gap_id_for_question_source_task,
    record_question_source_task_leaves,
    write_conversion_funnel,
)
from e2r.research_brain.runtime.current_operation import CurrentDeepOutcome
from tests import test_contract_blind_claim_compiler as phase9_fixture


class ConversionFunnelObservabilityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.as_of_date = "2026-06-30"
        cls.specs = (
            ("CAND-FULL", "TARGET-FULL", "ARCH-FULL"),
            ("CAND-REROUTED", "TARGET-REROUTED", "ARCH-ORIGINAL"),
            ("CAND-MAPPING", "TARGET-MAPPING", "ARCH-MAPPING"),
            ("CAND-PROVIDER", "TARGET-PROVIDER", "ARCH-PROVIDER"),
            ("CAND-RISK", "TARGET-RISK", "ARCH-RISK"),
        )
        cls.candidates = tuple(
            FunnelCandidate(
                candidate_id=candidate_id,
                target_id=target_id,
                target_name=f"기업-{target_id}",
                as_of_date=cls.as_of_date,
                archetype_ids=(archetype_id,),
                primary_archetype_id=archetype_id,
                selected_for_deep=True,
                selection_reason="bounded current trigger priority",
            )
            for candidate_id, target_id, archetype_id in cls.specs
        )
        leaves: list[FunnelStageLeaf] = []
        paths: dict[str, dict[str, str]] = {}
        for candidate_id, _, archetype_id in cls.specs:
            paths[candidate_id] = cls._prefix(
                leaves,
                candidate_id=candidate_id,
                archetype_id=archetype_id,
            )

        full = paths["CAND-FULL"]
        full_result = cls._add(
            leaves,
            "FULL-RESULT",
            "CAND-FULL",
            FunnelStage.RESULT,
            FunnelLeafStatus.RETURNED.value,
            (full["query"],),
            "ARCH-FULL",
            recipe_id=full["recipe_id"],
            task_id=full["task_id"],
            query_text=full["query_text"],
        )
        full_fetch = cls._document_path(
            leaves,
            prefix="FULL",
            candidate_id="CAND-FULL",
            archetype_id="ARCH-FULL",
            parent_id=full_result,
            recipe_id=full["recipe_id"],
            task_id=full["task_id"],
        )
        full_claim = cls._claim_path(
            leaves,
            prefix="FULL",
            candidate_id="CAND-FULL",
            archetype_id="ARCH-FULL",
            assertion_parent=full_fetch["relevant"],
            document_id=full_fetch["document_id"],
            recipe_id=full["recipe_id"],
            task_id=full["task_id"],
            original_gap_id=full["gap_id"],
            primitive_id=full["primitive_id"],
            claim_status=FunnelLeafStatus.ACCEPTED_DIRECT.value,
            primitive_status=FunnelLeafStatus.SATISFIED.value,
        )
        full_score = cls._add(
            leaves,
            "FULL-SCORE",
            "CAND-FULL",
            FunnelStage.SCORE,
            AtomicScoreType.FULL_E2R_100.value,
            (full_claim["primitive"],),
            "ARCH-FULL",
            score_decision_id="DECISION-FULL",
            score_value=100.0,
            raw_reference_score=100.0,
            score_finalization_allowed=True,
        )
        cls._terminal(
            leaves,
            prefix="FULL",
            candidate_id="CAND-FULL",
            archetype_id="ARCH-FULL",
            parent_id=full_score,
            outcome=CurrentDeepOutcome.FULL_THESIS,
            reason="all material current claims directly closed",
        )

        rerouted = paths["CAND-REROUTED"]
        rerouted_result = cls._add(
            leaves,
            "REROUTED-RESULT",
            "CAND-REROUTED",
            FunnelStage.RESULT,
            FunnelLeafStatus.RETURNED.value,
            (rerouted["query"],),
            "ARCH-ORIGINAL",
            recipe_id=rerouted["recipe_id"],
            task_id=rerouted["task_id"],
            query_text=rerouted["query_text"],
        )
        rerouted_fetch = cls._document_path(
            leaves,
            prefix="REROUTED",
            candidate_id="CAND-REROUTED",
            archetype_id="ARCH-ORIGINAL",
            parent_id=rerouted_result,
            recipe_id=rerouted["recipe_id"],
            task_id=rerouted["task_id"],
        )
        rerouted_claim = cls._claim_path(
            leaves,
            prefix="REROUTED",
            candidate_id="CAND-REROUTED",
            archetype_id="ARCH-ALTERNATE",
            assertion_parent=rerouted_fetch["relevant"],
            document_id=rerouted_fetch["document_id"],
            recipe_id="RECIPE-ALTERNATE",
            task_id=rerouted["task_id"],
            original_gap_id=rerouted["gap_id"],
            primitive_id="PRIMITIVE-ALTERNATE",
            claim_status=FunnelLeafStatus.ACCEPTED_REROUTED.value,
            primitive_status=FunnelLeafStatus.REROUTED.value,
            assertion_archetype_id="ARCH-ORIGINAL",
            assertion_recipe_id=rerouted["recipe_id"],
        )
        rerouted_score = cls._add(
            leaves,
            "REROUTED-SCORE",
            "CAND-REROUTED",
            FunnelStage.SCORE,
            AtomicScoreType.NO_SCORE.value,
            (rerouted_claim["primitive"],),
            "ARCH-ALTERNATE",
            score_decision_id="DECISION-REROUTED",
            raw_reference_score=25.0,
        )
        cls._terminal(
            leaves,
            prefix="REROUTED",
            candidate_id="CAND-REROUTED",
            archetype_id="ARCH-ORIGINAL",
            parent_id=rerouted_score,
            outcome=CurrentDeepOutcome.SOURCE_PENDING,
            reason="original_gap_open_after_rerouted_claim",
        )
        extra_result = cls._add(
            leaves,
            "REROUTED-EXTRA-RESULT",
            "CAND-REROUTED",
            FunnelStage.RESULT,
            FunnelLeafStatus.RETURNED.value,
            (rerouted["query"],),
            "ARCH-ORIGINAL",
            recipe_id=rerouted["recipe_id"],
            task_id=rerouted["task_id"],
            query_text=rerouted["query_text"],
        )
        cls._add(
            leaves,
            "REROUTED-IRRELEVANT-FETCH",
            "CAND-REROUTED",
            FunnelStage.FETCHED_DOCUMENT,
            FunnelLeafStatus.FETCHED.value,
            (extra_result,),
            "ARCH-ORIGINAL",
            recipe_id=rerouted["recipe_id"],
            task_id=rerouted["task_id"],
            document_id="DOC-REROUTED-IRRELEVANT",
        )

        mapping = paths["CAND-MAPPING"]
        mapping_result = cls._add(
            leaves,
            "MAPPING-RESULT",
            "CAND-MAPPING",
            FunnelStage.RESULT,
            FunnelLeafStatus.RETURNED.value,
            (mapping["query"],),
            "ARCH-MAPPING",
            recipe_id=mapping["recipe_id"],
            task_id=mapping["task_id"],
            query_text=mapping["query_text"],
        )
        mapping_fetch = cls._document_path(
            leaves,
            prefix="MAPPING",
            candidate_id="CAND-MAPPING",
            archetype_id="ARCH-MAPPING",
            parent_id=mapping_result,
            recipe_id=mapping["recipe_id"],
            task_id=mapping["task_id"],
        )
        mapping_assertion = cls._add(
            leaves,
            "MAPPING-ASSERTION",
            "CAND-MAPPING",
            FunnelStage.ASSERTION,
            FunnelLeafStatus.EXTRACTED.value,
            (mapping_fetch["relevant"],),
            "ARCH-MAPPING",
            recipe_id=mapping["recipe_id"],
            task_id=mapping["task_id"],
            document_id=mapping_fetch["document_id"],
            assertion_id="ASSERTION-MAPPING",
        )
        mapping_claim = cls._add(
            leaves,
            "MAPPING-CLAIM",
            "CAND-MAPPING",
            FunnelStage.CLAIM,
            FunnelLeafStatus.MAPPING_REJECTED.value,
            (mapping_assertion,),
            "ARCH-MAPPING",
            recipe_id=mapping["recipe_id"],
            task_id=mapping["task_id"],
            original_gap_id=mapping["gap_id"],
            primitive_id=mapping["primitive_id"],
            document_id=mapping_fetch["document_id"],
            assertion_id="ASSERTION-MAPPING",
            claim_id="CLAIM-MAPPING",
        )
        cls._terminal(
            leaves,
            prefix="MAPPING",
            candidate_id="CAND-MAPPING",
            archetype_id="ARCH-MAPPING",
            parent_id=mapping_claim,
            outcome=CurrentDeepOutcome.SOURCE_PENDING,
            reason="mapping_rejected_original_gap_open",
        )

        provider = paths["CAND-PROVIDER"]
        provider_result = cls._add(
            leaves,
            "PROVIDER-RESULT",
            "CAND-PROVIDER",
            FunnelStage.RESULT,
            FunnelLeafStatus.PROVIDER_FAILED.value,
            (provider["query"],),
            "ARCH-PROVIDER",
            recipe_id=provider["recipe_id"],
            task_id=provider["task_id"],
            query_text=provider["query_text"],
            provider_error="official provider timeout",
        )
        cls._terminal(
            leaves,
            prefix="PROVIDER",
            candidate_id="CAND-PROVIDER",
            archetype_id="ARCH-PROVIDER",
            parent_id=provider_result,
            outcome=CurrentDeepOutcome.PROVIDER_PENDING,
            reason="official_provider_timeout",
        )

        risk = paths["CAND-RISK"]
        risk_result = cls._add(
            leaves,
            "RISK-RESULT",
            "CAND-RISK",
            FunnelStage.RESULT,
            FunnelLeafStatus.RETURNED.value,
            (risk["query"],),
            "ARCH-RISK",
            recipe_id=risk["recipe_id"],
            task_id=risk["task_id"],
            query_text=risk["query_text"],
        )
        risk_fetch = cls._document_path(
            leaves,
            prefix="RISK",
            candidate_id="CAND-RISK",
            archetype_id="ARCH-RISK",
            parent_id=risk_result,
            recipe_id=risk["recipe_id"],
            task_id=risk["task_id"],
        )
        risk_claim = cls._claim_path(
            leaves,
            prefix="RISK",
            candidate_id="CAND-RISK",
            archetype_id="ARCH-RISK",
            assertion_parent=risk_fetch["relevant"],
            document_id=risk_fetch["document_id"],
            recipe_id=risk["recipe_id"],
            task_id=risk["task_id"],
            original_gap_id=risk["gap_id"],
            primitive_id=risk["primitive_id"],
            claim_status=FunnelLeafStatus.COUNTER_DIRECT.value,
            primitive_status=FunnelLeafStatus.COUNTER.value,
        )
        risk_score = cls._add(
            leaves,
            "RISK-SCORE",
            "CAND-RISK",
            FunnelStage.SCORE,
            AtomicScoreType.NO_SCORE.value,
            (risk_claim["primitive"],),
            "ARCH-RISK",
            score_decision_id="DECISION-RISK",
            raw_reference_score=75.0,
            hard_break=True,
        )
        cls._terminal(
            leaves,
            prefix="RISK",
            candidate_id="CAND-RISK",
            archetype_id="ARCH-RISK",
            parent_id=risk_score,
            outcome=CurrentDeepOutcome.DISPROVED,
            reason="current_direct_material_hard_break",
        )
        cls.leaves = tuple(leaves)
        cls.usage_records = tuple(
            cls._usage(
                candidate_id,
                archetype_id,
                paths[candidate_id]["query"],
                result_count=result_count,
                fetch_count=fetch_count,
                tokens=tokens,
                cost=cost,
                runtime=runtime,
            )
            for (
                candidate_id,
                _,
                archetype_id,
            ), result_count, fetch_count, tokens, cost, runtime in zip(
                cls.specs,
                (1, 2, 1, 0, 1),
                (1, 2, 1, 0, 1),
                (150, 300, 150, 50, 150),
                (0.10, 0.20, 0.10, 0.05, 0.10),
                (5.0, 10.0, 5.0, 3.0, 5.0),
            )
        )
        cls.inputs = ConversionFunnelInput(
            as_of_date=cls.as_of_date,
            candidates=cls.candidates,
            stage_leaves=cls.leaves,
            usage_records=cls.usage_records,
            test_mode=True,
        )
        cls.result = compile_conversion_funnel(cls.inputs)

    @staticmethod
    def _add(
        leaves: list[FunnelStageLeaf],
        leaf_id: str,
        candidate_id: str,
        stage: FunnelStage,
        status: str,
        parent_ids: tuple[str, ...],
        archetype_id: str,
        **kwargs,
    ) -> str:
        leaves.append(
            FunnelStageLeaf(
                leaf_id=leaf_id,
                candidate_id=candidate_id,
                stage=stage.value,
                status=status,
                parent_ids=parent_ids,
                archetype_id=archetype_id,
                **kwargs,
            )
        )
        return leaf_id

    @classmethod
    def _prefix(
        cls,
        leaves: list[FunnelStageLeaf],
        *,
        candidate_id: str,
        archetype_id: str,
    ) -> dict[str, str]:
        prefix = candidate_id.removeprefix("CAND-")
        recipe_id = f"RECIPE-{prefix}"
        primitive_id = f"PRIMITIVE-{prefix}"
        task_id = f"TASK-{prefix}"
        gap_id = f"GAP-{prefix}"
        query_text = f"기업-{prefix} 2026 공식 근거 확인"
        hypothesis = cls._add(
            leaves,
            f"{prefix}-HYPOTHESIS",
            candidate_id,
            FunnelStage.HYPOTHESIS,
            FunnelLeafStatus.GENERATED.value,
            (candidate_id,),
            archetype_id,
        )
        retrieval = cls._add(
            leaves,
            f"{prefix}-RETRIEVAL",
            candidate_id,
            FunnelStage.RETRIEVAL,
            FunnelLeafStatus.RETRIEVED.value,
            (hypothesis,),
            archetype_id,
        )
        recipe = cls._add(
            leaves,
            f"{prefix}-RECIPE",
            candidate_id,
            FunnelStage.RECIPE,
            FunnelLeafStatus.SELECTED.value,
            (retrieval,),
            archetype_id,
            recipe_id=recipe_id,
            primitive_id=primitive_id,
        )
        task = cls._add(
            leaves,
            f"{prefix}-TASK",
            candidate_id,
            FunnelStage.SOURCE_TASK,
            FunnelLeafStatus.PLANNED.value,
            (recipe,),
            archetype_id,
            recipe_id=recipe_id,
            task_id=task_id,
            original_gap_id=gap_id,
            primitive_id=primitive_id,
        )
        query = cls._add(
            leaves,
            f"{prefix}-QUERY",
            candidate_id,
            FunnelStage.QUERY,
            FunnelLeafStatus.EXECUTED.value,
            (task,),
            archetype_id,
            recipe_id=recipe_id,
            task_id=task_id,
            query_text=query_text,
        )
        return {
            "hypothesis": hypothesis,
            "retrieval": retrieval,
            "recipe": recipe,
            "task": task,
            "query": query,
            "recipe_id": recipe_id,
            "primitive_id": primitive_id,
            "task_id": task_id,
            "gap_id": gap_id,
            "query_text": query_text,
        }

    @classmethod
    def _document_path(
        cls,
        leaves: list[FunnelStageLeaf],
        *,
        prefix: str,
        candidate_id: str,
        archetype_id: str,
        parent_id: str,
        recipe_id: str,
        task_id: str,
    ) -> dict[str, str]:
        document_id = f"DOC-{prefix}"
        fetched = cls._add(
            leaves,
            f"{prefix}-FETCHED",
            candidate_id,
            FunnelStage.FETCHED_DOCUMENT,
            FunnelLeafStatus.FETCHED.value,
            (parent_id,),
            archetype_id,
            recipe_id=recipe_id,
            task_id=task_id,
            document_id=document_id,
        )
        relevant = cls._add(
            leaves,
            f"{prefix}-RELEVANT",
            candidate_id,
            FunnelStage.RELEVANT_DOCUMENT,
            FunnelLeafStatus.RELEVANT.value,
            (fetched,),
            archetype_id,
            recipe_id=recipe_id,
            task_id=task_id,
            document_id=document_id,
        )
        return {
            "fetched": fetched,
            "relevant": relevant,
            "document_id": document_id,
        }

    @classmethod
    def _claim_path(
        cls,
        leaves: list[FunnelStageLeaf],
        *,
        prefix: str,
        candidate_id: str,
        archetype_id: str,
        assertion_parent: str,
        document_id: str,
        recipe_id: str,
        task_id: str,
        original_gap_id: str,
        primitive_id: str,
        claim_status: str,
        primitive_status: str,
        assertion_archetype_id: str | None = None,
        assertion_recipe_id: str | None = None,
    ) -> dict[str, str]:
        assertion_id = f"ASSERTION-{prefix}"
        claim_id = f"CLAIM-{prefix}"
        assertion = cls._add(
            leaves,
            f"{prefix}-ASSERTION",
            candidate_id,
            FunnelStage.ASSERTION,
            FunnelLeafStatus.EXTRACTED.value,
            (assertion_parent,),
            assertion_archetype_id or archetype_id,
            recipe_id=assertion_recipe_id or recipe_id,
            task_id=task_id,
            document_id=document_id,
            assertion_id=assertion_id,
        )
        claim = cls._add(
            leaves,
            f"{prefix}-CLAIM",
            candidate_id,
            FunnelStage.CLAIM,
            claim_status,
            (assertion,),
            archetype_id,
            recipe_id=recipe_id,
            task_id=task_id,
            original_gap_id=original_gap_id,
            primitive_id=primitive_id,
            document_id=document_id,
            assertion_id=assertion_id,
            claim_id=claim_id,
        )
        primitive = cls._add(
            leaves,
            f"{prefix}-PRIMITIVE",
            candidate_id,
            FunnelStage.PRIMITIVE,
            primitive_status,
            (claim,),
            archetype_id,
            recipe_id=recipe_id,
            task_id=task_id,
            original_gap_id=original_gap_id,
            primitive_id=primitive_id,
            document_id=document_id,
            assertion_id=assertion_id,
            claim_id=claim_id,
        )
        return {"assertion": assertion, "claim": claim, "primitive": primitive}

    @classmethod
    def _terminal(
        cls,
        leaves: list[FunnelStageLeaf],
        *,
        prefix: str,
        candidate_id: str,
        archetype_id: str,
        parent_id: str,
        outcome: CurrentDeepOutcome,
        reason: str,
    ) -> str:
        return cls._add(
            leaves,
            f"{prefix}-TERMINAL",
            candidate_id,
            FunnelStage.TERMINAL,
            outcome.value,
            (parent_id,),
            archetype_id,
            terminal_reason=reason,
        )

    @staticmethod
    def _usage(
        candidate_id: str,
        archetype_id: str,
        query_leaf_id: str,
        *,
        result_count: int,
        fetch_count: int,
        tokens: int,
        cost: float,
        runtime: float,
    ) -> FunnelUsageRecord:
        return FunnelUsageRecord(
            usage_id=f"USAGE-{candidate_id}",
            candidate_id=candidate_id,
            archetype_id=archetype_id,
            provider_name="fixture-observability-provider",
            operation_leaf_ids=(query_leaf_id,),
            query_count=1,
            result_count=result_count,
            fetch_count=fetch_count,
            input_tokens=tokens * 2 // 3,
            output_tokens=tokens // 3,
            cost_usd=cost,
            runtime_seconds=runtime,
        )

    def _global(self):
        return next(
            item
            for item in self.result.metric_rows
            if item.scope_type == FunnelMetricScope.GLOBAL.value
        )

    def test_every_candidate_has_a_leaf_lineage_and_one_terminal(self) -> None:
        self.assertEqual(len(self.result.candidates), 5)
        terminals = tuple(
            item
            for item in self.result.stage_leaves
            if item.stage == FunnelStage.TERMINAL.value
        )
        self.assertEqual(len(terminals), 5)
        self.assertEqual(
            {item.candidate_id for item in terminals},
            {item.candidate_id for item in self.result.candidates},
        )
        self.assertEqual(self.result.audit["critical_count_sum"], 0)

    def test_relevant_and_accepted_rates_are_recomputed_from_leaves(self) -> None:
        metric = self._global()
        self.assertEqual(metric.fetched_document_count, 5)
        self.assertEqual(metric.relevant_document_count, 4)
        self.assertEqual(metric.relevant_document_rate, 0.8)
        self.assertEqual(metric.assertion_count, 4)
        self.assertEqual(metric.claim_count, 4)
        self.assertEqual(metric.accepted_claim_count, 3)
        self.assertEqual(metric.accepted_claim_rate, 0.75)

    def test_direct_original_gap_closure_is_primary_progress_not_task_shells(self) -> None:
        metric = self._global()
        self.assertEqual(metric.source_task_count, 5)
        self.assertEqual(metric.original_gap_count, 5)
        self.assertEqual(metric.accepted_claim_count, 3)
        self.assertEqual(metric.direct_original_gap_closure_count, 1)
        self.assertEqual(metric.direct_original_gap_closure_rate, 0.2)
        self.assertEqual(metric.meaningful_progress_count, 1)
        self.assertEqual(metric.task_shell_progress_credit_count, 0)
        self.assertEqual(metric.primary_progress_metric, "DIRECT_ORIGINAL_GAP_CLOSURE")
        self.assertEqual(metric.rerouted_claim_count, 1)
        self.assertEqual(metric.mapping_rejection_count, 1)

        provider_task = next(
            item
            for item in self.leaves
            if item.candidate_id == "CAND-PROVIDER"
            and item.stage == FunnelStage.SOURCE_TASK.value
        )
        retry_same_gap = replace(
            provider_task,
            leaf_id="PROVIDER-TASK-RETRY-SAME-GAP",
            task_id="TASK-PROVIDER-RETRY",
        )
        retried = compile_conversion_funnel(
            replace(
                self.inputs,
                stage_leaves=(*self.leaves, retry_same_gap),
            )
        )
        retried_global = next(
            item
            for item in retried.metric_rows
            if item.scope_type == FunnelMetricScope.GLOBAL.value
        )
        self.assertEqual(retried_global.source_task_count, 6)
        self.assertEqual(retried_global.original_gap_count, 5)
        self.assertEqual(retried_global.direct_original_gap_closure_rate, 0.2)

    def test_candidate_and_archetype_metrics_keep_terminal_pending_reasons(self) -> None:
        metric = self._global()
        self.assertEqual(
            metric.terminal_outcome_counts,
            {
                CurrentDeepOutcome.FULL_THESIS.value: 1,
                CurrentDeepOutcome.DISPROVED.value: 1,
                CurrentDeepOutcome.SOURCE_PENDING.value: 2,
                CurrentDeepOutcome.PROVIDER_PENDING.value: 1,
                CurrentDeepOutcome.BUDGET_PENDING.value: 0,
            },
        )
        self.assertEqual(sum(metric.pending_reason_counts.values()), 3)
        scope_types = {item.scope_type for item in self.result.metric_rows}
        self.assertEqual(
            scope_types,
            {item.value for item in FunnelMetricScope},
        )
        alternate = next(
            item
            for item in self.result.metric_rows
            if item.scope_type == FunnelMetricScope.ARCHETYPE.value
            and item.scope_id == "ARCH-ALTERNATE"
        )
        self.assertEqual(alternate.rerouted_claim_count, 1)
        self.assertEqual(alternate.direct_original_gap_closure_count, 0)

    def test_usage_cost_runtime_and_writer_are_leaf_backed(self) -> None:
        metric = self._global()
        self.assertEqual(metric.query_usage_count, 5)
        self.assertEqual(metric.result_usage_count, 5)
        self.assertEqual(metric.fetch_usage_count, 5)
        self.assertEqual(metric.cost_usd, 0.55)
        self.assertEqual(metric.runtime_seconds, 28.0)
        with TemporaryDirectory() as tmp:
            paths = write_conversion_funnel(self.result, output_root=Path(tmp))
            self.assertTrue(all(path.exists() for path in paths.values()))
            report = paths["report"].read_text(encoding="utf-8")
            self.assertIn("DIRECT_ORIGINAL_GAP_CLOSURE", report)
            self.assertIn("SourceTask shell progress credit: 0", report)

    def test_audit_catches_graph_claim_and_assertion_lineage_mutations(self) -> None:
        duplicate = self.result.to_dict()
        duplicate["stage_leaves"].append(deepcopy(duplicate["stage_leaves"][0]))
        audit = audit_conversion_funnel(duplicate)
        self.assertEqual(audit["critical_counts"]["duplicate_leaf_id"], 1)

        wrong_parent = self.result.to_dict()
        recipe = next(
            item
            for item in wrong_parent["stage_leaves"]
            if item["stage"] == FunnelStage.RECIPE.value
        )
        recipe["parent_ids"] = [recipe["candidate_id"]]
        audit = audit_conversion_funnel(wrong_parent)
        self.assertEqual(audit["critical_counts"]["stage_parent_mismatch"], 1)

        missing_claim = self.result.to_dict()
        missing_claim["stage_leaves"] = [
            item
            for item in missing_claim["stage_leaves"]
            if item["leaf_id"] != "MAPPING-CLAIM"
        ]
        audit = audit_conversion_funnel(missing_claim)
        self.assertEqual(
            audit["critical_counts"]["assertion_without_one_claim_terminal"],
            1,
        )

    def test_audit_catches_reroute_and_progress_credit_forgery(self) -> None:
        reroute_as_direct = self.result.to_dict()
        rerouted_claim = next(
            item
            for item in reroute_as_direct["stage_leaves"]
            if item["leaf_id"] == "REROUTED-CLAIM"
        )
        rerouted_claim["status"] = FunnelLeafStatus.ACCEPTED_DIRECT.value
        audit = audit_conversion_funnel(reroute_as_direct)
        self.assertEqual(
            audit["critical_counts"]["direct_closure_route_mismatch"],
            1,
        )

        fake_progress = self.result.to_dict()
        global_metric = next(
            item
            for item in fake_progress["metric_rows"]
            if item["scope_type"] == FunnelMetricScope.GLOBAL.value
        )
        global_metric["meaningful_progress_count"] = 5
        global_metric["task_shell_progress_credit_count"] = 5
        audit = audit_conversion_funnel(fake_progress)
        self.assertEqual(
            audit["critical_counts"]["global_metric_projection_mismatch"],
            1,
        )
        self.assertEqual(
            audit["critical_counts"]["non_direct_original_gap_progress_credit"],
            1,
        )
        self.assertEqual(
            audit["critical_counts"]["source_task_shell_as_progress"],
            1,
        )

    def test_audit_catches_terminal_score_and_provider_pending_forgery(self) -> None:
        forged_full = self.result.to_dict()
        full_score = next(
            item
            for item in forged_full["stage_leaves"]
            if item["leaf_id"] == "FULL-SCORE"
        )
        full_score["status"] = AtomicScoreType.NO_SCORE.value
        full_score["score_value"] = None
        full_score["score_finalization_allowed"] = False
        audit = audit_conversion_funnel(forged_full)
        self.assertEqual(
            audit["critical_counts"]["full_thesis_without_final_full_score"],
            1,
        )

        hidden_provider_error = self.result.to_dict()
        provider_result = next(
            item
            for item in hidden_provider_error["stage_leaves"]
            if item["leaf_id"] == "PROVIDER-RESULT"
        )
        provider_result["status"] = FunnelLeafStatus.NO_RESULT.value
        provider_result["provider_error"] = None
        audit = audit_conversion_funnel(hidden_provider_error)
        self.assertEqual(
            audit["critical_counts"]["provider_pending_without_provider_error"],
            1,
        )

        rerouted_as_full = self.result.to_dict()
        rerouted_score = next(
            item
            for item in rerouted_as_full["stage_leaves"]
            if item["leaf_id"] == "REROUTED-SCORE"
        )
        rerouted_score["status"] = AtomicScoreType.FULL_E2R_100.value
        rerouted_score["score_value"] = 100.0
        rerouted_score["raw_reference_score"] = 100.0
        rerouted_score["score_finalization_allowed"] = True
        rerouted_terminal = next(
            item
            for item in rerouted_as_full["stage_leaves"]
            if item["leaf_id"] == "REROUTED-TERMINAL"
        )
        rerouted_terminal["status"] = CurrentDeepOutcome.FULL_THESIS.value
        rerouted_terminal["terminal_reason"] = "forged rerouted full thesis"
        audit = audit_conversion_funnel(rerouted_as_full)
        self.assertEqual(
            audit["critical_counts"]["full_thesis_with_open_original_gap"],
            1,
        )

    def test_usage_and_result_integrity_cannot_be_forged(self) -> None:
        changed_usage = self.result.to_dict()
        changed_usage["usage_records"][0]["cost_usd"] = 99.0
        audit = audit_conversion_funnel(changed_usage)
        self.assertGreater(
            audit["critical_counts"]["global_metric_projection_mismatch"],
            0,
        )
        self.assertEqual(
            audit["critical_counts"]["manifest_leaf_hash_mismatch"],
            1,
        )
        wrong_usage_count = self.result.to_dict()
        wrong_usage_count["usage_records"][0]["query_count"] = 2
        audit = audit_conversion_funnel(wrong_usage_count)
        self.assertEqual(
            audit["critical_counts"]["usage_count_leaf_mismatch"],
            1,
        )
        with self.assertRaisesRegex(ValueError, "integrity mismatch"):
            replace(self.result, audit={"critical_count_sum": 0})

    def test_canonical_source_task_acquisition_claim_and_atomic_ids_are_preserved(
        self,
    ) -> None:
        phase9_fixture.ContractBlindClaimCompilerTest.setUpClass()
        fixture = phase9_fixture.ContractBlindClaimCompilerTest(
            "test_contract_blind_input_and_direct_task_satisfaction"
        )
        task = phase9_fixture.ContractBlindClaimCompilerTest.task
        acquisition = fixture._acquisition(candidate_id="PHASE14-CANONICAL")
        compilation = fixture._compile(acquisition=acquisition)
        document = acquisition.documents[0]
        event = next(item for item in compilation.ledger_events if item.score_eligible)
        atomic_claim = adapt_claim_ledger_event_to_atomic_claim(
            event,
            source_content_hash=document.content_hash,
            material=True,
            test_mode=True,
        )
        rule = AtomicScoreRule(
            primitive_id=atomic_claim.primitive_id,
            component_key="phase14_direct_closure",
            max_points=100.0,
            material=True,
            green_required=True,
        )
        assessment = AtomicPrimitiveAssessment(
            primitive_id=atomic_claim.primitive_id,
            status=AtomicPrimitiveStatus.SATISFIED.value,
            evidence_strength=1.0,
            support_claim_ids=(atomic_claim.claim_id,),
        )
        decision = decide_atomic_score_stage(
            AtomicScoringInput(
                target_id=atomic_claim.target_id,
                as_of_date=task.as_of_date,
                scope=AtomicScoringScope.FULL_THESIS.value,
                claims=(atomic_claim,),
                primitive_assessments=(assessment,),
                rules=(rule,),
            )
        )

        candidate_id = "CAND-CANONICAL-PHASE14"
        hypothesis = FunnelStageLeaf(
            leaf_id="CANONICAL-HYPOTHESIS",
            candidate_id=candidate_id,
            stage=FunnelStage.HYPOTHESIS.value,
            status=FunnelLeafStatus.GENERATED.value,
            parent_ids=(candidate_id,),
            archetype_id=task.archetype_id,
        )
        retrieval = FunnelStageLeaf(
            leaf_id="CANONICAL-RETRIEVAL",
            candidate_id=candidate_id,
            stage=FunnelStage.RETRIEVAL.value,
            status=FunnelLeafStatus.RETRIEVED.value,
            parent_ids=(hypothesis.leaf_id,),
            archetype_id=task.archetype_id,
        )
        recipe = FunnelStageLeaf(
            leaf_id="CANONICAL-RECIPE",
            candidate_id=candidate_id,
            stage=FunnelStage.RECIPE.value,
            status=FunnelLeafStatus.SELECTED.value,
            parent_ids=(retrieval.leaf_id,),
            archetype_id=task.archetype_id,
            recipe_id=task.recipe_id,
            primitive_id=task.primitive_id,
        )
        task_leaf, query_leaves = record_question_source_task_leaves(
            candidate_id=candidate_id,
            recipe_parent_leaf_id=recipe.leaf_id,
            task=task,
        )
        query = query_leaves[0]
        result_leaf = FunnelStageLeaf(
            leaf_id=acquisition.acquisition_id,
            candidate_id=candidate_id,
            stage=FunnelStage.RESULT.value,
            status=FunnelLeafStatus.RETURNED.value,
            parent_ids=(query.leaf_id,),
            archetype_id=task.archetype_id,
            recipe_id=task.recipe_id,
            task_id=task.task_id,
            query_text=query.query_text,
        )
        fetched = FunnelStageLeaf(
            leaf_id=f"FETCHED-{document.document_id}",
            candidate_id=candidate_id,
            stage=FunnelStage.FETCHED_DOCUMENT.value,
            status=FunnelLeafStatus.FETCHED.value,
            parent_ids=(result_leaf.leaf_id,),
            archetype_id=task.archetype_id,
            recipe_id=task.recipe_id,
            task_id=task.task_id,
            document_id=document.document_id,
        )
        relevant = FunnelStageLeaf(
            leaf_id=f"RELEVANT-{document.document_id}",
            candidate_id=candidate_id,
            stage=FunnelStage.RELEVANT_DOCUMENT.value,
            status=FunnelLeafStatus.RELEVANT.value,
            parent_ids=(fetched.leaf_id,),
            archetype_id=task.archetype_id,
            recipe_id=task.recipe_id,
            task_id=task.task_id,
            document_id=document.document_id,
        )
        assertion = FunnelStageLeaf(
            leaf_id=f"ASSERTION-{event.raw_assertion_id}",
            candidate_id=candidate_id,
            stage=FunnelStage.ASSERTION.value,
            status=FunnelLeafStatus.EXTRACTED.value,
            parent_ids=(relevant.leaf_id,),
            archetype_id=task.archetype_id,
            recipe_id=task.recipe_id,
            task_id=task.task_id,
            document_id=document.document_id,
            assertion_id=event.raw_assertion_id,
        )
        gap_id = original_gap_id_for_question_source_task(task)
        claim = FunnelStageLeaf(
            leaf_id=f"CLAIM-{event.claim_id}",
            candidate_id=candidate_id,
            stage=FunnelStage.CLAIM.value,
            status=FunnelLeafStatus.ACCEPTED_DIRECT.value,
            parent_ids=(assertion.leaf_id,),
            archetype_id=str(event.mapped_archetype_id),
            recipe_id=str(event.mapped_recipe_id),
            task_id=task.task_id,
            original_gap_id=gap_id,
            primitive_id=str(event.mapped_primitive_id),
            document_id=document.document_id,
            assertion_id=event.raw_assertion_id,
            claim_id=event.claim_id,
        )
        primitive = FunnelStageLeaf(
            leaf_id=f"PRIMITIVE-{event.claim_id}",
            candidate_id=candidate_id,
            stage=FunnelStage.PRIMITIVE.value,
            status=FunnelLeafStatus.SATISFIED.value,
            parent_ids=(claim.leaf_id,),
            archetype_id=str(event.mapped_archetype_id),
            recipe_id=str(event.mapped_recipe_id),
            task_id=task.task_id,
            original_gap_id=gap_id,
            primitive_id=str(event.mapped_primitive_id),
            document_id=document.document_id,
            assertion_id=event.raw_assertion_id,
            claim_id=event.claim_id,
        )
        score = FunnelStageLeaf(
            leaf_id=f"SCORE-{decision.decision_id}",
            candidate_id=candidate_id,
            stage=FunnelStage.SCORE.value,
            status=decision.score_type,
            parent_ids=(primitive.leaf_id,),
            archetype_id=task.archetype_id,
            score_decision_id=decision.decision_id,
            score_value=decision.score_value,
            raw_reference_score=decision.raw_reference_score,
            score_finalization_allowed=decision.score_finalization_allowed,
        )
        terminal = FunnelStageLeaf(
            leaf_id="CANONICAL-TERMINAL",
            candidate_id=candidate_id,
            stage=FunnelStage.TERMINAL.value,
            status=CurrentDeepOutcome.FULL_THESIS.value,
            parent_ids=(score.leaf_id,),
            archetype_id=task.archetype_id,
            terminal_reason="canonical source-backed direct closure",
        )
        leaves = (
            hypothesis,
            retrieval,
            recipe,
            task_leaf,
            *query_leaves,
            result_leaf,
            fetched,
            relevant,
            assertion,
            claim,
            primitive,
            score,
            terminal,
        )
        observed = compile_conversion_funnel(
            ConversionFunnelInput(
                as_of_date=task.as_of_date,
                candidates=(
                    FunnelCandidate(
                        candidate_id=candidate_id,
                        target_id=task.target_id,
                        target_name=task.company_name,
                        as_of_date=task.as_of_date,
                        archetype_ids=(task.archetype_id,),
                        primary_archetype_id=task.archetype_id,
                        selected_for_deep=True,
                        selection_reason="canonical Phase 7-12 integration fixture",
                    ),
                ),
                stage_leaves=leaves,
                usage_records=(
                    FunnelUsageRecord(
                        usage_id="CANONICAL-USAGE",
                        candidate_id=candidate_id,
                        archetype_id=task.archetype_id,
                        provider_name="fixture-canonical-integration",
                        operation_leaf_ids=(query.leaf_id, result_leaf.leaf_id),
                        query_count=1,
                        result_count=1,
                        fetch_count=1,
                        runtime_seconds=1.0,
                    ),
                ),
                test_mode=True,
            )
        )
        global_metric = next(
            item
            for item in observed.metric_rows
            if item.scope_type == FunnelMetricScope.GLOBAL.value
        )
        self.assertEqual(task_leaf.task_id, task.task_id)
        self.assertEqual(query.query_text, task.query_intent.literal_queries[0])
        self.assertEqual(fetched.document_id, document.document_id)
        self.assertEqual(assertion.assertion_id, event.raw_assertion_id)
        self.assertEqual(claim.claim_id, event.claim_id)
        self.assertEqual(score.score_decision_id, decision.decision_id)
        self.assertEqual(global_metric.direct_original_gap_closure_count, 1)
        self.assertEqual(observed.audit["critical_count_sum"], 0)


if __name__ == "__main__":
    unittest.main()
