"""Failure-specific, LLM-query-driven adaptive investigation control."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from datetime import date
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Mapping, Protocol, Sequence

from e2r.research_brain.planning.provider_transport import (
    CodexStructuredProviderTransport,
)
from e2r.research_brain.planning.source_task import QuestionSourceTask, SourceBudget
from e2r.research_brain.runtime.claim_compiler import ClaimCompilationResult
from e2r.research_brain.runtime.source_acquisition import (
    AcquisitionResult,
    AcquisitionStatus,
    BudgetUsage,
)
from e2r.research_brain.runtime.task_satisfaction import TaskSatisfactionStatus


ADAPTIVE_INVESTIGATION_SCHEMA_VERSION = "e2r_adaptive_investigation_v1"
_MAX_CONSTRAINT_ITEMS = 20
_MAX_CONSTRAINT_TEXT_LENGTH = 500
_MAX_REQUIRED_TEXT_LENGTH = 5_000


class InvestigationFailureReason(str, Enum):
    NO_DOCUMENT_FOUND = "NO_DOCUMENT_FOUND"
    WRONG_SUBJECT = "WRONG_SUBJECT"
    STALE_ONLY = "STALE_ONLY"
    GENERIC_CONTEXT_ONLY = "GENERIC_CONTEXT_ONLY"
    REROUTED_PRIMITIVE = "REROUTED_PRIMITIVE"
    MAPPING_REJECTED = "MAPPING_REJECTED"
    CONTRADICTION_OPEN = "CONTRADICTION_OPEN"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    SOURCE_EXHAUSTED = "SOURCE_EXHAUSTED"


class InvestigationProviderKind(str, Enum):
    REAL_LLM = "REAL_LLM"
    TEST_FIXTURE_LLM = "TEST_FIXTURE_LLM"


class InvestigationRoundStatus(str, Enum):
    ACTION_PLANNED = "ACTION_PLANNED"
    PENDING = "PENDING"
    RESOLVED = "RESOLVED"


class AdaptiveInvestigationStatus(str, Enum):
    ACTION_PLANNED = "ACTION_PLANNED"
    PENDING = "PENDING"
    RESOLVED = "RESOLVED"


class ConstraintDimension(str, Enum):
    QUERY = "QUERY"
    SOURCE = "SOURCE"
    DOCUMENT = "DOCUMENT"
    TARGET = "TARGET"
    TIME = "TIME"


_REQUIRED_CHANGED_DIMENSIONS: Mapping[InvestigationFailureReason, frozenset[str]] = {
    InvestigationFailureReason.NO_DOCUMENT_FOUND: frozenset({"QUERY", "SOURCE", "DOCUMENT"}),
    InvestigationFailureReason.WRONG_SUBJECT: frozenset({"QUERY", "TARGET", "DOCUMENT"}),
    InvestigationFailureReason.STALE_ONLY: frozenset({"QUERY", "TIME", "DOCUMENT"}),
    InvestigationFailureReason.GENERIC_CONTEXT_ONLY: frozenset({"QUERY", "DOCUMENT", "TARGET"}),
    InvestigationFailureReason.REROUTED_PRIMITIVE: frozenset({"QUERY", "SOURCE", "DOCUMENT"}),
    InvestigationFailureReason.MAPPING_REJECTED: frozenset({"QUERY", "DOCUMENT"}),
    InvestigationFailureReason.CONTRADICTION_OPEN: frozenset({"QUERY", "SOURCE", "TARGET"}),
    InvestigationFailureReason.PROVIDER_FAILED: frozenset({"QUERY", "SOURCE"}),
    InvestigationFailureReason.SOURCE_EXHAUSTED: frozenset({"QUERY", "SOURCE", "DOCUMENT"}),
}

_OUTPUT_KEYS = frozenset(
    {
        "input_id",
        "failure_reason",
        "literal_queries",
        "changed_dimensions",
        "source_constraints",
        "document_constraints",
        "target_constraints",
        "rationale",
        "abstain",
        "abstention_reason",
    }
)
_SOURCE_CONSTRAINT_KEYS = frozenset({"prefer", "exclude", "required_changes"})
_DOCUMENT_CONSTRAINT_KEYS = frozenset(
    {
        "required_document_types",
        "required_sections",
        "freshness_or_date_constraints",
        "required_provenance",
    }
)
_TARGET_CONSTRAINT_KEYS = frozenset(
    {"required_subjects", "required_directness", "excluded_subjects"}
)
_RELATIVE_TIME_RE = re.compile(
    r"(?:\blatest\b|\btoday\b|\byesterday\b|최신|오늘|어제)",
    re.IGNORECASE,
)
_YEAR_RE = re.compile(r"(?<![0-9])(20[0-9]{2})(?![0-9])")
_ISO_DATE_RE = re.compile(r"(?<![0-9])(20[0-9]{2}-[01][0-9]-[0-3][0-9])(?![0-9])")
_QUARTER_RE = re.compile(
    r"(?<![0-9])(20[0-9]{2})(?:년|\s|[-_/])*(?:Q([1-4])|([1-4])Q|([1-4])분기)",
    re.IGNORECASE,
)
_ARCHETYPE_RE = re.compile(
    r"(?:^|[^A-Za-z0-9])(?:C[0-9]{2}|R13)_[A-Z0-9_]+(?:$|[^A-Za-z0-9])",
    re.IGNORECASE,
)
_SCORE_STAGE_OUTCOME_RE = re.compile(
    r"(?:\bscore\b|\bstage\b|\bmfe\b|\bmae\b|historical[_ -]?outcome|"
    r"outcome[_ -]?label|점수|매수|매도)",
    re.IGNORECASE,
)


INVESTIGATION_ACTION_OUTPUT_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "input_id": {"type": "string", "maxLength": 256},
        "failure_reason": {
            "type": "string",
            "enum": [item.value for item in InvestigationFailureReason],
        },
        "literal_queries": {
            "type": "array",
            "maxItems": 10,
            "items": {
                "type": "string",
                "maxLength": _MAX_CONSTRAINT_TEXT_LENGTH,
            },
        },
        "changed_dimensions": {
            "type": "array",
            "maxItems": len(ConstraintDimension),
            "items": {
                "type": "string",
                "enum": [item.value for item in ConstraintDimension],
            },
        },
        "source_constraints": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "prefer": {
                    "type": "array",
                    "maxItems": _MAX_CONSTRAINT_ITEMS,
                    "items": {"type": "string", "maxLength": 500},
                },
                "exclude": {
                    "type": "array",
                    "maxItems": _MAX_CONSTRAINT_ITEMS,
                    "items": {"type": "string", "maxLength": 500},
                },
                "required_changes": {
                    "type": "array",
                    "maxItems": _MAX_CONSTRAINT_ITEMS,
                    "items": {"type": "string", "maxLength": 500},
                },
            },
            "required": sorted(_SOURCE_CONSTRAINT_KEYS),
        },
        "document_constraints": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "required_document_types": {
                    "type": "array",
                    "maxItems": _MAX_CONSTRAINT_ITEMS,
                    "items": {"type": "string", "maxLength": 500},
                },
                "required_sections": {
                    "type": "array",
                    "maxItems": _MAX_CONSTRAINT_ITEMS,
                    "items": {"type": "string", "maxLength": 500},
                },
                "freshness_or_date_constraints": {
                    "type": "array",
                    "maxItems": _MAX_CONSTRAINT_ITEMS,
                    "items": {"type": "string", "maxLength": 500},
                },
                "required_provenance": {
                    "type": "array",
                    "maxItems": _MAX_CONSTRAINT_ITEMS,
                    "items": {"type": "string", "maxLength": 500},
                },
            },
            "required": sorted(_DOCUMENT_CONSTRAINT_KEYS),
        },
        "target_constraints": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "required_subjects": {
                    "type": "array",
                    "maxItems": _MAX_CONSTRAINT_ITEMS,
                    "items": {"type": "string", "maxLength": 500},
                },
                "required_directness": {
                    "type": "array",
                    "maxItems": _MAX_CONSTRAINT_ITEMS,
                    "items": {"type": "string", "maxLength": 500},
                },
                "excluded_subjects": {
                    "type": "array",
                    "maxItems": _MAX_CONSTRAINT_ITEMS,
                    "items": {"type": "string", "maxLength": 500},
                },
            },
            "required": sorted(_TARGET_CONSTRAINT_KEYS),
        },
        "rationale": {"type": "string", "maxLength": _MAX_REQUIRED_TEXT_LENGTH},
        "abstain": {"type": "boolean"},
        "abstention_reason": {
            "type": "string",
            "maxLength": _MAX_CONSTRAINT_TEXT_LENGTH,
        },
    },
    "required": sorted(_OUTPUT_KEYS),
}


@dataclass(frozen=True)
class InvestigationFailure:
    failure_id: str
    task_id: str
    reason: str
    detail: str
    acquisition_id: str
    compilation_id: str
    evidence_ids: tuple[str, ...]
    rejection_ids: tuple[str, ...]
    failed_source_families: tuple[str, ...]
    provider_errors: tuple[str, ...]
    rerouted_claim_ids: tuple[str, ...] = ()
    rerouted_recipe_ids: tuple[str, ...] = ()
    rerouted_primitive_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        InvestigationFailureReason(self.reason)
        if not all(
            item.strip()
            for item in (
                self.failure_id,
                self.task_id,
                self.detail,
                self.acquisition_id,
                self.compilation_id,
            )
        ):
            raise ValueError("investigation failure provenance is required")
        for values in (
            self.evidence_ids,
            self.rejection_ids,
            self.failed_source_families,
            self.provider_errors,
            self.rerouted_claim_ids,
            self.rerouted_recipe_ids,
            self.rerouted_primitive_ids,
        ):
            _require_unique_strings(values)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ReroutedClaimFeedback:
    task_id: str
    original_recipe_id: str
    original_primitive_id: str
    accepted_claim_ids: tuple[str, ...]
    mapped_recipe_ids: tuple[str, ...]
    mapped_primitive_ids: tuple[str, ...]
    sources_to_avoid_repeating: tuple[str, ...]
    safe_instruction: str = (
        "Preserve the accepted rerouted claim, keep the original gap open, and use a "
        "different bounded source/document path for the original question."
    )

    def __post_init__(self) -> None:
        if not all(
            item.strip()
            for item in (
                self.task_id,
                self.original_recipe_id,
                self.original_primitive_id,
                self.safe_instruction,
            )
        ):
            raise ValueError("rerouted claim feedback identity is required")
        if not self.accepted_claim_ids or not self.mapped_primitive_ids:
            raise ValueError("rerouted claim feedback requires accepted mapping provenance")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SourceInvestigationConstraints:
    prefer: tuple[str, ...]
    exclude: tuple[str, ...]
    required_changes: tuple[str, ...]

    def __post_init__(self) -> None:
        for values in (self.prefer, self.exclude, self.required_changes):
            _require_unique_strings(values, required=True)
        overlap = set(self.prefer).intersection(self.exclude)
        if overlap:
            raise ValueError(
                "investigation source cannot be both preferred and excluded: "
                + ",".join(sorted(overlap))
            )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DocumentInvestigationConstraints:
    required_document_types: tuple[str, ...]
    required_sections: tuple[str, ...]
    freshness_or_date_constraints: tuple[str, ...]
    required_provenance: tuple[str, ...]

    def __post_init__(self) -> None:
        for values in (
            self.required_document_types,
            self.required_sections,
            self.freshness_or_date_constraints,
            self.required_provenance,
        ):
            _require_unique_strings(values, required=True)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class TargetInvestigationConstraints:
    required_subjects: tuple[str, ...]
    required_directness: tuple[str, ...]
    excluded_subjects: tuple[str, ...]

    def __post_init__(self) -> None:
        for values in (
            self.required_subjects,
            self.required_directness,
            self.excluded_subjects,
        ):
            _require_unique_strings(values, required=True)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class InvestigationProviderTrace:
    trace_id: str
    provider_name: str
    provider_kind: str
    attempt: int
    input_hash: str
    response_hash: str
    validation_error: str | None = None

    def __post_init__(self) -> None:
        InvestigationProviderKind(self.provider_kind)
        if not self.trace_id.strip() or not self.provider_name.strip():
            raise ValueError("investigation provider trace identity is required")
        if self.attempt <= 0 or self.attempt > 3:
            raise ValueError("investigation provider attempt must be bounded by three")
        if not _is_sha256(self.input_hash) or not _is_sha256(self.response_hash):
            raise ValueError("investigation provider hashes must be SHA-256")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class NextInvestigationAction:
    action_id: str
    task_id: str
    round_number: int
    failure_reason: str
    literal_queries: tuple[str, ...]
    changed_dimensions: tuple[str, ...]
    source_constraints: SourceInvestigationConstraints
    document_constraints: DocumentInvestigationConstraints
    target_constraints: TargetInvestigationConstraints
    budget: SourceBudget
    stop_conditions: tuple[str, ...]
    provider_name: str
    provider_kind: str
    prompt_hash: str
    response_hash: str
    rationale: str
    rerouted_feedback: ReroutedClaimFeedback | None = None
    deterministic_query_synthesis: bool = False
    material_gap_open: bool = True
    score_valid: bool = False
    action_kind: str = "RUNTIME_INVESTIGATION"
    coding_agent_repair: bool = False

    def __post_init__(self) -> None:
        InvestigationFailureReason(self.failure_reason)
        InvestigationProviderKind(self.provider_kind)
        for name in (
            "deterministic_query_synthesis",
            "material_gap_open",
            "score_valid",
            "coding_agent_repair",
        ):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"investigation action {name} must be boolean")
        if self.round_number <= 0:
            raise ValueError("investigation action round must be positive")
        if not all(
            item.strip()
            for item in (
                self.action_id,
                self.task_id,
                self.provider_name,
                self.rationale,
            )
        ):
            raise ValueError("next investigation action identity is required")
        _require_unique_strings(self.literal_queries, required=True)
        _require_unique_strings(self.changed_dimensions, required=True)
        for item in self.changed_dimensions:
            ConstraintDimension(item)
        if len(self.literal_queries) > self.budget.max_queries:
            raise ValueError("investigation queries exceed reserved budget")
        if not self.stop_conditions:
            raise ValueError("investigation action requires stop conditions")
        if not _is_sha256(self.prompt_hash) or not _is_sha256(self.response_hash):
            raise ValueError("investigation action hashes must be SHA-256")
        if self.deterministic_query_synthesis:
            raise ValueError("deterministic query synthesis is forbidden")
        if not self.material_gap_open or self.score_valid:
            raise ValueError("unresolved investigation action must keep score invalid")
        if self.action_kind != "RUNTIME_INVESTIGATION" or self.coding_agent_repair:
            raise ValueError("runtime action cannot claim a coding-agent repair")
        if (
            self.failure_reason == InvestigationFailureReason.REROUTED_PRIMITIVE.value
            and self.rerouted_feedback is None
        ):
            raise ValueError("rerouted investigation action requires claim feedback")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class InvestigationRound:
    round_id: str
    task_id: str
    round_number: int
    status: str
    failure: InvestigationFailure | None
    action: NextInvestigationAction | None
    traces: tuple[InvestigationProviderTrace, ...]
    pending_reason: str | None
    material_gap_open: bool
    score_valid: bool
    runtime_self_repair_label_allowed: bool = False
    coding_agent_repair: bool = False

    def __post_init__(self) -> None:
        status = InvestigationRoundStatus(self.status)
        for name in (
            "material_gap_open",
            "score_valid",
            "runtime_self_repair_label_allowed",
            "coding_agent_repair",
        ):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"investigation round {name} must be boolean")
        if not self.round_id.strip() or not self.task_id.strip() or self.round_number <= 0:
            raise ValueError("investigation round identity is required")
        if status == InvestigationRoundStatus.ACTION_PLANNED:
            if self.failure is None or self.action is None or not self.traces:
                raise ValueError("planned round requires failure, action, and provider trace")
            if self.pending_reason is not None:
                raise ValueError("planned round cannot carry pending reason")
        elif status == InvestigationRoundStatus.PENDING:
            if self.failure is None or self.action is not None or not self.pending_reason:
                raise ValueError("pending round requires failure and exact pending reason")
        elif self.failure is not None or self.action is not None or self.pending_reason:
            raise ValueError("resolved round cannot carry failure/action/pending state")
        if self.failure is not None and self.failure.task_id != self.task_id:
            raise ValueError("investigation round failure task mismatch")
        if self.action is not None and (
            self.action.task_id != self.task_id
            or self.action.round_number != self.round_number
            or self.failure is None
            or self.action.failure_reason != self.failure.reason
        ):
            raise ValueError("investigation round action leaf identity mismatch")
        if status == InvestigationRoundStatus.RESOLVED and (
            self.material_gap_open or self.score_valid
        ):
            raise ValueError("resolved Phase 10 round cannot keep a gap or forge a score")
        if status != InvestigationRoundStatus.RESOLVED and (
            not self.material_gap_open or self.score_valid
        ):
            raise ValueError("unresolved investigation round must keep score invalid")
        if self.runtime_self_repair_label_allowed or self.coding_agent_repair:
            raise ValueError("runtime investigation is not systemic code repair")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class AdaptiveInvestigationInput:
    task: QuestionSourceTask
    acquisition: AcquisitionResult
    compilation: ClaimCompilationResult
    target_aliases: tuple[str, ...]
    cumulative_usage: BudgetUsage
    previous_rounds: tuple[InvestigationRound, ...] = ()
    round_limit: int = 3

    def __post_init__(self) -> None:
        if (
            self.acquisition.task_id != self.task.task_id
            or self.compilation.task_id != self.task.task_id
        ):
            raise ValueError("adaptive investigation task identity mismatch")
        if not self.target_aliases:
            raise ValueError("adaptive investigation requires target aliases")
        if isinstance(self.round_limit, bool) or not isinstance(self.round_limit, int):
            raise ValueError("adaptive investigation round_limit must be an integer")
        if self.round_limit <= 0 or self.round_limit > 10:
            raise ValueError("adaptive investigation round_limit must be between 1 and 10")
        if any(round_.task_id != self.task.task_id for round_ in self.previous_rounds):
            raise ValueError("adaptive investigation contains another task's round")
        if tuple(round_.round_number for round_ in self.previous_rounds) != tuple(
            range(1, len(self.previous_rounds) + 1)
        ):
            raise ValueError("adaptive investigation previous round sequence is invalid")
        if (
            self.cumulative_usage.queries < self.acquisition.usage.queries
            or self.cumulative_usage.candidates < self.acquisition.usage.candidates
            or self.cumulative_usage.fetches < self.acquisition.usage.fetches
        ):
            raise ValueError(
                "adaptive investigation cumulative usage cannot under-report acquisition usage"
            )


@dataclass(frozen=True)
class AdaptiveInvestigationResult:
    investigation_id: str
    task_id: str
    status: str
    rounds: tuple[InvestigationRound, ...]
    material_gap_open: bool
    score_valid: bool
    score_finalization_allowed: bool
    self_repair_claimed: bool
    production_runtime_ready: bool = False
    schema_version: str = ADAPTIVE_INVESTIGATION_SCHEMA_VERSION

    def __post_init__(self) -> None:
        AdaptiveInvestigationStatus(self.status)
        for name in (
            "material_gap_open",
            "score_valid",
            "score_finalization_allowed",
            "self_repair_claimed",
            "production_runtime_ready",
        ):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"adaptive investigation result {name} must be boolean")
        if not self.investigation_id.strip() or not self.task_id.strip() or not self.rounds:
            raise ValueError("adaptive investigation result identity is required")
        if any(round_.task_id != self.task_id for round_ in self.rounds):
            raise ValueError("adaptive investigation result contains another task's round")
        if self.current_round.status != self.status:
            raise ValueError("adaptive investigation status differs from current round")
        if self.status != AdaptiveInvestigationStatus.RESOLVED.value and (
            not self.material_gap_open or self.score_valid or self.score_finalization_allowed
        ):
            raise ValueError("unresolved material gap cannot finalize a score")
        if self.status == AdaptiveInvestigationStatus.RESOLVED.value and (
            self.material_gap_open or self.score_valid or self.score_finalization_allowed
        ):
            raise ValueError("resolved Phase 10 result cannot forge score finalization")
        if self.self_repair_claimed or self.production_runtime_ready:
            raise ValueError("Phase 10 runtime controller cannot claim repair/readiness")

    @property
    def current_round(self) -> InvestigationRound:
        return self.rounds[-1]

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class InvestigationProviderCompletion:
    payload: Mapping[str, Any]
    raw_response: str

    def __post_init__(self) -> None:
        if not isinstance(self.payload, Mapping):
            raise ValueError("investigation provider payload must be an object")
        if not isinstance(self.raw_response, str) or not self.raw_response.strip():
            raise ValueError("investigation provider raw response must be non-empty")


class InvestigationPlannerProvider(Protocol):
    provider_name: str
    provider_kind: str
    real_provider: bool
    fake_provider: bool

    def complete(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
    ) -> InvestigationProviderCompletion:
        ...


@dataclass
class FixtureInvestigationPlannerProvider:
    callback: Callable[[Mapping[str, Any]], Mapping[str, Any]]
    provider_name: str = "fixture_adaptive_investigation_planner"
    provider_kind: str = InvestigationProviderKind.TEST_FIXTURE_LLM.value
    real_provider: bool = False
    fake_provider: bool = True

    def complete(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
    ) -> InvestigationProviderCompletion:
        del output_schema
        payload = _prompt_payload_from_text(prompt)
        response = dict(self.callback(payload))
        return InvestigationProviderCompletion(
            payload=response,
            raw_response=_stable_json(response),
        )


@dataclass
class CodexInvestigationPlannerProvider:
    transport: CodexStructuredProviderTransport
    provider_name: str = "codex_cli_adaptive_investigation_planner"
    provider_kind: str = InvestigationProviderKind.REAL_LLM.value
    real_provider: bool = True
    fake_provider: bool = False

    def complete(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
    ) -> InvestigationProviderCompletion:
        response = self.transport.complete(
            prompt=prompt,
            output_schema=output_schema,
            schema_name="adaptive_investigation_action",
        )
        return InvestigationProviderCompletion(
            payload=response.payload,
            raw_response=response.raw_response,
        )


def build_codex_investigation_planner_provider(
    *,
    working_directory: str | Path | None = None,
    env_file: str | Path | None = ".env",
    load_env: bool = True,
) -> CodexInvestigationPlannerProvider:
    """Build the real adaptive planner with the canonical Codex transport."""

    from e2r.research_brain.planning.two_pass_brain_planner import (
        build_codex_two_pass_planner_provider,
    )

    planner = build_codex_two_pass_planner_provider(
        working_directory=working_directory,
        env_file=env_file,
        load_env=load_env,
    )
    return CodexInvestigationPlannerProvider(transport=planner.transport)


@dataclass
class AdaptiveInvestigationController:
    provider: InvestigationPlannerProvider | None
    test_mode: bool = False
    max_provider_attempts: int = 3

    def __post_init__(self) -> None:
        if not isinstance(self.test_mode, bool):
            raise ValueError("adaptive investigation test_mode must be boolean")
        if (
            isinstance(self.max_provider_attempts, bool)
            or not isinstance(self.max_provider_attempts, int)
            or self.max_provider_attempts <= 0
            or self.max_provider_attempts > 3
        ):
            raise ValueError("adaptive provider attempts must be between one and three")

    def plan_next(self, inputs: AdaptiveInvestigationInput) -> AdaptiveInvestigationResult:
        failure = normalize_investigation_failure(inputs)
        round_number = len(inputs.previous_rounds) + 1
        if failure is None:
            round_ = InvestigationRound(
                round_id=_stable_id(
                    "IROUND",
                    {"task_id": inputs.task.task_id, "round": round_number, "status": "RESOLVED"},
                ),
                task_id=inputs.task.task_id,
                round_number=round_number,
                status=InvestigationRoundStatus.RESOLVED.value,
                failure=None,
                action=None,
                traces=(),
                pending_reason=None,
                material_gap_open=False,
                score_valid=False,
            )
            return _investigation_result(
                inputs=inputs,
                round_=round_,
                status=AdaptiveInvestigationStatus.RESOLVED,
            )
        if len(inputs.previous_rounds) >= inputs.round_limit:
            return _pending_result(
                inputs=inputs,
                failure=failure,
                round_number=round_number,
                reason="ROUND_LIMIT_REACHED",
            )
        remaining_budget = _remaining_budget(inputs)
        if remaining_budget is None:
            return _pending_result(
                inputs=inputs,
                failure=failure,
                round_number=round_number,
                reason="INVESTIGATION_BUDGET_EXHAUSTED",
            )
        provider_error = _provider_policy_error(self.provider, test_mode=self.test_mode)
        if provider_error:
            return _pending_result(
                inputs=inputs,
                failure=failure,
                round_number=round_number,
                reason=provider_error,
            )

        assert self.provider is not None
        feedback: list[str] = []
        rejected_queries: list[str] = []
        traces: list[InvestigationProviderTrace] = []
        for attempt in range(1, self.max_provider_attempts + 1):
            prompt_payload = _investigation_prompt_payload(
                inputs=inputs,
                failure=failure,
                round_number=round_number,
                remaining_budget=remaining_budget,
                attempt=attempt,
                validation_feedback=tuple(feedback),
                rejected_queries=tuple(dict.fromkeys(rejected_queries)),
            )
            prompt = build_investigation_prompt(prompt_payload)
            prompt_hash = _sha256(prompt)
            try:
                completion = self.provider.complete(
                    prompt=prompt,
                    output_schema=INVESTIGATION_ACTION_OUTPUT_SCHEMA,
                )
            except Exception as exc:
                error = f"INVESTIGATION_PROVIDER_ERROR:{type(exc).__name__}:{exc}"
                traces.append(
                    _provider_trace(
                        provider=self.provider,
                        attempt=attempt,
                        prompt_hash=prompt_hash,
                        response_hash=_sha256(error),
                        validation_error=error,
                    )
                )
                return _pending_result(
                    inputs=inputs,
                    failure=failure,
                    round_number=round_number,
                    reason=error,
                    traces=tuple(traces),
                )
            response_hash = _sha256(completion.raw_response)
            try:
                decoded = decode_investigation_action_output(
                    completion.payload,
                    expected_input_id=str(prompt_payload["input_id"]),
                    expected_failure_reason=failure.reason,
                )
                if decoded["abstain"]:
                    traces.append(
                        _provider_trace(
                            provider=self.provider,
                            attempt=attempt,
                            prompt_hash=prompt_hash,
                            response_hash=response_hash,
                            validation_error=None,
                        )
                    )
                    return _pending_result(
                        inputs=inputs,
                        failure=failure,
                        round_number=round_number,
                        reason=f"INVESTIGATION_LLM_ABSTAINED:{decoded['abstention_reason']}",
                        traces=tuple(traces),
                    )
                action = _validated_action(
                    inputs=inputs,
                    failure=failure,
                    decoded=decoded,
                    round_number=round_number,
                    remaining_budget=remaining_budget,
                    provider_name=self.provider.provider_name,
                    provider_kind=self.provider.provider_kind,
                    prompt_hash=prompt_hash,
                    response_hash=response_hash,
                )
            except Exception as exc:
                raw_queries = completion.payload.get("literal_queries")
                if isinstance(raw_queries, (list, tuple)):
                    rejected_queries.extend(
                        item
                        for item in raw_queries
                        if isinstance(item, str) and item.strip()
                    )
                error = f"attempt_{attempt}:{type(exc).__name__}:{exc}"
                feedback.append(error)
                traces.append(
                    _provider_trace(
                        provider=self.provider,
                        attempt=attempt,
                        prompt_hash=prompt_hash,
                        response_hash=response_hash,
                        validation_error=error,
                    )
                )
                if attempt == self.max_provider_attempts:
                    return _pending_result(
                        inputs=inputs,
                        failure=failure,
                        round_number=round_number,
                        reason="INVESTIGATION_VALIDATION_RETRY_EXHAUSTED",
                        traces=tuple(traces),
                    )
                continue
            traces.append(
                _provider_trace(
                    provider=self.provider,
                    attempt=attempt,
                    prompt_hash=prompt_hash,
                    response_hash=response_hash,
                    validation_error=None,
                )
            )
            round_ = InvestigationRound(
                round_id=_stable_id(
                    "IROUND",
                    {
                        "task_id": inputs.task.task_id,
                        "round": round_number,
                        "failure_id": failure.failure_id,
                        "action_id": action.action_id,
                    },
                ),
                task_id=inputs.task.task_id,
                round_number=round_number,
                status=InvestigationRoundStatus.ACTION_PLANNED.value,
                failure=failure,
                action=action,
                traces=tuple(traces),
                pending_reason=None,
                material_gap_open=True,
                score_valid=False,
            )
            return _investigation_result(
                inputs=inputs,
                round_=round_,
                status=AdaptiveInvestigationStatus.ACTION_PLANNED,
            )
        raise AssertionError("bounded investigation provider loop exited unexpectedly")


def normalize_investigation_failure(
    inputs: AdaptiveInvestigationInput,
) -> InvestigationFailure | None:
    satisfaction = inputs.compilation.satisfaction
    if satisfaction.original_gap_closed:
        return None
    events = inputs.compilation.ledger_events
    acquisition_status = AcquisitionStatus(inputs.acquisition.status)
    provider_errors = tuple(
        dict.fromkeys(
            (*inputs.acquisition.provider_errors, *inputs.compilation.provider_errors)
        )
    )
    mapping_rejections = tuple(
        row
        for row in inputs.compilation.rejections
        if row.stage == "MAPPING"
    )
    contradiction_events = tuple(
        event
        for event in events
        if event.contradicted_claim_ids and not event.contradiction_resolved
    )
    if provider_errors or satisfaction.status == TaskSatisfactionStatus.PROVIDER_FAILED.value:
        reason = InvestigationFailureReason.PROVIDER_FAILED
        detail = "provider failed before direct original-gap closure"
    elif not inputs.acquisition.documents and acquisition_status == AcquisitionStatus.NO_EVIDENCE:
        reason = InvestigationFailureReason.NO_DOCUMENT_FOUND
        detail = "bounded connectors returned no document candidate"
    elif contradiction_events or satisfaction.status == TaskSatisfactionStatus.COUNTER_CLAIM_FOUND.value:
        reason = InvestigationFailureReason.CONTRADICTION_OPEN
        detail = "counter or unresolved contradiction requires a resolving source"
    elif satisfaction.status == TaskSatisfactionStatus.REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN.value:
        reason = InvestigationFailureReason.REROUTED_PRIMITIVE
        detail = "accepted claim mapped elsewhere and original task remains open"
    elif satisfaction.status == TaskSatisfactionStatus.WRONG_SUBJECT.value:
        reason = InvestigationFailureReason.WRONG_SUBJECT
        detail = "documents produced only wrong or indirect subject claims"
    elif satisfaction.status in {
        TaskSatisfactionStatus.STALE_ONLY.value,
        TaskSatisfactionStatus.LIFECYCLE_REFRESH_ONLY.value,
    }:
        reason = InvestigationFailureReason.STALE_ONLY
        detail = "only stale, expired, superseded, or lifecycle-only evidence was found"
    elif mapping_rejections:
        reason = InvestigationFailureReason.MAPPING_REJECTED
        detail = "claim existed but failed recipe/predicate mapping validation"
    elif not inputs.acquisition.documents or acquisition_status == AcquisitionStatus.SOURCE_EXHAUSTED:
        reason = InvestigationFailureReason.SOURCE_EXHAUSTED
        detail = "all bounded source routes were rejected or exhausted"
    else:
        reason = InvestigationFailureReason.GENERIC_CONTEXT_ONLY
        detail = "documents contained context but no claim that answered the question"

    failed_sources = tuple(
        dict.fromkeys(
            (
                *(document.source_family for document in inputs.acquisition.documents),
                *(rejection.source_family for rejection in inputs.acquisition.rejections),
                *(_source_family_from_gap(item) for item in inputs.acquisition.source_gaps),
            )
        )
    )
    failed_sources = tuple(item for item in failed_sources if item)
    if provider_errors and not inputs.acquisition.documents:
        failed_sources = tuple(
            dict.fromkeys(
                (
                    *failed_sources,
                    inputs.task.source_route.preferred_source_families[0],
                )
            )
        )
    rerouted_events = tuple(
        event
        for event in events
        if event.satisfaction_status
        == TaskSatisfactionStatus.REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN.value
    )
    failure_payload = {
        "task_id": inputs.task.task_id,
        "reason": reason.value,
        "acquisition_id": inputs.acquisition.acquisition_id,
        "compilation_id": inputs.compilation.compilation_id,
        "evidence_ids": [event.event_id for event in events],
        "rejection_ids": [row.rejection_id for row in inputs.compilation.rejections],
    }
    return InvestigationFailure(
        failure_id=_stable_id("IFAIL", failure_payload),
        task_id=inputs.task.task_id,
        reason=reason.value,
        detail=detail,
        acquisition_id=inputs.acquisition.acquisition_id,
        compilation_id=inputs.compilation.compilation_id,
        evidence_ids=tuple(event.event_id for event in events),
        rejection_ids=tuple(row.rejection_id for row in inputs.compilation.rejections),
        failed_source_families=failed_sources,
        provider_errors=provider_errors,
        rerouted_claim_ids=tuple(event.claim_id for event in rerouted_events),
        rerouted_recipe_ids=tuple(
            dict.fromkeys(
                str(event.mapped_recipe_id)
                for event in rerouted_events
                if event.mapped_recipe_id
            )
        ),
        rerouted_primitive_ids=tuple(
            dict.fromkeys(
                str(event.mapped_primitive_id)
                for event in rerouted_events
                if event.mapped_primitive_id
            )
        ),
    )


def decode_investigation_action_output(
    payload: Mapping[str, Any],
    *,
    expected_input_id: str,
    expected_failure_reason: str,
) -> Mapping[str, Any]:
    if set(payload) != _OUTPUT_KEYS:
        raise ValueError("investigation provider output keys differ from strict schema")
    input_id = _required_text(payload.get("input_id"), context="input_id")
    if input_id != expected_input_id:
        raise ValueError("investigation provider input_id mismatch")
    failure_reason = _required_text(payload.get("failure_reason"), context="failure_reason")
    if failure_reason != expected_failure_reason:
        raise ValueError("investigation provider failure reason mismatch")
    abstain = payload.get("abstain")
    if not isinstance(abstain, bool):
        raise ValueError("investigation abstain must be boolean")
    abstention_reason_raw = payload.get("abstention_reason")
    if not isinstance(abstention_reason_raw, str):
        raise ValueError("investigation abstention_reason must be string")
    abstention_reason = abstention_reason_raw.strip()
    if len(abstention_reason) > _MAX_CONSTRAINT_TEXT_LENGTH:
        raise ValueError("investigation abstention reason is too long")
    queries = _strict_string_tuple(payload.get("literal_queries"), context="literal_queries")
    changed = _strict_string_tuple(payload.get("changed_dimensions"), context="changed_dimensions")
    rationale = _required_text(payload.get("rationale"), context="rationale")
    source = _strict_object(payload.get("source_constraints"), _SOURCE_CONSTRAINT_KEYS, "source_constraints")
    document = _strict_object(
        payload.get("document_constraints"),
        _DOCUMENT_CONSTRAINT_KEYS,
        "document_constraints",
    )
    target = _strict_object(payload.get("target_constraints"), _TARGET_CONSTRAINT_KEYS, "target_constraints")
    source_values = {
        "prefer": _strict_string_tuple(source["prefer"], context="source.prefer"),
        "exclude": _strict_string_tuple(source["exclude"], context="source.exclude"),
        "required_changes": _strict_string_tuple(
            source["required_changes"], context="source.required_changes"
        ),
    }
    document_values = {
        "required_document_types": _strict_string_tuple(
            document["required_document_types"],
            context="document.required_document_types",
        ),
        "required_sections": _strict_string_tuple(
            document["required_sections"], context="document.required_sections"
        ),
        "freshness_or_date_constraints": _strict_string_tuple(
            document["freshness_or_date_constraints"],
            context="document.freshness_or_date_constraints",
        ),
        "required_provenance": _strict_string_tuple(
            document["required_provenance"],
            context="document.required_provenance",
        ),
    }
    target_values = {
        "required_subjects": _strict_string_tuple(
            target["required_subjects"], context="target.required_subjects"
        ),
        "required_directness": _strict_string_tuple(
            target["required_directness"], context="target.required_directness"
        ),
        "excluded_subjects": _strict_string_tuple(
            target["excluded_subjects"], context="target.excluded_subjects"
        ),
    }
    if abstain:
        if not abstention_reason or queries:
            raise ValueError("abstention requires reason and no executable query")
        return {
            "input_id": input_id,
            "failure_reason": failure_reason,
            "literal_queries": queries,
            "changed_dimensions": changed,
            "source_constraints": source_values,
            "document_constraints": document_values,
            "target_constraints": target_values,
            "rationale": rationale,
            "abstain": True,
            "abstention_reason": abstention_reason,
        }
    elif not queries or abstention_reason:
        raise ValueError("executable investigation output requires queries and no abstention reason")
    return {
        "input_id": input_id,
        "failure_reason": failure_reason,
        "literal_queries": queries,
        "changed_dimensions": changed,
        "source_constraints": SourceInvestigationConstraints(
            prefer=source_values["prefer"],
            exclude=source_values["exclude"],
            required_changes=source_values["required_changes"],
        ),
        "document_constraints": DocumentInvestigationConstraints(
            required_document_types=document_values["required_document_types"],
            required_sections=document_values["required_sections"],
            freshness_or_date_constraints=document_values[
                "freshness_or_date_constraints"
            ],
            required_provenance=document_values["required_provenance"],
        ),
        "target_constraints": TargetInvestigationConstraints(
            required_subjects=target_values["required_subjects"],
            required_directness=target_values["required_directness"],
            excluded_subjects=target_values["excluded_subjects"],
        ),
        "rationale": rationale,
        "abstain": abstain,
        "abstention_reason": abstention_reason,
    }


def build_investigation_prompt(payload: Mapping[str, Any]) -> str:
    return "\n\n".join(
        (
            "You plan one bounded follow-up investigation for an unresolved E2R question.",
            "Use only the supplied target, as-of, question, failure facts, source gaps, and prior queries.",
            "Generate new literal queries yourself. Do not repeat or lightly rewrite a prior query.",
            "Do not output score, Stage, historical outcome, investment action, or a deterministic template.",
            "Return exactly one JSON object matching the supplied schema.",
            _stable_json(payload),
        )
    )


def _validated_action(
    *,
    inputs: AdaptiveInvestigationInput,
    failure: InvestigationFailure,
    decoded: Mapping[str, Any],
    round_number: int,
    remaining_budget: SourceBudget,
    provider_name: str,
    provider_kind: str,
    prompt_hash: str,
    response_hash: str,
) -> NextInvestigationAction:
    queries = validate_investigation_queries(
        decoded["literal_queries"],
        task=inputs.task,
        target_aliases=inputs.target_aliases,
        previous_queries=_previous_queries(inputs),
        forbidden_primitive_ids=(
            inputs.task.primitive_id,
            *failure.rerouted_primitive_ids,
        ),
        max_queries=remaining_budget.max_queries,
    )
    changed = tuple(decoded["changed_dimensions"])
    required_dimensions = _REQUIRED_CHANGED_DIMENSIONS[
        InvestigationFailureReason(failure.reason)
    ]
    if not required_dimensions.issubset(set(changed)):
        raise ValueError(
            "failure-specific changed dimensions missing: "
            + ",".join(sorted(required_dimensions - set(changed)))
        )
    source = decoded["source_constraints"]
    document = decoded["document_constraints"]
    target = decoded["target_constraints"]
    _validate_document_time_constraints(
        document.freshness_or_date_constraints,
        as_of_date=inputs.task.as_of_date,
        require_explicit_period=(
            failure.reason == InvestigationFailureReason.STALE_ONLY.value
        ),
    )
    target_tokens = {
        _normalize_query(item)
        for item in (
            inputs.task.company_name,
            inputs.task.symbol,
            inputs.task.target_id,
            *inputs.target_aliases,
        )
        if str(item).strip()
    }
    if not any(
        any(token in _normalize_query(subject) for token in target_tokens)
        for subject in target.required_subjects
    ):
        raise ValueError("target constraints do not explicitly require the target")
    if set(source.prefer).intersection(inputs.task.source_route.forbidden_source_families):
        raise ValueError("investigation action prefers a forbidden source family")
    if ConstraintDimension.SOURCE.value in required_dimensions:
        failed_sources = set(failure.failed_source_families)
        if failed_sources:
            if not set(source.exclude).intersection(failed_sources):
                raise ValueError(
                    "source-changing action must exclude an actually failed source path"
                )
            if not any(item not in failed_sources for item in source.prefer):
                raise ValueError(
                    "source-changing action must prefer a source outside failed paths"
                )
        else:
            original_primary = inputs.task.source_route.preferred_source_families[0]
            if original_primary not in source.exclude and set(source.prefer) == {
                original_primary
            }:
                raise ValueError(
                    "source-changing action repeats the original primary source only"
                )
    rerouted_feedback = _rerouted_feedback(inputs, failure=failure)
    budget = SourceBudget(
        max_queries=min(remaining_budget.max_queries, len(queries)),
        max_candidates=remaining_budget.max_candidates,
        max_fetches=remaining_budget.max_fetches,
    )
    action_id = _stable_id(
        "INVACTION",
        {
            "task_id": inputs.task.task_id,
            "round": round_number,
            "failure_id": failure.failure_id,
            "queries": list(queries),
            "source": source.to_dict(),
            "document": document.to_dict(),
            "target": target.to_dict(),
            "response_hash": response_hash,
        },
    )
    return NextInvestigationAction(
        action_id=action_id,
        task_id=inputs.task.task_id,
        round_number=round_number,
        failure_reason=failure.reason,
        literal_queries=queries,
        changed_dimensions=changed,
        source_constraints=source,
        document_constraints=document,
        target_constraints=target,
        budget=budget,
        stop_conditions=inputs.task.stop_condition.resolution_conditions,
        provider_name=provider_name,
        provider_kind=provider_kind,
        prompt_hash=prompt_hash,
        response_hash=response_hash,
        rationale=str(decoded["rationale"]),
        rerouted_feedback=rerouted_feedback,
    )


def validate_investigation_queries(
    queries: Sequence[str],
    *,
    task: QuestionSourceTask,
    target_aliases: Sequence[str],
    previous_queries: Sequence[str],
    forbidden_primitive_ids: Sequence[str],
    max_queries: int,
) -> tuple[str, ...]:
    clean = tuple(str(item).strip() for item in queries)
    _require_unique_strings(clean, required=True)
    if len(clean) > max_queries:
        raise ValueError("investigation query count exceeds remaining budget")
    previous = {_normalize_query(item) for item in previous_queries}
    as_of = date.fromisoformat(task.as_of_date)
    targets = tuple(
        _normalize_query(item)
        for item in (task.company_name, task.symbol, task.target_id, *target_aliases)
        if str(item).strip()
    )
    for query in clean:
        normalized = _normalize_query(query)
        if normalized in previous:
            raise ValueError("identical or already planned investigation query")
        if len(query) < 8 or len(query) > 500:
            raise ValueError("investigation query length is outside safe bounds")
        if not any(target and target in normalized for target in targets):
            raise ValueError("investigation query is not target-scoped")
        years = tuple(int(item) for item in _YEAR_RE.findall(query))
        if not years:
            raise ValueError("investigation query lacks explicit reporting year")
        if any(year > as_of.year for year in years):
            raise ValueError("investigation query contains future reporting year")
        for value in _ISO_DATE_RE.findall(query):
            if date.fromisoformat(value) > as_of:
                raise ValueError("investigation query contains future ISO date")
        for match in _QUARTER_RE.finditer(query):
            year = int(match.group(1))
            quarter = int(next(item for item in match.groups()[1:] if item))
            as_of_quarter = (as_of.month - 1) // 3 + 1
            if year > as_of.year or (year == as_of.year and quarter > as_of_quarter):
                raise ValueError("investigation query contains future reporting quarter")
        if _RELATIVE_TIME_RE.search(query):
            raise ValueError("investigation query uses relative time")
        if _ARCHETYPE_RE.search(query) or _SCORE_STAGE_OUTCOME_RE.search(query):
            raise ValueError("investigation query contains internal score/archetype/outcome context")
        for primitive_id in forbidden_primitive_ids:
            tokens = tuple(
                token
                for token in re.split(r"[_\W]+", str(primitive_id).casefold())
                if len(token) >= 3
            )
            if tokens and all(token in normalized for token in tokens):
                raise ValueError("investigation query copies internal primitive label")
    return clean


def audit_adaptive_investigation_results(
    results: Sequence[AdaptiveInvestigationResult],
    *,
    tasks_by_id: Mapping[str, QuestionSourceTask],
) -> Mapping[str, Any]:
    rounds = [round_ for result in results for round_ in result.rounds]
    actions = [round_.action for round_ in rounds if round_.action is not None]
    identical_query_retry = 0
    for result in results:
        task = tasks_by_id.get(result.task_id)
        seen = {
            _normalize_query(query)
            for query in (task.query_intent.literal_queries if task else ())
        }
        for round_ in result.rounds:
            if round_.action is None:
                continue
            for query in round_.action.literal_queries:
                normalized = _normalize_query(query)
                if normalized in seen:
                    identical_query_retry += 1
                seen.add(normalized)
    critical = {
        "unknown_task_identity": sum(
            result.task_id not in tasks_by_id for result in results
        ),
        "retry_without_failure_reason": sum(
            round_.status != InvestigationRoundStatus.RESOLVED.value
            and round_.failure is None
            for round_ in rounds
        ),
        "identical_query_retry": identical_query_retry,
        "failure_specific_constraint_missing": sum(
            action is not None
            and not _REQUIRED_CHANGED_DIMENSIONS[
                InvestigationFailureReason(action.failure_reason)
            ].issubset(set(action.changed_dimensions))
            for action in actions
        ),
        "rerouted_feedback_missing": sum(
            action.failure_reason
            == InvestigationFailureReason.REROUTED_PRIMITIVE.value
            and action.rerouted_feedback is None
            for action in actions
        ),
        "action_without_provider_trace": sum(
            round_.action is not None and not round_.traces for round_ in rounds
        ),
        "unresolved_material_score_valid": sum(
            result.material_gap_open
            and (result.score_valid or result.score_finalization_allowed)
            for result in results
        ),
        "pending_without_exact_reason": sum(
            round_.status == InvestigationRoundStatus.PENDING.value
            and not round_.pending_reason
            for round_ in rounds
        ),
        "runtime_retry_labeled_self_repair": sum(
            round_.runtime_self_repair_label_allowed or round_.coding_agent_repair
            for round_ in rounds
        ),
        "deterministic_query_synthesis": sum(
            action.deterministic_query_synthesis for action in actions
        ),
    }
    return {
        "schema_version": "e2r_adaptive_investigation_audit_v1",
        "status": (
            "ADAPTIVE_EVIDENCE_CLOSURE_PASS"
            if results and sum(critical.values()) == 0
            else "ADAPTIVE_EVIDENCE_CLOSURE_FAIL"
        ),
        "result_count": len(results),
        "round_count": len(rounds),
        "planned_action_count": len(actions),
        "pending_round_count": sum(
            round_.status == InvestigationRoundStatus.PENDING.value
            for round_ in rounds
        ),
        "resolved_round_count": sum(
            round_.status == InvestigationRoundStatus.RESOLVED.value
            for round_ in rounds
        ),
        "rerouted_feedback_action_count": sum(
            action.rerouted_feedback is not None for action in actions
        ),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "result_hash": _sha256(
            _stable_json({"results": [result.to_dict() for result in results]})
        ),
        "production_runtime_ready": False,
    }


def _investigation_prompt_payload(
    *,
    inputs: AdaptiveInvestigationInput,
    failure: InvestigationFailure,
    round_number: int,
    remaining_budget: SourceBudget,
    attempt: int,
    validation_feedback: Sequence[str],
    rejected_queries: Sequence[str],
) -> Mapping[str, Any]:
    rerouted_feedback = _rerouted_feedback(inputs, failure=failure)
    payload = {
        "schema_version": ADAPTIVE_INVESTIGATION_SCHEMA_VERSION,
        "task_id": inputs.task.task_id,
        "target": {
            "target_id": inputs.task.target_id,
            "company_name": inputs.task.company_name,
            "symbol": inputs.task.symbol,
            "aliases": list(inputs.target_aliases),
        },
        "as_of_date": inputs.task.as_of_date,
        "question": inputs.task.question_to_answer,
        "why_material": inputs.task.why_material,
        "accepted_predicates": [
            item.to_dict() for item in inputs.task.acceptance_contract.accepted_predicates
        ],
        "counter_questions": list(inputs.task.acceptance_contract.counter_questions),
        "rejection_conditions": list(inputs.task.acceptance_contract.rejection_conditions),
        "source_route": inputs.task.source_route.to_dict(),
        "failure": failure.to_dict(),
        "rerouted_feedback": rerouted_feedback.to_dict() if rerouted_feedback else None,
        "required_changed_dimensions": sorted(
            _REQUIRED_CHANGED_DIMENSIONS[InvestigationFailureReason(failure.reason)]
        ),
        "previous_queries": list(_previous_queries(inputs)),
        "remaining_budget": remaining_budget.to_dict(),
        "round_number": round_number,
        "round_limit": inputs.round_limit,
        "attempt": attempt,
        "validation_feedback": list(validation_feedback),
        "rejected_queries": list(rejected_queries),
        "rules": [
            "Literal queries must be newly generated by the LLM.",
            "Do not repeat an executed, rejected, or previously planned query.",
            "Keep every query target-scoped and on/before as_of_date.",
            "Change the failure-specific query/source/document/target/time dimensions.",
            "Do not output score, Stage, historical outcome, or investment action.",
        ],
    }
    payload["input_id"] = _stable_id("INVINPUT", payload)
    return payload


def _rerouted_feedback(
    inputs: AdaptiveInvestigationInput,
    *,
    failure: InvestigationFailure,
) -> ReroutedClaimFeedback | None:
    if failure.reason != InvestigationFailureReason.REROUTED_PRIMITIVE.value:
        return None
    if not failure.rerouted_claim_ids or not failure.rerouted_primitive_ids:
        raise ValueError("rerouted failure lacks accepted claim/mapping provenance")
    return ReroutedClaimFeedback(
        task_id=inputs.task.task_id,
        original_recipe_id=inputs.task.recipe_id,
        original_primitive_id=inputs.task.primitive_id,
        accepted_claim_ids=failure.rerouted_claim_ids,
        mapped_recipe_ids=failure.rerouted_recipe_ids,
        mapped_primitive_ids=failure.rerouted_primitive_ids,
        sources_to_avoid_repeating=failure.failed_source_families,
    )


def _remaining_budget(inputs: AdaptiveInvestigationInput) -> SourceBudget | None:
    reserved_queries = sum(
        len(round_.action.literal_queries)
        for round_ in inputs.previous_rounds
        if round_.action is not None
    )
    values = (
        inputs.task.budget.max_queries - inputs.cumulative_usage.queries - reserved_queries,
        inputs.task.budget.max_candidates - inputs.cumulative_usage.candidates,
        inputs.task.budget.max_fetches - inputs.cumulative_usage.fetches,
    )
    if min(values) <= 0:
        return None
    return SourceBudget(
        max_queries=values[0],
        max_candidates=values[1],
        max_fetches=values[2],
    )


def _previous_queries(inputs: AdaptiveInvestigationInput) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(
            (
                *inputs.task.query_intent.literal_queries,
                *(
                    query
                    for round_ in inputs.previous_rounds
                    if round_.action is not None
                    for query in round_.action.literal_queries
                ),
            )
        )
    )


def _provider_policy_error(
    provider: InvestigationPlannerProvider | None,
    *,
    test_mode: bool,
) -> str | None:
    if provider is None:
        return "INVESTIGATION_PROVIDER_NOT_CONFIGURED"
    if (
        not isinstance(provider.provider_name, str)
        or not provider.provider_name.strip()
        or not isinstance(provider.provider_kind, str)
        or not isinstance(provider.real_provider, bool)
        or not isinstance(provider.fake_provider, bool)
    ):
        return "INVALID_INVESTIGATION_PROVIDER_IDENTITY"
    identity_valid = bool(provider.real_provider) != bool(provider.fake_provider)
    if not identity_valid:
        return "INVALID_INVESTIGATION_PROVIDER_IDENTITY"
    if provider.provider_kind == InvestigationProviderKind.REAL_LLM.value:
        if not provider.real_provider:
            return "INVALID_REAL_INVESTIGATION_PROVIDER_IDENTITY"
    elif provider.provider_kind == InvestigationProviderKind.TEST_FIXTURE_LLM.value:
        if not provider.fake_provider:
            return "INVALID_FIXTURE_INVESTIGATION_PROVIDER_IDENTITY"
        if not test_mode:
            return "FIXTURE_INVESTIGATION_PROVIDER_OUTSIDE_TEST_MODE"
    else:
        return "UNKNOWN_INVESTIGATION_PROVIDER_KIND"
    return None


def _provider_trace(
    *,
    provider: InvestigationPlannerProvider,
    attempt: int,
    prompt_hash: str,
    response_hash: str,
    validation_error: str | None,
) -> InvestigationProviderTrace:
    return InvestigationProviderTrace(
        trace_id=_stable_id(
            "INVTRACE",
            {
                "provider": provider.provider_name,
                "attempt": attempt,
                "input_hash": prompt_hash,
                "response_hash": response_hash,
            },
        ),
        provider_name=provider.provider_name,
        provider_kind=provider.provider_kind,
        attempt=attempt,
        input_hash=prompt_hash,
        response_hash=response_hash,
        validation_error=validation_error,
    )


def _pending_result(
    *,
    inputs: AdaptiveInvestigationInput,
    failure: InvestigationFailure,
    round_number: int,
    reason: str,
    traces: Sequence[InvestigationProviderTrace] = (),
) -> AdaptiveInvestigationResult:
    round_ = InvestigationRound(
        round_id=_stable_id(
            "IROUND",
            {
                "task_id": inputs.task.task_id,
                "round": round_number,
                "failure_id": failure.failure_id,
                "pending_reason": reason,
            },
        ),
        task_id=inputs.task.task_id,
        round_number=round_number,
        status=InvestigationRoundStatus.PENDING.value,
        failure=failure,
        action=None,
        traces=tuple(traces),
        pending_reason=reason,
        material_gap_open=True,
        score_valid=False,
    )
    return _investigation_result(
        inputs=inputs,
        round_=round_,
        status=AdaptiveInvestigationStatus.PENDING,
    )


def _investigation_result(
    *,
    inputs: AdaptiveInvestigationInput,
    round_: InvestigationRound,
    status: AdaptiveInvestigationStatus,
) -> AdaptiveInvestigationResult:
    rounds = (*inputs.previous_rounds, round_)
    return AdaptiveInvestigationResult(
        investigation_id=_stable_id(
            "AINV",
            {
                "task_id": inputs.task.task_id,
                "round_ids": [item.round_id for item in rounds],
                "status": status.value,
            },
        ),
        task_id=inputs.task.task_id,
        status=status.value,
        rounds=rounds,
        material_gap_open=status != AdaptiveInvestigationStatus.RESOLVED,
        score_valid=False,
        score_finalization_allowed=False,
        self_repair_claimed=False,
    )


def _source_family_from_gap(value: str) -> str:
    parts = str(value).split(":")
    return parts[-1].strip() if len(parts) > 1 else ""


def _prompt_payload_from_text(prompt: str) -> Mapping[str, Any]:
    raw = prompt.rsplit("\n\n", 1)[-1]
    payload = json.loads(raw)
    if not isinstance(payload, Mapping):
        raise ValueError("investigation prompt payload is not an object")
    return payload


def _strict_object(value: Any, keys: frozenset[str], context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping) or set(value) != keys:
        raise ValueError(f"{context} keys differ from strict schema")
    return value


def _strict_string_tuple(value: Any, *, context: str) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)) or any(
        not isinstance(item, str) for item in value
    ):
        raise ValueError(f"{context} must be a string array")
    if len(value) > _MAX_CONSTRAINT_ITEMS:
        raise ValueError(f"{context} exceeds the bounded item count")
    clean = tuple(item.strip() for item in value)
    if any(len(item) > _MAX_CONSTRAINT_TEXT_LENGTH for item in clean):
        raise ValueError(f"{context} contains overlong text")
    _require_unique_strings(clean)
    return clean


def _required_text(value: Any, *, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{context} must be a non-empty string")
    clean = value.strip()
    if len(clean) > _MAX_REQUIRED_TEXT_LENGTH:
        raise ValueError(f"{context} exceeds the bounded text length")
    return clean


def _require_unique_strings(
    values: Sequence[str],
    *,
    required: bool = False,
) -> None:
    if required and not values:
        raise ValueError("investigation constraint cannot be empty")
    if any(not isinstance(item, str) or not item.strip() for item in values):
        raise ValueError("investigation string tuple contains empty values")
    if len(values) != len(set(values)):
        raise ValueError("investigation string tuple contains duplicates")


def _normalize_query(value: str) -> str:
    return re.sub(r"[^0-9a-z가-힣]", "", str(value).casefold())


def _validate_document_time_constraints(
    values: Sequence[str],
    *,
    as_of_date: str,
    require_explicit_period: bool,
) -> None:
    as_of = date.fromisoformat(as_of_date)
    explicit_period = False
    for value in values:
        if _RELATIVE_TIME_RE.search(value):
            raise ValueError("document time constraint uses relative time")
        years = tuple(int(item) for item in _YEAR_RE.findall(value))
        explicit_period = explicit_period or bool(years)
        if any(year > as_of.year for year in years):
            raise ValueError("document time constraint contains future reporting year")
        for iso_value in _ISO_DATE_RE.findall(value):
            if date.fromisoformat(iso_value) > as_of:
                raise ValueError("document time constraint contains future ISO date")
        for match in _QUARTER_RE.finditer(value):
            year = int(match.group(1))
            quarter = int(next(item for item in match.groups()[1:] if item))
            as_of_quarter = (as_of.month - 1) // 3 + 1
            if year > as_of.year or (year == as_of.year and quarter > as_of_quarter):
                raise ValueError(
                    "document time constraint contains future reporting quarter"
                )
    if require_explicit_period and not explicit_period:
        raise ValueError("stale-only action requires an explicit reporting period")


def _stable_id(prefix: str, payload: Mapping[str, Any]) -> str:
    return f"{prefix}-{_sha256(_stable_json(payload))[:24]}"


def _stable_json(value: Any) -> str:
    return json.dumps(
        _json_safe(value),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _is_sha256(value: str) -> bool:
    return re.fullmatch(r"[0-9a-f]{64}", str(value)) is not None


def _json_safe(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (tuple, list, set, frozenset)):
        return [_json_safe(item) for item in value]
    if hasattr(value, "__dataclass_fields__"):
        return _json_safe(asdict(value))
    return value


__all__ = [
    "ADAPTIVE_INVESTIGATION_SCHEMA_VERSION",
    "INVESTIGATION_ACTION_OUTPUT_SCHEMA",
    "AdaptiveInvestigationController",
    "AdaptiveInvestigationInput",
    "AdaptiveInvestigationResult",
    "AdaptiveInvestigationStatus",
    "CodexInvestigationPlannerProvider",
    "ConstraintDimension",
    "DocumentInvestigationConstraints",
    "FixtureInvestigationPlannerProvider",
    "InvestigationFailure",
    "InvestigationFailureReason",
    "InvestigationPlannerProvider",
    "InvestigationProviderTrace",
    "InvestigationRound",
    "InvestigationRoundStatus",
    "NextInvestigationAction",
    "ReroutedClaimFeedback",
    "SourceInvestigationConstraints",
    "TargetInvestigationConstraints",
    "build_codex_investigation_planner_provider",
    "build_investigation_prompt",
    "audit_adaptive_investigation_results",
    "decode_investigation_action_output",
    "normalize_investigation_failure",
    "validate_investigation_queries",
]
