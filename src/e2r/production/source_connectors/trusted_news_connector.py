"""Trusted-news fallback connector placeholder with explicit provider failure."""

from __future__ import annotations

from datetime import date, datetime
from pathlib import Path

from .source_provider_registry import SourceFetchResult


class TrustedNewsLiveConnector:
    provider_name = "TrustedNews"
    source_class = "TrustedNews"

    def __init__(self, *, repo_root: str | Path = ".") -> None:
        self.repo_root = Path(repo_root)

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str) -> SourceFetchResult:
        request_id = f"SRCREQ-TRUSTEDNEWS-{symbol}-{as_of_date.isoformat()}"
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=request_id,
            request_params={"symbol": symbol, "company_name": company_name},
            status="PROVIDER_FAILED" if mode == "live" else "NO_RESULT",
            fetched_at=datetime.utcnow().isoformat(timespec="seconds") + "Z",
            provider_error="trusted_news_provider_not_configured; general search is not a score source",
            provider_request_id=request_id,
        )


__all__ = ["TrustedNewsLiveConnector"]
