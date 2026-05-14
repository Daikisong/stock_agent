"""Historical official source archive for as-of research replay."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Mapping

from e2r.models import DisclosureEvent, FinancialActual, Instrument, Market, PriceBar
from e2r.sources.kind import KINDConnector, KINDRiskRecord
from e2r.sources.opendart import OpenDARTConnector
from e2r.sources.source_errors import date_value, datetime_value, float_or_none, int_or_none, load_fixture_records, market_value


DEFAULT_HISTORICAL_OFFICIAL_ROOT = Path("data/historical_official")


@dataclass(frozen=True)
class HistoricalOfficialCoverage:
    """Historical official archive coverage at one replay date."""

    universe_available: bool
    price_available: bool
    disclosure_available: bool
    financial_available: bool
    risk_available: bool
    notes: tuple[str, ...] = ()

    def limitations(self) -> tuple[str, ...]:
        notes = list(self.notes)
        if not self.universe_available:
            notes.append("insufficient_official_historical_universe")
        if not self.price_available:
            notes.append("no_price_history")
        if not self.disclosure_available:
            notes.append("no_disclosure_snapshot")
        if not self.financial_available:
            notes.append("no_financial_snapshot")
        return tuple(dict.fromkeys(notes))


class HistoricalOfficialStore:
    """CSV/JSON-backed official historical source archive."""

    def __init__(self, root: str | Path = DEFAULT_HISTORICAL_OFFICIAL_ROOT) -> None:
        self.root = Path(root)

    def load_universe(self, as_of_date: date, market: Market = Market.KR) -> tuple[Instrument, ...]:
        rows = load_fixture_records(self.root / "universe", "universe")
        instruments = tuple(_instrument(row) for row in rows)
        return tuple(
            sorted(
                (
                    item
                    for item in instruments
                    if item.market == market and (item.listed_date is None or item.listed_date <= as_of_date)
                ),
                key=lambda item: item.symbol,
            )
        )

    def load_price_bars(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[PriceBar, ...]:
        bars = tuple(_price_bar(row) for row in load_fixture_records(self.root / "prices", "prices"))
        return tuple(
            sorted(
                (
                    item
                    for item in bars
                    if item.symbol == symbol
                    and start <= item.date <= min(end, as_of_date)
                    and item.as_of_date <= as_of_date
                ),
                key=lambda item: item.date,
            )
        )

    def load_disclosures(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[DisclosureEvent, ...]:
        events = tuple(OpenDARTConnector.normalize_disclosure(row) for row in load_fixture_records(self.root / "disclosures", "disclosures"))
        return tuple(
            sorted(
                (
                    item
                    for item in events
                    if item.symbol == symbol
                    and start <= item.published_at.date() <= min(end, as_of_date)
                    and item.available_at.date() <= as_of_date
                ),
                key=lambda item: item.published_at,
            )
        )

    def load_financial_actuals(self, symbol: str, as_of_date: date) -> tuple[FinancialActual, ...]:
        actuals = tuple(_financial_actual(row) for row in load_fixture_records(self.root / "financials", "financials"))
        return tuple(
            sorted(
                (
                    item
                    for item in actuals
                    if item.symbol == symbol and item.reported_at.date() <= as_of_date and item.as_of_date <= as_of_date
                ),
                key=lambda item: (item.period_end, item.reported_at),
            )
        )

    def load_risk_records(self, symbol: str, as_of_date: date) -> tuple[KINDRiskRecord, ...]:
        records = tuple(KINDConnector.normalize_risk_record(row) for row in load_fixture_records(self.root / "risks", "risks"))
        return tuple(
            sorted((item for item in records if item.symbol == symbol and item.as_of_date <= as_of_date), key=lambda item: item.as_of_date)
        )

    def coverage(self, as_of_date: date, market: Market = Market.KR) -> HistoricalOfficialCoverage:
        universe = self.load_universe(as_of_date, market)
        sample_symbols = tuple(item.symbol for item in universe[:20])
        price_available = any(
            self.load_price_bars(symbol, as_of_date - timedelta(days=370), as_of_date, as_of_date) for symbol in sample_symbols
        )
        disclosure_available = any(self.load_disclosures(symbol, as_of_date - timedelta(days=370), as_of_date, as_of_date) for symbol in sample_symbols)
        financial_available = any(self.load_financial_actuals(symbol, as_of_date) for symbol in sample_symbols)
        risk_available = any(self.load_risk_records(symbol, as_of_date) for symbol in sample_symbols)
        return HistoricalOfficialCoverage(
            universe_available=bool(universe),
            price_available=price_available,
            disclosure_available=disclosure_available,
            financial_available=financial_available,
            risk_available=risk_available,
            notes=(("fixture_official_archive" if universe else "official_history_missing"),),
        )


@dataclass(frozen=True)
class HistoricalOfficialSources:
    """KoreaCheapScanner-compatible source bundle backed by official history."""

    store: HistoricalOfficialStore

    def list_instruments(self, market: Market, as_of_date: date) -> tuple[Instrument, ...]:
        return self.store.load_universe(as_of_date, market)

    def get_price_bars(self, symbol: str, as_of_date: date, lookback_days: int = 370) -> tuple[PriceBar, ...]:
        return self.store.load_price_bars(symbol, as_of_date - timedelta(days=lookback_days), as_of_date, as_of_date)

    def get_disclosures(self, symbol: str, as_of_date: date, lookback_days: int = 45) -> tuple[DisclosureEvent, ...]:
        return self.store.load_disclosures(symbol, as_of_date - timedelta(days=lookback_days), as_of_date, as_of_date)

    def get_financial_actuals(self, symbol: str, as_of_date: date) -> tuple[FinancialActual, ...]:
        return self.store.load_financial_actuals(symbol, as_of_date)

    def get_risk_records(self, symbol: str, as_of_date: date) -> tuple[KINDRiskRecord, ...]:
        return self.store.load_risk_records(symbol, as_of_date)

    def get_stock_issuance_records(self, symbol: str, as_of_date: date) -> tuple[dict[str, Any], ...]:
        return ()


def _instrument(row: Mapping[str, Any]) -> Instrument:
    return Instrument(
        symbol=str(row.get("symbol") or row.get("srtnCd") or row.get("isinCd")),
        name=str(row.get("name") or row.get("itmsNm") or row.get("corpNm")),
        market=market_value(row.get("market"), Market.KR),
        exchange=str(row.get("exchange") or row.get("mrktCtg") or "KRX"),
        sector_custom=str(row.get("sector_custom")) if row.get("sector_custom") else None,
        listed_date=date_value(row["listed_date"]) if row.get("listed_date") else None,
        currency=str(row.get("currency") or "KRW"),
        is_managed=_bool(row.get("is_managed")),
        is_invest_warning=_bool(row.get("is_invest_warning")),
        is_trading_halt=_bool(row.get("is_trading_halt")),
    )


def _price_bar(row: Mapping[str, Any]) -> PriceBar:
    close = float_or_none(row.get("close") or row.get("clpr")) or 1.0
    open_price = float_or_none(row.get("open") or row.get("mkp")) or close
    high = float_or_none(row.get("high") or row.get("hipr")) or max(open_price, close)
    low = float_or_none(row.get("low") or row.get("lopr")) or min(open_price, close)
    return PriceBar(
        symbol=str(row.get("symbol") or row.get("srtnCd") or row.get("isinCd")),
        date=date_value(row.get("date") or row.get("basDt")),
        open=open_price,
        high=max(high, close, open_price),
        low=min(low, close, open_price),
        close=close,
        adj_close=float_or_none(row.get("adj_close")) or close,
        volume=int_or_none(row.get("volume") or row.get("trqu")) or 0,
        trading_value=float_or_none(row.get("trading_value") or row.get("trPrc")) or 0.0,
        market_cap=float_or_none(row.get("market_cap") or row.get("mrktTotAmt")),
        source=str(row.get("source") or "historical_official"),
        as_of_date=date_value(row.get("as_of_date") or row.get("date") or row.get("basDt")),
    )


def _financial_actual(row: Mapping[str, Any]) -> FinancialActual:
    return FinancialActual(
        symbol=str(row["symbol"]),
        fiscal_year=int(float(row["fiscal_year"])),
        fiscal_quarter=int(float(row["fiscal_quarter"])) if row.get("fiscal_quarter") not in (None, "") else None,
        period_end=date_value(row["period_end"]),
        reported_at=datetime_value(row["reported_at"]),
        as_of_date=date_value(row.get("as_of_date") or row["reported_at"]),
        source=str(row.get("source") or "historical_official"),
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


def _bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return False
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on", "있음"}


__all__ = [
    "DEFAULT_HISTORICAL_OFFICIAL_ROOT",
    "HistoricalOfficialCoverage",
    "HistoricalOfficialSources",
    "HistoricalOfficialStore",
]
