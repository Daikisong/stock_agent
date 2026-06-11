"""Apply bounded v12 research patches into the runtime scoring profile.

The v12 ingest outputs remain the audit ledger. This module is the missing
execution step: it converts validated `apply_next_patch` specs into a small,
scoped E2R 2.2 rolling profile and can make that profile the active default.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
import json

from .scoring_profile import ACTIVE_PROFILE_PATH, CALIBRATED_PROFILE_PATH, V2_2_PROFILE_PATH, load_scoring_profile


SAFE_PATCH_AXES = {
    "stage2_bonus_candidate_delta",
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "full_4b_overlay_candidate",
    "earlier_thesis_break_watch",
    "hard_4c_confirmation",
}

AXIS_TO_GUARDRAIL_SCOPE_KEY = {
    "stage2_bonus_candidate_delta": "v12_stage2_bonus_scopes",
    "stage2_required_bridge": "v12_stage2_required_bridge_scopes",
    "local_4b_watch_guard": "v12_local_4b_watch_guard_scopes",
    "full_4b_overlay_candidate": "v12_full_4b_overlay_scopes",
    "earlier_thesis_break_watch": "v12_earlier_4c_watch_scopes",
    "hard_4c_confirmation": "v12_hard_4c_confirmation_scopes",
}


def _json_default(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    return value


def _read_jsonl(path: str | Path) -> list[dict[str, Any]]:
    path_obj = Path(path)
    if not path_obj.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path_obj.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _write_json(path: Path, payload: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, default=_json_default, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    return path


def _write_yaml(path: Path, payload: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    for key in ("profile_id", "profile_status", "previous_default_profile", "profile_basis"):
        if key in payload:
            lines.append(f"{key}: {payload[key]}")
    for section in ("thresholds", "adjustments", "guardrails"):
        lines.append(f"{section}:")
        for key, value in payload.get(section, {}).items():
            rendered = "true" if value is True else "false" if value is False else value
            lines.append(f"  {key}: {rendered}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _scope_key(scope: str) -> str:
    return scope.strip()


def _safe_patch_specs(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    specs: list[dict[str, Any]] = []
    for row in rows:
        axis = str(row.get("axis") or "")
        scope = str(row.get("scope") or "")
        if axis not in SAFE_PATCH_AXES or not scope:
            continue
        if axis == "stage2_bonus_candidate_delta":
            try:
                value = float(row.get("new_value", 0.0))
            except (TypeError, ValueError):
                continue
            if value <= 0.0 or value > 1.0:
                continue
        specs.append(row)
    return specs


def build_v12_rolling_profile_payload(
    *,
    patch_specs: list[dict[str, Any]],
    base_profile_path: str | Path = CALIBRATED_PROFILE_PATH,
) -> dict[str, Any]:
    """Build a scoped E2R 2.2 profile from safe v12 patch specs."""

    base = load_scoring_profile(base_profile_path)
    safe_specs = _safe_patch_specs(patch_specs)
    scopes_by_key: dict[str, set[str]] = defaultdict(set)
    axis_counts: Counter[str] = Counter()
    for spec in safe_specs:
        axis = str(spec.get("axis") or "")
        scope_key = AXIS_TO_GUARDRAIL_SCOPE_KEY.get(axis)
        if not scope_key:
            continue
        scopes_by_key[scope_key].add(_scope_key(str(spec["scope"])))
        axis_counts[axis] += 1

    guardrails: dict[str, bool | float | str] = dict(base.guardrails)
    guardrails.update(
        {
            "rolling_calibration_enabled": True,
            "rolling_calibration_source": "v12_apply_next_patch_specs",
            "archetype_weight_runtime_enabled": True,
            "archetype_weight_profile_path": "configs/e2r_archetype_weight_profile_v2_2.json",
            "archetype_classification_required": True,
            "archetype_large_sector_fallback_allowed": False,
            "stage3_green_not_loosened_by_v12": True,
            "case_library_not_candidate_input": True,
            "price_only_blowoff_blocks_positive_stage": True,
            "full_4b_requires_non_price_evidence": True,
            "hard_4c_thesis_break_routes_to_4c": True,
        }
    )
    for key, scopes in sorted(scopes_by_key.items()):
        guardrails[key] = "|".join(sorted(scopes))

    adjustments = dict(base.adjustments)
    adjustments["v12_stage2_archetype_bonus"] = 1.0 if scopes_by_key.get("v12_stage2_bonus_scopes") else 0.0

    return {
        "profile_id": "e2r_2_2_rolling_calibrated",
        "profile_status": "default_enabled",
        "previous_default_profile": base.profile_id,
        "profile_basis": "v12_validated_rolling_calibration_apply_next_patch",
        "thresholds": dict(base.thresholds),
        "adjustments": adjustments,
        "guardrails": guardrails,
        "applied_patch_count": len(safe_specs),
        "applied_axis_counts": dict(sorted(axis_counts.items())),
    }


def write_v12_rolling_profile(
    *,
    patch_specs_path: str | Path = "data/e2r/calibration/v12/v12_patch_specs.jsonl",
    profile_path: str | Path = V2_2_PROFILE_PATH,
    active_profile_path: str | Path = ACTIVE_PROFILE_PATH,
    report_directory: str | Path = "reports/e2r_calibration/v12",
    activate: bool = True,
) -> dict[str, Any]:
    patch_specs = _read_jsonl(patch_specs_path)
    payload = build_v12_rolling_profile_payload(patch_specs=patch_specs)
    profile_output = _write_yaml(Path(profile_path), payload)

    active_output: Path | None = None
    if activate:
        active_output = Path(active_profile_path)
        active_output.parent.mkdir(parents=True, exist_ok=True)
        active_output.write_text("active_profile: e2r_2_2\nrollback_profile: calibrated\n", encoding="utf-8")

    report_dir = Path(report_directory)
    report_dir.mkdir(parents=True, exist_ok=True)
    summary = {
        "profile_path": str(profile_output),
        "active_profile_path": str(active_output) if active_output else None,
        "profile_id": payload["profile_id"],
        "activate": activate,
        "production_default_scoring_changed": activate,
        "applied_patch_count": payload["applied_patch_count"],
        "applied_axis_counts": payload["applied_axis_counts"],
        "stage3_green_not_loosened": payload["guardrails"]["stage3_green_not_loosened_by_v12"],
        "rollback_profile": "calibrated",
    }
    _write_json(report_dir / "rolling_calibration_apply_summary.json", summary)
    (report_dir / "rolling_calibration_apply_report.md").write_text(
        _render_apply_report(summary, payload),
        encoding="utf-8",
    )
    return {"summary": summary, "profile_payload": payload}


def _render_apply_report(summary: dict[str, Any], payload: dict[str, Any]) -> str:
    lines = [
        "# V12 Rolling Calibration Apply Report",
        "",
        "v12 연구 결과의 `apply_next_patch` 항목을 기본 점수 프로파일에 반영했습니다.",
        "반영은 전역 완화가 아니라 large sector / canonical archetype scope가 맞을 때만 작동합니다.",
        "Stage 3-Green 기준은 낮추지 않았고, 가격만 오른 케이스는 positive Stage 승격을 막는 방향으로 유지했습니다.",
        "",
        f"- profile_id: `{summary['profile_id']}`",
        f"- profile_path: `{summary['profile_path']}`",
        f"- active_profile_path: `{summary['active_profile_path']}`",
        f"- production_default_scoring_changed: `{summary['production_default_scoring_changed']}`",
        f"- applied_patch_count: `{summary['applied_patch_count']}`",
        f"- applied_axis_counts: `{summary['applied_axis_counts']}`",
        f"- rollback_profile: `{summary['rollback_profile']}`",
        "",
        "## Applied Scope Counts",
    ]
    for key in (
        "v12_stage2_bonus_scopes",
        "v12_stage2_required_bridge_scopes",
        "v12_local_4b_watch_guard_scopes",
        "v12_full_4b_overlay_scopes",
        "v12_earlier_4c_watch_scopes",
        "v12_hard_4c_confirmation_scopes",
    ):
        scopes = str(payload["guardrails"].get(key, ""))
        count = len([item for item in scopes.split("|") if item])
        lines.append(f"- {key}: `{count}`")
    lines.extend(
        [
            "",
            "## Simple Example",
            "",
            "- 예전: C22 보험 archetype 연구가 쌓여도 보고서에만 남고 기본 점수는 바뀌지 않았습니다.",
            "- 지금: payload에 `canonical_archetype_id`가 직접 매칭될 때만 해당 scope의 bridge/guard와 runtime weight가 실제 적용됩니다.",
            "- 이번 배치처럼 `v12_stage2_bonus_scopes`가 0이면 Stage2 +1 보정은 적용하지 않습니다.",
            "- 반대로 price-only 4B scope에서는 주가 급등만으로 Stage2/Stage3 또는 full 4B가 되지 않도록 더 강하게 막습니다.",
        ]
    )
    return "\n".join(lines) + "\n"
