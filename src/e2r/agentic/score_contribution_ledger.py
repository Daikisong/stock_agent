"""ScoreContributionV2 construction from primitive states."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from .evidence_os import PrimitiveStateV2, PrimitiveStatus, ScoreContributionV2


DEFAULT_SCORE_COMPONENT_MAX_POINTS: Mapping[str, float] = {
    "eps_fcf_explosion": 20.0,
    "earnings_visibility": 20.0,
    "bottleneck_pricing": 20.0,
    "market_mispricing": 15.0,
    "valuation_rerating": 15.0,
    "capital_allocation": 5.0,
    "information_confidence": 5.0,
}


@dataclass(frozen=True)
class PrimitiveScoreRule:
    component_key: str
    criterion_id: str
    primitive_id: str
    points: float
    max_points: float
    claim_side: str = "support"

    def __post_init__(self) -> None:
        if self.claim_side not in {"support", "counter"}:
            raise ValueError("claim_side must be support or counter")
        if self.points < 0 or self.max_points < 0:
            raise ValueError("points and max_points must be non-negative")


def build_score_contributions_from_primitives(
    *,
    primitive_states: Mapping[str, PrimitiveStateV2],
    rules: Sequence[PrimitiveScoreRule],
) -> tuple[ScoreContributionV2, ...]:
    contributions: list[ScoreContributionV2] = []
    for rule in rules:
        state = primitive_states.get(rule.primitive_id)
        if state is None:
            contributions.append(_zero_contribution(rule, cap_reason="primitive_missing_from_state"))
            continue
        claim_ids = state.support_claim_ids if rule.claim_side == "support" else state.counter_claim_ids
        mapping_ids = state.support_mapping_ids if rule.claim_side == "support" else state.counter_mapping_ids
        source_family_ids = (
            state.support_source_family_ids if rule.claim_side == "support" else state.counter_source_family_ids
        )
        if state.status != PrimitiveStatus.PRESENT_CURRENT:
            contributions.append(_zero_contribution(rule, cap_reason=f"primitive_status:{state.status.value}"))
            continue
        if not claim_ids:
            contributions.append(_zero_contribution(rule, cap_reason="no_claim_ids_for_rule_side"))
            continue
        if not mapping_ids:
            contributions.append(_zero_contribution(rule, cap_reason="no_mapping_ids_for_rule_side"))
            continue
        if not source_family_ids:
            contributions.append(_zero_contribution(rule, cap_reason="no_source_family_ids_for_rule_side"))
            continue
        contributions.append(
            ScoreContributionV2.build(
                component_key=rule.component_key,
                criterion_id=rule.criterion_id,
                raw_points=min(rule.points, rule.max_points),
                max_points=rule.max_points,
                support_claim_ids=tuple(claim_ids),
                mapping_ids=tuple(mapping_ids),
                source_family_ids=tuple(source_family_ids),
                rationale=f"primitive:{rule.primitive_id}",
            )
        )
    return tuple(contributions)


def build_component_score_contributions_from_rubric(
    *,
    components: Mapping[str, float],
    primitive_states: Mapping[str, PrimitiveStateV2],
    score_rubric: Mapping[str, Sequence[str]],
    component_max_points: Mapping[str, float] = DEFAULT_SCORE_COMPONENT_MAX_POINTS,
) -> tuple[ScoreContributionV2, ...]:
    """Build component-level contributions from an explicit contract rubric.

    This does not infer component support from primitive names.  The contract
    decides which primitives can support each score component.
    """

    contributions: list[ScoreContributionV2] = []
    for component_key, raw_value in components.items():
        primitive_ids = tuple(dict.fromkeys(str(item).strip() for item in score_rubric.get(component_key, ()) if str(item).strip()))
        max_points = float(component_max_points.get(component_key, raw_value))
        (
            support_claim_ids,
            counter_claim_ids,
            mapping_ids,
            source_family_ids,
            cap_reasons,
            present_count,
        ) = _claim_ids_for_component_rubric(
            primitive_ids=primitive_ids,
            primitive_states=primitive_states,
        )
        raw_points = _rubric_component_points(max_points=max_points, primitive_ids=primitive_ids, present_count=present_count)
        if raw_points > 0.0 and support_claim_ids and mapping_ids and source_family_ids:
            contributions.append(
                ScoreContributionV2.build(
                    component_key=component_key,
                    criterion_id=f"agentic_v2_rubric_{component_key}",
                    raw_points=raw_points,
                    max_points=max_points,
                    support_claim_ids=support_claim_ids,
                    counter_claim_ids=counter_claim_ids,
                    mapping_ids=mapping_ids,
                    source_family_ids=source_family_ids,
                    rationale="agentic Evidence Contract v2 score_rubric component support",
                )
            )
            continue
        cap_reason = _component_cap_reason(raw_points=raw_points, primitive_ids=primitive_ids, cap_reasons=cap_reasons)
        contributions.append(
            ScoreContributionV2.build(
                component_key=component_key,
                criterion_id=f"agentic_v2_rubric_{component_key}",
                raw_points=0.0,
                max_points=max_points,
                support_claim_ids=(),
                counter_claim_ids=counter_claim_ids,
                mapping_ids=mapping_ids,
                source_family_ids=source_family_ids,
                cap_reason=cap_reason,
                rationale="agentic Evidence Contract v2 score_rubric component support",
            )
        )
    return tuple(contributions)


def _claim_ids_for_component_rubric(
    *,
    primitive_ids: Sequence[str],
    primitive_states: Mapping[str, PrimitiveStateV2],
) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...], tuple[str, ...], tuple[str, ...], int]:
    support_claim_ids: list[str] = []
    counter_claim_ids: list[str] = []
    mapping_ids: list[str] = []
    source_family_ids: list[str] = []
    cap_reasons: list[str] = []
    if not primitive_ids:
        return (), (), (), (), ("score_rubric_component_empty",), 0
    present_count = 0
    for primitive_id in primitive_ids:
        state = primitive_states.get(primitive_id)
        if state is None:
            cap_reasons.append(f"{primitive_id}:primitive_missing_from_state")
            continue
        counter_claim_ids.extend(state.counter_claim_ids)
        mapping_ids.extend(state.counter_mapping_ids)
        source_family_ids.extend(state.counter_source_family_ids)
        if state.status == PrimitiveStatus.PRESENT_CURRENT and state.support_claim_ids:
            present_count += 1
            support_claim_ids.extend(state.support_claim_ids)
            mapping_ids.extend(state.support_mapping_ids)
            source_family_ids.extend(state.support_source_family_ids)
            if not state.support_mapping_ids:
                cap_reasons.append(f"{primitive_id}:mapping_ids_missing")
            if not state.support_source_family_ids:
                cap_reasons.append(f"{primitive_id}:source_family_ids_missing")
            continue
        cap_reasons.append(f"{primitive_id}:primitive_status:{state.status.value}")
    return (
        tuple(dict.fromkeys(support_claim_ids)),
        tuple(dict.fromkeys(counter_claim_ids)),
        tuple(dict.fromkeys(mapping_ids)),
        tuple(dict.fromkeys(source_family_ids)),
        tuple(dict.fromkeys(cap_reasons)),
        present_count,
    )


def _rubric_component_points(*, max_points: float, primitive_ids: Sequence[str], present_count: int) -> float:
    if max_points <= 0.0 or not primitive_ids or present_count <= 0:
        return 0.0
    coverage = min(float(present_count) / float(len(tuple(primitive_ids))), 1.0)
    return round(max_points * coverage, 4)


def _component_cap_reason(
    *,
    raw_points: float,
    primitive_ids: Sequence[str],
    cap_reasons: Sequence[str],
) -> str:
    if not primitive_ids:
        return "score_rubric_component_empty"
    if raw_points <= 0.0:
        return ";".join(dict.fromkeys(cap_reasons)) or "zero component score"
    return ";".join(dict.fromkeys(cap_reasons)) or "score_rubric_no_present_support_claim_ids"


def _zero_contribution(rule: PrimitiveScoreRule, *, cap_reason: str) -> ScoreContributionV2:
    return ScoreContributionV2.build(
        component_key=rule.component_key,
        criterion_id=rule.criterion_id,
        raw_points=0.0,
        max_points=rule.max_points,
        support_claim_ids=(),
        cap_reason=cap_reason,
        rationale=f"primitive:{rule.primitive_id}",
    )


__all__ = [
    "DEFAULT_SCORE_COMPONENT_MAX_POINTS",
    "PrimitiveScoreRule",
    "build_component_score_contributions_from_rubric",
    "build_score_contributions_from_primitives",
]
