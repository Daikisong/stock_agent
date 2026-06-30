"""Issuer IR/trusted news Census v3 source family attempt rows."""

from __future__ import annotations

from . import attempt_row


def collect_issuer_ir_news_attempt(symbol: str, *, provider_gap: str | None = None) -> dict:
    return attempt_row(
        symbol=symbol,
        source_family="IssuerIR/TrustedNews",
        status="PROVIDER_GAP" if provider_gap else "OPTIONAL_PROVIDER_CHECKED",
        detail={"provider_gap": provider_gap} if provider_gap else {},
    )


__all__ = ["collect_issuer_ir_news_attempt"]
