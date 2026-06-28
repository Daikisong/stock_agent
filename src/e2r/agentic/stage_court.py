"""Stage Court v2 for Evidence OS decisions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .evidence_os import (
    BaseStage,
    EvidenceContractV2,
    PrimitiveStateV2,
    PrimitiveStatus,
    ScoreInterval,
    ScoreStatus,
    StageDecisionV2,
    StageInvestigationStatus,
    TransitionOverlay,
)


@dataclass(frozen=True)
class StageCourtInput:
    score_interval: ScoreInterval
    primitive_states: Mapping[str, PrimitiveStateV2]
    contract: EvidenceContractV2
    current_hard_break_claim_ids: tuple[str, ...] = ()
    has_prior_live_thesis: bool = False
    stage1_threshold: float = 40.0
    stage2_threshold: float = 65.0
    yellow_threshold: float = 80.0
    green_threshold: float = 90.0


@dataclass(frozen=True)
class StageCourtOutput:
    decision: StageDecisionV2
    score_status: ScoreStatus
    score_interval: ScoreInterval
    unresolved_material_gap_points: float
    material_stage_boundaries_crossed: tuple[float, ...]
    present_green_primitives: tuple[str, ...]
    missing_green_primitives: tuple[str, ...]
    reasons: tuple[str, ...] = ()


def decide_stage_court(inputs: StageCourtInput) -> StageCourtOutput:
    score_status = _score_status_for_stage_boundaries(inputs)
    present = _present_support_primitives(inputs.primitive_states)
    green_gate_primitives = inputs.contract.green_gate.primitive_ids()
    missing_green = tuple(primitive for primitive in green_gate_primitives if primitive not in present)
    green_gate_satisfied = inputs.contract.green_gate_satisfied(present)
    contradicted = tuple(
        primitive_id
        for primitive_id, state in inputs.primitive_states.items()
        if state.status == PrimitiveStatus.CONTRADICTED
    )
    reasons: list[str] = []
    if score_status == ScoreStatus.INVALID_EVIDENCE:
        reasons.append("score_status:INVALID_EVIDENCE")
    if score_status == ScoreStatus.PROVIDER_FAILURE:
        reasons.append("score_status:PROVIDER_FAILURE")
    if score_status == ScoreStatus.PENDING_MATERIAL_GAPS:
        reasons.append("score_status:PENDING_MATERIAL_GAPS")
    if contradicted:
        reasons.append("contradicted_primitives:" + ",".join(sorted(contradicted)))
    if missing_green and inputs.score_interval.verified_score >= inputs.green_threshold:
        reasons.append("green_gate_missing:" + ",".join(missing_green))
    if inputs.current_hard_break_claim_ids:
        reasons.append("current_hard_break_claims:" + ",".join(inputs.current_hard_break_claim_ids))

    decision = StageDecisionV2(
        base_stage=_base_stage(inputs, green_gate_satisfied=green_gate_satisfied),
        investigation_status=_investigation_status(
            score_status=score_status,
            has_contradiction=bool(contradicted),
            green_missing_at_green_score=bool(missing_green and inputs.score_interval.verified_score >= inputs.green_threshold),
        ),
        transition_overlay=TransitionOverlay.STAGE_4C
        if inputs.current_hard_break_claim_ids and inputs.has_prior_live_thesis
        else TransitionOverlay.NONE,
        has_prior_live_thesis=inputs.has_prior_live_thesis,
    )
    return StageCourtOutput(
        decision=decision,
        score_status=score_status,
        score_interval=inputs.score_interval,
        unresolved_material_gap_points=max(
            0.0,
            inputs.score_interval.potential_score_upper_bound - inputs.score_interval.verified_score,
        ),
        material_stage_boundaries_crossed=_material_stage_boundaries_crossed(inputs),
        present_green_primitives=tuple(primitive for primitive in green_gate_primitives if primitive in present),
        missing_green_primitives=missing_green,
        reasons=tuple(reasons),
    )


def _score_status_for_stage_boundaries(inputs: StageCourtInput) -> ScoreStatus:
    interval = inputs.score_interval
    if interval.invalid_evidence:
        return ScoreStatus.INVALID_EVIDENCE
    if interval.provider_failed:
        return ScoreStatus.PROVIDER_FAILURE
    if interval.unresolved_hard_break_candidate:
        return ScoreStatus.PENDING_MATERIAL_GAPS
    for boundary in sorted(
        {
            inputs.stage1_threshold,
            inputs.stage2_threshold,
            inputs.yellow_threshold,
            inputs.green_threshold,
        }
    ):
        if interval.verified_score < boundary <= interval.potential_score_upper_bound:
            return ScoreStatus.PENDING_MATERIAL_GAPS
    if interval.potential_score_upper_bound > interval.verified_score:
        return ScoreStatus.FINAL_WITH_NONMATERIAL_GAPS
    return ScoreStatus.FINAL


def _material_stage_boundaries_crossed(inputs: StageCourtInput) -> tuple[float, ...]:
    interval = inputs.score_interval
    return tuple(
        boundary
        for boundary in sorted(
            {
                inputs.stage1_threshold,
                inputs.stage2_threshold,
                inputs.yellow_threshold,
                inputs.green_threshold,
            }
        )
        if interval.verified_score < boundary <= interval.potential_score_upper_bound
    )


def _base_stage(inputs: StageCourtInput, *, green_gate_satisfied: bool) -> BaseStage:
    interval = inputs.score_interval
    if interval.invalid_evidence or interval.provider_failed:
        return BaseStage.STAGE_0
    score = interval.verified_score
    if inputs.current_hard_break_claim_ids and not inputs.has_prior_live_thesis:
        return BaseStage.RED
    if score >= inputs.green_threshold:
        return BaseStage.GREEN if green_gate_satisfied else BaseStage.YELLOW
    if score >= inputs.yellow_threshold:
        return BaseStage.YELLOW
    if score >= inputs.stage2_threshold:
        return BaseStage.STAGE_2
    if score >= inputs.stage1_threshold:
        return BaseStage.STAGE_1
    return BaseStage.STAGE_0


def _investigation_status(
    *,
    score_status: ScoreStatus,
    has_contradiction: bool,
    green_missing_at_green_score: bool,
) -> StageInvestigationStatus:
    if score_status in {ScoreStatus.INVALID_EVIDENCE, ScoreStatus.PROVIDER_FAILURE}:
        return StageInvestigationStatus.FAILED
    if has_contradiction:
        return StageInvestigationStatus.CONTRADICTED
    if score_status == ScoreStatus.PENDING_MATERIAL_GAPS or green_missing_at_green_score:
        return StageInvestigationStatus.PENDING
    return StageInvestigationStatus.COMPLETE


def _present_support_primitives(primitive_states: Mapping[str, PrimitiveStateV2]) -> tuple[str, ...]:
    return tuple(
        sorted(
            primitive_id
            for primitive_id, state in primitive_states.items()
            if state.status == PrimitiveStatus.PRESENT_CURRENT and bool(state.support_claim_ids)
        )
    )


__all__ = [
    "StageCourtInput",
    "StageCourtOutput",
    "decide_stage_court",
]
