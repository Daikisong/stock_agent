"""Canonical schemas for E2R v5 Researcher Mode."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Mapping


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


__all__ = [
    "AnchorConfidence",
    "HistoricalResearchJudgment",
    "HistoricalScoreSchemaType",
]
