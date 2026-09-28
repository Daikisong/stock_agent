"""Canonical verified-fact and accepted-lineage snapshots for saturation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from ..ids import canonical_hash


@dataclass(frozen=True)
class VerifiedResearchSnapshot:
    verified_fact_ids: tuple[str, ...]
    fact_snapshot_hash: str
    accepted_lineage_roster_hash: str
    active_lineage_roster: tuple[Mapping[str, Any], ...]


def compile_verified_research_snapshot(
    dossier: Mapping[str, Any],
    verified_fact_ids: Sequence[str],
) -> VerifiedResearchSnapshot:
    fact_rows = tuple(
        row
        for collection in ("material_facts", "counterfacts", "resolution_facts")
        for row in dossier.get(collection) or ()
    )
    facts_by_id = {
        str(row.get("dossier_fact_id") or ""): row for row in fact_rows
    }
    if len(facts_by_id) != len(fact_rows):
        raise ValueError("duplicate dossier fact ids are forbidden in saturation snapshot")
    verified = tuple(sorted(set(str(value) for value in verified_fact_ids)))
    if not set(verified).issubset(facts_by_id):
        raise ValueError("verified fact roster contains an unknown dossier fact id")
    fact_snapshot_hash = canonical_hash([facts_by_id[value] for value in verified])
    verified_set = frozenset(verified)
    source_documents = {
        str(row.get("source_document_id") or ""): row
        for row in dossier.get("source_documents") or ()
    }
    active_lineages = tuple(
        sorted(
            (
                {
                    "source_lineage_id": (
                        row.get("source_lineage_id") or row.get("lineage_id")
                    ),
                    "source_urls": sorted(
                        {
                            str(url)
                            for url in row.get("source_urls") or ()
                            if str(url)
                        }
                        | {
                            str(document.get("canonical_url") or "")
                            for source_document_id in row.get(
                                "source_document_ids"
                            )
                            or ()
                            for document in (
                                source_documents.get(
                                    str(source_document_id)
                                )
                                or {},
                            )
                            if str(document.get("canonical_url") or "")
                        }
                    ),
                    "fact_ids": sorted(
                        set(str(value) for value in row.get("fact_ids") or ()).intersection(
                            verified_set
                        )
                    ),
                    "independence_group_id": row.get("independence_group_id"),
                }
                for row in dossier.get("source_lineages") or ()
                if row.get("status") == "ACTIVE"
                and set(str(value) for value in row.get("fact_ids") or ()).intersection(
                    verified_set
                )
            ),
            key=lambda row: str(row["source_lineage_id"]),
        )
    )
    return VerifiedResearchSnapshot(
        verified_fact_ids=verified,
        fact_snapshot_hash=fact_snapshot_hash,
        accepted_lineage_roster_hash=canonical_hash(active_lineages),
        active_lineage_roster=active_lineages,
    )


__all__ = ["VerifiedResearchSnapshot", "compile_verified_research_snapshot"]
