from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from typing import Any, Mapping, Sequence

from e2r.research_brain.compiler.evidence_impact_rubric_compiler import compile_evidence_impact_rubrics
from e2r.research_brain.runtime.scoring_contracts import load_archetype_scoring_contract


DIRECTIONS = {"SUPPORT", "COUNTER", "NEUTRAL", "RESOLUTION"}
SUPPORT_TYPES = {"DIRECT_ACTUAL", "DIRECT_FORWARD", "PARTIAL_BRIDGE", "PROFILE_ONLY", "DISCOVERY_ONLY", "RISK_OPEN", "RISK_RESOLVED"}
STRENGTH_BANDS = {"NONE", "WEAK", "MODERATE", "STRONG", "VERY_STRONG"}
COMPLETENESS_BANDS = {"MENTION", "PARTIAL", "SUBSTANTIAL", "COMPLETE_FOR_PRIMITIVE"}
CAUSAL_DISTANCES = {"DIRECT", "ONE_HOP", "TWO_HOP", "INDUSTRY_ONLY"}


def _hash(payload: Any) -> str:
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode()).hexdigest()


@dataclass(frozen=True)
class ClaimImpactProposal:
    impact_id: str
    claim_id: str
    mapping_id: str
    target_id: str
    archetype_id: str
    primitive_id: str
    component_id: str
    direction: str
    support_type: str
    strength_band: str
    completeness_band: str
    causal_distance: str
    temporal_scope: str
    source_family: str
    evidence_family_id: str
    confidence: float
    rationale: str
    unsupported_aspects: tuple[str, ...]
    counter_claim_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.direction not in DIRECTIONS or self.support_type not in SUPPORT_TYPES:
            raise ValueError("claim impact direction or support type is invalid")
        if self.strength_band not in STRENGTH_BANDS or self.completeness_band not in COMPLETENESS_BANDS:
            raise ValueError("claim impact strength or completeness band is invalid")
        if self.causal_distance not in CAUSAL_DISTANCES:
            raise ValueError("claim impact causal distance is invalid")
        if not 0 <= self.confidence <= 1 or not self.rationale.strip() or not self.unsupported_aspects:
            raise ValueError("claim impact requires confidence, rationale, and unsupported aspects")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ValidatedClaimImpact:
    proposal: ClaimImpactProposal
    validation_status: str = "LINEAGE_AND_EDGE_VALIDATED"
    original_source_task_gap_closed: bool = False

    def to_dict(self) -> Mapping[str, Any]:
        return {**self.proposal.to_dict(), "validation_status": self.validation_status, "original_source_task_gap_closed": self.original_source_task_gap_closed}


@dataclass(frozen=True)
class ClaimImpactLedgerResult:
    status: str
    validated_impacts: tuple[ValidatedClaimImpact, ...]
    rejected_impacts: tuple[Mapping[str, Any], ...]
    source_task_satisfaction: tuple[Mapping[str, Any], ...]
    audit: Mapping[str, Any]


