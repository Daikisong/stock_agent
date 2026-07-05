"""Build runtime memory cards from research reverse-engineering records."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping

from e2r.source_routing.research_source_route_recovery import build_source_route_patterns


def _load_contracts(repo_root: Path) -> list[dict[str, Any]]:
    return json.loads(
        (repo_root / "configs" / "e2r_archetype_evidence_contracts_v12.json").read_text(encoding="utf-8")
    )["contracts"]


def _runtime_policy(*, url_count: int, proxy_count: int, source_gap: bool) -> str:
    if source_gap:
        return "SOURCE_REPAIR_REQUIRED"
    if url_count:
        return "READY_FOR_ROUTING"
    if proxy_count:
        return "PLANNING_ONLY"
    return "SOURCE_REPAIR_REQUIRED"


def build_runtime_memory_cards(
    *,
    repo_root: str | Path = ".",
    records: Iterable[Mapping[str, Any]],
) -> dict[str, Any]:
    root = Path(repo_root)
    contracts = _load_contracts(root)
    records = list(records)
    by_arch: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for record in records:
        by_arch[str(record["canonical_archetype_id"])].append(record)
    route_patterns = build_source_route_patterns(repo_root=root, records=records)
    routes_by_arch_primitive: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for pattern in route_patterns["patterns"]:
        routes_by_arch_primitive[pattern["archetype_id"]][pattern["primitive_id"]].append(pattern)

    cards: list[dict[str, Any]] = []
    prompt_payloads: list[dict[str, Any]] = []
    for contract in contracts:
        archetype_id = contract["canonical_archetype_id"]
        arch_records = by_arch.get(archetype_id, [])
        url_cases = [record["research_case_id"] for record in arch_records if record["source_quality"] == "A2_URL_BACKED"]
        proxy_cases = [record["research_case_id"] for record in arch_records if record["source_proxy_only"]]
        pending_cases = [record["research_case_id"] for record in arch_records if record["evidence_url_pending"]]
        required = list(contract.get("required_primitives") or [])
        positive = list(contract.get("positive_primitives") or required)
        green = list(contract.get("green_gate_primitives") or positive[:3])
        source_route_priority = {
            primitive: [
                {
                    "source_family": route["source_family"],
                    "route_role": route["route_role"],
                    "official_first_required": route["official_first_required"],
                    "requires_full_source": route["requires_full_source"],
                }
                for route in routes_by_arch_primitive[archetype_id].get(primitive, [])
            ]
            for primitive in required
        }
        card = {
            "schema_version": "e2r_archetype_runtime_memory_card_v2",
            "archetype_id": archetype_id,
            "large_sector_id": contract.get("large_sector_id"),
            "canonical_mechanism": contract.get("runtime_bridge_group") or archetype_id,
            "positive_unlock_primitives": positive,
            "stage2_actionable_primitives": positive[: max(1, min(2, len(positive)))],
            "yellow_unlock_primitives": positive[: max(1, min(3, len(positive)))],
            "green_unlock_primitives": green,
            "required_positive_primitives": required,
            "green_blockers": sorted({item for record in arch_records for item in record.get("green_blockers", [])}),
            "4b_watch_patterns": sorted({record["research_case_id"] for record in arch_records if record["case_role"] == "4B"})[:20],
            "4c_hard_break_patterns": sorted({record["research_case_id"] for record in arch_records if record["case_role"] == "4C"})[:20],
            "false_positive_patterns": sorted(
                {item for record in arch_records for item in record.get("false_positive_patterns", [])}
            ),
            "source_route_priority_by_primitive": source_route_priority,
            "source_family_success_examples": url_cases[:20],
            "source_family_failure_examples": pending_cases[:20],
            "url_backed_replay_cases": url_cases[:50],
            "source_proxy_only_cases": proxy_cases[:50],
            "evidence_url_pending_cases": pending_cases[:50],
            "runtime_query_intent_templates": [
                {
                    "primitive_id": primitive,
                    "intent": f"LLM should propose source-backed ways to verify current {primitive} for the target company.",
                }
                for primitive in required
            ],
            "do_not_promote_rules": [
                "ResearchMemory rows are planning-only.",
                "source_proxy_only and evidence_url_pending rows cannot score.",
                "price-path/outcome labels are excluded from runtime planner payload.",
            ],
            "source_gap_repair_tasks": [
                {
                    "primitive_id": primitive,
                    "repair_task": "find_current_source_backed_anchor_or_record_source_blocker",
                }
                for primitive in required
                if not source_route_priority.get(primitive)
            ],
            "confidence": "HIGH" if url_cases else ("MEDIUM" if proxy_cases else "LOW"),
            "runtime_usage_policy": _runtime_policy(
                url_count=len(url_cases), proxy_count=len(proxy_cases), source_gap=not bool(arch_records)
            ),
        }
        cards.append(card)
        prompt_payloads.append(
            {
                "archetype_id": archetype_id,
                "required_positive_primitives": required,
                "source_route_priority_by_primitive": source_route_priority,
                "runtime_query_intent_templates": card["runtime_query_intent_templates"],
                "do_not_promote_rules": card["do_not_promote_rules"],
            }
        )
    return {
        "schema_version": "e2r_research_runtime_memory_cards_v2",
        "card_count": len(cards),
        "cards": cards,
        "runtime_planner_payloads": prompt_payloads,
    }


def build_memory_card_matrix(cards_payload: Mapping[str, Any]) -> dict[str, Any]:
    rows = []
    for card in cards_payload.get("cards", []):
        routes = card.get("source_route_priority_by_primitive", {})
        route_covered = sum(1 for value in routes.values() if value)
        required_count = len(card.get("required_positive_primitives", []))
        rows.append(
            {
                "archetype_id": card["archetype_id"],
                "runtime_usage_policy": card["runtime_usage_policy"],
                "confidence": card["confidence"],
                "required_positive_primitive_count": required_count,
                "source_route_covered_primitive_count": route_covered,
                "url_backed_replay_case_count": len(card.get("url_backed_replay_cases", [])),
                "source_proxy_only_case_count": len(card.get("source_proxy_only_cases", [])),
                "evidence_url_pending_case_count": len(card.get("evidence_url_pending_cases", [])),
            }
        )
    return {
        "schema_version": "e2r_research_runtime_memory_card_matrix_v2",
        "card_count": len(rows),
        "ready_for_routing_count": sum(1 for row in rows if row["runtime_usage_policy"] == "READY_FOR_ROUTING"),
        "source_repair_required_count": sum(
            1 for row in rows if row["runtime_usage_policy"] == "SOURCE_REPAIR_REQUIRED"
        ),
        "planning_only_count": sum(1 for row in rows if row["runtime_usage_policy"] == "PLANNING_ONLY"),
        "rows": rows,
    }


__all__ = ["build_memory_card_matrix", "build_runtime_memory_cards"]
