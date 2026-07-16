"""Provider-backed checkpoint supervision without fixed-round completion."""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from datetime import date
import hashlib
import json
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)

from .component_researcher import ComponentResearchResult, StructuredResearchProvider
from .red_team_researcher import RedTeamResearchResult
from .schemas import (
    CANONICAL_COMPONENT_ORDER,
    EvidenceFact,
    assert_blind_research_output,
    scrub_blind_research_payload,
)
from .source_query_planner import CANONICAL_SOURCE_FAMILIES
from .prompt_projection import (
    project_counter_route_proof,
    project_structured_result,
    project_supervisor_evidence_facts,
    project_supervisor_failures,
    project_supervisor_source_graph_checkpoint,
)
from .source_graph_explorer import validate_source_graph_checkpoint
from .structured_data_researcher import StructuredResearchResult


SUPERVISOR_FAILURE_CLASSES = (
    "PROVIDER_FAILURE",
    "AUTH_FAILURE",
    "RATE_LIMIT",
    "FETCH_FAILURE",
    "PARSER_EXTRACTOR_FAILURE",
    "IRRELEVANT_DOCUMENT",
    "DUPLICATE_QUERY",
    "FUTURE_LEAKAGE",
    "INSUFFICIENT_SEARCH",
    "SOURCE_ABSENCE_CANDIDATE",
)


@dataclass(frozen=True)
class SupervisorComponentFinding:
    component_id: str
    memo_sufficient: bool
    missing_fact_needs: tuple[str, ...]
    rationale: str

    def __post_init__(self) -> None:
        if self.component_id not in CANONICAL_COMPONENT_ORDER:
            raise ValueError("supervisor finding has unknown component")
        if not self.rationale.strip():
            raise ValueError("supervisor component rationale is required")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SupervisorFactGap:
    component_id: str
    fact_need: str
    why_material: str
    direction: str

    def __post_init__(self) -> None:
        if self.component_id not in CANONICAL_COMPONENT_ORDER:
            raise ValueError("supervisor fact gap has unknown component")
        if self.direction not in {"POSITIVE", "COUNTER", "RESOLUTION"}:
            raise ValueError("supervisor fact gap direction is invalid")
        if not self.fact_need.strip() or not self.why_material.strip():
            raise ValueError("supervisor fact gap requires semantic detail")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SupervisorFailureAssessment:
    failure_id: str
    classification: str
    rationale: str
    retryable: bool
    source_absence_claim_allowed: bool

    def __post_init__(self) -> None:
        if not self.failure_id.strip() or not self.rationale.strip():
            raise ValueError("supervisor failure assessment identity is required")
        if self.classification not in SUPERVISOR_FAILURE_CLASSES:
            raise ValueError("unknown supervisor failure classification")
        if self.source_absence_claim_allowed and self.classification != "SOURCE_ABSENCE_CANDIDATE":
            raise ValueError("source absence permission requires absence classification")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SupervisorSourceDirection:
    objective_id: str
    source_family: str
    direction: str
    rationale: str
    counter_or_supersession: bool

    def __post_init__(self) -> None:
        if self.source_family not in CANONICAL_SOURCE_FAMILIES:
            raise ValueError("supervisor invented an unknown source family")
        if not all(
            value.strip()
            for value in (self.objective_id, self.direction, self.rationale)
        ):
            raise ValueError("supervisor source direction is incomplete")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SupervisorQueryDirection:
    objective_id: str
    research_need: str
    avoid_repeating: tuple[str, ...]
    counter_or_supersession: bool

    def __post_init__(self) -> None:
        if not self.objective_id.strip() or not self.research_need.strip():
            raise ValueError("supervisor query direction is incomplete")
        if len(self.avoid_repeating) != len(set(self.avoid_repeating)):
            raise ValueError("supervisor avoid-repeating values must be unique")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ResearchSupervisorReview:
    review_id: str
    epoch: int
    status: str
    component_status: Mapping[str, str]
    unresolved_material_questions: tuple[str, ...]
    source_family_gaps: tuple[str, ...]
    parser_or_extractor_failures: tuple[str, ...]
    next_actions: tuple[str, ...]
    counter_and_supersession_checked: bool
    structured_data_complete: bool
    ready_for_independent_saturation_review: bool
    completion_based_on_round_count: bool = False
    reviewer_role: str = "RESEARCH_SUPERVISOR_A"
    component_findings: tuple[SupervisorComponentFinding, ...] = ()
    missing_material_facts: tuple[SupervisorFactGap, ...] = ()
    failure_assessments: tuple[SupervisorFailureAssessment, ...] = ()
    new_source_family_directions: tuple[SupervisorSourceDirection, ...] = ()
    query_direction_briefs: tuple[SupervisorQueryDirection, ...] = ()
    component_memos_sufficient: bool = False
    reasonable_positive_routes_remaining: bool = True
    rationale: str = "legacy deterministic supervisor review"
    provider_name: str = "DETERMINISTIC_SUPERVISOR_SCAFFOLD"
    prompt_hash: str | None = None
    llm_direction_generation_used: bool = False
    search_zero_result_treated_as_saturation: bool = False
    transport_budget_treated_as_completion: bool = False
    schema_version: str = "e2r_research_supervisor_review_v2"

    def __post_init__(self) -> None:
        if self.epoch < 0:
            raise ValueError("research epoch cannot be negative")
        if self.reviewer_role not in {
            "RESEARCH_SUPERVISOR_A",
            "RESEARCH_SUPERVISOR_B",
        }:
            raise ValueError("unknown Research Supervisor review role")
        if set(self.component_status) != set(CANONICAL_COMPONENT_ORDER):
            raise ValueError("supervisor review requires all component statuses")
        finding_ids = [row.component_id for row in self.component_findings]
        if finding_ids and (
            len(finding_ids) != len(set(finding_ids))
            or set(finding_ids) != set(CANONICAL_COMPONENT_ORDER)
        ):
            raise ValueError("provider supervisor findings must cover seven components")
        if self.status not in {
            "NEXT_RESEARCH_REQUIRED",
            "READY_FOR_INDEPENDENT_SATURATION_REVIEW",
        }:
            raise ValueError("unknown supervisor review status")
        if self.completion_based_on_round_count:
            raise ValueError("fixed round count cannot complete research")
        if self.search_zero_result_treated_as_saturation:
            raise ValueError("zero search results cannot complete research")
        if self.transport_budget_treated_as_completion:
            raise ValueError("transport budget cannot complete research")
        if not self.rationale.strip():
            raise ValueError("supervisor rationale is required")
        if self.ready_for_independent_saturation_review != (
            self.status == "READY_FOR_INDEPENDENT_SATURATION_REVIEW"
        ):
            raise ValueError("supervisor ready flag and status disagree")
        if self.ready_for_independent_saturation_review and (
            self.unresolved_material_questions
            or self.missing_material_facts
            or self.parser_or_extractor_failures
            or self.reasonable_positive_routes_remaining
            or not self.counter_and_supersession_checked
            or not self.structured_data_complete
            or not self.component_memos_sufficient
            or self.next_actions
        ):
            raise ValueError("supervisor cannot declare readiness with semantic gaps")

    def to_dict(self) -> Mapping[str, Any]:
        payload = asdict(self)
        return payload

    def to_score_gap_context(self) -> Mapping[str, Any]:
        """Context for the LLM query planner, never a deterministic query."""

        return {
            "supervisor_review_id": self.review_id,
            "epoch": self.epoch,
            "unresolved_material_questions": list(
                self.unresolved_material_questions
            ),
            "missing_material_facts": [
                row.to_dict() for row in self.missing_material_facts
            ],
            "failure_assessments": [
                row.to_dict() for row in self.failure_assessments
            ],
            "new_source_family_directions": [
                row.to_dict() for row in self.new_source_family_directions
            ],
            "query_direction_briefs": [
                row.to_dict() for row in self.query_direction_briefs
            ],
            "source_family_gaps": list(self.source_family_gaps),
            "parser_or_extractor_failures": list(
                self.parser_or_extractor_failures
            ),
            "counter_and_supersession_checked": (
                self.counter_and_supersession_checked
            ),
            "structured_data_complete": self.structured_data_complete,
            "component_memos_sufficient": self.component_memos_sufficient,
            "reasonable_positive_routes_remaining": (
                self.reasonable_positive_routes_remaining
            ),
            "next_actions": list(self.next_actions),
        }


