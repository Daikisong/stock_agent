"""Search provider abstractions for fixture-first web research."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence
from urllib.parse import urlparse

from e2r.sources.report_search import is_recognized_report_domain
from e2r.sources.source_errors import SourceRequest, datetime_value, float_or_none, load_fixture_records, text_or_none


@dataclass(frozen=True)
class SearchResult:
    """Normalized search result metadata."""

    title: str
    url: str
    snippet: str | None = None
    source: str = "fixture-search"
    published_at: datetime | None = None
    query: str | None = None
    rank: int = 0
    is_pdf: bool = False
    is_report_domain: bool = False
    is_news: bool = False
    is_disclosure: bool = False
    confidence: float = 0.5
    date_verified: bool | None = None
    green_allowed_by_date: bool | None = None

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("title must be non-empty")
        if not self.url.strip():
            raise ValueError("url must be non-empty")
        if self.confidence < 0 or self.confidence > 1:
            raise ValueError("confidence must be between 0 and 1")


class SearchProvider(Protocol):
    """Search provider contract used by the web research runner."""

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        """Return normalized results visible as of ``as_of_date``."""


@dataclass(frozen=True)
class FixtureSearchProvider:
    """Search provider backed by in-memory records or CSV/JSON fixtures."""

    results_by_query: Mapping[str, Sequence[SearchResult | Mapping[str, Any]]] = field(default_factory=dict)
    fixture_root: str | Path | None = None
    fixture_stem: str = "search_results"

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        rows: list[SearchResult] = []
        for item in self.results_by_query.get(query, ()):
            rows.append(item if isinstance(item, SearchResult) else normalize_search_result(item, fallback_query=query))
        for record in load_fixture_records(self.fixture_root, self.fixture_stem):
            item = normalize_search_result(record, fallback_query=text_or_none(record.get("query")) or query)
            if item.query == query:
                rows.append(item)

        visible = (
            item
            for item in rows
            if item.published_at is None or item.published_at.date() <= as_of_date
        )
        return tuple(sorted(visible, key=lambda item: item.rank or 9999)[:max_results])


class EmptySearchProvider:
    """No-result provider for tests and missing connector paths."""

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        return ()


@dataclass
class RequestOnlySearchProvider:
    """Provider that records future live request plans without executing them."""

    provider_name: str = "naver"
    base_url: str | None = None
    fixture_mode: bool = True
    credential_name: str | None = None
    built_requests: list[SourceRequest] = field(default_factory=list)

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        self.built_requests.append(self.build_request(query, as_of_date, max_results))
        return ()

    def build_request(self, query: str, as_of_date: date, max_results: int = 100) -> SourceRequest:
        provider = self.provider_name.lower()
        if provider == "naver":
            url = self.base_url or "https://openapi.naver.com/v1/search/webkr.json"
            params = {"query": query, "display": max_results, "sort": "date", "as_of_date": as_of_date.isoformat()}
            credential = self.credential_name or "NAVER_CLIENT_ID/NAVER_CLIENT_SECRET"
        elif provider == "bing":
            url = self.base_url or "https://api.bing.microsoft.com/v7.0/search"
            params = {"q": query, "count": max_results, "as_of_date": as_of_date.isoformat()}
            credential = self.credential_name or "BING_SEARCH_KEY"
        elif provider == "serpapi":
            url = self.base_url or "https://serpapi.com/search.json"
            params = {"q": query, "num": max_results, "as_of_date": as_of_date.isoformat()}
            credential = self.credential_name or "SERPAPI_API_KEY"
        else:
            url = self.base_url or f"fixture://{provider}"
            params = {"query": query, "max_results": max_results, "as_of_date": as_of_date.isoformat()}
            credential = self.credential_name
        return SourceRequest(
            method="GET",
            url=url,
            params=params,
            fixture_mode=self.fixture_mode,
            credential_name=credential,
        )


def normalize_search_result(row: Mapping[str, Any], *, fallback_query: str | None = None) -> SearchResult:
    """Normalize a fixture row into ``SearchResult``."""

    url = str(row.get("url") or row.get("link") or "")
    title = str(row.get("title") or url)
    source = str(row.get("source") or _domain(url) or "fixture-search")
    published = row.get("published_at") or row.get("publish_date") or row.get("date")
    is_pdf = _boolish(row.get("is_pdf")) or _is_pdf_url(url)
    report_domain = _boolish(row.get("is_report_domain") or row.get("is_recognized_report_domain"))
    return SearchResult(
        title=title,
        url=url,
        snippet=text_or_none(row.get("snippet") or row.get("description")),
        source=source,
        published_at=datetime_value(published) if published else None,
        query=text_or_none(row.get("query")) or fallback_query,
        rank=int(float(row.get("rank") or 0)),
        is_pdf=is_pdf,
        is_report_domain=report_domain or is_recognized_report_domain(url),
        is_news=_boolish(row.get("is_news")) or _looks_like_news(source, url),
        is_disclosure=_boolish(row.get("is_disclosure")) or _looks_like_disclosure(title, url),
        confidence=float_or_none(row.get("confidence")) or 0.5,
        date_verified=_optional_boolish(row.get("date_verified")),
        green_allowed_by_date=_optional_boolish(row.get("green_allowed_by_date")),
    )


def _boolish(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value in (None, ""):
        return False
    if isinstance(value, (int, float)):
        return value != 0
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def _optional_boolish(value: Any) -> bool | None:
    if value in (None, ""):
        return None
    return _boolish(value)


def _is_pdf_url(url: str) -> bool:
    lowered = url.lower()
    return urlparse(lowered).path.endswith(".pdf") or ".pdf?" in lowered


def _looks_like_news(source: str, url: str) -> bool:
    haystack = f"{source} {url}".lower()
    return any(token in haystack for token in ("news", "naver.com", "yna.co.kr", "reuters", "bloomberg"))


def _looks_like_disclosure(title: str, url: str) -> bool:
    haystack = f"{title} {url}"
    return any(token in haystack for token in ("단일판매", "공급계약", "신규시설투자", "dart.fss", "kind.krx"))


def _domain(url: str) -> str:
    return urlparse(url).netloc


__all__ = [
    "EmptySearchProvider",
    "FixtureSearchProvider",
    "RequestOnlySearchProvider",
    "SearchProvider",
    "SearchResult",
    "normalize_search_result",
]
