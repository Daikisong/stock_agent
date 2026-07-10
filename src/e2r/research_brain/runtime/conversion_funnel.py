"""Leaf-backed conversion funnel observability for the canonical Research Brain."""

from __future__ import annotations

import math
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import date
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text
from e2r.research_brain.planning.source_task import QuestionSourceTask
from e2r.research_brain.runtime.atomic_score_stage import AtomicScoreType
from e2r.research_brain.runtime.current_operation import CurrentDeepOutcome


CONVERSION_FUNNEL_SCHEMA_VERSION = "e2r_conversion_funnel_v1"
CONVERSION_FUNNEL_AUDIT_SCHEMA_VERSION = "e2r_conversion_funnel_audit_v1"


class FunnelStage(str, Enum):
    HYPOTHESIS = "HYPOTHESIS"
    RETRIEVAL = "RETRIEVAL"
    RECIPE = "RECIPE"
    SOURCE_TASK = "SOURCE_TASK"
    QUERY = "QUERY"
    RESULT = "RESULT"
    FETCHED_DOCUMENT = "FETCHED_DOCUMENT"
    RELEVANT_DOCUMENT = "RELEVANT_DOCUMENT"
    ASSERTION = "ASSERTION"
    CLAIM = "CLAIM"
    PRIMITIVE = "PRIMITIVE"
    SCORE = "SCORE"
    TERMINAL = "TERMINAL"


class FunnelLeafStatus(str, Enum):
    GENERATED = "GENERATED"
    RETRIEVED = "RETRIEVED"
    NO_RETRIEVAL_HIT = "NO_RETRIEVAL_HIT"
    SELECTED = "SELECTED"
    PLANNED = "PLANNED"
    EXECUTED = "EXECUTED"
    REJECTED = "REJECTED"
    RETURNED = "RETURNED"
    NO_RESULT = "NO_RESULT"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    FETCHED = "FETCHED"
    RELEVANT = "RELEVANT"
    EXTRACTED = "EXTRACTED"
    ACCEPTED_DIRECT = "ACCEPTED_DIRECT"
    ACCEPTED_REROUTED = "ACCEPTED_REROUTED"
    COUNTER_DIRECT = "COUNTER_DIRECT"
    MAPPING_REJECTED = "MAPPING_REJECTED"
    CLAIM_REJECTED = "CLAIM_REJECTED"
    SATISFIED = "SATISFIED"
    REROUTED = "REROUTED"
    COUNTER = "COUNTER"
    MISSING = "MISSING"


class FunnelMetricScope(str, Enum):
    GLOBAL = "GLOBAL"
    CANDIDATE = "CANDIDATE"
    ARCHETYPE = "ARCHETYPE"


_CLAIM_ACCEPTED_STATUSES = frozenset(
    {
        FunnelLeafStatus.ACCEPTED_DIRECT.value,
        FunnelLeafStatus.ACCEPTED_REROUTED.value,
        FunnelLeafStatus.COUNTER_DIRECT.value,
    }
)
_PENDING_OUTCOMES = frozenset(
    {
        CurrentDeepOutcome.SOURCE_PENDING.value,
        CurrentDeepOutcome.PROVIDER_PENDING.value,
        CurrentDeepOutcome.BUDGET_PENDING.value,
    }
)
_ALLOWED_STATUS_BY_STAGE = {
    FunnelStage.HYPOTHESIS.value: {FunnelLeafStatus.GENERATED.value},
    FunnelStage.RETRIEVAL.value: {
        FunnelLeafStatus.RETRIEVED.value,
        FunnelLeafStatus.NO_RETRIEVAL_HIT.value,
    },
    FunnelStage.RECIPE.value: {FunnelLeafStatus.SELECTED.value},
    FunnelStage.SOURCE_TASK.value: {FunnelLeafStatus.PLANNED.value},
    FunnelStage.QUERY.value: {
        FunnelLeafStatus.EXECUTED.value,
        FunnelLeafStatus.REJECTED.value,
    },
    FunnelStage.RESULT.value: {
        FunnelLeafStatus.RETURNED.value,
        FunnelLeafStatus.NO_RESULT.value,
        FunnelLeafStatus.PROVIDER_FAILED.value,
    },
    FunnelStage.FETCHED_DOCUMENT.value: {FunnelLeafStatus.FETCHED.value},
    FunnelStage.RELEVANT_DOCUMENT.value: {FunnelLeafStatus.RELEVANT.value},
    FunnelStage.ASSERTION.value: {FunnelLeafStatus.EXTRACTED.value},
    FunnelStage.CLAIM.value: {
        FunnelLeafStatus.ACCEPTED_DIRECT.value,
        FunnelLeafStatus.ACCEPTED_REROUTED.value,
        FunnelLeafStatus.COUNTER_DIRECT.value,
        FunnelLeafStatus.MAPPING_REJECTED.value,
        FunnelLeafStatus.CLAIM_REJECTED.value,
    },
    FunnelStage.PRIMITIVE.value: {
        FunnelLeafStatus.SATISFIED.value,
        FunnelLeafStatus.REROUTED.value,
        FunnelLeafStatus.COUNTER.value,
        FunnelLeafStatus.MISSING.value,
    },
    FunnelStage.SCORE.value: {item.value for item in AtomicScoreType},
    FunnelStage.TERMINAL.value: {item.value for item in CurrentDeepOutcome},
}
_EXPECTED_PARENT_STAGE = {
    FunnelStage.HYPOTHESIS.value: "CANDIDATE",
    FunnelStage.RETRIEVAL.value: FunnelStage.HYPOTHESIS.value,
    FunnelStage.RECIPE.value: FunnelStage.RETRIEVAL.value,
    FunnelStage.SOURCE_TASK.value: FunnelStage.RECIPE.value,
    FunnelStage.QUERY.value: FunnelStage.SOURCE_TASK.value,
    FunnelStage.RESULT.value: FunnelStage.QUERY.value,
    FunnelStage.FETCHED_DOCUMENT.value: FunnelStage.RESULT.value,
    FunnelStage.RELEVANT_DOCUMENT.value: FunnelStage.FETCHED_DOCUMENT.value,
    FunnelStage.ASSERTION.value: FunnelStage.RELEVANT_DOCUMENT.value,
    FunnelStage.CLAIM.value: FunnelStage.ASSERTION.value,
    FunnelStage.PRIMITIVE.value: FunnelStage.CLAIM.value,
    FunnelStage.SCORE.value: FunnelStage.PRIMITIVE.value,
}


