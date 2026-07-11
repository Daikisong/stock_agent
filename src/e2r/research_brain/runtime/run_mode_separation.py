"""Shared mode identity and contamination guards for replay and current runs."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Mapping

from e2r.production.metadata import stable_hash, write_json


RUN_MODE_MARKER_SCHEMA_VERSION = "e2r_run_mode_marker_v1"


class CanonicalRunMode(str, Enum):
    HISTORICAL_REPLAY = "HISTORICAL_REPLAY"
    CURRENT_OPERATION = "CURRENT_OPERATION"


_MODE_MANIFEST_NAMES: Mapping[CanonicalRunMode, str] = {
    CanonicalRunMode.HISTORICAL_REPLAY: "historical_replay_manifest.json",
    CanonicalRunMode.CURRENT_OPERATION: "current_operation_manifest.json",
}
_FORBIDDEN_PLANNER_KEY_FRAGMENTS = (
    "expected_archetype",
    "expected_stage",
    "expected_outcome",
    "future_outcome",
    "outcome_label",
    "future_return",
    "mfe",
    "mae",
)
_FORBIDDEN_PLANNER_VALUE_RE = re.compile(
    r"(?:\bmfe\b|\bmae\b|future[_ -]?(?:outcome|return)|"
    r"outcome[_ -]?label|expected[_ -]?(?:stage|archetype))",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class RunModeMarker:
    run_id: str
    mode: str
    output_namespace: str
    production_runtime_ready: bool = False
    schema_version: str = RUN_MODE_MARKER_SCHEMA_VERSION

    def __post_init__(self) -> None:
        CanonicalRunMode(self.mode)
        if not self.run_id.strip() or not self.output_namespace.strip():
            raise ValueError("run mode marker identity is required")
        expected_namespace = {
            CanonicalRunMode.HISTORICAL_REPLAY.value: "historical_replay",
            CanonicalRunMode.CURRENT_OPERATION.value: "current_operation",
        }[self.mode]
        if self.output_namespace != expected_namespace:
            raise ValueError("run mode output namespace mismatch")
        if not isinstance(self.production_runtime_ready, bool):
            raise ValueError("run mode readiness must be boolean")
        if self.production_runtime_ready:
            raise ValueError("Phase 11 mode marker cannot declare runtime ready")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def claim_mode_output_root(
    output_root: str | Path,
    *,
    mode: CanonicalRunMode | str,
    run_id: str,
) -> Path:
    """Claim an output root for exactly one canonical mode."""

    selected_mode = CanonicalRunMode(mode)
    root = Path(output_root)
    if root.exists() and not root.is_dir():
        raise ValueError("run output root exists and is not a directory")
    root.mkdir(parents=True, exist_ok=True)
    marker_path = root / "e2r_run_mode.json"
    if marker_path.exists():
        raw = json.loads(marker_path.read_text(encoding="utf-8"))
        if raw.get("mode") != selected_mode.value:
            raise ValueError("historical replay and current operation cannot share output root")
        # A dated operational root may be deterministically refreshed after a
        # newly accepted checkpoint is promoted.  The hard boundary is the
        # canonical mode, not an obsolete run ID from an earlier same-day pass.
    for manifest_mode, filename in _MODE_MANIFEST_NAMES.items():
        if manifest_mode != selected_mode and (root / filename).exists():
            raise ValueError("opposite-mode manifest already exists in output root")
    marker = RunModeMarker(
        run_id=run_id,
        mode=selected_mode.value,
        output_namespace={
            CanonicalRunMode.HISTORICAL_REPLAY: "historical_replay",
            CanonicalRunMode.CURRENT_OPERATION: "current_operation",
        }[selected_mode],
    )
    write_json(marker_path, marker.to_dict())
    return marker_path


def forbidden_planner_context_paths(payload: Any) -> tuple[str, ...]:
    """Return evaluator/outcome paths that must not enter a planner payload."""

    findings: list[str] = []

    def visit(value: Any, path: str) -> None:
        if isinstance(value, Mapping):
            for key, item in value.items():
                key_text = str(key).casefold()
                next_path = f"{path}.{key}" if path else str(key)
                if any(fragment in key_text for fragment in _FORBIDDEN_PLANNER_KEY_FRAGMENTS):
                    findings.append(next_path)
                visit(item, next_path)
        elif isinstance(value, (tuple, list)):
            for index, item in enumerate(value):
                visit(item, f"{path}[{index}]")
        elif isinstance(value, str) and _FORBIDDEN_PLANNER_VALUE_RE.search(value):
            findings.append(path or "<root>")

    visit(payload, "")
    return tuple(dict.fromkeys(findings))


def audit_historical_current_separation(
    *,
    historical_manifest: Mapping[str, Any],
    current_manifest: Mapping[str, Any],
) -> Mapping[str, Any]:
    required_historical = {
        "run_id",
        "mode",
        "output_namespace",
        "status",
        "leaf_hash",
        "current_watchlist_eligible_count",
        "production_runtime_ready",
    }
    required_current = {
        "run_id",
        "mode",
        "output_namespace",
        "status",
        "leaf_hash",
        "historical_replay_input_count",
        "forced_archetype_materialization_count",
        "archetype_quota_count",
        "expected_or_outcome_context_count",
        "production_runtime_ready",
    }
    critical = {
        "historical_manifest_field_missing": len(
            required_historical - set(historical_manifest)
        ),
        "current_manifest_field_missing": len(required_current - set(current_manifest)),
        "historical_mode_identity_mismatch": int(
            historical_manifest.get("mode")
            != CanonicalRunMode.HISTORICAL_REPLAY.value
        ),
        "current_mode_identity_mismatch": int(
            current_manifest.get("mode")
            != CanonicalRunMode.CURRENT_OPERATION.value
        ),
        "historical_output_namespace_mismatch": int(
            historical_manifest.get("output_namespace") != "historical_replay"
        ),
        "current_output_namespace_mismatch": int(
            current_manifest.get("output_namespace") != "current_operation"
        ),
        "historical_parity_not_pass": int(
            historical_manifest.get("status") != "HISTORICAL_REPLAY_PARITY_PASS"
        ),
        "current_mode_separation_not_pass": int(
            current_manifest.get("status")
            != "CURRENT_OPERATION_MODE_SEPARATION_PASS"
        ),
        "shared_run_identity": int(
            bool(historical_manifest.get("run_id"))
            and historical_manifest.get("run_id") == current_manifest.get("run_id")
        ),
        "historical_row_current_watchlist_eligible": int(
            historical_manifest.get("current_watchlist_eligible_count", 0)
        ),
        "historical_input_in_current_operation": int(
            current_manifest.get("historical_replay_input_count", 0)
        ),
        "forced_current_archetype_materialization": int(
            current_manifest.get("forced_archetype_materialization_count", 0)
        ),
        "current_archetype_quota": int(
            current_manifest.get("archetype_quota_count", 0)
        ),
        "expected_or_outcome_context_in_current": int(
            current_manifest.get("expected_or_outcome_context_count", 0)
        ),
        "phase11_production_readiness_overclaim": int(
            bool(historical_manifest.get("production_runtime_ready"))
            or bool(current_manifest.get("production_runtime_ready"))
        ),
    }
    payload = {
        "historical_run_id": historical_manifest.get("run_id"),
        "current_run_id": current_manifest.get("run_id"),
        "historical_leaf_hash": historical_manifest.get("leaf_hash"),
        "current_leaf_hash": current_manifest.get("leaf_hash"),
        "critical_counts": critical,
    }
    return {
        "schema_version": "e2r_historical_current_separation_audit_v1",
        "status": (
            "HISTORICAL_CURRENT_MODE_SEPARATION_PASS"
            if sum(critical.values()) == 0
            else "HISTORICAL_CURRENT_MODE_SEPARATION_FAIL"
        ),
        **payload,
        "critical_count_sum": sum(critical.values()),
        "result_hash": stable_hash(payload),
        "production_runtime_ready": False,
    }


__all__ = [
    "RUN_MODE_MARKER_SCHEMA_VERSION",
    "CanonicalRunMode",
    "RunModeMarker",
    "audit_historical_current_separation",
    "claim_mode_output_root",
    "forbidden_planner_context_paths",
]
