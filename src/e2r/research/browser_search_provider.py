"""Playwright-capable browser search provider with fixture HTML mode."""

from __future__ import annotations

import html
import re
from dataclasses import dataclass, field
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Mapping
from urllib.parse import quote_plus, urlparse

from e2r.research.search_provider import SearchResult
from e2r.sources.report_search import is_recognized_report_domain
from e2r.sources.source_errors import datetime_value


BLOCK_TOKENS: tuple[str, ...] = (
    "captcha",
    "unusual traffic",
    "automated queries",
    "robot check",
    "자동입력",
    "보안문자",
    "차단",
)

NEWS_DOMAIN_TOKENS: tuple[str, ...] = (
    "news",
    "naver.com",
    "yna.co.kr",
    "hankyung.com",
    "mk.co.kr",
    "edaily.co.kr",
    "reuters.com",
    "bloomberg.com",
    "sedaily.com",
)

DISCLOSURE_DOMAIN_TOKENS: tuple[str, ...] = (
    "dart.fss.or.kr",
    "opendart.fss.or.kr",
    "kind.krx.co.kr",
    "sec.gov",
)


@dataclass
class BrowserSearchProvider:
    """Search provider that parses local HTML and can later drive Playwright."""

    fixture_html_by_query: Mapping[str, str | Path] = field(default_factory=dict)
    search_engine: str = "bing"
    live_enabled: bool = False
    timeout_ms: int = 15_000
    stop_on_captcha_or_block: bool = True
    errors: list[str] = field(default_factory=list)
    blocked: bool = False

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        html_text = self._fixture_html(query)
        if html_text is not None:
            return self.parse_search_results(html_text, query, as_of_date)[:max_results]
        if not self.live_enabled:
            return ()
        html_text = self._search_with_playwright(query)
        if not html_text:
            return ()
        return self.parse_search_results(html_text, query, as_of_date)[:max_results]

    def parse_search_results(self, html_text: str, query: str, as_of_date: date) -> tuple[SearchResult, ...]:
        if self._is_blocked(html_text):
            self.blocked = True
            self.errors.append("captcha_or_block_detected")
            return ()
        parser = _SearchHTMLParser()
        parser.feed(html_text)
        parsed = parser.results()
        results: list[SearchResult] = []
        for index, item in enumerate(parsed, start=1):
            published_at = None
            if item.get("published_at"):
                try:
                    published_at = datetime_value(item["published_at"])
                except ValueError:
                    published_at = None
            if published_at is not None and published_at.date() > as_of_date:
                continue
            url = str(item.get("url") or "")
            title = str(item.get("title") or url)
            snippet = str(item.get("snippet") or "") or None
            result_type = self.classify_result_type(url, title, snippet)
            results.append(
                SearchResult(
                    title=title,
                    url=url,
                    snippet=snippet,
                    source=str(item.get("source") or _domain(url) or "BrowserSearch"),
                    published_at=published_at,
                    query=query,
                    rank=int(item.get("rank") or index),
                    is_pdf=self.detect_pdf(url, title),
                    is_report_domain=self.detect_report_domain(url),
                    is_news=result_type == "news",
                    is_disclosure=result_type == "disclosure",
                    confidence=0.75 if result_type != "unknown" else 0.45,
                )
            )
        return tuple(results)

    def classify_result_type(self, url: str, title: str, snippet: str | None = None) -> str:
        haystack = f"{title} {snippet or ''} {url}"
        if self.detect_disclosure_domain(url) or any(token in haystack for token in ("공시", "단일판매", "신규시설투자")):
            return "disclosure"
        if self.detect_report_domain(url) or self.detect_pdf(url, title) or any(token in haystack for token in ("Review", "리포트", "목표주가", "OPM")):
            return "report"
        if self.detect_news_domain(url) or any(token in haystack for token in ("뉴스", "보도", "기사", "Reuters")):
            return "news"
        return "unknown"

    @staticmethod
    def detect_pdf(url: str, title: str = "") -> bool:
        lowered = f"{url} {title}".lower()
        return urlparse(url.lower()).path.endswith(".pdf") or ".pdf?" in lowered or " pdf" in lowered

    @staticmethod
    def detect_report_domain(url: str) -> bool:
        return is_recognized_report_domain(url)

    @staticmethod
    def detect_news_domain(url: str) -> bool:
        lowered = url.lower()
        return any(token in lowered for token in NEWS_DOMAIN_TOKENS)

    @staticmethod
    def detect_disclosure_domain(url: str) -> bool:
        lowered = url.lower()
        return any(token in lowered for token in DISCLOSURE_DOMAIN_TOKENS)

    def build_search_url(self, query: str) -> str:
        encoded = quote_plus(query)
        engine = self.search_engine.lower()
        if engine == "google":
            return f"https://www.google.com/search?q={encoded}"
        if engine == "naver":
            return f"https://search.naver.com/search.naver?query={encoded}"
        return f"https://www.bing.com/search?q={encoded}"

    def _fixture_html(self, query: str) -> str | None:
        if query not in self.fixture_html_by_query:
            return None
        value = self.fixture_html_by_query[query]
        if isinstance(value, Path) or _path_exists(str(value)):
            return Path(value).read_text(encoding="utf-8")
        return str(value)

    def _search_with_playwright(self, query: str) -> str | None:
        try:
            from playwright.sync_api import sync_playwright  # type: ignore
        except ImportError:
            self.errors.append("playwright_not_installed")
            return None

        try:
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(self.build_search_url(query), wait_until="domcontentloaded", timeout=self.timeout_ms)
                content = page.content()
                browser.close()
                return content
        except Exception as exc:  # pragma: no cover - depends on local browser runtime
            self.errors.append(f"playwright_search_failed:{type(exc).__name__}:{exc}")
            return None

    @staticmethod
    def _is_blocked(html_text: str) -> bool:
        lowered = html.unescape(html_text).lower()
        return any(token.lower() in lowered for token in BLOCK_TOKENS)


