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
        version = str(normalized.get("schema_version") or "")
        is_v2_or_v3 = version in {
            "e2r_pro_research_dossier_v2",
            "e2r_pro_research_dossier_v3",
        }
        if is_v2_or_v3:
            normalized["selected_archetypes"] = sorted(
                normalized.get("selected_archetypes") or ()
            )
            normalized["resolution_facts"] = sorted(
                normalized.get("resolution_facts") or (),
                key=lambda row: str(row.get("dossier_fact_id") or ""),
            )
            normalized["question_family_results"] = sorted(
                normalized.get("question_family_results") or (),
                key=lambda row: str(row.get("question_family_id") or ""),
            )
            normalized["source_lineages"] = sorted(
                normalized.get("source_lineages") or (),
                key=lambda row: str(row.get("source_lineage_id") or ""),
            )
            normalized["search_route_receipts"] = sorted(
                normalized.get("search_route_receipts") or (),
                key=lambda row: str(row.get("route_receipt_id") or ""),
            )
            normalized["research_passes"] = sorted(
                normalized.get("research_passes") or (),
                key=lambda row: str(row.get("pass_id") or ""),
            )
            if version == "e2r_pro_research_dossier_v2":
                normalized["verification_repair_register"] = sorted(
                    normalized.get("verification_repair_register") or (),
                    key=lambda row: str(row.get("candidate_id") or ""),
                )
            else:
                normalized["source_documents"] = sorted(
                    normalized.get("source_documents") or (),
                    key=lambda row: str(row.get("source_document_id") or ""),
                )
                normalized["derived_metrics"] = sorted(
                    normalized.get("derived_metrics") or (),
                    key=lambda row: str(row.get("derived_metric_id") or ""),
                )
        if "sources" in normalized:
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
        operations = [
            "SORT_CANDIDATE_ARCHETYPES",
            "SORT_FACTS_BY_DOSSIER_FACT_ID",
            "SORT_SOURCES_BY_URL_AND_ID",
        ]
        if is_v2_or_v3:
            operations.extend(
                (
                    "SORT_SELECTED_ARCHETYPES",
                    "SORT_QUESTION_CLOSURE_RESULTS",
                    "SORT_SOURCE_LINEAGES_AND_ROUTE_RECEIPTS",
                )
            )
        if version == "e2r_pro_research_dossier_v2":
            operations.append("SORT_RESEARCH_PASS_AND_REPAIR_LEDGERS")
        if version == "e2r_pro_research_dossier_v3":
            operations.extend(
                (
                    "SORT_RESEARCH_PASS_LEDGER",
                    "SORT_SOURCE_DOCUMENT_REGISTRY",
                    "SORT_DERIVED_METRIC_REGISTRY",
                )
            )
        return NormalizedDossier(
            payload=normalized,
            before_hash=before_hash,
            after_hash=canonical_hash(normalized),
            operations=tuple(operations),
        )


def _fact_ids(payload: Mapping[str, Any]) -> tuple[str, ...]:
    return tuple(
        str(row.get("dossier_fact_id") or "")
        for key in ("material_facts", "counterfacts", "resolution_facts")
        for row in payload.get(key) or ()
    )


def _source_urls(payload: Mapping[str, Any]) -> tuple[str, ...]:
    fact_urls = tuple(
        str(row.get("source_url") or "")
        for key in ("material_facts", "counterfacts", "resolution_facts")
        for row in payload.get(key) or ()
    )
    source_urls = tuple(
        str(row.get("source_url") or "") for row in payload.get("sources") or ()
    )
    document_urls = tuple(
        str(row.get(key) or "")
        for row in payload.get("source_documents") or ()
        for key in ("canonical_url", "opened_url")
    )
    lineage_urls = tuple(
        str(url)
        for row in payload.get("source_lineages") or ()
        for url in row.get("source_urls") or ()
    )
    route_urls = tuple(
        str(url)
        for row in payload.get("search_route_receipts") or ()
        for url in row.get("opened_source_urls") or ()
    )
    return fact_urls + source_urls + document_urls + lineage_urls + route_urls


__all__ = ["NormalizedDossier", "ResearchDossierNormalizer"]
