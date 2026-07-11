from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import date
from typing import Any, Mapping, Sequence

from e2r.calibration.archetype_weight_profile import CANONICAL_COMPONENT_MAX_POINTS
from e2r.models import ScoreSnapshot
from e2r.staging import StageClassificationInput, StageClassifier
from e2r.research_brain.runtime.scoring_contracts import ArchetypeScoringContract
from .component_assessment import ComponentAssessment
from .component_scorer import ResearchCalibratedScoreResult
from .impact_validator import CreditValidatedImpact


@dataclass(frozen=True)
class AtomicStageDecisionV2:
    decision_id: str; target_id: str; as_of_date: str; score_type: str
    verified_supported_score: float; provisional_score_lower: float; provisional_score_upper: float
    full_e2r_score: float | None; full_score_valid: bool
    component_assessment_ids: tuple[str,...]; claim_impact_ids: tuple[str,...]
    accepted_claim_ids: tuple[str,...]; material_nonterminal_components: tuple[str,...]
    stage_event_claim_ids: tuple[str,...]
    risk_overlay: Mapping[str,Any]; canonical_stage: str; decision_status: str
    stage_reason: tuple[str,...]; trace_id: str
    def to_dict(self)->Mapping[str,Any]: return asdict(self)


class AtomicStageCourtV2:
    def decide(self, *, target_id: str, as_of_date: str, contract: ArchetypeScoringContract, score: ResearchCalibratedScoreResult, assessments: Sequence[ComponentAssessment], impacts: Sequence[CreditValidatedImpact], accepted_claim_ids: Sequence[str], claim_eligibility_decisions: Sequence[Mapping[str,Any]] = (), risk_overlay: Mapping[str,Any] | None=None) -> AtomicStageDecisionV2:
        date.fromisoformat(as_of_date); risk=dict(risk_overlay or {})
        assessment_ids=tuple(a.assessment_id for a in assessments); impact_ids=tuple(i.impact_id for i in impacts); claim_ids=tuple(dict.fromkeys(str(v) for v in accepted_claim_ids))
        if any(i.claim_id not in claim_ids for i in impacts): raise ValueError("stage score impact lineage references an unaccepted claim")
        if set(score.component_score_vector)!={a.component_id for a in assessments}: raise ValueError("stage score component vector differs from assessments")
        hard_break=set(str(v) for v in risk.get("hard_break_claim_ids") or ()); direct_open=set(str(v) for v in risk.get("current_direct_open_counter_claim_ids") or ())
        if not hard_break<=direct_open: raise ValueError("hard break requires current direct OPEN counter claim")
        event_claim_ids=tuple(str(row.get("claim_id") or "") for row in claim_eligibility_decisions if row.get("stage_event_eligibility") is True)
        if not set(event_claim_ids)<=set(claim_ids): raise ValueError("stage event eligibility references an unaccepted claim")
        if not score.full_score_valid:
            stage="0"; reasons=("full score is pending material component assessment",); status=_pending_status(assessments)
        else:
            snapshot=_score_snapshot(target_id,as_of_date,contract,score,claim_ids,impact_ids)
            staged=StageClassifier().classify(StageClassificationInput(score=snapshot,company_event_score=60.0 if event_claim_ids else 0.0,high_quality_company_event=bool(event_claim_ids),evidence_ids=event_claim_ids))
            stage=staged.stage.value; reasons=staged.stage_reason; status="RISK_REVIEW" if hard_break else "FINAL"
        payload={"target_id":target_id,"as_of_date":as_of_date,"score_type":score.score_type,"verified_supported_score":score.verified_supported_score,"full_e2r_score":score.full_e2r_score,"component_assessment_ids":assessment_ids,"claim_impact_ids":impact_ids,"accepted_claim_ids":claim_ids,"stage_event_claim_ids":event_claim_ids,"canonical_stage":stage,"decision_status":status}
        trace="STAGEV2-"+_hash(payload)[:24]
        return AtomicStageDecisionV2("ADEC2-"+_hash({**payload,"trace_id":trace})[:24],target_id,as_of_date,score.score_type,score.verified_supported_score,score.provisional_score_lower,score.provisional_score_upper,score.full_e2r_score,score.full_score_valid,assessment_ids,impact_ids,claim_ids,score.material_nonterminal_components,event_claim_ids,risk,stage,status,tuple(reasons),trace)


def _score_snapshot(target_id: str, as_of_date: str, contract: ArchetypeScoringContract, score: ResearchCalibratedScoreResult, claim_ids: Sequence[str], impact_ids: Sequence[str]) -> ScoreSnapshot:
    raw={}
    diagnostics={"score_valid":1.0,"archetype_weight_profile_applied":1.0,"claim_backed_claim_count_capped":float(len(claim_ids)),"score_claim_backed_component_ratio":100.0,"orphan_score_component_count_capped":0.0}
    for key,value in score.component_score_vector.items():
        canonical_max=CANONICAL_COMPONENT_MAX_POINTS[key]
        calibrated_max=contract.component_max_points[key]
        raw[key]=round((float(value)/calibrated_max)*canonical_max,6) if calibrated_max else 0.0
        diagnostics[f"archetype_weight_{key}"]=calibrated_max; diagnostics[f"archetype_component_{key}"]=float(value)
    kwargs={f"{key}_score":raw[key] for key in raw}
    return ScoreSnapshot(symbol=target_id,as_of_date=date.fromisoformat(as_of_date),risk_penalty=0.0,total_score=float(score.full_e2r_score or 0.0),diagnostic_scores=diagnostics,evidence_ids=tuple(claim_ids)+tuple(impact_ids),**kwargs)


def _pending_status(assessments: Sequence[ComponentAssessment])->str:
    text=" ".join(a.status for a in assessments)
    if "PROVIDER_PENDING" in text:return "PROVIDER_PENDING"
    if "SOURCE_PENDING" in text:return "SOURCE_PENDING"
    if "BUDGET_PENDING" in text:return "BUDGET_PENDING"
    return "PENDING_MATERIAL_COMPONENTS"


def _hash(payload:Any)->str:return hashlib.sha256(json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()


__all__=["AtomicStageCourtV2","AtomicStageDecisionV2"]
