"""Data connector interfaces and mock/fallback implementations."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

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
    SourceTier,
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


def _blank_to_none(value: Any) -> Any:
    if value == "":
        return None
    return value


def _text_or_none(value: Any) -> str | None:
    value = _blank_to_none(value)
    if value is None:
        return None
    return str(value)


def _float_or_none(value: Any) -> float | None:
    value = _blank_to_none(value)
    if value is None:
        return None
    return float(value)


def _int_or_none(value: Any) -> int | None:
    value = _blank_to_none(value)
    if value is None:
        return None
    return int(float(value))


def _bool_value(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None or value == "":
        return False
    if isinstance(value, (int, float)):
        return value != 0
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def _date_value(value: Any) -> date:
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    return date.fromisoformat(str(value))


def _datetime_value(value: Any) -> datetime:
    if isinstance(value, datetime):
        return value
    text = str(value)
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    return datetime.fromisoformat(text)


def _mapping_value(value: Any) -> dict[str, Any]:
    value = _blank_to_none(value)
    if value is None:
        return {}
    if isinstance(value, Mapping):
        return dict(value)
    parsed = json.loads(str(value))
    if not isinstance(parsed, dict):
        raise ValueError("parsed_fields must decode to a JSON object")
    return parsed


def _tuple_value(value: Any) -> tuple[str, ...]:
    value = _blank_to_none(value)
    if value is None:
        return ()
    if isinstance(value, (tuple, list)):
        return tuple(str(item) for item in value)
    text = str(value).strip()
    if not text:
        return ()
    if text.startswith("["):
        parsed = json.loads(text)
        return tuple(str(item) for item in parsed)
    return tuple(item.strip() for item in text.split("|") if item.strip())


def _records_from_path(path: Path) -> tuple[dict[str, Any], ...]:
    if path.suffix == ".csv":
        with path.open("r", encoding="utf-8", newline="") as handle:
            return tuple(dict(row) for row in csv.DictReader(handle))
    if path.suffix == ".json":
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        if not isinstance(payload, list):
            raise ValueError(f"{path} must contain a JSON array")
        return tuple(dict(row) for row in payload)
    raise ValueError(f"unsupported fixture file extension: {path}")


def _load_records(root: Path, stem: str) -> tuple[dict[str, Any], ...]:
    rows: list[dict[str, Any]] = []
    for suffix in (".csv", ".json"):
        path = root / f"{stem}{suffix}"
        if path.exists():
            rows.extend(_records_from_path(path))
    return tuple(rows)


def _parsed_fields_with_unknowns(record: Mapping[str, Any], known_keys: set[str]) -> dict[str, Any]:
    parsed = _mapping_value(record.get("parsed_fields"))
    for key, value in record.items():
        if key in known_keys or value in (None, ""):
            continue
        parsed[key] = _coerce_jsonish(value)
    return parsed


def _coerce_jsonish(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    text = value.strip()
    if not text:
        return None
    if text.lower() in {"true", "false"}:
        return text.lower() == "true"
    try:
        if "." in text:
            return float(text)
        return int(text)
    except ValueError:
        return text


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
                    if item.symbol == symbol
                    and item.reported_at.date() <= as_of_date
                    and item.as_of_date <= as_of_date
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
                    and item.as_of_date <= as_of_date
                ),
                key=lambda item: item.published_at,
            )
        )


@dataclass(frozen=True)
class CSVJSONDataConnector(MockDataConnector):
    """Load fallback research data from CSV and JSON files in one directory."""

    @classmethod
    def from_directory(cls, root: str | Path) -> "CSVJSONDataConnector":
        root_path = Path(root)
        if not root_path.exists():
            raise ValueError(f"fixture directory does not exist: {root_path}")
        return cls(
            instruments=tuple(cls._instrument(row) for row in _load_records(root_path, "instruments")),
            price_bars=tuple(cls._price_bar(row) for row in _load_records(root_path, "prices")),
            financial_actuals=tuple(cls._financial_actual(row) for row in _load_records(root_path, "financial_actuals")),
            consensus=tuple(cls._consensus(row) for row in _load_records(root_path, "consensus")),
            consensus_revisions=tuple(cls._consensus_revision(row) for row in _load_records(root_path, "consensus_revisions")),
            disclosures=tuple(cls._disclosure(row) for row in _load_records(root_path, "disclosures")),
            research_reports=tuple(cls._research_report(row) for row in _load_records(root_path, "research_reports")),
            news_items=tuple(cls._news_item(row) for row in _load_records(root_path, "news")),
        )

    @staticmethod
    def _instrument(row: Mapping[str, Any]) -> Instrument:
        return Instrument(
            symbol=str(row["symbol"]),
            name=str(row["name"]),
            market=Market(str(row["market"])),
            exchange=str(row["exchange"]),
            sector_exchange=_text_or_none(row.get("sector_exchange")),
            sector_custom=_text_or_none(row.get("sector_custom")),
            listed_date=_date_value(row["listed_date"]) if row.get("listed_date") else None,
            currency=str(row.get("currency") or "KRW"),
            is_preferred=_bool_value(row.get("is_preferred")),
            is_spac=_bool_value(row.get("is_spac")),
            is_reit=_bool_value(row.get("is_reit")),
            is_etf=_bool_value(row.get("is_etf")),
            is_managed=_bool_value(row.get("is_managed")),
            is_invest_warning=_bool_value(row.get("is_invest_warning")),
            is_trading_halt=_bool_value(row.get("is_trading_halt")),
        )

    @staticmethod
    def _price_bar(row: Mapping[str, Any]) -> PriceBar:
        return PriceBar(
            symbol=str(row["symbol"]),
            date=_date_value(row["date"]),
            open=float(row["open"]),
            high=float(row["high"]),
            low=float(row["low"]),
            close=float(row["close"]),
            adj_close=float(row.get("adj_close") or row["close"]),
            volume=int(float(row.get("volume") or 0)),
            trading_value=float(row.get("trading_value") or 0),
            market_cap=_float_or_none(row.get("market_cap")),
            source=str(row.get("source") or "file"),
            as_of_date=_date_value(row.get("as_of_date") or row["date"]),
        )

    @staticmethod
    def _financial_actual(row: Mapping[str, Any]) -> FinancialActual:
        return FinancialActual(
            symbol=str(row["symbol"]),
            fiscal_year=int(float(row["fiscal_year"])),
            fiscal_quarter=_int_or_none(row.get("fiscal_quarter")),
            period_end=_date_value(row["period_end"]),
            reported_at=_datetime_value(row["reported_at"]),
            as_of_date=_date_value(row["as_of_date"]),
            source=str(row.get("source") or "file"),
            sales=_float_or_none(row.get("sales")),
            operating_profit=_float_or_none(row.get("operating_profit")),
            net_income=_float_or_none(row.get("net_income")),
            eps=_float_or_none(row.get("eps")),
            bps=_float_or_none(row.get("bps")),
            roe=_float_or_none(row.get("roe")),
            opm=_float_or_none(row.get("opm")),
            debt_ratio=_float_or_none(row.get("debt_ratio")),
            cashflow_from_operations=_float_or_none(row.get("cashflow_from_operations")),
            capex=_float_or_none(row.get("capex")),
            fcf=_float_or_none(row.get("fcf")),
            receivables=_float_or_none(row.get("receivables")),
            inventory=_float_or_none(row.get("inventory")),
        )

    @staticmethod
    def _consensus(row: Mapping[str, Any]) -> ConsensusSnapshot:
        return ConsensusSnapshot(
            symbol=str(row["symbol"]),
            date=_date_value(row["date"]),
            fiscal_year=int(float(row["fiscal_year"])),
            as_of_date=_date_value(row["as_of_date"]),
            source=str(row.get("source") or "file"),
            sales_e=_float_or_none(row.get("sales_e")),
            op_e=_float_or_none(row.get("op_e")),
            net_income_e=_float_or_none(row.get("net_income_e")),
            eps_e=_float_or_none(row.get("eps_e")),
            fcf_e=_float_or_none(row.get("fcf_e")),
            bps_e=_float_or_none(row.get("bps_e")),
            roe_e=_float_or_none(row.get("roe_e")),
            per_e=_float_or_none(row.get("per_e")),
            pbr_e=_float_or_none(row.get("pbr_e")),
            analyst_count=_int_or_none(row.get("analyst_count")),
            target_price=_float_or_none(row.get("target_price")),
            target_multiple_type=_text_or_none(row.get("target_multiple_type")),
            target_multiple=_float_or_none(row.get("target_multiple")),
        )

    @staticmethod
    def _consensus_revision(row: Mapping[str, Any]) -> ConsensusRevision:
        return ConsensusRevision(
            symbol=str(row["symbol"]),
            date=_date_value(row["date"]),
            fiscal_year=int(float(row["fiscal_year"])),
            as_of_date=_date_value(row["as_of_date"]),
            eps_revision_1w=_float_or_none(row.get("eps_revision_1w")),
            eps_revision_1m=_float_or_none(row.get("eps_revision_1m")),
            eps_revision_3m=_float_or_none(row.get("eps_revision_3m")),
            op_revision_1w=_float_or_none(row.get("op_revision_1w")),
            op_revision_1m=_float_or_none(row.get("op_revision_1m")),
            op_revision_3m=_float_or_none(row.get("op_revision_3m")),
            fcf_revision_1m=_float_or_none(row.get("fcf_revision_1m")),
            target_price_revision_1m=_float_or_none(row.get("target_price_revision_1m")),
            analyst_count_change=_int_or_none(row.get("analyst_count_change")),
            street_high_eps_revision_1m=_float_or_none(row.get("street_high_eps_revision_1m")),
            street_low_eps_revision_1m=_float_or_none(row.get("street_low_eps_revision_1m")),
        )

    @staticmethod
    def _disclosure(row: Mapping[str, Any]) -> DisclosureEvent:
        known = {
            "symbol",
            "source",
            "report_type",
            "title",
            "published_at",
            "observed_at",
            "available_at",
            "as_of_date",
            "rcept_no",
            "raw_text",
            "parsed_fields",
        }
        return DisclosureEvent(
            symbol=str(row["symbol"]),
            source=str(row.get("source") or "file"),
            report_type=str(row["report_type"]),
            title=str(row["title"]),
            published_at=_datetime_value(row["published_at"]),
            observed_at=_datetime_value(row.get("observed_at") or row["published_at"]),
            available_at=_datetime_value(row.get("available_at") or row["published_at"]),
            as_of_date=_date_value(row["as_of_date"]),
            rcept_no=_text_or_none(row.get("rcept_no")),
            raw_text=_text_or_none(row.get("raw_text")),
            parsed_fields=_parsed_fields_with_unknowns(row, known),
        )

    @staticmethod
    def _research_report(row: Mapping[str, Any]) -> ResearchReport:
        known = {
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
        return ResearchReport(
            symbol=str(row["symbol"]),
            publish_date=_date_value(row["publish_date"]),
            broker=str(row["broker"]),
            title=str(row["title"]),
            as_of_date=_date_value(row["as_of_date"]),
            analyst=_text_or_none(row.get("analyst")),
            current_price=_float_or_none(row.get("current_price")),
            target_price=_float_or_none(row.get("target_price")),
            rating=_text_or_none(row.get("rating")),
            target_revision_pct=_float_or_none(row.get("target_revision_pct")),
            target_multiple_before=_float_or_none(row.get("target_multiple_before")),
            target_multiple_after=_float_or_none(row.get("target_multiple_after")),
            fy1_sales=_float_or_none(row.get("fy1_sales")),
            fy1_op=_float_or_none(row.get("fy1_op")),
            fy1_eps=_float_or_none(row.get("fy1_eps")),
            fy2_sales=_float_or_none(row.get("fy2_sales")),
            fy2_op=_float_or_none(row.get("fy2_op")),
            fy2_eps=_float_or_none(row.get("fy2_eps")),
            fy3_sales=_float_or_none(row.get("fy3_sales")),
            fy3_op=_float_or_none(row.get("fy3_op")),
            fy3_eps=_float_or_none(row.get("fy3_eps")),
            est_per=_float_or_none(row.get("est_per")),
            est_pbr=_float_or_none(row.get("est_pbr")),
            upside_pct=_float_or_none(row.get("upside_pct")),
            fifty_two_week_high=_float_or_none(row.get("fifty_two_week_high")),
            fifty_two_week_low=_float_or_none(row.get("fifty_two_week_low")),
            one_month_return=_float_or_none(row.get("one_month_return")),
            three_month_return=_float_or_none(row.get("three_month_return")),
            twelve_month_return=_float_or_none(row.get("twelve_month_return")),
            roe=_float_or_none(row.get("roe")),
            opm=_float_or_none(row.get("opm")),
            backlog=_float_or_none(row.get("backlog")),
            new_orders=_float_or_none(row.get("new_orders")),
            order_backlog_to_sales=_float_or_none(row.get("order_backlog_to_sales")),
            capa_increase_pct=_float_or_none(row.get("capa_increase_pct")),
            export_ratio=_float_or_none(row.get("export_ratio")),
            us_revenue_ratio=_float_or_none(row.get("us_revenue_ratio")),
            asp_increase_mentioned=_bool_value(row.get("asp_increase_mentioned")),
            lead_time_mentioned=_bool_value(row.get("lead_time_mentioned")),
            shortage_mentioned=_bool_value(row.get("shortage_mentioned")),
            investment_points=_tuple_value(row.get("investment_points")),
            risk_points=_tuple_value(row.get("risk_points")),
            raw_text=_text_or_none(row.get("raw_text")),
            parsed_fields=_parsed_fields_with_unknowns(row, known),
        )

    @staticmethod
    def _news_item(row: Mapping[str, Any]) -> NewsItem:
        known = {
            "symbol",
            "sector",
            "published_at",
            "source",
            "title",
            "as_of_date",
            "body",
            "source_tier",
            "theme_tags",
            "sentiment",
            "parsed_fields",
        }
        tier = row.get("source_tier")
        return NewsItem(
            symbol=_text_or_none(row.get("symbol")),
            sector=_text_or_none(row.get("sector")),
            published_at=_datetime_value(row["published_at"]),
            source=str(row.get("source") or "file"),
            title=str(row["title"]),
            as_of_date=_date_value(row["as_of_date"]),
            body=_text_or_none(row.get("body")),
            source_tier=SourceTier(int(float(tier))) if tier not in (None, "") else SourceTier.TIER_2,
            theme_tags=_tuple_value(row.get("theme_tags")),
            sentiment=_float_or_none(row.get("sentiment")),
            parsed_fields=_parsed_fields_with_unknowns(row, known),
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
