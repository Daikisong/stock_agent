"""CompanyGuide/FnGuide live connector for revision/report provider coverage."""

from __future__ import annotations

import hashlib
import time
from datetime import date, datetime
from functools import lru_cache
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
            return SourceFetchResult(
                provider_name=self.provider_name,
                source_class=self.source_class,
                mode="live",
                request_id=request_id,
                request_params={"symbol": symbol, "company_name": company_name, **params},
                status="FETCHED",
                canonical_url=canonical_url,
                official_document_id=f"companyguide:{symbol}",
                published_at=as_of_date.isoformat(),
                available_at=as_of_date.isoformat(),
                fetched_at=_utc_now(),
                content_hash=content_hash,
                raw_text=text[:200_000],
                structured_payload={
                    "symbol": symbol,
                    "company_name": company_name,
                    "revision_report_provider_path": "FnGuide CompanyGuide company page",
                    "score_usage": "provider_coverage_only_until_numeric_revision_parser_accepts_claims",
                },
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
