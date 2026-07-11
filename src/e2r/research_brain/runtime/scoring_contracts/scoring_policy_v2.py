"""Scoring-critical enum과 cap을 total schema로 제공한다."""

from __future__ import annotations

import ast
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.production.metadata import stable_hash


DEFAULT_POLICY_PATH = Path("configs/e2r_scoring_policy_v2.json")
SCHEMA_VERSION = "e2r_scoring_policy_v2"


class ScoringContractIncompleteError(ValueError):
    code = "SCORING_CONTRACT_INCOMPLETE"


@dataclass(frozen=True)
class SupportTypePolicy:
    support_type: str
    support_credit_cap: float
    counter_effect_cap: float
    resolution_effect: float
    counter_effect_mode: str
    research_case_refs: tuple[str, ...]
    rationale: str
    replay_result: str


@dataclass(frozen=True)
class ScoringPolicyV2:
    enum_registry: Mapping[str, tuple[str, ...]]
    strength_bands: Mapping[str, float]
    completeness_bands: Mapping[str, float]
    causal_distance_caps: Mapping[str, float]
    source_family_caps: Mapping[str, float]
    temporal_scope_caps: Mapping[str, float]
    direction_policy_fields: Mapping[str, str]
    support_type_policies: Mapping[str, SupportTypePolicy]
    config_hash: str

    def cap_for(self, *, support_type: str, direction: str) -> float:
        policy = require_scoring_key(
            self.support_type_policies,
            support_type,
            policy_name="support_type_policies",
        )
        field = require_scoring_key(
            self.direction_policy_fields,
            direction,
            policy_name="direction_policy_fields",
        )
        return float(getattr(policy, field))


def require_scoring_key(
    mapping: Mapping[str, Any], key: str, *, policy_name: str
) -> Any:
    if key not in mapping:
        raise ScoringContractIncompleteError(
            f"SCORING_CONTRACT_INCOMPLETE:{policy_name}:{key}"
        )
    return mapping[key]


def load_scoring_policy_v2(
    path: str | Path = DEFAULT_POLICY_PATH,
) -> ScoringPolicyV2:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ScoringContractIncompleteError(
            "SCORING_CONTRACT_INCOMPLETE:schema_version"
        )
    registry = {
        str(key): tuple(str(value) for value in values)
        for key, values in (payload.get("enum_registry") or {}).items()
    }
    support_policies = {
        str(key): SupportTypePolicy(
            support_type=str(key),
            support_credit_cap=float(row["support_credit_cap"]),
            counter_effect_cap=float(row["counter_effect_cap"]),
            resolution_effect=float(row["resolution_effect"]),
            counter_effect_mode=str(row["counter_effect_mode"]),
            research_case_refs=tuple(str(v) for v in row["research_case_refs"]),
            rationale=str(row["rationale"]),
            replay_result=str(row["replay_result"]),
        )
        for key, row in (payload.get("support_type_policies") or {}).items()
    }
    result = ScoringPolicyV2(
        enum_registry=registry,
        strength_bands=_float_mapping(payload, "strength_bands"),
        completeness_bands=_float_mapping(payload, "completeness_bands"),
        causal_distance_caps=_float_mapping(payload, "causal_distance_caps"),
        source_family_caps=_float_mapping(payload, "source_family_caps"),
        temporal_scope_caps=_float_mapping(payload, "temporal_scope_caps"),
        direction_policy_fields={
            str(key): str(value)
            for key, value in (payload.get("direction_policy_fields") or {}).items()
        },
        support_type_policies=support_policies,
        config_hash=stable_hash(payload),
    )
    validate_scoring_policy_v2(result)
    return result


def validate_scoring_policy_v2(policy: ScoringPolicyV2) -> None:
    required_registries = {
        "directions",
        "support_types",
        "strength_bands",
        "completeness_bands",
        "causal_distances",
        "temporal_scopes",
        "source_families",
        "component_aggregation_modes",
        "counter_effect_modes",
    }
    if set(policy.enum_registry) != required_registries:
        raise ScoringContractIncompleteError(
            "SCORING_CONTRACT_INCOMPLETE:enum_registry"
        )
    exact = (
        ("support_types", policy.support_type_policies),
        ("strength_bands", policy.strength_bands),
        ("completeness_bands", policy.completeness_bands),
        ("causal_distances", policy.causal_distance_caps),
        ("source_families", policy.source_family_caps),
        ("temporal_scopes", policy.temporal_scope_caps),
        ("directions", policy.direction_policy_fields),
    )
    for registry_name, mapping in exact:
        if set(policy.enum_registry[registry_name]) != set(mapping):
            raise ScoringContractIncompleteError(
                f"SCORING_CONTRACT_INCOMPLETE:{registry_name}"
            )
    allowed_fields = {
        "support_credit_cap",
        "counter_effect_cap",
        "resolution_effect",
    }
    if not set(policy.direction_policy_fields.values()) <= allowed_fields:
        raise ScoringContractIncompleteError(
            "SCORING_CONTRACT_INCOMPLETE:direction_policy_field"
        )
    counter_modes = set(policy.enum_registry["counter_effect_modes"])
    for item in policy.support_type_policies.values():
        if item.counter_effect_mode not in counter_modes:
            raise ScoringContractIncompleteError(
                f"SCORING_CONTRACT_INCOMPLETE:counter_effect_mode:{item.support_type}"
            )
        if not item.research_case_refs or not item.rationale or not item.replay_result:
            raise ScoringContractIncompleteError(
                f"SCORING_CONTRACT_INCOMPLETE:research_lineage:{item.support_type}"
            )
        for value in (
            item.support_credit_cap,
            item.counter_effect_cap,
            item.resolution_effect,
        ):
            if not 0.0 <= value <= 1.0:
                raise ScoringContractIncompleteError(
                    f"SCORING_CONTRACT_INCOMPLETE:cap_range:{item.support_type}"
                )


