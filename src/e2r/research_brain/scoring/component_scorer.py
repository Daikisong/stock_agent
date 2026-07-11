from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping, Sequence

from e2r.research_brain.runtime.scoring_contracts import ArchetypeScoringContract
from .component_assessment import ComponentAssessment, TERMINAL_FULL_SCORE_STATUSES
from .impact_validator import CreditValidatedImpact


@dataclass(frozen=True)
class ResearchCalibratedScoreResult:
    profile_id: str
    profile_version: str
    contract_hash: str
    component_score_vector: Mapping[str,float]
    verified_supported_score: float
    provisional_score_lower: float
    provisional_score_upper: float
    full_e2r_score: float | None
    full_score_valid: bool
    score_type: str
    score_confidence: float
    material_nonterminal_components: tuple[str,...]
    audit: Mapping[str,Any]

    def to_dict(self)->Mapping[str,Any]: return asdict(self)


class ResearchCalibratedComponentScorer:
    def score(self, *, contract: ArchetypeScoringContract, impacts: Sequence[CreditValidatedImpact], assessments: Sequence[ComponentAssessment]) -> ResearchCalibratedScoreResult:
        by_component={a.component_id:a for a in assessments}
        if set(by_component)!=set(contract.component_weights): raise ValueError("component assessment coverage differs from calibrated profile")
        for component_id,a in by_component.items():
            if abs(a.max_points-contract.component_max_points[component_id])>1e-6: raise ValueError("component max points differ from calibrated profile")
            expected_fraction=min(1.0,sum(i.validated_credit_fraction for i in impacts if i.component_id==component_id and i.direction=="SUPPORT"))
            expected=round(a.max_points*expected_fraction,6)
            if a.support_impact_ids and abs(a.verified_points-expected)>1e-6: raise ValueError("component points differ from validated impacts")
        vector={key:round(by_component[key].verified_points,6) for key in contract.component_weights}
        verified=round(sum(vector.values()),6)
        lower=round(sum(a.lower_bound_points for a in assessments),6); upper=round(sum(a.upper_bound_points for a in assessments),6)
        nonterminal=tuple(a.component_id for a in assessments if a.status not in TERMINAL_FULL_SCORE_STATUSES)
        full_valid=not nonterminal
        full=verified if full_valid else None
        confidence=round(sum(a.confidence*a.max_points for a in assessments)/100.0,6)
        critical={
            "balanced_point_score_count":int(len(set(vector.values()))==1 and len(vector)>1 and verified>0),
            "calibrated_profile_not_used_count":0,
            "supported_component_lost_count":sum(bool(a.support_impact_ids) and a.verified_points<=0 for a in assessments),
            "full_score_with_nonterminal_component_count":int(full is not None and bool(nonterminal)),
            "component_sum_total_mismatch_count":int(full is not None and abs(sum(vector.values())-full)>1e-6),
        }
        return ResearchCalibratedScoreResult(profile_id=contract.profile_id,profile_version=contract.profile_version,contract_hash=contract.config_hash,component_score_vector=vector,verified_supported_score=verified,provisional_score_lower=lower,provisional_score_upper=upper,full_e2r_score=full,full_score_valid=full_valid,score_type="FULL_E2R_100" if full_valid else "VERIFIED_COMPONENT_PARTIAL",score_confidence=confidence,material_nonterminal_components=nonterminal,audit={"schema_version":"e2r_research_calibrated_score_audit_v1","status":"RESEARCH_CALIBRATED_COMPONENT_SCORING_PASS" if sum(critical.values())==0 else "RESEARCH_CALIBRATED_COMPONENT_SCORING_FAIL","critical_counts":critical,"critical_count_sum":sum(critical.values())})


__all__=["ResearchCalibratedComponentScorer","ResearchCalibratedScoreResult"]
