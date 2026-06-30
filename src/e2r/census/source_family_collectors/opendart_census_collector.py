"""OpenDART Census v3 source family attempt rows."""

from __future__ import annotations

from . import attempt_row


def collect_opendart_attempt(symbol: str, *, has_leaf_event: bool = False) -> dict:
    return attempt_row(
        symbol=symbol,
        source_family="OpenDART",
        status="LEAF_EVENT_PRESENT" if has_leaf_event else "INDEX_CHECKED_NO_CURRENT_ACCEPTED_CLAIM",
    )


__all__ = ["collect_opendart_attempt"]