@dataclass(frozen=True)
class FunnelCandidate:
    candidate_id: str
    target_id: str
    target_name: str
    as_of_date: str
    archetype_ids: tuple[str, ...]
    primary_archetype_id: str
    selected_for_deep: bool
    selection_reason: str

    def __post_init__(self) -> None:
        if not all(
            isinstance(item, str) and item.strip()
            for item in (
                self.candidate_id,
                self.target_id,
                self.target_name,
                self.as_of_date,
                self.primary_archetype_id,
                self.selection_reason,
            )
        ):
            raise ValueError("funnel candidate identity is required")
        date.fromisoformat(self.as_of_date)
        _require_unique_text(self.archetype_ids, context="candidate archetypes")
        if self.primary_archetype_id not in self.archetype_ids:
            raise ValueError("primary archetype must be one of candidate archetypes")
        if not isinstance(self.selected_for_deep, bool):
            raise ValueError("candidate selected_for_deep must be boolean")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class FunnelStageLeaf:
    leaf_id: str
    candidate_id: str
    stage: str
    status: str
    parent_ids: tuple[str, ...]
    archetype_id: str
    recipe_id: str | None = None
    task_id: str | None = None
    original_gap_id: str | None = None
    primitive_id: str | None = None
    query_text: str | None = None
    document_id: str | None = None
    assertion_id: str | None = None
    claim_id: str | None = None
    score_decision_id: str | None = None
    score_value: float | None = None
    raw_reference_score: float | None = None
    score_finalization_allowed: bool = False
    hard_break: bool = False
    terminal_reason: str | None = None
    provider_error: str | None = None
    schema_version: str = CONVERSION_FUNNEL_SCHEMA_VERSION

    def __post_init__(self) -> None:
        selected_stage = FunnelStage(self.stage)
        if self.status not in _ALLOWED_STATUS_BY_STAGE[selected_stage.value]:
            raise ValueError("funnel leaf status is invalid for its stage")
        if not all(
            isinstance(item, str) and item.strip()
            for item in (self.leaf_id, self.candidate_id, self.archetype_id)
        ):
            raise ValueError("funnel leaf identity is required")
        _require_unique_text(self.parent_ids, context="funnel parent ids")
        if not self.parent_ids:
            raise ValueError("every funnel stage leaf requires parent lineage")
        for name in ("score_finalization_allowed", "hard_break"):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"funnel {name} must be boolean")
        self._validate_stage_fields(selected_stage)

    def _validate_stage_fields(self, stage: FunnelStage) -> None:
        if stage in {
            FunnelStage.RECIPE,
            FunnelStage.SOURCE_TASK,
            FunnelStage.QUERY,
            FunnelStage.RESULT,
            FunnelStage.FETCHED_DOCUMENT,
            FunnelStage.RELEVANT_DOCUMENT,
            FunnelStage.ASSERTION,
            FunnelStage.CLAIM,
            FunnelStage.PRIMITIVE,
        } and not str(self.recipe_id or "").strip():
            raise ValueError("recipe-routed funnel leaf requires recipe_id")
        if stage in {
            FunnelStage.SOURCE_TASK,
            FunnelStage.QUERY,
            FunnelStage.RESULT,
            FunnelStage.FETCHED_DOCUMENT,
            FunnelStage.RELEVANT_DOCUMENT,
            FunnelStage.ASSERTION,
            FunnelStage.CLAIM,
            FunnelStage.PRIMITIVE,
        } and not str(self.task_id or "").strip():
            raise ValueError("task-routed funnel leaf requires task_id")
        if stage in {
            FunnelStage.SOURCE_TASK,
            FunnelStage.CLAIM,
            FunnelStage.PRIMITIVE,
        } and not str(self.original_gap_id or "").strip():
            raise ValueError("gap-routed funnel leaf requires original_gap_id")
        if stage in {
            FunnelStage.RECIPE,
            FunnelStage.SOURCE_TASK,
            FunnelStage.CLAIM,
            FunnelStage.PRIMITIVE,
        } and not str(self.primitive_id or "").strip():
            raise ValueError("primitive-routed funnel leaf requires primitive_id")
        if stage in {FunnelStage.QUERY, FunnelStage.RESULT} and not str(
            self.query_text or ""
        ).strip():
            raise ValueError("query/result funnel leaf requires literal query lineage")
        if stage in {
            FunnelStage.FETCHED_DOCUMENT,
            FunnelStage.RELEVANT_DOCUMENT,
            FunnelStage.ASSERTION,
            FunnelStage.CLAIM,
            FunnelStage.PRIMITIVE,
        } and not str(self.document_id or "").strip():
            raise ValueError("document-routed funnel leaf requires document_id")
        if stage in {
            FunnelStage.ASSERTION,
            FunnelStage.CLAIM,
            FunnelStage.PRIMITIVE,
        } and not str(self.assertion_id or "").strip():
            raise ValueError("assertion-routed funnel leaf requires assertion_id")
        if stage in {FunnelStage.CLAIM, FunnelStage.PRIMITIVE} and not str(
            self.claim_id or ""
        ).strip():
            raise ValueError("claim-routed funnel leaf requires claim_id")
        if stage == FunnelStage.RESULT:
            if self.status == FunnelLeafStatus.PROVIDER_FAILED.value:
                if not str(self.provider_error or "").strip():
                    raise ValueError("provider-failed result requires exact error")
            elif self.provider_error is not None:
                raise ValueError("non-failed result cannot carry provider error")
        elif self.provider_error is not None:
            raise ValueError("provider_error belongs only to RESULT leaf")
        if stage == FunnelStage.SCORE:
            self._validate_score_fields()
        elif any(
            (
                self.score_decision_id is not None,
                self.score_value is not None,
                self.raw_reference_score is not None,
                self.score_finalization_allowed,
                self.hard_break,
            )
        ):
            raise ValueError("score fields belong only to SCORE leaf")
        if stage == FunnelStage.TERMINAL:
            if not str(self.terminal_reason or "").strip():
                raise ValueError("terminal funnel leaf requires exact reason")
        elif self.terminal_reason is not None:
            raise ValueError("terminal_reason belongs only to TERMINAL leaf")

    def _validate_score_fields(self) -> None:
        if not str(self.score_decision_id or "").strip():
            raise ValueError("score funnel leaf requires atomic decision id")
        for name in ("score_value", "raw_reference_score"):
            value = getattr(self, name)
            if value is not None and (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(float(value))
                or not 0.0 <= float(value) <= 100.0
            ):
                raise ValueError(f"funnel {name} must be finite within 0..100")
        score_type = AtomicScoreType(self.status)
        if score_type == AtomicScoreType.FULL_E2R_100:
            if self.score_value is None or not self.score_finalization_allowed:
                raise ValueError("full score leaf requires value and finalization")
            if self.hard_break:
                raise ValueError("final full score cannot carry hard break")
        elif score_type == AtomicScoreType.EVENT_EVIDENCE_PARTIAL:
            if self.score_value is None or self.score_finalization_allowed:
                raise ValueError("event partial score cannot finalize")
            if self.hard_break:
                raise ValueError("event partial score cannot carry hard break")
        elif self.score_value is not None or self.score_finalization_allowed:
            raise ValueError("NO_SCORE leaf cannot expose finalized score")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class FunnelUsageRecord:
    usage_id: str
    candidate_id: str
    archetype_id: str
    provider_name: str
    operation_leaf_ids: tuple[str, ...]
    query_count: int = 0
    result_count: int = 0
    fetch_count: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0
    runtime_seconds: float = 0.0
    schema_version: str = CONVERSION_FUNNEL_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if not all(
            isinstance(item, str) and item.strip()
            for item in (
                self.usage_id,
                self.candidate_id,
                self.archetype_id,
                self.provider_name,
            )
        ):
            raise ValueError("funnel usage identity is required")
        _require_unique_text(
            self.operation_leaf_ids,
            context="funnel usage leaf lineage",
        )
        if not self.operation_leaf_ids:
            raise ValueError("funnel usage requires operation leaf lineage")
        for name in (
            "query_count",
            "result_count",
            "fetch_count",
            "input_tokens",
            "output_tokens",
        ):
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError(f"funnel usage {name} must be nonnegative integer")
        for name in ("cost_usd", "runtime_seconds"):
            value = getattr(self, name)
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(float(value))
                or float(value) < 0.0
            ):
                raise ValueError(f"funnel usage {name} must be finite nonnegative")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class FunnelMetricRow:
    scope_type: str
    scope_id: str
    candidate_count: int
    stage_counts: Mapping[str, int]
    source_task_count: int
    original_gap_count: int
    fetched_document_count: int
    relevant_document_count: int
    relevant_document_rate: float | None
    assertion_count: int
    claim_count: int
    accepted_claim_count: int
    accepted_claim_rate: float | None
    direct_original_gap_closure_count: int
    direct_original_gap_closure_rate: float | None
    meaningful_progress_count: int
    task_shell_progress_credit_count: int
    rerouted_claim_count: int
    mapping_rejection_count: int
    terminal_outcome_counts: Mapping[str, int]
    pending_reason_counts: Mapping[str, int]
    query_usage_count: int
    result_usage_count: int
    fetch_usage_count: int
    input_tokens: int
    output_tokens: int
    cost_usd: float
    runtime_seconds: float
    primary_progress_metric: str = "DIRECT_ORIGINAL_GAP_CLOSURE"
    schema_version: str = CONVERSION_FUNNEL_SCHEMA_VERSION

    def __post_init__(self) -> None:
        FunnelMetricScope(self.scope_type)
        if not self.scope_id.strip():
            raise ValueError("funnel metric scope id is required")
        expected_stages = {item.value for item in FunnelStage}
        if set(self.stage_counts) != expected_stages:
            raise ValueError("funnel metric stage counts are incomplete")
        expected_outcomes = {item.value for item in CurrentDeepOutcome}
        if set(self.terminal_outcome_counts) != expected_outcomes:
            raise ValueError("funnel terminal outcome counts are incomplete")
        integer_values = (
            self.candidate_count,
            *self.stage_counts.values(),
            self.source_task_count,
            self.original_gap_count,
            self.fetched_document_count,
            self.relevant_document_count,
            self.assertion_count,
            self.claim_count,
            self.accepted_claim_count,
            self.direct_original_gap_closure_count,
            self.meaningful_progress_count,
            self.task_shell_progress_credit_count,
            self.rerouted_claim_count,
            self.mapping_rejection_count,
            *self.terminal_outcome_counts.values(),
            *self.pending_reason_counts.values(),
            self.query_usage_count,
            self.result_usage_count,
            self.fetch_usage_count,
            self.input_tokens,
            self.output_tokens,
        )
        if any(
            isinstance(value, bool) or not isinstance(value, int) or value < 0
            for value in integer_values
        ):
            raise ValueError("funnel metric counts must be nonnegative integers")
        for value in (
            self.relevant_document_rate,
            self.accepted_claim_rate,
            self.direct_original_gap_closure_rate,
        ):
            if value is not None and (
                not isinstance(value, (int, float))
                or isinstance(value, bool)
                or not math.isfinite(float(value))
                or not 0.0 <= float(value) <= 1.0
            ):
                raise ValueError("funnel rates must be null or within 0..1")
        if self.meaningful_progress_count != self.direct_original_gap_closure_count:
            raise ValueError("meaningful progress must equal direct gap closure")
        if self.task_shell_progress_credit_count:
            raise ValueError("SourceTask shells cannot receive progress credit")
        if self.primary_progress_metric != "DIRECT_ORIGINAL_GAP_CLOSURE":
            raise ValueError("direct original-gap closure must be primary progress")
        for name in ("cost_usd", "runtime_seconds"):
            value = getattr(self, name)
            if (
                not isinstance(value, (int, float))
                or isinstance(value, bool)
                or not math.isfinite(float(value))
                or value < 0.0
            ):
                raise ValueError(f"funnel metric {name} must be finite nonnegative")

    def to_dict(self) -> dict[str, Any]:
        return {
            **asdict(self),
            "stage_counts": dict(self.stage_counts),
            "terminal_outcome_counts": dict(self.terminal_outcome_counts),
            "pending_reason_counts": dict(self.pending_reason_counts),
        }


