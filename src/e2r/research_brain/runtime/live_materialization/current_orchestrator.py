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
import os
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.env import load_project_env
from e2r.production.metadata import stable_hash, write_json
from e2r.research_brain.runtime.current_operation_runner import (
    CurrentOperationRunnerInput,
    load_current_operation_runner_input,
)

from .current_operation_input_builder import (
    CurrentOperationRunnerInputBuilder,
    write_current_operation_input_manifest,
)
from .baseline_materializer import (
    BaselineLane,
    BaselineMaterializerConfig,
    CurrentBaselineMaterializer,
    load_baseline_lanes,
    write_baseline_materialization,
)
from .current_state_store import (
    CurrentStateBootstrapper,
    load_current_state_store,
    write_current_state_bootstrap,
)
from .depth_selector import (
    CurrentDepthSelector,
    DepthSelectionConfig,
    load_depth_decisions,
    write_depth_selection,
)
from .schemas import LiveRunProfile, load_live_run_profile
from .trigger_fusion import (
    CurrentTriggerFusion,
    TriggerFusionConfig,
    load_candidate_events,
    load_trigger_signals,
    write_trigger_fusion,
)
from .universe_materializer import (
    CurrentKrxUniverseMaterializer,
    UniverseMaterializerConfig,
    load_universe_rows,
    write_universe_materialization,
)


LIVE_CURRENT_ORCHESTRATOR_SCHEMA_VERSION = "e2r_live_current_orchestrator_v1"
LIVE_ACCEPTANCE_PROMOTION_SCHEMA_VERSION = "e2r_live_acceptance_promotion_v1"


@dataclass(frozen=True)
class LiveCurrentOrchestrationResult:
    inputs: CurrentOperationRunnerInput
    builder_audit: Mapping[str, Any]
    orchestration_audit: Mapping[str, Any]
    input_paths: Mapping[str, Path]


class LiveMaterializationPendingError(RuntimeError):
    """A resumable live boundary, with machine-readable blocker context."""

    def __init__(
        self,
        *,
        blocker_codes: Sequence[str],
        pending_stage_id: str,
        audit_path: Path,
        detail: str,
    ) -> None:
        self.blocker_codes = tuple(dict.fromkeys(str(item) for item in blocker_codes))
        self.pending_stage_id = pending_stage_id
        self.audit_path = audit_path
        self.detail = detail
        super().__init__(f"{pending_stage_id}: {detail}")