class ResearchSupervisor:
    """Analyze each epoch; operational directions require an LLM provider."""

    reviewer_role = "RESEARCH_SUPERVISOR_A"

    def __init__(
        self,
        *,
        provider: StructuredResearchProvider | None = None,
        reviewer_role: str = "RESEARCH_SUPERVISOR_A",
    ) -> None:
        if reviewer_role not in {
            "RESEARCH_SUPERVISOR_A",
            "RESEARCH_SUPERVISOR_B",
        }:
            raise ValueError("unknown Research Supervisor role")
        self.provider = provider
        self.reviewer_role = reviewer_role

    def review_epoch(
        self,
        *,
        epoch: int,
        target_id: str,
        as_of_date: str,
        component_results: Sequence[ComponentResearchResult],
        red_team_result: RedTeamResearchResult | None,
        structured_result: Any | None,
        evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
        source_graph_checkpoint: Mapping[str, Any],
        open_objectives: Sequence[Mapping[str, Any]],
        prior_failures: Sequence[Mapping[str, Any]],
        counter_and_supersession_route_proof: Sequence[Mapping[str, Any]],
        prior_review: ResearchSupervisorReview | Mapping[str, Any] | None = None,
    ) -> ResearchSupervisorReview:
        cutoff = date.fromisoformat(as_of_date)
        facts = tuple(_coerce_fact(row) for row in evidence_facts)
        _validate_current_inputs(
            target_id=target_id,
            cutoff=cutoff,
            facts=facts,
            component_results=component_results,
            red_team_result=red_team_result,
            structured_result=structured_result,
            source_graph_checkpoint=source_graph_checkpoint,
        )
        objective_ids = {
            str(row.get("objective_id") or "").strip() for row in open_objectives
        }
        if "" in objective_ids or len(objective_ids) != len(open_objectives):
            raise ValueError("open research objectives require unique ids")
        failures = _collect_prior_failures(
            prior_failures,
            source_graph_checkpoint=source_graph_checkpoint,
        )
        failure_by_id = {str(row["failure_id"]): row for row in failures}
        if len(failure_by_id) != len(failures):
            raise ValueError("prior query/source failures require unique ids")
        counter_route_proof_complete = _counter_route_proof_complete(
            counter_and_supersession_route_proof,
            source_graph_checkpoint=source_graph_checkpoint,
            objective_ids=(
                objective_ids
                | {
                    str(row.get("objective_id") or "")
                    for row in source_graph_checkpoint.get("generated_queries") or ()
                    if str(row.get("objective_id") or "")
                }
                | {
                    str(value)
                    for value in source_graph_checkpoint.get(
                        "resolved_objective_ids"
                    )
                    or ()
                }
            ),
            required_objective_ids={
                str(row.get("objective_id") or "")
                for row in open_objectives
                if bool(row.get("counter_or_supersession_required", True))
            },
            structured_result=structured_result,
        )
        source_graph_zero_result_only = _source_graph_zero_result_only(
            source_graph_checkpoint
        )
        source_graph_research_pending = _source_graph_research_pending(
            source_graph_checkpoint
        )
        if self.provider is None:
            return _provider_pending_review(
                epoch=epoch,
                component_results=component_results,
                reason="SUPERVISOR_PROVIDER_NOT_CONFIGURED",
                reviewer_role=self.reviewer_role,
                provider_name="UNCONFIGURED",
            )
        failure_projection = project_supervisor_failures(failures)
        failure_prompt_projection = _supervisor_failure_prompt_projection(
            failure_projection
        )
        required_failure_group_ids = tuple(
            sorted(
                str(value)
                for value in failure_projection["failure_group_members"]
            )
        )
        payload = scrub_blind_research_payload(
            {
                "reviewer_role": self.reviewer_role,
                "epoch": epoch,
                "target_id": target_id,
                "as_of_date": as_of_date,
                "component_results": [row.to_dict() for row in component_results],
                "red_team_result": (
                    red_team_result.to_dict() if red_team_result else None
                ),
                "structured_result": (
                    project_structured_result(structured_result)
                ),
                "current_evidence_fact_graph": project_supervisor_evidence_facts(
                    facts
                ),
                "source_graph_checkpoint": _supervisor_source_graph_payload(
                    source_graph_checkpoint
                ),
                "open_research_objectives": list(open_objectives),
                "prior_query_source_failures": failure_prompt_projection[
                    "failures"
                ],
                "prior_query_source_failure_projection": {
                    key: value
                    for key, value in failure_prompt_projection.items()
                    if key != "failures"
                },
                "required_output_rosters": {
                    "canonical_component_ids": list(CANONICAL_COMPONENT_ORDER),
                    "failure_group_ids": list(required_failure_group_ids),
                    "failure_group_count": len(required_failure_group_ids),
                    "instruction": (
                        "component_findings must contain every canonical component "
                        "id exactly once. failure_assessments must contain every "
                        "failure_group_id exactly once, with no omission, duplicate, "
                        "or extra id. An empty failure_group_ids roster requires an "
                        "empty failure_assessments array."
                    ),
                },
                "counter_and_supersession_route_proof": project_counter_route_proof(
                    counter_and_supersession_route_proof
                ),
                "prior_supervisor_review": (
                    _prior_supervisor_review_prompt_projection(prior_review)
                    if prior_review
                    else None
                ),
            }
        )
        attempt_payload = payload
        validation_retry_used = False
        while True:
            try:
                response = self.provider.complete(
                    pass_name="RESEARCH_SUPERVISOR_REVIEW",
                    payload=attempt_payload,
                )
            except (
                StructuredProviderUnavailable,
                StructuredProviderRejected,
                TimeoutError,
                OSError,
                RuntimeError,
            ) as exc:
                return _provider_pending_review(
                    epoch=epoch,
                    component_results=component_results,
                    reason=(
                        "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                        f"{type(exc).__name__}:{_clean_error(exc)}"
                    ),
                    reviewer_role=self.reviewer_role,
                    provider_name=str(
                        getattr(
                            self.provider,
                            "provider_name",
                            type(self.provider).__name__,
                        )
                    ),
                    prompt_hash=_provider_prompt_hash(
                        self.provider, attempt_payload
                    ),
                )
            prompt_hash = _provider_prompt_hash(self.provider, attempt_payload)
            try:
                assert_blind_research_output(response)
                return _review_from_provider_response(
                    response=response,
                    epoch=epoch,
                    reviewer_role=self.reviewer_role,
                    component_results=component_results,
                    red_team_result=red_team_result,
                    structured_result=structured_result,
                    objective_ids=objective_ids,
                    failure_by_id=failure_by_id,
                    failure_group_members={
                        str(group_id): tuple(str(value) for value in member_ids)
                        for group_id, member_ids in failure_projection[
                            "failure_group_members"
                        ].items()
                    },
                    counter_route_proof_complete=counter_route_proof_complete,
                    source_graph_zero_result_only=source_graph_zero_result_only,
                    source_graph_research_pending=source_graph_research_pending,
                    provider_name=str(
                        getattr(
                            self.provider,
                            "provider_name",
                            type(self.provider).__name__,
                        )
                    ),
                    prompt_hash=prompt_hash,
                )
            except (KeyError, TypeError, ValueError) as exc:
                _invalidate_provider_response_cache(self.provider, exc)
                failure_roster_diagnostics = _failure_assessment_roster_diagnostics(
                    response=response,
                    required_failure_group_ids=required_failure_group_ids,
                )
                if validation_retry_used:
                    return _provider_pending_review(
                        epoch=epoch,
                        component_results=component_results,
                        reason=(
                            "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                            f"{type(exc).__name__}:{_clean_error(exc)}"
                        ),
                        reviewer_role=self.reviewer_role,
                        provider_name=str(
                            getattr(
                                self.provider,
                                "provider_name",
                                type(self.provider).__name__,
                            )
                        ),
                        prompt_hash=prompt_hash,
                    )
                validation_retry_used = True
                red_team_complete = _red_team_complete(red_team_result)
                attempt_payload = scrub_blind_research_payload(
                    {
                        **payload,
                        "supervisor_validation_retry_context": {
                            "validation_error": _clean_error(exc),
                            "rejected_response": response,
                            "allowed_objective_ids": sorted(objective_ids),
                            "canonical_component_ids": list(
                                CANONICAL_COMPONENT_ORDER
                            ),
                            "required_failure_group_ids": list(
                                required_failure_group_ids
                            ),
                            "failure_assessment_roster_diagnostics": (
                                failure_roster_diagnostics
                            ),
                            "deterministic_current_state": {
                                "structured_data_complete": (
                                    _structured_data_complete(structured_result)
                                ),
                                "red_team_complete": red_team_complete,
                                "counter_route_proof_complete": (
                                    counter_route_proof_complete
                                ),
                                "counter_completion_may_be_true": bool(
                                    counter_route_proof_complete
                                    and red_team_complete
                                ),
                                "source_graph_zero_result_only": (
                                    source_graph_zero_result_only
                                ),
                                "source_graph_research_pending": (
                                    source_graph_research_pending
                                ),
                            },
                            "instruction": (
                                "Rewrite the complete supervisor response once. "
                                "Treat validation_error and deterministic_current_state "
                                "as authoritative correction feedback. Reference only "
                                "allowed_objective_ids and assess every canonical "
                                "component and supplied failure group exactly once. "
                                "structured_data_complete must exactly match the "
                                "deterministic value. counter_and_supersession_checked "
                                "must be false when counter_completion_may_be_true is "
                                "false. Make component/readiness booleans agree with "
                                "the current records and with the gaps, directions, "
                                "unresolved questions, and next actions in the rewritten "
                                "response. Copy every required_failure_group_id into "
                                "failure_assessments exactly once; use the roster "
                                "diagnostics to restore omissions and remove duplicates "
                                "or extras. Do not invent evidence, queries, scores, or stages."
                            ),
                        },
                    }
                )

    def review(
        self,
        *,
        epoch: int,
        component_results: Sequence[ComponentResearchResult],
        red_team_result: RedTeamResearchResult | None,
        structured_result: StructuredResearchResult | None,
        reviewed_source_families: Sequence[str],
        available_source_families: Sequence[str],
        parser_or_extractor_failures: Sequence[str] = (),
    ) -> ResearchSupervisorReview:
        """Backward-compatible deterministic readiness scaffold.

        It may identify pending work, but it never creates operational queries.
        Phase 87 operational runs use :meth:`review_epoch` with a provider.
        """

        by_component = {row.component_id: row for row in component_results}
        component_status = {
            component_id: (
                by_component[component_id].status
                if component_id in by_component
                else "NOT_RESEARCHED"
            )
            for component_id in CANONICAL_COMPONENT_ORDER
        }
        unresolved = []
        next_actions = []
        for component_id in CANONICAL_COMPONENT_ORDER:
            result = by_component.get(component_id)
            if result is None:
                unresolved.append(f"{component_id}:component memo missing")
                next_actions.append(f"{component_id}:independent component research")
                continue
            if result.status != "COMPLETE":
                unresolved.extend(
                    f"{component_id}:{reason}" for reason in result.pending_reasons
                )
                next_actions.append(
                    f"{component_id}:return failure context to the LLM supervisor"
                )
            if result.memo is not None:
                unresolved.extend(
                    f"{component_id}:{question}"
                    for question in result.memo.uncertainties
                )
        red_team_complete = bool(
            red_team_result
            and red_team_result.status == "COMPLETE"
            and red_team_result.memo
        )
        counter_checked = red_team_complete
        if not red_team_complete:
            unresolved.append("independent counter/supersession review incomplete")
            next_actions.append("run independent red-team source and claim review")
        elif red_team_result and red_team_result.memo:
            unresolved.extend(red_team_result.memo.unresolved_challenges)
            next_actions.extend(red_team_result.memo.recommended_research_directions)
        structured_complete = bool(
            structured_result and structured_result.status == "COMPLETE"
        )
        if not structured_complete:
            unresolved.append("required structured data incomplete")
            next_actions.append("execute an untried structured-data fallback route")
        reviewed = {value.upper() for value in reviewed_source_families}
        available = {value.upper() for value in available_source_families}
        source_gaps = tuple(sorted(available - reviewed))
        parser_failures = tuple(dict.fromkeys(parser_or_extractor_failures))
        if parser_failures:
            next_actions.append(
                "repair parser/extractor and reprocess already fetched documents"
            )
        component_sufficient = bool(
            set(by_component) == set(CANONICAL_COMPONENT_ORDER)
            and all(row.status == "COMPLETE" for row in by_component.values())
            and not any(
                row.memo and row.memo.uncertainties for row in by_component.values()
            )
        )
        ready = bool(
            component_sufficient
            and red_team_complete
            and not (
                red_team_result.memo.unresolved_challenges
                if red_team_result and red_team_result.memo
                else ()
            )
            and structured_complete
            and not source_gaps
            and not parser_failures
        )
        status = (
            "READY_FOR_INDEPENDENT_SATURATION_REVIEW"
            if ready
            else "NEXT_RESEARCH_REQUIRED"
        )
        payload = {
            "epoch": epoch,
            "component_status": component_status,
            "unresolved": unresolved,
            "source_gaps": source_gaps,
            "parser_failures": parser_failures,
            "next_actions": next_actions,
            "status": status,
        }
        return ResearchSupervisorReview(
            review_id=stable_intelligence_id("RSUP", payload),
            epoch=epoch,
            status=status,
            component_status=component_status,
            unresolved_material_questions=tuple(dict.fromkeys(unresolved)),
            source_family_gaps=source_gaps,
            parser_or_extractor_failures=parser_failures,
            next_actions=tuple(dict.fromkeys(next_actions)),
            counter_and_supersession_checked=counter_checked,
            structured_data_complete=structured_complete,
            ready_for_independent_saturation_review=ready,
            component_memos_sufficient=component_sufficient,
            reasonable_positive_routes_remaining=not ready,
        )


