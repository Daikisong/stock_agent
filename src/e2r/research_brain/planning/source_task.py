"""Question-centric SourceTask contracts and LLM literal-query validation."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from datetime import date
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence

from e2r.research_brain.intelligence_schema import (
    AcceptedClaimPredicate,
    CurrentEvidenceFact,
    EvidenceRecipe,
    PlannerSourceTaskDraft,
    stable_intelligence_id,
)
from e2r.research_brain.planning.provider_transport import (
    CodexStructuredProviderTransport,
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)


QUESTION_SOURCE_TASK_SCHEMA_VERSION = "e2r_question_source_task_v1"


class QuestionTaskPlanningStatus(str, Enum):
    COMPLETE = "COMPLETE"
    PENDING = "PENDING"
    ABSTAINED = "ABSTAINED"


class QueryGeneratorKind(str, Enum):
    REAL_LLM = "REAL_LLM"
    TEST_FIXTURE_LLM = "TEST_FIXTURE_LLM"


_OFFICIAL_FIRST_SOURCE_FAMILIES = frozenset(
    {
        "DART",
        "KIND",
        "KRX",
        "IssuerIR",
        "IssuerNewsroom",
        "CompanyEarningsCall",
        "CompanyGuide",
        "SEC",
        "Regulator",
        "ClinicalTrialRegistry",
        "CustomerOfficial",
        "CustomerNewsroom",
        "PeerReviewedPublication",
        "IndustryData",
        "Official",
        "IR",
    }
)
_NAVER_SOURCE_FAMILIES = frozenset({"Naver", "NaverNews", "NaverSearch"})
_GENERIC_QUESTION_RE = re.compile(
    r"^(?:verify|check|find|confirm|validate)\s+(?:the\s+)?"
    r"(?:primitive|primitive[_ -]?gap|gap|evidence)(?:\s|$)",
    re.IGNORECASE,
)
_GENERIC_QUERY_RE = re.compile(
    r"^(?:verify|check|find evidence for|confirm)\s+"
    r"(?:primitive|primitive[_ -]?gap|gap)(?:\s|$)",
    re.IGNORECASE,
)
_CANONICAL_ARCHETYPE_RE = re.compile(
    r"(?:^|[^A-Za-z0-9])(?:C[0-9]{2}|R13)_[A-Z0-9_]+(?:$|[^A-Za-z0-9])",
    re.IGNORECASE,
)
_FORBIDDEN_QUERY_CONTEXT_RE = re.compile(
    r"(?:source[_ -]?primary|expected[_ -]?archetype|expected[_ -]?stage|"
    r"target[_ -]?score|future[_ -]?outcome|outcome[_ -]?label|"
    r"mfe(?:[_ -]?[0-9]+[a-z]*)?|mae(?:[_ -]?[0-9]+[a-z]*)?|"
    r"(?:e2r|final|planner|target)\s+score\s*(?:[:=]|is|was)?\s*[0-9]|"
    r"score\s*(?:[:=]|is\s|was\s|of\s)\s*[0-9]|"
    r"stage\s*[:=]\s*(?:0|1|2|3|4[abc]?|5|3-(?:green|yellow|red))|"
    r"stage\s+(?:3-(?:green|yellow|red)|4[abc]))",
    re.IGNORECASE,
)
_RELATIVE_TIME_RE = re.compile(
    r"(?:\blatest\b|\btoday\b|\byesterday\b|최신|오늘|어제)",
    re.IGNORECASE,
)
_ISO_DATE_RE = re.compile(r"(?<![0-9])(20[0-9]{2}-[01][0-9]-[0-3][0-9])(?![0-9])")
_YEAR_RE = re.compile(r"(?<![0-9])(20[0-9]{2})(?![0-9])")
_QUARTER_RE = re.compile(
    r"(?<![0-9])(20[0-9]{2})(?:년|\s|[-_/])*(?:Q([1-4])|([1-4])Q|([1-4])분기)",
    re.IGNORECASE,
)


QUERY_INTENT_OUTPUT_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "input_id": {"type": "string"},
        "literal_queries": {
            "type": "array",
            "maxItems": 10,
            "items": {"type": "string"},
        },
        "generation_rationale": {"type": "string"},
        "ambiguity_reasons": {"type": "array", "items": {"type": "string"}},
        "abstain": {"type": "boolean"},
        "abstention_reason": {"type": "string"},
    },
    "required": [
        "abstain",
        "abstention_reason",
        "ambiguity_reasons",
        "generation_rationale",
        "input_id",
        "literal_queries",
    ],
}
_QUERY_OUTPUT_KEYS = frozenset(QUERY_INTENT_OUTPUT_SCHEMA["required"])


@dataclass(frozen=True)
class QuestionAcceptanceContract:
    accepted_predicates: tuple[AcceptedClaimPredicate, ...]
    required_entities: tuple[str, ...]
    required_values: tuple[str, ...]
    required_units: tuple[str, ...]
    required_time_scope: tuple[str, ...]
    required_target_directness: tuple[str, ...]
    required_current_lifecycle: tuple[str, ...]
    counter_questions: tuple[str, ...]
    rejection_conditions: tuple[str, ...]

    def __post_init__(self) -> None:
        required = {
            "accepted_predicates": self.accepted_predicates,
            "required_entities": self.required_entities,
            "required_values": self.required_values,
            "required_units": self.required_units,
            "required_time_scope": self.required_time_scope,
            "required_target_directness": self.required_target_directness,
            "required_current_lifecycle": self.required_current_lifecycle,
            "counter_questions": self.counter_questions,
            "rejection_conditions": self.rejection_conditions,
        }
        missing = [name for name, values in required.items() if not values]
        if missing:
            raise ValueError(f"question acceptance contract fields are empty: {missing}")
        if any(
            not isinstance(predicate, AcceptedClaimPredicate)
            for predicate in self.accepted_predicates
        ):
            raise ValueError("accepted_predicates must use canonical predicate objects")
        for name, values in required.items():
            if name != "accepted_predicates":
                _require_unique_nonempty_strings(values, context=name)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class SourceRouteContract:
    preferred_source_families: tuple[str, ...]
    fallback_source_families: tuple[str, ...]
    preferred_document_types: tuple[str, ...]
    preferred_sections: tuple[str, ...]
    discovery_source_families: tuple[str, ...]
    forbidden_source_families: tuple[str, ...]

    def __post_init__(self) -> None:
        required = {
            "preferred_source_families": self.preferred_source_families,
            "preferred_document_types": self.preferred_document_types,
            "preferred_sections": self.preferred_sections,
            "discovery_source_families": self.discovery_source_families,
            "forbidden_source_families": self.forbidden_source_families,
        }
        missing = [name for name, values in required.items() if not values]
        if missing:
            raise ValueError(f"source route contract fields are empty: {missing}")
        if self.preferred_source_families[0] not in _OFFICIAL_FIRST_SOURCE_FAMILIES:
            raise ValueError("question SourceTask violates official-first ordering")
        for name, values in {
            **required,
            "fallback_source_families": self.fallback_source_families,
        }.items():
            _require_unique_nonempty_strings(values, context=name)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class SourceBudget:
    max_queries: int
    max_candidates: int
    max_fetches: int

    def __post_init__(self) -> None:
        for name, value, maximum in (
            ("max_queries", self.max_queries, 10),
            ("max_candidates", self.max_candidates, 100),
            ("max_fetches", self.max_fetches, 20),
        ):
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError(f"{name} must be an integer")
            if value <= 0 or value > maximum:
                raise ValueError(f"{name} must be positive and bounded by {maximum}")

    def to_dict(self) -> dict[str, int]:
        return asdict(self)


@dataclass(frozen=True)
class StopCondition:
    resolution_conditions: tuple[str, ...]
    exhaustion_conditions: tuple[str, ...]
    stop_on_resolution: bool = True

    def __post_init__(self) -> None:
        _require_unique_nonempty_strings(
            self.resolution_conditions,
            context="resolution_conditions",
        )
        _require_unique_nonempty_strings(
            self.exhaustion_conditions,
            context="exhaustion_conditions",
        )
        if not self.resolution_conditions or not self.exhaustion_conditions:
            raise ValueError("stop and exhaustion conditions must be non-empty")
        if not self.stop_on_resolution:
            raise ValueError("canonical SourceTask must stop on resolution")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class QuestionTaskContext:
    context_id: str
    target_id: str
    target_name: str
    symbol: str
    target_aliases: tuple[str, ...]
    as_of_date: str
    current_facts: tuple[CurrentEvidenceFact, ...]
    missing_information: tuple[str, ...]
    existing_queries: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        required = (self.context_id, self.target_id, self.target_name, self.as_of_date)
        if not all(item.strip() for item in required):
            raise ValueError("question task context identity is required")
        try:
            as_of = date.fromisoformat(self.as_of_date)
        except ValueError as exc:
            raise ValueError("question task as_of_date must be an ISO date") from exc
        if not self.current_facts or not self.missing_information:
            raise ValueError("question task context requires facts and missing information")
        if any(date.fromisoformat(fact.observed_date) > as_of for fact in self.current_facts):
            raise ValueError("question task context contains future evidence")
        if len({fact.fact_id for fact in self.current_facts}) != len(self.current_facts):
            raise ValueError("question task context contains duplicate fact IDs")
        if any(
            _CANONICAL_ARCHETYPE_RE.search(fact.text)
            or _FORBIDDEN_QUERY_CONTEXT_RE.search(fact.text)
            for fact in self.current_facts
        ):
            raise ValueError("question task context contains planner leakage")
        _require_unique_nonempty_strings(self.target_aliases, context="target_aliases")
        _require_unique_nonempty_strings(
            self.missing_information,
            context="missing_information",
        )
        if any(
            _CANONICAL_ARCHETYPE_RE.search(item)
            or _FORBIDDEN_QUERY_CONTEXT_RE.search(item)
            for item in self.missing_information
        ):
            raise ValueError("missing information contains planner leakage")
        _require_unique_nonempty_strings(self.existing_queries, context="existing_queries")
        for query in self.existing_queries:
            if (
                _CANONICAL_ARCHETYPE_RE.search(query)
                or _FORBIDDEN_QUERY_CONTEXT_RE.search(query)
                or _RELATIVE_TIME_RE.search(query)
            ):
                raise ValueError("existing query contains planner leakage")
            if _YEAR_RE.search(query) is None or not _query_mentions_target(query, self):
                raise ValueError("existing query lacks target or explicit reporting year")
            _validate_query_time_scope(query, as_of=as_of)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class QueryIntent:
    intent_id: str
    semantic_intent: str
    literal_queries: tuple[str, ...]
    generation_rationale: str
    generator_kind: str
    provider_name: str
    prompt_hash: str
    response_hash: str
    generation_attempt_count: int
    ambiguity_reasons: tuple[str, ...] = ()
    validation_feedback: tuple[str, ...] = ()
    rejected_queries: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        QueryGeneratorKind(self.generator_kind)
        required = (
            self.intent_id,
            self.semantic_intent,
            self.generation_rationale,
            self.provider_name,
        )
        if not all(item.strip() for item in required):
            raise ValueError("query intent identity and rationale are required")
        _require_unique_nonempty_strings(self.literal_queries, context="literal_queries")
        if not self.literal_queries:
            raise ValueError("query intent requires LLM-generated literal queries")
        if not _is_sha256(self.prompt_hash) or not _is_sha256(self.response_hash):
            raise ValueError("query intent prompt/response hashes must be SHA-256")
        if self.generation_attempt_count <= 0 or self.generation_attempt_count > 3:
            raise ValueError("query intent generation attempts must be bounded by three")
        _require_unique_nonempty_strings(
            self.ambiguity_reasons,
            context="query_intent.ambiguity_reasons",
        )
        _require_unique_nonempty_strings(
            self.validation_feedback,
            context="query_intent.validation_feedback",
        )
        _require_unique_nonempty_strings(
            self.rejected_queries,
            context="query_intent.rejected_queries",
        )
        if len(self.validation_feedback) != self.generation_attempt_count - 1:
            raise ValueError("query intent retry feedback count is inconsistent")

    @property
    def real_provider(self) -> bool:
        return self.generator_kind == QueryGeneratorKind.REAL_LLM.value

    @property
    def fake_provider(self) -> bool:
        return self.generator_kind == QueryGeneratorKind.TEST_FIXTURE_LLM.value

    def to_dict(self) -> dict[str, Any]:
        payload = _json_safe(asdict(self))
        payload["real_provider"] = self.real_provider
        payload["fake_provider"] = self.fake_provider
        return payload


@dataclass(frozen=True)
class QuestionSourceTask:
    task_id: str
    context_id: str
    candidate_event_id: str
    target_id: str
    symbol: str
    company_name: str
    as_of_date: str
    archetype_id: str
    primitive_id: str
    recipe_id: str
    task_type: str
    question_to_answer: str
    why_material: str
    supporting_current_fact_ids: tuple[str, ...]
    missing_information: tuple[str, ...]
    acceptance_contract: QuestionAcceptanceContract
    source_route: SourceRouteContract
    query_intent: QueryIntent
    budget: SourceBudget
    stop_condition: StopCondition
    test_only: bool
    runtime_score_eligible: bool = False
    schema_version: str = QUESTION_SOURCE_TASK_SCHEMA_VERSION

    def __post_init__(self) -> None:
        required = (
            self.task_id,
            self.context_id,
            self.candidate_event_id,
            self.target_id,
            self.company_name,
            self.as_of_date,
            self.archetype_id,
            self.primitive_id,
            self.recipe_id,
            self.task_type,
            self.question_to_answer,
            self.why_material,
        )
        if not all(item.strip() for item in required):
            raise ValueError("question SourceTask identity and material question are required")
        try:
            date.fromisoformat(self.as_of_date)
        except ValueError as exc:
            raise ValueError("question SourceTask as_of_date must be ISO date") from exc
        if _is_generic_question(self.question_to_answer, self.primitive_id):
            raise ValueError("generic verify-primitive SourceTask is forbidden")
        _require_unique_nonempty_strings(
            self.supporting_current_fact_ids,
            context="supporting_current_fact_ids",
        )
        _require_unique_nonempty_strings(
            self.missing_information,
            context="question_task.missing_information",
        )
        if not self.supporting_current_fact_ids or not self.missing_information:
            raise ValueError("question SourceTask requires current fact and gap lineage")
        if self.query_intent.fake_provider and not self.test_only:
            raise ValueError("fixture query provider is test-mode only")
        if self.runtime_score_eligible:
            raise ValueError("QuestionSourceTask cannot directly contribute to score")

    @property
    def production_execution_allowed(self) -> bool:
        return self.query_intent.real_provider and not self.test_only

    def to_dict(self) -> dict[str, Any]:
        payload = _json_safe(asdict(self))
        payload["production_execution_allowed"] = self.production_execution_allowed
        return payload


@dataclass(frozen=True)
class QueryGenerationTrace:
    provider_name: str
    generator_kind: str
    prompt_hash: str
    response_hash: str

    def __post_init__(self) -> None:
        QueryGeneratorKind(self.generator_kind)
        if not self.provider_name.strip():
            raise ValueError("query generation trace provider is required")
        if not _is_sha256(self.prompt_hash) or not _is_sha256(self.response_hash):
            raise ValueError("query generation trace hashes must be SHA-256")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class QuestionTaskPending:
    input_id: str
    reason_code: str
    reason_detail: str
    provider_name: str
    prompt_hash: str
    response_hash: str
    attempt_count: int
    validation_feedback: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        required = (
            self.input_id,
            self.reason_code,
            self.reason_detail,
            self.provider_name,
        )
        if not all(item.strip() for item in required):
            raise ValueError("question task pending provenance is incomplete")
        if not _is_sha256(self.prompt_hash) or not _is_sha256(self.response_hash):
            raise ValueError("question task pending hashes must be SHA-256")
        if self.attempt_count <= 0:
            raise ValueError("question task pending attempt_count must be positive")
        _require_unique_nonempty_strings(
            self.validation_feedback,
            context="validation_feedback",
        )
        if len(self.validation_feedback) > self.attempt_count:
            raise ValueError("question task pending feedback exceeds attempt count")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class QuestionTaskPlanningResult:
    input_id: str
    status: str
    task: QuestionSourceTask | None
    pending: QuestionTaskPending | None
    traces: tuple[QueryGenerationTrace, ...]
    abstention_reason: str | None = None

    def __post_init__(self) -> None:
        QuestionTaskPlanningStatus(self.status)
        if not self.input_id.strip():
            raise ValueError("question task planning result input id is required")
        if self.status == QuestionTaskPlanningStatus.COMPLETE.value:
            if self.task is None or self.pending is not None or not self.traces:
                raise ValueError("complete question task result requires task and trace")
            final_trace = self.traces[-1]
            if (
                self.task.query_intent.prompt_hash != final_trace.prompt_hash
                or self.task.query_intent.response_hash != final_trace.response_hash
                or self.task.query_intent.provider_name != final_trace.provider_name
                or self.task.query_intent.generator_kind != final_trace.generator_kind
            ):
                raise ValueError("question task result trace identity mismatch")
        elif self.status == QuestionTaskPlanningStatus.PENDING.value:
            if self.pending is None or self.task is not None:
                raise ValueError("pending question task result requires pending detail")
            if self.pending.input_id != self.input_id:
                raise ValueError("question task pending input identity mismatch")
            if self.pending.attempt_count not in {
                len(self.traces),
                len(self.traces) + 1,
            }:
                raise ValueError("question task pending trace count is inconsistent")
        elif (
            self.task is not None
            or self.pending is not None
            or not self.traces
            or not str(self.abstention_reason or "").strip()
        ):
            raise ValueError("abstained question task result requires trace and reason")

    @property
    def trace(self) -> QueryGenerationTrace | None:
        return self.traces[-1] if self.traces else None

    def to_dict(self) -> dict[str, Any]:
        return {
            "input_id": self.input_id,
            "status": self.status,
            "task": self.task.to_dict() if self.task else None,
            "pending": self.pending.to_dict() if self.pending else None,
            "traces": [trace.to_dict() for trace in self.traces],
            "abstention_reason": self.abstention_reason,
        }


@dataclass(frozen=True)
class QueryProviderCompletion:
    payload: Mapping[str, Any]
    raw_response: str


class QuestionQueryProvider:
    provider_name = "abstract"
    generator_kind = QueryGeneratorKind.REAL_LLM.value
    real_provider = False
    fake_provider = False

    def complete(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
    ) -> QueryProviderCompletion:
        raise NotImplementedError


@dataclass
class CodexQuestionQueryProvider(QuestionQueryProvider):
    transport: CodexStructuredProviderTransport

    provider_name = "codex_cli_question_query_provider"
    generator_kind = QueryGeneratorKind.REAL_LLM.value
    real_provider = True
    fake_provider = False

    def complete(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
    ) -> QueryProviderCompletion:
        response = self.transport.complete(
            prompt=prompt,
            output_schema=output_schema,
            schema_name="question_source_task_queries",
        )
        return QueryProviderCompletion(
            payload=response.payload,
            raw_response=response.raw_response,
        )


@dataclass
class FixtureQuestionQueryProvider(QuestionQueryProvider):
    callback: Callable[[Mapping[str, Any]], Mapping[str, Any]]

    provider_name = "fixture_question_query_provider"
    generator_kind = QueryGeneratorKind.TEST_FIXTURE_LLM.value
    real_provider = False
    fake_provider = True

    def complete(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
    ) -> QueryProviderCompletion:
        del output_schema
        payload = _prompt_payload(prompt)
        response = dict(self.callback(payload))
        return QueryProviderCompletion(
            payload=response,
            raw_response=_stable_json(response),
        )


def build_codex_question_query_provider(
    *,
    working_directory: str | Path | None = None,
    env_file: str | Path | None = ".env",
    load_env: bool = True,
) -> CodexQuestionQueryProvider:
    from e2r.research_brain.planning.two_pass_brain_planner import (
        build_codex_two_pass_planner_provider,
    )

    planner_provider = build_codex_two_pass_planner_provider(
        working_directory=working_directory,
        env_file=env_file,
        load_env=load_env,
    )
    return CodexQuestionQueryProvider(transport=planner_provider.transport)


def compile_question_task_context(
    *,
    target_id: str,
    target_name: str,
    symbol: str,
    target_aliases: Iterable[str],
    as_of_date: str,
    current_facts: Sequence[CurrentEvidenceFact],
    missing_information: Iterable[str],
    existing_queries: Iterable[str] = (),
) -> QuestionTaskContext:
    aliases = _unique_strings(target_aliases)
    missing = _unique_strings(missing_information)
    previous_queries = _unique_strings(existing_queries)
    context_id = stable_intelligence_id(
        "question-task-context",
        {
            "target_id": target_id,
            "target_name": target_name,
            "symbol": symbol,
            "target_aliases": list(aliases),
            "as_of_date": as_of_date,
            "current_facts": [fact.to_dict() for fact in current_facts],
            "missing_information": list(missing),
            "existing_queries": list(previous_queries),
        },
    )
    return QuestionTaskContext(
        context_id=context_id,
        target_id=target_id,
        target_name=target_name,
        symbol=symbol,
        target_aliases=aliases,
        as_of_date=as_of_date,
        current_facts=tuple(current_facts),
        missing_information=missing,
        existing_queries=previous_queries,
    )


def plan_question_source_task(
    *,
    draft: PlannerSourceTaskDraft,
    recipe: EvidenceRecipe,
    context: QuestionTaskContext,
    candidate_event_id: str,
    task_type: str,
    provider: QuestionQueryProvider | None,
    test_mode: bool = False,
    max_generation_attempts: int = 3,
) -> QuestionTaskPlanningResult:
    _validate_draft_recipe_alignment(draft, recipe)
    _validate_task_type_for_recipe(task_type, recipe)
    if (
        isinstance(max_generation_attempts, bool)
        or not isinstance(max_generation_attempts, int)
        or max_generation_attempts <= 0
        or max_generation_attempts > 3
    ):
        raise ValueError("max_generation_attempts must be between 1 and 3")
    base_prompt_payload = _query_prompt_payload(
        draft=draft,
        recipe=recipe,
        context=context,
    )
    initial_payload = _query_attempt_prompt_payload(
        base_prompt_payload,
        attempt=1,
        validation_feedback=(),
        rejected_queries=(),
    )
    input_id = str(initial_payload["input_id"])
    prompt = build_question_query_prompt(initial_payload)
    prompt_hash = _sha256(prompt)
    if provider is None:
        return _pending_result(
            input_id=input_id,
            provider_name="none",
            reason_code="QUERY_PROVIDER_NOT_CONFIGURED",
            reason_detail="No LLM query provider was configured.",
            prompt_hash=prompt_hash,
            attempt_count=1,
        )
    provider_identity_valid = (
        bool(provider.real_provider) != bool(provider.fake_provider)
        and (
            (
                provider.generator_kind == QueryGeneratorKind.REAL_LLM.value
                and provider.real_provider
            )
            or (
                provider.generator_kind
                == QueryGeneratorKind.TEST_FIXTURE_LLM.value
                and provider.fake_provider
            )
        )
    )
    if not provider_identity_valid:
        return _pending_result(
            input_id=input_id,
            provider_name=provider.provider_name,
            reason_code="INVALID_QUERY_PROVIDER_IDENTITY",
            reason_detail="Query provider real/fake identity is inconsistent.",
            prompt_hash=prompt_hash,
            attempt_count=1,
        )
    if provider.fake_provider and not test_mode:
        return _pending_result(
            input_id=input_id,
            provider_name=provider.provider_name,
            reason_code="FAKE_QUERY_PROVIDER_NOT_ALLOWED",
            reason_detail="Fixture query provider is test-mode only.",
            prompt_hash=prompt_hash,
            attempt_count=1,
        )

    budget = SourceBudget(
        max_queries=draft.max_queries,
        max_candidates=draft.max_candidates,
        max_fetches=draft.max_fetches,
    )
    feedback: list[str] = []
    rejected_queries: list[str] = []
    traces: list[QueryGenerationTrace] = []
    for attempt in range(1, max_generation_attempts + 1):
        attempt_payload = _query_attempt_prompt_payload(
            base_prompt_payload,
            attempt=attempt,
            validation_feedback=tuple(feedback),
            rejected_queries=_unique_strings(rejected_queries),
        )
        input_id = str(attempt_payload["input_id"])
        prompt = build_question_query_prompt(attempt_payload)
        prompt_hash = _sha256(prompt)
        try:
            completion = provider.complete(
                prompt=prompt,
                output_schema=QUERY_INTENT_OUTPUT_SCHEMA,
            )
        except Exception as exc:  # provider process failures cannot synthesize a fallback
            return _pending_result(
                input_id=input_id,
                provider_name=provider.provider_name,
                reason_code=_query_provider_reason_code(exc),
                reason_detail=f"{type(exc).__name__}: {exc}",
                prompt_hash=prompt_hash,
                attempt_count=attempt,
                validation_feedback=tuple(feedback),
                traces=tuple(traces),
            )

        response_hash = _sha256(completion.raw_response)
        trace = QueryGenerationTrace(
            provider_name=provider.provider_name,
            generator_kind=provider.generator_kind,
            prompt_hash=prompt_hash,
            response_hash=response_hash,
        )
        traces.append(trace)
        try:
            decoded = decode_query_generation_output(
                completion.payload,
                expected_input_id=input_id,
            )
            if decoded["abstain"]:
                return QuestionTaskPlanningResult(
                    input_id=input_id,
                    status=QuestionTaskPlanningStatus.ABSTAINED.value,
                    task=None,
                    pending=None,
                    traces=tuple(traces),
                    abstention_reason=str(decoded["abstention_reason"]),
                )
            literal_queries = validate_llm_literal_queries(
                decoded["literal_queries"],
                context=context,
                primitive_id=recipe.primitive_id,
                budget=budget,
                prior_rejected_queries=tuple(rejected_queries),
            )
            query_intent = QueryIntent(
                intent_id=stable_intelligence_id(
                    "query-intent",
                    {
                        "input_id": input_id,
                        "literal_queries": list(literal_queries),
                        "response_hash": response_hash,
                    },
                ),
                semantic_intent=draft.query_intent,
                literal_queries=literal_queries,
                generation_rationale=str(decoded["generation_rationale"]),
                generator_kind=provider.generator_kind,
                provider_name=provider.provider_name,
                prompt_hash=prompt_hash,
                response_hash=response_hash,
                generation_attempt_count=attempt,
                ambiguity_reasons=tuple(decoded["ambiguity_reasons"]),
                validation_feedback=tuple(feedback),
                rejected_queries=_unique_strings(rejected_queries),
            )
            task = _question_task_from_validated_query(
                draft=draft,
                recipe=recipe,
                context=context,
                candidate_event_id=candidate_event_id,
                task_type=task_type,
                query_intent=query_intent,
                test_mode=test_mode,
            )
            return QuestionTaskPlanningResult(
                input_id=input_id,
                status=QuestionTaskPlanningStatus.COMPLETE.value,
                task=task,
                pending=None,
                traces=tuple(traces),
            )
        except Exception as exc:  # strict output/query failures feed the next LLM attempt
            raw_queries = completion.payload.get("literal_queries")
            if isinstance(raw_queries, (list, tuple)):
                rejected_queries.extend(
                    query for query in raw_queries if isinstance(query, str) and query.strip()
                )
            feedback.append(f"attempt_{attempt}:{type(exc).__name__}:{exc}")
            if attempt == max_generation_attempts:
                return _pending_result(
                    input_id=input_id,
                    provider_name=provider.provider_name,
                    reason_code="QUERY_VALIDATION_RETRY_EXHAUSTED",
                    reason_detail=feedback[-1],
                    prompt_hash=prompt_hash,
                    response_hash=response_hash,
                    attempt_count=attempt,
                    validation_feedback=tuple(feedback),
                    traces=tuple(traces),
                )
    raise AssertionError("bounded query generation loop exited unexpectedly")


def decode_query_generation_output(
    raw: Mapping[str, Any],
    *,
    expected_input_id: str,
) -> Mapping[str, Any]:
    actual_keys = {str(key) for key in raw}
    if actual_keys != _QUERY_OUTPUT_KEYS:
        raise ValueError(
            "query provider output keys differ: "
            f"missing={sorted(_QUERY_OUTPUT_KEYS - actual_keys)}, "
            f"unknown={sorted(actual_keys - _QUERY_OUTPUT_KEYS)}"
        )
    input_id = _required_text(raw.get("input_id"), context="query input_id")
    if input_id != expected_input_id:
        raise ValueError("query provider output input_id mismatch")
    literal_queries = _strict_string_array(
        raw.get("literal_queries"),
        context="literal_queries",
    )
    rationale = _required_text(
        raw.get("generation_rationale"),
        context="generation_rationale",
    )
    ambiguity = _strict_string_array(
        raw.get("ambiguity_reasons"),
        context="ambiguity_reasons",
    )
    abstain = raw.get("abstain")
    if not isinstance(abstain, bool):
        raise ValueError("query abstain must be a boolean")
    abstention_reason_raw = raw.get("abstention_reason")
    if not isinstance(abstention_reason_raw, str):
        raise ValueError("query abstention_reason must be a string")
    abstention_reason = abstention_reason_raw.strip()
    if abstain and not abstention_reason:
        raise ValueError("query abstention requires a reason")
    if abstain and literal_queries:
        raise ValueError("query abstention cannot carry executable literal queries")
    if not abstain and not literal_queries:
        raise ValueError("non-abstaining query output requires literal queries")
    if not abstain and abstention_reason:
        raise ValueError("non-abstaining query output cannot carry abstention reason")
    return {
        "input_id": input_id,
        "literal_queries": literal_queries,
        "generation_rationale": rationale,
        "ambiguity_reasons": ambiguity,
        "abstain": abstain,
        "abstention_reason": abstention_reason,
    }


def validate_llm_literal_queries(
    queries: Iterable[str],
    *,
    context: QuestionTaskContext,
    primitive_id: str,
    budget: SourceBudget,
    prior_rejected_queries: Sequence[str] = (),
) -> tuple[str, ...]:
    raw_queries = tuple(queries)
    if any(not isinstance(query, str) for query in raw_queries):
        raise ValueError("literal_queries items must be strings")
    clean = tuple(query.strip() for query in raw_queries)
    _require_unique_nonempty_strings(clean, context="literal_queries")
    if not clean:
        raise ValueError("LLM returned no literal query")
    if len(clean) > budget.max_queries:
        raise ValueError("LLM literal query count exceeds bounded budget")
    existing = {
        _normalize_query(query)
        for query in (*context.existing_queries, *prior_rejected_queries)
    }
    seen: set[str] = set()
    as_of = date.fromisoformat(context.as_of_date)
    for query in clean:
        normalized = _normalize_query(query)
        if len(query) < 8 or len(query) > 500:
            raise ValueError("LLM literal query length is outside safe bounds")
        if normalized in seen or normalized in existing:
            raise ValueError("LLM literal query is duplicate or already executed")
        if _GENERIC_QUERY_RE.search(query):
            raise ValueError("generic verify-primitive literal query is forbidden")
        if _CANONICAL_ARCHETYPE_RE.search(query):
            raise ValueError("literal query copies a canonical archetype label")
        if _FORBIDDEN_QUERY_CONTEXT_RE.search(query):
            raise ValueError("literal query contains score/stage/outcome leakage")
        if _RELATIVE_TIME_RE.search(query):
            raise ValueError("literal query uses relative time instead of as-of scope")
        if _YEAR_RE.search(query) is None:
            raise ValueError("literal query lacks an explicit reporting year")
        if _primitive_appears_in_query(primitive_id, query):
            raise ValueError("literal query copies primitive_id instead of current context")
        if not _query_mentions_target(query, context):
            raise ValueError("literal query is not scoped to the target company")
        _validate_query_time_scope(query, as_of=as_of)
        seen.add(normalized)
    return clean


def build_question_query_prompt(payload: Mapping[str, Any]) -> str:
    return "\n\n".join(
        (
            "You generate literal source queries for one E2R question-centric SourceTask.",
            (
                "Use the current target facts, as-of date, unresolved question, accepted "
                "predicates, counter questions, and source route. Do not copy primitive IDs."
            ),
            (
                "Every query must name the target, use an explicit safe reporting period, "
                "avoid duplicates, and remain within the supplied budget."
            ),
            "Do not output score, Stage, outcome, or investment instructions.",
            "Return exactly one JSON object matching the supplied schema.",
            _stable_json(payload),
        )
    )


def audit_question_source_tasks(
    tasks: Sequence[QuestionSourceTask],
) -> Mapping[str, Any]:
    empty_question_count = sum(not task.question_to_answer.strip() for task in tasks)
    empty_predicate_count = sum(
        not task.acceptance_contract.accepted_predicates for task in tasks
    )
    empty_rejection_count = sum(
        not task.acceptance_contract.rejection_conditions for task in tasks
    )
    generic_task_count = sum(
        _is_generic_question(task.question_to_answer, task.primitive_id) for task in tasks
    )
    official_first_violation_count = sum(
        task.source_route.preferred_source_families[0]
        not in _OFFICIAL_FIRST_SOURCE_FAMILIES
        for task in tasks
    )
    naver_first_material_count = sum(
        _material_official_gap(task)
        and task.source_route.preferred_source_families[0] in _NAVER_SOURCE_FAMILIES
        for task in tasks
    )
    unbounded_count = sum(
        task.budget.max_queries <= 0
        or task.budget.max_candidates <= 0
        or task.budget.max_fetches <= 0
        for task in tasks
    )
    missing_query_count = sum(not task.query_intent.literal_queries for task in tasks)
    critical = {
        "empty_question": empty_question_count,
        "empty_accepted_predicate": empty_predicate_count,
        "empty_rejection_condition": empty_rejection_count,
        "generic_verify_primitive_task": generic_task_count,
        "official_first_violation": official_first_violation_count,
        "fcf_contract_backlog_naver_first": naver_first_material_count,
        "unbounded_query_or_fetch": unbounded_count,
        "missing_llm_literal_query": missing_query_count,
    }
    return {
        "schema_version": "e2r_question_source_task_audit_v1",
        "status": (
            "QUESTION_SOURCE_TASK_CONTRACT_PASS"
            if tasks and sum(critical.values()) == 0
            else "QUESTION_SOURCE_TASK_CONTRACT_FAIL"
        ),
        "task_count": len(tasks),
        "real_query_provider_task_count": sum(
            task.query_intent.real_provider for task in tasks
        ),
        "fixture_query_provider_task_count": sum(
            task.query_intent.fake_provider for task in tasks
        ),
        "retried_query_task_count": sum(
            task.query_intent.generation_attempt_count > 1 for task in tasks
        ),
        "production_execution_allowed_count": sum(
            task.production_execution_allowed for task in tasks
        ),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "result_hash": hashlib.sha256(
            _stable_json({"tasks": [task.to_dict() for task in tasks]}).encode("utf-8")
        ).hexdigest(),
        "production_runtime_ready": False,
    }


def _query_prompt_payload(
    *,
    draft: PlannerSourceTaskDraft,
    recipe: EvidenceRecipe,
    context: QuestionTaskContext,
) -> Mapping[str, Any]:
    return {
        "schema_version": QUESTION_SOURCE_TASK_SCHEMA_VERSION,
        "target": {
            "target_id": context.target_id,
            "target_name": context.target_name,
            "symbol": context.symbol,
            "target_aliases": list(context.target_aliases),
        },
        "as_of_date": context.as_of_date,
        "current_facts": [fact.to_dict() for fact in context.current_facts],
        "missing_information": list(context.missing_information),
        "existing_queries": list(context.existing_queries),
        "question_contract": {
            "draft_id": draft.draft_id,
            "question_to_answer": draft.question_to_answer,
            "why_material": draft.why_material,
            "semantic_query_intent": draft.query_intent,
            "accepted_predicates": [
                predicate.to_dict() for predicate in recipe.accepted_claim_predicates
            ],
            "required_entities": list(recipe.required_entities),
            "required_values": list(recipe.required_values),
            "required_units": list(recipe.required_units),
            "required_time_scope": list(recipe.required_time_scope),
            "required_target_directness": list(
                recipe.required_target_directness
            ),
            "required_current_lifecycle": list(
                recipe.required_current_lifecycle
            ),
            "counter_questions": list(recipe.counter_questions),
            "rejection_conditions": list(recipe.rejection_conditions),
            "query_intent_constraints": list(recipe.query_intent_constraints),
        },
        "source_route": {
            "preferred_source_families": list(draft.preferred_source_families),
            "fallback_source_families": list(draft.fallback_source_families),
            "preferred_document_types": list(recipe.preferred_document_types),
            "preferred_sections": list(recipe.preferred_sections),
            "discovery_source_families": list(recipe.discovery_sources),
            "forbidden_source_families": list(recipe.forbidden_score_sources),
        },
        "budget": {
            "max_queries": draft.max_queries,
            "max_candidates": draft.max_candidates,
            "max_fetches": draft.max_fetches,
        },
    }


def _query_attempt_prompt_payload(
    base_payload: Mapping[str, Any],
    *,
    attempt: int,
    validation_feedback: Sequence[str],
    rejected_queries: Sequence[str],
) -> Mapping[str, Any]:
    payload = {
        **base_payload,
        "query_generation_attempt": attempt,
        "validation_feedback": list(validation_feedback),
        "rejected_queries": list(rejected_queries),
    }
    input_id = stable_intelligence_id("query-generation-input", payload)
    return {**payload, "input_id": input_id}


def _question_task_from_validated_query(
    *,
    draft: PlannerSourceTaskDraft,
    recipe: EvidenceRecipe,
    context: QuestionTaskContext,
    candidate_event_id: str,
    task_type: str,
    query_intent: QueryIntent,
    test_mode: bool,
) -> QuestionSourceTask:
    acceptance = QuestionAcceptanceContract(
        accepted_predicates=recipe.accepted_claim_predicates,
        required_entities=recipe.required_entities,
        required_values=recipe.required_values,
        required_units=recipe.required_units,
        required_time_scope=recipe.required_time_scope,
        required_target_directness=recipe.required_target_directness,
        required_current_lifecycle=recipe.required_current_lifecycle,
        counter_questions=recipe.counter_questions,
        rejection_conditions=recipe.rejection_conditions,
    )
    source_route = SourceRouteContract(
        preferred_source_families=draft.preferred_source_families,
        fallback_source_families=draft.fallback_source_families,
        preferred_document_types=recipe.preferred_document_types,
        preferred_sections=recipe.preferred_sections,
        discovery_source_families=recipe.discovery_sources,
        forbidden_source_families=recipe.forbidden_score_sources,
    )
    budget = SourceBudget(
        max_queries=draft.max_queries,
        max_candidates=draft.max_candidates,
        max_fetches=draft.max_fetches,
    )
    stop = StopCondition(
        resolution_conditions=_unique_strings(
            (draft.stop_condition, *recipe.stop_conditions)
        ),
        exhaustion_conditions=recipe.source_exhaustion_conditions,
    )
    payload = {
        "context_id": context.context_id,
        "candidate_event_id": candidate_event_id,
        "target_id": context.target_id,
        "as_of_date": context.as_of_date,
        "recipe_id": recipe.recipe_id,
        "question": draft.question_to_answer,
        "query_intent": query_intent.to_dict(),
        "budget": budget.to_dict(),
    }
    return QuestionSourceTask(
        task_id=stable_intelligence_id("QSOURCE", payload),
        context_id=context.context_id,
        candidate_event_id=candidate_event_id,
        target_id=context.target_id,
        symbol=context.symbol,
        company_name=context.target_name,
        as_of_date=context.as_of_date,
        archetype_id=recipe.archetype_id,
        primitive_id=recipe.primitive_id,
        recipe_id=recipe.recipe_id,
        task_type=task_type,
        question_to_answer=draft.question_to_answer,
        why_material=draft.why_material,
        supporting_current_fact_ids=tuple(
            fact.fact_id for fact in context.current_facts
        ),
        missing_information=context.missing_information,
        acceptance_contract=acceptance,
        source_route=source_route,
        query_intent=query_intent,
        budget=budget,
        stop_condition=stop,
        test_only=bool(test_mode or query_intent.fake_provider),
    )


def _validate_draft_recipe_alignment(
    draft: PlannerSourceTaskDraft,
    recipe: EvidenceRecipe,
) -> None:
    if draft.recipe_id != recipe.recipe_id:
        raise ValueError("source-task draft recipe identity mismatch")
    if _is_generic_question(draft.question_to_answer, recipe.primitive_id):
        raise ValueError("generic verify-primitive question is forbidden")
    if _GENERIC_QUERY_RE.search(draft.query_intent) or _primitive_appears_in_query(
        recipe.primitive_id,
        draft.query_intent,
    ):
        raise ValueError("generic or primitive-copy semantic query intent is forbidden")
    allowed_sources = {
        *recipe.preferred_source_families,
        *recipe.discovery_sources,
    }
    if not set(draft.preferred_source_families) <= allowed_sources:
        raise ValueError("source-task draft invents a preferred source family")
    if not set(draft.fallback_source_families) <= allowed_sources:
        raise ValueError("source-task draft invents a fallback source family")
    SourceBudget(
        max_queries=draft.max_queries,
        max_candidates=draft.max_candidates,
        max_fetches=draft.max_fetches,
    )
    SourceRouteContract(
        preferred_source_families=draft.preferred_source_families,
        fallback_source_families=draft.fallback_source_families,
        preferred_document_types=recipe.preferred_document_types,
        preferred_sections=recipe.preferred_sections,
        discovery_source_families=recipe.discovery_sources,
        forbidden_source_families=recipe.forbidden_score_sources,
    )


def _validate_task_type_for_recipe(task_type: str, recipe: EvidenceRecipe) -> None:
    if not str(task_type).strip():
        raise ValueError("question SourceTask task_type is required")
    if recipe.role in {"GUARD", "HARD_BREAK"} and task_type not in {
        "red_team",
        "contradiction_resolution",
        "lifecycle_followup",
    }:
        raise ValueError("guard/hard-break recipe requires a defensive task type")


def _validate_query_time_scope(query: str, *, as_of: date) -> None:
    for match in _ISO_DATE_RE.finditer(query):
        try:
            explicit = date.fromisoformat(match.group(1))
        except ValueError as exc:
            raise ValueError("literal query contains an invalid ISO date") from exc
        if explicit > as_of:
            raise ValueError("literal query contains a future date")
    current_quarter = (as_of.month - 1) // 3 + 1
    for match in _QUARTER_RE.finditer(query):
        year = int(match.group(1))
        quarter = int(next(value for value in match.groups()[1:] if value))
        if (year, quarter) > (as_of.year, current_quarter):
            raise ValueError("literal query contains a future reporting quarter")
    for match in _YEAR_RE.finditer(query):
        if int(match.group(1)) > as_of.year:
            raise ValueError("literal query contains a future year")


def _query_mentions_target(query: str, context: QuestionTaskContext) -> bool:
    normalized_query = _normalize_target_token(query)
    targets = (
        context.target_name,
        context.symbol,
        *context.target_aliases,
    )
    return any(
        normalized and normalized in normalized_query
        for normalized in (_normalize_target_token(item) for item in targets)
    )


def _primitive_appears_in_query(primitive_id: str, query: str) -> bool:
    normalized_query = _normalize_query(query).replace("-", "_").replace(" ", "_")
    normalized_primitive = _normalize_query(primitive_id).replace("-", "_").replace(
        " ", "_"
    )
    return bool(normalized_primitive and normalized_primitive in normalized_query)


def _is_generic_question(question: str, primitive_id: str) -> bool:
    clean = str(question or "").strip()
    if not clean or len(clean) < 12 or _GENERIC_QUESTION_RE.search(clean):
        return True
    normalized_question = _normalize_query(clean).replace("-", "_").replace(" ", "_")
    normalized_primitive = _normalize_query(primitive_id).replace("-", "_").replace(
        " ", "_"
    )
    return normalized_question in {
        normalized_primitive,
        f"verify_{normalized_primitive}",
        f"check_{normalized_primitive}",
    }


def _material_official_gap(task: QuestionSourceTask) -> bool:
    text = f"{task.primitive_id} {task.question_to_answer}".lower()
    return any(token in text for token in ("fcf", "cash flow", "contract", "backlog"))


def _pending_result(
    *,
    input_id: str,
    provider_name: str,
    reason_code: str,
    reason_detail: str,
    prompt_hash: str,
    attempt_count: int,
    response_hash: str | None = None,
    validation_feedback: tuple[str, ...] = (),
    traces: tuple[QueryGenerationTrace, ...] = (),
) -> QuestionTaskPlanningResult:
    preserved_response_hash = response_hash or _sha256(
        _stable_json(
            {
                "response_unavailable": True,
                "reason_code": reason_code,
                "reason_detail": reason_detail,
            }
        )
    )
    return QuestionTaskPlanningResult(
        input_id=input_id,
        status=QuestionTaskPlanningStatus.PENDING.value,
        task=None,
        pending=QuestionTaskPending(
            input_id=input_id,
            reason_code=reason_code,
            reason_detail=reason_detail,
            provider_name=provider_name,
            prompt_hash=prompt_hash,
            response_hash=preserved_response_hash,
            attempt_count=attempt_count,
            validation_feedback=validation_feedback,
        ),
        traces=traces,
    )


def _query_provider_reason_code(exc: Exception) -> str:
    if isinstance(exc, StructuredProviderUnavailable):
        return "QUERY_PROVIDER_UNAVAILABLE"
    if isinstance(exc, StructuredProviderRejected):
        return "QUERY_PROVIDER_REJECTED"
    return "QUERY_PROVIDER_OR_OUTPUT_ERROR"


def _required_text(value: Any, *, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{context} must be a non-empty string")
    return value.strip()


def _strict_string_array(value: Any, *, context: str) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)) or isinstance(value, (str, bytes)):
        raise ValueError(f"{context} must be an array")
    if any(not isinstance(item, str) for item in value):
        raise ValueError(f"{context} items must be strings")
    clean = tuple(item.strip() for item in value)
    _require_unique_nonempty_strings(clean, context=context)
    return clean


def _require_unique_nonempty_strings(values: Sequence[str], *, context: str) -> None:
    if any(not isinstance(item, str) or not item.strip() for item in values):
        raise ValueError(f"{context} contains an empty or non-string value")
    if len({item.strip() for item in values}) != len(values):
        raise ValueError(f"{context} contains duplicates")


def _unique_strings(values: Iterable[Any]) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(str(item).strip() for item in values if str(item).strip())
    )


def _normalize_query(value: str) -> str:
    clean = re.sub(r"[^0-9a-z가-힣]+", " ", value.casefold())
    return re.sub(r"\s+", " ", clean).strip()


def _normalize_target_token(value: str) -> str:
    return re.sub(r"[^0-9a-z가-힣]", "", str(value).casefold())


def _prompt_payload(prompt: str) -> Mapping[str, Any]:
    for block in reversed(prompt.split("\n\n")):
        try:
            payload = json.loads(block)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, Mapping):
            return payload
    raise ValueError("fixture query provider could not read prompt payload")


def _stable_json(value: Mapping[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _is_sha256(value: str) -> bool:
    return re.fullmatch(r"[0-9a-f]{64}", value) is not None


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
    "QUERY_INTENT_OUTPUT_SCHEMA",
    "QUESTION_SOURCE_TASK_SCHEMA_VERSION",
    "CodexQuestionQueryProvider",
    "FixtureQuestionQueryProvider",
    "QueryGenerationTrace",
    "QueryGeneratorKind",
    "QueryIntent",
    "QuestionAcceptanceContract",
    "QuestionQueryProvider",
    "QuestionSourceTask",
    "QuestionTaskContext",
    "QuestionTaskPending",
    "QuestionTaskPlanningResult",
    "QuestionTaskPlanningStatus",
    "SourceBudget",
    "SourceRouteContract",
    "StopCondition",
    "audit_question_source_tasks",
    "build_codex_question_query_provider",
    "build_question_query_prompt",
    "compile_question_task_context",
    "decode_query_generation_output",
    "plan_question_source_task",
    "validate_llm_literal_queries",
]
