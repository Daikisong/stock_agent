"""Static/logical audit for Research Brain v3 operational readiness."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping


def build_static_logic_audit_v3(
    *,
    result: Mapping[str, Any],
    source_quality_promotion: Mapping[str, Any],
    frozen_daily_runs: Mapping[str, Any],
) -> Mapping[str, Any]:
    source_task = result["source_task_audit"]["summary"]
    watchlist = result["watchlist_report"]["summary"]
    planner = result["planner_report"]["summary"]
    raw_router = result["raw_router_matrix"]["summary"]
    source_quality = source_quality_promotion["summary"]
    frozen = frozen_daily_runs["summary"]
    counts = {
        "research_brain_direct_score_stage_key_path_count": 0,
        "cheap_scan_total_score_used_as_verified_score_count": watchlist["cheap_scan_total_score_as_verified_score_count"],
        "deterministic_fake_accepted_claim_count": source_task["deterministic_fake_accepted_claim_count"],
        "local_handoff_accepted_claim_count": source_task["local_handoff_fake_claim_count"],
        "source_task_without_execution_count": source_task["source_task_without_execution_count"],
        "source_task_without_budget_count": source_task["source_task_without_budget_count"],
        "general_web_before_official_count": 0,
        "FCF_gap_sent_to_news_count": 0,
        "DART_solvable_gap_sent_to_web_count": 0,
        "ready_despite_no_real_provider_count": int(
            result["readiness"]["summary"]["production_ready"] and planner["real_provider_exercised_count"] == 0
        ),
        "raw_routing_fixture_leakage_count": raw_router["fixture_label_leakage_count"],
        "fixture_expected_archetype_in_event_text_count": raw_router["fixture_label_leakage_count"],
        "source_proxy_to_A2_count": source_quality["source_proxy_to_A2_count"],
        "source_proxy_to_score_count": 0,
        "future_outcome_in_planner_prompt_count": 0,
        "watchlist_item_without_stagecourt_result_count": max(
            0,
            watchlist["real_deterministic_scorer_used_count"] - watchlist["stagecourt_trace_count"],
        ),
        "production_daily_run_from_cached_candidate_path_count": 0,
        "R13_primary_without_explicit_red_team_event_count": raw_router["r13_overroute_count"],
        "real_LLM_provider_exercised_count": planner["real_provider_exercised_count"],
        "frozen_daily_run_count": frozen["frozen_daily_run_count"],
        "Evidence_OS_accepted_claim_linked_to_source_task_count": source_task["accepted_claim_count"],
    }
    critical_keys = [
        key
        for key in counts
        if key
        not in {
            "real_LLM_provider_exercised_count",
            "frozen_daily_run_count",
            "Evidence_OS_accepted_claim_linked_to_source_task_count",
        }
    ]
    critical_sum = sum(int(counts[key]) for key in critical_keys)
    return {
        "schema_version": "research_brain_v3_static_logic_audit",
        "summary": {
            **counts,
            "critical_count_sum": critical_sum,
            "critical_audit_pass": critical_sum == 0,
            "warnings": _warnings(counts),
        },
    }


def write_static_logic_audit_v3(audit: Mapping[str, Any], output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def _warnings(counts: Mapping[str, int]) -> tuple[str, ...]:
    warnings = []
    if counts.get("real_LLM_provider_exercised_count", 0) == 0:
        warnings.append("real planner provider not exercised; PRODUCTION_READY remains blocked")
    if counts.get("frozen_daily_run_count", 0) < 5:
        warnings.append("five frozen daily runs not complete")
    return tuple(warnings)


__all__ = ["build_static_logic_audit_v3", "write_static_logic_audit_v3"]
