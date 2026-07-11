from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class EvidenceImpactRubric:
    rubric_id: str
    archetype_id: str
    primitive_id: str
    allowed_component_ids: tuple[str, ...]
    economic_mechanism: str
    positive_predicates: tuple[str, ...]
    partial_predicates: tuple[str, ...]
    counter_predicates: tuple[str, ...]
    unsupported_predicates: tuple[str, ...]
    strength_bands: Mapping[str, float]
    completeness_bands: Mapping[str, float]
    causal_distance_caps: Mapping[str, float]
    source_family_caps: Mapping[str, float]
    actual_vs_forward_rules: Mapping[str, float]
    evidence_family_diversity_rules: Mapping[str, Any]
    double_count_correlation_rules: Mapping[str, Any]
    positive_historical_case_refs: tuple[str, ...]
    counterexample_refs: tuple[str, ...]
    source_backed_examples: tuple[Mapping[str, Any], ...]
    source_proxy_planning_only: bool

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class EvidenceImpactRubricCatalog:
    schema_version: str
    archetype_id: str
    rubrics: tuple[EvidenceImpactRubric, ...]
    policies: Mapping[str, bool]
    config_hash: str

    def by_primitive(self) -> Mapping[str, EvidenceImpactRubric]:
        return {item.primitive_id: item for item in self.rubrics}


__all__ = ["EvidenceImpactRubric", "EvidenceImpactRubricCatalog"]
