"""Runtime scoring-profile loader for baseline/calibrated E2R scoring."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import os


CONFIG_DIR = Path("configs")
BASELINE_PROFILE_PATH = CONFIG_DIR / "e2r_scoring_profile_baseline.yaml"
CALIBRATED_PROFILE_PATH = CONFIG_DIR / "e2r_scoring_profile_calibrated.yaml"
ACTIVE_PROFILE_PATH = CONFIG_DIR / "e2r_scoring_profile_active.yaml"


@dataclass(frozen=True)
class ScoringProfile:
    profile_id: str
    profile_status: str
    previous_default_profile: str | None = None
    thresholds: dict[str, float] = field(default_factory=dict)
    adjustments: dict[str, float] = field(default_factory=dict)
    guardrails: dict[str, bool | float | str] = field(default_factory=dict)
    basis: str | None = None

    def threshold(self, key: str, default: float) -> float:
        return float(self.thresholds.get(key, default))

    def adjustment(self, key: str, default: float = 0.0) -> float:
        return float(self.adjustments.get(key, default))

    def guardrail_enabled(self, key: str, default: bool = False) -> bool:
        value = self.guardrails.get(key, default)
        if isinstance(value, bool):
            return value
        return str(value).strip().lower() in {"true", "yes", "1", "enabled"}


def _parse_scalar(value: str) -> Any:
    stripped = value.strip()
    if stripped.lower() in {"true", "false"}:
        return stripped.lower() == "true"
    try:
        if "." in stripped:
            return float(stripped)
        return int(stripped)
    except ValueError:
        return stripped.strip('"').strip("'")


def _load_simple_yaml(path: Path) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_section: str | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" ") and line.endswith(":"):
            current_section = line[:-1].strip()
            data[current_section] = {}
            continue
        if ":" not in line:
            continue
        key, value = [part.strip() for part in line.split(":", 1)]
        if raw_line.startswith("  ") and current_section:
            data.setdefault(current_section, {})[key] = _parse_scalar(value)
        else:
            data[key] = _parse_scalar(value)
            current_section = None
    return data


def load_scoring_profile(path: str | Path) -> ScoringProfile:
    path_obj = Path(path)
    payload = _load_simple_yaml(path_obj)
    return ScoringProfile(
        profile_id=str(payload.get("profile_id", path_obj.stem)),
        profile_status=str(payload.get("profile_status", "unknown")),
        previous_default_profile=payload.get("previous_default_profile"),
        thresholds=dict(payload.get("thresholds", {})),
        adjustments=dict(payload.get("adjustments", {})),
        guardrails=dict(payload.get("guardrails", {})),
        basis=payload.get("profile_basis"),
    )


def active_profile_path() -> Path:
    override = os.environ.get("E2R_SCORING_PROFILE", "").strip().lower()
    if override == "baseline":
        return BASELINE_PROFILE_PATH
    if override == "calibrated":
        return CALIBRATED_PROFILE_PATH
    if ACTIVE_PROFILE_PATH.exists():
        payload = _load_simple_yaml(ACTIVE_PROFILE_PATH)
        active = str(payload.get("active_profile", "calibrated")).strip().lower()
        if active == "baseline":
            return BASELINE_PROFILE_PATH
    return CALIBRATED_PROFILE_PATH if CALIBRATED_PROFILE_PATH.exists() else BASELINE_PROFILE_PATH


def get_active_scoring_profile() -> ScoringProfile:
    path = active_profile_path()
    if path.exists():
        return load_scoring_profile(path)
    return ScoringProfile(
        profile_id="e2r_2_0_baseline",
        profile_status="fallback_default",
        thresholds={
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
        },
    )
