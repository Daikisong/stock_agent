"""Deterministic exact-alias projection onto existing closed scope enums."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import unicodedata
from typing import Mapping, Sequence

from e2r.research_brain.scoring.business_mechanism_scope import (
    load_mechanism_scope_contracts,
)


@dataclass(frozen=True)
class ClosedScopeMapping:
    business_segment: str
    product_family: str
    segment_changed: bool
    product_changed: bool
    mapping_complete: bool


class ClosedEnumScopeMapper:
    def __init__(self, *, contract_path: str | Path | None = None) -> None:
        self.contract_path = (
            Path(contract_path).resolve()
            if contract_path
            else Path(__file__).resolve().parents[4]
            / "configs/e2r_archetype_mechanism_scopes_v1.json"
        )

    def map_fact(
        self,
        *,
        fact: Mapping[str, object],
        source_document: Mapping[str, object],
        archetype_ids: Sequence[str],
    ) -> ClosedScopeMapping:
        allowed_segments, allowed_products = self._allowed_values(archetype_ids)
        scope = source_document.get("target_scope") or {}
        if not isinstance(scope, Mapping):
            scope = {}
        original_segment = str(fact.get("business_segment") or "").strip()
        original_product = str(fact.get("product_family") or "").strip()
        segment = _map_exact_alias(
            (original_segment, str(scope.get("business_segment") or "")),
            allowed_segments,
        )
        product = _map_exact_alias(
            (original_product, str(scope.get("product_family") or "")),
            allowed_products,
        )
        return ClosedScopeMapping(
            business_segment=segment or original_segment,
            product_family=product or original_product,
            segment_changed=bool(segment and segment != original_segment),
            product_changed=bool(product and product != original_product),
            mapping_complete=bool(segment and product),
        )

    def _allowed_values(
        self, archetype_ids: Sequence[str]
    ) -> tuple[tuple[str, ...], tuple[str, ...]]:
        contracts = load_mechanism_scope_contracts(self.contract_path)
        selected = [
            contract
            for contract_id, contract in contracts.items()
            if any(
                contract_id == archetype_id
                or contract_id.startswith(f"{archetype_id}_")
                for archetype_id in archetype_ids
            )
        ]
        segments = {
            "CORPORATE_GENERIC",
            *(
                value
                for contract in selected
                for value in (
                    *contract.allowed_business_segments,
                    *contract.forbidden_business_segments,
                )
            ),
        }
        products = {
            "CORPORATE_GENERIC",
            *(
                value
                for contract in selected
                for value in (
                    *contract.allowed_product_families,
                    *contract.forbidden_product_families,
                )
            ),
        }
        return tuple(sorted(segments)), tuple(sorted(products))


def _map_exact_alias(
    candidates: Sequence[str],
    allowed_values: Sequence[str],
) -> str | None:
    aliases: dict[str, list[str]] = {}
    for value in allowed_values:
        aliases.setdefault(_identity(value), []).append(value)
    for candidate in candidates:
        matches = aliases.get(_identity(candidate), ())
        if len(matches) == 1:
            return matches[0]
    return None


def _identity(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", str(value or "")).casefold()
    return re.sub(r"[^\w]+", "", normalized, flags=re.UNICODE)


__all__ = ["ClosedEnumScopeMapper", "ClosedScopeMapping"]
