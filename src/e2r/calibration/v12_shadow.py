"""Build v12 sector/archetype shadow calibration profiles."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any
import json

from .v12_promotion_planner import build_v12_promotion_plan, write_v12_promotion_plan_outputs


def _json_default(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    return value


def _write_json(path: Path, payload: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, default=_json_default, allow_nan=False) + "\n", encoding="utf-8")
    return path


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True, default=_json_default, allow_nan=False) + "\n")
    return path


def _group_metrics(aggregates: list[dict[str, Any]], group_name: str) -> list[dict[str, Any]]:
    return [row for row in aggregates if row.get("group_name") == group_name]


def _confidence(metric: dict[str, Any]) -> str:
    unique_symbols = int(metric.get("unique_symbol_count") or 0)
    positives = int(metric.get("positive_case_count") or 0)
    counters = int(metric.get("counterexample_count") or 0)
    if unique_symbols >= 6 and positives >= 3 and counters >= 2:
        return "medium"
    if unique_symbols >= 3 and positives >= 2 and counters >= 1:
        return "low_medium"
    return "low"


def _promotion_ready(metric: dict[str, Any]) -> bool:
    return (
        int(metric.get("evidence_url_pending_count") or 0) == 0
        and int(metric.get("source_proxy_only_count") or 0) == 0
        and int(metric.get("positive_case_count") or 0) >= 2
        and int(metric.get("counterexample_count") or 0) >= 2
    )


def _stage2_candidate(metric: dict[str, Any], scope: str) -> dict[str, Any] | None:
    good = int(metric.get("good_stage2_count") or 0)
    bad = int(metric.get("bad_stage2_count") or 0)
    high_mae = int(metric.get("stage2_high_mae_count") or 0)
    if good <= 0 and bad <= 0 and high_mae <= 0:
        return None
    if good > bad and high_mae == 0:
        axis = "stage2_bonus_candidate_delta"
        direction = "strengthen_conditional_stage2_actionable"
        reason = "Stage2/Stage2-Actionable rows show positive asymmetry with limited high-MAE evidence."
        value = 1.0
    else:
        axis = "stage2_required_bridge"
        direction = "tighten_stage2_bridge_or_high_mae_guard"
        reason = "Stage2 rows include weak or high-MAE outcomes, so the shadow profile should require a stronger evidence bridge."
        value = "require_non_price_bridge"
    return _candidate(metric, scope, axis, direction, value, reason)


def _four_b_candidate(metric: dict[str, Any], scope: str) -> dict[str, Any] | None:
    good = int(metric.get("good_4b_timing_count") or 0)
    too_early = int(metric.get("too_early_4b_count") or 0)
    price_only = int(metric.get("price_only_4b_count") or 0)
    if good <= 0 and too_early <= 0 and price_only <= 0:
        return None
    if good > too_early + price_only:
        return _candidate(
            metric,
            scope,
            "full_4b_overlay_candidate",
            "strengthen_non_price_4b_overlay",
            "non_price_4b_required",
            "Non-price 4B rows show useful peak-capture timing in this scope.",
        )
    return _candidate(
        metric,
        scope,
        "local_4b_watch_guard",
        "keep_price_only_4b_as_watch_only",
        "price_only_local_watch",
        "Price-only or early 4B rows dominate, so full 4B must not be strengthened.",
    )


def _four_c_candidate(metric: dict[str, Any], scope: str) -> dict[str, Any] | None:
    late = int(metric.get("4c_late_count") or 0)
    hard = int(metric.get("hard_4c_count") or 0)
    if late <= 0 and hard <= 0:
        return None
    if late > 0:
        return _candidate(
            metric,
            scope,
            "earlier_thesis_break_watch",
            "tighten_4c_watch_before_hard_4c",
            "watch_before_hard_4c",
            "Some 4C rows were late; propose earlier watch logic, not automatic hard 4C.",
        )
    return _candidate(
        metric,
        scope,
        "hard_4c_confirmation",
        "retain_hard_4c_when_non_price_break_exists",
        "hard_4c_non_price_evidence",
        "Hard 4C rows are supported by thesis-break evidence in this scope.",
    )


def _candidate(metric: dict[str, Any], scope: str, axis: str, direction: str, value: Any, reason: str) -> dict[str, Any]:
    return {
        "axis": axis,
        "scope": scope,
        "large_sector_id": metric.get("group_value") if metric.get("group_name") == "large_sector_id" else None,
        "canonical_archetype_id": metric.get("group_value") if metric.get("group_name") == "canonical_archetype_id" else None,
        "old_global_value": None,
        "shadow_candidate_value": value,
        "direction": direction,
        "confidence": _confidence(metric),
        "row_count": metric.get("row_count", metric.get("count", 0)),
        "unique_case_count": metric.get("unique_case_count", 0),
        "unique_symbol_count": metric.get("unique_symbol_count", 0),
        "positive_case_count": metric.get("positive_case_count", 0),
        "counterexample_count": metric.get("counterexample_count", 0),
        "good_stage2_count": metric.get("good_stage2_count", 0),
        "bad_stage2_count": metric.get("bad_stage2_count", 0),
        "stage2_high_mae_count": metric.get("stage2_high_mae_count", 0),
        "good_4b_timing_count": metric.get("good_4b_timing_count", 0),
        "too_early_4b_count": metric.get("too_early_4b_count", 0),
        "price_only_4b_count": metric.get("price_only_4b_count", 0),
        "4c_late_count": metric.get("4c_late_count", 0),
        "hard_4c_count": metric.get("hard_4c_count", 0),
        "source_proxy_only_count": metric.get("source_proxy_only_count", 0),
        "evidence_url_pending_count": metric.get("evidence_url_pending_count", 0),
        "promotion_ready": _promotion_ready(metric),
        "reason": reason,
        "supporting_trigger_ids": [],
    }


def build_v12_shadow_payloads(
    representative_rows: list[dict[str, Any]],
    aggregate_metrics: list[dict[str, Any]],
    stage_transition_rows: list[dict[str, Any]],
    rejected_rows: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    sector_candidates: list[dict[str, Any]] = []
    archetype_candidates: list[dict[str, Any]] = []
    for metric in _group_metrics(aggregate_metrics, "large_sector_id"):
        for builder in (_stage2_candidate, _four_b_candidate, _four_c_candidate):
            candidate = builder(metric, "large_sector")
            if candidate:
                sector_candidates.append(candidate)
    for metric in _group_metrics(aggregate_metrics, "canonical_archetype_id"):
        for builder in (_stage2_candidate, _four_b_candidate, _four_c_candidate):
            candidate = builder(metric, "canonical_archetype")
            if candidate:
                archetype_candidates.append(candidate)

    residual_ledger = [
        {
            "trigger_id": row.get("trigger_id"),
            "case_id": row.get("case_id"),
            "symbol": row.get("symbol"),
            "large_sector_id": row.get("large_sector_id"),
            "canonical_archetype_id": row.get("canonical_archetype_id"),
            "current_profile_verdict": row.get("current_profile_verdict"),
            "trigger_outcome_label": row.get("trigger_outcome_label"),
            "current_profile_error": row.get("current_profile_error"),
            "source_proxy_only": row.get("source_proxy_only"),
            "evidence_url_pending": row.get("evidence_url_pending"),
        }
        for row in representative_rows
        if row.get("current_profile_error") or row.get("source_proxy_only") or row.get("evidence_url_pending")
    ]
    sector_profile = {
        "profile_id": "v12_sector_shadow_profile",
        "profile_status": "shadow_only_not_active",
        "production_default_scoring_changed": False,
        "candidates": sector_candidates,
    }
    archetype_profile = {
        "profile_id": "v12_archetype_shadow_profile",
        "profile_status": "shadow_only_not_active",
        "production_default_scoring_changed": False,
        "candidates": archetype_candidates,
    }
    e2r_2_2_candidate = {
        "profile_id": "e2r_2_2_sector_archetype_candidate",
        "profile_status": "candidate_not_active",
        "previous_default_profile": "e2r_2_1_stock_web_calibrated",
        "production_default_scoring_changed": False,
        "active_default_profile_must_remain": "e2r_2_1_stock_web_calibrated",
        "sector_shadow_candidate_count": len(sector_candidates),
        "archetype_shadow_candidate_count": len(archetype_candidates),
        "stage_transition_summary_rows": len(stage_transition_rows),
        "promotion_ready": all(candidate["promotion_ready"] for candidate in sector_candidates + archetype_candidates)
        and bool(sector_candidates or archetype_candidates),
        "promotion_blockers": _promotion_blockers(representative_rows, rejected_rows or []),
    }
    return {
        "sector_shadow_profile": sector_profile,
        "archetype_shadow_profile": archetype_profile,
        "residual_error_ledger": residual_ledger,
        "v12_shadow_weight_candidates": sector_candidates + archetype_candidates,
        "e2r_2_2_candidate_profile": e2r_2_2_candidate,
    }


def _promotion_blockers(rows: list[dict[str, Any]], rejected_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    blockers = []
    evidence_pending = sum(1 for row in rows if row.get("evidence_url_pending"))
    source_proxy = sum(1 for row in rows if row.get("source_proxy_only"))
    rejected = len(rejected_rows)
    if evidence_pending:
        blockers.append(
            {
                "blocker": "evidence_url_pending",
                "count": evidence_pending,
                "reason": "v12 rows can support shadow analysis but need exact public evidence URLs before default promotion.",
                "needed_to_clear": "Attach verified DART/IR/report/news URLs or mark rows as evidence-verified.",
            }
        )
    if source_proxy:
        blockers.append(
            {
                "blocker": "source_proxy_only",
                "count": source_proxy,
                "reason": "Some evidence is source-name-level historical event proxy, not verified production evidence.",
                "needed_to_clear": "Replace proxy rows with verified as-of evidence records.",
            }
        )
    if rejected:
        blockers.append(
            {
                "blocker": "rejected_rows",
                "count": rejected,
                "reason": "Some rows failed validation or were not usable for shadow calibration.",
                "needed_to_clear": "Fix missing sector/archetype IDs, price fields, or evidence flags.",
            }
        )
    if not blockers:
        blockers.append(
            {
                "blocker": "case_balance_review",
                "count": 0,
                "reason": "Even with clean rows, v12 requires explicit human approval before default promotion.",
                "needed_to_clear": "Run separate promotion task with readiness report all clear.",
            }
        )
    return blockers


def write_v12_shadow_outputs(
    representative_rows: list[dict[str, Any]],
    aggregate_metrics: list[dict[str, Any]],
    stage_transition_rows: list[dict[str, Any]],
    *,
    rejected_rows: list[dict[str, Any]] | None = None,
    data_directory: str | Path,
    report_directory: str | Path,
) -> dict[str, Path]:
    data_dir = Path(data_directory)
    report_dir = Path(report_directory)
    data_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)
    payloads = build_v12_shadow_payloads(representative_rows, aggregate_metrics, stage_transition_rows, rejected_rows)
    paths = {
        "sector_shadow_profile": _write_json(data_dir / "sector_shadow_profile.json", payloads["sector_shadow_profile"]),
        "archetype_shadow_profile": _write_json(data_dir / "archetype_shadow_profile.json", payloads["archetype_shadow_profile"]),
        "residual_error_ledger": _write_jsonl(data_dir / "residual_error_ledger.jsonl", payloads["residual_error_ledger"]),
        "v12_shadow_weight_candidates": _write_jsonl(
            data_dir / "v12_shadow_weight_candidates.jsonl", payloads["v12_shadow_weight_candidates"]
        ),
        "e2r_2_2_candidate_profile": _write_json(
            data_dir / "e2r_2_2_candidate_profile.json", payloads["e2r_2_2_candidate_profile"]
        ),
    }
    promotion_plan = build_v12_promotion_plan(
        representative_rows,
        aggregate_metrics,
        stage_transition_rows,
        payloads["v12_shadow_weight_candidates"],
        rejected_rows or [],
    )
    payloads["v12_promotion_plan"] = promotion_plan
    payloads["e2r_2_2_candidate_profile"].update(
        {
            "promotion_decision_counts": promotion_plan["decision_counts"],
            "promotion_type_counts": promotion_plan["promotion_type_counts"],
            "apply_next_patch_count": len(promotion_plan["patch_specs"]),
            "next_patch_ready": promotion_plan["next_patch_ready"],
        }
    )
    # Re-write after the decision counts are attached to the candidate profile.
    paths["e2r_2_2_candidate_profile"] = _write_json(
        data_dir / "e2r_2_2_candidate_profile.json", payloads["e2r_2_2_candidate_profile"]
    )
    paths.update(write_v12_promotion_plan_outputs(promotion_plan, data_dir, report_dir))
    paths.update(write_v12_shadow_reports(payloads, report_dir))
    return paths


def write_v12_shadow_reports(payloads: dict[str, Any], report_dir: Path) -> dict[str, Path]:
    reports = {
        "sector_shadow_profile_report": report_dir / "sector_shadow_profile_report.md",
        "archetype_shadow_profile_report": report_dir / "archetype_shadow_profile_report.md",
        "residual_error_report": report_dir / "residual_error_report.md",
        "promotion_readiness_report": report_dir / "promotion_readiness_report.md",
        "e2r_2_2_candidate_profile_report": report_dir / "e2r_2_2_candidate_profile_report.md",
        "evidence_url_pending_report": report_dir / "evidence_url_pending_report.md",
    }
    reports["sector_shadow_profile_report"].write_text(
        _render_candidate_report("V12 Sector Shadow Profile", payloads["sector_shadow_profile"]["candidates"]),
        encoding="utf-8",
    )
    reports["archetype_shadow_profile_report"].write_text(
        _render_candidate_report("V12 Archetype Shadow Profile", payloads["archetype_shadow_profile"]["candidates"]),
        encoding="utf-8",
    )
    reports["residual_error_report"].write_text(_render_residual_error_report(payloads["residual_error_ledger"]), encoding="utf-8")
    reports["promotion_readiness_report"].write_text(
        _render_promotion_readiness(payloads["e2r_2_2_candidate_profile"], payloads.get("v12_promotion_plan")),
        encoding="utf-8",
    )
    reports["e2r_2_2_candidate_profile_report"].write_text(
        _render_e2r_2_2_report(payloads["e2r_2_2_candidate_profile"]), encoding="utf-8"
    )
    pending = [row for row in payloads["residual_error_ledger"] if row.get("evidence_url_pending")]
    reports["evidence_url_pending_report"].write_text(_render_residual_error_report(pending, "Evidence URL Pending Report"), encoding="utf-8")
    return reports


def _render_candidate_report(title: str, candidates: list[dict[str, Any]]) -> str:
    lines = [
        f"# {title}",
        "",
        "이 보고서는 v12 shadow-only 후보입니다. 기본 scoring profile을 바꾸지 않습니다.",
        "",
        "| scope | sector | archetype | axis | direction | confidence | positive | counterexample | ready | reason |",
        "|---|---|---|---|---|---|---:|---:|---|---|",
    ]
    for candidate in candidates:
        lines.append(
            "| {scope} | {sector} | {arch} | {axis} | {direction} | {confidence} | {positive} | {counter} | {ready} | {reason} |".format(
                scope=candidate.get("scope"),
                sector=candidate.get("large_sector_id"),
                arch=candidate.get("canonical_archetype_id"),
                axis=candidate.get("axis"),
                direction=candidate.get("direction"),
                confidence=candidate.get("confidence"),
                positive=candidate.get("positive_case_count"),
                counter=candidate.get("counterexample_count"),
                ready=candidate.get("promotion_ready"),
                reason=candidate.get("reason"),
            )
        )
    return "\n".join(lines) + "\n"


def _render_residual_error_report(rows: list[dict[str, Any]], title: str = "V12 Residual Error Report") -> str:
    lines = [
        f"# {title}",
        "",
        f"- residual_rows: `{len(rows)}`",
        "",
        "| trigger_id | symbol | archetype | verdict | source_proxy_only | evidence_url_pending |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row.get('trigger_id')} | {row.get('symbol')} | {row.get('canonical_archetype_id')} | {row.get('current_profile_verdict')} | {row.get('source_proxy_only')} | {row.get('evidence_url_pending')} |"
        )
    return "\n".join(lines) + "\n"


def _render_promotion_readiness(profile: dict[str, Any], promotion_plan: dict[str, Any] | None = None) -> str:
    lines = [
        "# V12 Promotion Readiness Report",
        "",
        "- active_profile_preserved: `true`",
        "- production_default_scoring_changed: `false`",
        f"- default_promotion_ready: `{profile.get('promotion_ready')}`",
        f"- next_patch_ready: `{profile.get('next_patch_ready')}`",
        f"- apply_next_patch_count: `{profile.get('apply_next_patch_count')}`",
        f"- stage_transition_summary_rows: `{profile.get('stage_transition_summary_rows')}`",
        "",
        "## Promotion Decisions",
        "",
        "| axis | scope | decision | promotion_type | ready_for_next_patch | missing_to_promote | recommended_next_action |",
        "|---|---|---|---|---|---|---|",
    ]
    for decision in (promotion_plan or {}).get("promotion_decisions", []):
        scope = decision.get("canonical_archetype_id") or decision.get("large_sector_id") or decision.get("scope")
        lines.append(
            "| {axis} | {scope} | {decision} | {ptype} | {ready} | {missing} | {action} |".format(
                axis=decision.get("axis"),
                scope=scope,
                decision=decision.get("decision"),
                ptype=decision.get("promotion_type"),
                ready=decision.get("ready_for_next_patch"),
                missing=", ".join(decision.get("missing_to_promote", [])),
                action=decision.get("recommended_next_action"),
            )
        )
    lines.extend(
        [
            "",
            "## Blockers",
        ]
    )
    for blocker in profile.get("promotion_blockers", []):
        lines.append(
            f"- {blocker['blocker']}: {blocker['count']} / {blocker['reason']} / needed: {blocker['needed_to_clear']}"
        )
    return "\n".join(lines) + "\n"


def _render_e2r_2_2_report(profile: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# E2R 2.2 Candidate Profile Report",
            "",
            f"- profile_id: `{profile.get('profile_id')}`",
            f"- profile_status: `{profile.get('profile_status')}`",
            f"- previous_default_profile: `{profile.get('previous_default_profile')}`",
            f"- sector_shadow_candidate_count: `{profile.get('sector_shadow_candidate_count')}`",
            f"- archetype_shadow_candidate_count: `{profile.get('archetype_shadow_candidate_count')}`",
            f"- production_default_scoring_changed: `{profile.get('production_default_scoring_changed')}`",
            "- note: v12는 sector/archetype shadow 후보이며 별도 승인 없이는 active default가 아닙니다.",
        ]
    ) + "\n"
