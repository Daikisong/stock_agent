"""Canonical schemas for E2R v5 Researcher Mode."""

from __future__ import annotations

import json
import math
import re
from dataclasses import asdict, dataclass
from datetime import date
from enum import Enum
from typing import Any, Mapping, Sequence


CANONICAL_COMPONENT_ORDER = (
    "eps_fcf_explosion",
    "earnings_visibility",
    "bottleneck_pricing",
    "market_mispricing",
    "valuation_rerating",
    "capital_allocation",
    "information_confidence",
)

# This is the generic 100-point fallback only.  Runtime planning should prefer
# the selected archetype contract's component_max_points.
CANONICAL_COMPONENT_MAX_POINTS: Mapping[str, float] = {
    "eps_fcf_explosion": 20.0,
    "earnings_visibility": 20.0,
    "bottleneck_pricing": 20.0,
    "market_mispricing": 15.0,
    "valuation_rerating": 15.0,
    "capital_allocation": 5.0,
    "information_confidence": 5.0,
}


class EvidenceDirection(str, Enum):
    POSITIVE = "POSITIVE"
    COUNTER = "COUNTER"
    NEUTRAL = "NEUTRAL"
    RESOLUTION = "RESOLUTION"


class EvidenceLifecycle(str, Enum):
    OPEN = "OPEN"
    CURRENT = "CURRENT"
    RESOLVED = "RESOLVED"
    SUPERSEDED = "SUPERSEDED"


class ComponentJudgeRole(str, Enum):
    ANALYST = "ANALYST"
    SKEPTIC = "SKEPTIC"
    CALIBRATION_JUDGE = "CALIBRATION_JUDGE"


class HistoricalScoreSchemaType(str, Enum):
    DIRECT_COMPONENT_POINTS = "DIRECT_COMPONENT_POINTS"
    NORMALIZED_COMPONENT_RATINGS = "NORMALIZED_COMPONENT_RATINGS"
    CUSTOM_ARCHETYPE_POINTS = "CUSTOM_ARCHETYPE_POINTS"
    TOTAL_ONLY_PROXY = "TOTAL_ONLY_PROXY"
    RULE_ONLY = "RULE_ONLY"
    NO_SCORE = "NO_SCORE"


class AnchorConfidence(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


@dataclass(frozen=True)
class HistoricalResearchJudgment:
    judgment_id: str
    research_case_id: str
    archetype_id: str
    as_of_date: str | None
    source_quality: str
    fact_signatures: tuple[str, ...]
    counter_fact_signatures: tuple[str, ...]
    score_schema_type: str
    normalized_component_vector: Mapping[str, float]
    component_max_points: Mapping[str, float]
    reported_total_proxy: float | None
    reported_stage: str | None
    future_outcome_ref: str | None
    usable_as_exact_anchor: bool
    usable_as_ordinal_anchor: bool
    anchor_confidence: str
    company_name: str
    symbol: str
    source_file: str
    source_row_ids: tuple[str, ...]
    score_source_row_ids: tuple[str, ...]
    score_mapping_confidence: str
    score_conflict: bool = False
    runtime_score_eligible: bool = False
    runtime_prompt_future_outcome_allowed: bool = False
    schema_version: str = "e2r_historical_research_judgment_v1"

    def __post_init__(self) -> None:
        HistoricalScoreSchemaType(self.score_schema_type)
        AnchorConfidence(self.anchor_confidence)
        if not self.judgment_id or not self.research_case_id or not self.archetype_id:
            raise ValueError("historical judgment identity is required")
        if self.runtime_score_eligible or self.runtime_prompt_future_outcome_allowed:
            raise ValueError("historical judgments cannot directly score current evidence")
        if self.usable_as_exact_anchor and self.anchor_confidence != AnchorConfidence.HIGH.value:
            raise ValueError("exact historical anchors require HIGH confidence")
        if self.usable_as_exact_anchor and not self.normalized_component_vector:
            raise ValueError("exact historical anchors require a component vector")
        for component_id, points in self.normalized_component_vector.items():
            maximum = float(self.component_max_points.get(component_id, -1.0))
            if maximum < 0 or not 0.0 <= float(points) <= maximum + 1e-9:
                raise ValueError("historical component points exceed canonical range")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)

    def to_runtime_anchor(self) -> Mapping[str, Any]:
        """Return the blind-safe anchor payload exposed to current researchers."""

        return {
            "judgment_id": self.judgment_id,
            "research_case_id": self.research_case_id,
            "archetype_id": self.archetype_id,
            "as_of_date": self.as_of_date,
            "source_quality": self.source_quality,
            "fact_signatures": list(self.fact_signatures),
            "counter_fact_signatures": list(self.counter_fact_signatures),
            "score_schema_type": self.score_schema_type,
            "normalized_component_vector": dict(self.normalized_component_vector),
            "component_max_points": dict(self.component_max_points),
            "reported_total_proxy": self.reported_total_proxy,
            "reported_stage": self.reported_stage,
            "usable_as_exact_anchor": self.usable_as_exact_anchor,
            "usable_as_ordinal_anchor": self.usable_as_ordinal_anchor,
            "anchor_confidence": self.anchor_confidence,
            "score_mapping_confidence": self.score_mapping_confidence,
        }


