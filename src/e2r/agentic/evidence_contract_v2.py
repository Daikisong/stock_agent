"""Config loader for Evidence Contract v2."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS, normalise_canonical_archetype_id

from .evidence_os import (
    Directness,
    EvidenceContractV2,
    FreshnessPolicy,
    GateExpression,
    SourceQuorumRule,
    SourceType,
    TargetScopeStatus,
)


EVIDENCE_CONTRACT_V2_SCHEMA_VERSION = "e2r_agentic_evidence_contracts_v2"
DEFAULT_EVIDENCE_CONTRACT_V2_PATH = (
    Path(__file__).resolve().parents[3] / "configs" / "e2r_agentic_evidence_contracts_v2.json"
)


def load_evidence_contracts_v2(
    *,
    path: str | Path | None = None,
    require_all_archetypes: bool = False,
) -> Mapping[str, EvidenceContractV2]:
    contract_path = Path(path) if path is not None else DEFAULT_EVIDENCE_CONTRACT_V2_PATH
    payload = json.loads(contract_path.read_text())
    return load_evidence_contracts_v2_from_mapping(
        payload,
        require_all_archetypes=require_all_archetypes,
    )


def load_evidence_contracts_v2_from_mapping(
    payload: Mapping[str, Any],
    *,
    require_all_archetypes: bool = False,
) -> Mapping[str, EvidenceContractV2]:
    if payload.get("schema_version") != EVIDENCE_CONTRACT_V2_SCHEMA_VERSION:
        raise ValueError("unsupported Evidence Contract v2 schema_version")
    rows = payload.get("contracts")
    if not isinstance(rows, list):
        raise ValueError("Evidence Contract v2 config must contain contracts list")
    declared_count = payload.get("contract_count")
    if not isinstance(declared_count, int):
        raise ValueError("Evidence Contract v2 config must contain integer contract_count")
    if declared_count != len(rows):
        raise ValueError(f"Evidence Contract v2 count mismatch: {declared_count} != {len(rows)}")

    contracts: dict[str, EvidenceContractV2] = {}
    for raw in rows:
        if not isinstance(raw, Mapping):
            raise ValueError("each Evidence Contract v2 row must be an object")
        contract = evidence_contract_v2_from_mapping(raw)
        if contract.archetype_id in contracts:
            raise ValueError(f"duplicate Evidence Contract v2 row: {contract.archetype_id}")
        contracts[contract.archetype_id] = contract
    if require_all_archetypes:
        missing = set(CANONICAL_ARCHETYPE_IDS) - set(contracts)
        if missing:
            raise ValueError(f"missing Evidence Contract v2 rows: {sorted(missing)}")
    return contracts


def evidence_contract_v2_from_mapping(raw: Mapping[str, Any]) -> EvidenceContractV2:
    archetype_id = normalise_canonical_archetype_id(raw.get("archetype_id") or raw.get("canonical_archetype_id"))
    if not archetype_id:
        raise ValueError(f"unknown Evidence Contract v2 archetype: {raw.get('archetype_id')}")
    required_primitives = _clean_tuple(raw.get("required_primitives"))
    if not required_primitives:
        raise ValueError(f"missing required_primitives for {archetype_id}")
    gate_payload = raw.get("green_gate")
    if not isinstance(gate_payload, Mapping):
        raise ValueError(f"missing green_gate for {archetype_id}")
    alternative_primitives = _string_tuple_mapping(raw.get("alternative_primitives"))
    score_rubric = _string_tuple_mapping(raw.get("score_rubric"))
    freshness = dict(_freshness_mapping(raw.get("freshness")))
    _apply_default_bridge_freshness(
        freshness,
        required_primitives=required_primitives,
        green_gate=_gate_from_mapping(gate_payload),
        alternative_primitives=alternative_primitives,
        score_rubric=score_rubric,
    )
    return EvidenceContractV2(
        archetype_id=archetype_id,
        required_primitives=required_primitives,
        green_gate=_gate_from_mapping(gate_payload),
        allowed_target_scopes=_target_scope_tuple(raw.get("allowed_target_scopes")),
        allowed_directness=_directness_tuple(raw.get("allowed_directness")),
        alternative_primitives=alternative_primitives,
        primitive_aliases=_string_tuple_mapping(raw.get("primitive_aliases")),
        route_hints=_string_tuple_mapping(raw.get("route_hints")),
        score_rubric=score_rubric,
        source_quorum=_source_quorum_mapping(raw.get("source_quorum")),
        freshness=freshness,
        guard_modes=_string_mapping(raw.get("guard_modes")),
        aggregation_rules=_clean_tuple(raw.get("aggregation_rules")),
    )


def _apply_default_bridge_freshness(
    freshness: dict[str, FreshnessPolicy],
    *,
    required_primitives: tuple[str, ...],
    green_gate: GateExpression,
    alternative_primitives: Mapping[str, tuple[str, ...]],
    score_rubric: Mapping[str, tuple[str, ...]],
) -> None:
    primitive_ids = set(required_primitives)
    primitive_ids.update(green_gate.primitive_ids())
    primitive_ids.update(alternative_primitives)
    primitive_ids.update(primitive for values in alternative_primitives.values() for primitive in values)
    primitive_ids.update(primitive for values in score_rubric.values() for primitive in values)
    if "cash_or_revision_conversion" not in primitive_ids:
        return
    freshness.setdefault(
        "cash_or_revision_conversion",
        FreshnessPolicy(
            primitive_id="cash_or_revision_conversion",
            max_age_days=730,
            supersession_rule="latest_authoritative_cash_or_revision_update",
            closure_conditions=(
                "superseded_by_newer_cash_flow_or_revision_claim",
                "resolved_by_authoritative_followup",
            ),
            authoritative_followup_sources=(
                SourceType.FILING,
                SourceType.XBRL,
                SourceType.IR,
                SourceType.RESEARCH_REPORT,
                SourceType.NEWS,
            ),
        ),
    )


def _gate_from_mapping(raw: Mapping[str, Any]) -> GateExpression:
    if "primitive" in raw:
        return GateExpression.primitive(str(raw["primitive"]).strip())
    if "any" in raw:
        return GateExpression.any(_gate_children(raw["any"]))
    if "all" in raw:
        return GateExpression.all(_gate_children(raw["all"]))
    if "k_of_n" in raw:
        payload = raw["k_of_n"]
        if not isinstance(payload, Mapping):
            raise ValueError("k_of_n gate must be an object")
        return GateExpression.k_of_n(
            k=int(payload.get("k")),
            children=_gate_children(payload.get("children")),
        )
    raise ValueError("green_gate must contain primitive, any, all, or k_of_n")


def _gate_children(value: Any) -> tuple[GateExpression, ...]:
    if not isinstance(value, list):
        raise ValueError("gate children must be a list")
    children: list[GateExpression] = []
    for item in value:
        if not isinstance(item, Mapping):
            raise ValueError("gate child must be an object")
        children.append(_gate_from_mapping(item))
    return tuple(children)


def _source_quorum_mapping(value: Any) -> Mapping[str, SourceQuorumRule]:
    if value is None:
        return {}
    if not isinstance(value, Mapping):
        raise ValueError("source_quorum must be an object")
    result: dict[str, SourceQuorumRule] = {}
    for key, raw in value.items():
        if not isinstance(raw, Mapping):
            raise ValueError("source_quorum rule must be an object")
        result[str(key)] = SourceQuorumRule(
            min_official=int(raw.get("min_official") or 0),
            min_independent_tier2=int(raw.get("min_independent_tier2") or 0),
        )
    return result


def _freshness_mapping(value: Any) -> Mapping[str, FreshnessPolicy]:
    if value is None:
        return {}
    if not isinstance(value, Mapping):
        raise ValueError("freshness must be an object")
    result: dict[str, FreshnessPolicy] = {}
    for primitive_id, raw in value.items():
        if not isinstance(raw, Mapping):
            raise ValueError("freshness policy must be an object")
        result[str(primitive_id)] = FreshnessPolicy(
            primitive_id=str(primitive_id),
            max_age_days=_optional_int(raw.get("max_age_days")),
            supersession_rule=_optional_text(raw.get("supersession_rule")),
            closure_conditions=_clean_tuple(raw.get("closure_conditions")),
            authoritative_followup_sources=tuple(
                SourceType(str(item)) for item in _clean_tuple(raw.get("authoritative_followup_sources"))
            ),
        )
    return result


def _string_tuple_mapping(value: Any) -> Mapping[str, tuple[str, ...]]:
    if value is None:
        return {}
    if not isinstance(value, Mapping):
        raise ValueError("expected object mapping to string lists")
    return {str(key).strip(): _clean_tuple(raw) for key, raw in value.items() if str(key).strip()}


def _target_scope_tuple(value: Any) -> tuple[TargetScopeStatus, ...]:
    values = _clean_tuple(value)
    if not values:
        return (TargetScopeStatus.DIRECT,)
    return tuple(TargetScopeStatus(item) for item in values)


def _directness_tuple(value: Any) -> tuple[Directness, ...]:
    values = _clean_tuple(value)
    if not values:
        return (Directness.DIRECT,)
    return tuple(Directness(item) for item in values)


def _string_mapping(value: Any) -> Mapping[str, str]:
    if value is None:
        return {}
    if not isinstance(value, Mapping):
        raise ValueError("expected string object mapping")
    return {
        str(key).strip(): str(raw).strip()
        for key, raw in value.items()
        if str(key).strip() and str(raw).strip()
    }


def _clean_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    values = value if isinstance(value, (list, tuple)) and not isinstance(value, (str, bytes)) else (value,)
    return tuple(dict.fromkeys(str(item).strip() for item in values if str(item).strip()))


def _optional_text(value: Any) -> str | None:
    clean = str(value or "").strip()
    return clean or None


def _optional_int(value: Any) -> int | None:
    if value in (None, ""):
        return None
    return int(value)


__all__ = [
    "EVIDENCE_CONTRACT_V2_SCHEMA_VERSION",
    "evidence_contract_v2_from_mapping",
    "load_evidence_contracts_v2",
    "load_evidence_contracts_v2_from_mapping",
]