@dataclass(frozen=True)
class ConversionFunnelInput:
    as_of_date: str
    candidates: tuple[FunnelCandidate, ...]
    stage_leaves: tuple[FunnelStageLeaf, ...]
    usage_records: tuple[FunnelUsageRecord, ...]
    test_mode: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if not self.candidates:
            raise ValueError("conversion funnel requires candidates")
        if any(item.as_of_date != self.as_of_date for item in self.candidates):
            raise ValueError("conversion funnel candidate as-of mismatch")
        if not isinstance(self.test_mode, bool):
            raise ValueError("conversion funnel test_mode must be boolean")

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": CONVERSION_FUNNEL_SCHEMA_VERSION,
            "as_of_date": self.as_of_date,
            "candidates": [item.to_dict() for item in self.candidates],
            "stage_leaves": [item.to_dict() for item in self.stage_leaves],
            "usage_records": [item.to_dict() for item in self.usage_records],
            "test_mode": self.test_mode,
        }


@dataclass(frozen=True)
class ConversionFunnelResult:
    run_id: str
    as_of_date: str
    candidates: tuple[FunnelCandidate, ...]
    stage_leaves: tuple[FunnelStageLeaf, ...]
    usage_records: tuple[FunnelUsageRecord, ...]
    metric_rows: tuple[FunnelMetricRow, ...]
    test_mode: bool
    audit: Mapping[str, Any]
    manifest: Mapping[str, Any]
    production_runtime_ready: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        projection = _result_projection_payload(self)
        expected_audit = audit_conversion_funnel(projection)
        leaf_hash = stable_hash(_mapping_leaf_payload(projection))
        expected_run_id = _run_id(self.as_of_date, leaf_hash)
        if (
            not self.run_id.strip()
            or self.run_id != expected_run_id
            or dict(self.audit) != dict(expected_audit)
            or expected_audit.get("critical_count_sum") != 0
            or self.manifest.get("run_id") != self.run_id
            or self.manifest.get("leaf_hash") != leaf_hash
            or self.manifest.get("metric_hash")
            != stable_hash([item.to_dict() for item in self.metric_rows])
            or self.manifest.get("critical_counts")
            != expected_audit.get("critical_counts")
            or self.production_runtime_ready
        ):
            raise ValueError("conversion funnel result integrity mismatch")

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": CONVERSION_FUNNEL_SCHEMA_VERSION,
            "run_id": self.run_id,
            "as_of_date": self.as_of_date,
            "candidates": [item.to_dict() for item in self.candidates],
            "stage_leaves": [item.to_dict() for item in self.stage_leaves],
            "usage_records": [item.to_dict() for item in self.usage_records],
            "metric_rows": [item.to_dict() for item in self.metric_rows],
            "test_mode": self.test_mode,
            "audit": dict(self.audit),
            "manifest": dict(self.manifest),
            "production_runtime_ready": False,
        }


def compile_conversion_funnel(
    inputs: ConversionFunnelInput,
) -> ConversionFunnelResult:
    candidate_rows = [item.to_dict() for item in inputs.candidates]
    leaf_rows = [item.to_dict() for item in inputs.stage_leaves]
    usage_rows = [item.to_dict() for item in inputs.usage_records]
    metric_rows = _recompute_metric_rows(candidate_rows, leaf_rows, usage_rows)
    leaf_payload = {
        "candidates": candidate_rows,
        "stage_leaves": leaf_rows,
        "usage_records": usage_rows,
        "test_mode": inputs.test_mode,
    }
    leaf_hash = stable_hash(leaf_payload)
    run_id = _run_id(inputs.as_of_date, leaf_hash)
    metric_hash = stable_hash([item.to_dict() for item in metric_rows])
    global_metrics = next(
        item for item in metric_rows if item.scope_type == FunnelMetricScope.GLOBAL.value
    )
    manifest = {
        "schema_version": CONVERSION_FUNNEL_SCHEMA_VERSION,
        "status": "CONVERSION_FUNNEL_OBSERVABILITY_PASS",
        "run_id": run_id,
        "as_of_date": inputs.as_of_date,
        "candidate_count": len(inputs.candidates),
        "stage_leaf_count": len(inputs.stage_leaves),
        "usage_record_count": len(inputs.usage_records),
        "metric_row_count": len(metric_rows),
        "source_task_count": global_metrics.source_task_count,
        "original_gap_count": global_metrics.original_gap_count,
        "relevant_document_rate": global_metrics.relevant_document_rate,
        "accepted_claim_rate": global_metrics.accepted_claim_rate,
        "direct_original_gap_closure_count": (
            global_metrics.direct_original_gap_closure_count
        ),
        "direct_original_gap_closure_rate": (
            global_metrics.direct_original_gap_closure_rate
        ),
        "meaningful_progress_count": global_metrics.meaningful_progress_count,
        "task_shell_progress_credit_count": 0,
        "rerouted_claim_count": global_metrics.rerouted_claim_count,
        "mapping_rejection_count": global_metrics.mapping_rejection_count,
        "terminal_outcome_counts": dict(global_metrics.terminal_outcome_counts),
        "pending_reason_counts": dict(global_metrics.pending_reason_counts),
        "cost_usd": global_metrics.cost_usd,
        "runtime_seconds": global_metrics.runtime_seconds,
        "leaf_hash": leaf_hash,
        "metric_hash": metric_hash,
        "test_mode": inputs.test_mode,
        "production_runtime_ready": False,
    }
    audit_payload = {
        "schema_version": CONVERSION_FUNNEL_SCHEMA_VERSION,
        "run_id": run_id,
        "as_of_date": inputs.as_of_date,
        **leaf_payload,
        "metric_rows": [item.to_dict() for item in metric_rows],
        "manifest": manifest,
        "production_runtime_ready": False,
    }
    audit = audit_conversion_funnel(audit_payload)
    if audit["critical_count_sum"]:
        raise ValueError(f"conversion funnel audit failed: {audit['critical_counts']}")
    manifest = {
        **manifest,
        "critical_counts": dict(audit["critical_counts"]),
        "critical_count_sum": 0,
    }
    return ConversionFunnelResult(
        run_id=run_id,
        as_of_date=inputs.as_of_date,
        candidates=inputs.candidates,
        stage_leaves=inputs.stage_leaves,
        usage_records=inputs.usage_records,
        metric_rows=metric_rows,
        test_mode=inputs.test_mode,
        audit=audit,
        manifest=manifest,
    )


