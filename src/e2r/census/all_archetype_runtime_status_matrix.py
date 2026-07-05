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


_POSITIVE_ROLE_MARKERS = ("positive", "success", "green", "yellow", "stage2", "stage3")
_COUNTEREXAMPLE_ROLE_MARKERS = ("counter", "failed", "4c", "red")
_GUARD_ROLE_MARKERS = ("guard", "4b", "4c", "profile_cap", "false_positive")
_URL_BACKED_SOURCE_QUALITIES = {"A2_URL_BACKED"}
_SOURCE_PROXY_SOURCE_QUALITIES = {"SOURCE_PROXY_ONLY"}
_EVIDENCE_PENDING_SOURCE_QUALITIES = {"EVIDENCE_URL_PENDING", "A1_URL_PENDING"}


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
    if int(row.get("targetless_source_task_execution_count") or 0) or int(
        row.get("target_materialization_required_seed_count") or 0
    ):
        return "ARCHETYPE_DISCOVERY_TARGET_MATERIALIZATION_REQUIRED"
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
    if int(row.get("targetless_source_task_execution_count") or 0):
        return "TARGETLESS_SOURCE_SHELL_EXECUTED_NO_TARGET"
    if int(row.get("target_materialization_required_seed_count") or 0):
        return "TARGET_MATERIALIZATION_REQUIRED_BEFORE_SOURCE_EXECUTION"
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
    if int(row.get("targetless_source_task_execution_count") or 0) or int(
        row.get("target_materialization_required_seed_count") or 0
    ):
        return "NOT_PROVEN_TARGET_MATERIALIZATION_REQUIRED"
    if int(row.get("runtime_planner_top1_count") or 0) or int(row.get("runtime_planner_topk_count") or 0):
        return "NOT_PROVEN_PLANNER_ONLY"
    if int(row.get("source_backed_fixture_count") or 0):
        return "NOT_PROVEN_REPLAY_ONLY"
    return "NOT_PROVEN_NO_RUNTIME_EVIDENCE"


def _inventory_counts_by_archetype(research_inventory: Mapping[str, Any] | None) -> dict[str, Counter[str]]:
    counts: dict[str, Counter[str]] = defaultdict(Counter)
    if not research_inventory:
        return counts
    for record in research_inventory.get("records", []):
        if not isinstance(record, Mapping):
            continue
        archetype_id = str(record.get("canonical_archetype_id") or "")
        if not archetype_id:
            continue
        bucket = counts[archetype_id]
        bucket["research_case_count"] += 1

        source_quality = str(record.get("source_quality") or "")
        if source_quality in _URL_BACKED_SOURCE_QUALITIES:
            bucket["url_backed_case_count"] += 1
        if source_quality in _SOURCE_PROXY_SOURCE_QUALITIES or record.get("source_proxy_only") is True:
            bucket["source_proxy_case_count"] += 1
        if source_quality in _EVIDENCE_PENDING_SOURCE_QUALITIES or record.get("evidence_url_pending") is True:
            bucket["evidence_url_pending_count"] += 1

        role = str(record.get("case_role") or "").lower()
        if any(marker in role for marker in _POSITIVE_ROLE_MARKERS):
            bucket["positive_case_count"] += 1
        if any(marker in role for marker in _COUNTEREXAMPLE_ROLE_MARKERS):
            bucket["counterexample_case_count"] += 1
        if any(marker in role for marker in _GUARD_ROLE_MARKERS):
            bucket["guard_case_count"] += 1
    return counts


def _research_counts(archetype_id: str, card: Mapping[str, Any], inventory_counts: Mapping[str, Counter[str]]) -> dict[str, int]:
    inventory = inventory_counts.get(archetype_id, Counter())
    url_backed = int(inventory.get("url_backed_case_count") or len(card.get("url_backed_replay_cases") or []))
    source_proxy = int(inventory.get("source_proxy_case_count") or len(card.get("source_proxy_only_cases") or []))
    pending = int(inventory.get("evidence_url_pending_count") or len(card.get("evidence_url_pending_cases") or []))
    total = int(inventory.get("research_case_count") or (url_backed + source_proxy + pending))
    return {
        "research_case_count": total,
        "url_backed_case_count": url_backed,
        "source_proxy_case_count": source_proxy,
        "evidence_url_pending_count": pending,
        "positive_case_count": int(inventory.get("positive_case_count") or 0),
        "counterexample_case_count": int(inventory.get("counterexample_case_count") or 0),
        "guard_case_count": int(inventory.get("guard_case_count") or 0),
    }


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _resolve_output_root(parity_audit: Mapping[str, Any]) -> Path | None:
    output_root = parity_audit.get("output_root")
    if not output_root:
        return None
    path = Path(str(output_root))
    if path.is_absolute():
        return path
    for base in (Path.cwd(), Path(__file__).resolve().parents[3]):
        candidate = base / path
        if candidate.exists():
            return candidate
    return path


