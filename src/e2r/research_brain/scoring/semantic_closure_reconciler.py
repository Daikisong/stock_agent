"""Question-to-claim-to-impact-to-component semantic closure reconciliation."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash

from .question_impact_contract import QuestionImpactContract


SCORING_STATUSES = {
    "SUPPORTED_SCORING",
    "PARTIALLY_SUPPORTED_SCORING",
}
PENDING_STATUSES = {
    "SOURCE_PENDING",
    "PROVIDER_PENDING",
    "BUDGET_PENDING",
}
INTERNAL_REJECTION_REASONS = {
    "RUBRIC_EDGE_VIOLATION",
    "MECHANISM_SCOPE_MISSING",
    "MECHANISM_SCOPE_INCOMPLETE",
    "CROSS_MECHANISM_IMPACT",
    "ELIGIBILITY_DECISION_MISSING",
    "CLAIM_COMPONENT_INELIGIBLE",
    "PROVENANCE_MAPPING_MISSING",
    "UNVALIDATED_LEDGER_IMPACT",
    "PRIMITIVE_COMPONENT_EDGE_NOT_ALLOWED",
    "SCORING_CONTRACT_INCOMPLETE",
}


@dataclass(frozen=True)
class QuestionComponentReconciliation:
    reconciliation_id: str
    question_family_id: str
    question_contract_hash: str
    input_closure_status: str
    reconciled_closure_status: str
    reconciliation_status: str
    supporting_claim_ids: tuple[str, ...]
    positive_scoring_claim_ids: tuple[str, ...]
    eligibility_decision_ids: tuple[str, ...]
    proposal_impact_ids: tuple[str, ...]
    positive_proposal_impact_ids: tuple[str, ...]
    validated_impact_ids: tuple[str, ...]
    component_ids: tuple[str, ...]
    component_subcriterion_ids: tuple[str, ...]
    credit_result: str
    component_states: Mapping[str, str]
    component_links: tuple[Mapping[str, Any], ...]
    search_adequate: bool
    provider_failure: bool
    internal_rejection: bool
    error_codes: tuple[str, ...]

    def to_dict(self) -> Mapping[str, Any]:
        return json.loads(json.dumps(asdict(self), ensure_ascii=False))


@dataclass(frozen=True)
class SemanticClosureReconciliationResult:
    status: str
    reconciliations: tuple[QuestionComponentReconciliation, ...]
    question_closures: tuple[Mapping[str, Any], ...]
    audit: Mapping[str, Any]


class SemanticClosureReconciler:
    def reconcile(
        self,
        *,
        contracts: Mapping[str, QuestionImpactContract],
        question_closures: Sequence[Mapping[str, Any]],
        claims: Sequence[Mapping[str, Any]],
        primitive_mappings: Sequence[Mapping[str, Any]],
        eligibility_decisions: Sequence[Mapping[str, Any]],
        proposed_impacts: Sequence[Any],
        validated_impacts: Sequence[Any],
        component_assessments: Sequence[Any] = (),
        rejected_impacts: Sequence[Mapping[str, Any]] = (),
        adjudications: Sequence[Mapping[str, Any]] = (),
        search_adequacy: Sequence[Mapping[str, Any]] = (),
    ) -> SemanticClosureReconciliationResult:
        closure_by_question = {
            str(row.get("question_family_id") or ""): dict(row)
            for row in question_closures
        }
        claim_by_id = {
            str(row.get("claim_id") or ""): row for row in claims
        }
        eligibility_by_claim = {
            str(row.get("claim_id") or ""): row
            for row in eligibility_decisions
        }
        mappings_by_claim: dict[str, list[Mapping[str, Any]]] = {}
        for row in primitive_mappings:
            if row.get("accepted_by_evidence_os") is True:
                mappings_by_claim.setdefault(
                    str(row.get("claim_id") or ""), []
                ).append(row)
        assessments = {
            str(_value(row, "component_id") or ""): row
            for row in component_assessments
        }
        adequacy_by_question = {
            str(row.get("question_family_id") or ""): row
            for row in search_adequacy
        }
        adjudication_by_claim = {
            str(row.get("claim_id") or ""): row for row in adjudications
        }
        proposal_by_id = {
            str(_value(row, "impact_id") or ""): row
            for row in proposed_impacts
        }
        rejected_by_impact = {
            str(row.get("impact_id") or ""): row
            for row in rejected_impacts
        }
        reconciliations = []
        corrected_closures = []
        for question_id, contract in contracts.items():
            closure = dict(closure_by_question.get(question_id) or {})
            input_status = str(closure.get("status") or "SOURCE_PENDING")
            relevant_claim_ids = tuple(
                claim_id
                for claim_id, claim in claim_by_id.items()
                if claim.get("accepted") is True
                and any(
                    str(mapping.get("primitive_id") or "")
                    in contract.allowed_primitive_ids
                    for mapping in mappings_by_claim.get(claim_id, ())
                )
            )
            declared_positive_claim_ids = {
                str(claim_id)
                for claim_id in (
                    *(closure.get("supporting_claim_ids") or ()),
                    *(closure.get("partial_supporting_claim_ids") or ()),
                )
            }
            positive_claim_ids = tuple(
                claim_id
                for claim_id in relevant_claim_ids
                if claim_id in declared_positive_claim_ids
                if eligibility_by_claim.get(claim_id, {}).get(
                    "component_scoring_eligibility"
                )
                is True
                and not _claim_is_counter(
                    claim_by_id[claim_id],
                    mappings_by_claim.get(claim_id, ()),
                )
            )
            question_proposals = tuple(
                row
                for row in proposed_impacts
                if str(_value(row, "question_family_id") or "")
                == question_id
            )
            question_impacts = tuple(
                row
                for row in validated_impacts
                if str(_value(row, "question_family_id") or "")
                == question_id
                and float(_value(row, "validated_credit_fraction") or 0.0)
                > 0
            )
            positive_proposals = tuple(
                row
                for row in question_proposals
                if str(_value(row, "direction") or "") == "SUPPORT"
            )
            positive_proposal_ids = tuple(
                str(_value(row, "impact_id") or "")
                for row in positive_proposals
            )
            support_impacts = tuple(
                row
                for row in question_impacts
                if float(_value(row, "support_credit_fraction") or 0.0) > 0
            )
            counter_impacts = tuple(
                row
                for row in question_impacts
                if float(_value(row, "counter_effect_fraction") or 0.0) > 0
            )
            bounded_support = tuple(
                row
                for row in support_impacts
                if 0
                < float(_value(row, "support_credit_fraction") or 0.0)
                < 1
                or str(_value(row, "support_type") or "")
                == "PARTIAL_BRIDGE"
            )
            component_links = _component_links(
                impacts=question_impacts,
                assessments=assessments,
            )
            component_states = {
                component_id: str(_value(row, "status") or "NOT_ASSESSED")
                for component_id, row in assessments.items()
                if component_id in contract.allowed_component_ids
            }
            cap_or_counter = bool(counter_impacts) or any(
                str(link["component_state"])
                in {
                    "SUPPORT_WITH_COUNTER_CAP",
                    "CONTRADICTED_OPEN",
                    "VERIFIED_COUNTER",
                    "RESOLVED_COUNTER",
                }
                for link in component_links
            )
            provider_failure = input_status == "PROVIDER_PENDING" or any(
                str(adjudication_by_claim.get(claim_id, {}).get("status") or "")
                in {
                    "IMPACT_ADJUDICATION_FAIL",
                    "REVIEW_PENDING",
                    "PROVIDER_ERROR",
                }
                for claim_id in relevant_claim_ids
            )
            internal_rejection = _internal_rejection(
                positive_proposals=positive_proposals,
                question_impacts=question_impacts,
                rejected_by_impact=rejected_by_impact,
                proposal_by_id=proposal_by_id,
            )
            search_is_adequate = _search_adequate(
                closure=closure,
                adequacy=adequacy_by_question.get(question_id),
            )
            errors = []
            if input_status == "SUPPORTED_SCORING" and not (
                support_impacts or cap_or_counter
            ):
                errors.append("SUPPORTED_SCORING_WITHOUT_CREDIT")
            if input_status == "PARTIALLY_SUPPORTED_SCORING" and not bounded_support:
                errors.append("PARTIAL_SUPPORT_WITHOUT_BOUNDED_CREDIT")
            if input_status == "SUPPORTED_NON_SCORING" and support_impacts:
                errors.append("NON_SCORING_SUPPORT_HAS_COMPONENT_CREDIT")
            if input_status == "EVALUATED_ABSENT" and (
                positive_claim_ids or positive_proposals or support_impacts
            ):
                errors.append("ABSENCE_HAS_POSITIVE_SCORING_LINEAGE")
            if input_status == "EVALUATED_ABSENT" and internal_rejection:
                errors.append("ABSENCE_MASKS_INTERNAL_REJECTION")
            if input_status == "EVALUATED_ABSENT" and provider_failure:
                errors.append("ABSENCE_MASKS_PROVIDER_FAILURE")
            if input_status == "EVALUATED_ABSENT" and not search_is_adequate:
                errors.append("ABSENCE_WITH_INADEQUATE_SEARCH")
            linked_claim_ids = {
                str(link["claim_id"]) for link in component_links
            }
            missing_positive_claim_ids = set(positive_claim_ids) - linked_claim_ids
            linked_impact_ids = {
                str(link["impact_id"]) for link in component_links
            }
            missing_positive_proposal_ids = (
                set(positive_proposal_ids) - linked_impact_ids
            )
            if missing_positive_claim_ids and not provider_failure:
                errors.append("POSITIVE_CLAIM_WITHOUT_COMPONENT")
            if missing_positive_proposal_ids and not provider_failure:
                errors.append("POSITIVE_PROPOSAL_WITHOUT_COMPONENT")
            reconciled_status = input_status
            if provider_failure and errors:
                reconciled_status = "PROVIDER_PENDING"
            elif "ABSENCE_WITH_INADEQUATE_SEARCH" in errors and len(errors) == 1:
                reconciled_status = "SOURCE_PENDING"
            elif errors:
                reconciled_status = "SCORING_PIPELINE_ERROR"
            credit_result = _credit_result(
                support_impacts=support_impacts,
                counter_impacts=counter_impacts,
                bounded_support=bounded_support,
                input_status=input_status,
            )
            payload = {
                "question_family_id": question_id,
                "question_contract_hash": contract.contract_hash,
                "input_closure_status": input_status,
                "reconciled_closure_status": reconciled_status,
                "positive_scoring_claim_ids": positive_claim_ids,
                "proposal_impact_ids": tuple(
                    str(_value(row, "impact_id") or "")
                    for row in question_proposals
                ),
                "validated_impact_ids": tuple(
                    str(_value(row, "impact_id") or "")
                    for row in question_impacts
                ),
                "component_links": component_links,
                "error_codes": tuple(errors),
            }
            reconciliation = QuestionComponentReconciliation(
                reconciliation_id="RECON-" + stable_hash(payload)[:24],
                question_family_id=question_id,
                question_contract_hash=contract.contract_hash,
                input_closure_status=input_status,
                reconciled_closure_status=reconciled_status,
                reconciliation_status=(
                    "SEMANTIC_CLOSURE_RECONCILED"
                    if not errors
                    else reconciled_status
                ),
                supporting_claim_ids=tuple(
                    dict.fromkeys(
                        (
                            *(closure.get("supporting_claim_ids") or ()),
                            *(closure.get("partial_supporting_claim_ids") or ()),
                        )
                    )
                ),
                positive_scoring_claim_ids=positive_claim_ids,
                eligibility_decision_ids=tuple(
                    str(eligibility_by_claim[claim_id].get("eligibility_decision_id") or "")
                    for claim_id in relevant_claim_ids
                    if claim_id in eligibility_by_claim
                ),
                proposal_impact_ids=payload["proposal_impact_ids"],
                positive_proposal_impact_ids=positive_proposal_ids,
                validated_impact_ids=payload["validated_impact_ids"],
                component_ids=tuple(
                    dict.fromkeys(
                        str(link["component_id"]) for link in component_links
                    )
                ),
                component_subcriterion_ids=tuple(
                    dict.fromkeys(
                        str(link["component_subcriterion_id"])
                        for link in component_links
                    )
                ),
                credit_result=credit_result,
                component_states=component_states,
                component_links=component_links,
                search_adequate=search_is_adequate,
                provider_failure=provider_failure,
                internal_rejection=internal_rejection,
                error_codes=tuple(errors),
            )
            reconciliations.append(reconciliation)
            corrected_closures.append(
                {
                    **closure,
                    "question_family_id": question_id,
                    "question_contract_hash": contract.contract_hash,
                    "original_status": input_status,
                    "status": reconciled_status,
                    "reconciliation_id": reconciliation.reconciliation_id,
                    "semantic_reconciliation_status": (
                        reconciliation.reconciliation_status
                    ),
                    "reconciled_component_ids": list(
                        reconciliation.component_ids
                    ),
                    "reconciliation_search_adequate": search_is_adequate,
                    "reconciliation_error_codes": list(errors),
                }
            )
        critical = _critical_counts(reconciliations)
        critical_sum = sum(critical.values())
        audit = {
            "schema_version": "e2r_question_component_reconciliation_audit_v1",
            "status": (
                "QUESTION_COMPONENT_RECONCILIATION_PASS"
                if critical_sum == 0
                else "QUESTION_COMPONENT_RECONCILIATION_FAIL"
            ),
            "question_count": len(reconciliations),
            "pipeline_error_question_count": sum(
                row.reconciled_closure_status == "SCORING_PIPELINE_ERROR"
                for row in reconciliations
            ),
            "critical_counts": critical,
            "critical_count_sum": critical_sum,
        }
        return SemanticClosureReconciliationResult(
            status=str(audit["status"]),
            reconciliations=tuple(reconciliations),
            question_closures=tuple(corrected_closures),
            audit=audit,
        )


def _component_links(
    *, impacts: Sequence[Any], assessments: Mapping[str, Any]
) -> tuple[Mapping[str, Any], ...]:
    return tuple(
        {
            "impact_id": str(_value(impact, "impact_id") or ""),
            "claim_id": str(_value(impact, "claim_id") or ""),
            "eligibility_decision_id": str(
                _value(impact, "eligibility_decision_id") or ""
            ),
            "component_id": str(_value(impact, "component_id") or ""),
            "component_subcriterion_id": str(
                _value(impact, "component_subcriterion_id") or ""
            ),
            "direction": str(_value(impact, "direction") or ""),
            "support_credit_fraction": float(
                _value(impact, "support_credit_fraction") or 0.0
            ),
            "counter_effect_fraction": float(
                _value(impact, "counter_effect_fraction") or 0.0
            ),
            "resolution_effect": float(
                _value(impact, "resolution_effect") or 0.0
            ),
            "component_state": str(
                _value(
                    assessments.get(
                        str(_value(impact, "component_id") or "")
                    ),
                    "status",
                )
                or "NOT_ASSESSED"
            ),
        }
        for impact in impacts
    )


def _critical_counts(
    rows: Sequence[QuestionComponentReconciliation],
) -> Mapping[str, int]:
    return {
        "supported_question_zero_credit_count": sum(
            row.input_closure_status == "SUPPORTED_SCORING"
            and "SUPPORTED_SCORING_WITHOUT_CREDIT" in row.error_codes
            for row in rows
        ),
        "partially_supported_question_zero_credit_count": sum(
            row.input_closure_status == "PARTIALLY_SUPPORTED_SCORING"
            and "PARTIAL_SUPPORT_WITHOUT_BOUNDED_CREDIT" in row.error_codes
            for row in rows
        ),
        "supported_question_absent_component_count": sum(
            row.input_closure_status in SCORING_STATUSES
            and not row.component_links
            for row in rows
        ),
        "positive_claim_absent_component_count": sum(
            len(
                set(row.positive_scoring_claim_ids)
                - {
                    str(link["claim_id"])
                    for link in row.component_links
                }
            )
            if not row.provider_failure
            else 0
            for row in rows
        ),
        "positive_proposal_absent_component_count": sum(
            len(
                set(row.positive_proposal_impact_ids)
                - {
                    str(link["impact_id"])
                    for link in row.component_links
                }
            )
            if not row.provider_failure
            else 0
            for row in rows
        ),
        "absence_with_internal_rejection_count": sum(
            row.input_closure_status == "EVALUATED_ABSENT"
            and row.internal_rejection
            for row in rows
        ),
        "absence_with_provider_failure_count": sum(
            row.input_closure_status == "EVALUATED_ABSENT"
            and row.provider_failure
            for row in rows
        ),
        "absence_with_inadequate_search_count": sum(
            row.input_closure_status == "EVALUATED_ABSENT"
            and not row.search_adequate
            for row in rows
        ),
        "supported_non_scoring_component_credit_count": sum(
            row.input_closure_status == "SUPPORTED_NON_SCORING"
            and bool(row.validated_impact_ids)
            for row in rows
        ),
    }


def _internal_rejection(
    *,
    positive_proposals: Sequence[Any],
    question_impacts: Sequence[Any],
    rejected_by_impact: Mapping[str, Mapping[str, Any]],
    proposal_by_id: Mapping[str, Any],
) -> bool:
    validated_ids = {
        str(_value(row, "impact_id") or "") for row in question_impacts
    }
    for proposal in positive_proposals:
        impact_id = str(_value(proposal, "impact_id") or "")
        if impact_id in validated_ids:
            continue
        rejection = rejected_by_impact.get(impact_id, {})
        reason = str(rejection.get("reason") or "")
        if reason in INTERNAL_REJECTION_REASONS or reason.startswith(
            "SCORING_CONTRACT_INCOMPLETE"
        ):
            return True
        if impact_id in proposal_by_id:
            return True
    return False


def _search_adequate(
    *, closure: Mapping[str, Any], adequacy: Mapping[str, Any] | None
) -> bool:
    adequacy = adequacy or {}
    if adequacy.get("adequate_absence_allowed") is True:
        return True
    if str(adequacy.get("saturation_status") or "") in {
        "ADEQUATE_ABSENCE",
        "EVIDENCE_FOUND",
    }:
        return True
    execution = closure.get("research_execution") or {}
    return bool(closure.get("search_exhaustion_proof")) and (
        str(closure.get("failure_class") or "")
        in {"ADEQUATE_ABSENCE", "SOURCE_EXHAUSTED"}
        or (
            execution.get("bounded") is True
            and execution.get("official_attempted") is True
        )
    )


def _claim_is_counter(
    claim: Mapping[str, Any], mappings: Sequence[Mapping[str, Any]]
) -> bool:
    if str(claim.get("polarity") or "").upper() in {
        "NEGATIVE",
        "COUNTER",
    }:
        return True
    return any(
        str(row.get("support_direction") or "").upper() == "COUNTER"
        for row in mappings
    )


def _credit_result(
    *,
    support_impacts: Sequence[Any],
    counter_impacts: Sequence[Any],
    bounded_support: Sequence[Any],
    input_status: str,
) -> str:
    if support_impacts and counter_impacts:
        return "SUPPORT_WITH_COUNTER_EFFECT"
    if bounded_support:
        return "NONZERO_BOUNDED_SUPPORT"
    if support_impacts:
        return "NONZERO_SUPPORT"
    if counter_impacts:
        return "EXPLICIT_COUNTER_OR_CAP"
    if input_status == "SUPPORTED_NON_SCORING":
        return "NON_SCORING_SUPPORT"
    if input_status == "EVALUATED_ABSENT":
        return "EVALUATED_ABSENCE"
    return "ZERO_CREDIT"


def _value(row: Any, key: str) -> Any:
    if row is None:
        return None
    if isinstance(row, Mapping):
        return row.get(key)
    return getattr(row, key, None)


__all__ = [
    "audit_question_component_reconciliation",
    "QuestionComponentReconciliation",
    "SemanticClosureReconciler",
    "SemanticClosureReconciliationResult",
]


def audit_question_component_reconciliation() -> Mapping[str, Any]:
    from .question_impact_contract import load_question_impact_contracts

    contracts = {
        key: value
        for key, value in load_question_impact_contracts().items()
        if value.archetype_id == "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
    }
    valid = _audit_valid_reconciliation(contracts)
    guards = _audit_guard_reconciliations(contracts)
    guard_expectations = {
        "supported_zero_credit": (
            "supported_question_zero_credit_count",
            "SCORING_PIPELINE_ERROR",
        ),
        "partial_zero_credit": (
            "partially_supported_question_zero_credit_count",
            "SCORING_PIPELINE_ERROR",
        ),
        "positive_proposal_missing_component": (
            "positive_proposal_absent_component_count",
            "SCORING_PIPELINE_ERROR",
        ),
        "absence_internal_rejection": (
            "absence_with_internal_rejection_count",
            "SCORING_PIPELINE_ERROR",
        ),
        "absence_provider_failure": (
            "absence_with_provider_failure_count",
            "PROVIDER_PENDING",
        ),
        "absence_inadequate_search": (
            "absence_with_inadequate_search_count",
            "SOURCE_PENDING",
        ),
        "non_scoring_with_component_credit": (
            "supported_non_scoring_component_credit_count",
            "SCORING_PIPELINE_ERROR",
        ),
    }
    guard_failures = sum(
        int(result.audit["critical_counts"][counter_name]) <= 0
        or _guard_question(result).reconciled_closure_status != expected_status
        for name, result in guards.items()
        for counter_name, expected_status in (guard_expectations[name],)
    )
    critical = {
        **{
            key: int(value)
            for key, value in valid.audit["critical_counts"].items()
        },
        "guard_canary_failure_count": guard_failures,
    }
    critical_sum = sum(critical.values())
    audit = {
        "schema_version": "e2r_question_component_reconciliation_audit_v1",
        "status": (
            "QUESTION_COMPONENT_RECONCILIATION_PASS"
            if critical_sum == 0
            else "QUESTION_COMPONENT_RECONCILIATION_FAIL"
        ),
        "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        "question_count": len(valid.reconciliations),
        "reconciliations": [
            row.to_dict() for row in valid.reconciliations
        ],
        "guard_canaries": {
            name: {
                "detected_critical_counts": result.audit["critical_counts"],
                "reconciled_closure_status": (
                    _guard_question(result).reconciled_closure_status
                ),
                "error_codes": list(_guard_question(result).error_codes),
            }
            for name, result in guards.items()
        },
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
    }
    return json.loads(json.dumps(audit, ensure_ascii=False))


def _audit_valid_reconciliation(
    contracts: Mapping[str, QuestionImpactContract],
) -> SemanticClosureReconciliationResult:
    claims = (
        {"claim_id": "C-SUPPORT", "accepted": True},
        {"claim_id": "C-PARTIAL", "accepted": True},
        {"claim_id": "C-NONSCORING", "accepted": True},
        {"claim_id": "C-COUNTER", "accepted": True, "polarity": "COUNTER"},
    )
    mappings = (
        _audit_mapping("C-SUPPORT", "customer_preorder_or_allocation"),
        _audit_mapping("C-PARTIAL", "actual_earnings_conversion"),
        _audit_mapping("C-NONSCORING", "hbm_product_profile"),
        _audit_mapping(
            "C-COUNTER", "conventional_memory_drag", direction="COUNTER"
        ),
    )
    eligibility = (
        _audit_eligibility("C-SUPPORT", True),
        _audit_eligibility("C-PARTIAL", True),
        _audit_eligibility("C-NONSCORING", False),
        _audit_eligibility("C-COUNTER", False),
    )
    closures = (
        {
            "question_family_id": "current_customer_allocation_commitment",
            "status": "SUPPORTED_SCORING",
            "supporting_claim_ids": ["C-SUPPORT"],
        },
        {
            "question_family_id": "revenue_operating_profit_conversion",
            "status": "PARTIALLY_SUPPORTED_SCORING",
            "partial_supporting_claim_ids": ["C-PARTIAL"],
        },
        {
            "question_family_id": "shipment_mass_production_generation",
            "status": "SUPPORTED_NON_SCORING",
            "non_scoring_claim_ids": ["C-NONSCORING"],
        },
        {
            "question_family_id": "qualification_pass_lag_reopen",
            "status": "EVALUATED_ABSENT",
            "search_exhaustion_proof": ["SEARCH-QUALIFICATION"],
            "failure_class": "SOURCE_EXHAUSTED",
        },
        {
            "question_family_id": "conventional_memory_drag",
            "status": "COUNTER_SUPPORTED",
            "counter_claim_ids": ["C-COUNTER"],
        },
    )
    support = _audit_proposal(
        "I-SUPPORT",
        "C-SUPPORT",
        "current_customer_allocation_commitment",
        "customer_preorder_or_allocation",
        "earnings_visibility",
        "C06_VIS_CUSTOMER_COMMITMENT",
    )
    partial = _audit_proposal(
        "I-PARTIAL",
        "C-PARTIAL",
        "revenue_operating_profit_conversion",
        "actual_earnings_conversion",
        "eps_fcf_explosion",
        "C06_EPS_ACTUAL_REVENUE_PROFIT",
    )
    counter = _audit_proposal(
        "I-COUNTER",
        "C-COUNTER",
        "conventional_memory_drag",
        "conventional_memory_drag",
        "earnings_visibility",
        "C06_VIS_MEDIUM_REVISION",
        direction="COUNTER",
    )
    return SemanticClosureReconciler().reconcile(
        contracts=contracts,
        question_closures=closures,
        claims=claims,
        primitive_mappings=mappings,
        eligibility_decisions=eligibility,
        proposed_impacts=(support, partial, counter),
        validated_impacts=(
            _audit_impact(support, support=0.8),
            _audit_impact(partial, support=0.4),
            _audit_impact(counter, counter=0.6),
        ),
        component_assessments=(
            {
                "component_id": "earnings_visibility",
                "status": "SUPPORT_WITH_COUNTER_CAP",
            },
            {
                "component_id": "eps_fcf_explosion",
                "status": "VERIFIED_WEAK_SUPPORT",
            },
        ),
    )


def _audit_guard_reconciliations(
    contracts: Mapping[str, QuestionImpactContract],
) -> Mapping[str, SemanticClosureReconciliationResult]:
    support_claim = {"claim_id": "C-GUARD", "accepted": True}
    mapping = _audit_mapping("C-GUARD", "qualification_state")
    eligibility = _audit_eligibility("C-GUARD", True)
    proposal = _audit_proposal(
        "I-GUARD",
        "C-GUARD",
        "qualification_pass_lag_reopen",
        "qualification_state",
        "earnings_visibility",
        "C06_VIS_QUALIFICATION",
    )

    def run(
        *,
        status: str,
        claims: Sequence[Mapping[str, Any]] = (),
        mappings: Sequence[Mapping[str, Any]] = (),
        decisions: Sequence[Mapping[str, Any]] = (),
        proposals: Sequence[Mapping[str, Any]] = (),
        impacts: Sequence[Mapping[str, Any]] = (),
        rejected: Sequence[Mapping[str, Any]] = (),
        adjudications: Sequence[Mapping[str, Any]] = (),
        proof: bool = True,
    ) -> SemanticClosureReconciliationResult:
        closure = {
            "question_family_id": "qualification_pass_lag_reopen",
            "status": status,
            "supporting_claim_ids": (
                ["C-GUARD"] if status == "SUPPORTED_SCORING" else []
            ),
            "partial_supporting_claim_ids": (
                ["C-GUARD"]
                if status == "PARTIALLY_SUPPORTED_SCORING"
                else []
            ),
            "search_exhaustion_proof": ["SEARCH-GUARD"] if proof else [],
            "failure_class": "SOURCE_EXHAUSTED" if proof else None,
        }
        return SemanticClosureReconciler().reconcile(
            contracts=contracts,
            question_closures=(closure,),
            claims=claims,
            primitive_mappings=mappings,
            eligibility_decisions=decisions,
            proposed_impacts=proposals,
            validated_impacts=impacts,
            rejected_impacts=rejected,
            adjudications=adjudications,
        )

    supported_zero = run(
        status="SUPPORTED_SCORING",
        claims=(support_claim,),
        mappings=(mapping,),
        decisions=(eligibility,),
    )
    partial_zero = run(
        status="PARTIALLY_SUPPORTED_SCORING",
        claims=(support_claim,),
        mappings=(mapping,),
        decisions=(eligibility,),
    )
    proposal_missing = run(
        status="SUPPORTED_SCORING",
        claims=(support_claim,),
        mappings=(mapping,),
        decisions=(eligibility,),
        proposals=(proposal,),
    )
    absence_internal = run(
        status="EVALUATED_ABSENT",
        claims=(support_claim,),
        mappings=(mapping,),
        decisions=(eligibility,),
        proposals=(proposal,),
        rejected=(
            {"impact_id": "I-GUARD", "reason": "RUBRIC_EDGE_VIOLATION"},
        ),
    )
    absence_provider = run(
        status="EVALUATED_ABSENT",
        claims=(support_claim,),
        mappings=(mapping,),
        decisions=(eligibility,),
        adjudications=(
            {"claim_id": "C-GUARD", "status": "IMPACT_ADJUDICATION_FAIL"},
        ),
    )
    absence_inadequate = run(
        status="EVALUATED_ABSENT",
        proof=False,
    )
    non_scoring_impact = _audit_impact(proposal, support=0.4)
    non_scoring = run(
        status="SUPPORTED_NON_SCORING",
        claims=(support_claim,),
        mappings=(mapping,),
        decisions=(eligibility,),
        proposals=(proposal,),
        impacts=(non_scoring_impact,),
    )
    return {
        "supported_zero_credit": supported_zero,
        "partial_zero_credit": partial_zero,
        "positive_proposal_missing_component": proposal_missing,
        "absence_internal_rejection": absence_internal,
        "absence_provider_failure": absence_provider,
        "absence_inadequate_search": absence_inadequate,
        "non_scoring_with_component_credit": non_scoring,
    }


def _guard_question(
    result: SemanticClosureReconciliationResult,
) -> QuestionComponentReconciliation:
    return next(
        row
        for row in result.reconciliations
        if row.question_family_id == "qualification_pass_lag_reopen"
    )


def _audit_mapping(
    claim_id: str, primitive_id: str, *, direction: str = "SUPPORT"
) -> Mapping[str, Any]:
    return {
        "claim_id": claim_id,
        "primitive_id": primitive_id,
        "support_direction": direction,
        "accepted_by_evidence_os": True,
    }


def _audit_eligibility(
    claim_id: str, component_eligible: bool
) -> Mapping[str, Any]:
    return {
        "claim_id": claim_id,
        "eligibility_decision_id": f"ELIG-{claim_id}",
        "component_scoring_eligibility": component_eligible,
    }


def _audit_proposal(
    impact_id: str,
    claim_id: str,
    question_id: str,
    primitive_id: str,
    component_id: str,
    subcriterion_id: str,
    *,
    direction: str = "SUPPORT",
) -> Mapping[str, Any]:
    return {
        "impact_id": impact_id,
        "claim_id": claim_id,
        "question_family_id": question_id,
        "primitive_id": primitive_id,
        "component_id": component_id,
        "component_subcriterion_id": subcriterion_id,
        "direction": direction,
    }


def _audit_impact(
    proposal: Mapping[str, Any], *, support: float = 0.0, counter: float = 0.0
) -> Mapping[str, Any]:
    return {
        **proposal,
        "eligibility_decision_id": f"ELIG-{proposal['claim_id']}",
        "validated_credit_fraction": max(support, counter),
        "support_credit_fraction": support,
        "counter_effect_fraction": counter,
        "resolution_effect": 0.0,
        "support_type": (
            "PARTIAL_BRIDGE" if support and support < 1 else "RISK_OPEN"
        ),
    }
