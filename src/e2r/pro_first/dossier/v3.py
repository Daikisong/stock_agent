"""ResearchDossierV3 source-document and atomic-fact graph invariants."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Any, Mapping, Sequence
from urllib.parse import parse_qsl, urlsplit


DOSSIER_V3_SCHEMA_VERSION = "e2r_pro_research_dossier_v3"


class FactKindV3(str, Enum):
    MATERIAL = "MATERIAL"
    COUNTER = "COUNTER"
    RESOLUTION = "RESOLUTION"


class FactLifecycleV3(str, Enum):
    CURRENT = "CURRENT"
    OPEN = "OPEN"
    RESOLVED = "RESOLVED"
    SUPERSEDED = "SUPERSEDED"
    HISTORICAL_ONLY = "HISTORICAL_ONLY"


@dataclass(frozen=True)
class DossierV3EvidenceSummary:
    source_document_ids: tuple[str, ...]
    canonical_source_urls: tuple[str, ...]
    fact_ids: tuple[str, ...]
    material_fact_ids: tuple[str, ...]
    counter_fact_ids: tuple[str, ...]
    resolution_fact_ids: tuple[str, ...]
    derived_metric_ids: tuple[str, ...]
    lineage_ids: tuple[str, ...]


def v3_atomic_fact_identity(fact: Mapping[str, Any]) -> tuple[str, str, str, str]:
    """Return the validator's canonical identity for one atomic fact."""

    return (
        str(fact.get("source_document_id") or ""),
        str(fact.get("predicate_id") or ""),
        _normalized_text(fact.get("subject")),
        _normalized_text(fact.get("supporting_excerpt")),
    )


