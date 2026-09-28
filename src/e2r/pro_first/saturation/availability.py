"""Deterministic availability semantics for one question family."""

from __future__ import annotations

from typing import Any, Mapping

from .models import (
    AvailabilityDecision,
    NONTERMINAL_QUESTION_STATUSES,
    RouteAdequacyDecision,
    TERMINAL_QUESTION_STATUSES,
)


def adjudicate_availability(
    *,
    question_result: Mapping[str, Any],
    route_adequacy: RouteAdequacyDecision,
) -> AvailabilityDecision:
    question_id = str(question_result.get("question_family_id") or "")
    status = str(question_result.get("status") or "")
    availability = str(question_result.get("availability_class") or "")
    failures: list[str] = []
    terminal = status in TERMINAL_QUESTION_STATUSES
    if status not in TERMINAL_QUESTION_STATUSES | NONTERMINAL_QUESTION_STATUSES:
        failures.append("UNKNOWN_QUESTION_STATUS")
        terminal = False
    if status in {"PUBLIC_SEARCHABLE", "UNKNOWN_ROUTE_NOT_YET_TESTED"}:
        terminal = False
    if availability in {"PROVIDER_BLOCKED", "PARSER_BLOCKED"}:
        terminal = False
    if status in {"EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH", "LIKELY_NONPUBLIC"}:
        if not route_adequacy.adequate:
            failures.append("ABSENCE_OR_NONPUBLIC_WITHOUT_ADEQUATE_SEARCH")
            terminal = False
    if status == "LIKELY_NONPUBLIC" and availability != "LIKELY_NONPUBLIC":
        failures.append("LIKELY_NONPUBLIC_AVAILABILITY_MISMATCH")
        terminal = False
    if status == "FUTURE_EVENT_ONLY" and availability != "FUTURE_EVENT_ONLY":
        failures.append("FUTURE_EVENT_AVAILABILITY_MISMATCH")
        terminal = False
    if status == "NOT_APPLICABLE_WITH_REASON":
        if availability != "NOT_APPLICABLE":
            failures.append("NOT_APPLICABLE_AVAILABILITY_MISMATCH")
            terminal = False
        if len(str(question_result.get("closure_reason") or "").strip()) < 10:
            failures.append("NOT_APPLICABLE_REASON_INSUFFICIENT")
            terminal = False
    likely = status == "LIKELY_NONPUBLIC" and terminal
    future = status == "FUTURE_EVENT_ONLY" and terminal
    return AvailabilityDecision(
        question_family_id=question_id,
        availability_class=availability,
        terminal=terminal,
        known_evidence_preserved=True,
        information_confidence_cap_allowed=likely,
        component_upper_bound_allowed=likely,
        stage_ceiling_allowed=likely,
        component_zeroing_allowed=False,
        whole_score_invalidation_allowed=False,
        monitoring_only=future,
        failure_codes=tuple(dict.fromkeys(failures)),
    )


__all__ = ["adjudicate_availability"]