def _load_source_task_execution_rows(parity_audit: Mapping[str, Any]) -> list[dict[str, Any]]:
    output_root = _resolve_output_root(parity_audit)
    if output_root is None:
        return []
    return _read_jsonl(output_root / "source_task_executions.jsonl")


def _load_claim_mapping_trace_rows(parity_audit: Mapping[str, Any]) -> list[dict[str, Any]]:
    output_root = _resolve_output_root(parity_audit)
    candidates: list[Path] = []
    if output_root is not None:
        candidates.append(output_root / "brain_claim_mapping_trace.jsonl")
    repo_root = Path(__file__).resolve().parents[3]
    candidates.append(repo_root / "docs" / "operational" / "census_mode_v4_brain_claim_mapping_trace.jsonl")
    for path in candidates:
        rows = _read_jsonl(path)
        if rows:
            return rows
    return []


def _short_text(value: Any, *, max_chars: int = 260) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3].rstrip() + "..."


def _claim_trace_archetype_id(trace: Mapping[str, Any]) -> str | None:
    archetype_id = str(trace.get("archetype_id") or "").strip()
    if archetype_id:
        return archetype_id
    company_name = str(trace.get("company_name") or "").strip()
    if company_name.startswith("C") or company_name.startswith("R13_"):
        return company_name
    return None


def _claim_trace_rejection_reasons(trace: Mapping[str, Any]) -> list[str]:
    raw_reasons = trace.get("eligibility_reasons") or trace.get("source_task_not_eligible_reasons") or []
    reasons = [str(reason) for reason in raw_reasons if str(reason).strip()]
    rejection_reason = str(trace.get("rejection_reason") or "").strip()
    if rejection_reason:
        reasons.extend(part.strip() for part in rejection_reason.split(";") if part.strip())
    return list(dict.fromkeys(reasons))


def _normalized_reason_key(reason: str) -> str:
    return reason.split(":", 1)[0]


def _claim_mapping_sample(trace: Mapping[str, Any]) -> dict[str, Any]:
    reasons = _claim_trace_rejection_reasons(trace)
    return {
        "claim_id": trace.get("claim_id"),
        "source_task_id": trace.get("source_task_id"),
        "symbol": trace.get("symbol"),
        "primitive_gap": trace.get("primitive_gap"),
        "primitive_id": trace.get("primitive_id"),
        "contract_rule_id": trace.get("contract_rule_id"),
        "mapping_status": trace.get("mapping_status"),
        "trace_status": trace.get("trace_status"),
        "semantic_status": trace.get("semantic_status"),
        "target_scope_status": trace.get("target_scope_status"),
        "temporal_status": trace.get("temporal_status"),
        "source_provider": trace.get("source_provider"),
        "source_url": trace.get("source_url"),
        "rejection_reasons": reasons[:6],
        "quote_excerpt": _short_text(trace.get("quote_text") or trace.get("exact_quote")),
    }


def _claim_mapping_trace_audit_by_archetype(
    claim_mapping_trace_rows: list[Mapping[str, Any]],
) -> dict[str, dict[str, Any]]:
    audit: dict[str, dict[str, Any]] = {}
    for trace in claim_mapping_trace_rows:
        archetype_id = _claim_trace_archetype_id(trace)
        if not archetype_id:
            continue
        row = audit.setdefault(
            archetype_id,
            {
                "claim_mapping_trace_log_count": 0,
                "claim_mapping_accepted_trace_count": 0,
                "claim_mapping_rejected_trace_count": 0,
                "claim_mapping_rejection_reason_counts": Counter(),
                "claim_mapping_rejected_samples": [],
            },
        )
        row["claim_mapping_trace_log_count"] += 1
        accepted = trace.get("accepted") is True or trace.get("trace_status") == "ACCEPTED_FOR_SCORE"
        if accepted:
            row["claim_mapping_accepted_trace_count"] += 1
            continue

        row["claim_mapping_rejected_trace_count"] += 1
        for reason in _claim_trace_rejection_reasons(trace):
            row["claim_mapping_rejection_reason_counts"][_normalized_reason_key(reason)] += 1
        if len(row["claim_mapping_rejected_samples"]) < 3:
            row["claim_mapping_rejected_samples"].append(_claim_mapping_sample(trace))

    normalized: dict[str, dict[str, Any]] = {}
    for archetype_id, row in audit.items():
        reason_counts = row["claim_mapping_rejection_reason_counts"]
        normalized[archetype_id] = {
            "claim_mapping_trace_log_count": row["claim_mapping_trace_log_count"],
            "claim_mapping_accepted_trace_count": row["claim_mapping_accepted_trace_count"],
            "claim_mapping_rejected_trace_count": row["claim_mapping_rejected_trace_count"],
            "claim_mapping_rejection_reason_counts": dict(sorted(reason_counts.items())),
            "claim_mapping_top_rejection_reasons": [
                {"reason": reason, "count": count} for reason, count in reason_counts.most_common(8)
            ],
            "claim_mapping_rejected_samples": row["claim_mapping_rejected_samples"],
        }
    return normalized


