"""Naver Finance item-page consensus parser.

The connector builds request metadata and normalizes saved HTML payloads.  It
does not execute live web requests. Live collection must be wired by an
explicit caller that can enforce source licensing, caching, and rate limits.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass
from datetime import date
from typing import Any

from e2r.models import ConsensusSnapshot
from e2r.sources.source_errors import SourceRequest, float_or_none


NAVER_FINANCE_ITEM_MAIN_URL = "https://finance.naver.com/item/main.nhn"


@dataclass(frozen=True)
class NaverFinanceConnector:
    """Build Naver Finance request metadata and normalize fixture payloads."""

    fixture_mode: bool = True
    item_main_url: str = NAVER_FINANCE_ITEM_MAIN_URL

    def build_item_main_request(self, symbol: str, as_of_date: date) -> SourceRequest:
        return SourceRequest(
            method="GET",
            url=self.item_main_url,
            params={"code": symbol, "as_of_date": as_of_date.isoformat()},
            headers={"User-Agent": "Mozilla/5.0"},
            fixture_mode=self.fixture_mode,
        )

    @staticmethod
    def parse_item_main_html(html_text: str, *, symbol: str, as_of_date: date) -> ConsensusSnapshot:
        source_date = _item_main_date(html_text)
        if source_date > as_of_date:
            raise ValueError("Naver Finance item page date cannot be after as_of_date")
        table_html = _financial_analysis_table(html_text)
        rows = _table_rows(table_html)
        column_labels = _financial_table_columns(rows)
        annual_estimate_index = _annual_estimate_column_index(column_labels)
        row_values = _financial_metric_values(rows, annual_estimate_index)
        fiscal_year = _fiscal_year_from_column(column_labels[annual_estimate_index])
        target_price = _target_price(html_text)
        return ConsensusSnapshot(
            symbol=symbol,
            date=source_date,
            fiscal_year=fiscal_year,
            as_of_date=as_of_date,
            source="naver_finance_item_main",
            sales_e=row_values.get("sales_e"),
            op_e=row_values.get("op_e"),
            net_income_e=row_values.get("net_income_e"),
            eps_e=row_values.get("eps_e"),
            bps_e=row_values.get("bps_e"),
            roe_e=row_values.get("roe_e"),
            per_e=row_values.get("per_e"),
            pbr_e=row_values.get("pbr_e"),
            target_price=target_price,
            parsed_fields={
                "source": "naver_finance_item_main",
                "source_family": "naver_finance_fnguide_consensus_snapshot",
                "structured_consensus_source": True,
                "consensus_method": "recent_3_month_broker_average_from_financial_analysis_table",
                "financial_statement_unit": "KRW_100M",
                "selected_column": column_labels[annual_estimate_index],
                "source_page_date": source_date.isoformat(),
            },
        )


def _item_main_date(html_text: str) -> date:
    text = html.unescape(html_text)
    patterns = (
        r'<em\s+class=["\']date["\']>\s*([0-9]{4})[.]([0-9]{2})[.]([0-9]{2})',
        r"([0-9]{4})년\s*([0-9]{2})월\s*([0-9]{2})일\s*[0-9]{1,2}시\s*[0-9]{1,2}분\s*기준",
    )
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    raise ValueError("Naver Finance item page does not expose a parsable 기준 date")


def _financial_analysis_table(html_text: str) -> str:
    match = re.search(
        r'<table[^>]+summary=["\']기업실적분석[^"\']*["\'][^>]*>.*?</table>',
        html_text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if match:
        return match.group(0)
    match = re.search(
        r'<caption>\s*기업실적분석\s*테이블\s*</caption>.*?</table>',
        html_text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if match:
        start = html_text.rfind("<table", 0, match.start())
        if start >= 0:
            return html_text[start : match.end()]
    raise ValueError("Naver Finance 기업실적분석 table not found")


def _table_rows(table_html: str) -> tuple[tuple[str, ...], ...]:
    rows: list[tuple[str, ...]] = []
    for row_html in re.findall(r"<tr[^>]*>(.*?)</tr>", table_html, flags=re.IGNORECASE | re.DOTALL):
        cells = tuple(
            _strip_html(cell_html)
            for _, cell_html in re.findall(
                r"<(th|td)[^>]*>(.*?)</\1>",
                row_html,
                flags=re.IGNORECASE | re.DOTALL,
            )
        )
        if any(cells):
            rows.append(cells)
    return tuple(rows)


def _strip_html(value: str) -> str:
    text = re.sub(r"<[^>]+>", " ", value)
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def _financial_table_columns(rows: tuple[tuple[str, ...], ...]) -> tuple[str, ...]:
    for row in rows:
        labels = tuple(_normalize_column_label(cell) for cell in row)
        date_like = tuple(label for label in labels if re.match(r"20[0-9]{2}[.][0-9]{2}(?:\s*\(E\))?$", label))
        if len(date_like) >= 2:
            return date_like
    raise ValueError("Naver Finance 기업실적분석 table has no date columns")


def _normalize_column_label(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("( E )", "(E)").replace("(E)", " (E)")).strip()


def _annual_estimate_column_index(column_labels: tuple[str, ...]) -> int:
    for index, label in enumerate(column_labels):
        if label.endswith("(E)") and ".12" in label:
            return index
    raise ValueError("Naver Finance 기업실적분석 table has no annual estimate column")


def _fiscal_year_from_column(label: str) -> int:
    match = re.match(r"(20[0-9]{2})[.][0-9]{2}", label)
    if not match:
        raise ValueError("Naver Finance annual estimate column has no fiscal year")
    return int(match.group(1))


def _financial_metric_values(rows: tuple[tuple[str, ...], ...], column_index: int) -> dict[str, float]:
    mapping = {
        "매출액": "sales_e",
        "영업이익": "op_e",
        "당기순이익": "net_income_e",
        "EPS(원)": "eps_e",
        "BPS(원)": "bps_e",
        "ROE(지배주주)": "roe_e",
        "PER(배)": "per_e",
        "PBR(배)": "pbr_e",
    }
    values: dict[str, float] = {}
    for row in rows:
        if len(row) < column_index + 2:
            continue
        metric_key = mapping.get(row[0])
        if metric_key is None:
            continue
        value = _safe_float(row[column_index + 1])
        if value is not None:
            values[metric_key] = value
    if not any(key in values for key in ("op_e", "eps_e", "sales_e")):
        raise ValueError("Naver Finance 기업실적분석 table has no parsable estimate values")
    return values


def _target_price(html_text: str) -> float | None:
    table_match = re.search(
        r'<table[^>]+summary=["\']투자의견 정보["\'][^>]*>.*?</table>',
        html_text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not table_match:
        return None
    values = tuple(_safe_float(cell) for cell in re.findall(r"<em[^>]*>(.*?)</em>", table_match.group(0), re.DOTALL))
    numeric_values = tuple(value for value in values if value is not None)
    if len(numeric_values) < 2:
        return None
    return numeric_values[1]


def _safe_float(value: Any) -> float | None:
    try:
        return float_or_none(value)
    except (TypeError, ValueError):
        return None
