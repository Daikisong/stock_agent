"""Build Goal4 next-run attempt plans from the all-archetype status matrix."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Mapping


DISCOVERY_ONLY_FAMILIES = {"GeneralWebSearch", "NaverSearch", "ResearchMemory"}
FORBIDDEN_SOURCE_CLASSES = [
    "snippet_only_score",
    "source_proxy_only",
    "evidence_url_pending",
    "unbounded_general_search",
]
DEFAULT_FALLBACK_SOURCE_CLASSES = [
    "TrustedNews",
    "ReportPDF",
    "BrokerReportPublicPDF",
    "CompanyNewsroom",
    "NaverSearch",
    "GeneralWebSearch",
]
PLACEHOLDER_SYMBOLS = {"", "000000", "0000000", "UNKNOWN", "N/A", "NONE", "NULL"}


def _stable_id(prefix: str, *parts: object, length: int = 20) -> str:
    raw = "|".join(str(part) for part in parts)
    digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:length]
    return f"{prefix}-{digest}"


def _prefix(archetype_id: str) -> str:
    return archetype_id.split("_", 1)[0]


def _route_priority(card: Mapping[str, Any], primitive_id: str) -> list[dict[str, Any]]:
    routes = list((card.get("source_route_priority_by_primitive") or {}).get(primitive_id) or [])
    filtered = [
        {
            "source_family": route.get("source_family"),
            "route_role": route.get("route_role"),
            "official_first_required": bool(route.get("official_first_required")),
            "requires_full_source": bool(route.get("requires_full_source")),
        }
        for route in routes
        if route.get("route_role") != "FORBIDDEN_FOR_SCORE"
    ]
    return filtered


def _preferred_sources(route_priority: Iterable[Mapping[str, Any]]) -> list[str]:
    preferred: list[str] = []
    for route in route_priority:
        role = route.get("route_role")
        family = str(route.get("source_family") or "")
        if not family or family in DISCOVERY_ONLY_FAMILIES:
            continue
        if role in {"PRIMARY", "SECONDARY"} and family not in preferred:
            preferred.append(family)
    return preferred or ["DART", "KIND", "IssuerIR", "CompanyGuide"]


def _fallback_sources(route_priority: Iterable[Mapping[str, Any]]) -> list[str]:
    fallback: list[str] = []
    for route in route_priority:
        family = str(route.get("source_family") or "")
        if not family:
            continue
        if route.get("route_role") in {"FALLBACK", "DISCOVERY_ONLY"} and family not in fallback:
            fallback.append(family)
    for family in DEFAULT_FALLBACK_SOURCE_CLASSES:
        if family not in fallback:
            fallback.append(family)
    return fallback


def _candidate_primitives(row: Mapping[str, Any], card: Mapping[str, Any], *, max_primitives: int) -> list[str]:
    required = list(card.get("required_positive_primitives") or [])
    green = list(card.get("green_unlock_primitives") or [])
    stage2 = list(card.get("stage2_actionable_primitives") or [])
    ordered: list[str] = []
    for primitive in required + green + stage2:
        if primitive and primitive not in ordered:
            ordered.append(str(primitive))
    return ordered[:max_primitives]


def _attempt_priority(row: Mapping[str, Any]) -> int:
    proof = row.get("runtime_parity_proof_status")
    if proof == "NOT_PROVEN_SCORE_PATH_ONLY":
        return 10
    if proof == "NOT_PROVEN_BLOCKED_BY_MATERIAL_GAP":
        return 20
    if proof == "NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM":
        return 30
    if proof == "NOT_PROVEN_ACCEPTED_CLAIM_NOT_CLOSED":
        return 40
    if proof == "NOT_PROVEN_PLANNER_ONLY":
        return 50
    if proof == "NOT_PROVEN_REPLAY_ONLY":
        return 60
    return 90


def _attempt_type(row: Mapping[str, Any]) -> str:
    proof = row.get("runtime_parity_proof_status")
    if proof == "NOT_PROVEN_SCORE_PATH_ONLY":
        return "PROMOTED_SCORE_PATH_GAP_CLOSURE"
    if proof == "NOT_PROVEN_BLOCKED_BY_MATERIAL_GAP":
        return "BLOCKED_CANDIDATE_GAP_CLOSURE"
    if proof == "NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM":
        return "SOURCE_EXECUTION_REPAIR"
    if proof == "NOT_PROVEN_ACCEPTED_CLAIM_NOT_CLOSED":
        return "ACCEPTED_CLAIM_TO_FULL_THESIS_CLOSURE"
    if proof == "NOT_PROVEN_PLANNER_ONLY":
        return "PLANNER_TO_SOURCE_TASK_MATERIALIZATION"
    if proof == "NOT_PROVEN_REPLAY_ONLY":
        return "REPLAY_TO_PRODUCTION_RUNTIME_ATTEMPT"
    return "RUNTIME_PARITY_MONITORING"


def _symbols_for_attempt(row: Mapping[str, Any]) -> list[str | None]:
    symbols = list(row.get("blocked_symbols") or row.get("full_thesis_symbols") or [])
    if not symbols:
        symbols = list(row.get("symbols_sample") or [])
    clean_symbols = [
        str(symbol)
        for symbol in symbols
        if symbol is not None and str(symbol).strip().upper() not in PLACEHOLDER_SYMBOLS
    ]
    if clean_symbols:
        return clean_symbols[:2]
    return [None]


def build_all_archetype_next_runtime_attempt_plan(
    *,
    status_matrix: Mapping[str, Any],
    memory_cards: Mapping[str, Any],
    max_primitives_per_archetype: int = 3,
) -> dict[str, Any]:
    cards_by_id = {card["archetype_id"]: card for card in memory_cards.get("cards", [])}
    plan_rows: list[dict[str, Any]] = []
    source_tasks: list[dict[str, Any]] = []
    seed_events: list[dict[str, Any]] = []
    as_of_date = status_matrix.get("as_of_date") or "2026-07-05"

    for row in status_matrix.get("rows", []):
        archetype_id = str(row["archetype_id"])
        proof_status = row.get("runtime_parity_proof_status")
        if proof_status == "RUNTIME_PARITY_PROVEN":
            continue
        card = cards_by_id.get(archetype_id, {})
        primitives = _candidate_primitives(row, card, max_primitives=max_primitives_per_archetype)
        if not primitives:
            primitives = ["archetype_current_positive_bridge"]
        attempt_id = _stable_id("RTATTEMPT", as_of_date, archetype_id, proof_status)
        symbols = _symbols_for_attempt(row)
        plan_rows.append(
            {
                "schema_version": "e2r_all_archetype_next_runtime_attempt_row_v1",
                "attempt_id": attempt_id,
                "archetype_id": archetype_id,
                "archetype_prefix": _prefix(archetype_id),
                "priority": _attempt_priority(row),
                "attempt_type": _attempt_type(row),
                "current_runtime_parity_proof_status": proof_status,
                "current_runtime_attempt_status": row.get("runtime_attempt_status"),
                "current_source_execution_status": row.get("runtime_source_route_execution_status"),
                "current_accepted_claim_status": row.get("accepted_claim_status"),
                "current_full_thesis_status": row.get("full_thesis_status"),
                "target_symbol_mode": "SYMBOL_SPECIFIC" if symbols != [None] else "ARCHETYPE_LEVEL_DISCOVERY",
                "target_symbols": [symbol for symbol in symbols if symbol],
                "primitive_attempts": primitives,
                "score_allowed_before_execution": False,
                "stage_promotion_allowed_before_execution": False,
                "llm_query_required": True,
                "hardcoded_queries": [],
                "hardcoded_query_count": 0,
                "next_required_action": row.get("next_required_action"),
                "status_reason_ko": row.get("status_reason_ko"),
            }
        )
        for primitive in primitives:
            route_priority = _route_priority(card, primitive)
            for symbol in symbols:
                task_id = _stable_id("RTTASK", as_of_date, archetype_id, primitive, symbol or "DISCOVERY")
                source_task = {
                    "schema_version": "e2r_all_archetype_next_runtime_source_task_v1",
                    "task_id": task_id,
                    "attempt_id": attempt_id,
                    "task_type": "runtime_parity_gap_closure",
                    "task_status": "PLANNING_REQUIRED",
                    "source_task_origin": "all_archetype_runtime_status_matrix",
                    "as_of_date": as_of_date,
                    "symbol": symbol,
                    "target_symbol_mode": "SYMBOL_SPECIFIC" if symbol else "ARCHETYPE_LEVEL_DISCOVERY",
                    "archetype_id": archetype_id,
                    "primitive_gap": primitive,
                    "current_runtime_parity_proof_status": proof_status,
                    "preferred_source_classes": _preferred_sources(route_priority),
                    "fallback_source_classes": _fallback_sources(route_priority),
                    "forbidden_source_classes": FORBIDDEN_SOURCE_CLASSES,
                    "official_first_required": True,
                    "general_search_allowed": True,
                    "llm_query_required": True,
                    "llm_query_allowed": True,
                    "query_intents": [
                        (
                            "Ask the LLM planner for bounded official-first queries that verify current, "
                            f"direct target-company evidence for primitive `{primitive}`."
                        )
                    ],
                    "hardcoded_queries": [],
                    "hardcoded_query_count": 0,
                    "max_queries": 3,
                    "max_queries_per_task": 3,
                    "max_candidates": 20,
                    "max_candidates_per_query": 20,
                    "max_fetches": 3,
                    "max_fetches_per_task": 3,
                    "date_window": {"end": as_of_date, "lookback_days": 730},
                    "stop_condition": {
                        "accepted_claim_count": 1,
                        "counter_claim_check_done": True,
                        "source_budget_exhausted_status": "SOURCE_PENDING",
                    },
                    "score_allowed_before_execution": False,
                    "stage_promotion_allowed_before_execution": False,
                    "next_actions": [
                        "ASK_LLM_PLANNER_FOR_MISSING_PRIMITIVE_QUERY",
                        "RUN_BOUNDED_OFFICIAL_FIRST_SOURCE_TASK",
                        "EXTRACT_EVIDENCE_OS_CLAIM",
                        "RETRY_FULL_THESIS_STAGECOURT_IF_MATERIAL",
                    ],
                    "route_priority": route_priority,
                }
                source_tasks.append(source_task)
                seed_events.append(
                    {
                        "schema_version": "e2r_all_archetype_next_runtime_seed_event_v1",
                        "candidate_event_id": _stable_id("CEV4-RTATTEMPT", as_of_date, archetype_id, primitive, symbol or "DISCOVERY"),
                        "event_type": "all_archetype_runtime_parity_follow_up_seed",
                        "event_date": as_of_date,
                        "detected_at": as_of_date,
                        "symbol": symbol,
                        "target_symbol_mode": source_task["target_symbol_mode"],
                        "target_archetype": archetype_id,
                        "target_archetype_status": "RUNTIME_PARITY_FOLLOW_UP_REQUIRED",
                        "primitive_gap": primitive,
                        "follow_up_task_id": task_id,
                        "seed_role": "planner_input_only",
                        "research_brain_eligible": True,
                        "score_evidence_allowed": False,
                        "stage_promotion_allowed_before_execution": False,
                        "source_family": "AllArchetypeRuntimeParityFollowUp",
                        "raw_reason_codes": [
                            "GOAL4_RUNTIME_PARITY_FOLLOW_UP",
                            archetype_id,
                            str(proof_status),
                            primitive,
                        ],
                        "event_summary": (
                            f"planner input only. archetype_id={archetype_id}; primitive_gap={primitive}; "
                            "source-backed Evidence OS claim required before any production score/stage use"
                        ),
                        "structured_payload": {
                            "attempt_id": attempt_id,
                            "follow_up_task_id": task_id,
                            "target_archetype": archetype_id,
                            "target_archetype_status": "RUNTIME_PARITY_FOLLOW_UP_REQUIRED",
                            "primitive_gap": primitive,
                            "target_symbol_mode": source_task["target_symbol_mode"],
                            "seed_role": "planner_input_only",
                            "follow_up_origin": "all_archetype_runtime_status_matrix",
                            "preferred_source_classes": source_task["preferred_source_classes"],
                            "fallback_source_classes": source_task["fallback_source_classes"],
                            "forbidden_source_classes": source_task["forbidden_source_classes"],
                            "official_first_required": True,
                            "llm_query_required": True,
                            "query_intents": source_task["query_intents"],
                            "hardcoded_queries": [],
                            "hardcoded_query_count": 0,
                            "max_queries": 3,
                            "max_candidates": 20,
                            "max_fetches": 3,
                            "date_window": source_task["date_window"],
                            "stop_condition": source_task["stop_condition"],
                        },
                    }
                )

    plan_rows.sort(key=lambda item: (int(item["priority"]), str(item["archetype_id"])))
    source_tasks.sort(key=lambda item: (str(item["archetype_id"]), str(item["primitive_gap"]), str(item.get("symbol"))))
    seed_events.sort(key=lambda item: (str(item["target_archetype"]), str(item["primitive_gap"]), str(item.get("symbol"))))
    by_attempt_type = Counter(row["attempt_type"] for row in plan_rows)
    by_symbol_mode = Counter(row["target_symbol_mode"] for row in plan_rows)
    return {
        "schema_version": "e2r_all_archetype_next_runtime_attempt_plan_v1",
        "as_of_date": as_of_date,
        "plan_row_count": len(plan_rows),
        "source_task_count": len(source_tasks),
        "seed_event_count": len(seed_events),
        "attempt_type_counts": dict(sorted(by_attempt_type.items())),
        "target_symbol_mode_counts": dict(sorted(by_symbol_mode.items())),
        "all_tasks_score_blocked_before_execution": all(
            not task["score_allowed_before_execution"] and not task["stage_promotion_allowed_before_execution"]
            for task in source_tasks
        ),
        "all_tasks_require_llm_query_generation": all(task["llm_query_required"] for task in source_tasks),
        "all_tasks_have_no_hardcoded_queries": all(task["hardcoded_query_count"] == 0 and not task["hardcoded_queries"] for task in source_tasks),
        "all_tasks_have_finite_budget": all(
            task["max_queries"] is not None and task["max_candidates"] is not None and task["max_fetches"] is not None
            for task in source_tasks
        ),
        "production_score_ready": False,
        "plan_rows": plan_rows,
        "source_tasks": source_tasks,
        "seed_events": seed_events,
    }


def render_all_archetype_next_runtime_attempt_plan_markdown(plan: Mapping[str, Any]) -> str:
    lines = [
        "# All Archetype Next Runtime Attempt Plan - 2026-07-05",
        "",
        "이 문서는 전수 runtime status matrix의 `next_required_action`을 다음 실행 입력으로 바꾼다.",
        "",
        "쉬운 예: 상태표가 'C08은 아직 production에서 검사하지 않았다'고 말하면, 이 문서는 'C08을 어떤 primitive와 source route로 다음 검사에 넣을지'를 적는다.",
        "",
        "## Summary",
        "",
        f"- plan_row_count: `{plan['plan_row_count']}`",
        f"- source_task_count: `{plan['source_task_count']}`",
        f"- seed_event_count: `{plan['seed_event_count']}`",
        f"- attempt_type_counts: `{json.dumps(plan['attempt_type_counts'], ensure_ascii=False, sort_keys=True)}`",
        f"- target_symbol_mode_counts: `{json.dumps(plan['target_symbol_mode_counts'], ensure_ascii=False, sort_keys=True)}`",
        f"- all_tasks_score_blocked_before_execution: `{plan['all_tasks_score_blocked_before_execution']}`",
        f"- all_tasks_require_llm_query_generation: `{plan['all_tasks_require_llm_query_generation']}`",
        f"- all_tasks_have_no_hardcoded_queries: `{plan['all_tasks_have_no_hardcoded_queries']}`",
        f"- all_tasks_have_finite_budget: `{plan['all_tasks_have_finite_budget']}`",
        "",
        "## Plan Rows",
        "",
        "| archetype | priority | attempt type | symbol mode | primitives | current proof |",
        "|---|---:|---|---|---|---|",
    ]
    for row in plan.get("plan_rows", []):
        lines.append(
            "| {archetype} | {priority} | {attempt_type} | {symbol_mode} | {primitives} | {proof} |".format(
                archetype=row["archetype_id"],
                priority=row["priority"],
                attempt_type=row["attempt_type"],
                symbol_mode=row["target_symbol_mode"],
                primitives=", ".join(row["primitive_attempts"]),
                proof=row["current_runtime_parity_proof_status"],
            )
        )
    lines.extend(
        [
            "",
            "## Safety",
            "",
            "이 plan은 점수를 만들지 않는다. 모든 source task는 LLM query generation과 source-backed Evidence OS claim을 요구하며, 실행 전 score/stage promotion은 금지된다.",
            "",
        ]
    )
    return "\n".join(lines)


def _write_jsonl(path: Path, rows: list[Mapping[str, Any]]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def write_all_archetype_next_runtime_attempt_plan(
    *,
    status_matrix: Mapping[str, Any],
    memory_cards: Mapping[str, Any],
    docs_dir: str | Path = "docs/operational",
) -> dict[str, Any]:
    docs_path = Path(docs_dir)
    docs_path.mkdir(parents=True, exist_ok=True)
    plan = build_all_archetype_next_runtime_attempt_plan(
        status_matrix=status_matrix,
        memory_cards=memory_cards,
    )
    json_path = docs_path / "all_archetype_next_runtime_attempt_plan_2026-07-05.json"
    alias_json_path = docs_path / "all_archetype_next_runtime_attempt_plan.json"
    markdown_path = docs_path / "all_archetype_next_runtime_attempt_plan_2026-07-05.md"
    source_task_path = docs_path / "all_archetype_next_runtime_source_tasks_2026-07-05.jsonl"
    seed_event_path = docs_path / "all_archetype_next_runtime_seed_events_2026-07-05.jsonl"
    json_text = json.dumps(plan, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    json_path.write_text(json_text, encoding="utf-8")
    alias_json_path.write_text(json_text, encoding="utf-8")
    markdown_path.write_text(render_all_archetype_next_runtime_attempt_plan_markdown(plan), encoding="utf-8")
    _write_jsonl(source_task_path, plan["source_tasks"])
    _write_jsonl(seed_event_path, plan["seed_events"])
    return {
        "plan": plan,
        "json_path": json_path,
        "alias_json_path": alias_json_path,
        "markdown_path": markdown_path,
        "source_task_path": source_task_path,
        "seed_event_path": seed_event_path,
    }


__all__ = [
    "build_all_archetype_next_runtime_attempt_plan",
    "render_all_archetype_next_runtime_attempt_plan_markdown",
    "write_all_archetype_next_runtime_attempt_plan",
]
