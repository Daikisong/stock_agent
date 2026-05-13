"""Naver Web/Doc report-search connector."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping

from e2r.sources.report_search import REPORT_QUERY_TEMPLATES, ReportSearchResult, is_recognized_report_domain
from e2r.sources.source_errors import (
    SourceRequest,
    date_value,
    load_fixture_records,
    parsed_fields_from_record,
    require_credential,
    text_or_none,
)


NAVER_WEBDOC_BASE_URL = "https://openapi.naver.com/v1/search/webkr.json"


@dataclass(frozen=True)
class NaverWebDocConnector:
    """Fixture-first Naver Web/Doc connector for broker PDF discovery."""

    client_id: str | None = None
    client_secret: str | None = None
    fixture_root: str | Path | None = "data/raw/naver_webdoc"
    fixture_mode: bool = True
    base_url: str = NAVER_WEBDOC_BASE_URL

    def build_report_search_requests(self, company: str, as_of_date: date) -> tuple[SourceRequest, ...]:
        return tuple(self._build_request(template.format(company=company), as_of_date) for template in REPORT_QUERY_TEMPLATES)

    def require_live_credentials(self) -> tuple[str, str]:
        return (
            require_credential(self.client_id, "NAVER_CLIENT_ID"),
            require_credential(self.client_secret, "NAVER_CLIENT_SECRET"),
        )

    def search_reports(self, company: str, as_of_date: date) -> tuple[ReportSearchResult, ...]:
        results = tuple(self.normalize_result(row) for row in load_fixture_records(self.fixture_root, "reports"))
        return tuple(
            sorted(
                (
                    item
                    for item in results
                    if (item.company in (None, company) or company in item.title)
                    and (item.publish_date is None or item.publish_date <= as_of_date)
                ),
                key=lambda item: (item.publish_date or date.min, item.title),
            )
        )

    def _build_request(self, query: str, as_of_date: date) -> SourceRequest:
        headers = {}
        if self.client_id:
            headers["X-Naver-Client-Id"] = self.client_id
        if self.client_secret:
            headers["X-Naver-Client-Secret"] = self.client_secret
        return SourceRequest(
            method="GET",
            url=self.base_url,
            params={"query": query, "display": 20, "sort": "date", "as_of_date": as_of_date.isoformat()},
            headers=headers,
            fixture_mode=self.fixture_mode,
            credential_name="NAVER_CLIENT_ID/NAVER_CLIENT_SECRET",
        )

    @staticmethod
    def normalize_result(row: Mapping[str, Any]) -> ReportSearchResult:
        known = {
            "url",
            "link",
            "title",
            "source",
            "publish_date",
            "company",
            "query",
            "snippet",
            "description",
            "parsed_fields",
        }
        url = str(row.get("url") or row.get("link"))
        parsed = parsed_fields_from_record(row, known)
        return ReportSearchResult(
            url=url,
            title=str(row.get("title") or url),
            source=str(row.get("source") or "Naver WebDoc"),
            publish_date=date_value(row["publish_date"]) if row.get("publish_date") else None,
            company=text_or_none(row.get("company")),
            query=text_or_none(row.get("query")),
            snippet=text_or_none(row.get("snippet") or row.get("description")),
            is_pdf=url.lower().split("?")[0].endswith(".pdf"),
            is_recognized_report_domain=is_recognized_report_domain(url),
            parsed_fields=parsed,
        )
