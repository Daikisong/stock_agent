"""AtomicStageCourtV2 bridge with explicit event and OPEN risk overlays."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from e2r.research_brain.researcher_mode.schemas import EvidenceFact
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)
from e2r.research_brain.scoring import (
    AtomicStageCourtV2,
    AtomicStageDecisionV2,
    EventOverlayInput,
    FullThesisStageInput,
    RiskOverlayInput,
)

from .scorer_bridge import CalibratedScoreBridgeResult


@dataclass(frozen=True)
class StageCourtBridgeResult:
    decision: AtomicStageDecisionV2
    ignored_proposed_stage: str | None

    @property
    def receipt_payload(self) -> Mapping[str, Any]:
        return {
            "schema_version": "e2r_pro_atomic_stagecourt_bridge_receipt_v1",
            "status": "ATOMIC_STAGECOURT_COMPLETE",
            "decision": self.decision.to_dict(),
            "stagecourt_class": "AtomicStageCourtV2",
            "ignored_proposed_stage": self.ignored_proposed_stage,
            "pro_stage_ignored": True,
            "new_stage_engine_count": 0,
            "production_score_authority": False,
            "production_stage_authority": True,
        }


class ProAtomicStageCourtBridge:
    def decide(
        self,
        *,
        target_id: str,
        as_of_date: str,
        selected_archetype_id: str,
        score_result: CalibratedScoreBridgeResult,
        accepted_claim_ids: Sequence[str],
        evidence_facts: Sequence[EvidenceFact],
        event_overlay_input: EventOverlayInput | None = None,
        hard_break_claim_ids: Sequence[str] = (),
        ignored_proposed_stage: str | None = None,
    ) -> StageCourtBridgeResult:
        if score_result.score is None or not score_result.assessments:
            raise ValueError("StageCourt requires a deterministic calibrated score result")
        accepted = tuple(dict.fromkeys(str(value) for value in accepted_claim_ids))
        counter_open_claims = tuple(
            dict.fromkeys(
                claim_id
                for fact in evidence_facts
                if fact.direction == "COUNTER" and fact.current_lifecycle == "OPEN"
                for claim_id in fact.claim_ids
            )
        )
        hard_breaks = tuple(dict.fromkeys(str(value) for value in hard_break_claim_ids))
        if not set(hard_breaks).issubset(counter_open_claims):
            raise ValueError("hard break must reference current direct OPEN counter claims")
        contract = load_archetype_scoring_contract(selected_archetype_id)
        decision = AtomicStageCourtV2().decide_full_thesis(
            full_thesis_input=FullThesisStageInput(
                target_id=target_id,
                as_of_date=as_of_date,
                contract=contract,
                score=score_result.score,
                assessments=score_result.assessments,
                impacts=score_result.impacts,
                accepted_claim_ids=accepted,
            ),
            event_overlay_input=event_overlay_input or EventOverlayInput(),
            risk_overlay_input=RiskOverlayInput(
                hard_break_claim_ids=hard_breaks,
                current_direct_open_counter_claim_ids=counter_open_claims,
                risk_state="HARD_BREAK_REVIEW" if hard_breaks else "NO_HARD_BREAK",
            ),
        )
        return StageCourtBridgeResult(
            decision=decision,
            ignored_proposed_stage=ignored_proposed_stage,
        )


__all__ = ["ProAtomicStageCourtBridge", "StageCourtBridgeResult"]
