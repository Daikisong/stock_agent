"""Regex-based broker research report parser.

The parser consumes already extracted PDF text or local ``.txt`` fixtures. It
does not download PDFs and it never fills fields that are not present in text or
metadata.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping

from e2r.models import Evidence, Market, ResearchReport, SourceTier
from e2r.sources.source_errors import date_value, float_or_none, market_value, text_or_none, tuple_value


@dataclass(frozen=True)
class ReportParseResult:
    """Parsed report object, evidence object, and normalized field map."""

    report: ResearchReport
    evidence: Evidence
    parsed_fields: Mapping[str, Any]


def parse_research_report_file(
    path: str | Path,
    *,
    symbol: str,
    market: Market = Market.KR,
    metadata: Mapping[str, Any] | None = None,
) -> ReportParseResult:
    text = Path(path).read_text(encoding="utf-8")
    return parse_research_report_text(symbol=symbol, market=market, text=text, metadata=metadata)


def parse_research_report_text(
    *,
    symbol: str,
    market: Market = Market.KR,
    text: str,
    metadata: Mapping[str, Any] | None = None,
) -> ReportParseResult:
    metadata = dict(metadata or {})
    report_date = _report_date(text, metadata)
    as_of_date = date_value(metadata.get("as_of_date") or report_date)
    broker = str(metadata.get("broker") or _line_value(text, ("증권사", "Broker", "발행처")) or "UnknownBroker")
    analyst = text_or_none(metadata.get("analyst") or _line_value(text, ("애널리스트", "Analyst")))
    title = str(metadata.get("title") or _line_value(text, ("제목", "Title")) or _first_heading(text) or "Research report")

    parsed = _extract_fields(text)
    for key in (
        "current_price",
        "target_price",
        "target_revision_pct",
        "upside_pct",
        "fifty_two_week_high",
        "fifty_two_week_low",
        "one_month_return",
        "three_month_return",
        "twelve_month_return",
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
        "roe",
        "opm",
        "backlog",
        "new_orders",
        "order_backlog_to_sales",
        "capa_increase_pct",
        "export_ratio",
        "us_revenue_ratio",
        "target_multiple_before",
        "target_multiple_after",
    ):
        if metadata.get(key) not in (None, ""):
            parsed.setdefault(key, float_or_none(metadata.get(key)))
    for key in ("asp_increase_mentioned", "lead_time_mentioned", "shortage_mentioned"):
        if metadata.get(key) not in (None, ""):
            parsed.setdefault(key, bool(metadata[key]))

    investment_points = tuple_value(metadata.get("investment_points")) or _points_after(text, ("투자포인트", "투자 포인트", "Investment points"))
    risk_points = tuple_value(metadata.get("risk_points")) or _points_after(text, ("리스크", "Risk"))
    parsed["parser_confidence"] = _confidence(parsed, text)

    report = ResearchReport(
        symbol=symbol,
        publish_date=report_date,
        broker=broker,
        title=title,
        as_of_date=as_of_date,
        analyst=analyst,
        current_price=parsed.get("current_price"),
        target_price=parsed.get("target_price"),
        rating=text_or_none(metadata.get("rating") or _line_value(text, ("투자의견", "Rating"))),
        target_revision_pct=parsed.get("target_revision_pct"),
        target_multiple_before=parsed.get("target_multiple_before"),
        target_multiple_after=parsed.get("target_multiple_after"),
        fy1_sales=parsed.get("fy1_sales"),
        fy1_op=parsed.get("fy1_op"),
        fy1_eps=parsed.get("fy1_eps"),
        fy2_sales=parsed.get("fy2_sales"),
        fy2_op=parsed.get("fy2_op"),
        fy2_eps=parsed.get("fy2_eps"),
        fy3_sales=parsed.get("fy3_sales"),
        fy3_op=parsed.get("fy3_op"),
        fy3_eps=parsed.get("fy3_eps"),
        est_per=parsed.get("est_per"),
        est_pbr=parsed.get("est_pbr"),
        upside_pct=parsed.get("upside_pct"),
        fifty_two_week_high=parsed.get("fifty_two_week_high"),
        fifty_two_week_low=parsed.get("fifty_two_week_low"),
        one_month_return=parsed.get("one_month_return"),
        three_month_return=parsed.get("three_month_return"),
        twelve_month_return=parsed.get("twelve_month_return"),
        roe=parsed.get("roe"),
        opm=parsed.get("opm"),
        backlog=parsed.get("backlog"),
        new_orders=parsed.get("new_orders"),
        order_backlog_to_sales=parsed.get("order_backlog_to_sales"),
        capa_increase_pct=parsed.get("capa_increase_pct"),
        export_ratio=parsed.get("export_ratio"),
        us_revenue_ratio=parsed.get("us_revenue_ratio"),
        asp_increase_mentioned=bool(parsed.get("asp_increase_mentioned")),
        lead_time_mentioned=bool(parsed.get("lead_time_mentioned")),
        shortage_mentioned=bool(parsed.get("shortage_mentioned")),
        investment_points=investment_points,
        risk_points=risk_points,
        raw_text=text,
        parsed_fields=parsed,
    )
    published_at = datetime(report_date.year, report_date.month, report_date.day, 8, 0)
    evidence = Evidence(
        evidence_id=f"research:{symbol}:{report_date.isoformat()}:{_stable_id(title)}",
        source_type="research_report",
        source_name=broker,
        source_tier=SourceTier.TIER_1,
        published_at=published_at,
        observed_at=published_at,
        available_at=published_at,
        as_of_date=as_of_date,
        market=market_value(metadata.get("market"), market),
        symbol=symbol,
        title=title,
        url_or_identifier=text_or_none(metadata.get("url")),
        excerpt_or_value=text[:240],
        parsed_fields=parsed,
        confidence=parsed["parser_confidence"],
    )
    return ReportParseResult(report=report, evidence=evidence, parsed_fields=parsed)


def _extract_fields(text: str) -> dict[str, Any]:
    fields: dict[str, Any] = {}
    aliases = {
        "current_price": ("현재가", "현재주가", "Current price"),
        "target_price": ("목표주가", "Target price"),
        "target_revision_pct": ("목표주가 상향", "Target revision"),
        "upside_pct": ("상승여력", "Upside"),
        "fifty_two_week_high": ("52주 최고", "52-week high"),
        "fifty_two_week_low": ("52주 최저", "52-week low"),
        "one_month_return": ("1개월 수익률", "1M return"),
        "three_month_return": ("3개월 수익률", "3M return"),
        "twelve_month_return": ("12개월 수익률", "12M return"),
        "est_per": ("PER", "Est PER"),
        "est_pbr": ("PBR", "Est PBR"),
        "roe": ("ROE",),
        "opm": ("OPM", "영업이익률"),
        "backlog": ("수주잔고", "Backlog"),
        "new_orders": ("신규수주", "New orders"),
        "order_backlog_to_sales": ("수주잔고/매출", "order backlog to sales"),
        "capa_increase_pct": ("CAPA 증가율", "CAPA 증설", "생산능력 증가"),
        "export_ratio": ("수출 비중", "Export ratio"),
        "us_revenue_ratio": ("미국향 매출 비중", "북미 매출 비중", "US revenue ratio"),
        "target_multiple_before": ("기존 멀티플", "target multiple before"),
        "target_multiple_after": ("상향 멀티플", "target multiple after"),
    }
    percent_fields = {
        "target_revision_pct",
        "upside_pct",
        "one_month_return",
        "three_month_return",
        "twelve_month_return",
        "roe",
        "opm",
        "order_backlog_to_sales",
        "capa_increase_pct",
        "export_ratio",
        "us_revenue_ratio",
    }
    for key, labels in aliases.items():
        value = _number_after(text, labels, percent=key in percent_fields)
        if value is not None:
            fields[key] = value

    for index, year_key in enumerate(("fy1", "fy2", "fy3"), start=1):
        year_match = re.search(
            rf"FY{index}|20[0-9]{{2}}E",
            text,
            re.IGNORECASE,
        )
        if not year_match and index > 1:
            continue
        for output, labels in (
            (f"{year_key}_sales", ("매출액", "Sales")),
            (f"{year_key}_op", ("영업이익", "OP")),
            (f"{year_key}_eps", ("EPS",)),
        ):
            value = _number_in_year_line(text, index, labels)
            if value is not None:
                fields[output] = value

    if "ASP" in text or "판가" in text:
        fields["asp_increase_mentioned"] = any(token in text for token in ("ASP 상승", "판가 상승", "가격 상승", "ASP 개선"))
    if "리드타임" in text or "lead time" in text.lower():
        fields["lead_time_mentioned"] = True
    if "공급부족" in text or "공급 부족" in text or "shortage" in text.lower():
        fields["shortage_mentioned"] = True
    return fields


def _report_date(text: str, metadata: Mapping[str, Any]) -> date:
    if metadata.get("report_date") or metadata.get("publish_date"):
        return date_value(metadata.get("report_date") or metadata.get("publish_date"))
    match = re.search(r"(20[0-9]{2})[.\-/년]\s*([0-9]{1,2})[.\-/월]\s*([0-9]{1,2})", text)
    if match:
        return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    return date.today()


def _line_value(text: str, labels: tuple[str, ...]) -> str | None:
    for label in labels:
        match = re.search(rf"{re.escape(label)}\s*[:：]?\s*(?P<value>[^\n]+)", text, re.IGNORECASE)
        if match:
            value = match.group("value").strip(" -\t")
            return value[:160] if value else None
    return None


def _first_heading(text: str) -> str | None:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and len(stripped) <= 120:
            return stripped.strip("# ")
    return None


def _number_after(text: str, labels: tuple[str, ...], *, percent: bool = False) -> float | None:
    for label in labels:
        pattern = rf"{re.escape(label)}[^0-9\-]*(?P<number>-?[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<unit>%|억원|억|원|배|x)?"
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            continue
        value = float(match.group("number").replace(",", ""))
        unit = match.group("unit")
        if unit in {"억원", "억"}:
            value *= 100_000_000.0
        return value if percent or unit != "%" else value
    return None


def _number_in_year_line(text: str, fy_index: int, labels: tuple[str, ...]) -> float | None:
    year_markers = (f"FY{fy_index}", f"FY{fy_index}E")
    lines = [line for line in text.splitlines() if any(marker in line.upper() for marker in year_markers)]
    if not lines:
        years = re.findall(r"20[0-9]{2}E[^\n]+", text)
        if len(years) >= fy_index:
            lines = [years[fy_index - 1]]
    for line in lines:
        for label in labels:
            match = re.search(rf"{re.escape(label)}[^0-9\-]*(?P<number>-?[0-9][0-9,]*(?:\.[0-9]+)?)", line, re.IGNORECASE)
            if match:
                return float(match.group("number").replace(",", ""))
    return None


def _points_after(text: str, labels: tuple[str, ...]) -> tuple[str, ...]:
    for label in labels:
        match = re.search(rf"{re.escape(label)}\s*[:：]\s*(?P<value>[^\n]+)", text, re.IGNORECASE)
        if match:
            return tuple(item.strip(" -\t") for item in re.split(r"[|;·]", match.group("value")) if item.strip())
    return ()


def _confidence(fields: Mapping[str, Any], text: str) -> float:
    numeric_count = sum(1 for value in fields.values() if isinstance(value, (int, float)))
    keyword_bonus = sum(1 for token in ("수주잔고", "CAPA", "ASP", "리드타임", "공급부족") if token in text) * 0.03
    return min(1.0, 0.35 + numeric_count * 0.035 + keyword_bonus)


def _stable_id(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]
