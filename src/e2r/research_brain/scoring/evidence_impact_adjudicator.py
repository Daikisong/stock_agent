from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Any, Mapping, Protocol, Sequence

from .claim_impact_ledger import ClaimImpactProposal
from .evidence_impact_rubric import EvidenceImpactRubric


SCORE_KEYS = {"score", "total_score", "full_e2r_score"}
STAGE_KEYS = {"stage", "canonical_stage", "expected_stage"}
FUTURE_KEYS = {"mfe", "mae", "future_outcome"}
FORBIDDEN_KEYS = SCORE_KEYS | STAGE_KEYS | FUTURE_KEYS


class EvidenceImpactProvider(Protocol):
    provider_name: str
    def complete(self, *, pass_name: str, payload: Mapping[str, Any]) -> Mapping[str, Any]: ...


@dataclass(frozen=True)
class EvidenceImpactAdjudicationResult:
    status: str
    proposals: tuple[ClaimImpactProposal, ...]
    unsupported_aspects: tuple[str, ...]
    counter_thesis: tuple[str, ...]
    prompt_hashes: tuple[str, ...]
    response_hashes: tuple[str, ...]
    audit: Mapping[str, Any]


class EvidenceImpactAdjudicator:
    def __init__(self, provider: EvidenceImpactProvider) -> None:
        self.provider = provider

    def adjudicate(
        self,
        *,
        target_identity: Mapping[str, Any],
        as_of_date: str,
        archetype_id: str,
        accepted_claim: Mapping[str, Any],
        exact_quote: str,
        document_metadata: Mapping[str, Any],
        current_claim_ledger: Sequence[Mapping[str, Any]],
        counter_claims: Sequence[Mapping[str, Any]],
        rubrics: Sequence[EvidenceImpactRubric],
        allowed_component_ids: Sequence[str],
        high_importance: bool = True,
    ) -> EvidenceImpactAdjudicationResult:
        payload = {
            "task": "Map the accepted current claim to one or more bounded economic impacts. Never output a score or Stage.",
            "target_identity": _sanitize(target_identity), "as_of_date": as_of_date,
            "archetype_id": archetype_id, "accepted_claim": _sanitize(accepted_claim),
            "exact_quote": exact_quote, "document_metadata": _sanitize(document_metadata),
            "current_claim_ledger": _sanitize(list(current_claim_ledger)),
            "counter_claims": _sanitize(list(counter_claims)),
            "rubrics": [_sanitize(item.to_dict()) for item in rubrics],
            "allowed_component_ids": list(allowed_component_ids),
            "required_output": {"impacts": "array", "unsupported_aspects": "non-empty array", "counter_thesis": "array", "reasoning_summary": "text"},
        }
        prompt_hashes = [_hash(payload)]
        response_a = self.provider.complete(pass_name="IMPACT_PROPOSAL", payload=payload)
        response_hashes = [_hash(response_a)]
        score_key_count = _forbidden_key_count(response_a, SCORE_KEYS)
        stage_key_count = _forbidden_key_count(response_a, STAGE_KEYS)
        proposals, unsupported, counters, parse_errors = _decode_proposals(response_a, accepted_claim=accepted_claim, archetype_id=archetype_id, allowed_component_ids=set(allowed_component_ids))
        review_pending = False
        if high_importance and not parse_errors and not score_key_count and not stage_key_count:
            skeptic_payload = {**payload, "pass_a": _sanitize(response_a), "task": "Skeptically test each proposed impact, unsupported aspect, causal distance, and counter thesis. Output APPROVE or REVIEW_PENDING; never score or Stage."}
            prompt_hashes.append(_hash(skeptic_payload))
            response_b = self.provider.complete(pass_name="IMPACT_SKEPTIC", payload=skeptic_payload)
            response_hashes.append(_hash(response_b))
            score_key_count += _forbidden_key_count(response_b, SCORE_KEYS)
            stage_key_count += _forbidden_key_count(response_b, STAGE_KEYS)
            review_pending = str(response_b.get("verdict") or "") != "APPROVE"
        critical = {
            "llm_final_score_key_count": score_key_count,
            "llm_stage_key_count": stage_key_count,
            "future_outcome_leakage_count": _forbidden_input_count(payload),
            "impact_without_rationale_count": parse_errors,
            "unsupported_aspect_omission_count": int(not unsupported),
        }
        status = "IMPACT_ADJUDICATION_PASS"
        if review_pending:
            status = "REVIEW_PENDING"
            proposals = ()
        elif sum(critical.values()):
            status = "IMPACT_ADJUDICATION_FAIL"
            proposals = ()
        return EvidenceImpactAdjudicationResult(status=status, proposals=tuple(proposals), unsupported_aspects=tuple(unsupported), counter_thesis=tuple(counters), prompt_hashes=tuple(prompt_hashes), response_hashes=tuple(response_hashes), audit={"provider_name":self.provider.provider_name,"provider_call_count":len(response_hashes),"critical_counts":critical,"critical_count_sum":sum(critical.values())})


