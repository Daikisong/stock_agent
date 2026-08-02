"""Provider-backed checkpoint supervision without fixed-round completion."""

from __future__ import annotations

from collections import Counter
from dataclasses import MISSING, asdict, dataclass
from datetime import date
import hashlib
import json
import re
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderUnavailable,
)

from .component_judge import SynthesisResult
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
    normalize_collaboration_transport_wait,
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
    prior_review_prompt_projection: Mapping[str, Any] | None = None
    synthesis_memo_id: str | None = None
    synthesis_memo_hash: str | None = None
    llm_direction_generation_used: bool = False
    search_zero_result_treated_as_saturation: bool = False
    transport_budget_treated_as_completion: bool = False
    schema_version: str = "e2r_research_supervisor_review_v3"

    def __post_init__(self) -> None:
        if self.schema_version not in {
            "e2r_research_supervisor_review_v2",
            "e2r_research_supervisor_review_v3",
        }:
            raise ValueError("unknown Research Supervisor review schema")
        if (
            self.schema_version == "e2r_research_supervisor_review_v2"
            and self.prior_review_prompt_projection is not None
        ):
            raise ValueError(
                "legacy supervisor review cannot carry a v3 prior-review commitment"
            )
        if self.prior_review_prompt_projection is not None:
            _validate_prior_review_prompt_projection(
                self.prior_review_prompt_projection
            )
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
        if bool(self.synthesis_memo_id) != bool(self.synthesis_memo_hash):
            raise ValueError("supervisor synthesis lineage is incomplete")
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
        if self.schema_version == "e2r_research_supervisor_review_v2":
            payload.pop("prior_review_prompt_projection", None)
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


@dataclass(frozen=True)
class _SupervisorPromptMaterial:
    payload: Mapping[str, Any]
    prior_review_prompt_projection: Mapping[str, Any] | None
    objective_ids: frozenset[str]
    objective_component_by_id: Mapping[str, str]
    failure_by_id: Mapping[str, Mapping[str, Any]]
    failure_group_members: Mapping[str, tuple[str, ...]]
    required_failure_group_ids: tuple[str, ...]
    material_score_disagreement_component_ids: tuple[str, ...]
    transport_wait_score_component_ids: tuple[str, ...]
    counter_route_proof_complete: bool
    source_graph_zero_result_only: bool
    source_graph_research_pending: bool


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
        synthesis_result: SynthesisResult | None,
        structured_result: Any | None,
        evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
        source_graph_checkpoint: Mapping[str, Any],
        open_objectives: Sequence[Mapping[str, Any]],
        prior_failures: Sequence[Mapping[str, Any]],
        counter_and_supersession_route_proof: Sequence[Mapping[str, Any]],
        prior_review: ResearchSupervisorReview | Mapping[str, Any] | None = None,
        score_gap_context: Mapping[str, Any] | None = None,
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
        synthesis_binding, synthesis_pending_reason = _current_synthesis_binding(
            target_id=target_id,
            component_results=component_results,
            red_team_result=red_team_result,
            synthesis_result=synthesis_result,
        )
        if synthesis_binding is None:
            return _provider_pending_review(
                epoch=epoch,
                component_results=component_results,
                reason=(
                    "SUPERVISOR_SYNTHESIS_LINEAGE_PENDING:"
                    f"{synthesis_pending_reason}"
                ),
                reviewer_role=self.reviewer_role,
                provider_name=(
                    str(
                        getattr(
                            self.provider,
                            "provider_name",
                            type(self.provider).__name__,
                        )
                    )
                    if self.provider is not None
                    else "UNCONFIGURED"
                ),
            )
        current_synthesis_memo = synthesis_result.memo
        assert current_synthesis_memo is not None
        prior_review_prompt_projection = None
        if prior_review is not None and not _prior_review_matches_synthesis(
            prior_review,
            synthesis_binding=synthesis_binding,
        ):
            prior_review = None
        if prior_review is not None:
            (
                transport_wait_only,
                restored_prior_projection,
            ) = _prior_supervisor_transport_wait_projection(prior_review)
            if transport_wait_only:
                # A collaboration response wait is transport state, not a new
                # Supervisor judgment.  Replaying the pending scaffold as the
                # next prior review changes the prompt/request id and makes the
                # already awaited response impossible to consume on resume.
                prior_review = None
                prior_review_prompt_projection = restored_prior_projection
        if self.provider is None:
            return _provider_pending_review(
                epoch=epoch,
                component_results=component_results,
                reason="SUPERVISOR_PROVIDER_NOT_CONFIGURED",
                reviewer_role=self.reviewer_role,
                provider_name="UNCONFIGURED",
                synthesis_binding=synthesis_binding,
            )
        material = _build_supervisor_prompt_material(
            reviewer_role=self.reviewer_role,
            target_id=target_id,
            as_of_date=as_of_date,
            component_results=component_results,
            red_team_result=red_team_result,
            current_synthesis_memo=current_synthesis_memo,
            synthesis_binding=synthesis_binding,
            structured_result=structured_result,
            facts=facts,
            source_graph_checkpoint=source_graph_checkpoint,
            open_objectives=open_objectives,
            prior_failures=prior_failures,
            counter_and_supersession_route_proof=(
                counter_and_supersession_route_proof
            ),
            prior_review=prior_review,
            prior_review_prompt_projection=prior_review_prompt_projection,
            score_gap_context=score_gap_context,
        )
        payload = material.payload
        objective_ids = set(material.objective_ids)
        objective_component_by_id = material.objective_component_by_id
        failure_by_id = material.failure_by_id
        required_failure_group_ids = material.required_failure_group_ids
        material_score_disagreement_component_ids = (
            material.material_score_disagreement_component_ids
        )
        transport_wait_score_component_ids = (
            material.transport_wait_score_component_ids
        )
        counter_route_proof_complete = material.counter_route_proof_complete
        source_graph_zero_result_only = material.source_graph_zero_result_only
        source_graph_research_pending = material.source_graph_research_pending
        failure_group_members = material.failure_group_members
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
                    prior_review_prompt_projection=(
                        material.prior_review_prompt_projection
                    ),
                    synthesis_binding=synthesis_binding,
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
                    failure_group_members=failure_group_members,
                    material_score_disagreement_component_ids=(
                        material_score_disagreement_component_ids
                    ),
                    transport_wait_score_component_ids=(
                        transport_wait_score_component_ids
                    ),
                    objective_component_by_id=objective_component_by_id,
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
                    prior_review_prompt_projection=(
                        material.prior_review_prompt_projection
                    ),
                    synthesis_binding=synthesis_binding,
                )
            except (KeyError, TypeError, ValueError) as exc:
                _invalidate_provider_response_cache(self.provider, exc)
                failure_roster_diagnostics = _failure_assessment_roster_diagnostics(
                    response=response,
                    required_failure_group_ids=required_failure_group_ids,
                    failure_by_id=failure_by_id,
                    failure_group_members=failure_group_members,
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
                        prior_review_prompt_projection=(
                            material.prior_review_prompt_projection
                        ),
                        synthesis_binding=synthesis_binding,
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
                            "material_score_disagreement_component_ids": list(
                                material_score_disagreement_component_ids
                            ),
                            "transport_wait_score_component_ids": list(
                                transport_wait_score_component_ids
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
                                "material_score_disagreement_component_ids": list(
                                    material_score_disagreement_component_ids
                                ),
                                "transport_wait_score_component_ids": list(
                                    transport_wait_score_component_ids
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
                                "or extras. For every id listed in "
                                "source_absence_proof_invalid_group_ids, set "
                                "source_absence_claim_allowed=false and choose a "
                                "non-SOURCE_ABSENCE_CANDIDATE classification from the "
                                "supplied failure state. source_absence_claim_allowed=true "
                                "is valid only when the classification is exactly "
                                "SOURCE_ABSENCE_CANDIDATE and the id is listed in "
                                "source_absence_proof_valid_group_ids; otherwise it must "
                                "be false. Mark every component listed in "
                                "material_score_disagreement_component_ids as "
                                "memo_sufficient=false and explain the semantic "
                                "rewrite needed; request a new source only when the "
                                "supplied judge reviews identify a concrete missing "
                                "source-backed fact. Keep every component listed in "
                                "transport_wait_score_component_ids sufficient unless "
                                "you also return a concrete missing_material_facts row "
                                "for that component. Every source/query direction must "
                                "map to a component with such a fact row. Do not invent "
                                "evidence, queries, scores, or stages."
                            ),
                        },
                    }
                )

    def preview_prompt_hash(
        self,
        *,
        epoch: int,
        target_id: str,
        as_of_date: str,
        component_results: Sequence[ComponentResearchResult],
        red_team_result: RedTeamResearchResult | None,
        synthesis_result: SynthesisResult | None,
        structured_result: Any | None,
        evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
        source_graph_checkpoint: Mapping[str, Any],
        open_objectives: Sequence[Mapping[str, Any]],
        prior_failures: Sequence[Mapping[str, Any]],
        counter_and_supersession_route_proof: Sequence[Mapping[str, Any]],
        prior_review: ResearchSupervisorReview | Mapping[str, Any] | None = None,
        prior_review_prompt_projection: Mapping[str, Any] | None = None,
        score_gap_context: Mapping[str, Any] | None = None,
    ) -> str:
        """Rebuild the exact first-attempt Supervisor prompt without I/O."""

        del epoch
        if self.provider is None:
            raise ValueError("Research Supervisor preview requires a provider")
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
        synthesis_binding, synthesis_pending_reason = _current_synthesis_binding(
            target_id=target_id,
            component_results=component_results,
            red_team_result=red_team_result,
            synthesis_result=synthesis_result,
        )
        if synthesis_binding is None or synthesis_result is None:
            raise ValueError(
                "supervisor prompt preview lacks current synthesis:"
                f"{synthesis_pending_reason}"
            )
        current_synthesis_memo = synthesis_result.memo
        if current_synthesis_memo is None:
            raise ValueError("supervisor prompt preview lacks synthesis memo")
        if prior_review is not None and not _prior_review_matches_synthesis(
            prior_review,
            synthesis_binding=synthesis_binding,
        ):
            prior_review = None
        material = _build_supervisor_prompt_material(
            reviewer_role=self.reviewer_role,
            target_id=target_id,
            as_of_date=as_of_date,
            component_results=component_results,
            red_team_result=red_team_result,
            current_synthesis_memo=current_synthesis_memo,
            synthesis_binding=synthesis_binding,
            structured_result=structured_result,
            facts=facts,
            source_graph_checkpoint=source_graph_checkpoint,
            open_objectives=open_objectives,
            prior_failures=prior_failures,
            counter_and_supersession_route_proof=(
                counter_and_supersession_route_proof
            ),
            prior_review=prior_review,
            prior_review_prompt_projection=prior_review_prompt_projection,
            score_gap_context=score_gap_context,
        )
        preview = getattr(self.provider, "preview_prompt_hash", None)
        if callable(preview):
            return str(
                preview(
                    pass_name="RESEARCH_SUPERVISOR_REVIEW",
                    payload=material.payload,
                )
            )
        return _stable_payload_hash(material.payload)

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
    material_score_disagreement_component_ids: Sequence[str],
    transport_wait_score_component_ids: Sequence[str],
    objective_component_by_id: Mapping[str, str],
    counter_route_proof_complete: bool,
    source_graph_zero_result_only: bool,
    source_graph_research_pending: bool,
    provider_name: str,
    prompt_hash: str,
    prior_review_prompt_projection: Mapping[str, Any] | None,
    synthesis_binding: Mapping[str, str],
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
    finding_by_component = {row.component_id: row for row in findings}
    if any(
        finding_by_component[component_id].memo_sufficient
        for component_id in material_score_disagreement_component_ids
    ):
        raise ValueError(
            "material score disagreement requires a semantic component rewrite"
        )
    gaps = tuple(
        SupervisorFactGap(
            component_id=str(row["component_id"]),
            fact_need=str(row["fact_need"]),
            why_material=str(row["why_material"]),
            direction=str(row["direction"]),
        )
        for row in _mapping_rows(response, "missing_material_facts")
    )
    gap_component_ids = {row.component_id for row in gaps}
    if any(
        not finding_by_component[component_id].memo_sufficient
        and component_id not in gap_component_ids
        for component_id in transport_wait_score_component_ids
    ):
        raise ValueError(
            "transport-pending judge responses cannot reopen a component memo"
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
    if any(
        objective_component_by_id[row.objective_id] not in gap_component_ids
        for row in (*directions, *query_directions)
    ):
        raise ValueError(
            "supervisor source/query direction requires a concrete component fact gap"
        )
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
        and all(
            row.memo and row.memo.research_complete
            for row in component_results
        )
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
        and _failure_blocks_readiness(row, failure_by_id[row.failure_id])
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
        "synthesis_binding": dict(synthesis_binding),
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
        prior_review_prompt_projection=prior_review_prompt_projection,
        synthesis_memo_id=synthesis_binding["synthesis_memo_id"],
        synthesis_memo_hash=synthesis_binding["synthesis_memo_hash"],
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
    prior_review_prompt_projection: Mapping[str, Any] | None = None,
    synthesis_binding: Mapping[str, str] | None = None,
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
        prior_review_prompt_projection=prior_review_prompt_projection,
        synthesis_memo_id=(
            synthesis_binding["synthesis_memo_id"]
            if synthesis_binding is not None
            else None
        ),
        synthesis_memo_hash=(
            synthesis_binding["synthesis_memo_hash"]
            if synthesis_binding is not None
            else None
        ),
    )


