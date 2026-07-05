"""Balanced full-thesis candidate selection audit helpers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Sequence


def _prefix(archetype_id: str) -> str:
    return archetype_id.split("_", 1)[0]


def select_balanced_full_thesis_archetype_attempts(
    parity_audit: Mapping[str, Any],
    *,
    mandatory_prefixes: Sequence[str] = ("C06", "C08", "C15", "C17", "C24", "C28"),
    max_archetypes: int = 12,
) -> list[dict[str, Any]]:
    """Return archetype-level attempts needed for a balanced next run."""

    rows = list(parity_audit.get("rows") or [])
    by_prefix = {_prefix(str(row["archetype_id"])): row for row in rows}
    selected: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add(row: Mapping[str, Any], reason: str, priority: int) -> None:
        archetype_id = str(row["archetype_id"])
        if archetype_id in seen:
            return
        seen.add(archetype_id)
        selected.append(
            {
                "archetype_id": archetype_id,
                "priority": priority,
                "reason": reason,
                "current_runtime_parity_status": row.get("runtime_parity_status"),
                "current_source_route_status": row.get("source_route_status"),
                "runtime_full_thesis_row_count": row.get("runtime_full_thesis_row_count", 0),
                "runtime_planner_top1_count": row.get("runtime_planner_top1_count", 0),
                "runtime_source_task_execution_count": row.get("runtime_source_task_execution_count", 0),
                "source_backed_fixture_count": row.get("source_backed_fixture_count", 0),
            }
        )

    for prefix in mandatory_prefixes:
        row = by_prefix.get(prefix)
        if row and int(row.get("runtime_full_thesis_row_count") or 0) == 0:
            add(row, "mandatory_archetype_missing_production_full_thesis", 10)

    for row in rows:
        if int(row.get("runtime_planner_top1_count") or 0) == 0 and int(row.get("source_backed_fixture_count") or 0) > 0:
            add(row, "source_backed_replay_ready_but_no_runtime_planner_top1", 20)

    for row in rows:
        if int(row.get("runtime_full_thesis_row_count") or 0) == 0 and row.get("source_route_status") != "NOT_ATTEMPTED":
            add(row, "attempted_but_not_promoted_to_full_thesis", 30)

    selected.sort(key=lambda item: (int(item["priority"]), str(item["archetype_id"])))
    return selected[:max_archetypes]


def build_balanced_full_thesis_candidate_selection_audit(
    parity_audit: Mapping[str, Any],
    *,
    mandatory_prefixes: Sequence[str] = ("C06", "C08", "C15", "C17", "C24", "C28"),
    max_archetypes: int = 12,
) -> dict[str, Any]:
    selected = select_balanced_full_thesis_archetype_attempts(
        parity_audit,
        mandatory_prefixes=mandatory_prefixes,
        max_archetypes=max_archetypes,
    )
    blockers: list[str] = []
    if parity_audit.get("c05_full_thesis_share", 0) > 0.35:
        blockers.append("c05_share_over_balanced_selection_limit")
    if int(parity_audit.get("distinct_runtime_attempted_archetype_count") or 0) < 6:
        blockers.append("runtime_attempted_archetype_count_below_minimum")
    if int(parity_audit.get("distinct_full_thesis_archetype_count") or 0) < 3:
        blockers.append("full_thesis_archetype_count_below_meaningful_minimum")
    if parity_audit.get("target_archetype_unknown_promoted_count", 0):
        blockers.append("target_archetype_unknown_promoted")
    if parity_audit.get("source_primary_context_promoted_count", 0):
        blockers.append("source_primary_context_promoted")
    if parity_audit.get("required_positive_missing_full_thesis_row_count", 0):
        blockers.append("required_positive_missing_promoted_rows")

    return {
        "schema_version": "e2r_balanced_full_thesis_candidate_selection_audit_v1",
        "status": "BALANCED_FULL_THESIS_SELECTION_PASS" if not blockers else "BALANCED_FULL_THESIS_SELECTION_NOT_READY",
        "blockers": blockers,
        "selection_rule": (
            "Prioritize mandatory archetypes without production full thesis, then source-backed replay rows "
            "with no runtime planner top1, then attempted rows not promoted."
        ),
        "current_full_thesis_row_count": parity_audit.get("full_thesis_row_count"),
        "current_distinct_full_thesis_archetype_count": parity_audit.get("distinct_full_thesis_archetype_count"),
        "current_c05_full_thesis_share": parity_audit.get("c05_full_thesis_share"),
        "mandatory_archetype_attempt_missing": parity_audit.get("mandatory_archetype_attempt_missing", []),
        "mandatory_archetype_full_thesis_missing": parity_audit.get("mandatory_archetype_full_thesis_missing", []),
        "next_required_archetype_attempts": selected,
        "next_required_archetype_attempt_count": len(selected),
        "meaningful_pass_allowed": bool(parity_audit.get("meaningful_full_thesis_evidence_pass")),
    }


def write_balanced_full_thesis_candidate_selection_audit(
    parity_audit: Mapping[str, Any],
    *,
    docs_dir: str | Path = "docs/operational",
    mandatory_prefixes: Sequence[str] = ("C06", "C08", "C15", "C17", "C24", "C28"),
    max_archetypes: int = 12,
) -> dict[str, Any]:
    docs_path = Path(docs_dir)
    docs_path.mkdir(parents=True, exist_ok=True)
    audit = build_balanced_full_thesis_candidate_selection_audit(
        parity_audit,
        mandatory_prefixes=mandatory_prefixes,
        max_archetypes=max_archetypes,
    )
    path = docs_path / "balanced_full_thesis_candidate_selection_audit_2026-07-05.json"
    path.write_text(json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return audit


__all__ = [
    "build_balanced_full_thesis_candidate_selection_audit",
    "select_balanced_full_thesis_archetype_attempts",
    "write_balanced_full_thesis_candidate_selection_audit",
]
