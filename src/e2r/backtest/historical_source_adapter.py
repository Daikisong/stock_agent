"""Point-in-time historical sources for E2R_STANDARD replay."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Mapping, Sequence

from e2r.models import DisclosureEvent, FinancialActual, Instrument, Market, PriceBar
from e2r.research.report_snapshot_store import ReportSnapshotStore
from e2r.research.search_provider import SearchProvider, SearchResult
from e2r.research.search_snapshot_store import SearchSnapshotStore
from e2r.sources.kind import KINDRiskRecord


@dataclass(frozen=True)
class HistoricalSourceCoverage:
    """Coverage flags for one replay date."""

    universe_available: bool
    price_available: bool
    disclosure_available: bool
    financial_available: bool
    search_snapshot_available: bool
    report_snapshot_available: bool
    llm_available: bool = False
    coverage_notes: tuple[str, ...] = field(default_factory=tuple)

    def limitations(self) -> tuple[str, ...]:
        notes = list(self.coverage_notes)
        if not self.universe_available:
            notes.append("official_data_unavailable")
        if not self.price_available:
            notes.append("price_unavailable")
        if not self.disclosure_available:
            notes.append("disclosure_unavailable")
        if not self.financial_available:
            notes.append("financial_unavailable")
        if not self.search_snapshot_available:
            notes.append("search_snapshot_unavailable")
        if not self.report_snapshot_available:
            notes.append("report_snapshot_unavailable")
        if not self.search_snapshot_available or not self.report_snapshot_available:
            notes.append("candidate_generation_limited_by_missing_snapshots")
        return tuple(dict.fromkeys(notes))


@dataclass(frozen=True)
class HistoricalSourceBundle:
    """Sources and fixture text visible to E2R_STANDARD on one replay date."""

    sources: "SnapshotCheapScanSources"
    search_provider: "SnapshotSearchProvider"
    fixture_text_by_url: Mapping[str, str | Path]
    coverage: HistoricalSourceCoverage


class HistoricalPointInTimeSourceAdapter:
    """Build E2R_STANDARD-compatible sources for one historical replay date."""

    def __init__(
        self,
        *,
        search_snapshot_root: str | Path = "data/search_snapshots",
        report_snapshot_root: str | Path = "data/report_snapshots",
    ) -> None:
        self.search_store = SearchSnapshotStore(search_snapshot_root)
        self.report_store = ReportSnapshotStore(report_snapshot_root)

    def build(
        self,
        *,
        as_of_date: date,
        market: Market = Market.KR,
        use_search_snapshots: bool = True,
        use_report_snapshots: bool = True,
    ) -> HistoricalSourceBundle:
        searches = self.search_store.load_snapshots(as_of_date=as_of_date) if use_search_snapshots else ()
        reports = self.report_store.load_snapshots(as_of_date=as_of_date) if use_report_snapshots else ()
        instruments = _instruments_from_snapshots(searches, reports, market)
        provider = SnapshotSearchProvider(search_store=self.search_store if use_search_snapshots else None)
        text_by_url = self.report_store.fixture_text_by_url(as_of_date=as_of_date) if use_report_snapshots else {}
        coverage = HistoricalSourceCoverage(
            universe_available=bool(instruments),
            price_available=False,
            disclosure_available=False,
            financial_available=False,
            search_snapshot_available=bool(searches),
            report_snapshot_available=bool(reports),
            llm_available=False,
            coverage_notes=("snapshot_derived_universe" if instruments else "insufficient_historical_source_coverage",),
        )
        return HistoricalSourceBundle(
            sources=SnapshotCheapScanSources(instruments=instruments),
            search_provider=provider,
            fixture_text_by_url=text_by_url,
            coverage=coverage,
        )


@dataclass(frozen=True)
class SnapshotCheapScanSources:
    """Minimal cheap-scan source bundle backed by replay snapshots.

    Official historical rows can be added later. For now this intentionally
    exposes only point-in-time snapshot-derived universe membership and empty
    official sensors, instead of silently falling back to curated case fixtures.
    """

    instruments: tuple[Instrument, ...] = field(default_factory=tuple)
    price_bars_by_symbol: Mapping[str, tuple[PriceBar, ...]] = field(default_factory=dict)
    disclosures_by_symbol: Mapping[str, tuple[DisclosureEvent, ...]] = field(default_factory=dict)
    actuals_by_symbol: Mapping[str, tuple[FinancialActual, ...]] = field(default_factory=dict)
    risks_by_symbol: Mapping[str, tuple[KINDRiskRecord, ...]] = field(default_factory=dict)

    def list_instruments(self, market: Market, as_of_date: date) -> tuple[Instrument, ...]:
        return tuple(
            sorted(
                (
                    item
                    for item in self.instruments
                    if item.market == market and (item.listed_date is None or item.listed_date <= as_of_date)
                ),
                key=lambda item: item.symbol,
            )
        )

    def get_price_bars(self, symbol: str, as_of_date: date, lookback_days: int = 370) -> tuple[PriceBar, ...]:
        return tuple(item for item in self.price_bars_by_symbol.get(symbol, ()) if item.as_of_date <= as_of_date)

    def get_disclosures(self, symbol: str, as_of_date: date, lookback_days: int = 3) -> tuple[DisclosureEvent, ...]:
        return tuple(item for item in self.disclosures_by_symbol.get(symbol, ()) if item.available_at.date() <= as_of_date)

    def get_financial_actuals(self, symbol: str, as_of_date: date) -> tuple[FinancialActual, ...]:
        return tuple(item for item in self.actuals_by_symbol.get(symbol, ()) if item.as_of_date <= as_of_date)

    def get_risk_records(self, symbol: str, as_of_date: date) -> tuple[KINDRiskRecord, ...]:
        return tuple(self.risks_by_symbol.get(symbol, ()))

    def get_stock_issuance_records(self, symbol: str, as_of_date: date) -> tuple[dict, ...]:
        return ()


@dataclass(frozen=True)
class SnapshotSearchProvider:
    """Search provider backed by point-in-time search snapshots."""

    search_store: SearchSnapshotStore | None = None

    def search(self, query: str, as_of_date: date, max_results: int = 10) -> tuple[SearchResult, ...]:
        if self.search_store is None:
            return ()
        results = self.search_store.search_results(query=query, as_of_date=as_of_date, max_results=max_results)
        return tuple(item for item in results if item.published_at is None or item.published_at.date() <= as_of_date)


def _instruments_from_snapshots(
    searches: Sequence,
    reports: Sequence,
    market: Market,
) -> tuple[Instrument, ...]:
    by_symbol: dict[str, Instrument] = {}
    for item in tuple(searches) + tuple(reports):
        symbol = getattr(item, "symbol", None)
        company_name = getattr(item, "company_name", None)
        if not symbol or not company_name:
            continue
        by_symbol.setdefault(
            symbol,
            Instrument(
                symbol=symbol,
                name=company_name,
                market=market,
                exchange="KRX" if market == Market.KR else market.value,
                currency="KRW" if market == Market.KR else "USD",
            ),
        )
    return tuple(sorted(by_symbol.values(), key=lambda item: item.symbol))


__all__ = [
    "HistoricalPointInTimeSourceAdapter",
    "HistoricalSourceBundle",
    "HistoricalSourceCoverage",
    "SnapshotCheapScanSources",
    "SnapshotSearchProvider",
]
