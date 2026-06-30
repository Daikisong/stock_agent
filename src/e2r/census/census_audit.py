"""Static and artifact audit for Census Mode."""

from __future__ import annotations

from typing import Any, Iterable, Mapping, Sequence

from e2r.production.metadata import git_head_sha

from .checkpoint_store import checkpoint_missing_hash_count
from .deep_dossier_scheduler import source_task_without_budget_count
from .schemas import BaseStage, CensusStageStatus, ScoreValidStatus
from .shard_planner import duplicate_symbol_count
from .triage import research_brain_output_forbidden_key_count


CRITICAL_COUNT_KEYS = (
    "eligible_symbol_missing_stage_status_count",
    "duplicate_symbol_stage_status_count",
    "census_assessment_event_to_score_count",
    "no_claim_nonzero_score_count",
    "source_proxy_to_score_count",
    "evidence_url_pending_to_score_count",
    "price_path_only_to_score_count",
    "market_anomaly_to_score_count",
    "news_snippet_to_score_count",
    "provider_failed_final_score_count",
    "old_risk_without_current_open_to_score_count",
    "stale_claim_reused_current_count",
    "cheap_scan_score_as_verified_score_count",
    "research_brain_stage_direct_output_count",
    "research_brain_score_direct_output_count",
    "stage_without_confidence_count",
    "no_current_event_marked_red_count",
    "source_pending_marked_red_count",
    "unbounded_fetch_config_count",
    "checkpoint_missing_hash_count",
    "shard_merge_duplicate_count",
    "report_head_sha_mismatch_count",
    "one_line_large_report_count",
)


def audit_census_mode(
    *,
    eligible_symbols: Sequence[str],
    stage_status_rows: Sequence[CensusStageStatus | Mapping[str, Any]],
    census_assessment_event_score_count: int = 0,
    source_proxy_to_score_count: int = 0,
    evidence_url_pending_to_score_count: int = 0,
    price_path_only_to_score_count: int = 0,
    market_anomaly_to_score_count: int = 0,
    news_snippet_to_score_count: int = 0,
    old_risk_without_current_open_to_score_count: int = 0,
    stale_claim_reused_current_count: int = 0,
    cheap_scan_score_as_verified_score_count: int = 0,
    research_brain_plans: Sequence[Mapping[str, Any]] = (),
    source_tasks: Sequence[Mapping[str, Any]] = (),
    checkpoints: Sequence[Mapping[str, Any]] = (),
    report_metadata: Mapping[str, Any] | None = None,
    report_line_counts: Sequence[int] = (),
) -> dict[str, Any]:
    rows = tuple(_row_dict(row) for row in stage_status_rows)
    eligible = {str(symbol).zfill(6) for symbol in eligible_symbols}
    row_symbols = [str(row.get("symbol") or "").zfill(6) for row in rows]
    row_symbol_set = set(row_symbols)
    no_claim_nonzero = sum(1 for row in rows if (row.get("verified_score") or 0) and int(row.get("accepted_claim_count") or 0) == 0)
    provider_failed_final = sum(
        1
        for row in rows
        if row.get("score_valid_status") == ScoreValidStatus.PROVIDER_FAILED.value
        and row.get("base_stage") in {BaseStage.RED.value, BaseStage.REJECT.value}
    )
    market_anomaly_to_score = sum(1 for row in rows if int(row.get("market_anomaly_count") or 0) > 0 and row.get("verified_score") is not None)
    no_current_red = sum(
        1
        for row in rows
        if row.get("score_valid_status") == ScoreValidStatus.NO_CURRENT_EVENT.value
        and row.get("base_stage") in {BaseStage.RED.value, BaseStage.REJECT.value}
    )
    source_pending_red = sum(
        1
        for row in rows
        if row.get("census_status") in {"PENDING_SOURCE", "PENDING_PROVIDER"}
        and row.get("base_stage") in {BaseStage.RED.value, BaseStage.REJECT.value}
    )
    rb_stage = sum(1 for plan in research_brain_plans if research_brain_output_forbidden_key_count(plan) and "stage" in plan)
    rb_score = sum(
        1
        for plan in research_brain_plans
        if any(key in plan for key in ("score", "verified_score", "current_score_eligible"))
    )
    metadata = dict(report_metadata or {})
    head_mismatch = int(bool(metadata) and metadata.get("git_head_sha") not in {None, git_head_sha(".")})
    critical = {
        "eligible_symbol_missing_stage_status_count": len(eligible - row_symbol_set),
        "duplicate_symbol_stage_status_count": duplicate_symbol_count(rows),
        "census_assessment_event_to_score_count": census_assessment_event_score_count,
        "no_claim_nonzero_score_count": no_claim_nonzero,
        "source_proxy_to_score_count": source_proxy_to_score_count,
        "evidence_url_pending_to_score_count": evidence_url_pending_to_score_count,
        "price_path_only_to_score_count": price_path_only_to_score_count,
        "market_anomaly_to_score_count": market_anomaly_to_score + market_anomaly_to_score_count,
        "news_snippet_to_score_count": news_snippet_to_score_count,
        "provider_failed_final_score_count": provider_failed_final,
        "old_risk_without_current_open_to_score_count": old_risk_without_current_open_to_score_count,
        "stale_claim_reused_current_count": stale_claim_reused_current_count,
        "cheap_scan_score_as_verified_score_count": cheap_scan_score_as_verified_score_count,
        "research_brain_stage_direct_output_count": rb_stage,
        "research_brain_score_direct_output_count": rb_score,
        "stage_without_confidence_count": sum(1 for row in rows if not row.get("stage_confidence")),
        "no_current_event_marked_red_count": no_current_red,
        "source_pending_marked_red_count": source_pending_red,
        "unbounded_fetch_config_count": source_task_without_budget_count(source_tasks),
        "checkpoint_missing_hash_count": checkpoint_missing_hash_count(checkpoints),
        "shard_merge_duplicate_count": duplicate_symbol_count(rows),
        "report_head_sha_mismatch_count": head_mismatch,
        "one_line_large_report_count": sum(1 for value in report_line_counts if value <= 1),
    }
    return {
        "schema_version": "e2r_census_static_logic_audit_v1",
        "summary": {
            "critical_count_sum": sum(int(critical[key]) for key in CRITICAL_COUNT_KEYS),
            "status": "CENSUS_STATIC_AUDIT_PASS" if sum(int(critical[key]) for key in CRITICAL_COUNT_KEYS) == 0 else "CENSUS_STATIC_AUDIT_FAIL",
        },
        "critical_counts": critical,
        "warnings": _warnings(rows),
    }


def _warnings(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    total = len(rows)
    provider_pending = sum(1 for row in rows if row.get("census_status") == "PENDING_PROVIDER")
    stage1 = sum(1 for row in rows if row.get("base_stage") == "Stage1")
    stage0 = sum(1 for row in rows if row.get("base_stage") == "Stage0")
    return {
        "provider_gap_rate_high": bool(total and provider_pending / total > 0.3),
        "too_many_stage1_rows": bool(total and stage1 / total > 0.8),
        "too_many_no_current_catalyst_rows": bool(total and stage0 / total > 0.9),
        "no_green_yellow_found": not any(row.get("base_stage") in {"Stage3-Green", "Stage3-Yellow"} for row in rows),
    }


def _row_dict(row: CensusStageStatus | Mapping[str, Any]) -> dict[str, Any]:
    return row.to_dict() if isinstance(row, CensusStageStatus) else dict(row)


__all__ = ["CRITICAL_COUNT_KEYS", "audit_census_mode"]