def _empty_claim_mapping_trace_audit() -> dict[str, Any]:
    return {
        "claim_mapping_trace_log_count": 0,
        "claim_mapping_accepted_trace_count": 0,
        "claim_mapping_rejected_trace_count": 0,
        "claim_mapping_rejection_reason_counts": {},
        "claim_mapping_top_rejection_reasons": [],
        "claim_mapping_rejected_samples": [],
    }


def _source_task_failure_axes(execution: Mapping[str, Any]) -> list[str]:
    axes: list[str] = []
    accepted_claim_ids = execution.get("accepted_claim_ids") or []
    direct_accepted_claim_ids = execution.get("direct_accepted_claim_ids") or []
    rerouted_accepted_claim_ids = execution.get("rerouted_accepted_claim_ids") or []
    stop_reason = str(execution.get("stop_reason") or "")
    status = str(execution.get("status") or "")
    not_eligible = [str(value) for value in (execution.get("not_eligible_reasons") or [])]

    if direct_accepted_claim_ids or (accepted_claim_ids and execution.get("satisfies_source_task") is True):
        axes.append("DIRECT_ACCEPTED_CLAIM")
    elif rerouted_accepted_claim_ids:
        axes.append("REROUTED_ACCEPTED_CLAIM_ORIGINAL_GAP_UNSATISFIED")
    elif accepted_claim_ids:
        axes.append("ACCEPTED_CLAIM_NOT_TASK_SATISFYING")
    else:
        axes.append("NO_ACCEPTED_CLAIM")

    if status == "PROVIDER_FAILED":
        axes.append("PROVIDER_FAILED")
    if status == "REJECTED_BY_POLICY" or stop_reason == "source_task_rejected_by_v4_policy":
        axes.append("POLICY_REJECTED")
    if status == "NO_EVIDENCE_FOUND" or stop_reason == "no_score_eligible_real_claim":
        axes.append("NO_SCORE_ELIGIBLE_REAL_CLAIM")
    if stop_reason == "accepted_baseline_claim_without_task_primitive":
        axes.append("BASELINE_CLAIM_NOT_TASK_PRIMITIVE")
    if execution.get("provider_errors"):
        axes.append("PROVIDER_ERROR_RECORDED")
    if not execution.get("fetched_document_ids"):
        axes.append("NO_FETCHED_DOCUMENT")
    if execution.get("primitive_gap_unsatisfied_ids"):
        axes.append("PRIMITIVE_GAP_UNSATISFIED")
    if any(reason.startswith("primitive_mapping_rejected") for reason in not_eligible):
        axes.append("PRIMITIVE_MAPPING_REJECTED")
    if any(reason.startswith("mapping_not_accepted") for reason in not_eligible):
        axes.append("MAPPING_NOT_ACCEPTED")
    if any(
        reason.startswith(("semantic_rejected", "target_scope_not_allowed", "target_not_direct"))
        for reason in not_eligible
    ):
        axes.append("SEMANTIC_OR_TARGET_REJECTED")
    if any(reason.startswith(("anchor_validation", "source_lineage_unverified_original")) for reason in not_eligible):
        axes.append("ANCHOR_OR_LINEAGE_REJECTED")
    return axes


