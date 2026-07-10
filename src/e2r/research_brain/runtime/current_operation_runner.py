"""Bounded full-universe daily Census on the canonical current-only path."""

from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import asdict, dataclass
from datetime import date
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence
from urllib.parse import urlsplit

from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text
from e2r.research_brain.runtime.atomic_score_stage import (
    AtomicHardBreakSignal,
    AtomicPrimitiveAssessment,
    AtomicScoreClaim,
    AtomicScoreContribution,
    AtomicScoreRule,
    AtomicScoreType,
    AtomicScoringScope,
    AtomicStageConfig,
    AtomicStageCourtTrace,
    AtomicStageDecision,
    CanonicalStage,
    audit_atomic_stage_decisions,
)
from e2r.research_brain.runtime.current_operation import (
    CurrentDeepOutcome,
    CurrentTriggerSignal,
    CurrentTriggerType,
)
from e2r.research_brain.runtime.run_mode_separation import (
    CanonicalRunMode,
    claim_mode_output_root,
)


CURRENT_OPERATION_RUNNER_SCHEMA_VERSION = "e2r_current_operation_runner_v1"
CURRENT_OPERATION_RUNNER_AUDIT_SCHEMA_VERSION = (
    "e2r_current_operation_runner_audit_v1"
)


class DailyBaselineLaneType(str, Enum):
    OFFICIAL = "OFFICIAL"
    PRICE = "PRICE"
    RISK = "RISK"
    EXISTING_LEDGER = "EXISTING_LEDGER"


class DailyBaselineLaneStatus(str, Enum):
    OBSERVED = "OBSERVED"
    NO_RESULT = "NO_RESULT"
    PROVIDER_FAILED = "PROVIDER_FAILED"


class CensusDepthLevel(str, Enum):
    L0_UNIVERSE = "L0_UNIVERSE"
    L1_BASELINE = "L1_BASELINE"
    L2_OFFICIAL_LIGHT = "L2_OFFICIAL_LIGHT"
    L3_RESEARCH_BRAIN = "L3_RESEARCH_BRAIN"
    L4_ACQUISITION = "L4_ACQUISITION"
    L5_FULL_THESIS = "L5_FULL_THESIS"


class DailyTerminalStatus(str, Enum):
    BASELINE_ONLY = "BASELINE_ONLY"
    OFFICIAL_LIGHT = "OFFICIAL_LIGHT"
    NOT_SELECTED_BUDGET = "NOT_SELECTED_BUDGET"
    FULL_THESIS = CurrentDeepOutcome.FULL_THESIS.value
    DISPROVED = CurrentDeepOutcome.DISPROVED.value
    SOURCE_PENDING = CurrentDeepOutcome.SOURCE_PENDING.value
    PROVIDER_PENDING = CurrentDeepOutcome.PROVIDER_PENDING.value
    BUDGET_PENDING = CurrentDeepOutcome.BUDGET_PENDING.value


class DailyProviderKind(str, Enum):
    CODEX = "CODEX"
    FIXTURE = "FIXTURE"
    NONE = "NONE"


_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_NON_PRODUCTION_SOURCE_HOSTS = frozenset(
    {
        "example.com",
        "example.net",
        "example.org",
        "example.test",
        "localhost",
    }
)


@dataclass(frozen=True)
class DailyClaimProvenance:
    provenance_id: str
    claim_id: str
    target_id: str
    document_id: str
    source_url: str
    published_date: str
    available_date: str
    content_sha256: str
    document_text: str
    exact_quote: str
    source_ids: tuple[str, ...]
    anchor_ids: tuple[str, ...]
    mapping_ids: tuple[str, ...]
    extraction_provider_kind: str
    mapping_provider_kind: str
    decision_use: str = "SCORE"
    directness: str = "DIRECT"
    temporal_status: str = "CURRENT"
    mapping_status: str = "ACCEPTED"
    fetched: bool = True
    anchor_verified: bool = True
    source_proxy_only: bool = False
    test_only: bool = False

    def __post_init__(self) -> None:
        for provider in (
            self.extraction_provider_kind,
            self.mapping_provider_kind,
        ):
            if DailyProviderKind(provider) == DailyProviderKind.NONE:
                raise ValueError("claim provenance requires an explicit provider")
        if not all(
            isinstance(item, str) and item.strip()
            for item in (
                self.provenance_id,
                self.claim_id,
                self.target_id,
                self.document_id,
                self.source_url,
                self.document_text,
                self.exact_quote,
            )
        ):
            raise ValueError("claim provenance identity/source/quote is required")
        published = date.fromisoformat(self.published_date)
        available = date.fromisoformat(self.available_date)
        if available < published:
            raise ValueError("claim provenance cannot predate publication")
        if not _SHA256_RE.fullmatch(self.content_sha256):
            raise ValueError("claim provenance content hash must be SHA-256")
        if (
            hashlib.sha256(self.document_text.encode("utf-8")).hexdigest()
            != self.content_sha256
            or self.exact_quote not in self.document_text
        ):
            raise ValueError("claim provenance document hash/quote mismatch")
        if self.decision_use not in {"SCORE", "HARD_BREAK"}:
            raise ValueError("claim provenance decision use is invalid")
        for field_name in ("source_ids", "anchor_ids", "mapping_ids"):
            _require_unique_text(
                getattr(self, field_name),
                context=f"claim provenance {field_name}",
                required=field_name != "mapping_ids" or self.decision_use == "SCORE",
            )
        if (
            self.directness != "DIRECT"
            or self.temporal_status != "CURRENT"
            or (
                self.decision_use == "SCORE"
                and self.mapping_status != "ACCEPTED"
            )
            or (
                self.decision_use == "HARD_BREAK"
                and self.mapping_status != "NOT_REQUIRED_HARD_BREAK"
            )
        ):
            raise ValueError("claim provenance must be direct/current/accepted")
        for field_name in (
            "fetched",
            "anchor_verified",
            "source_proxy_only",
            "test_only",
        ):
            if not isinstance(getattr(self, field_name), bool):
                raise ValueError(f"claim provenance {field_name} must be boolean")
        if not self.fetched or not self.anchor_verified or self.source_proxy_only:
            raise ValueError("claim provenance must be fetched, anchored, and non-proxy")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class DailyThesisLifecycle(str, Enum):
    ACTIVE_CURRENT = "ACTIVE_CURRENT"
    RISK_REVIEW = "RISK_REVIEW"
    NEEDS_REFRESH = "NEEDS_REFRESH"
    INVESTIGATION_OPEN = "INVESTIGATION_OPEN"
    PROVIDER_PENDING = "PROVIDER_PENDING"
    NO_CURRENT_THESIS = "NO_CURRENT_THESIS"


class DailyConfidence(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


class DailyNextAction(str, Enum):
    OBSERVE_ONLY = "OBSERVE_ONLY"
    MONITOR_NEXT_EARNINGS_AND_BACKLOG = "MONITOR_NEXT_EARNINGS_AND_BACKLOG"
    RECHECK_OFFICIAL_SOURCE = "RECHECK_OFFICIAL_SOURCE"
    RETRY_PROVIDER = "RETRY_PROVIDER"
    COMPLETE_MATERIAL_GAPS = "COMPLETE_MATERIAL_GAPS"
    REVIEW_CURRENT_COUNTER_CLAIM = "REVIEW_CURRENT_COUNTER_CLAIM"


class DailyTimelineRole(str, Enum):
    BASELINE = "BASELINE"
    TRIGGER = "TRIGGER"
    CLAIM = "CLAIM"


_REQUIRED_BASELINE_LANES = tuple(item.value for item in DailyBaselineLaneType)
_PENDING_TERMINALS = frozenset(
    {
        DailyTerminalStatus.SOURCE_PENDING.value,
        DailyTerminalStatus.PROVIDER_PENDING.value,
        DailyTerminalStatus.BUDGET_PENDING.value,
    }
)
_FORBIDDEN_WATCHLIST_TERMS = (
    "매수",
    "매도",
    "비중 확대",
    "비중 축소",
    "buy",
    "sell",
    "overweight",
    "underweight",
)
_TRIGGER_PRIORITY = {
    CurrentTriggerType.RISK.value: 100,
    CurrentTriggerType.OFFICIAL.value: 90,
    CurrentTriggerType.EARNINGS.value: 85,
    CurrentTriggerType.IR.value: 80,
    CurrentTriggerType.EXISTING_LEDGER.value: 75,
    CurrentTriggerType.REPORT.value: 70,
    CurrentTriggerType.NEWS.value: 50,
    CurrentTriggerType.MARKET.value: 40,
}


@dataclass(frozen=True)
class DailyUniverseMember:
    target_id: str
    target_name: str
    market: str
    as_of_date: str
    eligible: bool = True
    exclusion_reason: str | None = None

    def __post_init__(self) -> None:
        if not all(
            isinstance(item, str) and item.strip()
            for item in (
                self.target_id,
                self.target_name,
                self.market,
                self.as_of_date,
            )
        ):
            raise ValueError("daily universe member identity is required")
        date.fromisoformat(self.as_of_date)
        if not isinstance(self.eligible, bool):
            raise ValueError("daily universe eligibility must be boolean")
        if not self.eligible and not str(self.exclusion_reason or "").strip():
            raise ValueError("ineligible daily universe member needs exact reason")
        if self.eligible and self.exclusion_reason is not None:
            raise ValueError("eligible daily universe member cannot carry exclusion")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DailyBaselineLane:
    target_id: str
    as_of_date: str
    lane_type: str
    lane_status: str
    source_ids: tuple[str, ...] = ()
    observed_date: str | None = None
    provider_error: str | None = None

    def __post_init__(self) -> None:
        DailyBaselineLaneType(self.lane_type)
        selected_status = DailyBaselineLaneStatus(self.lane_status)
        if not self.target_id.strip():
            raise ValueError("daily baseline lane target is required")
        as_of = date.fromisoformat(self.as_of_date)
        _require_unique_text(
            self.source_ids,
            context="daily baseline source ids",
            required=False,
        )
        observed = (
            date.fromisoformat(self.observed_date)
            if self.observed_date is not None
            else None
        )
        if observed is not None and observed > as_of:
            raise ValueError("future baseline lane entered daily Census")
        if selected_status == DailyBaselineLaneStatus.OBSERVED:
            if not self.source_ids or observed is None or self.provider_error is not None:
                raise ValueError("observed baseline lane needs dated sources only")
        elif selected_status == DailyBaselineLaneStatus.NO_RESULT:
            if self.source_ids or self.provider_error is not None:
                raise ValueError("no-result baseline lane cannot carry source/error")
        elif not str(self.provider_error or "").strip() or self.source_ids:
            raise ValueError("provider-failed baseline lane needs exact error only")

    @property
    def score_evidence_eligible(self) -> bool:
        return False

    def to_dict(self) -> dict[str, Any]:
        return {**asdict(self), "score_evidence_eligible": False}


@dataclass(frozen=True)
class DailySourceTaskRecord:
    task_id: str
    target_id: str
    question_task_id: str
    source_class: str
    max_queries: int
    max_candidates: int
    max_fetches: int
    max_retries: int
    stop_condition: str = "stop_on_resolution"
    allows_general_web: bool = False
    official_first_attempted: bool = True
    official_gap_reasons: tuple[str, ...] = ()
    test_only: bool = False

    def __post_init__(self) -> None:
        if not all(
            isinstance(item, str) and item.strip()
            for item in (
                self.task_id,
                self.target_id,
                self.question_task_id,
                self.source_class,
            )
        ):
            raise ValueError("daily SourceTask record identity is required")
        for name, maximum in (
            ("max_queries", 10),
            ("max_candidates", 100),
            ("max_fetches", 20),
        ):
            value = getattr(self, name)
            if (
                isinstance(value, bool)
                or not isinstance(value, int)
                or value <= 0
                or value > maximum
            ):
                raise ValueError(f"daily SourceTask {name} must be within 1..{maximum}")
        if (
            isinstance(self.max_retries, bool)
            or not isinstance(self.max_retries, int)
            or not 0 <= self.max_retries <= 3
        ):
            raise ValueError("daily SourceTask retries must be within 0..3")
        if self.stop_condition != "stop_on_resolution":
            raise ValueError("daily SourceTask must stop on resolution")
        for name in ("allows_general_web", "official_first_attempted", "test_only"):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"daily SourceTask {name} must be boolean")
        _require_unique_text(
            self.official_gap_reasons,
            context="daily SourceTask official gap reasons",
            required=False,
        )
        if self.allows_general_web and (
            not self.official_first_attempted or not self.official_gap_reasons
        ):
            raise ValueError("daily web SourceTask requires official-first exact gap")
        if not self.allows_general_web and self.official_gap_reasons:
            raise ValueError("official-only SourceTask cannot carry web fallback gap")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DailyDeepExecution:
    execution_id: str
    target_id: str
    outcome: str
    trigger_signal_ids: tuple[str, ...]
    terminal_reason: str
    atomic_decision_id: str | None = None
    source_task_ids: tuple[str, ...] = ()
    provider_kind: str = DailyProviderKind.NONE.value
    provider_trace_id: str | None = None
    llm_calls: int = 0
    source_tasks: int = 0
    fetches: int = 0
    retries: int = 0
    general_web_fetches: int = 0
    official_first_attempted: bool = False
    official_gap_reasons: tuple[str, ...] = ()
    runtime_seconds: float = 0.0

    def __post_init__(self) -> None:
        CurrentDeepOutcome(self.outcome)
        provider_kind = DailyProviderKind(self.provider_kind)
        if not all(
            isinstance(item, str) and item.strip()
            for item in (self.execution_id, self.target_id, self.terminal_reason)
        ):
            raise ValueError("daily deep execution identity and terminal reason required")
        _require_unique_text(
            self.trigger_signal_ids,
            context="daily deep execution triggers",
        )
        _require_unique_text(
            self.source_task_ids,
            context="daily deep execution SourceTask ids",
            required=False,
        )
        _require_unique_text(
            self.official_gap_reasons,
            context="daily official gap reasons",
            required=False,
        )
        for name in (
            "llm_calls",
            "source_tasks",
            "fetches",
            "retries",
            "general_web_fetches",
        ):
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError(f"daily deep execution {name} must be nonnegative")
        if (
            not isinstance(self.runtime_seconds, (int, float))
            or isinstance(self.runtime_seconds, bool)
            or not math.isfinite(float(self.runtime_seconds))
            or self.runtime_seconds < 0.0
        ):
            raise ValueError("daily deep runtime must be finite and nonnegative")
        if not isinstance(self.official_first_attempted, bool):
            raise ValueError("daily official-first flag must be boolean")
        if self.general_web_fetches and (
            not self.official_first_attempted or not self.official_gap_reasons
        ):
            raise ValueError("general web requires official-first attempt and exact gap")
        if self.source_tasks != len(self.source_task_ids):
            raise ValueError("daily deep SourceTask count differs from task leaf refs")
        if self.llm_calls and provider_kind == DailyProviderKind.NONE:
            raise ValueError("LLM calls require an explicit provider kind")
        if provider_kind != DailyProviderKind.NONE and not str(
            self.provider_trace_id or ""
        ).strip():
            raise ValueError("planner provider use requires trace id")
        if self.outcome in {
            CurrentDeepOutcome.FULL_THESIS.value,
            CurrentDeepOutcome.DISPROVED.value,
        } and not str(self.atomic_decision_id or "").strip():
            raise ValueError("terminal full/disproved outcome needs atomic decision")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CurrentOperationRunnerConfig:
    max_official_light_targets: int
    max_deep_candidates: int
    max_brain_candidates: int
    max_acquisition_candidates: int
    max_llm_calls_per_candidate: int
    max_source_tasks_per_candidate: int
    max_fetches_per_candidate: int
    max_retries_per_candidate: int
    max_general_web_fetches_per_candidate: int
    max_runtime_seconds: float
    test_mode: bool = False
    require_claim_provenance: bool = False

    def __post_init__(self) -> None:
        positive = (
            "max_official_light_targets",
            "max_deep_candidates",
            "max_brain_candidates",
            "max_acquisition_candidates",
            "max_llm_calls_per_candidate",
            "max_source_tasks_per_candidate",
            "max_fetches_per_candidate",
        )
        nonnegative = (
            "max_retries_per_candidate",
            "max_general_web_fetches_per_candidate",
        )
        for name in positive:
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                raise ValueError(f"bounded daily config {name} must be positive")
        for name in nonnegative:
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError(f"bounded daily config {name} must be nonnegative")
        if not (
            self.max_acquisition_candidates
            <= self.max_brain_candidates
            <= self.max_deep_candidates
        ):
            raise ValueError("daily L3/L4/deep budgets must be nested")
        if (
            not isinstance(self.max_runtime_seconds, (int, float))
            or isinstance(self.max_runtime_seconds, bool)
            or not math.isfinite(float(self.max_runtime_seconds))
            or self.max_runtime_seconds <= 0.0
        ):
            raise ValueError("daily runtime budget must be finite and positive")
        for name in ("test_mode", "require_claim_provenance"):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"daily {name} must be boolean")
        if self.test_mode and self.require_claim_provenance:
            raise ValueError("test mode cannot claim production provenance enforcement")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DailySourceTimelineEvent:
    event_id: str
    target_id: str
    event_date: str
    role: str
    source_family: str
    source_ids: tuple[str, ...]
    trigger_type: str | None = None
    claim_id: str | None = None
    current_open: bool = False
    candidate_event_eligible: bool = False
    score_evidence_eligible: bool = False

    def __post_init__(self) -> None:
        DailyTimelineRole(self.role)
        if not all(
            isinstance(item, str) and item.strip()
            for item in (
                self.event_id,
                self.target_id,
                self.event_date,
                self.source_family,
            )
        ):
            raise ValueError("daily source timeline event identity required")
        date.fromisoformat(self.event_date)
        _require_unique_text(self.source_ids, context="daily timeline source ids")
        for name in (
            "current_open",
            "candidate_event_eligible",
            "score_evidence_eligible",
        ):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"daily timeline {name} must be boolean")
        if self.role == DailyTimelineRole.TRIGGER.value:
            CurrentTriggerType(str(self.trigger_type or ""))
            if not self.candidate_event_eligible or self.score_evidence_eligible:
                raise ValueError("daily trigger opens investigation and never scores")
        elif self.role == DailyTimelineRole.CLAIM.value:
            if not str(self.claim_id or "").strip() or self.trigger_type is not None:
                raise ValueError("daily claim timeline needs claim id only")
        elif (
            self.trigger_type is not None
            or self.claim_id is not None
            or self.candidate_event_eligible
            or self.score_evidence_eligible
        ):
            raise ValueError("daily baseline timeline event is diagnostic only")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DailySourceTimeline:
    timeline_id: str
    target_id: str
    as_of_date: str
    events: tuple[DailySourceTimelineEvent, ...]

    def __post_init__(self) -> None:
        if not self.timeline_id.strip() or not self.target_id.strip():
            raise ValueError("daily source timeline identity required")
        as_of = date.fromisoformat(self.as_of_date)
        if any(date.fromisoformat(item.event_date) > as_of for item in self.events):
            raise ValueError("future event entered daily source timeline")
        if len({item.event_id for item in self.events}) != len(self.events):
            raise ValueError("daily source timeline has duplicate event ids")

    def to_dict(self) -> dict[str, Any]:
        return {
            **asdict(self),
            "events": [item.to_dict() for item in self.events],
        }


