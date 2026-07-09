"""Compatibility case aggregation owned by Research Brain."""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any, Iterable, Mapping


def build_archetype_coverage_matrix(records: Iterable[Mapping[str, Any]], contract_ids: list[str]) -> dict[str, Any]:
    by_arch: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for record in records:
        by_arch[str(record["canonical_archetype_id"])].append(record)

    rows: list[dict[str, Any]] = []
    for archetype_id in contract_ids:
        arch_records = by_arch.get(archetype_id, [])
        quality = Counter(str(record["source_quality"]) for record in arch_records)
        roles = Counter(str(record["case_role"]) for record in arch_records)
        positives = Counter(
            primitive for record in arch_records for primitive in record.get("primitive_bridge_positive", [])
        )
        missing = Counter(
            primitive for record in arch_records for primitive in record.get("primitive_bridge_missing", [])
        )
        rows.append(
            {
                "archetype_id": archetype_id,
                "record_count": len(arch_records),
                "has_pattern_summary": bool(arch_records),
                "source_gap": not bool(arch_records),
                "source_quality_counts": dict(sorted(quality.items())),
                "case_role_counts": dict(sorted(roles.items())),
                "top_positive_primitives": [key for key, _ in positives.most_common(10)],
                "top_missing_primitives": [key for key, _ in missing.most_common(10)],
                "url_backed_case_count": quality.get("A2_URL_BACKED", 0),
                "source_proxy_only_case_count": quality.get("SOURCE_PROXY_ONLY", 0),
                "evidence_url_pending_case_count": quality.get("EVIDENCE_URL_PENDING", 0),
            }
        )
    return {
        "schema_version": "e2r_research_reverse_archetype_coverage_matrix_v1",
        "archetype_count": len(contract_ids),
        "covered_archetype_count": sum(1 for row in rows if row["record_count"] > 0),
        "source_gap_archetype_count": sum(1 for row in rows if row["source_gap"]),
        "rows": rows,
    }


def build_source_quality_matrix(records: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    records = list(records)
    quality_counts = Counter(str(record["source_quality"]) for record in records)
    proxy_score_leaks = [
        record["research_case_id"]
        for record in records
        if record.get("source_proxy_only") and record.get("production_scoring_changed")
    ]
    url_backed_replay_candidates = [
        record["research_case_id"] for record in records if record.get("source_quality") == "A2_URL_BACKED"
    ]
    return {
        "schema_version": "e2r_research_reverse_source_quality_matrix_v1",
        "record_count": len(records),
        "source_quality_counts": dict(sorted(quality_counts.items())),
        "source_proxy_score_leak_count": len(proxy_score_leaks),
        "source_proxy_score_leak_case_ids": proxy_score_leaks[:100],
        "url_backed_replay_candidate_count": len(url_backed_replay_candidates),
        "url_backed_replay_candidate_ids_sample": url_backed_replay_candidates[:100],
        "price_path_rows_runtime_prompt_allowed": False,
        "source_proxy_rows_runtime_score_allowed": False,
    }


__all__ = ["build_archetype_coverage_matrix", "build_source_quality_matrix"]
