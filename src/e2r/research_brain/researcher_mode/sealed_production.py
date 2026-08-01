"""Verify a completed production lane before opening post-run Gold.

This module intentionally has no dependency on the Gold corpus or comparison
code.  A failed seal must be detected while the production process is still
Gold-blind so the caller can safely fall back to the normal production path.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash

from .canary_leaf_contract import canary_output_tree_hash


PRODUCTION_SEMANTICS_SEAL_SCHEMA_VERSION = (
    "e2r_v5_phase94_production_semantics_seal_v1"
)
SEALED_PRODUCTION_SEMANTICS_MATCH = "SEALED_PRODUCTION_SEMANTICS_MATCH"
INVALID_PRODUCTION_SEMANTICS = "INVALID_PRODUCTION_SEMANTICS"

ROOT_FROZEN_PRODUCTION_FILES = (
    "production_lane_manifest.json",
    "production_material_facts.jsonl",
    "production_component_memos.jsonl",
    "production_input_manifest.jsonl",
)
TARGET_FROZEN_PRODUCTION_FILES = (
    "evidence_facts.jsonl",
    "component_research_memos.jsonl",
    "score_vector.json",
    "stagecourt_trace.json",
)

_CANONICAL_STAGES = {
    "0",
    "1",
    "2",
    "3-Green",
    "3-Yellow",
    "3-Red",
    "4A",
    "4B",
    "4C",
    "5",
}
_POST_RUN_GOLD_MARKERS = (
    "post_run_gold",
    "gold_material_facts",
    "gold_source_map",
    "gold_question_coverage",
    "gold_fact_comparison",
    "post_run_gold_semantic",
)
_POST_RUN_ONLY_CODE_FILES = {
    "full_thesis_gold_benchmark.py",
    "blind_benchmark.py",
}


@dataclass(frozen=True)
class SealedProductionVerification:
    eligible: bool
    reasons: tuple[str, ...]
    frozen_file_sha256: Mapping[str, str]
    target_statuses: Mapping[str, str]
    target_completion_gates: Mapping[str, Mapping[str, bool]]


def build_current_production_semantics(
    *,
    config: Any,
    targets: Sequence[Any],
    registry_rows: Sequence[Mapping[str, Any]],
    target_registry_path: str | Path,
    provider_manifest: Mapping[str, Any],
    repo_root: str | Path,
) -> Mapping[str, Any]:
    """Fingerprint every current semantic authority needed to reuse a lane."""

    root = Path(repo_root).resolve()
    code_root = Path(__file__).resolve().parents[2]
    code_rows = tuple(
        {
            "path": str(path.relative_to(code_root)),
            "sha256": _sha256(path),
        }
        for path in sorted(code_root.rglob("*.py"))
        if path.is_file() and path.name not in _POST_RUN_ONLY_CODE_FILES
    )
    reference_paths = _production_reference_paths(
        repo_root=root,
        target_registry_path=target_registry_path,
    )
    reference_rows = tuple(
        {
            "path": _display_path(path, root),
            "sha256": _sha256(path),
        }
        for path in reference_paths
    )
    config_contract = {
        "schema_version": str(getattr(config, "schema_version", "")),
        "as_of_date": str(getattr(config, "as_of_date", "")),
        "archetype_id": str(getattr(config, "archetype_id", "")),
        "live_materialization_authorized": bool(
            getattr(config, "live_materialization_authorized", False)
        ),
        "checkpoint_resume": bool(getattr(config, "checkpoint_resume", False)),
        "gold_lane_isolated": bool(
            getattr(config, "gold_lane_isolated", False)
        ),
        "require_researcher_parity": bool(
            getattr(config, "require_researcher_parity", False)
        ),
        "latest_trading_snapshot_date": getattr(
            config, "latest_trading_snapshot_date", None
        ),
        "source_acquisition_mode": str(
            getattr(config, "source_acquisition_mode", "")
        ),
    }
    target_contract = tuple(
        {
            "target_id": str(getattr(target, "target_id", "")),
            "company_name": str(getattr(target, "company_name", "")),
            "aliases": list(getattr(target, "aliases", ()) or ()),
            "official_domains": list(
                getattr(target, "official_domains", ()) or ()
            ),
        }
        for target in targets
    )
    input_contract = {
        "config": config_contract,
        "targets": target_contract,
        "registry_rows": tuple(dict(row) for row in registry_rows),
        "reference_files": reference_rows,
    }
    fingerprints = {
        "code_fingerprint": stable_hash(code_rows),
        "config_fingerprint": stable_hash(config_contract),
        "provider_fingerprint": stable_hash(dict(provider_manifest)),
        "input_semantics_fingerprint": stable_hash(input_contract),
    }
    return {
        "schema_version": PRODUCTION_SEMANTICS_SEAL_SCHEMA_VERSION,
        **fingerprints,
        "semantics_fingerprint": stable_hash(fingerprints),
        "code_file_count": len(code_rows),
        "reference_file_count": len(reference_rows),
    }


def make_production_semantics_seal(
    *,
    before_run: Mapping[str, Any],
    after_run: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Seal only when code/config/provider/input stayed fixed for the run."""

    fingerprint_keys = (
        "code_fingerprint",
        "config_fingerprint",
        "provider_fingerprint",
        "input_semantics_fingerprint",
        "semantics_fingerprint",
    )
    unchanged = all(
        before_run.get(key) == after_run.get(key) for key in fingerprint_keys
    )
    return {
        "schema_version": PRODUCTION_SEMANTICS_SEAL_SCHEMA_VERSION,
        "status": (
            SEALED_PRODUCTION_SEMANTICS_MATCH
            if unchanged
            else INVALID_PRODUCTION_SEMANTICS
        ),
        **{key: after_run.get(key) for key in fingerprint_keys},
        "code_file_count": after_run.get("code_file_count"),
        "reference_file_count": after_run.get("reference_file_count"),
        "run_semantics_unchanged": unchanged,
        "before_run_semantics_fingerprint": before_run.get(
            "semantics_fingerprint"
        ),
        "after_run_semantics_fingerprint": after_run.get(
            "semantics_fingerprint"
        ),
    }


