"""Korea cheap-scan source bundle and free fixture adapters."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Mapping

from e2r.models import DisclosureEvent, FinancialActual, Instrument, Market, PriceBar
from e2r.sources import KINDConnector, KRXConnector, OpenDARTConnector
from e2r.sources.kind import KINDRiskRecord
from e2r.sources.source_errors import SourceRequest, date_value, float_or_none, int_or_none, load_fixture_records, require_credential


FSC_BASE_URL = "https://apis.data.go.kr/1160100/service"


@dataclass(frozen=True)
class DataGoKrFSCConnector:
    """Fixture-first Financial Services Commission API adapter.

    Live calls are represented as ``SourceRequest`` objects. Tests use fixture
    records only.
    """

    service_key: str | None = None
    fixture_root: str | Path | None = "data/raw/data_go_kr_fsc"
    fixture_mode: bool = True
    base_url: str = FSC_BASE_URL
    enable_stock_issuance_source: bool = False

    def require_live_credentials(self) -> str:
        return require_credential(self.service_key, "DATA_GO_KR_SERVICE_KEY")

    def build_listed_items_request(self, market: Market, as_of_date: date) -> SourceRequest:
        return self._request(
            "GetKrxListedInfoService/getItemInfo",
            {
                "market": market.value,
                "basDt": as_of_date.strftime("%Y%m%d"),
            },
        )

    def build_listed_items_page_request(self, market: Market, as_of_date: date, page_no: int = 1, num_rows: int = 1000) -> SourceRequest:
        return self._request(
            "GetKrxListedInfoService/getItemInfo",
            {
                "market": market.value,
                "basDt": as_of_date.strftime("%Y%m%d"),
                "pageNo": page_no,
                "numOfRows": num_rows,
            },
        )

    def build_stock_price_request(self, symbol: str, start: date, end: date, as_of_date: date) -> SourceRequest:
        return self._request(
            "GetStockSecuritiesInfoService/getStockPriceInfo",
            {
                "likeSrtnCd": symbol,
                "beginBasDt": start.strftime("%Y%m%d"),
                "endBasDt": min(end, as_of_date).strftime("%Y%m%d"),
            },
        )

    def build_stock_price_page_request(self, start: date, end: date, as_of_date: date, page_no: int = 1, num_rows: int = 1000) -> SourceRequest:
        return self._request(
            "GetStockSecuritiesInfoService/getStockPriceInfo",
            {
                "beginBasDt": start.strftime("%Y%m%d"),
                "endBasDt": min(end, as_of_date).strftime("%Y%m%d"),
                "pageNo": page_no,
                "numOfRows": num_rows,
            },
        )

    def build_financial_info_request(self, symbol: str, as_of_date: date) -> SourceRequest:
        return self._request(
            "GetCorpFinanceInfoService/getCorpFinanceInfo",
            {
                "likeSrtnCd": symbol,
                "basDt": as_of_date.strftime("%Y%m%d"),
            },
        )

    def build_disclosure_info_request(self, symbol: str, start: date, end: date, as_of_date: date) -> SourceRequest:
        return self._request(
            "GetCorpDisclosureInfoService/getDisclosureInfo",
            {
                "likeSrtnCd": symbol,
                "beginBasDt": start.strftime("%Y%m%d"),
                "endBasDt": min(end, as_of_date).strftime("%Y%m%d"),
            },
        )

    def build_stock_issuance_request(self, symbol: str, as_of_date: date) -> SourceRequest:
        return self._request(
            "GetStockIssuanceInfoService/getStockIssueInfo",
            {
                "likeSrtnCd": symbol,
                "basDt": as_of_date.strftime("%Y%m%d"),
            },
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
                ),
                key=lambda item: item.symbol,
            )
        )

    def get_price_bars(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[PriceBar, ...]:
        bars = tuple(self.normalize_price_bar(row) for row in load_fixture_records(self.fixture_root, "prices"))
        return tuple(
            sorted(
                (
                    item
                    for item in bars
                    if item.symbol == symbol
                    and start <= item.date <= end
                    and item.date <= as_of_date
                    and item.as_of_date <= as_of_date
                ),
                key=lambda item: item.date,
            )
        )

    def get_financial_actuals(self, symbol: str, as_of_date: date) -> tuple[FinancialActual, ...]:
        rows = load_fixture_records(self.fixture_root, "financial_actuals")
        return tuple(
            sorted(
                (
                    _financial_actual(row)
                    for row in rows
                    if str(row.get("symbol")) == symbol
                    and date_value(row.get("as_of_date") or row.get("reported_at")) <= as_of_date
                ),
                key=lambda item: (item.period_end, item.reported_at),
            )
        )

    def get_disclosures(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[DisclosureEvent, ...]:
        events = tuple(OpenDARTConnector.normalize_disclosure(row) for row in load_fixture_records(self.fixture_root, "disclosures"))
        return tuple(
            sorted(
                (
                    item
                    for item in events
                    if item.symbol == symbol
                    and start <= item.published_at.date() <= end
                    and item.published_at.date() <= as_of_date
                    and item.available_at.date() <= as_of_date
                ),
                key=lambda item: item.published_at,
            )
        )

    def get_stock_issuance_records(self, symbol: str, as_of_date: date) -> tuple[dict[str, Any], ...]:
        """Return raw FSC stock-issuance fixture rows visible as of date."""

        if not self.enable_stock_issuance_source:
            return ()
        rows = load_fixture_records(self.fixture_root, "stock_issuance")
        return tuple(
            row
            for row in rows
            if str(row.get("symbol") or row.get("srtnCd") or row.get("isinCd")) == symbol
            and date_value(row.get("as_of_date") or row.get("basDt") or as_of_date) <= as_of_date
        )

    def _request(self, path: str, params: Mapping[str, Any]) -> SourceRequest:
        payload = dict(params)
        if self.service_key:
            payload["serviceKey"] = self.service_key
        payload.setdefault("resultType", "json")
        return SourceRequest(
            method="GET",
            url=f"{self.base_url}/{path}",
            params=payload,
            fixture_mode=self.fixture_mode,
            credential_name="DATA_GO_KR_SERVICE_KEY",
        )

    @staticmethod
    def normalize_instrument(row: Mapping[str, Any]) -> Instrument:
        return _instrument_from_fsc(row)

    @staticmethod
    def normalize_price_bar(row: Mapping[str, Any]) -> PriceBar:
        mapped = {
            "symbol": row.get("symbol") or row.get("srtnCd") or row.get("isinCd"),
            "date": row.get("date") or row.get("basDt"),
            "open": row.get("open") or row.get("mkp") or row.get("clpr"),
            "high": row.get("high") or row.get("hipr") or row.get("clpr"),
            "low": row.get("low") or row.get("lopr") or row.get("clpr"),
            "close": row.get("close") or row.get("clpr"),
            "adj_close": row.get("adj_close") or row.get("clpr") or row.get("close"),
            "volume": row.get("volume") or row.get("trqu") or 0,
            "trading_value": row.get("trading_value") or row.get("trPrc") or 0,
            "market_cap": row.get("market_cap") or row.get("mrktTotAmt"),
            "source": row.get("source") or "data.go.kr FSC",
            "as_of_date": row.get("as_of_date") or row.get("basDt") or row.get("date"),
        }
        return PriceBar(
            symbol=str(mapped["symbol"]),
            date=date_value(mapped["date"]),
            open=float_or_none(mapped["open"]) or 0.0,
            high=float_or_none(mapped["high"]) or 0.0,
            low=float_or_none(mapped["low"]) or 0.0,
            close=float_or_none(mapped["close"]) or 0.0,
            adj_close=float_or_none(mapped["adj_close"]) or 0.0,
            volume=int_or_none(mapped["volume"]) or 0,
            trading_value=float_or_none(mapped["trading_value"]) or 0.0,
            market_cap=float_or_none(mapped["market_cap"]),
            source=str(mapped["source"]),
            as_of_date=date_value(mapped["as_of_date"]),
        )


@dataclass(frozen=True)
class KoreaCheapScanSources:
    """Source bundle for Korea cheap scan."""

    krx: KRXConnector | None = None
    opendart: OpenDARTConnector | None = None
    kind: KINDConnector | None = None
    fsc: DataGoKrFSCConnector | None = None

    @classmethod
    def local_defaults(cls) -> "KoreaCheapScanSources":
        return cls(
            krx=KRXConnector(),
            opendart=OpenDARTConnector(),
            kind=KINDConnector(),
            fsc=DataGoKrFSCConnector(),
        )

    def list_instruments(self, market: Market, as_of_date: date) -> tuple[Instrument, ...]:
        instruments: dict[str, Instrument] = {}
        if self.krx is not None:
            for item in self.krx.list_instruments(market, as_of_date):
                instruments.setdefault(item.symbol, item)
        if self.fsc is not None:
            for item in self.fsc.list_instruments(market, as_of_date):
                instruments.setdefault(item.symbol, item)
        return tuple(sorted(instruments.values(), key=lambda item: item.symbol))

    def get_price_bars(self, symbol: str, as_of_date: date, lookback_days: int = 370) -> tuple[PriceBar, ...]:
        start = as_of_date - timedelta(days=lookback_days)
        bars: dict[tuple[str, date], PriceBar] = {}
        if self.krx is not None:
            for item in self.krx.get_price_bars(symbol, start, as_of_date, as_of_date):
                bars[(item.symbol, item.date)] = item
        if self.fsc is not None:
            for item in self.fsc.get_price_bars(symbol, start, as_of_date, as_of_date):
                bars.setdefault((item.symbol, item.date), item)
        return tuple(sorted(bars.values(), key=lambda item: item.date))

    def get_disclosures(self, symbol: str, as_of_date: date, lookback_days: int = 3) -> tuple[DisclosureEvent, ...]:
        start = as_of_date - timedelta(days=lookback_days)
        events: dict[str, DisclosureEvent] = {}
        if self.opendart is not None:
            for item in self.opendart.get_disclosures(symbol, start, as_of_date, as_of_date):
                events[f"{item.source}:{item.rcept_no or item.published_at.isoformat()}"] = item
        if self.fsc is not None:
            for item in self.fsc.get_disclosures(symbol, start, as_of_date, as_of_date):
                events.setdefault(f"{item.source}:{item.rcept_no or item.published_at.isoformat()}", item)
        return tuple(sorted(events.values(), key=lambda item: item.published_at))

    def get_financial_actuals(self, symbol: str, as_of_date: date) -> tuple[FinancialActual, ...]:
        actuals: dict[tuple[int, int | None, date], FinancialActual] = {}
        if self.opendart is not None:
            for item in self.opendart.get_financial_actuals(symbol, as_of_date):
                actuals[(item.fiscal_year, item.fiscal_quarter, item.period_end)] = item
        if self.fsc is not None:
            for item in self.fsc.get_financial_actuals(symbol, as_of_date):
                actuals.setdefault((item.fiscal_year, item.fiscal_quarter, item.period_end), item)
        return tuple(sorted(actuals.values(), key=lambda item: (item.period_end, item.reported_at)))

    def get_risk_records(self, symbol: str, as_of_date: date) -> tuple[KINDRiskRecord, ...]:
        if self.kind is None:
            return ()
        return self.kind.get_risk_records(symbol, as_of_date)

    def get_stock_issuance_records(self, symbol: str, as_of_date: date) -> tuple[dict[str, Any], ...]:
        if self.fsc is None:
            return ()
        return self.fsc.get_stock_issuance_records(symbol, as_of_date)


def _instrument_from_fsc(row: Mapping[str, Any]) -> Instrument:
    return Instrument(
        symbol=str(row.get("symbol") or row.get("srtnCd") or row.get("isinCd")),
        name=str(row.get("name") or row.get("itmsNm") or row.get("corpNm")),
        market=Market(str(row.get("market") or "KR")),
        exchange=str(row.get("exchange") or row.get("mrktCtg") or "KRX"),
        sector_exchange=str(row.get("sector_exchange")) if row.get("sector_exchange") else None,
        listed_date=date_value(row["listed_date"]) if row.get("listed_date") else None,
        currency=str(row.get("currency") or "KRW"),
    )


def _financial_actual(row: Mapping[str, Any]) -> FinancialActual:
    from e2r.sources.source_errors import datetime_value, float_or_none

    return FinancialActual(
        symbol=str(row["symbol"]),
        fiscal_year=int(float(row["fiscal_year"])),
        fiscal_quarter=int(float(row["fiscal_quarter"])) if row.get("fiscal_quarter") not in (None, "") else None,
        period_end=date_value(row["period_end"]),
        reported_at=datetime_value(row["reported_at"]),
        as_of_date=date_value(row.get("as_of_date") or row["reported_at"]),
        source=str(row.get("source") or "data.go.kr FSC"),
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


__all__ = ["DataGoKrFSCConnector", "KoreaCheapScanSources"]
