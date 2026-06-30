"""Deep backfill planning for Census Mode."""

from __future__ import annotations

from typing import Any, Mapping, Sequence


def build_deep_backfill_plan(stage_rows: Sequence[Mapping[str, Any]], *, shard_count: int = 10) -> dict[str, Any]:
    stage2plus = [
        row
        for row in stage_rows
        if row.get("base_stage") in {"Stage2-Watch", "Stage2-Actionable", "Stage3-Yellow", "Stage3-Green"}
    ]
    pending = [row for row in stage_rows if row.get("census_status") in {"PENDING_PROVIDER", "PENDING_SOURCE"}]
    source_gaps: dict[str, int] = {}
    sectors: dict[str, int] = {}
    for row in stage_rows:
        sector = str(row.get("large_sector_id") or "unknown")
        sectors[sector] = sectors.get(sector, 0) + 1
        for gap in row.get("source_gaps") or row.get("provider_gaps") or ():
            source_gaps[str(gap)] = source_gaps.get(str(gap), 0) + 1
    return {
        "schema_version": "e2r_census_deep_backfill_plan_v1",
        "shard_count": shard_count,
        "sector_priority": sorted(sectors, key=lambda key: (-sectors[key], key))[:10],
        "archetype_priority": [],
        "provider_gap_priority": sorted(source_gaps, key=lambda key: (-source_gaps[key], key))[:10],
        "pending_symbol_list": [row["symbol"] for row in pending],
        "Stage2plus_candidate_list": [row["symbol"] for row in stage2plus],
        "source_heavy_candidate_list": [row["symbol"] for row in stage_rows if row.get("source_gaps") or row.get("provider_gaps")],
        "expected_runtime": "multi-shard; bounded per shard",
        "expected_llm_calls": len(stage2plus),
        "expected_provider_calls": len(stage2plus) * 3 + len(pending),
        "checkpoint_strategy": "per-shard checkpoint with source/config hash",
        "resume_strategy": "skip processed symbols and merge deterministic stage rows",
    }


def render_deep_backfill_plan(plan: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# Census Mode v1 Deep Backfill Plan",
            "",
            "이번 Goal에서는 full deep backfill을 실행하지 않고 계획만 생성한다.",
            "",
            f"- shard_count: {plan.get('shard_count')}",
            f"- pending_symbol_count: {len(plan.get('pending_symbol_list') or [])}",
            f"- Stage2plus_candidate_count: {len(plan.get('Stage2plus_candidate_list') or [])}",
            f"- top source/provider gaps: {plan.get('provider_gap_priority')}",
            f"- checkpoint_strategy: {plan.get('checkpoint_strategy')}",
            f"- resume_strategy: {plan.get('resume_strategy')}",
            "",
        ]
    )


__all__ = ["build_deep_backfill_plan", "render_deep_backfill_plan"]
