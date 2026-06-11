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
    parsed_fields = {
        "source": "company_guide_recent_report",
        "report_id": row.get("RPT_ID"),
        "idx": row.get("IDX"),
        "file_name": text_or_none(row.get("FILE_NM")),
        "page_count": _safe_int(row.get("PAGE_CNT")),
        "close_price": _safe_float(row.get("CLOSE_PRC")),
        "comment": _strip_html(text_or_none(row.get("COMMENT")) or ""),
        "target_price_action": text_or_none(row.get("PRC_ACTION_TYP_NM")),
        "eps_action": text_or_none(row.get("EPS_ACTION_TYP_NM")),
        "recommend_action": text_or_none(row.get("RECOMM_ACTION_TYP_NM")),
    }
    return ResearchReport(
        symbol=symbol,
        publish_date=publish_date,
        broker=str(row.get("BRK_NM_SHORT_KOR") or row.get("BRK_NM_KOR") or "CompanyGuide"),
        title=str(row.get("RPT_TITLE") or "CompanyGuide report"),
        as_of_date=as_of_date,
        analyst=text_or_none(row.get("ANL_NM_KOR")),
        current_price=_safe_float(row.get("CLOSE_PRC")),
        target_price=_safe_float(row.get("TARGET_PRC")),
        rating=text_or_none(row.get("RECOMM")),
        fy1_eps=_safe_float(row.get("EPS")),
        raw_text=parsed_fields["comment"],
        parsed_fields={key: value for key, value in parsed_fields.items() if value not in (None, "")},
    )


def _snapshot_date(html_text: str, fallback: date) -> date:
    match = re.search(r"\[기준\s*:\s*([0-9]{4})[.-]([0-9]{2})[.-]([0-9]{2})\]", html.unescape(html_text))
    if not match:
        return fallback
    return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))


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
