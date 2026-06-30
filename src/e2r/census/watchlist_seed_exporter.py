"""Export Census watchlist seed candidates."""

from __future__ import annotations

from typing import Any, Mapping, Sequence


def export_watchlist_seed(stage_rows: Sequence[Mapping[str, Any]], *, as_of_date: str) -> dict[str, Any]:
    seeds: list[dict[str, Any]] = []
    for row in stage_rows:
        category = _seed_category(row)
        if category is None:
            continue
        seeds.append(
            {
                "symbol": row["symbol"],
                "company_name": row.get("company_name"),
                "as_of_date": as_of_date,
                "category": category,
                "seed_reason": _seed_reason(row, category),
                "base_stage": row.get("base_stage"),
                "score_status": row.get("score_valid_status"),
                "primary_archetype": row.get("primary_archetype"),
                "accepted_claim_ids": [],
                "missing_primitives": row.get("missing_primitives") or [],
                "next_actions": row.get("next_actions") or [],
                "refresh_frequency": _refresh_frequency(category),
                "source_followup_tasks": row.get("source_gaps") or row.get("provider_gaps") or [],
            }
        )
    return {
        "schema_version": "e2r_census_watchlist_seed_v1",
        "as_of_date": as_of_date,
        "seed_count": len(seeds),
        "category_counts": _count_by(seeds, "category"),
        "next_action_counts": _next_action_counts(seeds),
        "items": seeds,
    }


def render_watchlist_seed_report(seed: Mapping[str, Any]) -> str:
    lines = [
        "# Census Mode v1 Watchlist Seed Report",
        "",
        f"- seed_count: {seed.get('seed_count', 0)}",
        f"- category_counts: {seed.get('category_counts', {})}",
        f"- next_action_counts: {seed.get('next_action_counts', {})}",
        "",
        "매수/매도 언어 없이 daily trigger가 추적할 상태만 export한다.",
    ]
    return "\n".join(lines) + "\n"


def _seed_category(row: Mapping[str, Any]) -> str | None:
    stage = row.get("base_stage")
    status = row.get("census_status")
    priority = float(row.get("trigger_priority_score") or 0.0)
    if stage == "Stage3-Green":
        return "Green"
    if stage == "Stage3-Yellow":
        return "Yellow-Pending"
    if stage == "Stage2-Actionable":
        return "Stage2-Actionable"
    if stage == "Stage2-Watch" and priority >= 25.0:
        return "Stage2-Watch"
    if status == "PENDING_PROVIDER" and priority >= 25.0:
        return "ProviderPending"
    if row.get("risk_event_count"):
        return "RiskReview"
    return None


def _seed_reason(row: Mapping[str, Any], category: str) -> str:
    if category == "ProviderPending":
        return "material provider/source gap requires retry"
    if category == "RiskReview":
        return "current risk flag requires source-backed lifecycle review"
    return f"{category} census status requires daily trigger tracking"


def _refresh_frequency(category: str) -> str:
    if category in {"Green", "Yellow-Pending", "RiskReview"}:
        return "daily"
    if category == "ProviderPending":
        return "on_event"
    return "weekly"


def _count_by(rows: Sequence[Mapping[str, Any]], key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        value = str(row.get(key) or "UNKNOWN")
        counts[value] = counts.get(value, 0) + 1
    return counts


def _next_action_counts(rows: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        for action in row.get("next_actions") or ():
            counts[str(action)] = counts.get(str(action), 0) + 1
    return counts


__all__ = ["export_watchlist_seed", "render_watchlist_seed_report"]
