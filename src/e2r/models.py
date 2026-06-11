"""Core E2R 2.0 data models.

The models are deliberately dependency-free. Validation is strict enough to
catch bad checkpoint fixtures without introducing a runtime framework yet.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum, IntEnum
from typing import Any, Mapping


class Market(str, Enum):
    """Supported equity markets."""

    KR = "KR"
    US = "US"


class SourceTier(IntEnum):
    """Evidence reliability tier, where lower values are more reliable."""

    TIER_0 = 0
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 3
    TIER_4 = 4
    TIER_5 = 5


class Stage(str, Enum):
    """Canonical E2R 2.0 state machine stages."""

    STAGE_0 = "0"
    STAGE_1 = "1"
    STAGE_2 = "2"
    STAGE_3_GREEN = "3-Green"
    STAGE_3_YELLOW = "3-Yellow"
    STAGE_3_RED = "3-Red"
    STAGE_4A = "4A"
    STAGE_4B = "4B"
    STAGE_4C = "4C"
    STAGE_5 = "5"


class ShortageType(str, Enum):
    """Supply-demand shortage type used by feature engineering."""

    NONE = "none"
    ONE_OFF = "one_off"
    CYCLICAL = "cyclical"
    STRUCTURAL = "structural"
    UNKNOWN = "unknown"


def _require_text(value: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")


def _require_date(value: date, field_name: str) -> None:
    if type(value) is not date:
        raise ValueError(f"{field_name} must be a date")


def _require_datetime(value: datetime, field_name: str) -> None:
    if not isinstance(value, datetime):
        raise ValueError(f"{field_name} must be a datetime")


def _require_non_negative(value: float | int | None, field_name: str) -> None:
    if value is not None and value < 0:
        raise ValueError(f"{field_name} must be non-negative")


def _require_positive(value: float | int | None, field_name: str) -> None:
    if value is not None and value <= 0:
        raise ValueError(f"{field_name} must be positive")


def _require_score(value: float | int, field_name: str, max_score: float = 100.0) -> None:
    if value < 0 or value > max_score:
        raise ValueError(f"{field_name} must be between 0 and {max_score}")


def _copy_mapping(value: Mapping[str, Any] | None) -> dict[str, Any]:
    return dict(value or {})


def _copy_tuple(value: tuple[str, ...] | list[str] | None) -> tuple[str, ...]:
    return tuple(value or ())


def _validate_temporal_evidence(
    *,
    published_at: datetime,
    observed_at: datetime,
    available_at: datetime,
    as_of_date: date,
) -> None:
    _require_datetime(published_at, "published_at")
    _require_datetime(observed_at, "observed_at")
    _require_datetime(available_at, "available_at")
    _require_date(as_of_date, "as_of_date")
    if observed_at < published_at:
        raise ValueError("observed_at cannot be before published_at")
    if available_at < observed_at:
        raise ValueError("available_at cannot be before observed_at")
    if available_at.date() > as_of_date:
        raise ValueError("available_at cannot be after as_of_date")


@dataclass(frozen=True)
class Evidence:
    """Point-in-time evidence behind a score or stage decision."""

    evidence_id: str
    source_type: str
    source_name: str
    source_tier: SourceTier
    published_at: datetime
    observed_at: datetime
    available_at: datetime
    as_of_date: date
    market: Market
    symbol: str
    title: str
    url_or_identifier: str | None = None
    excerpt_or_value: str | float | int | None = None
    parsed_fields: Mapping[str, Any] = field(default_factory=dict)
    confidence: float = 1.0

    def __post_init__(self) -> None:
        _require_text(self.evidence_id, "evidence_id")
        _require_text(self.source_type, "source_type")
        _require_text(self.source_name, "source_name")
        _require_text(self.symbol, "symbol")
        _require_text(self.title, "title")
        _require_score(self.confidence, "confidence", 1.0)
        _validate_temporal_evidence(
            published_at=self.published_at,
            observed_at=self.observed_at,
            available_at=self.available_at,
            as_of_date=self.as_of_date,
        )
        object.__setattr__(self, "parsed_fields", _copy_mapping(self.parsed_fields))


@dataclass(frozen=True)
class Instrument:
    """Listed equity instrument."""

    symbol: str
    name: str
    market: Market
    exchange: str
    sector_exchange: str | None = None
    sector_custom: str | None = None
    corp_code: str | None = None
    listed_date: date | None = None
    currency: str = "KRW"
    is_preferred: bool = False
    is_spac: bool = False
    is_reit: bool = False
    is_etf: bool = False
    is_managed: bool = False
    is_invest_warning: bool = False
    is_trading_halt: bool = False

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_text(self.name, "name")
        _require_text(self.exchange, "exchange")
        _require_text(self.currency, "currency")
        if self.listed_date is not None:
            _require_date(self.listed_date, "listed_date")


@dataclass(frozen=True)
class PriceBar:
    """Daily OHLCV record used for price stage and backtest metrics."""

    symbol: str
    date: date
    open: float
    high: float
    low: float
    close: float
    adj_close: float
    volume: int
    trading_value: float
    market_cap: float | None
    source: str
    as_of_date: date

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_text(self.source, "source")
        _require_date(self.date, "date")
        _require_date(self.as_of_date, "as_of_date")
        if self.as_of_date < self.date:
            raise ValueError("as_of_date cannot be before price date")
        for field_name in ("open", "high", "low", "close", "adj_close"):
            _require_positive(getattr(self, field_name), field_name)
        if self.low > self.high:
            raise ValueError("low cannot be greater than high")
        if self.close < self.low or self.close > self.high:
            raise ValueError("close must be inside low/high range")
        _require_non_negative(self.volume, "volume")
        _require_non_negative(self.trading_value, "trading_value")
        _require_positive(self.market_cap, "market_cap")


@dataclass(frozen=True)
class FinancialActual:
    """Reported financial data as available on a given date."""

    symbol: str
    fiscal_year: int
    fiscal_quarter: int | None
    period_end: date
    reported_at: datetime
    as_of_date: date
    source: str
    sales: float | None = None
    operating_profit: float | None = None
    net_income: float | None = None
    eps: float | None = None
    bps: float | None = None
    equity: float | None = None
    roe: float | None = None
    opm: float | None = None
    debt_ratio: float | None = None
    cashflow_from_operations: float | None = None
    capex: float | None = None
    fcf: float | None = None
    receivables: float | None = None
    inventory: float | None = None

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_text(self.source, "source")
        _require_date(self.period_end, "period_end")
        _require_datetime(self.reported_at, "reported_at")
        _require_date(self.as_of_date, "as_of_date")
        if self.fiscal_quarter is not None and self.fiscal_quarter not in (1, 2, 3, 4):
            raise ValueError("fiscal_quarter must be 1, 2, 3, 4, or None")
        if self.reported_at.date() > self.as_of_date:
            raise ValueError("reported_at cannot be after as_of_date")
        for field_name in ("sales", "bps", "equity", "receivables", "inventory"):
            _require_non_negative(getattr(self, field_name), field_name)


@dataclass(frozen=True)
class ConsensusSnapshot:
    """Consensus estimates known as of a date."""

    symbol: str
    date: date
    fiscal_year: int
    as_of_date: date
    source: str
    sales_e: float | None = None
    op_e: float | None = None
    net_income_e: float | None = None
    eps_e: float | None = None
    fcf_e: float | None = None
    bps_e: float | None = None
    roe_e: float | None = None
    per_e: float | None = None
    pbr_e: float | None = None
    analyst_count: int | None = None
    target_price: float | None = None
    target_multiple_type: str | None = None
    target_multiple: float | None = None
    parsed_fields: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_text(self.source, "source")
        _require_date(self.date, "date")
        _require_date(self.as_of_date, "as_of_date")
        if self.date > self.as_of_date:
            raise ValueError("consensus date cannot be after as_of_date")
        for field_name in ("sales_e", "fcf_e", "bps_e", "per_e", "pbr_e", "target_price", "target_multiple"):
            _require_non_negative(getattr(self, field_name), field_name)
        _require_non_negative(self.analyst_count, "analyst_count")
        object.__setattr__(self, "parsed_fields", _copy_mapping(self.parsed_fields))


@dataclass(frozen=True)
class ConsensusRevision:
    """Revision metrics known as of a date."""

    symbol: str
    date: date
    fiscal_year: int
    as_of_date: date
    eps_revision_1w: float | None = None
    eps_revision_1m: float | None = None
    eps_revision_3m: float | None = None
    op_revision_1w: float | None = None
    op_revision_1m: float | None = None
    op_revision_3m: float | None = None
    fcf_revision_1m: float | None = None
    target_price_revision_1m: float | None = None
    analyst_count_change: int | None = None
    street_high_eps_revision_1m: float | None = None
    street_low_eps_revision_1m: float | None = None
    source: str = "unknown"
    parsed_fields: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_text(self.source, "source")
        _require_date(self.date, "date")
        _require_date(self.as_of_date, "as_of_date")
        if self.date > self.as_of_date:
            raise ValueError("revision date cannot be after as_of_date")
        object.__setattr__(self, "parsed_fields", _copy_mapping(self.parsed_fields))


@dataclass(frozen=True)
class DisclosureEvent:
    """Parsed filing or exchange disclosure event."""

    symbol: str
    source: str
    report_type: str
    title: str
    published_at: datetime
    observed_at: datetime
    available_at: datetime
    as_of_date: date
    rcept_no: str | None = None
    raw_text: str | None = None
    parsed_fields: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_text(self.source, "source")
        _require_text(self.report_type, "report_type")
        _require_text(self.title, "title")
        _validate_temporal_evidence(
            published_at=self.published_at,
            observed_at=self.observed_at,
            available_at=self.available_at,
            as_of_date=self.as_of_date,
        )
        object.__setattr__(self, "parsed_fields", _copy_mapping(self.parsed_fields))


@dataclass(frozen=True)
class ResearchReport:
    """Parsed broker research report."""

    symbol: str
    publish_date: date
    broker: str
    title: str
    as_of_date: date
    analyst: str | None = None
    current_price: float | None = None
    target_price: float | None = None
    rating: str | None = None
    target_revision_pct: float | None = None
    target_multiple_before: float | None = None
    target_multiple_after: float | None = None
    fy1_sales: float | None = None
    fy1_op: float | None = None
    fy1_eps: float | None = None
    fy2_sales: float | None = None
    fy2_op: float | None = None
    fy2_eps: float | None = None
    fy3_sales: float | None = None
    fy3_op: float | None = None
    fy3_eps: float | None = None
    est_per: float | None = None
    est_pbr: float | None = None
    upside_pct: float | None = None
    fifty_two_week_high: float | None = None
    fifty_two_week_low: float | None = None
    one_month_return: float | None = None
    three_month_return: float | None = None
    twelve_month_return: float | None = None
    roe: float | None = None
    opm: float | None = None
    backlog: float | None = None
    new_orders: float | None = None
    order_backlog_to_sales: float | None = None
    capa_increase_pct: float | None = None
    export_ratio: float | None = None
    us_revenue_ratio: float | None = None
    asp_increase_mentioned: bool = False
    lead_time_mentioned: bool = False
    shortage_mentioned: bool = False
    investment_points: tuple[str, ...] = field(default_factory=tuple)
    risk_points: tuple[str, ...] = field(default_factory=tuple)
    raw_text: str | None = None
    parsed_fields: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_text(self.broker, "broker")
        _require_text(self.title, "title")
        _require_date(self.publish_date, "publish_date")
        _require_date(self.as_of_date, "as_of_date")
        if self.publish_date > self.as_of_date:
            raise ValueError("publish_date cannot be after as_of_date")
        for field_name in (
            "current_price",
            "target_price",
            "target_multiple_before",
            "target_multiple_after",
            "fy1_sales",
            "fy2_sales",
            "fy3_sales",
            "est_per",
            "est_pbr",
            "fifty_two_week_high",
            "fifty_two_week_low",
            "backlog",
            "new_orders",
            "order_backlog_to_sales",
        ):
            _require_non_negative(getattr(self, field_name), field_name)
        object.__setattr__(self, "investment_points", _copy_tuple(self.investment_points))
        object.__setattr__(self, "risk_points", _copy_tuple(self.risk_points))
        object.__setattr__(self, "parsed_fields", _copy_mapping(self.parsed_fields))


@dataclass(frozen=True)
class NewsItem:
    """News or official industry item."""

    symbol: str | None
    sector: str | None
    published_at: datetime
    source: str
    title: str
    as_of_date: date
    body: str | None = None
    source_tier: SourceTier = SourceTier.TIER_2
    theme_tags: tuple[str, ...] = field(default_factory=tuple)
    sentiment: float | None = None
    parsed_fields: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _require_datetime(self.published_at, "published_at")
        _require_text(self.source, "source")
        _require_text(self.title, "title")
        _require_date(self.as_of_date, "as_of_date")
        if self.published_at.date() > self.as_of_date:
            raise ValueError("published_at cannot be after as_of_date")
        if self.sentiment is not None and (self.sentiment < -1 or self.sentiment > 1):
            raise ValueError("sentiment must be between -1 and 1")
        object.__setattr__(self, "theme_tags", _copy_tuple(self.theme_tags))
        object.__setattr__(self, "parsed_fields", _copy_mapping(self.parsed_fields))


@dataclass(frozen=True)
class SectorRegime:
    """Sector-level regime score."""

    sector: str
    date: date
    as_of_date: date
    theme_regime_score: float
    high_quality_news_count: int = 0
    official_data_confirmation: float = 0.0
    sector_relative_strength: float = 0.0
    report_keyword_density: float = 0.0
    cross_company_disclosure_count: int = 0

    def __post_init__(self) -> None:
        _require_text(self.sector, "sector")
        _require_date(self.date, "date")
        _require_date(self.as_of_date, "as_of_date")
        if self.date > self.as_of_date:
            raise ValueError("date cannot be after as_of_date")
        _require_score(self.theme_regime_score, "theme_regime_score")
        _require_non_negative(self.high_quality_news_count, "high_quality_news_count")
        _require_non_negative(self.cross_company_disclosure_count, "cross_company_disclosure_count")


@dataclass(frozen=True)
class IndustrialSubScores:
    """Durability sub-scores behind visibility and bottleneck components."""

    contract_quality: float = 0.0
    backlog_rpo_visibility: float = 0.0
    capa_constraint: float = 0.0
    asp_pricing_power: float = 0.0
    structural_shortage: float = 0.0
    one_off_shortage_risk: float = 0.0
    shortage_type: ShortageType = ShortageType.UNKNOWN
    evidence_ids: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        _require_score(self.contract_quality, "contract_quality")
        _require_score(self.backlog_rpo_visibility, "backlog_rpo_visibility")
        _require_score(self.capa_constraint, "capa_constraint")
        _require_score(self.asp_pricing_power, "asp_pricing_power")
        _require_score(self.structural_shortage, "structural_shortage")
        _require_score(self.one_off_shortage_risk, "one_off_shortage_risk")
        if not isinstance(self.shortage_type, ShortageType):
            object.__setattr__(self, "shortage_type", ShortageType(self.shortage_type))
        object.__setattr__(self, "evidence_ids", _copy_tuple(self.evidence_ids))

    def as_diagnostic_scores(self) -> dict[str, float]:
        """Expose sub-scores through the existing numeric diagnostic channel."""

        return {
            "contract_quality": self.contract_quality,
            "backlog_rpo_visibility": self.backlog_rpo_visibility,
            "capa_constraint": self.capa_constraint,
            "asp_pricing_power": self.asp_pricing_power,
            "structural_shortage": self.structural_shortage,
            "one_off_shortage_risk": self.one_off_shortage_risk,
        }


@dataclass(frozen=True)
class ScoreSnapshot:
    """Deterministic score result for one instrument and date."""

    symbol: str
    as_of_date: date
    eps_fcf_explosion_score: float
    earnings_visibility_score: float
    bottleneck_pricing_score: float
    market_mispricing_score: float
    valuation_rerating_score: float
    capital_allocation_score: float
    information_confidence_score: float
    risk_penalty: float
    total_score: float
    diagnostic_scores: Mapping[str, float] = field(default_factory=dict)
    evidence_ids: tuple[str, ...] = field(default_factory=tuple)
    scoring_version: str = "e2r-2.0-cp1"

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_date(self.as_of_date, "as_of_date")
        _require_score(self.eps_fcf_explosion_score, "eps_fcf_explosion_score", 20)
        _require_score(self.earnings_visibility_score, "earnings_visibility_score", 20)
        _require_score(self.bottleneck_pricing_score, "bottleneck_pricing_score", 20)
        _require_score(self.market_mispricing_score, "market_mispricing_score", 15)
        _require_score(self.valuation_rerating_score, "valuation_rerating_score", 15)
        _require_score(self.capital_allocation_score, "capital_allocation_score", 5)
        _require_score(self.information_confidence_score, "information_confidence_score", 5)
        _require_non_negative(self.risk_penalty, "risk_penalty")
        _require_score(self.total_score, "total_score")
        _require_text(self.scoring_version, "scoring_version")
        for key, value in self.diagnostic_scores.items():
            _require_text(key, "diagnostic score key")
            _require_score(value, f"diagnostic score {key}")
        object.__setattr__(self, "diagnostic_scores", _copy_mapping(self.diagnostic_scores))
        object.__setattr__(self, "evidence_ids", _copy_tuple(self.evidence_ids))


@dataclass(frozen=True)
class StageSnapshot:
    """Stage classification result. Rules are implemented in checkpoint 2."""

    symbol: str
    as_of_date: date
    stage: Stage
    previous_stage: Stage | None = None
    stage_changed: bool = False
    grade: str | None = None
    stage_reason: tuple[str, ...] = field(default_factory=tuple)
    red_team_status: str | None = None
    evidence_ids: tuple[str, ...] = field(default_factory=tuple)
    classifier_version: str = "e2r-2.0-cp1"

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_date(self.as_of_date, "as_of_date")
        _require_text(self.classifier_version, "classifier_version")
        object.__setattr__(self, "stage_reason", _copy_tuple(self.stage_reason))
        object.__setattr__(self, "evidence_ids", _copy_tuple(self.evidence_ids))


@dataclass(frozen=True)
class RedTeamFinding:
    """Evidence-backed Red Team risk finding."""

    symbol: str
    as_of_date: date
    risk_type: str
    severity: float
    is_hard_break: bool
    description: str
    evidence_ids: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_date(self.as_of_date, "as_of_date")
        _require_text(self.risk_type, "risk_type")
        _require_text(self.description, "description")
        _require_score(self.severity, "severity")
        object.__setattr__(self, "evidence_ids", _copy_tuple(self.evidence_ids))


@dataclass(frozen=True)
class BacktestResult:
    """Required point-in-time backtest metrics for a Stage 3 event."""

    symbol: str
    stage3_date: date
    stage3_price: float
    pre_runup_252d: float | None = None
    pre_runup_3y: float | None = None
    mfe_30d: float | None = None
    mfe_90d: float | None = None
    mfe_180d: float | None = None
    mfe_1y: float | None = None
    mfe_2y: float | None = None
    mae_30d: float | None = None
    mae_90d: float | None = None
    mae_180d: float | None = None
    mae_1y: float | None = None
    below_entry_flag: bool | None = None
    time_to_50pct: int | None = None
    time_to_100pct: int | None = None
    time_to_200pct: int | None = None
    time_to_4b: int | None = None
    time_to_4c: int | None = None
    stage4b_date: date | None = None
    stage4b_price: float | None = None
    stage4b_return_from_stage3: float | None = None
    stage4c_date: date | None = None
    stage4c_price: float | None = None
    peak_date: date | None = None
    peak_price: float | None = None
    peak_return_from_stage3: float | None = None
    drawdown_after_peak: float | None = None

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_date(self.stage3_date, "stage3_date")
        _require_positive(self.stage3_price, "stage3_price")
        for field_name in ("stage4b_date", "stage4c_date", "peak_date"):
            value = getattr(self, field_name)
            if value is not None:
                _require_date(value, field_name)
                if value < self.stage3_date:
                    raise ValueError(f"{field_name} cannot be before stage3_date")
        for field_name in ("stage4b_price", "stage4c_price", "peak_price"):
            _require_positive(getattr(self, field_name), field_name)
        for field_name in ("time_to_50pct", "time_to_100pct", "time_to_200pct", "time_to_4b", "time_to_4c"):
            _require_non_negative(getattr(self, field_name), field_name)
