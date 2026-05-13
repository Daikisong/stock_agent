"""Data connector interfaces and mock/fallback implementations."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Protocol, Sequence

from .fixtures import FIXTURE_CASES, FixtureCase
from .models import (
    ConsensusRevision,
    ConsensusSnapshot,
    DisclosureEvent,
    FinancialActual,
    Instrument,
    Market,
    NewsItem,
    PriceBar,
    ResearchReport,
)


def _require_date(value: date, field_name: str) -> None:
    if type(value) is not date:
        raise ValueError(f"{field_name} must be a date")


def _require_text(value: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")


def _validate_range(start: date, end: date, as_of_date: date) -> None:
    _require_date(start, "start")
    _require_date(end, "end")
    _require_date(as_of_date, "as_of_date")
    if start > end:
        raise ValueError("start cannot be after end")


class DataConnector(Protocol):
    """Stable data access interface for mock and future live connectors."""

    def list_instruments(self, market: Market, as_of_date: date) -> tuple[Instrument, ...]:
        """Return instruments available as of the date."""

    def get_price_bars(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[PriceBar, ...]:
        """Return price bars known as of the date."""

    def get_financial_actuals(self, symbol: str, as_of_date: date) -> tuple[FinancialActual, ...]:
        """Return reported financials known as of the date."""

    def get_consensus(self, symbol: str, as_of_date: date) -> tuple[ConsensusSnapshot, ...]:
        """Return consensus snapshots known as of the date."""

    def get_consensus_revisions(self, symbol: str, as_of_date: date) -> tuple[ConsensusRevision, ...]:
        """Return consensus revision metrics known as of the date."""

    def get_disclosures(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[DisclosureEvent, ...]:
        """Return filings and exchange disclosures known as of the date."""

    def get_research_reports(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[ResearchReport, ...]:
        """Return research reports known as of the date."""

    def get_news(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[NewsItem, ...]:
        """Return news items known as of the date."""


@dataclass(frozen=True)
class MockDataConnector:
    """In-memory connector used before live API integration."""

    instruments: Sequence[Instrument] = field(default_factory=tuple)
    price_bars: Sequence[PriceBar] = field(default_factory=tuple)
    financial_actuals: Sequence[FinancialActual] = field(default_factory=tuple)
    consensus: Sequence[ConsensusSnapshot] = field(default_factory=tuple)
    consensus_revisions: Sequence[ConsensusRevision] = field(default_factory=tuple)
    disclosures: Sequence[DisclosureEvent] = field(default_factory=tuple)
    research_reports: Sequence[ResearchReport] = field(default_factory=tuple)
    news_items: Sequence[NewsItem] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        object.__setattr__(self, "instruments", tuple(self.instruments))
        object.__setattr__(self, "price_bars", tuple(self.price_bars))
        object.__setattr__(self, "financial_actuals", tuple(self.financial_actuals))
        object.__setattr__(self, "consensus", tuple(self.consensus))
        object.__setattr__(self, "consensus_revisions", tuple(self.consensus_revisions))
        object.__setattr__(self, "disclosures", tuple(self.disclosures))
        object.__setattr__(self, "research_reports", tuple(self.research_reports))
        object.__setattr__(self, "news_items", tuple(self.news_items))

    @classmethod
    def from_fixture_cases(cls, fixture_cases: Sequence[FixtureCase] = FIXTURE_CASES) -> "MockDataConnector":
        """Create a mock connector from synthetic fixture cases."""

        instruments: list[Instrument] = []
        price_bars: list[PriceBar] = []
        consensus: list[ConsensusSnapshot] = []
        reports: list[ResearchReport] = []
        news: list[NewsItem] = []

        for case in fixture_cases:
            symbol = case.scoring_payload.symbol
            first_bar_date = min(bar.date for bar in case.price_bars)
            instruments.append(
                Instrument(
                    symbol=symbol,
                    name=case.case_id,
                    market=case.market,
                    exchange="KRX" if case.market == Market.KR else "US-MOCK",
                    sector_custom=case.category.value,
                    listed_date=first_bar_date,
                    currency="KRW" if case.market == Market.KR else "USD",
                )
            )
            price_bars.extend(case.price_bars)
            consensus.append(
                ConsensusSnapshot(
                    symbol=symbol,
                    date=case.scoring_payload.as_of_date,
                    fiscal_year=case.scoring_payload.as_of_date.year + 1,
                    as_of_date=case.scoring_payload.as_of_date,
                    source="fixture-consensus",
                    analyst_count=3,
                    target_price=case.stage3_price * 1.5,
                )
            )
            reports.append(
                ResearchReport(
                    symbol=symbol,
                    publish_date=case.scoring_payload.as_of_date,
                    broker="FixtureBroker",
                    title=f"{case.case_id} structured rerating fixture",
                    as_of_date=case.scoring_payload.as_of_date,
                    current_price=case.stage3_price,
                    target_price=case.stage3_price * 1.5,
                    investment_points=(case.description,),
                    risk_points=("synthetic fixture only",),
                )
            )
            news.append(
                NewsItem(
                    symbol=symbol,
                    sector=case.category.value,
                    published_at=datetime(
                        case.scoring_payload.as_of_date.year,
                        case.scoring_payload.as_of_date.month,
                        case.scoring_payload.as_of_date.day,
                        8,
                        0,
                    ),
                    source="fixture-news",
                    title=f"{case.case_id} regime note",
                    as_of_date=case.scoring_payload.as_of_date,
                    theme_tags=(case.category.value,),
                    parsed_fields={"fixture": True},
                )
            )

        return cls(
            instruments=tuple(instruments),
            price_bars=tuple(price_bars),
            consensus=tuple(consensus),
            research_reports=tuple(reports),
            news_items=tuple(news),
        )

    def list_instruments(self, market: Market, as_of_date: date) -> tuple[Instrument, ...]:
        _require_date(as_of_date, "as_of_date")
        return tuple(
            sorted(
                (
                    instrument
                    for instrument in self.instruments
                    if instrument.market == market
                    and (instrument.listed_date is None or instrument.listed_date <= as_of_date)
                ),
                key=lambda instrument: instrument.symbol,
            )
        )

    def get_price_bars(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[PriceBar, ...]:
        _require_text(symbol, "symbol")
        _validate_range(start, end, as_of_date)
        return tuple(
            sorted(
                (
                    bar
                    for bar in self.price_bars
                    if bar.symbol == symbol
                    and start <= bar.date <= end
                    and bar.as_of_date <= as_of_date
                ),
                key=lambda bar: bar.date,
            )
        )

    def get_financial_actuals(self, symbol: str, as_of_date: date) -> tuple[FinancialActual, ...]:
        _require_text(symbol, "symbol")
        _require_date(as_of_date, "as_of_date")
        return tuple(
            sorted(
                (
                    item
                    for item in self.financial_actuals
                    if item.symbol == symbol and item.reported_at.date() <= as_of_date
                ),
                key=lambda item: (item.period_end, item.reported_at),
            )
        )

    def get_consensus(self, symbol: str, as_of_date: date) -> tuple[ConsensusSnapshot, ...]:
        _require_text(symbol, "symbol")
        _require_date(as_of_date, "as_of_date")
        return tuple(
            sorted(
                (
                    item
                    for item in self.consensus
                    if item.symbol == symbol and item.date <= as_of_date and item.as_of_date <= as_of_date
                ),
                key=lambda item: (item.date, item.fiscal_year),
            )
        )

    def get_consensus_revisions(self, symbol: str, as_of_date: date) -> tuple[ConsensusRevision, ...]:
        _require_text(symbol, "symbol")
        _require_date(as_of_date, "as_of_date")
        return tuple(
            sorted(
                (
                    item
                    for item in self.consensus_revisions
                    if item.symbol == symbol and item.date <= as_of_date and item.as_of_date <= as_of_date
                ),
                key=lambda item: (item.date, item.fiscal_year),
            )
        )

    def get_disclosures(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[DisclosureEvent, ...]:
        _require_text(symbol, "symbol")
        _validate_range(start, end, as_of_date)
        return tuple(
            sorted(
                (
                    item
                    for item in self.disclosures
                    if item.symbol == symbol
                    and start <= item.published_at.date() <= end
                    and item.available_at.date() <= as_of_date
                ),
                key=lambda item: item.published_at,
            )
        )

    def get_research_reports(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[ResearchReport, ...]:
        _require_text(symbol, "symbol")
        _validate_range(start, end, as_of_date)
        return tuple(
            sorted(
                (
                    item
                    for item in self.research_reports
                    if item.symbol == symbol
                    and start <= item.publish_date <= end
                    and item.as_of_date <= as_of_date
                ),
                key=lambda item: item.publish_date,
            )
        )

    def get_news(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[NewsItem, ...]:
        _require_text(symbol, "symbol")
        _validate_range(start, end, as_of_date)
        return tuple(
            sorted(
                (
                    item
                    for item in self.news_items
                    if item.symbol == symbol
                    and start <= item.published_at.date() <= end
                    and item.published_at.date() <= as_of_date
                ),
                key=lambda item: item.published_at,
            )
        )


@dataclass(frozen=True)
class EmptyDataConnector(MockDataConnector):
    """Explicit empty fallback connector."""


@dataclass(frozen=True)
class FallbackDataConnector:
    """Use fallback data when the primary connector has no result."""

    primary: DataConnector
    fallback: DataConnector

    def list_instruments(self, market: Market, as_of_date: date) -> tuple[Instrument, ...]:
        result = self.primary.list_instruments(market, as_of_date)
        return result if result else self.fallback.list_instruments(market, as_of_date)

    def get_price_bars(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[PriceBar, ...]:
        result = self.primary.get_price_bars(symbol, start, end, as_of_date)
        return result if result else self.fallback.get_price_bars(symbol, start, end, as_of_date)

    def get_financial_actuals(self, symbol: str, as_of_date: date) -> tuple[FinancialActual, ...]:
        result = self.primary.get_financial_actuals(symbol, as_of_date)
        return result if result else self.fallback.get_financial_actuals(symbol, as_of_date)

    def get_consensus(self, symbol: str, as_of_date: date) -> tuple[ConsensusSnapshot, ...]:
        result = self.primary.get_consensus(symbol, as_of_date)
        return result if result else self.fallback.get_consensus(symbol, as_of_date)

    def get_consensus_revisions(self, symbol: str, as_of_date: date) -> tuple[ConsensusRevision, ...]:
        result = self.primary.get_consensus_revisions(symbol, as_of_date)
        return result if result else self.fallback.get_consensus_revisions(symbol, as_of_date)

    def get_disclosures(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[DisclosureEvent, ...]:
        result = self.primary.get_disclosures(symbol, start, end, as_of_date)
        return result if result else self.fallback.get_disclosures(symbol, start, end, as_of_date)

    def get_research_reports(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[ResearchReport, ...]:
        result = self.primary.get_research_reports(symbol, start, end, as_of_date)
        return result if result else self.fallback.get_research_reports(symbol, start, end, as_of_date)

    def get_news(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[NewsItem, ...]:
        result = self.primary.get_news(symbol, start, end, as_of_date)
        return result if result else self.fallback.get_news(symbol, start, end, as_of_date)

