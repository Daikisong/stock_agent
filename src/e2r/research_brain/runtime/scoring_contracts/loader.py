from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from .schemas import ArchetypeScoringContract, ScoringContractCatalog
from .scoring_policy_v2 import load_scoring_policy_v2
from .validator import validate_scoring_contract


DEFAULT_WEIGHT_PROFILE = Path("configs/e2r_archetype_weight_profile_v2_2.json")
DEFAULT_EVIDENCE_CONTRACTS = Path("configs/e2r_archetype_evidence_contracts_v12.json")
DEFAULT_EDGE_CATALOG = Path("configs/e2r_archetype_scoring_contract_edges_v1.json")
DEFAULT_STAGE_CONFIG = Path("configs/e2r_scoring_profile_v2_2.yaml")


def _stable_hash(payload: Any) -> str:
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _read_json(path: Path) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"scoring contract input must be an object: {path}")
    return payload


def load_scoring_contract_catalog(
    *,
    weight_profile_path: str | Path = DEFAULT_WEIGHT_PROFILE,
    evidence_contract_path: str | Path = DEFAULT_EVIDENCE_CONTRACTS,
    edge_catalog_path: str | Path = DEFAULT_EDGE_CATALOG,
    stage_config_path: str | Path = DEFAULT_STAGE_CONFIG,
) -> ScoringContractCatalog:
    weight_path = Path(weight_profile_path)
    evidence_path = Path(evidence_contract_path)
    edge_path = Path(edge_catalog_path)
    stage_path = Path(stage_config_path)
    scoring_policy = load_scoring_policy_v2()
    weights = _read_json(weight_path)
    evidence = _read_json(evidence_path)
    edges = _read_json(edge_path)
    if weights.get("enabled") is not True:
        raise ValueError("canonical archetype weight profile is disabled")
    evidence_by_id = {
        str(row.get("canonical_archetype_id") or ""): row
        for row in evidence.get("contracts") or ()
    }
    edge_by_id = dict(edges.get("contracts") or {})
    stage_config = {
        "path": str(stage_path),
        "sha256": hashlib.sha256(stage_path.read_bytes()).hexdigest(),
    }
    contracts: dict[str, ArchetypeScoringContract] = {}
    for archetype_id, profile_row in sorted((weights.get("archetype_weights") or {}).items()):
        evidence_row = evidence_by_id.get(str(archetype_id))
        if evidence_row is None:
            raise ValueError(f"archetype evidence contract missing: {archetype_id}")
        edge_row = dict(edge_by_id.get(str(archetype_id)) or {})
        component_weights = {
            str(key): float(value)
            for key, value in (profile_row.get("weights") or {}).items()
        }
        payload = {
            "archetype_id": str(archetype_id),
            "profile_id": str(weights.get("profile_id") or weight_path.stem),
            "profile_version": "v2_2",
            "component_weights": component_weights,
            "component_max_points": dict(component_weights),
            "primitive_to_component_allowed_edges": {
                str(key): tuple(str(value) for value in values)
                for key, values in (edge_row.get("primitive_to_component_allowed_edges") or {}).items()
            },
            "primitive_materiality": {
                str(key): bool(value)
                for key, value in (edge_row.get("primitive_materiality") or {}).items()
            },
            "primitive_green_requirements": {
                str(key): bool(value)
                for key, value in (edge_row.get("primitive_green_requirements") or {}).items()
            },
            "component_required_evidence_roles": {
                str(key): tuple(str(value) for value in values)
                for key, values in (edge_row.get("component_required_evidence_roles") or {}).items()
            },
            "component_caps": {
                str(key): float(value)
                for key, value in (edge_row.get("component_caps") or component_weights).items()
            },
            "source_tier_caps": {
                str(key): float(value)
                for key, value in (
                    edge_row.get("source_tier_caps")
                    or scoring_policy.source_family_caps
                ).items()
            },
            "freshness_caps": {
                str(key): float(value)
                for key, value in (
                    edge_row.get("freshness_caps")
                    or scoring_policy.temporal_scope_caps
                ).items()
            },
            "correlation_groups": {
                str(key): tuple(str(value) for value in values)
                for key, values in (edge_row.get("correlation_groups") or {}).items()
            },
            "counter_effect_rules": {
                str(key): str(value)
                for key, value in (
                    edge_row.get("counter_effect_rules")
                    or {
                        component_id: "NET_SUPPORT_COUNTER"
                        for component_id in component_weights
                    }
                ).items()
            },
            "stage_config": stage_config,
            "edge_catalog_status": "EXPLICIT" if edge_row else "EXPLICIT_PENDING",
        }
        contract = ArchetypeScoringContract(**payload, config_hash=_stable_hash(payload))
        validate_scoring_contract(
            contract,
            required_primitives=tuple(evidence_row.get("required_primitives") or ()),
            require_edges=bool(edge_row),
        )
        contracts[str(archetype_id)] = contract
    catalog_payload = {
        "profile_id": weights.get("profile_id"),
        "profile_version": "v2_2",
        "contract_hashes": {key: value.config_hash for key, value in contracts.items()},
        "weight_profile_sha256": hashlib.sha256(weight_path.read_bytes()).hexdigest(),
        "evidence_contract_sha256": hashlib.sha256(evidence_path.read_bytes()).hexdigest(),
        "edge_catalog_sha256": hashlib.sha256(edge_path.read_bytes()).hexdigest(),
    }
    return ScoringContractCatalog(
        profile_id=str(weights.get("profile_id") or weight_path.stem),
        profile_version="v2_2",
        contracts=contracts,
        config_hash=_stable_hash(catalog_payload),
    )


def load_archetype_scoring_contract(archetype_id: str, **kwargs: Any) -> ArchetypeScoringContract:
    catalog = load_scoring_contract_catalog(**kwargs)
    contract = catalog.get(archetype_id)
    if contract is None:
        raise ValueError(f"unknown canonical archetype scoring contract: {archetype_id}")
    return contract


__all__ = ["load_archetype_scoring_contract", "load_scoring_contract_catalog"]
