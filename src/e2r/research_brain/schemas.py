"""Schemas for Research Brain v1.

Research Brain is a planning layer.  These schemas intentionally do not expose
score, stage, accepted-claim, or eligibility fields as writable planner output.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from datetime import date
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence


RESEARCH_MEMORY_SCHEMA_VERSION = "research_memory_v1"


class SourceQualityClass(str, Enum):
    A_URL_BACKED_REPLAY_READY = "A_URL_BACKED_REPLAY_READY"
    B_URL_BACKED_REPAIR_NEEDED = "B_URL_BACKED_REPAIR_NEEDED"
    C_SOURCE_PROXY_ONTOLOGY_ONLY = "C_SOURCE_PROXY_ONTOLOGY_ONLY"
    D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK = "D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK"
    E_INVALID_OR_DUPLICATE = "E_INVALID_OR_DUPLICATE"


class MemoryType(str, Enum):
    PRIMITIVE_SUCCESS_CASE = "primitive_success_case"
    PRIMITIVE_FAILURE_CASE = "primitive_failure_case"
    PRIMITIVE_PARTIAL_CASE = "primitive_partial_case"
    GREEN_BLOCKER = "green_blocker"
    YELLOW_BLOCKER = "yellow_blocker"
    STAGE2_ACTIONABLE_UNLOCK = "stage2_actionable_unlock"
    STAGE2_WATCH_CAP = "stage2_watch_cap"
    FALSE_POSITIVE_PATTERN = "false_positive_pattern"
    COUNTEREXAMPLE = "counterexample"
    FOUR_B_WATCH_CONDITION = "4b_watch_condition"
    FOUR_B_LATE_PHASE_CONDITION = "4b_late_phase_condition"
    FOUR_C_THESIS_BREAK_CONDITION = "4c_thesis_break_condition"
    HARD_BREAK_PATTERN = "hard_break_pattern"
    LIFECYCLE_RULE = "lifecycle_rule"
    SOURCE_ROUTE_PATTERN = "source_route_pattern"
    SOURCE_FAMILY_RELIABILITY = "source_family_reliability"
    SOURCE_GAP = "source_gap"
    QUERY_SUCCESS_PATTERN = "query_success_pattern"
    QUERY_FAILURE_PATTERN = "query_failure_pattern"
    EVIDENCE_CONTRACT_CANDIDATE = "evidence_contract_candidate"
    SOURCE_QUORUM_HINT = "source_quorum_hint"
    REPLAY_FIXTURE_CANDIDATE = "replay_fixture_candidate"
    PRODUCTION_FIXTURE_CANDIDATE = "production_fixture_candidate"
    ONTOLOGY_ONLY_RULE_CANDIDATE = "ontology_only_rule_candidate"
    SCORE_WEIGHT_SUPPORT = "score_weight_support"
    SCORE_WEIGHT_COUNTEREXAMPLE = "score_weight_counterexample"


class CandidateEventType(str, Enum):
    SUPPLY_CONTRACT = "supply_contract"
    FACILITY_INVESTMENT = "facility_investment"
    EARNINGS_SURPRISE = "earnings_surprise"
    REVISION_UP = "revision_up"
    REPORT_RADAR = "report_radar"
    RELATIVE_STRENGTH = "relative_strength"
    RISK_EVENT = "risk_event"
    IR_UPDATE = "ir_update"
    NEWS_DISCOVERY = "news_discovery"
    OTHER = "other"


class SourceTaskType(str, Enum):
    POSITIVE_VERIFY = "positive_verify"
    GREEN_CLOSURE = "green_closure"
    RED_TEAM = "red_team"
    SOURCE_REPAIR = "source_repair"
    LIFECYCLE_FOLLOWUP = "lifecycle_followup"
    CONTRADICTION_RESOLUTION = "contradiction_resolution"


@dataclass(frozen=True)
class UsagePolicy:
    allowed_for_runtime_planning: bool = True
    allowed_for_evidence_extraction_prompt: bool = False
    allowed_for_score_contribution: bool = False
    allowed_for_replay_fixture: bool = False
    allowed_for_ontology: bool = True
    allowed_for_query_planning: bool = True
    allowed_for_red_team_planning: bool = True


@dataclass(frozen=True)
class LeakageControls:
    contains_future_price_outcome: bool = False
    contains_future_stage_label: bool = False
    may_be_seen_by_runtime_llm: bool = False
    may_be_seen_by_extractor_llm: bool = False
    may_be_seen_by_planner_llm_as_pattern_summary: bool = True


@dataclass(frozen=True)
class PriceOutcome:
    mfe_30d_pct: float | None = None
    mae_30d_pct: float | None = None
    mfe_90d_pct: float | None = None
    mae_90d_pct: float | None = None
    mfe_180d_pct: float | None = None
    mae_180d_pct: float | None = None
    post_peak_drawdown_pct: float | None = None
    corporate_action_contaminated: bool = False
    future_outcome_zone: bool = False


@dataclass(frozen=True)
class ArtifactInventoryRow:
    path: str
    sha256: str
    artifact_type: str
    size_bytes: int
    modified_time: float | None = None
    schema_family: str | None = None
    detected_canonical_archetype_id: str | None = None
    detected_large_sector_id: str | None = None
    detected_round: str | None = None
    detected_loop: int | None = None
    row_block_count: int = 0
    jsonl_row_count: int = 0
    table_row_count: int = 0
    evidence_url_count: int = 0
    source_proxy_count: int = 0
    evidence_url_pending_count: int = 0
    calibration_usable_count: int = 0
    duplicate_count: int = 0
    parse_error_count: int = 0
    parse_errors: tuple[str, ...] = ()


@dataclass(frozen=True)
class RawResearchRow:
    source_artifact_path: str
    source_artifact_sha256: str
    source_artifact_type: str
    source_line_or_span: str
    row_kind: str
    data: Mapping[str, Any]
    text: str = ""

    def stable_payload(self) -> Mapping[str, Any]:
        return {
            "path": self.source_artifact_path,
            "sha256": self.source_artifact_sha256,
            "span": self.source_line_or_span,
            "row_kind": self.row_kind,
            "data": _json_safe(self.data),
            "text": self.text[:2_000],
        }


@dataclass(frozen=True)
class ResearchMemoryRecord:
    record_id: str
    source_artifact_path: str
    source_artifact_sha256: str
    source_artifact_type: str
    source_line_or_span: str
    memory_type: str
    canonical_archetype_id: str | None = None
    large_sector_id: str | None = None
    fine_archetype_id: str | None = None
    research_session: str | None = None
    mode: str | None = None
    round: str | None = None
    loop: int | None = None
    row_type: str | None = None
    case_id: str | None = None
    trigger_id: str | None = None
    symbol: str | None = None
    company_name: str | None = None
    trigger_type: str | None = None
    trigger_date: str | None = None
    entry_date: str | None = None
    positive_or_counterexample: str = "unknown"
    stage_before: str | None = None
    stage_after: str | None = None
    expected_stage_effect: str | None = None
    primitive_ids: tuple[str, ...] = ()
    required_bridges: tuple[str, ...] = ()
    missing_bridges: tuple[str, ...] = ()
    green_blockers: tuple[str, ...] = ()
    guard_primitives: tuple[str, ...] = ()
    hard_break_primitives: tuple[str, ...] = ()
    false_positive_patterns: tuple[str, ...] = ()
    source_family: str | None = None
    source_url: str | None = None
    source_quality: str = "unknown"
    source_quality_class: str = SourceQualityClass.C_SOURCE_PROXY_ONTOLOGY_ONLY.value
    evidence_url_status: str = "not_applicable"
    source_proxy_only: bool = False
    evidence_url_pending: bool = False
    production_ready_evidence: bool = False
    fixture_usable: bool = False
    ontology_usable: bool = True
    runtime_score_eligible: bool = False
    free_source_route_hints: tuple[str, ...] = ()
    preferred_source_classes: tuple[str, ...] = ()
    fallback_source_classes: tuple[str, ...] = ()
    forbidden_source_classes: tuple[str, ...] = ()
    query_pattern_hints: tuple[str, ...] = ()
    bad_query_patterns: tuple[str, ...] = ()
    price_outcome: PriceOutcome = field(default_factory=PriceOutcome)
    usage_policy: UsagePolicy = field(default_factory=UsagePolicy)
    leakage_controls: LeakageControls = field(default_factory=LeakageControls)
    dedupe_key: str = ""
    confidence: str = "medium"
    notes: str = ""
    schema_version: str = RESEARCH_MEMORY_SCHEMA_VERSION

    def __post_init__(self) -> None:
        forbidden_score = {
            "score",
            "stage",
            "current_score_eligible",
            "hard_break_final",
            "verified_final",
            "accepted_claim_final",
        }
        if self.memory_type not in {item.value for item in MemoryType}:
            raise ValueError(f"unknown memory_type: {self.memory_type}")
        if self.source_quality_class not in {item.value for item in SourceQualityClass}:
            raise ValueError(f"unknown source_quality_class: {self.source_quality_class}")
        payload = asdict(self)
        if forbidden_score & set(payload):
            raise ValueError("ResearchMemoryRecord contains forbidden scoring fields")
        if self.runtime_score_eligible:
            raise ValueError("ResearchMemoryRecord cannot be runtime score eligible")
        if self.usage_policy.allowed_for_score_contribution:
            raise ValueError("Research memory cannot be allowed for score contribution")
        if self.usage_policy.allowed_for_evidence_extraction_prompt:
            raise ValueError("Research memory cannot be shown to extraction prompt")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "ResearchMemoryRecord":
        payload = dict(data)
        if isinstance(payload.get("price_outcome"), Mapping):
            payload["price_outcome"] = PriceOutcome(**payload["price_outcome"])
        if isinstance(payload.get("usage_policy"), Mapping):
            payload["usage_policy"] = UsagePolicy(**payload["usage_policy"])
        if isinstance(payload.get("leakage_controls"), Mapping):
            payload["leakage_controls"] = LeakageControls(**payload["leakage_controls"])
        for key in (
            "primitive_ids",
            "required_bridges",
            "missing_bridges",
            "green_blockers",
            "guard_primitives",
            "hard_break_primitives",
            "false_positive_patterns",
            "free_source_route_hints",
            "preferred_source_classes",
            "fallback_source_classes",
            "forbidden_source_classes",
            "query_pattern_hints",
            "bad_query_patterns",
        ):
            if isinstance(payload.get(key), list):
                payload[key] = tuple(payload[key])
        return cls(**payload)


@dataclass(frozen=True)
class CandidateEvent:
    candidate_event_id: str
    symbol: str
    company_name: str
    event_date: str
    event_type: str
    source_family: str
    source_id: str
    magnitude: Mapping[str, Any] = field(default_factory=dict)
    freshness_days: int = 0
    candidate_reason: str = ""
    initial_evidence_ids: tuple[str, ...] = ()
    structured_fields: Mapping[str, Any] = field(default_factory=dict)
    price_context: Mapping[str, Any] = field(default_factory=dict)
    eligible_for_research_brain: bool = True

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class SourceTask:
    task_id: str
    candidate_event_id: str
    symbol: str
    company_name: str
    archetype_id: str
    primitive_gap: str
    task_type: str
    preferred_source_classes: tuple[str, ...]
    fallback_source_classes: tuple[str, ...] = ()
    forbidden_source_classes: tuple[str, ...] = ("unbounded_general_search",)
    allowed_domains: tuple[str, ...] = ()
    date_window: Mapping[str, Any] = field(default_factory=dict)
    max_queries: int = 3
    max_candidates: int = 20
    max_fetches: int = 5
    stop_condition: Mapping[str, Any] = field(
        default_factory=lambda: {"accepted_claim_count": 1, "counter_claim_check_done": True}
    )
    llm_query_allowed: bool = True
    general_search_allowed: bool = False
    reason_from_memory: str = ""
    memory_record_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.task_type not in {item.value for item in SourceTaskType}:
            raise ValueError(f"unknown task_type: {self.task_type}")
        for name in ("max_queries", "max_candidates", "max_fetches"):
            value = getattr(self, name)
            if value is None or value <= 0:
                raise ValueError(f"{name} must be a positive bounded integer")
        if not self.preferred_source_classes:
            raise ValueError("preferred_source_classes is required")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ResearchBrainPlan:
    primary_archetype_hypothesis: str
    secondary_archetype_hypotheses: tuple[str, ...]
    positive_thesis: str
    counter_thesis: str
    recalled_memory_patterns: tuple[str, ...]
    must_verify_primitives: tuple[str, ...]
    green_blockers_to_close: tuple[str, ...]
    red_team_checks: tuple[str, ...]
    source_tasks: tuple[SourceTask, ...]
    query_suggestions: tuple[str, ...] = ()
    do_not_promote_reasons: tuple[str, ...] = ()
    planning_confidence: str = "medium"

    def __post_init__(self) -> None:
        forbidden = {
            "score",
            "stage",
            "current_score_eligible",
            "hard_break_final",
            "verified_final",
            "accepted_claim_final",
        }
        if forbidden & set(asdict(self)):
            raise ValueError("ResearchBrainPlan cannot expose score/stage finalization fields")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ArchetypeMemoryProfile:
    canonical_archetype_id: str
    large_sector_id: str | None
    memory_record_count: int
    url_backed_count: int
    source_proxy_count: int
    price_path_only_count: int
    production_fixture_count: int
    ontology_only_count: int
    positive_patterns: tuple[str, ...] = ()
    failure_patterns: tuple[str, ...] = ()
    false_positive_patterns: tuple[str, ...] = ()
    green_blockers: tuple[str, ...] = ()
    yellow_blockers: tuple[str, ...] = ()
    stage2_unlock_conditions: tuple[str, ...] = ()
    stage2_cap_conditions: tuple[str, ...] = ()
    four_b_watch_conditions: tuple[str, ...] = ()
    four_c_thesis_break_conditions: tuple[str, ...] = ()
    required_primitives_observed: tuple[str, ...] = ()
    optional_primitives_observed: tuple[str, ...] = ()
    guard_primitives_observed: tuple[str, ...] = ()
    hard_break_primitives_observed: tuple[str, ...] = ()
    source_routes: tuple[str, ...] = ()
    source_family_reliability: tuple[str, ...] = ()
    query_pattern_hints: tuple[str, ...] = ()
    bad_query_patterns: tuple[str, ...] = ()
    fixture_status: Mapping[str, bool] = field(default_factory=dict)
    source_gap_summary: tuple[str, ...] = ()
    runtime_usage_policy: str = "planning_only"

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


def deterministic_id(prefix: str, payload: Mapping[str, Any] | Sequence[Any] | str) -> str:
    text = json.dumps(_json_safe(payload), ensure_ascii=False, sort_keys=True) if not isinstance(payload, str) else payload
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:24]
    return f"{prefix}-{digest}"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _json_safe(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, tuple):
        return [_json_safe(item) for item in value]
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if hasattr(value, "__dataclass_fields__"):
        return _json_safe(asdict(value))
    return value


__all__ = [
    "ArchetypeMemoryProfile",
    "ArtifactInventoryRow",
    "CandidateEvent",
    "CandidateEventType",
    "LeakageControls",
    "MemoryType",
    "PriceOutcome",
    "RESEARCH_MEMORY_SCHEMA_VERSION",
    "RawResearchRow",
    "ResearchBrainPlan",
    "ResearchMemoryRecord",
    "SourceQualityClass",
    "SourceTask",
    "SourceTaskType",
    "UsagePolicy",
    "deterministic_id",
    "sha256_file",
]