def record_question_source_task_leaves(
    *,
    candidate_id: str,
    recipe_parent_leaf_id: str,
    task: QuestionSourceTask,
) -> tuple[FunnelStageLeaf, tuple[FunnelStageLeaf, ...]]:
    """Record canonical SourceTask and LLM literal-query leaves without inventing queries."""

    original_gap_id = original_gap_id_for_question_source_task(task)
    task_leaf = FunnelStageLeaf(
        leaf_id="FLEAF-"
        + stable_hash(
            {
                "stage": FunnelStage.SOURCE_TASK.value,
                "candidate_id": candidate_id,
                "task_id": task.task_id,
            }
        )[:24],
        candidate_id=candidate_id,
        stage=FunnelStage.SOURCE_TASK.value,
        status=FunnelLeafStatus.PLANNED.value,
        parent_ids=(recipe_parent_leaf_id,),
        archetype_id=task.archetype_id,
        recipe_id=task.recipe_id,
        task_id=task.task_id,
        original_gap_id=original_gap_id,
        primitive_id=task.primitive_id,
    )
    query_leaves = tuple(
        FunnelStageLeaf(
            leaf_id="FLEAF-"
            + stable_hash(
                {
                    "stage": FunnelStage.QUERY.value,
                    "candidate_id": candidate_id,
                    "task_id": task.task_id,
                    "query": query,
                }
            )[:24],
            candidate_id=candidate_id,
            stage=FunnelStage.QUERY.value,
            status=FunnelLeafStatus.EXECUTED.value,
            parent_ids=(task_leaf.leaf_id,),
            archetype_id=task.archetype_id,
            recipe_id=task.recipe_id,
            task_id=task.task_id,
            query_text=query,
        )
        for query in task.query_intent.literal_queries
    )
    return task_leaf, query_leaves


def original_gap_id_for_question_source_task(task: QuestionSourceTask) -> str:
    return "OGAP-" + stable_hash(
        {
            "context_id": task.context_id,
            "recipe_id": task.recipe_id,
            "primitive_id": task.primitive_id,
            "missing_information": list(task.missing_information),
        }
    )[:24]


