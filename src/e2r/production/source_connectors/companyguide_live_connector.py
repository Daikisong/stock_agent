"""CompanyGuide live connector placeholder with explicit provider failure."""

from __future__ import annotations

from datetime import date, datetime
from pathlib import Path

from .source_provider_registry import SourceFetchResult


class CompanyGuideLiveConnector:
    provider_name = "CompanyGuide"
    source_class = "CompanyGuide"

    def __init__(self, *, repo_root: str | Path = ".") -> None:
        self.repo_root = Path(repo_root)

    def fetch(self, *, symbol: str, company_name: str, as_of_date: date, mode: str) -> SourceFetchResult:
        request_id = f"SRCREQ-COMPANYGUIDE-{symbol}-{as_of_date.isoformat()}"
        return SourceFetchResult(
            provider_name=self.provider_name,
            source_class=self.source_class,
            mode=mode,
            request_id=request_id,
            request_params={"symbol": symbol, "company_name": company_name},
            status="PROVIDER_FAILED" if mode == "live" else "NO_RESULT",
            fetched_at=datetime.utcnow().isoformat(timespec="seconds") + "Z",
            provider_error="companyguide_live_connector_requires_provider_contract; NOT_READY until implemented",
            provider_request_id=request_id,
        )


__all__ = ["CompanyGuideLiveConnector"]
