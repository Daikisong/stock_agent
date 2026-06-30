"""Baseline classification helpers."""

from __future__ import annotations

from .schemas import BaselineScanResult


def baseline_reason_category(scan: BaselineScanResult) -> str:
    if scan.has_provider_failure:
        return "PROVIDER_PENDING"
    if scan.has_current_event:
        return "CURRENT_EVENT"
    if scan.market_only_signal:
        return "MARKET_ANOMALY_ONLY"
    return "NO_CURRENT_CATALYST"


__all__ = ["baseline_reason_category"]
