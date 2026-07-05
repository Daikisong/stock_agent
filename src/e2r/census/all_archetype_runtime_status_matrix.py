"""All-archetype runtime status matrix for Goal4.

The parity audit has the raw counters.  This module turns those counters into
operator-readable status axes so C01~C32 plus the four R13 contracts cannot be
mistaken for a completed production parity run.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping


def _prefix(archetype_id: str) -> str:
    return archetype_id.split("_", 1)[0]


def _runtime_attempt_status(row: Mapping[str, Any]) -> str:
    if int(row.get("runtime_full_thesis_row_count") or 0):
        return "PRODUCTION_FULL_THESIS_ATTEMPTED"
    if int(row.get("runtime_blocked_candidate_count") or 0):
        return "PRODUCTION_CANDIDATE_BLOCKED"
    if int(row.get("runtime_stagecourt_trace_count") or 0):
        return "STAGECOURT_ATTEMPTED_NOT_PROMOTED"
    if int(row.get("runtime_source_task_execution_count") or 0):
        return "SOURCE_TASK_EXECUTED"
    if int(row.get("runtime_follow_up_source_task_count") or 0):
        return "FOLLOWUP_SOURCE_TASK_CREATED"
    if int(row.get("runtime_planner_top1_count") or 0) or int(row.get("runtime_planner_topk_count") or 0):
        return "PLANNER_ATTEMPTED_ONLY"
    if int(row.get("source_backed_fixture_count") or 0):
        return "REPLAY_READY_NOT_RUNTIME_ATTEMPTED"
    return "NOT_ATTEMPTED"


def _runtime_source_execution_status(row: Mapping[str, Any], *, route_pattern_count: int) -> str:
    accepted = int(row.get("runtime_source_task_accepted_claim_count") or 0)
    executed = int(row.get("runtime_source_task_execution_count") or 0)
    followup = int(row.get("runtime_follow_up_source_task_count") or 0)
    if executed and accepted:
        return "SOURCE_TASK_EXECUTED_WITH_ACCEPTED_CLAIMS"
    if executed:
        return "SOURCE_TASK_EXECUTED_NO_ACCEPTED_CLAIMS"
    if followup:
        return "FOLLOWUP_SOURCE_TASK_CREATED_NOT_EXECUTED"
    if route_pattern_count:
        return "ROUTE_RECOVERED_NOT_EXECUTED"
    return "SOURCE_ROUTE_NOT_RECOVERED"


def _accepted_claim_status(row: Mapping[str, Any]) -> str:
    runtime_claims = int(row.get("runtime_accepted_claim_count") or 0)
    source_claims = int(row.get("runtime_source_task_accepted_claim_count") or 0)
    replay_claims = int(row.get("replay_accepted_claim_count") or 0)
    full_rows = int(row.get("runtime_full_thesis_row_count") or 0)
    if full_rows and (runtime_claims or source_claims):
        return "PRODUCTION_SCORE_PATH_HAS_ACCEPTED_CLAIMS"
    if runtime_claims or source_claims:
        return "ACCEPTED_CLAIM_PRESENT_NOT_FULL_THESIS_CLOSED"
    if replay_claims:
        return "REPLAY_ACCEPTED_CLAIM_ONLY"
    return "NO_ACCEPTED_CLAIM"


def _full_thesis_status(row: Mapping[str, Any]) -> str:
    full_rows = int(row.get("runtime_full_thesis_row_count") or 0)
    if full_rows:
        required_gaps = int(row.get("runtime_full_thesis_row_with_required_positive_missing_count") or 0)
        green_gaps = int(row.get("runtime_full_thesis_row_with_green_gap_count") or 0)
        if required_gaps == 0 and green_gaps == 0:
            return "MEANINGFUL_FULL_THESIS_READY"
        return "SCORE_PATH_ONLY_WITH_REQUIRED_OR_GREEN_GAPS"
    if int(row.get("runtime_blocked_candidate_count") or 0):
        return "FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP"
    if int(row.get("runtime_stagecourt_trace_count") or 0):
        return "STAGECOURT_TRACE_NOT_PROMOTED"
    return "NO_PRODUCTION_FULL_THESIS_ROW"


def _proof_status(row: Mapping[str, Any], full_thesis_status: str) -> str:
    if full_thesis_status == "MEANINGFUL_FULL_THESIS_READY":
        return "RUNTIME_PARITY_PROVEN"
    if full_thesis_status == "SCORE_PATH_ONLY_WITH_REQUIRED_OR_GREEN_GAPS":
        return "NOT_PROVEN_SCORE_PATH_ONLY"
    if full_thesis_status == "FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP":
        return "NOT_PROVEN_BLOCKED_BY_MATERIAL_GAP"
    if int(row.get("runtime_source_task_accepted_claim_count") or 0) or int(row.get("runtime_accepted_claim_count") or 0):
        return "NOT_PROVEN_ACCEPTED_CLAIM_NOT_CLOSED"
    if int(row.get("runtime_source_task_execution_count") or 0):
        return "NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM"
    if int(row.get("runtime_planner_top1_count") or 0) or int(row.get("runtime_planner_topk_count") or 0):
        return "NOT_PROVEN_PLANNER_ONLY"
    if int(row.get("source_backed_fixture_count") or 0):
        return "NOT_PROVEN_REPLAY_ONLY"
    return "NOT_PROVEN_NO_RUNTIME_EVIDENCE"


def _next_action(row: Mapping[str, Any], *, full_thesis_status: str, accepted_claim_status: str) -> str:
    if full_thesis_status == "MEANINGFUL_FULL_THESIS_READY":
        return "KEEP_MONITORING_FOR_LIFECYCLE_SUPERSESSION"
    if full_thesis_status == "SCORE_PATH_ONLY_WITH_REQUIRED_OR_GREEN_GAPS":
        return "CLOSE_REQUIRED_POSITIVE_AND_GREEN_GAPS_BEFORE_MEANINGFUL_PASS"
    if full_thesis_status == "FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP":
        return "EXECUTE_OFFICIAL_FIRST_FOLLOWUP_TASKS_FOR_BLOCKED_PRIMITIVES"
    if accepted_claim_status == "ACCEPTED_CLAIM_PRESENT_NOT_FULL_THESIS_CLOSED":
        return "MAP_ACCEPTED_CLAIMS_TO_SCORE_CONTRIBUTIONS_OR_EXPLAIN_REMAINING_GAPS"
    if int(row.get("runtime_source_task_execution_count") or 0):
        return "REPLAN_SOURCE_TASKS_WITH_RESEARCH_MEMORY_AND_REQUIRE_ANCHORS"
    if int(row.get("runtime_planner_top1_count") or 0) or int(row.get("runtime_planner_topk_count") or 0):
        return "TURN_PLANNER_ATTEMPT_INTO_BOUNDED_SOURCE_TASKS"
    if int(row.get("source_backed_fixture_count") or 0):
        return "CONNECT_SOURCE_BACKED_REPLAY_TO_PRODUCTION_RUNTIME_ATTEMPT"
    return "CREATE_RESEARCH_MEMORY_AND_SOURCE_ROUTE_BEFORE_RUNTIME_ATTEMPT"


def _reason_ko(
    *,
    row: Mapping[str, Any],
    attempt_status: str,
    accepted_claim_status: str,
    full_thesis_status: str,
) -> str:
    if full_thesis_status == "SCORE_PATH_ONLY_WITH_REQUIRED_OR_GREEN_GAPS":
        return "production 점수 경로는 닫혔지만 required-positive/Green 빈칸이 남아 있어 meaningful pass가 아니다."
    if full_thesis_status == "FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP":
        return "production 후보까지 갔지만 필수 또는 Green primitive의 source-backed claim이 부족해 full thesis로 승격되지 않았다."
    if accepted_claim_status == "ACCEPTED_CLAIM_PRESENT_NOT_FULL_THESIS_CLOSED":
        return "source-backed accepted claim은 있지만 score contribution/full thesis closure까지 이어지지 않았다."
    if attempt_status == "PLANNER_ATTEMPTED_ONLY":
        return "planner 가설은 있었지만 production source task와 accepted claim으로 닫히지 않았다."
    if attempt_status == "REPLAY_READY_NOT_RUNTIME_ATTEMPTED":
        return "연구 replay fixture는 준비됐지만 이번 production runtime에서 시도되지 않았다."
    if int(row.get("source_backed_fixture_count") or 0):
        return "source-backed 연구 판례는 있으나 current production 증거로 재실행되지 않았다."
    return "현재 production runtime에서 이 아키타입을 증명할 충분한 evidence path가 없다."


def build_all_archetype_runtime_status_matrix(
    *,
    parity_audit: Mapping[str, Any],
    memory_cards: Mapping[str, Any],
    source_routes: Mapping[str, Any],
    candidate_selection: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    cards_by_id = {card["archetype_id"]: card for card in memory_cards.get("cards", [])}
    route_counts: Counter[str] = Counter()
    official_route_counts: Counter[str] = Counter()
    route_primitives: dict[str, set[str]] = defaultdict(set)
    for pattern in source_routes.get("patterns", []):
        archetype_id = str(pattern.get("archetype_id"))
        route_counts[archetype_id] += 1
        route_primitives[archetype_id].add(str(pattern.get("primitive_id")))
        if pattern.get("official_first_required"):
            official_route_counts[archetype_id] += 1

    gap_task_counts: Counter[str] = Counter()
    for task in source_routes.get("gap_tasks", []):
        gap_task_counts[str(task.get("archetype_id"))] += 1

    next_attempt_reasons = {
        row["archetype_id"]: row.get("reason")
        for row in (candidate_selection or {}).get("next_required_archetype_attempts", [])
    }

    status_rows: list[dict[str, Any]] = []
    for row in parity_audit.get("rows", []):
        archetype_id = str(row["archetype_id"])
        card = cards_by_id.get(archetype_id, {})
        route_pattern_count = route_counts[archetype_id]
        source_route_recovery_status = (
            "SOURCE_ROUTE_PATTERN_READY_WITH_GAPS"
            if route_pattern_count and gap_task_counts[archetype_id]
            else "SOURCE_ROUTE_PATTERN_READY"
            if route_pattern_count
            else "SOURCE_ROUTE_PATTERN_MISSING"
        )
        attempt_status = _runtime_attempt_status(row)
        source_execution_status = _runtime_source_execution_status(row, route_pattern_count=route_pattern_count)
        accepted_claim_status = _accepted_claim_status(row)
        full_thesis_status = _full_thesis_status(row)
        proof_status = _proof_status(row, full_thesis_status)
        status_rows.append(
            {
                "schema_version": "e2r_all_archetype_runtime_status_row_v1",
                "archetype_id": archetype_id,
                "archetype_prefix": _prefix(archetype_id),
                "contract_registration_status": "REGISTERED",
                "registry_scope": "C01_TO_C32" if _prefix(archetype_id).startswith("C") else "R13_CROSS_ARCHETYPE",
                "research_memory_status": "MEMORY_CARD_READY" if archetype_id in cards_by_id else "MEMORY_CARD_MISSING",
                "source_route_recovery_status": source_route_recovery_status,
                "runtime_attempt_status": attempt_status,
                "runtime_source_route_execution_status": source_execution_status,
                "accepted_claim_status": accepted_claim_status,
                "full_thesis_status": full_thesis_status,
                "runtime_parity_proof_status": proof_status,
                "next_required_action": _next_action(
                    row,
                    full_thesis_status=full_thesis_status,
                    accepted_claim_status=accepted_claim_status,
                ),
                "next_balanced_attempt_reason": next_attempt_reasons.get(archetype_id),
                "status_reason_ko": _reason_ko(
                    row=row,
                    attempt_status=attempt_status,
                    accepted_claim_status=accepted_claim_status,
                    full_thesis_status=full_thesis_status,
                ),
                "source_route_pattern_count": route_pattern_count,
                "official_first_route_pattern_count": official_route_counts[archetype_id],
                "source_route_gap_task_count": gap_task_counts[archetype_id],
                "memory_required_positive_primitive_count": len(card.get("required_positive_primitives") or []),
                "memory_url_backed_replay_case_count": len(card.get("url_backed_replay_cases") or []),
                "memory_source_proxy_only_case_count": len(card.get("source_proxy_only_cases") or []),
                "source_backed_fixture_count": row.get("source_backed_fixture_count", 0),
                "replay_accepted_claim_count": row.get("replay_accepted_claim_count", 0),
                "runtime_planner_top1_count": row.get("runtime_planner_top1_count", 0),
                "runtime_planner_topk_count": row.get("runtime_planner_topk_count", 0),
                "runtime_source_task_execution_count": row.get("runtime_source_task_execution_count", 0),
                "runtime_source_task_accepted_claim_count": row.get("runtime_source_task_accepted_claim_count", 0),
                "runtime_accepted_claim_count": row.get("runtime_accepted_claim_count", 0),
                "runtime_stagecourt_trace_count": row.get("runtime_stagecourt_trace_count", 0),
                "runtime_blocked_candidate_count": row.get("runtime_blocked_candidate_count", 0),
                "runtime_full_thesis_row_count": row.get("runtime_full_thesis_row_count", 0),
                "runtime_full_thesis_row_with_required_positive_missing_count": row.get(
                    "runtime_full_thesis_row_with_required_positive_missing_count", 0
                ),
                "runtime_full_thesis_row_with_green_gap_count": row.get(
                    "runtime_full_thesis_row_with_green_gap_count", 0
                ),
                "blocker_classes": row.get("blocker_classes", []),
                "symbols_sample": row.get("symbols_sample", []),
                "full_thesis_symbols": row.get("full_thesis_symbols", []),
                "blocked_symbols": row.get("blocked_symbols", []),
            }
        )

    c_rows = [row for row in status_rows if row["registry_scope"] == "C01_TO_C32"]
    r13_rows = [row for row in status_rows if row["registry_scope"] == "R13_CROSS_ARCHETYPE"]
    proof_counts = Counter(row["runtime_parity_proof_status"] for row in status_rows)
    attempt_counts = Counter(row["runtime_attempt_status"] for row in status_rows)
    full_thesis_counts = Counter(row["full_thesis_status"] for row in status_rows)
    accepted_counts = Counter(row["accepted_claim_status"] for row in status_rows)

    return {
        "schema_version": "e2r_all_archetype_runtime_status_matrix_v1",
        "as_of_date": parity_audit.get("as_of_date"),
        "registry_contract_count": len(status_rows),
        "c01_to_c32_contract_count": len(c_rows),
        "r13_cross_archetype_contract_count": len(r13_rows),
        "registry_scope_note": "레지스트리 기준 36개는 C01~C32 32개와 R13 cross-archetype 4개다.",
        "all_contracts_have_runtime_status_axes": all(
            row["runtime_attempt_status"]
            and row["source_route_recovery_status"]
            and row["accepted_claim_status"]
            and row["full_thesis_status"]
            for row in status_rows
        ),
        "all_contracts_have_memory_card": all(row["research_memory_status"] == "MEMORY_CARD_READY" for row in status_rows),
        "all_contracts_have_source_route_patterns": all(
            row["source_route_pattern_count"] > 0 for row in status_rows
        ),
        "runtime_parity_proof_status_counts": dict(sorted(proof_counts.items())),
        "runtime_attempt_status_counts": dict(sorted(attempt_counts.items())),
        "accepted_claim_status_counts": dict(sorted(accepted_counts.items())),
        "full_thesis_status_counts": dict(sorted(full_thesis_counts.items())),
        "meaningful_runtime_parity_ready": proof_counts.get("RUNTIME_PARITY_PROVEN", 0) == len(status_rows),
        "rows": status_rows,
    }


def render_all_archetype_runtime_status_markdown(matrix: Mapping[str, Any]) -> str:
    lines = [
        "# All Archetype Runtime Status Matrix - 2026-07-05",
        "",
        "이 문서는 C01~C32와 R13 4개, 총 36개 registered contract의 runtime 상태를 전수로 보여준다.",
        "",
        "쉬운 예: `source route recovered`는 어디 병원에 가야 하는지 안다는 뜻이고, `runtime source executed`는 실제 예약하고 검사했다는 뜻이다. 둘은 다르다.",
        "",
        "## Summary",
        "",
        f"- registry_contract_count: `{matrix['registry_contract_count']}`",
        f"- c01_to_c32_contract_count: `{matrix['c01_to_c32_contract_count']}`",
        f"- r13_cross_archetype_contract_count: `{matrix['r13_cross_archetype_contract_count']}`",
        f"- all_contracts_have_runtime_status_axes: `{matrix['all_contracts_have_runtime_status_axes']}`",
        f"- all_contracts_have_memory_card: `{matrix['all_contracts_have_memory_card']}`",
        f"- all_contracts_have_source_route_patterns: `{matrix['all_contracts_have_source_route_patterns']}`",
        f"- meaningful_runtime_parity_ready: `{matrix['meaningful_runtime_parity_ready']}`",
        "",
        "## Status Counts",
        "",
        f"- runtime_attempt_status_counts: `{json.dumps(matrix['runtime_attempt_status_counts'], ensure_ascii=False, sort_keys=True)}`",
        f"- accepted_claim_status_counts: `{json.dumps(matrix['accepted_claim_status_counts'], ensure_ascii=False, sort_keys=True)}`",
        f"- full_thesis_status_counts: `{json.dumps(matrix['full_thesis_status_counts'], ensure_ascii=False, sort_keys=True)}`",
        f"- runtime_parity_proof_status_counts: `{json.dumps(matrix['runtime_parity_proof_status_counts'], ensure_ascii=False, sort_keys=True)}`",
        "",
        "## Matrix",
        "",
        "| archetype | attempt | source route | source execution | accepted claim | full thesis | proof | next action |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for row in matrix.get("rows", []):
        lines.append(
            "| {archetype} | {attempt} | {route} | {execution} | {claim} | {full} | {proof} | {next_action} |".format(
                archetype=row["archetype_id"],
                attempt=row["runtime_attempt_status"],
                route=row["source_route_recovery_status"],
                execution=row["runtime_source_route_execution_status"],
                claim=row["accepted_claim_status"],
                full=row["full_thesis_status"],
                proof=row["runtime_parity_proof_status"],
                next_action=row["next_required_action"],
            )
        )
    lines.extend(
        [
            "",
            "## Operator Reading",
            "",
            "`RUNTIME_PARITY_PROVEN`이 아닌 행은 goal4 완료 증거가 아니다. `REPLAY_ACCEPTED_CLAIM_ONLY`는 연구 판례 재생성이지 production 점수가 아니다.",
            "",
        ]
    )
    return "\n".join(lines)


def write_all_archetype_runtime_status_matrix(
    *,
    parity_audit: Mapping[str, Any],
    memory_cards: Mapping[str, Any],
    source_routes: Mapping[str, Any],
    candidate_selection: Mapping[str, Any] | None = None,
    docs_dir: str | Path = "docs/operational",
) -> dict[str, Any]:
    docs_path = Path(docs_dir)
    docs_path.mkdir(parents=True, exist_ok=True)
    matrix = build_all_archetype_runtime_status_matrix(
        parity_audit=parity_audit,
        memory_cards=memory_cards,
        source_routes=source_routes,
        candidate_selection=candidate_selection,
    )
    json_path = docs_path / "all_archetype_runtime_status_matrix_2026-07-05.json"
    md_path = docs_path / "all_archetype_runtime_status_matrix_2026-07-05.md"
    alias_json_path = docs_path / "all_archetype_runtime_status_matrix.json"
    json_text = json.dumps(matrix, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    json_path.write_text(json_text, encoding="utf-8")
    alias_json_path.write_text(json_text, encoding="utf-8")
    md_path.write_text(render_all_archetype_runtime_status_markdown(matrix), encoding="utf-8")
    return {
        "matrix": matrix,
        "json_path": json_path,
        "alias_json_path": alias_json_path,
        "markdown_path": md_path,
    }


__all__ = [
    "build_all_archetype_runtime_status_matrix",
    "render_all_archetype_runtime_status_markdown",
    "write_all_archetype_runtime_status_matrix",
]
