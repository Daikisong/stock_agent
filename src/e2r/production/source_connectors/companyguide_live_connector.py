"""CompanyGuide/FnGuide live connector for revision/report provider coverage."""

from __future__ import annotations

import hashlib
import html
import re
import time
from datetime import date, datetime
from functools import lru_cache
from typing import Any
from pathlib import Path

import requests

from .source_provider_registry import SourceFetchResult


_COMPANYGUIDE_URL = "https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp"


class CompanyGuideLiveConnector:
    provider_name = "CompanyGuide"
    source_class = "CompanyGuide"

    def __init__(self, *, repo_root: str | Path = ".") -> None:
        self.repo_root = Path(repo_root)

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str) -> SourceFetchResult:
        request_id = f"SRCREQ-COMPANYGUIDE-{symbol}-{as_of_date.isoformat()}"
        if mode != "live":
            return SourceFetchResult(
                provider_name=self.provider_name,
                source_class=self.source_class,
                mode=mode,
                request_id=request_id,
                request_params={"symbol": symbol, "company_name": company_name},
                status="NO_RESULT",
                fetched_at=_utc_now(),
                provider_request_id=request_id,
                provider_error="companyguide_connector_live_only_for_cutover_gate",
            )
        started = time.monotonic()
        params = {"pGB": "1", "gicode": f"A{symbol}"}
        try:
            text, content_hash, canonical_url = _fetch_companyguide_main(symbol)
            consensus = parse_companyguide_live_consensus_payload(
                text, as_of_date=as_of_date
            )
            consensus_date = _date_from_yyyy_slash(consensus.get("CONSENSUS_AS_OF_DATE")) if consensus else None
            score_usage = None
            if consensus and consensus_date and consensus_date > as_of_date:
                score_usage = "companyguide_consensus_after_as_of_date_not_score_evidence"
            elif not consensus:
                score_usage = "provider_coverage_only_until_numeric_revision_parser_accepts_claims"
            structured_payload = {
                "symbol": symbol,
                "company_name": company_name,
                "revision_report_provider_path": "FnGuide CompanyGuide company page",
                **consensus,
            }
            if score_usage:
                structured_payload["score_usage"] = score_usage
            return SourceFetchResult(
                provider_name=self.provider_name,
                source_class=self.source_class,
                mode="live",
                request_id=request_id,
                request_params={"symbol": symbol, "company_name": company_name, **params},
                status="FETCHED",
                canonical_url=canonical_url,
                official_document_id=f"companyguide:{symbol}",
                published_at=(consensus_date or as_of_date).isoformat(),
                available_at=(consensus_date or as_of_date).isoformat(),
                fetched_at=_utc_now(),
                content_hash=content_hash,
                raw_text=text[:200_000],
                structured_payload=structured_payload,
                provider_request_id=request_id,
                freshness_seconds=round(time.monotonic() - started, 4),
            )
        except Exception as exc:  # pragma: no cover - live provider variance
            return SourceFetchResult(
                provider_name=self.provider_name,
                source_class=self.source_class,
                mode="live",
                request_id=request_id,
                request_params={"symbol": symbol, "company_name": company_name, **params},
                status="PROVIDER_FAILED",
                fetched_at=_utc_now(),
                provider_request_id=request_id,
                provider_error=f"{type(exc).__name__}: {exc}",
                freshness_seconds=round(time.monotonic() - started, 4),
            )


def _utc_now() -> str:
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


def parse_companyguide_live_consensus_payload(
    text: str, *, as_of_date: date
) -> dict[str, Any]:
    block = _companyguide_consensus_block(text)
    if not block:
        return {}
    row_values = _first_table_row_values(block)
    if len(row_values) < 5:
        return {}
    explicit_consensus_date = _companyguide_consensus_date(
        block
    ) or _companyguide_page_date(text)
    consensus_date = explicit_consensus_date or as_of_date.strftime("%Y/%m/%d")
    payload: dict[str, Any] = {
        "CONSENSUS_AS_OF_DATE": consensus_date,
        "CONSENSUS_DATE_VERIFIED": explicit_consensus_date is not None,
        "COMPANY_NAME": _companyguide_company_name(text),
        "INVESTMENT_OPINION_SCORE": _number(row_values[0]),
        "TARGET_PRC": _number(row_values[1]),
        "EPS": _number(row_values[2]),
        "FORWARD_PER": _number(row_values[3]),
        "CONSENSUS_PROVIDER_COUNT": _number(row_values[4]),
        "score_anchor_text": block[:4000],
        **_parse_companyguide_forward_fundamentals(text),
        **_parse_companyguide_trailing_header(text),
    }
    return {key: value for key, value in payload.items() if value not in (None, "")}