def _current_synthesis_binding(
    *,
    target_id: str,
    component_results: Sequence[ComponentResearchResult],
    red_team_result: RedTeamResearchResult | None,
    synthesis_result: SynthesisResult | None,
) -> tuple[Mapping[str, str] | None, str | None]:
    if synthesis_result is None or synthesis_result.status != "COMPLETE":
        return None, "CURRENT_SYNTHESIS_NOT_COMPLETE"
    memo = synthesis_result.memo
    if memo is None or not memo.synthesis_complete:
        return None, "CURRENT_SYNTHESIS_MEMO_NOT_COMPLETE"
    if memo.target_id != target_id:
        return None, "CURRENT_SYNTHESIS_TARGET_MISMATCH"
    by_component = {row.component_id: row for row in component_results}
    if (
        len(component_results) != len(CANONICAL_COMPONENT_ORDER)
        or set(by_component) != set(CANONICAL_COMPONENT_ORDER)
        or any(
            row.status != "COMPLETE"
            or row.memo is None
            or not row.memo.research_complete
            for row in component_results
        )
    ):
        return None, "CURRENT_COMPONENT_MEMO_ROSTER_INCOMPLETE"
    current_memos = tuple(
        by_component[component_id].memo
        for component_id in CANONICAL_COMPONENT_ORDER
    )
    if any(row is None for row in current_memos):
        return None, "CURRENT_COMPONENT_MEMO_ROSTER_INCOMPLETE"
    archetype_ids = {row.archetype_id for row in current_memos if row is not None}
    if (
        len(archetype_ids) != 1
        or memo.archetype_id not in archetype_ids
        or red_team_result is None
        or red_team_result.status != "COMPLETE"
        or red_team_result.memo is None
        or not red_team_result.memo.review_complete
        or red_team_result.memo.target_id != target_id
        or red_team_result.memo.archetype_id != memo.archetype_id
    ):
        return None, "CURRENT_SYNTHESIS_ARCHETYPE_MISMATCH"
    current_red_team_memo = red_team_result.memo
    if (
        memo.red_team_memo_id != current_red_team_memo.memo_id
        or memo.red_team_memo_hash
        != _stable_payload_hash(current_red_team_memo.to_dict())
    ):
        return None, "CURRENT_SYNTHESIS_RED_TEAM_LINEAGE_MISMATCH"
    current_memo_ids = {
        row.memo_id for row in current_memos if row is not None
    }
    synthesis_memo_ids = tuple(memo.component_memo_ids)
    if (
        len(synthesis_memo_ids) != len(CANONICAL_COMPONENT_ORDER)
        or len(set(synthesis_memo_ids)) != len(synthesis_memo_ids)
        or set(synthesis_memo_ids) != current_memo_ids
    ):
        return None, "CURRENT_SYNTHESIS_COMPONENT_MEMO_ROSTER_MISMATCH"
    return (
        {
            "schema_version": "e2r_supervisor_synthesis_binding_v1",
            "synthesis_memo_id": memo.memo_id,
            "synthesis_memo_hash": _stable_payload_hash(memo.to_dict()),
        },
        None,
    )


