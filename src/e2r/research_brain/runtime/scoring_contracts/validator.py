from __future__ import annotations

from typing import Any, Mapping, Sequence

from .archetype_component_catalog import CANONICAL_COMPONENT_IDS
from .schemas import ArchetypeScoringContract, ScoringContractCatalog


def validate_scoring_contract(
    contract: ArchetypeScoringContract,
    *,
    required_primitives: Sequence[str] = (),
    require_edges: bool = False,
) -> None:
    expected = set(CANONICAL_COMPONENT_IDS)
    if set(contract.component_weights) != expected:
        raise ValueError("scoring contract component set mismatch")
    if abs(sum(contract.component_weights.values()) - 100.0) > 1e-6:
        raise ValueError("scoring contract component weights must sum to 100")
    if contract.component_max_points != contract.component_weights:
        raise ValueError("archetype component max points must equal calibrated weights")
    if set(contract.component_caps) != expected:
        raise ValueError("scoring contract component caps are incomplete")
    for component_id, cap in contract.component_caps.items():
        if cap < 0 or cap > contract.component_max_points[component_id]:
            raise ValueError("component cap exceeds calibrated max points")
    for primitive_id, component_ids in contract.primitive_to_component_allowed_edges.items():
        if not primitive_id or not component_ids or not set(component_ids) <= expected:
            raise ValueError("primitive-to-component edge is invalid")
    if require_edges:
        missing = set(required_primitives) - set(contract.primitive_to_component_allowed_edges)
        if missing:
            raise ValueError(f"required primitive scoring edges missing: {sorted(missing)}")
    if contract.edge_catalog_status not in {"EXPLICIT", "EXPLICIT_PENDING"}:
        raise ValueError("unknown profile fallback must be explicit")


def audit_scoring_contract_catalog(catalog: ScoringContractCatalog) -> Mapping[str, Any]:
    critical = {
        "component_weight_sum_mismatch_count": 0,
        "missing_component_contract_count": 0,
        "source_task_defined_score_weight_count": 0,
        "unknown_profile_silent_fallback_count": 0,
    }
    for contract in catalog.contracts.values():
        try:
            validate_scoring_contract(contract)
        except ValueError:
            critical["missing_component_contract_count"] += 1
        critical["component_weight_sum_mismatch_count"] += int(
            abs(sum(contract.component_weights.values()) - 100.0) > 1e-6
        )
        critical["unknown_profile_silent_fallback_count"] += int(
            contract.edge_catalog_status not in {"EXPLICIT", "EXPLICIT_PENDING"}
        )
    return {
        "schema_version": "e2r_canonical_scoring_contract_audit_v1",
        "status": "CANONICAL_SCORING_CONTRACT_PASS" if sum(critical.values()) == 0 else "CANONICAL_SCORING_CONTRACT_FAIL",
        "profile_id": catalog.profile_id,
        "profile_version": catalog.profile_version,
        "contract_count": len(catalog.contracts),
        "config_hash": catalog.config_hash,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }


__all__ = ["audit_scoring_contract_catalog", "validate_scoring_contract"]
