"""Strict loader for all 36 ArchetypeResearchContractV2 records."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from .validator import validate_contract_catalog


CROSS_GUARD_IDS = (
    "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
    "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
    "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
    "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
)


@dataclass(frozen=True)
class ContractBundle:
    primary_contracts: tuple[Mapping[str, Any], ...]
    cross_guard_contracts: tuple[Mapping[str, Any], ...]

    @property
    def contracts(self) -> tuple[Mapping[str, Any], ...]:
        return (*self.primary_contracts, *self.cross_guard_contracts)

    @property
    def contract_ids(self) -> tuple[str, ...]:
        return tuple(str(row["archetype_id"]) for row in self.contracts)


def default_contract_path() -> Path:
    return (
        Path(__file__).resolve().parents[4]
        / "configs/e2r_archetype_research_contracts_v2.json"
    )


@lru_cache(maxsize=4)
def _load_cached(path_text: str) -> tuple[Mapping[str, Any], ...]:
    path = Path(path_text)
    payload = json.loads(path.read_text(encoding="utf-8"))
    validate_contract_catalog(payload)
    return tuple(dict(row) for row in payload["contracts"])


def load_all_research_contracts(
    path: str | Path | None = None,
) -> tuple[Mapping[str, Any], ...]:
    resolved = (Path(path) if path else default_contract_path()).resolve()
    return _load_cached(str(resolved))


def load_research_contract(
    archetype_id: str,
    *,
    path: str | Path | None = None,
) -> Mapping[str, Any]:
    matches = [
        row
        for row in load_all_research_contracts(path)
        if row["archetype_id"] == archetype_id
    ]
    if len(matches) != 1:
        raise KeyError(f"unknown research contract: {archetype_id}")
    return matches[0]


def select_contract_bundle(
    primary_archetype_ids: Sequence[str],
    *,
    path: str | Path | None = None,
) -> ContractBundle:
    primary_ids = tuple(dict.fromkeys(str(value) for value in primary_archetype_ids))
    if not 1 <= len(primary_ids) <= 3:
        raise ValueError("a Pro V2 job requires one to three primary contracts")
    if set(primary_ids).intersection(CROSS_GUARD_IDS):
        raise ValueError("cross guards are attached automatically, not selected as primary")
    rows = {str(row["archetype_id"]): row for row in load_all_research_contracts(path)}
    unknown = set(primary_ids) - set(rows)
    if unknown:
        raise KeyError(f"unknown primary research contracts: {sorted(unknown)}")
    primary = tuple(rows[value] for value in primary_ids)
    if any(row["contract_role"] != "PRIMARY" for row in primary):
        raise ValueError("primary selection contains a non-primary contract")
    guards = tuple(rows[value] for value in CROSS_GUARD_IDS)
    return ContractBundle(primary_contracts=primary, cross_guard_contracts=guards)


__all__ = [
    "CROSS_GUARD_IDS",
    "ContractBundle",
    "default_contract_path",
    "load_all_research_contracts",
    "load_research_contract",
    "select_contract_bundle",
]