def reviewed_post_run_semantic_files_present(output_root: str | Path) -> bool:
    """Check names only; do not open any Gold-visible review content."""

    root = Path(output_root)
    primary = root / "post_run_gold_semantic_primary.json"
    reviews = root / "post_run_gold_semantic_reviews"
    return bool(
        primary.is_file()
        and reviews.is_dir()
        and len(tuple(path for path in reviews.glob("*.json") if path.is_file()))
        >= 2
    )


def verify_sealed_production(
    *,
    output_root: str | Path,
    target_ids: Sequence[str],
    as_of_date: str,
    archetype_id: str,
    expected_semantics: Mapping[str, Any],
) -> SealedProductionVerification:
    """Load, contract-check, and hash a completed production lane."""

    root = Path(output_root)
    expected_target_ids = tuple(str(value) for value in target_ids)
    expected_target_set = set(expected_target_ids)
    reasons: list[str] = []
    target_statuses: dict[str, str] = {}
    target_gates: dict[str, Mapping[str, bool]] = {}

    lane = _read_json_object(
        root / "production_lane_manifest.json",
        reasons=reasons,
        label="production_lane_manifest",
    )
    if lane:
        _require_equal(
            reasons,
            lane.get("schema_version"),
            "e2r_v5_phase94_production_lane_v1",
            "production_lane_schema_mismatch",
        )
        _require_equal(
            reasons,
            lane.get("as_of_date"),
            as_of_date,
            "production_lane_as_of_date_mismatch",
        )
        _require_equal(
            reasons,
            lane.get("archetype_id"),
            archetype_id,
            "production_lane_archetype_mismatch",
        )
        if tuple(str(value) for value in lane.get("target_ids") or ()) != (
            expected_target_ids
        ):
            reasons.append("production_lane_target_roster_mismatch")
        if lane.get("production_research_complete") is not True:
            reasons.append("production_lane_not_complete")
        if lane.get("comparison_timing") != "POST_RUN_ONLY":
            reasons.append("production_lane_comparison_timing_invalid")
        for key in (
            "gold_visibility",
            "gold_query_visibility",
            "gold_url_visibility",
            "gold_fact_visibility",
        ):
            if lane.get(key) is not False:
                reasons.append(f"production_lane_{key}_not_false")
        lane_statuses = lane.get("target_statuses")
        if not isinstance(lane_statuses, Mapping) or set(lane_statuses) != (
            expected_target_set
        ):
            reasons.append("production_lane_target_statuses_mismatch")
        elif any(
            status
            != "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
            for status in lane_statuses.values()
        ):
            reasons.append("production_lane_target_not_complete")
        _validate_semantics_seal(
            reasons,
            seal=lane.get("production_semantics_seal"),
            expected=expected_semantics,
        )

    root_rows = {
        name: _read_jsonl_objects(root / name, reasons=reasons, label=name)
        for name in ROOT_FROZEN_PRODUCTION_FILES
        if name.endswith(".jsonl")
    }
    for filename, rows in root_rows.items():
        if not rows:
            reasons.append(f"{filename}:empty")
            continue
        row_targets = {
            str(row.get("target_id") or "")
            for row in rows
            if str(row.get("target_id") or "")
        }
        if row_targets != expected_target_set:
            reasons.append(f"{filename}:target_roster_mismatch")
        if _contains_post_run_gold_marker(rows):
            reasons.append(f"{filename}:post_run_gold_visible")
    for row in root_rows.get("production_material_facts.jsonl", ()):
        if row.get("gold_visibility") is not False:
            reasons.append("production_material_fact_gold_visibility_not_false")
            break
    for row in root_rows.get("production_component_memos.jsonl", ()):
        if row.get("gold_visibility") is not False:
            reasons.append("production_component_memo_gold_visibility_not_false")
            break

    for target_id in expected_target_ids:
        target_root = root / target_id
        manifest = _read_json_object(
            target_root / "target_run_manifest.json",
            reasons=reasons,
            label=f"{target_id}:target_run_manifest",
        )
        audit = _read_json_object(
            target_root / "current_researcher_mode_audit.json",
            reasons=reasons,
            label=f"{target_id}:current_researcher_mode_audit",
        )
        canary = _read_json_object(
            target_root / "canary_leaf_contract_audit.json",
            reasons=reasons,
            label=f"{target_id}:canary_leaf_contract_audit",
        )
        gates = _validate_target_manifests(
            reasons,
            root=target_root,
            target_id=target_id,
            as_of_date=as_of_date,
            archetype_id=archetype_id,
            manifest=manifest,
            audit=audit,
            canary=canary,
        )
        target_gates[target_id] = gates
        target_statuses[target_id] = str(manifest.get("status") or "")

        evidence_rows = _read_jsonl_objects(
            target_root / "evidence_facts.jsonl",
            reasons=reasons,
            label=f"{target_id}:evidence_facts",
        )
        memo_rows = _read_jsonl_objects(
            target_root / "component_research_memos.jsonl",
            reasons=reasons,
            label=f"{target_id}:component_research_memos",
        )
        if not evidence_rows:
            reasons.append(f"{target_id}:evidence_facts_empty")
        if not memo_rows:
            reasons.append(f"{target_id}:component_research_memos_empty")
        for label, rows in (
            ("evidence_facts", evidence_rows),
            ("component_research_memos", memo_rows),
        ):
            if any(str(row.get("target_id") or "") != target_id for row in rows):
                reasons.append(f"{target_id}:{label}_scope_mismatch")
            if _contains_post_run_gold_marker(rows):
                reasons.append(f"{target_id}:{label}_post_run_gold_visible")

        score = _read_json_object(
            target_root / "score_vector.json",
            reasons=reasons,
            label=f"{target_id}:score_vector",
        )
        _validate_score_vector(
            reasons,
            root=target_root,
            target_id=target_id,
            as_of_date=as_of_date,
            score=score,
        )
        trace = _read_json_object(
            target_root / "stagecourt_trace.json",
            reasons=reasons,
            label=f"{target_id}:stagecourt_trace",
        )
        _validate_stagecourt_trace(
            reasons,
            target_id=target_id,
            as_of_date=as_of_date,
            trace=trace,
        )

    frozen_paths = _frozen_paths(root, expected_target_ids)
    frozen_hashes: dict[str, str] = {}
    for path in frozen_paths:
        if not path.is_file():
            reasons.append(f"frozen_file_missing:{path.relative_to(root)}")
            continue
        frozen_hashes[str(path.relative_to(root))] = _sha256(path)
    if len(frozen_hashes) != len(frozen_paths):
        reasons.append("frozen_file_roster_incomplete")
    return SealedProductionVerification(
        eligible=not reasons,
        reasons=tuple(dict.fromkeys(reasons)),
        frozen_file_sha256=frozen_hashes,
        target_statuses=target_statuses,
        target_completion_gates=target_gates,
    )


