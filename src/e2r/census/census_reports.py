"""Report and artifact generation for Census Mode."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl, write_text

from .schemas import CensusStageStatus


STAGE_MAP_COLUMNS = (
    "symbol",
    "company_name",
    "market",
    "large_sector_id",
    "census_status",
    "assessment_depth",
    "base_stage",
    "investigation_status",
    "transition_overlay",
    "stage_confidence",
    "score_valid_status",
    "trigger_priority_score",
    "verified_score",
    "provisional_score",
    "score_interval_lower",
    "score_interval_upper",
    "accepted_claim_count",
    "score_contribution_count",
    "recent_event_count",
    "primary_archetype",
    "failed_stage_gates",
    "missing_primitives",
    "provider_gaps",
    "source_gaps",
    "next_actions",
)


def stage_rows_to_dicts(rows: Sequence[CensusStageStatus | Mapping[str, Any]]) -> tuple[dict[str, Any], ...]:
    return tuple(row.to_dict() if isinstance(row, CensusStageStatus) else dict(row) for row in rows)


def build_stage_summary(rows: Sequence[CensusStageStatus | Mapping[str, Any]], *, total_universe_count: int) -> dict[str, Any]:
    data = stage_rows_to_dicts(rows)
    by_stage = _count_by(data, "base_stage")
    by_status = _count_by(data, "census_status")
    by_depth = _count_by(data, "assessment_depth")
    return {
        "schema_version": "e2r_census_stage_summary_v1",
        "total_universe_count": total_universe_count,
        "eligible_symbol_count": len(data),
        "scanned_symbol_count": len(data),
        "completed_symbol_count": sum(1 for row in data if row.get("investigation_status") in {"COMPLETE", "NO_CURRENT_CATALYST"}),
        "failed_symbol_count": sum(1 for row in data if row.get("census_status") == "FAILED"),
        "provider_pending_count": by_status.get("PENDING_PROVIDER", 0),
        "runtime_pending_count": sum(1 for row in data if row.get("investigation_status") == "RUNTIME_BUDGET_EXHAUSTED"),
        "no_current_catalyst_count": sum(1 for row in data if row.get("investigation_status") == "NO_CURRENT_CATALYST"),
        "stage0_count": by_stage.get("Stage0", 0),
        "stage1_count": by_stage.get("Stage1", 0),
        "stage2_watch_count": by_stage.get("Stage2-Watch", 0),
        "stage2_actionable_count": by_stage.get("Stage2-Actionable", 0),
        "yellow_pending_count": by_stage.get("Stage3-Yellow", 0),
        "green_count": by_stage.get("Stage3-Green", 0),
        "reject_red_count": by_stage.get("Reject", 0) + by_stage.get("Red", 0),
        "risk_review_count": sum(1 for row in data if "RISK_REVIEW" in row.get("next_actions", [])),
        "verified_score_count": sum(1 for row in data if row.get("verified_score") is not None),
        "no_score_count": sum(1 for row in data if row.get("verified_score") is None),
        "accepted_claim_total": sum(int(row.get("accepted_claim_count") or 0) for row in data),
        "score_contribution_total": sum(int(row.get("score_contribution_count") or 0) for row in data),
        "orphan_score_count": sum(int(row.get("orphan_score_count") or 0) for row in data),
        "source_proxy_to_score_count": 0,
        "stage_distribution": by_stage,
        "status_distribution": by_status,
        "depth_distribution": by_depth,
    }


def build_sector_distribution(rows: Sequence[CensusStageStatus | Mapping[str, Any]]) -> dict[str, Any]:
    data = stage_rows_to_dicts(rows)
    sectors: dict[str, dict[str, Any]] = {}
    for row in data:
        key = str(row.get("large_sector_id") or "unknown")
        sector = sectors.setdefault(
            key,
            {
                "eligible_count": 0,
                "scanned_count": 0,
                "stage_distribution": {},
                "ProviderPending_count": 0,
                "SourceGap_count": 0,
                "DeepDossier_count": 0,
                "Stage2plus_count": 0,
                "accepted_claim_count": 0,
            },
        )
        sector["eligible_count"] += 1
        sector["scanned_count"] += 1
        stage = str(row.get("base_stage"))
        sector["stage_distribution"][stage] = sector["stage_distribution"].get(stage, 0) + 1
        if row.get("census_status") == "PENDING_PROVIDER":
            sector["ProviderPending_count"] += 1
        if row.get("source_gaps"):
            sector["SourceGap_count"] += 1
        if row.get("assessment_depth") == "DEEP_DOSSIER":
            sector["DeepDossier_count"] += 1
        if stage in {"Stage2-Watch", "Stage2-Actionable", "Stage3-Yellow", "Stage3-Green"}:
            sector["Stage2plus_count"] += 1
        sector["accepted_claim_count"] += int(row.get("accepted_claim_count") or 0)
    return {"schema_version": "e2r_census_sector_distribution_v1", "sectors": sectors}


def build_provider_gap_report(rows: Sequence[CensusStageStatus | Mapping[str, Any]]) -> dict[str, Any]:
    data = stage_rows_to_dicts(rows)
    counts: dict[str, int] = {}
    for row in data:
        for gap in row.get("provider_gaps") or ():
            counts[str(gap)] = counts.get(str(gap), 0) + 1
    return {
        "schema_version": "e2r_census_provider_gap_report_v1",
        "provider_pending_count": sum(1 for row in data if row.get("census_status") == "PENDING_PROVIDER"),
        "provider_gap_counts": counts,
    }


def build_source_gap_report(rows: Sequence[CensusStageStatus | Mapping[str, Any]]) -> dict[str, Any]:
    data = stage_rows_to_dicts(rows)
    counts: dict[str, int] = {}
    for row in data:
        for gap in row.get("source_gaps") or ():
            counts[str(gap)] = counts.get(str(gap), 0) + 1
    return {"schema_version": "e2r_census_source_gap_report_v1", "source_gap_counts": counts, "source_gap_count": sum(counts.values())}


def write_census_outputs(
    *,
    output_root: str | Path,
    universe_rows: Sequence[Mapping[str, Any]],
    event_rows: Sequence[Mapping[str, Any]],
    baseline_rows: Sequence[Mapping[str, Any]],
    depth_rows: Sequence[Mapping[str, Any]],
    research_plans: Sequence[Mapping[str, Any]],
    source_tasks: Sequence[Mapping[str, Any]],
    source_task_executions: Sequence[Mapping[str, Any]],
    stage_rows: Sequence[Mapping[str, Any]],
    run_metadata: Mapping[str, Any],
    audit_summary: Mapping[str, Any],
    stage_summary: Mapping[str, Any],
    sector_distribution: Mapping[str, Any],
    provider_gap_report: Mapping[str, Any],
    source_gap_report: Mapping[str, Any],
    watchlist_seed_candidates: Mapping[str, Any],
    operator_digest_md: str,
    deep_backfill_plan: Mapping[str, Any] | None = None,
) -> None:
    root = Path(output_root)
    write_json(root / "run_metadata.json", run_metadata)
    write_jsonl(root / "universe.jsonl", universe_rows)
    write_jsonl(root / "census_assessment_events.jsonl", event_rows)
    write_jsonl(root / "baseline_scan_results.jsonl", baseline_rows)
    write_jsonl(root / "depth_decisions.jsonl", depth_rows)
    write_jsonl(root / "research_brain_plans.jsonl", research_plans)
    write_jsonl(root / "source_tasks.jsonl", source_tasks)
    write_jsonl(root / "source_task_executions.jsonl", source_task_executions)
    for name in ("evidence_documents", "evidence_anchors", "accepted_claims", "primitive_states", "score_contributions", "stagecourt_traces"):
        write_jsonl(root / f"{name}.jsonl", [])
    write_jsonl(root / "census_stage_status.jsonl", stage_rows)
    write_jsonl(root / "census_stage_map.jsonl", stage_rows)
    _write_stage_csv(root / "census_stage_map.csv", stage_rows)
    write_json(root / "census_stage_summary.json", stage_summary)
    write_json(root / "sector_stage_distribution.json", sector_distribution)
    write_json(root / "provider_gap_report.json", provider_gap_report)
    write_json(root / "source_gap_report.json", source_gap_report)
    write_json(root / "watchlist_seed_candidates.json", watchlist_seed_candidates)
    write_text(root / "operator_digest.md", operator_digest_md)
    write_json(root / "audit_summary.json", audit_summary)
    write_json(root / "deep_backfill_plan.json", deep_backfill_plan or {})


def render_stage_map_summary_md(summary: Mapping[str, Any]) -> str:
    stage = dict(summary.get("stage_distribution") or {})
    lines = [
        "# Census Mode v1 Stage Map Summary",
        "",
        f"- total_universe_count: {summary.get('total_universe_count')}",
        f"- eligible_symbol_count: {summary.get('eligible_symbol_count')}",
        f"- scanned_symbol_count: {summary.get('scanned_symbol_count')}",
        f"- provider_pending_count: {summary.get('provider_pending_count')}",
        f"- no_current_catalyst_count: {summary.get('no_current_catalyst_count')}",
        "",
        "## Stage Distribution",
    ]
    for key in sorted(stage):
        lines.append(f"- {key}: {stage[key]}")
    return "\n".join(lines) + "\n"


def render_operator_digest(
    *,
    summary: Mapping[str, Any],
    watchlist_seed: Mapping[str, Any],
    provider_gap_report: Mapping[str, Any],
    source_gap_report: Mapping[str, Any],
) -> str:
    return "\n".join(
        [
            "# Census Operator Digest",
            "",
            "## 전체 요약",
            f"- eligible: {summary.get('eligible_symbol_count')}",
            f"- Stage0/NoCurrentCatalyst: {summary.get('stage0_count')} / {summary.get('no_current_catalyst_count')}",
            f"- ProviderPending: {summary.get('provider_pending_count')}",
            f"- Watchlist seed: {watchlist_seed.get('seed_count', 0)}",
            "",
            "## Stage3-Green",
            f"- count: {summary.get('green_count')}",
            "",
            "## Stage3-Yellow-Pending",
            f"- count: {summary.get('yellow_pending_count')}",
            "",
            "## Stage2-Actionable",
            f"- count: {summary.get('stage2_actionable_count')}",
            "",
            "## Stage2-Watch",
            f"- count: {summary.get('stage2_watch_count')}",
            "",
            "## Provider/Source Pending",
            f"- provider gaps: {provider_gap_report.get('provider_gap_counts', {})}",
            f"- source gaps: {source_gap_report.get('source_gap_counts', {})}",
            "",
            "## NoCurrentCatalyst summary",
            "- 새 claim이나 official event가 없는 종목은 낮은 점수나 Red가 아니라 Stage0 상태로 남겼다.",
            "",
            "## Watchlist seed",
            "- daily trigger track 대상만 seed로 넘긴다. 매수/매도 표현은 포함하지 않는다.",
            "",
            "## Deep backfill candidates",
            "- deep backfill은 이번 Goal에서 실행하지 않고 계획만 생성한다.",
            "",
        ]
    )


def _count_by(rows: Sequence[Mapping[str, Any]], key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        value = str(row.get(key) or "UNKNOWN")
        counts[value] = counts.get(value, 0) + 1
    return counts


def _write_stage_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=STAGE_MAP_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _csv_cell(row.get(key)) for key in STAGE_MAP_COLUMNS})


def _csv_cell(value: Any) -> Any:
    if isinstance(value, (list, tuple)):
        return "|".join(str(item) for item in value)
    return value


__all__ = [
    "STAGE_MAP_COLUMNS",
    "build_provider_gap_report",
    "build_sector_distribution",
    "build_source_gap_report",
    "build_stage_summary",
    "render_operator_digest",
    "render_stage_map_summary_md",
    "stage_rows_to_dicts",
    "write_census_outputs",
]
