"""Promotion of deduped historical calibration into default scoring profile."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
import json

from .aggregate import aggregate_validated_rows
from .scoring_profile import ACTIVE_PROFILE_PATH, BASELINE_PROFILE_PATH, CALIBRATED_PROFILE_PATH
from .validation import FOUR_B_TYPES, FOUR_C_TYPES, POSITIVE_TRIGGER_TYPES


@dataclass(frozen=True)
class PromotionResult:
    promotion_status: str
    production_default_scoring_changed: bool
    applied_axes: list[dict[str, Any]]
    shadow_only_axes: list[dict[str, Any]]
    rejected_axes: list[dict[str, Any]]
    baseline_profile_path: Path
    calibrated_profile_path: Path
    active_profile_path: Path


BASELINE_THRESHOLDS = {
    "stage2_total_min": 65.0,
    "stage2_eps_fcf_min": 10.0,
    "stage2_valuation_min": 7.0,
    "stage2_information_confidence_min": 3.0,
    "stage3_yellow_total_min": 80.0,
    "stage3_green_total_min": 85.0,
    "stage3_green_eps_fcf_min": 17.0,
    "stage3_green_visibility_min": 15.0,
    "stage3_green_bottleneck_min": 15.0,
    "stage3_green_mispricing_min": 10.0,
    "stage3_green_valuation_min": 10.0,
    "stage3_green_revision_min": 50.0,
    "stage3_green_structural_visibility_min": 45.0,
}

CALIBRATED_THRESHOLDS = {
    **BASELINE_THRESHOLDS,
    "stage3_yellow_total_min": 75.0,
    "stage3_green_total_min": 87.0,
    "stage3_green_revision_min": 55.0,
}

CALIBRATED_ADJUSTMENTS = {
    "stage2_actionable_evidence_bonus": 2.0,
    "stage3_cross_evidence_green_buffer": 1.5,
    "stage2_actionable_volatility_guard_penalty": 2.0,
    "high_mae_risk_guard_penalty": 2.0,
}

CALIBRATED_GUARDRAILS = {
    "price_only_blowoff_blocks_positive_stage": True,
    "full_4b_requires_non_price_evidence": True,
    "hard_4c_thesis_break_routes_to_4c": True,
}


def _write_yaml(path: Path, payload: dict[str, Any]) -> Path:
    lines: list[str] = []
    for key, value in payload.items():
        if isinstance(value, dict):
            lines.append(f"{key}:")
            for child_key, child_value in value.items():
                if isinstance(child_value, bool):
                    child_text = "true" if child_value else "false"
                else:
                    child_text = str(child_value)
                lines.append(f"  {child_key}: {child_text}")
        else:
            lines.append(f"{key}: {value}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _unique(rows: list[dict[str, Any]], key: str) -> set[Any]:
    return {row.get(key) for row in rows if row.get(key)}


def _axis(
    axis: str,
    scope: str,
    old_value: Any,
    new_value: Any,
    confidence: str,
    rows: list[dict[str, Any]],
    reason: str,
) -> dict[str, Any]:
    try:
        delta = float(new_value) - float(old_value)
    except (TypeError, ValueError):
        delta = "changed"
    return {
        "axis": axis,
        "scope": scope,
        "old_value": old_value,
        "new_value": new_value,
        "delta": delta,
        "confidence": confidence,
        "unique_case_count": len(_unique(rows, "case_id")),
        "unique_round_count": len(_unique(rows, "round")),
        "supporting_trigger_count": len(rows),
        "reason": reason,
    }


def _promotable_positive_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        row
        for row in rows
        if row.get("trigger_type") in POSITIVE_TRIGGER_TYPES and row.get("usable_for_weight_calibration") is True
    ]


def promote_calibrated_profile(
    representative_rows: list[dict[str, Any]],
    *,
    coverage_passed: bool,
    output_directory: str | Path = "data/e2r/calibration",
    write_runtime_profiles: bool = True,
) -> PromotionResult:
    output_path = Path(output_directory)
    output_path.mkdir(parents=True, exist_ok=True)
    applied_axes: list[dict[str, Any]] = []
    shadow_only_axes: list[dict[str, Any]] = []
    rejected_axes: list[dict[str, Any]] = []

    if not coverage_passed:
        rejected_axes.append(
            {
                "axis": "all",
                "scope": "global",
                "reason": "blocked_by_coverage_failure",
                "needed_for_promotion": "discovered_result_md_count >= 100 and rounds R1-R13 covered",
            }
        )
        if write_runtime_profiles:
            _write_baseline_only_profiles()
        return PromotionResult(
            promotion_status="blocked_by_coverage_failure",
            production_default_scoring_changed=False,
            applied_axes=[],
            shadow_only_axes=shadow_only_axes,
            rejected_axes=rejected_axes,
            baseline_profile_path=BASELINE_PROFILE_PATH,
            calibrated_profile_path=CALIBRATED_PROFILE_PATH,
            active_profile_path=ACTIVE_PROFILE_PATH,
        )

    positives = _promotable_positive_rows(representative_rows)
    stage2_rows = [row for row in positives if row.get("trigger_type") in {"Stage2", "Stage2-Actionable"}]
    stage3_yellow_rows = [row for row in positives if row.get("trigger_type") == "Stage3-Yellow"]
    stage3_green_rows = [row for row in positives if row.get("trigger_type") == "Stage3-Green"]
    four_b_rows = [row for row in representative_rows if row.get("trigger_type") in FOUR_B_TYPES]
    four_c_rows = [row for row in representative_rows if row.get("trigger_type") in FOUR_C_TYPES]
    price_only_4b = [row for row in four_b_rows if row.get("guardrail_class") == "price_only_4b_rejection"]

    if len(_unique(stage2_rows, "case_id")) >= 4 and len(_unique(stage2_rows, "round")) >= 2:
        applied_axes.append(
            _axis(
                "stage2_actionable_evidence_bonus",
                "global",
                0,
                CALIBRATED_ADJUSTMENTS["stage2_actionable_evidence_bonus"],
                "medium",
                stage2_rows,
                "Deduped Stage2/Stage2-Actionable rows repeatedly captured early non-price evidence before Green confirmation.",
            )
        )
    else:
        shadow_only_axes.append(
            {
                "axis": "stage2_actionable_evidence_bonus",
                "scope": "global",
                "reason": "unique_case_or_round_count_below_promotion_threshold",
                "needed_for_promotion": ">=4 unique cases and >=2 unique rounds",
            }
        )

    if len(_unique(stage3_yellow_rows, "case_id")) >= 4 and len(_unique(stage3_yellow_rows, "round")) >= 2:
        applied_axes.append(
            _axis(
                "stage3_yellow_total_min",
                "global",
                BASELINE_THRESHOLDS["stage3_yellow_total_min"],
                CALIBRATED_THRESHOLDS["stage3_yellow_total_min"],
                "medium",
                stage3_yellow_rows,
                "Stage3-Yellow is validated as an intermediate state when evidence is strong but Green gates remain open.",
            )
        )
    else:
        shadow_only_axes.append(
            {
                "axis": "stage3_yellow_total_min",
                "scope": "global",
                "reason": "Stage3-Yellow rows remain below full global threshold",
                "needed_for_promotion": ">=4 unique cases and >=2 unique rounds",
            }
        )

    if len(_unique(stage3_green_rows, "case_id")) >= 4:
        applied_axes.append(
            _axis(
                "stage3_green_total_min",
                "global",
                BASELINE_THRESHOLDS["stage3_green_total_min"],
                CALIBRATED_THRESHOLDS["stage3_green_total_min"],
                "high",
                stage3_green_rows,
                "Late/false Green evidence supports stricter Green confirmation rather than broad relaxation.",
            )
        )
        applied_axes.append(
            _axis(
                "stage3_green_revision_min",
                "global",
                BASELINE_THRESHOLDS["stage3_green_revision_min"],
                CALIBRATED_THRESHOLDS["stage3_green_revision_min"],
                "high",
                stage3_green_rows,
                "Green should require stronger EPS/OP/FCF revision confirmation after cumulative calibration.",
            )
        )
        applied_axes.append(
            _axis(
                "stage3_cross_evidence_green_buffer",
                "global",
                0,
                CALIBRATED_ADJUSTMENTS["stage3_cross_evidence_green_buffer"],
                "medium",
                stage3_green_rows,
                "Strong multi-family evidence may bridge small total-score rounding gaps while stricter Green gates remain active.",
            )
        )

    if len(price_only_4b) >= 3 or len(four_b_rows) >= 4:
        applied_axes.append(
            _axis(
                "full_4b_requires_non_price_evidence",
                "4B_guardrail",
                False,
                True,
                "high",
                four_b_rows,
                "Price-only local peaks repeatedly failed as full 4B; full 4B now requires non-price evidence.",
            )
        )

    if len(four_c_rows) >= 3:
        applied_axes.append(
            _axis(
                "hard_4c_thesis_break_routes_to_4c",
                "4C_guardrail",
                False,
                True,
                "high",
                four_c_rows,
                "4C rows are thesis-break/protection logic and must never train positive entry weights.",
            )
        )

    if not applied_axes:
        rejected_axes.append(
            {
                "axis": "all",
                "scope": "global",
                "reason": "no_axis_met_promotion_threshold",
                "needed_for_promotion": "validated deduped non-price evidence with enough unique cases/rounds",
            }
        )
        if write_runtime_profiles:
            _write_baseline_only_profiles()
        status = "no_axis_met_promotion_threshold"
        changed = False
    else:
        if write_runtime_profiles:
            _write_promoted_profiles()
        status = "applied"
        changed = True

    (output_path / "applied_weight_changes.json").write_text(
        json.dumps(applied_axes, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )
    (output_path / "rejected_promotion_candidates.json").write_text(
        json.dumps(rejected_axes + shadow_only_axes, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    (output_path / "calibrated_weight_aggregate.json").write_text(
        json.dumps(
            {
                "promotion_status": status,
                "production_default_scoring_changed": changed,
                "aggregates": aggregate_validated_rows(representative_rows),
            },
            ensure_ascii=False,
            indent=2,
            allow_nan=False,
        )
        + "\n",
        encoding="utf-8",
    )
    (output_path / "shadow_weight_aggregate.json").write_text(
        json.dumps({"shadow_only_axes": shadow_only_axes}, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )

    return PromotionResult(
        promotion_status=status,
        production_default_scoring_changed=changed,
        applied_axes=applied_axes,
        shadow_only_axes=shadow_only_axes,
        rejected_axes=rejected_axes,
        baseline_profile_path=BASELINE_PROFILE_PATH,
        calibrated_profile_path=CALIBRATED_PROFILE_PATH,
        active_profile_path=ACTIVE_PROFILE_PATH,
    )


def _write_baseline_only_profiles() -> None:
    _write_yaml(
        BASELINE_PROFILE_PATH,
        {
            "profile_id": "e2r_2_0_baseline",
            "profile_status": "rollback_available",
            "profile_basis": "pre_stock_web_calibration_default",
            "thresholds": BASELINE_THRESHOLDS,
            "adjustments": {},
            "guardrails": {},
        },
    )
    _write_yaml(
        CALIBRATED_PROFILE_PATH,
        {
            "profile_id": "e2r_2_1_stock_web_calibrated",
            "profile_status": "not_promoted",
            "previous_default_profile": "e2r_2_0_baseline",
            "profile_basis": "deduped_stock_web_historical_calibration_md",
            "thresholds": BASELINE_THRESHOLDS,
            "adjustments": {},
            "guardrails": {},
        },
    )
    _write_yaml(ACTIVE_PROFILE_PATH, {"active_profile": "baseline", "rollback_profile": "baseline"})


def _write_promoted_profiles() -> None:
    _write_yaml(
        BASELINE_PROFILE_PATH,
        {
            "profile_id": "e2r_2_0_baseline",
            "profile_status": "rollback_available",
            "profile_basis": "pre_stock_web_calibration_default",
            "thresholds": BASELINE_THRESHOLDS,
            "adjustments": {},
            "guardrails": {},
        },
    )
    _write_yaml(
        CALIBRATED_PROFILE_PATH,
        {
            "profile_id": "e2r_2_1_stock_web_calibrated",
            "profile_status": "default_enabled",
            "previous_default_profile": "e2r_2_0_baseline",
            "profile_basis": "deduped_stock_web_historical_calibration_md",
            "thresholds": CALIBRATED_THRESHOLDS,
            "adjustments": CALIBRATED_ADJUSTMENTS,
            "guardrails": CALIBRATED_GUARDRAILS,
        },
    )
    _write_yaml(ACTIVE_PROFILE_PATH, {"active_profile": "calibrated", "rollback_profile": "baseline"})