class ClaimImpactLedgerBuilder:
    def build(
        self,
        *,
        proposals: Sequence[ClaimImpactProposal],
        accepted_current_claims: Sequence[Mapping[str, Any]],
        claim_provenance: Sequence[Mapping[str, Any]],
        source_task_satisfaction: Sequence[Mapping[str, Any]],
    ) -> ClaimImpactLedgerResult:
        claims = _unique(accepted_current_claims, "claim_id")
        provenance_mappings: dict[str, set[str]] = {}
        for row in claim_provenance:
            provenance_mappings.setdefault(str(row.get("claim_id") or ""), set()).update(str(v) for v in row.get("mapping_ids") or ())
        validated: list[ValidatedClaimImpact] = []
        rejected: list[Mapping[str, Any]] = []
        economic_keys: set[tuple[str, str, str, str]] = set()
        impact_ids: set[str] = set()
        for proposal in proposals:
            reason = ""
            claim = claims.get(proposal.claim_id)
            if proposal.impact_id in impact_ids:
                reason = "DUPLICATE_IMPACT_ID"
            elif claim is None or claim.get("accepted") is not True:
                reason = "CLAIM_NOT_ACCEPTED"
            elif str(claim.get("target_id") or claim.get("target_entity_id") or "") != proposal.target_id:
                reason = "TARGET_MISMATCH"
            elif proposal.mapping_id not in set(str(v) for v in claim.get("mapping_ids") or ()):
                reason = "CLAIM_MAPPING_LINEAGE_MISSING"
            elif proposal.mapping_id not in provenance_mappings.get(proposal.claim_id, set()):
                reason = "PROVENANCE_MAPPING_LINEAGE_MISSING"
            else:
                contract = load_archetype_scoring_contract(proposal.archetype_id)
                rubric = compile_evidence_impact_rubrics(proposal.archetype_id).by_primitive().get(proposal.primitive_id)
                allowed = set(rubric.allowed_component_ids if rubric else contract.primitive_to_component_allowed_edges.get(proposal.primitive_id, ()))
                if proposal.component_id not in allowed:
                    reason = "PRIMITIVE_COMPONENT_EDGE_NOT_ALLOWED"
            economic_key = (proposal.claim_id, proposal.component_id, proposal.direction, proposal.evidence_family_id)
            if not reason and economic_key in economic_keys:
                reason = "DUPLICATE_ECONOMIC_CREDIT"
            if reason:
                rejected.append({"impact_id": proposal.impact_id, "claim_id": proposal.claim_id, "reason": reason})
                continue
            impact_ids.add(proposal.impact_id)
            economic_keys.add(economic_key)
            validated.append(ValidatedClaimImpact(proposal=proposal))
        rerouted_mapping_ids = {
            str(mapping_id)
            for row in source_task_satisfaction
            if row.get("status") == "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN"
            for mapping_id in row.get("rerouted_mapping_ids") or ()
        }
        validated_mapping_ids = {item.proposal.mapping_id for item in validated}
        critical = {
            "valid_rerouted_claim_lost_score_impact_count": len(rerouted_mapping_ids - validated_mapping_ids),
            "one_claim_multiple_impact_rejected_count": 0,
            "mapping_lineage_loss_count": sum(row["reason"] in {"CLAIM_MAPPING_LINEAGE_MISSING", "PROVENANCE_MAPPING_LINEAGE_MISSING"} for row in rejected),
            "duplicate_economic_credit_count": sum(row["reason"] == "DUPLICATE_ECONOMIC_CREDIT" for row in rejected),
            "original_gap_closed_by_rerouted_count": sum(row.get("status") == "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN" and row.get("original_gap_open") is not True for row in source_task_satisfaction),
        }
        audit = {
            "schema_version": "e2r_claim_impact_ledger_audit_v1",
            "proposal_count": len(proposals),
            "validated_impact_count": len(validated),
            "rejected_impact_count": len(rejected),
            "multi_impact_claim_count": sum(1 for claim_id in {p.claim_id for p in proposals} if sum(v.proposal.claim_id == claim_id for v in validated) > 1),
            "critical_counts": critical,
            "critical_count_sum": sum(critical.values()),
        }
        return ClaimImpactLedgerResult(
            status="MANY_TO_MANY_CLAIM_IMPACT_PASS" if not rejected and sum(critical.values()) == 0 else "MANY_TO_MANY_CLAIM_IMPACT_FAIL",
            validated_impacts=tuple(validated),
            rejected_impacts=tuple(rejected),
            source_task_satisfaction=tuple(dict(row) for row in source_task_satisfaction),
            audit=audit,
        )


def _unique(rows: Sequence[Mapping[str, Any]], key: str) -> Mapping[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        identity = str(row.get(key) or "")
        if not identity or identity in result:
            raise ValueError("claim impact ledger requires unique accepted claims")
        result[identity] = row
    return result


__all__ = ["ClaimImpactLedgerBuilder", "ClaimImpactLedgerResult", "ClaimImpactProposal", "ValidatedClaimImpact"]
