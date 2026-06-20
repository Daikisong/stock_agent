"""Numeric coercion helpers for bounded diagnostic score channels."""

from __future__ import annotations

import math
from typing import Mapping


_MISSING = object()


def diagnostic_value(value: object, *, invalid_default: float = 0.0) -> float:
    """Return a numeric diagnostic value without letting malformed data crash gates."""

    if isinstance(value, bool):
        return 100.0 if value else 0.0
    try:
        number = float(value)
    except (TypeError, ValueError):
        return float(invalid_default)
    if not math.isfinite(number):
        return float(invalid_default)
    return number


def numeric_diagnostic(
    diagnostics: Mapping[str, object],
    key: str,
    default: float = 0.0,
    *,
    invalid_default: float = 0.0,
) -> float:
    """Read one diagnostic, separating missing values from malformed explicit values."""

    value = diagnostics.get(key, _MISSING)
    if value is _MISSING:
        return float(default)
    return diagnostic_value(value, invalid_default=invalid_default)
