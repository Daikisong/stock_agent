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
    AtomicScoreClaim,
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
    claims: tuple[AtomicScoreClaim, ...]
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
        claim_provenance: Sequence[Mapping[str, Any]] = (),
    ) -> CurrentAtomicDecisionResult:
        date.fromisoformat(as_of_date)
        gap_by_task = {
            str(item.get("source_task_id") or ""): item for item in gap_status_rows
        }
        primitives_by_target: dict[str, dict[str, list[Mapping[str, Any]]]] = {}
        for item in source_task_satisfaction:
            target_id = str(item.get("target_id") or "")
            primitive_id = str(item.get("primitive_id") or "")
            task_id = str(item.get("source_task_id") or "")
            if not target_id or not primitive_id or not task_id:
                raise ValueError("atomic input has incomplete material-gap lineage")
            primitives_by_target.setdefault(target_id, {}).setdefault(
                primitive_id, []
            ).append(item)
        claims = _adapt_direct_current_claims(
            accepted_current_claims=accepted_current_claims,
            claim_provenance=claim_provenance,
            source_task_satisfaction=source_task_satisfaction,
            as_of_date=as_of_date,
        )
        claims_by_target_primitive: dict[tuple[str, str], list[AtomicScoreClaim]] = {}
        for claim in claims:
            claims_by_target_primitive.setdefault(
                (claim.target_id, claim.primitive_id), []
            ).append(claim)
        states: list[CurrentPrimitiveState] = []
        decisions: list[AtomicStageDecision] = []
        for target_id, primitive_rows in sorted(primitives_by_target.items()):
            unique = tuple(primitive_rows)
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
            assessments: list[AtomicPrimitiveAssessment] = []
            for primitive in unique:
                support = tuple(
                    item.claim_id
                    for item in claims_by_target_primitive.get(
                        (target_id, primitive), ()
                    )
                )
                assessments.append(
                    AtomicPrimitiveAssessment(
                        primitive_id=primitive,
                        status=(
                            AtomicPrimitiveStatus.SATISFIED.value
                            if support
                            else AtomicPrimitiveStatus.MISSING.value
                        ),
                        evidence_strength=1.0 if support else 0.0,
                        support_claim_ids=support,
                    )
                )
            target_task_ids = {
                str(row.get("source_task_id") or "")
                for rows in primitive_rows.values()
                for row in rows
            }
            target_gaps = tuple(
                gap_by_task[task_id]
                for task_id in target_task_ids
                if task_id in gap_by_task
            )
            provider_pending = any(
                item.get("terminal_status") == "PROVIDER_PENDING" for item in target_gaps
            )
            source_pending = bool(
                any(item.status == AtomicPrimitiveStatus.MISSING.value for item in assessments)
                or any(
                    item.get("terminal_status") == "SOURCE_PENDING"
                    for item in target_gaps
                )
            )
            target_claims = tuple(item for item in claims if item.target_id == target_id)
            decision = decide_atomic_score_stage(
                AtomicScoringInput(
                    target_id=target_id,
                    as_of_date=as_of_date,
                    scope=AtomicScoringScope.FULL_THESIS.value,
                    claims=target_claims,
                    primitive_assessments=tuple(assessments),
                    rules=rules,
                    provider_pending=provider_pending,
                    source_pending=source_pending,
                )
            )
            decisions.append(decision)
            for assessment in assessments:
                present = assessment.status == AtomicPrimitiveStatus.SATISFIED.value
                states.append(
                    CurrentPrimitiveState(
                        target_id=target_id,
                        primitive_id=assessment.primitive_id,
                        state="PRESENT_CURRENT" if present else "UNKNOWN",
                        support_claim_ids=assessment.support_claim_ids,
                        counter_claim_ids=(),
                        material_gap_open=not present,
                        reason=(
                            "direct current claim and provenance satisfy the primitive"
                            if present
                            else "no accepted current claim; deterministic score remains pending"
                        ),
                    )
                )
        audit = _audit_current_atomic(states=states, decisions=decisions)
        return CurrentAtomicDecisionResult(
            as_of_date=as_of_date,
            status="CURRENT_ATOMIC_DECISION_PASS" if audit["hard_acceptance_pass"] else "CURRENT_ATOMIC_DECISION_FAIL",
            primitive_states=tuple(states),
            claims=claims,
            decisions=tuple(decisions),
            audit=audit,
        )