@dataclass(frozen=True)
class DailyLastEffectiveThesis:
    thesis_id: str
    target_id: str
    as_of_date: str
    lifecycle_status: str
    canonical_stage: str
    score_type: str
    atomic_decision_id: str | None
    current_open_claim_ids: tuple[str, ...]
    reason_codes: tuple[str, ...]
    recent_cutoff_applied: bool = False

    def __post_init__(self) -> None:
        DailyThesisLifecycle(self.lifecycle_status)
        CanonicalStage(self.canonical_stage)
        AtomicScoreType(self.score_type)
        if not self.thesis_id.strip() or not self.target_id.strip():
            raise ValueError("daily last-effective-thesis identity required")
        date.fromisoformat(self.as_of_date)
        _require_unique_text(
            self.current_open_claim_ids,
            context="daily current OPEN claims",
            required=False,
        )
        _require_unique_text(self.reason_codes, context="daily thesis reasons")
        if not isinstance(self.recent_cutoff_applied, bool):
            raise ValueError("daily recent cutoff flag must be boolean")
        if self.recent_cutoff_applied:
            raise ValueError("recent lookback cannot delete current Stage/thesis")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DailyDepthDecision:
    depth_id: str
    target_id: str
    completed_depths: tuple[str, ...]
    maximum_depth: str
    selected_for_deep: bool
    selection_reason: str
    source_task_budget: Mapping[str, int]
    llm_budget: Mapping[str, int]

    def __post_init__(self) -> None:
        selected_maximum = CensusDepthLevel(self.maximum_depth)
        if not self.depth_id.strip() or not self.target_id.strip():
            raise ValueError("daily depth decision identity required")
        if not str(self.selection_reason).strip():
            raise ValueError("daily depth selection reason required")
        depths = tuple(CensusDepthLevel(item) for item in self.completed_depths)
        if not depths or depths[-1] != selected_maximum:
            raise ValueError("daily maximum depth must equal completed path tail")
        if len(depths) != len(set(depths)):
            raise ValueError("daily completed depth path contains duplicates")
        expected_order = tuple(CensusDepthLevel)
        positions = tuple(expected_order.index(item) for item in depths)
        if positions != tuple(sorted(positions)):
            raise ValueError("daily depth path must be ordered L0 through L5")
        if not isinstance(self.selected_for_deep, bool):
            raise ValueError("daily selected-for-deep flag must be boolean")
        for budget in (self.source_task_budget, self.llm_budget):
            if any(
                isinstance(value, bool)
                or not isinstance(value, int)
                or value < 0
                for value in budget.values()
            ):
                raise ValueError("daily depth budget must be bounded nonnegative ints")

    def to_dict(self) -> dict[str, Any]:
        return {
            **asdict(self),
            "source_task_budget": dict(self.source_task_budget),
            "llm_budget": dict(self.llm_budget),
        }


@dataclass(frozen=True)
class DailyCensusStageStatus:
    status_id: str
    target_id: str
    target_name: str
    as_of_date: str
    maximum_depth: str
    terminal_status: str
    selected_for_deep: bool
    atomic_decision_id: str | None
    canonical_stage: str
    score_type: str
    score_value: float | None
    raw_reference_score: float | None
    score_valid: bool
    score_finalization_allowed: bool
    confidence: str
    trigger_signal_ids: tuple[str, ...]
    trigger_families: tuple[str, ...]
    accepted_claim_ids: tuple[str, ...]
    missing_conditions: tuple[str, ...]
    material_gap_ids: tuple[str, ...]
    provider_gaps: tuple[str, ...]
    source_gaps: tuple[str, ...]
    next_action: str
    source_timeline_id: str
    thesis_id: str
    recent_cutoff_applied: bool = False

    def __post_init__(self) -> None:
        CensusDepthLevel(self.maximum_depth)
        DailyTerminalStatus(self.terminal_status)
        CanonicalStage(self.canonical_stage)
        score_type = AtomicScoreType(self.score_type)
        DailyConfidence(self.confidence)
        DailyNextAction(self.next_action)
        if not all(
            isinstance(item, str) and item.strip()
            for item in (
                self.status_id,
                self.target_id,
                self.target_name,
                self.as_of_date,
                self.source_timeline_id,
                self.thesis_id,
            )
        ):
            raise ValueError("daily Census status identity required")
        date.fromisoformat(self.as_of_date)
        for name in ("selected_for_deep", "score_valid", "score_finalization_allowed"):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"daily Census status {name} must be boolean")
        for field_name in (
            "trigger_signal_ids",
            "trigger_families",
            "accepted_claim_ids",
            "missing_conditions",
            "material_gap_ids",
            "provider_gaps",
            "source_gaps",
        ):
            _require_unique_text(
                getattr(self, field_name),
                context=f"daily Census {field_name}",
                required=False,
            )
        if any(
            item not in {trigger.value for trigger in CurrentTriggerType}
            for item in self.trigger_families
        ):
            raise ValueError("daily Census status uses unknown trigger family")
        if score_type == AtomicScoreType.NO_SCORE:
            if self.score_value is not None or self.score_valid:
                raise ValueError("daily NO_SCORE cannot expose valid score")
        elif self.atomic_decision_id is None or self.score_value is None:
            raise ValueError("daily visible score requires atomic decision")
        if self.score_finalization_allowed and score_type != AtomicScoreType.FULL_E2R_100:
            raise ValueError("daily finalization requires FULL_E2R_100")
        if self.canonical_stage not in {
            CanonicalStage.STAGE_0.value,
            CanonicalStage.STAGE_1.value,
        } and self.atomic_decision_id is None:
            raise ValueError("daily Stage beyond L1 requires atomic decision")
        if not isinstance(self.recent_cutoff_applied, bool):
            raise ValueError("daily status recent cutoff flag must be boolean")
        if self.recent_cutoff_applied:
            raise ValueError("daily status cannot apply recent Stage cutoff")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CurrentWatchlistItem:
    watchlist_id: str
    target_id: str
    target_name: str
    as_of_date: str
    canonical_stage: str
    terminal_status: str
    score_type: str
    score_value: float | None
    raw_reference_score: float | None
    confidence: str
    claim_ids: tuple[str, ...]
    missing_conditions: tuple[str, ...]
    gap_ids: tuple[str, ...]
    trigger_families: tuple[str, ...]
    next_action: str
    monitoring_label: str

    def __post_init__(self) -> None:
        CanonicalStage(self.canonical_stage)
        DailyTerminalStatus(self.terminal_status)
        AtomicScoreType(self.score_type)
        DailyConfidence(self.confidence)
        DailyNextAction(self.next_action)
        if not all(
            isinstance(item, str) and item.strip()
            for item in (
                self.watchlist_id,
                self.target_id,
                self.target_name,
                self.as_of_date,
                self.monitoring_label,
            )
        ):
            raise ValueError("current watchlist identity and monitoring label required")
        date.fromisoformat(self.as_of_date)
        for field_name in (
            "claim_ids",
            "missing_conditions",
            "gap_ids",
            "trigger_families",
        ):
            _require_unique_text(
                getattr(self, field_name),
                context=f"watchlist {field_name}",
                required=False,
            )
        safety_text = " ".join(
            (self.next_action, self.monitoring_label)
        ).casefold()
        if any(term.casefold() in safety_text for term in _FORBIDDEN_WATCHLIST_TERMS):
            raise ValueError("watchlist contains direct investment recommendation")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CurrentOperationRunnerInput:
    as_of_date: str
    universe: tuple[DailyUniverseMember, ...]
    baseline_lanes: tuple[DailyBaselineLane, ...]
    triggers: tuple[CurrentTriggerSignal, ...]
    claims: tuple[AtomicScoreClaim, ...]
    source_tasks: tuple[DailySourceTaskRecord, ...]
    atomic_decisions: tuple[AtomicStageDecision, ...]
    deep_executions: tuple[DailyDeepExecution, ...]
    config: CurrentOperationRunnerConfig
    claim_provenance: tuple[DailyClaimProvenance, ...] = ()

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if not self.universe:
            raise ValueError("daily current operation requires full universe")

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": CURRENT_OPERATION_RUNNER_SCHEMA_VERSION,
            "as_of_date": self.as_of_date,
            "universe": [item.to_dict() for item in self.universe],
            "baseline_lanes": [item.to_dict() for item in self.baseline_lanes],
            "triggers": [item.to_dict() for item in self.triggers],
            "claims": [item.to_dict() for item in self.claims],
            "claim_provenance": [
                item.to_dict() for item in self.claim_provenance
            ],
            "source_tasks": [item.to_dict() for item in self.source_tasks],
            "atomic_decisions": [
                item.to_dict() for item in self.atomic_decisions
            ],
            "deep_executions": [item.to_dict() for item in self.deep_executions],
            "config": self.config.to_dict(),
        }


