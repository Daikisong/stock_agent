"""Build deterministic current primitive states and atomic Stage decisions."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import write_json, write_jsonl
from e2r.research_brain.runtime.atomic_score_stage import (
    AtomicPrimitiveAssessment,
    AtomicPrimitiveStatus,
    AtomicScoreRule,
    AtomicScoreType,
    AtomicScoringInput,
    AtomicScoringScope,
    AtomicStageDecision,
    CanonicalStage,
    audit_atomic_stage_decisions,
    decide_atomic_score_stage,
)


@dataclass(frozen=True)
class CurrentPrimitiveState:
    target_id: str
    primitive_id: str
    state: str
    support_claim_ids: tuple[str, ...]
    counter_claim_ids: tuple[str, ...]
    material_gap_open: bool
    reason: str

    def __post_init__(self) -> None:
        if self.state not in {
            "PRESENT_CURRENT",
            "ABSENT_CURRENT",
            "UNKNOWN",
            "CONTRADICTED",
            "HISTORICAL_ONLY",
            "RESOLVED",
        }:
            raise ValueError("unknown current primitive state")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CurrentAtomicDecisionResult:
    as_of_date: str
    status: str
    primitive_states: tuple[CurrentPrimitiveState, ...]
    decisions: tuple[AtomicStageDecision, ...]
    audit: Mapping[str, Any]


class CurrentAtomicDecisionBuilder:
    def build(
        self,
        *,
        as_of_date: str,
        source_task_satisfaction: Sequence[Mapping[str, Any]],
        gap_status_rows: Sequence[Mapping[str, Any]],
        accepted_current_claims: Sequence[Mapping[str, Any]],
    ) -> CurrentAtomicDecisionResult:
        date.fromisoformat(as_of_date)
        if accepted_current_claims:
            raise ValueError(
                "live accepted claims require the claim-to-atomic adapter before scoring"
            )
        gap_by_task = {
            str(item.get("source_task_id") or ""): item for item in gap_status_rows
        }
        primitives_by_target: dict[str, list[tuple[str, str]]] = {}
        for item in source_task_satisfaction:
            target_id = str(item.get("target_id") or "")
            primitive_id = str(item.get("primitive_id") or "")
            task_id = str(item.get("source_task_id") or "")
            if not target_id or not primitive_id or task_id not in gap_by_task:
                raise ValueError("atomic input has incomplete material-gap lineage")
            primitives_by_target.setdefault(target_id, []).append((primitive_id, task_id))
        states: list[CurrentPrimitiveState] = []
        decisions: list[AtomicStageDecision] = []
        for target_id, primitive_tasks in sorted(primitives_by_target.items()):
            unique = tuple(dict.fromkeys(primitive for primitive, _ in primitive_tasks))
            if len(unique) != len(primitive_tasks):
                raise ValueError("target has duplicate primitive SourceTasks")
            points = _balanced_points(len(unique))
            rules = tuple(
                AtomicScoreRule(
                    primitive_id=primitive,
                    component_key=f"current:{primitive}",
                    max_points=point,
                    material=True,
                    green_required=True,
                )
                for primitive, point in zip(unique, points)
            )
            assessments = tuple(
                AtomicPrimitiveAssessment(
                    primitive_id=primitive,
                    status=AtomicPrimitiveStatus.MISSING.value,
                    evidence_strength=0.0,
                )
                for primitive in unique
            )
            target_gaps = tuple(gap_by_task[task_id] for _, task_id in primitive_tasks)
            provider_pending = any(
                item.get("terminal_status") == "PROVIDER_PENDING" for item in target_gaps
            )
            source_pending = any(
                item.get("terminal_status") == "SOURCE_PENDING" for item in target_gaps
            )
            decision = decide_atomic_score_stage(
                AtomicScoringInput(
                    target_id=target_id,
                    as_of_date=as_of_date,
                    scope=AtomicScoringScope.FULL_THESIS.value,
                    claims=(),
                    primitive_assessments=assessments,
                    rules=rules,
                    provider_pending=provider_pending,
                    source_pending=source_pending,
                )
            )
            decisions.append(decision)
            states.extend(
                CurrentPrimitiveState(
                    target_id=target_id,
                    primitive_id=primitive,
                    state="UNKNOWN",
                    support_claim_ids=(),
                    counter_claim_ids=(),
                    material_gap_open=True,
                    reason="no accepted current claim; deterministic score remains pending",
                )
                for primitive in unique
            )
        audit = _audit_current_atomic(states=states, decisions=decisions)
        return CurrentAtomicDecisionResult(
            as_of_date=as_of_date,
            status="CURRENT_ATOMIC_DECISION_PASS" if audit["hard_acceptance_pass"] else "CURRENT_ATOMIC_DECISION_FAIL",
            primitive_states=tuple(states),
            decisions=tuple(decisions),
            audit=audit,
        )


def write_current_atomic_decisions(
    result: CurrentAtomicDecisionResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "states": root / "primitive_states.jsonl",
        "decisions": root / "atomic_stage_decisions.jsonl",
        "audit": root / "atomic_score_audit.json",
    }
    write_jsonl(paths["states"], (item.to_dict() for item in result.primitive_states))
    write_jsonl(paths["decisions"], (item.to_dict() for item in result.decisions))
    write_json(paths["audit"], {**dict(result.audit), "status": result.status})
    return paths


def _balanced_points(count: int) -> tuple[float, ...]:
    if count <= 0:
        raise ValueError("atomic score configuration requires primitives")
    base = round(100.0 / count, 6)
    values = [base] * count
    values[-1] = round(100.0 - sum(values[:-1]), 6)
    return tuple(values)


def _audit_current_atomic(
    *,
    states: Sequence[CurrentPrimitiveState],
    decisions: Sequence[AtomicStageDecision],
) -> Mapping[str, Any]:
    canonical = audit_atomic_stage_decisions(decisions)
    critical = {
        "claimless_nonzero_score": sum(not item.claims and item.score_value not in {None, 0} for item in decisions),
        "orphan_score": sum(bool(item.contributions) and not item.accepted_claim_ids for item in decisions),
        "event_partial_as_full_score": sum(
            item.score_type == AtomicScoreType.EVENT_EVIDENCE_PARTIAL.value
            and item.score_finalization_allowed for item in decisions
        ),
        "atomic_stage_trace_mismatch": int(canonical["critical_count_sum"] > 0),
        "hard_break_without_current_direct_open": sum(
            bool(item.hard_break_claim_ids) for item in decisions
        ),
        "unexplained_score_delta": 0,
    }
    return {
        "schema_version": "e2r_live_current_atomic_score_audit_v1",
        "primitive_state_count": len(states),
        "unknown_primitive_count": sum(item.state == "UNKNOWN" for item in states),
        "atomic_decision_count": len(decisions),
        "no_score_count": sum(item.score_type == AtomicScoreType.NO_SCORE.value for item in decisions),
        "stage_zero_count": sum(item.canonical_stage == CanonicalStage.STAGE_0.value for item in decisions),
        "score_valid_true_count": sum(item.score_valid for item in decisions),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "hard_acceptance_pass": sum(critical.values()) == 0,
        "production_runtime_ready": False,
    }


__all__ = [
    "CurrentAtomicDecisionBuilder",
    "CurrentAtomicDecisionResult",
    "CurrentPrimitiveState",
    "write_current_atomic_decisions",
]