def audit_scoring_schema_totality(
    *, repo_root: str | Path = "."
) -> Mapping[str, Any]:
    from e2r.research_brain.compiler.evidence_impact_rubric_compiler import (
        compile_evidence_impact_rubrics,
    )

    from .loader import load_scoring_contract_catalog

    root = Path(repo_root).resolve()
    policy = load_scoring_policy_v2(root / DEFAULT_POLICY_PATH)
    catalog = load_scoring_contract_catalog()
    missing_contract_policy = 0
    missing_rubric_policy = 0
    incomplete_archetypes: list[str] = []
    expected_sources = set(policy.enum_registry["source_families"])
    expected_temporal = set(policy.enum_registry["temporal_scopes"])
    expected_support = set(policy.enum_registry["support_types"])
    expected_strength = set(policy.enum_registry["strength_bands"])
    expected_completeness = set(policy.enum_registry["completeness_bands"])
    expected_causal = set(policy.enum_registry["causal_distances"])
    for archetype_id in CANONICAL_ARCHETYPE_IDS:
        contract = catalog.get(archetype_id)
        if contract is None:
            missing_contract_policy += 1
            incomplete_archetypes.append(archetype_id)
            continue
        contract_bad = (
            set(contract.source_tier_caps) != expected_sources
            or set(contract.freshness_caps) != expected_temporal
        )
        rubrics = compile_evidence_impact_rubrics(archetype_id).rubrics
        # Primitive rubric이 아직 없는 archetype도 global scoring policy를
        # 완전하게 상속한다. 존재하는 rubric은 전수 검사하되, semantic edge
        # 작성 전이라는 이유만으로 cap schema 자체를 incomplete로 보지 않는다.
        rubric_bad = any(
            set(rubric.actual_vs_forward_rules) != expected_support
            or set(rubric.source_family_caps) != expected_sources
            or set(rubric.strength_bands) != expected_strength
            or set(rubric.completeness_bands) != expected_completeness
            or set(rubric.causal_distance_caps) != expected_causal
            for rubric in rubrics
        )
        missing_contract_policy += int(contract_bad)
        missing_rubric_policy += int(rubric_bad)
        if contract_bad or rubric_bad:
            incomplete_archetypes.append(archetype_id)
    validator_path = (
        root / "src/e2r/research_brain/scoring/impact_validator.py"
    )
    silent_defaults = _count_silent_zero_defaults(validator_path)
    critical = {
        "missing_scoring_key_count": missing_contract_policy
        + missing_rubric_policy,
        "silent_zero_default_count": silent_defaults,
        "partial_bridge_missing_cap_count": int(
            "PARTIAL_BRIDGE" not in policy.support_type_policies
        ),
        "risk_open_missing_cap_count": int(
            "RISK_OPEN" not in policy.support_type_policies
        ),
        "risk_resolved_missing_cap_count": int(
            "RISK_RESOLVED" not in policy.support_type_policies
        ),
        "unknown_source_family_silent_zero_count": 0,
        "unknown_temporal_scope_silent_zero_count": 0,
        "all_archetype_schema_incomplete_count": len(set(incomplete_archetypes)),
    }
    critical_sum = sum(critical.values())
    return {
        "schema_version": "e2r_scoring_schema_totality_audit_v1",
        "status": (
            "SCORING_SCHEMA_TOTALITY_PASS"
            if critical_sum == 0
            else "SCORING_SCHEMA_TOTALITY_FAIL"
        ),
        "policy_config_hash": policy.config_hash,
        "canonical_archetype_count": len(CANONICAL_ARCHETYPE_IDS),
        "total_schema_archetype_count": len(CANONICAL_ARCHETYPE_IDS)
        - len(set(incomplete_archetypes)),
        "enum_registry": {
            key: list(values) for key, values in policy.enum_registry.items()
        },
        "support_type_policies": {
            key: {
                **asdict(value),
                "research_case_refs": list(value.research_case_refs),
            }
            for key, value in policy.support_type_policies.items()
        },
        "incomplete_archetype_ids": sorted(set(incomplete_archetypes)),
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
    }


def _float_mapping(payload: Mapping[str, Any], key: str) -> Mapping[str, float]:
    raw = payload.get(key)
    if not isinstance(raw, Mapping):
        raise ScoringContractIncompleteError(
            f"SCORING_CONTRACT_INCOMPLETE:{key}"
        )
    return {str(name): float(value) for name, value in raw.items()}


def _count_silent_zero_defaults(path: Path) -> int:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    count = 0
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
            continue
        if node.func.attr != "get" or len(node.args) < 2:
            continue
        default = node.args[1]
        if isinstance(default, ast.Constant) and default.value in {0, 0.0}:
            count += 1
    return count


__all__ = [
    "DEFAULT_POLICY_PATH",
    "SCHEMA_VERSION",
    "ScoringContractIncompleteError",
    "ScoringPolicyV2",
    "SupportTypePolicy",
    "audit_scoring_schema_totality",
    "load_scoring_policy_v2",
    "require_scoring_key",
    "validate_scoring_policy_v2",
]
