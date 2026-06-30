"""Source family attempt helpers for Census v3."""

from __future__ import annotations

from typing import Any, Mapping


def attempt_row(*, symbol: str, source_family: str, status: str, detail: Mapping[str, Any] | None = None) -> dict[str, Any]:
    return {
        "symbol": str(symbol).zfill(6),
        "source_family": source_family,
        "attempt_status": status,
        "detail": dict(detail or {}),
    }


__all__ = ["attempt_row"]