def audit_conversion_funnel(
    result: ConversionFunnelResult | Mapping[str, Any],
) -> Mapping[str, Any]:
    payload = result.to_dict() if isinstance(result, ConversionFunnelResult) else dict(result)
    raw_candidates = payload.get("candidates")
    raw_leaves = payload.get("stage_leaves")
    raw_usages = payload.get("usage_records")
    raw_metrics = payload.get("metric_rows")
    candidates = tuple(_mapping_rows(payload.get("candidates")))
    leaves = tuple(_mapping_rows(payload.get("stage_leaves")))
    usages = tuple(_mapping_rows(payload.get("usage_records")))
    projected_metrics = tuple(_mapping_rows(payload.get("metric_rows")))
    candidate_ids = tuple(str(item.get("candidate_id") or "") for item in candidates)
    leaf_ids = tuple(str(item.get("leaf_id") or "") for item in leaves)
    usage_ids = tuple(str(item.get("usage_id") or "") for item in usages)
    candidate_by_id = {
        str(item.get("candidate_id") or ""): item
        for item in candidates
        if item.get("candidate_id")
    }
    leaf_by_id = {
        str(item.get("leaf_id") or ""): item
        for item in leaves
        if item.get("leaf_id")
    }
    node_stage = {candidate_id: "CANDIDATE" for candidate_id in candidate_by_id}
    node_stage.update(
        {
            leaf_id: str(item.get("stage") or "")
            for leaf_id, item in leaf_by_id.items()
        }
    )
    node_candidate = {
        candidate_id: candidate_id for candidate_id in candidate_by_id
    }
    node_candidate.update(
        {
            leaf_id: str(item.get("candidate_id") or "")
            for leaf_id, item in leaf_by_id.items()
        }
    )

    invalid_candidate_contract = sum(
        not _candidate_mapping_valid(item) for item in candidates
    )
    invalid_leaf_contract = sum(not _leaf_mapping_valid(item) for item in leaves)
    invalid_usage_contract = sum(not _usage_mapping_valid(item) for item in usages)
    invalid_nonmapping_row = sum(
        _sequence_size(raw) - len(rows)
        for raw, rows in (
            (raw_candidates, candidates),
            (raw_leaves, leaves),
            (raw_usages, usages),
            (raw_metrics, projected_metrics),
        )
    )
    parent_missing = 0
    cross_candidate_parent = 0
    stage_parent_mismatch = 0
    for leaf in leaves:
        stage = str(leaf.get("stage") or "")
        candidate_id = str(leaf.get("candidate_id") or "")
        parents = tuple(str(item) for item in leaf.get("parent_ids") or ())
        if not parents:
            parent_missing += 1
        for parent_id in parents:
            if parent_id not in node_stage:
                parent_missing += 1
                continue
            if node_candidate.get(parent_id) != candidate_id:
                cross_candidate_parent += 1
            if stage == FunnelStage.TERMINAL.value:
                if node_stage[parent_id] == FunnelStage.TERMINAL.value:
                    stage_parent_mismatch += 1
            elif node_stage[parent_id] != _EXPECTED_PARENT_STAGE.get(stage):
                stage_parent_mismatch += 1
    edge_lineage_mismatch = _edge_lineage_mismatch(
        leaves=leaves,
        leaf_by_id=leaf_by_id,
    )

    children_by_parent: dict[str, list[Mapping[str, Any]]] = {}
    for leaf in leaves:
        for parent_id in leaf.get("parent_ids") or ():
            children_by_parent.setdefault(str(parent_id), []).append(leaf)
    assertion_without_claim_terminal = sum(
        sum(
            str(child.get("stage") or "") == FunnelStage.CLAIM.value
            for child in children_by_parent.get(str(item.get("leaf_id") or ""), ())
        )
        != 1
        for item in leaves
        if item.get("stage") == FunnelStage.ASSERTION.value
    )

    task_by_candidate_and_id = {
        (str(item.get("candidate_id") or ""), str(item.get("task_id") or "")): item
        for item in leaves
        if item.get("stage") == FunnelStage.SOURCE_TASK.value and item.get("task_id")
    }
    claim_without_task_lineage = 0
    direct_closure_route_mismatch = 0
    rerouted_without_route_change = 0
    primitive_claim_lineage_mismatch = 0
    primitive_status_mismatch = 0
    for leaf in leaves:
        stage = str(leaf.get("stage") or "")
        if stage == FunnelStage.CLAIM.value:
            key = (
                str(leaf.get("candidate_id") or ""),
                str(leaf.get("task_id") or ""),
            )
            task = task_by_candidate_and_id.get(key)
            if task is None:
                claim_without_task_lineage += 1
                continue
            same_route = all(
                leaf.get(field_name) == task.get(field_name)
                for field_name in (
                    "archetype_id",
                    "recipe_id",
                    "primitive_id",
                    "original_gap_id",
                )
            )
            status = str(leaf.get("status") or "")
            if status in {
                FunnelLeafStatus.ACCEPTED_DIRECT.value,
                FunnelLeafStatus.COUNTER_DIRECT.value,
            } and not same_route:
                direct_closure_route_mismatch += 1
            if status == FunnelLeafStatus.ACCEPTED_REROUTED.value and (
                same_route
                or leaf.get("original_gap_id") != task.get("original_gap_id")
            ):
                rerouted_without_route_change += 1
        elif stage == FunnelStage.PRIMITIVE.value:
            parent_claims = tuple(
                leaf_by_id.get(str(parent_id))
                for parent_id in leaf.get("parent_ids") or ()
            )
            if any(item is None for item in parent_claims) or any(
                item is not None
                and any(
                    leaf.get(field_name) != item.get(field_name)
                    for field_name in (
                        "candidate_id",
                        "archetype_id",
                        "recipe_id",
                        "task_id",
                        "original_gap_id",
                        "primitive_id",
                        "document_id",
                        "assertion_id",
                        "claim_id",
                    )
                )
                for item in parent_claims
            ):
                primitive_claim_lineage_mismatch += 1
            else:
                expected_status = {
                    FunnelLeafStatus.ACCEPTED_DIRECT.value: (
                        FunnelLeafStatus.SATISFIED.value
                    ),
                    FunnelLeafStatus.ACCEPTED_REROUTED.value: (
                        FunnelLeafStatus.REROUTED.value
                    ),
                    FunnelLeafStatus.COUNTER_DIRECT.value: (
                        FunnelLeafStatus.COUNTER.value
                    ),
                }.get(str(parent_claims[0].get("status") or ""))
                if expected_status is None or leaf.get("status") != expected_status:
                    primitive_status_mismatch += 1

    terminal_by_candidate: dict[str, list[Mapping[str, Any]]] = {}
    for leaf in leaves:
        if leaf.get("stage") == FunnelStage.TERMINAL.value:
            terminal_by_candidate.setdefault(
                str(leaf.get("candidate_id") or ""), []
            ).append(leaf)
    full_thesis_without_full_score = 0
    pending_with_final_score = 0
    disproved_without_hard_break = 0
    provider_pending_without_provider_error = 0
    full_thesis_with_open_original_gap = 0
    for candidate_id, terminals in terminal_by_candidate.items():
        for terminal in terminals:
            ancestors = _ancestor_rows(terminal, leaf_by_id)
            scores = tuple(
                item
                for item in ancestors
                if item.get("stage") == FunnelStage.SCORE.value
            )
            outcome = str(terminal.get("status") or "")
            if outcome == CurrentDeepOutcome.FULL_THESIS.value and not any(
                item.get("status") == AtomicScoreType.FULL_E2R_100.value
                and item.get("score_finalization_allowed") is True
                for item in scores
            ):
                full_thesis_without_full_score += 1
            if outcome == CurrentDeepOutcome.FULL_THESIS.value:
                original_gap_ids = {
                    str(item.get("original_gap_id") or "")
                    for item in leaves
                    if item.get("candidate_id") == candidate_id
                    and item.get("stage") == FunnelStage.SOURCE_TASK.value
                }
                directly_closed_gap_ids = {
                    str(item.get("original_gap_id") or "")
                    for item in leaves
                    if item.get("candidate_id") == candidate_id
                    and item.get("stage") == FunnelStage.CLAIM.value
                    and item.get("status")
                    == FunnelLeafStatus.ACCEPTED_DIRECT.value
                }
                if original_gap_ids - directly_closed_gap_ids:
                    full_thesis_with_open_original_gap += 1
            elif outcome in _PENDING_OUTCOMES and any(
                item.get("score_finalization_allowed") is True for item in scores
            ):
                pending_with_final_score += 1
            elif outcome == CurrentDeepOutcome.DISPROVED.value and not any(
                item.get("status") == AtomicScoreType.NO_SCORE.value
                and item.get("hard_break") is True
                for item in scores
            ):
                disproved_without_hard_break += 1
            if outcome == CurrentDeepOutcome.PROVIDER_PENDING.value and not any(
                item.get("stage") == FunnelStage.RESULT.value
                and item.get("status") == FunnelLeafStatus.PROVIDER_FAILED.value
                and str(item.get("provider_error") or "").strip()
                for item in ancestors
            ):
                provider_pending_without_provider_error += 1

    usage_leaf_reference_mismatch = 0
    for usage in usages:
        candidate_id = str(usage.get("candidate_id") or "")
        for leaf_id in usage.get("operation_leaf_ids") or ():
            leaf = leaf_by_id.get(str(leaf_id))
            if leaf is None or str(leaf.get("candidate_id") or "") != candidate_id:
                usage_leaf_reference_mismatch += 1
    usage_operation_leaf_ids = tuple(
        str(leaf_id)
        for item in usages
        for leaf_id in item.get("operation_leaf_ids") or ()
    )
    duplicate_usage_operation_leaf = len(usage_operation_leaf_ids) - len(
        set(usage_operation_leaf_ids)
    )
    usage_count_leaf_mismatch = 0
    for candidate_id in candidate_by_id:
        candidate_leaves = tuple(
            item for item in leaves if item.get("candidate_id") == candidate_id
        )
        candidate_usages = tuple(
            item for item in usages if item.get("candidate_id") == candidate_id
        )
        expected_counts = {
            "query_count": sum(
                item.get("stage") == FunnelStage.QUERY.value
                and item.get("status") == FunnelLeafStatus.EXECUTED.value
                for item in candidate_leaves
            ),
            "result_count": sum(
                item.get("stage") == FunnelStage.RESULT.value
                and item.get("status") == FunnelLeafStatus.RETURNED.value
                for item in candidate_leaves
            ),
            "fetch_count": sum(
                item.get("stage") == FunnelStage.FETCHED_DOCUMENT.value
                for item in candidate_leaves
            ),
        }
        for field_name, expected_count in expected_counts.items():
            actual_count = sum(
                max(0, _safe_nonnegative_int(item.get(field_name)))
                for item in candidate_usages
            )
            if actual_count != expected_count:
                usage_count_leaf_mismatch += 1

    expected_metrics = _recompute_metric_rows(candidates, leaves, usages)
    expected_metric_by_scope = {
        (item.scope_type, item.scope_id): item.to_dict() for item in expected_metrics
    }
    projected_metric_by_scope = {
        (str(item.get("scope_type") or ""), str(item.get("scope_id") or "")): item
        for item in projected_metrics
        if item.get("scope_type") and item.get("scope_id")
    }
    projected_metric_scope_keys = tuple(
        (
            str(item.get("scope_type") or ""),
            str(item.get("scope_id") or ""),
        )
        for item in projected_metrics
    )
    candidate_metric_projection_mismatch = _scope_projection_mismatches(
        FunnelMetricScope.CANDIDATE,
        expected_metric_by_scope,
        projected_metric_by_scope,
    )
    archetype_metric_projection_mismatch = _scope_projection_mismatches(
        FunnelMetricScope.ARCHETYPE,
        expected_metric_by_scope,
        projected_metric_by_scope,
    )
    global_metric_projection_mismatch = _scope_projection_mismatches(
        FunnelMetricScope.GLOBAL,
        expected_metric_by_scope,
        projected_metric_by_scope,
    )
    projected_metric_contract_failure = sum(
        not _metric_mapping_valid(item) for item in projected_metrics
    )
    non_direct_progress_credit = sum(
        _safe_nonnegative_int(item.get("meaningful_progress_count"))
        != _safe_nonnegative_int(
            expected_metric_by_scope.get(
                (
                    str(item.get("scope_type") or ""),
                    str(item.get("scope_id") or ""),
                ),
                {},
            ).get("direct_original_gap_closure_count")
        )
        for item in projected_metrics
    )
    task_shell_as_progress = sum(
        _safe_nonnegative_int(item.get("task_shell_progress_credit_count")) != 0
        for item in projected_metrics
    )

    as_of = str(payload.get("as_of_date") or "")
    leaf_payload = _mapping_leaf_payload(payload)
    leaf_hash = stable_hash(leaf_payload)
    expected_run_id = _run_id(as_of, leaf_hash) if _safe_date(as_of) else ""
    manifest = payload.get("manifest")
    manifest_mapping = dict(manifest) if isinstance(manifest, Mapping) else {}
    critical = {
        "invalid_candidate_contract": invalid_candidate_contract,
        "invalid_leaf_contract": invalid_leaf_contract,
        "invalid_usage_contract": invalid_usage_contract,
        "invalid_nonmapping_row": invalid_nonmapping_row,
        "duplicate_candidate_id": len(candidate_ids) - len(set(candidate_ids)),
        "duplicate_leaf_id": len(leaf_ids) - len(set(leaf_ids)),
        "duplicate_usage_id": len(usage_ids) - len(set(usage_ids)),
        "duplicate_metric_scope": len(projected_metric_scope_keys)
        - len(set(projected_metric_scope_keys)),
        "candidate_leaf_id_collision": len(set(candidate_ids).intersection(leaf_ids)),
        "leaf_outside_candidate": sum(
            str(item.get("candidate_id") or "") not in candidate_by_id
            for item in leaves
        ),
        "usage_outside_candidate": sum(
            str(item.get("candidate_id") or "") not in candidate_by_id
            for item in usages
        ),
        "parent_missing": parent_missing,
        "cross_candidate_parent": cross_candidate_parent,
        "stage_parent_mismatch": stage_parent_mismatch,
        "edge_lineage_mismatch": edge_lineage_mismatch,
        "duplicate_source_task_lineage": _duplicate_stage_key_count(
            leaves,
            stage=FunnelStage.SOURCE_TASK,
            fields=("candidate_id", "task_id"),
        ),
        "duplicate_query_lineage": _duplicate_stage_key_count(
            leaves,
            stage=FunnelStage.QUERY,
            fields=("candidate_id", "task_id", "query_text"),
        ),
        "duplicate_fetched_document_lineage": _duplicate_stage_key_count(
            leaves,
            stage=FunnelStage.FETCHED_DOCUMENT,
            fields=("candidate_id", "document_id"),
        ),
        "duplicate_claim_lineage": _duplicate_stage_key_count(
            leaves,
            stage=FunnelStage.CLAIM,
            fields=("candidate_id", "claim_id"),
        ),
        "duplicate_score_decision_lineage": _duplicate_stage_key_count(
            leaves,
            stage=FunnelStage.SCORE,
            fields=("candidate_id", "score_decision_id"),
        ),
        "unexplained_archetype_attribution": _unexplained_archetype_count(
            candidates=candidates,
            leaves=leaves,
            usages=usages,
            leaf_by_id=leaf_by_id,
        ),
        "candidate_without_terminal": sum(
            len(terminal_by_candidate.get(candidate_id, ())) == 0
            for candidate_id in candidate_by_id
        ),
        "candidate_with_multiple_terminals": sum(
            max(0, len(terminal_by_candidate.get(candidate_id, ())) - 1)
            for candidate_id in candidate_by_id
        ),
        "terminal_outside_candidate": len(
            set(terminal_by_candidate) - set(candidate_by_id)
        ),
        "assertion_without_one_claim_terminal": assertion_without_claim_terminal,
        "claim_without_source_task_lineage": claim_without_task_lineage,
        "direct_closure_route_mismatch": direct_closure_route_mismatch,
        "rerouted_without_route_change": rerouted_without_route_change,
        "primitive_claim_lineage_mismatch": primitive_claim_lineage_mismatch,
        "primitive_status_mismatch": primitive_status_mismatch,
        "full_thesis_without_final_full_score": full_thesis_without_full_score,
        "full_thesis_with_open_original_gap": (
            full_thesis_with_open_original_gap
        ),
        "pending_with_finalized_score": pending_with_final_score,
        "disproved_without_hard_break_score": disproved_without_hard_break,
        "provider_pending_without_provider_error": (
            provider_pending_without_provider_error
        ),
        "usage_leaf_reference_mismatch": usage_leaf_reference_mismatch,
        "duplicate_usage_operation_leaf": duplicate_usage_operation_leaf,
        "usage_count_leaf_mismatch": usage_count_leaf_mismatch,
        "candidate_metric_projection_mismatch": (
            candidate_metric_projection_mismatch
        ),
        "archetype_metric_projection_mismatch": (
            archetype_metric_projection_mismatch
        ),
        "global_metric_projection_mismatch": global_metric_projection_mismatch,
        "projected_metric_contract_failure": projected_metric_contract_failure,
        "non_direct_original_gap_progress_credit": non_direct_progress_credit,
        "source_task_shell_as_progress": task_shell_as_progress,
        "run_id_mismatch": int(
            bool(payload.get("run_id"))
            and str(payload.get("run_id")) != expected_run_id
        ),
        "manifest_leaf_hash_mismatch": int(
            bool(manifest_mapping)
            and manifest_mapping.get("leaf_hash") != leaf_hash
        ),
        "manifest_metric_hash_mismatch": int(
            bool(manifest_mapping)
            and manifest_mapping.get("metric_hash")
            != stable_hash([item.to_dict() for item in expected_metrics])
        ),
        "production_runtime_ready_overclaim": int(
            payload.get("production_runtime_ready") is True
            or manifest_mapping.get("production_runtime_ready") is True
        ),
    }
    return {
        "schema_version": CONVERSION_FUNNEL_AUDIT_SCHEMA_VERSION,
        "status": (
            "CONVERSION_FUNNEL_OBSERVABILITY_PASS"
            if candidates and sum(critical.values()) == 0
            else "CONVERSION_FUNNEL_OBSERVABILITY_FAIL"
        ),
        "candidate_count": len(candidates),
        "stage_leaf_count": len(leaves),
        "usage_record_count": len(usages),
        "metric_row_count": len(expected_metrics),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "result_hash": leaf_hash,
        "metric_hash": stable_hash([item.to_dict() for item in expected_metrics]),
        "production_runtime_ready": False,
    }


