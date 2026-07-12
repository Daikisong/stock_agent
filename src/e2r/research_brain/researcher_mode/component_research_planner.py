"""Plan seven open-ended component investigations from contracts and memory.

The planner creates research questions, not web-search strings and not score
gates.  Every current fact is visible to every component researcher so a new
economic mechanism is not discarded just because an old primitive catalog did
not anticipate it.
"""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)

from .schemas import (
    CANONICAL_COMPONENT_ORDER,
    ComponentAnchor,
    ComponentResearchPlan,
    EvidenceFact,
)
from .research_question_seed_catalog import ResearchQuestionSeed


COMPONENT_RESEARCHER_ROLE_BY_COMPONENT: Mapping[str, str] = {
    "eps_fcf_explosion": "EPSFCFResearcher",
    "earnings_visibility": "EarningsVisibilityResearcher",
    "bottleneck_pricing": "BottleneckPricingResearcher",
    "market_mispricing": "MarketExpectationResearcher",
    "valuation_rerating": "ValuationResearcher",
    "capital_allocation": "CapitalAllocationResearcher",
    "information_confidence": "InformationConfidenceResearcher",
}


class ComponentResearchPlanner:
    """Build one independent plan for each canonical broad component."""

    def plan(
        self,
        *,
        target_id: str,
        archetype_id: str,
        evidence_facts: Sequence[EvidenceFact | Mapping[str, Any]],
        historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
        research_seeds: Sequence[ResearchQuestionSeed | Mapping[str, Any]] = (),
        component_max_points: Mapping[str, float] | None = None,
        structured_metric_requirements: Mapping[str, Sequence[str]] | None = None,
    ) -> tuple[ComponentResearchPlan, ...]:
        maxima, contract_requirements = _resolve_component_contract(
            archetype_id=archetype_id,
            component_max_points=component_max_points,
        )
        requirements = {
            component_id: tuple(values)
            for component_id, values in (
                structured_metric_requirements or contract_requirements
            ).items()
        }
        fact_ids = tuple(
            dict.fromkeys(
                _required_id(row, "fact_id") for row in evidence_facts
            )
        )
        plans = []
        for component_id in CANONICAL_COMPONENT_ORDER:
            matching_seeds = tuple(
                row
                for row in research_seeds
                if _seed_matches(row, archetype_id, component_id)
            )
            anchor_ids = tuple(
                dict.fromkeys(
                    _required_id(row, "anchor_id")
                    for row in historical_anchors
                    if _field(row, "archetype_id") == archetype_id
                    and _field(row, "component_id") == component_id
                )
            )
            questions = tuple(
                dict.fromkeys(
                    value
                    for seed in matching_seeds
                    for value in _sequence_field(seed, "research_predicates")
                    if value
                )
            ) or (
                "현재 증거와 반증을 함께 읽고 이 component의 경제적 강도와 지속성을 조사한다",
                "추가 source family에서 확인하거나 반박해야 할 material fact를 식별한다",
            )
            source_routes = tuple(
                dict.fromkeys(
                    value
                    for seed in matching_seeds
                    for value in _sequence_field(seed, "source_route_hints")
                    if value
                )
            )
            counter_routes = tuple(
                dict.fromkeys(
                    value
                    for seed in matching_seeds
                    for value in _sequence_field(seed, "counter_route_hints")
                    if value
                )
            )
            payload = {
                "target_id": target_id,
                "archetype_id": archetype_id,
                "component_id": component_id,
                "researcher_role": COMPONENT_RESEARCHER_ROLE_BY_COMPONENT[component_id],
                "component_max_points": maxima[component_id],
                "research_questions": questions,
                "source_route_hints": source_routes,
                "counter_route_hints": counter_routes,
                # Deliberately all facts: primitive/tag matching is not a gateway.
                "candidate_fact_ids": fact_ids,
                "candidate_anchor_ids": anchor_ids,
            }
            plans.append(
                ComponentResearchPlan(
                    plan_id=stable_intelligence_id("CRPLAN", payload),
                    target_id=target_id,
                    archetype_id=archetype_id,
                    component_id=component_id,
                    researcher_role=COMPONENT_RESEARCHER_ROLE_BY_COMPONENT[
                        component_id
                    ],
                    component_max_points=maxima[component_id],
                    research_questions=questions,
                    source_route_hints=source_routes,
                    counter_route_hints=counter_routes,
                    structured_metric_requirements=tuple(
                        dict.fromkeys(requirements.get(component_id, ()))
                    ),
                    candidate_fact_ids=fact_ids,
                    candidate_anchor_ids=anchor_ids,
                )
            )
        return tuple(plans)


def _resolve_component_contract(
    *,
    archetype_id: str,
    component_max_points: Mapping[str, float] | None,
) -> tuple[Mapping[str, float], Mapping[str, Sequence[str]]]:
    contract = None
    if component_max_points is None:
        contract = load_archetype_scoring_contract(archetype_id)
        component_max_points = contract.component_max_points
    missing = set(CANONICAL_COMPONENT_ORDER) - set(component_max_points)
    extra = set(component_max_points) - set(CANONICAL_COMPONENT_ORDER)
    if missing or extra:
        raise ValueError(
            f"component maxima must contain exactly seven components; missing={sorted(missing)}, extra={sorted(extra)}"
        )
    maxima = {
        component_id: float(component_max_points[component_id])
        for component_id in CANONICAL_COMPONENT_ORDER
    }
    if any(value <= 0 for value in maxima.values()):
        raise ValueError("all component maxima must be positive")
    requirements = (
        contract.component_required_evidence_roles if contract is not None else {}
    )
    return maxima, requirements


def _seed_matches(
    row: ResearchQuestionSeed | Mapping[str, Any],
    archetype_id: str,
    component_id: str,
) -> bool:
    return (
        _field(row, "archetype_id") == archetype_id
        and component_id in _sequence_field(row, "component_topic_hints")
    )


def _field(row: Any, key: str) -> Any:
    if isinstance(row, Mapping):
        return row.get(key)
    return getattr(row, key)


def _sequence_field(row: Any, key: str) -> tuple[str, ...]:
    value = _field(row, key) or ()
    return tuple(str(item) for item in value if str(item).strip())


def _required_id(row: Any, key: str) -> str:
    value = str(_field(row, key) or "").strip()
    if not value:
        raise ValueError(f"{key} is required")
    return value


__all__ = [
    "COMPONENT_RESEARCHER_ROLE_BY_COMPONENT",
    "ComponentResearchPlanner",
]
