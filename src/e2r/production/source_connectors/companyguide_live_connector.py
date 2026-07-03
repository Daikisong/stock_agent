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
            consensus = _parse_companyguide_consensus(text, as_of_date=as_of_date)
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


def _parse_companyguide_consensus(text: str, *, as_of_date: date) -> dict[str, Any]:
    block = _companyguide_consensus_block(text)
    if not block:
        return {}
    row_values = _first_table_row_values(block)
    if len(row_values) < 5:
        return {}
    consensus_date = _companyguide_consensus_date(block) or as_of_date.strftime("%Y/%m/%d")
    payload: dict[str, Any] = {
        "CONSENSUS_AS_OF_DATE": consensus_date,
        "INVESTMENT_OPINION_SCORE": _number(row_values[0]),
        "TARGET_PRC": _number(row_values[1]),
        "EPS": _number(row_values[2]),
        "FORWARD_PER": _number(row_values[3]),
        "CONSENSUS_PROVIDER_COUNT": _number(row_values[4]),
        "score_anchor_text": block[:4000],
    }
    return {key: value for key, value in payload.items() if value not in (None, "")}


def _companyguide_consensus_block(text: str) -> str:
    marker = "투자의견 컨센서스"
    start = text.find(marker)
    if start < 0:
        return ""
    table_start = text.find("<table", start)
    table_end = text.find("</table>", table_start)
    if table_start < 0 or table_end < 0:
        return ""
    return text[start : table_end + len("</table>")]


def _companyguide_consensus_date(block: str) -> str | None:
    match = re.search(r"class=[\"']date[\"']>\s*\[(\d{4}/\d{2}/\d{2})\]", block)
    if match:
        return match.group(1)
    return None


def _first_table_row_values(block: str) -> tuple[str, ...]:
    row_match = re.search(r"<tbody[^>]*>.*?<tr[^>]*>(.*?)</tr>", block, flags=re.IGNORECASE | re.DOTALL)
    if not row_match:
        return ()
    cells = re.findall(r"<td[^>]*>(.*?)</td>", row_match.group(1), flags=re.IGNORECASE | re.DOTALL)
    return tuple(_strip_html(cell) for cell in cells)


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


__all__ = ["CompanyGuideLiveConnector"]