def _review_from_provider_response(
    *,
    response: Mapping[str, Any],
    epoch: int,
    reviewer_role: str,
    component_results: Sequence[ComponentResearchResult],
    red_team_result: RedTeamResearchResult | None,
    structured_result: Any | None,
    objective_ids: set[str],
    failure_by_id: Mapping[str, Mapping[str, Any]],
    failure_group_members: Mapping[str, Sequence[str]],
    counter_route_proof_complete: bool,
    source_graph_zero_result_only: bool,
    source_graph_research_pending: bool,
    provider_name: str,
    prompt_hash: str,
) -> ResearchSupervisorReview:
    findings = tuple(
        SupervisorComponentFinding(
            component_id=str(row["component_id"]),
            memo_sufficient=_required_bool(row, "memo_sufficient"),
            missing_fact_needs=_string_tuple(row.get("missing_fact_needs")),
            rationale=str(row["rationale"]),
        )
        for row in _mapping_rows(response, "component_findings")
    )
    finding_components = [row.component_id for row in findings]
    if len(finding_components) != len(set(finding_components)) or set(
        finding_components
    ) != set(CANONICAL_COMPONENT_ORDER):
        raise ValueError("supervisor must assess every component exactly once")
    gaps = tuple(
        SupervisorFactGap(
            component_id=str(row["component_id"]),
            fact_need=str(row["fact_need"]),
            why_material=str(row["why_material"]),
            direction=str(row["direction"]),
        )
        for row in _mapping_rows(response, "missing_material_facts")
    )
    group_assessments = tuple(
        SupervisorFailureAssessment(
            failure_id=str(row["failure_id"]),
            classification=str(row["classification"]),
            rationale=str(row["rationale"]),
            retryable=_required_bool(row, "retryable"),
            source_absence_claim_allowed=_required_bool(
                row, "source_absence_claim_allowed"
            ),
        )
        for row in _mapping_rows(response, "failure_assessments")
    )
    assessment_ids = [row.failure_id for row in group_assessments]
    if len(assessment_ids) != len(set(assessment_ids)) or set(assessment_ids) != set(
        failure_group_members
    ):
        expected_ids = set(failure_group_members)
        received_ids = set(assessment_ids)
        raise ValueError(
            "supervisor failure assessment roster mismatch:"
            f"expected_count={len(expected_ids)}:"
            f"received_count={len(assessment_ids)}:"
            f"missing_count={len(expected_ids - received_ids)}:"
            f"extra_count={len(received_ids - expected_ids)}:"
            f"duplicate_count={len(assessment_ids) - len(received_ids)}"
        )
    assessments = tuple(
        SupervisorFailureAssessment(
            failure_id=member_failure_id,
            classification=group.classification,
            rationale=group.rationale,
            retryable=group.retryable,
            source_absence_claim_allowed=group.source_absence_claim_allowed,
        )
        for group in group_assessments
        for member_failure_id in failure_group_members[group.failure_id]
    )
    expanded_ids = [row.failure_id for row in assessments]
    if len(expanded_ids) != len(set(expanded_ids)) or set(expanded_ids) != set(
        failure_by_id
    ):
        raise ValueError("failure-group expansion lost or duplicated a failure id")
    for row in assessments:
        source = failure_by_id[row.failure_id]
        if row.classification == "SOURCE_ABSENCE_CANDIDATE" or row.source_absence_claim_allowed:
            if not _source_absence_proof_valid(source):
                raise ValueError("source absence was claimed without adequate search proof")
    directions = tuple(
        SupervisorSourceDirection(
            objective_id=str(row["objective_id"]),
            source_family=str(row["source_family"]),
            direction=str(row["direction"]),
            rationale=str(row["rationale"]),
            counter_or_supersession=_required_bool(
                row, "counter_or_supersession"
            ),
        )
        for row in _mapping_rows(response, "new_source_family_directions")
    )
    query_directions = tuple(
        SupervisorQueryDirection(
            objective_id=str(row["objective_id"]),
            research_need=str(row["research_need"]),
            avoid_repeating=_string_tuple(row.get("avoid_repeating")),
            counter_or_supersession=_required_bool(
                row, "counter_or_supersession"
            ),
        )
        for row in _mapping_rows(response, "query_direction_briefs")
    )
    if any(row.objective_id not in objective_ids for row in (*directions, *query_directions)):
        raise ValueError("supervisor referenced an unknown research objective")
    unresolved = _string_tuple(response.get("unresolved_material_questions"))
    next_actions = _string_tuple(response.get("next_actions"))
    counter_checked = _required_bool(response, "counter_and_supersession_checked")
    structured_complete = _required_bool(response, "structured_data_complete")
    component_sufficient = _required_bool(response, "component_memos_sufficient")
    reasonable_routes = _required_bool(
        response, "reasonable_positive_routes_remaining"
    )
    provider_ready = _required_bool(
        response, "ready_for_independent_saturation_review"
    )
    component_status = {
        component_id: "NOT_RESEARCHED" for component_id in CANONICAL_COMPONENT_ORDER
    }
    for row in component_results:
        component_status[row.component_id] = row.status
    actual_component_sufficient = bool(
        set(row.component_id for row in component_results)
        == set(CANONICAL_COMPONENT_ORDER)
        and all(row.status == "COMPLETE" for row in component_results)
        and all(row.memo and not row.memo.uncertainties for row in component_results)
        and all(row.memo_sufficient for row in findings)
    )
    actual_structured_complete = _structured_data_complete(structured_result)
    red_team_complete = _red_team_complete(red_team_result)
    if component_sufficient != actual_component_sufficient:
        raise ValueError("supervisor component sufficiency contradicts current memos")
    if structured_complete != actual_structured_complete:
        raise ValueError("supervisor structured-data status contradicts current records")
    if counter_checked and (not counter_route_proof_complete or not red_team_complete):
        raise ValueError("counter/supersession completion lacks route and red-team proof")
    blocking_failures = tuple(
        row.failure_id
        for row in assessments
        if _failure_blocks_readiness(row, failure_by_id[row.failure_id])
    )
    deterministic_ready = bool(
        actual_component_sufficient
        and actual_structured_complete
        and red_team_complete
        and counter_checked
        and not gaps
        and not unresolved
        and not directions
        and not query_directions
        and not reasonable_routes
        and not blocking_failures
        and not source_graph_zero_result_only
        and not source_graph_research_pending
    )
    if provider_ready != deterministic_ready:
        raise ValueError("supervisor readiness contradicts deterministic semantic gates")
    if not provider_ready and not next_actions:
        raise ValueError("pending supervisor review requires next actions")
    parser_failures = tuple(
        row.failure_id
        for row in assessments
        if row.classification == "PARSER_EXTRACTOR_FAILURE"
    )
    source_gaps = tuple(sorted({row.source_family for row in directions}))
    identity = {
        "epoch": epoch,
        "reviewer_role": reviewer_role,
        "component_status": component_status,
        "gaps": [row.to_dict() for row in gaps],
        "assessments": [row.to_dict() for row in assessments],
        "directions": [row.to_dict() for row in directions],
        "query_directions": [row.to_dict() for row in query_directions],
        "unresolved": unresolved,
        "ready": provider_ready,
        "prompt_hash": prompt_hash,
    }
    return ResearchSupervisorReview(
        review_id=stable_intelligence_id("RSUP", identity),
        epoch=epoch,
        status=(
            "READY_FOR_INDEPENDENT_SATURATION_REVIEW"
            if provider_ready
            else "NEXT_RESEARCH_REQUIRED"
        ),
        component_status=component_status,
        unresolved_material_questions=unresolved,
        source_family_gaps=source_gaps,
        parser_or_extractor_failures=parser_failures,
        next_actions=next_actions,
        counter_and_supersession_checked=counter_checked,
        structured_data_complete=structured_complete,
        ready_for_independent_saturation_review=provider_ready,
        reviewer_role=reviewer_role,
        component_findings=findings,
        missing_material_facts=gaps,
        failure_assessments=assessments,
        new_source_family_directions=directions,
        query_direction_briefs=query_directions,
        component_memos_sufficient=component_sufficient,
        reasonable_positive_routes_remaining=reasonable_routes,
        rationale=str(response["rationale"]),
        provider_name=provider_name,
        prompt_hash=prompt_hash,
        llm_direction_generation_used=True,
    )