def _source_task_execution_audit_by_archetype(
    runtime_source_task_executions: list[Mapping[str, Any]],
) -> dict[str, dict[str, Any]]:
    audit: dict[str, dict[str, Any]] = {}
    for execution in runtime_source_task_executions:
        archetype_id = execution.get("archetype_id")
        if not archetype_id:
            continue
        row = audit.setdefault(
            str(archetype_id),
            {
                "source_task_execution_log_count": 0,
                "source_task_no_accepted_claim_execution_count": 0,
                "source_task_direct_accepted_claim_count": 0,
                "source_task_rerouted_accepted_claim_count": 0,
                "source_task_any_accepted_claim_count": 0,
                "source_task_rejected_claim_count": 0,
                "failure_axis_counts": Counter(),
                "status_counts": Counter(),
                "stop_reason_counts": Counter(),
                "provider_error_counts": Counter(),
                "not_eligible_reason_counts": Counter(),
                "unsatisfied_primitive_counts": Counter(),
            },
        )
        row["source_task_execution_log_count"] += 1
        accepted_claim_ids = execution.get("accepted_claim_ids") or []
        direct_accepted_claim_ids = execution.get("direct_accepted_claim_ids") or []
        rerouted_accepted_claim_ids = execution.get("rerouted_accepted_claim_ids") or []
        if not accepted_claim_ids:
            row["source_task_no_accepted_claim_execution_count"] += 1
        row["source_task_any_accepted_claim_count"] += len(accepted_claim_ids)
        row["source_task_direct_accepted_claim_count"] += len(direct_accepted_claim_ids)
        row["source_task_rerouted_accepted_claim_count"] += len(rerouted_accepted_claim_ids)
        row["source_task_rejected_claim_count"] += len(execution.get("rejected_claim_ids") or [])

        row["status_counts"][str(execution.get("status") or "UNKNOWN")] += 1
        row["stop_reason_counts"][str(execution.get("stop_reason") or "UNKNOWN")] += 1
        for error in execution.get("provider_errors") or []:
            row["provider_error_counts"][str(error)] += 1
        for reason in execution.get("not_eligible_reasons") or []:
            row["not_eligible_reason_counts"][str(reason).split(":", 1)[0]] += 1
        for primitive_id in execution.get("primitive_gap_unsatisfied_ids") or []:
            row["unsatisfied_primitive_counts"][str(primitive_id)] += 1
        for axis in _source_task_failure_axes(execution):
            row["failure_axis_counts"][axis] += 1

    normalized: dict[str, dict[str, Any]] = {}
    for archetype_id, row in audit.items():
        failure_axis_counts = row["failure_axis_counts"]
        normalized[archetype_id] = {
            "source_task_execution_log_count": row["source_task_execution_log_count"],
            "source_task_no_accepted_claim_execution_count": row["source_task_no_accepted_claim_execution_count"],
            "source_task_direct_accepted_claim_count": row["source_task_direct_accepted_claim_count"],
            "source_task_rerouted_accepted_claim_count": row["source_task_rerouted_accepted_claim_count"],
            "source_task_any_accepted_claim_count": row["source_task_any_accepted_claim_count"],
            "source_task_rejected_claim_count": row["source_task_rejected_claim_count"],
            "source_task_failure_axis_counts": dict(sorted(failure_axis_counts.items())),
            "source_task_top_failure_axes": [
                {"axis": axis, "count": count} for axis, count in failure_axis_counts.most_common(6)
            ],
            "source_task_status_counts": dict(sorted(row["status_counts"].items())),
            "source_task_stop_reason_counts": dict(sorted(row["stop_reason_counts"].items())),
            "source_task_provider_error_counts": dict(sorted(row["provider_error_counts"].items())),
            "source_task_not_eligible_reason_counts": dict(sorted(row["not_eligible_reason_counts"].items())),
            "source_task_top_unsatisfied_primitives": [
                {"primitive_id": primitive_id, "count": count}
                for primitive_id, count in row["unsatisfied_primitive_counts"].most_common(8)
            ],
        }
    return normalized


def _empty_source_task_execution_audit() -> dict[str, Any]:
    return {
        "source_task_execution_log_count": 0,
        "source_task_no_accepted_claim_execution_count": 0,
        "source_task_direct_accepted_claim_count": 0,
        "source_task_rerouted_accepted_claim_count": 0,
        "source_task_any_accepted_claim_count": 0,
        "source_task_rejected_claim_count": 0,
        "source_task_failure_axis_counts": {},
        "source_task_top_failure_axes": [],
        "source_task_status_counts": {},
        "source_task_stop_reason_counts": {},
        "source_task_provider_error_counts": {},
        "source_task_not_eligible_reason_counts": {},
        "source_task_top_unsatisfied_primitives": [],
    }


def _required_positive_missing_rate(row: Mapping[str, Any]) -> float | None:
    full_rows = int(row.get("runtime_full_thesis_row_count") or 0)
    if full_rows <= 0:
        return None
    return round(int(row.get("runtime_full_thesis_row_with_required_positive_missing_count") or 0) / full_rows, 6)


def _green_gap_rate(row: Mapping[str, Any]) -> float | None:
    full_rows = int(row.get("runtime_full_thesis_row_count") or 0)
    if full_rows <= 0:
        return None
    return round(int(row.get("runtime_full_thesis_row_with_green_gap_count") or 0) / full_rows, 6)


def _goal4_runtime_status(
    *,
    row: Mapping[str, Any],
    attempt_status: str,
    source_execution_status: str,
    accepted_claim_status: str,
    full_thesis_status: str,
    proof_status: str,
) -> str:
    if proof_status == "RUNTIME_PARITY_PROVEN":
        return "MEANINGFUL_FULL_THESIS_READY"
    if full_thesis_status == "SCORE_PATH_ONLY_WITH_REQUIRED_OR_GREEN_GAPS":
        return "SCORE_PATH_CLOSED_WITH_THESIS_GAPS"
    if full_thesis_status == "FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP":
        return "SOURCE_REPAIR_REQUIRED"
    if accepted_claim_status == "ACCEPTED_CLAIM_PRESENT_NOT_FULL_THESIS_CLOSED":
        return "SCORE_PATH_NOT_CLOSED"
    if source_execution_status == "SOURCE_TASK_EXECUTED_NO_ACCEPTED_CLAIMS":
        return "SOURCE_REPAIR_REQUIRED"
    if source_execution_status == "SOURCE_TASK_EXECUTED_WITH_ACCEPTED_CLAIMS":
        return "SCORE_PATH_NOT_CLOSED"
    if attempt_status == "ARCHETYPE_DISCOVERY_TARGET_MATERIALIZATION_REQUIRED":
        return "TARGET_MATERIALIZATION_REQUIRED"
    if attempt_status == "PLANNER_ATTEMPTED_ONLY":
        return "PLANNING_ONLY"
    if attempt_status == "REPLAY_READY_NOT_RUNTIME_ATTEMPTED":
        return "REPLAY_ONLY_NOT_RUNTIME_PROVEN"
    if int(row.get("source_backed_fixture_count") or 0):
        return "REPLAY_ONLY_NOT_RUNTIME_PROVEN"
    return "NOT_ATTEMPTED"