class LiveCurrentMaterializationOrchestrator:
    """Materialize missing pre-deep stages, then resume validated deep stages."""

    def __init__(
        self,
        *,
        universe_materializer: CurrentKrxUniverseMaterializer | None = None,
        baseline_materializer: CurrentBaselineMaterializer | None = None,
        env_file: str | Path | None = ".env",
        environment: Mapping[str, str] | None = None,
        test_mode: bool = False,
    ) -> None:
        self.universe_materializer = (
            universe_materializer or CurrentKrxUniverseMaterializer()
        )
        self.baseline_materializer = (
            baseline_materializer or CurrentBaselineMaterializer()
        )
        self.env_file = env_file
        self.environment = environment
        self.test_mode = test_mode

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
        if not profile.checkpoint_resume:
            raise ValueError("live current orchestration requires bounded checkpoint resume")
        root.mkdir(parents=True, exist_ok=True)
        state_root.mkdir(parents=True, exist_ok=True)
        if self.environment is None:
            load_project_env(self.env_file, override=False)
        environment = os.environ if self.environment is None else self.environment
        stage_rows, changed, provider_blockers = self._ensure_pre_deep_chain(
            as_of_date=as_of_date,
            live_root=root,
            current_state_root=state_root,
            profile=profile,
            environment=environment,
        )
        downstream_rows, pending = _validate_downstream_stage_chain(
            as_of_date=as_of_date,
            live_root=root,
            current_state_root=state_root,
            profile=profile,
            pre_deep_changed=changed,
        )
        stage_rows.extend(downstream_rows)
        if pending is not None:
            pending_stage, pending_reason = pending
            blockers = tuple(
                dict.fromkeys(
                    (*provider_blockers, "VALIDATED_DOWNSTREAM_CHECKPOINT_PENDING")
                )
            )
            audit_path = root / "current_orchestration_audit.json"
            audit = _pending_orchestration_audit(
                as_of_date=as_of_date,
                profile=profile,
                stage_rows=stage_rows,
                pending_stage_id=pending_stage,
                pending_reason=pending_reason,
                blocker_codes=blockers,
            )
            write_json(audit_path, audit)
            raise LiveMaterializationPendingError(
                blocker_codes=blockers,
                pending_stage_id=pending_stage,
                audit_path=audit_path,
                detail=pending_reason,
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

    def _ensure_pre_deep_chain(
        self,
        *,
        as_of_date: str,
        live_root: Path,
        current_state_root: Path,
        profile: LiveRunProfile,
        environment: Mapping[str, str],
    ) -> tuple[list[Mapping[str, Any]], bool, tuple[str, ...]]:
        rows: list[Mapping[str, Any]] = []
        changed = False
        provider_blockers: list[str] = []

        universe_valid, universe_reason = _validate_pre_deep_stage(
            stage_id="current_universe",
            as_of_date=as_of_date,
            live_root=live_root,
            current_state_root=current_state_root,
        )
        if universe_valid:
            universe = load_universe_rows(live_root / "universe_eligible.jsonl")
            rows.extend(
                _checkpoint_rows(
                    ("credential_provider_preflight", "current_universe"),
                    live_root=live_root,
                    current_state_root=current_state_root,
                )
            )
        else:
            result = self.universe_materializer.materialize(
                UniverseMaterializerConfig(
                    as_of_date=as_of_date,
                    excluded_instrument_types=tuple(
                        profile.universe_policy.get("exclude_instrument_types")
                        or UniverseMaterializerConfig(as_of_date=as_of_date).excluded_instrument_types
                    ),
                    test_mode=self.test_mode,
                ),
                credential=str(environment.get("KRX_OPENAPI_KEY") or "") or None,
                env_file=None,
            )
            write_universe_materialization(result, output_root=live_root)
            if not result.audit.get("hard_acceptance_pass"):
                blockers = tuple(result.blockers) or tuple(result.audit.get("blockers") or ())
                self._raise_stage_pending(
                    as_of_date=as_of_date,
                    profile=profile,
                    stage_rows=rows,
                    stage_id="current_universe",
                    reason=universe_reason,
                    blockers=blockers or ("CURRENT_UNIVERSE_MATERIALIZATION_PENDING",),
                    live_root=live_root,
                )
            universe = result.eligible_rows
            changed = True
            rows.extend(
                _materialized_rows(
                    ("credential_provider_preflight", "current_universe"),
                    live_root=live_root,
                    current_state_root=current_state_root,
                )
            )

        state_valid, _ = _validate_pre_deep_stage(
            stage_id="current_state_bootstrap",
            as_of_date=as_of_date,
            live_root=live_root,
            current_state_root=current_state_root,
        )
        if state_valid and not changed:
            current_state = load_current_state_store(
                current_state_root / "current_state_store.jsonl"
            )
            rows.extend(
                _checkpoint_rows(
                    ("current_state_bootstrap",),
                    live_root=live_root,
                    current_state_root=current_state_root,
                )
            )
        else:
            prior_state = _load_latest_prior_state(
                current_state_root=current_state_root,
                as_of_date=as_of_date,
            )
            bootstrap = CurrentStateBootstrapper().bootstrap(
                as_of_date=as_of_date,
                universe=universe,
                prior_records=prior_state,
            )
            write_current_state_bootstrap(bootstrap, output_root=current_state_root)
            current_state = bootstrap.records
            changed = True
            rows.extend(
                _materialized_rows(
                    ("current_state_bootstrap",),
                    live_root=live_root,
                    current_state_root=current_state_root,
                )
            )

        baseline_valid, _ = _validate_pre_deep_stage(
            stage_id="baseline_lanes",
            as_of_date=as_of_date,
            live_root=live_root,
            current_state_root=current_state_root,
        )
        if baseline_valid and not changed:
            baseline_lanes = load_baseline_lanes(live_root / "baseline_lanes.jsonl")
            rows.extend(
                _checkpoint_rows(
                    ("baseline_lanes",),
                    live_root=live_root,
                    current_state_root=current_state_root,
                )
            )
        else:
            effective_dates = {item.source_effective_date for item in universe}
            if len(effective_dates) != 1:
                self._raise_stage_pending(
                    as_of_date=as_of_date,
                    profile=profile,
                    stage_rows=rows,
                    stage_id="baseline_lanes",
                    reason="universe has no single latest trading snapshot",
                    blockers=("INVALID_UNIVERSE_EFFECTIVE_DATE",),
                    live_root=live_root,
                )
            latest_trading_date = next(iter(effective_dates))
            baseline = self.baseline_materializer.materialize(
                BaselineMaterializerConfig(
                    as_of_date=as_of_date,
                    price_effective_date=latest_trading_date,
                    dart_index_start_date=latest_trading_date,
                    dart_page_count=100,
                    dart_max_pages=min(
                        20, max(1, int(profile.budgets["max_fetches_per_candidate"]))
                    ),
                    test_mode=self.test_mode,
                ),
                universe=universe,
                prior_state=current_state,
                krx_credential=str(environment.get("KRX_OPENAPI_KEY") or "") or None,
                opendart_credential=(
                    str(
                        environment.get("OPENDART_API_KEY")
                        or environment.get("OPEN_DART_API_KEY")
                        or ""
                    )
                    or None
                ),
                env_file=None,
                load_environment=False,
            )
            write_baseline_materialization(baseline, output_root=live_root)
            baseline_lanes = baseline.lanes
            changed = True
            rows.extend(
                _materialized_rows(
                    ("baseline_lanes",),
                    live_root=live_root,
                    current_state_root=current_state_root,
                )
            )
        provider_blockers.extend(_baseline_provider_blockers(baseline_lanes))

        trigger_valid, _ = _validate_pre_deep_stage(
            stage_id="trigger_fusion",
            as_of_date=as_of_date,
            live_root=live_root,
            current_state_root=current_state_root,
        )
        if trigger_valid and not changed:
            trigger_signals = load_trigger_signals(live_root / "trigger_signals.jsonl")
            candidate_events = load_candidate_events(live_root / "candidate_events.jsonl")
            rows.extend(
                _checkpoint_rows(
                    ("trigger_fusion",),
                    live_root=live_root,
                    current_state_root=current_state_root,
                )
            )
        else:
            fused = CurrentTriggerFusion().fuse(
                TriggerFusionConfig(as_of_date=as_of_date, test_mode=self.test_mode),
                universe=universe,
                baseline_lanes=baseline_lanes,
                current_state=current_state,
            )
            write_trigger_fusion(fused, output_root=live_root)
            trigger_signals = fused.trigger_signals
            candidate_events = fused.candidate_events
            changed = True
            rows.extend(
                _materialized_rows(
                    ("trigger_fusion",),
                    live_root=live_root,
                    current_state_root=current_state_root,
                )
            )

        depth_valid, _ = _validate_pre_deep_stage(
            stage_id="depth_selection",
            as_of_date=as_of_date,
            live_root=live_root,
            current_state_root=current_state_root,
        )
        if depth_valid and not changed:
            rows.extend(
                _checkpoint_rows(
                    ("depth_selection",),
                    live_root=live_root,
                    current_state_root=current_state_root,
                )
            )
        else:
            selected = CurrentDepthSelector().select(
                DepthSelectionConfig.from_run_profile(
                    as_of_date=as_of_date,
                    profile=profile,
                    test_mode=self.test_mode,
                ),
                universe=universe,
                baseline_lanes=baseline_lanes,
                candidate_events=candidate_events,
                trigger_signals=trigger_signals,
            )
            write_depth_selection(selected, output_root=live_root)
            changed = True
            rows.extend(
                _materialized_rows(
                    ("depth_selection",),
                    live_root=live_root,
                    current_state_root=current_state_root,
                )
            )
        return rows, changed, tuple(sorted(set(provider_blockers)))

    @staticmethod
    def _raise_stage_pending(
        *,
        as_of_date: str,
        profile: LiveRunProfile,
        stage_rows: Sequence[Mapping[str, Any]],
        stage_id: str,
        reason: str,
        blockers: Sequence[str],
        live_root: Path,
    ) -> None:
        audit_path = live_root / "current_orchestration_audit.json"
        write_json(
            audit_path,
            _pending_orchestration_audit(
                as_of_date=as_of_date,
                profile=profile,
                stage_rows=stage_rows,
                pending_stage_id=stage_id,
                pending_reason=reason,
                blocker_codes=blockers,
            ),
        )
        raise LiveMaterializationPendingError(
            blocker_codes=blockers,
            pending_stage_id=stage_id,
            audit_path=audit_path,
            detail=reason,
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


def _pending_orchestration_audit(
    *,
    as_of_date: str,
    profile: LiveRunProfile,
    stage_rows: Sequence[Mapping[str, Any]],
    pending_stage_id: str,
    pending_reason: str,
    blocker_codes: Sequence[str],
) -> Mapping[str, Any]:
    return {
        "schema_version": LIVE_CURRENT_ORCHESTRATOR_SCHEMA_VERSION,
        "status": "LIVE_PRE_DEEP_MATERIALIZED_DOWNSTREAM_PENDING",
        "as_of_date": as_of_date,
        "run_mode": profile.run_mode,
        "execution_mode": "STAGE_RESUMABLE_PRE_DEEP_MATERIALIZATION",
        "materializer_called": True,
        "manifest_self_generated": False,
        "stage_count": len(stage_rows),
        "stages": list(stage_rows),
        "pending_stage_id": pending_stage_id,
        "pending_reason": pending_reason,
        "blockers": list(dict.fromkeys(str(item) for item in blocker_codes)),
        "score_valid": False,
        "canonical_stage": "0",
        "critical_counts": {"validated_downstream_checkpoint_pending": 1},
        "critical_count_sum": 1,
        "hard_acceptance_pass": False,
    }


def _validate_pre_deep_stage(
    *,
    stage_id: str,
    as_of_date: str,
    live_root: Path,
    current_state_root: Path,
) -> tuple[bool, str]:
    specs = {
        item[0]: item
        for item in _required_stage_specs(current_state_root=current_state_root)
    }
    if stage_id not in specs:
        return False, f"unknown pre-deep stage {stage_id}"
    _, leaf_paths, audit_path = specs[stage_id]
    resolved = tuple(
        path if path.is_absolute() else live_root / path for path in leaf_paths
    )
    audit_file = audit_path if audit_path.is_absolute() else live_root / audit_path
    missing = tuple(path for path in (*resolved, audit_file) if not path.is_file())
    if missing:
        return False, "missing checkpoint leaves: " + ", ".join(str(path) for path in missing)
    try:
        audit = _read_json(audit_file)
        if str(audit.get("as_of_date") or "") != as_of_date:
            return False, "checkpoint as_of_date mismatch"
        if (
            int(audit.get("critical_count_sum") or 0) != 0
            or audit.get("hard_acceptance_pass") is not True
        ):
            return False, "checkpoint audit is not a hard acceptance pass"
        as_of = date.fromisoformat(as_of_date)
        if stage_id == "current_universe":
            rows = load_universe_rows(resolved[0])
            if not rows or any(not row.eligible for row in rows):
                return False, "eligible universe leaf is empty or contains excluded rows"
            if any(date.fromisoformat(row.source_effective_date) > as_of for row in rows):
                return False, "future universe row detected"
            if int(audit.get("eligible_universe_count") or -1) != len(rows):
                return False, "universe audit count does not match leaf"
        elif stage_id == "current_state_bootstrap":
            records = load_current_state_store(resolved[0])
            if not records or any(record.as_of_date != as_of_date for record in records):
                return False, "current-state leaf is empty or date-mismatched"
        elif stage_id == "baseline_lanes":
            lanes = load_baseline_lanes(resolved[0])
            if not lanes or any(lane.observed_date != as_of_date for lane in lanes):
                return False, "baseline leaf is empty or date-mismatched"
            by_target: dict[str, set[str]] = {}
            for lane in lanes:
                by_target.setdefault(lane.target_id, set()).add(lane.lane)
            required = {item.value for item in BaselineLane}
            if any(values != required for values in by_target.values()):
                return False, "baseline four-lane coverage is incomplete"
        elif stage_id == "trigger_fusion":
            signals = load_trigger_signals(resolved[0])
            candidates = load_candidate_events(resolved[1])
            if any(
                date.fromisoformat(item.effective_date) > as_of
                or date.fromisoformat(item.detected_at) > as_of
                for item in signals
            ):
                return False, "future trigger signal detected"
            if any(item.as_of_date != as_of_date for item in candidates):
                return False, "candidate event date mismatch"
        elif stage_id == "depth_selection":
            decisions = load_depth_decisions(resolved[0])
            if not decisions or any(item.as_of_date != as_of_date for item in decisions):
                return False, "depth decision leaf is empty or date-mismatched"
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        return False, f"checkpoint semantic validation failed: {type(exc).__name__}: {exc}"
    return True, "validated"


def _validate_downstream_stage_chain(
    *,
    as_of_date: str,
    live_root: Path,
    current_state_root: Path,
    profile: LiveRunProfile,
    pre_deep_changed: bool,
) -> tuple[list[Mapping[str, Any]], tuple[str, str] | None]:
    if not profile.checkpoint_resume:
        raise ValueError("live current orchestration requires bounded checkpoint resume")
    downstream = _required_stage_specs(current_state_root=current_state_root)[6:]
    if pre_deep_changed:
        return [], (
            downstream[0][0],
            "pre-deep lineage changed; planner/source checkpoints must be regenerated",
        )
    rows: list[Mapping[str, Any]] = []
    for stage_id, _, _ in downstream:
        valid, reason = _validate_stage_checkpoint_basic(
            stage_id=stage_id,
            as_of_date=as_of_date,
            live_root=live_root,
            current_state_root=current_state_root,
        )
        if not valid:
            return rows, (stage_id, reason)
        rows.extend(
            _checkpoint_rows(
                (stage_id,),
                live_root=live_root,
                current_state_root=current_state_root,
            )
        )
    return rows, None


def _validate_stage_checkpoint_basic(
    *,
    stage_id: str,
    as_of_date: str,
    live_root: Path,
    current_state_root: Path,
) -> tuple[bool, str]:
    specs = {
        item[0]: item
        for item in _required_stage_specs(current_state_root=current_state_root)
    }
    _, leaf_paths, audit_path = specs[stage_id]
    resolved = tuple(
        path if path.is_absolute() else live_root / path for path in leaf_paths
    )
    audit_file = audit_path if audit_path.is_absolute() else live_root / audit_path
    missing = tuple(path for path in (*resolved, audit_file) if not path.is_file())
    if missing:
        return False, "missing checkpoint leaves: " + ", ".join(str(path) for path in missing)
    try:
        audit = _read_json(audit_file)
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        return False, f"invalid checkpoint audit: {type(exc).__name__}: {exc}"
    audit_date = str(audit.get("as_of_date") or as_of_date)
    if audit_date != as_of_date:
        return False, "checkpoint as_of_date mismatch"
    if int(audit.get("critical_count_sum") or 0) != 0:
        return False, "checkpoint audit contains critical failures"
    return True, "validated"


def _stage_row(
    *,
    stage_id: str,
    execution_mode: str,
    live_root: Path,
    current_state_root: Path,
) -> Mapping[str, Any]:
    specs = {
        item[0]: item
        for item in _required_stage_specs(current_state_root=current_state_root)
    }
    _, leaf_paths, audit_path = specs[stage_id]
    resolved = tuple(
        path if path.is_absolute() else live_root / path for path in leaf_paths
    )
    audit_file = audit_path if audit_path.is_absolute() else live_root / audit_path
    return {
        "stage_id": stage_id,
        "execution_mode": execution_mode,
        "audit_path": str(audit_file),
        "audit_hash": _file_sha256(audit_file),
        "leaf_count": len(resolved),
        "leaf_tree_hash": stable_hash(
            [{"path": str(path), "sha256": _file_sha256(path)} for path in resolved]
        ),
    }


def _checkpoint_rows(
    stage_ids: Sequence[str],
    *,
    live_root: Path,
    current_state_root: Path,
) -> list[Mapping[str, Any]]:
    return [
        _stage_row(
            stage_id=stage_id,
            execution_mode="CHECKPOINT_RESUME_VALIDATED",
            live_root=live_root,
            current_state_root=current_state_root,
        )
        for stage_id in stage_ids
    ]


def _materialized_rows(
    stage_ids: Sequence[str],
    *,
    live_root: Path,
    current_state_root: Path,
) -> list[Mapping[str, Any]]:
    return [
        _stage_row(
            stage_id=stage_id,
            execution_mode="MISSING_OR_INVALID_CHECKPOINT_MATERIALIZED",
            live_root=live_root,
            current_state_root=current_state_root,
        )
        for stage_id in stage_ids
    ]


def _load_latest_prior_state(
    *,
    current_state_root: Path,
    as_of_date: str,
) -> tuple[Any, ...]:
    as_of = date.fromisoformat(as_of_date)
    candidates: list[tuple[date, Path]] = []
    for child in current_state_root.parent.iterdir():
        try:
            effective = date.fromisoformat(child.name)
        except ValueError:
            continue
        leaf = child / "current_state_store.jsonl"
        if effective < as_of and leaf.is_file():
            candidates.append((effective, leaf))
    for effective, leaf in sorted(candidates, reverse=True):
        try:
            records = load_current_state_store(leaf)
        except (OSError, TypeError, ValueError, json.JSONDecodeError):
            continue
        if records and all(date.fromisoformat(item.as_of_date) == effective for item in records):
            return records
    return ()


def _baseline_provider_blockers(lanes: Sequence[Any]) -> tuple[str, ...]:
    return tuple(
        sorted(
            {
                str(lane.provider_error_category)
                for lane in lanes
                if lane.provider_error_category
            }
        )
    )


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
    "LiveMaterializationPendingError",
    "write_live_acceptance_promotion",
]
