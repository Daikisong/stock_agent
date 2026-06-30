"""KIND/KRX Census v3 source family attempt rows."""

from __future__ import annotations

from . import attempt_row


def collect_kind_krx_attempt(symbol: str, *, has_risk_event: bool = False) -> dict:
    return attempt_row(
        symbol=symbol,
        source_family="KIND/KRX",
        status="RISK_EVENT_PRESENT" if has_risk_event else "LISTING_RISK_CHECKED",
    )


__all__ = ["collect_kind_krx_attempt"]