def write_conversion_funnel(
    result: ConversionFunnelResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "manifest": root / "conversion_funnel_manifest.json",
        "audit": root / "conversion_funnel_audit.json",
        "candidates": root / "conversion_funnel_candidates.jsonl",
        "stage_leaves": root / "conversion_funnel_stage_leaves.jsonl",
        "usage": root / "conversion_funnel_usage.jsonl",
        "metrics": root / "conversion_funnel_metrics.jsonl",
        "report": root / "conversion_funnel_report.md",
    }
    write_json(paths["manifest"], result.manifest)
    write_json(paths["audit"], result.audit)
    write_jsonl(paths["candidates"], (item.to_dict() for item in result.candidates))
    write_jsonl(
        paths["stage_leaves"],
        (item.to_dict() for item in result.stage_leaves),
    )
    write_jsonl(paths["usage"], (item.to_dict() for item in result.usage_records))
    write_jsonl(paths["metrics"], (item.to_dict() for item in result.metric_rows))
    write_text(paths["report"], render_conversion_funnel_report(result.manifest))
    return paths


def render_conversion_funnel_report(manifest: Mapping[str, Any]) -> str:
    return "\n".join(
        (
            "# Conversion Funnel Observability",
            "",
            f"- status: {manifest['status']}",
            f"- as_of_date: {manifest['as_of_date']}",
            f"- candidates: {manifest['candidate_count']}",
            f"- SourceTask shells: {manifest['source_task_count']}",
            f"- distinct original gaps: {manifest['original_gap_count']}",
            (
                "- direct original-gap closures: "
                f"{manifest['direct_original_gap_closure_count']}"
            ),
            f"- relevant document rate: {manifest['relevant_document_rate']}",
            f"- accepted claim rate: {manifest['accepted_claim_rate']}",
            f"- rerouted claims: {manifest['rerouted_claim_count']}",
            f"- mapping rejections: {manifest['mapping_rejection_count']}",
            f"- terminal outcomes: {manifest['terminal_outcome_counts']}",
            f"- pending reasons: {manifest['pending_reason_counts']}",
            f"- cost USD: {manifest['cost_usd']}",
            f"- runtime seconds: {manifest['runtime_seconds']}",
            "- primary progress: DIRECT_ORIGINAL_GAP_CLOSURE",
            "- SourceTask shell progress credit: 0",
            "- production_runtime_ready: false",
            "",
        )
    )


