"""Rolling v12 promotion-decision planner.

The v12 ingest layer is intentionally shadow-only. This module turns the
shadow candidates into a ledger of apply/hold/block decisions and small,
reversible patch specs for a later explicit E2R 2.2 scoring task.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
import json
import re


DECISIONS = {
    "apply_next_patch",
    "hold_for_more_evidence",
    "blocked_by_data_quality",
    "blocked_by_logic_risk",
}

SAFETY_AXES = {
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "earlier_thesis_break_watch",
    "hard_4c_confirmation",
}

FULL_4B_AXES = {"full_4b_overlay_candidate"}
TYPE2_AXES = {"stage2_bonus_candidate_delta"}


def _json_default(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    return value


def _write_json(path: Path, payload: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, default=_json_default, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    return path


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True, default=_json_default, allow_nan=False) + "\n")
    return path


def _safe_int(value: Any) -> int:
    if isinstance(value, bool) or value is None:
        return 0
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return 0


def _safe_float(value: Any) -> float:
    if isinstance(value, bool) or value is None:
        return 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _rate(count: int, total: int) -> float:
    if total <= 0:
        return 0.0
    return round(count / total, 4)


def _truthy_text(value: Any) -> bool:
    if value is None:
        return False
    text = str(value).strip().lower()
    return bool(text) and text not in {"none", "null", "n/a", "na", "unknown", "unavailable"}


def _canonical_token(value: Any) -> str | None:
    if not _truthy_text(value):
        return None
    text = str(value).strip().lower()
    text = re.sub(r"[^0-9a-zA-Z가-힣_+./%-]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    if not text or text in {"songdaiki/stock-web", "public_report_proxy", "price", "price_only"}:
        return None
    return text[:96]


def _split_tokens(value: Any) -> list[str]:
    if isinstance(value, list):
        parts = value
    else:
        parts = re.split(r"[,;|/\n]+", str(value or ""))
    tokens = []
    for part in parts:
        token = _canonical_token(part)
        if token:
            tokens.append(token)
    return tokens


def _row_evidence_tokens(row: dict[str, Any]) -> list[str]:
    keys = (
        "evidence_family",
        "trigger_family",
        "evidence_source",
        "evidence_available_at_that_date",
        "supporting_evidence_fields",
        "must_have_fields",
        "key_evidence_fields",
        "positive_evidence_fields",
        "negative_evidence_fields",
    )
    tokens: list[str] = []
    for key in keys:
        if row.get(key):
            tokens.extend(_split_tokens(row.get(key)))
    return tokens


def _positive_row(row: dict[str, Any]) -> bool:
    label = str(row.get("positive_or_counterexample") or "").lower()
    case_type = str(row.get("case_type") or "").lower()
    return label == "positive" or case_type in {"structural_success", "success_candidate", "cyclical_success"}


def _success_candidate_row(row: dict[str, Any]) -> bool:
    return str(row.get("case_type") or "").lower() == "success_candidate"


def _counterexample_row(row: dict[str, Any]) -> bool:
    label = str(row.get("positive_or_counterexample") or "").lower()
    case_type = str(row.get("case_type") or "").lower()
    return label == "counterexample" or case_type in {
        "one_off",
        "overheat",
        "failed_rerating",
        "4c_thesis_break",
        "boom_bust",
    }


def _unique_symbols(rows: list[dict[str, Any]], predicate) -> list[str]:
    return sorted({str(row.get("symbol")) for row in rows if row.get("symbol") and predicate(row)})


def _unique_case_ids(rows: list[dict[str, Any]], predicate, limit: int = 12) -> list[str]:
    dated: list[tuple[str, str]] = []
    for row in rows:
        case_id = row.get("case_id")
        if not case_id or not predicate(row):
            continue
        date = str(row.get("trigger_date") or row.get("entry_date") or "")
        dated.append((date, str(case_id)))
    ordered = [case_id for _, case_id in sorted(dated, reverse=True)]
    deduped = []
    seen = set()
    for case_id in ordered:
        if case_id not in seen:
            deduped.append(case_id)
            seen.add(case_id)
    return deduped[:limit]


def _common_evidence(rows: list[dict[str, Any]], predicate, limit: int = 8) -> list[str]:
    counter: Counter[str] = Counter()
    for row in rows:
        if predicate(row):
            counter.update(_row_evidence_tokens(row))
    return [token for token, _ in counter.most_common(limit)]


def _group_rows_by_archetype(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        archetype = row.get("canonical_archetype_id")
        if archetype:
            grouped[str(archetype)].append(row)
    return dict(grouped)


def _most_common(values: list[Any]) -> Any:
    filtered = [value for value in values if _truthy_text(value)]
    if not filtered:
        return None
    return Counter(filtered).most_common(1)[0][0]


def build_archetype_evidence_state(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Build the cumulative evidence ledger by canonical archetype."""

    state: dict[str, dict[str, Any]] = {}
    for archetype, members in sorted(_group_rows_by_archetype(rows).items()):
        positive_symbols = _unique_symbols(members, _positive_row)
        counter_symbols = _unique_symbols(members, _counterexample_row)
        stage4b_cases = _unique_case_ids(members, lambda row: row.get("trigger_type") == "Stage4B", limit=20)
        stage4c_cases = _unique_case_ids(members, lambda row: row.get("trigger_type") == "Stage4C", limit=20)
        state[archetype] = {
            "large_sector_id": _most_common([row.get("large_sector_id") for row in members]),
            "canonical_archetype_id": archetype,
            "unique_positive_symbols": positive_symbols,
            "unique_success_candidate_symbols": _unique_symbols(members, _success_candidate_row),
            "unique_counterexample_symbols": counter_symbols,
            "unique_4b_cases": stage4b_cases,
            "unique_4c_cases": stage4c_cases,
            "latest_positive_case_ids": _unique_case_ids(members, _positive_row),
            "latest_counterexample_case_ids": _unique_case_ids(members, _counterexample_row),
            "common_positive_evidence_fields": _common_evidence(members, _positive_row),
            "common_failure_evidence_fields": _common_evidence(members, _counterexample_row),
            "current_patch_state": "unpatched_shadow",
            "last_patch_version": None,
            "next_delta_recommendation": "pending_promotion_decision",
        }
    return state


