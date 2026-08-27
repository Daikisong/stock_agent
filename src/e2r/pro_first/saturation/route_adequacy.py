"""Question-bound source-route adequacy without component-count shortcuts."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from ..gaps.source_family_policy import source_family_evidence_role
from ..ids import canonical_hash
from .fixpoint import (
    NoNewRouteConfirmation,
    evaluate_semantic_no_new_route_fixpoint,
)
from .models import RouteAdequacyDecision


ABSENCE_TERMINAL_STATUSES = frozenset(
    {"EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH", "LIKELY_NONPUBLIC"}
)


def evaluate_route_adequacy(
    *,
    question_contract: Mapping[str, Any],
    question_result: Mapping[str, Any],
    route_receipts: Sequence[Mapping[str, Any]],
    fixpoint_confirmations: Sequence[NoNewRouteConfirmation] = (),
) -> RouteAdequacyDecision:
    question_id = str(question_contract["question_family_id"])
    archetype_id = str(question_result.get("archetype_id") or "")
    requested_ids = tuple(
        str(value) for value in question_result.get("search_route_receipt_ids") or ()
    )
    receipt_by_id = {
        str(row.get("route_receipt_id") or ""): row for row in route_receipts
    }
    failures: list[str] = []
    if len(receipt_by_id) != len(tuple(route_receipts)):
        failures.append("DUPLICATE_ROUTE_RECEIPT_ID")
    missing_ids = tuple(value for value in requested_ids if value not in receipt_by_id)
    if missing_ids:
        failures.append("UNKNOWN_ROUTE_RECEIPT_REFERENCE")
    linked = tuple(receipt_by_id[value] for value in requested_ids if value in receipt_by_id)
    if any(
        str(row.get("question_family_id") or "") != question_id
        or str(row.get("archetype_id") or "") != archetype_id
        for row in linked
    ):
        failures.append("ROUTE_RECEIPT_IDENTITY_MISMATCH")
    route_signatures = {
        canonical_hash(
            {
                "source_role_id": row.get("source_role_id"),
                "query_or_navigation_objective": row.get(
                    "query_or_navigation_objective"
                ),
                "query_text": row.get("query_text"),
                "opened_source_urls": sorted(row.get("opened_source_urls") or ()),
            }
        )
        for row in linked
    }
    requirements = question_contract.get("adequate_search_requirements") or {}
    minimum_routes = int(requirements.get("minimum_distinct_source_routes") or 1)
    required_confirmations = int(
        requirements.get("independent_no_new_route_confirmations_for_absence") or 2
    )
    attempted_roles = {
        str(row.get("source_role_id") or "") for row in linked
    }
    official_route_attempted = any(
        source_family_evidence_role(role) == "CORE"
        or "OFFICIAL" in role.upper()
        or role.upper().startswith(("REGULATOR", "GOVERNMENT"))
        for role in attempted_roles
    )
    if requirements.get("official_route_attempt_required") is True and not official_route_attempted:
        failures.append("OFFICIAL_ROUTE_NOT_ATTEMPTED")
    if len(route_signatures) < minimum_routes:
        failures.append("DISTINCT_SOURCE_ROUTE_QUORUM_NOT_MET")
    active_routes = _latest_question_route_cohort(linked)
    provider_parser_normal = all(
        row.get("provider_status") == "SUCCESS"
        and row.get("parser_status", "SUCCESS") == "SUCCESS"
        for row in active_routes
    )
    if linked and not provider_parser_normal:
        failures.append("PROVIDER_OR_PARSER_NOT_NORMAL")
    accepted_fact_delta_zero = all(
        not tuple(row.get("accepted_fact_ids") or ()) for row in active_routes
    )
    status = str(question_result.get("status") or "")
    confirmations = tuple(
        row
        for row in fixpoint_confirmations
        if row.question_family_id == question_id
    )
    fixpoint = evaluate_semantic_no_new_route_fixpoint(
        confirmations,
        minimum_independent_confirmations=max(2, required_confirmations),
    )
    if status in ABSENCE_TERMINAL_STATUSES:
        if question_result.get("adequate_search_proven") is not True:
            failures.append("ADEQUATE_SEARCH_NOT_CLAIMED")
        no_new_receipts = tuple(
            row for row in linked if not tuple(row.get("accepted_fact_ids") or ())
        )
        required_roles = {
            str(value)
            for value in question_contract.get("required_source_roles") or ()
        }
        if not required_roles.issubset(attempted_roles):
            failures.append("REQUIRED_SOURCE_ROLE_ROUTE_NOT_ATTEMPTED")
        if len(no_new_receipts) < max(minimum_routes, required_confirmations):
            failures.append("ABSENCE_ROUTE_RECEIPT_QUORUM_NOT_MET")
        if not provider_parser_normal:
            failures.append("ABSENCE_PROVIDER_OR_PARSER_NOT_NORMAL")
        if any(
            not str(row.get("no_new_route_reason") or "").strip()
            for row in no_new_receipts
        ):
            failures.append("NO_NEW_ROUTE_REASON_MISSING")
        if not fixpoint.reached:
            failures.append("SEMANTIC_FIXPOINT_NOT_PROVEN")
            failures.extend(f"FIXPOINT_{value}" for value in fixpoint.failure_codes)
    adequate = not failures
    return RouteAdequacyDecision(
        question_family_id=question_id,
        adequate=adequate,
        official_route_attempted=official_route_attempted,
        distinct_route_count=len(route_signatures),
        independent_no_new_route_confirmation_count=len(
            fixpoint.accepted_confirmation_ids
        ),
        provider_parser_normal=provider_parser_normal,
        accepted_fact_delta_zero=accepted_fact_delta_zero,
        semantic_fixpoint=fixpoint.reached,
        linked_route_receipt_ids=tuple(
            str(row.get("route_receipt_id") or "") for row in linked
        ),
        failure_codes=tuple(dict.fromkeys(failures)),
    )


def _latest_question_route_cohort(
    linked_routes: Sequence[Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    """Return the newest append-only pass cohort for one question.

    Question route ids are an append-only ledger: delta merge retains prior
    ids first and appends the current pass ids.  Historical provider/parser
    failures remain auditable, but they are not the current provider state
    after a later pass has retried the question.  Every route in the newest
    cohort must still be normal, so one successful route cannot hide another
    unresolved route from the same current pass.

    A question that was not updated simply keeps its previous last cohort.
    The empty case deliberately remains vacuously normal; route-count and
    official-route requirements report the missing acquisition separately.
    """

    rows = tuple(linked_routes)
    if not rows:
        return ()
    latest_pass_id = str(rows[-1].get("pass_id") or "")
    return tuple(
        row for row in rows if str(row.get("pass_id") or "") == latest_pass_id
    )


__all__ = ["ABSENCE_TERMINAL_STATUSES", "evaluate_route_adequacy"]