def _adapt_direct_current_claims(
    *,
    accepted_current_claims: Sequence[Mapping[str, Any]],
    claim_provenance: Sequence[Mapping[str, Any]],
    source_task_satisfaction: Sequence[Mapping[str, Any]],
    as_of_date: str,
) -> tuple[AtomicScoreClaim, ...]:
    """Promote only direct task closures with exact live provenance to atomic claims."""

    provenance_by_claim = {
        str(item.get("claim_id") or ""): item for item in claim_provenance
    }
    if len(provenance_by_claim) != len(claim_provenance):
        raise ValueError("duplicate or empty current claim provenance")
    closure_by_claim: dict[str, tuple[str, str, tuple[str, ...]]] = {}
    for item in source_task_satisfaction:
        if (
            item.get("status") != "DIRECT_TASK_SATISFIED"
            or item.get("original_gap_open") is not False
        ):
            continue
        target_id = str(item.get("target_id") or "")
        primitive_id = str(item.get("primitive_id") or "")
        mapping_ids = tuple(str(value) for value in item.get("accepted_mapping_ids") or ())
        for claim_id in item.get("accepted_claim_ids") or ():
            key = str(claim_id)
            value = (target_id, primitive_id, mapping_ids)
            if key in closure_by_claim and closure_by_claim[key] != value:
                raise ValueError("current claim closes multiple direct primitives")
            closure_by_claim[key] = value

    adapted: list[AtomicScoreClaim] = []
    for row in accepted_current_claims:
        claim_id = str(row.get("claim_id") or "")
        closure = closure_by_claim.get(claim_id)
        if closure is None:
            continue
        target_id, primitive_id, closure_mapping_ids = closure
        provenance = provenance_by_claim.get(claim_id)
        if provenance is None:
            raise ValueError("direct accepted current claim lacks provenance")
        row_mapping_ids = tuple(str(value) for value in row.get("mapping_ids") or ())
        provenance_mapping_ids = tuple(
            str(value) for value in provenance.get("mapping_ids") or ()
        )
        mapping_ids = tuple(
            value
            for value in closure_mapping_ids
            if value in row_mapping_ids and value in provenance_mapping_ids
        )
        available_date = str(provenance.get("available_date") or "")
        if (
            str(row.get("target_id") or row.get("target_entity_id") or "")
            != target_id
            or str(provenance.get("target_id") or "") != target_id
            or row.get("accepted") is not True
            or row.get("directness") != "DIRECT"
            or row.get("temporal_status") != "CURRENT"
            or row.get("semantic_status") != "PASS"
            or provenance.get("directness") != "DIRECT"
            or provenance.get("temporal_status") != "CURRENT"
            or provenance.get("mapping_status") != "ACCEPTED"
            or provenance.get("fetched") is not True
            or provenance.get("anchor_verified") is not True
            or provenance.get("source_proxy_only") is not False
            or not mapping_ids
            or not available_date
            or available_date > as_of_date
        ):
            raise ValueError("direct accepted current claim violates atomic bridge contract")
        adapted.append(
            AtomicScoreClaim(
                claim_id=claim_id,
                target_id=target_id,
                primitive_id=primitive_id,
                observed_date=available_date,
                content_hash=str(provenance.get("content_sha256") or ""),
                source_ids=tuple(str(value) for value in provenance.get("source_ids") or ()),
                anchor_ids=tuple(str(value) for value in provenance.get("anchor_ids") or ()),
                mapping_ids=mapping_ids,
                polarity="SUPPORT",
                target_direct=True,
                current_open=True,
                source_backed=True,
                material=True,
                contradiction_resolved=True,
                historical_replay=False,
                mapping_accepted=True,
                score_eligible=True,
            )
        )
    return tuple(adapted)


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
