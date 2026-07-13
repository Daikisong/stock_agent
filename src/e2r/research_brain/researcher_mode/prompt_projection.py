"""Loss-accounted prompt projections for already-validated research artifacts.

Fact extraction is the only phase that needs full document bodies.  Later LLM
passes consume verified facts, exact accepted quotes, document manifests, and
deterministic summaries of every structured record.  The complete artifacts
remain on disk; these projections are prompt-transport representations, never
research-completion caps or score authorities.
"""

from __future__ import annotations

import hashlib
import json
import math
from statistics import median
from typing import Any, Mapping, Sequence


_DOCUMENT_MANIFEST_FIELDS = (
    "schema_version",
    "document_id",
    "full_source_document_id",
    "target_id",
    "as_of_date",
    "canonical_url",
    "discovery_urls",
    "title",
    "source_family",
    "source_provider",
    "published_at",
    "available_at",
    "fetched_at",
    "content_type",
    "content_hash",
    "full_source_content_hash",
    "full_source_text_chars",
    "chunk_index",
    "chunk_count",
    "all_chunks_preserved",
    "query_ids",
    "objective_ids",
    "source_independence_group",
    "referenced_urls",
    "referenced_document_ids",
    "full_fetch_performed",
    "full_source_fetch_performed",
    "snippet_only",
    "snippet_used_as_document",
    "evidence_eligible",
)


def project_source_documents(
    rows: Sequence[Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    """Keep every document identity/date/hash while removing duplicate bodies."""

    output = []
    for raw in rows:
        row = dict(raw)
        content = str(
            row.get("content_text")
            or row.get("full_text")
            or row.get("content")
            or ""
        )
        projected = {
            key: row[key] for key in _DOCUMENT_MANIFEST_FIELDS if key in row
        }
        projected.update(
            {
                "content_transport": "OMITTED_AFTER_VERIFIED_FACT_EXTRACTION",
                "content_chars": len(content),
                "content_hash_recomputed": (
                    hashlib.sha256(content.encode("utf-8")).hexdigest()
                    if content
                    else None
                ),
                "exact_quotes_available_in_source_claims": True,
                "prompt_projection_is_research_cap": False,
                "production_score_authority": False,
            }
        )
        output.append(projected)
    return tuple(output)


def project_source_graph_checkpoint(
    checkpoint: Mapping[str, Any], *, keys: Sequence[str]
) -> Mapping[str, Any]:
    output = {key: checkpoint.get(key) for key in keys if key in checkpoint}
    if "evidence_documents" in output:
        documents = tuple(output.get("evidence_documents") or ())
        output["evidence_documents"] = list(project_source_documents(documents))
        output["evidence_document_count"] = len(documents)
        output["evidence_document_manifest_hash"] = _stable_hash(documents)
        output["full_document_bodies_omitted_after_fact_extraction"] = True
    return output


def project_structured_records(
    records: Sequence[Any],
) -> Mapping[str, Any]:
    """Summarize all rows by semantic series and hash the complete roster."""

    payloads = tuple(_record_dict(row) for row in records)
    ordered = tuple(
        sorted(payloads, key=lambda row: str(row.get("record_id") or ""))
    )
    groups: dict[tuple[Any, ...], list[Mapping[str, Any]]] = {}
    for row in ordered:
        key = (
            str(row.get("metric_id") or ""),
            str(row.get("unit") or ""),
            str(row.get("dataset") or ""),
            str(row.get("record_kind") or ""),
            str(row.get("source_route") or ""),
            tuple(sorted(str(value) for value in row.get("evidence_roles") or ())),
        )
        groups.setdefault(key, []).append(row)
    summaries = []
    for key in sorted(groups, key=lambda value: tuple(map(str, value))):
        rows = groups[key]
        chronological = sorted(
            rows,
            key=lambda row: (
                str(row.get("available_at") or row.get("observed_at") or ""),
                str(row.get("observed_at") or ""),
                str(row.get("period") or ""),
                str(row.get("record_id") or ""),
            ),
        )
        numeric_values = [
            float(row["value"])
            for row in rows
            if _finite_number(row.get("value"))
        ]
        text_counts: dict[str, int] = {}
        for row in rows:
            if _finite_number(row.get("value")):
                continue
            text = str(row.get("value"))
            text_counts[text] = text_counts.get(text, 0) + 1
        summary: dict[str, Any] = {
            "metric_id": key[0],
            "unit": key[1],
            "dataset": key[2],
            "record_kind": key[3],
            "source_route": key[4],
            "evidence_roles": list(key[5]),
            "record_count": len(rows),
            "record_roster_hash": _stable_hash(rows),
            "source_ids": sorted(
                {
                    str(source_id)
                    for row in rows
                    for source_id in row.get("source_ids") or ()
                }
            ),
            "earliest_record": _record_snapshot(chronological[0]),
            "latest_record": _record_snapshot(chronological[-1]),
        }
        if numeric_values:
            summary["numeric_distribution"] = {
                "count": len(numeric_values),
                "minimum": min(numeric_values),
                "median": median(numeric_values),
                "maximum": max(numeric_values),
            }
        if text_counts:
            summary["categorical_value_counts"] = dict(sorted(text_counts.items()))
        summaries.append(summary)
    return {
        "schema_version": "e2r_v5_structured_prompt_projection_v1",
        "record_count": len(ordered),
        "record_roster_hash": _stable_hash(ordered),
        "semantic_series_count": len(summaries),
        "semantic_series": summaries,
        "every_record_accounted_by_hash_and_series_count": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def project_structured_result(result: Any | None) -> Mapping[str, Any] | None:
    if result is None:
        return None
    method = getattr(result, "to_prompt_projection", None)
    if callable(method):
        return method()
    payload = result.to_dict() if hasattr(result, "to_dict") else dict(result)
    records = tuple(getattr(result, "records", ()) or payload.get("records") or ())
    if not records:
        return payload
    output = {
        key: value
        for key, value in payload.items()
        if key not in {"records"}
    }
    projection = project_structured_records(records)
    output["record_projection"] = projection
    output["records"] = [
        {
            "transport_projection": True,
            "record_count": projection["record_count"],
            "record_roster_hash": projection["record_roster_hash"],
            "full_records_persisted_outside_prompt": True,
        }
    ]
    return output


def _record_dict(value: Any) -> Mapping[str, Any]:
    return value.to_dict() if hasattr(value, "to_dict") else dict(value)


def _record_snapshot(row: Mapping[str, Any]) -> Mapping[str, Any]:
    fields = (
        "record_id",
        "metric_id",
        "value",
        "unit",
        "period",
        "evidence_roles",
        "source_ids",
        "source_route",
        "observed_at",
        "available_at",
        "record_kind",
        "confidence",
        "dataset",
        "provenance",
        "input_record_ids",
        "metadata",
    )
    return {key: row[key] for key in fields if key in row}


def _finite_number(value: Any) -> bool:
    return (
        not isinstance(value, bool)
        and isinstance(value, (int, float))
        and math.isfinite(float(value))
    )


def _stable_hash(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


__all__ = [
    "project_source_documents",
    "project_source_graph_checkpoint",
    "project_structured_records",
    "project_structured_result",
]
