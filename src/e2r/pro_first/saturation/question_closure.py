"""Question-family closure over verified fact and source lineage links."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from ..gaps.source_family_policy import source_family_evidence_role
from .availability import adjudicate_availability
from .fixpoint import NoNewRouteConfirmation
from .models import (
    DeterministicQuestionBound,
    NONTERMINAL_QUESTION_STATUSES,
    QuestionClosureDecision,
    TERMINAL_QUESTION_STATUSES,
)
from .route_adequacy import evaluate_route_adequacy


_FACT_BACKED_STATUSES = frozenset(
    {
        "SUPPORTED_SCORING",
        "PARTIALLY_SUPPORTED_SCORING",
        "SUPPORTED_NON_SCORING",
        "COUNTER_SUPPORTED",
        "FUTURE_EVENT_ONLY",
    }
)


def compile_question_closure_decision(
    *,
    question_contract: Mapping[str, Any],
    question_result: Mapping[str, Any],
    dossier_facts: Sequence[Mapping[str, Any]],
    source_lineages: Sequence[Mapping[str, Any]],
    route_receipts: Sequence[Mapping[str, Any]],
    verified_fact_ids: frozenset[str],
    source_documents: Sequence[Mapping[str, Any]] = (),
    deterministic_bound: DeterministicQuestionBound | None = None,
    fixpoint_confirmations: Sequence[NoNewRouteConfirmation] = (),
) -> QuestionClosureDecision:
    question_id = str(question_contract["question_family_id"])
    archetype_id = str(question_result.get("archetype_id") or "")
    status = str(question_result.get("status") or "")
    facts_by_id = {
        str(row.get("dossier_fact_id") or row.get("fact_id") or ""): row
        for row in dossier_facts
    }
    lineage_by_id = {
        str(row.get("source_lineage_id") or row.get("lineage_id") or ""): row
        for row in source_lineages
    }
    source_document_by_id = {
        str(row.get("source_document_id") or ""): row
        for row in source_documents
    }
    linked_fact_ids = tuple(
        dict.fromkeys(
            str(value)
            for key in ("support_fact_ids", "counter_fact_ids", "resolution_fact_ids")
            for value in question_result.get(key) or ()
        )
    )
    verified_linked = tuple(
        value for value in linked_fact_ids if value in verified_fact_ids
    )
    linked_lineages = tuple(
        dict.fromkeys(
            _fact_lineage_id(
                facts_by_id[value],
                source_document_by_id=source_document_by_id,
            )
            for value in verified_linked
            if value in facts_by_id
        )
    )
    active_lineage_ids = {
        lineage_id
        for lineage_id, row in lineage_by_id.items()
        if row.get("status") == "ACTIVE"
    }
    route_adequacy = evaluate_route_adequacy(
        question_contract=question_contract,
        question_result=question_result,
        route_receipts=route_receipts,
        fixpoint_confirmations=fixpoint_confirmations,
    )
    availability = adjudicate_availability(
        question_result=question_result,
        route_adequacy=route_adequacy,
    )
    requested_route_ids = {
        str(value)
        for value in question_result.get("search_route_receipt_ids") or ()
    }
    linked_routes = tuple(
        row
        for row in route_receipts
        if str(row.get("route_receipt_id") or "") in requested_route_ids
        and str(row.get("question_family_id") or "") == question_id
        and str(row.get("archetype_id") or "") == archetype_id
    )
    route_bound_verified = _route_bound_verified_fact_ids(
        facts_by_id=facts_by_id,
        source_document_by_id=source_document_by_id,
        route_receipts=route_receipts,
        verified_fact_ids=verified_fact_ids,
    )
    verified_roles: set[str] = set()
    for route in linked_routes:
        accepted = {
            str(value) for value in route.get("accepted_fact_ids") or ()
        }.intersection(verified_fact_ids)
        if accepted:
            verified_roles.add(str(route.get("source_role_id") or ""))
    for fact_id in verified_linked:
        fact = facts_by_id.get(fact_id) or {}
        for key in ("source_role_id", "source_family"):
            if fact.get(key):
                verified_roles.add(str(fact[key]))
        verified_roles.update(
            str(value) for value in fact.get("source_role_ids") or ()
        )
        source_document = source_document_by_id.get(
            str(fact.get("source_document_id") or "")
        ) or {}
        for key in ("source_role_id", "source_family"):
            if source_document.get(key):
                verified_roles.add(str(source_document[key]))
        verified_roles.update(
            str(value) for value in source_document.get("source_role_ids") or ()
        )
    required_roles = tuple(
        str(value) for value in question_contract.get("required_source_roles") or ()
    )
    missing_roles = tuple(value for value in required_roles if value not in verified_roles)
    missing_core = tuple(
        value
        for value in missing_roles
        if source_family_evidence_role(value) != "SUPPORTING"
    )
    missing_corroboration = tuple(
        value
        for value in missing_roles
        if source_family_evidence_role(value) == "SUPPORTING"
    )
    failures: list[str] = []
    if question_result.get("question_family_id") != question_id:
        failures.append("QUESTION_CONTRACT_IDENTITY_MISMATCH")
    if status not in TERMINAL_QUESTION_STATUSES | NONTERMINAL_QUESTION_STATUSES:
        failures.append("UNKNOWN_QUESTION_STATUS")
    referenced_unknown = set(linked_fact_ids) - set(facts_by_id)
    if referenced_unknown:
        failures.append("QUESTION_REFERENCES_UNKNOWN_FACT")
    unverified = set(linked_fact_ids) - verified_fact_ids
    if unverified:
        failures.append("QUESTION_REFERENCES_UNVERIFIED_FACT")
    if any(value not in active_lineage_ids for value in linked_lineages):
        failures.append("QUESTION_REFERENCES_NONACTIVE_LINEAGE")
    if any(not value for value in linked_lineages):
        failures.append("QUESTION_FACT_MISSING_SOURCE_LINEAGE")
    pro_claimed_satisfied = {
        str(value)
        for value in question_result.get("required_source_roles_satisfied") or ()
    }
    if not pro_claimed_satisfied.issubset(verified_roles):
        failures.append("PRO_CLAIMED_SOURCE_ROLE_UNVERIFIED")
    fact_backed = status in _FACT_BACKED_STATUSES
    if fact_backed and not verified_linked:
        failures.append("TERMINAL_EVIDENCE_STATUS_HAS_NO_VERIFIED_FACT")
    question_roles = set(question_contract.get("question_roles") or ())
    if "ECONOMIC_BRIDGE" in question_roles and status in _FACT_BACKED_STATUSES:
        if not verified_linked:
            failures.append("ECONOMIC_BRIDGE_UNVERIFIED")
    if status == "COUNTER_SUPPORTED" and not set(
        str(value) for value in question_result.get("counter_fact_ids") or ()
    ).intersection(verified_fact_ids):
        failures.append("COUNTER_STATUS_HAS_NO_VERIFIED_COUNTERFACT")
    if status in _FACT_BACKED_STATUSES:
        if not set(verified_linked).issubset(route_bound_verified):
            failures.append("QUESTION_FACT_NOT_BOUND_TO_ROUTE_RECEIPT")
        linkage_complete = bool(
            verified_linked
            and set(linked_lineages).issubset(active_lineage_ids)
            and set(verified_linked).issubset(route_bound_verified)
        )
    elif status in {
        "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
        "LIKELY_NONPUBLIC",
    }:
        linkage_complete = route_adequacy.adequate
    elif status == "NOT_APPLICABLE_WITH_REASON":
        linkage_complete = not availability.failure_codes
    else:
        linkage_complete = bool(linked_routes) and not route_adequacy.failure_codes
    if not linkage_complete:
        failures.append("QUESTION_TO_SOURCE_LINKAGE_INCOMPLETE")
    failures.extend(availability.failure_codes)
    if status != "NOT_APPLICABLE_WITH_REASON":
        failures.extend(route_adequacy.failure_codes)

    materiality = _materiality(question_contract, deterministic_bound)
    public_material = bool(
        status in {"PUBLIC_SEARCHABLE", "UNKNOWN_ROUTE_NOT_YET_TESTED", "SOURCE_PENDING"}
        and materiality not in {"NON_MATERIAL", "MONITORING"}
    )
    hard_break_pending = bool(
        status == "CONTRADICTED_UNRESOLVED"
        and (
            materiality == "HARD_BREAK"
            or question_contract.get("could_change_hard_break") is True
        )
    )
    provider_parser_pending = status in {"PROVIDER_PENDING", "PARSER_PENDING"} or str(
        question_result.get("availability_class") or ""
    ) in {"PROVIDER_BLOCKED", "PARSER_BLOCKED"}
    terminal = availability.terminal and status in TERMINAL_QUESTION_STATUSES
    deterministic_status = status
    gap_class = "NO_GAP"
    if hard_break_pending:
        gap_class = "HARD_BREAK_GAP"
        deterministic_status = "CONTRADICTED_UNRESOLVED"
    elif (
        status == "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH"
        and route_adequacy.adequate
    ):
        gap_class = "NO_GAP"
    elif status == "NOT_APPLICABLE_WITH_REASON" and availability.terminal:
        gap_class = "NO_GAP"
    elif provider_parser_pending or missing_core:
        gap_class = "CORE_SCORE_BLOCKER"
        deterministic_status = (
            status if status in NONTERMINAL_QUESTION_STATUSES else "SOURCE_PENDING"
        )
    elif public_material:
        gap_class = _material_gap_label(materiality)
    elif failures and status in _FACT_BACKED_STATUSES:
        gap_class = "CORE_SCORE_BLOCKER"
        deterministic_status = "SOURCE_PENDING"
    elif missing_corroboration:
        can_cap = bool(
            not missing_core
            and verified_linked
            and deterministic_bound is not None
            and deterministic_bound.score_stage_range_bounded
            and deterministic_bound.hard_break_polarity_resolved
            and not deterministic_bound.missing_predicate_is_new_core
            and route_adequacy.semantic_fixpoint
        )
        if can_cap:
            gap_class = "CORROBORATION_CAP"
        else:
            gap_class = _material_gap_label(materiality)
            if gap_class == "NO_GAP":
                gap_class = "CORE_SCORE_BLOCKER"
            terminal = False
            deterministic_status = "PUBLIC_SEARCHABLE"
            failures.append("CORROBORATION_CAP_CONDITIONS_NOT_MET")
    elif materiality == "MONITORING" and status in NONTERMINAL_QUESTION_STATUSES:
        gap_class = "MONITORING_GAP"
    if status in NONTERMINAL_QUESTION_STATUSES:
        terminal = False
    proposal = {
        "could_change_score": question_result.get("could_change_score") is True,
        "could_change_stage": question_result.get("could_change_stage") is True,
        "could_change_hard_break": question_result.get("could_change_hard_break")
        is True,
    }
    deterministic_flags = (
        {
            "could_change_score": question_contract.get("could_change_score")
            is True,
            "could_change_stage": question_contract.get("could_change_stage")
            is True,
            "could_change_hard_break": question_contract.get(
                "could_change_hard_break"
            )
            is True,
        }
        if deterministic_bound is None
        else {
            "could_change_score": materiality
            in {"CORE_SCORE", "SCORE_BOUNDARY", "STAGE_BOUNDARY"},
            "could_change_stage": materiality == "STAGE_BOUNDARY",
            "could_change_hard_break": materiality == "HARD_BREAK",
        }
    )
    return QuestionClosureDecision(
        archetype_id=archetype_id,
        question_family_id=question_id,
        mandatory=question_contract.get("mandatory_for_full_thesis") is True,
        status=status,
        deterministic_status=deterministic_status,
        terminal=terminal,
        materiality=materiality,
        gap_class=gap_class,
        component_ids=tuple(
            str(value) for value in question_contract.get("affected_component_ids") or ()
        ),
        required_source_roles=required_roles,
        verified_source_roles=tuple(sorted(verified_roles)),
        missing_core_source_roles=missing_core,
        missing_corroboration_source_roles=missing_corroboration,
        linked_fact_ids=linked_fact_ids,
        verified_linked_fact_ids=verified_linked,
        linked_source_lineage_ids=linked_lineages,
        question_to_source_linkage_complete=linkage_complete,
        route_adequacy=route_adequacy,
        availability=availability,
        pro_materiality_proposal=proposal,
        deterministic_materiality_diverged=proposal != deterministic_flags,
        failure_codes=tuple(dict.fromkeys(failures)),
    )


def _route_bound_verified_fact_ids(
    *,
    facts_by_id: Mapping[str, Mapping[str, Any]],
    source_document_by_id: Mapping[str, Mapping[str, Any]],
    route_receipts: Sequence[Mapping[str, Any]],
    verified_fact_ids: frozenset[str],
) -> frozenset[str]:
    """Bind facts to immutable acquisition routes without relabelling routes.

    One source fact can support several question families even though the
    acquisition receipt remains owned by the question that opened the source.
    A currently verified direct fact is also bound when a normal route from
    the same immutable research pass opened its exact source URL; this covers
    a Pro receipt that acquired the document but omitted one fact id from its
    accepted-id roster without permitting cross-pass URL rebinding.
    Derived counter/resolution relationship facts inherit route provenance
    only when every declared source anchor occurs in immutable accepted-route
    history.  The relationship fact itself must still be currently verified;
    direct facts without an accepted route remain unbound.
    """

    acquisition_bound = {
        str(value)
        for route in route_receipts
        for value in route.get("accepted_fact_ids") or ()
        if str(value)
    }
    normal_routes = tuple(
        route
        for route in route_receipts
        if str(route.get("provider_status") or "") == "SUCCESS"
        and str(route.get("parser_status") or "SUCCESS") == "SUCCESS"
    )
    for fact_id in verified_fact_ids:
        fact = facts_by_id.get(fact_id) or {}
        source_document = source_document_by_id.get(
            str(fact.get("source_document_id") or "")
        ) or {}
        fact_urls = {
            str(value)
            for value in (
                fact.get("source_url"),
                fact.get("url"),
                source_document.get("canonical_url"),
                source_document.get("opened_url"),
            )
            if str(value or "")
        }
        fact_pass_id = str(fact.get("research_pass_id") or "")
        if (
            not fact_urls
            or not fact_pass_id
            or tuple(fact.get("source_anchor_fact_ids") or ())
        ):
            continue
        if any(
            str(route.get("pass_id") or "") == fact_pass_id
            and bool(
                fact_urls.intersection(
                    {
                str(value)
                for value in route.get("opened_source_urls") or ()
                if str(value)
                    }
                )
            )
            for route in normal_routes
        ):
            acquisition_bound.add(fact_id)
    bound = set(verified_fact_ids).intersection(acquisition_bound)
    while True:
        added: set[str] = set()
        for fact_id in verified_fact_ids - bound:
            fact = facts_by_id.get(fact_id) or {}
            anchors = {
                str(value)
                for value in fact.get("source_anchor_fact_ids") or ()
                if str(value)
            }
            if anchors and anchors.issubset(acquisition_bound):
                added.add(fact_id)
        if not added:
            return frozenset(bound)
        bound.update(added)
        acquisition_bound.update(added)


def _fact_lineage_id(
    fact: Mapping[str, Any],
    *,
    source_document_by_id: Mapping[str, Mapping[str, Any]],
) -> str:
    """Resolve V2 direct lineage or V3 fact->document->lineage identity."""

    direct = str(fact.get("source_lineage_id") or "")
    if direct:
        return direct
    source_document = source_document_by_id.get(
        str(fact.get("source_document_id") or "")
    ) or {}
    return str(
        source_document.get("lineage_id")
        or source_document.get("source_lineage_id")
        or ""
    )


def _materiality(
    contract: Mapping[str, Any], bound: DeterministicQuestionBound | None
) -> str:
    if bound is not None:
        if bound.question_family_id != contract["question_family_id"]:
            raise ValueError("deterministic question bound belongs to another question")
        return bound.materiality
    if contract.get("could_change_hard_break") is True:
        return "HARD_BREAK"
    if contract.get("could_change_stage") is True:
        return "STAGE_BOUNDARY"
    if contract.get("could_change_score") is True:
        return "CORE_SCORE"
    return "MONITORING"


def _material_gap_label(materiality: str) -> str:
    return {
        "HARD_BREAK": "HARD_BREAK_GAP",
        "STAGE_BOUNDARY": "STAGE_BOUNDARY_GAP",
        "SCORE_BOUNDARY": "CORE_SCORE_BLOCKER",
        "CORE_SCORE": "CORE_SCORE_BLOCKER",
        "MONITORING": "MONITORING_GAP",
        "NON_MATERIAL": "NO_GAP",
    }[materiality]


__all__ = ["compile_question_closure_decision"]
