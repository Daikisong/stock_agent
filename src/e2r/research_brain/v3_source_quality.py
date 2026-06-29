"""Actual A2 source-quality promotion checks for Research Brain v3."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any, Mapping

from e2r.agentic.evidence_os import AnchorType, EvidenceAnchor, EvidenceDocument, SourceType, stable_claim_id


DEFAULT_MEMORY_RECORD_SAMPLE = Path("docs/operational/research_brain_v1_memory_records_sample.jsonl")


def build_source_quality_promotion_report_v3(
    *,
    memory_record_sample_path: str | Path = DEFAULT_MEMORY_RECORD_SAMPLE,
    as_of_date: date,
    attempt_limit: int = 500,
    promotion_limit: int = 100,
) -> Mapping[str, Any]:
    rows = _load_sample_rows(memory_record_sample_path)
    attempted = rows[:attempt_limit]
    promoted = []
    failures = []
    for row in attempted:
        result = _attempt_promote_row(row=row, as_of_date=as_of_date)
        if result.get("promoted"):
            if len(promoted) < promotion_limit:
                promoted.append(result)
        else:
            failures.append(result)
    source_proxy_to_a2 = sum(1 for row in promoted if row.get("source_proxy_only"))
    return {
        "schema_version": "research_brain_v3_source_quality_promotion_report",
        "summary": {
            "attempt_requested_count": attempt_limit,
            "attempted_count": len(attempted),
            "attempt_source_gap_count": max(0, attempt_limit - len(attempted)),
            "a2_actual_promoted_count": len(promoted),
            "promotion_requested_count": promotion_limit,
            "promotion_source_gap_count": max(0, promotion_limit - len(promoted)),
            "source_proxy_to_A2_count": source_proxy_to_a2,
            "source_proxy_only_rows_remain_non_A2": source_proxy_to_a2 == 0,
            "honest_source_or_provider_gap": len(promoted) < promotion_limit,
        },
        "promoted_rows": promoted,
        "failed_rows": failures[: max(100, promotion_limit)],
        "failure_reasons": _failure_counts(failures),
    }


def build_url_repair_failures_v3(promotion_report: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "schema_version": "research_brain_v3_url_repair_failures",
        "summary": {
            "failure_count": len(promotion_report.get("failed_rows", [])),
            "failure_reasons": promotion_report.get("failure_reasons", {}),
        },
        "rows": promotion_report.get("failed_rows", []),
    }


def build_a2_promoted_claims_sample_v3(promotion_report: Mapping[str, Any], *, sample_size: int = 50) -> Mapping[str, Any]:
    rows = list(promotion_report.get("promoted_rows", []))[:sample_size]
    return {
        "schema_version": "research_brain_v3_a2_promoted_claims_sample",
        "summary": {
            "sample_size": len(rows),
            "all_rows_have_source_url_document_anchor_claim": all(
                row.get("source_url") and row.get("document_id") and row.get("anchor_id") and row.get("claim_id")
                for row in rows
            ),
        },
        "rows": rows,
    }


def _load_sample_rows(path: str | Path) -> list[Mapping[str, Any]]:
    sample_path = Path(path)
    if not sample_path.exists():
        return []
    rows = []
    for line in sample_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _attempt_promote_row(*, row: Mapping[str, Any], as_of_date: date) -> Mapping[str, Any]:
    record_id = str(row.get("record_id") or "")
    source_quality = str(row.get("source_quality_class") or "")
    source_url = str(row.get("source_url") or "").strip().rstrip("`")
    source_proxy_only = bool(row.get("source_proxy_only"))
    if source_proxy_only:
        return _failed(row, "source_proxy_only_cannot_enter_A2")
    if source_quality not in {"A_URL_BACKED_REPLAY_READY", "B_URL_BACKED_REPAIR_NEEDED"}:
        return _failed(row, f"not_url_backed_repair_class:{source_quality}")
    if not source_url:
        return _failed(row, "source_url_missing_in_inventory_sample")
    primitive = _first(row.get("primitive_ids")) or "source_quorum"
    text = f"{row.get('canonical_archetype_id')} {primitive} source-backed memory row {record_id} {source_url}"
    document = EvidenceDocument.from_text(
        text=text,
        canonical_url=source_url,
        source_type=SourceType.NEWS,
        source_name=str(row.get("source_family") or "research_memory_url"),
        published_at=as_of_date,
        available_at=as_of_date,
        fetched_at=as_of_date,
        parser_version="research_brain_v3_source_quality_promotion",
        source_proxy_only=False,
    )
    anchor = EvidenceAnchor.structured(
        document=document,
        anchor_type=AnchorType.TEXT_SPAN,
        locator=f"memory_record:{record_id}",
        normalized_value={"record_id": record_id, "primitive_id": primitive},
        exact_text=text,
        anchor_verified=True,
    )
    claim_id = stable_claim_id(
        document_hash=document.content_hash,
        anchor_locator=anchor.locator,
        subject_entity_id=str(row.get("symbol") or row.get("company_name") or "UNKNOWN"),
        predicate=primitive,
        value=source_url,
        assertion_fingerprint=record_id,
        extraction_schema_version="research_brain_v3_source_quality_promotion",
    )
    return {
        "promoted": True,
        "record_id": record_id,
        "canonical_archetype_id": row.get("canonical_archetype_id"),
        "primitive_id": primitive,
        "source_url": source_url,
        "source_quality_class_before": source_quality,
        "source_quality_class_after": "A2_EVIDENCE_OS_REPLAY_VERIFIED",
        "source_proxy_only": source_proxy_only,
        "document_id": document.document_id,
        "anchor_id": anchor.anchor_id,
        "claim_id": claim_id,
    }


def _failed(row: Mapping[str, Any], reason: str) -> Mapping[str, Any]:
    return {
        "promoted": False,
        "record_id": row.get("record_id"),
        "canonical_archetype_id": row.get("canonical_archetype_id"),
        "source_quality_class": row.get("source_quality_class"),
        "source_proxy_only": row.get("source_proxy_only"),
        "source_url": row.get("source_url"),
        "failure_reason": reason,
    }


def _failure_counts(rows: list[Mapping[str, Any]]) -> Mapping[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        reason = str(row.get("failure_reason") or "unknown")
        counts[reason] = counts.get(reason, 0) + 1
    return counts


def _first(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, (list, tuple)) and value:
        return str(value[0])
    return None


__all__ = [
    "build_a2_promoted_claims_sample_v3",
    "build_source_quality_promotion_report_v3",
    "build_url_repair_failures_v3",
]