@dataclass(frozen=True)
class CurrentOperationRunnerResult:
    run_id: str
    as_of_date: str
    universe: tuple[DailyUniverseMember, ...]
    baseline_lanes: tuple[DailyBaselineLane, ...]
    triggers: tuple[CurrentTriggerSignal, ...]
    claims: tuple[AtomicScoreClaim, ...]
    claim_provenance: tuple[DailyClaimProvenance, ...]
    source_tasks: tuple[DailySourceTaskRecord, ...]
    source_timelines: tuple[DailySourceTimeline, ...]
    thesis_states: tuple[DailyLastEffectiveThesis, ...]
    depth_decisions: tuple[DailyDepthDecision, ...]
    deep_executions: tuple[DailyDeepExecution, ...]
    atomic_decisions: tuple[AtomicStageDecision, ...]
    stage_statuses: tuple[DailyCensusStageStatus, ...]
    watchlist: tuple[CurrentWatchlistItem, ...]
    config: CurrentOperationRunnerConfig
    audit: Mapping[str, Any]
    manifest: Mapping[str, Any]
    mode: str = CanonicalRunMode.CURRENT_OPERATION.value
    production_runtime_ready: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if not self.run_id.strip() or self.mode != CanonicalRunMode.CURRENT_OPERATION.value:
            raise ValueError("daily current operation result identity/mode mismatch")
        leaf_payload = _result_leaf_payload(self)
        expected_leaf_hash = stable_hash(leaf_payload)
        expected_run_id = "DAILY-" + stable_hash(
            {"as_of_date": self.as_of_date, "leaf_hash": expected_leaf_hash}
        )[:24]
        expected_audit = audit_current_daily_census(
            {
                "schema_version": CURRENT_OPERATION_RUNNER_SCHEMA_VERSION,
                "as_of_date": self.as_of_date,
                **leaf_payload,
            }
        )
        if (
            self.run_id != expected_run_id
            or self.manifest.get("run_id") != self.run_id
            or self.manifest.get("leaf_hash") != expected_leaf_hash
            or dict(self.audit) != dict(expected_audit)
            or expected_audit.get("critical_count_sum") != 0
            or self.manifest.get("critical_counts")
            != expected_audit.get("critical_counts")
            or self.manifest.get("critical_count_sum") != 0
        ):
            raise ValueError("daily current operation manifest/audit mismatch")
        if self.production_runtime_ready:
            raise ValueError("fixture/contract daily run cannot claim production ready")

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": CURRENT_OPERATION_RUNNER_SCHEMA_VERSION,
            "run_id": self.run_id,
            "as_of_date": self.as_of_date,
            "mode": self.mode,
            **_result_leaf_payload(self),
            "audit": dict(self.audit),
            "manifest": dict(self.manifest),
            "production_runtime_ready": False,
        }


def run_current_daily_census(
    inputs: CurrentOperationRunnerInput,
) -> CurrentOperationRunnerResult:
    """Compile one bounded current run without performing live I/O."""

    context = _validate_current_inputs(inputs)
    timelines = _build_daily_source_timelines(inputs, context=context)
    thesis_states = _build_daily_thesis_states(
        inputs,
        timelines=timelines,
        context=context,
    )
    depth_decisions = _build_daily_depth_decisions(inputs, context=context)
    stage_statuses = _build_daily_stage_statuses(
        inputs,
        timelines=timelines,
        thesis_states=thesis_states,
        depth_decisions=depth_decisions,
        context=context,
    )
    watchlist = _build_current_watchlist(stage_statuses)
    leaf_payload = _leaf_payload_from_parts(
        universe=inputs.universe,
        baseline_lanes=inputs.baseline_lanes,
        triggers=inputs.triggers,
        claims=inputs.claims,
        claim_provenance=inputs.claim_provenance,
        source_tasks=inputs.source_tasks,
        source_timelines=timelines,
        thesis_states=thesis_states,
        depth_decisions=depth_decisions,
        deep_executions=inputs.deep_executions,
        atomic_decisions=inputs.atomic_decisions,
        stage_statuses=stage_statuses,
        watchlist=watchlist,
        config=inputs.config,
    )
    audit = audit_current_daily_census(
        {
            "schema_version": CURRENT_OPERATION_RUNNER_SCHEMA_VERSION,
            "as_of_date": inputs.as_of_date,
            **leaf_payload,
        }
    )
    if audit["critical_count_sum"]:
        raise ValueError(f"daily current operation audit failed: {audit['critical_counts']}")
    leaf_hash = stable_hash(leaf_payload)
    run_id = "DAILY-" + stable_hash(
        {"as_of_date": inputs.as_of_date, "leaf_hash": leaf_hash}
    )[:24]
    outcome_counts = {
        outcome.value: sum(
            item.outcome == outcome.value for item in inputs.deep_executions
        )
        for outcome in CurrentDeepOutcome
    }
    depth_counts = {
        depth.value: sum(
            depth.value in item.completed_depths for item in depth_decisions
        )
        for depth in CensusDepthLevel
    }
    trigger_family_counts = {
        trigger.value: sum(
            item.trigger_type == trigger.value for item in inputs.triggers
        )
        for trigger in CurrentTriggerType
    }
    manifest = {
        "schema_version": CURRENT_OPERATION_RUNNER_SCHEMA_VERSION,
        "status": "BOUNDED_DAILY_CENSUS_PASS",
        "run_id": run_id,
        "mode": CanonicalRunMode.CURRENT_OPERATION.value,
        "as_of_date": inputs.as_of_date,
        "full_universe_count": len(inputs.universe),
        "eligible_universe_count": sum(item.eligible for item in inputs.universe),
        "baseline_lane_count": len(inputs.baseline_lanes),
        "source_task_count": len(inputs.source_tasks),
        "required_baseline_lane_count": sum(
            item.eligible for item in inputs.universe
        )
        * len(_REQUIRED_BASELINE_LANES),
        "source_timeline_count": len(timelines),
        "last_effective_thesis_count": len(thesis_states),
        "census_stage_status_count": len(stage_statuses),
        "candidate_target_count": len(context["candidate_target_ids"]),
        "selected_deep_candidate_count": len(context["selected_target_ids"]),
        "max_deep_candidates": inputs.config.max_deep_candidates,
        "deep_terminal_outcome_count": len(inputs.deep_executions),
        "deep_outcome_counts": outcome_counts,
        "depth_counts": depth_counts,
        "trigger_family_counts": trigger_family_counts,
        "watchlist_count": len(watchlist),
        "current_open_claim_count": sum(
            item.current_open and item.source_backed and not item.historical_replay
            for item in inputs.claims
        ),
        "claim_provenance_count": len(inputs.claim_provenance),
        "recent_cutoff_stage_drop_count": 0,
        "market_news_score_evidence_count": 0,
        "llm_outside_selected_deep_count": 0,
        "archetype_quota_count": 0,
        "forced_archetype_materialization_count": 0,
        "critical_counts": dict(audit["critical_counts"]),
        "critical_count_sum": 0,
        "leaf_hash": leaf_hash,
        "test_mode": inputs.config.test_mode,
        "production_bounded_contract_ready": True,
        "live_execution_observed": bool(
            not inputs.config.test_mode
            and inputs.config.require_claim_provenance
            and inputs.claim_provenance
            and any(item.fetches > 0 for item in inputs.deep_executions)
        ),
        "production_runtime_ready": False,
    }
    return CurrentOperationRunnerResult(
        run_id=run_id,
        as_of_date=inputs.as_of_date,
        universe=inputs.universe,
        baseline_lanes=inputs.baseline_lanes,
        triggers=inputs.triggers,
        claims=inputs.claims,
        claim_provenance=inputs.claim_provenance,
        source_tasks=inputs.source_tasks,
        source_timelines=timelines,
        thesis_states=thesis_states,
        depth_decisions=depth_decisions,
        deep_executions=inputs.deep_executions,
        atomic_decisions=inputs.atomic_decisions,
        stage_statuses=stage_statuses,
        watchlist=watchlist,
        config=inputs.config,
        audit=audit,
        manifest=manifest,
    )


def _validate_current_inputs(
    inputs: CurrentOperationRunnerInput,
) -> Mapping[str, Any]:
    as_of = date.fromisoformat(inputs.as_of_date)
    universe_by_target = _unique_by(
        inputs.universe,
        key=lambda item: item.target_id,
        context="daily universe target",
    )
    if any(item.as_of_date != inputs.as_of_date for item in inputs.universe):
        raise ValueError("daily universe as-of mismatch")
    eligible_target_ids = {
        item.target_id for item in inputs.universe if item.eligible
    }
    lanes_by_target: dict[str, dict[str, DailyBaselineLane]] = {}
    lane_keys: set[tuple[str, str]] = set()
    for lane in inputs.baseline_lanes:
        if lane.as_of_date != inputs.as_of_date:
            raise ValueError("daily baseline lane as-of mismatch")
        member = universe_by_target.get(lane.target_id)
        if member is None or not member.eligible:
            raise ValueError("daily baseline lane target is not eligible universe")
        key = (lane.target_id, lane.lane_type)
        if key in lane_keys:
            raise ValueError("duplicate daily baseline lane")
        lane_keys.add(key)
        lanes_by_target.setdefault(lane.target_id, {})[lane.lane_type] = lane
    for target_id in eligible_target_ids:
        if set(lanes_by_target.get(target_id, {})) != set(
            _REQUIRED_BASELINE_LANES
        ):
            raise ValueError("eligible target lacks four required baseline lanes")

    trigger_by_id = _unique_by(
        inputs.triggers,
        key=lambda item: item.signal_id,
        context="daily trigger",
    )
    triggers_by_target: dict[str, list[CurrentTriggerSignal]] = {}
    for trigger in inputs.triggers:
        if trigger.target_id not in eligible_target_ids:
            raise ValueError("daily trigger target is outside eligible universe")
        if date.fromisoformat(trigger.observed_date) > as_of:
            raise ValueError("future trigger entered daily current operation")
        triggers_by_target.setdefault(trigger.target_id, []).append(trigger)

    claim_by_id = _unique_by(
        inputs.claims,
        key=lambda item: item.claim_id,
        context="daily claim",
    )
    claims_by_target: dict[str, list[AtomicScoreClaim]] = {}
    for claim in inputs.claims:
        if claim.target_id not in eligible_target_ids:
            raise ValueError("daily claim target is outside eligible universe")
        if date.fromisoformat(claim.observed_date) > as_of:
            raise ValueError("future claim entered daily current operation")
        if claim.historical_replay:
            raise ValueError("historical replay claim entered daily current operation")
        claims_by_target.setdefault(claim.target_id, []).append(claim)
    provenance_by_claim = _unique_by(
        inputs.claim_provenance,
        key=lambda item: item.claim_id,
        context="daily claim provenance",
    )
    for provenance in inputs.claim_provenance:
        claim = claim_by_id.get(provenance.claim_id)
        if claim is None or provenance.target_id != claim.target_id:
            raise ValueError("claim provenance differs from current claim ledger")
        if (
            provenance.source_ids != claim.source_ids
            or provenance.anchor_ids != claim.anchor_ids
            or provenance.mapping_ids != claim.mapping_ids
        ):
            raise ValueError("claim provenance source/anchor/mapping lineage mismatch")
        if (
            date.fromisoformat(provenance.published_date) > as_of
            or date.fromisoformat(provenance.available_date) > as_of
            or date.fromisoformat(provenance.available_date)
            > date.fromisoformat(claim.observed_date)
        ):
            raise ValueError("future claim provenance entered daily current operation")
        if not inputs.config.test_mode and provenance.test_only:
            raise ValueError("test-only claim provenance entered production daily mode")
        if (
            not inputs.config.test_mode
            and (
                provenance.extraction_provider_kind
                != DailyProviderKind.CODEX.value
                or provenance.mapping_provider_kind
                != DailyProviderKind.CODEX.value
                or not _is_production_source_url(provenance.source_url)
            )
        ):
            raise ValueError(
                "production claim provenance requires Codex providers and a live URL"
            )
    if inputs.config.require_claim_provenance:
        effective_claim_ids = {
            claim_id
            for decision in inputs.atomic_decisions
            for claim_id in (
                *decision.accepted_claim_ids,
                *decision.hard_break_claim_ids,
            )
        }
        missing_provenance = effective_claim_ids - set(provenance_by_claim)
        if missing_provenance:
            raise ValueError(
                "production score claims lack claim provenance: "
                + ",".join(sorted(missing_provenance))
            )
    decision_by_id = _unique_by(
        inputs.atomic_decisions,
        key=lambda item: item.decision_id,
        context="daily atomic decision",
    )
    decision_by_target: dict[str, AtomicStageDecision] = {}
    for decision in inputs.atomic_decisions:
        if decision.target_id not in eligible_target_ids:
            raise ValueError("daily atomic decision target is outside universe")
        if decision.as_of_date != inputs.as_of_date:
            raise ValueError("daily atomic decision as-of mismatch")
        if decision.target_id in decision_by_target:
            raise ValueError("daily target has multiple atomic decisions")
        decision_by_target[decision.target_id] = decision
        for claim in decision.claims:
            canonical_claim = claim_by_id.get(claim.claim_id)
            if canonical_claim is None or canonical_claim.to_dict() != claim.to_dict():
                raise ValueError("atomic decision claim differs from current ledger")
            if date.fromisoformat(claim.observed_date) > as_of or claim.historical_replay:
                raise ValueError("future/historical claim entered daily decision")

    source_task_by_id = _unique_by(
        inputs.source_tasks,
        key=lambda item: item.task_id,
        context="daily SourceTask",
    )
    source_tasks_by_target: dict[str, list[DailySourceTaskRecord]] = {}
    for task in inputs.source_tasks:
        if task.target_id not in eligible_target_ids:
            raise ValueError("daily SourceTask target is outside eligible universe")
        if not inputs.config.test_mode and task.test_only:
            raise ValueError("test-only SourceTask cannot enter production daily mode")
        source_tasks_by_target.setdefault(task.target_id, []).append(task)

    candidate_target_ids = tuple(
        target_id
        for target_id, _ in sorted(
            triggers_by_target.items(),
            key=lambda item: _candidate_sort_key(item[0], item[1]),
        )
    )
    selected_target_ids = candidate_target_ids[
        : inputs.config.max_deep_candidates
    ]
    official_light_target_ids = candidate_target_ids[
        : inputs.config.max_official_light_targets
    ]

    execution_by_id = _unique_by(
        inputs.deep_executions,
        key=lambda item: item.execution_id,
        context="daily deep execution",
    )
    execution_by_target = _unique_by(
        inputs.deep_executions,
        key=lambda item: item.target_id,
        context="daily deep execution target",
    )
    if set(execution_by_target) != set(selected_target_ids):
        raise ValueError("every selected deep target needs one terminal execution")
    llm_target_count = 0
    acquisition_target_count = 0
    referenced_source_task_ids: list[str] = []
    for execution in inputs.deep_executions:
        target_triggers = {
            item.signal_id for item in triggers_by_target[execution.target_id]
        }
        if not set(execution.trigger_signal_ids).issubset(target_triggers):
            raise ValueError("deep execution trigger lineage mismatch")
        if execution.llm_calls:
            llm_target_count += 1
        if execution.source_tasks or execution.fetches:
            acquisition_target_count += 1
        execution_tasks = tuple(
            source_task_by_id.get(task_id) for task_id in execution.source_task_ids
        )
        if any(task is None for task in execution_tasks) or any(
            task is not None and task.target_id != execution.target_id
            for task in execution_tasks
        ):
            raise ValueError("deep execution SourceTask leaf mismatch")
        referenced_source_task_ids.extend(execution.source_task_ids)
        if execution.fetches > sum(
            task.max_fetches for task in execution_tasks if task is not None
        ):
            raise ValueError("deep execution fetches exceed SourceTask leaf budgets")
        if execution.retries > sum(
            task.max_retries for task in execution_tasks if task is not None
        ):
            raise ValueError("deep execution retries exceed SourceTask leaf budgets")
        if execution.general_web_fetches and not any(
            task is not None and task.allows_general_web
            for task in execution_tasks
        ):
            raise ValueError("general web execution lacks authorized SourceTask")
        if (
            execution.llm_calls > inputs.config.max_llm_calls_per_candidate
            or execution.source_tasks
            > inputs.config.max_source_tasks_per_candidate
            or execution.fetches > inputs.config.max_fetches_per_candidate
            or execution.retries > inputs.config.max_retries_per_candidate
            or execution.general_web_fetches
            > inputs.config.max_general_web_fetches_per_candidate
        ):
            raise ValueError("daily deep execution exceeded per-candidate budget")
        if (
            not inputs.config.test_mode
            and execution.provider_kind == DailyProviderKind.FIXTURE.value
        ):
            raise ValueError("fixture provider cannot enter production daily mode")
        _validate_execution_decision(
            execution,
            decision=decision_by_target.get(execution.target_id),
        )
    if llm_target_count > inputs.config.max_brain_candidates:
        raise ValueError("daily Research Brain target budget exceeded")
    if acquisition_target_count > inputs.config.max_acquisition_candidates:
        raise ValueError("daily acquisition target budget exceeded")
    if (
        len(referenced_source_task_ids) != len(set(referenced_source_task_ids))
        or set(referenced_source_task_ids) != set(source_task_by_id)
    ):
        raise ValueError("daily SourceTask leaves must be referenced exactly once")
    if sum(item.runtime_seconds for item in inputs.deep_executions) > float(
        inputs.config.max_runtime_seconds
    ):
        raise ValueError("daily total runtime budget exceeded")
    if set(decision_by_target) != {
        item.target_id
        for item in inputs.deep_executions
        if item.atomic_decision_id is not None
    }:
        raise ValueError("daily atomic decision is not linked to terminal execution")

    return {
        "universe_by_target": universe_by_target,
        "eligible_target_ids": eligible_target_ids,
        "lanes_by_target": lanes_by_target,
        "trigger_by_id": trigger_by_id,
        "triggers_by_target": triggers_by_target,
        "claim_by_id": claim_by_id,
        "claims_by_target": claims_by_target,
        "provenance_by_claim": provenance_by_claim,
        "decision_by_id": decision_by_id,
        "decision_by_target": decision_by_target,
        "source_task_by_id": source_task_by_id,
        "source_tasks_by_target": source_tasks_by_target,
        "execution_by_id": execution_by_id,
        "execution_by_target": execution_by_target,
        "candidate_target_ids": candidate_target_ids,
        "selected_target_ids": selected_target_ids,
        "official_light_target_ids": official_light_target_ids,
    }