def parse_companyguide_live_page_metadata(text: str) -> dict[str, Any]:
    """Parse page identity independently from the optional consensus row.

    CompanyGuide keeps the issuer title and page date even when the consensus
    table says that no recent analyst opinion exists.  Peer verification must
    therefore not report an identity failure merely because the numeric table
    is empty.  This helper exposes only identity/time metadata; it never
    manufactures a valuation value.
    """

    payload = {
        "COMPANY_NAME": _companyguide_company_name(text),
        "PAGE_AS_OF_DATE": _companyguide_page_date(text),
    }
    payload["PAGE_DATE_VERIFIED"] = payload["PAGE_AS_OF_DATE"] is not None
    return {
        key: value
        for key, value in payload.items()
        if value not in (None, "")
    }


# Compatibility alias for tests and older internal imports.
_parse_companyguide_consensus = parse_companyguide_live_consensus_payload


def _companyguide_consensus_block(text: str) -> str:
    table_match = re.search(
        r'<table\b(?=[^>]*\bid=["\']cTB15["\'])[^>]*>',
        text,
        flags=re.IGNORECASE,
    )
    if table_match is None:
        return ""
    table_start = table_match.start()
    table_end = text.find("</table>", table_start)
    if table_end < 0:
        return ""

    # The provider repeats this phrase in the page metadata.  Anchor the
    # section from the exact cTB15 table first, then search backwards only in
    # the nearby section.  This prevents an og:description/meta hit from
    # selecting an unrelated table near the top of the document.
    marker = "투자의견 컨센서스"
    nearby_start = max(0, table_start - 4_000)
    heading_start = text.rfind(marker, nearby_start, table_start)
    block_start = heading_start if heading_start >= 0 else table_start
    return text[block_start : table_end + len("</table>")]


def _companyguide_consensus_date(block: str) -> str | None:
    match = re.search(r"class=[\"']date[\"']>\s*\[(\d{4}/\d{2}/\d{2})\]", block)
    if match:
        return match.group(1)
    return _companyguide_page_date(block)


def _companyguide_page_date(text: str) -> str | None:
    match = re.search(
        r"\[\s*기준\s*:\s*([0-9]{4})[./-]([0-9]{2})[./-]([0-9]{2})\s*\]",
        html.unescape(text),
    )
    if not match:
        return None
    return f"{match.group(1)}/{match.group(2)}/{match.group(3)}"


