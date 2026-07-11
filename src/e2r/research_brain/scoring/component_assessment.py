from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Mapping, Sequence

from e2r.research_brain.runtime.scoring_contracts import ArchetypeScoringContract
from .impact_validator import CreditValidatedImpact


class ComponentAssessmentStatus(str, Enum):
    VERIFIED_STRONG_SUPPORT="VERIFIED_STRONG_SUPPORT"
    VERIFIED_PARTIAL_SUPPORT="VERIFIED_PARTIAL_SUPPORT"
    VERIFIED_WEAK_SUPPORT="VERIFIED_WEAK_SUPPORT"
    VERIFIED_ABSENT_AFTER_SEARCH="VERIFIED_ABSENT_AFTER_SEARCH"
    VERIFIED_COUNTER="VERIFIED_COUNTER"
    CONTRADICTED_OPEN="CONTRADICTED_OPEN"
    HISTORICAL_ONLY="HISTORICAL_ONLY"
    NOT_APPLICABLE="NOT_APPLICABLE"
    UNKNOWN_UNINVESTIGATED="UNKNOWN_UNINVESTIGATED"
    SOURCE_PENDING="SOURCE_PENDING"
    PROVIDER_PENDING="PROVIDER_PENDING"
    BUDGET_PENDING="BUDGET_PENDING"


TERMINAL_FULL_SCORE_STATUSES={
    ComponentAssessmentStatus.VERIFIED_STRONG_SUPPORT.value,
    ComponentAssessmentStatus.VERIFIED_PARTIAL_SUPPORT.value,
    ComponentAssessmentStatus.VERIFIED_WEAK_SUPPORT.value,
    ComponentAssessmentStatus.VERIFIED_ABSENT_AFTER_SEARCH.value,
    ComponentAssessmentStatus.VERIFIED_COUNTER.value,
    ComponentAssessmentStatus.NOT_APPLICABLE.value,
}


@dataclass(frozen=True)
class ComponentAssessment:
    assessment_id: str
    component_id: str
    max_points: float
    status: str
    support_impact_ids: tuple[str,...]
    counter_impact_ids: tuple[str,...]
    verified_points: float
    lower_bound_points: float
    upper_bound_points: float
    missing_questions: tuple[str,...]
    search_exhaustion_proof: tuple[str,...]
    confidence: float

    def to_dict(self)->Mapping[str,Any]: return asdict(self)


@dataclass(frozen=True)
class ComponentAssessmentResult:
    status: str
    assessments: tuple[ComponentAssessment,...]
    material_nonterminal_components: tuple[str,...]
    audit: Mapping[str,Any]


class ComponentAssessmentBuilder:
    def build(self, *, contract: ArchetypeScoringContract, impacts: Sequence[CreditValidatedImpact], terminal_evidence: Mapping[str,Mapping[str,Any]] | None = None) -> ComponentAssessmentResult:
        terminal_evidence = terminal_evidence or {}
        assessments=[]
        for component_id,max_points in contract.component_max_points.items():
            support=tuple(i for i in impacts if i.component_id==component_id and i.direction=="SUPPORT" and i.validated_credit_fraction>0)
            counter=tuple(i for i in impacts if i.component_id==component_id and i.direction=="COUNTER" and i.validated_credit_fraction>0)
            explicit=dict(terminal_evidence.get(component_id) or {})
            fraction=min(1.0,sum(i.validated_credit_fraction for i in support))
            verified=round(max_points*fraction,6)
            proof=tuple(str(v) for v in explicit.get("search_exhaustion_proof") or ())
            missing=tuple(str(v) for v in explicit.get("missing_questions") or ())
            if support:
                state=(ComponentAssessmentStatus.VERIFIED_STRONG_SUPPORT.value if fraction>=.75 else ComponentAssessmentStatus.VERIFIED_PARTIAL_SUPPORT.value if fraction>=.4 else ComponentAssessmentStatus.VERIFIED_WEAK_SUPPORT.value)
            elif counter: state=ComponentAssessmentStatus.VERIFIED_COUNTER.value
            else: state=str(explicit.get("status") or ComponentAssessmentStatus.UNKNOWN_UNINVESTIGATED.value)
            if state not in {v.value for v in ComponentAssessmentStatus}: raise ValueError("unknown component assessment state")
            if state==ComponentAssessmentStatus.VERIFIED_ABSENT_AFTER_SEARCH.value and not proof: raise ValueError("evaluated absence requires search exhaustion proof")
            if state in {ComponentAssessmentStatus.VERIFIED_ABSENT_AFTER_SEARCH.value,ComponentAssessmentStatus.VERIFIED_COUNTER.value,ComponentAssessmentStatus.NOT_APPLICABLE.value}: verified=0.0
            terminal=state in TERMINAL_FULL_SCORE_STATUSES
            upper=verified if terminal else float(max_points)
            confidence=max((i.validated_credit_fraction for i in (*support,*counter)),default=float(explicit.get("confidence") or 0.0))
            aid=f"COMP-{contract.config_hash[:8]}-{component_id}"
            assessments.append(ComponentAssessment(aid,component_id,float(max_points),state,tuple(i.impact_id for i in support),tuple(i.impact_id for i in counter),verified,verified,round(upper,6),missing,proof,round(confidence,6)))
        nonterminal=tuple(a.component_id for a in assessments if a.status not in TERMINAL_FULL_SCORE_STATUSES)
        critical={
            "evaluated_absent_blocks_full_score_count":0,
            "unknown_uninvestigated_allows_full_score_count":0,
            "provider_pending_allows_full_score_count":0,
            "supported_component_erased_by_other_gap_count":sum(bool(a.support_impact_ids) and a.verified_points<=0 for a in assessments),
        }
        return ComponentAssessmentResult(status="COMPONENT_ASSESSMENT_STATE_PASS" if sum(critical.values())==0 else "COMPONENT_ASSESSMENT_STATE_FAIL",assessments=tuple(assessments),material_nonterminal_components=nonterminal,audit={"schema_version":"e2r_component_assessment_audit_v1","component_count":len(assessments),"terminal_component_count":len(assessments)-len(nonterminal),"nonterminal_component_count":len(nonterminal),"verified_supported_points":round(sum(a.verified_points for a in assessments),6),"critical_counts":critical,"critical_count_sum":sum(critical.values())})


__all__=["ComponentAssessment","ComponentAssessmentBuilder","ComponentAssessmentResult","ComponentAssessmentStatus","TERMINAL_FULL_SCORE_STATUSES"]
