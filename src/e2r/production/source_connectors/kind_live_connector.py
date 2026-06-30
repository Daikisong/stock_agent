"""KIND live connector for official disclosure/risk provider coverage."""

from __future__ import annotations

import hashlib
import time
from datetime import date, datetime
from functools import lru_cache
from pathlib import Path

import requests

from .source_provider_registry import SourceFetchResult


_KIND_MAIN_URL = "https://kind.krx.co.kr/main.do"


class KINDLiveConnector:
    provider_name = "KIND"
    source_class = "KIND"

    def __init__(self, *, repo_root: str | Path = ".") -> None:
        self.repo_root = Path(repo_root)

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str) -> SourceFetchResult:
        request_id = f"SRCREQ-KIND-{symbol}-{as_of_date.isoformat()}"
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
                provider_error="kind_connector_live_only_for_cutover_gate",
            )
        started = time.monotonic()
        try:
            text, content_hash = _fetch_kind_main()
            return SourceFetchResult(
                provider_name=self.provider_name,
                source_class=self.source_class,
                mode="live",
                request_id=request_id,
                request_params={"symbol": symbol, "company_name": company_name, "risk_lookup_scope": "KIND_PORTAL"},
                status="FETCHED",
                canonical_url=_KIND_MAIN_URL,
                official_document_id="kind:main",
                published_at=as_of_date.isoformat(),
                available_at=as_of_date.isoformat(),
                fetched_at=_utc_now(),
                content_hash=content_hash,
                raw_text=text[:200_000],
                structured_payload={
                    "symbol": symbol,
                    "company_name": company_name,
                    "risk_provider_path": "KIND official disclosure portal",
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


@lru_cache(maxsize=1)
def _fetch_kind_main() -> tuple[str, str]:
    response = requests.get(
        _KIND_MAIN_URL,
        headers={"User-Agent": "Mozilla/5.0 E2R-Cutover/3.0"},
        timeout=(3.05, 10),
    )
    response.raise_for_status()
    text = response.text
    if len(text.strip()) < 500:
        raise RuntimeError("KIND response body too small to anchor provider fetch")
    return text, hashlib.sha256(response.content).hexdigest()


__all__ = ["KINDLiveConnector"]
