"""CompanyGuide/WiseReport fixture-first parser.

The connector builds request metadata and normalizes saved HTML/JSON payloads.
It does not execute live web requests. Live collection must be wired by an
explicit caller that can enforce source licensing, caching, and rate limits.
"""

from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass
from datetime import date
from html.parser import HTMLParser
from typing import Any, Mapping, Sequence

from e2r.models import ConsensusSnapshot, ResearchReport
from e2r.sources.source_errors import SourceRequest, float_or_none, int_or_none, text_or_none


COMPANY_GUIDE_SNAPSHOT_URL = "https://comp.wisereport.co.kr/company/c1010001.aspx"
COMPANY_GUIDE_RECENT_REPORTS_URL = "https://comp.wisereport.co.kr/company/ajax/c1080001_data.aspx"


@dataclass(frozen=True)
class BrokerTargetRow:
    """One broker target-price row from the CompanyGuide consensus page."""

    symbol: str
    date: date
    as_of_date: date
    broker: str
    target_price: float | None = None
    previous_target_price: float | None = None
    target_price_revision_pct: float | None = None
    rating: str | None = None
    previous_rating: str | None = None

    def __post_init__(self) -> None:
        if self.date > self.as_of_date:
            raise ValueError("broker target date cannot be after as_of_date")


@dataclass(frozen=True)
class CompanyGuideConsensusResult:
    """Normalized consensus snapshot plus broker-level target rows."""

    consensus: ConsensusSnapshot
    broker_targets: tuple[BrokerTargetRow, ...]


@dataclass(frozen=True)
class CompanyGuideConnector:
    """Build CompanyGuide request metadata and normalize fixture payloads."""

    fixture_mode: bool = True
    snapshot_url: str = COMPANY_GUIDE_SNAPSHOT_URL
    recent_reports_url: str = COMPANY_GUIDE_RECENT_REPORTS_URL

    def build_snapshot_request(self, symbol: str, as_of_date: date) -> SourceRequest:
        return SourceRequest(
            method="GET",
            url=self.snapshot_url,
            params={"cmp_cd": symbol, "cn": "", "as_of_date": as_of_date.isoformat()},
            fixture_mode=self.fixture_mode,
        )

    def build_recent_reports_request(self, symbol: str, as_of_date: date, *, per_page: int = 20, cur_page: int = 1) -> SourceRequest:
        return SourceRequest(
            method="GET",
            url=self.recent_reports_url,
            params={
                "cmp_cd": symbol,
                "perPage": per_page,
                "curPage": cur_page,
                "as_of_date": as_of_date.isoformat(),
            },
            fixture_mode=self.fixture_mode,
        )

    @staticmethod
    def parse_consensus_snapshot_html(
        html_text: str,
        *,
        symbol: str,
        as_of_date: date,
        fiscal_year: int | None = None,
    ) -> CompanyGuideConsensusResult:
        tables = _parse_html_tables(html_text)
        source_date = _snapshot_date(html_text, as_of_date)
        consensus = _parse_consensus_table(
            tables.get("cTB15", ()),
            symbol=symbol,
            source_date=source_date,
            as_of_date=as_of_date,
            fiscal_year=fiscal_year or as_of_date.year,
        )
        broker_targets = _parse_broker_target_table(
            tables.get("cTB24", ()),
            symbol=symbol,
            as_of_date=as_of_date,
        )
        return CompanyGuideConsensusResult(consensus=consensus, broker_targets=broker_targets)

    @staticmethod
    def parse_broker_targets_html(html_text: str, *, symbol: str, as_of_date: date) -> tuple[BrokerTargetRow, ...]:
        tables = _parse_html_tables(html_text)
        return _parse_broker_target_table(
            tables.get("cTB24", ()),
            symbol=symbol,
            as_of_date=as_of_date,
        )

    @staticmethod
    def parse_recent_reports_payload(payload: str | Mapping[str, Any], *, symbol: str, as_of_date: date) -> tuple[ResearchReport, ...]:
        data = json.loads(payload) if isinstance(payload, str) else dict(payload)
        rows = data.get("lists") or ()
        reports: list[ResearchReport] = []
        for row in rows:
            if not isinstance(row, Mapping):
                continue
            report = _research_report_from_row(row, symbol=symbol, as_of_date=as_of_date)
            if report is not None:
                reports.append(report)
        return tuple(reports)