def _prior_review_matches_synthesis(
    review: ResearchSupervisorReview | Mapping[str, Any],
    *,
    synthesis_binding: Mapping[str, str],
) -> bool:
    payload = (
        review.to_dict()
        if isinstance(review, ResearchSupervisorReview)
        else review
    )
    return bool(
        payload.get("synthesis_memo_id")
        == synthesis_binding["synthesis_memo_id"]
        and payload.get("synthesis_memo_hash")
        == synthesis_binding["synthesis_memo_hash"]
    )


def _build_supervisor_prompt_material(
    *,
    reviewer_role: str,
    target_id: str,
    as_of_date: str,
    component_results: Sequence[ComponentResearchResult],
    red_team_result: RedTeamResearchResult | None,
    current_synthesis_memo: Any,
    synthesis_binding: Mapping[str, str],
    structured_result: Any | None,
    facts: Sequence[EvidenceFact],
    source_graph_checkpoint: Mapping[str, Any],
    open_objectives: Sequence[Mapping[str, Any]],
    prior_failures: Sequence[Mapping[str, Any]],
    counter_and_supersession_route_proof: Sequence[Mapping[str, Any]],
    prior_review: ResearchSupervisorReview | Mapping[str, Any] | None,
    score_gap_context: Mapping[str, Any] | None,
    prior_review_prompt_projection: Mapping[str, Any] | None = None,
) -> _SupervisorPromptMaterial:
    """Build all deterministic commitments for one Supervisor provider call."""

    objective_ids = {
        str(row.get("objective_id") or "").strip() for row in open_objectives
    }
    if "" in objective_ids or len(objective_ids) != len(open_objectives):
        raise ValueError("open research objectives require unique ids")
    objective_component_by_id = {
        str(row.get("objective_id") or "").strip(): str(
            row.get("component_id") or ""
        ).strip()
        for row in open_objectives
    }
    if any(
        component_id not in CANONICAL_COMPONENT_ORDER
        for component_id in objective_component_by_id.values()
    ):
        raise ValueError(
            "open research objectives require canonical component ids"
        )
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
        evidence_facts=facts,
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
    failure_projection = project_supervisor_failures(failures)
    failure_prompt_projection = _supervisor_failure_prompt_projection(
        failure_projection
    )
    failure_group_members = {
        str(group_id): tuple(str(value) for value in member_ids)
        for group_id, member_ids in failure_projection[
            "failure_group_members"
        ].items()
    }
    required_failure_group_ids = tuple(sorted(failure_group_members))
    material_score_disagreement_component_ids = (
        _material_score_disagreement_component_ids(score_gap_context)
    )
    transport_wait_score_component_ids = (
        _transport_wait_score_component_ids(score_gap_context)
    )
    prior_prompt_projection = (
        dict(prior_review_prompt_projection)
        if prior_review_prompt_projection is not None
        else (
            _prior_supervisor_review_prompt_projection(prior_review)
            if prior_review
            else None
        )
    )
    information_confidence_result = next(
        (
            result
            for result in component_results
            if result.component_id == "information_confidence"
        ),
        None,
    )
    information_confidence_memo_fact_ids = (
        tuple(
            dict.fromkeys(
                (
                    *information_confidence_result.memo.positive_fact_ids,
                    *information_confidence_result.memo.counter_fact_ids,
                    *information_confidence_result.memo.resolution_fact_ids,
                    *information_confidence_result.memo.context_fact_ids,
                )
            )
        )
        if information_confidence_result is not None
        and information_confidence_result.status == "COMPLETE"
        and information_confidence_result.memo is not None
        and information_confidence_result.memo.research_complete
        else None
    )
    payload = scrub_blind_research_payload(
        {
            "reviewer_role": reviewer_role,
            "target_id": target_id,
            "as_of_date": as_of_date,
            "component_results": [row.to_dict() for row in component_results],
            "red_team_result": (
                red_team_result.to_dict() if red_team_result else None
            ),
            "current_synthesis": {
                "binding": dict(synthesis_binding),
                "memo": current_synthesis_memo.to_dict(),
            },
            "structured_result": project_structured_result(structured_result),
            "current_evidence_fact_graph": project_supervisor_evidence_facts(
                facts,
                independent_corroboration_fact_ids=(
                    information_confidence_memo_fact_ids
                ),
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
                "material_score_disagreement_component_ids": list(
                    material_score_disagreement_component_ids
                ),
                "transport_wait_score_component_ids": list(
                    transport_wait_score_component_ids
                ),
                "independent_corroboration_review_contract": {
                    "projection_path": (
                        "current_evidence_fact_graph."
                        "independent_corroboration_review"
                    ),
                    "llm_owns_gap_materiality": True,
                    "literal_query_generation_owner": (
                        "SOURCE_QUERY_GENERATION_LLM"
                    ),
                    "instruction": (
                        "For information-confidence findings, compare the "
                        "named relationships described by current memos and "
                        "synthesis with the projected primary and corroborating "
                        "source-family coverage. When a reasonable independent "
                        "official route remains, emit one concrete missing fact, "
                        "one objective-bound source-family direction, and one "
                        "semantic query-direction brief. Do not write a literal "
                        "query and do not treat an empty corroboration count as "
                        "deterministic source absence or a mandatory gap."
                    ),
                },
                "structured_report_source_candidate_review_contract": {
                    "projection_path": (
                        "deterministic_score_gap_context."
                        "structured_report_source_candidates"
                    ),
                    "llm_owns_candidate_materiality": True,
                    "literal_query_generation_owner": (
                        "SOURCE_QUERY_GENERATION_LLM"
                    ),
                    "instruction": (
                        "Treat each structured-provider report row only as a "
                        "bounded discovery hint, never as evidence. Decide from "
                        "its broker, title, publication date, provider identity, "
                        "and current fact graph whether resolving the full report "
                        "could answer a concrete material fact gap for a canonical "
                        "objective. For a material candidate, emit that concrete "
                        "missing fact, an objective-bound PUBLIC_BROKER_PDF source "
                        "family direction, and a semantic query-direction brief "
                        "that preserves the candidate identity needed by the query "
                        "LLM. Do not create a literal query or URL, do not treat "
                        "preview numbers as facts, and do not open a gap merely "
                        "because a candidate exists."
                    ),
                },
                "instruction": (
                    "component_findings must contain every canonical component "
                    "id exactly once. failure_assessments must contain every "
                    "failure_group_id exactly once, with no omission, duplicate, "
                    "or extra id. An empty failure_group_ids roster requires an "
                    "empty failure_assessments array. Every component in "
                    "material_score_disagreement_component_ids must be marked "
                    "memo_sufficient=false until a semantic component rewrite "
                    "and new independent judges remove that disagreement. Decide "
                    "from the supplied judge reviews whether a genuinely missing "
                    "source-backed fact exists; do not invent a query merely to "
                    "change a score. Transport-only missing judge responses do "
                    "not reopen an otherwise complete component memo. A source "
                    "or query direction is valid only when missing_material_facts "
                    "contains a concrete fact gap for that objective's component."
                ),
            },
            "deterministic_score_gap_context": dict(score_gap_context or {}),
            "counter_and_supersession_route_proof": project_counter_route_proof(
                counter_and_supersession_route_proof
            ),
            "prior_supervisor_review": prior_prompt_projection,
        }
    )
    return _SupervisorPromptMaterial(
        payload=payload,
        prior_review_prompt_projection=payload.get(
            "prior_supervisor_review"
        ),
        objective_ids=frozenset(objective_ids),
        objective_component_by_id=objective_component_by_id,
        failure_by_id=failure_by_id,
        failure_group_members=failure_group_members,
        required_failure_group_ids=required_failure_group_ids,
        material_score_disagreement_component_ids=(
            material_score_disagreement_component_ids
        ),
        transport_wait_score_component_ids=transport_wait_score_component_ids,
        counter_route_proof_complete=counter_route_proof_complete,
        source_graph_zero_result_only=source_graph_zero_result_only,
        source_graph_research_pending=source_graph_research_pending,
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


_PRIOR_REVIEW_PROMPT_LINEAGE_FIELDS = frozenset(
    {
        "review_id",
        "epoch",
        "prompt_hash",
        "prior_review_prompt_projection",
    }
)
_PRIOR_REVIEW_PROMPT_COMPACTED_FIELDS = frozenset(
    {
        "failure_assessments",
        "parser_or_extractor_failures",
    }
)
_PRIOR_REVIEW_PROMPT_PROJECTION_FIELDS = frozenset(
    {
        "failure_assessment_projection",
        "parser_or_extractor_failure_projection",
        "prior_review_semantic_hash",
        "checkpoint_lineage_excluded_from_provider",
        "excluded_checkpoint_lineage_fields",
        "full_prior_review_persisted_outside_prompt",
        "fixed_top_n_used",
        "prompt_projection_is_research_cap",
        "score_authority",
    }
)


def _prior_review_prompt_projection_top_keys() -> set[str]:
    """Derive the closed projection roster from the canonical review schema."""

    return (
        set(ResearchSupervisorReview.__dataclass_fields__)
        - _PRIOR_REVIEW_PROMPT_LINEAGE_FIELDS
        - _PRIOR_REVIEW_PROMPT_COMPACTED_FIELDS
    ) | set(_PRIOR_REVIEW_PROMPT_PROJECTION_FIELDS)


def _prior_review_prompt_excluded_lineage_fields(
    schema_version: Any,
) -> list[str]:
    fields = ["review_id", "epoch", "prompt_hash"]
    if schema_version == "e2r_research_supervisor_review_v3":
        fields.append("prior_review_prompt_projection")
    elif schema_version != "e2r_research_supervisor_review_v2":
        raise ValueError("prior supervisor projection schema is invalid")
    return fields


def _prior_review_prompt_default(field_name: str) -> Any:
    field = ResearchSupervisorReview.__dataclass_fields__[field_name]
    if field.default is not MISSING:
        return field.default
    required_defaults: Mapping[str, Any] = {
        "review_id": "",
        "epoch": 0,
        "status": "NEXT_RESEARCH_REQUIRED",
        "component_status": {
            component_id: "NOT_RESEARCHED"
            for component_id in CANONICAL_COMPONENT_ORDER
        },
        "unresolved_material_questions": (),
        "source_family_gaps": (),
        "parser_or_extractor_failures": (),
        "next_actions": (),
        "counter_and_supersession_checked": False,
        "structured_data_complete": False,
        "ready_for_independent_saturation_review": False,
    }
    if field_name not in required_defaults:
        raise ValueError(
            f"prior supervisor review lacks canonical field: {field_name}"
        )
    return required_defaults[field_name]


def _canonical_prior_review_prompt_source(
    review: ResearchSupervisorReview | Mapping[str, Any],
) -> Mapping[str, Any]:
    raw = (
        dict(review.to_dict())
        if isinstance(review, ResearchSupervisorReview)
        else dict(review)
    )
    review_fields = set(ResearchSupervisorReview.__dataclass_fields__)
    if not set(raw).issubset(review_fields):
        raise ValueError("prior supervisor review has unknown fields")
    return {
        field_name: (
            raw[field_name]
            if field_name in raw
            else _prior_review_prompt_default(field_name)
        )
        for field_name in ResearchSupervisorReview.__dataclass_fields__
    }


def _validate_prior_review_prompt_projection(
    projection: Mapping[str, Any],
) -> None:
    """Validate the exact prior-review fragment committed by a v3 review."""

    if not isinstance(projection, Mapping):
        raise ValueError("prior supervisor review prompt commitment must be an object")
    if set(projection) != _prior_review_prompt_projection_top_keys():
        raise ValueError(
            "prior supervisor review prompt commitment key roster mismatch"
        )
    expected_excluded_fields = _prior_review_prompt_excluded_lineage_fields(
        projection.get("schema_version")
    )
    if (
        projection.get("checkpoint_lineage_excluded_from_provider") is not True
        or projection.get("excluded_checkpoint_lineage_fields")
        != expected_excluded_fields
        or projection.get("full_prior_review_persisted_outside_prompt") is not True
        or projection.get("fixed_top_n_used") is not False
        or projection.get("prompt_projection_is_research_cap") is not False
        or projection.get("score_authority") is not False
    ):
        raise ValueError("invalid prior supervisor review prompt commitment")
    _validate_prior_review_prompt_projection_semantics(projection)
    semantic_projection = dict(projection)
    expected_semantic_hash = str(
        semantic_projection.pop("prior_review_semantic_hash", "")
    )
    for key in (
        "checkpoint_lineage_excluded_from_provider",
        "excluded_checkpoint_lineage_fields",
        "full_prior_review_persisted_outside_prompt",
        "fixed_top_n_used",
        "prompt_projection_is_research_cap",
        "score_authority",
    ):
        semantic_projection.pop(key, None)
    if (
        len(expected_semantic_hash) != 64
        or _stable_payload_hash(semantic_projection)
        != expected_semantic_hash
    ):
        raise ValueError("prior supervisor review semantic commitment hash mismatch")


def _validate_prior_review_prompt_projection_semantics(
    projection: Mapping[str, Any],
) -> None:
    component_status = projection.get("component_status")
    if (
        not isinstance(component_status, Mapping)
        or set(component_status) != set(CANONICAL_COMPONENT_ORDER)
        or any(
            not isinstance(value, str) or not value
            for value in component_status.values()
        )
    ):
        raise ValueError("prior supervisor component status roster mismatch")
    for key in (
        "unresolved_material_questions",
        "source_family_gaps",
        "next_actions",
    ):
        _validate_projection_string_array(projection.get(key), key)
    for key in (
        "completion_based_on_round_count",
        "counter_and_supersession_checked",
        "structured_data_complete",
        "ready_for_independent_saturation_review",
        "component_memos_sufficient",
        "reasonable_positive_routes_remaining",
        "llm_direction_generation_used",
        "search_zero_result_treated_as_saturation",
        "transport_budget_treated_as_completion",
    ):
        if type(projection.get(key)) is not bool:
            raise ValueError(f"prior supervisor projection {key} must be boolean")
    if projection.get("status") not in {
        "NEXT_RESEARCH_REQUIRED",
        "READY_FOR_INDEPENDENT_SATURATION_REVIEW",
    }:
        raise ValueError("prior supervisor projection status is invalid")
    if projection.get("reviewer_role") not in {
        "RESEARCH_SUPERVISOR_A",
        "RESEARCH_SUPERVISOR_B",
    }:
        raise ValueError("prior supervisor projection reviewer role is invalid")
    if projection.get("schema_version") not in {
        "e2r_research_supervisor_review_v2",
        "e2r_research_supervisor_review_v3",
    }:
        raise ValueError("prior supervisor projection schema is invalid")
    for key in ("rationale", "provider_name"):
        if not isinstance(projection.get(key), str) or not str(
            projection[key]
        ).strip():
            raise ValueError(f"prior supervisor projection {key} is invalid")
    synthesis_memo_id = projection.get("synthesis_memo_id")
    synthesis_memo_hash = projection.get("synthesis_memo_hash")
    if bool(synthesis_memo_id) != bool(synthesis_memo_hash):
        raise ValueError("prior supervisor projection synthesis lineage is incomplete")
    if synthesis_memo_id is not None and (
        not isinstance(synthesis_memo_id, str)
        or not isinstance(synthesis_memo_hash, str)
        or re.fullmatch(r"[0-9a-f]{64}", synthesis_memo_hash) is None
    ):
        raise ValueError("prior supervisor projection synthesis lineage is invalid")

    finding_rows = _validate_projection_rows(
        projection.get("component_findings"),
        set(SupervisorComponentFinding.__dataclass_fields__),
        "component finding",
    )
    findings = tuple(
        SupervisorComponentFinding(
            component_id=_required_projection_string(row, "component_id"),
            memo_sufficient=_required_projection_bool(row, "memo_sufficient"),
            missing_fact_needs=_projection_string_tuple(
                row.get("missing_fact_needs"),
                "missing_fact_needs",
            ),
            rationale=_required_projection_string(row, "rationale"),
        )
        for row in finding_rows
    )
    finding_ids = [row.component_id for row in findings]
    if finding_ids and (
        len(finding_ids) != len(set(finding_ids))
        or set(finding_ids) != set(CANONICAL_COMPONENT_ORDER)
    ):
        raise ValueError("prior supervisor findings must cover seven components")
    for row in _validate_projection_rows(
        projection.get("missing_material_facts"),
        set(SupervisorFactGap.__dataclass_fields__),
        "fact gap",
    ):
        SupervisorFactGap(
            component_id=_required_projection_string(row, "component_id"),
            fact_need=_required_projection_string(row, "fact_need"),
            why_material=_required_projection_string(row, "why_material"),
            direction=_required_projection_string(row, "direction"),
        )
    for row in _validate_projection_rows(
        projection.get("new_source_family_directions"),
        set(SupervisorSourceDirection.__dataclass_fields__),
        "source direction",
    ):
        SupervisorSourceDirection(
            objective_id=_required_projection_string(row, "objective_id"),
            source_family=_required_projection_string(row, "source_family"),
            direction=_required_projection_string(row, "direction"),
            rationale=_required_projection_string(row, "rationale"),
            counter_or_supersession=_required_projection_bool(
                row,
                "counter_or_supersession",
            ),
        )
    for row in _validate_projection_rows(
        projection.get("query_direction_briefs"),
        set(SupervisorQueryDirection.__dataclass_fields__),
        "query direction",
    ):
        SupervisorQueryDirection(
            objective_id=_required_projection_string(row, "objective_id"),
            research_need=_required_projection_string(row, "research_need"),
            avoid_repeating=_projection_string_tuple(
                row.get("avoid_repeating"),
                "avoid_repeating",
            ),
            counter_or_supersession=_required_projection_bool(
                row,
                "counter_or_supersession",
            ),
        )
    _validate_failure_assessment_prompt_projection(
        projection.get("failure_assessment_projection")
    )
    _validate_parser_failure_prompt_projection(
        projection.get("parser_or_extractor_failure_projection")
    )


def _validate_failure_assessment_prompt_projection(value: Any) -> None:
    expected_keys = {
        "schema_version",
        "failure_assessment_count",
        "semantic_group_count",
        "semantic_groups",
        "failure_assessment_roster_hash",
        "every_assessment_accounted_by_group_count_and_hash",
        "full_failure_assessments_persisted_outside_prompt",
        "fixed_top_n_used",
        "prompt_projection_is_research_cap",
        "score_authority",
    }
    if not isinstance(value, Mapping) or set(value) != expected_keys:
        raise ValueError("prior supervisor failure projection key roster mismatch")
    if (
        value.get("schema_version")
        != "e2r_v5_prior_supervisor_failure_projection_v1"
        or value.get("every_assessment_accounted_by_group_count_and_hash")
        is not True
        or value.get("full_failure_assessments_persisted_outside_prompt")
        is not True
        or value.get("fixed_top_n_used") is not False
        or value.get("prompt_projection_is_research_cap") is not False
        or value.get("score_authority") is not False
    ):
        raise ValueError("invalid prior supervisor failure projection")
    failure_count = _nonnegative_projection_int(
        value.get("failure_assessment_count"),
        "failure_assessment_count",
    )
    group_count = _nonnegative_projection_int(
        value.get("semantic_group_count"),
        "semantic_group_count",
    )
    if not _is_sha256(value.get("failure_assessment_roster_hash")):
        raise ValueError("prior supervisor failure roster hash is invalid")
    group_rows = _validate_projection_rows(
        value.get("semantic_groups"),
        {
            "classification",
            "retryable",
            "source_absence_claim_allowed",
            "rationale",
            "assessment_count",
            "assessment_roster_hash",
        },
        "failure semantic group",
    )
    if len(group_rows) != group_count:
        raise ValueError("prior supervisor failure semantic group count mismatch")
    accounted_count = 0
    for row in group_rows:
        classification = _required_projection_string(
            row,
            "classification",
        )
        retryable = _required_projection_bool(row, "retryable")
        source_absence_allowed = _required_projection_bool(
            row,
            "source_absence_claim_allowed",
        )
        if classification not in SUPERVISOR_FAILURE_CLASSES:
            raise ValueError("prior supervisor failure classification is invalid")
        if (
            source_absence_allowed
            and classification != "SOURCE_ABSENCE_CANDIDATE"
        ):
            raise ValueError("prior supervisor source absence permission is invalid")
        del retryable
        _required_projection_string(row, "rationale")
        assessment_count = _positive_projection_int(
            row.get("assessment_count"),
            "assessment_count",
        )
        if not _is_sha256(row.get("assessment_roster_hash")):
            raise ValueError("prior supervisor assessment roster hash is invalid")
        accounted_count += assessment_count
    if accounted_count != failure_count:
        raise ValueError("prior supervisor failure assessment count mismatch")


def _validate_parser_failure_prompt_projection(value: Any) -> None:
    expected_keys = {
        "failure_count",
        "failure_roster_hash",
        "full_failure_ids_persisted_outside_prompt",
    }
    if not isinstance(value, Mapping) or set(value) != expected_keys:
        raise ValueError("prior supervisor parser projection key roster mismatch")
    _nonnegative_projection_int(value.get("failure_count"), "failure_count")
    if (
        not _is_sha256(value.get("failure_roster_hash"))
        or value.get("full_failure_ids_persisted_outside_prompt") is not True
    ):
        raise ValueError("invalid prior supervisor parser failure projection")


def _validate_projection_rows(
    value: Any,
    expected_keys: set[str],
    label: str,
) -> tuple[Mapping[str, Any], ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, (list, tuple)):
        raise ValueError(f"prior supervisor {label} rows must be an array")
    rows = tuple(value)
    if any(not isinstance(row, Mapping) or set(row) != expected_keys for row in rows):
        raise ValueError(f"prior supervisor {label} key roster mismatch")
    return rows


def _validate_projection_string_array(value: Any, label: str) -> None:
    _projection_string_tuple(value, label)


def _projection_string_tuple(value: Any, label: str) -> tuple[str, ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, (list, tuple)):
        raise ValueError(f"prior supervisor projection {label} must be an array")
    if any(not isinstance(item, str) for item in value):
        raise ValueError(
            f"prior supervisor projection {label} requires string values"
        )
    return tuple(value)


def _required_projection_string(row: Mapping[str, Any], key: str) -> str:
    value = row.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"prior supervisor projection {key} is invalid")
    return value