def validate_dossier_v3_evidence_graph(
    payload: Mapping[str, Any],
    *,
    target_id: str,
    as_of_date: str,
    allowed_question_ids: Sequence[str],
) -> DossierV3EvidenceSummary:
    """Validate V3 graph identity without inferring or rewriting evidence."""

    if payload.get("schema_version") != DOSSIER_V3_SCHEMA_VERSION:
        raise ValueError("V3 evidence graph requires ResearchDossierV3")
    cutoff = date.fromisoformat(as_of_date)
    allowed_questions = set(str(value) for value in allowed_question_ids)
    has_facts = any(payload.get(collection) for collection in (
        "material_facts",
        "counterfacts",
        "resolution_facts",
    ))

    source_documents = tuple(payload.get("source_documents") or ())
    source_ids = tuple(
        str(row.get("source_document_id") or "") for row in source_documents
    )
    _require_unique_nonempty(
        source_ids, "source document", allow_empty=not has_facts
    )
    source_by_id = dict(zip(source_ids, source_documents))
    canonical_urls = tuple(
        str(row.get("canonical_url") or "") for row in source_documents
    )
    _require_unique_nonempty(
        canonical_urls, "canonical source URL", allow_empty=not source_documents
    )
    for document in source_documents:
        document_id = str(document["source_document_id"])
        canonical_url = str(document["canonical_url"])
        opened_url = str(document["opened_url"])
        _validate_public_url(canonical_url)
        _validate_public_url(opened_url)
        if _has_tracking_query(canonical_url) or urlsplit(canonical_url).fragment:
            raise ValueError(
                f"canonical source URL retains tracking or fragment: {document_id}"
            )
        _validate_cutoff_date(
            document.get("publication_date"), cutoff, "source publication date"
        )
        _validate_cutoff_date(
            document.get("availability_date"), cutoff, "source availability date"
        )
        if date.fromisoformat(str(document["availability_date"])) < date.fromisoformat(
            str(document["publication_date"])
        ):
            raise ValueError(
                f"source availability precedes publication date: {document_id}"
            )
        if document.get("opened_and_read") is not True:
            raise ValueError(f"source document was not opened and read: {document_id}")
        if document.get("as_of_cutoff_pass") is not True:
            raise ValueError(f"source document failed as-of cutoff: {document_id}")
        scope = document.get("target_scope") or {}
        if str(scope.get("target_id") or "") != target_id:
            raise ValueError(f"source document target mismatch: {document_id}")

    collections = {
        "material_facts": FactKindV3.MATERIAL.value,
        "counterfacts": FactKindV3.COUNTER.value,
        "resolution_facts": FactKindV3.RESOLUTION.value,
    }
    facts: list[Mapping[str, Any]] = []
    fact_ids_by_kind: dict[str, tuple[str, ...]] = {}
    atomic_identities: set[tuple[str, str, str, str]] = set()
    for collection, expected_kind in collections.items():
        rows = tuple(payload.get(collection) or ())
        ids = tuple(str(row.get("dossier_fact_id") or "") for row in rows)
        fact_ids_by_kind[expected_kind] = ids
        for fact in rows:
            fact_id = str(fact.get("dossier_fact_id") or "")
            if str(fact.get("fact_kind") or "") != expected_kind:
                raise ValueError(
                    f"fact_kind does not match {collection}: {fact_id}"
                )
            if str(fact.get("target_id") or "") != target_id:
                raise ValueError(f"atomic fact target mismatch: {fact_id}")
            source_id = str(fact.get("source_document_id") or "")
            if source_id not in source_by_id:
                raise ValueError(
                    f"atomic fact references unknown source document: {fact_id}"
                )
            document_scope = source_by_id[source_id].get("target_scope") or {}
            if fact.get("issuer_scoped") is not document_scope.get("issuer_scoped"):
                raise ValueError(
                    f"atomic fact issuer scope differs from source document: {fact_id}"
                )
            question_ids = {
                str(value) for value in fact.get("question_family_ids") or ()
            }
            if not question_ids or not question_ids.issubset(allowed_questions):
                raise ValueError(
                    f"atomic fact has missing or out-of-contract question binding: {fact_id}"
                )
            _validate_cutoff_date(fact.get("event_date"), cutoff, "fact event date")
            lifecycle = str(fact.get("current_status") or "")
            if lifecycle not in {item.value for item in FactLifecycleV3}:
                raise ValueError(f"atomic fact lifecycle is not terminal: {fact_id}")
            direction = str(fact.get("direction") or "")
            if expected_kind == FactKindV3.RESOLUTION.value and direction != "RESOLUTION":
                raise ValueError(f"resolution fact lacks resolution direction: {fact_id}")
            if expected_kind == FactKindV3.COUNTER.value and direction not in {
                "NEGATIVE",
                "NEUTRAL",
            }:
                raise ValueError(f"counterfact has incompatible direction: {fact_id}")
            preflight = fact.get("verifier_preflight") or {}
            _validate_preflight(preflight, fact_id=fact_id)
            identity = v3_atomic_fact_identity(fact)
            if identity in atomic_identities:
                raise ValueError(
                    f"duplicate atomic predicate/source/excerpt identity: {fact_id}"
                )
            atomic_identities.add(identity)
            facts.append(fact)

    fact_ids = tuple(str(row.get("dossier_fact_id") or "") for row in facts)
    _require_unique_nonempty(fact_ids, "atomic fact", allow_empty=True)
    fact_id_set = set(fact_ids)

    metric_rows = tuple(payload.get("derived_metrics") or ())
    metric_ids = tuple(
        str(row.get("derived_metric_id") or "") for row in metric_rows
    )
    _require_unique_nonempty(metric_ids, "derived metric", allow_empty=True)
    for metric in metric_rows:
        metric_id = str(metric["derived_metric_id"])
        inputs = {str(value) for value in metric.get("input_fact_ids") or ()}
        if not inputs or not inputs.issubset(fact_id_set):
            raise ValueError(
                f"derived metric references missing atomic input fact: {metric_id}"
            )
        if metric.get("score_authority") is not False:
            raise ValueError(f"derived metric claims score authority: {metric_id}")

    lineage_rows = tuple(payload.get("source_lineages") or ())
    lineage_ids = tuple(str(row.get("lineage_id") or "") for row in lineage_rows)
    _require_unique_nonempty(
        lineage_ids, "source lineage", allow_empty=not source_documents
    )
    lineage_by_id = dict(zip(lineage_ids, lineage_rows))
    if not {
        str(row.get("lineage_id") or "") for row in source_documents
    }.issubset(set(lineage_ids)):
        raise ValueError("source document references an unknown V3 lineage")
    for lineage_id, lineage in lineage_by_id.items():
        linked_documents = {
            str(value) for value in lineage.get("source_document_ids") or ()
        }
        linked_facts = {str(value) for value in lineage.get("fact_ids") or ()}
        if not linked_documents or not linked_documents.issubset(set(source_ids)):
            raise ValueError(
                f"source lineage references missing document: {lineage_id}"
            )
        if not linked_facts.issubset(fact_id_set):
            raise ValueError(f"source lineage references missing fact: {lineage_id}")
        expected_documents = {
            source_id
            for source_id, document in source_by_id.items()
            if str(document.get("lineage_id") or "") == lineage_id
        }
        expected_facts = {
            str(fact.get("dossier_fact_id") or "")
            for fact in facts
            if str(
                source_by_id[str(fact.get("source_document_id"))].get(
                    "lineage_id"
                )
                or ""
            )
            == lineage_id
        }
        if linked_documents != expected_documents or linked_facts != expected_facts:
            raise ValueError(
                f"source lineage roster differs from document/fact graph: {lineage_id}"
            )

    return DossierV3EvidenceSummary(
        source_document_ids=source_ids,
        canonical_source_urls=canonical_urls,
        fact_ids=fact_ids,
        material_fact_ids=fact_ids_by_kind[FactKindV3.MATERIAL.value],
        counter_fact_ids=fact_ids_by_kind[FactKindV3.COUNTER.value],
        resolution_fact_ids=fact_ids_by_kind[FactKindV3.RESOLUTION.value],
        derived_metric_ids=metric_ids,
        lineage_ids=lineage_ids,
    )


