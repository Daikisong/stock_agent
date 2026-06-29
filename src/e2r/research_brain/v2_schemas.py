"""Research Brain v2 schemas.

Research Brain v2 remains a planning and orchestration layer.  It can route a
candidate event, plan source tasks, and report Evidence OS handoff state, but it
does not directly write score, stage, feature input, or score contribution
objects.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Mapping, Sequence

from e2r.research_brain.schemas import SourceTask, deterministic_id


class SourceQualityV2(str, Enum):
    A2_EVIDENCE_OS_REPLAY_VERIFIED = "A2_EVIDENCE_OS_REPLAY_VERIFIED"
    A1_URL_BACKED_ANCHOR_PENDING = "A1_URL_BACKED_ANCHOR_PENDING"
    A0_URL_STRING_ONLY = "A0_URL_STRING_ONLY"
    B_URL_REPAIR_NEEDED = "B_URL_REPAIR_NEEDED"
    C_SOURCE_PROXY_ONTOLOGY_ONLY = "C_SOURCE_PROXY_ONTOLOGY_ONLY"
    D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK = "D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK"
    E_INVALID_OR_DUPLICATE = "E_INVALID_OR_DUPLICATE"


class RouterConfidence(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class SourceTaskExecutionStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    FETCHED = "FETCHED"
    PARSED = "PARSED"
    EVIDENCE_OS_ACCEPTED = "EVIDENCE_OS_ACCEPTED"
    NO_EVIDENCE_FOUND = "NO_EVIDENCE_FOUND"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    BUDGET_EXHAUSTED = "BUDGET_EXHAUSTED"


FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS = {
    "score",
    "stage",
    "current_score_eligible",
    "hard_break_final",
    "verified_final",
    "accepted_claim_final",
    "feature_input",
    "score_contribution",
}


@dataclass(frozen=True)
class EventMagnitudeV2:
    contract_to_sales_pct: float | None = None
    facility_to_marketcap_pct: float | None = None
    eps_revision_pct: float | None = None
    opm_change_pctp: float | None = None
    fcf_change: float | None = None
    relative_strength_rank: float | None = None
    volume_spike_ratio: float | None = None


@dataclass(frozen=True)
class CandidateEventV2:
    candidate_event_id: str
    symbol: str
    company_name: str
    event_date: str
    detected_at: str
    source_family: str
    source_id: str
    event_type: str
    raw_reason_codes: tuple[str, ...] = ()
    primary_disclosure_type: str | None = None
    event_title: str = ""
    event_summary: str = ""
    magnitude: EventMagnitudeV2 = field(default_factory=EventMagnitudeV2)
    event_freshness_days: int = 0
    issuer_directness: str = "UNKNOWN"
    initial_evidence_document_ids: tuple[str, ...] = ()
    structured_payload: Mapping[str, Any] = field(default_factory=dict)
    price_context: Mapping[str, Any] = field(default_factory=dict)
    research_brain_eligible: bool = True

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ArchetypeMemoryCard:
    archetype_id: str
    large_sector_id: str | None
    version: str = "v2"
    generated_from_record_count: int = 0
    quality_breakdown: Mapping[str, int] = field(default_factory=dict)
    canonical_mechanism: str = ""
    stage2_unlocks: tuple[str, ...] = ()
    yellow_unlocks: tuple[str, ...] = ()
    green_unlocks: tuple[str, ...] = ()
    green_blockers: tuple[str, ...] = ()
    stage2_caps: tuple[str, ...] = ()
    false_positive_patterns: tuple[str, ...] = ()
    four_b_watch_patterns: tuple[str, ...] = ()
    four_c_hard_break_patterns: tuple[str, ...] = ()
    required_primitives: tuple[str, ...] = ()
    alternative_primitives: tuple[str, ...] = ()
    source_route_by_primitive: Mapping[str, tuple[str, ...]] = field(default_factory=dict)
    source_quorum_by_primitive: Mapping[str, str] = field(default_factory=dict)
    do_not_promote_rules: tuple[str, ...] = ()
    lifecycle_rules: tuple[str, ...] = ()
    query_intent_patterns: tuple[str, ...] = ()
    bad_query_patterns: tuple[str, ...] = ()
    representative_url_backed_fixture_ids: tuple[str, ...] = ()
    representative_source_proxy_ontology_ids: tuple[str, ...] = ()
    source_gaps: tuple[str, ...] = ()
    confidence: str = "MEDIUM"
    runtime_usage_policy: str = "PLANNING_ONLY"

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ArchetypeRouteCandidate:
    archetype_id: str
    probability_or_score: float
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ArchetypeRouteResult:
    primary_archetype: str | None
    top_k_archetypes: tuple[ArchetypeRouteCandidate, ...]
    router_confidence: str
    status: str
    why_not_other_top_archetypes: tuple[str, ...] = ()
    required_disambiguation_tasks: tuple[str, ...] = ()
    secondary_overlays: tuple[str, ...] = ()
    r13_primary_allowed: bool = False

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class SourceTaskExecution:
    task_id: str
    status: str
    attempted_sources: tuple[str, ...] = ()
    fetched_document_ids: tuple[str, ...] = ()
    parsed_anchor_count: int = 0
    accepted_claim_ids: tuple[str, ...] = ()
    rejected_claim_ids: tuple[str, ...] = ()
    stop_reason: str = ""
    provider_error: str | None = None
    budget_used: Mapping[str, int] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class LLMPlannerOutputV2:
    top_k_archetype_hypotheses: tuple[Mapping[str, Any], ...]
    positive_thesis: str
    counter_thesis: str
    must_verify_primitives: tuple[str, ...]
    green_blockers_to_close: tuple[str, ...]
    red_team_checks: tuple[str, ...]
    source_task_drafts: tuple[Mapping[str, Any], ...]
    query_intents: tuple[str, ...]
    do_not_promote_reasons: tuple[str, ...]
    planner_self_check: Mapping[str, bool]

    def __post_init__(self) -> None:
        payload = self.to_dict()
        if _contains_forbidden_key(payload):
            raise ValueError("LLMPlannerOutputV2 contains score/stage/finalization keys")
        self_check = self.planner_self_check
        if self_check.get("score_keys_present") or self_check.get("stage_keys_present"):
            raise ValueError("LLMPlannerOutputV2 self-check reports forbidden score/stage keys")
        if self_check.get("future_outcome_used"):
            raise ValueError("LLMPlannerOutputV2 self-check reports future outcome leakage")

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class DailyWatchlistItem:
    symbol: str
    company_name: str
    candidate_event_id: str
    event_type: str
    event_summary: str
    primary_archetype: str | None
    secondary_archetypes: tuple[str, ...] = ()
    research_memory_cards_used: tuple[str, ...] = ()
    verified_score: float | None = None
    provisional_score: float | None = None
    score_valid_status: str = "pending_evidence_os_claims"
    base_stage: str = "0"
    investigation_status: str = "PENDING"
    transition_overlay: str = "NONE"
    accepted_claim_ids: tuple[str, ...] = ()
    top_supporting_claims: tuple[str, ...] = ()
    green_blockers: tuple[str, ...] = ()
    red_team_checks: tuple[str, ...] = ()
    source_task_status_summary: Mapping[str, int] = field(default_factory=dict)
    follow_up_tasks: tuple[Mapping[str, Any], ...] = ()
    do_not_promote_reasons: tuple[str, ...] = ()
    operator_notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


def deterministic_event_id_v2(payload: Mapping[str, Any] | Sequence[Any] | str) -> str:
    return deterministic_id("CEV2", payload)


def deterministic_claim_id_v2(payload: Mapping[str, Any] | Sequence[Any] | str) -> str:
    return deterministic_id("RBCLM", payload)


def _contains_forbidden_key(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) in FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS:
                return True
            if _contains_forbidden_key(item):
                return True
    elif isinstance(value, (list, tuple)):
        return any(_contains_forbidden_key(item) for item in value)
    return False


def _json_safe(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
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
    "ArchetypeMemoryCard",
    "ArchetypeRouteCandidate",
    "ArchetypeRouteResult",
    "CandidateEventV2",
    "DailyWatchlistItem",
    "EventMagnitudeV2",
    "FORBIDDEN_RESEARCH_BRAIN_OUTPUT_KEYS",
    "LLMPlannerOutputV2",
    "RouterConfidence",
    "SourceQualityV2",
    "SourceTask",
    "SourceTaskExecution",
    "SourceTaskExecutionStatus",
    "deterministic_claim_id_v2",
    "deterministic_event_id_v2",
]