def _required_projection_bool(row: Mapping[str, Any], key: str) -> bool:
    value = row.get(key)
    if type(value) is not bool:
        raise ValueError(f"prior supervisor projection {key} must be boolean")
    return value


def _nonnegative_projection_int(value: Any, label: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"prior supervisor projection {label} is invalid")
    return value


def _positive_projection_int(value: Any, label: str) -> int:
    result = _nonnegative_projection_int(value, label)
    if result == 0:
        raise ValueError(f"prior supervisor projection {label} must be positive")
    return result


def _is_sha256(value: Any) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


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

    payload = dict(_canonical_prior_review_prompt_source(review))
    # These fields bind the persisted review to one checkpoint but do not
    # change its research judgment. Excluding them lets an unchanged semantic
    # review reuse the provider response after checkpoint resume.
    for key in _PRIOR_REVIEW_PROMPT_LINEAGE_FIELDS:
        payload.pop(key, None)
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
    payload["prior_review_semantic_hash"] = _stable_payload_hash(payload)
    payload["checkpoint_lineage_excluded_from_provider"] = True
    payload["excluded_checkpoint_lineage_fields"] = (
        _prior_review_prompt_excluded_lineage_fields(
            payload.get("schema_version")
        )
    )
    payload["full_prior_review_persisted_outside_prompt"] = True
    payload["fixed_top_n_used"] = False
    payload["prompt_projection_is_research_cap"] = False
    payload["score_authority"] = False
    return payload


