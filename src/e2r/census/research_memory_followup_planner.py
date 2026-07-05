"""Build research-memory informed follow-up tasks for blocked full-thesis candidates."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping


def _read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def build_research_memory_followup_tasks(
    *,
    docs_dir: str | Path = "docs/operational",
) -> dict[str, Any]:
    docs = Path(docs_dir)
    cards_payload = _read_json(docs / "research_runtime_memory_cards_v2.json")
    route_payload = _read_json(docs / "research_source_route_recovery_matrix.json")
    runner = _read_json(docs / "census_mode_v4_full_thesis_production_runner_audit.json")
    cards = {card["archetype_id"]: card for card in cards_payload.get("cards", [])}
    routes: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for pattern in route_payload.get("patterns", []):
        routes.setdefault((pattern["archetype_id"], pattern["primitive_id"]), []).append(pattern)

    tasks: list[dict[str, Any]] = []
    for blocked in runner.get("blocked_candidates", []):
        archetype_id = blocked.get("primary_archetype")
        if not archetype_id:
            continue
        card = cards.get(archetype_id, {})
        missing = list(blocked.get("source_pending_gap_primitives") or blocked.get("missing_required_primitives") or [])
        for primitive in missing:
            route_priority = [
                {
                    "source_family": route["source_family"],
                    "route_role": route["route_role"],
                    "official_first_required": route["official_first_required"],
                }
                for route in routes.get((archetype_id, primitive), [])
                if route["route_role"] != "FORBIDDEN_FOR_SCORE"
            ]
            tasks.append(
                {
                    "schema_version": "e2r_research_memory_followup_task_v1",
                    "task_id": f"RMFOLLOW-{blocked.get('symbol')}-{archetype_id}-{primitive}",
                    "symbol": blocked.get("symbol"),
                    "company_name": blocked.get("company_name"),
                    "archetype_id": archetype_id,
                    "missing_primitive": primitive,
                    "why_this_primitive_matters": (
                        f"{primitive} is required by the archetype memory card before the production thesis can be treated as complete."
                    ),
                    "source_route_priority": route_priority,
                    "query_intents": [
                        f"Ask LLM for bounded official-first ways to verify current {primitive}; do not create deterministic query strings."
                    ],
                    "disallowed_sources": ["snippet_only_score", "source_proxy_only", "evidence_url_pending"],
                    "success_condition": "accepted current direct claim with anchor mapped to missing primitive",
                    "expected_claim_schema": {
                        "target_scope_status": "DIRECT",
                        "temporal_status": "CURRENT",
                        "mapping_status": "ACCEPTED",
                        "primitive_id": primitive,
                    },
                    "fallback_if_not_found": "PENDING_SOURCE",
                    "memory_card_policy": card.get("runtime_usage_policy"),
                }
            )
    by_arch: dict[str, int] = {}
    for task in tasks:
        by_arch[task["archetype_id"]] = by_arch.get(task["archetype_id"], 0) + 1
    return {
        "schema_version": "e2r_research_memory_followup_task_audit_v1",
        "task_count": len(tasks),
        "blocked_candidate_count": len(runner.get("blocked_candidates", [])),
        "tasks_by_archetype": dict(sorted(by_arch.items())),
        "tasks": tasks,
        "all_tasks_use_memory_card_or_route": all(task["source_route_priority"] for task in tasks),
    }


def write_research_memory_followup_task_audit(*, docs_dir: str | Path = "docs/operational") -> dict[str, Any]:
    docs = Path(docs_dir)
    docs.mkdir(parents=True, exist_ok=True)
    payload = build_research_memory_followup_tasks(docs_dir=docs)
    path = docs / "research_memory_followup_task_audit.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload


__all__ = ["build_research_memory_followup_tasks", "write_research_memory_followup_task_audit"]
