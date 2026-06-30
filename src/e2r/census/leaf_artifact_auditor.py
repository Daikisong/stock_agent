"""Independent leaf artifact auditor for Census v3."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Sequence


REQUIRED_JSONL = (
    "universe.jsonl",
    "census_assessment_events.jsonl",
    "source_timelines.jsonl",
    "last_effective_thesis_states.jsonl",
    "baseline_scan_results.jsonl",
    "census_events.jsonl",
    "depth_decisions.jsonl",
    "research_brain_plans.jsonl",
    "source_tasks.jsonl",
    "source_task_executions.jsonl",
    "evidence_documents.jsonl",
    "evidence_anchors.jsonl",
    "raw_assertions.jsonl",
    "adjudicated_claims.jsonl",
    "accepted_claims.jsonl",
    "primitive_states.jsonl",
    "score_contributions.jsonl",
    "stagecourt_traces.jsonl",
    "census_stage_status.jsonl",
    "census_stage_map.jsonl",
    "claim_to_stage_trace.jsonl",
)

REQUIRED_JSON = (
    "baseline_inputs_summary.json",
    "census_stage_summary.json",
)


def audit_leaf_artifacts(output_root: str | Path) -> dict[str, Any]:
    root = Path(output_root)
    rows = {name: _read_jsonl(root / name) for name in REQUIRED_JSONL if (root / name).exists()}
    missing_files = [name for name in REQUIRED_JSONL if not (root / name).exists()]
    missing_files.extend(name for name in REQUIRED_JSON if not (root / name).exists())
    baseline_summary = _read_json(root / "baseline_inputs_summary.json", default={})
    universe = rows.get("universe.jsonl", [])
    eligible = [row for row in universe if row.get("eligible_for_census", True)]
    eligible_symbols = [str(row.get("symbol") or "").zfill(6) for row in eligible]
    eligible_set = set(eligible_symbols)
    stage_rows = rows.get("census_stage_status.jsonl", [])
    trace_rows = rows.get("claim_to_stage_trace.jsonl", [])
    accepted = rows.get("accepted_claims.jsonl", [])
    contributions = rows.get("score_contributions.jsonl", [])
    source_tasks = rows.get("source_tasks.jsonl", [])
    executions = rows.get("source_task_executions.jsonl", [])
    stagecourt = rows.get("stagecourt_traces.jsonl", [])
    timelines = rows.get("source_timelines.jsonl", [])
    thesis = rows.get("last_effective_thesis_states.jsonl", [])
    baseline = rows.get("baseline_scan_results.jsonl", [])
    depth = rows.get("depth_decisions.jsonl", [])
    events = rows.get("census_events.jsonl", [])

    stage_symbols = [str(row.get("symbol") or "").zfill(6) for row in stage_rows]
    trace_by_symbol = {str(row.get("symbol") or "").zfill(6): row for row in trace_rows}
    stagecourt_ids = {str(row.get("stagecourt_trace_id") or row.get("trace_id") or "") for row in stagecourt}
    accepted_ids = {str(row.get("claim_id") or "") for row in accepted}
    contribution_ids = {str(row.get("score_contribution_id") or row.get("contribution_id") or "") for row in contributions}
    stage_claim_ids = {str(item) for row in stage_rows for item in (row.get("accepted_claim_ids") or [])}
    stage_contribution_ids = {str(item) for row in stage_rows for item in (row.get("score_contribution_ids") or [])}

    stage_distribution = _count_by(stage_rows, "base_stage")
    status_distribution = _count_by(stage_rows, "census_status")
    depth_distribution = _count_by(stage_rows, "assessment_depth")
    event_taxonomy = _count_by(events, "event_category")
    source_family_attempts = _source_family_attempts(timelines)
    provider_failure_count = sum(len(row.get("provider_failures") or []) for row in timelines)
    source_gap_count = sum(len(row.get("source_gaps") or []) for row in stage_rows) + sum(len(row.get("source_gaps") or []) for row in timelines)
    nonzero_score_rows = [row for row in stage_rows if row.get("verified_score") is not None]
    stage2plus_rows = [
        row
        for row in stage_rows
        if row.get("base_stage") in {"Stage2-Watch", "Stage2-Actionable", "Stage3-Yellow", "Stage3-Green", "Reject", "Red"}
    ]
    source_task_with_claim = [row for row in executions if row.get("status") == "EVIDENCE_OS_ACCEPTED" and row.get("accepted_claim_ids")]
    fake_source_execution_count = sum(
        1
        for row in executions
        if row.get("status") in {"PARSED", "FETCHED"}
        or (row.get("status") == "EVIDENCE_OS_ACCEPTED" and not row.get("accepted_claim_ids"))
        or (row.get("claim_producing_execution") and not row.get("accepted_claim_ids"))
    )
    stage_rows_with_score_trace = [
        row
        for row in stage_rows
        if row.get("verified_score") is not None and row.get("accepted_claim_ids") and row.get("score_contribution_ids") and row.get("stagecourt_trace_id")
    ]
    trace_missing_for_score = sum(
        1
        for row in nonzero_score_rows
        if not row.get("accepted_claim_ids") or not row.get("score_contribution_ids") or not row.get("stagecourt_trace_id")
    )
    stage2_without_trace = sum(
        1
        for row in stage2plus_rows
        if row.get("census_status") not in {"PENDING_SOURCE", "PENDING_PROVIDER"} and not row.get("stagecourt_trace_id")
    )
    no_current_without_timeline = sum(
        1
        for row in stage_rows
        if row.get("investigation_status") == "NO_CURRENT_CATALYST"
        and not trace_by_symbol.get(str(row.get("symbol") or "").zfill(6), {}).get("source_timeline_id")
    )
    critical = {
        "missing_leaf_artifact_count": len(missing_files),
        "missing_symbol_count": len(eligible_set - set(stage_symbols)),
        "duplicate_symbol_count": _duplicate_count(stage_symbols),
        "stage_status_count_mismatch": int(len(stage_rows) != len(eligible_symbols)),
        "source_timeline_missing_count": len(eligible_set - {str(row.get("symbol") or "").zfill(6) for row in timelines}),
        "last_effective_thesis_missing_count": len(eligible_set - {str(row.get("symbol") or "").zfill(6) for row in thesis}),
        "baseline_scan_missing_count": len(eligible_set - {str(row.get("symbol") or "").zfill(6) for row in baseline}),
        "depth_decision_missing_count": len(eligible_set - {str(row.get("symbol") or "").zfill(6) for row in depth}),
        "empty_baseline_inputs_count": int(int(baseline_summary.get("empty_baseline_inputs_count") or 0) > 0),
        "baseline_source_family_less_than_5_count": int(len(source_family_attempts) < 5),
        "source_family_attempt_missing_count": sum(1 for row in timelines if not row.get("source_family_attempts")),
        "unknown_over_5pct_count": int(bool(stage_rows) and _count_stage_unknown(stage_rows) / len(stage_rows) > 0.05),
        "provider_pending_over_30pct_count": int(bool(stage_rows) and status_distribution.get("PENDING_PROVIDER", 0) / len(stage_rows) >= 0.30),
        "single_stage_bucket_count": int(len(stage_distribution) < 3),
        "single_status_bucket_count": int(len(status_distribution) < 4),
        "accepted_claim_total_zero_count": int(len(accepted) == 0),
        "score_contribution_total_zero_count": int(len(contributions) == 0),
        "source_task_total_zero_count": int(len(source_tasks) == 0),
        "source_task_execution_total_zero_count": int(len(executions) == 0),
        "stagecourt_trace_total_zero_count": int(len(stagecourt) == 0),
        "claim_to_stage_trace_missing_count": len(eligible_set - {str(row.get("symbol") or "").zfill(6) for row in trace_rows}),
        "claim_to_stage_unlinked_count": trace_missing_for_score,
        "score_contribution_unused_count": len(contribution_ids - stage_contribution_ids),
        "accepted_claim_unused_in_stage_count": len(accepted_ids - stage_claim_ids),
        "score_without_claim_count": trace_missing_for_score,
        "claimless_nonzero_score_count": sum(1 for row in nonzero_score_rows if not row.get("accepted_claim_ids")),
        "stage2_without_stagecourt_trace_count": stage2_without_trace,
        "stagecourt_trace_id_missing_from_leaf_count": sum(1 for row in nonzero_score_rows if row.get("stagecourt_trace_id") not in stagecourt_ids),
        "source_task_fake_execution_count": fake_source_execution_count,
        "source_task_with_accepted_claim_zero_count": int(len(source_task_with_claim) == 0),
        "all_unknown_count": int(bool(stage_rows) and _count_stage_unknown(stage_rows) == len(stage_rows)),
        "all_provider_pending_count": int(bool(stage_rows) and status_distribution.get("PENDING_PROVIDER", 0) == len(stage_rows)),
        "all_stage0_without_source_proof_count": int(bool(stage_rows) and stage_distribution.get("Stage0", 0) == len(stage_rows)),
        "no_current_catalyst_without_timeline_count": no_current_without_timeline,
        "source_proxy_to_score_count": sum(1 for row in contributions if row.get("source_proxy_only")),
        "evidence_url_pending_to_score_count": sum(1 for row in contributions if row.get("evidence_url_pending")),
        "price_path_only_to_score_count": sum(1 for row in contributions if row.get("price_path_only")),
        "market_anomaly_to_score_count": sum(1 for row in nonzero_score_rows if row.get("market_anomaly_count")),
        "news_snippet_to_score_count": sum(1 for row in contributions if row.get("source_type") == "snippet"),
        "research_memory_hint_to_score_count": sum(1 for row in contributions if row.get("source_family") == "ResearchMemory"),
        "census_assessment_to_score_count": sum(1 for row in contributions if row.get("source_family") == "FullUniverseCensus"),
        "provider_failed_final_score_count": sum(1 for row in stage_rows if row.get("census_status") == "PENDING_PROVIDER" and row.get("verified_score") is not None),
        "old_risk_without_current_open_to_score_count": _flagged_count(stage_rows, "old_risk_without_current_open_to_score") + _flagged_count(contributions, "old_risk_without_current_open_to_score"),
        "cheap_scan_score_as_verified_score_count": sum(1 for row in nonzero_score_rows if row.get("assessment_depth") == "CHEAP_BASELINE"),
        "recent_lookback_used_as_stage_cutoff_count": _flagged_count(stage_rows, "recent_lookback_cutoff_used") + _text_contains_count(baseline, "recent_lookback_cutoff"),
        "one_line_large_report_count": _one_line_large_report_count(root),
        "report_leaf_mismatch_count": _report_leaf_mismatch_count(root, leaf_stage_distribution=stage_distribution, accepted_count=len(accepted), score_contribution_count=len(contributions)),
    }
    metrics = {
        "raw_universe_count": len(universe),
        "eligible_symbol_count": len(eligible_symbols),
        "stage_status_count": len(stage_rows),
        "missing_symbol_count": critical["missing_symbol_count"],
        "duplicate_symbol_count": critical["duplicate_symbol_count"],
        "unknown_count": _count_stage_unknown(stage_rows),
        "provider_pending_count": status_distribution.get("PENDING_PROVIDER", 0),
        "no_current_catalyst_count": sum(1 for row in stage_rows if row.get("investigation_status") == "NO_CURRENT_CATALYST"),
        "accepted_claim_count": len(accepted),
        "score_contribution_count": len(contributions),
        "source_task_count": len(source_tasks),
        "source_task_execution_count": len(executions),
        "source_task_with_accepted_claim_count": len(source_task_with_claim),
        "stagecourt_trace_count": len(stagecourt),
        "claim_to_stage_trace_count": len(trace_rows),
        "stage_row_with_accepted_claims_count": sum(1 for row in stage_rows if row.get("accepted_claim_ids")),
        "stage_row_with_score_contribution_count": sum(1 for row in stage_rows if row.get("score_contribution_ids")),
        "stage_row_with_stagecourt_trace_count": sum(1 for row in stage_rows if row.get("stagecourt_trace_id")),
        "deterministic_stage_output_count": len(stage_rows_with_score_trace),
        "source_timeline_count": len(timelines),
        "last_effective_thesis_count": len(thesis),
        "baseline_scan_result_count": len(baseline),
        "depth_decision_count": len(depth),
        "research_brain_plan_count": len(rows.get("research_brain_plans.jsonl", [])),
        "stage_distribution": stage_distribution,
        "census_status_distribution": status_distribution,
        "depth_distribution": depth_distribution,
        "event_taxonomy_counts": event_taxonomy,
        "baseline_source_family_wired_count": len(source_family_attempts),
        "source_family_attempt_counts": source_family_attempts,
        "provider_failure_count": provider_failure_count,
        "source_gap_count": source_gap_count,
        "orphan_score_count": critical["score_without_claim_count"],
        "claimless_nonzero_score_count": critical["claimless_nonzero_score_count"],
        "score_contribution_unused_count": critical["score_contribution_unused_count"],
        "accepted_claim_unused_in_any_stage_or_backlog_count": critical["accepted_claim_unused_in_stage_count"],
    }
    critical_sum = sum(int(value) for value in critical.values())
    return {
        "schema_version": "e2r_census_v3_leaf_artifact_audit_v1",
        "output_root": str(root),
        "verdict": "PASS" if critical_sum == 0 else "FAIL",
        "critical_count": critical_sum,
        "critical_counts": critical,
        "metrics": metrics,
        "missing_leaf_artifacts": missing_files,
    }


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if text:
                rows.append(json.loads(text))
    return rows


def _read_json(path: Path, *, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def _count_by(rows: Sequence[Mapping[str, Any]], key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        value = str(row.get(key) or "UNKNOWN")
        counts[value] = counts.get(value, 0) + 1
    return counts


def _flagged_count(rows: Sequence[Mapping[str, Any]], key: str) -> int:
    return sum(1 for row in rows if row.get(key))


def _text_contains_count(rows: Sequence[Mapping[str, Any]], needle: str) -> int:
    return sum(1 for row in rows if needle in json.dumps(row, ensure_ascii=False, sort_keys=True))


def _duplicate_count(values: Sequence[str]) -> int:
    seen: set[str] = set()
    dupes = 0
    for value in values:
        if value in seen:
            dupes += 1
        seen.add(value)
    return dupes


def _count_stage_unknown(rows: Sequence[Mapping[str, Any]]) -> int:
    return sum(1 for row in rows if row.get("base_stage") in {None, "", "Unknown"} or row.get("census_status") in {None, "", "UNKNOWN"})


def _source_family_attempts(timelines: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for timeline in timelines:
        for attempt in timeline.get("source_family_attempts") or ():
            source = str(attempt.get("source_family") or "UNKNOWN")
            counts[source] = counts.get(source, 0) + 1
    return counts


def _one_line_large_report_count(root: Path) -> int:
    count = 0
    for path in root.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        if len(text) > 500 and len(text.splitlines()) <= 1:
            count += 1
    return count


def _report_leaf_mismatch_count(root: Path, *, leaf_stage_distribution: Mapping[str, int], accepted_count: int, score_contribution_count: int) -> int:
    summary_path = root / "census_stage_summary.json"
    if not summary_path.exists():
        return 1
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    mismatch = 0
    if dict(summary.get("stage_distribution") or {}) != dict(leaf_stage_distribution):
        mismatch += 1
    if int(summary.get("accepted_claim_total") or 0) != accepted_count:
        mismatch += 1
    if int(summary.get("score_contribution_total") or 0) != score_contribution_count:
        mismatch += 1
    return mismatch


__all__ = ["REQUIRED_JSONL", "REQUIRED_JSON", "audit_leaf_artifacts"]
