"""Deterministic dossier ordering without creating or deleting research facts."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Mapping

from ..ids import canonical_hash


@dataclass(frozen=True)
class NormalizedDossier:
    payload: Mapping[str, Any]
    before_hash: str
    after_hash: str
    operations: tuple[str, ...]


class ResearchDossierNormalizer:
    def normalize(self, payload: Mapping[str, Any]) -> NormalizedDossier:
        before_hash = canonical_hash(payload)
        normalized = deepcopy(dict(payload))
        before_fact_ids = _fact_ids(normalized)
        before_urls = _source_urls(normalized)
        normalized["candidate_archetypes"] = sorted(
            normalized.get("candidate_archetypes") or ()
        )
        normalized["material_facts"] = sorted(
            normalized.get("material_facts") or (),
            key=lambda row: str(row.get("dossier_fact_id") or ""),
        )
        normalized["counterfacts"] = sorted(
            normalized.get("counterfacts") or (),
            key=lambda row: str(row.get("dossier_fact_id") or ""),
        )
        normalized["sources"] = sorted(
            normalized.get("sources") or (),
            key=lambda row: (
                str(row.get("source_url") or ""),
                str(row.get("source_id") or ""),
            ),
        )
        if sorted(before_fact_ids) != sorted(_fact_ids(normalized)):
            raise ValueError("normalization cannot create, delete, or rename facts")
        if sorted(before_urls) != sorted(_source_urls(normalized)):
            raise ValueError("normalization cannot create, delete, or rewrite source URLs")
        return NormalizedDossier(
            payload=normalized,
            before_hash=before_hash,
            after_hash=canonical_hash(normalized),
            operations=(
                "SORT_CANDIDATE_ARCHETYPES",
                "SORT_FACTS_BY_DOSSIER_FACT_ID",
                "SORT_SOURCES_BY_URL_AND_ID",
            ),
        )


def _fact_ids(payload: Mapping[str, Any]) -> tuple[str, ...]:
    return tuple(
        str(row.get("dossier_fact_id") or "")
        for key in ("material_facts", "counterfacts")
        for row in payload.get(key) or ()
    )


def _source_urls(payload: Mapping[str, Any]) -> tuple[str, ...]:
    fact_urls = tuple(
        str(row.get("source_url") or "")
        for key in ("material_facts", "counterfacts")
        for row in payload.get(key) or ()
    )
    source_urls = tuple(
        str(row.get("source_url") or "") for row in payload.get("sources") or ()
    )
    return fact_urls + source_urls


__all__ = ["NormalizedDossier", "ResearchDossierNormalizer"]
