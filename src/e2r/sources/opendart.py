"""OpenDART disclosure connector and disclosure normalizer."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Sequence

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
    "계약 해지",
    "계약 취소",
    "계약 정정",
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
    "op_yoy_pct",
)

DISCLOSURE_SIGNAL_HIGH = "high_signal"
DISCLOSURE_SIGNAL_RISK = "risk_signal"
DISCLOSURE_SIGNAL_ROUTINE = "routine"
DISCLOSURE_SIGNAL_UNKNOWN = "unknown"


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

    def build_disclosure_detail_request(self, rcept_no: str, as_of_date: date) -> SourceRequest:
        params: dict[str, Any] = {
            "rcept_no": rcept_no,
            "as_of_date": as_of_date.isoformat(),
        }
        if self.api_key:
            params["crtfc_key"] = self.api_key
        return SourceRequest(
            method="GET",
            url=f"{self.base_url}/document.xml",
            params=params,
            fixture_mode=self.fixture_mode,
            credential_name="OPENDART_API_KEY",
        )

    def build_single_account_request(
        self,
        corp_code: str,
        fiscal_year: int,
        as_of_date: date,
        *,
        report_code: str = "11011",
        full_accounts: bool = False,
        fs_div: str = "CFS",
    ) -> SourceRequest:
        params: dict[str, Any] = {
            "corp_code": corp_code,
            "bsns_year": str(fiscal_year),
            "reprt_code": report_code,
            "as_of_date": as_of_date.isoformat(),
        }
        endpoint = "fnlttSinglAcnt.json"
        if full_accounts:
            endpoint = "fnlttSinglAcntAll.json"
            params["fs_div"] = fs_div
        if self.api_key:
            params["crtfc_key"] = self.api_key
        return SourceRequest(
            method="GET",
            url=f"{self.base_url}/{endpoint}",
            params=params,
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
        parsed.setdefault("watch_type", _watch_type(title, report_type))
        parsed.setdefault("signal_class", classify_disclosure_signal(title, report_type, raw_text=raw_text, parsed_fields=parsed))
        parsed.setdefault("parser_confidence", _parser_confidence(parsed, raw_text))

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

    @staticmethod
    def normalize_single_account_actuals(
        payload: Mapping[str, Any],
        *,
        symbol: str,
        fiscal_year: int,
        as_of_date: date,
        reported_at: date,
        fiscal_quarter: int | None = None,
        period_end: date | None = None,
    ) -> tuple[FinancialActual, ...]:
        rows = payload.get("list") or payload.get("items") or payload.get("data") or ()
        if not isinstance(rows, (list, tuple)):
            return ()
        selected = _single_account_values(rows)
        if not selected:
            return ()
        operating_profit = selected.get("operating_profit")
        net_income = selected.get("net_income")
        sales = selected.get("sales")
        cfo = selected.get("cashflow_from_operations")
        capex = selected.get("capex")
        fcf = selected.get("fcf")
        if fcf is None and cfo is not None and capex is not None:
            fcf = cfo - abs(capex)
        opm = operating_profit / sales * 100.0 if sales is not None and sales > 0 and operating_profit is not None else None
        return (
            FinancialActual(
                symbol=symbol,
                fiscal_year=fiscal_year,
                fiscal_quarter=fiscal_quarter,
                period_end=period_end or date(fiscal_year, 12, 31),
                reported_at=datetime_value(reported_at),
                as_of_date=as_of_date,
                source="OpenDART single account",
                sales=sales,
                operating_profit=operating_profit,
                net_income=net_income,
                eps=selected.get("eps"),
                bps=selected.get("bps"),
                equity=selected.get("equity"),
                opm=opm,
                cashflow_from_operations=cfo,
                capex=capex,
                fcf=fcf,
            ),
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
    lowered = text.lower()
    if any(token in text for token in ("최소 매출 보장", "최소매출 보장", "최소 물량 보장", "최소 구매 보장")) or any(
        token in lowered for token in ("minimum revenue guarantee", "minimum sales guarantee", "minimum purchase commitment")
    ):
        parsed["minimum_revenue_guarantee"] = True
        parsed["minimum_sales_guarantee"] = True
        parsed["revenue_visibility_contract"] = True
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
    op_yoy = _percent_after(
        text,
        (
            "영업이익 전년동기대비",
            "영업이익 전년 동기 대비",
            "영업이익 YoY",
            "영업이익 증가율",
            "OP YoY",
            "operating profit yoy",
        ),
    )
    if op_yoy is not None:
        parsed["op_yoy_pct"] = op_yoy

    if "사상 최대 수주잔고" in text or ("수주잔고" in text and "사상 최대" in text):
        parsed["record_backlog"] = True
    if any(token in text for token in ("ASP 상승", "판가 상승", "가격 상승", "ASP 개선", "판가 개선")):
        parsed["pricing_power_confirmed"] = True
        parsed["pricing_power_mentioned"] = True
        parsed["asp_increase_mentioned"] = True
    if "리드타임" in text:
        parsed["lead_time_mentioned"] = True
    if "리드타임 장기화" in text and ("공급부족" in text or "공급 부족" in text):
        parsed["lead_time_extended"] = True
        parsed["capacity_constraint"] = True
        parsed["capa_shortage"] = True
    if "공급부족" in text or "공급 부족" in text:
        parsed["shortage_mentioned"] = True
        parsed["supply_shortage_mentioned"] = True
    if "구조적 공급부족" in text:
        parsed["shortage_type"] = "structural"
        parsed["structural_shortage_mentioned"] = True
    if any(token in text for token in ("수출 비중 확대", "수출 확대", "수출 증가", "해외 매출 확대")):
        parsed["export_channel_expansion"] = True
        parsed["export_growth_mentioned"] = True
    if any(token in text for token in ("해외 채널 확대", "해외 채널 확장", "북미 채널", "미국 채널")):
        parsed["overseas_channel_expansion"] = True
        parsed["channel_expansion"] = True
    if "hbm" in text.lower() and any(token in text for token in ("수요 증가", "수요 확대", "수요 강세")):
        parsed["hbm_demand_mentioned"] = True
    if any(token in text for token in ("메모리 가격 상승", "DRAM 가격 상승", "D램 가격 상승", "NAND 가격 상승", "낸드 가격 상승")):
        parsed["memory_price_increase_mentioned"] = True
    if any(token in text for token in ("공급조절", "감산")) or "supply discipline" in text.lower():
        parsed["supply_discipline_mentioned"] = True
    if any(token in text for token in ("장기계약", "장기 공급계약", "장기공급계약", "다년 계약")) or any(token in lowered for token in ("multi-year", "lta", "long-term agreement")):
        parsed["multi_year_contract"] = True
    if any(token in text for token in ("정부 고객", "정부향", "폴란드", "방산")):
        parsed["government_customer"] = True

    if any(token in title for token in ("거래정지", "상장폐지", "관리종목")):
        parsed["listing_risk"] = True
    return parsed


def normalize_disclosure_detail(
    base_event: DisclosureEvent,
    raw_document: str,
    *,
    as_of_date: date,
) -> DisclosureEvent:
    """Create higher-quality detail evidence from an OpenDART document body.

    The detail parser only lifts confidence when explicit fields are present.
    It never fills missing values from the list headline alone.
    """

    text = extract_document_text(raw_document)
    parsed = dict(base_event.parsed_fields)
    detail_fields = parse_disclosure_text(text, title=base_event.title)
    parsed.update(detail_fields)
    parsed["detail_fetched"] = True
    parsed["raw_document_format"] = "xml" if raw_document.lstrip().startswith("<") else "text"
    parsed["signal_class"] = classify_disclosure_signal(base_event.title, base_event.report_type, raw_text=text, parsed_fields=parsed)
    parsed["parser_confidence"] = _detail_parser_confidence(parsed)
    raw_text = text[:20_000] if text else None
    return DisclosureEvent(
        symbol=base_event.symbol,
        source="OpenDART detail",
        report_type=base_event.report_type,
        title=base_event.title,
        published_at=base_event.published_at,
        observed_at=base_event.observed_at,
        available_at=base_event.available_at,
        as_of_date=as_of_date,
        rcept_no=base_event.rcept_no,
        raw_text=raw_text,
        parsed_fields=parsed,
    )


def extract_document_text(raw_document: str) -> str:
    """Extract readable text from OpenDART document XML or plain text."""

    text = raw_document.strip()
    if not text:
        return ""
    if text.lstrip().startswith("<"):
        try:
            root = ET.fromstring(text)
            parts = [part.strip() for part in root.itertext() if part and part.strip()]
            return "\n".join(parts)
        except ET.ParseError:
            return re.sub(r"<[^>]+>", "\n", text)
    return text


def classify_disclosure_signal(
    title: str,
    report_type: str = "",
    *,
    raw_text: str | None = None,
    parsed_fields: Mapping[str, Any] | None = None,
) -> str:
    """Classify a disclosure headline/body for Layer-1 routing."""

    fields = parsed_fields or {}
    haystack = f"{title} {report_type} {raw_text or ''}"
    if any(token in haystack for token in ("유상증자", "전환사채", "신주인수권부사채", "감사의견", "거래정지", "상장폐지", "관리종목", "소송", "계약 해지", "계약 취소", "계약 지연")):
        return DISCLOSURE_SIGNAL_RISK
    if any(
        token in haystack
        for token in (
            "단일판매",
            "공급계약",
            "장기공급",
            "신규시설투자",
            "잠정실적",
            "영업실적 전망",
            "영업(잠정)실적",
            "수주잔고",
            "CAPA",
            "생산능력",
        )
    ):
        return DISCLOSURE_SIGNAL_HIGH
    if any(
        key in fields
        for key in (
            "contract_amount",
            "contract_amount_to_prior_sales",
            "facility_investment_amount",
            "capa_increase_pct",
            "op_yoy_pct",
        )
    ):
        return DISCLOSURE_SIGNAL_HIGH
    if any(
        token in haystack
        for token in (
            "투자설명서",
            "일괄신고",
            "증권발행실적보고서",
            "효력발생안내",
            "임원ㆍ주요주주",
            "임원·주요주주",
            "주식등의대량보유",
            "분기보고서",
            "반기보고서",
            "사업보고서",
            "주주총회",
            "주주명부",
            "기업설명회",
            "의결권대리",
        )
    ):
        return DISCLOSURE_SIGNAL_ROUTINE
    return DISCLOSURE_SIGNAL_UNKNOWN


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


def _detail_parser_confidence(parsed: Mapping[str, Any]) -> float:
    explicit_fields = sum(1 for key in DISCLOSURE_PARSED_FIELDS if key in parsed and parsed.get(key) not in (None, ""))
    if explicit_fields <= 0:
        return 0.45
    return min(1.0, 0.55 + explicit_fields * 0.06)


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


def _single_account_values(rows: Sequence[Mapping[str, Any]]) -> dict[str, float]:
    values: dict[str, tuple[int, float]] = {}
    capex_by_priority: dict[int, float] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        key = _single_account_component(row)
        if key is None:
            continue
        amount = _single_account_amount(row)
        if amount is None:
            continue
        priority = _single_account_priority(row)
        if key == "capex":
            capex_by_priority[priority] = capex_by_priority.get(priority, 0.0) + abs(amount)
            continue
        existing = values.get(key)
        if existing is None or priority > existing[0]:
            values[key] = (priority, amount)
    result = {key: amount for key, (_, amount) in values.items()}
    if capex_by_priority:
        best_priority = max(capex_by_priority)
        result["capex"] = capex_by_priority[best_priority]
    return result


def _single_account_component(row: Mapping[str, Any]) -> str | None:
    account_name = str(row.get("account_nm") or row.get("account_name") or "").replace(" ", "")
    statement = str(row.get("sj_div") or row.get("statement") or "")
    if account_name in {"매출액", "수익(매출액)", "영업수익"}:
        return "sales"
    if account_name.startswith("영업이익"):
        return "operating_profit"
    if account_name in {"당기순이익", "당기순이익(손실)", "연결당기순이익", "분기순이익", "반기순이익"}:
        return "net_income"
    if "기본주당" in account_name and "이익" in account_name:
        return "eps"
    if account_name in {"주당순자산", "BPS"}:
        return "bps"
    if statement == "BS" and account_name in {"자본총계", "자본"}:
        return "equity"
    if statement == "CF" and account_name in {
        "영업활동현금흐름",
        "영업활동으로인한현금흐름",
        "영업활동으로부터의현금흐름",
        "영업활동순현금흐름",
        "영업활동으로인한순현금흐름",
    }:
        return "cashflow_from_operations"
    if "잉여현금흐름" in account_name or account_name.upper() == "FREECASHFLOW":
        return "fcf"
    if statement == "CF" and "취득" in account_name and any(token in account_name for token in ("유형자산", "무형자산")):
        return "capex"
    return None


def _single_account_priority(row: Mapping[str, Any]) -> int:
    priority = 0
    fs_div = str(row.get("fs_div") or "")
    fs_name = str(row.get("fs_nm") or "")
    if fs_div == "CFS" or "연결" in fs_name:
        priority += 10
    if str(row.get("sj_div") or "") in {"IS", "CIS", "BS", "CF"}:
        priority += 1
    return priority


def _single_account_amount(row: Mapping[str, Any]) -> float | None:
    for key in ("thstrm_amount", "amount", "current_amount"):
        value = row.get(key)
        parsed = _amount_float(value)
        if parsed is not None:
            return parsed
    return None


def _amount_float(value: Any) -> float | None:
    text = str(value or "").strip().replace(",", "")
    if not text or text in {"-", "nan", "NaN"}:
        return None
    negative = text.startswith("(") and text.endswith(")")
    if negative:
        text = text[1:-1]
    try:
        parsed = float(text)
    except ValueError:
        return None
    return -parsed if negative else parsed


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
        equity=float_or_none(row.get("equity") or row.get("total_equity")),
        roe=float_or_none(row.get("roe")),
        opm=float_or_none(row.get("opm")),
        debt_ratio=float_or_none(row.get("debt_ratio")),
        cashflow_from_operations=float_or_none(row.get("cashflow_from_operations")),
        capex=float_or_none(row.get("capex")),
        fcf=float_or_none(row.get("fcf")),
        receivables=float_or_none(row.get("receivables")),
        inventory=float_or_none(row.get("inventory")),
    )
