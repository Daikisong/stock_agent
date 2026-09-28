"""Fail-closed totality and semantic validation for V2 research contracts."""

from __future__ import annotations

from collections import Counter
from typing import Any, Mapping, Sequence


CONTRACT_SCHEMA = "e2r_archetype_research_contract_v2"
CATALOG_SCHEMA = "e2r_archetype_research_contract_catalog_v2"
TERMINAL_STATUSES = frozenset(
    {
        "SUPPORTED_SCORING",
        "PARTIALLY_SUPPORTED_SCORING",
        "SUPPORTED_NON_SCORING",
        "COUNTER_SUPPORTED",
        "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
        "LIKELY_NONPUBLIC",
        "FUTURE_EVENT_ONLY",
        "NOT_APPLICABLE_WITH_REASON",
    }
)
CONTRACT_FIELDS = frozenset(
    {
        "schema_version",
        "archetype_id",
        "contract_role",
        "large_sector_id",
        "runtime_bridge_group",
        "economic_mechanism",
        "required_primitives",
        "green_gate_primitives",
        "guard_primitives",
        "required_bridge_axes",
        "question_families",
        "source_role_policy",
        "source_quorum",
        "freshness_policy",
        "supersession_policy",
        "false_positive_guards",
        "hard_break_policy",
        "component_mapping",
        "adequate_search_policy",
        "historical_contract_lineage",
        "prompt_contract_version",
        "score_authority",
        "stage_authority",
    }
)
QUESTION_FIELDS = frozenset(
    {
        "question_family_id",
        "question_text",
        "economic_need",
        "mandatory_for_full_thesis",
        "required_primitives",
        "support_predicates",
        "partial_support_predicates",
        "counter_predicates",
        "non_scoring_predicates",
        "required_source_roles",
        "preferred_source_families",
        "required_independence",
        "freshness_days",
        "supersession_rule",
        "affected_component_ids",
        "could_change_score",
        "could_change_stage",
        "could_change_hard_break",
        "allowed_terminal_statuses",
        "adequate_search_requirements",
        "false_positive_guards",
    }
)
COUNTER_ROLES = frozenset({"COUNTER_HARD_BREAK", "LIFECYCLE_SUPERSESSION"})


class ContractValidationError(ValueError):
    pass


def validate_contract_catalog(payload: Mapping[str, Any]) -> None:
    if payload.get("schema_version") != CATALOG_SCHEMA:
        raise ContractValidationError("unsupported research contract catalog schema")
    contracts = payload.get("contracts")
    if not isinstance(contracts, Sequence) or isinstance(contracts, (str, bytes)):
        raise ContractValidationError("research contract catalog requires a list")
    if payload.get("contract_count") != len(contracts):
        raise ContractValidationError("declared research contract count is inconsistent")
    if len(contracts) != 36:
        raise ContractValidationError("research contract catalog must contain exactly 36 records")
    ids = [str(row.get("archetype_id") or "") for row in contracts]
    if len(set(ids)) != len(ids):
        raise ContractValidationError("research contract ids must be unique")
    for contract in contracts:
        if not isinstance(contract, Mapping):
            raise ContractValidationError("research contract must be an object")
        validate_research_contract(contract)
    _validate_no_generic_filler(contracts)


