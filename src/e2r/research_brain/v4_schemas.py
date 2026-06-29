"""Research Brain v4 production-shadow schemas.

v4 is the first path that may be called production-ready, but only when the
reports prove real planner, real source acquisition, real extraction, and real
deterministic scoring all ran without critical audit findings.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Mapping, Sequence

from e2r.research_brain.v2_schemas import CandidateEventV2, LLMPlannerOutputV2, _json_safe


class PlannerProviderModeV4(str, Enum):
    REAL = "real"
    FAKE = "fake"
    NONE = "none"


class SourceAcquisitionModeV4(str, Enum):
    FROZEN_REAL_SOURCE_SNAPSHOT = "frozen_real_source_snapshot"
    LIVE_OFFICIAL_ONLY = "live_official_only"
    LIVE_FULL_BOUNDED = "live_full_bounded"
    TEST_FAKE = "test_fake"


class SourceAcquisitionStatusV4(str, Enum):
    FETCHED = "FETCHED"
    PARSED = "PARSED"
    NO_EVIDENCE_FOUND = "NO_EVIDENCE_FOUND"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    REJECTED_BY_POLICY = "REJECTED_BY_POLICY"
    BUDGET_EXHAUSTED = "BUDGET_EXHAUSTED"


class SourceTaskExecutionStatusV4(str, Enum):
    EVIDENCE_OS_ACCEPTED = "EVIDENCE_OS_ACCEPTED"
    NO_EVIDENCE_FOUND = "NO_EVIDENCE_FOUND"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    REJECTED_BY_POLICY = "REJECTED_BY_POLICY"
    BUDGET_EXHAUSTED = "BUDGET_EXHAUSTED"


class ScoreValidStatusV4(str, Enum):
    FINAL = "FINAL"
    FINAL_WITH_NONMATERIAL_GAPS = "FINAL_WITH_NONMATERIAL_GAPS"
    PENDING_MATERIAL_GAPS = "PENDING_MATERIAL_GAPS"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    INVALID_EVIDENCE = "INVALID_EVIDENCE"
    PENDING_EVIDENCE_OS_CLAIMS = "PENDING_EVIDENCE_OS_CLAIMS"


@dataclass(frozen=True)
class PlannerRunV4:
    event: CandidateEventV2
    provider_name: str
    provider_mode: str
    real_provider_exercised: bool
    real_provider_success: bool
    fake_provider_used: bool
    output: LLMPlannerOutputV2 | None = None
    provider_error: str | None = None
    rejected_by_validator: bool = False
    planner_output_score_stage_key_count: int = 0
    r13_invalid_primary_rejected: bool = False
    model: str | None = None
    endpoint: str | None = None

    @property
    def provider_failed(self) -> bool:
        return self.output is None or bool(self.provider_error) or self.rejected_by_validator

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["event"] = self.event.to_dict()
        payload["output"] = self.output.to_dict() if self.output else None
        return _json_safe(payload)


@dataclass(frozen=True)
class SourceAcquisitionResultV4:
    task_id: str
    source_class: str
    provider_name: str
    status: str
    documents: tuple[Any, ...] = ()
    anchors: tuple[Any, ...] = ()
    document_text_by_id: Mapping[str, str] = field(default_factory=dict)
    fetched_document_ids: tuple[str, ...] = ()
    document_urls: tuple[str, ...] = ()
    document_hashes: tuple[str, ...] = ()
    anchor_ids: tuple[str, ...] = ()
    provider_errors: tuple[str, ...] = ()
    budget_used: Mapping[str, int] = field(default_factory=dict)
    stop_reason: str = ""

    def __post_init__(self) -> None:
        SourceAcquisitionStatusV4(self.status)

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["documents"] = [asdict(item) if hasattr(item, "__dataclass_fields__") else item for item in self.documents]
        payload["anchors"] = [asdict(item) if hasattr(item, "__dataclass_fields__") else item for item in self.anchors]
        return _json_safe(payload)


@dataclass(frozen=True)
class SourceTaskExecutionV4:
    task_id: str
    source_task: Mapping[str, Any]
    status: str
    fetched_document_ids: tuple[str, ...] = ()
    document_urls: tuple[str, ...] = ()
    document_hashes: tuple[str, ...] = ()
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
        SourceTaskExecutionStatusV4(self.status)
        if self.accepted_claim_ids and not self.fetched_document_ids:
            raise ValueError("accepted claims require real fetched document ids")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class DailyWatchlistItemV4:
    symbol: str
    company_name: str
    candidate_event_id: str
    event_type: str
    event_summary: str
    event_source: str
    primary_archetype: str | None
    secondary_archetypes: tuple[str, ...] = ()
    planner_provider: str = ""
    planner_real_provider: bool = False
    research_memory_cards_used: tuple[str, ...] = ()
    source_tasks: tuple[Mapping[str, Any], ...] = ()
    source_task_executions: tuple[Mapping[str, Any], ...] = ()
    accepted_claim_ids: tuple[str, ...] = ()
    top_supporting_claims: tuple[str, ...] = ()
    score_contribution_ids: tuple[str, ...] = ()
    trigger_priority_score: float | None = None
    verified_score: float | None = None
    provisional_score: float | None = None
    score_interval_lower: float | None = None
    score_interval_upper: float | None = None
    score_valid_status: str = ScoreValidStatusV4.PENDING_EVIDENCE_OS_CLAIMS.value
    base_stage: str = "0"
    investigation_status: str = "PENDING"
    transition_overlay: str = "NONE"
    failed_stage_gates: tuple[str, ...] = ()
    green_blockers: tuple[str, ...] = ()
    red_team_checks: tuple[str, ...] = ()
    do_not_promote_reasons: tuple[str, ...] = ()
    follow_up_tasks: tuple[Mapping[str, Any], ...] = ()
    operator_notes: str = ""
    stage_court_trace: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        ScoreValidStatusV4(self.score_valid_status)
        if self.verified_score is not None and not self.accepted_claim_ids:
            raise ValueError("verified_score requires Evidence OS accepted claims")
        if self.verified_score is not None and not self.score_contribution_ids:
            raise ValueError("verified_score requires deterministic score contribution ids")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ProductionShadowV4Config:
    as_of_date: str
    planner_provider: str = PlannerProviderModeV4.REAL.value
    source_acquisition: str = SourceAcquisitionModeV4.FROZEN_REAL_SOURCE_SNAPSHOT.value
    universe_limit: int = 40
    planner_success_limit: int = 10
    max_fetches_per_task: int = 3
    top_results: int = 20
    retry_max: int = 2
    fake_provider_allowed: bool = False

    def validate(self) -> None:
        if self.top_results is None:
            raise ValueError("v4 production shadow forbids top_results=None")
        if self.retry_max is None:
            raise ValueError("v4 production shadow forbids retry_max=None")
        if self.max_fetches_per_task <= 0:
            raise ValueError("v4 production shadow requires bounded max_fetches_per_task")
        if self.planner_provider == PlannerProviderModeV4.FAKE.value and not self.fake_provider_allowed:
            raise ValueError("fake planner provider is not allowed for production shadow")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


def clean_count_summary(mapping: Mapping[str, int]) -> dict[str, int]:
    return {str(key): int(value) for key, value in sorted(mapping.items())}


__all__ = [
    "DailyWatchlistItemV4",
    "PlannerProviderModeV4",
    "PlannerRunV4",
    "ProductionShadowV4Config",
    "ScoreValidStatusV4",
    "SourceAcquisitionModeV4",
    "SourceAcquisitionResultV4",
    "SourceAcquisitionStatusV4",
    "SourceTaskExecutionStatusV4",
    "SourceTaskExecutionV4",
    "clean_count_summary",
]
