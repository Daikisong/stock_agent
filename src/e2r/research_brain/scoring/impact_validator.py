from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from typing import Any, Mapping, Sequence

from e2r.research_brain.runtime.scoring_contracts import load_archetype_scoring_contract
from e2r.research_brain.runtime.scoring_contracts.scoring_policy_v2 import (
    load_scoring_policy_v2,
    require_scoring_key,
)
from .claim_impact_ledger import ValidatedClaimImpact


@dataclass(frozen=True)
class CreditValidatedImpact:
    impact_id: str
    claim_id: str
    mapping_id: str
    target_id: str
    archetype_id: str
    primitive_id: str
    component_id: str
    direction: str
    evidence_family_id: str
    raw_credit_fraction: float
    validated_credit_fraction: float
    strength_fraction: float
    completeness_fraction: float
    causal_cap: float
    source_cap: float
    temporal_cap: float
    support_type_cap: float
    claim_budget_scaled: bool
    correlation_scaled: bool
    lineage_mapping_ids: tuple[str, ...] = ()
    validation_status: str = "CREDIT_VALIDATED"

    def to_dict(self) -> Mapping[str, Any]: return asdict(self)


@dataclass(frozen=True)
class ImpactValidationResult:
    status: str
    impacts: tuple[CreditValidatedImpact, ...]
    rejected: tuple[Mapping[str, Any], ...]
    audit: Mapping[str, Any]


class ImpactValidator:
    def validate(self, *, impacts: Sequence[ValidatedClaimImpact], claim_provenance: Sequence[Mapping[str, Any]]) -> ImpactValidationResult:
        from e2r.research_brain.compiler.evidence_impact_rubric_compiler import (
            compile_evidence_impact_rubrics,
        )

        scoring_policy = load_scoring_policy_v2()
        provenance = {str(r.get("claim_id") or ""): r for r in claim_provenance}
        accepted: list[CreditValidatedImpact] = []; rejected: list[Mapping[str, Any]] = []
        group_by_primitive: dict[tuple[str,str], str] = {}
        for impact in impacts:
            p=impact.proposal; contract=load_archetype_scoring_contract(p.archetype_id)
            catalog=compile_evidence_impact_rubrics(p.archetype_id); rubric=catalog.by_primitive().get(p.primitive_id)
            prov=provenance.get(p.claim_id); reason=""
            if impact.validation_status != "LINEAGE_AND_EDGE_VALIDATED": reason="UNVALIDATED_LEDGER_IMPACT"
            elif rubric is None or p.component_id not in rubric.allowed_component_ids: reason="RUBRIC_EDGE_VIOLATION"
            elif prov is None or prov.get("source_proxy_only") is not False or prov.get("directness") != "DIRECT" or prov.get("temporal_status") != "CURRENT": reason="PROVENANCE_NOT_CURRENT_DIRECT"
            elif p.mapping_id not in set(str(v) for v in prov.get("mapping_ids") or ()): reason="PROVENANCE_MAPPING_MISSING"
            elif any(mapping_id not in set(str(v) for v in prov.get("mapping_ids") or ()) for mapping_id in p.lineage_mapping_ids): reason="PROVENANCE_MAPPING_MISSING"
            if reason:
                rejected.append({"impact_id":p.impact_id,"reason":reason}); continue
            strength=float(require_scoring_key(rubric.strength_bands,p.strength_band,policy_name="strength_bands")); completeness=float(require_scoring_key(rubric.completeness_bands,p.completeness_band,policy_name="completeness_bands"))
            causal=float(require_scoring_key(rubric.causal_distance_caps,p.causal_distance,policy_name="causal_distance_caps")); source=float(require_scoring_key(rubric.source_family_caps,p.source_family,policy_name="source_family_caps"))
            temporal=float(require_scoring_key(contract.freshness_caps,p.temporal_scope,policy_name="temporal_scope_caps")); support=float(scoring_policy.cap_for(support_type=p.support_type,direction=p.direction))
            raw=round(strength*completeness,6); validated=round(min(raw,causal,source,temporal,support),6)
            accepted.append(CreditValidatedImpact(impact_id=p.impact_id,claim_id=p.claim_id,mapping_id=p.mapping_id,target_id=p.target_id,archetype_id=p.archetype_id,primitive_id=p.primitive_id,component_id=p.component_id,direction=p.direction,evidence_family_id=p.evidence_family_id,raw_credit_fraction=raw,validated_credit_fraction=validated,strength_fraction=strength,completeness_fraction=completeness,causal_cap=causal,source_cap=source,temporal_cap=temporal,support_type_cap=support,claim_budget_scaled=False,correlation_scaled=False,lineage_mapping_ids=p.lineage_mapping_ids))
            for group, primitives in contract.correlation_groups.items():
                if p.primitive_id in primitives: group_by_primitive[(p.archetype_id,p.primitive_id)]=group
        accepted=_scale_groups(accepted, group_by_primitive)
        accepted=_scale_claim_budgets(accepted)
        critical={
            "unvalidated_impact_to_score_count":sum(r["reason"]=="UNVALIDATED_LEDGER_IMPACT" for r in rejected),
            "rubric_edge_violation_count":sum(r["reason"]=="RUBRIC_EDGE_VIOLATION" for r in rejected),
            "source_cap_violation_count":sum(i.validated_credit_fraction>i.source_cap+1e-9 for i in accepted),
            "claim_credit_budget_violation_count":sum(sum(i.validated_credit_fraction for i in accepted if i.claim_id==cid)>1.000001 for cid in {i.claim_id for i in accepted}),
            "correlated_double_count_count":0,
        }
        return ImpactValidationResult(status="IMPACT_CREDIT_CAP_PASS" if not rejected and sum(critical.values())==0 else "IMPACT_CREDIT_CAP_FAIL",impacts=tuple(accepted),rejected=tuple(rejected),audit={"schema_version":"e2r_impact_credit_cap_audit_v1","validated_impact_count":len(accepted),"rejected_impact_count":len(rejected),"claim_budget_scaled_count":sum(i.claim_budget_scaled for i in accepted),"correlation_scaled_count":sum(i.correlation_scaled for i in accepted),"critical_counts":critical,"critical_count_sum":sum(critical.values())})


def _scale_groups(items: list[CreditValidatedImpact], groups: Mapping[tuple[str,str],str]) -> list[CreditValidatedImpact]:
    result=list(items)
    keys={(i.claim_id,groups.get((i.archetype_id,i.primitive_id))) for i in items if groups.get((i.archetype_id,i.primitive_id))}
    for claim_id,group in keys:
        indexes=[n for n,i in enumerate(result) if i.claim_id==claim_id and groups.get((i.archetype_id,i.primitive_id))==group]
        total=sum(result[n].validated_credit_fraction for n in indexes)
        if total>1:
            for n in indexes: result[n]=replace(result[n],validated_credit_fraction=round(result[n].validated_credit_fraction/total,6),correlation_scaled=True)
    return result


def _scale_claim_budgets(items: list[CreditValidatedImpact]) -> list[CreditValidatedImpact]:
    result=list(items)
    for claim_id in {i.claim_id for i in result}:
        indexes=[n for n,i in enumerate(result) if i.claim_id==claim_id]; total=sum(result[n].validated_credit_fraction for n in indexes)
        if total>1:
            for n in indexes: result[n]=replace(result[n],validated_credit_fraction=round(result[n].validated_credit_fraction/total,6),claim_budget_scaled=True)
    return result


__all__=["CreditValidatedImpact","ImpactValidationResult","ImpactValidator"]
