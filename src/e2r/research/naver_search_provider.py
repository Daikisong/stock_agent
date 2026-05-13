"""Free Naver Search API provider with fixture fallback."""

from __future__ import annotations

import json
import os
import re
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import date, datetime
from email.utils import parsedate_to_datetime
from typing import Any, Mapping, Sequence

from e2r.research.search_provider import FixtureSearchProvider, SearchResult, normalize_search_result
from e2r.sources.source_errors import SourceRequest


NAVER_SEARCH_ENDPOINTS: Mapping[str, str] = {
    "news": "https://openapi.naver.com/v1/search/news.json",
    "web": "https://openapi.naver.com/v1/search/webkr.json",
    "doc": "https://openapi.naver.com/v1/search/doc.json",
}


@dataclass
class NaverFreeSearchProvider:
    """Optional free Naver search provider.

    Fixture mode is the default. Live API execution is enabled only when
    ``live_enabled`` is true and credentials are present.
    """

    client_id: str | None = None
    client_secret: str | None = None
    search_domains: Sequence[str] = ("news", "web", "doc")
    fixture_provider: FixtureSearchProvider | None = None
    fixture_mode: bool = True
    live_enabled: bool = False
    built_requests: list[SourceRequest] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.client_id is None:
            self.client_id = os.getenv("NAVER_CLIENT_ID")
        if self.client_secret is None:
            self.client_secret = os.getenv("NAVER_CLIENT_SECRET")

    def search(self, query: str, as_of_date: date, max_results: int = 10) -> tuple[SearchResult, ...]:
        fixture_results = self.fixture_provider.search(query, as_of_date, max_results) if self.fixture_provider else ()
        if self.fixture_mode:
            self.built_requests.extend(self.build_search_requests(query, as_of_date, max_results))
            return fixture_results
        if not self.live_enabled:
            self.built_requests.extend(self.build_search_requests(query, as_of_date, max_results))
            return fixture_results
        if not self.client_id or not self.client_secret:
            self.errors.append("missing_naver_credentials")
            self.built_requests.extend(self.build_search_requests(query, as_of_date, max_results))
            return fixture_results

        results: list[SearchResult] = list(fixture_results)
        for request in self.build_search_requests(query, as_of_date, max_results):
            self.built_requests.append(request)
            results.extend(self._execute_request(request, query, as_of_date))
        unique: dict[str, SearchResult] = {}
        for item in results:
            if item.published_at is not None and item.published_at.date() > as_of_date:
                continue
            unique.setdefault(item.url, item)
        return tuple(sorted(unique.values(), key=lambda item: item.rank or 9999)[:max_results])

    def build_search_requests(self, query: str, as_of_date: date, max_results: int = 10) -> tuple[SourceRequest, ...]:
        requests: list[SourceRequest] = []
        for domain in self.search_domains:
            if domain not in NAVER_SEARCH_ENDPOINTS:
                continue
            headers: dict[str, str] = {}
            if self.client_id:
                headers["X-Naver-Client-Id"] = self.client_id
            if self.client_secret:
                headers["X-Naver-Client-Secret"] = self.client_secret
            requests.append(
                SourceRequest(
                    method="GET",
                    url=NAVER_SEARCH_ENDPOINTS[domain],
                    params={
                        "query": query,
                        "display": min(max_results, 100),
                        "sort": "date",
                        "as_of_date": as_of_date.isoformat(),
                    },
                    headers=headers,
                    fixture_mode=self.fixture_mode,
                    credential_name="NAVER_CLIENT_ID/NAVER_CLIENT_SECRET",
                )
            )
        return tuple(requests)

    def _execute_request(self, request: SourceRequest, query: str, as_of_date: date) -> tuple[SearchResult, ...]:
        url = f"{request.url}?{urllib.parse.urlencode({k: v for k, v in request.params.items() if k != 'as_of_date'})}"
        http_request = urllib.request.Request(url, headers=dict(request.headers))
        try:
            with urllib.request.urlopen(http_request, timeout=10) as response:  # nosec - explicitly user-enabled provider
                payload = json.loads(response.read().decode("utf-8"))
        except Exception as exc:  # pragma: no cover - live network path
            self.errors.append(f"naver_live_search_failed:{type(exc).__name__}:{exc}")
            return ()
        return tuple(self.normalize_response(payload, query=query, as_of_date=as_of_date, source=request.url))

    @staticmethod
    def normalize_response(
        payload: Mapping[str, Any],
        *,
        query: str,
        as_of_date: date,
        source: str = "Naver Search",
    ) -> tuple[SearchResult, ...]:
        results: list[SearchResult] = []
        for rank, item in enumerate(payload.get("items", ()), start=1):
            row = _normalize_naver_item(item, query=query, rank=rank, source=source)
            result = normalize_search_result(row, fallback_query=query)
            if result.published_at is not None and result.published_at.date() > as_of_date:
                continue
            results.append(result)
        return tuple(results)


def _normalize_naver_item(item: Mapping[str, Any], *, query: str, rank: int, source: str) -> dict[str, Any]:
    title = _strip_html(str(item.get("title") or ""))
    snippet = _strip_html(str(item.get("description") or ""))
    url = str(item.get("originallink") or item.get("link") or "")
    published_at = _naver_datetime(item.get("pubDate") or item.get("postdate"))
    return {
        "title": title or url,
        "url": url,
        "snippet": snippet,
        "source": source,
        "published_at": published_at.isoformat() if published_at else None,
        "query": query,
        "rank": rank,
        "is_news": "news" in source.lower() or bool(item.get("originallink")),
    }


def _strip_html(value: str) -> str:
    return re.sub(r"<[^>]+>", "", value).replace("&quot;", '"').replace("&amp;", "&").strip()


def _naver_datetime(value: Any) -> datetime | None:
    if not value:
        return None
    text = str(value)
    try:
        if len(text) == 8 and text.isdigit():
            return datetime(int(text[:4]), int(text[4:6]), int(text[6:8]), 8, 0)
        return parsedate_to_datetime(text).replace(tzinfo=None)
    except (TypeError, ValueError):
        return None


__all__ = ["NAVER_SEARCH_ENDPOINTS", "NaverFreeSearchProvider"]
