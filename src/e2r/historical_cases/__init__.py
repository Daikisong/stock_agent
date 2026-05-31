"""Historical E2R case loader and point-in-time pipeline."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.backtesting import BacktestEngine, Stage3BacktestInput
from e2r.features import DeterministicFeatureEngineer, FeatureEngineeringInput, FeatureEngineeringResult
from e2r.models import (
    BacktestResult,
    ConsensusRevision,
    ConsensusSnapshot,
    DisclosureEvent,
    Evidence,
    FinancialActual,
    Instrument,
    Market,
    NewsItem,
    PriceBar,
    ResearchReport,
    SourceTier,
    Stage,
    StageSnapshot,
)
from e2r.red_team import RedTeamAssessment, RedTeamEngine
from e2r.scoring import ScoreSnapshot
from e2r.sources.source_errors import (
    bool_value,
    date_value,
    datetime_value,
    float_or_none,
    int_or_none,
    mapping_value,
    market_value,
    parsed_fields_from_record,
    source_tier_value,
    text_or_none,
    tuple_value,
)
from e2r.staging import StageClassificationInput, StageClassifier


DEFAULT_HISTORICAL_CASE_DIR = Path("data/historical_cases")


@dataclass(frozen=True)
class HistoricalCase:
    """One real historical case fixture."""

    case_id: str
    symbol: str
    company_name: str
    market: Market
    stage3_date: date
    stage3_price: float
    stage3_source: str
    expected_stage: Stage | None = None
    pre_runup_252d: float | None = None
    stage4b_date: date | None = None
    stage4b_reason: str | None = None
    stage4c_date: date | None = None
    stage4c_reason: str | None = None
    instrument: Instrument | None = None
    financial_actuals: Sequence[FinancialActual] = field(default_factory=tuple)
    consensus: Sequence[ConsensusSnapshot] = field(default_factory=tuple)
    consensus_revisions: Sequence[ConsensusRevision] = field(default_factory=tuple)
    disclosures: Sequence[DisclosureEvent] = field(default_factory=tuple)
    research_reports: Sequence[ResearchReport] = field(default_factory=tuple)
    news_items: Sequence[NewsItem] = field(default_factory=tuple)
    evidence: Sequence[Evidence] = field(default_factory=tuple)
    price_bars: Sequence[PriceBar] = field(default_factory=tuple)
    stage_snapshots: Sequence[StageSnapshot] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        object.__setattr__(self, "financial_actuals", tuple(self.financial_actuals))
        object.__setattr__(self, "consensus", tuple(self.consensus))
        object.__setattr__(self, "consensus_revisions", tuple(self.consensus_revisions))
        object.__setattr__(self, "disclosures", tuple(self.disclosures))
        object.__setattr__(self, "research_reports", tuple(self.research_reports))
        object.__setattr__(self, "news_items", tuple(self.news_items))
        object.__setattr__(self, "evidence", tuple(self.evidence))
        object.__setattr__(self, "price_bars", tuple(self.price_bars))
        object.__setattr__(self, "stage_snapshots", tuple(self.stage_snapshots))

    def feature_input(self) -> FeatureEngineeringInput:
        return FeatureEngineeringInput(
            symbol=self.symbol,
            as_of_date=self.stage3_date,
            company_name=self.company_name,
            sector_context=self.instrument.sector_custom if self.instrument is not None else None,
            price_bars=tuple(bar for bar in self.price_bars if bar.as_of_date <= self.stage3_date),
            financial_actuals=tuple(item for item in self.financial_actuals if item.as_of_date <= self.stage3_date),
            consensus=tuple(item for item in self.consensus if item.as_of_date <= self.stage3_date),
            consensus_revisions=tuple(item for item in self.consensus_revisions if item.as_of_date <= self.stage3_date),
            disclosures=tuple(item for item in self.disclosures if item.available_at.date() <= self.stage3_date),
            research_reports=tuple(item for item in self.research_reports if item.as_of_date <= self.stage3_date),
            news_items=tuple(item for item in self.news_items if item.as_of_date <= self.stage3_date),
        )

    def engineer(self) -> FeatureEngineeringResult:
        return DeterministicFeatureEngineer().engineer(self.feature_input())

    def score(self) -> ScoreSnapshot:
        return self.engineer().score()

    def red_team_assessment(self) -> RedTeamAssessment:
        return RedTeamEngine().assess(self.engineer().red_team_signals)

    def classify(self) -> StageSnapshot:
        result = self.engineer()
        return StageClassifier().classify(
            StageClassificationInput(
                score=result.score(),
                red_team=RedTeamEngine().assess(result.red_team_signals),
                theme_regime_score=80.0,
                company_event_score=80.0,
                evidence_ids=tuple(item.evidence_id for item in self.evidence if item.as_of_date <= self.stage3_date),
            )
        )

    def backtest(self) -> BacktestResult:
        return BacktestEngine().evaluate_stage3(
            Stage3BacktestInput(
                symbol=self.symbol,
                stage3_date=self.stage3_date,
                price_bars=self.price_bars,
                stage_snapshots=self.stage_snapshots,
                stage3_price=self.stage3_price,
            )
        )


@dataclass(frozen=True)
class HistoricalCasePipelineResult:
    case: HistoricalCase
    feature_input: FeatureEngineeringInput
    feature_result: FeatureEngineeringResult
    score: ScoreSnapshot
    red_team: RedTeamAssessment
    stage: StageSnapshot
    backtest: BacktestResult


def load_historical_case(path: str | Path) -> HistoricalCase:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return historical_case_from_mapping(payload)


def load_historical_cases(root: str | Path = DEFAULT_HISTORICAL_CASE_DIR) -> tuple[HistoricalCase, ...]:
    root_path = Path(root)
    return tuple(load_historical_case(path) for path in sorted(root_path.glob("*.json")))


def run_historical_case_pipeline(case: HistoricalCase) -> HistoricalCasePipelineResult:
    feature_input = case.feature_input()
    feature_result = case.engineer()
    score = feature_result.score()
    red_team = RedTeamEngine().assess(feature_result.red_team_signals)
    stage = StageClassifier().classify(
        StageClassificationInput(
            score=score,
            red_team=red_team,
            theme_regime_score=80.0,
            company_event_score=80.0,
            evidence_ids=tuple(item.evidence_id for item in case.evidence if item.as_of_date <= case.stage3_date),
        )
    )
    backtest = case.backtest()
    return HistoricalCasePipelineResult(
        case=case,
        feature_input=feature_input,
        feature_result=feature_result,
        score=score,
        red_team=red_team,
        stage=stage,
        backtest=backtest,
    )


def historical_case_from_mapping(payload: Mapping[str, Any]) -> HistoricalCase:
    market = market_value(payload.get("market"))
    symbol = str(payload["symbol"])
    stage3_date = date_value(payload["stage3_date"])
    instrument = Instrument(
        symbol=symbol,
        name=str(payload["company_name"]),
        market=market,
        exchange=str(payload.get("exchange") or ("KRX" if market == Market.KR else "NASDAQ")),
        sector_custom=text_or_none(payload.get("sector")),
        listed_date=date_value(payload["listed_date"]) if payload.get("listed_date") else None,
        currency=str(payload.get("currency") or ("KRW" if market == Market.KR else "USD")),
    )

    reports = tuple(_research_report(row, symbol, stage3_date) for row in payload.get("report_evidence", ()))
    disclosures = tuple(_disclosure(row, symbol, stage3_date) for row in payload.get("disclosure_evidence", ()))
    consensus = tuple(_consensus(row, symbol, stage3_date) for row in payload.get("consensus_evidence", ()))
    revisions = tuple(_revision(row, symbol, stage3_date) for row in payload.get("consensus_revisions", ()))
    actuals = tuple(_actual(row, symbol, stage3_date) for row in payload.get("financial_actuals", ()))
    news = tuple(_news(row, symbol, stage3_date) for row in payload.get("news_evidence", ()))
    price_bars = tuple(_price_bar(row, symbol) for row in payload.get("outcome_price_path", ()))
    stage_snapshots = tuple(_stage_snapshot(row, symbol) for row in payload.get("stage_snapshots", ()))
    evidence = _evidence_records(
        symbol=symbol,
        market=market,
        reports=reports,
        disclosures=disclosures,
        news_items=news,
        consensus=consensus,
        revisions=revisions,
        actuals=actuals,
    )
    expected_stage = Stage(payload["expected_stage"]) if payload.get("expected_stage") else None
    return HistoricalCase(
        case_id=str(payload.get("case_id") or Path(str(payload.get("symbol"))).stem),
        symbol=symbol,
        company_name=str(payload["company_name"]),
        market=market,
        stage3_date=stage3_date,
        stage3_price=float(payload["stage3_price"]),
        stage3_source=str(payload["stage3_source"]),
        expected_stage=expected_stage,
        pre_runup_252d=float_or_none(payload.get("pre_runup_252d")),
        stage4b_date=date_value(payload["stage4b_date"]) if payload.get("stage4b_date") else None,
        stage4b_reason=text_or_none(payload.get("stage4b_reason")),
        stage4c_date=date_value(payload["stage4c_date"]) if payload.get("stage4c_date") else None,
        stage4c_reason=text_or_none(payload.get("stage4c_reason")),
        instrument=instrument,
        financial_actuals=actuals,
        consensus=consensus,
        consensus_revisions=revisions,
        disclosures=disclosures,
        research_reports=reports,
        news_items=news,
        evidence=evidence,
        price_bars=price_bars,
        stage_snapshots=stage_snapshots,
    )


def _research_report(row: Mapping[str, Any], symbol: str, default_as_of: date) -> ResearchReport:
    parsed = mapping_value(row.get("parsed_fields"))
    for key, value in row.items():
        if key not in _REPORT_KEYS and value not in (None, ""):
            parsed[key] = value
    return ResearchReport(
        symbol=str(row.get("symbol") or symbol),
        publish_date=date_value(row["publish_date"]),
        broker=str(row.get("broker") or "HistoricalFixture"),
        title=str(row["title"]),
        as_of_date=date_value(row.get("as_of_date") or default_as_of),
        analyst=text_or_none(row.get("analyst")),
        current_price=float_or_none(row.get("current_price")),
        target_price=float_or_none(row.get("target_price")),
        rating=text_or_none(row.get("rating")),
        target_revision_pct=float_or_none(row.get("target_revision_pct")),
        target_multiple_before=float_or_none(row.get("target_multiple_before")),
        target_multiple_after=float_or_none(row.get("target_multiple_after")),
        fy1_sales=float_or_none(row.get("fy1_sales")),
        fy1_op=float_or_none(row.get("fy1_op")),
        fy1_eps=float_or_none(row.get("fy1_eps")),
        fy2_sales=float_or_none(row.get("fy2_sales")),
        fy2_op=float_or_none(row.get("fy2_op")),
        fy2_eps=float_or_none(row.get("fy2_eps")),
        fy3_sales=float_or_none(row.get("fy3_sales")),
        fy3_op=float_or_none(row.get("fy3_op")),
        fy3_eps=float_or_none(row.get("fy3_eps")),
        est_per=float_or_none(row.get("est_per")),
        est_pbr=float_or_none(row.get("est_pbr")),
        upside_pct=float_or_none(row.get("upside_pct")),
        fifty_two_week_high=float_or_none(row.get("fifty_two_week_high")),
        fifty_two_week_low=float_or_none(row.get("fifty_two_week_low")),
        one_month_return=float_or_none(row.get("one_month_return")),
        three_month_return=float_or_none(row.get("three_month_return")),
        twelve_month_return=float_or_none(row.get("twelve_month_return")),
        roe=float_or_none(row.get("roe")),
        opm=float_or_none(row.get("opm")),
        backlog=float_or_none(row.get("backlog")),
        new_orders=float_or_none(row.get("new_orders")),
        order_backlog_to_sales=float_or_none(row.get("order_backlog_to_sales")),
        capa_increase_pct=float_or_none(row.get("capa_increase_pct")),
        export_ratio=float_or_none(row.get("export_ratio")),
        us_revenue_ratio=float_or_none(row.get("us_revenue_ratio")),
        asp_increase_mentioned=bool_value(row.get("asp_increase_mentioned")),
        lead_time_mentioned=bool_value(row.get("lead_time_mentioned")),
        shortage_mentioned=bool_value(row.get("shortage_mentioned")),
        investment_points=tuple_value(row.get("investment_points")),
        risk_points=tuple_value(row.get("risk_points")),
        raw_text=text_or_none(row.get("raw_text")),
        parsed_fields=parsed,
    )


def _disclosure(row: Mapping[str, Any], symbol: str, default_as_of: date) -> DisclosureEvent:
    known = {"symbol", "source", "report_type", "title", "published_at", "observed_at", "available_at", "as_of_date", "rcept_no", "raw_text", "parsed_fields"}
    return DisclosureEvent(
        symbol=str(row.get("symbol") or symbol),
        source=str(row.get("source") or "HistoricalDisclosure"),
        report_type=str(row["report_type"]),
        title=str(row["title"]),
        published_at=datetime_value(row["published_at"]),
        observed_at=datetime_value(row.get("observed_at") or row["published_at"]),
        available_at=datetime_value(row.get("available_at") or row["published_at"]),
        as_of_date=date_value(row.get("as_of_date") or default_as_of),
        rcept_no=text_or_none(row.get("rcept_no")),
        raw_text=text_or_none(row.get("raw_text")),
        parsed_fields=parsed_fields_from_record(row, known),
    )


def _consensus(row: Mapping[str, Any], symbol: str, default_as_of: date) -> ConsensusSnapshot:
    return ConsensusSnapshot(
        symbol=str(row.get("symbol") or symbol),
        date=date_value(row.get("date") or row.get("as_of_date") or default_as_of),
        fiscal_year=int(row["fiscal_year"]),
        as_of_date=date_value(row.get("as_of_date") or default_as_of),
        source=str(row.get("source") or "HistoricalConsensus"),
        sales_e=float_or_none(row.get("sales_e")),
        op_e=float_or_none(row.get("op_e")),
        net_income_e=float_or_none(row.get("net_income_e")),
        eps_e=float_or_none(row.get("eps_e")),
        fcf_e=float_or_none(row.get("fcf_e")),
        bps_e=float_or_none(row.get("bps_e")),
        roe_e=float_or_none(row.get("roe_e")),
        per_e=float_or_none(row.get("per_e")),
        pbr_e=float_or_none(row.get("pbr_e")),
        analyst_count=int_or_none(row.get("analyst_count")),
        target_price=float_or_none(row.get("target_price")),
        target_multiple_type=text_or_none(row.get("target_multiple_type")),
        target_multiple=float_or_none(row.get("target_multiple")),
    )


def _revision(row: Mapping[str, Any], symbol: str, default_as_of: date) -> ConsensusRevision:
    return ConsensusRevision(
        symbol=str(row.get("symbol") or symbol),
        date=date_value(row.get("date") or row.get("as_of_date") or default_as_of),
        fiscal_year=int(row["fiscal_year"]),
        as_of_date=date_value(row.get("as_of_date") or default_as_of),
        eps_revision_1w=float_or_none(row.get("eps_revision_1w")),
        eps_revision_1m=float_or_none(row.get("eps_revision_1m")),
        eps_revision_3m=float_or_none(row.get("eps_revision_3m")),
        op_revision_1w=float_or_none(row.get("op_revision_1w")),
        op_revision_1m=float_or_none(row.get("op_revision_1m")),
        op_revision_3m=float_or_none(row.get("op_revision_3m")),
        fcf_revision_1m=float_or_none(row.get("fcf_revision_1m")),
        target_price_revision_1m=float_or_none(row.get("target_price_revision_1m")),
        analyst_count_change=int_or_none(row.get("analyst_count_change")),
        street_high_eps_revision_1m=float_or_none(row.get("street_high_eps_revision_1m")),
        street_low_eps_revision_1m=float_or_none(row.get("street_low_eps_revision_1m")),
    )


def _actual(row: Mapping[str, Any], symbol: str, default_as_of: date) -> FinancialActual:
    return FinancialActual(
        symbol=str(row.get("symbol") or symbol),
        fiscal_year=int(row["fiscal_year"]),
        fiscal_quarter=int_or_none(row.get("fiscal_quarter")),
        period_end=date_value(row["period_end"]),
        reported_at=datetime_value(row["reported_at"]),
        as_of_date=date_value(row.get("as_of_date") or default_as_of),
        source=str(row.get("source") or "HistoricalActual"),
        sales=float_or_none(row.get("sales")),
        operating_profit=float_or_none(row.get("operating_profit")),
        net_income=float_or_none(row.get("net_income")),
        eps=float_or_none(row.get("eps")),
        bps=float_or_none(row.get("bps")),
        roe=float_or_none(row.get("roe")),
        opm=float_or_none(row.get("opm")),
        cashflow_from_operations=float_or_none(row.get("cashflow_from_operations")),
        capex=float_or_none(row.get("capex")),
        fcf=float_or_none(row.get("fcf")),
        receivables=float_or_none(row.get("receivables")),
        inventory=float_or_none(row.get("inventory")),
    )


def _news(row: Mapping[str, Any], symbol: str, default_as_of: date) -> NewsItem:
    known = {"symbol", "sector", "published_at", "source", "title", "as_of_date", "body", "source_tier", "theme_tags", "sentiment", "parsed_fields"}
    return NewsItem(
        symbol=str(row.get("symbol") or symbol),
        sector=text_or_none(row.get("sector")),
        published_at=datetime_value(row["published_at"]),
        source=str(row.get("source") or "HistoricalNews"),
        title=str(row["title"]),
        as_of_date=date_value(row.get("as_of_date") or default_as_of),
        body=text_or_none(row.get("body")),
        source_tier=source_tier_value(row.get("source_tier"), SourceTier.TIER_2),
        theme_tags=tuple_value(row.get("theme_tags")),
        sentiment=float_or_none(row.get("sentiment")),
        parsed_fields=parsed_fields_from_record(row, known),
    )


def _price_bar(row: Mapping[str, Any], symbol: str) -> PriceBar:
    close = float(row["close"])
    low = float(row.get("low") or close)
    high = float(row.get("high") or close)
    return PriceBar(
        symbol=str(row.get("symbol") or symbol),
        date=date_value(row["date"]),
        open=float(row.get("open") or close),
        high=high,
        low=low,
        close=close,
        adj_close=float(row.get("adj_close") or close),
        volume=int_or_none(row.get("volume")) or 1000,
        trading_value=float_or_none(row.get("trading_value")) or close * (int_or_none(row.get("volume")) or 1000),
        market_cap=float_or_none(row.get("market_cap")) or close * 10_000_000.0,
        source=str(row.get("source") or "historical-case"),
        as_of_date=date_value(row.get("as_of_date") or row["date"]),
    )


def _stage_snapshot(row: Mapping[str, Any], symbol: str) -> StageSnapshot:
    return StageSnapshot(
        symbol=str(row.get("symbol") or symbol),
        as_of_date=date_value(row["as_of_date"]),
        stage=Stage(row["stage"]),
        previous_stage=Stage(row["previous_stage"]) if row.get("previous_stage") else None,
        stage_changed=bool_value(row.get("stage_changed", True)),
        grade=text_or_none(row.get("grade")),
        stage_reason=tuple_value(row.get("stage_reason")),
        red_team_status=text_or_none(row.get("red_team_status")),
        evidence_ids=tuple_value(row.get("evidence_ids")),
    )


def _evidence_records(
    *,
    symbol: str,
    market: Market,
    reports: Sequence[ResearchReport],
    disclosures: Sequence[DisclosureEvent],
    news_items: Sequence[NewsItem],
    consensus: Sequence[ConsensusSnapshot],
    revisions: Sequence[ConsensusRevision],
    actuals: Sequence[FinancialActual],
) -> tuple[Evidence, ...]:
    evidence: list[Evidence] = []
    for report in reports:
        timestamp = datetime(report.publish_date.year, report.publish_date.month, report.publish_date.day, 8, 0)
        evidence.append(
            Evidence(
                evidence_id=f"historical-report:{symbol}:{report.publish_date.isoformat()}:{report.broker}",
                source_type="research_report",
                source_name=report.broker,
                source_tier=SourceTier.TIER_1,
                published_at=timestamp,
                observed_at=timestamp,
                available_at=timestamp,
                as_of_date=report.as_of_date,
                market=market,
                symbol=symbol,
                title=report.title,
                excerpt_or_value=report.raw_text[:240] if report.raw_text else None,
                parsed_fields=report.parsed_fields,
                confidence=float(report.parsed_fields.get("parser_confidence", 0.8)),
            )
        )
    for item in disclosures:
        evidence.append(
            Evidence(
                evidence_id=f"historical-disclosure:{symbol}:{item.published_at.date().isoformat()}:{item.report_type}",
                source_type="disclosure",
                source_name=item.source,
                source_tier=SourceTier.TIER_0,
                published_at=item.published_at,
                observed_at=item.observed_at,
                available_at=item.available_at,
                as_of_date=item.as_of_date,
                market=market,
                symbol=symbol,
                title=item.title,
                url_or_identifier=item.rcept_no,
                excerpt_or_value=item.raw_text[:240] if item.raw_text else None,
                parsed_fields=item.parsed_fields,
                confidence=float(item.parsed_fields.get("parser_confidence", 0.8)),
            )
        )
    for item in news_items:
        evidence.append(
            Evidence(
                evidence_id=f"historical-news:{symbol}:{item.published_at.date().isoformat()}:{item.source}",
                source_type="news",
                source_name=item.source,
                source_tier=item.source_tier,
                published_at=item.published_at,
                observed_at=item.published_at,
                available_at=item.published_at,
                as_of_date=item.as_of_date,
                market=market,
                symbol=symbol,
                title=item.title,
                excerpt_or_value=item.body[:240] if item.body else None,
                parsed_fields=item.parsed_fields,
                confidence=float(item.parsed_fields.get("confidence", 0.7)),
            )
        )
    for item in consensus:
        timestamp = datetime(item.date.year, item.date.month, item.date.day, 8, 0)
        evidence.append(
            Evidence(
                evidence_id=f"historical-consensus:{symbol}:{item.date.isoformat()}:{item.fiscal_year}",
                source_type="consensus",
                source_name=item.source,
                source_tier=SourceTier.TIER_3,
                published_at=timestamp,
                observed_at=timestamp,
                available_at=timestamp,
                as_of_date=item.as_of_date,
                market=market,
                symbol=symbol,
                title=f"Consensus FY{item.fiscal_year}",
                parsed_fields={"eps_e": item.eps_e, "op_e": item.op_e, "fcf_e": item.fcf_e},
                confidence=0.7,
            )
        )
    for item in revisions:
        timestamp = datetime(item.date.year, item.date.month, item.date.day, 8, 0)
        evidence.append(
            Evidence(
                evidence_id=f"historical-revision:{symbol}:{item.date.isoformat()}:{item.fiscal_year}",
                source_type="consensus_revision",
                source_name="HistoricalConsensus",
                source_tier=SourceTier.TIER_3,
                published_at=timestamp,
                observed_at=timestamp,
                available_at=timestamp,
                as_of_date=item.as_of_date,
                market=market,
                symbol=symbol,
                title=f"Consensus revision FY{item.fiscal_year}",
                parsed_fields={
                    "eps_revision_1m": item.eps_revision_1m,
                    "op_revision_1m": item.op_revision_1m,
                    "fcf_revision_1m": item.fcf_revision_1m,
                    "target_price_revision_1m": item.target_price_revision_1m,
                },
                confidence=0.7,
            )
        )
    for item in actuals:
        evidence.append(
            Evidence(
                evidence_id=f"historical-actual:{symbol}:{item.period_end.isoformat()}",
                source_type="financial_actual",
                source_name=item.source,
                source_tier=SourceTier.TIER_0,
                published_at=item.reported_at,
                observed_at=item.reported_at,
                available_at=item.reported_at,
                as_of_date=item.as_of_date,
                market=market,
                symbol=symbol,
                title=f"Reported financials {item.period_end.isoformat()}",
                parsed_fields={"sales": item.sales, "operating_profit": item.operating_profit, "fcf": item.fcf},
                confidence=1.0,
            )
        )
    return tuple(evidence)


_REPORT_KEYS = {
    "symbol",
    "publish_date",
    "broker",
    "title",
    "as_of_date",
    "analyst",
    "current_price",
    "target_price",
    "rating",
    "target_revision_pct",
    "target_multiple_before",
    "target_multiple_after",
    "fy1_sales",
    "fy1_op",
    "fy1_eps",
    "fy2_sales",
    "fy2_op",
    "fy2_eps",
    "fy3_sales",
    "fy3_op",
    "fy3_eps",
    "est_per",
    "est_pbr",
    "upside_pct",
    "fifty_two_week_high",
    "fifty_two_week_low",
    "one_month_return",
    "three_month_return",
    "twelve_month_return",
    "roe",
    "opm",
    "backlog",
    "new_orders",
    "order_backlog_to_sales",
    "capa_increase_pct",
    "export_ratio",
    "us_revenue_ratio",
    "asp_increase_mentioned",
    "lead_time_mentioned",
    "shortage_mentioned",
    "investment_points",
    "risk_points",
    "raw_text",
    "parsed_fields",
}


__all__ = [
    "DEFAULT_HISTORICAL_CASE_DIR",
    "HistoricalCase",
    "HistoricalCasePipelineResult",
    "historical_case_from_mapping",
    "load_historical_case",
    "load_historical_cases",
    "run_historical_case_pipeline",
]
