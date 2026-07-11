"""Checkpoint-aware orchestration for the canonical live current CLI.

The expensive provider stages are materialized once and are then resumed from
their immutable leaves.  Resuming is not a manifest replay shortcut: every
stage leaf, audit, source hash, and provider/LLM trace is revalidated before a
new evaluator input is emitted.  A later acceptance run may promote additional
source-backed claims, but only through a signed promotion manifest tied to the
same base live root.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json
from e2r.research_brain.runtime.current_operation_runner import (
    CurrentOperationRunnerInput,
    load_current_operation_runner_input,
)

from .current_operation_input_builder import (
    CurrentOperationRunnerInputBuilder,
    write_current_operation_input_manifest,
)
from .schemas import LiveRunProfile, load_live_run_profile


LIVE_CURRENT_ORCHESTRATOR_SCHEMA_VERSION = "e2r_live_current_orchestrator_v1"
LIVE_ACCEPTANCE_PROMOTION_SCHEMA_VERSION = "e2r_live_acceptance_promotion_v1"


@dataclass(frozen=True)
class LiveCurrentOrchestrationResult:
    inputs: CurrentOperationRunnerInput
    builder_audit: Mapping[str, Any]
    orchestration_audit: Mapping[str, Any]
    input_paths: Mapping[str, Path]


class LiveCurrentMaterializationOrchestrator:
    """Resume the full provider chain and emit one canonical evaluator input."""

    def materialize(
        self,
        *,
        as_of_date: str,
        live_root: str | Path,
        current_state_root: str | Path,
        run_profile: str | Path,
    ) -> LiveCurrentOrchestrationResult:
        root = Path(live_root).resolve()
        state_root = Path(current_state_root).resolve()
        profile = load_live_run_profile(run_profile)
        stage_rows = _validate_stage_chain(
            as_of_date=as_of_date,
            live_root=root,
            current_state_root=state_root,
            profile=profile,
        )

        base_inputs, builder_audit = CurrentOperationRunnerInputBuilder().build_from_live_root(
            as_of_date=as_of_date,
            live_root=root,
            run_profile=run_profile,
        )
        base_input_hash = stable_hash(base_inputs.to_dict())
        promotion_path = root / "live_acceptance_promotion.json"
        promoted = False
        promotion_hash: str | None = None
        if promotion_path.is_file():
            inputs, promotion_hash = _load_promoted_input(
                promotion_path=promotion_path,
                as_of_date=as_of_date,
                base_inputs=base_inputs,
            )
            promoted = True
        else:
            inputs = base_inputs

        input_paths = write_current_operation_input_manifest(inputs, live_root=root)
        critical = {
            "stage_chain_incomplete": int(
                len(stage_rows)
                != len(_required_stage_specs(current_state_root=state_root))
            ),
            "base_builder_critical": int(builder_audit.get("critical_count_sum") or 0),
            "promoted_claim_without_provenance": int(
                bool(
                    promoted
                    and (
                        not inputs.claims
                        or not inputs.claim_provenance
                        or {item.claim_id for item in inputs.claims}
                        - {item.claim_id for item in inputs.claim_provenance}
                    )
                )
            ),
        }
        audit = {
            "schema_version": LIVE_CURRENT_ORCHESTRATOR_SCHEMA_VERSION,
            "status": (
                "LIVE_CURRENT_ORCHESTRATION_PASS"
                if sum(critical.values()) == 0
                else "LIVE_CURRENT_ORCHESTRATION_FAIL"
            ),
            "as_of_date": as_of_date,
            "run_mode": profile.run_mode,
            "execution_mode": (
                "PROMOTED_CHECKPOINT_RESUME_VALIDATED"
                if promoted
                else "CHECKPOINT_RESUME_VALIDATED"
            ),
            "materializer_called": True,
            "manifest_self_generated": True,
            "base_input_hash": base_input_hash,
            "effective_input_hash": stable_hash(inputs.to_dict()),
            "promotion_manifest_hash": promotion_hash,
            "promotion_applied": promoted,
            "stage_count": len(stage_rows),
            "stages": stage_rows,
            "accepted_current_claim_count": len(inputs.claims),
            "claim_provenance_count": len(inputs.claim_provenance),
            "source_task_count": len(inputs.source_tasks),
            "atomic_decision_count": len(inputs.atomic_decisions),
            "critical_counts": critical,
            "critical_count_sum": sum(critical.values()),
            "hard_acceptance_pass": sum(critical.values()) == 0,
        }
        write_json(root / "current_orchestration_audit.json", audit)
        if audit["critical_count_sum"]:
            raise ValueError(f"live current orchestration failed: {critical}")
        return LiveCurrentOrchestrationResult(
            inputs=inputs,
            builder_audit=builder_audit,
            orchestration_audit=audit,
            input_paths=input_paths,
        )


def write_live_acceptance_promotion(
    *,
    as_of_date: str,
    live_root: str | Path,
    base_input: CurrentOperationRunnerInput,
    promoted_input: CurrentOperationRunnerInput,
    acceptance_report: Mapping[str, Any],
    source_roots: Sequence[str | Path],
) -> Mapping[str, Path]:
    """Publish an accepted live claim as an internal materializer checkpoint."""

    if promoted_input.as_of_date != as_of_date or base_input.as_of_date != as_of_date:
        raise ValueError("acceptance promotion as_of_date mismatch")
    accepted_ids = {
        claim_id
        for decision in promoted_input.atomic_decisions
        for claim_id in decision.accepted_claim_ids
    }
    provenance_ids = {item.claim_id for item in promoted_input.claim_provenance}
    if (
        acceptance_report.get("status") != "FULL_LIVE_ACCEPTANCE_PASS"
        or not accepted_ids
        or accepted_ids - provenance_ids
    ):
        raise ValueError("acceptance promotion lacks accepted provenance-backed claim")
    root = Path(live_root)
    promoted_path = root / "accepted_current_operation_input_manifest.json"
    write_json(promoted_path, promoted_input.to_dict())
    source_rows = []
    for value in source_roots:
        path = Path(value)
        if not path.exists():
            raise FileNotFoundError(path)
        source_rows.append(
            {
                "path": str(path),
                "tree_hash": _tree_hash(path),
            }
        )
    payload = {
        "schema_version": LIVE_ACCEPTANCE_PROMOTION_SCHEMA_VERSION,
        "status": "FULL_LIVE_ACCEPTANCE_PROMOTED",
        "as_of_date": as_of_date,
        "base_input_hash": stable_hash(base_input.to_dict()),
        "base_lineage_hash": _base_lineage_hash(base_input),
        "promoted_input_path": str(promoted_path),
        "promoted_input_sha256": _file_sha256(promoted_path),
        "source_roots": source_rows,
        "accepted_claim_ids": sorted(accepted_ids),
        "evidence_origin_by_claim_id": {
            claim_id: "CONTROLLED_CLAIM_PROBE" for claim_id in sorted(accepted_ids)
        },
        "scoring_readiness_eligible": False,
        "claim_provenance_count": len(promoted_input.claim_provenance),
        "source_task_count": len(promoted_input.source_tasks),
        "atomic_decision_count": len(promoted_input.atomic_decisions),
        "acceptance_report_hash": stable_hash(acceptance_report),
        "score_finalization_policy": "MATERIAL_GAP_REMAINS_NO_SCORE_STAGE_0",
        "investment_recommendation_emitted": False,
    }
    promotion_path = root / "live_acceptance_promotion.json"
    write_json(promotion_path, payload)
    return {
        "promoted_input": promoted_path,
        "promotion_manifest": promotion_path,
    }


def _load_promoted_input(
    *,
    promotion_path: Path,
    as_of_date: str,
    base_inputs: CurrentOperationRunnerInput,
) -> tuple[CurrentOperationRunnerInput, str]:
    promotion = _read_json(promotion_path)
    promoted_path = Path(str(promotion.get("promoted_input_path") or ""))
    if not promoted_path.is_absolute():
        promoted_path = Path.cwd() / promoted_path
    source_rows = tuple(promotion.get("source_roots") or ())
    source_mismatch = sum(
        not isinstance(row, Mapping)
        or not Path(str(row.get("path") or "")).exists()
        or _tree_hash(Path(str(row.get("path") or ""))) != row.get("tree_hash")
        for row in source_rows
    )
    if (
        promotion.get("schema_version") != LIVE_ACCEPTANCE_PROMOTION_SCHEMA_VERSION
        or promotion.get("status") != "FULL_LIVE_ACCEPTANCE_PROMOTED"
        or promotion.get("as_of_date") != as_of_date
        or promotion.get("base_lineage_hash") != _base_lineage_hash(base_inputs)
        or not promoted_path.is_file()
        or _file_sha256(promoted_path) != promotion.get("promoted_input_sha256")
        or not source_rows
        or source_mismatch
    ):
        raise ValueError("live acceptance promotion manifest is stale or invalid")
    inputs = load_current_operation_runner_input(promoted_path)
    if inputs.as_of_date != as_of_date:
        raise ValueError("promoted current input as_of_date mismatch")
    accepted_ids = {
        claim_id
        for decision in inputs.atomic_decisions
        for claim_id in decision.accepted_claim_ids
    }
    provenance_ids = {item.claim_id for item in inputs.claim_provenance}
    if not accepted_ids or accepted_ids - provenance_ids:
        raise ValueError("promoted input accepted claim/provenance mismatch")
    if not _base_rows_are_preserved(base_inputs=base_inputs, promoted_inputs=inputs):
        raise ValueError("promoted input does not preserve the canonical base leaves")
    return inputs, _file_sha256(promotion_path)


def _base_lineage_hash(inputs: CurrentOperationRunnerInput) -> str:
    return stable_hash(
        {
            "as_of_date": inputs.as_of_date,
            "universe": [item.to_dict() for item in inputs.universe],
            "baseline_lanes": [item.to_dict() for item in inputs.baseline_lanes],
            "triggers": [item.to_dict() for item in inputs.triggers],
        }
    )


def _base_rows_are_preserved(
    *,
    base_inputs: CurrentOperationRunnerInput,
    promoted_inputs: CurrentOperationRunnerInput,
) -> bool:
    if _base_lineage_hash(base_inputs) != _base_lineage_hash(promoted_inputs):
        return False

    def rows_by_id(rows: Sequence[Any], field: str) -> Mapping[str, Mapping[str, Any]]:
        return {
            str(getattr(item, field)): item.to_dict()
            for item in rows
        }

    for base_rows, promoted_rows, field in (
        (base_inputs.claims, promoted_inputs.claims, "claim_id"),
        (base_inputs.claim_provenance, promoted_inputs.claim_provenance, "claim_id"),
        (base_inputs.source_tasks, promoted_inputs.source_tasks, "task_id"),
        (base_inputs.atomic_decisions, promoted_inputs.atomic_decisions, "decision_id"),
    ):
        base_map = rows_by_id(base_rows, field)
        promoted_map = rows_by_id(promoted_rows, field)
        if any(promoted_map.get(key) != value for key, value in base_map.items()):
            return False
    return True


def _validate_stage_chain(
    *,
    as_of_date: str,
    live_root: Path,
    current_state_root: Path,
    profile: LiveRunProfile,
) -> list[Mapping[str, Any]]:
    if not profile.checkpoint_resume:
        raise ValueError("live current orchestration requires bounded checkpoint resume")
    rows: list[Mapping[str, Any]] = []
    for stage_id, leaf_paths, audit_path in _required_stage_specs(
        current_state_root=current_state_root
    ):
        resolved = tuple(
            path if path.is_absolute() else live_root / path for path in leaf_paths
        )
        missing = tuple(str(path) for path in resolved if not path.is_file())
        audit_file = audit_path if audit_path.is_absolute() else live_root / audit_path
        if missing or not audit_file.is_file():
            raise ValueError(
                f"live materialization checkpoint missing for {stage_id}: "
                f"{list(missing) or [str(audit_file)]}"
            )
        audit = _read_json(audit_file)
        audit_date = str(audit.get("as_of_date") or as_of_date)
        if audit_date != as_of_date or int(audit.get("critical_count_sum") or 0) != 0:
            raise ValueError(f"live materialization checkpoint failed for {stage_id}")
        rows.append(
            {
                "stage_id": stage_id,
                "execution_mode": "CHECKPOINT_RESUME_VALIDATED",
                "audit_path": str(audit_file),
                "audit_hash": _file_sha256(audit_file),
                "leaf_count": len(resolved),
                "leaf_tree_hash": stable_hash(
                    [
                        {"path": str(path), "sha256": _file_sha256(path)}
                        for path in resolved
                    ]
                ),
            }
        )
    return rows


def _required_stage_specs(
    *, current_state_root: Path,
) -> tuple[tuple[str, tuple[Path, ...], Path], ...]:
    return (
        ("credential_provider_preflight", (Path("universe_provenance.json"),), Path("universe_audit.json")),
        ("current_universe", (Path("universe_eligible.jsonl"),), Path("universe_audit.json")),
        (
            "current_state_bootstrap",
            (
                current_state_root / "current_state_store.jsonl",
                current_state_root / "source_timelines.jsonl",
                current_state_root / "last_effective_thesis.jsonl",
            ),
            current_state_root / "bootstrap_completeness.json",
        ),
        ("baseline_lanes", (Path("baseline_lanes.jsonl"),), Path("baseline_lane_audit.json")),
        ("trigger_fusion", (Path("trigger_signals.jsonl"), Path("candidate_events.jsonl")), Path("trigger_fusion_audit.json")),
        ("depth_selection", (Path("depth_decisions.jsonl"),), Path("candidate_selection_audit.json")),
        ("research_brain", (Path("planner_runs.jsonl"), Path("llm_prompts.jsonl"), Path("llm_responses.jsonl")), Path("planner_validation.json")),
        ("source_task", (Path("source_tasks.jsonl"), Path("question_source_tasks.jsonl")), Path("source_task_audit.json")),
        ("source_acquisition", (Path("provider_requests.jsonl"), Path("provider_fetch_results.jsonl"), Path("evidence_documents.jsonl")), Path("provider_call_report.json")),
        ("claim_compiler", (Path("source_task_satisfaction.jsonl"), Path("adjudicated_claims.jsonl")), Path("claim_compiler_audit.json")),
        ("adaptive_closure", (Path("current_claim_ledger.jsonl"), Path("gap_closure_status.jsonl")), Path("adaptive_gap_audit.json")),
        ("atomic_decision", (Path("primitive_states.jsonl"), Path("atomic_stage_decisions.jsonl")), Path("atomic_score_audit.json")),
    )


def _tree_hash(path: Path) -> str:
    if path.is_file():
        return _file_sha256(path)
    rows = [
        {
            "path": str(item.relative_to(path)),
            "sha256": _file_sha256(item),
        }
        for item in sorted(path.rglob("*"))
        if item.is_file()
    ]
    return stable_hash(rows)


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_json(path: Path) -> Mapping[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError(f"JSON object required: {path}")
    return value


__all__ = [
    "LIVE_ACCEPTANCE_PROMOTION_SCHEMA_VERSION",
    "LIVE_CURRENT_ORCHESTRATOR_SCHEMA_VERSION",
    "LiveCurrentMaterializationOrchestrator",
    "LiveCurrentOrchestrationResult",
    "write_live_acceptance_promotion",
]