def _validate_preflight(preflight: Mapping[str, Any], *, fact_id: str) -> None:
    required_true = (
        "source_opened",
        "canonical_url_used",
        "exact_excerpt_copied_from_source",
        "statement_not_broader_than_excerpt",
        "single_atomic_predicate",
        "target_subject_scope_confirmed",
        "publication_date_confirmed",
        "as_of_cutoff_pass",
        "lineage_duplicate_checked",
    )
    if any(preflight.get(key) is not True for key in required_true):
        raise ValueError(f"atomic fact has failed verifier preflight: {fact_id}")
    if preflight.get("derived_calculation_mixed_into_fact") is not False:
        raise ValueError(f"atomic fact mixes a derived calculation: {fact_id}")


def _validate_public_url(value: str) -> None:
    parsed = urlsplit(str(value or ""))
    if (
        parsed.scheme.lower() not in {"http", "https"}
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
    ):
        raise ValueError(f"invalid public source URL: {value!r}")


def _has_tracking_query(value: str) -> bool:
    tracking = {"fbclid", "gclid", "mc_cid", "mc_eid", "ref", "source"}
    return any(
        key.casefold().startswith("utm_") or key.casefold() in tracking
        for key, _ in parse_qsl(urlsplit(value).query, keep_blank_values=True)
    )


def _validate_cutoff_date(value: Any, cutoff: date, label: str) -> None:
    if value is None or value == "":
        return
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00")).date()
    except ValueError:
        try:
            parsed = date.fromisoformat(str(value))
        except ValueError as error:
            raise ValueError(f"invalid {label}: {value!r}") from error
    if parsed > cutoff:
        raise ValueError(f"{label} exceeds as_of_date")


def _require_unique_nonempty(
    values: Sequence[str],
    label: str,
    *,
    allow_empty: bool = False,
) -> None:
    if not allow_empty and not values:
        raise ValueError(f"V3 requires at least one {label}")
    if any(not value for value in values) or len(values) != len(set(values)):
        raise ValueError(f"duplicate or empty {label} identity")


def _normalized_text(value: Any) -> str:
    return " ".join(str(value or "").split()).casefold()


__all__ = [
    "DOSSIER_V3_SCHEMA_VERSION",
    "DossierV3EvidenceSummary",
    "FactKindV3",
    "FactLifecycleV3",
    "v3_atomic_fact_identity",
    "validate_dossier_v3_evidence_graph",
]