def validate_research_contract(contract: Mapping[str, Any]) -> None:
    missing = CONTRACT_FIELDS - set(contract)
    if missing:
        raise ContractValidationError(
            f"{contract.get('archetype_id')}: missing contract fields {sorted(missing)}"
        )
    archetype_id = str(contract["archetype_id"])
    if contract["schema_version"] != CONTRACT_SCHEMA:
        raise ContractValidationError(f"{archetype_id}: invalid contract schema")
    role = contract["contract_role"]
    if role not in {"PRIMARY", "CROSS_GUARD"}:
        raise ContractValidationError(f"{archetype_id}: invalid contract role")
    if contract["prompt_contract_version"] != "v2":
        raise ContractValidationError(f"{archetype_id}: prompt contract must be v2")
    if contract["score_authority"] is not False or contract["stage_authority"] is not False:
        raise ContractValidationError(f"{archetype_id}: Pro cannot own score or Stage")
    questions = contract["question_families"]
    if not isinstance(questions, list) or len(questions) < 5:
        raise ContractValidationError(f"{archetype_id}: at least five questions required")
    question_ids: list[str] = []
    mapped: set[str] = set()
    counter_mapped: set[str] = set()
    roles: set[str] = set()
    for question in questions:
        if not isinstance(question, Mapping):
            raise ContractValidationError(f"{archetype_id}: question must be an object")
        missing_question = QUESTION_FIELDS - set(question)
        if missing_question:
            raise ContractValidationError(
                f"{archetype_id}: question missing fields {sorted(missing_question)}"
            )
        question_id = str(question["question_family_id"])
        question_ids.append(question_id)
        if not str(question["question_text"]).strip():
            raise ContractValidationError(f"{archetype_id}: empty question text")
        if not question["required_source_roles"]:
            raise ContractValidationError(f"{question_id}: source role is required")
        question_roles = {
            str(value)
            for value in (
                question.get("question_roles")
                or (question.get("question_role"),)
            )
            if value
        }
        guard_only = "GUARD_ONLY" in question_roles
        if not question["affected_component_ids"] and not guard_only:
            raise ContractValidationError(
                f"{question_id}: affected component or GUARD_ONLY role required"
            )
        statuses = set(question["allowed_terminal_statuses"])
        if not statuses or not statuses.issubset(TERMINAL_STATUSES):
            raise ContractValidationError(f"{question_id}: invalid terminal statuses")
        primitives = {str(value) for value in question["required_primitives"]}
        mapped.update(primitives)
        roles.update(question_roles)
        if question_roles.intersection(COUNTER_ROLES | {"GUARD_ONLY"}) or question.get("could_change_hard_break") is True:
            counter_mapped.update(primitives)
    if len(set(question_ids)) != len(question_ids):
        raise ContractValidationError(f"{archetype_id}: duplicate question ids")
    required = {str(value) for value in contract["required_primitives"]}
    green = {str(value) for value in contract["green_gate_primitives"]}
    guards = {str(value) for value in contract["guard_primitives"]}
    if required - mapped:
        raise ContractValidationError(
            f"{archetype_id}: required primitives unmapped {sorted(required - mapped)}"
        )
    if green - mapped:
        raise ContractValidationError(
            f"{archetype_id}: green primitives unmapped {sorted(green - mapped)}"
        )
    if guards - counter_mapped:
        raise ContractValidationError(
            f"{archetype_id}: guard primitives lack counter question {sorted(guards - counter_mapped)}"
        )
    if not contract["adequate_search_policy"]:
        raise ContractValidationError(f"{archetype_id}: adequate-search policy required")
    if role == "PRIMARY":
        if len(questions) < 5 or "ECONOMIC_BRIDGE" not in roles:
            raise ContractValidationError(f"{archetype_id}: positive bridge question missing")
        if not roles.intersection(COUNTER_ROLES):
            raise ContractValidationError(f"{archetype_id}: counter/lifecycle question missing")
        if "FINANCIAL_CASH_CONVERSION" not in roles:
            raise ContractValidationError(f"{archetype_id}: financial/cash question missing")
        if "LIFECYCLE_SUPERSESSION" not in roles:
            raise ContractValidationError(f"{archetype_id}: lifecycle question missing")
        valuation = contract.get("valuation_research_policy") or {}
        if (
            "EXPECTATION_VALUATION" not in roles
            and valuation.get("status") != "NOT_APPLICABLE_WITH_REASON"
        ):
            raise ContractValidationError(
                f"{archetype_id}: valuation question or explicit N/A policy required"
            )


def _validate_no_generic_filler(contracts: Sequence[Mapping[str, Any]]) -> None:
    primary_signatures = []
    question_texts = []
    for contract in contracts:
        texts = tuple(
            _normalize_text(str(row["question_text"]))
            for row in contract["question_families"]
        )
        question_texts.extend(texts)
        if contract["contract_role"] == "PRIMARY":
            primary_signatures.append(texts)
    if len(set(primary_signatures)) != len(primary_signatures):
        raise ContractValidationError("generic copied primary question roster detected")
    duplicates = [text for text, count in Counter(question_texts).items() if count > 1]
    if duplicates:
        raise ContractValidationError("duplicate generic question text detected")


def _normalize_text(value: str) -> str:
    return "".join(character.casefold() for character in value if character.isalnum())


__all__ = [
    "CATALOG_SCHEMA",
    "CONTRACT_SCHEMA",
    "ContractValidationError",
    "TERMINAL_STATUSES",
    "validate_contract_catalog",
    "validate_research_contract",
]