def assert_frozen_production_unchanged(
    *,
    output_root: str | Path,
    verification: SealedProductionVerification,
) -> None:
    """Fail if post-run work changed any sealed production byte."""

    if not verification.eligible:
        raise ValueError("cannot assert an ineligible production seal")
    root = Path(output_root)
    current = {
        relative: _sha256(root / relative)
        for relative in verification.frozen_file_sha256
        if (root / relative).is_file()
    }
    if current != dict(verification.frozen_file_sha256):
        changed = sorted(
            set(current)
            ^ set(verification.frozen_file_sha256)
            | {
                path
                for path in set(current) & set(verification.frozen_file_sha256)
                if current[path] != verification.frozen_file_sha256[path]
            }
        )
        raise RuntimeError(
            "post-run Gold mutated sealed production files: "
            + ",".join(changed)
        )


def _validate_semantics_seal(
    reasons: list[str],
    *,
    seal: Any,
    expected: Mapping[str, Any],
) -> None:
    if not isinstance(seal, Mapping):
        reasons.append("production_semantics_seal_missing")
        return
    if seal.get("schema_version") != PRODUCTION_SEMANTICS_SEAL_SCHEMA_VERSION:
        reasons.append("production_semantics_seal_schema_mismatch")
    if seal.get("status") != SEALED_PRODUCTION_SEMANTICS_MATCH:
        reasons.append("production_semantics_seal_not_valid")
    component_keys = (
        "code_fingerprint",
        "config_fingerprint",
        "provider_fingerprint",
        "input_semantics_fingerprint",
    )
    for key in (*component_keys, "semantics_fingerprint"):
        if not seal.get(key) or seal.get(key) != expected.get(key):
            reasons.append(f"production_semantics_{key}_mismatch")
    seal_components = {key: seal.get(key) for key in component_keys}
    expected_components = {key: expected.get(key) for key in component_keys}
    if seal.get("semantics_fingerprint") != stable_hash(seal_components):
        reasons.append("production_semantics_seal_hash_invalid")
    if expected.get("semantics_fingerprint") != stable_hash(
        expected_components
    ):
        reasons.append("current_production_semantics_hash_invalid")