def _build_patch_support_state(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Build support case IDs for both archetype and large-sector patch scopes."""

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        large_sector = row.get("large_sector_id")
        archetype = row.get("canonical_archetype_id")
        if large_sector:
            grouped[f"large_sector:{large_sector}"].append(row)
        if archetype:
            grouped[f"canonical_archetype:{archetype}"].append(row)

    return {
        scope: {
            "latest_positive_case_ids": _unique_case_ids(members, _positive_row),
            "latest_counterexample_case_ids": _unique_case_ids(members, _counterexample_row),
            "latest_support_case_ids": _unique_case_ids(members, lambda row: True, limit=20),
        }
        for scope, members in grouped.items()
    }


def _transition_count_for_scope(
    stage_transition_rows: list[dict[str, Any]],
    *,
    scope: str,
    large_sector_id: str | None,
    canonical_archetype_id: str | None,
) -> int:
    count = 0
    for row in stage_transition_rows:
        if scope == "large_sector" and large_sector_id and row.get("large_sector_id") == large_sector_id:
            count += 1
        elif scope == "canonical_archetype" and canonical_archetype_id and row.get("canonical_archetype_id") == canonical_archetype_id:
            count += 1
    return count


def _promotion_type(axis: str) -> str:
    if axis in SAFETY_AXES or axis in FULL_4B_AXES or "4b" in axis.lower() or "4c" in axis.lower():
        return "Type1_safety_guardrail"
    if axis in TYPE2_AXES or "stage2" in axis.lower() or "yellow" in axis.lower():
        return "Type2_stage2_yellow_observation"
    if "green" in axis.lower():
        return "Type3_stage3_green_conviction"
    return "Type2_stage2_yellow_observation"


def _is_defensive_axis(axis: str) -> bool:
    return axis in SAFETY_AXES or axis in FULL_4B_AXES or "guard" in axis.lower() or "4b" in axis.lower() or "4c" in axis.lower()


def _decision_for_candidate(candidate: dict[str, Any], transition_count: int) -> dict[str, Any]:
    axis = str(candidate.get("axis") or "")
    row_count = _safe_int(candidate.get("row_count") or candidate.get("unique_case_count"))
    positive = _safe_int(candidate.get("positive_case_count"))
    counter = _safe_int(candidate.get("counterexample_count"))
    symbols = _safe_int(candidate.get("unique_symbol_count"))
    pending = _safe_int(candidate.get("evidence_url_pending_count"))
    proxy = _safe_int(candidate.get("source_proxy_only_count"))
    good_stage2 = _safe_int(candidate.get("good_stage2_count"))
    bad_stage2 = _safe_int(candidate.get("bad_stage2_count"))
    high_mae = _safe_int(candidate.get("stage2_high_mae_count"))
    good_4b = _safe_int(candidate.get("good_4b_timing_count"))
    too_early_4b = _safe_int(candidate.get("too_early_4b_count"))
    price_only_4b = _safe_int(candidate.get("price_only_4b_count"))
    late_4c = _safe_int(candidate.get("4c_late_count"))
    hard_4c = _safe_int(candidate.get("hard_4c_count"))
    pending_rate = _rate(pending, row_count)
    proxy_rate = _rate(proxy, row_count)
    bad_stage2_rate = _rate(bad_stage2 + high_mae, max(good_stage2 + bad_stage2 + high_mae, 1))
    promo_type = _promotion_type(axis)
    defensive = _is_defensive_axis(axis)

    missing: list[str] = []
    decision = "hold_for_more_evidence"
    action = "collect_non_overlapping_cases"

    if promo_type == "Type3_stage3_green_conviction":
        if pending_rate > 0.10 or proxy_rate > 0.10:
            decision = "blocked_by_data_quality"
            missing.append("source_verified_support_rows_below_90pct")
        elif positive < 5 or counter < 3 or transition_count < 3:
            decision = "hold_for_more_evidence"
            missing.append("need_5_positive_symbols_3_counterexamples_3_full_stage_paths")
        elif bad_stage2 > 0 or price_only_4b > 0:
            decision = "blocked_by_logic_risk"
            missing.append("unsafe_green_or_price_only_risk")
        else:
            decision = "apply_next_patch"
            action = "implement_strict_archetype_green_gate"
    elif axis == "stage2_bonus_candidate_delta":
        if pending_rate > 0.25 or proxy_rate > 0.25:
            decision = "blocked_by_data_quality"
            missing.append("evidence_url_pending_or_source_proxy_rate_above_25pct")
        elif positive < 3 or counter < 2 or row_count < 8 or transition_count < 3:
            decision = "hold_for_more_evidence"
            missing.append("need_3_positive_symbols_2_counterexamples_8_rows_3_transitions")
        elif bad_stage2_rate > 0.35:
            decision = "blocked_by_logic_risk"
            missing.append("bad_stage2_or_high_mae_rate_too_high")
        else:
            decision = "apply_next_patch"
            action = "implement_bounded_stage2_bridge"
    elif axis == "full_4b_overlay_candidate":
        if pending > 0 or proxy > 0:
            decision = "blocked_by_data_quality"
            missing.append("full_4b_overlay_needs_verified_non_proxy_evidence")
        elif good_4b >= 2 and good_4b > too_early_4b + price_only_4b:
            decision = "apply_next_patch"
            action = "implement_non_price_4b_overlay"
        else:
            decision = "hold_for_more_evidence"
            missing.append("need_more_good_non_price_4b_timing_cases")
    elif defensive:
        bad_support = counter + bad_stage2 + high_mae + too_early_4b + price_only_4b + late_4c + hard_4c
        if symbols < 2 and bad_support < 3:
            decision = "hold_for_more_evidence"
            missing.append("need_more_independent_bad_cases_for_guardrail")
        elif bad_support >= 3 or counter >= 2 or good_4b >= 2 or late_4c >= 1 or hard_4c >= 1:
            decision = "apply_next_patch"
            action = "implement_defensive_guardrail"
        else:
            decision = "hold_for_more_evidence"
            missing.append("guardrail_support_below_minimum")
    else:
        if pending > 0 or proxy > 0:
            decision = "blocked_by_data_quality"
            missing.append("unverified_support_blocks_positive_patch")
        else:
            missing.append("axis_type_not_mapped_to_safe_patch")

    if decision not in DECISIONS:
        decision = "hold_for_more_evidence"
    if decision == "apply_next_patch":
        missing = []
    elif decision == "blocked_by_data_quality":
        action = "verify_evidence_urls_or_replace_source_proxy_rows"
    elif decision == "blocked_by_logic_risk":
        action = "keep_green_restricted_and_add_red_team_guard"

    return {
        "axis": axis,
        "scope": candidate.get("scope"),
        "large_sector_id": candidate.get("large_sector_id"),
        "canonical_archetype_id": candidate.get("canonical_archetype_id"),
        "decision": decision,
        "promotion_type": promo_type,
        "ready_for_next_patch": decision == "apply_next_patch",
        "missing_to_promote": missing or ["none"],
        "recommended_next_action": action,
        "row_count": row_count,
        "unique_symbol_count": symbols,
        "positive_case_count": positive,
        "counterexample_count": counter,
        "stage_transition_summary_rows": transition_count,
        "evidence_url_pending_count": pending,
        "source_proxy_only_count": proxy,
        "evidence_url_pending_support_rate": pending_rate,
        "source_proxy_only_support_rate": proxy_rate,
        "bad_stage2_rate": bad_stage2_rate,
        "good_stage2_count": good_stage2,
        "bad_stage2_count": bad_stage2,
        "good_4b_timing_count": good_4b,
        "too_early_4b_count": too_early_4b,
        "price_only_4b_count": price_only_4b,
        "4c_late_count": late_4c,
        "hard_4c_count": hard_4c,
        "confidence": candidate.get("confidence"),
        "reason": candidate.get("reason"),
    }


def _scope_label(decision: dict[str, Any]) -> str:
    if decision.get("canonical_archetype_id"):
        return f"canonical_archetype:{decision['canonical_archetype_id']}"
    if decision.get("large_sector_id"):
        return f"large_sector:{decision['large_sector_id']}"
    return str(decision.get("scope") or "global_v12")


def _sanitize_id(value: Any) -> str:
    text = str(value or "unknown")
    text = re.sub(r"[^0-9a-zA-Z가-힣_]+", "_", text)
    return re.sub(r"_+", "_", text).strip("_")[:96] or "unknown"


def _patch_type(axis: str) -> str:
    mapping = {
        "stage2_bonus_candidate_delta": "Stage2 bridge",
        "stage2_required_bridge": "Stage2 evidence guard",
        "full_4b_overlay_candidate": "4B non-price overlay",
        "local_4b_watch_guard": "4B price-only watch guard",
        "earlier_thesis_break_watch": "4C thesis-break watch",
        "hard_4c_confirmation": "4C hard-break confirmation",
    }
    return mapping.get(axis, "E2R 2.2 bounded patch")


def _patch_new_value(axis: str, candidate: dict[str, Any]) -> Any:
    if axis == "stage2_bonus_candidate_delta":
        return min(1.0, _safe_float(candidate.get("shadow_candidate_value") or 1.0))
    if axis == "stage2_required_bridge":
        return "require_non_price_bridge"
    if axis == "full_4b_overlay_candidate":
        return "full_4b_requires_verified_non_price_evidence"
    if axis == "local_4b_watch_guard":
        return "price_only_4b_watch_only_not_full_4b"
    if axis == "earlier_thesis_break_watch":
        return "earlier_4c_watch_before_hard_4c"
    if axis == "hard_4c_confirmation":
        return "hard_4c_requires_non_price_thesis_break"
    return candidate.get("shadow_candidate_value")


def _rollback_condition(axis: str) -> str:
    if axis == "stage2_bonus_candidate_delta":
        return "rollback_if_false_positive_stage2_rate_worsens_or_high_mae_counterexamples_dominate"
    if "4b" in axis.lower():
        return "rollback_if_4b_watch_triggers_too_early_on_verified_non_price_cases"
    if "4c" in axis.lower():
        return "rollback_if_4c_watch_blocks_intact_stage3_evidence_without_thesis_break"
    return "rollback_if_next_v12_batch_reverses_positive_counterexample_balance"


def _patch_spec(
    decision: dict[str, Any],
    evidence_state: dict[str, dict[str, Any]],
    patch_support_state: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    axis = str(decision.get("axis") or "unknown_axis")
    scope_value = decision.get("canonical_archetype_id") or decision.get("large_sector_id") or decision.get("scope")
    state = patch_support_state.get(_scope_label(decision)) or evidence_state.get(str(decision.get("canonical_archetype_id") or ""), {})
    support_ids = state.get("latest_positive_case_ids", [])[:8]
    guard_ids = state.get("latest_counterexample_case_ids", [])[:8]
    if _is_defensive_axis(axis):
        support_ids = support_ids or guard_ids or state.get("latest_support_case_ids", [])[:8]
        guard_ids = guard_ids or state.get("latest_support_case_ids", [])[:8] or support_ids
    patch_id = f"e2r_2_2_{_sanitize_id(scope_value)}_{_sanitize_id(axis)}_v1"
    return {
        "patch_id": patch_id,
        "patch_type": _patch_type(axis),
        "scope": _scope_label(decision),
        "axis": axis,
        "old_value": 0.0 if axis == "stage2_bonus_candidate_delta" else "not_configured",
        "new_value": _patch_new_value(axis, decision),
        "max_delta": 1.0 if axis == "stage2_bonus_candidate_delta" else "guardrail_only",
        "evidence_support_ids": support_ids,
        "counterexample_guard_ids": guard_ids,
        "rollback_condition": _rollback_condition(axis),
        "production_default_scoring_changed": False,
        "requires_explicit_future_patch_task": True,
    }


def build_v12_promotion_plan(
    representative_rows: list[dict[str, Any]],
    aggregate_metrics: list[dict[str, Any]],
    stage_transition_rows: list[dict[str, Any]],
    shadow_candidates: list[dict[str, Any]],
    rejected_rows: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Convert shadow candidates into rolling apply/hold/block decisions."""

    evidence_state = build_archetype_evidence_state(representative_rows)
    decisions: list[dict[str, Any]] = []
    for candidate in shadow_candidates:
        transition_count = _transition_count_for_scope(
            stage_transition_rows,
            scope=str(candidate.get("scope") or ""),
            large_sector_id=candidate.get("large_sector_id"),
            canonical_archetype_id=candidate.get("canonical_archetype_id"),
        )
        decisions.append(_decision_for_candidate(candidate, transition_count))

    patch_support_state = _build_patch_support_state(representative_rows)
    patch_specs = [
        _patch_spec(decision, evidence_state, patch_support_state)
        for decision in decisions
        if decision["decision"] == "apply_next_patch"
    ]
    decision_counts = dict(Counter(decision["decision"] for decision in decisions))
    promotion_type_counts = dict(Counter(decision["promotion_type"] for decision in decisions))

    for archetype, state in evidence_state.items():
        matching = [decision for decision in decisions if decision.get("canonical_archetype_id") == archetype]
        if any(decision["decision"] == "apply_next_patch" for decision in matching):
            state["next_delta_recommendation"] = "apply_limited_next_patch"
        elif any(decision["decision"].startswith("blocked") for decision in matching):
            state["next_delta_recommendation"] = "clear_named_blockers_before_patch"
        elif matching:
            state["next_delta_recommendation"] = "hold_for_more_non_overlapping_evidence"

    return {
        "schema_version": "v12_rolling_promotion_plan_v1",
        "production_default_scoring_changed": False,
        "active_default_profile_must_remain": "e2r_2_1_stock_web_calibrated",
        "archetype_evidence_state": evidence_state,
        "promotion_decisions": decisions,
        "patch_specs": patch_specs,
        "decision_counts": decision_counts,
        "promotion_type_counts": promotion_type_counts,
        "rejected_rows_count": len(rejected_rows or []),
        "default_promotion_ready": False,
        "next_patch_ready": bool(patch_specs),
    }


def write_v12_promotion_plan_outputs(plan: dict[str, Any], data_directory: str | Path, report_directory: str | Path) -> dict[str, Path]:
    data_dir = Path(data_directory)
    report_dir = Path(report_directory)
    paths = {
        "v12_archetype_evidence_state": _write_json(
            data_dir / "v12_archetype_evidence_state.json", plan["archetype_evidence_state"]
        ),
        "v12_promotion_decisions": _write_jsonl(data_dir / "v12_promotion_decisions.jsonl", plan["promotion_decisions"]),
        "v12_patch_specs": _write_jsonl(data_dir / "v12_patch_specs.jsonl", plan["patch_specs"]),
        "rolling_calibration_state": report_dir / "rolling_calibration_state.md",
        "apply_next_patch_plan": report_dir / "apply_next_patch_plan.md",
        "blocked_axes_report": report_dir / "blocked_axes_report.md",
    }
    report_dir.mkdir(parents=True, exist_ok=True)
    paths["rolling_calibration_state"].write_text(render_rolling_calibration_state(plan), encoding="utf-8")
    paths["apply_next_patch_plan"].write_text(render_apply_next_patch_plan(plan), encoding="utf-8")
    paths["blocked_axes_report"].write_text(render_blocked_axes_report(plan), encoding="utf-8")
    return paths


def render_rolling_calibration_state(plan: dict[str, Any]) -> str:
    state = plan.get("archetype_evidence_state", {})
    lines = [
        "# V12 Rolling Calibration State",
        "",
        "이 파일은 연구 자료를 바로 기본 scoring에 넣는 파일이 아닙니다.",
        "각 archetype에 성공/반례/4B/4C 증거가 얼마나 쌓였는지와 다음 작은 패치 후보를 추적합니다.",
        "",
        f"- archetype_count: `{len(state)}`",
        f"- decision_counts: `{plan.get('decision_counts')}`",
        f"- patch_spec_count: `{len(plan.get('patch_specs', []))}`",
        "- production_default_scoring_changed: `false`",
        "",
        "| archetype | large_sector | positive_symbols | counterexample_symbols | 4B_cases | 4C_cases | next_delta_recommendation |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for archetype, row in sorted(state.items()):
        lines.append(
            "| {arch} | {sector} | {pos} | {counter} | {fourb} | {fourc} | {rec} |".format(
                arch=archetype,
                sector=row.get("large_sector_id"),
                pos=len(row.get("unique_positive_symbols", [])),
                counter=len(row.get("unique_counterexample_symbols", [])),
                fourb=len(row.get("unique_4b_cases", [])),
                fourc=len(row.get("unique_4c_cases", [])),
                rec=row.get("next_delta_recommendation"),
            )
        )
    return "\n".join(lines) + "\n"

def render_apply_next_patch_plan(plan: dict[str, Any]) -> str:
    patches = plan.get("patch_specs", [])
    lines = [
        "# V12 Apply-Next-Patch Plan",
        "",
        "이 보고서는 다음 명시적 E2R 2.2 패치 작업의 입력입니다. 현재 실행에서는 active profile을 바꾸지 않습니다.",
        "",
        f"- apply_next_patch_count: `{len(patches)}`",
        "- active_default_profile_preserved: `true`",
        "- production_default_scoring_changed: `false`",
        "",
        "| patch_id | patch_type | scope | axis | new_value | rollback_condition |",
        "|---|---|---|---|---|---|",
    ]
    for patch in patches:
        lines.append(
            "| {patch_id} | {patch_type} | {scope} | {axis} | {new_value} | {rollback} |".format(
                patch_id=patch.get("patch_id"),
                patch_type=patch.get("patch_type"),
                scope=patch.get("scope"),
                axis=patch.get("axis"),
                new_value=patch.get("new_value"),
                rollback=patch.get("rollback_condition"),
            )
        )
    if not patches:
        lines.extend(["", "## No Apply-Next-Patch Axes", "현재 batch에서는 즉시 다음 패치로 넘길 축이 없습니다. `blocked_axes_report.md`의 차단 사유를 먼저 해소해야 합니다."])
    return "\n".join(lines) + "\n"


def render_blocked_axes_report(plan: dict[str, Any]) -> str:
    blocked = [row for row in plan.get("promotion_decisions", []) if row.get("decision") != "apply_next_patch"]
    lines = [
        "# V12 Blocked / Held Axes Report",
        "",
        "| axis | scope | decision | promotion_type | missing_to_promote | recommended_next_action |",
        "|---|---|---|---|---|---|",
    ]
    for row in blocked:
        lines.append(
            "| {axis} | {scope} | {decision} | {ptype} | {missing} | {action} |".format(
                axis=row.get("axis"),
                scope=_scope_label(row),
                decision=row.get("decision"),
                ptype=row.get("promotion_type"),
                missing=", ".join(row.get("missing_to_promote", [])),
                action=row.get("recommended_next_action"),
            )
        )
    return "\n".join(lines) + "\n"
