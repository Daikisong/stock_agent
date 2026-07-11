from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Any, Mapping, Protocol, Sequence

from .claim_impact_ledger import ClaimImpactProposal
from .business_mechanism_scope import (
    BusinessMechanismScope,
    MechanismScopeValidator,
    load_mechanism_scope_contracts,
)
from .claim_eligibility import ClaimEligibilityDecision
from .evidence_impact_rubric import EvidenceImpactRubric
from .question_impact_contract import QuestionImpactContract


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
    review_issues: tuple[str, ...]
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
        business_mechanism_scope: BusinessMechanismScope,
        question_impact_contracts: Sequence[QuestionImpactContract],
        claim_eligibility_decision: ClaimEligibilityDecision | Mapping[str, Any],
        component_subcriteria: Mapping[str, Sequence[Mapping[str, Any]]],
        high_importance: bool = True,
    ) -> EvidenceImpactAdjudicationResult:
        mechanism_contract = load_mechanism_scope_contracts().get(archetype_id)
        if mechanism_contract is None:
            raise ValueError("impact adjudication mechanism contract is missing")
        if not question_impact_contracts:
            raise ValueError("impact adjudication question contract is missing")
        eligibility_payload = (
            claim_eligibility_decision.to_dict()
            if isinstance(claim_eligibility_decision, ClaimEligibilityDecision)
            else dict(claim_eligibility_decision)
        )
        if not eligibility_payload.get("eligibility_decision_id"):
            raise ValueError("impact adjudication eligibility decision is missing")
        question_by_id = {
            item.question_family_id: item for item in question_impact_contracts
        }
        scope_validation_by_component = {
            component_id: MechanismScopeValidator().validate(
                scope=business_mechanism_scope,
                contract=mechanism_contract,
                component_id=component_id,
            ).to_dict()
            for component_id in allowed_component_ids
        }
        normalized_subcriteria = {
            str(component_id): tuple(dict(row) for row in rows)
            for component_id, rows in component_subcriteria.items()
        }
        if any(
            not normalized_subcriteria.get(component_id)
            for component_id in allowed_component_ids
        ):
            raise ValueError("impact adjudication component subcriteria are incomplete")
        payload = {
            "task": "Map the accepted current claim to one or more bounded economic impacts. Never output a score or Stage.",
            "target_identity": _sanitize(target_identity), "as_of_date": as_of_date,
            "archetype_id": archetype_id, "accepted_claim": _sanitize(accepted_claim),
            "exact_quote": exact_quote, "document_metadata": _sanitize(document_metadata),
            "current_claim_ledger": _sanitize(list(current_claim_ledger)),
            "counter_claims": _sanitize(list(counter_claims)),
            "business_mechanism_scope": _sanitize(
                business_mechanism_scope.to_dict()
            ),
            "mechanism_scope_validation_by_component": _sanitize(
                scope_validation_by_component
            ),
            "question_impact_contracts": [
                _sanitize(item.to_dict()) for item in question_impact_contracts
            ],
            "claim_eligibility_decision": _sanitize(eligibility_payload),
            "rubrics": [_sanitize(item.to_dict()) for item in rubrics],
            "allowed_component_ids": list(allowed_component_ids),
            "component_subcriteria": _sanitize(normalized_subcriteria),
            "required_output": {
                "impacts": (
                    "array of primitive_id, question_family_id, "
                    "question_contract_hash, component_id, "
                    "component_subcriterion_id, direction, support_type, "
                    "strength/completeness, causal_distance, "
                    "mechanism_scope_match, unsupported_aspects"
                ),
                "unsupported_aspects": "non-empty array",
                "counter_thesis": "array",
                "reasoning_summary": "text",
            },
        }
        prompt_hashes = [_hash(payload)]
        response_a = self.provider.complete(pass_name="IMPACT_PROPOSAL", payload=payload)
        response_hashes = [_hash(response_a)]
        score_key_count = _forbidden_key_count(response_a, SCORE_KEYS)
        stage_key_count = _forbidden_key_count(response_a, STAGE_KEYS)
        proposals, unsupported, counters, parse_errors = _decode_proposals(
            response_a,
            accepted_claim=accepted_claim,
            archetype_id=archetype_id,
            allowed_component_ids=set(allowed_component_ids),
            question_contracts=question_by_id,
            scope_validation_by_component=scope_validation_by_component,
            component_subcriteria=normalized_subcriteria,
        )
        raw_impacts = tuple(response_a.get("impacts") or ())
        impact_without_scope = sum(
            not isinstance(row.get("mechanism_scope_match"), bool)
            for row in raw_impacts
            if isinstance(row, Mapping)
        ) + sum(not isinstance(row, Mapping) for row in raw_impacts)
        impact_without_question = sum(
            not str(row.get("question_family_id") or "")
            or not str(row.get("question_contract_hash") or "")
            for row in raw_impacts
            if isinstance(row, Mapping)
        ) + sum(not isinstance(row, Mapping) for row in raw_impacts)
        impact_without_unsupported = sum(
            not tuple(row.get("unsupported_aspects") or ())
            for row in raw_impacts
            if isinstance(row, Mapping)
        ) + sum(not isinstance(row, Mapping) for row in raw_impacts)
        impact_without_subcriterion = sum(
            not str(row.get("component_subcriterion_id") or "")
            for row in raw_impacts
            if isinstance(row, Mapping)
        ) + sum(not isinstance(row, Mapping) for row in raw_impacts)
        review_pending = False
        mapping_rejected = False
        skeptic_verdict = "NOT_REQUIRED"
        review_issues: tuple[str, ...] = ()
        if high_importance and not parse_errors and not score_key_count and not stage_key_count:
            skeptic_payload = {**payload, "pass_a": _sanitize(response_a), "task": "Skeptically test each proposed impact, unsupported aspect, causal distance, and counter thesis. Output APPROVE or REVIEW_PENDING; never score or Stage."}
            prompt_hashes.append(_hash(skeptic_payload))
            response_b = self.provider.complete(pass_name="IMPACT_SKEPTIC", payload=skeptic_payload)
            response_hashes.append(_hash(response_b))
            score_key_count += _forbidden_key_count(response_b, SCORE_KEYS)
            stage_key_count += _forbidden_key_count(response_b, STAGE_KEYS)
            verdict = str(response_b.get("verdict") or "")
            skeptic_verdict = verdict
            review_pending = verdict == "REVIEW_PENDING"
            mapping_rejected = verdict == "REJECT_MAPPING"
            review_issues = tuple(
                str(value)
                for value in response_b.get("issues") or ()
                if str(value).strip()
            )
        critical = {
            "llm_final_score_key_count": score_key_count,
            "llm_stage_key_count": stage_key_count,
            "future_outcome_leakage_count": _forbidden_input_count(payload),
            "impact_decode_error_count": parse_errors,
            "impact_without_mechanism_scope_count": impact_without_scope,
            "impact_without_question_contract_count": impact_without_question,
            "impact_without_component_subcriterion_count": (
                impact_without_subcriterion
            ),
            "impact_without_unsupported_aspects_count": (
                impact_without_unsupported + int(not unsupported)
            ),
            "high_materiality_single_pass_count": int(
                high_importance and len(response_hashes) < 2
            ),
            "skeptic_invalid_verdict_count": int(
                high_importance
                and len(response_hashes) >= 2
                and skeptic_verdict
                not in {"APPROVE", "REVIEW_PENDING", "REJECT_MAPPING"}
            ),
        }
        status = "IMPACT_ADJUDICATION_PASS"
        if mapping_rejected:
            status = "IMPACT_MAPPING_REJECTED"
            proposals = ()
        elif review_pending:
            status = "REVIEW_PENDING"
            proposals = ()
        elif sum(critical.values()):
            status = "IMPACT_ADJUDICATION_FAIL"
            proposals = ()
        return EvidenceImpactAdjudicationResult(status=status, proposals=tuple(proposals), unsupported_aspects=tuple(unsupported), counter_thesis=tuple(counters), review_issues=review_issues, prompt_hashes=tuple(prompt_hashes), response_hashes=tuple(response_hashes), audit={"provider_name":self.provider.provider_name,"provider_call_count":len(response_hashes),"critical_counts":critical,"critical_count_sum":sum(critical.values())})


