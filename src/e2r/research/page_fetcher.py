"""Fixture-first page fetcher for web research."""

from __future__ import annotations

import hashlib
import html
import re
from dataclasses import dataclass
from datetime import date, datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib import error, parse, request
from typing import Mapping


@dataclass(frozen=True)
class FetchResult:
    """Fetched document text or a clear unavailable reason."""

    url: str
    ok: bool
    text: str | None = None
    content_type: str | None = None
    fetched_at: datetime | None = None
    reason: str | None = None
    source_path: str | None = None


@dataclass(frozen=True)
class PageFetcher:
    """Fetch page text from fixtures first, then live HTTP when enabled."""

    fixture_text_by_url: Mapping[str, str | Path] | None = None
    live_enabled: bool = False
    timeout_seconds: float = 10.0
    cache_directory: str | Path | None = None
    max_body_bytes: int = 2_000_000
    max_text_chars: int = 200_000
    user_agent: str = (
        "Mozilla/5.0 (compatible; E2RResearchBot/0.1; +https://example.invalid/e2r)"
    )

    def fetch(self, url: str, *, as_of_date: date) -> FetchResult:
        fetched_at = datetime(as_of_date.year, as_of_date.month, as_of_date.day, 8, 0)
        if self.fixture_text_by_url and url in self.fixture_text_by_url:
            value = self.fixture_text_by_url[url]
            if isinstance(value, Path) or (isinstance(value, str) and _path_exists(value)):
                path = Path(value)
                return FetchResult(
                    url=url,
                    ok=True,
                    text=path.read_text(encoding="utf-8"),
                    content_type="text/plain",
                    fetched_at=fetched_at,
                    source_path=str(path),
                )
            return FetchResult(
                url=url,
                ok=True,
                text=str(value),
                content_type="text/plain",
                fetched_at=fetched_at,
            )
        if not self.live_enabled:
            return FetchResult(
                url=url,
                ok=False,
                fetched_at=fetched_at,
                reason="live fetching is disabled and no fixture text was mapped for this URL",
            )
        return self._fetch_live(url, as_of_date=as_of_date, fetched_at=fetched_at)

    def _fetch_live(self, url: str, *, as_of_date: date, fetched_at: datetime) -> FetchResult:
        parsed = parse.urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            return FetchResult(
                url=url,
                ok=False,
                fetched_at=fetched_at,
                reason="unsupported_url_scheme_for_live_fetch",
            )
        if _looks_like_pdf_url(url):
            return FetchResult(
                url=url,
                ok=False,
                fetched_at=fetched_at,
                reason="live_pdf_text_extraction_not_implemented",
            )

        cache_path = _cache_path(self.cache_directory, url, as_of_date)
        if cache_path is not None and cache_path.exists():
            try:
                cached_text = cache_path.read_text(encoding="utf-8")
                if cached_text.strip():
                    return FetchResult(
                        url=url,
                        ok=True,
                        text=cached_text[: self.max_text_chars],
                        content_type="text/plain",
                        fetched_at=fetched_at,
                        source_path=str(cache_path),
                    )
            except OSError:
                pass

        try:
            req = request.Request(
                _http_request_url(url),
                headers={
                    "User-Agent": self.user_agent,
                    "Accept": "text/html, text/plain;q=0.9, */*;q=0.1",
                    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.6,en;q=0.5",
                },
                method="GET",
            )
            with request.urlopen(req, timeout=self.timeout_seconds) as response:
                content_type = _content_type(response)
                if "pdf" in content_type.lower():
                    return FetchResult(
                        url=url,
                        ok=False,
                        content_type=content_type,
                        fetched_at=fetched_at,
                        reason="live_pdf_text_extraction_not_implemented",
                    )
                body = response.read(max(1, self.max_body_bytes + 1))
                if len(body) > self.max_body_bytes:
                    body = body[: self.max_body_bytes]
                charset = _charset(response) or "utf-8"
        except (error.HTTPError, error.URLError, TimeoutError, OSError, UnicodeError, ValueError) as exc:
            return FetchResult(
                url=url,
                ok=False,
                fetched_at=fetched_at,
                reason=f"live_fetch_failed:{type(exc).__name__}:{exc}",
            )

        decoded = body.decode(charset, errors="replace")
        text = _text_from_response(decoded, content_type)
        if not text.strip():
            return FetchResult(
                url=url,
                ok=False,
                content_type=content_type,
                fetched_at=fetched_at,
                reason="live_fetch_empty_text",
            )
        text = text[: self.max_text_chars]
        source_path = _write_cache(cache_path, text)
        return FetchResult(
            url=url,
            ok=True,
            text=text,
            content_type=content_type,
            fetched_at=fetched_at,
            source_path=source_path,
        )


