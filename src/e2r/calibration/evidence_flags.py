"""Shared V12 evidence-quality flag detection."""

from __future__ import annotations

from typing import Any


EVIDENCE_URL_PENDING_TERMS = (
    "evidence url pending",
    "url pending",
    "urls pending",
    "pending_url_repair",
    "pending url repair",
    "url repair pending",
    "url repair deferred",
    "verified url repair pending",
    "exact report/news url hardening deferred",
    "report/news url hardening deferred",
    "url hardening deferred",
    "attach ids later",
    "attach ids deferred",
)

SOURCE_PROXY_ONLY_TERMS = (
    "source_proxy_only",
    "source proxy only",
    "source-name-level",
    "source name level",
    "historical public-event proxy",
    "historical public-event proxies",
    "historical public event proxy",
    "historical public event proxies",
    "public-event proxy",
    "public-event proxies",
    "public event proxy",
    "public event proxies",
    "event proxies",
    "public report proxy",
    "public disclosure / policy-event proxy",
    "policy-event proxy",
    "public quarterly disclosure / earnings-call proxy",
    "quarterly disclosure / earnings-call proxy",
    "historical public disclosure / policy-event proxy",
    "historical public event/research proxy",
    "historical public event / research proxy",
    "historical public disclosure/report narrative proxy",
    "historical company/news/proxy",
    "historical analyst-note proxy",
    "public market/report narrative proxy",
    "point-in-time research proxy",
    "report narrative proxy",
    "analyst-note proxy",
    "proxy without direct",
)

SOURCE_PROXY_FIELD_KEYS = (
    "evidence_source",
    "evidence_available_at_that_date",
)


def _parse_bool(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if value is None:
        return None
    text = str(value).strip().lower()
    if text in {"true", "yes", "y", "1", "pass"}:
        return True
    if text in {"false", "no", "n", "0", "fail"}:
        return False
    return None


def _values_text(row: dict[str, Any]) -> str:
    return " ".join(str(value) for value in row.values()).lower()


def _field_text(row: dict[str, Any], keys: tuple[str, ...]) -> str:
    return " ".join(str(row.get(key) or "") for key in keys).lower()


def text_has_evidence_url_pending(text: str) -> bool:
    lower = str(text or "").lower()
    return any(term in lower for term in EVIDENCE_URL_PENDING_TERMS)


def text_has_source_proxy_only(text: str) -> bool:
    lower = str(text or "").lower()
    return any(term in lower for term in SOURCE_PROXY_ONLY_TERMS)


def row_has_source_proxy_context(row: dict[str, Any]) -> bool:
    source_text = str(row.get("evidence_source") or "").lower()
    if "proxy" in source_text and "consensus_proxy" not in source_text:
        return True
    return text_has_source_proxy_only(_field_text(row, SOURCE_PROXY_FIELD_KEYS))


def normalise_evidence_quality_flags(row: dict[str, Any]) -> dict[str, Any]:
    """Return a copy with source-proxy and URL-pending markers normalized.

    Textual markers are treated as authoritative. This prevents rows such as
    ``source_proxy_only=False`` plus ``evidence_source=source_proxy_only_*``
    from being counted as clean support.
    """

    normalised = dict(row)
    text = _values_text(normalised)
    explicit_url_pending = _parse_bool(normalised.get("evidence_url_pending")) is True
    explicit_source_proxy = _parse_bool(normalised.get("source_proxy_only")) is True
    normalised["evidence_url_pending"] = explicit_url_pending or text_has_evidence_url_pending(text)
    normalised["source_proxy_only"] = explicit_source_proxy or text_has_source_proxy_only(text) or row_has_source_proxy_context(normalised)
    return normalised