def _primary_blocker_class(
    *,
    row: Mapping[str, Any],
    card_ready: bool,
    route_pattern_count: int,
    attempt_status: str,
    source_execution_status: str,
    accepted_claim_status: str,
    full_thesis_status: str,
) -> str:
    if not card_ready:
        return "NO_RESEARCH_MEMORY"
    if int(row.get("runtime_full_thesis_row_with_required_positive_missing_count") or 0):
        return "REQUIRED_POSITIVE_MISSING"
    if int(row.get("runtime_full_thesis_row_with_green_gap_count") or 0):
        return "GREEN_GAP_MISSING"
    if full_thesis_status == "MEANINGFUL_FULL_THESIS_READY":
        return "NONE"
    if full_thesis_status == "FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP":
        return "REQUIRED_POSITIVE_MISSING"
    if source_execution_status == "SOURCE_TASK_EXECUTED_NO_ACCEPTED_CLAIMS":
        return "ACCEPTED_CLAIM_NOT_CREATED"
    if accepted_claim_status == "ACCEPTED_CLAIM_PRESENT_NOT_FULL_THESIS_CLOSED":
        return "SCORE_PATH_NOT_CLOSED"
    if attempt_status == "ARCHETYPE_DISCOVERY_TARGET_MATERIALIZATION_REQUIRED":
        return "CANDIDATE_SELECTOR_DID_NOT_ATTEMPT"
    if attempt_status == "PLANNER_ATTEMPTED_ONLY":
        return "SOURCE_TASK_NOT_CREATED"
    if attempt_status == "REPLAY_READY_NOT_RUNTIME_ATTEMPTED":
        return "URL_BACKED_CASE_EXISTS_BUT_NOT_REPLAYED"
    if route_pattern_count == 0:
        return "SOURCE_ROUTE_NOT_RECOVERED"
    return "ACCEPTED_CLAIM_NOT_CREATED"


