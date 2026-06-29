"""Anchor validation for production claim extraction."""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class AnchorValidationResult:
    valid: bool
    reason: str
    anchor_type: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def validate_anchor(*, exact_quote: str | None, document_text: str | None, locator: str | None, anchor_type: str) -> AnchorValidationResult:
    if anchor_type in {"API_RECORD", "TABLE_CELL", "XBRL_FACT", "PDF_PAGE_REGION"} and locator:
        return AnchorValidationResult(valid=True, reason="structured_locator_present", anchor_type=anchor_type)
    if not exact_quote or not document_text:
        return AnchorValidationResult(valid=False, reason="missing_quote_or_document_text", anchor_type=anchor_type)
    if exact_quote.strip() not in document_text:
        return AnchorValidationResult(valid=False, reason="quote_not_found_in_document_text", anchor_type=anchor_type)
    return AnchorValidationResult(valid=True, reason="quote_span_verified", anchor_type=anchor_type)


__all__ = ["AnchorValidationResult", "validate_anchor"]
