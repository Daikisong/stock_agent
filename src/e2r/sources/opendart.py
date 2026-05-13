"""OpenDART disclosure connector and disclosure normalizer."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping

from e2r.models import DisclosureEvent, Evidence, FinancialActual, Market, SourceTier
from e2r.sources.source_errors import (
    SourceRequest,
    bool_value,
    coerce_jsonish,
    date_value,
    datetime_value,
    float_or_none,
    load_fixture_records,
    parsed_fields_from_record,
    require_credential,
    text_or_none,
)


OPENDART_BASE_URL = "https://opendart.fss.or.kr/api"

DISCLOSURE_WATCH_TYPES: tuple[str, ...] = (
    "단일판매·공급계약체결",
    "단일판매ㆍ공급계약체결",
    "신규시설투자",
    "잠정실적",
    "영업실적 전망",
    "사업보고서",
    "반기보고서",
    "분기보고서",
    "유상증자",
    "전환사채",
    "신주인수권부사채",
    "자기주식",
    "감사의견",
    "최대주주 변경",
    "소송",
    "거래정지",
)

DISCLOSURE_PARSED_FIELDS: tuple[str, ...] = (
    "contract_amount",
    "contract_amount_to_prior_sales",
    "contract_start",
    "contract_end",
    "contract_duration_months",
    "counterparty",
    "product_or_service",
    "region",
    "is_long_term",
    "is_cancellable",
    "prepayment_exists",
    "rpo_mentioned",
    "backlog_mentioned",
    "facility_investment_amount",
    "facility_investment_to_market_cap",
    "capa_increase_pct",
    "expected_completion_date",
    "dilution_type",
)


@dataclass(frozen=True)
class OpenDARTConnector:
    """OpenDART connector.

    Fixture mode is used by default. Live calls must be performed by external
    orchestration after obtaining ``SourceRequest`` objects and credentials.
    """

    api_key: str | None = None
    fixture_root: str | Path | None = "data/raw/opendart"
    fixture_mode: bool = True
    base_url: str = OPENDART_BASE_URL

    def build_disclosure_search_request(self, symbol: str, start: date, end: date, as_of_date: date) -> SourceRequest:
        params: dict[str, Any] = {
            "corp_code": symbol,
            "bgn_de": start.strftime("%Y%m%d"),
            "end_de": min(end, as_of_date).strftime("%Y%m%d"),
            "page_count": 100,
        }
        if self.api_key:
            params["crtfc_key"] = self.api_key
        return SourceRequest(
            method="GET",
            url=f"{self.base_url}/list.json",
            params=params,
            fixture_mode=self.fixture_mode,
            credential_name="OPENDART_API_KEY",
        )

    def build_company_code_request(self) -> SourceRequest:
        return SourceRequest(
            method="GET",
            url=f"{self.base_url}/corpCode.xml",
            params={"crtfc_key": self.api_key} if self.api_key else {},
            fixture_mode=self.fixture_mode,
            credential_name="OPENDART_API_KEY",
        )

    def require_live_credentials(self) -> str:
        return require_credential(self.api_key, "OPENDART_API_KEY")

    def get_disclosures(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[DisclosureEvent, ...]:
        disclosures = tuple(self.normalize_disclosure(row) for row in load_fixture_records(self.fixture_root, "disclosures"))
        return tuple(
            sorted(
                (
                    item
                    for item in disclosures
                    if item.symbol == symbol
                    and start <= item.published_at.date() <= end
                    and item.published_at.date() <= as_of_date
                    and item.available_at.date() <= as_of_date
                ),
                key=lambda item: item.published_at,
            )
        )

    def search_disclosures(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[DisclosureEvent, ...]:
        return self.get_disclosures(symbol, start, end, as_of_date)

    def get_financial_actuals(self, symbol: str, as_of_date: date) -> tuple[FinancialActual, ...]:
        actuals = tuple(_financial_actual(row) for row in load_fixture_records(self.fixture_root, "financial_actuals"))
        return tuple(
            sorted(
                (
                    item
                    for item in actuals
                    if item.symbol == symbol
                    and item.reported_at.date() <= as_of_date
                    and item.as_of_date <= as_of_date
                ),
                key=lambda item: (item.period_end, item.reported_at),
            )
        )

    @classmethod
    def normalize_disclosure(cls, row: Mapping[str, Any]) -> DisclosureEvent:
        published = datetime_value(
            row.get("published_at")
            or row.get("rcept_dt")
            or row.get("receipt_date")
            or row.get("date")
        )
        observed = datetime_value(row.get("observed_at") or published)
        available = datetime_value(row.get("available_at") or observed)
        raw_text = text_or_none(row.get("raw_text") or row.get("content") or row.get("body"))
        title = str(row.get("title") or row.get("report_nm") or row.get("report_name") or "")
        report_type = str(row.get("report_type") or row.get("report_nm") or row.get("category") or title or "disclosure")
        as_of = date_value(row.get("as_of_date") or available.date())

        known = {
            "symbol",
            "source",
            "report_type",
            "report_nm",
            "report_name",
            "category",
            "title",
            "published_at",
            "rcept_dt",
            "receipt_date",
            "date",
            "observed_at",
            "available_at",
            "as_of_date",
            "rcept_no",
            "raw_text",
            "content",
            "body",
            "parsed_fields",
        }
        parsed = parsed_fields_from_record(row, known)
        for key in DISCLOSURE_PARSED_FIELDS:
            if key in row and row[key] not in (None, ""):
                parsed[key] = _coerce_disclosure_value(key, row[key])
        if raw_text:
            for key, value in parse_disclosure_text(raw_text, title=title).items():
                parsed.setdefault(key, value)
        parsed.setdefault("parser_confidence", _parser_confidence(parsed, raw_text))
        parsed.setdefault("watch_type", _watch_type(title, report_type))

        return DisclosureEvent(
            symbol=str(row.get("symbol") or row.get("corp_code") or row.get("stock_code")),
            source=str(row.get("source") or "OpenDART"),
            report_type=report_type,
            title=title or report_type,
            published_at=published,
            observed_at=observed,
            available_at=available,
            as_of_date=as_of,
            rcept_no=text_or_none(row.get("rcept_no")),
            raw_text=raw_text,
            parsed_fields=parsed,
        )

    @staticmethod
    def to_evidence(event: DisclosureEvent, market: Market = Market.KR) -> Evidence:
        return Evidence(
            evidence_id=f"opendart:{event.symbol}:{event.rcept_no or event.published_at.date().isoformat()}:{event.report_type}",
            source_type="disclosure",
            source_name=event.source,
            source_tier=SourceTier.TIER_0,
            published_at=event.published_at,
            observed_at=event.observed_at,
            available_at=event.available_at,
            as_of_date=event.as_of_date,
            market=market,
            symbol=event.symbol,
            title=event.title,
            url_or_identifier=event.rcept_no,
            excerpt_or_value=event.raw_text[:240] if event.raw_text else None,
            parsed_fields=event.parsed_fields,
            confidence=float(event.parsed_fields.get("parser_confidence", 0.5)),
        )


def parse_disclosure_text(raw_text: str, *, title: str = "") -> dict[str, Any]:
    """Extract explicit disclosure fields without fabricating missing values."""

    text = raw_text.replace("\r\n", "\n")
    parsed: dict[str, Any] = {}

    contract_amount = _amount_after(text, ("계약금액", "계약 금액", "공급계약 금액", "contract amount"))
    if contract_amount is not None:
        parsed["contract_amount"] = contract_amount

    ratio = _percent_after(text, ("매출액 대비", "최근매출액 대비", "prior sales"))
    if ratio is not None:
        parsed["contract_amount_to_prior_sales"] = ratio / 100.0

    contract_dates = _contract_dates(text)
    if contract_dates is not None:
        start, end = contract_dates
        parsed["contract_start"] = start.isoformat()
        parsed["contract_end"] = end.isoformat()
        months = (end.year - start.year) * 12 + end.month - start.month
        if end.day >= start.day:
            months += 1
        parsed["contract_duration_months"] = max(0, months)

    for output_key, labels in (
        ("counterparty", ("계약상대방", "상대방", "counterparty")),
        ("product_or_service", ("계약내용", "주요제품", "공급제품", "product", "service")),
        ("region", ("공급지역", "지역", "region")),
    ):
        value = _line_value_after(text, labels)
        if value:
            parsed[output_key] = value

    if "장기" in text or parsed.get("contract_duration_months", 0) >= 24:
        parsed["is_long_term"] = True
    if any(token in text for token in ("해지 가능", "취소 가능", "계약 해지")):
        parsed["is_cancellable"] = True
    elif any(token in text for token in ("해지 불가", "취소 불가", "take-or-pay", "Take-or-pay")):
        parsed["is_cancellable"] = False
    if "선수금" in text or "선급금" in text or "prepayment" in text.lower():
        parsed["prepayment_exists"] = True
    if "RPO" in text or "remaining performance obligation" in text.lower():
        parsed["rpo_mentioned"] = True
    if "수주잔고" in text or "backlog" in text.lower():
        parsed["backlog_mentioned"] = True

    facility_amount = _amount_after(text, ("투자금액", "시설투자 금액", "facility investment"))
    if facility_amount is not None:
        parsed["facility_investment_amount"] = facility_amount
    facility_to_market_cap = _percent_after(text, ("시가총액 대비", "market cap"))
    if facility_to_market_cap is not None:
        parsed["facility_investment_to_market_cap"] = facility_to_market_cap / 100.0
    capa = _percent_after(text, ("CAPA", "생산능력", "capacity"))
    if capa is not None:
        parsed["capa_increase_pct"] = capa
    completion = _date_after(text, ("완공예정일", "준공예정일", "expected completion"))
    if completion is not None:
        parsed["expected_completion_date"] = completion.isoformat()

    dilution = _dilution_type(title + "\n" + text)
    if dilution:
        parsed["dilution_type"] = dilution

    if any(token in title for token in ("거래정지", "상장폐지", "관리종목")):
        parsed["listing_risk"] = True
    return parsed


def _coerce_disclosure_value(key: str, value: Any) -> Any:
    if key in {"is_long_term", "is_cancellable", "prepayment_exists", "rpo_mentioned", "backlog_mentioned"}:
        return bool_value(value)
    if key in {"contract_start", "contract_end", "expected_completion_date"}:
        return date_value(value).isoformat()
    if key in {
        "contract_amount",
        "contract_amount_to_prior_sales",
        "contract_duration_months",
        "facility_investment_amount",
        "facility_investment_to_market_cap",
        "capa_increase_pct",
    }:
        return float_or_none(value)
    return coerce_jsonish(value)


def _watch_type(title: str, report_type: str) -> str | None:
    haystack = f"{title} {report_type}"
    for item in DISCLOSURE_WATCH_TYPES:
        if item in haystack:
            return item
    return None


def _parser_confidence(parsed: Mapping[str, Any], raw_text: str | None) -> float:
    explicit_fields = sum(1 for key in DISCLOSURE_PARSED_FIELDS if key in parsed)
    if not raw_text:
        return min(1.0, 0.45 + explicit_fields * 0.04)
    return min(1.0, 0.35 + explicit_fields * 0.06)


def _amount_after(text: str, labels: tuple[str, ...]) -> float | None:
    for label in labels:
        match = re.search(
            rf"{re.escape(label)}[^0-9\-]*(?P<number>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<unit>억원|억|백만원|만원|원|USD|달러)?",
            text,
            re.IGNORECASE,
        )
        if match:
            return _scale_amount(float(match.group("number").replace(",", "")), match.group("unit"))
    return None


def _scale_amount(value: float, unit: str | None) -> float:
    if unit in {"억원", "억"}:
        return value * 100_000_000.0
    if unit == "백만원":
        return value * 1_000_000.0
    if unit == "만원":
        return value * 10_000.0
    return value


def _percent_after(text: str, labels: tuple[str, ...]) -> float | None:
    for label in labels:
        match = re.search(rf"{re.escape(label)}[^0-9\-]*(?P<number>-?[0-9]+(?:\.[0-9]+)?)\s*%", text, re.IGNORECASE)
        if match:
            return float(match.group("number"))
    return None


def _line_value_after(text: str, labels: tuple[str, ...]) -> str | None:
    for label in labels:
        match = re.search(rf"{re.escape(label)}\s*[:：]?\s*(?P<value>[^\n]+)", text, re.IGNORECASE)
        if match:
            value = match.group("value").strip(" -\t")
            return value[:120] if value else None
    return None


def _date_after(text: str, labels: tuple[str, ...]) -> date | None:
    for label in labels:
        match = re.search(rf"{re.escape(label)}[^0-9]*(?P<date>[0-9]{{4}}[.\-][0-9]{{1,2}}[.\-][0-9]{{1,2}})", text, re.IGNORECASE)
        if match:
            return date_value(match.group("date"))
    return None


def _contract_dates(text: str) -> tuple[date, date] | None:
    match = re.search(
        r"(?P<start>[0-9]{4}[.\-][0-9]{1,2}[.\-][0-9]{1,2})\s*(?:부터|~|--| - |까지|to)\s*(?P<end>[0-9]{4}[.\-][0-9]{1,2}[.\-][0-9]{1,2})",
        text,
        re.IGNORECASE,
    )
    if not match:
        return None
    return date_value(match.group("start")), date_value(match.group("end"))


def _dilution_type(text: str) -> str | None:
    if "유상증자" in text:
        return "rights_offering"
    if "전환사채" in text:
        return "convertible_bond"
    if "신주인수권부사채" in text:
        return "bond_with_warrant"
    return None


def _financial_actual(row: Mapping[str, Any]) -> FinancialActual:
    return FinancialActual(
        symbol=str(row["symbol"]),
        fiscal_year=int(float(row["fiscal_year"])),
        fiscal_quarter=int(float(row["fiscal_quarter"])) if row.get("fiscal_quarter") not in (None, "") else None,
        period_end=date_value(row["period_end"]),
        reported_at=datetime_value(row["reported_at"]),
        as_of_date=date_value(row.get("as_of_date") or row["reported_at"]),
        source=str(row.get("source") or "OpenDART"),
        sales=float_or_none(row.get("sales")),
        operating_profit=float_or_none(row.get("operating_profit")),
        net_income=float_or_none(row.get("net_income")),
        eps=float_or_none(row.get("eps")),
        bps=float_or_none(row.get("bps")),
        roe=float_or_none(row.get("roe")),
        opm=float_or_none(row.get("opm")),
        debt_ratio=float_or_none(row.get("debt_ratio")),
        cashflow_from_operations=float_or_none(row.get("cashflow_from_operations")),
        capex=float_or_none(row.get("capex")),
        fcf=float_or_none(row.get("fcf")),
        receivables=float_or_none(row.get("receivables")),
        inventory=float_or_none(row.get("inventory")),
    )
