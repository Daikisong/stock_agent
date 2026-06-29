"""Extraction audit builder for production cutover."""

from __future__ import annotations

from typing import Any, Mapping, Sequence


def build_claim_extraction_audit(
    *,
    v4_extraction_summary: Mapping[str, Any] | None = None,
    accepted_claim_rows: Sequence[Mapping[str, Any]] = (),
    extractor_contract_visible_count: int = 0,
) -> Mapping[str, Any]:
    summary = dict(v4_extraction_summary or {})
    event_summary_used = int(summary.get("event_summary_used_as_exact_quote_count", 0))
    forced_positive = int(summary.get("forced_positive_polarity_count", 0))
    forced_current = int(summary.get("forced_current_temporal_count", 0))
    forced_target = int(summary.get("forced_target_subject_count", 0))
    accepted_without_anchor = sum(1 for row in accepted_claim_rows if not row.get("anchor_id") and not row.get("source_anchor_id"))
    return {
        "schema_version": "production_cutover_claim_extraction_audit_v1",
        "summary": {
            "real_document_to_assertion_count": int(summary.get("real_document_to_raw_assertion_count", 0)),
            "assertion_to_claim_count": int(summary.get("raw_assertion_to_adjudicated_claim_count", 0)),
            "accepted_claim_count": int(summary.get("adjudicated_claim_to_accepted_claim_count", 0)),
            "forced_positive_polarity_count": forced_positive,
            "forced_current_temporal_count": forced_current,
            "forced_target_subject_count": forced_target,
            "event_summary_used_as_exact_quote_count": event_summary_used,
            "primitive_gap_direct_to_mapping_count": int(summary.get("primitive_gap_direct_to_mapping_count", 0)),
            "contract_visible_to_raw_extractor_count": extractor_contract_visible_count,
            "source_field_existence_to_score_without_adjudication_count": int(
                summary.get("source_field_existence_to_score_without_adjudication_count", 0)
            ),
            "accepted_claim_without_anchor_count": accepted_without_anchor,
            "wrong_subject_rejected_count": int(summary.get("wrong_subject_rejected_count", 0)),
            "historical_only_rejected_count": int(summary.get("historical_only_rejected_count", 0)),
        },
    }


__all__ = ["build_claim_extraction_audit"]
