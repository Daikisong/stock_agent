"""Issuer보다 좁은 사업부·제품·경제 메커니즘 범위를 검증한다."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping

from e2r.production.metadata import stable_hash


DEFAULT_SCOPE_PATH = Path("configs/e2r_archetype_mechanism_scopes_v1.json")


@dataclass(frozen=True)
class BusinessMechanismScope:
    issuer_id: str
    business_segment: str
    product_family: str
    technology_family: str
    customer_or_counterparty: str
    transaction_type: str
    economic_mechanism: str
    geography: str
    effective_period: str
    scope_confidence: float

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ArchetypeMechanismScopeContract:
    archetype_id: str
    allowed_business_segments: tuple[str, ...]
    allowed_product_families: tuple[str, ...]
    allowed_technology_families: tuple[str, ...]
    allowed_transaction_types: tuple[str, ...]
    allowed_economic_mechanisms: tuple[str, ...]
    generic_company_allowed_components: tuple[str, ...]
    forbidden_business_segments: tuple[str, ...]
    forbidden_product_families: tuple[str, ...]
    reroute_by_segment: Mapping[str, str]
    config_hash: str


@dataclass(frozen=True)
class MechanismScopeValidation:
    status: str
    scope_match: bool
    reason_code: str
    rerouted_archetype_id: str | None
    original_gap_open: bool
    scope: BusinessMechanismScope

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


class MechanismScopeValidator:
    def validate(
        self,
        *,
        scope: BusinessMechanismScope,
        contract: ArchetypeMechanismScopeContract,
        component_id: str,
    ) -> MechanismScopeValidation:
        reason = ""
        if scope.business_segment in contract.forbidden_business_segments:
            reason = "WRONG_BUSINESS_SEGMENT"
        elif scope.product_family in contract.forbidden_product_families:
            reason = "WRONG_PRODUCT_FAMILY"
        elif scope.business_segment == "CORPORATE_GENERIC":
            if component_id not in contract.generic_company_allowed_components:
                reason = "GENERIC_COMPANY_FACT_COMPONENT_NOT_ALLOWED"
            elif scope.economic_mechanism != "INFORMATION_ONLY":
                reason = "GENERIC_COMPANY_FACT_ARCHETYPE_LINK_MISSING"
        elif scope.business_segment not in contract.allowed_business_segments:
            reason = "BUSINESS_SEGMENT_NOT_ALLOWED"
        elif scope.product_family not in contract.allowed_product_families:
            reason = "PRODUCT_FAMILY_NOT_ALLOWED"
        elif scope.technology_family not in contract.allowed_technology_families:
            reason = "TECHNOLOGY_FAMILY_NOT_ALLOWED"
        elif scope.transaction_type not in contract.allowed_transaction_types:
            reason = "TRANSACTION_TYPE_NOT_ALLOWED"
        elif scope.economic_mechanism not in contract.allowed_economic_mechanisms:
            reason = "ECONOMIC_MECHANISM_NOT_ALLOWED"
        if not reason:
            return MechanismScopeValidation(
                status="MECHANISM_SCOPE_PASS",
                scope_match=True,
                reason_code="",
                rerouted_archetype_id=None,
                original_gap_open=False,
                scope=scope,
            )
        reroute = contract.reroute_by_segment.get(scope.business_segment)
        return MechanismScopeValidation(
            status=(
                "REROUTED_TO_OTHER_MECHANISM"
                if reroute
                else "MECHANISM_SCOPE_REJECTED"
            ),
            scope_match=False,
            reason_code=reason,
            rerouted_archetype_id=reroute,
            original_gap_open=True,
            scope=scope,
        )


def load_mechanism_scope_contracts(
    path: str | Path = DEFAULT_SCOPE_PATH,
) -> Mapping[str, ArchetypeMechanismScopeContract]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("schema_version") != "e2r_archetype_mechanism_scopes_v1":
        raise ValueError("mechanism scope schema mismatch")
    result = {}
    for archetype_id, row in (payload.get("contracts") or {}).items():
        base = {
            "archetype_id": str(archetype_id),
            "allowed_business_segments": tuple(row["allowed_business_segments"]),
            "allowed_product_families": tuple(row["allowed_product_families"]),
            "allowed_technology_families": tuple(row["allowed_technology_families"]),
            "allowed_transaction_types": tuple(row["allowed_transaction_types"]),
            "allowed_economic_mechanisms": tuple(row["allowed_economic_mechanisms"]),
            "generic_company_allowed_components": tuple(row["generic_company_allowed_components"]),
            "forbidden_business_segments": tuple(row["forbidden_business_segments"]),
            "forbidden_product_families": tuple(row["forbidden_product_families"]),
            "reroute_by_segment": {
                str(key): str(value)
                for key, value in row["reroute_by_segment"].items()
            },
        }
        result[str(archetype_id)] = ArchetypeMechanismScopeContract(
            **base, config_hash=stable_hash(base)
        )
    return result


def audit_business_mechanism_scope(
    *, repo_root: str | Path = "."
) -> Mapping[str, Any]:
    root = Path(repo_root).resolve()
    contracts = load_mechanism_scope_contracts(root / DEFAULT_SCOPE_PATH)
    c06 = contracts["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]
    rows = []
    filtered_question_rows = []
    for target_id in ("005930", "000660"):
        dossier = (
            root / "output/evidence_to_score/c06/2026-07-11" / target_id
        )
        claims = {
            str(row["claim_id"]): row
            for row in _jsonl(dossier / "accepted_current_claims.jsonl")
        }
        proposals = _jsonl(dossier / "claim_impacts_proposed.jsonl")
        questions = _jsonl(dossier / "question_closure.jsonl")
        for proposal in proposals:
            claim = claims.get(str(proposal.get("claim_id") or ""))
            if claim is None:
                rows.append(
                    {
                        "target_id": target_id,
                        "impact_id": proposal.get("impact_id"),
                        "status": "MECHANISM_SCOPE_MISSING",
                        "reason_code": "CLAIM_MISSING",
                    }
                )
                continue
            scope = infer_business_mechanism_scope(
                claim,
                primitive_id=str(proposal.get("primitive_id") or ""),
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            )
            validation = MechanismScopeValidator().validate(
                scope=scope,
                contract=c06,
                component_id=str(proposal.get("component_id") or ""),
            )
            rows.append(
                {
                    "target_id": target_id,
                    "impact_id": proposal.get("impact_id"),
                    "claim_id": proposal.get("claim_id"),
                    "primitive_id": proposal.get("primitive_id"),
                    "component_id": proposal.get("component_id"),
                    **validation.to_dict(),
                }
            )
        for question in questions:
            for claim_id in question.get("supporting_claim_ids") or ():
                claim = claims.get(str(claim_id))
                if claim is None:
                    continue
                scope = infer_business_mechanism_scope(
                    claim,
                    primitive_id=str(question.get("question_family_id") or ""),
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                )
                if scope.business_segment not in c06.forbidden_business_segments:
                    continue
                filtered_question_rows.append(
                    {
                        "target_id": target_id,
                        "question_family_id": question["question_family_id"],
                        "claim_id": claim_id,
                        "scope": scope.to_dict(),
                        "projected_question_support": False,
                        "original_gap_open": True,
                        "status": "REROUTED_TO_OTHER_MECHANISM",
                    }
                )
    accepted_rows = [row for row in rows if row.get("scope_match") is True]
    failed_rows = [row for row in rows if row.get("scope_match") is False]
    critical = {
        "cross_business_question_closure_count": sum(
            row.get("projected_question_support") is True
            for row in filtered_question_rows
        ),
        "same_issuer_wrong_segment_credit_count": sum(
            row.get("scope", {}).get("business_segment")
            in c06.forbidden_business_segments
            for row in accepted_rows
        ),
        "foundry_to_hbm_allocation_count": sum(
            row.get("scope", {}).get("business_segment") == "FOUNDRY"
            and row.get("scope_match") is True
            for row in rows
        ),
        "adjacent_product_to_target_capacity_count": sum(
            row.get("scope", {}).get("product_family")
            == "PACKAGE_SUBSTRATE_ADJACENT"
            and row.get("component_id")
            in {"earnings_visibility", "bottleneck_pricing"}
            and row.get("scope_match") is True
            for row in rows
        ),
        "mechanism_scope_missing_count": sum(
            row.get("status") == "MECHANISM_SCOPE_MISSING" for row in rows
        ),
    }
    critical_sum = sum(critical.values())
    return {
        "schema_version": "e2r_business_mechanism_scope_audit_v1",
        "status": (
            "BUSINESS_MECHANISM_SCOPE_PASS"
            if critical_sum == 0
            else "BUSINESS_MECHANISM_SCOPE_FAIL"
        ),
        "contract_count": len(contracts),
        "evaluated_impact_count": len(rows),
        "scope_pass_impact_count": len(accepted_rows),
        "wrong_scope_rejected_impact_count": len(failed_rows),
        "filtered_question_claim_count": len(filtered_question_rows),
        "scope_rows": rows,
        "filtered_question_rows": filtered_question_rows,
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
    }


def infer_business_mechanism_scope(
    claim: Mapping[str, Any], *, primitive_id: str, archetype_id: str
) -> BusinessMechanismScope:
    raw = claim.get("raw_assertion") or {}
    text = " ".join(
        str(value or "")
        for value in (
            raw.get("predicate"),
            raw.get("object_text"),
            claim.get("exact_quote"),
            claim.get("adjudication_rationale"),
            primitive_id,
        )
    ).casefold()
    if any(token in text for token in ("foundry", "위탁생산")):
        segment, product, technology = "FOUNDRY", "LOGIC_FOUNDRY", "FOUNDRY"
    elif archetype_id == "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY":
        segment, product, technology = (
            "SEMICONDUCTOR_COMPONENT",
            "SEMI_TEST_SOCKET",
            "SEMICONDUCTOR_TEST",
        )
    elif archetype_id == "C15_MATERIAL_SPREAD_SUPERCYCLE":
        segment, product, technology = (
            "MATERIALS",
            "MATERIAL_COMMODITY",
            "COMMODITY_SPREAD",
        )
    elif "hbm" in text or "ai memory" in text:
        segment, product, technology = "MEMORY", "HBM", "HBM"
    elif "nand" in text:
        segment, product, technology = "MEMORY", "NAND", "MEMORY"
    elif any(token in text for token in ("dram", "d램", "lpddr", "socamm")):
        segment, product, technology = "MEMORY", "DRAM", "DRAM"
    elif any(token in text for token in ("memory", "메모리")):
        segment, product, technology = "MEMORY", "MEMORY_GENERIC", "MEMORY"
    else:
        segment, product, technology = (
            "CORPORATE_GENERIC",
            "CORPORATE_GENERIC",
            "CORPORATE_GENERIC",
        )
    if archetype_id == "C15_MATERIAL_SPREAD_SUPERCYCLE" and "spread" in primitive_id:
        transaction, mechanism = "PRICING_ACTUAL", "MARGIN_SPREAD"
    elif archetype_id == "C15_MATERIAL_SPREAD_SUPERCYCLE" and "pricing" in primitive_id:
        transaction, mechanism = "PRICING_ACTUAL", "ISSUER_PASS_THROUGH"
    elif archetype_id == "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY" and any(
        token in primitive_id for token in ("customer", "order", "qualification")
    ):
        transaction, mechanism = "CUSTOMER_COMMITMENT", "NAMED_CUSTOMER_ORDER"
    else:
        transaction, mechanism = _transaction_and_mechanism(text, primitive_id)
    counterparty = "Tesla" if "tesla" in text else ""
    period = "/".join(
        str(value or "")
        for value in (
            claim.get("effective_start"),
            claim.get("effective_end"),
            claim.get("event_date"),
        )
        if value
    )
    return BusinessMechanismScope(
        issuer_id=str(
            claim.get("target_id") or claim.get("target_entity_id") or ""
        ),
        business_segment=segment,
        product_family=product,
        technology_family=technology,
        customer_or_counterparty=counterparty,
        transaction_type=transaction,
        economic_mechanism=mechanism,
        geography=str(raw.get("geography") or "UNSPECIFIED"),
        effective_period=period or "CURRENT_UNSPECIFIED",
        scope_confidence=0.95 if segment != "CORPORATE_GENERIC" else 0.5,
    )


def _transaction_and_mechanism(text: str, primitive_id: str) -> tuple[str, str]:
    joined = f"{text} {primitive_id}".casefold()
    if any(token in joined for token in ("valuation", "earnings multiple", "p/e", "밸류에이션")):
        return "VALUATION_ANALYSIS", "VALUATION_EARNINGS_BRIDGE"
    if any(token in joined for token in ("consensus", "expectation gap", "컨센서스", "기대 격차")):
        return "VALUATION_ANALYSIS", "MARKET_EXPECTATION_GAP"
    if any(token in joined for token in ("qualification", "qualif", "인증")):
        return "QUALIFICATION", "QUALIFICATION_EXECUTION"
    if any(token in joined for token in ("allocation", "preorder", "contract", "배정", "계약")):
        return "CUSTOMER_COMMITMENT", "CUSTOMER_ALLOCATION"
    if any(token in joined for token in ("shipment", "mass production", "출하", "양산")):
        return "PRODUCT_SHIPMENT", "PRODUCT_COMMERCIALIZATION"
    if any(token in joined for token in ("asp", "price", "pricing", "가격", "판매가격")):
        return "PRICING_ACTUAL", "PRICING_POWER"
    if any(token in joined for token in ("capacity", "capa", "capex", "invest", "투자")):
        return "CAPACITY_INVESTMENT", "SUPPLY_RESPONSE"
    if any(token in joined for token in ("revenue", "profit", "margin", "fcf", "매출", "이익")):
        return "REVENUE_ACTUAL", "REVENUE_CONVERSION"
    if any(token in joined for token in ("risk", "counter", "lag", "drag")):
        return "RISK", "RISK_COUNTER"
    if any(token in joined for token in ("profile", "spec", "product")):
        return "PRODUCT_PROFILE", "INFORMATION_ONLY"
    return "GENERIC_INFORMATION", "INFORMATION_ONLY"


def _jsonl(path: Path) -> list[Mapping[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


__all__ = [
    "ArchetypeMechanismScopeContract",
    "BusinessMechanismScope",
    "DEFAULT_SCOPE_PATH",
    "MechanismScopeValidation",
    "MechanismScopeValidator",
    "audit_business_mechanism_scope",
    "infer_business_mechanism_scope",
    "load_mechanism_scope_contracts",
]