def _provider_pending_review(
    *,
    epoch: int,
    component_results: Sequence[ComponentResearchResult],
    reason: str,
    reviewer_role: str,
    provider_name: str,
    prompt_hash: str | None = None,
) -> ResearchSupervisorReview:
    status = {component_id: "NOT_RESEARCHED" for component_id in CANONICAL_COMPONENT_ORDER}
    for row in component_results:
        status[row.component_id] = row.status
    payload = {
        "epoch": epoch,
        "reviewer_role": reviewer_role,
        "reason": reason,
        "component_status": status,
    }
    return ResearchSupervisorReview(
        review_id=stable_intelligence_id("RSUP-PENDING", payload),
        epoch=epoch,
        status="NEXT_RESEARCH_REQUIRED",
        component_status=status,
        unresolved_material_questions=(reason,),
        source_family_gaps=(),
        parser_or_extractor_failures=(),
        next_actions=("retry LLM Research Supervisor with failure context",),
        counter_and_supersession_checked=False,
        structured_data_complete=False,
        ready_for_independent_saturation_review=False,
        reviewer_role=reviewer_role,
        component_memos_sufficient=False,
        reasonable_positive_routes_remaining=True,
        rationale=reason,
        provider_name=provider_name,
        prompt_hash=prompt_hash,
    )