def _validate_target_manifests(
    reasons: list[str],
    *,
    root: Path,
    target_id: str,
    as_of_date: str,
    archetype_id: str,
    manifest: Mapping[str, Any],
    audit: Mapping[str, Any],
    canary: Mapping[str, Any],
) -> Mapping[str, bool]:
    required_status = "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
    for label, payload in (("manifest", manifest), ("audit", audit)):
        if str(payload.get("target_id") or "") != target_id:
            reasons.append(f"{target_id}:{label}_target_mismatch")
        if str(payload.get("as_of_date") or "") != as_of_date:
            reasons.append(f"{target_id}:{label}_as_of_date_mismatch")
        if payload.get("status") != required_status:
            reasons.append(f"{target_id}:{label}_status_not_complete")
        if payload.get("production_research_complete") is not True:
            reasons.append(f"{target_id}:{label}_production_not_complete")
        if payload.get("gold_visibility") is not False:
            reasons.append(f"{target_id}:{label}_gold_visibility_not_false")
    if str(manifest.get("archetype_id") or "") != archetype_id:
        reasons.append(f"{target_id}:manifest_archetype_mismatch")
    manifest_gates = manifest.get("completion_gates")
    audit_gates = audit.get("completion_gates")
    if (
        not isinstance(manifest_gates, Mapping)
        or not manifest_gates
        or any(value is not True for value in manifest_gates.values())
    ):
        reasons.append(f"{target_id}:manifest_completion_gates_invalid")
        gates: Mapping[str, bool] = {}
    else:
        gates = {str(key): bool(value) for key, value in manifest_gates.items()}
    if not isinstance(audit_gates, Mapping) or dict(audit_gates) != dict(
        manifest_gates or {}
    ):
        reasons.append(f"{target_id}:audit_completion_gates_mismatch")
    if (
        str(canary.get("target_id") or "") != target_id
        or str(canary.get("as_of_date") or "") != as_of_date
        or canary.get("status") != "CANARY_LEAF_CONTRACT_PASS"
        or canary.get("critical_count_sum") != 0
    ):
        reasons.append(f"{target_id}:canary_leaf_contract_invalid")
    canary_binding = manifest.get("canary_leaf_contract")
    if (
        not isinstance(canary_binding, Mapping)
        or canary_binding.get("status") != "CANARY_LEAF_CONTRACT_PASS"
        or canary_binding.get("critical_count_sum") != 0
    ):
        reasons.append(f"{target_id}:manifest_canary_binding_invalid")
    if manifest.get("output_tree_hash") != canary_output_tree_hash(
        root,
        include_post_run_gold=False,
    ):
        reasons.append(f"{target_id}:manifest_output_tree_hash_mismatch")
    return gates


