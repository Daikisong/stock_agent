"""Mandatory research-to-runtime replay matrix for goal4."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Sequence


MANDATORY_REPLAY_SPECS = (
    ("C06_HBM_MEMORY_CUSTOMER_CAPACITY", "c06_source_backed_semantic_replay.json", "c06_guard_replay_audit.json"),
    ("C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "c08_source_backed_semantic_replay.json", None),
    ("C15_MATERIAL_SPREAD_SUPERCYCLE", "c15_source_backed_semantic_replay.json", None),
    ("C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "c17_source_backed_semantic_replay.json", None),
    ("C24_BIO_TRIAL_DATA_EVENT_RISK", "c24_source_backed_semantic_replay.json", None),
    ("C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "c28_source_backed_semantic_replay.json", None),
)


def _read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _resolve_output_root(repo_root: Path, docs_dir: Path, explicit_output_root: str | Path | None) -> Path:
    if explicit_output_root:
        path = Path(explicit_output_root)
        return path if path.is_absolute() else repo_root / path
    manifest = _read_json(docs_dir / "census_mode_v4_artifact_manifest.json")
    output_root = manifest.get("output_root")
    if not output_root:
        raise FileNotFoundError("Cannot resolve output root from census_mode_v4_artifact_manifest.json")
    path = Path(output_root)
    return path if path.is_absolute() else repo_root / path


def _replay_status(replay: Mapping[str, Any]) -> str:
    if not replay:
        return "SOURCE_REPAIR_REQUIRED"
    if replay.get("positive_replay_pass") and int(replay.get("accepted_claim_count") or 0) > 0:
        return "ACCEPTED_CLAIM_CREATED"
    if replay.get("blockers"):
        return "SOURCE_REPAIR_REQUIRED"
    return "SOURCE_REPAIR_REQUIRED"


def build_research_to_runtime_replay_matrix(
    *,
    repo_root: str | Path = ".",
    output_root: str | Path | None = None,
    docs_dir: str | Path = "docs/operational",
    mandatory_specs: Sequence[tuple[str, str, str | None]] = MANDATORY_REPLAY_SPECS,
) -> dict[str, Any]:
    root = Path(repo_root).resolve()
    docs = Path(docs_dir)
    docs = docs if docs.is_absolute() else root / docs
    out = _resolve_output_root(root, docs, output_root)
    memory_cards = _read_json(docs / "research_runtime_memory_cards_v2.json")
    cards = {card["archetype_id"]: card for card in memory_cards.get("cards", [])}
    parity = _read_json(docs / "research_to_runtime_parity_matrix_2026-07-05.json")
    parity_rows = {row["archetype_id"]: row for row in parity.get("rows", [])}

    rows: list[dict[str, Any]] = []
    repair_tasks: list[dict[str, Any]] = []
    for archetype_id, replay_file, guard_file in mandatory_specs:
        replay = _read_json(out / replay_file)
        guard = _read_json(out / guard_file) if guard_file else replay
        card = cards.get(archetype_id, {})
        parity_row = parity_rows.get(archetype_id, {})
        source_proxy_cases = list(card.get("source_proxy_only_cases") or [])
        pending_cases = list(card.get("evidence_url_pending_cases") or [])
        url_cases = list(card.get("url_backed_replay_cases") or [])
        accepted_claim_ids = list(
            replay.get("positive_accepted_claim_ids")
            or replay.get("accepted_claim_ids")
            or []
        )
        guard_claim_ids = list(guard.get("guard_accepted_claim_ids") or guard.get("accepted_claim_ids") or [])
        positive_status = _replay_status(replay)
        guard_pass = bool(guard.get("guard_replay_pass") or guard.get("guard_cases_pass") or replay.get("guard_replay_pass"))
        guard_status = "ACCEPTED_CLAIM_CREATED" if guard_pass else "SOURCE_REPAIR_REQUIRED"
        lifecycle_status = "LIFECYCLE_NOT_CURRENT"
        if parity_row.get("runtime_full_thesis_row_count"):
            lifecycle_status = "CURRENT_PRODUCTION_FULL_THESIS_AVAILABLE"
        elif parity_row.get("source_route_status") == "BLOCKED_FULL_THESIS_CANDIDATE":
            lifecycle_status = "CURRENT_PRODUCTION_CANDIDATE_BLOCKED"

        source_proxy_repair_ids: list[str] = []
        for index, case_id in enumerate((source_proxy_cases + pending_cases)[:3], start=1):
            task = {
                "schema_version": "e2r_research_to_runtime_source_repair_task_v1",
                "task_id": f"RTR-REPAIR-{archetype_id}-{index}",
                "archetype_id": archetype_id,
                "source_case_id": case_id,
                "source_case_quality": "SOURCE_PROXY_ONLY" if case_id in source_proxy_cases else "EVIDENCE_URL_PENDING",
                "runtime_replay_status": "SOURCE_REPAIR_REQUIRED",
                "production_score_allowed": False,
                "next_action": "repair_url_or_fetch_current_source_backed_anchor_before_score",
            }
            repair_tasks.append(task)
            source_proxy_repair_ids.append(task["task_id"])

        row = {
            "schema_version": "e2r_research_to_runtime_replay_row_v1",
            "archetype_id": archetype_id,
            "positive_replay_file": replay_file,
            "guard_replay_file": guard_file or replay_file,
            "positive_runtime_replay_status": positive_status,
            "positive_pass": positive_status == "ACCEPTED_CLAIM_CREATED",
            "positive_accepted_claim_ids": accepted_claim_ids,
            "positive_primitive_states": replay.get("positive_accepted_primitive_ids")
            or replay.get("accepted_primitive_ids")
            or [],
            "score_contribution_ids": replay.get("score_contribution_ids") or [],
            "stagecourt_trace_id": replay.get("stagecourt_trace_id"),
            "guard_runtime_replay_status": guard_status,
            "guard_pass": guard_pass,
            "guard_accepted_claim_ids": guard_claim_ids,
            "source_proxy_repair_task_ids": source_proxy_repair_ids,
            "source_proxy_repair_required": bool(source_proxy_repair_ids),
            "current_lifecycle_validation_status": lifecycle_status,
            "production_score_evidence_allowed": bool(replay.get("production_score_evidence_allowed")),
            "runtime_full_thesis_row_count": int(parity_row.get("runtime_full_thesis_row_count") or 0),
            "runtime_parity_status": parity_row.get("runtime_parity_status"),
            "url_backed_replay_case_count": len(url_cases),
            "source_proxy_only_case_count": len(source_proxy_cases),
            "evidence_url_pending_case_count": len(pending_cases),
            "pass": positive_status == "ACCEPTED_CLAIM_CREATED" and guard_pass and not bool(replay.get("production_score_evidence_allowed")),
        }
        rows.append(row)

    return {
        "schema_version": "e2r_research_to_runtime_replay_matrix_v1",
        "mandatory_archetype_count": len(rows),
        "accepted_claim_replay_count": sum(1 for row in rows if row["positive_pass"]),
        "guard_replay_pass_count": sum(1 for row in rows if row["guard_pass"]),
        "production_score_leak_count": sum(1 for row in rows if row["production_score_evidence_allowed"]),
        "source_proxy_repair_task_count": len(repair_tasks),
        "all_source_proxy_cases_planning_only": all(not task["production_score_allowed"] for task in repair_tasks),
        "rows": rows,
        "source_repair_tasks": repair_tasks,
    }


def write_research_to_runtime_replay_reports(
    *,
    repo_root: str | Path = ".",
    output_root: str | Path | None = None,
    docs_dir: str | Path = "docs/operational",
) -> dict[str, Any]:
    root = Path(repo_root).resolve()
    docs = Path(docs_dir)
    docs = docs if docs.is_absolute() else root / docs
    payload = build_research_to_runtime_replay_matrix(repo_root=root, output_root=output_root, docs_dir=docs)
    matrix_path = docs / "research_to_runtime_replay_matrix_v1.json"
    repair_path = docs / "research_to_runtime_source_repair_queue_v1.json"
    docs.mkdir(parents=True, exist_ok=True)
    matrix_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    repair_path.write_text(
        json.dumps(
            {
                "schema_version": "e2r_research_to_runtime_source_repair_queue_v1",
                "source_proxy_score_allowed": False,
                "repair_task_count": payload["source_proxy_repair_task_count"],
                "tasks": payload["source_repair_tasks"],
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return {"replay_matrix": payload, "replay_matrix_path": matrix_path, "source_repair_queue_path": repair_path}


__all__ = [
    "MANDATORY_REPLAY_SPECS",
    "build_research_to_runtime_replay_matrix",
    "write_research_to_runtime_replay_reports",
]
