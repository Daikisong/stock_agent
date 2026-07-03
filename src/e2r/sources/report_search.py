"""Broker report search connector and domain recognition."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Mapping
from urllib.parse import parse_qs, urlparse

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
    "stock.pstatic.net/stock-research/company",
    "stock.pstatic.net/stock-research/industry",
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

NON_REPORT_URL_HINTS: tuple[str, ...] = (
    "agreement",
    "brochure",
    "customer",
    "event",
    "manual",
    "notice",
    "policy",
    "privacy",
    "product",
    "terms",
    "약관",
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
    parsed = _parse_url_like(url)
    host = _normalized_hostname(parsed.hostname or "")
    path = parsed.path.lower()
    if not host:
        return False
    for domain in RECOGNIZED_REPORT_DOMAINS:
        domain_text = domain.lower().strip()
        if not domain_text:
            continue
        domain_host, domain_path = _split_domain_path(domain_text)
        if not _host_matches_domain(host, domain_host):
            continue
        if domain_path and not path.startswith(domain_path):
            continue
        return True
    return False


def is_verified_report_original_url(
    url: str,
    *,
    title: str | None = None,
    content_type: str | None = None,
) -> bool:
    """Return true only for report-original PDF routes, not any broker-domain PDF."""

    if not is_recognized_report_domain(url):
        return False
    parsed = _parse_url_like(url)
    host = _normalized_hostname(parsed.hostname or "")
    path = parsed.path.lower()
    query = parsed.query.lower()
    content_type_text = str(content_type or "").lower()
    path_query = " ".join((path, query))
    if any(hint in path_query for hint in NON_REPORT_URL_HINTS):
        return False
    if not _looks_like_pdf(parsed, content_type=content_type_text):
        return False
    if host == "stock.pstatic.net":
        return path.startswith("/stock-research/company/") or path.startswith("/stock-research/industry/")
    if host == "ssl.pstatic.net":
        return path.startswith("/imgstock/upload/research/")
    if host == "file.alphasquare.co.kr":
        return path.startswith("/media/pdfs/")
    if host == "hanaw.com" or host.endswith(".hanaw.com"):
        return path.startswith("/download/research/")
    if host == "samsungpop.com" or host.endswith(".samsungpop.com"):
        return _is_samsungpop_research_download(parsed)
    return False


def _is_pdf_url(url: str) -> bool:
    return _parse_url_like(url).path.lower().endswith(".pdf") or ".pdf?" in url.lower()


def _looks_like_pdf(parsed: Any, *, content_type: str) -> bool:
    url = parsed.geturl().lower()
    query_values = " ".join(value for values in parse_qs(parsed.query).values() for value in values).lower()
    return (
        parsed.path.lower().endswith(".pdf")
        or ".pdf?" in url
        or "application/pdf" in content_type
        or "contenttype=application/pdf" in parsed.query.lower()
        or ".pdf" in query_values
    )


def _domain(url: str) -> str:
    return _parse_url_like(url).netloc or "unknown"


def _is_samsungpop_research_download(parsed: Any) -> bool:
    if parsed.path.lower() != "/common.do":
        return False
    query = {str(key).lower(): tuple(str(value).lower() for value in values) for key, values in parse_qs(parsed.query).items()}
    save_keys = query.get("savekey", ())
    file_names = query.get("filename", ())
    content_types = query.get("contenttype", ())
    commands = query.get("cmd", ())
    return (
        any(value == "research.pdf" for value in save_keys)
        and any(".pdf" in value for value in file_names)
        and any(value == "down" for value in commands)
        and any("application/pdf" in value for value in content_types)
    )


def _parse_url_like(url: str) -> Any:
    value = str(url or "").strip()
    if value and "://" not in value:
        value = f"https://{value}"
    return urlparse(value)


def _normalized_hostname(host: str) -> str:
    normalized = str(host or "").strip().lower().strip(".")
    if normalized.startswith("www."):
        normalized = normalized[4:]
    return normalized


def _split_domain_path(domain: str) -> tuple[str, str]:
    if "/" not in domain:
        return _normalized_hostname(domain), ""
    host, path = domain.split("/", 1)
    return _normalized_hostname(host), f"/{path.strip('/')}"


def _host_matches_domain(host: str, domain_host: str) -> bool:
    if not host or not domain_host:
        return False
    return host == domain_host or host.endswith(f".{domain_host}")
