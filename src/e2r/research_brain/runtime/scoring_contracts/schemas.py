from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class ArchetypeScoringContract:
    archetype_id: str
    profile_id: str
    profile_version: str
    component_weights: Mapping[str, float]
    component_max_points: Mapping[str, float]
    primitive_to_component_allowed_edges: Mapping[str, tuple[str, ...]]
    primitive_materiality: Mapping[str, bool]
    primitive_green_requirements: Mapping[str, bool]
    component_required_evidence_roles: Mapping[str, tuple[str, ...]]
    component_caps: Mapping[str, float]
    source_tier_caps: Mapping[str, float]
    freshness_caps: Mapping[str, float]
    correlation_groups: Mapping[str, tuple[str, ...]]
    counter_effect_rules: Mapping[str, str]
    stage_config: Mapping[str, Any]
    edge_catalog_status: str
    config_hash: str

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ScoringContractCatalog:
    profile_id: str
    profile_version: str
    contracts: Mapping[str, ArchetypeScoringContract]
    config_hash: str

    def get(self, archetype_id: str) -> ArchetypeScoringContract | None:
        return self.contracts.get(archetype_id)


__all__ = ["ArchetypeScoringContract", "ScoringContractCatalog"]
