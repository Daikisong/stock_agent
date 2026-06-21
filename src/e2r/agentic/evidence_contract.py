"""Archetype evidence contracts used before score finalisation."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.calibration.taxonomy import (
    CANONICAL_ARCHETYPE_IDS,
    large_sector_for_archetype,
    normalise_canonical_archetype_id,
    normalise_large_sector_id,
)


DEFAULT_EVIDENCE_CONTRACT_PATH = (
    Path(__file__).resolve().parents[3] / "configs" / "e2r_archetype_evidence_contracts_v12.json"
)


@dataclass(frozen=True)
class EvidenceContract:
    """Runtime contract for the primitives an archetype needs."""

    canonical_archetype_id: str
    large_sector_id: str
    runtime_bridge_group: str
    required_primitives: tuple[str, ...]
    required_bridge_axes: tuple[str, ...]
    positive_primitives: tuple[str, ...] = ()
    guard_primitives: tuple[str, ...] = ()
    green_gate_primitives: tuple[str, ...] = ()
    source_matrix: str | None = None

    def gap_context(self, present_primitives: Sequence[str] = ()) -> str:
        present = {str(item).strip() for item in present_primitives if str(item).strip()}
        missing_required = tuple(item for item in self.required_primitives if item not in present)
        missing_positive = tuple(item for item in self.positive_primitives if item not in present)
        missing_green_gate = tuple(item for item in self.green_gate_primitives if item not in present)
        present_guard = tuple(item for item in self.guard_primitives if item in present)
        missing_guard = tuple(item for item in self.guard_primitives if item not in present_guard)
        missing_required_text = ", ".join(missing_required) if missing_required else "none"
        missing_text = ", ".join(missing_positive) if missing_positive else "none"
        missing_green_text = ", ".join(missing_green_gate) if missing_green_gate else "none"
        positive_text = ", ".join(self.positive_primitives) if self.positive_primitives else "none"
        guard_text = ", ".join(self.guard_primitives) if self.guard_primitives else "none"
        present_guard_text = ", ".join(present_guard) if present_guard else "none"
        missing_guard_text = ", ".join(missing_guard) if missing_guard else "none"
        primitive_text = ", ".join(self.required_primitives)
        axis_text = ", ".join(self.required_bridge_axes)
        return (
            f"archetype_evidence_contract:{self.canonical_archetype_id}; "
            f"bridge_group={self.runtime_bridge_group}; "
            f"required_primitives={primitive_text}; "
            f"missing_required_primitives={missing_required_text}; "
            f"positive_primitives={positive_text}; "
            f"missing_positive_primitives={missing_text}; "
            f"missing_green_gate_primitives={missing_green_text}; "
            f"guard_primitives_to_check={guard_text}; "
            f"present_guard_primitives={present_guard_text}; "
            f"missing_guard_primitives={missing_guard_text}; "
            f"required_bridge_axes={axis_text}; "
            "find source-backed issuer-scoped claims for missing positive primitives where applicable and verify guard primitives before score/stage finalisation"
        )


def evidence_contract_for_archetype(
    canonical_archetype_id: Any,
    *,
    path: str | Path | None = None,
) -> EvidenceContract | None:
    """Return the configured contract for a canonical archetype."""

    canonical = normalise_canonical_archetype_id(canonical_archetype_id)
    if canonical is None:
        return None
    return load_evidence_contracts(path=path).get(canonical)


def evidence_contract_gap_context(
    canonical_archetype_id: Any,
    *,
    present_primitives: Sequence[str] = (),
    path: str | Path | None = None,
) -> tuple[str, ...]:
    """Return LLM-ready gap context for the archetype contract."""

    contract = evidence_contract_for_archetype(canonical_archetype_id, path=path)
    if contract is None:
        return ()
    return (contract.gap_context(present_primitives),)


@lru_cache(maxsize=8)
def _load_contracts_cached(path_text: str) -> Mapping[str, EvidenceContract]:
    return _load_contracts_from_path(Path(path_text))


def load_evidence_contracts(*, path: str | Path | None = None) -> Mapping[str, EvidenceContract]:
    contract_path = Path(path) if path is not None else DEFAULT_EVIDENCE_CONTRACT_PATH
    return _load_contracts_cached(str(contract_path))


def _load_contracts_from_path(path: Path) -> Mapping[str, EvidenceContract]:
    payload = json.loads(path.read_text())
    if payload.get("schema_version") != "e2r_archetype_evidence_contracts_v1":
        raise ValueError("unsupported evidence contract schema_version")
    rows = payload.get("contracts")
    if not isinstance(rows, list):
        raise ValueError("evidence contract config must contain contracts list")
    declared_count = payload.get("contract_count")
    if not isinstance(declared_count, int):
        raise ValueError("evidence contract config must contain integer contract_count")
    if declared_count != len(rows):
        raise ValueError(f"evidence contract_count mismatch: {declared_count} != {len(rows)}")

    contracts: dict[str, EvidenceContract] = {}
    for raw in rows:
        if not isinstance(raw, Mapping):
            raise ValueError("each evidence contract must be an object")
        contract = _contract_from_mapping(raw)
        if contract.canonical_archetype_id in contracts:
            raise ValueError(f"duplicate evidence contract: {contract.canonical_archetype_id}")
        contracts[contract.canonical_archetype_id] = contract

    missing = set(CANONICAL_ARCHETYPE_IDS) - set(contracts)
    if missing:
        raise ValueError(f"missing evidence contracts: {sorted(missing)}")
    return contracts


def _contract_from_mapping(raw: Mapping[str, Any]) -> EvidenceContract:
    canonical = normalise_canonical_archetype_id(raw.get("canonical_archetype_id"))
    if canonical not in CANONICAL_ARCHETYPE_IDS:
        raise ValueError(f"unknown evidence contract archetype: {raw.get('canonical_archetype_id')}")

    large = normalise_large_sector_id(raw.get("large_sector_id"))
    expected_large = large_sector_for_archetype(canonical)
    if large != expected_large:
        raise ValueError(f"evidence contract large sector mismatch for {canonical}: {large} != {expected_large}")

    runtime_bridge_group = str(raw.get("runtime_bridge_group") or "").strip()
    if not runtime_bridge_group:
        raise ValueError(f"missing runtime_bridge_group for {canonical}")

    primitives = _clean_tuple(raw.get("required_primitives"))
    axes = _clean_tuple(raw.get("required_bridge_axes"))
    positives = _clean_tuple(raw.get("positive_primitives")) if "positive_primitives" in raw else primitives
    guards = _clean_tuple(raw.get("guard_primitives")) if "guard_primitives" in raw else ()
    green_gate = _clean_tuple(raw.get("green_gate_primitives"))
    if not primitives:
        raise ValueError(f"missing required_primitives for {canonical}")
    if not axes:
        raise ValueError(f"missing required_bridge_axes for {canonical}")
    unknown_roles = (set(positives) | set(guards)) - set(primitives)
    if unknown_roles:
        raise ValueError(f"primitive roles not in required_primitives for {canonical}: {sorted(unknown_roles)}")
    if set(positives) & set(guards):
        raise ValueError(f"positive and guard primitives overlap for {canonical}")
    if set(positives) | set(guards) != set(primitives):
        raise ValueError(f"positive and guard primitives must cover required_primitives for {canonical}")
    unknown_green_gate = set(green_gate) - set(positives)
    if unknown_green_gate:
        raise ValueError(f"green_gate_primitives must be positive primitives for {canonical}: {sorted(unknown_green_gate)}")

    source_matrix = raw.get("source_matrix")
    return EvidenceContract(
        canonical_archetype_id=canonical,
        large_sector_id=large or "",
        runtime_bridge_group=runtime_bridge_group,
        required_primitives=primitives,
        required_bridge_axes=axes,
        positive_primitives=positives,
        guard_primitives=guards,
        green_gate_primitives=green_gate,
        source_matrix=str(source_matrix).strip() if source_matrix else None,
    )


def _clean_tuple(value: Any) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)):
        return ()
    return tuple(dict.fromkeys(str(item).strip() for item in value if str(item).strip()))


__all__ = [
    "DEFAULT_EVIDENCE_CONTRACT_PATH",
    "EvidenceContract",
    "evidence_contract_for_archetype",
    "evidence_contract_gap_context",
    "load_evidence_contracts",
]