def _validate_current_inputs(
    *,
    target_id: str,
    cutoff: date,
    facts: Sequence[EvidenceFact],
    component_results: Sequence[ComponentResearchResult],
    red_team_result: RedTeamResearchResult | None,
    structured_result: Any | None,
    source_graph_checkpoint: Mapping[str, Any],
) -> None:
    component_ids = [row.component_id for row in component_results]
    if len(component_ids) != len(set(component_ids)):
        raise ValueError("supervisor component results must be unique")
    fact_ids = [row.fact_id for row in facts]
    if len(fact_ids) != len(set(fact_ids)):
        raise ValueError("supervisor EvidenceFact ids must be unique")
    if any(row.target_id != target_id or row.as_of_date != cutoff.isoformat() for row in facts):
        raise ValueError("supervisor fact graph target/as_of mismatch")
    archetype_ids = set()
    for result in component_results:
        if result.memo:
            if result.memo.component_id != result.component_id:
                raise ValueError("supervisor component result/memo identity mismatch")
            if (
                result.memo.target_id != target_id
                or result.memo.to_dict().get("as_of_date", cutoff.isoformat())
                not in {None, cutoff.isoformat()}
            ):
                raise ValueError("supervisor component memo target/as_of mismatch")
            archetype_ids.add(result.memo.archetype_id)
            cited_fact_ids = {
                *result.memo.positive_fact_ids,
                *result.memo.counter_fact_ids,
                *result.memo.resolution_fact_ids,
            }
            if not cited_fact_ids.issubset(fact_ids):
                raise ValueError("supervisor component memo cites an unknown EvidenceFact")
    if len(archetype_ids) > 1:
        raise ValueError("supervisor received cross-archetype component memos")
    if red_team_result and red_team_result.memo and red_team_result.memo.target_id != target_id:
        raise ValueError("supervisor red-team target mismatch")
    if structured_result is not None and (
        getattr(structured_result, "target_id", target_id) != target_id
        or getattr(structured_result, "as_of_date", cutoff.isoformat())
        != cutoff.isoformat()
    ):
        raise ValueError("supervisor structured result target/as_of mismatch")
    if not source_graph_checkpoint:
        raise ValueError("Research Supervisor requires a Source Graph checkpoint")
    validate_source_graph_checkpoint(
        source_graph_checkpoint,
        target_id=target_id,
        as_of_date=cutoff.isoformat(),
    )
    if bool(source_graph_checkpoint.get("transport_budget_can_complete_research")):
        raise ValueError("transport budget cannot complete supervised research")