def _validate_score_vector(
    reasons: list[str],
    *,
    root: Path,
    target_id: str,
    as_of_date: str,
    score: Mapping[str, Any],
) -> None:
    if (
        score.get("schema_version") != "e2r_v5_canary_score_vector_v1"
        or score.get("target_id") != target_id
        or score.get("as_of_date") != as_of_date
        or score.get("status") != "COMPLETE"
        or score.get("score_valid") is not True
        or score.get("production_stage_authority") is not False
        or score.get("pending_reasons") not in ([], ())
    ):
        reasons.append(f"{target_id}:score_vector_invalid")
    source_name = score.get("source_artifact")
    source = root / str(source_name or "")
    if (
        source_name != "deterministic_total_score.json"
        or not source.is_file()
        or score.get("source_sha256") != _sha256(source)
    ):
        reasons.append(f"{target_id}:score_vector_source_binding_invalid")


def _validate_stagecourt_trace(
    reasons: list[str],
    *,
    target_id: str,
    as_of_date: str,
    trace: Mapping[str, Any],
) -> None:
    decision = trace.get("decision")
    audit = trace.get("audit")
    invalid = bool(
        trace.get("schema_version") != "e2r_v5_researcher_stagecourt_run_v1"
        or not isinstance(decision, Mapping)
        or decision.get("target_id") != target_id
        or decision.get("as_of_date") != as_of_date
        or decision.get("status") != "FINAL"
        or decision.get("score_valid") is not True
        or decision.get("research_complete") is not True
        or decision.get("counter_thesis_complete") is not True
        or decision.get("stage_gates_complete") is not True
        or decision.get("canonical_stage") not in _CANONICAL_STAGES
        or not isinstance(audit, Mapping)
        or audit.get("status") != "STAGECOURT_AUDIT_PASS"
        or audit.get("critical_count_sum") != 0
        or audit.get("canonical_stage") != decision.get("canonical_stage")
    )
    if invalid:
        reasons.append(f"{target_id}:stagecourt_trace_invalid")
    if _contains_post_run_gold_marker(trace):
        reasons.append(f"{target_id}:stagecourt_trace_post_run_gold_visible")


