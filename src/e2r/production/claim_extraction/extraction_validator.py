"""Validation helpers for v2 LLM raw assertion output."""

from __future__ import annotations

from typing import Mapping, Sequence

from .anchor_validator import validate_anchor
from .contract_blind_extractor import RawAssertionRecord


_FORBIDDEN_OUTPUT_KEYS = {
    "score",
    "stage",
    "primitive_id",
    "hard_break",
    "current_score_eligible",
    "verified",
}


def count_forbidden_extractor_output_keys(value: object) -> int:
    if isinstance(value, Mapping):
        return sum(1 for key in value if str(key) in _FORBIDDEN_OUTPUT_KEYS) + sum(
            count_forbidden_extractor_output_keys(item) for item in value.values()
        )
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return sum(count_forbidden_extractor_output_keys(item) for item in value)
    return 0


def assertion_anchor_validated(
    assertion: RawAssertionRecord,
    *,
    document_text: str,
    anchor_type: str,
    locator: str | None,
) -> bool:
    return validate_anchor(
        exact_quote=assertion.exact_quote,
        document_text=document_text,
        locator=locator,
        anchor_type=anchor_type,
    ).valid


__all__ = ["assertion_anchor_validated", "count_forbidden_extractor_output_keys"]