def _validate_execution_decision(
    execution: DailyDeepExecution,
    *,
    decision: AtomicStageDecision | None,
) -> None:
    if execution.atomic_decision_id is None:
        if decision is not None:
            raise ValueError("unreferenced atomic decision entered deep execution")
    elif decision is None or decision.decision_id != execution.atomic_decision_id:
        raise ValueError("deep execution atomic decision lineage mismatch")
    outcome = CurrentDeepOutcome(execution.outcome)
    if outcome == CurrentDeepOutcome.FULL_THESIS:
        if (
            decision is None
            or decision.score_type != AtomicScoreType.FULL_E2R_100.value
            or not decision.score_valid
            or not decision.score_finalization_allowed
            or decision.material_gap_ids
            or decision.hard_break_claim_ids
            or execution.source_tasks <= 0
            or execution.fetches <= 0
        ):
            raise ValueError("daily full thesis lacks final atomic source path")
    elif outcome == CurrentDeepOutcome.DISPROVED:
        if (
            decision is None
            or decision.score_type != AtomicScoreType.NO_SCORE.value
            or not decision.hard_break_claim_ids
        ):
            raise ValueError("daily disproved outcome needs source-backed hard break")
    elif outcome == CurrentDeepOutcome.SOURCE_PENDING:
        if decision is not None and (
            decision.score_type != AtomicScoreType.NO_SCORE.value
            or not decision.source_pending
        ):
            raise ValueError("source pending cannot carry a finalized score")
    elif outcome == CurrentDeepOutcome.PROVIDER_PENDING:
        if decision is not None and (
            decision.score_type != AtomicScoreType.NO_SCORE.value
            or not decision.provider_pending
        ):
            raise ValueError("provider pending cannot carry a finalized score")
    elif decision is not None and decision.score_type == AtomicScoreType.FULL_E2R_100.value:
        raise ValueError("budget pending cannot carry a finalized full score")


def _candidate_sort_key(
    target_id: str,
    signals: Sequence[CurrentTriggerSignal],
) -> tuple[Any, ...]:
    priorities = tuple(_TRIGGER_PRIORITY[item.trigger_type] for item in signals)
    families = {item.trigger_type for item in signals}
    return (-max(priorities), -len(families), -len(signals), target_id)


def _build_daily_source_timelines(
    inputs: CurrentOperationRunnerInput,
    *,
    context: Mapping[str, Any],
) -> tuple[DailySourceTimeline, ...]:
    lanes_by_target = context["lanes_by_target"]
    triggers_by_target = context["triggers_by_target"]
    claims_by_target = context["claims_by_target"]
    timelines: list[DailySourceTimeline] = []
    for member in inputs.universe:
        events: list[DailySourceTimelineEvent] = []
        for lane in lanes_by_target.get(member.target_id, {}).values():
            source_ids = lane.source_ids or (
                "BASELINE-STATUS-"
                + stable_hash(
                    {
                        "target_id": lane.target_id,
                        "lane_type": lane.lane_type,
                        "lane_status": lane.lane_status,
                        "as_of_date": lane.as_of_date,
                    }
                )[:20],
            )
            event_payload = {
                "target_id": member.target_id,
                "role": DailyTimelineRole.BASELINE.value,
                "lane_type": lane.lane_type,
                "lane_status": lane.lane_status,
                "source_ids": list(source_ids),
            }
            events.append(
                DailySourceTimelineEvent(
                    event_id="DTL-" + stable_hash(event_payload)[:24],
                    target_id=member.target_id,
                    event_date=lane.observed_date or inputs.as_of_date,
                    role=DailyTimelineRole.BASELINE.value,
                    source_family=lane.lane_type,
                    source_ids=tuple(source_ids),
                )
            )
        for trigger in triggers_by_target.get(member.target_id, ()):
            event_payload = {
                "target_id": member.target_id,
                "role": DailyTimelineRole.TRIGGER.value,
                "signal_id": trigger.signal_id,
            }
            events.append(
                DailySourceTimelineEvent(
                    event_id="DTL-" + stable_hash(event_payload)[:24],
                    target_id=member.target_id,
                    event_date=trigger.observed_date,
                    role=DailyTimelineRole.TRIGGER.value,
                    source_family=trigger.trigger_type,
                    source_ids=(trigger.source_id,),
                    trigger_type=trigger.trigger_type,
                    candidate_event_eligible=True,
                    score_evidence_eligible=False,
                )
            )
        for claim in claims_by_target.get(member.target_id, ()):
            event_payload = {
                "target_id": member.target_id,
                "role": DailyTimelineRole.CLAIM.value,
                "claim_id": claim.claim_id,
                "content_hash": claim.content_hash,
            }
            events.append(
                DailySourceTimelineEvent(
                    event_id="DTL-" + stable_hash(event_payload)[:24],
                    target_id=member.target_id,
                    event_date=claim.observed_date,
                    role=DailyTimelineRole.CLAIM.value,
                    source_family="CURRENT_CLAIM_LEDGER",
                    source_ids=claim.source_ids,
                    claim_id=claim.claim_id,
                    current_open=claim.current_open,
                    score_evidence_eligible=claim.score_eligible,
                )
            )
        events.sort(
            key=lambda item: (
                item.event_date,
                tuple(DailyTimelineRole).index(DailyTimelineRole(item.role)),
                item.event_id,
            )
        )
        timeline_payload = {
            "target_id": member.target_id,
            "as_of_date": inputs.as_of_date,
            "event_ids": [item.event_id for item in events],
        }
        timelines.append(
            DailySourceTimeline(
                timeline_id="DTIM-" + stable_hash(timeline_payload)[:24],
                target_id=member.target_id,
                as_of_date=inputs.as_of_date,
                events=tuple(events),
            )
        )
    return tuple(timelines)


def _build_daily_thesis_states(
    inputs: CurrentOperationRunnerInput,
    *,
    timelines: Sequence[DailySourceTimeline],
    context: Mapping[str, Any],
) -> tuple[DailyLastEffectiveThesis, ...]:
    timeline_by_target = {item.target_id: item for item in timelines}
    decision_by_target = context["decision_by_target"]
    execution_by_target = context["execution_by_target"]
    claims_by_target = context["claims_by_target"]
    triggers_by_target = context["triggers_by_target"]
    states: list[DailyLastEffectiveThesis] = []
    for member in inputs.universe:
        decision = decision_by_target.get(member.target_id)
        execution = execution_by_target.get(member.target_id)
        current_claim_ids = tuple(
            item.claim_id
            for item in claims_by_target.get(member.target_id, ())
            if item.current_open and item.source_backed and not item.historical_replay
        )
        if decision is not None and decision.hard_break_claim_ids:
            lifecycle = DailyThesisLifecycle.RISK_REVIEW
            reasons = ("current_source_backed_hard_break",)
        elif decision is not None and (
            decision.score_type == AtomicScoreType.FULL_E2R_100.value
            and decision.score_finalization_allowed
        ):
            lifecycle = DailyThesisLifecycle.ACTIVE_CURRENT
            reasons = ("current_atomic_full_thesis",)
        elif execution is not None and (
            execution.outcome == CurrentDeepOutcome.PROVIDER_PENDING.value
        ):
            lifecycle = DailyThesisLifecycle.PROVIDER_PENDING
            reasons = ("provider_pending_no_final_score",)
        elif current_claim_ids:
            lifecycle = DailyThesisLifecycle.NEEDS_REFRESH
            reasons = ("current_open_claim_requires_atomic_refresh",)
        elif triggers_by_target.get(member.target_id):
            lifecycle = DailyThesisLifecycle.INVESTIGATION_OPEN
            reasons = ("daily_trigger_opens_investigation",)
        else:
            lifecycle = DailyThesisLifecycle.NO_CURRENT_THESIS
            reasons = ("no_current_trigger_or_open_claim",)
        canonical_stage = (
            decision.canonical_stage
            if decision is not None
            else CanonicalStage.STAGE_0.value
        )
        score_type = (
            decision.score_type
            if decision is not None
            else AtomicScoreType.NO_SCORE.value
        )
        state_payload = {
            "target_id": member.target_id,
            "as_of_date": inputs.as_of_date,
            "lifecycle_status": lifecycle.value,
            "decision_id": decision.decision_id if decision is not None else None,
            "current_open_claim_ids": list(current_claim_ids),
            "timeline_id": timeline_by_target[member.target_id].timeline_id,
        }
        states.append(
            DailyLastEffectiveThesis(
                thesis_id="DTH-" + stable_hash(state_payload)[:24],
                target_id=member.target_id,
                as_of_date=inputs.as_of_date,
                lifecycle_status=lifecycle.value,
                canonical_stage=canonical_stage,
                score_type=score_type,
                atomic_decision_id=(
                    decision.decision_id if decision is not None else None
                ),
                current_open_claim_ids=current_claim_ids,
                reason_codes=reasons,
                recent_cutoff_applied=False,
            )
        )
    return tuple(states)