_SUPERVISOR_COLLABORATION_RESPONSE_PENDING_RE = re.compile(
    r"^SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
    r"StructuredProviderUnavailable:"
    r"COLLABORATION_RESPONSE_PENDING:COLLABREQ-[0-9a-f]{64}$"
)


def _prior_supervisor_transport_wait_projection(
    review: ResearchSupervisorReview | Mapping[str, Any],
) -> tuple[bool, Mapping[str, Any] | None]:
    """Recover the semantic prior hidden by one async transport wait.

    ``_provider_pending_review`` persists the exact prior prompt projection so
    a resumed collaboration request can rebuild the same identity.  Only the
    canonical, transport-only scaffold is unwrapped here; semantic Supervisor
    gaps and noncanonical provider errors remain visible to the next review.
    """

    payload = dict(_canonical_prior_review_prompt_source(review))
    reason = str(payload.get("rationale") or "").strip()
    unresolved = tuple(
        str(value)
        for value in payload.get("unresolved_material_questions") or ()
    )
    next_actions = tuple(
        str(value) for value in payload.get("next_actions") or ()
    )
    transport_wait_only = bool(
        _SUPERVISOR_COLLABORATION_RESPONSE_PENDING_RE.fullmatch(reason)
        and unresolved == (reason,)
        and next_actions
        == ("retry LLM Research Supervisor with failure context",)
        and payload.get("status") == "NEXT_RESEARCH_REQUIRED"
        and payload.get("ready_for_independent_saturation_review") is False
        and payload.get("reasonable_positive_routes_remaining") is True
        and payload.get("counter_and_supersession_checked") is False
        and payload.get("structured_data_complete") is False
        and payload.get("component_memos_sufficient") is False
        and not (payload.get("missing_material_facts") or ())
        and not (payload.get("new_source_family_directions") or ())
        and not (payload.get("query_direction_briefs") or ())
    )
    if not transport_wait_only:
        return False, None
    restored = payload.get("prior_review_prompt_projection")
    if restored is None:
        return True, None
    if not isinstance(restored, Mapping):
        raise TypeError("pending Supervisor prior projection must be an object")
    _validate_prior_review_prompt_projection(restored)
    return True, dict(restored)


