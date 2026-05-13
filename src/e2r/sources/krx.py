"""KRX source connector for instruments, prices, and listing status."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Mapping

from e2r.models import (
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
from e2r.sources.source_errors import (
    SourceRequest,
    bool_value,
    date_value,
    float_or_none,
    int_or_none,
    load_fixture_records,
    text_or_none,
)


KRX_BASE_URL = "https://data.krx.co.kr"


@dataclass(frozen=True)
class KRXConnector:
    """KRX connector with fixture mode as the default.

    Live KRX endpoints can be represented as request metadata, but this class
    does not execute live scraping. Tests and local research use CSV/JSON files.
    """

    fixture_root: str | Path | None = "data/raw/krx"
    fixture_mode: bool = True
    base_url: str = KRX_BASE_URL

    def build_instruments_request(self, market: Market, as_of_date: date) -> SourceRequest:
        return SourceRequest(
            method="GET",
            url=f"{self.base_url}/comm/bldAttendant/getJsonData.cmd",
            params={
                "bld": "dbms/MDC/STAT/standard/MDCSTAT01901",
                "mktId": "STK" if market == Market.KR else market.value,
                "trdDd": as_of_date.strftime("%Y%m%d"),
            },
            fixture_mode=self.fixture_mode,
        )

    def build_price_bars_request(self, symbol: str, start: date, end: date, as_of_date: date) -> SourceRequest:
        return SourceRequest(
            method="GET",
            url=f"{self.base_url}/comm/bldAttendant/getJsonData.cmd",
            params={
                "bld": "dbms/MDC/STAT/standard/MDCSTAT01701",
                "isuCd": symbol,
                "strtDd": start.strftime("%Y%m%d"),
                "endDd": min(end, as_of_date).strftime("%Y%m%d"),
            },
            fixture_mode=self.fixture_mode,
        )

    def list_instruments(self, market: Market, as_of_date: date) -> tuple[Instrument, ...]:
        rows = load_fixture_records(self.fixture_root, "instruments")
        instruments = tuple(self.normalize_instrument(row) for row in rows)
        return tuple(
            sorted(
                (
                    item
                    for item in instruments
                    if item.market == market
                    and (item.listed_date is None or item.listed_date <= as_of_date)
                    and not self._delisted_by_as_of(item.symbol, as_of_date)
                ),
                key=lambda item: item.symbol,
            )
        )

    def get_price_bars(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[PriceBar, ...]:
        bars = tuple(self.normalize_price_bar(row) for row in load_fixture_records(self.fixture_root, "prices"))
        return tuple(
            sorted(
                (
                    bar
                    for bar in bars
                    if bar.symbol == symbol
                    and start <= bar.date <= end
                    and bar.date <= as_of_date
                    and bar.as_of_date <= as_of_date
                ),
                key=lambda item: item.date,
            )
        )

    def get_52_week_range(self, symbol: str, as_of_date: date) -> tuple[float | None, float | None]:
        """Return low/high for the latest 52-week window available as of date."""

        bars = self.get_price_bars(symbol, as_of_date - timedelta(days=370), as_of_date, as_of_date)
        if not bars:
            return None, None
        return min(bar.low for bar in bars), max(bar.high for bar in bars)

    def get_listing_status(self, symbol: str, as_of_date: date) -> dict[str, Any]:
        """Return fixture-backed exchange risk/status fields when available."""

        for row in load_fixture_records(self.fixture_root, "instruments"):
            if str(row.get("symbol")) != symbol:
                continue
            delisted_date = text_or_none(row.get("delisted_date"))
            return {
                "is_managed": bool_value(row.get("is_managed")),
                "is_invest_warning": bool_value(row.get("is_invest_warning")),
                "is_trading_halt": bool_value(row.get("is_trading_halt")),
                "delisted_date": delisted_date,
                "is_delisted_as_of": bool(delisted_date and date_value(delisted_date) <= as_of_date),
            }
        return {}

    @staticmethod
    def normalize_instrument(row: Mapping[str, Any]) -> Instrument:
        market = Market(str(row.get("market") or "KR"))
        return Instrument(
            symbol=str(row["symbol"]),
            name=str(row["name"]),
            market=market,
            exchange=str(row.get("exchange") or "KRX"),
            sector_exchange=text_or_none(row.get("sector_exchange")),
            sector_custom=text_or_none(row.get("sector_custom")),
            listed_date=date_value(row["listed_date"]) if row.get("listed_date") else None,
            currency=str(row.get("currency") or ("KRW" if market == Market.KR else "USD")),
            is_preferred=bool_value(row.get("is_preferred")),
            is_spac=bool_value(row.get("is_spac")),
            is_reit=bool_value(row.get("is_reit")),
            is_etf=bool_value(row.get("is_etf")),
            is_managed=bool_value(row.get("is_managed")),
            is_invest_warning=bool_value(row.get("is_invest_warning")),
            is_trading_halt=bool_value(row.get("is_trading_halt")),
        )

    @staticmethod
    def normalize_price_bar(row: Mapping[str, Any]) -> PriceBar:
        return PriceBar(
            symbol=str(row["symbol"]),
            date=date_value(row["date"]),
            open=float(str(row["open"]).replace(",", "")),
            high=float(str(row["high"]).replace(",", "")),
            low=float(str(row["low"]).replace(",", "")),
            close=float(str(row["close"]).replace(",", "")),
            adj_close=float(str(row.get("adj_close") or row["close"]).replace(",", "")),
            volume=int_or_none(row.get("volume")) or 0,
            trading_value=float_or_none(row.get("trading_value")) or 0.0,
            market_cap=float_or_none(row.get("market_cap")),
            source=str(row.get("source") or "krx-fixture"),
            as_of_date=date_value(row.get("as_of_date") or row["date"]),
        )

    def _delisted_by_as_of(self, symbol: str, as_of_date: date) -> bool:
        status = self.get_listing_status(symbol, as_of_date)
        return bool(status.get("is_delisted_as_of"))

    def get_financial_actuals(self, symbol: str, as_of_date: date) -> tuple[FinancialActual, ...]:
        return ()

    def get_consensus(self, symbol: str, as_of_date: date) -> tuple[ConsensusSnapshot, ...]:
        return ()

    def get_consensus_revisions(self, symbol: str, as_of_date: date) -> tuple[ConsensusRevision, ...]:
        return ()

    def get_disclosures(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[DisclosureEvent, ...]:
        return ()

    def get_research_reports(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[ResearchReport, ...]:
        return ()

    def get_news(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[NewsItem, ...]:
        return ()
