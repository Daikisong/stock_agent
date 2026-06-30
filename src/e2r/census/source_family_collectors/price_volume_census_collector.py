"""Price/volume Census v3 source family attempt rows."""

from __future__ import annotations

from . import attempt_row


def collect_price_volume_attempt(symbol: str, *, has_market_anomaly: bool = False) -> dict:
    return attempt_row(
        symbol=symbol,
        source_family="PriceVolume",
        status="MARKET_ANOMALY_PRESENT" if has_market_anomaly else "PRICE_VOLUME_CHECKED",
    )


__all__ = ["collect_price_volume_attempt"]