def project_current_supervisor_review(
    review: ResearchSupervisorReview | Mapping[str, Any],
) -> Mapping[str, Any]:
    """Project every current Supervisor judgment and restore exact binding.

    The shared loss-accounted projection collapses expanded failure assessments
    into semantic groups.  Saturation additionally needs the identity of the
    *current* provider review, so this wrapper restores its checkpoint-relevant
    lineage and binds the projection to the full persisted review hash.
    """

    full_review = (
        dict(review.to_dict())
        if isinstance(review, ResearchSupervisorReview)
        else dict(review)
    )
    projection = dict(_prior_supervisor_review_prompt_projection(full_review))
    projection["current_review_binding"] = {
        key: full_review.get(key)
        for key in (
            "review_id",
            "epoch",
            "prompt_hash",
            "synthesis_memo_id",
            "synthesis_memo_hash",
        )
    }
    projection["full_review_hash"] = _stable_payload_hash(full_review)
    projection["current_review_binding_preserved"] = True
    projection["full_current_review_persisted_outside_prompt"] = True
    projection["fixed_top_n_used"] = False
    projection["prompt_projection_is_research_cap"] = False
    projection["score_authority"] = False
    return projection


def _prior_supervisor_text_projection(value: Any) -> str:
    """Bound transport diagnostics while preserving normal research prose."""

    text = " ".join(str(value).split())
    text = normalize_collaboration_transport_wait(text)
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
    """Return whether the independent counter review covered the full roster.

    ``unresolved_challenges`` is an honest inventory of risks and monitoring
    limits, not a second completion flag.  The provider-backed Supervisor
    separately decides which of those items is still material and has a
    reasonable research route; those decisions are enforced by the readiness
    gates in ``_review_from_provider_response``.
    """

    return bool(
        result
        and result.status == "COMPLETE"
        and result.memo
        and set(result.memo.reviewed_component_ids)
        == set(CANONICAL_COMPONENT_ORDER)
        and result.memo.review_complete
    )


def build_counter_and_supersession_route_proof(
    *,
    source_graph_checkpoint: Mapping[str, Any],
    document_dispositions: Sequence[Mapping[str, Any]],
    evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
    required_objective_ids: Sequence[str],
) -> tuple[Mapping[str, Any], ...]:
    """Materialize verified counter/supersession lineage from persisted work.

    A query flag alone is never proof.  Each emitted row must join an executed
    counter/supersession query to an eligible full document, a successful
    extractor disposition, and a source-backed fact of the matching semantic
    kind.
    """

    required = {
        str(value).strip()
        for value in required_objective_ids
        if str(value).strip()
    }
    query_by_id = {
        str(row.get("query_id") or ""): dict(row)
        for row in source_graph_checkpoint.get("generated_queries") or ()
        if str(row.get("query_id") or "").strip()
        and str(row.get("objective_id") or "").strip() in required
        and bool(row.get("counter_or_supersession_search"))
        and str(row.get("execution_status") or "") == "SEARCH_EXECUTED"
    }
    disposition_by_document: dict[str, Mapping[str, Any]] = {}
    for source in document_dispositions:
        row = dict(source)
        document_id = str(row.get("document_id") or "").strip()
        if not document_id:
            continue
        prior = disposition_by_document.get(document_id)
        if prior is not None and dict(prior) != row:
            raise ValueError("conflicting fact-extraction document dispositions")
        disposition_by_document[document_id] = row

    fact_by_id: dict[str, EvidenceFact] = {}
    facts_by_document: dict[str, list[EvidenceFact]] = {}
    for source in evidence_facts:
        fact = _coerce_fact(source)
        if fact.fact_id in fact_by_id and fact_by_id[fact.fact_id] != fact:
            raise ValueError("conflicting EvidenceFact ids in counter route proof")
        fact_by_id[fact.fact_id] = fact
        for source_id in fact.source_ids:
            facts_by_document.setdefault(str(source_id), []).append(fact)

    members: dict[tuple[str, str], dict[str, set[str]]] = {}
    for source in source_graph_checkpoint.get("evidence_documents") or ():
        document = dict(source)
        document_id = str(document.get("document_id") or "").strip()
        if (
            not document_id
            or document.get("evidence_eligible") is not True
            or document.get("full_fetch_performed") is not True
            or bool(document.get("snippet_only"))
            or str(
                disposition_by_document.get(document_id, {}).get("status") or ""
            )
            != "FACTS_EXTRACTED"
        ):
            continue
        document_objectives = {
            str(value).strip()
            for value in document.get("objective_ids") or ()
            if str(value).strip()
        }
        linked_query_ids = {
            str(value).strip()
            for value in document.get("query_ids") or ()
            if str(value).strip()
        }
        for query_id in sorted(linked_query_ids & set(query_by_id)):
            query = query_by_id[query_id]
            objective_id = str(query.get("objective_id") or "").strip()
            if objective_id not in document_objectives:
                continue
            for fact in facts_by_document.get(document_id, ()):
                route_kind = None
                if (
                    fact.direction == "COUNTER"
                    and fact.current_lifecycle in {"CURRENT", "OPEN"}
                ):
                    route_kind = "COUNTER"
                elif (
                    fact.direction == "RESOLUTION"
                    or fact.current_lifecycle in {"RESOLVED", "SUPERSEDED"}
                ):
                    route_kind = "SUPERSESSION"
                if route_kind is None:
                    continue
                bucket = members.setdefault(
                    (objective_id, route_kind),
                    {
                        "query_ids": set(),
                        "document_ids": set(),
                        "fact_ids": set(),
                    },
                )
                bucket["query_ids"].add(query_id)
                bucket["document_ids"].add(document_id)
                bucket["fact_ids"].add(fact.fact_id)

    rows = []
    for (objective_id, route_kind), lineage in sorted(members.items()):
        rows.append(
            {
                "objective_id": objective_id,
                "route_kind": route_kind,
                "query_ids": sorted(lineage["query_ids"]),
                "document_ids": sorted(lineage["document_ids"]),
                "fact_ids": sorted(lineage["fact_ids"]),
                "parser_extractor_verified": True,
                "zero_result_only": False,
            }
        )
    return tuple(rows)