class _SearchHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._items: list[dict[str, Any]] = []
        self._current: dict[str, Any] | None = None
        self._capture: str | None = None
        self._buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {key: value or "" for key, value in attrs}
        classes = attr.get("class", "")
        if tag in {"div", "article", "li"} and any(token in classes.split() for token in ("result", "search-result")):
            self._finish_current()
            self._current = {
                "source": attr.get("data-source"),
                "published_at": attr.get("data-published-at") or attr.get("data-date"),
                "rank": attr.get("data-rank"),
            }
            return
        if tag == "a" and attr.get("href"):
            if self._current is None:
                self._current = {}
            if not self._current.get("url"):
                self._current["url"] = attr["href"]
                self._capture = "title"
                self._buffer = []
        elif tag in {"p", "span"} and self._current is not None:
            if "snippet" in classes.split() or "desc" in classes.split():
                self._capture = "snippet"
                self._buffer = []

    def handle_endtag(self, tag: str) -> None:
        if self._capture and tag in {"a", "p", "span"}:
            text = " ".join("".join(self._buffer).split())
            if text and self._current is not None:
                self._current[self._capture] = text
            self._capture = None
            self._buffer = []
        if tag in {"div", "article", "li"} and self._current is not None and self._current.get("url"):
            self._finish_current()

    def handle_data(self, data: str) -> None:
        if self._capture:
            self._buffer.append(data)

    def results(self) -> tuple[dict[str, Any], ...]:
        self._finish_current()
        unique: dict[str, dict[str, Any]] = {}
        for item in self._items:
            url = item.get("url")
            title = item.get("title")
            if not url or not title:
                continue
            unique.setdefault(str(url), item)
        return tuple(unique.values())

    def _finish_current(self) -> None:
        if self._current and self._current.get("url") and self._current.get("title"):
            item = dict(self._current)
            if item.get("rank") not in (None, ""):
                try:
                    item["rank"] = int(float(str(item["rank"])))
                except ValueError:
                    item.pop("rank", None)
            self._items.append(item)
        self._current = None


def _domain(url: str) -> str:
    return urlparse(url).netloc


def _path_exists(value: str) -> bool:
    try:
        return Path(value).exists()
    except OSError:
        return False


__all__ = ["BrowserSearchProvider"]
