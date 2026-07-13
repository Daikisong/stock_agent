"""Fixture-first page fetcher for web research."""

from __future__ import annotations

import hashlib
import html
import json
import re
from dataclasses import dataclass
from datetime import date, datetime
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib import error, parse, request
from typing import Any, Mapping

from e2r.research.pdf_text_extractor import (
    PDFTextExtractor,
    extracted_text_unreadable_reason,
)


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
    referenced_urls: tuple[str, ...] = ()
    response_last_modified_at: datetime | None = None


@dataclass(frozen=True)
class PageFetcher:
    """Fetch page text from fixtures first, then live HTTP when enabled."""

    fixture_text_by_url: Mapping[str, str | Path] | None = None
    live_enabled: bool = False
    timeout_seconds: float = 10.0
    cache_directory: str | Path | None = None
    pdf_text_extractor: PDFTextExtractor | None = None
    max_body_bytes: int = 2_000_000
    max_pdf_body_bytes: int = 25_000_000
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
                text = path.read_text(encoding="utf-8")
                unreadable = extracted_text_unreadable_reason(text)
                if unreadable is not None:
                    return FetchResult(
                        url=url,
                        ok=False,
                        fetched_at=fetched_at,
                        reason=f"unreadable_fixture_text:{unreadable}",
                        source_path=str(path),
                    )
                return FetchResult(
                    url=url,
                    ok=True,
                    text=text,
                    content_type="text/plain",
                    fetched_at=fetched_at,
                    source_path=str(path),
                )
            text = str(value)
            unreadable = extracted_text_unreadable_reason(text)
            if unreadable is not None:
                return FetchResult(
                    url=url,
                    ok=False,
                    fetched_at=fetched_at,
                    reason=f"unreadable_fixture_text:{unreadable}",
                )
            return FetchResult(
                url=url,
                ok=True,
                text=text,
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

        cache_path = _cache_path(self.cache_directory, url, as_of_date)
        if cache_path is not None and cache_path.exists():
            try:
                cached_text = cache_path.read_text(encoding="utf-8")
                unreadable = extracted_text_unreadable_reason(cached_text)
                if unreadable is None:
                    cache_metadata = _read_cache_metadata(cache_path)
                    return FetchResult(
                        url=url,
                        ok=True,
                        text=cached_text[: self.max_text_chars],
                        content_type="text/plain",
                        fetched_at=fetched_at,
                        source_path=str(cache_path),
                        referenced_urls=tuple(
                            str(value)
                            for value in cache_metadata.get("referenced_urls", ())
                            if str(value).strip()
                        ),
                        response_last_modified_at=_cached_datetime(
                            cache_metadata.get("response_last_modified_at")
                        ),
                    )
            except OSError:
                pass

        try:
            req = request.Request(
                _http_request_url(url),
                headers={
                    "User-Agent": self.user_agent,
                    "Accept": "text/html, text/plain, application/pdf;q=0.9, */*;q=0.1",
                    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.6,en;q=0.5",
                },
                method="GET",
            )
            with request.urlopen(req, timeout=self.timeout_seconds) as response:
                content_type = _content_type(response)
                response_last_modified_at = _response_last_modified_at(response)
                pdf_like = _looks_like_pdf_url(url) or "pdf" in content_type.lower()
                body_limit = max(1, self.max_pdf_body_bytes if pdf_like else self.max_body_bytes)
                body = response.read(body_limit + 1)
                if len(body) > body_limit:
                    if pdf_like:
                        return FetchResult(
                            url=url,
                            ok=False,
                            content_type=content_type or "application/pdf",
                            fetched_at=fetched_at,
                            reason=f"live_fetch_body_too_large:pdf:{body_limit}",
                        )
                    body = body[: self.max_body_bytes]
                charset = _charset(response) or "utf-8"
        except (error.HTTPError, error.URLError, TimeoutError, OSError, UnicodeError, ValueError) as exc:
            return FetchResult(
                url=url,
                ok=False,
                fetched_at=fetched_at,
                reason=f"live_fetch_failed:{type(exc).__name__}:{exc}",
            )

        if _looks_like_pdf_url(url) or "pdf" in content_type.lower():
            extraction = (self.pdf_text_extractor or PDFTextExtractor()).extract_text_from_bytes(body)
            if not extraction.ok or not (extraction.text or "").strip():
                reason = extraction.reason or "empty_pdf_text"
                return FetchResult(
                    url=url,
                    ok=False,
                    content_type=content_type or "application/pdf",
                    fetched_at=fetched_at,
                    reason=f"live_pdf_text_extraction_failed:{reason}",
                )
            unreadable = extracted_text_unreadable_reason(extraction.text or "")
            if unreadable is not None:
                return FetchResult(
                    url=url,
                    ok=False,
                    content_type=content_type or "application/pdf",
                    fetched_at=fetched_at,
                    reason=f"live_pdf_text_extraction_failed:{unreadable}",
                )
            text = (extraction.text or "")[: self.max_text_chars]
            source_path = _write_cache(
                cache_path,
                text,
                response_last_modified_at=response_last_modified_at,
            )
            return FetchResult(
                url=url,
                ok=True,
                text=text,
                content_type=content_type or "application/pdf",
                fetched_at=fetched_at,
                source_path=source_path,
                response_last_modified_at=response_last_modified_at,
            )

        decoded = body.decode(charset, errors="replace")
        if "html" in content_type.lower() or _looks_like_html(decoded):
            text, referenced_urls = _html_text_and_references(
                decoded,
                base_url=url,
            )
        else:
            text = _normalize_text(decoded)
            referenced_urls = ()
        unreadable = extracted_text_unreadable_reason(text)
        if unreadable is not None:
            return FetchResult(
                url=url,
                ok=False,
                content_type=content_type,
                fetched_at=fetched_at,
                reason=f"live_fetch_unreadable_text:{unreadable}",
            )
        text = text[: self.max_text_chars]
        source_path = _write_cache(
            cache_path,
            text,
            referenced_urls=referenced_urls,
            response_last_modified_at=response_last_modified_at,
        )
        return FetchResult(
            url=url,
            ok=True,
            text=text,
            content_type=content_type,
            fetched_at=fetched_at,
            source_path=source_path,
            referenced_urls=referenced_urls,
            response_last_modified_at=response_last_modified_at,
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


def _write_cache(
    cache_path: Path | None,
    text: str,
    *,
    referenced_urls: tuple[str, ...] = (),
    response_last_modified_at: datetime | None = None,
) -> str | None:
    if cache_path is None:
        return None
    try:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(text, encoding="utf-8")
        _cache_metadata_path(cache_path).write_text(
            json.dumps(
                {
                    "referenced_urls": list(referenced_urls),
                    "response_last_modified_at": (
                        response_last_modified_at.isoformat()
                        if response_last_modified_at is not None
                        else None
                    ),
                },
                ensure_ascii=False,
                sort_keys=True,
            ),
            encoding="utf-8",
        )
    except OSError:
        return None
    return str(cache_path)


def _cache_metadata_path(cache_path: Path) -> Path:
    return cache_path.with_suffix(cache_path.suffix + ".metadata.json")


def _read_cache_metadata(cache_path: Path) -> Mapping[str, Any]:
    metadata_path = _cache_metadata_path(cache_path)
    if not metadata_path.is_file():
        return {}
    try:
        value = json.loads(metadata_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, Mapping) else {}


def _cached_datetime(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value))
    except ValueError:
        return None


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


def _response_last_modified_at(response: object) -> datetime | None:
    headers = getattr(response, "headers", None)
    if headers is None or not hasattr(headers, "get"):
        return None
    value = headers.get("Last-Modified") or headers.get("last-modified")
    if not value:
        return None
    try:
        return parsedate_to_datetime(str(value))
    except (TypeError, ValueError, OverflowError):
        return None


def _text_from_response(decoded: str, content_type: str) -> str:
    if "html" in content_type.lower() or _looks_like_html(decoded):
        return _html_text_and_references(decoded, base_url="")[0]
    return _normalize_text(decoded)


def _html_text_and_references(
    decoded: str,
    *,
    base_url: str,
) -> tuple[str, tuple[str, ...]]:
    parser = _HTMLTextExtractor(base_url=base_url)
    parser.feed(decoded)
    parser.close()
    raw_redirects = re.findall(
        r"(?:window\s*\.\s*)?(?:top\s*\.\s*)?location"
        r"(?:\s*\.\s*href)?\s*=\s*['\"]([^'\"]+)['\"]",
        decoded,
        flags=re.IGNORECASE,
    )
    references = tuple(
        dict.fromkeys(
            (
                *parser.referenced_urls(),
                *(
                    resolved
                    for value in raw_redirects
                    for resolved in (_resolved_http_url(base_url, value),)
                    if resolved is not None
                ),
            )
        )
    )
    return parser.text(), references


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

    def __init__(self, *, base_url: str = "") -> None:
        super().__init__(convert_charrefs=True)
        self._base_url = base_url
        self._parts: list[str] = []
        self._referenced_urls: list[str] = []
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
        if tag in {"a", "iframe", "source"}:
            attrs_by_name = {
                key.lower(): value for key, value in attrs if key and value
            }
            for attribute in ("href", "src"):
                resolved = _resolved_http_url(
                    self._base_url,
                    attrs_by_name.get(attribute),
                )
                if resolved is not None:
                    self._referenced_urls.append(resolved)
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

    def referenced_urls(self) -> tuple[str, ...]:
        return tuple(dict.fromkeys(self._referenced_urls))


def _resolved_http_url(base_url: str, value: str | None) -> str | None:
    raw = str(value or "").strip()
    if not raw or raw.startswith(("#", "data:", "javascript:", "mailto:", "tel:")):
        return None
    resolved = parse.urljoin(base_url, raw)
    parts = parse.urlsplit(resolved)
    if parts.scheme not in {"http", "https"} or not parts.netloc:
        return None
    return parse.urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, ""))


def _normalize_text(text: str) -> str:
    unescaped = html.unescape(text).replace("\xa0", " ")
    lines = [re.sub(r"[ \t\r\f\v]+", " ", line).strip() for line in unescaped.splitlines()]
    return "\n".join(line for line in lines if line)


__all__ = ["FetchResult", "PageFetcher"]