def _counter_route_proof_complete(
    rows: Sequence[Mapping[str, Any]],
    *,
    source_graph_checkpoint: Mapping[str, Any],
    evidence_facts: Sequence[EvidenceFact],
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
    document_by_id = {
        str(row.get("document_id") or row.get("source_id") or ""): row
        for row in source_graph_checkpoint.get("evidence_documents") or ()
        if str(row.get("document_id") or row.get("source_id") or "")
    }
    document_ids = set(document_by_id)
    fact_by_id = {row.fact_id: row for row in evidence_facts}
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
        route_kind = str(route_kind_value or "").upper()
        if route_kind in {"COUNTER", "SUPERSESSION"}:
            covered_route_kinds.add(route_kind)
            covered_by_objective.setdefault(objective_id, set()).add(route_kind)
        else:
            return False
        query_ids = _proof_ids(row, "query_ids", "query_id")
        proof_document_ids = _proof_ids(row, "document_ids", "document_id")
        proof_fact_ids = _proof_ids(row, "fact_ids", "fact_id")
        proof_structured_record_ids = _proof_ids(
            row, "structured_record_ids", "structured_record_id"
        )
        source_ids = _proof_ids(row, "source_ids", "source_id")
        if not (query_ids and proof_document_ids and proof_fact_ids):
            return False
        if any(query_id not in query_by_id for query_id in query_ids):
            return False
        for query_id in query_ids:
            query = query_by_id[query_id]
            if not bool(query.get("counter_or_supersession_search")):
                return False
            if str(query.get("execution_status") or "") not in {
                "SEARCH_EXECUTED",
            }:
                return False
            if str(query.get("objective_id") or "") != objective_id:
                return False
        if proof_document_ids and not set(proof_document_ids).issubset(document_ids):
            return False
        for document_id in proof_document_ids:
            document = document_by_id[document_id]
            linked_queries = {
                str(value) for value in document.get("query_ids") or ()
            }
            linked_objectives = {
                str(value) for value in document.get("objective_ids") or ()
            }
            if (
                objective_id not in linked_objectives
                or not linked_queries.intersection(query_ids)
                or document.get("evidence_eligible") is not True
                or document.get("full_fetch_performed") is not True
                or bool(document.get("snippet_only"))
            ):
                return False
        if query_ids and any(
            not any(
                query_id in {
                    str(value) for value in document_by_id[document_id].get(
                        "query_ids"
                    )
                    or ()
                }
                for document_id in proof_document_ids
            )
            for query_id in query_ids
        ):
            return False
        if proof_fact_ids and not set(proof_fact_ids).issubset(fact_by_id):
            return False
        for fact_id in proof_fact_ids:
            fact = fact_by_id[fact_id]
            if not set(fact.source_ids).intersection(proof_document_ids):
                return False
            if route_kind == "COUNTER" and not (
                fact.direction == "COUNTER"
                and fact.current_lifecycle in {"CURRENT", "OPEN"}
            ):
                return False
            if route_kind == "SUPERSESSION" and not (
                fact.direction == "RESOLUTION"
                or fact.current_lifecycle in {"RESOLVED", "SUPERSEDED"}
            ):
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
            rows.append(row)
    by_id: dict[str, Mapping[str, Any]] = {}
    for source in rows:
        row = _normalize_failure(source)
        failure_id = str(row["failure_id"])
        prior = by_id.get(failure_id)
        if prior is not None and dict(prior) != dict(row):
            raise ValueError("conflicting prior query/source failure ids")
        by_id[failure_id] = row
    generation_lineage = _query_generation_failure_lineage(
        source_graph_checkpoint,
        resolved_objectives=resolved_objectives,
    )
    normalized: dict[str, Mapping[str, Any]] = {}
    for failure_id in sorted(by_id):
        row = dict(by_id[failure_id])
        if _is_multi_objective_generation_failure(row):
            reason = str(row.get("failure_reason") or "")
            scopes = generation_lineage.get(reason) or []
            if scopes:
                row["objective_ids"] = list(scopes.pop(0))
                row["objective_lineage"] = (
                    "QUERY_GENERATION_HISTORY_FEEDBACK"
                )
        objective_ids = _failure_objective_ids(row)
        if objective_ids and set(objective_ids).issubset(resolved_objectives):
            row["resolved"] = True
            row["resolved_by"] = "SOURCE_GRAPH_OBJECTIVE_RESOLUTION"
        normalized[failure_id] = row
    return tuple(normalized[key] for key in sorted(normalized))


def _query_generation_failure_lineage(
    checkpoint: Mapping[str, Any],
    *,
    resolved_objectives: set[str],
) -> dict[str, list[tuple[str, ...]]]:
    """Recover exact query-generation scope from the persisted raw ledger."""

    source_graph = checkpoint.get("source_graph")
    graph = source_graph if isinstance(source_graph, Mapping) else {}
    raw_objectives = graph.get("open_objectives")
    objective_rows = (
        raw_objectives
        if isinstance(raw_objectives, (list, tuple))
        else ()
    )
    objective_roster = tuple(
        dict.fromkeys(
            str(row.get("objective_id") or "").strip()
            for row in objective_rows
            if isinstance(row, Mapping)
            and str(row.get("objective_id") or "").strip()
        )
    )
    roster_set = set(objective_roster)
    terminal_full_roster = bool(
        objective_roster
        and checkpoint.get("status") == "STOPPED_ON_RESOLUTION"
        and roster_set.issubset(resolved_objectives)
    )
    lineage: dict[str, list[tuple[str, ...]]] = {}
    for raw in checkpoint.get("query_generation_history") or ():
        if not isinstance(raw, Mapping):
            continue
        if (
            raw.get("deterministic_fallback_query_used") is not False
            or not str(raw.get("prompt_hash") or "").strip()
            or not str(raw.get("provider_name") or "").strip()
        ):
            continue
        explicit_scope = _string_sequence(raw.get("objective_ids"))
        observed_scope = tuple(
            dict.fromkeys(
                str(row.get("objective_id") or "").strip()
                for key in ("queries", "rejected_suggestions")
                for row in (
                    raw.get(key)
                    if isinstance(raw.get(key), (list, tuple))
                    else ()
                )
                if isinstance(row, Mapping)
                and str(row.get("objective_id") or "").strip()
            )
        )
        scope = explicit_scope or observed_scope
        if scope and (not roster_set or not set(scope).issubset(roster_set)):
            continue
        rejected_scope_by_feedback: dict[str, tuple[str, ...]] = {}
        for rejected in raw.get("rejected_suggestions") or ():
            if not isinstance(rejected, Mapping):
                continue
            objective_id = str(rejected.get("objective_id") or "").strip()
            if not objective_id or (
                roster_set and objective_id not in roster_set
            ):
                continue
            reason = str(rejected.get("reason") or "").strip()
            feedback_suffix = str(
                rejected.get("literal_query")
                or rejected.get("suggestion_index")
                or ""
            ).strip()
            if reason and feedback_suffix:
                rejected_scope_by_feedback[
                    f"{reason}:{feedback_suffix}"
                ] = (objective_id,)
        for value in raw.get("feedback_for_next_llm_call") or ():
            reason = str(value).strip()
            rejected_scope = rejected_scope_by_feedback.get(reason)
            if rejected_scope:
                lineage.setdefault(reason, []).append(rejected_scope)
                continue
            if not _is_resolvable_generation_failure_reason(reason):
                continue
            resolved_scope = scope
            if not resolved_scope and terminal_full_roster:
                resolved_scope = objective_roster
            if resolved_scope:
                lineage.setdefault(reason, []).append(resolved_scope)
    return lineage


def _is_multi_objective_generation_failure(
    row: Mapping[str, Any],
) -> bool:
    return bool(
        str(row.get("failure_kind") or "") == "QUERY_FAILURE"
        and str(row.get("query_id") or "") == "QUERY_GENERATION"
        and str(row.get("objective_id") or "") == "MULTI_OBJECTIVE"
        and str(row.get("failure_reason") or "").strip()
    )


def _is_resolvable_generation_failure_reason(reason: str) -> bool:
    return bool(
        reason == "LLM_RETURNED_NO_NEW_VALID_QUERY"
        or reason.startswith("QUERY_PROVIDER_ERROR:")
    )


def _failure_objective_ids(row: Mapping[str, Any]) -> tuple[str, ...]:
    objective_ids = _string_sequence(row.get("objective_ids"))
    objective_id = str(row.get("objective_id") or "").strip()
    if objective_id and objective_id != "MULTI_OBJECTIVE":
        objective_ids = (*objective_ids, objective_id)
    return tuple(dict.fromkeys(objective_ids))


def _string_sequence(value: Any) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)):
        return ()
    return tuple(
        dict.fromkeys(
            str(item).strip() for item in value if str(item).strip()
        )
    )


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


