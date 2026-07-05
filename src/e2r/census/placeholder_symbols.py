"""Shared placeholder-symbol helpers for Census/Goal4 audits."""

from __future__ import annotations

from typing import Any


PLACEHOLDER_SYMBOLS = {
    "",
    "000000",
    "0000000",
    "UNKNOWN",
    "N/A",
    "NONE",
    "NULL",
}


def is_placeholder_symbol(value: Any) -> bool:
    text = str(value or "").strip().upper()
    if len(text) in {6, 7} and len(set(text)) == 1 and text.isdigit():
        return True
    return text in PLACEHOLDER_SYMBOLS


def normalized_real_symbol(value: Any) -> str:
    text = str(value or "").strip()
    if is_placeholder_symbol(text):
        return ""
    return text.zfill(6)


__all__ = ["PLACEHOLDER_SYMBOLS", "is_placeholder_symbol", "normalized_real_symbol"]
