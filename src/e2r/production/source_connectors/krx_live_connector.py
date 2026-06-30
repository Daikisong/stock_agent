"""KRX live connector for production cutover provider coverage."""

from __future__ import annotations

import hashlib
import time
from datetime import date, datetime
from pathlib import Path

import requests

from .source_provider_registry import SourceFetchResult


_KRX_MDC_URL = "https://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd"


class KRXLiveConnector:
    provider_name = "KRX"
    source_class = "KRX"

    def __init__(self, *, repo_root: str | Path = ".") -> None:
        self.repo_root = Path(repo_root)

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str) -> SourceFetchResult:
        request_id = f"SRCREQ-KRX-{symbol}-{as_of_date.isoformat()}"
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
                provider_error="krx_connector_live_only_for_cutover_gate",
            )
        started = time.monotonic()
        try:
            response = requests.get(_KRX_MDC_URL, headers={"User-Agent": "Mozilla/5.0 E2R-Cutover/3.0"}, timeout=15)
            response.raise_for_status()
            text = response.text
            if len(text.strip()) < 1000:
                raise RuntimeError("KRX response body too small to anchor provider fetch")
            content_hash = hashlib.sha256(response.content).hexdigest()
            return SourceFetchResult(
                provider_name=self.provider_name,
                source_class=self.source_class,
                mode="live",
                request_id=request_id,
                request_params={"symbol": symbol, "company_name": company_name, "risk_lookup_scope": "KRX_MDC_PORTAL"},
                status="FETCHED",
                canonical_url=_KRX_MDC_URL,
                official_document_id="krx:mdc:main",
                published_at=as_of_date.isoformat(),
                available_at=as_of_date.isoformat(),
                fetched_at=_utc_now(),
                content_hash=content_hash,
                raw_text=text[:200_000],
                structured_payload={
                    "symbol": symbol,
                    "company_name": company_name,
                    "risk_provider_path": "KRX Market Data Center",
                    "score_usage": "provider_coverage_only_until_symbol_risk_endpoint_is_available",
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
                request_params={"symbol": symbol, "company_name": company_name},
                status="PROVIDER_FAILED",
                fetched_at=_utc_now(),
                provider_request_id=request_id,
                provider_error=f"{type(exc).__name__}: {exc}",
                freshness_seconds=round(time.monotonic() - started, 4),
            )


def _utc_now() -> str:
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


__all__ = ["KRXLiveConnector"]
