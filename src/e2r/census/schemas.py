"""Schemas for E2R Census Mode v1."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
from enum import Enum
from typing import Any, Mapping, Sequence


class CensusStatus(str, Enum):
    SCANNED = "SCANNED"
    LIGHT_ONLY = "LIGHT_ONLY"
    DEEP_VERIFIED = "DEEP_VERIFIED"
    PENDING_SOURCE = "PENDING_SOURCE"
    PENDING_PROVIDER = "PENDING_PROVIDER"
    SKIPPED_INELIGIBLE = "SKIPPED_INELIGIBLE"
    FAILED = "FAILED"


class AssessmentDepth(str, Enum):
    UNIVERSE_ONLY = "UNIVERSE_ONLY"
    CHEAP_BASELINE = "CHEAP_BASELINE"
    OFFICIAL_LIGHT = "OFFICIAL_LIGHT"
    RESEARCH_BRAIN_TRIAGE = "RESEARCH_BRAIN_TRIAGE"
    DEEP_DOSSIER = "DEEP_DOSSIER"
    VERIFIED_STAGE = "VERIFIED_STAGE"


class BaseStage(str, Enum):
    STAGE0 = "Stage0"
    STAGE1 = "Stage1"
    STAGE2_WATCH = "Stage2-Watch"
    STAGE2_ACTIONABLE = "Stage2-Actionable"
    STAGE3_YELLOW = "Stage3-Yellow"
    STAGE3_GREEN = "Stage3-Green"
    REJECT = "Reject"
    RED = "Red"
    UNKNOWN = "Unknown"


class InvestigationStatus(str, Enum):
    COMPLETE = "COMPLETE"
    PENDING = "PENDING"
    EXHAUSTED = "EXHAUSTED"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    RUNTIME_BUDGET_EXHAUSTED = "RUNTIME_BUDGET_EXHAUSTED"
    NO_CURRENT_CATALYST = "NO_CURRENT_CATALYST"


class TransitionOverlay(str, Enum):
    NONE = "NONE"
    STAGE4A = "4A"
    STAGE4B = "4B"
    STAGE4C = "4C"


class StageConfidence(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


class ScoreValidStatus(str, Enum):
    FINAL = "FINAL"
    FINAL_WITH_NONMATERIAL_GAPS = "FINAL_WITH_NONMATERIAL_GAPS"
    PENDING_MATERIAL_GAPS = "PENDING_MATERIAL_GAPS"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    NO_CURRENT_EVENT = "NO_CURRENT_EVENT"
    INVALID_EVIDENCE = "INVALID_EVIDENCE"
    NOT_SCORED = "NOT_SCORED"


class InstrumentType(str, Enum):
    COMMON = "COMMON"
    PREFERRED = "PREFERRED"
    SPAC = "SPAC"
    ETF = "ETF"
    REIT = "REIT"
    ETN = "ETN"
    OTHER = "OTHER"


class DepthLevel(str, Enum):
    L0_UNIVERSE_ONLY = "L0_UNIVERSE_ONLY"
    L1_CHEAP_BASELINE = "L1_CHEAP_BASELINE"
    L2_OFFICIAL_LIGHT = "L2_OFFICIAL_LIGHT"
    L3_RESEARCH_BRAIN_TRIAGE = "L3_RESEARCH_BRAIN_TRIAGE"
    L4_DEEP_DOSSIER = "L4_DEEP_DOSSIER"
    L5_VERIFIED_STAGE = "L5_VERIFIED_STAGE"


class SourceTaskStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    FETCHED = "FETCHED"
    PARSED = "PARSED"
    EVIDENCE_OS_ACCEPTED = "EVIDENCE_OS_ACCEPTED"
    NO_EVIDENCE_FOUND = "NO_EVIDENCE_FOUND"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    BUDGET_EXHAUSTED = "BUDGET_EXHAUSTED"
    SKIPPED_BY_DEPTH_POLICY = "SKIPPED_BY_DEPTH_POLICY"


def _tuple(value: Sequence[Any] | None) -> tuple[Any, ...]:
    return tuple(value or ())


def _clean_strings(value: Sequence[str] | None) -> tuple[str, ...]:
    return tuple(dict.fromkeys(str(item).strip() for item in (value or ()) if str(item).strip()))


def _enum_value(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, tuple):
        return [_enum_value(item) for item in value]
    if isinstance(value, list):
        return [_enum_value(item) for item in value]
    if isinstance(value, dict):
        return {str(k): _enum_value(v) for k, v in value.items()}
    return value


def to_plain_dict(obj: Any) -> dict[str, Any]:
    return {key: _enum_value(value) for key, value in asdict(obj).items()}


@dataclass(frozen=True)
class UniverseInstrument:
    symbol: str
    company_name: str
    market: str
    instrument_type: InstrumentType = InstrumentType.COMMON
    is_active: bool = True
    listing_status: str = "ACTIVE"
    large_sector_id: str | None = None
    sector_source: str = "unknown"
    eligible_for_census: bool = True
    exclusion_reason: str | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "symbol", str(self.symbol).strip().zfill(6))
        object.__setattr__(self, "company_name", str(self.company_name).strip())
        object.__setattr__(self, "market", str(self.market).strip() or "UNKNOWN")
        object.__setattr__(self, "instrument_type", InstrumentType(self.instrument_type))

    def to_dict(self) -> dict[str, Any]:
        return to_plain_dict(self)


@dataclass(frozen=True)
class CensusAssessmentEvent:
    assessment_event_id: str
    symbol: str
    company_name: str
    as_of_date: str
    assessment_type: str = "baseline_census"
    source_family: str = "FullUniverseCensus"
    reason: str = "periodic full-universe E2R stage assessment"
    universe_source: str = "KRX"
    instrument_status: str = "ACTIVE"
    market: str = "KOSPI"
    large_sector_id: str | None = None
    existing_watchlist_status: str | None = None
    recent_candidate_events: tuple[str, ...] = ()
    recent_claim_ledger_refs: tuple[str, ...] = ()
    baseline_scan_refs: tuple[str, ...] = ()
    eligible_for_deep_dossier: bool = False

    @property
    def score_evidence_eligible(self) -> bool:
        return False

    def to_dict(self) -> dict[str, Any]:
        payload = to_plain_dict(self)
        payload["score_evidence_eligible"] = False
        return payload


@dataclass(frozen=True)
class BaselineScanResult:
    symbol: str
    as_of_date: str
    scan_status: str = "SCANNED"
    recent_disclosure_count: int = 0
    recent_supply_contract_count: int = 0
    recent_facility_investment_count: int = 0
    recent_earnings_event_count: int = 0
    recent_risk_event_count: int = 0
    revision_signal_count: int = 0
    price_anomaly_count: int = 0
    relative_strength_rank: float | None = None
    trading_value_rank: float | None = None
    existing_claim_count: int = 0
    existing_stage: str | None = None
    provider_errors: tuple[str, ...] = ()
    reason_codes: tuple[str, ...] = ()
    trigger_priority_score: float = 0.0

    def __post_init__(self) -> None:
        object.__setattr__(self, "provider_errors", _clean_strings(self.provider_errors))
        object.__setattr__(self, "reason_codes", _clean_strings(self.reason_codes))

    @property
    def has_current_event(self) -> bool:
        return any(
            value > 0
            for value in (
                self.recent_disclosure_count,
                self.recent_supply_contract_count,
                self.recent_facility_investment_count,
                self.recent_earnings_event_count,
                self.recent_risk_event_count,
                self.revision_signal_count,
                self.existing_claim_count,
            )
        )

    @property
    def has_provider_failure(self) -> bool:
        return self.scan_status == "PROVIDER_FAILED" or bool(self.provider_errors)

    @property
    def market_only_signal(self) -> bool:
        return self.price_anomaly_count > 0 and not self.has_current_event and not self.has_provider_failure

    def to_dict(self) -> dict[str, Any]:
        return to_plain_dict(self)


@dataclass(frozen=True)
class DepthDecision:
    symbol: str
    recommended_depth: DepthLevel
    reason: str
    expected_runtime_cost: str = "LOW"
    source_task_budget: Mapping[str, Any] = field(default_factory=dict)
    llm_budget: Mapping[str, Any] = field(default_factory=dict)
    must_not_deepen_reason: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return to_plain_dict(self)


@dataclass(frozen=True)
class SourceTask:
    task_id: str
    symbol: str
    depth_level: DepthLevel
    task_class: str
    source_class: str
    budget: Mapping[str, int]
    stop_condition: str = "stop_on_resolution"
    allows_general_web: bool = False
    reason: str = ""

    def __post_init__(self) -> None:
        object.__setattr__(self, "depth_level", DepthLevel(self.depth_level))
        if not self.budget:
            raise ValueError("SourceTask budget must be non-empty")
        if any(value is None for value in self.budget.values()):
            raise ValueError("SourceTask budget values cannot be None")

    def to_dict(self) -> dict[str, Any]:
        return to_plain_dict(self)


@dataclass(frozen=True)
class SourceTaskExecution:
    task_id: str
    symbol: str
    depth_level: DepthLevel
    source_class: str
    status: SourceTaskStatus
    accepted_claim_ids: tuple[str, ...] = ()
    provider_errors: tuple[str, ...] = ()
    budget_used: Mapping[str, int] = field(default_factory=dict)
    stop_reason: str = ""

    def __post_init__(self) -> None:
        object.__setattr__(self, "depth_level", DepthLevel(self.depth_level))
        object.__setattr__(self, "status", SourceTaskStatus(self.status))
        object.__setattr__(self, "accepted_claim_ids", _clean_strings(self.accepted_claim_ids))
        object.__setattr__(self, "provider_errors", _clean_strings(self.provider_errors))

    def to_dict(self) -> dict[str, Any]:
        return to_plain_dict(self)


@dataclass(frozen=True)
class CensusStageStatus:
    symbol: str
    company_name: str
    as_of_date: str
    census_status: CensusStatus
    assessment_depth: AssessmentDepth
    base_stage: BaseStage
    investigation_status: InvestigationStatus
    transition_overlay: TransitionOverlay = TransitionOverlay.NONE
    stage_confidence: StageConfidence = StageConfidence.INSUFFICIENT_EVIDENCE
    score_valid_status: ScoreValidStatus = ScoreValidStatus.NOT_SCORED
    trigger_priority_score: float | None = None
    verified_score: float | None = None
    provisional_score: float | None = None
    score_interval_lower: float | None = None
    score_interval_upper: float | None = None
    primary_archetype: str | None = None
    secondary_archetypes: tuple[str, ...] = ()
    large_sector_id: str | None = None
    accepted_claim_count: int = 0
    score_contribution_count: int = 0
    claim_backed_score_ratio: float = 0.0
    orphan_score_count: int = 0
    recent_event_count: int = 0
    recent_official_event_count: int = 0
    market_anomaly_count: int = 0
    risk_event_count: int = 0
    missing_primitives: tuple[str, ...] = ()
    failed_stage_gates: tuple[str, ...] = ()
    provider_gaps: tuple[str, ...] = ()
    source_gaps: tuple[str, ...] = ()
    next_actions: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "census_status", CensusStatus(self.census_status))
        object.__setattr__(self, "assessment_depth", AssessmentDepth(self.assessment_depth))
        object.__setattr__(self, "base_stage", BaseStage(self.base_stage))
        object.__setattr__(self, "investigation_status", InvestigationStatus(self.investigation_status))
        object.__setattr__(self, "transition_overlay", TransitionOverlay(self.transition_overlay))
        object.__setattr__(self, "stage_confidence", StageConfidence(self.stage_confidence))
        object.__setattr__(self, "score_valid_status", ScoreValidStatus(self.score_valid_status))
        for field_name in (
            "secondary_archetypes",
            "missing_primitives",
            "failed_stage_gates",
            "provider_gaps",
            "source_gaps",
            "next_actions",
        ):
            object.__setattr__(self, field_name, _clean_strings(getattr(self, field_name)))

    def to_dict(self) -> dict[str, Any]:
        return to_plain_dict(self)


def score_contribution_claim_ids(contribution: Mapping[str, Any]) -> tuple[str, ...]:
    ids = contribution.get("support_claim_ids") or contribution.get("accepted_claim_ids") or contribution.get("claim_ids") or ()
    return _clean_strings(ids)


def accepted_claim_id(claim: Mapping[str, Any]) -> str:
    return str(claim.get("claim_id") or claim.get("id") or "").strip()


__all__ = [
    "AssessmentDepth",
    "BaseStage",
    "BaselineScanResult",
    "CensusAssessmentEvent",
    "CensusStageStatus",
    "CensusStatus",
    "DepthDecision",
    "DepthLevel",
    "InstrumentType",
    "InvestigationStatus",
    "ScoreValidStatus",
    "SourceTask",
    "SourceTaskExecution",
    "SourceTaskStatus",
    "StageConfidence",
    "TransitionOverlay",
    "UniverseInstrument",
    "accepted_claim_id",
    "score_contribution_claim_ids",
    "to_plain_dict",
]
