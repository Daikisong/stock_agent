"""Synthetic E2R 2.0 fixture cases.

These fixtures are behavioral examples for tests and demos. They intentionally
use synthetic symbols and must not be referenced by scoring or stage logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from enum import Enum

from .backtesting import BacktestEngine, Stage3BacktestInput
from .models import BacktestResult, Evidence, Market, PriceBar, SourceTier, Stage, StageSnapshot
from .red_team import RedTeamAssessment, RedTeamEngine, RedTeamSignals
from .scoring import DeterministicScorer, ScoringPayload
from .staging import StageClassificationInput, StageClassifier


class FixtureCategory(str, Enum):
    """Required fixture behavior categories from the E2R 2.0 spec."""

    POWER_EQUIPMENT_SUCCESS = "power_equipment_success"
    SEMICONDUCTOR_TURNAROUND = "semiconductor_turnaround"
    NON_POWER_RERATING = "non_power_rerating"
    MOMENTUM_FALSE_POSITIVE = "momentum_false_positive"
    PEAK_OUT_AFTER_SUCCESS = "peak_out_after_success"
    STAGE3_OVERHEAT = "stage3_overheat"
    US_BOOM_BUST = "us_boom_bust"


@dataclass(frozen=True)
class FixtureCase:
    """One synthetic fixture case with point-in-time inputs and expectations."""

    case_id: str
    category: FixtureCategory
    market: Market
    description: str
    scoring_payload: ScoringPayload
    expected_stage: Stage
    red_team_signals: RedTeamSignals
    price_bars: tuple[PriceBar, ...]
    stage3_date: date
    stage3_price: float
    stage_snapshots: tuple[StageSnapshot, ...] = field(default_factory=tuple)
    evidence: tuple[Evidence, ...] = field(default_factory=tuple)
    previous_stage: Stage | None = None
    theme_regime_score: float = 0.0
    company_event_score: float = 0.0
    high_quality_company_event: bool = False
    thesis_ongoing: bool = False
    archive_requested: bool = False
    coverage_impossible: bool = False

    def score(self):
        return DeterministicScorer().score(self.scoring_payload)

    def red_team_assessment(self) -> RedTeamAssessment:
        return RedTeamEngine().assess(self.red_team_signals)

    def stage_input(self) -> StageClassificationInput:
        return StageClassificationInput(
            score=self.score(),
            red_team=self.red_team_assessment(),
            previous_stage=self.previous_stage,
            theme_regime_score=self.theme_regime_score,
            company_event_score=self.company_event_score,
            high_quality_company_event=self.high_quality_company_event,
            thesis_ongoing=self.thesis_ongoing,
            archive_requested=self.archive_requested,
            coverage_impossible=self.coverage_impossible,
            evidence_ids=tuple(evidence.evidence_id for evidence in self.evidence),
        )

    def classify(self) -> StageSnapshot:
        return StageClassifier().classify(self.stage_input())

    def backtest(self) -> BacktestResult:
        return BacktestEngine().evaluate_stage3(
            Stage3BacktestInput(
                symbol=self.scoring_payload.symbol,
                stage3_date=self.stage3_date,
                price_bars=self.price_bars,
                stage_snapshots=self.stage_snapshots,
                stage3_price=self.stage3_price,
            )
        )


def _bar(symbol: str, day_offset: int, low: float, high: float, close: float) -> PriceBar:
    bar_date = date(2024, 1, 1) + timedelta(days=day_offset)
    return PriceBar(
        symbol=symbol,
        date=bar_date,
        open=close,
        high=high,
        low=low,
        close=close,
        adj_close=close,
        volume=1000 + day_offset,
        trading_value=close * (1000 + day_offset),
        market_cap=1_000_000_000.0 + close * 1000,
        source="fixture",
        as_of_date=bar_date,
    )


def _bars(symbol: str, path: tuple[tuple[float, float, float], ...]) -> tuple[PriceBar, ...]:
    return tuple(_bar(symbol, index, low, high, close) for index, (low, high, close) in enumerate(path))


def _evidence(symbol: str, market: Market, as_of_date: date, suffix: str, source_type: str) -> Evidence:
    available = datetime(as_of_date.year, as_of_date.month, as_of_date.day, 8, 0)
    return Evidence(
        evidence_id=f"{symbol}-{suffix}",
        source_type=source_type,
        source_name="FixtureSource",
        source_tier=SourceTier.TIER_1,
        published_at=available,
        observed_at=available,
        available_at=available,
        as_of_date=as_of_date,
        market=market,
        symbol=symbol,
        title=f"{suffix} fixture evidence",
        parsed_fields={"fixture": True},
        confidence=1.0,
    )


def _payload(
    *,
    symbol: str,
    as_of_date: date,
    components: dict[str, float],
    diagnostic_scores: dict[str, float] | None = None,
    evidence_ids: tuple[str, ...] = (),
    large_sector_id: str,
    canonical_archetype_id: str,
) -> ScoringPayload:
    return ScoringPayload(
        symbol=symbol,
        as_of_date=as_of_date,
        components=components,
        diagnostic_scores=diagnostic_scores or {},
        evidence_ids=evidence_ids,
        large_sector_id=large_sector_id,
        canonical_archetype_id=canonical_archetype_id,
    )


SUCCESS_PATH = (
    (70, 76, 72),
    (62, 72, 66),
    (50, 66, 60),
    (58, 70, 65),
    (82, 96, 90),
    (96, 112, 100),
    (104, 132, 125),
    (120, 158, 150),
    (140, 205, 198),
    (180, 250, 230),
    (215, 270, 260),
    (240, 310, 300),
)

BOOM_BUST_PATH = (
    (45, 55, 50),
    (48, 65, 60),
    (55, 80, 75),
    (70, 95, 90),
    (92, 125, 118),
    (95, 120, 100),
    (130, 180, 170),
    (165, 245, 230),
    (220, 310, 300),
    (260, 360, 330),
    (130, 180, 150),
    (80, 120, 95),
)

FALSE_POSITIVE_PATH = (
    (40, 48, 45),
    (44, 55, 52),
    (51, 68, 64),
    (63, 90, 85),
    (84, 125, 118),
    (95, 135, 100),
    (82, 110, 90),
    (75, 95, 80),
    (65, 85, 70),
    (55, 72, 60),
)


def _stage(symbol: str, day_offset: int, stage: Stage) -> StageSnapshot:
    return StageSnapshot(
        symbol=symbol,
        as_of_date=date(2024, 1, 1) + timedelta(days=day_offset),
        stage=stage,
        evidence_ids=(f"{symbol}-{stage.value}",),
    )


def build_fixture_cases() -> tuple[FixtureCase, ...]:
    """Build all synthetic fixture cases."""

    stage3_date = date(2024, 1, 6)

    def case_evidence(symbol: str, market: Market, as_of_date: date) -> tuple[Evidence, ...]:
        return (
            _evidence(symbol, market, as_of_date, "numbers", "consensus"),
            _evidence(symbol, market, as_of_date, "thesis", "research_report"),
        )

    pwr_evidence = case_evidence("KR-PWR-GREEN", Market.KR, stage3_date)
    mem_evidence = case_evidence("KR-MEM-TURN", Market.KR, stage3_date)
    non_power_evidence = case_evidence("KR-NONPWR-GREEN", Market.KR, stage3_date)
    momentum_evidence = case_evidence("KR-THEME-RED", Market.KR, stage3_date)
    peak_date = date(2024, 1, 11)
    peak_evidence = case_evidence("KR-PEAK-4C", Market.KR, peak_date)
    overheat_evidence = case_evidence("US-OVERHEAT-3R", Market.US, stage3_date)
    boom_date = date(2024, 1, 9)
    boom_evidence = case_evidence("US-BOOM-BUST", Market.US, boom_date)

    return (
        FixtureCase(
            case_id="power_equipment_success_green",
            category=FixtureCategory.POWER_EQUIPMENT_SUCCESS,
            market=Market.KR,
            description="Synthetic industrial bottleneck case with strong backlog, pricing power, revision, and valuation runway.",
            scoring_payload=_payload(
                symbol="KR-PWR-GREEN",
                as_of_date=stage3_date,
                components={
                    "eps_fcf_explosion": 20,
                    "earnings_visibility": 18,
                    "bottleneck_pricing": 18,
                    "market_mispricing": 13,
                    "valuation_rerating": 12,
                    "capital_allocation": 4,
                    "information_confidence": 4,
                },
                diagnostic_scores={"revision_score": 85, "price_stage_score": 70},
                evidence_ids=tuple(evidence.evidence_id for evidence in pwr_evidence),
                large_sector_id="L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
                canonical_archetype_id="C02_POWER_GRID_DATACENTER_CAPEX",
            ),
            expected_stage=Stage.STAGE_3_GREEN,
            red_team_signals=RedTeamSignals(symbol="KR-PWR-GREEN", as_of_date=stage3_date),
            price_bars=_bars("KR-PWR-GREEN", SUCCESS_PATH),
            stage3_date=stage3_date,
            stage3_price=100,
            stage_snapshots=(_stage("KR-PWR-GREEN", 9, Stage.STAGE_4B),),
            evidence=pwr_evidence,
            theme_regime_score=88,
            company_event_score=82,
        ),
        FixtureCase(
            case_id="semiconductor_turnaround_green",
            category=FixtureCategory.SEMICONDUCTOR_TURNAROUND,
            market=Market.KR,
            description="Synthetic turnaround where trailing numbers are weak, but forward EPS/FCF and high-value mix are improving.",
            scoring_payload=_payload(
                symbol="KR-MEM-TURN",
                as_of_date=stage3_date,
                components={
                    "eps_fcf_explosion": 19,
                    "earnings_visibility": 17,
                    "bottleneck_pricing": 18,
                    "market_mispricing": 12,
                    "valuation_rerating": 12,
                    "capital_allocation": 3,
                    "information_confidence": 5,
                },
                diagnostic_scores={
                    "revision_score": 78,
                    "price_stage_score": 82,
                    "actual_profit_conversion_score": 75,
                    "fcf_quality_score": 70,
                    "domain_specific_evidence_score": 70,
                    "structural_visibility_quality": 60,
                    "research_axis_bridge_present_count_capped": 4,
                },
                evidence_ids=tuple(evidence.evidence_id for evidence in mem_evidence),
                large_sector_id="L2_AI_SEMICONDUCTOR_ELECTRONICS",
                canonical_archetype_id="C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
            ),
            expected_stage=Stage.STAGE_3_GREEN,
            red_team_signals=RedTeamSignals(symbol="KR-MEM-TURN", as_of_date=stage3_date),
            price_bars=_bars("KR-MEM-TURN", SUCCESS_PATH),
            stage3_date=stage3_date,
            stage3_price=100,
            evidence=mem_evidence,
            theme_regime_score=86,
            company_event_score=78,
        ),
        FixtureCase(
            case_id="non_power_rerating_green",
            category=FixtureCategory.NON_POWER_RERATING,
            market=Market.KR,
            description="Synthetic non-power rerating case where overseas mix and margin structure support a new frame.",
            scoring_payload=_payload(
                symbol="KR-NONPWR-GREEN",
                as_of_date=stage3_date,
                components={
                    "eps_fcf_explosion": 19,
                    "earnings_visibility": 17,
                    "bottleneck_pricing": 17,
                    "market_mispricing": 12,
                    "valuation_rerating": 12,
                    "capital_allocation": 4,
                    "information_confidence": 5,
                },
                diagnostic_scores={"revision_score": 74, "price_stage_score": 76},
                evidence_ids=tuple(evidence.evidence_id for evidence in non_power_evidence),
                large_sector_id="L5_CONSUMER_BRAND_DISTRIBUTION",
                canonical_archetype_id="C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
            ),
            expected_stage=Stage.STAGE_3_GREEN,
            red_team_signals=RedTeamSignals(symbol="KR-NONPWR-GREEN", as_of_date=stage3_date),
            price_bars=_bars("KR-NONPWR-GREEN", SUCCESS_PATH),
            stage3_date=stage3_date,
            stage3_price=100,
            evidence=non_power_evidence,
            theme_regime_score=75,
            company_event_score=80,
        ),
        FixtureCase(
            case_id="momentum_false_positive_red",
            category=FixtureCategory.MOMENTUM_FALSE_POSITIVE,
            market=Market.KR,
            description="Synthetic theme-heavy case where valuation runway is thin even though headline momentum is strong.",
            scoring_payload=_payload(
                symbol="KR-THEME-RED",
                as_of_date=stage3_date,
                components={
                    "eps_fcf_explosion": 20,
                    "earnings_visibility": 20,
                    "bottleneck_pricing": 20,
                    "market_mispricing": 15,
                    "valuation_rerating": 5,
                    "capital_allocation": 5,
                    "information_confidence": 5,
                },
                diagnostic_scores={"revision_score": 60, "theme_overheat_score": 75},
                evidence_ids=tuple(evidence.evidence_id for evidence in momentum_evidence),
                large_sector_id="L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
                canonical_archetype_id="C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
            ),
            expected_stage=Stage.STAGE_3_RED,
            red_team_signals=RedTeamSignals(symbol="KR-THEME-RED", as_of_date=stage3_date),
            price_bars=_bars("KR-THEME-RED", FALSE_POSITIVE_PATH),
            stage3_date=stage3_date,
            stage3_price=100,
            evidence=momentum_evidence,
            theme_regime_score=82,
            company_event_score=76,
        ),
        FixtureCase(
            case_id="peak_out_after_success_4c",
            category=FixtureCategory.PEAK_OUT_AFTER_SUCCESS,
            market=Market.KR,
            description="Synthetic early-success case where a later contract delay breaks the core thesis.",
            scoring_payload=_payload(
                symbol="KR-PEAK-4C",
                as_of_date=peak_date,
                components={
                    "eps_fcf_explosion": 18,
                    "earnings_visibility": 16,
                    "bottleneck_pricing": 16,
                    "market_mispricing": 11,
                    "valuation_rerating": 10,
                    "capital_allocation": 4,
                    "information_confidence": 5,
                },
                diagnostic_scores={"revision_score": 65},
                evidence_ids=tuple(evidence.evidence_id for evidence in peak_evidence),
                large_sector_id="L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
                canonical_archetype_id="C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
            ),
            expected_stage=Stage.STAGE_4C,
            red_team_signals=RedTeamSignals(
                symbol="KR-PEAK-4C",
                as_of_date=peak_date,
                thesis_break_factors={"contract_cancelled_or_delayed": 1.0},
                evidence_ids_by_signal={"contract_cancelled_or_delayed": ("KR-PEAK-4C-thesis",)},
            ),
            price_bars=_bars("KR-PEAK-4C", BOOM_BUST_PATH),
            stage3_date=stage3_date,
            stage3_price=100,
            stage_snapshots=(_stage("KR-PEAK-4C", 10, Stage.STAGE_4C),),
            evidence=peak_evidence,
            previous_stage=Stage.STAGE_4A,
            thesis_ongoing=True,
        ),
        FixtureCase(
            case_id="stage3_overheat_red",
            category=FixtureCategory.STAGE3_OVERHEAT,
            market=Market.US,
            description="Synthetic Stage 3 signal where the move is dominated by overheat diagnostics.",
            scoring_payload=_payload(
                symbol="US-OVERHEAT-3R",
                as_of_date=stage3_date,
                components={
                    "eps_fcf_explosion": 20,
                    "earnings_visibility": 18,
                    "bottleneck_pricing": 18,
                    "market_mispricing": 13,
                    "valuation_rerating": 12,
                    "capital_allocation": 4,
                    "information_confidence": 4,
                },
                diagnostic_scores={"revision_score": 85, "theme_overheat_score": 85},
                evidence_ids=tuple(evidence.evidence_id for evidence in overheat_evidence),
                large_sector_id="L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
                canonical_archetype_id="R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
            ),
            expected_stage=Stage.STAGE_3_RED,
            red_team_signals=RedTeamSignals(symbol="US-OVERHEAT-3R", as_of_date=stage3_date),
            price_bars=_bars("US-OVERHEAT-3R", FALSE_POSITIVE_PATH),
            stage3_date=stage3_date,
            stage3_price=100,
            evidence=overheat_evidence,
            theme_regime_score=80,
            company_event_score=80,
        ),
        FixtureCase(
            case_id="us_boom_bust_4b_then_4c",
            category=FixtureCategory.US_BOOM_BUST,
            market=Market.US,
            description="Synthetic US boom-bust case where 4B crowding appears before a later thesis-break outcome.",
            scoring_payload=_payload(
                symbol="US-BOOM-BUST",
                as_of_date=boom_date,
                components={
                    "eps_fcf_explosion": 19,
                    "earnings_visibility": 16,
                    "bottleneck_pricing": 17,
                    "market_mispricing": 12,
                    "valuation_rerating": 11,
                    "capital_allocation": 4,
                    "information_confidence": 5,
                },
                diagnostic_scores={"revision_score": 70},
                evidence_ids=tuple(evidence.evidence_id for evidence in boom_evidence),
                large_sector_id="L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
                canonical_archetype_id="R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
            ),
            expected_stage=Stage.STAGE_4B,
            red_team_signals=RedTeamSignals(
                symbol="US-BOOM-BUST",
                as_of_date=boom_date,
                soft_4b_factors={
                    "return_since_stage3": 1.0,
                    "return_12_24m": 1.0,
                    "extreme_forward_valuation": 1.0,
                    "revision_slowdown": 1.0,
                },
            ),
            price_bars=_bars("US-BOOM-BUST", BOOM_BUST_PATH),
            stage3_date=stage3_date,
            stage3_price=100,
            stage_snapshots=(
                _stage("US-BOOM-BUST", 8, Stage.STAGE_4B),
                _stage("US-BOOM-BUST", 10, Stage.STAGE_4C),
            ),
            evidence=boom_evidence,
            previous_stage=Stage.STAGE_3_GREEN,
            thesis_ongoing=True,
        ),
    )


FIXTURE_CASES = build_fixture_cases()


def fixture_cases_by_category(category: FixtureCategory) -> tuple[FixtureCase, ...]:
    """Return fixture cases in a category."""

    return tuple(case for case in FIXTURE_CASES if case.category == category)
