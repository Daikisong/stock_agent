"""Broker report search connector and domain recognition."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Mapping
from urllib.parse import urlparse

from e2r.sources.source_errors import (
    SourceRequest,
    date_value,
    load_fixture_records,
    parsed_fields_from_record,
    text_or_none,
)


REPORT_QUERY_TEMPLATES: tuple[str, ...] = (
    "{company} 목표주가 상향 EPS 상향 PDF",
    "{company} 컨센서스 상회 Review PDF",
    "{company} 1Q Review 영업이익 컨센서스 PDF",
    "{company} 2Q Review 영업이익 컨센서스 PDF",
    "{company} 3Q Review 영업이익 컨센서스 PDF",
    "{company} 4Q Review 영업이익 컨센서스 PDF",
    "{company} 수주잔고 OPM 수출 비중 PDF",
    "{company} 신규시설투자 CAPA 증설 PDF",
    "{company} 장기공급계약 매출액 대비 PDF",
    "{company} ASP 상승 판가 상승 리드타임 PDF",
    "{company} 북미 미국향 데이터센터 수주 PDF",
    "{company} 실적 서프라이즈 목표주가 상향 PDF",
)

RECOGNIZED_REPORT_DOMAINS: tuple[str, ...] = (
    "ssl.pstatic.net/imgstock/upload/research/company",
    "file.alphasquare.co.kr/media/pdfs",
    "hanaw.com/download/research",
    "samsungpop.com",
    "m.ibks.com",
    "ibks.com",
    "kiwoom.com",
    "miraeasset.com",
    "shinhansec.com",
    "nhqv.com",
    "eugenefn.com",
    "sk증권",
    "sks.co.kr",
    "yuantakorea.com",
)


@dataclass(frozen=True)
class ReportSearchResult:
    """Metadata for a discovered report-like document."""

    url: str
    title: str
    source: str
    publish_date: date | None = None
    company: str | None = None
    query: str | None = None
    snippet: str | None = None
    is_pdf: bool = False
    is_recognized_report_domain: bool = False
    parsed_fields: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "parsed_fields", dict(self.parsed_fields))


@dataclass(frozen=True)
class ReportSearchConnector:
    """Fixture-first report discovery connector."""

    fixture_root: str | Path | None = "data/raw/report_search"
    fixture_mode: bool = True
    base_url: str = "fixture://report-search"

    def build_report_search_requests(self, company: str, as_of_date: date) -> tuple[SourceRequest, ...]:
        return tuple(
            SourceRequest(
                method="GET",
                url=self.base_url,
                params={"query": template.format(company=company), "as_of_date": as_of_date.isoformat()},
                fixture_mode=self.fixture_mode,
            )
            for template in REPORT_QUERY_TEMPLATES
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

    @staticmethod
    def normalize_result(row: Mapping[str, Any]) -> ReportSearchResult:
        known = {
            "url",
            "title",
            "source",
            "publish_date",
            "company",
            "query",
            "snippet",
            "is_pdf",
            "is_recognized_report_domain",
            "parsed_fields",
        }
        url = str(row["url"])
        parsed = parsed_fields_from_record(row, known)
        return ReportSearchResult(
            url=url,
            title=str(row.get("title") or url),
            source=str(row.get("source") or _domain(url)),
            publish_date=date_value(row["publish_date"]) if row.get("publish_date") else None,
            company=text_or_none(row.get("company")),
            query=text_or_none(row.get("query")),
            snippet=text_or_none(row.get("snippet")),
            is_pdf=_is_pdf_url(url) or str(row.get("is_pdf", "")).lower() == "true",
            is_recognized_report_domain=is_recognized_report_domain(url)
            or str(row.get("is_recognized_report_domain", "")).lower() == "true",
            parsed_fields=parsed,
        )

    def download_report_text(self, result: ReportSearchResult) -> str | None:
        """Stub for later PDF download/extraction.

        CP9 intentionally does not scrape or download aggressively. If a fixture
        has extracted text, callers should pass it to the research parser.
        """

        text = result.parsed_fields.get("extracted_text")
        return str(text) if text else None


def is_recognized_report_domain(url: str) -> bool:
    parsed = urlparse(url)
    normalized = f"{parsed.netloc}{parsed.path}".lower()
    return any(domain.lower() in normalized for domain in RECOGNIZED_REPORT_DOMAINS)


def _is_pdf_url(url: str) -> bool:
    return urlparse(url).path.lower().endswith(".pdf") or ".pdf?" in url.lower()


def _domain(url: str) -> str:
    return urlparse(url).netloc or "unknown"
