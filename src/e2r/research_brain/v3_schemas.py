"""Research Brain v3 production-shadow schemas.

v3 keeps the same hard boundary as Evidence OS v2:

* Research Brain may plan and route.
* SourceTask execution must create source-backed Evidence OS rows.
* Score and Stage come from deterministic scorer + StageCourt only.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Mapping, Sequence

from e2r.research_brain.v2_schemas import CandidateEventV2, LLMPlannerOutputV2, _json_safe


class SourceTaskExecutionStatusV3(str, Enum):
    FETCHED = "FETCHED"
    PARSED = "PARSED"
    EVIDENCE_OS_ACCEPTED = "EVIDENCE_OS_ACCEPTED"
    NO_EVIDENCE_FOUND = "NO_EVIDENCE_FOUND"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    BUDGET_EXHAUSTED = "BUDGET_EXHAUSTED"
    REJECTED_BY_POLICY = "REJECTED_BY_POLICY"


class ScoreValidStatusV3(str, Enum):
    FINAL = "FINAL"
    FINAL_WITH_NONMATERIAL_GAPS = "FINAL_WITH_NONMATERIAL_GAPS"
    PENDING_MATERIAL_GAPS = "PENDING_MATERIAL_GAPS"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    INVALID_EVIDENCE = "INVALID_EVIDENCE"
    PENDING_EVIDENCE_OS_CLAIMS = "PENDING_EVIDENCE_OS_CLAIMS"


class OperationalMode(str, Enum):
    RESEARCH_BACKFILL = "research_backfill"
    PRODUCTION_DAILY = "production_daily"
    TEST = "test"


@dataclass(frozen=True)
class SourceTaskExecutionV3:
    task_id: str
    source_task: Mapping[str, Any]
    status: str
    fetched_document_ids: tuple[str, ...] = ()
    evidence_anchor_ids: tuple[str, ...] = ()
    raw_assertion_ids: tuple[str, ...] = ()
    adjudicated_claim_ids: tuple[str, ...] = ()
    accepted_claim_ids: tuple[str, ...] = ()
    rejected_claim_ids: tuple[str, ...] = ()
    not_eligible_reasons: tuple[str, ...] = ()
    provider_errors: tuple[str, ...] = ()
    budget_used: Mapping[str, int] = field(default_factory=dict)
    stop_reason: str = ""

    def __post_init__(self) -> None:
        if not self.task_id.strip():
            raise ValueError("task_id must be non-empty")
        SourceTaskExecutionStatusV3(self.status)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class PlannerRunV3:
    event: CandidateEventV2
    provider_name: str
    real_provider_exercised: bool
    fake_provider_used: bool
    output: LLMPlannerOutputV2 | None = None
    provider_error: str | None = None
    rejected_by_validator: bool = False

    @property
    def provider_failed(self) -> bool:
        return self.output is None or bool(self.provider_error) or self.rejected_by_validator

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["event"] = self.event.to_dict()
        payload["output"] = self.output.to_dict() if self.output else None
        return _json_safe(payload)


@dataclass(frozen=True)
class ScoreIntervalV3:
    lower: float
    upper: float

    def __post_init__(self) -> None:
        if self.lower < 0 or self.upper < 0:
            raise ValueError("score interval cannot be negative")
        if self.upper < self.lower:
            raise ValueError("score interval upper must be >= lower")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class DailyWatchlistItemV3:
    symbol: str
    company_name: str
    candidate_event_id: str
    event_type: str
    event_summary: str
    primary_archetype: str | None
    secondary_archetypes: tuple[str, ...] = ()
    research_memory_cards_used: tuple[str, ...] = ()
    trigger_priority_score: float | None = None
    verified_score: float | None = None
    provisional_score: float | None = None
    score_interval_lower: float | None = None
    score_interval_upper: float | None = None
    score_valid_status: str = ScoreValidStatusV3.PENDING_EVIDENCE_OS_CLAIMS.value
    base_stage: str = "0"
    investigation_status: str = "PENDING"
    transition_overlay: str = "NONE"
    accepted_claim_ids: tuple[str, ...] = ()
    score_contribution_ids: tuple[str, ...] = ()
    failed_stage_gates: tuple[str, ...] = ()
    green_blockers: tuple[str, ...] = ()
    red_team_checks: tuple[str, ...] = ()
    source_task_status_summary: Mapping[str, int] = field(default_factory=dict)
    follow_up_tasks: tuple[Mapping[str, Any], ...] = ()
    do_not_promote_reasons: tuple[str, ...] = ()
    stage_court_trace: Mapping[str, Any] = field(default_factory=dict)
    operator_notes: str = ""

    def __post_init__(self) -> None:
        ScoreValidStatusV3(self.score_valid_status)
        if self.verified_score is not None and not self.accepted_claim_ids:
            raise ValueError("verified_score requires accepted_claim_ids")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class OperationalModePreset:
    mode: OperationalMode
    max_results_per_query: int
    top_results: int | None
    retry_max: int | None
    max_fetches_per_task: int | None
    general_web_fallback_allowed: bool
    fake_provider_allowed: bool
    production_readiness_allowed: bool

    def validate(self) -> None:
        if self.mode == OperationalMode.PRODUCTION_DAILY:
            if self.top_results is None:
                raise ValueError("production daily preset forbids top_results=None")
            if self.retry_max is None:
                raise ValueError("production daily preset forbids retry_max=None")
            if self.max_fetches_per_task is None:
                raise ValueError("production daily preset requires max_fetches_per_task")
            if self.fake_provider_allowed:
                raise ValueError("production daily preset forbids fake provider")
        if self.max_results_per_query <= 0:
            raise ValueError("max_results_per_query must be positive")
        if self.top_results is not None and self.top_results <= 0:
            raise ValueError("top_results must be positive when provided")
        if self.retry_max is not None and self.retry_max < 0:
            raise ValueError("retry_max cannot be negative")
        if self.max_fetches_per_task is not None and self.max_fetches_per_task <= 0:
            raise ValueError("max_fetches_per_task must be positive when provided")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


def research_backfill_preset() -> OperationalModePreset:
    preset = OperationalModePreset(
        mode=OperationalMode.RESEARCH_BACKFILL,
        max_results_per_query=100,
        top_results=None,
        retry_max=None,
        max_fetches_per_task=None,
        general_web_fallback_allowed=True,
        fake_provider_allowed=False,
        production_readiness_allowed=False,
    )
    return preset


def production_daily_preset() -> OperationalModePreset:
    preset = OperationalModePreset(
        mode=OperationalMode.PRODUCTION_DAILY,
        max_results_per_query=100,
        top_results=20,
        retry_max=2,
        max_fetches_per_task=5,
        general_web_fallback_allowed=False,
        fake_provider_allowed=False,
        production_readiness_allowed=True,
    )
    preset.validate()
    return preset


def test_preset() -> OperationalModePreset:
    preset = OperationalModePreset(
        mode=OperationalMode.TEST,
        max_results_per_query=20,
        top_results=5,
        retry_max=1,
        max_fetches_per_task=3,
        general_web_fallback_allowed=False,
        fake_provider_allowed=True,
        production_readiness_allowed=False,
    )
    preset.validate()
    return preset


__all__ = [
    "DailyWatchlistItemV3",
    "OperationalMode",
    "OperationalModePreset",
    "PlannerRunV3",
    "ScoreIntervalV3",
    "ScoreValidStatusV3",
    "SourceTaskExecutionStatusV3",
    "SourceTaskExecutionV3",
    "production_daily_preset",
    "research_backfill_preset",
    "test_preset",
]