def _parse_consensus_table(
    rows: Sequence[Sequence[str]],
    *,
    symbol: str,
    source_date: date,
    as_of_date: date,
    fiscal_year: int,
) -> ConsensusSnapshot:
    for row in rows:
        values = tuple(cell for cell in row if cell)
        if len(values) < 5:
            continue
        opinion = _safe_float(values[0])
        target_price = _safe_float(values[1])
        eps = _safe_float(values[2])
        per = _safe_float(values[3])
        analyst_count = _safe_int(values[4])
        if opinion is None or target_price is None or analyst_count is None:
            continue
        return ConsensusSnapshot(
            symbol=symbol,
            date=source_date,
            fiscal_year=fiscal_year,
            as_of_date=as_of_date,
            source="company_guide_snapshot",
            eps_e=eps,
            per_e=per,
            analyst_count=analyst_count,
            target_price=target_price,
        )
    raise ValueError("CompanyGuide consensus table cTB15 does not contain a parsable value row")


def _safe_float(value: Any) -> float | None:
    try:
        return float_or_none(value)
    except (TypeError, ValueError):
        return None


def _safe_int(value: Any) -> int | None:
    try:
        return int_or_none(value)
    except (TypeError, ValueError):
        return None


def _parse_broker_target_table(rows: Sequence[Sequence[str]], *, symbol: str, as_of_date: date) -> tuple[BrokerTargetRow, ...]:
    targets: list[BrokerTargetRow] = []
    for row in rows:
        values = tuple(cell for cell in row if cell)
        if len(values) < 7 or values[0] == "제공처":
            continue
        row_date = _yy_mm_dd_date(values[1], as_of_date)
        if row_date > as_of_date:
            continue
        targets.append(
            BrokerTargetRow(
                symbol=symbol,
                date=row_date,
                as_of_date=as_of_date,
                broker=values[0],
                target_price=_safe_float(values[2]),
                previous_target_price=_safe_float(values[3]),
                target_price_revision_pct=_safe_float(values[4]),
                rating=text_or_none(values[5]),
                previous_rating=text_or_none(values[6]),
            )
        )
    return tuple(targets)


def _research_report_from_row(row: Mapping[str, Any], *, symbol: str, as_of_date: date) -> ResearchReport | None:
    raw_date = text_or_none(row.get("ANL_DT"))
    if raw_date is None:
        return None
    publish_date = _yy_mm_dd_date(raw_date, as_of_date)
    if publish_date > as_of_date:
        return None
    target_price_action = text_or_none(row.get("PRC_ACTION_TYP_NM"))
    eps_action = text_or_none(row.get("EPS_ACTION_TYP_NM"))
    recommend_action = text_or_none(row.get("RECOMM_ACTION_TYP_NM"))
    target_price_direction = _action_direction(target_price_action)
    eps_direction = _action_direction(eps_action)
    broker = str(row.get("BRK_NM_SHORT_KOR") or row.get("BRK_NM_KOR") or "CompanyGuide")
    title = str(row.get("RPT_TITLE") or "CompanyGuide report")
    comment = _strip_html(text_or_none(row.get("COMMENT")) or "")
    parsed_fields = {
        "source": "company_guide_recent_report",
        "report_id": row.get("RPT_ID"),
        "idx": row.get("IDX"),
        "file_name": text_or_none(row.get("FILE_NM")),
        "page_count": _safe_int(row.get("PAGE_CNT")),
        "close_price": _safe_float(row.get("CLOSE_PRC")),
        "comment": comment,
        "target_price_action": target_price_action,
        "eps_action": eps_action,
        "recommend_action": recommend_action,
        "target_price_revision_direction": target_price_direction,
        "eps_revision_direction": eps_direction,
        "target_price_upgrade_mentioned": target_price_direction == "up",
        "target_price_downgrade_mentioned": target_price_direction == "down",
        "eps_revision_up_mentioned": eps_direction == "up",
        "eps_revision_down_mentioned": eps_direction == "down",
    }
    forward_fields = _recent_report_forward_fields(f"{title}\n{comment}")
    merged_fields = dict(forward_fields)
    merged_fields.update({key: value for key, value in parsed_fields.items() if value not in (None, "")})
    return ResearchReport(
        symbol=symbol,
        publish_date=publish_date,
        broker=broker,
        title=title,
        as_of_date=as_of_date,
        analyst=text_or_none(row.get("ANL_NM_KOR")),
        current_price=_safe_float(row.get("CLOSE_PRC")),
        target_price=_safe_float(row.get("TARGET_PRC")),
        rating=text_or_none(row.get("RECOMM")),
        fy1_eps=_safe_float(row.get("EPS")),
        fy1_sales=forward_fields.get("fy1_sales"),
        fy1_op=forward_fields.get("fy1_op"),
        raw_text=comment,
        parsed_fields={key: value for key, value in merged_fields.items() if value not in (None, "")},
    )


