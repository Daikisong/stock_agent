"""Stable evidence identifier helpers."""

from __future__ import annotations

import hashlib
import re
from datetime import date


def stable_text_hash(*parts: object, length: int = 12) -> str:
    """Return a short deterministic hash for evidence identifiers."""

    text = "\x1f".join(str(part or "").strip() for part in parts)
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:length]


def stable_news_evidence_id(
    *,
    symbol: str | None,
    published_date: date,
    source: str | None,
    source_url: str | None = None,
    title: str | None = None,
    prefix: str = "news",
) -> str:
    """Build a stable news evidence id without using process-random ``hash()``."""

    symbol_key = (symbol or "UNKNOWN").strip() or "UNKNOWN"
    source_key = (source or "unknown-source").strip() or "unknown-source"
    suffix = stable_text_hash(symbol_key, published_date.isoformat(), source_key, source_url, title)
    return f"{prefix}:{symbol_key}:{published_date.isoformat()}:{source_key}:{suffix}"


def stable_estimate_source_key(source: str | None) -> str:
    """Return an id-safe source key for consensus and revision evidence."""

    raw = (source or "unknown-source").strip() or "unknown-source"
    normalized = re.sub(r"[^A-Za-z0-9_.-]+", "_", raw).strip("_.-")
    if not normalized:
        normalized = "source"
    if normalized != raw or len(normalized) > 48:
        normalized = f"{normalized[:40].strip('_.-') or 'source'}_{stable_text_hash(raw, length=8)}"
    return normalized


def stable_consensus_evidence_id(
    *,
    symbol: str,
    estimate_date: date,
    fiscal_year: int,
    source: str | None,
) -> str:
    """Build a source-aware consensus evidence id."""

    symbol_key = (symbol or "UNKNOWN").strip() or "UNKNOWN"
    return f"consensus:{symbol_key}:{estimate_date.isoformat()}:{fiscal_year}:{stable_estimate_source_key(source)}"


def stable_revision_evidence_id(
    *,
    symbol: str,
    estimate_date: date,
    fiscal_year: int,
    source: str | None,
) -> str:
    """Build a source-aware consensus revision evidence id."""

    symbol_key = (symbol or "UNKNOWN").strip() or "UNKNOWN"
    return f"revision:{symbol_key}:{estimate_date.isoformat()}:{fiscal_year}:{stable_estimate_source_key(source)}"


__all__ = [
    "stable_consensus_evidence_id",
    "stable_estimate_source_key",
    "stable_news_evidence_id",
    "stable_revision_evidence_id",
    "stable_text_hash",
]
