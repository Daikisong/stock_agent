"""Atomic full-thesis StageCourt with separate event and risk overlays."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import date
from typing import Any, Mapping, Sequence

from e2r.calibration.archetype_weight_profile import (
    CANONICAL_COMPONENT_MAX_POINTS,
)
from e2r.models import ScoreSnapshot
from e2r.staging import StageClassificationInput, StageClassifier
from e2r.research_brain.runtime.scoring_contracts import (
    ArchetypeScoringContract,
)

from .component_assessment import (
    ComponentAssessment,
    TERMINAL_FULL_SCORE_STATUSES,
)
from .component_scorer import ResearchCalibratedScoreResult
from .impact_validator import CreditValidatedImpact


HIGH_QUALITY_EVENT_PASS = "HIGH_QUALITY_EVENT_PASS"


@dataclass(frozen=True)
class FullThesisStageInput:
    target_id: str
    as_of_date: str
    contract: ArchetypeScoringContract
    score: ResearchCalibratedScoreResult
    assessments: tuple[ComponentAssessment, ...]
    impacts: tuple[CreditValidatedImpact, ...]
    accepted_claim_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        object.__setattr__(
            self,
            "accepted_claim_ids",
            tuple(dict.fromkeys(str(value) for value in self.accepted_claim_ids)),
        )


@dataclass(frozen=True)
class EventOverlayInput:
    event_quality_contract_status: str = "NO_QUALIFYING_EVENT"
    event_claim_ids: tuple[str, ...] = ()
    event_type: str = ""
    event_rationale: str = ""
    source_evidence_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "event_claim_ids",
            tuple(dict.fromkeys(str(value) for value in self.event_claim_ids)),
        )
        object.__setattr__(
            self,
            "source_evidence_ids",
            tuple(
                dict.fromkeys(str(value) for value in self.source_evidence_ids)
            ),
        )
        if (
            self.event_quality_contract_status == HIGH_QUALITY_EVENT_PASS
            and not self.event_claim_ids
        ):
            raise ValueError(
                "high-quality event contract requires explicit event claim ids"
            )


@dataclass(frozen=True)
class RiskOverlayInput:
    hard_break_claim_ids: tuple[str, ...] = ()
    current_direct_open_counter_claim_ids: tuple[str, ...] = ()
    risk_state: str = "NO_HARD_BREAK"

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "hard_break_claim_ids",
            tuple(dict.fromkeys(str(value) for value in self.hard_break_claim_ids)),
        )
        object.__setattr__(
            self,
            "current_direct_open_counter_claim_ids",
            tuple(
                dict.fromkeys(
                    str(value)
                    for value in self.current_direct_open_counter_claim_ids
                )
            ),
        )
        if not set(self.hard_break_claim_ids) <= set(
            self.current_direct_open_counter_claim_ids
        ):
            raise ValueError(
                "hard break requires current direct OPEN counter claim"
            )

    @classmethod
    def from_mapping(cls, row: Mapping[str, Any] | None) -> "RiskOverlayInput":
        payload = dict(row or {})
        return cls(
            hard_break_claim_ids=tuple(
                payload.get("hard_break_claim_ids") or ()
            ),
            current_direct_open_counter_claim_ids=tuple(
                payload.get("current_direct_open_counter_claim_ids") or ()
            ),
            risk_state=str(payload.get("risk_state") or "NO_HARD_BREAK"),
        )

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AtomicStageDecisionV2:
    decision_id: str
    target_id: str
    as_of_date: str
    score_type: str
    verified_supported_score: float
    provisional_score_lower: float
    provisional_score_upper: float
    full_e2r_score: float | None
    full_score_valid: bool
    component_assessment_ids: tuple[str, ...]
    claim_impact_ids: tuple[str, ...]
    accepted_claim_ids: tuple[str, ...]
    material_nonterminal_components: tuple[str, ...]
    stage_event_claim_ids: tuple[str, ...]
    risk_overlay: Mapping[str, Any]
    canonical_stage: str
    full_thesis_stage: str
    decision_status: str
    stage_signal: str
    event_overlay: Mapping[str, Any]
    stage_reason: tuple[str, ...]
    trace_id: str

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


class AtomicStageCourtV2:
    def decide(
        self,
        *,
        target_id: str,
        as_of_date: str,
        contract: ArchetypeScoringContract,
        score: ResearchCalibratedScoreResult,
        assessments: Sequence[ComponentAssessment],
        impacts: Sequence[CreditValidatedImpact],
        accepted_claim_ids: Sequence[str],
        claim_eligibility_decisions: Sequence[Mapping[str, Any]] = (),
        risk_overlay: Mapping[str, Any] | None = None,
        event_overlay_input: EventOverlayInput | None = None,
        risk_overlay_input: RiskOverlayInput | None = None,
    ) -> AtomicStageDecisionV2:
        """Compatibility wrapper; canonical callers use separate inputs."""

        if event_overlay_input is None:
            explicit_event_rows = tuple(
                row
                for row in claim_eligibility_decisions
                if row.get("stage_event_eligibility") is True
                and row.get("event_quality_contract_status")
                == HIGH_QUALITY_EVENT_PASS
            )
            event_overlay_input = EventOverlayInput(
                event_quality_contract_status=(
                    HIGH_QUALITY_EVENT_PASS
                    if explicit_event_rows
                    else "NO_QUALIFYING_EVENT"
                ),
                event_claim_ids=tuple(
                    str(row.get("claim_id") or "")
                    for row in explicit_event_rows
                ),
                event_type="ELIGIBILITY_DECISION_EVENT",
                event_rationale=(
                    "Explicit event-quality contract and event eligibility passed."
                    if explicit_event_rows
                    else "No explicit event-quality contract passed."
                ),
            )
        return self.decide_full_thesis(
            full_thesis_input=FullThesisStageInput(
                target_id=target_id,
                as_of_date=as_of_date,
                contract=contract,
                score=score,
                assessments=tuple(assessments),
                impacts=tuple(impacts),
                accepted_claim_ids=tuple(accepted_claim_ids),
            ),
            event_overlay_input=event_overlay_input,
            risk_overlay_input=(
                risk_overlay_input
                if risk_overlay_input is not None
                else RiskOverlayInput.from_mapping(risk_overlay)
            ),
        )

    def decide_full_thesis(
        self,
        *,
        full_thesis_input: FullThesisStageInput,
        event_overlay_input: EventOverlayInput | None = None,
        risk_overlay_input: RiskOverlayInput | None = None,
    ) -> AtomicStageDecisionV2:
        stage_input = full_thesis_input
        event_input = event_overlay_input or EventOverlayInput()
        risk_input = risk_overlay_input or RiskOverlayInput()
        assessment_ids = tuple(
            row.assessment_id for row in stage_input.assessments
        )
        impact_ids = tuple(row.impact_id for row in stage_input.impacts)
        claim_ids = stage_input.accepted_claim_ids
        if any(row.claim_id not in claim_ids for row in stage_input.impacts):
            raise ValueError(
                "stage score impact lineage references an unaccepted claim"
            )
        if set(stage_input.score.component_score_vector) != {
            row.component_id for row in stage_input.assessments
        }:
            raise ValueError(
                "stage score component vector differs from assessments"
            )
        if not set(event_input.event_claim_ids) <= set(claim_ids):
            raise ValueError(
                "event overlay references an unaccepted claim"
            )
        event_active = (
            event_input.event_quality_contract_status
            == HIGH_QUALITY_EVENT_PASS
            and bool(event_input.event_claim_ids)
        )
        event_claim_ids = event_input.event_claim_ids if event_active else ()
        event_overlay = {
            "status": (
                "EVENT_OVERLAY_ACTIVE"
                if event_active
                else "NO_EVENT_OVERLAY"
            ),
            "stage_signal": "EVENT_WATCH" if event_active else "NO_EVENT_SIGNAL",
            "event_quality_contract_status": (
                event_input.event_quality_contract_status
            ),
            "event_claim_ids": list(event_claim_ids),
            "event_type": event_input.event_type,
            "event_rationale": event_input.event_rationale,
            "source_evidence_ids": list(event_input.source_evidence_ids),
            "canonical_stage_effect": "NONE",
        }
        hard_break = bool(risk_input.hard_break_claim_ids)
        if not stage_input.score.full_score_valid:
            stage = "0"
            validity = stage_input.score.audit.get(
                "full_score_validity", {}
            )
            blocking_reasons = tuple(
                str(value)
                for value in validity.get("blocking_reasons") or ()
            )
            reasons = (
                "full score is pending semantic validity: "
                + ", ".join(blocking_reasons),
            )
            status = _pending_status(
                stage_input.assessments,
                semantic_blocking_reasons=blocking_reasons,
            )
            stage_signal = "FULL_THESIS_PENDING"
        else:
            snapshot = _score_snapshot(
                stage_input.target_id,
                stage_input.as_of_date,
                stage_input.contract,
                stage_input.score,
                claim_ids,
                impact_ids,
            )
            staged = StageClassifier().classify(
                StageClassificationInput(
                    score=snapshot,
                    company_event_score=0.0,
                    high_quality_company_event=False,
                    evidence_ids=(),
                )
            )
            stage = staged.stage.value
            reasons = staged.stage_reason
            status = "RISK_REVIEW" if hard_break else "FINAL"
            stage_signal = (
                "RISK_REVIEW"
                if hard_break
                else f"FULL_THESIS_STAGE_{stage}"
            )
        payload = {
            "target_id": stage_input.target_id,
            "as_of_date": stage_input.as_of_date,
            "score_type": stage_input.score.score_type,
            "verified_supported_score": (
                stage_input.score.verified_supported_score
            ),
            "full_e2r_score": stage_input.score.full_e2r_score,
            "component_assessment_ids": assessment_ids,
            "claim_impact_ids": impact_ids,
            "accepted_claim_ids": claim_ids,
            "stage_event_claim_ids": event_claim_ids,
            "canonical_stage": stage,
            "full_thesis_stage": stage,
            "decision_status": status,
            "stage_signal": stage_signal,
            "event_overlay": event_overlay,
        }
        trace_id = "STAGEV2-" + _hash(payload)[:24]
        return AtomicStageDecisionV2(
            decision_id="ADEC2-"
            + _hash({**payload, "trace_id": trace_id})[:24],
            target_id=stage_input.target_id,
            as_of_date=stage_input.as_of_date,
            score_type=stage_input.score.score_type,
            verified_supported_score=(
                stage_input.score.verified_supported_score
            ),
            provisional_score_lower=(
                stage_input.score.provisional_score_lower
            ),
            provisional_score_upper=(
                stage_input.score.provisional_score_upper
            ),
            full_e2r_score=stage_input.score.full_e2r_score,
            full_score_valid=stage_input.score.full_score_valid,
            component_assessment_ids=assessment_ids,
            claim_impact_ids=impact_ids,
            accepted_claim_ids=claim_ids,
            material_nonterminal_components=(
                stage_input.score.material_nonterminal_components
            ),
            stage_event_claim_ids=event_claim_ids,
            risk_overlay=risk_input.to_dict(),
            canonical_stage=stage,
            full_thesis_stage=stage,
            decision_status=status,
            stage_signal=stage_signal,
            event_overlay=event_overlay,
            stage_reason=tuple(reasons),
            trace_id=trace_id,
        )


def _score_snapshot(
    target_id: str,
    as_of_date: str,
    contract: ArchetypeScoringContract,
    score: ResearchCalibratedScoreResult,
    claim_ids: Sequence[str],
    impact_ids: Sequence[str],
) -> ScoreSnapshot:
    raw = {}
    diagnostics = {
        "score_valid": 1.0,
        "archetype_weight_profile_applied": 1.0,
        "claim_backed_claim_count_capped": float(len(claim_ids)),
        "score_claim_backed_component_ratio": 100.0,
        "orphan_score_component_count_capped": 0.0,
    }
    for key, value in score.component_score_vector.items():
        canonical_max = CANONICAL_COMPONENT_MAX_POINTS[key]
        calibrated_max = contract.component_max_points[key]
        raw[key] = (
            round((float(value) / calibrated_max) * canonical_max, 6)
            if calibrated_max
            else 0.0
        )
        diagnostics[f"archetype_weight_{key}"] = calibrated_max
        diagnostics[f"archetype_component_{key}"] = float(value)
    kwargs = {f"{key}_score": raw[key] for key in raw}
    return ScoreSnapshot(
        symbol=target_id,
        as_of_date=date.fromisoformat(as_of_date),
        risk_penalty=0.0,
        total_score=float(score.full_e2r_score or 0.0),
        diagnostic_scores=diagnostics,
        evidence_ids=tuple(claim_ids) + tuple(impact_ids),
        **kwargs,
    )


def _pending_status(
    assessments: Sequence[ComponentAssessment],
    *,
    semantic_blocking_reasons: Sequence[str] = (),
) -> str:
    text = " ".join(row.status for row in assessments)
    if "PROVIDER_PENDING" in text:
        return "PROVIDER_PENDING"
    if "SOURCE_PENDING" in text:
        return "SOURCE_PENDING"
    if "BUDGET_PENDING" in text:
        return "BUDGET_PENDING"
    if any(
        row.status not in TERMINAL_FULL_SCORE_STATUSES
        for row in assessments
    ):
        return "PENDING_MATERIAL_COMPONENTS"
    if semantic_blocking_reasons:
        return "SEMANTIC_VALIDITY_PENDING"
    return "PENDING_MATERIAL_COMPONENTS"


def _hash(payload: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            default=str,
        ).encode()
    ).hexdigest()


__all__ = [
    "AtomicStageCourtV2",
    "AtomicStageDecisionV2",
    "EventOverlayInput",
    "FullThesisStageInput",
    "RiskOverlayInput",
]