def _supervisor_source_graph_payload(checkpoint: Mapping[str, Any]) -> Mapping[str, Any]:
    return project_supervisor_source_graph_checkpoint(checkpoint)


def _supervisor_failure_prompt_projection(
    projection: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Keep provider-classifiable failure groups without repeated member ids.

    The complete group-to-member expansion remains in deterministic memory and
    is passed separately to output validation.  The provider only classifies a
    semantic group id once, so replaying hundreds of opaque member ids and old
    literal queries wastes context without changing its judgment.  Every
    omitted relation and member roster is hash-accounted here.
    """

    failures = []
    for raw in projection.get("failures") or ():
        row = dict(raw)
        member_ids = tuple(str(value) for value in row.pop("member_failure_ids", ()))
        relation_coverage = dict(row.pop("relation_coverage", {}) or {})
        visible_relations = {
            key: value
            for key, value in relation_coverage.items()
            if key in {"objective_id", "objective_ids"}
        }
        row["relation_coverage"] = visible_relations
        row["omitted_relation_coverage_hash"] = _stable_payload_hash(
            {
                key: value
                for key, value in relation_coverage.items()
                if key not in visible_relations
            }
        )
        row["member_failure_count"] = int(
            row.get("member_failure_count") or len(member_ids)
        )
        row["member_failure_roster_hash"] = str(
            row.get("member_failure_roster_hash")
            or _stable_payload_hash(member_ids)
        )
        failures.append(row)

    group_members = projection.get("failure_group_members") or {}
    return {
        "schema_version": "e2r_v5_supervisor_failure_prompt_projection_v2",
        "failure_count": projection.get("failure_count", 0),
        "failure_group_count": projection.get("failure_group_count", 0),
        "failure_roster_hash": projection.get("failure_roster_hash"),
        "failure_group_member_mapping_hash": _stable_payload_hash(group_members),
        "failures": failures,
        "every_failure_id_preserved_by_group_roster_hash": True,
        "provider_assesses_each_group_once_then_code_expands_to_members": True,
        "full_failure_records_and_member_mapping_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def _prior_supervisor_review_prompt_projection(
    review: ResearchSupervisorReview | Mapping[str, Any],
) -> Mapping[str, Any]:
    """Carry prior supervisor semantics without replaying expanded failures.

    A provider judgment is expanded back to every original failure id before it
    is persisted.  Feeding that expanded ledger into the next provider prompt
    duplicates the already-grouped current failure projection and can exhaust
    the context window.  The prior review therefore keeps its semantic states,
    counts, and full-roster hashes in the prompt while the exact prior artifact
    remains in the immutable epoch checkpoint.
    """

    payload = (
        dict(review.to_dict())
        if isinstance(review, ResearchSupervisorReview)
        else dict(review)
    )
    assessments = tuple(
        dict(row)
        for row in payload.pop("failure_assessments", ()) or ()
        if isinstance(row, Mapping)
    )
    parser_failure_ids = tuple(
        str(value)
        for value in payload.pop("parser_or_extractor_failures", ()) or ()
    )
    payload["unresolved_material_questions"] = [
        _prior_supervisor_text_projection(value)
        for value in payload.get("unresolved_material_questions") or ()
    ]
    payload["next_actions"] = [
        _prior_supervisor_text_projection(value)
        for value in payload.get("next_actions") or ()
    ]
    payload["rationale"] = _prior_supervisor_text_projection(
        payload.get("rationale") or ""
    )

    grouped: dict[tuple[Any, ...], list[Mapping[str, Any]]] = {}
    for row in assessments:
        key = (
            str(row.get("classification") or ""),
            bool(row.get("retryable")),
            bool(row.get("source_absence_claim_allowed")),
            str(row.get("rationale") or ""),
        )
        grouped.setdefault(key, []).append(row)
    assessment_groups = []
    for key in sorted(grouped, key=lambda value: tuple(map(str, value))):
        rows = grouped[key]
        assessment_groups.append(
            {
                "classification": key[0],
                "retryable": key[1],
                "source_absence_claim_allowed": key[2],
                "rationale": _prior_supervisor_text_projection(key[3]),
                "assessment_count": len(rows),
                "assessment_roster_hash": _stable_payload_hash(rows),
            }
        )
    payload["failure_assessment_projection"] = {
        "schema_version": "e2r_v5_prior_supervisor_failure_projection_v1",
        "failure_assessment_count": len(assessments),
        "semantic_group_count": len(assessment_groups),
        "semantic_groups": assessment_groups,
        "failure_assessment_roster_hash": _stable_payload_hash(assessments),
        "every_assessment_accounted_by_group_count_and_hash": (
            sum(row["assessment_count"] for row in assessment_groups)
            == len(assessments)
        ),
        "full_failure_assessments_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }
    payload["parser_or_extractor_failure_projection"] = {
        "failure_count": len(parser_failure_ids),
        "failure_roster_hash": _stable_payload_hash(parser_failure_ids),
        "full_failure_ids_persisted_outside_prompt": True,
    }
    payload["prior_review_roster_hash"] = _stable_payload_hash(
        review.to_dict()
        if isinstance(review, ResearchSupervisorReview)
        else dict(review)
    )
    payload["full_prior_review_persisted_outside_prompt"] = True
    payload["fixed_top_n_used"] = False
    payload["prompt_projection_is_research_cap"] = False
    payload["score_authority"] = False
    return payload


def _prior_supervisor_text_projection(value: Any) -> str:
    """Bound transport diagnostics while preserving normal research prose."""

    text = " ".join(str(value).split())
    if len(text) <= 2_000:
        return text
    folded = text.casefold()
    if text.startswith("SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"):
        marker = "PROVIDER_OUTPUT_ERROR"
        if "context window" in folded or "ran out of room" in folded:
            marker = "PROVIDER_CONTEXT_WINDOW_EXCEEDED"
        elif "usage limit" in folded or "purchase more credits" in folded:
            marker = "PROVIDER_USAGE_LIMIT"
        elif "timed out" in folded or "timeouterror" in folded:
            marker = "PROVIDER_TIMEOUT"
        return (
            f"SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:{marker}:"
            f"DETAIL_CHARS={len(text)}:DETAIL_HASH={_stable_payload_hash(text)}"
        )
    return (
        f"PRIOR_SUPERVISOR_TEXT_OMITTED_FROM_TRANSPORT:"
        f"TEXT_CHARS={len(text)}:TEXT_HASH={_stable_payload_hash(text)}"
    )


def _stable_payload_hash(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _normalize_failure(row: Mapping[str, Any]) -> Mapping[str, Any]:
    payload = dict(row)
    failure_id = str(payload.get("failure_id") or "").strip()
    if not failure_id:
        failure_id = stable_intelligence_id("RSFAIL", payload)
    payload["failure_id"] = failure_id
    payload.setdefault("absence_eligible", False)
    reason = str(payload.get("failure_reason") or payload.get("reason") or "")
    payload["zero_result_only"] = bool(payload.get("zero_result_only")) or (
        "NO_RESULT" in reason.upper() or "ZERO_RESULT" in reason.upper()
    )
    return payload


def _failure_blocks_readiness(
    assessment: SupervisorFailureAssessment,
    source: Mapping[str, Any],
) -> bool:
    """Keep unresolved transport/parser gaps from masquerading as absence."""

    if bool(source.get("resolved")) or str(source.get("resolved_by") or "").strip():
        return False
    if assessment.retryable or bool(source.get("zero_result_only")):
        return True
    if assessment.classification == "SOURCE_ABSENCE_CANDIDATE":
        return not (
            assessment.source_absence_claim_allowed
            and _source_absence_proof_valid(source)
        )
    return assessment.classification in {
        "PROVIDER_FAILURE",
        "AUTH_FAILURE",
        "RATE_LIMIT",
        "FETCH_FAILURE",
        "PARSER_EXTRACTOR_FAILURE",
        "INSUFFICIENT_SEARCH",
    }


def _source_absence_proof_valid(source: Mapping[str, Any]) -> bool:
    attempted_families = source.get("attempted_source_families") or ()
    return bool(
        source.get("absence_eligible")
        and not source.get("zero_result_only")
        and source.get("parser_extractor_verified") is True
        and source.get("provider_transport_verified") is True
        and (
            attempted_families
            or str(source.get("source_family") or "").strip()
        )
    )


def _source_graph_zero_result_only(checkpoint: Mapping[str, Any]) -> bool:
    executed = tuple(
        row
        for row in checkpoint.get("generated_queries") or ()
        if str(row.get("execution_status") or "")
        not in {"", "PENDING", "BLOCKED_OFFICIAL_FIRST"}
    )
    return bool(
        executed
        and not (checkpoint.get("evidence_documents") or ())
        and all(str(row.get("execution_status")) == "NO_RESULT" for row in executed)
    )


def _source_graph_research_pending(checkpoint: Mapping[str, Any]) -> bool:
    return str(checkpoint.get("status") or "") not in {
        "EPOCH_COMPLETE_REQUIRES_SUPERVISOR",
        "STOPPED_ON_RESOLUTION",
    }


def _structured_data_complete(result: Any | None) -> bool:
    if result is None or getattr(result, "status", None) != "COMPLETE":
        return False
    records = getattr(result, "records", None)
    if not records:
        return False
    missing = getattr(result, "missing_roles_by_component", {}) or {}
    return not any(missing.values())


def _red_team_complete(result: RedTeamResearchResult | None) -> bool:
    return bool(
        result
        and result.status == "COMPLETE"
        and result.memo
        and set(result.memo.reviewed_component_ids)
        == set(CANONICAL_COMPONENT_ORDER)
        and not result.memo.unresolved_challenges
    )


def _counter_route_proof_complete(
    rows: Sequence[Mapping[str, Any]],
    *,
    source_graph_checkpoint: Mapping[str, Any],
    objective_ids: set[str],
    required_objective_ids: set[str],
    structured_result: Any | None,
) -> bool:
    """Validate that counter and supersession routes were actually executed."""

    if not rows:
        return False
    query_by_id = {
        str(row.get("query_id") or ""): row
        for row in source_graph_checkpoint.get("generated_queries") or ()
        if str(row.get("query_id") or "")
    }
    document_ids = {
        str(row.get("document_id") or row.get("source_id") or "")
        for row in source_graph_checkpoint.get("evidence_documents") or ()
        if str(row.get("document_id") or row.get("source_id") or "")
    }
    structured_record_ids = {
        str(getattr(record, "record_id", "") or "")
        for record in (getattr(structured_result, "records", ()) or ())
        if str(getattr(record, "record_id", "") or "")
    }
    structured_source_ids = {
        str(source_id)
        for record in (getattr(structured_result, "records", ()) or ())
        for source_id in (getattr(record, "source_ids", ()) or ())
        if str(source_id)
    }
    covered_route_kinds: set[str] = set()
    covered_by_objective: dict[str, set[str]] = {}
    for row in rows:
        objective_id = str(row.get("objective_id") or "").strip()
        if not objective_id or objective_id not in objective_ids:
            return False
        route_kind_value = row.get("route_kind") or row.get("direction")
        if not route_kind_value and row.get("counter_and_supersession"):
            route_kind_value = "COUNTER_AND_SUPERSESSION"
        route_kind = str(route_kind_value or "").upper()
        if route_kind == "COUNTER_AND_SUPERSESSION":
            covered_route_kinds.update(("COUNTER", "SUPERSESSION"))
            covered_by_objective.setdefault(objective_id, set()).update(
                ("COUNTER", "SUPERSESSION")
            )
        elif route_kind in {"COUNTER", "SUPERSESSION"}:
            covered_route_kinds.add(route_kind)
            covered_by_objective.setdefault(objective_id, set()).add(route_kind)
        else:
            return False
        query_ids = _proof_ids(row, "query_ids", "query_id")
        proof_document_ids = _proof_ids(row, "document_ids", "document_id")
        proof_structured_record_ids = _proof_ids(
            row, "structured_record_ids", "structured_record_id"
        )
        source_ids = _proof_ids(row, "source_ids", "source_id")
        if not (
            query_ids
            or proof_document_ids
            or proof_structured_record_ids
            or source_ids
        ):
            return False
        if any(query_id not in query_by_id for query_id in query_ids):
            return False
        for query_id in query_ids:
            query = query_by_id[query_id]
            if not bool(query.get("counter_or_supersession_search")):
                return False
            if str(query.get("execution_status") or "") not in {
                "SEARCH_EXECUTED",
                "NO_RESULT",
            }:
                return False
        if proof_document_ids and not set(proof_document_ids).issubset(document_ids):
            return False
        if proof_structured_record_ids and not set(
            proof_structured_record_ids
        ).issubset(structured_record_ids):
            return False
        if source_ids and not set(source_ids).issubset(
            document_ids | structured_source_ids
        ):
            return False
        if bool(row.get("zero_result_only")):
            return False
        if row.get("parser_extractor_verified") is not True:
            return False
    return bool(
        covered_route_kinds == {"COUNTER", "SUPERSESSION"}
        and all(
            covered_by_objective.get(objective_id) == {"COUNTER", "SUPERSESSION"}
            for objective_id in required_objective_ids
        )
    )


def _proof_ids(
    row: Mapping[str, Any], plural_key: str, singular_key: str
) -> tuple[str, ...]:
    raw = row.get(plural_key)
    values = raw if isinstance(raw, (list, tuple)) else ()
    singular = str(row.get(singular_key) or "").strip()
    result = tuple(str(value).strip() for value in values if str(value).strip())
    if singular:
        result = (*result, singular)
    return tuple(dict.fromkeys(result))


def _collect_prior_failures(
    explicit_rows: Sequence[Mapping[str, Any]],
    *,
    source_graph_checkpoint: Mapping[str, Any],
) -> tuple[Mapping[str, Any], ...]:
    """Collect every checkpoint failure so callers cannot silently omit one."""

    resolved_objectives = {
        str(value)
        for value in source_graph_checkpoint.get("resolved_objective_ids") or ()
    }
    rows: list[Mapping[str, Any]] = [dict(row) for row in explicit_rows]
    for key, kind in (
        ("query_failures", "QUERY_FAILURE"),
        ("provider_failures", "PROVIDER_FAILURE"),
        ("rejected_documents", "DOCUMENT_REJECTION"),
    ):
        for source in source_graph_checkpoint.get(key) or ():
            row = dict(source)
            row.setdefault("failure_kind", kind)
            objective_id = str(row.get("objective_id") or "")
            if objective_id and objective_id in resolved_objectives:
                row.setdefault("resolved", True)
                row.setdefault("resolved_by", "SOURCE_GRAPH_OBJECTIVE_RESOLUTION")
            rows.append(row)
    by_id: dict[str, Mapping[str, Any]] = {}
    for source in rows:
        row = _normalize_failure(source)
        failure_id = str(row["failure_id"])
        prior = by_id.get(failure_id)
        if prior is not None and dict(prior) != dict(row):
            raise ValueError("conflicting prior query/source failure ids")
        by_id[failure_id] = row
    return tuple(by_id[key] for key in sorted(by_id))


def _coerce_fact(row: EvidenceFact | Mapping[str, Any]) -> EvidenceFact:
    if isinstance(row, EvidenceFact):
        return row
    payload = dict(row)
    for key in (
        "source_ids",
        "claim_ids",
        "quote_ids",
        "corroborating_independence_groups",
        "question_family_tags",
        "primitive_tags",
        "allowed_component_ids",
        "structured_evidence_roles",
    ):
        payload[key] = tuple(payload.get(key) or ())
    return EvidenceFact(**payload)


def _mapping_rows(response: Mapping[str, Any], key: str) -> tuple[Mapping[str, Any], ...]:
    value = response.get(key)
    if not isinstance(value, (list, tuple)):
        raise TypeError(f"{key} must be an array")
    if any(not isinstance(row, Mapping) for row in value):
        raise TypeError(f"{key} rows must be objects")
    return tuple(value)


def _required_bool(row: Mapping[str, Any], key: str) -> bool:
    value = row[key]
    if type(value) is not bool:
        raise TypeError(f"{key} must be a boolean")
    return value


def _string_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, (list, tuple)):
        raise TypeError("expected an array of strings")
    rows = tuple(str(row).strip() for row in value)
    if any(not row for row in rows) or len(rows) != len(set(rows)):
        raise ValueError("string array must contain unique non-empty values")
    return rows


def _provider_prompt_hash(
    provider: StructuredResearchProvider, payload: Mapping[str, Any]
) -> str:
    calls = getattr(provider, "calls", None)
    if isinstance(calls, list) and calls:
        value = calls[-1].get("prompt_hash")
        if value:
            return str(value)
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _invalidate_provider_response_cache(
    provider: StructuredResearchProvider,
    error: Exception,
) -> None:
    """Evict one rejected response before the bounded semantic rewrite."""

    invalidate = getattr(provider, "invalidate_last_response_cache", None)
    if not callable(invalidate):
        return
    try:
        invalidate(reason=f"{error.__class__.__name__}:{_clean_error(error)}")
    except (OSError, TypeError, ValueError, RuntimeError):
        # Cache audit failure cannot make the rejected response valid or block
        # the single provider correction attempt.
        return


def _failure_assessment_roster_diagnostics(
    *,
    response: Mapping[str, Any],
    required_failure_group_ids: Sequence[str],
) -> Mapping[str, Any]:
    """Return exact bounded roster feedback for one semantic rewrite."""

    raw_rows = response.get("failure_assessments")
    if isinstance(raw_rows, (str, bytes)) or not isinstance(raw_rows, Sequence):
        received_ids: list[str] = []
        response_array_valid = False
    else:
        received_ids = [
            str(row.get("failure_id") or "")
            for row in raw_rows
            if isinstance(row, Mapping)
        ]
        response_array_valid = len(received_ids) == len(raw_rows)
    required_ids = tuple(str(value) for value in required_failure_group_ids)
    required_set = set(required_ids)
    received_set = set(received_ids)
    received_counts = Counter(received_ids)
    duplicate_ids = sorted(
        value for value, count in received_counts.items() if count > 1
    )
    return {
        "required_count": len(required_ids),
        "received_count": len(received_ids),
        "missing_failure_group_ids": sorted(required_set - received_set),
        "extra_failure_group_ids": sorted(received_set - required_set),
        "duplicate_failure_group_ids": duplicate_ids,
        "failure_assessments_array_was_valid": response_array_valid,
        "received_failure_group_roster_hash": _stable_payload_hash(received_ids),
        "required_failure_group_roster_hash": _stable_payload_hash(required_ids),
    }


def _clean_error(error: Exception) -> str:
    return " ".join(str(error).split())[-500:] or error.__class__.__name__


__all__ = [
    "ResearchSupervisor",
    "ResearchSupervisorReview",
    "SUPERVISOR_FAILURE_CLASSES",
    "SupervisorComponentFinding",
    "SupervisorFactGap",
    "SupervisorFailureAssessment",
    "SupervisorQueryDirection",
    "SupervisorSourceDirection",
]
