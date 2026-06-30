"""Census v2 acceptance audit."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from .census_audit import audit_census_mode
from .census_reports import build_stage_summary, stage_rows_to_dicts


def audit_census_mode_v2(
    *,
    eligible_symbols: Sequence[str],
    stage_rows: Sequence[Mapping[str, Any]],
    source_tasks: Sequence[Mapping[str, Any]],
    report_metadata: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    rows = stage_rows_to_dicts(stage_rows)
    base_audit = audit_census_mode(
        eligible_symbols=eligible_symbols,
        stage_status_rows=rows,
        source_tasks=source_tasks,
        report_metadata=report_metadata,
        report_line_counts=(10,),
    )
    summary = build_stage_summary(rows, total_universe_count=len(eligible_symbols))
    unknown_count = sum(1 for row in rows if row.get("base_stage") in {None, "", "Unknown"} or row.get("census_status") in {None, "", "UNKNOWN"})
    provider_pending_count = sum(1 for row in rows if row.get("census_status") == "PENDING_PROVIDER")
    provider_pending_rate = provider_pending_count / len(rows) if rows else 0.0
    status_buckets = {str(row.get("census_status") or "UNKNOWN") for row in rows}
    stage_buckets = {str(row.get("base_stage") or "Unknown") for row in rows}
    accepted_total = sum(int(row.get("accepted_claim_count") or 0) for row in rows)
    score_total = sum(int(row.get("score_contribution_count") or 0) for row in rows)
    source_task_count = len(source_tasks)
    v2_critical = {
        "unknown_stage_status_count": unknown_count,
        "provider_pending_rate_over_30pct_count": int(provider_pending_rate >= 0.30),
        "status_bucket_lt_4_count": int(len(status_buckets) < 4),
        "base_stage_bucket_lt_3_count": int(len(stage_buckets) < 3),
        "accepted_claim_total_zero_count": int(accepted_total <= 0),
        "score_contribution_total_zero_count": int(score_total <= 0),
        "source_task_total_zero_count": int(source_task_count <= 0),
        "all_stage0_or_provider_pending_count": int(
            rows
            and all(row.get("base_stage") == "Stage0" or row.get("census_status") == "PENDING_PROVIDER" for row in rows)
        ),
    }
    critical_sum = int(base_audit["summary"]["critical_count_sum"]) + sum(v2_critical.values())
    labels = []
    if critical_sum == 0:
        labels = [
            "CENSUS_V1_RECLASSIFIED",
            "BASELINE_SOURCE_WIRED_PASS",
            "SOURCE_TIMELINE_PASS",
            "LAST_EFFECTIVE_THESIS_PASS",
            "CENSUS_LIGHT_PASS",
            "CENSUS_SELECTIVE_DEEP_PASS",
            "FULL_UNIVERSE_STAGE_MAP_PASS",
            "SELF_REPAIR_LOOP_PASS",
            "CENSUS_STATIC_AUDIT_PASS",
        ]
    return {
        "schema_version": "e2r_census_v2_acceptance_audit_v1",
        "summary": {
            "status": "CENSUS_V2_ACCEPTANCE_PASS" if critical_sum == 0 else "CENSUS_V2_ACCEPTANCE_FAIL",
            "critical_count_sum": critical_sum,
            "labels": labels,
        },
        "critical_counts": {**base_audit["critical_counts"], **v2_critical},
        "v2_metrics": {
            "eligible_symbol_count": len(eligible_symbols),
            "stage_row_count": len(rows),
            "unknown_count": unknown_count,
            "unknown_rate": unknown_count / len(rows) if rows else 1.0,
            "provider_pending_count": provider_pending_count,
            "provider_pending_rate": provider_pending_rate,
            "status_bucket_count": len(status_buckets),
            "base_stage_bucket_count": len(stage_buckets),
            "accepted_claim_total": accepted_total,
            "score_contribution_total": score_total,
            "source_task_count": source_task_count,
            "stage_distribution": summary.get("stage_distribution"),
            "status_distribution": summary.get("status_distribution"),
        },
        "base_audit": base_audit,
    }


__all__ = ["audit_census_mode_v2"]