def _build_daily_depth_decisions(
    inputs: CurrentOperationRunnerInput,
    *,
    context: Mapping[str, Any],
) -> tuple[DailyDepthDecision, ...]:
    selected = set(context["selected_target_ids"])
    official_light = set(context["official_light_target_ids"])
    execution_by_target = context["execution_by_target"]
    decisions: list[DailyDepthDecision] = []
    for member in inputs.universe:
        depths = [CensusDepthLevel.L0_UNIVERSE]
        is_selected = member.target_id in selected
        execution = execution_by_target.get(member.target_id)
        if member.eligible:
            depths.append(CensusDepthLevel.L1_BASELINE)
        if member.target_id in official_light:
            depths.append(CensusDepthLevel.L2_OFFICIAL_LIGHT)
        if is_selected:
            depths.append(CensusDepthLevel.L3_RESEARCH_BRAIN)
        if execution is not None and (
            execution.source_tasks > 0
            or execution.fetches > 0
            or execution.outcome
            in {
                CurrentDeepOutcome.FULL_THESIS.value,
                CurrentDeepOutcome.DISPROVED.value,
                CurrentDeepOutcome.SOURCE_PENDING.value,
                CurrentDeepOutcome.PROVIDER_PENDING.value,
            }
        ):
            depths.append(CensusDepthLevel.L4_ACQUISITION)
        if execution is not None and (
            execution.outcome == CurrentDeepOutcome.FULL_THESIS.value
        ):
            depths.append(CensusDepthLevel.L5_FULL_THESIS)
        if not member.eligible:
            reason = f"ineligible:{member.exclusion_reason}"
        elif is_selected:
            reason = "current_trigger_rank_within_bounded_deep_budget"
        elif member.target_id in context["candidate_target_ids"]:
            reason = "current_trigger_retained_outside_deep_budget"
        else:
            reason = "full_universe_baseline_only"
        depth_payload = {
            "target_id": member.target_id,
            "as_of_date": inputs.as_of_date,
            "completed_depths": [item.value for item in depths],
            "selected": is_selected,
        }
        decisions.append(
            DailyDepthDecision(
                depth_id="DDEP-" + stable_hash(depth_payload)[:24],
                target_id=member.target_id,
                completed_depths=tuple(item.value for item in depths),
                maximum_depth=depths[-1].value,
                selected_for_deep=is_selected,
                selection_reason=reason,
                source_task_budget=(
                    {
                        "max_tasks": inputs.config.max_source_tasks_per_candidate,
                        "max_fetches": inputs.config.max_fetches_per_candidate,
                        "max_retries": inputs.config.max_retries_per_candidate,
                        "max_general_web_fetches": (
                            inputs.config.max_general_web_fetches_per_candidate
                        ),
                    }
                    if is_selected
                    else {
                        "max_tasks": 0,
                        "max_fetches": 0,
                        "max_retries": 0,
                        "max_general_web_fetches": 0,
                    }
                ),
                llm_budget={
                    "max_calls": (
                        inputs.config.max_llm_calls_per_candidate
                        if is_selected
                        else 0
                    )
                },
            )
        )
    return tuple(decisions)


def _build_daily_stage_statuses(
    inputs: CurrentOperationRunnerInput,
    *,
    timelines: Sequence[DailySourceTimeline],
    thesis_states: Sequence[DailyLastEffectiveThesis],
    depth_decisions: Sequence[DailyDepthDecision],
    context: Mapping[str, Any],
) -> tuple[DailyCensusStageStatus, ...]:
    timeline_by_target = {item.target_id: item for item in timelines}
    thesis_by_target = {item.target_id: item for item in thesis_states}
    depth_by_target = {item.target_id: item for item in depth_decisions}
    triggers_by_target = context["triggers_by_target"]
    decision_by_target = context["decision_by_target"]
    execution_by_target = context["execution_by_target"]
    lanes_by_target = context["lanes_by_target"]
    candidate_targets = set(context["candidate_target_ids"])
    official_light_targets = set(context["official_light_target_ids"])
    statuses: list[DailyCensusStageStatus] = []
    for member in inputs.universe:
        triggers = tuple(triggers_by_target.get(member.target_id, ()))
        decision = decision_by_target.get(member.target_id)
        execution = execution_by_target.get(member.target_id)
        depth = depth_by_target[member.target_id]
        provider_gaps = tuple(
            f"{lane.lane_type}:{lane.provider_error}"
            for lane in lanes_by_target.get(member.target_id, {}).values()
            if lane.lane_status == DailyBaselineLaneStatus.PROVIDER_FAILED.value
        )
        source_gaps: list[str] = []
        missing_conditions: list[str] = []
        material_gaps: list[str] = []
        if decision is not None:
            canonical_stage = decision.canonical_stage
            score_type = decision.score_type
            score_value = decision.score_value
            raw_reference_score = decision.raw_reference_score
            score_valid = decision.score_valid
            finalization_allowed = decision.score_finalization_allowed
            accepted_claim_ids = tuple(
                dict.fromkeys(
                    (*decision.accepted_claim_ids, *decision.hard_break_claim_ids)
                )
            )
            missing_conditions.extend(decision.missing_conditions)
            material_gaps.extend(decision.material_gap_ids)
        else:
            canonical_stage = (
                CanonicalStage.STAGE_1.value
                if triggers and execution is None
                else CanonicalStage.STAGE_0.value
            )
            score_type = AtomicScoreType.NO_SCORE.value
            score_value = None
            raw_reference_score = None
            score_valid = False
            finalization_allowed = False
            accepted_claim_ids = ()
        if not member.eligible:
            terminal = DailyTerminalStatus.BASELINE_ONLY
            next_action = DailyNextAction.OBSERVE_ONLY
        elif execution is not None:
            terminal = DailyTerminalStatus(execution.outcome)
            if execution.outcome == CurrentDeepOutcome.FULL_THESIS.value:
                next_action = DailyNextAction.MONITOR_NEXT_EARNINGS_AND_BACKLOG
            elif execution.outcome == CurrentDeepOutcome.DISPROVED.value:
                next_action = DailyNextAction.REVIEW_CURRENT_COUNTER_CLAIM
            elif execution.outcome == CurrentDeepOutcome.PROVIDER_PENDING.value:
                next_action = DailyNextAction.RETRY_PROVIDER
                missing_conditions.append(execution.terminal_reason)
                provider_gaps = tuple(
                    dict.fromkeys((*provider_gaps, execution.terminal_reason))
                )
            elif execution.outcome == CurrentDeepOutcome.SOURCE_PENDING.value:
                next_action = DailyNextAction.RECHECK_OFFICIAL_SOURCE
                missing_conditions.append(execution.terminal_reason)
                source_gaps.append(execution.terminal_reason)
            else:
                next_action = DailyNextAction.COMPLETE_MATERIAL_GAPS
                missing_conditions.append(execution.terminal_reason)
                source_gaps.append(execution.terminal_reason)
        elif member.target_id in candidate_targets:
            if member.target_id in official_light_targets:
                terminal = DailyTerminalStatus.OFFICIAL_LIGHT
                next_action = DailyNextAction.RECHECK_OFFICIAL_SOURCE
            else:
                terminal = DailyTerminalStatus.NOT_SELECTED_BUDGET
                next_action = DailyNextAction.OBSERVE_ONLY
            missing_conditions.append("deep_budget_not_selected")
        else:
            terminal = DailyTerminalStatus.BASELINE_ONLY
            next_action = DailyNextAction.OBSERVE_ONLY
        confidence = _daily_confidence(
            score_type=score_type,
            canonical_stage=canonical_stage,
            material_gaps=material_gaps,
            terminal_status=terminal.value,
        )
        status_payload = {
            "target_id": member.target_id,
            "as_of_date": inputs.as_of_date,
            "maximum_depth": depth.maximum_depth,
            "terminal_status": terminal.value,
            "atomic_decision_id": (
                decision.decision_id if decision is not None else None
            ),
            "canonical_stage": canonical_stage,
            "score_type": score_type,
        }
        statuses.append(
            DailyCensusStageStatus(
                status_id="DCSS-" + stable_hash(status_payload)[:24],
                target_id=member.target_id,
                target_name=member.target_name,
                as_of_date=inputs.as_of_date,
                maximum_depth=depth.maximum_depth,
                terminal_status=terminal.value,
                selected_for_deep=depth.selected_for_deep,
                atomic_decision_id=(
                    decision.decision_id if decision is not None else None
                ),
                canonical_stage=canonical_stage,
                score_type=score_type,
                score_value=score_value,
                raw_reference_score=raw_reference_score,
                score_valid=score_valid,
                score_finalization_allowed=finalization_allowed,
                confidence=confidence.value,
                trigger_signal_ids=tuple(item.signal_id for item in triggers),
                trigger_families=tuple(
                    dict.fromkeys(item.trigger_type for item in triggers)
                ),
                accepted_claim_ids=accepted_claim_ids,
                missing_conditions=tuple(dict.fromkeys(missing_conditions)),
                material_gap_ids=tuple(dict.fromkeys(material_gaps)),
                provider_gaps=provider_gaps,
                source_gaps=tuple(dict.fromkeys(source_gaps)),
                next_action=next_action.value,
                source_timeline_id=timeline_by_target[member.target_id].timeline_id,
                thesis_id=thesis_by_target[member.target_id].thesis_id,
                recent_cutoff_applied=False,
            )
        )
    return tuple(statuses)


def _daily_confidence(
    *,
    score_type: str,
    canonical_stage: str,
    material_gaps: Sequence[str],
    terminal_status: str,
) -> DailyConfidence:
    if score_type == AtomicScoreType.FULL_E2R_100.value:
        if not material_gaps and canonical_stage == CanonicalStage.STAGE_3_GREEN.value:
            return DailyConfidence.HIGH
        return DailyConfidence.MEDIUM
    if score_type == AtomicScoreType.EVENT_EVIDENCE_PARTIAL.value:
        return DailyConfidence.LOW
    if terminal_status in {
        DailyTerminalStatus.OFFICIAL_LIGHT.value,
        DailyTerminalStatus.NOT_SELECTED_BUDGET.value,
    }:
        return DailyConfidence.LOW
    return DailyConfidence.INSUFFICIENT_EVIDENCE


def _build_current_watchlist(
    stage_statuses: Sequence[DailyCensusStageStatus],
) -> tuple[CurrentWatchlistItem, ...]:
    rows: list[CurrentWatchlistItem] = []
    for status in stage_statuses:
        if (
            not status.trigger_signal_ids
            and not status.accepted_claim_ids
            and status.terminal_status == DailyTerminalStatus.BASELINE_ONLY.value
        ):
            continue
        gap_ids = tuple(
            dict.fromkeys(
                (
                    *status.material_gap_ids,
                    *status.provider_gaps,
                    *status.source_gaps,
                )
            )
        )
        monitoring_label = _monitoring_label(status)
        payload = {
            "target_id": status.target_id,
            "as_of_date": status.as_of_date,
            "status_id": status.status_id,
            "next_action": status.next_action,
        }
        rows.append(
            CurrentWatchlistItem(
                watchlist_id="DWL-" + stable_hash(payload)[:24],
                target_id=status.target_id,
                target_name=status.target_name,
                as_of_date=status.as_of_date,
                canonical_stage=status.canonical_stage,
                terminal_status=status.terminal_status,
                score_type=status.score_type,
                score_value=status.score_value,
                raw_reference_score=status.raw_reference_score,
                confidence=status.confidence,
                claim_ids=status.accepted_claim_ids,
                missing_conditions=status.missing_conditions,
                gap_ids=gap_ids,
                trigger_families=status.trigger_families,
                next_action=status.next_action,
                monitoring_label=monitoring_label,
            )
        )
    return tuple(rows)


def _monitoring_label(status: DailyCensusStageStatus) -> str:
    if status.canonical_stage == CanonicalStage.STAGE_4C.value:
        return "Stage 4C 논리 훼손 감시"
    if status.canonical_stage == CanonicalStage.STAGE_3_RED.value:
        return "Stage 3-Red 현재 counter claim 감시"
    if status.terminal_status == DailyTerminalStatus.FULL_THESIS.value:
        return "다음 실적과 수주잔고 확인"
    if status.terminal_status in _PENDING_TERMINALS:
        return "근거 보완 후 Stage 재검증"
    return "daily trigger 변화 관찰"