def _companyguide_company_name(text: str) -> str | None:
    match = re.search(
        r"<title[^>]*>\s*(.*?)\s*-\s*기업(?:현황|정보)",
        html.unescape(text),
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not match:
        return None
    value = _strip_html(match.group(1))
    return value or None


def _first_table_row_values(block: str) -> tuple[str, ...]:
    for row_html in re.findall(
        r"<tr[^>]*>(.*?)</tr>", block, flags=re.IGNORECASE | re.DOTALL
    ):
        cells = re.findall(
            r"<td[^>]*>(.*?)</td>",
            row_html,
            flags=re.IGNORECASE | re.DOTALL,
        )
        if len(cells) >= 5:
            return tuple(_strip_html(cell) for cell in cells)
    return ()


def _parse_companyguide_trailing_header(text: str) -> dict[str, Any]:
    """Parse provider-published trailing values without relabeling as forward.

    CompanyGuide exposes these values in the company header and documents PER
    and PBR as previous-close divided by the latest fiscal EPS/BPS.  Keep that
    namespace separate from both the consensus table and the Fwd. 12M table.
    """

    definitions = {
        "EPS": "TRAILING_EPS",
        "BPS": "TRAILING_BPS",
        "PER": "TRAILING_PER",
        "PBR": "TRAILING_PBR",
    }
    parsed: dict[str, Any] = {}
    anchors: dict[str, str] = {}
    for label, key in definitions.items():
        match = re.search(
            rf"<p[^>]*>\s*{label}\s*<b[^>]*>(?P<value>.*?)</b>\s*</p>",
            text,
            flags=re.IGNORECASE | re.DOTALL,
        )
        if match is None:
            continue
        value_text = _strip_html(match.group("value"))
        value = _number(value_text)
        if value is None:
            continue
        parsed[key] = value
        anchors[key] = f"{label} {value_text}"
    close_match = re.search(
        r"<p[^>]*>\s*전일종가\s*<b[^>]*>(?P<value>.*?)</b>\s*</p>",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if close_match is not None:
        value_text = _strip_html(close_match.group("value"))
        value = _number(value_text)
        if value is not None:
            parsed["PROVIDER_PREVIOUS_CLOSE"] = value
            anchors["PROVIDER_PREVIOUS_CLOSE"] = f"전일종가 {value_text}"
    if not parsed:
        return {}
    page_date = _companyguide_page_date(text)
    if page_date is not None:
        parsed["TRAILING_VALUATION_AS_OF_DATE"] = page_date
        parsed["TRAILING_VALUATION_DATE_VERIFIED"] = True
    parsed["TRAILING_VALUATION_STRUCTURED"] = True
    parsed["TRAILING_VALUATION_FIELD_ANCHORS"] = anchors
    return parsed


def _parse_companyguide_forward_fundamentals(text: str) -> dict[str, Any]:
    """Parse the dated Fwd. 12M column from CompanyGuide fundamentals.

    This is deliberately limited to the structured fundamentals table.  It
    does not infer values from narrative text or reuse the trailing actual
    PER/PBR shown in the company header as forward valuation.
    """

    match = re.search(
        r'<table[^>]+summary=["\'][^"\']*기업\s*펀더멘털\s*실적[^"\']*["\'][^>]*>'
        r"(?P<body>.*?)</table>",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not match:
        return {}
    table = match.group(0)
    header_match = re.search(
        r"<thead[^>]*>(?P<header>.*?)</thead>",
        table,
        flags=re.IGNORECASE | re.DOTALL,
    )
    headers = (
        tuple(
            _strip_html(cell)
            for cell in re.findall(
                r"<th[^>]*>(.*?)</th>",
                header_match.group("header") if header_match else "",
                flags=re.IGNORECASE | re.DOTALL,
            )
        )
        if header_match
        else ()
    )
    forward_index = next(
        (
            index
            for index, value in enumerate(headers)
            if "Fwd" in value and "12M" in value
        ),
        None,
    )
    # Rows have one metric header followed by the dated actual, FY estimate,
    # and Fwd. 12M estimate.  If the provider removes that explicit header we
    # fail closed instead of silently treating another column as forward.
    if forward_index is None or forward_index <= 0:
        return {}
    metric_keys = {
        "PER": ("FORWARD_12M_PER", "MULTIPLE"),
        "PBR": ("FORWARD_12M_PBR", "MULTIPLE"),
        "EV/EBITDA": ("FORWARD_12M_EV_EBITDA", "MULTIPLE"),
        "EPS": ("FORWARD_12M_EPS", "PER_SHARE"),
        "BPS": ("FORWARD_12M_BPS", "PER_SHARE"),
        "EBITDA": ("FORWARD_12M_EBITDA", "TOTAL_CURRENCY"),
    }
    parsed: dict[str, Any] = {}
    for row_html in re.findall(
        r"<tr[^>]*>(.*?)</tr>", table, flags=re.IGNORECASE | re.DOTALL
    ):
        cells = tuple(
            _strip_html(cell)
            for cell in re.findall(
                r"<(?:th|td)[^>]*>(.*?)</(?:th|td)>",
                row_html,
                flags=re.IGNORECASE | re.DOTALL,
            )
        )
        if len(cells) <= forward_index:
            continue
        metric = cells[0].replace(" ", "").upper()
        definition = metric_keys.get(metric)
        if definition is None:
            continue
        key, value_kind = definition
        value = _fundamental_value(cells[forward_index], value_kind=value_kind)
        if value is not None:
            parsed[key] = value
    if parsed:
        parsed["FORWARD_FUNDAMENTALS_COLUMN"] = headers[forward_index]
        parsed["FORWARD_FUNDAMENTALS_STRUCTURED"] = True
    return parsed


def _fundamental_value(value: str, *, value_kind: str) -> float | int | None:
    parsed = _number(value)
    if parsed is None:
        return None
    if value_kind == "TOTAL_CURRENCY":
        normalized = value.replace(" ", "").lower()
        if "조원" in normalized or normalized.endswith("조"):
            parsed = float(parsed) * 1_000_000_000_000.0
        elif "억원" in normalized or normalized.endswith("억"):
            parsed = float(parsed) * 100_000_000.0
        elif "백만원" in normalized:
            parsed = float(parsed) * 1_000_000.0
        elif "만원" in normalized:
            parsed = float(parsed) * 10_000.0
    return int(parsed) if float(parsed).is_integer() else float(parsed)


def _strip_html(value: str) -> str:
    text = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def _number(value: str) -> float | int | None:
    clean = re.sub(r"[^0-9.+-]", "", str(value or ""))
    if not clean:
        return None
    try:
        parsed = float(clean)
    except ValueError:
        return None
    return int(parsed) if parsed.is_integer() else parsed


def _date_from_yyyy_slash(value: Any) -> date | None:
    if not value:
        return None
    try:
        return datetime.strptime(str(value), "%Y/%m/%d").date()
    except ValueError:
        return None


@lru_cache(maxsize=256)
def _fetch_companyguide_main(symbol: str) -> tuple[str, str, str]:
    params = {"pGB": "1", "gicode": f"A{symbol}"}
    response = requests.get(
        _COMPANYGUIDE_URL,
        params=params,
        headers={"User-Agent": "Mozilla/5.0 E2R-Cutover/3.0"},
        timeout=(3.05, 15),
    )
    response.raise_for_status()
    text = response.text
    if len(text.strip()) < 1000:
        raise RuntimeError("CompanyGuide response body too small to anchor provider fetch")
    return text, hashlib.sha256(response.content).hexdigest(), response.url


__all__ = [
    "CompanyGuideLiveConnector",
    "parse_companyguide_live_consensus_payload",
    "parse_companyguide_live_page_metadata",
]