def compile_question_component_subcriteria(
    question_contracts: Sequence[QuestionImpactContract],
    *,
    allowed_component_ids: Sequence[str],
) -> Mapping[str, tuple[Mapping[str, Any], ...]]:
    result: dict[str, list[Mapping[str, Any]]] = {
        component_id: [] for component_id in allowed_component_ids
    }
    for contract in question_contracts:
        for component_id in contract.allowed_component_ids:
            if component_id not in result:
                continue
            result[component_id].append(
                {
                    "subcriterion_id": (
                        f"{component_id}:{contract.question_family_id}"
                    ),
                    "question_family_id": contract.question_family_id,
                    "role": "QUESTION_BOUNDED_IMPACT",
                }
            )
    for component_id, rows in result.items():
        if not rows:
            rows.append(
                {
                    "subcriterion_id": f"{component_id}:non_applicable_to_claim",
                    "question_family_id": "NON_APPLICABLE_TO_CURRENT_CLAIM",
                    "role": "NO_IMPACT_ALLOWED_FOR_CURRENT_CLAIM",
                }
            )
    return {key: tuple(value) for key, value in result.items()}


def _decode_proposals(
    response: Mapping[str, Any],
    *,
    accepted_claim: Mapping[str, Any],
    archetype_id: str,
    allowed_component_ids: set[str],
    question_contracts: Mapping[str, QuestionImpactContract],
    scope_validation_by_component: Mapping[str, Mapping[str, Any]],
    component_subcriteria: Mapping[str, Sequence[Mapping[str, Any]]],
) -> tuple[tuple[ClaimImpactProposal, ...], tuple[str, ...], tuple[str, ...], int]:
    unsupported = tuple(str(v) for v in response.get("unsupported_aspects") or () if str(v).strip())
    counters = tuple(str(v) for v in response.get("counter_thesis") or () if str(v).strip())
    proposals: list[ClaimImpactProposal] = []
    errors = 0
    for index, row in enumerate(response.get("impacts") or ()):
        try:
            component_id = str(row.get("component_id") or "")
            if component_id not in allowed_component_ids:
                raise ValueError("component is outside allowed catalog")
            question_id = str(row.get("question_family_id") or "")
            question = question_contracts.get(question_id)
            if question is None:
                raise ValueError("impact question contract is unknown")
            primitive_id = str(row.get("primitive_id") or "")
            if primitive_id not in question.allowed_primitive_ids:
                raise ValueError("primitive is outside question contract")
            if component_id not in question.allowed_component_ids:
                raise ValueError("component is outside question contract")
            question_hash = str(row.get("question_contract_hash") or "")
            if question_hash != question.contract_hash:
                raise ValueError("question contract hash mismatch")
            subcriterion_id = str(row.get("component_subcriterion_id") or "")
            allowed_subcriteria = {
                str(value.get("subcriterion_id") or "")
                for value in component_subcriteria.get(component_id, ())
            }
            if subcriterion_id not in allowed_subcriteria:
                raise ValueError("component subcriterion is unknown")
            scope_match = row.get("mechanism_scope_match")
            if not isinstance(scope_match, bool):
                raise ValueError("mechanism scope match must be boolean")
            deterministic_scope_match = bool(
                scope_validation_by_component[component_id].get("scope_match")
            )
            if scope_match != deterministic_scope_match:
                raise ValueError("mechanism scope verdict disagrees with deterministic scope")
            base = {"claim_id":str(accepted_claim.get("claim_id") or ""),"mapping_id":str(row.get("mapping_id") or ""),"target_id":str(accepted_claim.get("target_id") or accepted_claim.get("target_entity_id") or ""),"archetype_id":archetype_id,"primitive_id":primitive_id,"component_id":component_id,"direction":str(row.get("direction") or ""),"support_type":str(row.get("support_type") or ""),"strength_band":str(row.get("strength_band") or ""),"completeness_band":str(row.get("completeness_band") or ""),"causal_distance":str(row.get("causal_distance") or ""),"temporal_scope":str(row.get("temporal_scope") or "CURRENT"),"source_family":str(row.get("source_family") or ""),"evidence_family_id":str(row.get("evidence_family_id") or ""),"confidence":float(row.get("confidence") or 0),"rationale":str(row.get("rationale") or ""),"unsupported_aspects":tuple(str(v) for v in row.get("unsupported_aspects") or ()),"counter_claim_ids":tuple(str(v) for v in row.get("counter_claim_ids") or ()),"question_family_id":question_id,"question_contract_hash":question_hash,"component_subcriterion_id":subcriterion_id,"mechanism_scope_match":scope_match}
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


__all__ = [
    "EvidenceImpactAdjudicator",
    "EvidenceImpactAdjudicationResult",
    "EvidenceImpactProvider",
    "compile_question_component_subcriteria",
]