def _production_reference_paths(
    *, repo_root: Path, target_registry_path: str | Path
) -> tuple[Path, ...]:
    candidates = [
        Path(target_registry_path).resolve(),
        repo_root / "configs/e2r_issuer_official_domains_v1.json",
        repo_root / "docs/operational/e2r_v5_component_anchor_atlas.json",
    ]
    paths = {path for path in candidates if path.is_file()}
    atlas_root = repo_root / "output/researcher_parity/judgment_atlas"
    if candidates[-1] not in paths and atlas_root.is_dir():
        paths.update(path for path in atlas_root.rglob("*") if path.is_file())
    return tuple(sorted(paths))


def _frozen_paths(root: Path, target_ids: Sequence[str]) -> tuple[Path, ...]:
    return tuple(root / name for name in ROOT_FROZEN_PRODUCTION_FILES) + tuple(
        root / target_id / name
        for target_id in target_ids
        for name in TARGET_FROZEN_PRODUCTION_FILES
    )


def _contains_post_run_gold_marker(value: Any) -> bool:
    if isinstance(value, Mapping):
        return any(
            _contains_post_run_gold_marker(key)
            or _contains_post_run_gold_marker(item)
            for key, item in value.items()
        )
    if isinstance(value, (list, tuple)):
        return any(_contains_post_run_gold_marker(item) for item in value)
    if isinstance(value, str):
        normalized = value.casefold().replace("-", "_")
        return any(marker in normalized for marker in _POST_RUN_GOLD_MARKERS)
    return False


def _read_json_object(
    path: Path, *, reasons: list[str], label: str
) -> Mapping[str, Any]:
    if not path.is_file():
        reasons.append(f"{label}:missing")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        reasons.append(f"{label}:invalid_json")
        return {}
    if not isinstance(value, Mapping):
        reasons.append(f"{label}:not_object")
        return {}
    return dict(value)


def _read_jsonl_objects(
    path: Path, *, reasons: list[str], label: str
) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        reasons.append(f"{label}:missing")
        return ()
    rows: list[Mapping[str, Any]] = []
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, Mapping):
                reasons.append(f"{label}:non_object_row")
                return ()
            rows.append(dict(value))
    except (OSError, UnicodeError, json.JSONDecodeError):
        reasons.append(f"{label}:invalid_jsonl")
        return ()
    return tuple(rows)


def _require_equal(
    reasons: list[str], actual: Any, expected: Any, reason: str
) -> None:
    if actual != expected:
        reasons.append(reason)


def _display_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


__all__ = [
    "INVALID_PRODUCTION_SEMANTICS",
    "PRODUCTION_SEMANTICS_SEAL_SCHEMA_VERSION",
    "ROOT_FROZEN_PRODUCTION_FILES",
    "SEALED_PRODUCTION_SEMANTICS_MATCH",
    "TARGET_FROZEN_PRODUCTION_FILES",
    "SealedProductionVerification",
    "assert_frozen_production_unchanged",
    "build_current_production_semantics",
    "make_production_semantics_seal",
    "reviewed_post_run_semantic_files_present",
    "verify_sealed_production",
]
