"""Question family별 claim·primitive·component 성공 의미를 계약화한다."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash


DEFAULT_QUESTION_CONTRACT_PATH = Path(
    "configs/e2r_question_impact_contracts_v1.json"
)
QUESTION_CLOSURE_STATUSES = {
    "SUPPORTED_SCORING",
    "PARTIALLY_SUPPORTED_SCORING",
    "SUPPORTED_NON_SCORING",
    "COUNTER_SUPPORTED",
    "EVALUATED_ABSENT",
    "SOURCE_PENDING",
    "PROVIDER_PENDING",
    "BUDGET_PENDING",
}


@dataclass(frozen=True)
class QuestionImpactContract:
    question_family_id: str
    archetype_id: str
    mechanism_scope: str
    accepted_claim_predicates: tuple[str, ...]
    allowed_primitive_ids: tuple[str, ...]
    allowed_component_ids: tuple[str, ...]
    partial_support_predicates: tuple[str, ...]
    counter_predicates: tuple[str, ...]
    non_scoring_support_predicates: tuple[str, ...]
    required_source_routes: tuple[str, ...]
    required_counter_routes: tuple[str, ...]
    terminal_absence_policy: str
    required_keyword_groups: tuple[tuple[str, ...], ...]
    full_support_keywords: tuple[str, ...]
    partial_keywords: tuple[str, ...]
    counter_keywords: tuple[str, ...]
    contract_hash: str

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


def load_question_impact_contracts(
    path: str | Path = DEFAULT_QUESTION_CONTRACT_PATH,
) -> Mapping[str, QuestionImpactContract]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("schema_version") != "e2r_question_impact_contracts_v1":
        raise ValueError("question impact contract schema mismatch")
    result = {}
    for row in payload.get("contracts") or ():
        base = {
            "question_family_id": str(row["question_family_id"]),
            "archetype_id": str(row["archetype_id"]),
            "mechanism_scope": str(row["mechanism_scope"]),
            "accepted_claim_predicates": tuple(row["accepted_claim_predicates"]),
            "allowed_primitive_ids": tuple(row["allowed_primitive_ids"]),
            "allowed_component_ids": tuple(row["allowed_component_ids"]),
            "partial_support_predicates": tuple(row["partial_support_predicates"]),
            "counter_predicates": tuple(row["counter_predicates"]),
            "non_scoring_support_predicates": tuple(row["non_scoring_support_predicates"]),
            "required_source_routes": tuple(row["required_source_routes"]),
            "required_counter_routes": tuple(row["required_counter_routes"]),
            "terminal_absence_policy": str(row["terminal_absence_policy"]),
            "required_keyword_groups": tuple(
                tuple(str(value).casefold() for value in group)
                for group in row["required_keyword_groups"]
            ),
            "full_support_keywords": tuple(
                str(value).casefold()
                for value in row["full_support_keywords"]
            ),
            "partial_keywords": tuple(
                str(value).casefold() for value in row["partial_keywords"]
            ),
            "counter_keywords": tuple(
                str(value).casefold() for value in row["counter_keywords"]
            ),
        }
        contract = QuestionImpactContract(
            **base, contract_hash=stable_hash(base)
        )
        if contract.question_family_id in result:
            raise ValueError("duplicate question impact contract")
        if (
            not contract.allowed_primitive_ids
            or not contract.allowed_component_ids
            or not contract.required_source_routes
            or not contract.required_counter_routes
            or not contract.full_support_keywords
            or contract.terminal_absence_policy != "REQUIRE_ADEQUATE_SEARCH"
        ):
            raise ValueError("question impact contract is incomplete")
        result[contract.question_family_id] = contract
    return result


def compile_question_closures_v2(
    *,
    contracts: Mapping[str, QuestionImpactContract],
    claims: Sequence[Mapping[str, Any]],
    primitive_mappings: Sequence[Mapping[str, Any]],
    eligibility_decisions: Sequence[Mapping[str, Any]],
    prior_closures: Sequence[Mapping[str, Any]] = (),
    validated_impacts: Sequence[Any] | None = None,
) -> tuple[Mapping[str, Any], ...]:
    claims_by_id = {
        str(row.get("claim_id") or ""): row for row in claims
    }
    eligibility = {
        str(row.get("claim_id") or ""): row for row in eligibility_decisions
    }
    mappings_by_claim: dict[str, list[Mapping[str, Any]]] = {}
    for row in primitive_mappings:
        if row.get("accepted_by_evidence_os") is True:
            mappings_by_claim.setdefault(
                str(row.get("claim_id") or ""), []
            ).append(row)
    prior_by_family = {
        str(row.get("question_family_id") or ""): row
        for row in prior_closures
    }
    impacts_by_claim: dict[str, list[Any]] = {}
    if validated_impacts is not None:
        for impact in validated_impacts:
            impacts_by_claim.setdefault(
                str(_impact_value(impact, "claim_id") or ""), []
            ).append(impact)
    results = []
    for question_id, contract in contracts.items():
        scoring_ids = []
        partial_ids = []
        non_scoring_ids = []
        counter_ids = []
        accepted_mapping_ids = []
        for claim_id, claim in claims_by_id.items():
            matching_mappings = [
                row
                for row in mappings_by_claim.get(claim_id, ())
                if str(row.get("primitive_id") or "")
                in contract.allowed_primitive_ids
            ]
            if not matching_mappings:
                continue
            accepted_mapping_ids.extend(
                str(row.get("mapping_id") or "") for row in matching_mappings
            )
            decision = eligibility.get(claim_id, {})
            text = _claim_text(claim)
            counter = any(
                str(row.get("support_direction") or "").upper() == "COUNTER"
                for row in matching_mappings
            ) or _contains_any(text, contract.counter_keywords)
            if counter and decision.get("risk_scoring_eligibility") is True:
                counter_ids.append(claim_id)
                continue
            if decision.get("component_scoring_eligibility") is not True:
                non_scoring_ids.append(claim_id)
                continue
            has_validated_scoring_impact = False
            if validated_impacts is not None:
                has_validated_scoring_impact = _has_scoring_impact(
                    claim_id=claim_id,
                    matching_mappings=matching_mappings,
                    impacts_by_claim=impacts_by_claim,
                    contract=contract,
                )
                if not has_validated_scoring_impact:
                    non_scoring_ids.append(claim_id)
                    continue
            full_match = all(
                _contains_any(text, group)
                for group in contract.required_keyword_groups
            ) and _contains_any(text, contract.full_support_keywords)
            partial_match = _contains_any(text, contract.partial_keywords)
            if full_match:
                scoring_ids.append(claim_id)
            elif partial_match or has_validated_scoring_impact:
                partial_ids.append(claim_id)
            else:
                non_scoring_ids.append(claim_id)
        prior = prior_by_family.get(question_id, {})
        if scoring_ids:
            status = "SUPPORTED_SCORING"
            supporting = scoring_ids
        elif partial_ids:
            status = "PARTIALLY_SUPPORTED_SCORING"
            supporting = partial_ids
        elif counter_ids:
            status = "COUNTER_SUPPORTED"
            supporting = []
        elif non_scoring_ids:
            status = "SUPPORTED_NON_SCORING"
            supporting = []
        elif prior.get("status") in {
            "SOURCE_PENDING",
            "PROVIDER_PENDING",
            "BUDGET_PENDING",
        }:
            status = str(prior["status"])
            supporting = []
        else:
            status = "EVALUATED_ABSENT"
            supporting = []
        result = {
            "question_family_id": question_id,
            "archetype_id": contract.archetype_id,
            "question_contract_hash": contract.contract_hash,
            "status": status,
            "supporting_claim_ids": list(dict.fromkeys(supporting)),
            "partial_supporting_claim_ids": list(dict.fromkeys(partial_ids)),
            "non_scoring_claim_ids": list(dict.fromkeys(non_scoring_ids)),
            "counter_claim_ids": list(dict.fromkeys(counter_ids)),
            "eligibility_decision_ids": [
                str(eligibility[claim_id]["eligibility_decision_id"])
                for claim_id in dict.fromkeys((*supporting, *counter_ids))
                if claim_id in eligibility
            ],
            "candidate_eligibility_decision_ids": [
                str(eligibility[claim_id]["eligibility_decision_id"])
                for claim_id in dict.fromkeys(
                    (*scoring_ids, *partial_ids, *non_scoring_ids, *counter_ids)
                )
                if claim_id in eligibility
            ],
            "accepted_mapping_ids": list(dict.fromkeys(accepted_mapping_ids)),
            "allowed_primitive_ids": list(contract.allowed_primitive_ids),
            "allowed_component_ids": list(contract.allowed_component_ids),
            "search_exhaustion_proof": list(
                prior.get("search_exhaustion_proof") or ()
            ),
            "failure_class": prior.get("failure_class"),
            "next_action": prior.get("next_action"),
            "source_task_id": prior.get("source_task_id"),
            "target_id": prior.get("target_id"),
        }
        if status not in QUESTION_CLOSURE_STATUSES:
            raise ValueError("unknown question closure v2 status")
        results.append(result)
    return tuple(results)


def audit_question_impact_contracts(
    *, repo_root: str | Path = "."
) -> Mapping[str, Any]:
    root = Path(repo_root).resolve()
    contracts = load_question_impact_contracts(
        root / DEFAULT_QUESTION_CONTRACT_PATH
    )
    closure_rows = []
    all_decisions = []
    for target_id in ("005930", "000660"):
        dossier = (
            root / "output/evidence_to_score/c06/2026-07-11" / target_id
        )
        claims = _jsonl(dossier / "accepted_current_claims.jsonl")
        provenance = _jsonl(dossier / "claim_provenance.jsonl")
        from .claim_eligibility import compile_claim_eligibility_decisions

        decisions = tuple(
            {**decision.to_dict(), "target_id": target_id}
            for decision in compile_claim_eligibility_decisions(
                claims=claims,
                claim_provenance=provenance,
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            )
        )
        all_decisions.extend(decisions)
        target_closures = compile_question_closures_v2(
            contracts=contracts,
            claims=claims,
            primitive_mappings=_jsonl(dossier / "primitive_mappings.jsonl"),
            eligibility_decisions=decisions,
            prior_closures=_jsonl(dossier / "question_closure.jsonl"),
            validated_impacts=_jsonl(
                dossier / "claim_impacts_validated.jsonl"
            ),
        )
        closure_rows.extend(
            {**row, "target_id": target_id} for row in target_closures
        )
    decision_by_claim = {
        (str(row["target_id"]), str(row["claim_id"])): row
        for row in all_decisions
    }
    scoring_statuses = {
        "SUPPORTED_SCORING",
        "PARTIALLY_SUPPORTED_SCORING",
    }
    wrong_mechanism = 0
    non_scoring_as_scoring = 0
    for row in closure_rows:
        if row["status"] not in scoring_statuses:
            continue
        scoring_claim_ids = dict.fromkeys(
            (
                *(row.get("supporting_claim_ids") or ()),
                *(row.get("partial_supporting_claim_ids") or ()),
            )
        )
        for claim_id in scoring_claim_ids:
            decision = decision_by_claim[(row["target_id"], claim_id)]
            wrong_mechanism += int(
                decision["eligibility_status"]
                == "INELIGIBLE_WRONG_MECHANISM"
            )
            non_scoring_as_scoring += int(
                decision["component_scoring_eligibility"] is not True
            )
    expected_questions = {
        "current_customer_allocation_commitment",
        "capacity_constraint_presold_status",
        "qualification_pass_lag_reopen",
        "shipment_mass_production_generation",
        "hbm_ai_memory_revenue_mix",
        "asp_pricing_actual",
        "revenue_operating_profit_conversion",
        "margin_fcf_conversion",
        "medium_term_revision_consensus",
        "valuation_market_expectation",
        "conventional_memory_drag",
        "capex_supply_oversupply",
        "customer_concentration_dependency",
    }
    critical = {
        "question_supported_by_wrong_mechanism_count": wrong_mechanism,
        "question_supported_by_non_scoring_claim_count": non_scoring_as_scoring,
        "question_contract_missing_count": len(
            expected_questions ^ set(contracts)
        ),
    }
    critical_sum = sum(critical.values())
    return {
        "schema_version": "e2r_question_impact_contract_audit_v1",
        "status": (
            "QUESTION_IMPACT_CONTRACT_PASS"
            if critical_sum == 0
            else "QUESTION_IMPACT_CONTRACT_FAIL"
        ),
        "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        "question_contract_count": len(contracts),
        "contracts": {
            key: {
                **value.to_dict(),
                "accepted_claim_predicates": list(value.accepted_claim_predicates),
                "allowed_primitive_ids": list(value.allowed_primitive_ids),
                "allowed_component_ids": list(value.allowed_component_ids),
                "partial_support_predicates": list(value.partial_support_predicates),
                "counter_predicates": list(value.counter_predicates),
                "non_scoring_support_predicates": list(value.non_scoring_support_predicates),
                "required_source_routes": list(value.required_source_routes),
                "required_counter_routes": list(value.required_counter_routes),
                "required_keyword_groups": [
                    list(group) for group in value.required_keyword_groups
                ],
                "full_support_keywords": list(value.full_support_keywords),
                "partial_keywords": list(value.partial_keywords),
                "counter_keywords": list(value.counter_keywords),
            }
            for key, value in contracts.items()
        },
        "projected_question_closures": closure_rows,
        "status_counts": dict(
            sorted(
                __import__("collections").Counter(
                    str(row["status"]) for row in closure_rows
                ).items()
            )
        ),
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
    }


def _claim_text(claim: Mapping[str, Any]) -> str:
    raw = claim.get("raw_assertion") or {}
    return " ".join(
        str(value or "")
        for value in (
            raw.get("predicate"),
            raw.get("object_text"),
            claim.get("exact_quote"),
            claim.get("adjudication_rationale"),
        )
    ).casefold()


def _contains_any(text: str, tokens: Sequence[str]) -> bool:
    return any(str(token).casefold() in text for token in tokens)


def _impact_value(impact: Any, name: str) -> Any:
    if isinstance(impact, Mapping):
        return impact.get(name)
    return getattr(impact, name, None)


def _has_scoring_impact(
    *,
    claim_id: str,
    matching_mappings: Sequence[Mapping[str, Any]],
    impacts_by_claim: Mapping[str, Sequence[Any]],
    contract: QuestionImpactContract,
) -> bool:
    mapping_ids = {
        str(row.get("mapping_id") or "") for row in matching_mappings
    }
    for impact in impacts_by_claim.get(claim_id, ()):
        impact_question_id = str(
            _impact_value(impact, "question_family_id") or ""
        )
        if (
            impact_question_id
            and impact_question_id != contract.question_family_id
        ):
            continue
        lineage = {
            str(value)
            for value in (_impact_value(impact, "lineage_mapping_ids") or ())
        }
        if not (
            str(_impact_value(impact, "mapping_id") or "") in mapping_ids
            or lineage.intersection(mapping_ids)
        ):
            continue
        if str(_impact_value(impact, "primitive_id") or "") not in set(
            contract.allowed_primitive_ids
        ):
            continue
        if str(_impact_value(impact, "component_id") or "") not in set(
            contract.allowed_component_ids
        ):
            continue
        if str(_impact_value(impact, "direction") or "").upper() not in {
            "SUPPORT",
            "RESOLUTION",
        }:
            continue
        credit = _impact_value(impact, "validated_credit_fraction")
        if (
            credit is None
            or float(credit) > 0
            or (
                _impact_value(impact, "corroboration_only") is True
                and bool(_impact_value(impact, "duplicate_reason"))
            )
        ):
            return True
    return False


def _jsonl(path: Path) -> list[Mapping[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


__all__ = [
    "DEFAULT_QUESTION_CONTRACT_PATH",
    "QUESTION_CLOSURE_STATUSES",
    "QuestionImpactContract",
    "audit_question_impact_contracts",
    "compile_question_closures_v2",
    "load_question_impact_contracts",
]