def _snapshot_date(html_text: str, fallback: date) -> date:
    match = re.search(r"\[기준\s*:\s*([0-9]{4})[.-]([0-9]{2})[.-]([0-9]{2})\]", html.unescape(html_text))
    if not match:
        return fallback
    return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))


def _action_direction(value: str | None) -> str | None:
    text = (value or "").strip()
    if not text:
        return None
    if any(token in text for token in ("상향", "인상", "올림", "증가", "raise", "up")):
        return "up"
    if any(token in text for token in ("하향", "인하", "내림", "감소", "lower", "down")):
        return "down"
    if any(token in text for token in ("변동없음", "유지", "없음", "unchanged", "maintain")):
        return "unchanged"
    return None


def _recent_report_forward_fields(text: str) -> dict[str, Any]:
    fields: dict[str, Any] = {}
    lowered = text.lower()
    if not any(
        token in lowered
        for token in (
            "예상",
            "전망",
            "전망치",
            "추정",
            "추정치",
            "가이던스",
            "forecast",
            "estimate",
            "expected",
            "guidance",
        )
    ):
        return fields
    op = _forward_money_after(text, ("영업이익", "영업익", "OP", "operating profit"))
    if op is not None:
        fields["fy1_op"] = op
        fields["forward_op_estimate"] = op
        fields["forward_estimate_present"] = True
    sales = _forward_money_after(text, ("매출액", "매출", "Sales", "Revenue"))
    if sales is not None:
        fields["fy1_sales"] = sales
        fields["forward_sales_estimate"] = sales
        fields["forward_estimate_present"] = True
    if _estimate_upgrade_mentioned(text):
        fields["estimate_upgrade_mentioned"] = True
    return fields


def _forward_money_after(text: str, labels: tuple[str, ...]) -> float | None:
    for label in labels:
        label_pattern = re.escape(label)
        patterns = (
            rf"(?P<label>{label_pattern})[^\n]{{0,48}}?(?P<number>-?[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<unit>조원|조|억원|억|백만원|만원|원|trillion|billion|million)\s*(?:으로|로)?[^\n]{{0,96}}?(?:예상|전망|전망치|추정|추정치|가이던스|상향|forecast|estimate|expected|guidance|raised)",
            rf"(?:예상|전망|전망치|추정|추정치|가이던스|상향|forecast|estimate|expected|guidance|raised)[^\n]{{0,48}}?(?P<label>{label_pattern})[^\n]{{0,48}}?(?P<number>-?[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<unit>조원|조|억원|억|백만원|만원|원|trillion|billion|million)",
            rf"(?:FY[1-3]|20[0-9]{{2}}E|[1-4]\s*Q\s*'?[0-9]{{2,4}}|Q\s*[1-4]\s*'?[0-9]{{2,4}})[^\n]{{0,80}}?(?P<label>{label_pattern})[^\n]{{0,48}}?(?P<number>-?[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<unit>조원|조|억원|억|백만원|만원|원|trillion|billion|million)",
        )
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if not match:
                continue
            if _estimate_number_crosses_target_price_label(text, match):
                continue
            value = _safe_float(match.group("number"))
            if value is None:
                continue
            return _scale_amount(value, match.group("unit"))
    return None