def _decode_proposals(response: Mapping[str, Any], *, accepted_claim: Mapping[str, Any], archetype_id: str, allowed_component_ids: set[str]) -> tuple[tuple[ClaimImpactProposal, ...], tuple[str, ...], tuple[str, ...], int]:
    unsupported = tuple(str(v) for v in response.get("unsupported_aspects") or () if str(v).strip())
    counters = tuple(str(v) for v in response.get("counter_thesis") or () if str(v).strip())
    proposals: list[ClaimImpactProposal] = []
    errors = 0
    for index, row in enumerate(response.get("impacts") or ()):
        try:
            component_id = str(row.get("component_id") or "")
            if component_id not in allowed_component_ids:
                raise ValueError("component is outside allowed catalog")
            base = {"claim_id":str(accepted_claim.get("claim_id") or ""),"mapping_id":str(row.get("mapping_id") or ""),"target_id":str(accepted_claim.get("target_id") or accepted_claim.get("target_entity_id") or ""),"archetype_id":archetype_id,"primitive_id":str(row.get("primitive_id") or ""),"component_id":component_id,"direction":str(row.get("direction") or ""),"support_type":str(row.get("support_type") or ""),"strength_band":str(row.get("strength_band") or ""),"completeness_band":str(row.get("completeness_band") or ""),"causal_distance":str(row.get("causal_distance") or ""),"temporal_scope":str(row.get("temporal_scope") or "CURRENT"),"source_family":str(row.get("source_family") or ""),"evidence_family_id":str(row.get("evidence_family_id") or ""),"confidence":float(row.get("confidence") or 0),"rationale":str(row.get("rationale") or ""),"unsupported_aspects":tuple(str(v) for v in row.get("unsupported_aspects") or ()),"counter_claim_ids":tuple(str(v) for v in row.get("counter_claim_ids") or ())}
            proposals.append(ClaimImpactProposal(impact_id=str(row.get("impact_id") or "IMPACT-"+_hash({"index":index,**base})[:24]),**base))
        except (TypeError, ValueError): errors += 1
    return tuple(proposals), unsupported, counters, errors


def _sanitize(value: Any) -> Any:
    if isinstance(value, Mapping): return {str(k):_sanitize(v) for k,v in value.items() if str(k).lower() not in FORBIDDEN_KEYS}
    if isinstance(value, (list,tuple)): return [_sanitize(v) for v in value]
    return value


def _forbidden_key_count(value: Any, keys: set[str] = FORBIDDEN_KEYS) -> int:
    if isinstance(value, Mapping): return sum(str(k).lower() in keys for k in value)+sum(_forbidden_key_count(v, keys) for v in value.values())
    if isinstance(value, (list,tuple)): return sum(_forbidden_key_count(v, keys) for v in value)
    return 0


def _forbidden_input_count(payload: Mapping[str, Any]) -> int: return _forbidden_key_count(payload)
def _hash(payload: Any) -> str: return hashlib.sha256(json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()


__all__ = ["EvidenceImpactAdjudicator","EvidenceImpactAdjudicationResult","EvidenceImpactProvider"]
