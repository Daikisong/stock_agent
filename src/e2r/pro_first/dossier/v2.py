"""Deterministic V2 question-closure and route-receipt semantics."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping, Sequence

from ..research_contracts import select_contract_bundle
from ..research_contracts.validator import TERMINAL_STATUSES


DOSSIER_V2_SCHEMA_VERSION = "e2r_pro_research_dossier_v2"


class QuestionStatus(str, Enum):
    SUPPORTED_SCORING = "SUPPORTED_SCORING"
    PARTIALLY_SUPPORTED_SCORING = "PARTIALLY_SUPPORTED_SCORING"
    SUPPORTED_NON_SCORING = "SUPPORTED_NON_SCORING"
    COUNTER_SUPPORTED = "COUNTER_SUPPORTED"
    EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH = "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH"
    LIKELY_NONPUBLIC = "LIKELY_NONPUBLIC"
    FUTURE_EVENT_ONLY = "FUTURE_EVENT_ONLY"
    NOT_APPLICABLE_WITH_REASON = "NOT_APPLICABLE_WITH_REASON"
    PUBLIC_SEARCHABLE = "PUBLIC_SEARCHABLE"
    UNKNOWN_ROUTE_NOT_YET_TESTED = "UNKNOWN_ROUTE_NOT_YET_TESTED"
    CONTRADICTED_UNRESOLVED = "CONTRADICTED_UNRESOLVED"
    SOURCE_PENDING = "SOURCE_PENDING"
    PROVIDER_PENDING = "PROVIDER_PENDING"
    PARSER_PENDING = "PARSER_PENDING"
    VERIFIER_REPAIR_REQUIRED = "VERIFIER_REPAIR_REQUIRED"


class AvailabilityClass(str, Enum):
    PUBLIC_SEARCHABLE = "PUBLIC_SEARCHABLE"
    LIKELY_NONPUBLIC = "LIKELY_NONPUBLIC"
    FUTURE_EVENT_ONLY = "FUTURE_EVENT_ONLY"
    PROVIDER_BLOCKED = "PROVIDER_BLOCKED"
    PARSER_BLOCKED = "PARSER_BLOCKED"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    UNKNOWN_ROUTE_NOT_YET_TESTED = "UNKNOWN_ROUTE_NOT_YET_TESTED"


class ResearchPassName(str, Enum):
    ARCHETYPE_CONFIRMATION = "ARCHETYPE_CONFIRMATION"
    PRIMARY_OFFICIAL_RESEARCH = "PRIMARY_OFFICIAL_RESEARCH"
    ECOSYSTEM_COUNTER_RESEARCH = "ECOSYSTEM_COUNTER_RESEARCH"
    REVISION_VALUATION_RESEARCH = "REVISION_VALUATION_RESEARCH"
    QUESTION_CLOSURE_AUDIT = "QUESTION_CLOSURE_AUDIT"
    PUBLIC_GAP_CLOSURE = "PUBLIC_GAP_CLOSURE"
    COUNTER_SUPERSESSION_CLOSURE = "COUNTER_SUPERSESSION_CLOSURE"
    SOURCE_VERIFICATION = "SOURCE_VERIFICATION"
    VERIFIER_REPAIR = "VERIFIER_REPAIR"
    SATURATION_AUDIT = "SATURATION_AUDIT"
    FULL_THESIS_READY = "FULL_THESIS_READY"


@dataclass(frozen=True)
class DossierV2ClosureSummary:
    expected_mandatory_question_ids: tuple[str, ...]
    reported_question_ids: tuple[str, ...]
    missing_mandatory_question_ids: tuple[str, ...]
    nonterminal_mandatory_question_ids: tuple[str, ...]
    public_searchable_question_ids: tuple[str, ...]
    counter_supersession_pending_question_ids: tuple[str, ...]
    verifier_repair_pending_question_ids: tuple[str, ...]
    provider_parser_pending_question_ids: tuple[str, ...]
    likely_nonpublic_question_ids: tuple[str, ...]

    @property
    def full_thesis_question_closure(self) -> bool:
        return not (
            self.missing_mandatory_question_ids
            or self.nonterminal_mandatory_question_ids
            or self.verifier_repair_pending_question_ids
            or self.provider_parser_pending_question_ids
        )

    @property
    def expected_research_status(self) -> str:
        if self.provider_parser_pending_question_ids:
            return "PROVIDER_PENDING"
        if self.verifier_repair_pending_question_ids:
            return "NEEDS_VERIFIER_REPAIR"
        if self.public_searchable_question_ids or self.missing_mandatory_question_ids:
            return "NEEDS_PUBLIC_GAP_CLOSURE"
        if self.counter_supersession_pending_question_ids:
            return "NEEDS_COUNTER_SUPERSESSION"
        if self.nonterminal_mandatory_question_ids:
            return "NEEDS_PUBLIC_GAP_CLOSURE"
        if self.likely_nonpublic_question_ids:
            return "COMPLETE_WITH_LIKELY_NONPUBLIC_REMAINDER"
        return "COMPLETE"


def compile_dossier_v2_closure_summary(
    payload: Mapping[str, Any],
) -> DossierV2ClosureSummary:
    selected = tuple(str(value) for value in payload.get("selected_archetypes") or ())
    bundle = select_contract_bundle(selected)
    expected = tuple(
        str(question["question_family_id"])
        for contract in bundle.contracts
        for question in contract["question_families"]
        if question["mandatory_for_full_thesis"] is True
    )
    results = tuple(payload.get("question_family_results") or ())
    by_id = {
        str(row.get("question_family_id") or ""): row
        for row in results
    }
    reported = tuple(by_id)
    missing = tuple(value for value in expected if value not in by_id)
    nonterminal = tuple(
        value
        for value in expected
        if value in by_id and str(by_id[value].get("status") or "") not in TERMINAL_STATUSES
    )
    public = tuple(
        value
        for value in expected
        if value in by_id
        and by_id[value].get("status")
        in {"PUBLIC_SEARCHABLE", "UNKNOWN_ROUTE_NOT_YET_TESTED", "SOURCE_PENDING"}
    )
    counter = tuple(
        value
        for value in expected
        if value in by_id and by_id[value].get("status") == "CONTRADICTED_UNRESOLVED"
    )
    repair = tuple(
        value
        for value in expected
        if value in by_id and by_id[value].get("status") == "VERIFIER_REPAIR_REQUIRED"
    )
    provider = tuple(
        value
        for value in expected
        if value in by_id
        and (
            by_id[value].get("status") in {"PROVIDER_PENDING", "PARSER_PENDING"}
            or by_id[value].get("availability_class")
            in {"PROVIDER_BLOCKED", "PARSER_BLOCKED"}
        )
    )
    likely = tuple(
        value
        for value in expected
        if value in by_id
        and (
            by_id[value].get("status") == "LIKELY_NONPUBLIC"
            or by_id[value].get("availability_class") == "LIKELY_NONPUBLIC"
        )
    )
    return DossierV2ClosureSummary(
        expected_mandatory_question_ids=expected,
        reported_question_ids=reported,
        missing_mandatory_question_ids=missing,
        nonterminal_mandatory_question_ids=nonterminal,
        public_searchable_question_ids=public,
        counter_supersession_pending_question_ids=counter,
        verifier_repair_pending_question_ids=repair,
        provider_parser_pending_question_ids=provider,
        likely_nonpublic_question_ids=likely,
    )


def validate_route_bindings(payload: Mapping[str, Any]) -> None:
    receipts = tuple(payload.get("search_route_receipts") or ())
    receipt_by_id = {
        str(row.get("route_receipt_id") or ""): row
        for row in receipts
    }
    if len(receipt_by_id) != len(receipts):
        raise ValueError("duplicate search route receipt ids are forbidden")
    pass_ids = {
        str(row.get("pass_id") or "")
        for row in payload.get("research_passes") or ()
    }
    for receipt in receipts:
        if str(receipt.get("pass_id") or "") not in pass_ids:
            raise ValueError("search route receipt is detached from research pass")
    for result in payload.get("question_family_results") or ():
        question_id = str(result.get("question_family_id") or "")
        archetype_id = str(result.get("archetype_id") or "")
        for receipt_id in result.get("search_route_receipt_ids") or ():
            receipt = receipt_by_id.get(str(receipt_id))
            if receipt is None:
                raise ValueError("question references an unknown search route receipt")
            if (
                receipt.get("question_family_id") != question_id
                or receipt.get("archetype_id") != archetype_id
            ):
                raise ValueError("search route receipt belongs to another question")
        status = str(result.get("status") or "")
        if status in {
            "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
            "LIKELY_NONPUBLIC",
        }:
            if result.get("adequate_search_proven") is not True:
                raise ValueError(f"{status} requires adequate-search proof")
            if len(result.get("search_route_receipt_ids") or ()) < 2:
                raise ValueError(f"{status} requires at least two route receipts")
            linked = [receipt_by_id[value] for value in result["search_route_receipt_ids"]]
            if any(row.get("provider_status") != "SUCCESS" for row in linked):
                raise ValueError(f"{status} requires normal provider/parser receipts")
            if status == "LIKELY_NONPUBLIC" and any(
                not str(row.get("no_new_route_reason") or "").strip() for row in linked
            ):
                raise ValueError("LIKELY_NONPUBLIC requires no-new-route reasons")


def validate_research_status(payload: Mapping[str, Any]) -> DossierV2ClosureSummary:
    summary = compile_dossier_v2_closure_summary(payload)
    actual = str(payload.get("research_status") or "")
    if actual in {"COMPLETE", "COMPLETE_WITH_LIKELY_NONPUBLIC_REMAINDER"}:
        if not summary.full_thesis_question_closure:
            raise ValueError("complete research status has non-terminal mandatory questions")
        if actual != summary.expected_research_status:
            raise ValueError(
                f"research status disagrees with question closure: expected {summary.expected_research_status}"
            )
    elif actual == "NEEDS_PUBLIC_GAP_CLOSURE" and not (
        summary.public_searchable_question_ids or summary.missing_mandatory_question_ids
    ):
        raise ValueError("public-gap status lacks a public or missing mandatory question")
    elif actual == "NEEDS_COUNTER_SUPERSESSION" and not summary.counter_supersession_pending_question_ids:
        raise ValueError("counter/supersession status lacks unresolved contradiction")
    elif actual == "NEEDS_VERIFIER_REPAIR" and not summary.verifier_repair_pending_question_ids:
        raise ValueError("verifier-repair status lacks a repair-required question")
    return summary


__all__ = [
    "AvailabilityClass",
    "DOSSIER_V2_SCHEMA_VERSION",
    "DossierV2ClosureSummary",
    "QuestionStatus",
    "ResearchPassName",
    "compile_dossier_v2_closure_summary",
    "validate_research_status",
    "validate_route_bindings",
]
