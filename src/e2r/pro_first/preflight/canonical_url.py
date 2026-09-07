"""Deterministic public-document URL canonicalization without web search."""

from __future__ import annotations

from dataclasses import dataclass
import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


TRACKING_QUERY_KEYS = frozenset(
    {
        "fbclid",
        "gclid",
        "mc_cid",
        "mc_eid",
        "ref",
        "referrer",
        "source",
    }
)


@dataclass(frozen=True)
class CanonicalURLResolution:
    original_url: str
    canonical_url: str
    removed_query_keys: tuple[str, ...]
    fragment_removed: bool
    trailing_slash_removed: bool
    redirect_applied: bool

    @property
    def changed(self) -> bool:
        return self.original_url != self.canonical_url


class CanonicalURLResolver:
    def resolve(
        self,
        value: str,
        *,
        final_redirect_url: str | None = None,
    ) -> CanonicalURLResolution:
        original = str(value or "").strip()
        redirect = str(final_redirect_url or "").strip()
        selected = redirect or original
        parsed = urlsplit(selected)
        if (
            parsed.scheme.casefold() not in {"http", "https"}
            or not parsed.hostname
            or parsed.username is not None
            or parsed.password is not None
        ):
            raise ValueError(f"preflight requires a public HTTP(S) URL: {selected!r}")
        scheme = parsed.scheme.casefold()
        hostname = parsed.hostname.casefold()
        port = parsed.port
        if port is not None and not (
            (scheme == "http" and port == 80)
            or (scheme == "https" and port == 443)
        ):
            netloc = f"{hostname}:{port}"
        else:
            netloc = hostname
        removed: list[str] = []
        retained: list[tuple[str, str]] = []
        for key, item in parse_qsl(parsed.query, keep_blank_values=True):
            normalized_key = key.casefold()
            if normalized_key.startswith("utm_") or normalized_key in TRACKING_QUERY_KEYS:
                removed.append(key)
            else:
                retained.append((key, item))
        path = re.sub(r"/{2,}", "/", parsed.path or "/")
        trailing_removed = len(path) > 1 and path.endswith("/")
        if trailing_removed:
            path = path.rstrip("/")
        canonical = urlunsplit(
            (
                scheme,
                netloc,
                path,
                urlencode(sorted(retained), doseq=True),
                "",
            )
        )
        return CanonicalURLResolution(
            original_url=original,
            canonical_url=canonical,
            removed_query_keys=tuple(sorted(set(removed))),
            fragment_removed=bool(parsed.fragment),
            trailing_slash_removed=trailing_removed,
            redirect_applied=bool(redirect and redirect != original),
        )


__all__ = [
    "CanonicalURLResolution",
    "CanonicalURLResolver",
    "TRACKING_QUERY_KEYS",
]