def _blocker_detail(primary_blocker_class: str) -> str:
    details = {
        "NONE": "meaningful full thesis evidence row로 볼 수 있는 상태다.",
        "NO_RESEARCH_MEMORY": "이 아키타입은 연구 memory card가 없어 운영 query intent를 만들 근거가 없다.",
        "SOURCE_ROUTE_NOT_RECOVERED": "연구 판례에서 어떤 source family를 우선 찾아야 하는지 route가 복원되지 않았다.",
        "URL_BACKED_CASE_EXISTS_BUT_NOT_REPLAYED": "URL-backed 연구 판례는 있지만 이번 production runtime에서 source-backed row로 재실행되지 않았다.",
        "CANDIDATE_SELECTOR_DID_NOT_ATTEMPT": "아키타입 discovery는 열렸지만 실제 종목 symbol이 materialize되지 않아 issuer claim으로 닫히지 않았다.",
        "SOURCE_TASK_NOT_CREATED": "planner 가설은 있었지만 bounded source task 생성/실행까지 이어지지 않았다.",
        "ACCEPTED_CLAIM_NOT_CREATED": "source task는 실행됐지만 운영 원문에서 accepted claim을 만들지 못했다.",
        "SCORE_PATH_NOT_CLOSED": "accepted claim은 있으나 score contribution, StageCourt, full thesis row까지 이어지지 않았다.",
        "REQUIRED_POSITIVE_MISSING": "점수 경로 또는 후보는 생겼지만 아키타입 필수 positive primitive가 source-backed claim으로 채워지지 않았다.",
        "GREEN_GAP_MISSING": "기본 점수 경로는 있으나 Green 판단에 필요한 source-backed primitive가 남아 있다.",
    }
    return details.get(primary_blocker_class, "goal4 blocker class가 row에 기록됐지만 별도 설명이 필요하다.")


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
    if int(row.get("targetless_source_task_execution_count") or 0) or int(
        row.get("target_materialization_required_seed_count") or 0
    ):
        return "MATERIALIZE_REAL_TARGET_SYMBOLS_FROM_ARCHETYPE_DISCOVERY_BEFORE_SOURCE_EXECUTION"
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
    if attempt_status == "ARCHETYPE_DISCOVERY_TARGET_MATERIALIZATION_REQUIRED":
        return "아키타입 수준 discovery seed는 실행됐지만 실제 target symbol이 없어 source-backed issuer claim으로 닫힐 수 없다."
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
    research_inventory: Mapping[str, Any] | None = None,
    runtime_source_task_executions: list[Mapping[str, Any]] | None = None,
    claim_mapping_trace_rows: list[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    cards_by_id = {card["archetype_id"]: card for card in memory_cards.get("cards", [])}
    inventory_counts = _inventory_counts_by_archetype(research_inventory)
    if runtime_source_task_executions is None:
        runtime_source_task_executions = _load_source_task_execution_rows(parity_audit)
    if claim_mapping_trace_rows is None:
        claim_mapping_trace_rows = _load_claim_mapping_trace_rows(parity_audit)
    source_task_execution_audit = _source_task_execution_audit_by_archetype(runtime_source_task_executions)
    claim_mapping_trace_audit = _claim_mapping_trace_audit_by_archetype(claim_mapping_trace_rows)
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
        card_ready = archetype_id in cards_by_id
        research_counts = _research_counts(archetype_id, card, inventory_counts)
        runtime_source_task_executed_count = int(row.get("runtime_source_task_execution_count") or 0) + int(
            row.get("targetless_source_task_execution_count") or 0
        )
        runtime_source_task_count = (
            runtime_source_task_executed_count
            + int(row.get("runtime_follow_up_source_task_count") or 0)
            + gap_task_counts[archetype_id]
        )
        runtime_status = _goal4_runtime_status(
            row=row,
            attempt_status=attempt_status,
            source_execution_status=source_execution_status,
            accepted_claim_status=accepted_claim_status,
            full_thesis_status=full_thesis_status,
            proof_status=proof_status,
        )
        primary_blocker_class = _primary_blocker_class(
            row=row,
            card_ready=card_ready,
            route_pattern_count=route_pattern_count,
            attempt_status=attempt_status,
            source_execution_status=source_execution_status,
            accepted_claim_status=accepted_claim_status,
            full_thesis_status=full_thesis_status,
        )
        source_task_audit = source_task_execution_audit.get(archetype_id, _empty_source_task_execution_audit())
        claim_mapping_audit = claim_mapping_trace_audit.get(archetype_id, _empty_claim_mapping_trace_audit())
        source_route_gaps: list[str] = []
        if route_pattern_count == 0:
            source_route_gaps.append("SOURCE_ROUTE_NOT_RECOVERED")
        if gap_task_counts[archetype_id]:
            source_route_gaps.append("SOURCE_ROUTE_GAP_TASKS_PRESENT")
        if research_counts["source_proxy_case_count"]:
            source_route_gaps.append("SOURCE_PROXY_CASES_REQUIRE_REPAIR")
        if research_counts["evidence_url_pending_count"]:
            source_route_gaps.append("EVIDENCE_URL_PENDING_CASES_REQUIRE_REPAIR")
        status_rows.append(
            {
                "schema_version": "e2r_all_archetype_runtime_status_row_v1",
                "archetype_id": archetype_id,
                "archetype_prefix": _prefix(archetype_id),
                "large_sector_id": card.get("large_sector_id"),
                "exists_in_registry": True,
                "contract_registration_status": "REGISTERED",
                "registry_scope": "C01_TO_C32" if _prefix(archetype_id).startswith("C") else "R13_CROSS_ARCHETYPE",
                "research_memory_status": "MEMORY_CARD_READY" if card_ready else "MEMORY_CARD_MISSING",
                **research_counts,
                "source_route_recovery_status": source_route_recovery_status,
                "runtime_attempt_status": attempt_status,
                "runtime_source_route_execution_status": source_execution_status,
                "accepted_claim_status": accepted_claim_status,
                "full_thesis_status": full_thesis_status,
                "runtime_parity_proof_status": proof_status,
                "runtime_status": runtime_status,
                "primary_blocker_class": primary_blocker_class,
                "blocker_detail": _blocker_detail(primary_blocker_class),
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
                "source_route_ready": route_pattern_count > 0,
                "source_route_gaps": source_route_gaps,
                "memory_card_ready": card_ready,
                "memory_required_positive_primitive_count": len(card.get("required_positive_primitives") or []),
                "memory_url_backed_replay_case_count": len(card.get("url_backed_replay_cases") or []),
                "memory_source_proxy_only_case_count": len(card.get("source_proxy_only_cases") or []),
                "source_backed_fixture_count": row.get("source_backed_fixture_count", 0),
                "replay_accepted_claim_count": row.get("replay_accepted_claim_count", 0),
                "runtime_planner_top1_count": row.get("runtime_planner_top1_count", 0),
                "runtime_planner_attempt_count": row.get("runtime_planner_top1_count", 0),
                "runtime_planner_topk_count": row.get("runtime_planner_topk_count", 0),
                "runtime_source_task_count": runtime_source_task_count,
                "runtime_source_task_executed_count": runtime_source_task_executed_count,
                **source_task_audit,
                **claim_mapping_audit,
                "runtime_source_task_execution_count": row.get("runtime_source_task_execution_count", 0),
                "targetless_source_task_execution_count": row.get("targetless_source_task_execution_count", 0),
                "archetype_level_discovery_seed_count": row.get("archetype_level_discovery_seed_count", 0),
                "target_materialization_required_seed_count": row.get(
                    "target_materialization_required_seed_count", 0
                ),
                "placeholder_symbol_seed_count": row.get("placeholder_symbol_seed_count", 0),
                "runtime_source_task_accepted_claim_count": row.get("runtime_source_task_accepted_claim_count", 0),
                "runtime_accepted_claim_count": row.get("runtime_accepted_claim_count", 0),
                "runtime_score_contribution_count": row.get("runtime_score_contribution_count", 0),
                "runtime_stagecourt_trace_count": row.get("runtime_stagecourt_trace_count", 0),
                "runtime_candidate_attempt_count": row.get("runtime_candidate_attempt_count", 0),
                "runtime_blocked_candidate_count": row.get("runtime_blocked_candidate_count", 0),
                "runtime_full_thesis_row_count": row.get("runtime_full_thesis_row_count", 0),
                "runtime_full_thesis_row_with_required_positive_missing_count": row.get(
                    "runtime_full_thesis_row_with_required_positive_missing_count", 0
                ),
                "runtime_full_thesis_row_with_green_gap_count": row.get(
                    "runtime_full_thesis_row_with_green_gap_count", 0
                ),
                "required_positive_missing_rate": _required_positive_missing_rate(row),
                "green_gap_rate": _green_gap_rate(row),
                "followup_task_count": row.get("runtime_follow_up_source_task_count", 0),
                "source_repair_task_count": gap_task_counts[archetype_id]
                + research_counts["source_proxy_case_count"]
                + research_counts["evidence_url_pending_count"],
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
    source_execution_counts = Counter(row["runtime_source_route_execution_status"] for row in status_rows)
    full_thesis_counts = Counter(row["full_thesis_status"] for row in status_rows)
    accepted_counts = Counter(row["accepted_claim_status"] for row in status_rows)
    runtime_status_counts = Counter(row["runtime_status"] for row in status_rows)
    primary_blocker_counts = Counter(row["primary_blocker_class"] for row in status_rows)

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
        "runtime_source_route_execution_status_counts": dict(sorted(source_execution_counts.items())),
        "accepted_claim_status_counts": dict(sorted(accepted_counts.items())),
        "full_thesis_status_counts": dict(sorted(full_thesis_counts.items())),
        "runtime_status_counts": dict(sorted(runtime_status_counts.items())),
        "primary_blocker_class_counts": dict(sorted(primary_blocker_counts.items())),
        "source_route_ready_count": sum(1 for row in status_rows if row["source_route_ready"]),
        "memory_card_ready_count": sum(1 for row in status_rows if row["memory_card_ready"]),
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
        f"- runtime_source_route_execution_status_counts: `{json.dumps(matrix['runtime_source_route_execution_status_counts'], ensure_ascii=False, sort_keys=True)}`",
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


def render_all_archetype_runtime_parity_summary_markdown(matrix: Mapping[str, Any]) -> str:
    def fmt_rate(value: Any) -> str:
        return "-" if value is None else str(value)

    def fmt_failure_axes(row: Mapping[str, Any]) -> str:
        axes = row.get("source_task_top_failure_axes") or []
        if not axes:
            return "-"
        return ", ".join(f"{item['axis']}:{item['count']}" for item in axes[:3])

    def fmt_claim_rejections(row: Mapping[str, Any]) -> str:
        reasons = row.get("claim_mapping_top_rejection_reasons") or []
        if not reasons:
            return "-"
        return ", ".join(f"{item['reason']}:{item['count']}" for item in reasons[:3])

    lines = [
        "# All Archetype Runtime Parity Summary - 2026-07-05",
        "",
        "이 문서는 goal4가 요구한 안정 파일명용 요약이다. 같은 rows를 `all_archetype_runtime_parity_matrix.json`에 저장한다.",
        "",
        "쉬운 예: 연구자료는 진료과별 교과서이고, source route는 어느 검사를 해야 하는지 적은 처방전이다. 하지만 production accepted claim은 실제 검사 결과지다. 처방전이 있어도 검사 결과지가 없으면 점수에 넣을 수 없다.",
        "",
        "## Verdict",
        "",
        f"- registry_contract_count: `{matrix['registry_contract_count']}`",
        f"- c01_to_c32_contract_count: `{matrix['c01_to_c32_contract_count']}`",
        f"- r13_cross_archetype_contract_count: `{matrix['r13_cross_archetype_contract_count']}`",
        f"- source_route_ready_count: `{matrix['source_route_ready_count']}`",
        f"- memory_card_ready_count: `{matrix['memory_card_ready_count']}`",
        f"- meaningful_runtime_parity_ready: `{matrix['meaningful_runtime_parity_ready']}`",
        "",
        "## Runtime Status Counts",
        "",
        f"- runtime_status_counts: `{json.dumps(matrix['runtime_status_counts'], ensure_ascii=False, sort_keys=True)}`",
        f"- primary_blocker_class_counts: `{json.dumps(matrix['primary_blocker_class_counts'], ensure_ascii=False, sort_keys=True)}`",
        f"- runtime_parity_proof_status_counts: `{json.dumps(matrix['runtime_parity_proof_status_counts'], ensure_ascii=False, sort_keys=True)}`",
        "",
        "## Matrix",
        "",
        "| archetype | runtime status | primary blocker | research cases | URL-backed | source tasks | execution logs | claim traces | accepted claims | full rows | top source-task failure axes | top claim rejection reasons | req gap rate | green gap rate |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---:|---:|",
    ]
    for row in matrix.get("rows", []):
        accepted = int(row.get("runtime_accepted_claim_count") or 0) + int(
            row.get("runtime_source_task_accepted_claim_count") or 0
        )
        lines.append(
            "| {archetype} | {runtime_status} | {blocker} | {research_cases} | {url_backed} | {source_tasks} | {execution_logs} | {claim_traces} | {accepted} | {full_rows} | {failure_axes} | {claim_rejections} | {req_rate} | {green_rate} |".format(
                archetype=row["archetype_id"],
                runtime_status=row["runtime_status"],
                blocker=row["primary_blocker_class"],
                research_cases=row["research_case_count"],
                url_backed=row["url_backed_case_count"],
                source_tasks=row["runtime_source_task_count"],
                execution_logs=row["source_task_execution_log_count"],
                claim_traces=row["claim_mapping_trace_log_count"],
                accepted=accepted,
                full_rows=row["runtime_full_thesis_row_count"],
                failure_axes=fmt_failure_axes(row),
                claim_rejections=fmt_claim_rejections(row),
                req_rate=fmt_rate(row["required_positive_missing_rate"]),
                green_rate=fmt_rate(row["green_gap_rate"]),
            )
        )
    lines.extend(
        [
            "",
            "## Operator Reading",
            "",
            "- `SCORE_PATH_CLOSED_WITH_THESIS_GAPS`: 점수 계산 경로는 닫혔지만 필수 positive 또는 Green 증거가 남아 있다.",
            "- `SOURCE_REPAIR_REQUIRED`: 연구 route나 source task는 있지만 current accepted claim이 부족하다.",
            "- `PLANNING_ONLY`: planner나 discovery는 열렸지만 실제 종목/소스 실행으로 닫히지 않았다.",
            "- `REPLAY_ONLY_NOT_RUNTIME_PROVEN`: 과거 URL-backed 판례가 있을 뿐, 현재 production run에서 재검증되지 않았다.",
            "- `top source-task failure axes`: source task가 왜 accepted claim으로 닫히지 않았는지의 실행 로그 기반 요약이다.",
            "- `top claim rejection reasons`: 실제 원문 claim 매핑 trace에서 왜 score-eligible claim이 되지 못했는지의 상위 원인이다.",
            "",
            "즉 이 summary에서 중요한 것은 높은 row count가 아니라 `accepted claims -> score contributions -> full thesis row`가 아키타입별로 닫혔는지다.",
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
    research_inventory: Mapping[str, Any] | None = None,
    docs_dir: str | Path = "docs/operational",
) -> dict[str, Any]:
    docs_path = Path(docs_dir)
    docs_path.mkdir(parents=True, exist_ok=True)
    matrix = build_all_archetype_runtime_status_matrix(
        parity_audit=parity_audit,
        memory_cards=memory_cards,
        source_routes=source_routes,
        candidate_selection=candidate_selection,
        research_inventory=research_inventory,
        runtime_source_task_executions=_load_source_task_execution_rows(parity_audit),
        claim_mapping_trace_rows=_load_claim_mapping_trace_rows(parity_audit),
    )
    json_path = docs_path / "all_archetype_runtime_status_matrix_2026-07-05.json"
    md_path = docs_path / "all_archetype_runtime_status_matrix_2026-07-05.md"
    alias_json_path = docs_path / "all_archetype_runtime_status_matrix.json"
    parity_json_path = docs_path / "all_archetype_runtime_parity_matrix.json"
    parity_summary_path = docs_path / "all_archetype_runtime_parity_summary.md"
    json_text = json.dumps(matrix, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    json_path.write_text(json_text, encoding="utf-8")
    alias_json_path.write_text(json_text, encoding="utf-8")
    parity_json_path.write_text(json_text, encoding="utf-8")
    md_path.write_text(render_all_archetype_runtime_status_markdown(matrix), encoding="utf-8")
    parity_summary_path.write_text(render_all_archetype_runtime_parity_summary_markdown(matrix), encoding="utf-8")
    return {
        "matrix": matrix,
        "json_path": json_path,
        "alias_json_path": alias_json_path,
        "markdown_path": md_path,
        "parity_json_path": parity_json_path,
        "parity_summary_path": parity_summary_path,
    }


__all__ = [
    "build_all_archetype_runtime_status_matrix",
    "render_all_archetype_runtime_parity_summary_markdown",
    "render_all_archetype_runtime_status_markdown",
    "write_all_archetype_runtime_status_matrix",
]