def _estimate_number_crosses_target_price_label(text: str, match: re.Match[str]) -> bool:
    context = text[match.start("label") : match.start("number")].lower()
    return any(token in context for token in ("목표주가", "목표가", "적정주가", "target price"))


def _scale_amount(value: float, unit: str | None) -> float:
    normalized = (unit or "").lower()
    if normalized in {"조원", "조", "trillion"}:
        return value * 1_000_000_000_000.0
    if normalized in {"억원", "억", "billion"}:
        return value * 100_000_000.0
    if normalized in {"백만원", "million"}:
        return value * 1_000_000.0
    if normalized == "만원":
        return value * 10_000.0
    return value


def _estimate_upgrade_mentioned(text: str) -> bool:
    lowered = text.lower()
    return (
        "실적 전망치 상향" in text
        or "실적 추정치 상향" in text
        or "영업이익 전망치 상향" in text
        or "영업이익 추정치 상향" in text
        or "eps 상향" in lowered
        or "estimate upgrade" in lowered
        or "estimate raised" in lowered
    )


def _yy_mm_dd_date(value: str, as_of_date: date) -> date:
    match = re.match(r"\s*([0-9]{2})/([0-9]{2})/([0-9]{2})\s*$", value)
    if not match:
        text = value.strip().replace(".", "-")
        return date.fromisoformat(text[:10])
    year = 2000 + int(match.group(1))
    return date(year, int(match.group(2)), int(match.group(3)))


def _parse_html_tables(html_text: str) -> dict[str, tuple[tuple[str, ...], ...]]:
    parser = _TableHTMLParser()
    parser.feed(html_text)
    return {table_id: tuple(tuple(cell for cell in row) for row in rows) for table_id, rows in parser.tables.items()}


def _strip_html(value: str) -> str:
    parser = _TextHTMLParser()
    parser.feed(value)
    return " ".join(" ".join(parser.parts).split())


class _TableHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tables: dict[str, list[list[str]]] = {}
        self._table_stack: list[str | None] = []
        self._current_row: list[str] | None = None
        self._current_cell: list[str] | None = None

    @property
    def _current_table_id(self) -> str | None:
        return self._table_stack[-1] if self._table_stack else None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {key: value or "" for key, value in attrs}
        if tag == "table":
            table_id = attr.get("id") or None
            self._table_stack.append(table_id)
            if table_id:
                self.tables.setdefault(table_id, [])
            return
        if not self._current_table_id:
            return
        if tag == "tr":
            self._current_row = []
        elif tag in {"td", "th"} and self._current_row is not None:
            self._current_cell = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"td", "th"} and self._current_cell is not None and self._current_row is not None:
            self._current_row.append(" ".join("".join(self._current_cell).split()))
            self._current_cell = None
            return
        if tag == "tr" and self._current_row is not None:
            table_id = self._current_table_id
            if table_id:
                self.tables.setdefault(table_id, []).append(self._current_row)
            self._current_row = None
            return
        if tag == "table" and self._table_stack:
            self._table_stack.pop()

    def handle_data(self, data: str) -> None:
        if self._current_cell is not None:
            self._current_cell.append(html.unescape(data))


class _TextHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(html.unescape(data))


__all__ = [
    "BrokerTargetRow",
    "COMPANY_GUIDE_RECENT_REPORTS_URL",
    "COMPANY_GUIDE_SNAPSHOT_URL",
    "CompanyGuideConnector",
    "CompanyGuideConsensusResult",
]