def _recompute_metric_rows(
    candidate_rows: Sequence[Mapping[str, Any]],
    leaf_rows: Sequence[Mapping[str, Any]],
    usage_rows: Sequence[Mapping[str, Any]],
) -> tuple[FunnelMetricRow, ...]:
    candidate_by_id = {
        str(item.get("candidate_id") or ""): item
        for item in candidate_rows
        if item.get("candidate_id")
    }
    rows = [
        _metric_for_scope(
            scope_type=FunnelMetricScope.GLOBAL,
            scope_id="GLOBAL",
            candidate_ids=set(candidate_by_id),
            leaves=tuple(leaf_rows),
            usages=tuple(usage_rows),
        )
    ]
    for candidate_id in sorted(candidate_by_id):
        rows.append(
            _metric_for_scope(
                scope_type=FunnelMetricScope.CANDIDATE,
                scope_id=candidate_id,
                candidate_ids={candidate_id},
                leaves=tuple(
                    item
                    for item in leaf_rows
                    if str(item.get("candidate_id") or "") == candidate_id
                ),
                usages=tuple(
                    item
                    for item in usage_rows
                    if str(item.get("candidate_id") or "") == candidate_id
                ),
            )
        )
    archetype_ids = {
        str(archetype_id)
        for item in candidate_rows
        for archetype_id in item.get("archetype_ids") or ()
        if str(archetype_id).strip()
    }
    archetype_ids.update(
        str(item.get("archetype_id"))
        for item in (*tuple(leaf_rows), *tuple(usage_rows))
        if str(item.get("archetype_id") or "").strip()
    )
    for archetype_id in sorted(archetype_ids):
        archetype_leaves = tuple(
            item
            for item in leaf_rows
            if str(item.get("archetype_id") or "") == archetype_id
        )
        archetype_usages = tuple(
            item
            for item in usage_rows
            if str(item.get("archetype_id") or "") == archetype_id
        )
        candidate_ids = {
            str(item.get("candidate_id") or "")
            for item in candidate_rows
            if archetype_id in tuple(item.get("archetype_ids") or ())
        }
        candidate_ids.update(
            str(item.get("candidate_id") or "")
            for item in (*archetype_leaves, *archetype_usages)
        )
        rows.append(
            _metric_for_scope(
                scope_type=FunnelMetricScope.ARCHETYPE,
                scope_id=archetype_id,
                candidate_ids=candidate_ids,
                leaves=archetype_leaves,
                usages=archetype_usages,
            )
        )
    return tuple(rows)


def _metric_for_scope(
    *,
    scope_type: FunnelMetricScope,
    scope_id: str,
    candidate_ids: set[str],
    leaves: Sequence[Mapping[str, Any]],
    usages: Sequence[Mapping[str, Any]],
) -> FunnelMetricRow:
    stage_counts = {
        stage.value: sum(item.get("stage") == stage.value for item in leaves)
        for stage in FunnelStage
    }
    fetched_count = stage_counts[FunnelStage.FETCHED_DOCUMENT.value]
    relevant_count = stage_counts[FunnelStage.RELEVANT_DOCUMENT.value]
    claim_rows = tuple(
        item for item in leaves if item.get("stage") == FunnelStage.CLAIM.value
    )
    accepted_claim_count = sum(
        str(item.get("status") or "") in _CLAIM_ACCEPTED_STATUSES
        for item in claim_rows
    )
    direct_gap_ids = {
        str(item.get("original_gap_id") or "")
        for item in claim_rows
        if item.get("status") == FunnelLeafStatus.ACCEPTED_DIRECT.value
        and str(item.get("original_gap_id") or "").strip()
    }
    source_task_count = stage_counts[FunnelStage.SOURCE_TASK.value]
    original_gap_ids = {
        str(item.get("original_gap_id") or "")
        for item in leaves
        if item.get("stage") == FunnelStage.SOURCE_TASK.value
        and str(item.get("original_gap_id") or "").strip()
    }
    terminal_rows = tuple(
        item for item in leaves if item.get("stage") == FunnelStage.TERMINAL.value
    )
    terminal_counts = {
        outcome.value: sum(item.get("status") == outcome.value for item in terminal_rows)
        for outcome in CurrentDeepOutcome
    }
    pending_reasons = Counter(
        str(item.get("terminal_reason") or "")
        for item in terminal_rows
        if item.get("status") in _PENDING_OUTCOMES
        and str(item.get("terminal_reason") or "").strip()
    )
    return FunnelMetricRow(
        scope_type=scope_type.value,
        scope_id=scope_id,
        candidate_count=len({item for item in candidate_ids if item}),
        stage_counts=stage_counts,
        source_task_count=source_task_count,
        original_gap_count=len(original_gap_ids),
        fetched_document_count=fetched_count,
        relevant_document_count=relevant_count,
        relevant_document_rate=_ratio(relevant_count, fetched_count),
        assertion_count=stage_counts[FunnelStage.ASSERTION.value],
        claim_count=len(claim_rows),
        accepted_claim_count=accepted_claim_count,
        accepted_claim_rate=_ratio(accepted_claim_count, len(claim_rows)),
        direct_original_gap_closure_count=len(direct_gap_ids),
        direct_original_gap_closure_rate=_ratio(
            len(direct_gap_ids), len(original_gap_ids)
        ),
        meaningful_progress_count=len(direct_gap_ids),
        task_shell_progress_credit_count=0,
        rerouted_claim_count=sum(
            item.get("status") == FunnelLeafStatus.ACCEPTED_REROUTED.value
            for item in claim_rows
        ),
        mapping_rejection_count=sum(
            item.get("status") == FunnelLeafStatus.MAPPING_REJECTED.value
            for item in claim_rows
        ),
        terminal_outcome_counts=terminal_counts,
        pending_reason_counts=dict(sorted(pending_reasons.items())),
        query_usage_count=sum(
            max(0, _safe_nonnegative_int(item.get("query_count")))
            for item in usages
        ),
        result_usage_count=sum(
            max(0, _safe_nonnegative_int(item.get("result_count")))
            for item in usages
        ),
        fetch_usage_count=sum(
            max(0, _safe_nonnegative_int(item.get("fetch_count")))
            for item in usages
        ),
        input_tokens=sum(
            max(0, _safe_nonnegative_int(item.get("input_tokens")))
            for item in usages
        ),
        output_tokens=sum(
            max(0, _safe_nonnegative_int(item.get("output_tokens")))
            for item in usages
        ),
        cost_usd=round(
            sum(max(0.0, _safe_nonnegative_float(item.get("cost_usd"))) for item in usages),
            6,
        ),
        runtime_seconds=round(
            sum(
                max(0.0, _safe_nonnegative_float(item.get("runtime_seconds")))
                for item in usages
            ),
            6,
        ),
    )


def _candidate_mapping_valid(payload: Mapping[str, Any]) -> bool:
    try:
        FunnelCandidate(
            **{
                **dict(payload),
                "archetype_ids": tuple(payload.get("archetype_ids") or ()),
            }
        )
    except (TypeError, ValueError):
        return False
    return True


def _leaf_mapping_valid(payload: Mapping[str, Any]) -> bool:
    try:
        FunnelStageLeaf(
            **{
                **dict(payload),
                "parent_ids": tuple(payload.get("parent_ids") or ()),
            }
        )
    except (TypeError, ValueError):
        return False
    return True


def _usage_mapping_valid(payload: Mapping[str, Any]) -> bool:
    try:
        FunnelUsageRecord(
            **{
                **dict(payload),
                "operation_leaf_ids": tuple(
                    payload.get("operation_leaf_ids") or ()
                ),
            }
        )
    except (TypeError, ValueError):
        return False
    return True


def _metric_mapping_valid(payload: Mapping[str, Any]) -> bool:
    try:
        FunnelMetricRow(**dict(payload))
    except (TypeError, ValueError):
        return False
    return True


