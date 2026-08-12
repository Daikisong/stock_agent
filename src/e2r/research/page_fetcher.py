"""Fixture-first page fetcher for web research."""

from __future__ import annotations

import hashlib
import html
import json
import re
import socket
import ssl
import warnings
from dataclasses import dataclass
from datetime import date, datetime
from email.message import Message
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib import error, parse, request
from typing import Any, Mapping

import certifi
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.utils import CryptographyDeprecationWarning
from cryptography.x509.oid import (
    AuthorityInformationAccessOID,
    ExtensionOID,
)
from cryptography.x509.verification import DNSName, PolicyBuilder, Store

from e2r.research.pdf_text_extractor import (
    PDF_TEXT_EXTRACTION_SEMANTICS_VERSION,
    PDFTextExtractor,
    extracted_text_unreadable_reason,
)


PUBLICATION_METADATA_SEMANTICS_VERSION = (
    "e2r_page_fetch_publication_metadata_v1"
)
TEXT_CACHE_SEMANTICS_VERSION = "e2r_page_fetch_text_cache_v2"
RESPONSE_CONTENT_CLASSIFICATION_SEMANTICS_VERSION = (
    "e2r_page_fetch_response_content_classification_v2"
)
TLS_AIA_INTERMEDIATE_RECOVERY_SEMANTICS_VERSION = (
    "e2r_page_fetch_tls_aia_intermediate_recovery_v1"
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
    publication_metadata_parts: tuple[str, ...] = ()
    publication_metadata_semantics_version: str | None = None
    text_complete: bool = True
    original_text_chars: int | None = None
    returned_text_chars: int | None = None
    text_cache_semantics_version: str | None = None
    text_extraction_semantics_version: str | None = None


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
    max_text_chars: int | None = 200_000
    user_agent: str = "Mozilla/5.0 E2R-ResearcherMode/5.0"

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
                    cached_content_type = str(
                        cache_metadata.get("content_type") or "text/plain"
                    )
                    current_text_cache = (
                        cache_metadata.get("text_cache_semantics_version")
                        == TEXT_CACHE_SEMANTICS_VERSION
                    )
                    legacy_uncapped_cache = (
                        not cache_metadata.get("text_cache_semantics_version")
                        and len(cached_text) < 200_000
                    )
                    pdf_semantics_current = (
                        "pdf" not in cached_content_type.casefold()
                        or cache_metadata.get(
                            "text_extraction_semantics_version"
                        )
                        == PDF_TEXT_EXTRACTION_SEMANTICS_VERSION
                    )
                    if (
                        cache_metadata.get(
                            "publication_metadata_semantics_version"
                        )
                        == PUBLICATION_METADATA_SEMANTICS_VERSION
                        and (current_text_cache or legacy_uncapped_cache)
                        and pdf_semantics_current
                    ):
                        returned_text, text_complete = _bounded_text(
                            cached_text,
                            self.max_text_chars,
                        )
                        return FetchResult(
                            url=url,
                            ok=True,
                            text=returned_text,
                            content_type=cached_content_type,
                            fetched_at=fetched_at,
                            source_path=str(cache_path),
                            referenced_urls=tuple(
                                str(value)
                                for value in cache_metadata.get(
                                    "referenced_urls", ()
                                )
                                if str(value).strip()
                            ),
                            response_last_modified_at=_cached_datetime(
                                cache_metadata.get("response_last_modified_at")
                            ),
                            publication_metadata_parts=tuple(
                                str(value)
                                for value in cache_metadata.get(
                                    "publication_metadata_parts", ()
                                )
                                if str(value).strip()
                            ),
                            publication_metadata_semantics_version=(
                                PUBLICATION_METADATA_SEMANTICS_VERSION
                            ),
                            text_complete=text_complete,
                            original_text_chars=len(cached_text),
                            returned_text_chars=len(returned_text),
                            text_cache_semantics_version=(
                                TEXT_CACHE_SEMANTICS_VERSION
                            ),
                            text_extraction_semantics_version=(
                                str(
                                    cache_metadata.get(
                                        "text_extraction_semantics_version"
                                    )
                                    or ""
                                )
                                or None
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
            with _urlopen_with_verified_aia_intermediate_recovery(
                req,
                timeout=self.timeout_seconds,
            ) as response:
                content_type = _content_type(response)
                content_disposition_filename = (
                    _content_disposition_filename(response)
                )
                response_last_modified_at = _response_last_modified_at(response)
                declared_pdf_like = _looks_like_pdf_response(
                    url=url,
                    content_type=content_type,
                    content_disposition_filename=(
                        content_disposition_filename
                    ),
                )
                body, pdf_like, body_limit = _read_bounded_response_body(
                    response,
                    declared_pdf_like=declared_pdf_like,
                    content_type=content_type,
                    max_body_bytes=self.max_body_bytes,
                    max_pdf_body_bytes=self.max_pdf_body_bytes,
                )
                if len(body) > body_limit:
                    return FetchResult(
                        url=url,
                        ok=False,
                        content_type=(
                            content_type or (
                                "application/pdf" if pdf_like else "text/html"
                            )
                        ),
                        fetched_at=fetched_at,
                        reason=(
                            "live_fetch_body_too_large:"
                            f"{'pdf' if pdf_like else 'html'}:{body_limit}"
                        ),
                        text_complete=False,
                        original_text_chars=None,
                        returned_text_chars=0,
                        text_cache_semantics_version=(
                            TEXT_CACHE_SEMANTICS_VERSION
                        ),
                    )
                charset = _charset(response) or "utf-8"
        except (error.HTTPError, error.URLError, TimeoutError, OSError, UnicodeError, ValueError) as exc:
            return FetchResult(
                url=url,
                ok=False,
                fetched_at=fetched_at,
                reason=f"live_fetch_failed:{type(exc).__name__}:{exc}",
            )

        if pdf_like:
            effective_content_type = (
                content_type
                if "pdf" in content_type.casefold()
                else "application/pdf"
            )
            extraction = (self.pdf_text_extractor or PDFTextExtractor()).extract_text_from_bytes(body)
            if not extraction.ok or not (extraction.text or "").strip():
                reason = extraction.reason or "empty_pdf_text"
                return FetchResult(
                    url=url,
                    ok=False,
                    content_type=effective_content_type,
                    fetched_at=fetched_at,
                    reason=f"live_pdf_text_extraction_failed:{reason}",
                )
            unreadable = extracted_text_unreadable_reason(extraction.text or "")
            if unreadable is not None:
                return FetchResult(
                    url=url,
                    ok=False,
                    content_type=effective_content_type,
                    fetched_at=fetched_at,
                    reason=f"live_pdf_text_extraction_failed:{unreadable}",
                )
            full_text = extraction.text or ""
            extraction_semantics_version = (
                extraction.extraction_semantics_version
                or PDF_TEXT_EXTRACTION_SEMANTICS_VERSION
            )
            text, text_complete = _bounded_text(
                full_text,
                self.max_text_chars,
            )
            source_path = _write_cache(
                cache_path,
                full_text,
                content_type=effective_content_type,
                response_last_modified_at=response_last_modified_at,
                text_extraction_semantics_version=(
                    extraction_semantics_version
                ),
            )
            return FetchResult(
                url=url,
                ok=True,
                text=text,
                content_type=effective_content_type,
                fetched_at=fetched_at,
                source_path=source_path,
                response_last_modified_at=response_last_modified_at,
                publication_metadata_semantics_version=(
                    PUBLICATION_METADATA_SEMANTICS_VERSION
                ),
                text_complete=text_complete,
                original_text_chars=len(full_text),
                returned_text_chars=len(text),
                text_cache_semantics_version=TEXT_CACHE_SEMANTICS_VERSION,
                text_extraction_semantics_version=(
                    extraction_semantics_version
                ),
            )

        decoded = body.decode(charset, errors="replace")
        publication_metadata_parts: tuple[str, ...] = ()
        if "html" in content_type.lower() or _looks_like_html(decoded):
            text, referenced_urls = _html_text_and_references(
                decoded,
                base_url=url,
            )
            publication_metadata_parts = _html_publication_metadata_parts(
                decoded
            )
        else:
            text = _normalize_text(decoded)
            referenced_urls = ()
        unreadable = extracted_text_unreadable_reason(text)
        if unreadable is not None:
            return FetchResult(
                url=url,
                ok=False,
                text=text,
                content_type=content_type,
                fetched_at=fetched_at,
                reason=f"live_fetch_unreadable_text:{unreadable}",
                referenced_urls=referenced_urls,
                response_last_modified_at=response_last_modified_at,
            )
        full_text = text
        text, text_complete = _bounded_text(
            full_text,
            self.max_text_chars,
        )
        source_path = _write_cache(
            cache_path,
            full_text,
            content_type=content_type,
            referenced_urls=referenced_urls,
            response_last_modified_at=response_last_modified_at,
            publication_metadata_parts=publication_metadata_parts,
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
            publication_metadata_parts=publication_metadata_parts,
            publication_metadata_semantics_version=(
                PUBLICATION_METADATA_SEMANTICS_VERSION
            ),
            text_complete=text_complete,
            original_text_chars=len(full_text),
            returned_text_chars=len(text),
            text_cache_semantics_version=TEXT_CACHE_SEMANTICS_VERSION,
        )


def _path_exists(value: str) -> bool:
    try:
        return Path(value).exists()
    except OSError:
        return False


def _urlopen_with_verified_aia_intermediate_recovery(
    req: request.Request,
    *,
    timeout: float,
):
    """Open HTTPS once more when a server omitted its intermediate CA.

    Some otherwise valid publisher sites send only the leaf certificate.  A
    normal TLS client then fails with ``unable to get local issuer
    certificate`` even though the leaf advertises its intermediate through
    the standard Authority Information Access (AIA) extension.

    This recovery never disables verification for document transport.  It
    uses an unverified handshake only to read the public leaf certificate,
    downloads the advertised CA certificate, verifies leaf + intermediate +
    DNS name against the normal certifi root store, and only then repeats the
    HTTP request with a verifying ``SSLContext``.  Any ambiguity falls back to
    the original fail-closed TLS error.
    """

    try:
        return request.urlopen(req, timeout=timeout)
    except error.URLError as original_error:
        if not _is_missing_intermediate_tls_error(original_error):
            raise
        try:
            context = _verified_aia_intermediate_context(
                req.full_url,
                timeout=timeout,
            )
            return request.urlopen(
                req,
                timeout=timeout,
                context=context,
            )
        except Exception:
            # Preserve the stable provider failure taxonomy.  Recovery is a
            # bounded compatibility path, not permission to replace a TLS
            # verification failure with an unrelated parser/network error.
            raise original_error


def _is_missing_intermediate_tls_error(exc: BaseException) -> bool:
    parts: list[str] = []
    current: BaseException | None = exc
    visited: set[int] = set()
    while current is not None and id(current) not in visited:
        visited.add(id(current))
        parts.append(str(current).casefold())
        reason = getattr(current, "reason", None)
        current = reason if isinstance(reason, BaseException) else current.__cause__
    detail = " ".join(parts)
    return bool(
        "certificate_verify_failed" in detail
        and "unable to get local issuer certificate" in detail
    )


def _verified_aia_intermediate_context(
    url: str,
    *,
    timeout: float,
) -> ssl.SSLContext:
    parsed = parse.urlparse(url)
    host = str(parsed.hostname or "")
    if parsed.scheme != "https" or not host:
        raise ValueError("AIA TLS recovery requires an HTTPS hostname")
    port = int(parsed.port or 443)

    # This socket reads only the peer's public leaf certificate.  No HTTP
    # request or evidence bytes travel through the unverified connection.
    probe_context = ssl._create_unverified_context()  # noqa: SLF001
    with socket.create_connection((host, port), timeout=timeout) as raw_socket:
        with probe_context.wrap_socket(
            raw_socket,
            server_hostname=host,
        ) as tls_socket:
            leaf_der = tls_socket.getpeercert(binary_form=True)
    if not leaf_der:
        raise ssl.SSLCertVerificationError("peer did not provide a leaf certificate")
    leaf = x509.load_der_x509_certificate(leaf_der)

    aia = leaf.extensions.get_extension_for_oid(
        ExtensionOID.AUTHORITY_INFORMATION_ACCESS
    ).value
    issuer_urls = tuple(
        str(description.access_location.value)
        for description in aia
        if description.access_method == AuthorityInformationAccessOID.CA_ISSUERS
        and str(description.access_location.value).startswith(("http://", "https://"))
    )
    if not issuer_urls:
        raise ssl.SSLCertVerificationError("leaf has no HTTP AIA CA issuer URL")

    intermediates: list[x509.Certificate] = []
    for issuer_url in issuer_urls[:3]:
        issuer_request = request.Request(
            issuer_url,
            headers={"User-Agent": "Mozilla/5.0 E2R-TLS-AIA-Recovery/1.0"},
            method="GET",
        )
        with request.urlopen(issuer_request, timeout=timeout) as response:
            issuer_bytes = response.read(1_000_001)
        if len(issuer_bytes) > 1_000_000:
            raise ValueError("AIA issuer certificate exceeds 1 MB")
        try:
            intermediate = x509.load_der_x509_certificate(issuer_bytes)
        except ValueError:
            intermediate = x509.load_pem_x509_certificate(issuer_bytes)
        intermediates.append(intermediate)

    # The public Mozilla bundle can contain a grandfathered legacy root with
    # a non-positive serial.  It remains an OpenSSL trust-store input today;
    # suppress only that library deprecation while parsing the complete bundle.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", CryptographyDeprecationWarning)
        root_certificates = x509.load_pem_x509_certificates(
            Path(certifi.where()).read_bytes()
        )
    if not root_certificates:
        raise ssl.SSLCertVerificationError("trusted root store is empty")
    verifier = (
        PolicyBuilder()
        .store(Store(root_certificates))
        .build_server_verifier(DNSName(host))
    )
    verifier.verify(leaf, intermediates)

    verified_context = ssl.create_default_context(cafile=certifi.where())
    verified_context.load_verify_locations(
        cadata="\n".join(
            certificate.public_bytes(serialization.Encoding.PEM).decode("ascii")
            for certificate in intermediates
        )
    )
    return verified_context


def _http_request_url(url: str) -> str:
    parts = parse.urlsplit(url)
    netloc = parts.netloc.encode("idna").decode("ascii") if parts.netloc else ""
    path = parse.quote(parts.path or "/", safe="/%:@&+$,;=-_.!~*'()")
    query = parse.quote(parts.query, safe="=&?/:;+,%@-._~!$'()*[]")
    return parse.urlunsplit((parts.scheme, netloc, path, query, ""))


def _looks_like_pdf_url(url: str) -> bool:
    lowered = url.lower()
    return parse.urlparse(lowered).path.endswith(".pdf") or ".pdf?" in lowered


def _looks_like_pdf_response(
    *,
    url: str,
    content_type: str,
    content_disposition_filename: str | None,
) -> bool:
    if _looks_like_pdf_url(url) or "pdf" in content_type.casefold():
        return True
    return bool(
        content_disposition_filename
        and content_disposition_filename.casefold().endswith(".pdf")
    )


def _body_looks_like_pdf(body: bytes) -> bool:
    marker_index = body[:1024].find(b"%PDF-")
    return marker_index >= 0


def _content_type_allows_pdf_magic(content_type: str) -> bool:
    media_type = content_type.partition(";")[0].strip().casefold()
    return media_type in {
        "",
        "application/download",
        "application/octet-stream",
        "application/x-download",
        "binary/octet-stream",
    }


def _read_bounded_response_body(
    response: object,
    *,
    declared_pdf_like: bool,
    content_type: str,
    max_body_bytes: int,
    max_pdf_body_bytes: int,
) -> tuple[bytes, bool, int]:
    html_limit = max(1, max_body_bytes)
    pdf_limit = max(1, max_pdf_body_bytes)
    reader = getattr(response, "read")
    if declared_pdf_like:
        return _read_up_to(reader, pdf_limit + 1), True, pdf_limit
    if not _content_type_allows_pdf_magic(content_type):
        return _read_up_to(reader, html_limit + 1), False, html_limit

    probe_limit = min(1024, max(html_limit, pdf_limit) + 1)
    prefix = _read_up_to(reader, probe_limit)
    pdf_like = _body_looks_like_pdf(prefix)
    body_limit = pdf_limit if pdf_like else html_limit
    remaining_limit = body_limit + 1 - len(prefix)
    if remaining_limit <= 0:
        return prefix, pdf_like, body_limit
    return (
        prefix + _read_up_to(reader, remaining_limit),
        pdf_like,
        body_limit,
    )


def _read_up_to(reader: Any, limit: int) -> bytes:
    chunks: list[bytes] = []
    remaining = max(0, limit)
    while remaining:
        chunk = reader(remaining)
        if not chunk:
            break
        value = bytes(chunk)
        if len(value) > remaining:
            raise ValueError(
                "response_reader_exceeded_requested_byte_count:"
                f"{len(value)}>{remaining}"
            )
        chunks.append(value)
        remaining -= len(value)
    return b"".join(chunks)


def _cache_path(cache_directory: str | Path | None, url: str, as_of_date: date) -> Path | None:
    if cache_directory is None:
        return None
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()
    return Path(cache_directory) / as_of_date.isoformat() / f"{digest}.txt"


def _write_cache(
    cache_path: Path | None,
    text: str,
    *,
    content_type: str = "text/plain",
    referenced_urls: tuple[str, ...] = (),
    response_last_modified_at: datetime | None = None,
    publication_metadata_parts: tuple[str, ...] = (),
    text_extraction_semantics_version: str | None = None,
) -> str | None:
    if cache_path is None:
        return None
    try:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(text, encoding="utf-8")
        _cache_metadata_path(cache_path).write_text(
            json.dumps(
                {
                    "content_type": content_type,
                    "referenced_urls": list(referenced_urls),
                    "response_last_modified_at": (
                        response_last_modified_at.isoformat()
                        if response_last_modified_at is not None
                        else None
                    ),
                    "publication_metadata_parts": list(
                        publication_metadata_parts
                    ),
                    "publication_metadata_semantics_version": (
                        PUBLICATION_METADATA_SEMANTICS_VERSION
                    ),
                    "text_cache_semantics_version": (
                        TEXT_CACHE_SEMANTICS_VERSION
                    ),
                    "text_complete": True,
                    "original_text_chars": len(text),
                    "text_extraction_semantics_version": (
                        text_extraction_semantics_version
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


def _bounded_text(text: str, maximum_chars: int | None) -> tuple[str, bool]:
    if maximum_chars is None:
        return text, True
    if isinstance(maximum_chars, bool) or maximum_chars <= 0:
        raise ValueError("max_text_chars must be a positive integer or None")
    if len(text) <= maximum_chars:
        return text, True
    return text[:maximum_chars], False


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


def _content_disposition_filename(response: object) -> str | None:
    headers = getattr(response, "headers", None)
    if headers is None or not hasattr(headers, "get"):
        return None
    value = headers.get("Content-Disposition") or headers.get(
        "content-disposition"
    )
    if not value:
        return None
    message = Message()
    message["Content-Disposition"] = str(value)
    filename = message.get_filename()
    return str(filename).strip() if filename else None


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


def _html_publication_metadata_parts(decoded: str) -> tuple[str, ...]:
    parser = _HTMLPublicationMetadataExtractor()
    parser.feed(decoded)
    parser.close()
    return parser.publication_metadata_parts()


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
        if tag in {"a", "frame", "iframe", "source"}:
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


class _HTMLPublicationMetadataExtractor(HTMLParser):
    """Collect document-level publication metadata without body-date guessing."""

    _META_KEYS = {
        "articlepublishedtime",
        "date",
        "datepublished",
        "pubdate",
        "publishdate",
    }
    _SINGLE_BODY_CLASSES = {"single", "single-post", "singular"}
    _PUBLISHED_ARTICLE_CLASSES = {"hentry", "status-publish"}
    _DATE_CLASSES = {"date", "entry-date", "post-date", "published"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._parts: list[str] = []
        self._single_document_body = False
        self._article_selected = False
        self._article_depth = 0
        self._date_capture_tag: str | None = None
        self._date_capture_parts: list[str] = []
        self._json_ld_parts: list[str] | None = None

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        tag = tag.lower()
        attrs_by_name = {
            key.lower(): str(value)
            for key, value in attrs
            if key and value is not None
        }
        if tag == "script" and (
            attrs_by_name.get("type", "").split(";", 1)[0].strip().lower()
            == "application/ld+json"
        ):
            self._json_ld_parts = []
            return
        if tag == "meta":
            key = (
                attrs_by_name.get("property")
                or attrs_by_name.get("name")
                or attrs_by_name.get("itemprop")
                or ""
            )
            content = attrs_by_name.get("content", "").strip()
            normalized_key = re.sub(r"[^a-z0-9]", "", key.casefold())
            if normalized_key in self._META_KEYS and content:
                self._parts.append(f"HTML_META_{normalized_key}:{content}")
            return
        class_tokens = {
            value.casefold()
            for value in attrs_by_name.get("class", "").split()
            if value.strip()
        }
        if tag == "body":
            self._single_document_body = bool(
                class_tokens & self._SINGLE_BODY_CLASSES
                or any(value.startswith("single-") for value in class_tokens)
            )
        if tag == "article":
            if self._article_depth:
                self._article_depth += 1
            elif (
                self._single_document_body
                and not self._article_selected
                and class_tokens & self._PUBLISHED_ARTICLE_CLASSES
            ):
                self._article_selected = True
                self._article_depth = 1
        if not self._article_depth:
            return
        if tag == "time":
            value = attrs_by_name.get("datetime", "").strip()
            if value:
                self._parts.append(f"SINGLE_ARTICLE_TIME:{value}")
        if (
            self._date_capture_tag is None
            and class_tokens & self._DATE_CLASSES
        ):
            self._date_capture_tag = tag
            self._date_capture_parts = []

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "script" and self._json_ld_parts is not None:
            self._parts.extend(
                _json_ld_publication_metadata_parts(
                    "".join(self._json_ld_parts)
                )
            )
            self._json_ld_parts = None
        if tag == self._date_capture_tag:
            value = " ".join(self._date_capture_parts).strip()
            if value:
                self._parts.append(f"SINGLE_ARTICLE_DATE:{value}")
            self._date_capture_tag = None
            self._date_capture_parts = []
        if tag == "article" and self._article_depth:
            self._article_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._json_ld_parts is not None:
            self._json_ld_parts.append(data)
        elif self._date_capture_tag is not None and data.strip():
            self._date_capture_parts.append(data.strip())

    def publication_metadata_parts(self) -> tuple[str, ...]:
        return tuple(dict.fromkeys(value for value in self._parts if value))


def _json_ld_publication_metadata_parts(payload: str) -> tuple[str, ...]:
    values: list[str] = []
    try:
        decoded = json.loads(payload)
    except json.JSONDecodeError:
        for match in re.finditer(
            r'(?i)["\']datePublished["\']\s*:\s*["\']([^"\']+)',
            payload,
        ):
            values.append(match.group(1).strip())
    else:
        pending = [decoded]
        while pending:
            value = pending.pop()
            if isinstance(value, Mapping):
                for key, nested in value.items():
                    if re.sub(r"[^a-z0-9]", "", str(key).casefold()) == (
                        "datepublished"
                    ):
                        if isinstance(nested, (str, int, float)):
                            values.append(str(nested).strip())
                    elif isinstance(nested, (Mapping, list, tuple)):
                        pending.append(nested)
            elif isinstance(value, (list, tuple)):
                pending.extend(value)
    return tuple(
        f"JSON_LD_DATE_PUBLISHED:{value}"
        for value in dict.fromkeys(values)
        if value
    )


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


__all__ = [
    "FetchResult",
    "PUBLICATION_METADATA_SEMANTICS_VERSION",
    "RESPONSE_CONTENT_CLASSIFICATION_SEMANTICS_VERSION",
    "TEXT_CACHE_SEMANTICS_VERSION",
    "PageFetcher",
]