@dataclass(frozen=True)
class ComponentAnchor:
    anchor_id: str
    archetype_id: str
    component_id: str
    economic_fact_patterns: tuple[str, ...]
    role: str
    score_band: str
    points_lower: float
    points_mid: float
    points_upper: float
    max_points: float
    source_backed_case_ids: tuple[str, ...]
    source_proxy_guard_case_ids: tuple[str, ...]
    source_score_anchor_ids: tuple[str, ...]
    confidence: str
    usable_as_exact_anchor: bool
    usable_as_ordinal_anchor: bool
    company_name_conditioned: bool = False
    target_symbol_conditioned: bool = False
    schema_version: str = "e2r_component_anchor_v1"

    def __post_init__(self) -> None:
        AnchorConfidence(self.confidence)
        if not self.anchor_id or not self.archetype_id or not self.component_id:
            raise ValueError("component anchor identity is required")
        if not 0.0 <= self.points_lower <= self.points_mid <= self.points_upper <= self.max_points:
            raise ValueError("component anchor point band is invalid")
        if self.usable_as_exact_anchor and (
            self.confidence != AnchorConfidence.HIGH.value
            or not self.source_backed_case_ids
            or self.source_proxy_guard_case_ids
        ):
            raise ValueError("exact component anchors require source-backed HIGH lineage")
        if self.company_name_conditioned or self.target_symbol_conditioned:
            raise ValueError("component anchors must be economic-fact based")

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class EvidenceFact:
    """One source-backed economic fact used by open-ended researchers.

    Question families and primitive ids may be attached by upstream systems,
    but neither is required here.  The economic mechanism and source lineage
    are the canonical identity, so a previously unseen but material fact does
    not disappear merely because no exact primitive exists yet.
    """

    fact_id: str
    target_id: str
    as_of_date: str
    subject: str
    business_segment: str
    product_family: str
    economic_mechanism: str
    predicate: str
    value: Any
    unit: str | None
    period: str
    direction: str
    source_ids: tuple[str, ...]
    claim_ids: tuple[str, ...]
    quote_ids: tuple[str, ...]
    current_lifecycle: str
    source_independence_group: str
    confidence: float
    corroborating_independence_groups: tuple[str, ...] = ()
    question_family_tags: tuple[str, ...] = ()
    primitive_tags: tuple[str, ...] = ()
    allowed_component_ids: tuple[str, ...] = ()
    structured_evidence_roles: tuple[str, ...] = ()
    schema_version: str = "e2r_evidence_fact_v1"

    def __post_init__(self) -> None:
        for value, label in (
            (self.fact_id, "fact_id"),
            (self.target_id, "target_id"),
            (self.subject, "subject"),
            (self.economic_mechanism, "economic_mechanism"),
            (self.predicate, "predicate"),
            (self.period, "period"),
            (self.source_independence_group, "source_independence_group"),
        ):
            _require_text(value, label)
        _require_iso_date(self.as_of_date, "as_of_date")
        EvidenceDirection(self.direction)
        EvidenceLifecycle(self.current_lifecycle)
        _require_probability(self.confidence, "confidence")
        _require_unique_texts(self.source_ids, "source_ids", allow_empty=False)
        _require_unique_texts(self.claim_ids, "claim_ids", allow_empty=True)
        _require_unique_texts(self.quote_ids, "quote_ids", allow_empty=True)
        if not self.claim_ids and not self.quote_ids:
            raise ValueError("EvidenceFact requires claim or quote lineage")
        _require_unique_texts(
            self.corroborating_independence_groups,
            "corroborating_independence_groups",
            allow_empty=True,
        )
        _require_unique_texts(
            self.question_family_tags, "question_family_tags", allow_empty=True
        )
        _require_unique_texts(self.primitive_tags, "primitive_tags", allow_empty=True)
        _require_unique_texts(
            self.allowed_component_ids, "allowed_component_ids", allow_empty=True
        )
        _require_unique_texts(
            self.structured_evidence_roles,
            "structured_evidence_roles",
            allow_empty=True,
        )
        if set(self.allowed_component_ids) - set(CANONICAL_COMPONENT_ORDER):
            raise ValueError(
                "EvidenceFact allowed_component_ids contains unknown component"
            )
        if set(self.structured_evidence_roles) - {
            "SEGMENT_CONTRIBUTION",
            "QOQ_GROWTH",
            "FORWARD_GUIDANCE",
            "LATEST_ACTUAL_DEPRECIATION_AMORTIZATION",
            "EPS_REVISION",
            "OPERATING_PROFIT_REVISION",
            "FORWARD_BOOK_VALUE",
            "FORWARD_PB",
            "FORWARD_EV_EBITDA",
            "DURABLE_VISIBILITY",
        }:
            raise ValueError("EvidenceFact contains unknown structured evidence role")

    def to_dict(self) -> Mapping[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class BusinessModelMemo:
    memo_id: str
    target_id: str
    archetype_id: str
    as_of_date: str
    business_model_summary: str
    revenue_engines: tuple[str, ...]
    cost_and_cash_drivers: tuple[str, ...]
    capacity_and_supply_constraints: tuple[str, ...]
    customer_and_channel_dependencies: tuple[str, ...]
    fact_ids: tuple[str, ...]
    source_ids: tuple[str, ...]
    uncertainties: tuple[str, ...]
    confidence: float
    research_complete: bool
    schema_version: str = "e2r_business_model_memo_v1"

    def __post_init__(self) -> None:
        for value, label in (
            (self.memo_id, "memo_id"),
            (self.target_id, "target_id"),
            (self.archetype_id, "archetype_id"),
            (self.business_model_summary, "business_model_summary"),
        ):
            _require_text(value, label)
        _require_iso_date(self.as_of_date, "as_of_date")
        _require_probability(self.confidence, "confidence")
        for values, label, allow_empty in (
            (self.revenue_engines, "revenue_engines", False),
            (self.cost_and_cash_drivers, "cost_and_cash_drivers", True),
            (
                self.capacity_and_supply_constraints,
                "capacity_and_supply_constraints",
                True,
            ),
            (
                self.customer_and_channel_dependencies,
                "customer_and_channel_dependencies",
                True,
            ),
            (self.fact_ids, "fact_ids", True),
            (self.source_ids, "source_ids", True),
            (self.uncertainties, "uncertainties", True),
        ):
            _require_unique_texts(values, label, allow_empty=allow_empty)
        if self.research_complete and (not self.fact_ids or not self.source_ids):
            raise ValueError("complete business-model research requires source-backed facts")

    def to_dict(self) -> Mapping[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ComponentResearchPlan:
    plan_id: str
    target_id: str
    archetype_id: str
    component_id: str
    researcher_role: str
    component_max_points: float
    research_questions: tuple[str, ...]
    source_route_hints: tuple[str, ...]
    counter_route_hints: tuple[str, ...]
    structured_metric_requirements: tuple[str, ...]
    candidate_fact_ids: tuple[str, ...]
    candidate_anchor_ids: tuple[str, ...]
    schema_version: str = "e2r_component_research_plan_v1"

    def __post_init__(self) -> None:
        for value, label in (
            (self.plan_id, "plan_id"),
            (self.target_id, "target_id"),
            (self.archetype_id, "archetype_id"),
            (self.component_id, "component_id"),
            (self.researcher_role, "researcher_role"),
        ):
            _require_text(value, label)
        _require_component(self.component_id)
        _require_positive(self.component_max_points, "component_max_points")
        _require_unique_texts(
            self.research_questions, "research_questions", allow_empty=False
        )
        for values, label in (
            (self.source_route_hints, "source_route_hints"),
            (self.counter_route_hints, "counter_route_hints"),
            (self.structured_metric_requirements, "structured_metric_requirements"),
            (self.candidate_fact_ids, "candidate_fact_ids"),
            (self.candidate_anchor_ids, "candidate_anchor_ids"),
        ):
            _require_unique_texts(values, label, allow_empty=True)

    def to_dict(self) -> Mapping[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ComponentResearchMemo:
    memo_id: str
    target_id: str
    archetype_id: str
    component_id: str
    component_max_points: float
    positive_fact_ids: tuple[str, ...]
    counter_fact_ids: tuple[str, ...]
    resolution_fact_ids: tuple[str, ...]
    structured_metrics: Mapping[str, Any]
    historical_anchor_ids: tuple[str, ...]
    researcher_summary: str
    positive_case: str
    counter_case: str
    uncertainties: tuple[str, ...]
    source_coverage: tuple[str, ...]
    proposed_score_lower: float
    proposed_score_mid: float
    proposed_score_upper: float
    confidence: float
    research_complete: bool
    nearest_positive_anchor_ids: tuple[str, ...]
    nearest_counter_anchor_ids: tuple[str, ...]
    why_not_higher: str
    why_not_lower: str
    researcher_role: str
    context_fact_ids: tuple[str, ...] = ()
    schema_version: str = "e2r_component_research_memo_v2"

    def __post_init__(self) -> None:
        for value, label in (
            (self.memo_id, "memo_id"),
            (self.target_id, "target_id"),
            (self.archetype_id, "archetype_id"),
            (self.component_id, "component_id"),
            (self.researcher_summary, "researcher_summary"),
            (self.positive_case, "positive_case"),
            (self.counter_case, "counter_case"),
            (self.why_not_higher, "why_not_higher"),
            (self.why_not_lower, "why_not_lower"),
            (self.researcher_role, "researcher_role"),
        ):
            _require_text(value, label)
        _require_component(self.component_id)
        _require_positive(self.component_max_points, "component_max_points")
        _require_score_band(
            self.proposed_score_lower,
            self.proposed_score_mid,
            self.proposed_score_upper,
            self.component_max_points,
        )
        _require_probability(self.confidence, "confidence")
        for values, label in (
            (self.positive_fact_ids, "positive_fact_ids"),
            (self.counter_fact_ids, "counter_fact_ids"),
            (self.resolution_fact_ids, "resolution_fact_ids"),
            (self.context_fact_ids, "context_fact_ids"),
            (self.historical_anchor_ids, "historical_anchor_ids"),
            (self.uncertainties, "uncertainties"),
            (self.source_coverage, "source_coverage"),
            (self.nearest_positive_anchor_ids, "nearest_positive_anchor_ids"),
            (self.nearest_counter_anchor_ids, "nearest_counter_anchor_ids"),
        ):
            _require_unique_texts(values, label, allow_empty=True)
        fact_sets = (
            set(self.positive_fact_ids),
            set(self.counter_fact_ids),
            set(self.resolution_fact_ids),
            set(self.context_fact_ids),
        )
        if any(
            fact_sets[left] & fact_sets[right]
            for left in range(len(fact_sets))
            for right in range(left + 1, len(fact_sets))
        ):
            raise ValueError("memo fact direction lists must be disjoint")
        if not set(self.nearest_positive_anchor_ids).issubset(
            self.historical_anchor_ids
        ) or not set(self.nearest_counter_anchor_ids).issubset(
            self.historical_anchor_ids
        ):
            raise ValueError("nearest anchors must be included in historical_anchor_ids")
        if self.proposed_score_mid > 0 and not (
            self.positive_fact_ids or self.structured_metrics
        ):
            raise ValueError("positive points require fact or structured-metric lineage")

    def to_dict(self) -> Mapping[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class RedTeamMemo:
    memo_id: str
    target_id: str
    archetype_id: str
    reviewed_component_ids: tuple[str, ...]
    challenged_fact_ids: tuple[str, ...]
    counter_fact_ids: tuple[str, ...]
    resolved_challenges: tuple[str, ...]
    unresolved_challenges: tuple[str, ...]
    recommended_research_directions: tuple[str, ...]
    source_coverage: tuple[str, ...]
    confidence: float
    review_complete: bool
    schema_version: str = "e2r_red_team_memo_v1"

    def __post_init__(self) -> None:
        for value, label in (
            (self.memo_id, "memo_id"),
            (self.target_id, "target_id"),
            (self.archetype_id, "archetype_id"),
        ):
            _require_text(value, label)
        _require_probability(self.confidence, "confidence")
        for values, label in (
            (self.reviewed_component_ids, "reviewed_component_ids"),
            (self.challenged_fact_ids, "challenged_fact_ids"),
            (self.counter_fact_ids, "counter_fact_ids"),
            (self.resolved_challenges, "resolved_challenges"),
            (self.unresolved_challenges, "unresolved_challenges"),
            (
                self.recommended_research_directions,
                "recommended_research_directions",
            ),
            (self.source_coverage, "source_coverage"),
        ):
            _require_unique_texts(values, label, allow_empty=True)
        if any(value not in CANONICAL_COMPONENT_ORDER for value in self.reviewed_component_ids):
            raise ValueError("red-team memo contains an unknown component")

    def to_dict(self) -> Mapping[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class SynthesisMemo:
    memo_id: str
    target_id: str
    archetype_id: str
    component_memo_ids: tuple[str, ...]
    red_team_memo_id: str
    red_team_memo_hash: str
    cross_component_support: tuple[str, ...]
    cross_component_tensions: tuple[str, ...]
    unresolved_material_questions: tuple[str, ...]
    synthesis_summary: str
    confidence: float
    synthesis_complete: bool
    schema_version: str = "e2r_synthesis_memo_v2"

    def __post_init__(self) -> None:
        for value, label in (
            (self.memo_id, "memo_id"),
            (self.target_id, "target_id"),
            (self.archetype_id, "archetype_id"),
            (self.red_team_memo_id, "red_team_memo_id"),
            (self.red_team_memo_hash, "red_team_memo_hash"),
            (self.synthesis_summary, "synthesis_summary"),
        ):
            _require_text(value, label)
        if len(self.red_team_memo_hash) != 64:
            raise ValueError("red_team_memo_hash must be sha256")
        try:
            int(self.red_team_memo_hash, 16)
        except ValueError as exc:
            raise ValueError(
                "red_team_memo_hash must be hexadecimal"
            ) from exc
        _require_probability(self.confidence, "confidence")
        for values, label, allow_empty in (
            (self.component_memo_ids, "component_memo_ids", False),
            (self.cross_component_support, "cross_component_support", True),
            (self.cross_component_tensions, "cross_component_tensions", True),
            (
                self.unresolved_material_questions,
                "unresolved_material_questions",
                True,
            ),
        ):
            _require_unique_texts(values, label, allow_empty=allow_empty)

    def to_dict(self) -> Mapping[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class ComponentJudgeDecision:
    judge_id: str
    judge_call_id: str
    memo_id: str
    component_id: str
    component_max_points: float
    role: str
    pass_name: str
    prompt_hash: str
    response_hash: str
    provider_name: str
    anchor_comparisons: tuple[str, ...]
    proposed_points: float
    allowed_range: tuple[float, float]
    rationale: str
    disagreements: tuple[str, ...]
    support_fact_ids: tuple[str, ...]
    counter_fact_ids: tuple[str, ...]
    nearest_anchor_ids: tuple[str, ...]
    why_not_higher: str
    why_not_lower: str
    production_total_score_authority: bool = False
    production_stage_authority: bool = False
    schema_version: str = "e2r_component_judge_decision_v2"

    def __post_init__(self) -> None:
        for value, label in (
            (self.judge_id, "judge_id"),
            (self.judge_call_id, "judge_call_id"),
            (self.memo_id, "memo_id"),
            (self.pass_name, "pass_name"),
            (self.prompt_hash, "prompt_hash"),
            (self.response_hash, "response_hash"),
            (self.provider_name, "provider_name"),
            (self.rationale, "rationale"),
            (self.why_not_higher, "why_not_higher"),
            (self.why_not_lower, "why_not_lower"),
        ):
            _require_text(value, label)
        _require_component(self.component_id)
        ComponentJudgeRole(self.role)
        expected_pass = {
            ComponentJudgeRole.ANALYST.value: "COMPONENT_ANALYST_JUDGE",
            ComponentJudgeRole.SKEPTIC.value: "COMPONENT_SKEPTIC_JUDGE",
            ComponentJudgeRole.CALIBRATION_JUDGE.value: "CALIBRATION_JUDGE",
        }[self.role]
        if self.pass_name != expected_pass:
            raise ValueError("judge role and provider pass do not match")
        if len(self.prompt_hash) != 64 or len(self.response_hash) != 64:
            raise ValueError("judge prompt and response hashes must be sha256")
        try:
            int(self.prompt_hash, 16)
            int(self.response_hash, 16)
        except ValueError as exc:
            raise ValueError("judge prompt and response hashes must be hexadecimal") from exc
        if isinstance(self.component_max_points, bool):
            raise ValueError("component_max_points must be numeric")
        _require_positive(self.component_max_points, "component_max_points")
        if len(self.allowed_range) != 2:
            raise ValueError("allowed_range must have lower and upper points")
        if isinstance(self.proposed_points, bool) or any(
            isinstance(value, bool) for value in self.allowed_range
        ):
            raise ValueError("judge point fields must be numeric")
        lower, upper = (float(value) for value in self.allowed_range)
        proposed = float(self.proposed_points)
        maximum = float(self.component_max_points)
        if not all(math.isfinite(value) for value in (lower, proposed, upper, maximum)):
            raise ValueError("judge point fields must be finite")
        if (
            lower < 0
            or upper < lower
            or upper > maximum
            or not lower <= proposed <= upper
        ):
            raise ValueError("judge proposed points must be inside allowed_range")
        for values, label in (
            (self.anchor_comparisons, "anchor_comparisons"),
            (self.disagreements, "disagreements"),
            (self.support_fact_ids, "support_fact_ids"),
            (self.counter_fact_ids, "counter_fact_ids"),
            (self.nearest_anchor_ids, "nearest_anchor_ids"),
        ):
            _require_unique_texts(values, label, allow_empty=True)
        if bool(self.anchor_comparisons) != bool(self.nearest_anchor_ids):
            raise ValueError(
                "judge anchor comparisons and nearest anchor IDs must be present together"
            )
        if proposed > 0 and not self.support_fact_ids:
            raise ValueError("positive proposed points require support facts")
        if self.production_total_score_authority or self.production_stage_authority:
            raise ValueError("component judges cannot decide total score or Stage")

    def to_dict(self) -> Mapping[str, Any]:
        return _json_safe(asdict(self))


@dataclass(frozen=True)
class FinalComponentDecision:
    component_id: str
    support_points: float
    counter_effect: float
    final_points: float
    max_points: float
    fact_ids: tuple[str, ...]
    counter_fact_ids: tuple[str, ...]
    anchor_ids: tuple[str, ...]
    judge_ids: tuple[str, ...]
    research_complete: bool
    confidence: float
    decision_trace: str
    proposal_median: float
    consensus_band: tuple[float, float]
    confidence_interval: tuple[float, float]
    judge_proposals: Mapping[str, float]
    config_hash: str
    prompt_hashes: tuple[str, ...]
    response_hashes: tuple[str, ...]
    judge_call_ids: tuple[str, ...]
    corroboration_group_count: int
    source_confidence_affects_points: bool = False
    production_stage_authority: bool = False
    schema_version: str = "e2r_final_component_decision_v2"

    def __post_init__(self) -> None:
        _require_component(self.component_id)
        _require_positive(self.max_points, "max_points")
        _require_between(self.support_points, 0.0, self.max_points, "support_points")
        _require_between(self.counter_effect, 0.0, self.max_points, "counter_effect")
        _require_between(self.final_points, 0.0, self.max_points, "final_points")
        _require_between(self.proposal_median, 0.0, self.max_points, "proposal_median")
        _require_probability(self.confidence, "confidence")
        _require_text(self.decision_trace, "decision_trace")
        _require_text(self.config_hash, "config_hash")
        if len(self.config_hash) != 64:
            raise ValueError("component decision config_hash must be sha256")
        try:
            int(self.config_hash, 16)
        except ValueError as exc:
            raise ValueError("component decision config_hash must be hexadecimal") from exc
        if len(self.consensus_band) != 2 or len(self.confidence_interval) != 2:
            raise ValueError("component decision intervals require lower and upper")
        consensus_lower, consensus_upper = (
            float(value) for value in self.consensus_band
        )
        confidence_lower, confidence_upper = (
            float(value) for value in self.confidence_interval
        )
        if not all(
            math.isfinite(value)
            for value in (
                consensus_lower,
                consensus_upper,
                confidence_lower,
                confidence_upper,
            )
        ):
            raise ValueError("component decision intervals must be finite")
        if not 0.0 <= consensus_lower <= consensus_upper <= self.max_points:
            raise ValueError("component consensus band is invalid")
        if not 0.0 <= confidence_lower <= confidence_upper <= self.max_points:
            raise ValueError("component confidence interval is invalid")
        if not confidence_lower <= self.final_points <= confidence_upper:
            raise ValueError("final component points must lie inside confidence interval")
        expected_roles = {value.value for value in ComponentJudgeRole}
        if set(self.judge_proposals) != expected_roles:
            raise ValueError("component decision requires one proposal per judge role")
        for role, points in self.judge_proposals.items():
            if isinstance(points, bool):
                raise ValueError(f"judge proposal for {role} must be numeric")
            _require_between(points, 0.0, self.max_points, f"judge_proposals[{role}]")
        for values, label, allow_empty in (
            (self.fact_ids, "fact_ids", True),
            (self.counter_fact_ids, "counter_fact_ids", True),
            (self.anchor_ids, "anchor_ids", False),
            (self.judge_ids, "judge_ids", False),
            (self.prompt_hashes, "prompt_hashes", False),
            (self.response_hashes, "response_hashes", False),
            (self.judge_call_ids, "judge_call_ids", False),
        ):
            _require_unique_texts(values, label, allow_empty=allow_empty)
        if not self.research_complete:
            raise ValueError("final component decision requires complete research")
        if self.support_points > 0 and not self.fact_ids:
            raise ValueError("positive component support requires fact lineage")
        if any(
            len(values) != len(expected_roles)
            for values in (
                self.judge_ids,
                self.prompt_hashes,
                self.response_hashes,
                self.judge_call_ids,
            )
        ):
            raise ValueError("component decision requires three independent judge lineages")
        for values, label in (
            (self.prompt_hashes, "prompt_hashes"),
            (self.response_hashes, "response_hashes"),
        ):
            if any(len(value) != 64 for value in values):
                raise ValueError(f"{label} must contain sha256 values")
            try:
                for value in values:
                    int(value, 16)
            except ValueError as exc:
                raise ValueError(f"{label} must contain hexadecimal values") from exc
        if (
            isinstance(self.corroboration_group_count, bool)
            or not isinstance(self.corroboration_group_count, int)
            or self.corroboration_group_count < 0
        ):
            raise ValueError("corroboration_group_count must be a nonnegative integer")
        if self.final_points > self.support_points + 1e-9:
            raise ValueError("counter application cannot increase component points")
        if abs((self.support_points - self.counter_effect) - self.final_points) > 1e-6:
            raise ValueError("counter effect must reconcile support and final points")
        if self.source_confidence_affects_points:
            raise ValueError("source confidence cannot multiply economic points")
        if self.production_stage_authority:
            raise ValueError("component decision cannot decide Stage")

    def to_dict(self) -> Mapping[str, Any]:
        return _json_safe(asdict(self))


_FORBIDDEN_RESEARCH_KEYS = {
    "stage",
    "canonical_stage",
    "final_stage",
    "stage_override",
    "reported_stage",
    "expected_stage",
    "expected_score",
    "expected_points",
    "total_score",
    "total_points",
    "aggregate_score",
    "investment_recommendation",
    "future_outcome",
    "future_outcome_ref",
    "mfe",
    "mae",
    "mfe_30d",
    "mfe_60d",
    "mfe_90d",
    "mae_30d",
    "mae_60d",
    "mae_90d",
    "forward_return",
    "realized_return",
    "subsequent_return",
}


def scrub_blind_research_payload(value: Any) -> Any:
    """Remove outcome/answer fields before a current researcher sees history.

    This is a defense-in-depth boundary.  Historical atlas objects already
    expose blind-safe views, but source metadata can contain legacy fields.
    """

    if isinstance(value, Mapping):
        return {
            str(key): scrub_blind_research_payload(item)
            for key, item in value.items()
            if not _is_forbidden_research_key(str(key))
        }
    if isinstance(value, (list, tuple)):
        return [scrub_blind_research_payload(item) for item in value]
    return value


def assert_blind_research_output(value: Any) -> None:
    """Reject a provider response that attempts to decide Stage or use outcomes."""

    if isinstance(value, Mapping):
        for key, item in value.items():
            if _is_forbidden_research_key(str(key)):
                raise ValueError(f"researcher output contains forbidden field: {key}")
            assert_blind_research_output(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            assert_blind_research_output(item)


def _is_forbidden_research_key(key: str) -> bool:
    normalized = re.sub(r"[^a-z0-9]+", "_", key.lower()).strip("_")
    if normalized in _FORBIDDEN_RESEARCH_KEYS:
        return True
    return any(
        normalized.startswith(prefix)
        for prefix in (
            "mfe_",
            "mae_",
            "future_outcome_",
            "expected_score_",
            "total_score_",
            "total_points_",
        )
    )


def _require_component(component_id: str) -> None:
    if component_id not in CANONICAL_COMPONENT_ORDER:
        raise ValueError(f"unknown canonical component: {component_id}")


def _require_iso_date(value: str, label: str) -> None:
    _require_text(value, label)
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{label} must be ISO date") from exc


def _require_text(value: Any, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} is required")


def _require_positive(value: float, label: str) -> None:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} must be numeric") from exc
    if number <= 0:
        raise ValueError(f"{label} must be positive")


def _require_probability(value: float, label: str) -> None:
    _require_between(value, 0.0, 1.0, label)


def _require_between(value: float, lower: float, upper: float, label: str) -> None:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} must be numeric") from exc
    if not lower <= number <= upper:
        raise ValueError(f"{label} must be between {lower} and {upper}")


def _require_score_band(lower: float, mid: float, upper: float, maximum: float) -> None:
    numbers = tuple(float(value) for value in (lower, mid, upper, maximum))
    if not 0.0 <= numbers[0] <= numbers[1] <= numbers[2] <= numbers[3]:
        raise ValueError("component score band is invalid")


def _require_unique_texts(
    values: Sequence[str], label: str, *, allow_empty: bool
) -> None:
    if isinstance(values, str):
        raise ValueError(f"{label} must be a sequence")
    normalized = tuple(str(value).strip() for value in values)
    if not allow_empty and not normalized:
        raise ValueError(f"{label} cannot be empty")
    if any(not value for value in normalized):
        raise ValueError(f"{label} contains an empty value")
    if len(normalized) != len(set(normalized)):
        raise ValueError(f"{label} must be unique")


def _json_safe(value: Any) -> Any:
    return json.loads(json.dumps(value, ensure_ascii=False, default=str))


__all__ = [
    "AnchorConfidence",
    "BusinessModelMemo",
    "CANONICAL_COMPONENT_MAX_POINTS",
    "CANONICAL_COMPONENT_ORDER",
    "ComponentAnchor",
    "ComponentJudgeDecision",
    "ComponentJudgeRole",
    "ComponentResearchMemo",
    "ComponentResearchPlan",
    "EvidenceDirection",
    "EvidenceFact",
    "EvidenceLifecycle",
    "FinalComponentDecision",
    "HistoricalResearchJudgment",
    "HistoricalScoreSchemaType",
    "RedTeamMemo",
    "SynthesisMemo",
    "assert_blind_research_output",
    "scrub_blind_research_payload",
]
