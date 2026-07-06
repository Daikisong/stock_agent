"""Build Goal4 next-run attempt plans from the all-archetype status matrix."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Mapping

from e2r.census.placeholder_symbols import is_placeholder_symbol, normalized_real_symbol


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

SOURCE_QUALITY_PRIORITY = {
    "A2_URL_BACKED": 60,
    "EVIDENCE_URL_PENDING": 40,
    "SOURCE_PROXY_ONLY": 30,
    "PRICE_PATH_ONLY": 5,
    "SHADOW_ONLY": 1,
}

CLAIM_FAILURE_REPAIR_ACTIONS = {
    "ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE": [
        "DO_NOT_ACCEPT_GENERIC_DISCLOSURE_PROFILE_AS_PRIMITIVE_EVIDENCE",
        "ASK_LLM_FOR_PRIMITIVE_SPECIFIC_SOURCE_OR_SECTION_ROUTE",
        "FETCH_FULL_SOURCE_ANCHOR_BEFORE_MAPPING_RETRY",
    ],
    "ROUTE_SIGNAL_FAMILY_MISMATCH": [
        "ASK_LLM_TO_MATCH_SOURCE_FAMILY_TO_PRIMITIVE_FAMILY",
        "REJECT_PREVIOUS_MISMATCHED_SOURCE_FAMILY_AS_SCORE_INPUT",
        "REPLAN_SOURCE_TASK_BEFORE_MAPPING_RETRY",
    ],
    "SOURCE_CLASS_DOCUMENT_TYPE_MISMATCH": [
        "ASK_LLM_FOR_DOCUMENT_TYPE_COMPATIBLE_WITH_PRIMITIVE",
        "VALIDATE_SOURCE_CLASS_BEFORE_FETCH_SELECTION",
    ],
    "TARGET_SCOPE_NOT_DIRECT": [
        "ASK_LLM_FOR_DIRECT_TARGET_COMPANY_SOURCE",
        "RECHECK_ENTITY_RELATION_BEFORE_SCORE_ELIGIBILITY",
    ],
    "SEMANTIC_REJECTED": [
        "ASK_LLM_TO_EXTRACT_ONLY_LITERAL_SOURCE_BACKED_CLAIMS",
        "RETRY_WITH_REJECTION_REASON_FEEDBACK",
    ],
    "ANCHOR_OR_SOURCE_LINEAGE_REJECTED": [
        "REPAIR_ORIGINAL_SOURCE_ANCHOR",
        "REQUIRE_CANONICAL_SOURCE_OR_STABLE_DOCUMENT_LOCATOR",
    ],
    "PROVIDER_ERROR_SCORE_BLOCK": [
        "RESOLVE_PROVIDER_OR_RECORD_EXTERNAL_BLOCKER",
        "DO_NOT_CONVERT_PROVIDER_FAILURE_TO_LOW_SCORE",
    ],
    "PRIMITIVE_MAPPING_REJECTED": [
        "ASK_LLM_FOR_CLAIM_THAT_DIRECTLY_SATISFIES_REQUIRED_PRIMITIVE",
        "INSPECT_EVIDENCE_CONTRACT_MAPPING_BEFORE_SCORE_RETRY",
    ],
    "MAPPING_NOT_ACCEPTED": [
        "RETRY_MAPPING_ONLY_AFTER_NEW_SOURCE_BACKED_CLAIM",
        "DO_NOT_PROMOTE_REJECTED_MAPPING_TO_SCORE",
    ],
}

CLAIM_FAILURE_REPAIR_HINT_BY_MODE = {
    "ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE": "REROUTE_TO_PRIMITIVE_SPECIFIC_SECTION_OR_SOURCE",
    "ROUTE_SIGNAL_FAMILY_MISMATCH": "REPLAN_SOURCE_TASK_TO_MATCH_PRIMITIVE_FAMILY",
    "SOURCE_CLASS_DOCUMENT_TYPE_MISMATCH": "FIX_SOURCE_CLASS_OR_DOCUMENT_TYPE_ROUTE",
    "TARGET_SCOPE_NOT_DIRECT": "TIGHTEN_TARGET_ENTITY_FILTER_OR_RELATION_ADJUDICATION",
    "SEMANTIC_REJECTED": "RECHECK_EXTRACTOR_SEMANTICS_OR_QUERY_INTENT",
    "ANCHOR_OR_SOURCE_LINEAGE_REJECTED": "REPAIR_ORIGINAL_SOURCE_ANCHOR_LINEAGE",
    "PROVIDER_ERROR_SCORE_BLOCK": "RESOLVE_PROVIDER_OR_MARK_EXTERNAL_BLOCKER",
    "PRIMITIVE_MAPPING_REJECTED": "INSPECT_MAPPER_VS_EVIDENCE_CONTRACT_FOR_THIS_PRIMITIVE",
    "MAPPING_NOT_ACCEPTED": "INSPECT_MAPPING_DECISION_AND_REQUIRED_PRIMITIVE",
}


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


def _claim_failure_primary_mode(row: Mapping[str, Any]) -> str | None:
    mode = row.get("claim_failure_primary_mode")
    return str(mode) if mode else None


def _claim_failure_repair_hint(row: Mapping[str, Any], primary_mode: str | None) -> str | None:
    hint = row.get("claim_failure_repair_hint")
    if hint:
        return str(hint)
    if primary_mode:
        return CLAIM_FAILURE_REPAIR_HINT_BY_MODE.get(primary_mode)
    return None


def _claim_failure_top_modes(row: Mapping[str, Any]) -> list[dict[str, Any]]:
    modes = row.get("claim_failure_top_modes") or []
    if not isinstance(modes, list):
        return []
    normalized: list[dict[str, Any]] = []
    for item in modes:
        if not isinstance(item, Mapping):
            continue
        mode = item.get("mode")
        if not mode:
            continue
        normalized.append({"mode": str(mode), "count": int(item.get("count") or 0)})
    return normalized


def _source_route_repair_actions(primary_mode: str | None) -> list[str]:
    if not primary_mode:
        return []
    return list(CLAIM_FAILURE_REPAIR_ACTIONS.get(primary_mode, ["INSPECT_REJECTED_CLAIM_SAMPLE"]))


def _planner_failure_feedback(
    *,
    row: Mapping[str, Any],
    primitive: str,
    primary_mode: str | None,
    repair_hint: str | None,
    repair_actions: list[str],
) -> dict[str, Any]:
    return {
        "previous_claim_failure_primary_mode": primary_mode,
        "previous_claim_failure_repair_hint": repair_hint,
        "previous_claim_failure_top_modes": _claim_failure_top_modes(row),
        "previous_top_claim_rejection_reasons": row.get("claim_mapping_top_rejection_reasons") or [],
        "source_route_repair_actions": repair_actions,
        "score_evidence_allowed_from_previous_rejected_claims": False,
        "primitive_gap": primitive,
    }


def _success_condition(*, archetype_id: str, primitive: str, symbol: str | None) -> str:
    target = f"symbol `{symbol}`" if symbol else f"a real current target symbol for `{archetype_id}`"
    return (
        f"Create at least one accepted Evidence OS claim for primitive `{primitive}` on {target}. "
        "The claim must have direct target-company scope, a verified source anchor, current/as-of-valid "
        "temporal status, accepted primitive mapping, and no source_proxy_only/evidence_url_pending/snippet-only "
        "score contribution."
    )


def _expected_claim_schema(*, archetype_id: str, primitive: str, symbol: str | None) -> dict[str, Any]:
    return {
        "schema_version": "e2r_expected_runtime_parity_claim_v1",
        "archetype_id": archetype_id,
        "primitive_id": primitive,
        "symbol": symbol,
        "target_scope_status": "DIRECT",
        "temporal_status": "CURRENT_OR_AS_OF_VALID",
        "anchor_status": "VERIFIED_SOURCE_ANCHOR",
        "semantic_status": "PASS",
        "mapping_status": "ACCEPTED",
        "required_claim_status": "ACCEPTED_FOR_SCORE",
        "score_forbidden_until_claim_accepted": True,
        "forbidden_source_classes": list(FORBIDDEN_SOURCE_CLASSES),
    }


def _fallback_if_not_found(
    *,
    row: Mapping[str, Any],
    symbol: str | None,
    primary_mode: str | None,
) -> str:
    if symbol is None or row.get("runtime_parity_proof_status") == "NOT_PROVEN_TARGET_MATERIALIZATION_REQUIRED":
        return "TARGET_MATERIALIZATION_REQUIRED"
    if primary_mode == "PROVIDER_ERROR_SCORE_BLOCK":
        return "PENDING_SOURCE"
    if row.get("runtime_parity_proof_status") in {
        "NOT_PROVEN_SCORE_PATH_ONLY",
        "NOT_PROVEN_BLOCKED_BY_MATERIAL_GAP",
    }:
        return "PENDING_MATERIAL_GAP"
    return "SOURCE_REPAIR_REQUIRED"


def _failure_feedback_intent(
    *,
    primary_mode: str | None,
    repair_hint: str | None,
    repair_actions: list[str],
) -> str | None:
    if not primary_mode and not repair_actions:
        return None
    base = (
        "Previous runtime attempt failed before accepted claim creation. "
        f"primary_failure_mode={primary_mode or 'UNKNOWN'}; "
        f"repair_hint={repair_hint or 'INSPECT_REJECTED_CLAIM_SAMPLE'}; "
        f"required_repair_actions={', '.join(repair_actions) if repair_actions else 'INSPECT_REJECTED_CLAIM_SAMPLE'}."
    )
    if primary_mode == "ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE":
        return (
            base
            + " Do not reuse generic disclosure cover/profile/company overview text as score evidence; "
            "ask the LLM planner for a source or document section that directly states the missing primitive."
        )
    if primary_mode == "ROUTE_SIGNAL_FAMILY_MISMATCH":
        return (
            base
            + " The next source task must match the primitive family; a contract-style source cannot satisfy "
            "a clinical/regulatory/retention/spread primitive unless the source text directly states that primitive."
        )
    if primary_mode == "SOURCE_CLASS_DOCUMENT_TYPE_MISMATCH":
        return base + " Validate source class and document type before fetch selection."
    if primary_mode == "TARGET_SCOPE_NOT_DIRECT":
        return base + " Require direct target-company scope or explicit accepted relation adjudication before score use."
    if primary_mode == "PROVIDER_ERROR_SCORE_BLOCK":
        return base + " Provider failure must remain Source Pending or external blocker, not a low score."
    return base + " Feed the prior rejection reason to the LLM planner and require a new source-backed claim before retry."


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
    if proof == "NOT_PROVEN_TARGET_MATERIALIZATION_REQUIRED":
        return 25
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
    if proof == "NOT_PROVEN_TARGET_MATERIALIZATION_REQUIRED":
        return "ARCHETYPE_TARGET_MATERIALIZATION"
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
        if symbol is not None and not is_placeholder_symbol(symbol)
    ]
    if clean_symbols:
        return clean_symbols[:2]
    return [None]


def _case_records(case_inventory: Mapping[str, Any] | None) -> list[Mapping[str, Any]]:
    if not case_inventory:
        return []
    records = case_inventory.get("records") or case_inventory.get("case_records") or []
    if not isinstance(records, list):
        return []
    return [record for record in records if isinstance(record, Mapping)]


def _case_file_matches_archetype(source_file: str, archetype_id: str) -> bool:
    return archetype_id in source_file


def _case_file_mentions_prefix(source_file: str, archetype_id: str) -> bool:
    prefix = _prefix(archetype_id)
    return bool(re.search(rf"(^|[^A-Z0-9]){re.escape(prefix)}([^A-Z0-9]|$)", source_file))


def _materialization_candidate_score(archetype_id: str, record: Mapping[str, Any]) -> int:
    source_file = str(record.get("source_file") or "")
    score = 0
    if _case_file_matches_archetype(source_file, archetype_id):
        score += 300
    elif _case_file_mentions_prefix(source_file, archetype_id):
        score += 150
    if source_file.startswith("docs/round/"):
        score += 100
    score += SOURCE_QUALITY_PRIORITY.get(str(record.get("source_quality") or ""), 0)
    if record.get("source_urls"):
        score += 10
    if record.get("company_name"):
        score += 5
    return score


def _research_memory_target_candidates(
    *,
    archetype_id: str,
    card: Mapping[str, Any],
    case_inventory: Mapping[str, Any] | None,
    max_symbols: int,
) -> list[dict[str, Any]]:
    """Pick research-memory symbols as next-run targets, never as score evidence."""

    records = _case_records(case_inventory)
    if not records:
        return []
    preferred_case_ids = set(card.get("url_backed_replay_cases") or []) | set(
        card.get("source_family_success_examples") or []
    )
    candidates_by_symbol: dict[str, dict[str, Any]] = {}
    for record in records:
        if str(record.get("canonical_archetype_id") or "") != archetype_id:
            continue
        symbol = normalized_real_symbol(record.get("symbol"))
        if not symbol:
            continue
        score = _materialization_candidate_score(archetype_id, record)
        if record.get("research_case_id") in preferred_case_ids:
            score += 100
        if score <= 0:
            continue
        existing = candidates_by_symbol.get(symbol)
        if existing and int(existing["materialization_score"]) >= score:
            existing["support_case_ids"].append(record.get("research_case_id"))
            continue
        candidates_by_symbol[symbol] = {
            "symbol": symbol,
            "company_name": record.get("company_name"),
            "target_materialization_source": "RESEARCH_REVERSE_CASE_INVENTORY",
            "target_materialization_status": "RESEARCH_MEMORY_TARGET_CANDIDATE_SOURCE_RECHECK_REQUIRED",
            "materialization_score": score,
            "support_case_ids": [record.get("research_case_id")],
            "support_case_source_quality": record.get("source_quality"),
            "support_case_source_file": record.get("source_file"),
            "support_case_role": record.get("case_role"),
            "score_evidence_allowed_from_research": False,
        }
    candidates = sorted(
        candidates_by_symbol.values(),
        key=lambda item: (-int(item["materialization_score"]), str(item["symbol"])),
    )
    return candidates[:max_symbols]


def build_all_archetype_next_runtime_attempt_plan(
    *,
    status_matrix: Mapping[str, Any],
    memory_cards: Mapping[str, Any],
    case_inventory: Mapping[str, Any] | None = None,
    max_primitives_per_archetype: int = 3,
    max_materialized_symbols_per_archetype: int = 1,
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
        target_candidates: list[dict[str, Any]] = []
        target_symbol_mode = "SYMBOL_SPECIFIC" if symbols != [None] else "ARCHETYPE_LEVEL_DISCOVERY"
        if symbols == [None]:
            target_candidates = _research_memory_target_candidates(
                archetype_id=archetype_id,
                card=card,
                case_inventory=case_inventory,
                max_symbols=max_materialized_symbols_per_archetype,
            )
            if target_candidates:
                symbols = [candidate["symbol"] for candidate in target_candidates]
                target_symbol_mode = "RESEARCH_MEMORY_TARGET_CANDIDATE"
        candidate_by_symbol = {candidate["symbol"]: candidate for candidate in target_candidates}
        primary_failure_mode = _claim_failure_primary_mode(row)
        repair_hint = _claim_failure_repair_hint(row, primary_failure_mode)
        repair_actions = _source_route_repair_actions(primary_failure_mode)
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
                "target_symbol_mode": target_symbol_mode,
                "target_symbols": [symbol for symbol in symbols if symbol],
                "target_materialization_candidates": target_candidates,
                "requires_target_materialization_before_scoring": symbols == [None],
                "requires_current_source_confirmation_before_scoring": True,
                "primitive_attempts": primitives,
                "score_allowed_before_execution": False,
                "stage_promotion_allowed_before_execution": False,
                "llm_query_required": True,
                "hardcoded_queries": [],
                "hardcoded_query_count": 0,
                "previous_claim_failure_primary_mode": primary_failure_mode,
                "previous_claim_failure_repair_hint": repair_hint,
                "previous_claim_failure_top_modes": _claim_failure_top_modes(row),
                "source_route_repair_required": bool(repair_actions),
                "source_route_repair_actions": repair_actions,
                "next_required_action": row.get("next_required_action"),
                "status_reason_ko": row.get("status_reason_ko"),
            }
        )
        for primitive in primitives:
            route_priority = _route_priority(card, primitive)
            for symbol in symbols:
                task_id = _stable_id("RTTASK", as_of_date, archetype_id, primitive, symbol or "DISCOVERY")
                task_target_symbol_mode = target_symbol_mode if symbol else "ARCHETYPE_LEVEL_DISCOVERY"
                materialization_candidate = candidate_by_symbol.get(str(symbol)) if symbol else None
                if materialization_candidate:
                    query_intents = [
                        (
                            f"Research memory materialized `{symbol}` as a candidate target for "
                            f"`{archetype_id}` from case ids {materialization_candidate['support_case_ids']}. "
                            "Treat this only as a target candidate. Ask the LLM planner for bounded "
                            f"official-first queries that verify current, direct target-company evidence "
                            f"for primitive `{primitive}` before any score/stage use."
                        )
                    ]
                elif symbol is None:
                    query_intents = [
                        (
                            "Ask the LLM planner to first materialize real current target companies/tickers "
                            f"for archetype `{archetype_id}` and primitive `{primitive}`, then propose bounded "
                            "official-first source routes. Do not score archetype-level discovery results until "
                            "a real target symbol has source-backed Evidence OS claims."
                        )
                    ]
                else:
                    query_intents = [
                        (
                            "Ask the LLM planner for bounded official-first queries that verify current, "
                            f"direct target-company evidence for primitive `{primitive}`."
                        )
                    ]
                failure_feedback_intent = _failure_feedback_intent(
                    primary_mode=primary_failure_mode,
                    repair_hint=repair_hint,
                    repair_actions=repair_actions,
                )
                if failure_feedback_intent:
                    query_intents.append(failure_feedback_intent)
                planner_failure_feedback = _planner_failure_feedback(
                    row=row,
                    primitive=primitive,
                    primary_mode=primary_failure_mode,
                    repair_hint=repair_hint,
                    repair_actions=repair_actions,
                )
                success_condition = _success_condition(
                    archetype_id=archetype_id,
                    primitive=primitive,
                    symbol=symbol,
                )
                expected_claim_schema = _expected_claim_schema(
                    archetype_id=archetype_id,
                    primitive=primitive,
                    symbol=symbol,
                )
                fallback_if_not_found = _fallback_if_not_found(
                    row=row,
                    symbol=symbol,
                    primary_mode=primary_failure_mode,
                )
                source_task = {
                    "schema_version": "e2r_all_archetype_next_runtime_source_task_v1",
                    "task_id": task_id,
                    "attempt_id": attempt_id,
                    "task_type": "runtime_parity_gap_closure",
                    "task_status": "PLANNING_REQUIRED",
                    "source_task_origin": "all_archetype_runtime_status_matrix",
                    "as_of_date": as_of_date,
                    "symbol": symbol,
                    "target_symbol_mode": task_target_symbol_mode,
                    "requires_target_materialization_before_scoring": symbol is None,
                    "requires_current_source_confirmation_before_scoring": True,
                    "target_materialization_candidate": materialization_candidate,
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
                    "query_intents": query_intents,
                    "success_condition": success_condition,
                    "expected_claim_schema": expected_claim_schema,
                    "fallback_if_not_found": fallback_if_not_found,
                    "planner_failure_feedback": planner_failure_feedback,
                    "previous_claim_failure_primary_mode": primary_failure_mode,
                    "previous_claim_failure_repair_hint": repair_hint,
                    "source_route_repair_required": bool(repair_actions),
                    "source_route_repair_actions": repair_actions,
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
                        "target_symbol_mode": task_target_symbol_mode,
                        "target_materialization_candidate": materialization_candidate,
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
                            str(primary_failure_mode or "NO_PREVIOUS_CLAIM_FAILURE_MODE"),
                        ],
                        "event_summary": (
                            f"planner input only. archetype_id={archetype_id}; primitive_gap={primitive}; "
                            "source-backed Evidence OS claim required before any production score/stage use; "
                            f"previous_claim_failure_primary_mode={primary_failure_mode or 'NONE'}"
                        ),
                        "structured_payload": {
                            "attempt_id": attempt_id,
                            "follow_up_task_id": task_id,
                            "target_archetype": archetype_id,
                            "target_archetype_status": "RUNTIME_PARITY_FOLLOW_UP_REQUIRED",
                            "primitive_gap": primitive,
                            "target_symbol_mode": task_target_symbol_mode,
                            "target_materialization_candidate": materialization_candidate,
                            "requires_current_source_confirmation_before_scoring": True,
                            "seed_role": "planner_input_only",
                            "follow_up_origin": "all_archetype_runtime_status_matrix",
                            "preferred_source_classes": source_task["preferred_source_classes"],
                            "fallback_source_classes": source_task["fallback_source_classes"],
                            "forbidden_source_classes": source_task["forbidden_source_classes"],
                            "official_first_required": True,
                            "llm_query_required": True,
                            "query_intents": source_task["query_intents"],
                            "success_condition": success_condition,
                            "expected_claim_schema": expected_claim_schema,
                            "fallback_if_not_found": fallback_if_not_found,
                            "planner_failure_feedback": planner_failure_feedback,
                            "previous_claim_failure_primary_mode": primary_failure_mode,
                            "previous_claim_failure_repair_hint": repair_hint,
                            "source_route_repair_required": bool(repair_actions),
                            "source_route_repair_actions": repair_actions,
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
    by_repair_hint = Counter(
        task["previous_claim_failure_repair_hint"]
        for task in source_tasks
        if task.get("source_route_repair_required") and task.get("previous_claim_failure_repair_hint")
    )
    by_primary_failure_mode = Counter(
        task["previous_claim_failure_primary_mode"]
        for task in source_tasks
        if task.get("source_route_repair_required") and task.get("previous_claim_failure_primary_mode")
    )
    materialized_candidate_rows = [
        row for row in plan_rows if row.get("target_symbol_mode") == "RESEARCH_MEMORY_TARGET_CANDIDATE"
    ]
    return {
        "schema_version": "e2r_all_archetype_next_runtime_attempt_plan_v1",
        "as_of_date": as_of_date,
        "plan_row_count": len(plan_rows),
        "source_task_count": len(source_tasks),
        "seed_event_count": len(seed_events),
        "attempt_type_counts": dict(sorted(by_attempt_type.items())),
        "target_symbol_mode_counts": dict(sorted(by_symbol_mode.items())),
        "source_route_repair_task_count": sum(1 for task in source_tasks if task.get("source_route_repair_required")),
        "source_route_repair_hint_counts": dict(sorted(by_repair_hint.items())),
        "source_route_repair_primary_failure_mode_counts": dict(sorted(by_primary_failure_mode.items())),
        "research_memory_target_materialized_archetype_count": len(materialized_candidate_rows),
        "research_memory_target_materialized_task_count": sum(
            1 for task in source_tasks if task.get("target_symbol_mode") == "RESEARCH_MEMORY_TARGET_CANDIDATE"
        ),
        "target_materialization_unresolved_archetype_count": sum(
            1 for row in plan_rows if row.get("requires_target_materialization_before_scoring") is True
        ),
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
        "all_tasks_have_success_condition": all(bool(task.get("success_condition")) for task in source_tasks),
        "all_tasks_have_expected_claim_schema": all(
            bool(task.get("expected_claim_schema", {}).get("primitive_id"))
            and task.get("expected_claim_schema", {}).get("target_scope_status") == "DIRECT"
            and task.get("expected_claim_schema", {}).get("mapping_status") == "ACCEPTED"
            and task.get("expected_claim_schema", {}).get("score_forbidden_until_claim_accepted") is True
            for task in source_tasks
        ),
        "all_tasks_have_fallback_if_not_found": all(bool(task.get("fallback_if_not_found")) for task in source_tasks),
        "target_materialization_required_task_count": sum(
            1 for task in source_tasks if task.get("requires_target_materialization_before_scoring") is True
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
        f"- source_route_repair_task_count: `{plan.get('source_route_repair_task_count', 0)}`",
        f"- source_route_repair_hint_counts: `{json.dumps(plan.get('source_route_repair_hint_counts', {}), ensure_ascii=False, sort_keys=True)}`",
        f"- source_route_repair_primary_failure_mode_counts: `{json.dumps(plan.get('source_route_repair_primary_failure_mode_counts', {}), ensure_ascii=False, sort_keys=True)}`",
        f"- research_memory_target_materialized_archetype_count: `{plan.get('research_memory_target_materialized_archetype_count', 0)}`",
        f"- research_memory_target_materialized_task_count: `{plan.get('research_memory_target_materialized_task_count', 0)}`",
        f"- target_materialization_unresolved_archetype_count: `{plan.get('target_materialization_unresolved_archetype_count', 0)}`",
        f"- all_tasks_score_blocked_before_execution: `{plan['all_tasks_score_blocked_before_execution']}`",
        f"- all_tasks_require_llm_query_generation: `{plan['all_tasks_require_llm_query_generation']}`",
        f"- all_tasks_have_no_hardcoded_queries: `{plan['all_tasks_have_no_hardcoded_queries']}`",
        f"- all_tasks_have_finite_budget: `{plan['all_tasks_have_finite_budget']}`",
        f"- all_tasks_have_success_condition: `{plan.get('all_tasks_have_success_condition')}`",
        f"- all_tasks_have_expected_claim_schema: `{plan.get('all_tasks_have_expected_claim_schema')}`",
        f"- all_tasks_have_fallback_if_not_found: `{plan.get('all_tasks_have_fallback_if_not_found')}`",
        f"- target_materialization_required_task_count: `{plan['target_materialization_required_task_count']}`",
        "",
        "## Plan Rows",
        "",
        "| archetype | priority | attempt type | symbol mode | primitives | current proof | previous claim failure | repair hint |",
        "|---|---:|---|---|---|---|---|---|",
    ]
    for row in plan.get("plan_rows", []):
        lines.append(
            "| {archetype} | {priority} | {attempt_type} | {symbol_mode} | {primitives} | {proof} | {failure} | {repair_hint} |".format(
                archetype=row["archetype_id"],
                priority=row["priority"],
                attempt_type=row["attempt_type"],
                symbol_mode=row["target_symbol_mode"],
                primitives=", ".join(row["primitive_attempts"]),
                proof=row["current_runtime_parity_proof_status"],
                failure=row.get("previous_claim_failure_primary_mode") or "-",
                repair_hint=row.get("previous_claim_failure_repair_hint") or "-",
            )
        )
    lines.extend(
        [
            "",
            "## Safety",
            "",
            "이 plan은 점수를 만들지 않는다. 모든 source task는 LLM query generation과 source-backed Evidence OS claim을 요구하며, 실행 전 score/stage promotion은 금지된다.",
            "",
            "이전 rejected claim은 점수 근거가 아니라 planner feedback으로만 쓰인다. 예를 들어 C08이 DART 표지/개요만 읽고 실패했다면 다음 source task에는 generic disclosure를 score evidence로 재사용하지 말고 primitive-specific source/section을 찾으라는 repair hint가 붙는다.",
            "",
        ]
    )
    return "\n".join(lines)


def _write_jsonl(path: Path, rows: list[Mapping[str, Any]]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def _load_optional_json(path: Path) -> Mapping[str, Any] | None:
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        return None
    return payload


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
        case_inventory=_load_optional_json(docs_path / "research_reverse_case_inventory.json"),
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