def _path_exists(value: str) -> bool:
    try:
        return Path(value).exists()
    except OSError:
        return False


def _http_request_url(url: str) -> str:
    parts = parse.urlsplit(url)
    netloc = parts.netloc.encode("idna").decode("ascii") if parts.netloc else ""
    path = parse.quote(parts.path or "/", safe="/%:@&+$,;=-_.!~*'()")
    query = parse.quote(parts.query, safe="=&?/:;+,%@-._~!$'()*[]")
    return parse.urlunsplit((parts.scheme, netloc, path, query, ""))


def _looks_like_pdf_url(url: str) -> bool:
    lowered = url.lower()
    return parse.urlparse(lowered).path.endswith(".pdf") or ".pdf?" in lowered


def _cache_path(cache_directory: str | Path | None, url: str, as_of_date: date) -> Path | None:
    if cache_directory is None:
        return None
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()
    return Path(cache_directory) / as_of_date.isoformat() / f"{digest}.txt"


def _write_cache(cache_path: Path | None, text: str) -> str | None:
    if cache_path is None:
        return None
    try:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(text, encoding="utf-8")
    except OSError:
        return None
    return str(cache_path)


def _content_type(response: object) -> str:
    headers = getattr(response, "headers", None)
    if headers is not None and hasattr(headers, "get"):
        return str(headers.get("Content-Type") or headers.get("content-type") or "")
    return ""


def _charset(response: object) -> str | None:
    headers = getattr(response, "headers", None)
    if headers is None:
        return None
    getter = getattr(headers, "get_content_charset", None)
    if callable(getter):
        return getter()
    content_type = _content_type(response)
    match = re.search(r"charset=([\w.-]+)", content_type, flags=re.IGNORECASE)
    return match.group(1) if match else None


def _text_from_response(decoded: str, content_type: str) -> str:
    if "html" in content_type.lower() or _looks_like_html(decoded):
        parser = _HTMLTextExtractor()
        parser.feed(decoded)
        parser.close()
        return parser.text()
    return _normalize_text(decoded)


def _looks_like_html(text: str) -> bool:
    head = text[:500].lower()
    return "<html" in head or "<body" in head or "<!doctype html" in head


class _HTMLTextExtractor(HTMLParser):
    _SKIP_TAGS = {"script", "style", "noscript", "svg", "canvas"}
    _BLOCK_TAGS = {
        "article",
        "aside",
        "blockquote",
        "br",
        "dd",
        "div",
        "dl",
        "dt",
        "figcaption",
        "footer",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "li",
        "main",
        "p",
        "section",
        "table",
        "td",
        "th",
        "tr",
        "ul",
    }
    _META_KEYS = {
        "description",
        "og:description",
        "twitter:description",
        "title",
        "og:title",
        "twitter:title",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in self._SKIP_TAGS:
            self._skip_depth += 1
            return
        if tag == "meta":
            attrs_by_name = {key.lower(): value for key, value in attrs if key and value}
            meta_key = attrs_by_name.get("name") or attrs_by_name.get("property")
            content = attrs_by_name.get("content")
            if meta_key and content and meta_key.lower() in self._META_KEYS:
                self._parts.append(content)
        if tag in self._BLOCK_TAGS:
            self._parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in self._SKIP_TAGS and self._skip_depth > 0:
            self._skip_depth -= 1
            return
        if tag in self._BLOCK_TAGS:
            self._parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        if data.strip():
            self._parts.append(data)

    def text(self) -> str:
        return _normalize_text("\n".join(self._parts))


def _normalize_text(text: str) -> str:
    unescaped = html.unescape(text).replace("\xa0", " ")
    lines = [re.sub(r"[ \t\r\f\v]+", " ", line).strip() for line in unescaped.splitlines()]
    return "\n".join(line for line in lines if line)


__all__ = ["FetchResult", "PageFetcher"]
