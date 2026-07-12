"""Checkpoint-oriented research supervision without fixed-round completion."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id

from .component_researcher import ComponentResearchResult
from .red_team_researcher import RedTeamResearchResult
from .schemas import CANONICAL_COMPONENT_ORDER
from .structured_data_researcher import StructuredResearchResult


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

    def __post_init__(self) -> None:
        if self.epoch < 0:
            raise ValueError("research epoch cannot be negative")
        if self.status not in {
            "NEXT_RESEARCH_REQUIRED",
            "READY_FOR_INDEPENDENT_SATURATION_REVIEW",
        }:
            raise ValueError("unknown supervisor review status")
        if self.completion_based_on_round_count:
            raise ValueError("fixed round count cannot complete research")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


class ResearchSupervisor:
    """Turns component/source failures into the next semantic research action."""

    reviewer_role = "ResearchSupervisor"

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
                    f"{component_id}:analyze prior source/provider failure and choose a new route"
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
        if source_gaps:
            next_actions.extend(
                f"review source family {family}" for family in source_gaps
            )
        parser_failures = tuple(dict.fromkeys(parser_or_extractor_failures))
        if parser_failures:
            next_actions.append(
                "repair parser/extractor and reprocess already fetched documents"
            )
        ready = bool(
            set(by_component) == set(CANONICAL_COMPONENT_ORDER)
            and all(row.status == "COMPLETE" for row in by_component.values())
            and red_team_complete
            and not (
                red_team_result.memo.unresolved_challenges
                if red_team_result and red_team_result.memo
                else ()
            )
            and structured_complete
            and not source_gaps
            and not parser_failures
            and not any(
                row.memo and row.memo.uncertainties for row in by_component.values()
            )
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
        )


__all__ = ["ResearchSupervisor", "ResearchSupervisorReview"]