def _ancestor_rows(
    leaf: Mapping[str, Any],
    leaf_by_id: Mapping[str, Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    pending = [str(item) for item in leaf.get("parent_ids") or ()]
    visited: set[str] = set()
    rows: list[Mapping[str, Any]] = []
    while pending:
        leaf_id = pending.pop()
        if leaf_id in visited:
            continue
        visited.add(leaf_id)
        parent = leaf_by_id.get(leaf_id)
        if parent is None:
            continue
        rows.append(parent)
        pending.extend(str(item) for item in parent.get("parent_ids") or ())
    return tuple(rows)


def _edge_lineage_mismatch(
    *,
    leaves: Sequence[Mapping[str, Any]],
    leaf_by_id: Mapping[str, Mapping[str, Any]],
) -> int:
    mismatch = 0
    multi_parent_allowed = {
        FunnelStage.RETRIEVAL.value,
        FunnelStage.SCORE.value,
    }
    for leaf in leaves:
        stage = str(leaf.get("stage") or "")
        parent_ids = tuple(str(item) for item in leaf.get("parent_ids") or ())
        if stage not in multi_parent_allowed and len(parent_ids) != 1:
            mismatch += 1
        parents = tuple(
            leaf_by_id.get(parent_id)
            for parent_id in parent_ids
            if parent_id in leaf_by_id
        )
        for parent in parents:
            if parent is None:
                continue
            if stage in {
                FunnelStage.RETRIEVAL.value,
                FunnelStage.RECIPE.value,
            } and leaf.get("archetype_id") != parent.get("archetype_id"):
                mismatch += 1
            elif stage == FunnelStage.SOURCE_TASK.value and any(
                leaf.get(field_name) != parent.get(field_name)
                for field_name in ("archetype_id", "recipe_id", "primitive_id")
            ):
                mismatch += 1
            elif stage == FunnelStage.QUERY.value and any(
                leaf.get(field_name) != parent.get(field_name)
                for field_name in ("archetype_id", "recipe_id", "task_id")
            ):
                mismatch += 1
            elif stage == FunnelStage.RESULT.value and any(
                leaf.get(field_name) != parent.get(field_name)
                for field_name in (
                    "archetype_id",
                    "recipe_id",
                    "task_id",
                    "query_text",
                )
            ):
                mismatch += 1
            elif stage == FunnelStage.FETCHED_DOCUMENT.value and any(
                leaf.get(field_name) != parent.get(field_name)
                for field_name in ("archetype_id", "recipe_id", "task_id")
            ):
                mismatch += 1
            elif stage == FunnelStage.RELEVANT_DOCUMENT.value and any(
                leaf.get(field_name) != parent.get(field_name)
                for field_name in (
                    "archetype_id",
                    "recipe_id",
                    "task_id",
                    "document_id",
                )
            ):
                mismatch += 1
            elif stage == FunnelStage.ASSERTION.value and any(
                leaf.get(field_name) != parent.get(field_name)
                for field_name in (
                    "archetype_id",
                    "recipe_id",
                    "task_id",
                    "document_id",
                )
            ):
                mismatch += 1
            elif stage == FunnelStage.CLAIM.value and any(
                leaf.get(field_name) != parent.get(field_name)
                for field_name in (
                    "candidate_id",
                    "task_id",
                    "document_id",
                    "assertion_id",
                )
            ):
                mismatch += 1
    return mismatch


def _duplicate_stage_key_count(
    leaves: Sequence[Mapping[str, Any]],
    *,
    stage: FunnelStage,
    fields: Sequence[str],
) -> int:
    keys = tuple(
        tuple(str(item.get(field_name) or "") for field_name in fields)
        for item in leaves
        if item.get("stage") == stage.value
    )
    return len(keys) - len(set(keys))


def _unexplained_archetype_count(
    *,
    candidates: Sequence[Mapping[str, Any]],
    leaves: Sequence[Mapping[str, Any]],
    usages: Sequence[Mapping[str, Any]],
    leaf_by_id: Mapping[str, Mapping[str, Any]],
) -> int:
    candidate_archetypes = {
        str(item.get("candidate_id") or ""): {
            str(archetype_id) for archetype_id in item.get("archetype_ids") or ()
        }
        for item in candidates
    }
    mismatch = 0
    observed_by_candidate: dict[str, set[str]] = {
        candidate_id: set(values)
        for candidate_id, values in candidate_archetypes.items()
    }
    for leaf in leaves:
        candidate_id = str(leaf.get("candidate_id") or "")
        archetype_id = str(leaf.get("archetype_id") or "")
        if archetype_id in candidate_archetypes.get(candidate_id, set()):
            observed_by_candidate.setdefault(candidate_id, set()).add(archetype_id)
            continue
        stage = str(leaf.get("stage") or "")
        allowed = (
            stage == FunnelStage.CLAIM.value
            and leaf.get("status") == FunnelLeafStatus.ACCEPTED_REROUTED.value
        )
        if stage == FunnelStage.PRIMITIVE.value:
            allowed = any(
                (parent := leaf_by_id.get(str(parent_id))) is not None
                and parent.get("status")
                == FunnelLeafStatus.ACCEPTED_REROUTED.value
                and parent.get("archetype_id") == archetype_id
                for parent_id in leaf.get("parent_ids") or ()
            )
        if stage == FunnelStage.SCORE.value:
            allowed = any(
                (parent := leaf_by_id.get(str(parent_id))) is not None
                and parent.get("archetype_id") == archetype_id
                for parent_id in leaf.get("parent_ids") or ()
            )
        if allowed:
            observed_by_candidate.setdefault(candidate_id, set()).add(archetype_id)
        else:
            mismatch += 1
    for usage in usages:
        candidate_id = str(usage.get("candidate_id") or "")
        archetype_id = str(usage.get("archetype_id") or "")
        if archetype_id not in observed_by_candidate.get(candidate_id, set()):
            mismatch += 1
    return mismatch


def _scope_projection_mismatches(
    scope: FunnelMetricScope,
    expected: Mapping[tuple[str, str], Mapping[str, Any]],
    projected: Mapping[tuple[str, str], Mapping[str, Any]],
) -> int:
    expected_rows = {
        key: value for key, value in expected.items() if key[0] == scope.value
    }
    projected_rows = {
        key: value for key, value in projected.items() if key[0] == scope.value
    }
    return len(set(expected_rows) ^ set(projected_rows)) + sum(
        stable_hash(expected_rows[key]) != stable_hash(projected_rows[key])
        for key in set(expected_rows).intersection(projected_rows)
    )


def _result_projection_payload(result: ConversionFunnelResult) -> Mapping[str, Any]:
    return {
        "schema_version": CONVERSION_FUNNEL_SCHEMA_VERSION,
        "run_id": result.run_id,
        "as_of_date": result.as_of_date,
        "candidates": [item.to_dict() for item in result.candidates],
        "stage_leaves": [item.to_dict() for item in result.stage_leaves],
        "usage_records": [item.to_dict() for item in result.usage_records],
        "metric_rows": [item.to_dict() for item in result.metric_rows],
        "test_mode": result.test_mode,
        "manifest": dict(result.manifest),
        "production_runtime_ready": result.production_runtime_ready,
    }


def _mapping_leaf_payload(payload: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "candidates": payload.get("candidates"),
        "stage_leaves": payload.get("stage_leaves"),
        "usage_records": payload.get("usage_records"),
        "test_mode": payload.get("test_mode"),
    }


def _mapping_rows(value: Any) -> tuple[Mapping[str, Any], ...]:
    if not isinstance(value, (list, tuple)):
        return ()
    return tuple(item for item in value if isinstance(item, Mapping))


def _sequence_size(value: Any) -> int:
    if isinstance(value, (list, tuple)):
        return len(value)
    return 0 if value is None else 1


def _ratio(numerator: int, denominator: int) -> float | None:
    return round(numerator / denominator, 6) if denominator else None


def _run_id(as_of_date: str, leaf_hash: str) -> str:
    return "FUNNEL-" + stable_hash(
        {"as_of_date": as_of_date, "leaf_hash": leaf_hash}
    )[:24]


def _safe_date(value: Any) -> date | None:
    try:
        return date.fromisoformat(str(value or ""))
    except ValueError:
        return None


def _safe_nonnegative_int(value: Any) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        return -1
    return value


def _safe_nonnegative_float(value: Any) -> float:
    if (
        not isinstance(value, (int, float))
        or isinstance(value, bool)
        or not math.isfinite(float(value))
        or float(value) < 0.0
    ):
        return -1.0
    return float(value)


def _require_unique_text(values: Sequence[str], *, context: str) -> None:
    if any(not isinstance(item, str) or not item.strip() for item in values):
        raise ValueError(f"{context} contains empty text")
    if len(values) != len(set(values)):
        raise ValueError(f"{context} contains duplicates")


__all__ = [
    "CONVERSION_FUNNEL_AUDIT_SCHEMA_VERSION",
    "CONVERSION_FUNNEL_SCHEMA_VERSION",
    "ConversionFunnelInput",
    "ConversionFunnelResult",
    "FunnelCandidate",
    "FunnelLeafStatus",
    "FunnelMetricRow",
    "FunnelMetricScope",
    "FunnelStage",
    "FunnelStageLeaf",
    "FunnelUsageRecord",
    "audit_conversion_funnel",
    "compile_conversion_funnel",
    "original_gap_id_for_question_source_task",
    "record_question_source_task_leaves",
    "render_conversion_funnel_report",
    "write_conversion_funnel",
]