def _material_score_disagreement_component_ids(
    context: Mapping[str, Any] | None,
) -> tuple[str, ...]:
    """Return only semantic score disagreements, never transport waits.

    A missing judge response is an in-flight transport leaf and must not
    rewrite a complete component memo.  An aggregation-confirmed material
    disagreement is different: the three completed judges could not establish
    one intersecting range, so the semantic Supervisor must send that exact
    component back for clarification.
    """

    if context is None:
        return ()
    if not isinstance(context, Mapping):
        raise TypeError("score gap context must be an object")
    requests = context.get("component_research_requests") or ()
    if isinstance(requests, (str, bytes)) or not isinstance(
        requests, Sequence
    ):
        raise TypeError("component score research requests must be an array")
    component_ids = []
    for row in requests:
        if not isinstance(row, Mapping):
            raise TypeError("component score research request must be an object")
        reasons = row.get("reason_codes") or ()
        if isinstance(reasons, (str, bytes)) or not isinstance(
            reasons, Sequence
        ):
            raise TypeError("component score research reasons must be an array")
        if "UNRESOLVED_MATERIAL_JUDGE_DISAGREEMENT" not in {
            str(value) for value in reasons
        }:
            continue
        component_id = str(row.get("component_id") or "")
        if component_id not in CANONICAL_COMPONENT_ORDER:
            raise ValueError(
                "material score disagreement has an unknown component"
            )
        component_ids.append(component_id)
    return tuple(
        component_id
        for component_id in CANONICAL_COMPONENT_ORDER
        if component_id in set(component_ids)
    )


def _transport_wait_score_component_ids(
    context: Mapping[str, Any] | None,
) -> tuple[str, ...]:
    """Identify score requests caused only by missing provider responses."""

    if context is None:
        return ()
    if not isinstance(context, Mapping):
        raise TypeError("score gap context must be an object")
    requests = context.get("component_research_requests") or ()
    if isinstance(requests, (str, bytes)) or not isinstance(
        requests, Sequence
    ):
        raise TypeError("component score research requests must be an array")
    component_ids = []
    for row in requests:
        if not isinstance(row, Mapping):
            raise TypeError("component score research request must be an object")
        reasons = row.get("reason_codes") or ()
        if isinstance(reasons, (str, bytes)) or not isinstance(
            reasons, Sequence
        ):
            raise TypeError("component score research reasons must be an array")
        normalized = tuple(str(value) for value in reasons)
        if (
            normalized
            and "UNRESOLVED_MATERIAL_JUDGE_DISAGREEMENT" not in normalized
            and any(
                reason in {
                    "COMPONENT_SCORING_MEMO_NOT_READY",
                    "COMPONENT_SCORING_MEMO_RUN_NOT_READY",
                    "THREE_VALID_JUDGE_CONSENSUS_MISSING",
                }
                or "PROVIDER_ERROR:" in reason
                or "COLLABORATION_RESPONSE_PENDING" in reason
                for reason in normalized
            )
        ):
            component_id = str(row.get("component_id") or "")
            if component_id not in CANONICAL_COMPONENT_ORDER:
                raise ValueError(
                    "transport score wait has an unknown component"
                )
            component_ids.append(component_id)
    return tuple(
        component_id
        for component_id in CANONICAL_COMPONENT_ORDER
        if component_id in set(component_ids)
    )


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
    failure_by_id: Mapping[str, Mapping[str, Any]],
    failure_group_members: Mapping[str, Sequence[str]],
) -> Mapping[str, Any]:
    """Return exact bounded roster and absence-proof rewrite feedback.

    Failure classification remains provider-owned.  These diagnostics expose
    the deterministic validation boundary that rejected the prior answer, so
    the one allowed rewrite knows which semantic groups cannot lawfully claim
    source absence and does not carry an incompatible permission boolean into
    a non-absence classification.
    """

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
    response_by_id = {
        str(row.get("failure_id") or ""): row
        for row in raw_rows or ()
        if isinstance(row, Mapping)
        and str(row.get("failure_id") or "").strip()
    }
    duplicate_ids = sorted(
        value for value, count in received_counts.items() if count > 1
    )
    absence_proof_valid_ids = []
    absence_proof_invalid_ids = []
    permission_class_mismatch_ids = []
    for group_id in required_ids:
        member_ids = tuple(
            str(value) for value in failure_group_members.get(group_id) or ()
        )
        proof_valid = bool(member_ids) and all(
            member_id in failure_by_id
            and _source_absence_proof_valid(failure_by_id[member_id])
            for member_id in member_ids
        )
        (
            absence_proof_valid_ids
            if proof_valid
            else absence_proof_invalid_ids
        ).append(group_id)
        prior_row = response_by_id.get(group_id)
        if (
            isinstance(prior_row, Mapping)
            and prior_row.get("source_absence_claim_allowed") is True
            and str(prior_row.get("classification") or "")
            != "SOURCE_ABSENCE_CANDIDATE"
        ):
            permission_class_mismatch_ids.append(group_id)
    return {
        "required_count": len(required_ids),
        "received_count": len(received_ids),
        "missing_failure_group_ids": sorted(required_set - received_set),
        "extra_failure_group_ids": sorted(received_set - required_set),
        "duplicate_failure_group_ids": duplicate_ids,
        "failure_assessments_array_was_valid": response_array_valid,
        "received_failure_group_roster_hash": _stable_payload_hash(received_ids),
        "required_failure_group_roster_hash": _stable_payload_hash(required_ids),
        "source_absence_proof_valid_group_ids": absence_proof_valid_ids,
        "source_absence_proof_invalid_group_ids": absence_proof_invalid_ids,
        "source_absence_permission_class_mismatch_group_ids": (
            permission_class_mismatch_ids
        ),
    }


def _clean_error(error: Exception) -> str:
    return " ".join(str(error).split())[-500:] or error.__class__.__name__


__all__ = [
    "build_counter_and_supersession_route_proof",
    "project_current_supervisor_review",
    "ResearchSupervisor",
    "ResearchSupervisorReview",
    "SUPERVISOR_FAILURE_CLASSES",
    "SupervisorComponentFinding",
    "SupervisorFactGap",
    "SupervisorFailureAssessment",
    "SupervisorQueryDirection",
    "SupervisorSourceDirection",
]