def audit_current_daily_census(
    result: CurrentOperationRunnerResult | Mapping[str, Any],
) -> Mapping[str, Any]:
    payload = (
        result.to_dict()
        if isinstance(result, CurrentOperationRunnerResult)
        else dict(result)
    )
    universe = tuple(_mapping_rows(payload.get("universe")))
    lanes = tuple(_mapping_rows(payload.get("baseline_lanes")))
    triggers = tuple(_mapping_rows(payload.get("triggers")))
    claims = tuple(_mapping_rows(payload.get("claims")))
    claim_provenance = tuple(_mapping_rows(payload.get("claim_provenance")))
    source_tasks = tuple(_mapping_rows(payload.get("source_tasks")))
    timelines = tuple(_mapping_rows(payload.get("source_timelines")))
    theses = tuple(_mapping_rows(payload.get("thesis_states")))
    depths = tuple(_mapping_rows(payload.get("depth_decisions")))
    executions = tuple(_mapping_rows(payload.get("deep_executions")))
    decisions = tuple(_mapping_rows(payload.get("atomic_decisions")))
    statuses = tuple(_mapping_rows(payload.get("stage_statuses")))
    watchlist = tuple(_mapping_rows(payload.get("watchlist")))
    config = (
        dict(payload.get("config"))
        if isinstance(payload.get("config"), Mapping)
        else {}
    )
    universe_ids = tuple(str(item.get("target_id") or "") for item in universe)
    eligible_ids = {
        str(item.get("target_id") or "")
        for item in universe
        if item.get("eligible") is True
    }
    status_ids = tuple(str(item.get("target_id") or "") for item in statuses)
    timeline_ids = tuple(str(item.get("target_id") or "") for item in timelines)
    thesis_ids = tuple(str(item.get("target_id") or "") for item in theses)
    depth_ids = tuple(str(item.get("target_id") or "") for item in depths)
    selected_ids = {
        str(item.get("target_id") or "")
        for item in depths
        if item.get("selected_for_deep") is True
    }
    execution_target_ids = tuple(
        str(item.get("target_id") or "") for item in executions
    )
    execution_ids = set(execution_target_ids)
    execution_record_ids = tuple(
        str(item.get("execution_id") or "") for item in executions
    )
    decision_by_id = {
        str(item.get("decision_id") or ""): item
        for item in decisions
        if item.get("decision_id")
    }
    status_by_target = {
        str(item.get("target_id") or ""): item
        for item in statuses
        if item.get("target_id")
    }
    timeline_by_target = {
        str(item.get("target_id") or ""): item
        for item in timelines
        if item.get("target_id")
    }
    thesis_by_target = {
        str(item.get("target_id") or ""): item
        for item in theses
        if item.get("target_id")
    }
    depth_by_target = {
        str(item.get("target_id") or ""): item
        for item in depths
        if item.get("target_id")
    }
    claim_by_id = {
        str(item.get("claim_id") or ""): item
        for item in claims
        if item.get("claim_id")
    }
    provenance_ids = tuple(
        str(item.get("provenance_id") or "") for item in claim_provenance
    )
    provenance_claim_ids = tuple(
        str(item.get("claim_id") or "") for item in claim_provenance
    )
    provenance_by_claim = {
        str(item.get("claim_id") or ""): item
        for item in claim_provenance
        if item.get("claim_id")
    }
    source_task_ids = tuple(
        str(item.get("task_id") or "") for item in source_tasks
    )
    source_task_by_id = {
        str(item.get("task_id") or ""): item
        for item in source_tasks
        if item.get("task_id")
    }
    baseline_lane_missing = 0
    baseline_lane_duplicate = 0
    for target_id in eligible_ids:
        target_lanes = [
            str(item.get("lane_type") or "")
            for item in lanes
            if str(item.get("target_id") or "") == target_id
        ]
        baseline_lane_missing += len(
            set(_REQUIRED_BASELINE_LANES) - set(target_lanes)
        )
        baseline_lane_duplicate += len(target_lanes) - len(set(target_lanes))
    as_of = _safe_date(payload.get("as_of_date"))
    future_count = 0
    if as_of is None:
        future_count += 1
    else:
        for row, field_name in (
            *((item, "observed_date") for item in lanes if item.get("observed_date")),
            *((item, "observed_date") for item in triggers),
            *((item, "observed_date") for item in claims),
            *((item, "published_date") for item in claim_provenance),
            *((item, "available_date") for item in claim_provenance),
        ):
            observed = _safe_date(row.get(field_name))
            if observed is None or observed > as_of:
                future_count += 1
        for timeline in timelines:
            for event in _mapping_rows(timeline.get("events")):
                observed = _safe_date(event.get("event_date"))
                if observed is None or observed > as_of:
                    future_count += 1

    trigger_score_evidence_count = 0
    market_news_score_evidence_count = 0
    timeline_claim_ids_by_target: dict[str, set[str]] = {}
    for timeline in timelines:
        timeline_target_id = str(timeline.get("target_id") or "")
        for event in _mapping_rows(timeline.get("events")):
            if event.get("role") == DailyTimelineRole.CLAIM.value and event.get(
                "claim_id"
            ):
                timeline_claim_ids_by_target.setdefault(
                    timeline_target_id, set()
                ).add(str(event.get("claim_id")))
            if (
                event.get("role") == DailyTimelineRole.TRIGGER.value
                and event.get("score_evidence_eligible") is True
            ):
                trigger_score_evidence_count += 1
                if event.get("trigger_type") in {
                    CurrentTriggerType.MARKET.value,
                    CurrentTriggerType.NEWS.value,
                }:
                    market_news_score_evidence_count += 1
    trigger_score_evidence_count += sum(
        item.get("counts_as_score_evidence") is True for item in triggers
    )
    current_open_claim_ids_by_target: dict[str, set[str]] = {}
    for item in claims:
        if (
            item.get("current_open") is True
            and item.get("source_backed") is True
            and item.get("historical_replay") is False
        ):
            current_open_claim_ids_by_target.setdefault(
                str(item.get("target_id") or ""), set()
            ).add(str(item.get("claim_id") or ""))
    thesis_open_claim_ids_by_target = {
        str(item.get("target_id") or ""): {
            str(claim_id)
            for claim_id in item.get("current_open_claim_ids") or ()
        }
        for item in theses
    }
    current_open_claim_dropped = sum(
        len(
            claim_ids
            - thesis_open_claim_ids_by_target.get(target_id, set())
        )
        for target_id, claim_ids in current_open_claim_ids_by_target.items()
    )
    current_open_claim_missing_from_timeline = sum(
        len(claim_ids - timeline_claim_ids_by_target.get(target_id, set()))
        for target_id, claim_ids in current_open_claim_ids_by_target.items()
    )
    thesis_claim_lineage_mismatch = sum(
        claim_id not in claim_by_id
        or str(claim_by_id[claim_id].get("target_id") or "") != target_id
        or claim_by_id[claim_id].get("current_open") is not True
        or claim_by_id[claim_id].get("source_backed") is not True
        or claim_by_id[claim_id].get("historical_replay") is not False
        for target_id, claim_ids in thesis_open_claim_ids_by_target.items()
        for claim_id in claim_ids
    )
    accepted_effective_claim_ids = {
        str(claim_id)
        for decision in decisions
        for claim_id in decision.get("accepted_claim_ids") or ()
    }
    hard_break_effective_claim_ids = {
        str(claim_id)
        for decision in decisions
        for claim_id in decision.get("hard_break_claim_ids") or ()
    }
    effective_claim_ids = (
        accepted_effective_claim_ids | hard_break_effective_claim_ids
    )
    claim_provenance_contract_failure = 0
    for item in claim_provenance:
        claim_id = str(item.get("claim_id") or "")
        claim = claim_by_id.get(claim_id)
        published_date = _safe_date(item.get("published_date"))
        available_date = _safe_date(item.get("available_date"))
        claim_observed_date = (
            _safe_date(claim.get("observed_date"))
            if claim is not None
            else None
        )
        providers = {
            str(item.get("extraction_provider_kind") or ""),
            str(item.get("mapping_provider_kind") or ""),
        }
        if (
            claim is None
            or str(item.get("target_id") or "")
            != str(claim.get("target_id") or "")
            or tuple(item.get("source_ids") or ())
            != tuple(claim.get("source_ids") or ())
            or tuple(item.get("anchor_ids") or ())
            != tuple(claim.get("anchor_ids") or ())
            or tuple(item.get("mapping_ids") or ())
            != tuple(claim.get("mapping_ids") or ())
            or not str(item.get("document_id") or "").strip()
            or not str(item.get("source_url") or "").strip()
            or published_date is None
            or available_date is None
            or available_date < published_date
            or claim_observed_date is None
            or available_date > claim_observed_date
            or not str(item.get("document_text") or "").strip()
            or not str(item.get("exact_quote") or "").strip()
            or not _SHA256_RE.fullmatch(str(item.get("content_sha256") or ""))
            or hashlib.sha256(
                str(item.get("document_text") or "").encode("utf-8")
            ).hexdigest()
            != item.get("content_sha256")
            or str(item.get("exact_quote") or "")
            not in str(item.get("document_text") or "")
            or item.get("directness") != "DIRECT"
            or item.get("temporal_status") != "CURRENT"
            or item.get("decision_use") not in {"SCORE", "HARD_BREAK"}
            or (
                item.get("decision_use") == "SCORE"
                and (
                    item.get("mapping_status") != "ACCEPTED"
                    or claim_id not in accepted_effective_claim_ids
                )
            )
            or (
                item.get("decision_use") == "HARD_BREAK"
                and (
                    item.get("mapping_status") != "NOT_REQUIRED_HARD_BREAK"
                    or claim_id not in hard_break_effective_claim_ids
                )
            )
            or item.get("fetched") is not True
            or item.get("anchor_verified") is not True
            or item.get("source_proxy_only") is not False
            or not providers
            or DailyProviderKind.NONE.value in providers
            or not providers.issubset(
                {DailyProviderKind.CODEX.value, DailyProviderKind.FIXTURE.value}
            )
            or (
                config.get("test_mode") is False
                and (
                    item.get("test_only") is True
                    or providers != {DailyProviderKind.CODEX.value}
                    or not _is_production_source_url(
                        str(item.get("source_url") or "")
                    )
                )
            )
        ):
            claim_provenance_contract_failure += 1
    decision_claim_without_required_provenance = (
        len(effective_claim_ids - set(provenance_by_claim))
        if config.get("require_claim_provenance") is True
        else 0
    )

    max_deep = _safe_nonnegative_int(config.get("max_deep_candidates"))
    max_official = _safe_nonnegative_int(
        config.get("max_official_light_targets")
    )
    max_brain = _safe_nonnegative_int(config.get("max_brain_candidates"))
    max_acquisition = _safe_nonnegative_int(
        config.get("max_acquisition_candidates")
    )
    llm_targets = {
        str(item.get("target_id") or "")
        for item in executions
        if _safe_nonnegative_int(item.get("llm_calls")) > 0
    }
    acquisition_targets = {
        str(item.get("target_id") or "")
        for item in executions
        if _safe_nonnegative_int(item.get("source_tasks")) > 0
        or _safe_nonnegative_int(item.get("fetches")) > 0
    }
    general_web_targets = {
        str(item.get("target_id") or "")
        for item in executions
        if _safe_nonnegative_int(item.get("general_web_fetches")) > 0
    }
    official_light_count = sum(
        CensusDepthLevel.L2_OFFICIAL_LIGHT.value
        in tuple(item.get("completed_depths") or ())
        for item in depths
    )
    per_candidate_budget_violation = 0
    general_web_without_official_gap = 0
    fixture_provider_in_production = 0
    referenced_source_task_ids: list[str] = []
    execution_source_task_reference_mismatch = 0
    execution_fetches_exceed_source_task_budget = 0
    execution_retries_exceed_source_task_budget = 0
    for execution in executions:
        for actual_key, config_key in (
            ("llm_calls", "max_llm_calls_per_candidate"),
            ("source_tasks", "max_source_tasks_per_candidate"),
            ("fetches", "max_fetches_per_candidate"),
            ("retries", "max_retries_per_candidate"),
            (
                "general_web_fetches",
                "max_general_web_fetches_per_candidate",
            ),
        ):
            actual = _safe_nonnegative_int(execution.get(actual_key))
            maximum = _safe_nonnegative_int(config.get(config_key))
            if actual < 0 or maximum < 0 or actual > maximum:
                per_candidate_budget_violation += 1
        task_refs = tuple(
            str(item) for item in execution.get("source_task_ids") or ()
        )
        referenced_source_task_ids.extend(task_refs)
        execution_tasks = tuple(source_task_by_id.get(item) for item in task_refs)
        target_id = str(execution.get("target_id") or "")
        declared_task_count = _safe_nonnegative_int(
            execution.get("source_tasks")
        )
        if (
            len(task_refs) != len(set(task_refs))
            or declared_task_count != len(task_refs)
            or any(item is None for item in execution_tasks)
            or any(
                item is not None
                and str(item.get("target_id") or "") != target_id
                for item in execution_tasks
            )
        ):
            execution_source_task_reference_mismatch += 1
        task_fetch_budget = sum(
            _safe_nonnegative_int(item.get("max_fetches"))
            for item in execution_tasks
            if item is not None
        )
        task_retry_budget = sum(
            _safe_nonnegative_int(item.get("max_retries"))
            for item in execution_tasks
            if item is not None
        )
        if (
            any(
                _safe_nonnegative_int(item.get("max_fetches")) < 0
                for item in execution_tasks
                if item is not None
            )
            or _safe_nonnegative_int(execution.get("fetches"))
            > task_fetch_budget
        ):
            execution_fetches_exceed_source_task_budget += 1
        if (
            any(
                _safe_nonnegative_int(item.get("max_retries")) < 0
                for item in execution_tasks
                if item is not None
            )
            or _safe_nonnegative_int(execution.get("retries"))
            > task_retry_budget
        ):
            execution_retries_exceed_source_task_budget += 1
        if _safe_nonnegative_int(execution.get("general_web_fetches")) > 0 and (
            execution.get("official_first_attempted") is not True
            or not execution.get("official_gap_reasons")
            or not any(
                item is not None and item.get("allows_general_web") is True
                for item in execution_tasks
            )
        ):
            general_web_without_official_gap += 1
        if (
            config.get("test_mode") is False
            and execution.get("provider_kind") == DailyProviderKind.FIXTURE.value
        ):
            fixture_provider_in_production += 1
    execution_runtimes = tuple(
        _safe_nonnegative_float(item.get("runtime_seconds"))
        for item in executions
    )
    total_runtime = sum(execution_runtimes)
    max_runtime = _safe_nonnegative_float(config.get("max_runtime_seconds"))

    source_task_unbounded_or_no_stop = 0
    source_task_fixture_in_production = 0
    source_task_general_web_without_official_gap = 0
    for task in source_tasks:
        positive_budgets = tuple(
            _safe_nonnegative_int(task.get(key))
            for key in ("max_queries", "max_candidates", "max_fetches")
        )
        retry_budget = _safe_nonnegative_int(task.get("max_retries"))
        if (
            any(value <= 0 for value in positive_budgets)
            or positive_budgets[0] > 10
            or positive_budgets[1] > 100
            or positive_budgets[2] > 20
            or retry_budget < 0
            or retry_budget > 3
            or task.get("stop_condition") != "stop_on_resolution"
        ):
            source_task_unbounded_or_no_stop += 1
        if config.get("test_mode") is False and task.get("test_only") is True:
            source_task_fixture_in_production += 1
        if task.get("allows_general_web") is True and (
            task.get("official_first_attempted") is not True
            or not task.get("official_gap_reasons")
        ):
            source_task_general_web_without_official_gap += 1

    stage_decision_mismatch = 0
    pending_final_score = 0
    for status in statuses:
        decision_id = str(status.get("atomic_decision_id") or "")
        decision = decision_by_id.get(decision_id)
        if decision_id:
            if decision is None or any(
                status.get(status_key) != decision.get(decision_key)
                for status_key, decision_key in (
                    ("canonical_stage", "canonical_stage"),
                    ("score_type", "score_type"),
                    ("score_value", "score_value"),
                    ("raw_reference_score", "raw_reference_score"),
                    ("score_valid", "score_valid"),
                    ("score_finalization_allowed", "score_finalization_allowed"),
                )
            ):
                stage_decision_mismatch += 1
            elif tuple(status.get("accepted_claim_ids") or ()) != tuple(
                dict.fromkeys(
                    (
                        *(decision.get("accepted_claim_ids") or ()),
                        *(decision.get("hard_break_claim_ids") or ()),
                    )
                )
            ):
                stage_decision_mismatch += 1
        elif (
            status.get("score_type") != AtomicScoreType.NO_SCORE.value
            or status.get("score_value") is not None
            or status.get("canonical_stage")
            not in {CanonicalStage.STAGE_0.value, CanonicalStage.STAGE_1.value}
        ):
            stage_decision_mismatch += 1
        terminal = str(status.get("terminal_status") or "")
        if terminal in {
            DailyTerminalStatus.PROVIDER_PENDING.value,
            DailyTerminalStatus.SOURCE_PENDING.value,
        } and (
            status.get("score_type") != AtomicScoreType.NO_SCORE.value
            or status.get("score_value") is not None
            or status.get("score_finalization_allowed") is True
        ):
            pending_final_score += 1
        if terminal == DailyTerminalStatus.BUDGET_PENDING.value and (
            status.get("score_type") == AtomicScoreType.FULL_E2R_100.value
            or status.get("score_finalization_allowed") is True
        ):
            pending_final_score += 1

    watchlist_missing_required_field = 0
    watchlist_recommendation_language = 0
    required_watchlist_fields = {
        "score_type",
        "confidence",
        "claim_ids",
        "missing_conditions",
        "gap_ids",
        "next_action",
    }
    for item in watchlist:
        if not required_watchlist_fields.issubset(item):
            watchlist_missing_required_field += 1
        safety_text = " ".join(
            (
                str(item.get("next_action") or ""),
                str(item.get("monitoring_label") or ""),
            )
        ).casefold()
        if any(term.casefold() in safety_text for term in _FORBIDDEN_WATCHLIST_TERMS):
            watchlist_recommendation_language += 1
    watchlist_projection_mismatch = sum(
        target_id not in status_by_target
        or any(
            item.get(key) != status_by_target[target_id].get(status_key)
            for key, status_key in (
                ("canonical_stage", "canonical_stage"),
                ("terminal_status", "terminal_status"),
                ("score_type", "score_type"),
                ("score_value", "score_value"),
                ("confidence", "confidence"),
                ("next_action", "next_action"),
            )
        )
        for item in watchlist
        for target_id in (str(item.get("target_id") or ""),)
    )
    watchlist_target_ids = tuple(
        str(item.get("target_id") or "") for item in watchlist
    )
    expected_watchlist_target_ids = {
        str(item.get("target_id") or "")
        for item in statuses
        if item.get("trigger_signal_ids")
        or item.get("accepted_claim_ids")
        or item.get("terminal_status")
        != DailyTerminalStatus.BASELINE_ONLY.value
    }

    forbidden_config_keys = {
        "recent_lookback_days",
        "stage_cutoff_days",
        "recent_cutoff",
        "sector_sample_quota",
        "archetype_quota",
        "force_registry_materialization",
    }
    required_config_keys = {
        "max_official_light_targets",
        "max_deep_candidates",
        "max_brain_candidates",
        "max_acquisition_candidates",
        "max_llm_calls_per_candidate",
        "max_source_tasks_per_candidate",
        "max_fetches_per_candidate",
        "max_retries_per_candidate",
        "max_general_web_fetches_per_candidate",
        "max_runtime_seconds",
        "test_mode",
        "require_claim_provenance",
    }
    positive_config_keys = {
        "max_official_light_targets",
        "max_deep_candidates",
        "max_brain_candidates",
        "max_acquisition_candidates",
        "max_llm_calls_per_candidate",
        "max_source_tasks_per_candidate",
        "max_fetches_per_candidate",
    }
    nonnegative_config_keys = {
        "max_retries_per_candidate",
        "max_general_web_fetches_per_candidate",
    }
    unbounded_config = int(
        not required_config_keys.issubset(config)
        or any(
            _safe_nonnegative_int(config.get(key)) <= 0
            for key in positive_config_keys
        )
        or any(
            _safe_nonnegative_int(config.get(key)) < 0
            for key in nonnegative_config_keys
        )
        or _safe_nonnegative_float(config.get("max_runtime_seconds")) <= 0.0
        or not isinstance(config.get("test_mode"), bool)
        or not isinstance(config.get("require_claim_provenance"), bool)
        or (
            config.get("test_mode") is True
            and config.get("require_claim_provenance") is True
        )
    )
    nested_depth_budget_violation = int(
        any(
            value < 0
            for value in (max_deep, max_brain, max_acquisition)
        )
        or not max_acquisition <= max_brain <= max_deep
    )
    atomic_audit = audit_atomic_stage_decisions(decisions)
    decision_claim_not_in_current_ledger = sum(
        1
        for decision in decisions
        for claim in _mapping_rows(decision.get("claims"))
        if str(claim.get("claim_id") or "") not in claim_by_id
        or claim_by_id[str(claim.get("claim_id") or "")] != claim
    )
    execution_decision_reference_mismatch = 0
    for execution in executions:
        target_id = str(execution.get("target_id") or "")
        decision_id = str(execution.get("atomic_decision_id") or "")
        decision = decision_by_id.get(decision_id)
        if decision_id and (
            decision is None or str(decision.get("target_id") or "") != target_id
        ):
            execution_decision_reference_mismatch += 1
            continue
        outcome = str(execution.get("outcome") or "")
        if outcome == CurrentDeepOutcome.FULL_THESIS.value and (
            decision is None
            or decision.get("score_type") != AtomicScoreType.FULL_E2R_100.value
            or decision.get("score_finalization_allowed") is not True
            or decision.get("material_gap_ids")
            or decision.get("hard_break_claim_ids")
        ):
            execution_decision_reference_mismatch += 1
        elif outcome == CurrentDeepOutcome.DISPROVED.value and (
            decision is None
            or decision.get("score_type") != AtomicScoreType.NO_SCORE.value
            or not decision.get("hard_break_claim_ids")
        ):
            execution_decision_reference_mismatch += 1
        elif outcome == CurrentDeepOutcome.SOURCE_PENDING.value and (
            decision is not None
            and (
                decision.get("score_type") != AtomicScoreType.NO_SCORE.value
                or decision.get("source_pending") is not True
            )
        ):
            execution_decision_reference_mismatch += 1
        elif outcome == CurrentDeepOutcome.PROVIDER_PENDING.value and (
            decision is not None
            and (
                decision.get("score_type") != AtomicScoreType.NO_SCORE.value
                or decision.get("provider_pending") is not True
            )
        ):
            execution_decision_reference_mismatch += 1
        elif outcome == CurrentDeepOutcome.BUDGET_PENDING.value and (
            decision is not None
            and decision.get("score_type") == AtomicScoreType.FULL_E2R_100.value
        ):
            execution_decision_reference_mismatch += 1
    critical = {
        "full_universe_duplicate_target": len(universe_ids) - len(set(universe_ids)),
        "universe_symbol_without_status": len(set(universe_ids) - set(status_ids)),
        "status_outside_universe": len(set(status_ids) - set(universe_ids)),
        "eligible_symbol_without_status": len(eligible_ids - set(status_ids)),
        "duplicate_census_stage_status": len(status_ids) - len(set(status_ids)),
        "source_timeline_coverage_gap": len(set(universe_ids) - set(timeline_ids)),
        "duplicate_source_timeline": len(timeline_ids) - len(set(timeline_ids)),
        "last_effective_thesis_coverage_gap": len(set(universe_ids) - set(thesis_ids)),
        "duplicate_last_effective_thesis": len(thesis_ids) - len(set(thesis_ids)),
        "depth_policy_coverage_gap": len(set(universe_ids) - set(depth_ids)),
        "duplicate_depth_decision": len(depth_ids) - len(set(depth_ids)),
        "required_baseline_lane_missing": baseline_lane_missing,
        "duplicate_baseline_lane": baseline_lane_duplicate,
        "future_data_leakage": future_count,
        "duplicate_claim_provenance_id": len(provenance_ids)
        - len(set(provenance_ids)),
        "duplicate_claim_provenance_claim": len(provenance_claim_ids)
        - len(set(provenance_claim_ids)),
        "claim_provenance_contract_failure": (
            claim_provenance_contract_failure
        ),
        "decision_claim_without_required_provenance": (
            decision_claim_without_required_provenance
        ),
        "recent_lookback_stage_cutoff": sum(
            item.get("recent_cutoff_applied") is True
            for item in (*theses, *statuses)
        ),
        "current_open_claim_dropped_by_lookback": current_open_claim_dropped,
        "current_open_claim_missing_from_timeline": (
            current_open_claim_missing_from_timeline
        ),
        "thesis_claim_lineage_mismatch": thesis_claim_lineage_mismatch,
        "trigger_used_as_score_evidence": trigger_score_evidence_count,
        "market_news_used_as_score_evidence": market_news_score_evidence_count,
        "selected_deep_budget_exceeded": int(
            max_deep < 0 or len(selected_ids) > max_deep
        ),
        "selected_deep_without_terminal_outcome": len(selected_ids - execution_ids),
        "execution_outside_selected_deep": len(execution_ids - selected_ids),
        "duplicate_deep_execution_id": len(execution_record_ids)
        - len(set(execution_record_ids)),
        "duplicate_deep_execution_target": len(execution_target_ids)
        - len(set(execution_target_ids)),
        "duplicate_source_task_id": len(source_task_ids)
        - len(set(source_task_ids)),
        "source_task_outside_selected_deep": sum(
            str(item.get("target_id") or "") not in selected_ids
            for item in source_tasks
        ),
        "source_task_unreferenced_or_duplicate": (
            len(referenced_source_task_ids)
            - len(set(referenced_source_task_ids))
            + len(set(source_task_ids) - set(referenced_source_task_ids))
            + len(set(referenced_source_task_ids) - set(source_task_ids))
        ),
        "source_task_unbounded_or_no_stop": source_task_unbounded_or_no_stop,
        "source_task_fixture_in_production": source_task_fixture_in_production,
        "execution_source_task_reference_mismatch": (
            execution_source_task_reference_mismatch
        ),
        "execution_fetches_exceed_source_task_budget": (
            execution_fetches_exceed_source_task_budget
        ),
        "execution_retries_exceed_source_task_budget": (
            execution_retries_exceed_source_task_budget
        ),
        "llm_outside_selected_deep": len(llm_targets - selected_ids),
        "all_symbol_llm_execution": int(
            bool(eligible_ids)
            and llm_targets == eligible_ids
        ),
        "all_symbol_general_web_execution": int(
            bool(eligible_ids)
            and general_web_targets == eligible_ids
        ),
        "brain_target_budget_exceeded": int(
            max_brain < 0 or len(llm_targets) > max_brain
        ),
        "acquisition_target_budget_exceeded": int(
            max_acquisition < 0 or len(acquisition_targets) > max_acquisition
        ),
        "official_light_budget_exceeded": int(
            max_official < 0 or official_light_count > max_official
        ),
        "per_candidate_budget_exceeded": per_candidate_budget_violation,
        "runtime_budget_exceeded": int(
            max_runtime < 0
            or any(value < 0 for value in execution_runtimes)
            or total_runtime > max_runtime
        ),
        "unbounded_production_config": unbounded_config,
        "nested_depth_budget_violation": nested_depth_budget_violation,
        "forbidden_quota_or_recent_cutoff_config": len(
            forbidden_config_keys.intersection(config)
        ),
        "fixture_provider_in_production": fixture_provider_in_production,
        "general_web_without_official_gap": general_web_without_official_gap,
        "source_task_general_web_without_official_gap": (
            source_task_general_web_without_official_gap
        ),
        "stage_score_without_atomic_decision": stage_decision_mismatch,
        "atomic_decision_integrity_failure": atomic_audit["critical_count_sum"],
        "decision_claim_not_in_current_ledger": (
            decision_claim_not_in_current_ledger
        ),
        "execution_decision_reference_mismatch": (
            execution_decision_reference_mismatch
        ),
        "pending_final_score": pending_final_score,
        "watchlist_missing_required_field": watchlist_missing_required_field,
        "watchlist_projection_mismatch": watchlist_projection_mismatch,
        "watchlist_coverage_gap": len(
            expected_watchlist_target_ids - set(watchlist_target_ids)
        ),
        "duplicate_watchlist_target": len(watchlist_target_ids)
        - len(set(watchlist_target_ids)),
        "watchlist_outside_expected_status": len(
            set(watchlist_target_ids) - expected_watchlist_target_ids
        ),
        "watchlist_recommendation_language": watchlist_recommendation_language,
        "broken_status_timeline_reference": sum(
            str(item.get("source_timeline_id") or "")
            != str(
                timeline_by_target.get(
                    str(item.get("target_id") or ""), {}
                ).get("timeline_id")
                or ""
            )
            for item in statuses
        ),
        "broken_status_thesis_reference": sum(
            str(item.get("thesis_id") or "")
            != str(
                thesis_by_target.get(
                    str(item.get("target_id") or ""), {}
                ).get("thesis_id")
                or ""
            )
            for item in statuses
        ),
        "eligible_symbol_missing_l0_l1": sum(
            target_id not in depth_by_target
            or not {
                CensusDepthLevel.L0_UNIVERSE.value,
                CensusDepthLevel.L1_BASELINE.value,
            }.issubset(set(depth_by_target[target_id].get("completed_depths") or ()))
            for target_id in eligible_ids
        ),
    }
    leaf_payload = _mapping_leaf_payload(payload)
    return {
        "schema_version": CURRENT_OPERATION_RUNNER_AUDIT_SCHEMA_VERSION,
        "status": (
            "BOUNDED_DAILY_CENSUS_PASS"
            if leaf_payload and sum(critical.values()) == 0
            else "BOUNDED_DAILY_CENSUS_FAIL"
        ),
        "full_universe_count": len(universe),
        "eligible_universe_count": len(eligible_ids),
        "baseline_lane_count": len(lanes),
        "source_task_count": len(source_tasks),
        "selected_deep_candidate_count": len(selected_ids),
        "deep_terminal_outcome_count": len(executions),
        "watchlist_count": len(watchlist),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "result_hash": stable_hash(leaf_payload),
        "production_runtime_ready": False,
    }


def write_current_daily_census(
    result: CurrentOperationRunnerResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    mode_marker = claim_mode_output_root(
        root,
        mode=CanonicalRunMode.CURRENT_OPERATION,
        run_id=result.run_id,
    )
    paths = {
        "mode_marker": mode_marker,
        "manifest": root / "current_daily_census_manifest.json",
        "audit": root / "current_daily_census_audit.json",
        "universe": root / "current_daily_universe.jsonl",
        "baseline": root / "current_daily_baseline_lanes.jsonl",
        "claim_provenance": root / "current_daily_claim_provenance.jsonl",
        "source_tasks": root / "current_daily_source_tasks.jsonl",
        "timelines": root / "current_daily_source_timelines.jsonl",
        "theses": root / "current_daily_last_effective_theses.jsonl",
        "depths": root / "current_daily_depth_decisions.jsonl",
        "executions": root / "current_daily_deep_executions.jsonl",
        "decisions": root / "current_daily_atomic_decisions.jsonl",
        "statuses": root / "current_daily_census_stage_statuses.jsonl",
        "watchlist": root / "current_daily_watchlist.jsonl",
        "report": root / "current_daily_census_report.md",
    }
    write_json(paths["manifest"], result.manifest)
    write_json(paths["audit"], result.audit)
    write_jsonl(paths["universe"], (item.to_dict() for item in result.universe))
    write_jsonl(
        paths["baseline"],
        (item.to_dict() for item in result.baseline_lanes),
    )
    write_jsonl(
        paths["claim_provenance"],
        (item.to_dict() for item in result.claim_provenance),
    )
    write_jsonl(
        paths["source_tasks"],
        (item.to_dict() for item in result.source_tasks),
    )
    write_jsonl(
        paths["timelines"],
        (item.to_dict() for item in result.source_timelines),
    )
    write_jsonl(paths["theses"], (item.to_dict() for item in result.thesis_states))
    write_jsonl(
        paths["depths"],
        (item.to_dict() for item in result.depth_decisions),
    )
    write_jsonl(
        paths["executions"],
        (item.to_dict() for item in result.deep_executions),
    )
    write_jsonl(
        paths["decisions"],
        (item.to_dict() for item in result.atomic_decisions),
    )
    write_jsonl(
        paths["statuses"],
        (item.to_dict() for item in result.stage_statuses),
    )
    write_jsonl(paths["watchlist"], (item.to_dict() for item in result.watchlist))
    write_text(paths["report"], render_current_daily_census_report(result.manifest))
    return paths


def render_current_daily_census_report(manifest: Mapping[str, Any]) -> str:
    return "\n".join(
        (
            "# Bounded Current Daily Census",
            "",
            f"- status: {manifest['status']}",
            f"- as_of_date: {manifest['as_of_date']}",
            f"- full universe: {manifest['full_universe_count']}",
            (
                "- baseline lanes: "
                f"{manifest['baseline_lane_count']}/"
                f"{manifest['required_baseline_lane_count']}"
            ),
            (
                "- bounded selected deep: "
                f"{manifest['selected_deep_candidate_count']}/"
                f"{manifest['max_deep_candidates']}"
            ),
            f"- bounded SourceTask leaves: {manifest['source_task_count']}",
            f"- terminal outcomes: {manifest['deep_outcome_counts']}",
            f"- depth coverage: {manifest['depth_counts']}",
            f"- watchlist rows: {manifest['watchlist_count']}",
            "- market/news trigger score evidence: 0",
            "- recent Stage cutoff: 0",
            "- archetype quota: 0",
            f"- critical_count_sum: {manifest['critical_count_sum']}",
            "- production_runtime_ready: false",
            "",
        )
    )


def load_current_operation_runner_input(
    path: str | Path,
) -> CurrentOperationRunnerInput:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError("current operation input manifest must be an object")
    return current_operation_runner_input_from_mapping(payload)


def current_operation_runner_input_from_mapping(
    payload: Mapping[str, Any],
) -> CurrentOperationRunnerInput:
    if payload.get("schema_version") != CURRENT_OPERATION_RUNNER_SCHEMA_VERSION:
        raise ValueError("current operation input schema version mismatch")
    return CurrentOperationRunnerInput(
        as_of_date=str(payload.get("as_of_date") or ""),
        universe=tuple(
            DailyUniverseMember(**dict(item))
            for item in _mapping_rows(payload.get("universe"))
        ),
        baseline_lanes=tuple(
            DailyBaselineLane(
                target_id=str(item.get("target_id") or ""),
                as_of_date=str(item.get("as_of_date") or ""),
                lane_type=str(item.get("lane_type") or ""),
                lane_status=str(item.get("lane_status") or ""),
                source_ids=tuple(item.get("source_ids") or ()),
                observed_date=item.get("observed_date"),
                provider_error=item.get("provider_error"),
            )
            for item in _mapping_rows(payload.get("baseline_lanes"))
        ),
        triggers=tuple(
            CurrentTriggerSignal(**dict(item))
            for item in _mapping_rows(payload.get("triggers"))
        ),
        claims=tuple(
            _atomic_claim_from_mapping(item)
            for item in _mapping_rows(payload.get("claims"))
        ),
        claim_provenance=tuple(
            DailyClaimProvenance(
                **{
                    **dict(item),
                    "source_ids": tuple(item.get("source_ids") or ()),
                    "anchor_ids": tuple(item.get("anchor_ids") or ()),
                    "mapping_ids": tuple(item.get("mapping_ids") or ()),
                }
            )
            for item in _mapping_rows(payload.get("claim_provenance"))
        ),
        source_tasks=tuple(
            DailySourceTaskRecord(
                **{
                    **dict(item),
                    "official_gap_reasons": tuple(
                        item.get("official_gap_reasons") or ()
                    ),
                }
            )
            for item in _mapping_rows(payload.get("source_tasks"))
        ),
        atomic_decisions=tuple(
            atomic_stage_decision_from_mapping(item)
            for item in _mapping_rows(payload.get("atomic_decisions"))
        ),
        deep_executions=tuple(
            DailyDeepExecution(
                **{
                    **dict(item),
                    "trigger_signal_ids": tuple(
                        item.get("trigger_signal_ids") or ()
                    ),
                    "source_task_ids": tuple(
                        item.get("source_task_ids") or ()
                    ),
                    "official_gap_reasons": tuple(
                        item.get("official_gap_reasons") or ()
                    ),
                }
            )
            for item in _mapping_rows(payload.get("deep_executions"))
        ),
        config=CurrentOperationRunnerConfig(**dict(payload.get("config") or {})),
    )


def atomic_stage_decision_from_mapping(
    payload: Mapping[str, Any],
) -> AtomicStageDecision:
    data = dict(payload)
    data["claims"] = tuple(
        _atomic_claim_from_mapping(item)
        for item in _mapping_rows(payload.get("claims"))
    )
    data["score_rules"] = tuple(
        AtomicScoreRule(**dict(item))
        for item in _mapping_rows(payload.get("score_rules"))
    )
    stage_config = payload.get("stage_config")
    if not isinstance(stage_config, Mapping):
        raise ValueError("atomic decision stage config is missing")
    data["stage_config"] = AtomicStageConfig(**dict(stage_config))
    data["primitive_assessments"] = tuple(
        AtomicPrimitiveAssessment(
            **{
                **dict(item),
                "support_claim_ids": tuple(item.get("support_claim_ids") or ()),
                "counter_claim_ids": tuple(item.get("counter_claim_ids") or ()),
            }
        )
        for item in _mapping_rows(payload.get("primitive_assessments"))
    )
    data["contributions"] = tuple(
        AtomicScoreContribution(
            **{
                **dict(item),
                "support_claim_ids": tuple(item.get("support_claim_ids") or ()),
                "mapping_ids": tuple(item.get("mapping_ids") or ()),
            }
        )
        for item in _mapping_rows(payload.get("contributions"))
    )
    data["hard_break_signals"] = tuple(
        AtomicHardBreakSignal(**dict(item))
        for item in _mapping_rows(payload.get("hard_break_signals"))
    )
    trace = payload.get("stage_court_trace")
    if not isinstance(trace, Mapping):
        raise ValueError("atomic decision StageCourt trace is missing")
    data["stage_court_trace"] = AtomicStageCourtTrace(
        **{
            **dict(trace),
            "accepted_claim_ids": tuple(trace.get("accepted_claim_ids") or ()),
            "contribution_ids": tuple(trace.get("contribution_ids") or ()),
            "material_gap_ids": tuple(trace.get("material_gap_ids") or ()),
            "hard_break_claim_ids": tuple(
                trace.get("hard_break_claim_ids") or ()
            ),
            "reasons": tuple(trace.get("reasons") or ()),
        }
    )
    for field_name in (
        "accepted_claim_ids",
        "material_gap_ids",
        "missing_conditions",
        "hard_break_claim_ids",
        "rejected_hard_break_signal_ids",
    ):
        data[field_name] = tuple(payload.get(field_name) or ())
    return AtomicStageDecision(**data)


def _atomic_claim_from_mapping(payload: Mapping[str, Any]) -> AtomicScoreClaim:
    return AtomicScoreClaim(
        **{
            **dict(payload),
            "source_ids": tuple(payload.get("source_ids") or ()),
            "anchor_ids": tuple(payload.get("anchor_ids") or ()),
            "mapping_ids": tuple(payload.get("mapping_ids") or ()),
        }
    )


def _result_leaf_payload(
    result: CurrentOperationRunnerResult,
) -> Mapping[str, Any]:
    return _leaf_payload_from_parts(
        universe=result.universe,
        baseline_lanes=result.baseline_lanes,
        triggers=result.triggers,
        claims=result.claims,
        claim_provenance=result.claim_provenance,
        source_tasks=result.source_tasks,
        source_timelines=result.source_timelines,
        thesis_states=result.thesis_states,
        depth_decisions=result.depth_decisions,
        deep_executions=result.deep_executions,
        atomic_decisions=result.atomic_decisions,
        stage_statuses=result.stage_statuses,
        watchlist=result.watchlist,
        config=result.config,
    )


def _leaf_payload_from_parts(
    *,
    universe: Sequence[DailyUniverseMember],
    baseline_lanes: Sequence[DailyBaselineLane],
    triggers: Sequence[CurrentTriggerSignal],
    claims: Sequence[AtomicScoreClaim],
    claim_provenance: Sequence[DailyClaimProvenance],
    source_tasks: Sequence[DailySourceTaskRecord],
    source_timelines: Sequence[DailySourceTimeline],
    thesis_states: Sequence[DailyLastEffectiveThesis],
    depth_decisions: Sequence[DailyDepthDecision],
    deep_executions: Sequence[DailyDeepExecution],
    atomic_decisions: Sequence[AtomicStageDecision],
    stage_statuses: Sequence[DailyCensusStageStatus],
    watchlist: Sequence[CurrentWatchlistItem],
    config: CurrentOperationRunnerConfig,
) -> Mapping[str, Any]:
    return {
        "universe": [item.to_dict() for item in universe],
        "baseline_lanes": [item.to_dict() for item in baseline_lanes],
        "triggers": [item.to_dict() for item in triggers],
        "claims": [item.to_dict() for item in claims],
        "claim_provenance": [item.to_dict() for item in claim_provenance],
        "source_tasks": [item.to_dict() for item in source_tasks],
        "source_timelines": [item.to_dict() for item in source_timelines],
        "thesis_states": [item.to_dict() for item in thesis_states],
        "depth_decisions": [item.to_dict() for item in depth_decisions],
        "deep_executions": [item.to_dict() for item in deep_executions],
        "atomic_decisions": [item.to_dict() for item in atomic_decisions],
        "stage_statuses": [item.to_dict() for item in stage_statuses],
        "watchlist": [item.to_dict() for item in watchlist],
        "config": config.to_dict(),
    }


def _mapping_leaf_payload(payload: Mapping[str, Any]) -> Mapping[str, Any]:
    keys = (
        "universe",
        "baseline_lanes",
        "triggers",
        "claims",
        "claim_provenance",
        "source_tasks",
        "source_timelines",
        "thesis_states",
        "depth_decisions",
        "deep_executions",
        "atomic_decisions",
        "stage_statuses",
        "watchlist",
        "config",
    )
    return {key: payload.get(key) for key in keys}


def _mapping_rows(value: Any) -> tuple[Mapping[str, Any], ...]:
    if not isinstance(value, (list, tuple)):
        return ()
    return tuple(item for item in value if isinstance(item, Mapping))


def _is_production_source_url(value: str) -> bool:
    try:
        parsed = urlsplit(value)
    except ValueError:
        return False
    host = (parsed.hostname or "").casefold().rstrip(".")
    return bool(
        parsed.scheme in {"http", "https"}
        and host
        and host not in _NON_PRODUCTION_SOURCE_HOSTS
        and not host.endswith(
            (
                ".example.com",
                ".example.net",
                ".example.org",
                ".test",
                ".invalid",
                ".localhost",
            )
        )
    )


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


def _require_unique_text(
    values: Sequence[str],
    *,
    context: str,
    required: bool = True,
) -> None:
    if required and not values:
        raise ValueError(f"{context} cannot be empty")
    if any(not isinstance(item, str) or not item.strip() for item in values):
        raise ValueError(f"{context} contains empty text")
    if len(values) != len(set(values)):
        raise ValueError(f"{context} contains duplicates")


def _unique_by(
    values: Sequence[Any],
    *,
    key: Any,
    context: str,
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for item in values:
        identity = str(key(item))
        if not identity.strip() or identity in result:
            raise ValueError(f"duplicate or empty {context}: {identity}")
        result[identity] = item
    return result


__all__ = [
    "CURRENT_OPERATION_RUNNER_AUDIT_SCHEMA_VERSION",
    "CURRENT_OPERATION_RUNNER_SCHEMA_VERSION",
    "CensusDepthLevel",
    "CurrentOperationRunnerConfig",
    "CurrentOperationRunnerInput",
    "CurrentOperationRunnerResult",
    "CurrentWatchlistItem",
    "DailyBaselineLane",
    "DailyBaselineLaneStatus",
    "DailyBaselineLaneType",
    "DailyCensusStageStatus",
    "DailyClaimProvenance",
    "DailyConfidence",
    "DailyDeepExecution",
    "DailyDepthDecision",
    "DailyLastEffectiveThesis",
    "DailyNextAction",
    "DailyProviderKind",
    "DailySourceTimeline",
    "DailySourceTimelineEvent",
    "DailyTerminalStatus",
    "DailyThesisLifecycle",
    "DailyTimelineRole",
    "DailyUniverseMember",
    "atomic_stage_decision_from_mapping",
    "audit_current_daily_census",
    "current_operation_runner_input_from_mapping",
    "load_current_operation_runner_input",
    "render_current_daily_census_report",
    "run_current_daily_census",
    "write_current_daily_census",
]
