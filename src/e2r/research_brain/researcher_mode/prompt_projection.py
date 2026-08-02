"""Loss-accounted prompt projections for already-validated research artifacts.

Fact extraction is the only phase that needs full document bodies.  Later LLM
passes consume verified economic facts plus loss-accounted claim/document
profiles and deterministic summaries of every structured record.  Exact quotes,
full lineage, and complete artifacts remain on disk; these projections are
prompt-transport representations, never research-completion caps or score
authorities.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from statistics import median
from typing import Any, Mapping, Sequence


_DOCUMENT_MANIFEST_FIELDS = (
    "document_id",
    "full_source_document_id",
    "target_id",
    "as_of_date",
    "canonical_url",
    "title",
    "source_family",
    "source_provider",
    "published_at",
    "available_at",
    "content_type",
    "content_hash",
    "full_source_content_hash",
    "full_source_text_chars",
    "chunk_index",
    "chunk_count",
    "all_chunks_preserved",
    "source_independence_group",
    "full_fetch_performed",
    "full_source_fetch_performed",
    "snippet_only",
    "snippet_used_as_document",
    "evidence_eligible",
)

_DOCUMENT_RELATION_FIELDS = (
    "discovery_urls",
    "query_ids",
    "objective_ids",
    "referenced_urls",
    "referenced_document_ids",
)

_DOCUMENT_TABLE_FIELDS = (
    *_DOCUMENT_MANIFEST_FIELDS,
    "source_manifest_hash",
    "content_transport",
    "content_chars",
    "content_hash_recomputed",
)

_GENERATED_QUERY_PROMPT_FIELDS = (
    "query_id",
    "objective_id",
    "literal_query",
    "rationale",
    "source_families",
    "official_gap_reasons",
    "execution_status",
    "search_result_count",
    "counter_or_supersession_search",
    "provider_errors",
)

_FACT_GROUP_FIELDS = (
    "business_segment",
    "product_family",
    "direction",
    "current_lifecycle",
)

_FACT_OBSERVATION_FIELDS = (
    "subject",
    "economic_mechanism",
    "predicate",
    "value",
    "unit",
    "period",
    "confidence",
    "structured_evidence_roles",
)

_SUPERVISOR_FACT_GROUP_FIELDS = (
    "business_segment",
    "product_family",
    "direction",
    "current_lifecycle",
)

_PEER_FACT_GROUP_FIELDS = (
    "business_segment",
    "product_family",
    "direction",
    "current_lifecycle",
)

_PEER_CLAIM_GROUP_FIELDS = (
    "business_segment",
    "product_family",
    "direction",
    "source_family",
)

_CITABLE_FACT_PROMPT_FIELDS = (
    "fact_id",
    "subject",
    "business_segment",
    "product_family",
    "economic_mechanism",
    "predicate",
    "value",
    "unit",
    "period",
    "direction",
    "current_lifecycle",
    "confidence",
    "structured_evidence_roles",
)

_CITABLE_FACT_DERIVED_FIELDS = (
    "source_independence_group_index",
    "corroborating_independence_group_count",
)

_SOURCE_CLAIM_PROMPT_FIELDS = (
    "claim_id",
    "document_id",
    "source_ids",
    "exact_quote",
    "source_family",
    "source_tier",
    "published_at",
    "available_at",
    "structured_evidence_roles",
)

_SOURCE_CLAIM_EXTRACTION_TRANSPORT_FIELDS = (
    "provider_name",
    "provider_prompt_hash",
    "provider_response_hash",
)

_FAILURE_GROUP_FIELDS = (
    "failure_kind",
    "failure_stage",
    "failure_reason",
    "reason",
    "rejection_reason",
    "provider_error",
    "source_family",
    "retryable",
    "alternate_route_required",
    "absence_eligible",
    "zero_result_only",
    "resolved",
    "resolved_by",
    "parser_extractor_verified",
    "provider_transport_verified",
    "attempted_source_families",
    "full_fetch_attempted",
    "snippet_used_as_document",
)

_FAILURE_RELATION_FIELDS = (
    "objective_id",
    "objective_ids",
    "query_id",
    "query_ids",
    "candidate_id",
    "rejection_id",
    "literal_query",
    "accepted_claim_ids",
)

_COLLABORATION_TRANSPORT_WAIT_PREFIXES = (
    "",
    "QUERY_PROVIDER_ERROR:",
    "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:StructuredProviderUnavailable:",
    "FACT_EXTRACTION_RETRY_CONTEXT:"
    "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
    "StructuredProviderUnavailable:",
    "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:StructuredProviderUnavailable:",
    "PEER_SELECTION_PROVIDER_OR_SCHEMA_ERROR:",
    "PEER_SELECTION_PENDING:PEER_SELECTION_PROVIDER_OR_SCHEMA_ERROR:",
    "PROVIDER_ERROR:",
)
_COLLABORATION_TRANSPORT_WAIT_RE = re.compile(
    r"^(?:"
    + "|".join(
        re.escape(prefix)
        for prefix in _COLLABORATION_TRANSPORT_WAIT_PREFIXES
    )
    + r")COLLABORATION_RESPONSE_PENDING:"
    r"COLLABREQ-[0-9a-f]{64}$"
)
_FACT_TRANSPORT_PROGRESS_FEEDBACK_RE = re.compile(
    r"^FACT_EXTRACTION_RETRY_CONTEXT:"
    r"INCOMPLETE_DOCUMENT_TRANSPORT_CHUNKS:"
    r"[^:\s]+:([0-9]+)/([1-9][0-9]*)$"
)
_FACT_CANONICAL_STATE_REFRESH_FEEDBACK = (
    "FACT_EXTRACTION_RETRY_CONTEXT:"
    "FACT_EXTRACTION_CANONICAL_STATE_REFRESH_REQUIRED"
)
_DROP_COLLABORATION_TRANSPORT_WAIT = object()
_COLLABORATION_TRANSPORT_WAIT_REQUEST_ID_RE = re.compile(
    r"COLLABREQ-[0-9a-f]{64}$"
)


def project_source_documents(
    rows: Sequence[Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    """Keep every document identity/date/hash while removing duplicate bodies."""

    output = []
    for raw in rows:
        row = dict(raw)
        content = str(
            row.get("content_text")
            or row.get("full_text")
            or row.get("content")
            or ""
        )
        projected = {
            key: row[key] for key in _DOCUMENT_MANIFEST_FIELDS if key in row
        }
        projected.update(
            {
                "source_manifest_hash": _stable_hash(row),
                "content_transport": "OMITTED_AFTER_VERIFIED_FACT_EXTRACTION",
                "content_chars": len(content),
                "content_hash_recomputed": (
                    hashlib.sha256(content.encode("utf-8")).hexdigest()
                    if content
                    else None
                ),
                "exact_quotes_available_in_source_claims": True,
                "prompt_projection_is_research_cap": False,
                "production_score_authority": False,
            }
        )
        output.append(projected)
    return tuple(output)


def project_source_document_table(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Encode every body-free document manifest under one shared field legend."""

    payloads = tuple(dict(row) for row in rows)
    ordered = tuple(
        sorted(
            payloads,
            key=lambda row: (
                str(row.get("document_id") or ""),
                _stable_hash(row),
            ),
        )
    )
    manifests = project_source_documents(ordered)
    documents = [
        [row.get(field) for field in _DOCUMENT_TABLE_FIELDS]
        for row in manifests
    ]
    document_id_index = _DOCUMENT_TABLE_FIELDS.index("document_id")
    return {
        "schema_version": "e2r_v5_source_document_prompt_table_v1",
        "document_count": len(ordered),
        "document_roster_hash": _stable_hash(ordered),
        "document_fields": list(_DOCUMENT_TABLE_FIELDS),
        "documents": documents,
        "every_document_id_preserved": (
            len(
                {
                    str(row[document_id_index] or "") for row in documents
                }
            )
            == len(ordered)
            and all(str(row[document_id_index] or "").strip() for row in documents)
        ),
        "relation_coverage": {
            field: _relation_coverage(ordered, field)
            for field in _DOCUMENT_RELATION_FIELDS
        },
        "full_document_bodies_omitted_after_fact_extraction": True,
        "full_document_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def project_source_graph_checkpoint(
    checkpoint: Mapping[str, Any], *, keys: Sequence[str]
) -> Mapping[str, Any]:
    output = {key: checkpoint.get(key) for key in keys if key in checkpoint}
    if "generated_queries" in output:
        output["generated_queries"] = project_generated_queries(
            tuple(output.get("generated_queries") or ())
        )
    collection_specs = {
        "query_failures": (
            ("failure_id", "query_id"),
            (
                "failure_stage",
                "failure_reason",
                "alternate_route_required",
                "absence_eligible",
                "zero_result_only",
            ),
            ("objective_id", "query_id"),
            (),
        ),
        "provider_failures": (
            ("failure_id",),
            (
                "failure_stage",
                "failure_reason",
                "retryable",
                "absence_eligible",
                "zero_result_only",
            ),
            ("objective_id", "query_id"),
            (),
        ),
        "search_candidates": (
            ("candidate_id",),
            (
                "ranking_status",
                "fetch_status",
                "source",
                "query_lineage_valid",
            ),
            (
                "objective_ids",
                "query_ids",
                "is_disclosure",
                "is_news",
                "is_pdf",
                "is_report_domain",
            ),
            ("material_priority", "rank"),
        ),
        "candidate_materiality_decisions": (
            ("decision_id", "candidate_id"),
            (
                "material_relevance",
                "evidence_eligible",
                "snippet_discovery_only",
                "score_authority",
            ),
            ("objective_ids",),
            ("priority",),
        ),
        "fetch_records": (
            ("fetch_id", "candidate_id"),
            (
                "disposition",
                "provider_error",
                "full_fetch_attempted",
                "snippet_used_as_document",
                "score_authority",
            ),
            ("objective_ids", "query_ids"),
            (),
        ),
        "rejected_documents": (
            ("rejection_id", "candidate_id"),
            (
                "rejection_reason",
                "retryable",
                "snippet_used_as_document",
                "score_authority",
            ),
            ("objective_ids", "query_ids", "accepted_claim_ids"),
            (),
        ),
    }
    for key, (
        identity_fields,
        group_fields,
        relation_fields,
        numeric_fields,
    ) in collection_specs.items():
        if key not in output:
            continue
        output[key] = _project_state_collection(
            tuple(output.get(key) or ()),
            collection_name=key,
            identity_fields=identity_fields,
            group_fields=group_fields,
            relation_fields=relation_fields,
            numeric_fields=numeric_fields,
        )
    if "evidence_documents" in output:
        documents = tuple(output.get("evidence_documents") or ())
        output["evidence_documents"] = list(project_source_documents(documents))
        output["evidence_document_count"] = len(documents)
        output["evidence_document_manifest_hash"] = _stable_hash(documents)
        output["evidence_document_relation_coverage"] = {
            field: _relation_coverage(documents, field)
            for field in _DOCUMENT_RELATION_FIELDS
        }
        output["full_document_bodies_omitted_after_fact_extraction"] = True
    output["source_graph_prompt_projection"] = {
        "schema_version": "e2r_v5_source_graph_prompt_projection_v2",
        "complete_artifact_persisted_outside_prompt": True,
        "every_projected_collection_hash_accounted": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }
    return output


def project_supervisor_source_graph_checkpoint(
    checkpoint: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Project an unbounded Source Graph into complete semantic state groups.

    The canonical checkpoint keeps every query, candidate, fetch, rejection,
    and document.  A supervisor does not need every URL/title repeated after
    facts have already been extracted; it needs coverage, dispositions,
    failures, and proof that all ledger rows were accounted.  Literal queries
    and document identities therefore remain in deterministic roster hashes,
    never a fixed sample.
    """

    # ``checkpoint_id`` and ``epoch`` are persistence lineage, not research
    # evidence. Keeping them in the provider payload makes an otherwise
    # identical semantic checkpoint miss the response cache on every epoch.
    # The canonical Source Graph still retains and validates both fields before
    # this projection is built.
    output = {
        key: checkpoint.get(key)
        for key in (
            "resolved_objective_ids",
            "transport_budget_can_complete_research",
            "semantic_saturation_certified",
        )
        if key in checkpoint
    }
    quarantined_documents = tuple(
        dict(row) for row in checkpoint.get("quarantined_documents") or ()
    )
    normalized_quarantines = tuple(
        {
            **row,
            "quarantine_reason_class": (
                str(row.get("quarantine_reason") or "UNSPECIFIED")
                .split(":", 1)[0]
                .strip()
                or "UNSPECIFIED"
            ),
        }
        for row in quarantined_documents
    )
    quarantine_projection = dict(
        _project_state_collection(
            normalized_quarantines,
            collection_name="supervisor_quarantined_documents",
            identity_fields=("document_id", "candidate_id"),
            group_fields=(
                "quarantine_reason_class",
                "parser_refetch_required",
                "evidence_eligible",
                "score_authority",
            ),
            relation_fields=("objective_ids",),
            numeric_fields=(),
        )
    )
    quarantine_projection.update(
        {
            "document_id_roster": _project_text_roster(
                row.get("document_id") for row in quarantined_documents
            ),
            "candidate_id_roster": _project_text_roster(
                row.get("candidate_id") for row in quarantined_documents
            ),
            "query_id_roster": _project_text_roster(
                query_id
                for row in quarantined_documents
                for query_id in row.get("query_ids") or ()
            ),
            "url_roster": _project_text_roster(
                row.get("url") for row in quarantined_documents
            ),
            "content_hash_roster": _project_text_roster(
                row.get("content_hash") for row in quarantined_documents
            ),
            "quarantine_reason_roster": _project_text_roster(
                row.get("quarantine_reason") for row in quarantined_documents
            ),
            "full_quarantine_records_persisted_outside_prompt": True,
            "every_quarantine_accounted_by_hash_and_group_count": (
                quarantine_projection[
                    "every_record_accounted_by_hash_and_group_count"
                ]
            ),
        }
    )
    output["quarantined_documents"] = quarantine_projection
    collection_specs = {
        "query_failures": (
            ("failure_id", "query_id"),
            (
                "failure_stage",
                "alternate_route_required",
                "absence_eligible",
                "zero_result_only",
            ),
            ("objective_id",),
            (),
            ("failure_reason",),
        ),
        "provider_failures": (
            ("failure_id",),
            (
                "failure_stage",
                "retryable",
                "absence_eligible",
                "zero_result_only",
            ),
            ("objective_id",),
            (),
            ("failure_reason",),
        ),
        "search_candidates": (
            ("candidate_id",),
            (
                "ranking_status",
                "fetch_status",
                "candidate_source_family_hint",
                "verified_official_domain_candidate",
            ),
            ("objective_ids", "requested_source_families"),
            ("material_priority", "rank"),
            ("url", "title", "snippet"),
        ),
        "candidate_materiality_decisions": (
            ("decision_id", "candidate_id"),
            (
                "material_relevance",
                "evidence_eligible",
                "snippet_discovery_only",
                "score_authority",
            ),
            ("objective_ids",),
            ("priority",),
            ("rationale",),
        ),
        "fetch_records": (
            ("fetch_id", "candidate_id"),
            (
                "disposition",
                "full_fetch_attempted",
                "snippet_used_as_document",
                "score_authority",
            ),
            ("objective_ids",),
            (),
            ("provider_error", "error"),
        ),
        "rejected_documents": (
            ("rejection_id", "candidate_id"),
            (
                "retryable",
                "snippet_used_as_document",
                "score_authority",
            ),
            ("objective_ids", "accepted_claim_ids"),
            (),
            ("rejection_reason",),
        ),
    }
    for key, (
        identity_fields,
        group_fields,
        relation_fields,
        numeric_fields,
        hashed_text_fields,
    ) in collection_specs.items():
        rows = tuple(dict(row) for row in checkpoint.get(key) or ())
        projection = dict(
            _project_state_collection(
                rows,
                collection_name=f"supervisor_{key}",
                identity_fields=identity_fields,
                group_fields=group_fields,
                relation_fields=relation_fields,
                numeric_fields=numeric_fields,
            )
        )
        projection["omitted_text_rosters"] = {
            field: _project_text_roster(row.get(field) for row in rows)
            for field in hashed_text_fields
        }
        output[key] = projection

    queries = tuple(
        dict(row) for row in checkpoint.get("generated_queries") or ()
    )
    query_projection = dict(
        _project_state_collection(
            queries,
            collection_name="supervisor_generated_queries",
            identity_fields=("query_id",),
            group_fields=(
                "execution_status",
                "counter_or_supersession_search",
            ),
            relation_fields=(
                "objective_id",
                "source_families",
                "official_gap_reasons",
                "provider_errors",
            ),
            numeric_fields=("search_result_count",),
        )
    )
    query_projection.update(
        {
            "literal_query_roster": _project_text_roster(
                row.get("literal_query") for row in queries
            ),
            "query_rationale_roster": _project_text_roster(
                row.get("rationale") for row in queries
            ),
            "every_literal_query_accounted_by_hash": True,
        }
    )
    output["generated_queries"] = query_projection

    documents = tuple(
        dict(row) for row in checkpoint.get("evidence_documents") or ()
    )
    semantic_documents = tuple(
        {
            field: row.get(field)
            for field in (*_DOCUMENT_MANIFEST_FIELDS, "publication_date_source")
            if field in row
        }
        for row in documents
    )
    document_projection = dict(
        _project_state_collection(
            semantic_documents,
            collection_name="supervisor_evidence_documents",
            identity_fields=("document_id",),
            group_fields=(
                "source_family",
                "source_provider",
                "publication_date_source",
                "full_fetch_performed",
                "snippet_only",
                "evidence_eligible",
            ),
            relation_fields=(),
            group_relation_fields=("source_independence_group",),
            numeric_fields=(),
        )
    )
    document_projection.update(
        {
            "document_id_roster": _project_text_roster(
                row.get("document_id") for row in documents
            ),
            "canonical_url_roster": _project_text_roster(
                row.get("canonical_url") for row in documents
            ),
            "content_hash_roster": _project_text_roster(
                row.get("content_hash") for row in documents
            ),
            "acquisition_lineage_excluded_from_provider": True,
            "semantic_document_fields": [
                *_DOCUMENT_MANIFEST_FIELDS,
                "publication_date_source",
            ],
            "excluded_acquisition_lineage_fields": [
                *_DOCUMENT_RELATION_FIELDS,
                "verified_official_discovery_urls",
            ],
            "full_acquisition_lineage_persisted_in_source_graph": True,
            "full_document_bodies_omitted_after_fact_extraction": True,
            "every_semantic_document_accounted": (
                len(semantic_documents) == len(documents)
            ),
        }
    )
    output["evidence_documents"] = document_projection
    output["source_graph_prompt_projection"] = {
        "schema_version": "e2r_v5_supervisor_source_graph_projection_v4",
        "complete_artifact_persisted_outside_prompt": True,
        "every_query_document_and_state_row_accounted": True,
        "checkpoint_lineage_excluded_from_provider": True,
        "excluded_checkpoint_lineage_fields": ["checkpoint_id", "epoch"],
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }
    return output


def project_generated_queries(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Keep every literal query while dropping repeated provider transport data."""

    payloads = tuple(dict(row) for row in rows)
    ordered = tuple(
        sorted(
            payloads,
            key=lambda row: (
                str(row.get("query_id") or ""),
                _stable_hash(row),
            ),
        )
    )
    queries = [
        [row.get(key) for key in _GENERATED_QUERY_PROMPT_FIELDS]
        for row in ordered
    ]
    literal_query_index = _GENERATED_QUERY_PROMPT_FIELDS.index("literal_query")
    return {
        "schema_version": "e2r_v5_generated_query_prompt_projection_v1",
        "query_count": len(ordered),
        "query_roster_hash": _stable_hash(ordered),
        "query_fields": list(_GENERATED_QUERY_PROMPT_FIELDS),
        "queries": queries,
        "every_literal_query_preserved": all(
            str(row[literal_query_index] or "").strip() for row in queries
        ),
        "full_query_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def project_evidence_facts(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Keep every economic fact and lineage while compressing advisory tags.

    Question-family and primitive tags are extraction context rather than score
    gates.  Their complete coverage and the raw fact roster hash remain in the
    projection, while each fact keeps the economic mechanism, value, lifecycle,
    structured role, and source/claim/quote lineage used by the supervisor.
    """

    payloads = tuple(_record_dict(row) for row in rows)
    ordered = tuple(
        sorted(
            payloads,
            key=lambda row: (
                str(row.get("fact_id") or ""),
                _stable_hash(row),
            ),
        )
    )
    groups: dict[tuple[str, ...], list[Mapping[str, Any]]] = {}
    for row in ordered:
        key = tuple(str(row.get(field) or "") for field in _FACT_GROUP_FIELDS)
        groups.setdefault(key, []).append(row)

    semantic_groups = []
    for key in sorted(groups):
        grouped_rows = groups[key]
        observation_counts: dict[str, int] = {}
        for row in grouped_rows:
            observation = {
                field: row[field]
                for field in _FACT_OBSERVATION_FIELDS
                if field in row
            }
            encoded = json.dumps(
                observation,
                ensure_ascii=False,
                sort_keys=True,
                default=str,
            )
            observation_counts[encoded] = observation_counts.get(encoded, 0) + 1
        observations = []
        for encoded, count in sorted(observation_counts.items()):
            observation = json.loads(encoded)
            observations.append(
                [
                    *(observation.get(field) for field in _FACT_OBSERVATION_FIELDS),
                    count,
                ]
            )
        semantic_groups.append(
            {
                "state": {
                    field: key[index]
                    for index, field in enumerate(_FACT_GROUP_FIELDS)
                },
                "fact_count": len(grouped_rows),
                "fact_roster_hash": _stable_hash(grouped_rows),
                "fact_id_roster": _project_text_roster(
                    row.get("fact_id") for row in grouped_rows
                ),
                "source_id_roster": _project_text_roster(
                    source_id
                    for row in grouped_rows
                    for source_id in row.get("source_ids") or ()
                ),
                "claim_id_roster": _project_text_roster(
                    claim_id
                    for row in grouped_rows
                    for claim_id in row.get("claim_ids") or ()
                ),
                "quote_id_roster": _project_text_roster(
                    quote_id
                    for row in grouped_rows
                    for quote_id in row.get("quote_ids") or ()
                ),
                "source_independence_group_coverage": _relation_coverage(
                    grouped_rows, "source_independence_group"
                ),
                "corroborating_independence_group_coverage": _relation_coverage(
                    grouped_rows, "corroborating_independence_groups"
                ),
                "allowed_component_coverage": _relation_coverage(
                    grouped_rows, "allowed_component_ids"
                ),
                "semantic_observation_count": sum(observation_counts.values()),
                "semantic_observations": observations,
                "advisory_tag_roster_hash": _stable_hash(
                    [
                        {
                            "fact_id": row.get("fact_id"),
                            "question_family_tags": sorted(
                                str(value)
                                for value in row.get("question_family_tags") or ()
                            ),
                            "primitive_tags": sorted(
                                str(value)
                                for value in row.get("primitive_tags") or ()
                            ),
                        }
                        for row in grouped_rows
                    ]
                ),
            }
        )
    return {
        "schema_version": "e2r_v5_evidence_fact_prompt_projection_v1",
        "fact_count": len(ordered),
        "fact_roster_hash": _stable_hash(ordered),
        "target_id_coverage": _relation_coverage(ordered, "target_id"),
        "as_of_date_coverage": _relation_coverage(ordered, "as_of_date"),
        "semantic_group_count": len(semantic_groups),
        "semantic_observation_fields": [
            *_FACT_OBSERVATION_FIELDS,
            "fact_count",
        ],
        "question_family_tag_coverage": _relation_coverage(
            ordered, "question_family_tags"
        ),
        "primitive_tag_coverage": _relation_coverage(ordered, "primitive_tags"),
        "semantic_fact_groups": semantic_groups,
        "every_fact_accounted_by_hash_and_group_count": (
            sum(row["fact_count"] for row in semantic_groups) == len(ordered)
        ),
        "every_semantic_observation_accounted": all(
            row["semantic_observation_count"] == row["fact_count"]
            for row in semantic_groups
        ),
        "every_fact_accounted_by_hash": True,
        "advisory_tags_are_not_score_gates": True,
        "full_fact_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def project_fact_extraction_evidence_context(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Compact every prior fact for the full-document extraction prompt.

    A growing fact graph must not crowd the *new* full document out of the
    provider context window.  Exact prior fact records are already persisted
    and the deterministic compiler owns cross-document deduplication.  The
    extractor therefore needs semantic state/coverage plus a loss-accounting
    proof, not every old narrative, value, quote id, and source id replayed.

    No fact is sampled or dropped: every row contributes to the ordered roster
    hash, one semantic-state group, every aggregate coverage count, and the
    hashed observation/lineage rosters below.
    """

    payloads = tuple(_record_dict(row) for row in rows)
    ordered = tuple(
        sorted(
            payloads,
            key=lambda row: (
                str(row.get("fact_id") or ""),
                _stable_hash(row),
            ),
        )
    )
    groups: dict[tuple[str, ...], list[Mapping[str, Any]]] = {}
    for row in ordered:
        key = tuple(str(row.get(field) or "") for field in _FACT_GROUP_FIELDS)
        groups.setdefault(key, []).append(row)

    semantic_state_groups = []
    for key in sorted(groups):
        grouped_rows = groups[key]
        semantic_state_groups.append(
            [
                *key,
                len(grouped_rows),
                _stable_hash(grouped_rows),
            ]
        )

    observation_rows = tuple(
        {
            field: row.get(field)
            for field in _FACT_OBSERVATION_FIELDS
            if field in row
        }
        for row in ordered
    )
    advisory_rows = tuple(
        {
            "fact_id": row.get("fact_id"),
            "question_family_tags": tuple(
                sorted(str(value) for value in row.get("question_family_tags") or ())
            ),
            "primitive_tags": tuple(
                sorted(str(value) for value in row.get("primitive_tags") or ())
            ),
        }
        for row in ordered
    )
    return {
        "schema_version": "e2r_v5_fact_extraction_evidence_context_v1",
        "fact_count": len(ordered),
        "fact_roster_hash": _stable_hash(ordered),
        "semantic_state_fields": [
            *_FACT_GROUP_FIELDS,
            "fact_count",
            "fact_roster_hash",
        ],
        "semantic_state_group_count": len(semantic_state_groups),
        "semantic_state_groups": semantic_state_groups,
        "target_id_coverage": _relation_coverage(ordered, "target_id"),
        "as_of_date_coverage": _relation_coverage(ordered, "as_of_date"),
        "structured_evidence_role_coverage": _relation_coverage(
            ordered, "structured_evidence_roles"
        ),
        "allowed_component_coverage": _relation_coverage(
            ordered, "allowed_component_ids"
        ),
        "source_independence_group_coverage": _relation_coverage(
            ordered, "source_independence_group"
        ),
        "corroborating_independence_group_coverage": _relation_coverage(
            ordered, "corroborating_independence_groups"
        ),
        "predicate_roster": _project_text_roster(
            row.get("predicate") for row in ordered
        ),
        "economic_mechanism_roster": _project_text_roster(
            row.get("economic_mechanism") for row in ordered
        ),
        "fact_id_roster": _project_text_roster(
            row.get("fact_id") for row in ordered
        ),
        "source_id_roster": _project_text_roster(
            value
            for row in ordered
            for value in row.get("source_ids") or ()
        ),
        "claim_id_roster": _project_text_roster(
            value
            for row in ordered
            for value in row.get("claim_ids") or ()
        ),
        "quote_id_roster": _project_text_roster(
            value
            for row in ordered
            for value in row.get("quote_ids") or ()
        ),
        "semantic_observation_count": len(observation_rows),
        "semantic_observation_roster_hash": _stable_hash(observation_rows),
        "advisory_tag_roster_hash": _stable_hash(advisory_rows),
        "every_fact_accounted_by_hash_and_group_count": (
            sum(row[-2] for row in semantic_state_groups) == len(ordered)
        ),
        "every_semantic_observation_accounted_by_hash": True,
        "cross_document_deduplication_owner": "DETERMINISTIC_EVIDENCE_FACT_COMPILER",
        "full_fact_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def project_supervisor_evidence_facts(
    rows: Sequence[Mapping[str, Any]],
    *,
    independent_corroboration_fact_ids: Sequence[str] | None = None,
) -> Mapping[str, Any]:
    """Account for the complete fact graph without replaying every narrative.

    Component researchers receive the citable fact table and write the detailed
    synthesis.  The later supervisor needs the complete semantic coverage and
    lineage accounting, but not one copy of each already-persisted narrative,
    value, and source id.  This groups every fact and hashes every omitted
    observation; it never selects a top-N subset or authorizes a score.
    """

    payloads = tuple(_record_dict(row) for row in rows)
    projection = dict(
        _project_state_collection(
            payloads,
            collection_name="supervisor_evidence_fact_graph",
            identity_fields=("fact_id",),
            group_fields=_SUPERVISOR_FACT_GROUP_FIELDS,
            relation_fields=(),
            group_relation_fields=(
                "structured_evidence_roles",
                "allowed_component_ids",
            ),
            numeric_fields=("confidence",),
        )
    )
    semantic_group_fields = (
        *_SUPERVISOR_FACT_GROUP_FIELDS,
        "record_count",
        "record_roster_hash",
        "confidence_distribution",
        "structured_evidence_role_coverage",
        "allowed_component_coverage",
    )
    verbose_semantic_groups = tuple(projection.get("semantic_groups") or ())
    projection["semantic_groups"] = {
        "fields": list(semantic_group_fields),
        "confidence_distribution_fields": [
            "count",
            "minimum",
            "median",
            "maximum",
        ],
        "rows": [
            [
                *(
                    row.get("state", {}).get(field)
                    for field in _SUPERVISOR_FACT_GROUP_FIELDS
                ),
                row.get("record_count"),
                row.get("record_roster_hash"),
                [
                    (row.get("numeric_distributions", {})
                     .get("confidence", {})
                     .get(field))
                    for field in (
                        "count",
                        "minimum",
                        "median",
                        "maximum",
                    )
                ],
                (row.get("relation_coverage", {}) or {}).get(
                    "structured_evidence_roles", {}
                ),
                (row.get("relation_coverage", {}) or {}).get(
                    "allowed_component_ids", {}
                ),
            ]
            for row in verbose_semantic_groups
        ],
    }
    projection["semantic_group_encoding"] = "LOSSLESS_COLUMNAR_ALL_ROWS"
    projection["every_semantic_group_projected"] = (
        len(projection["semantic_groups"]["rows"])
        == int(projection.get("semantic_group_count") or 0)
    )
    all_current_information_confidence_rows = tuple(
        row
        for row in payloads
        if str(row.get("current_lifecycle") or "") in {"CURRENT", "OPEN"}
        and "information_confidence"
        in {
            str(value)
            for value in row.get("allowed_component_ids") or ()
        }
    )
    independent_corroboration_scope = (
        None
        if independent_corroboration_fact_ids is None
        else frozenset(
            str(value)
            for value in independent_corroboration_fact_ids
            if str(value)
        )
    )
    current_information_confidence_rows = tuple(
        row
        for row in all_current_information_confidence_rows
        if independent_corroboration_scope is None
        or str(row.get("fact_id") or "")
        in independent_corroboration_scope
    )
    matched_independent_corroboration_scope = frozenset(
        str(row.get("fact_id") or "")
        for row in current_information_confidence_rows
        if str(row.get("fact_id") or "")
    )
    unmatched_independent_corroboration_scope = frozenset(
        (independent_corroboration_scope or ())
    ) - matched_independent_corroboration_scope
    primary_independence_family_rows = tuple(
        {
            "source_family": _independence_group_source_family(
                row.get("source_independence_group")
            )
        }
        for row in current_information_confidence_rows
        if _independence_group_source_family(
            row.get("source_independence_group")
        )
    )
    corroborating_independence_family_rows = tuple(
        {"source_family": _independence_group_source_family(value)}
        for row in current_information_confidence_rows
        for value in _independent_corroborating_groups(row)
        if _independence_group_source_family(value)
    )
    relationship_fields = (
        "subject",
        "business_segment",
        "product_family",
        "economic_mechanism",
        "predicate",
        "direction",
        "current_lifecycle",
    )
    relationship_groups: dict[
        tuple[str, ...], list[Mapping[str, Any]]
    ] = {}
    for row in current_information_confidence_rows:
        key = tuple(str(row.get(field) or "") for field in relationship_fields)
        relationship_groups.setdefault(key, []).append(row)
    relationship_profiles = []
    for key in sorted(relationship_groups):
        grouped_rows = relationship_groups[key]
        independent_groups = tuple(
            value
            for row in grouped_rows
            for value in _independent_corroborating_groups(row)
        )
        relationship_profiles.append(
            {
                "relationship": {
                    field: key[index]
                    for index, field in enumerate(relationship_fields)
                },
                "fact_count": len(grouped_rows),
                "fact_roster_hash": _stable_hash(grouped_rows),
                "primary_source_family_coverage": _relation_coverage(
                    tuple(
                        {
                            "source_family": (
                                _independence_group_source_family(
                                    row.get("source_independence_group")
                                )
                            )
                        }
                        for row in grouped_rows
                    ),
                    "source_family",
                ),
                "independent_corroborating_source_family_coverage": (
                    _relation_coverage(
                        tuple(
                            {
                                "source_family": (
                                    _independence_group_source_family(value)
                                )
                            }
                            for value in independent_groups
                        ),
                        "source_family",
                    )
                ),
                "independent_corroboration_present": bool(independent_groups),
            }
        )
    if independent_corroboration_scope is None:
        projected_relationship_profiles: Any = relationship_profiles
        relationship_profile_encoding = "VERBOSE_OBJECT_ROWS"
    else:
        relationship_profile_fields = (
            *relationship_fields,
            "fact_count",
            "fact_roster_hash",
            "primary_source_family_coverage",
            "independent_corroborating_source_family_coverage",
            "independent_corroboration_present",
        )
        projected_relationship_profiles = {
            "fields": list(relationship_profile_fields),
            "rows": [
                [
                    *(
                        row["relationship"].get(field)
                        for field in relationship_fields
                    ),
                    row["fact_count"],
                    row["fact_roster_hash"],
                    row["primary_source_family_coverage"],
                    row[
                        "independent_corroborating_source_family_coverage"
                    ],
                    row["independent_corroboration_present"],
                ]
                for row in relationship_profiles
            ],
        }
        relationship_profile_encoding = "LOSSLESS_COLUMNAR_ALL_ROWS"
    projection.update(
        {
            "schema_version": "e2r_v5_supervisor_fact_prompt_projection_v4",
            "fact_id_roster": _project_text_roster(
                row.get("fact_id") for row in payloads
            ),
            "source_id_roster": _project_text_roster(
                source_id
                for row in payloads
                for source_id in row.get("source_ids") or ()
            ),
            "claim_id_roster": _project_text_roster(
                claim_id
                for row in payloads
                for claim_id in row.get("claim_ids") or ()
            ),
            "quote_id_roster": _project_text_roster(
                quote_id
                for row in payloads
                for quote_id in row.get("quote_ids") or ()
            ),
            "subject_roster": _project_text_roster(
                row.get("subject") for row in payloads
            ),
            "economic_mechanism_roster": _project_text_roster(
                row.get("economic_mechanism") for row in payloads
            ),
            "predicate_roster": _project_text_roster(
                row.get("predicate") for row in payloads
            ),
            "source_independence_group_roster": _project_text_roster(
                row.get("source_independence_group") for row in payloads
            ),
            "corroborating_independence_group_roster": _project_text_roster(
                value
                for row in payloads
                for value in row.get("corroborating_independence_groups") or ()
            ),
            "independent_corroboration_review": {
                "schema_version": (
                    "e2r_v5_independent_corroboration_review_projection_v1"
                ),
                "current_information_confidence_fact_count": len(
                    current_information_confidence_rows
                ),
                "all_current_information_confidence_fact_count": len(
                    all_current_information_confidence_rows
                ),
                "review_scope": (
                    "ALL_CURRENT_INFORMATION_CONFIDENCE_FACTS"
                    if independent_corroboration_scope is None
                    else "CURRENT_INFORMATION_CONFIDENCE_MEMO_FACTS"
                ),
                "review_scope_fact_id_roster_hash": _stable_hash(
                    sorted(independent_corroboration_scope or ())
                ),
                "review_scope_requested_fact_count": (
                    len(independent_corroboration_scope)
                    if independent_corroboration_scope is not None
                    else len(all_current_information_confidence_rows)
                ),
                "review_scope_matched_fact_count": len(
                    current_information_confidence_rows
                ),
                "review_scope_unmatched_fact_count": len(
                    unmatched_independent_corroboration_scope
                ),
                "review_scope_unmatched_fact_id_roster_hash": _stable_hash(
                    sorted(unmatched_independent_corroboration_scope)
                ),
                "review_scope_requested_equals_matched_plus_unmatched": (
                    (
                        len(independent_corroboration_scope)
                        if independent_corroboration_scope is not None
                        else len(all_current_information_confidence_rows)
                    )
                    == len(current_information_confidence_rows)
                    + len(unmatched_independent_corroboration_scope)
                ),
                "review_scope_uses_fixed_top_n": False,
                "facts_outside_current_memo_remain_accounted_in_semantic_groups": True,
                "primary_source_family_coverage": _relation_coverage(
                    primary_independence_family_rows,
                    "source_family",
                ),
                "corroborating_source_family_coverage": _relation_coverage(
                    corroborating_independence_family_rows,
                    "source_family",
                ),
                "fact_with_explicit_corroborating_group_count": sum(
                    bool(_independent_corroborating_groups(row))
                    for row in current_information_confidence_rows
                ),
                "fact_without_explicit_corroborating_group_count": sum(
                    not bool(_independent_corroborating_groups(row))
                    for row in current_information_confidence_rows
                ),
                "relationship_profiles": projected_relationship_profiles,
                "relationship_profile_encoding": (
                    relationship_profile_encoding
                ),
                "every_relationship_profile_projected": True,
                "every_information_confidence_fact_accounted_by_hash_and_group_count": (
                    sum(row["fact_count"] for row in relationship_profiles)
                    == len(current_information_confidence_rows)
                ),
                "review_required": True,
                "llm_owns_gap_materiality": True,
                "absence_of_corroboration_is_not_source_absence": True,
                "instruction": (
                    "Use this provenance coverage together with the supplied "
                    "component memos and synthesis to decide whether a named "
                    "relationship still needs an independent source family. "
                    "Coverage counts are diagnostic and never create a gap, "
                    "query, fact, score, or absence deterministically."
                ),
            },
            "value_observation_roster": _project_text_roster(
                json.dumps(
                    {
                        "value": row.get("value"),
                        "unit": row.get("unit"),
                        "period": row.get("period"),
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                    default=str,
                )
                for row in payloads
            ),
            "question_family_tag_roster": _project_text_roster(
                value
                for row in payloads
                for value in row.get("question_family_tags") or ()
            ),
            "primitive_tag_roster": _project_text_roster(
                value
                for row in payloads
                for value in row.get("primitive_tags") or ()
            ),
            "all_narrative_and_value_observations_accounted_by_hash": True,
            "full_fact_records_persisted_outside_prompt": True,
            "fixed_top_n_used": False,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
        }
    )
    return projection


def _independence_group_source_family(value: Any) -> str:
    """Project only the canonical provenance family, not host or URL detail."""

    text = str(value or "").strip()
    if not text:
        return ""
    return text.split(":", 1)[0].strip()


def _independent_corroborating_groups(
    row: Mapping[str, Any],
) -> tuple[str, ...]:
    """Exclude the primary provenance group from compiler group coverage."""

    primary = str(row.get("source_independence_group") or "").strip()
    primary_key = primary.casefold()
    return tuple(
        dict.fromkeys(
            str(value).strip()
            for value in row.get("corroborating_independence_groups") or ()
            if str(value).strip()
            and str(value).strip().casefold() != primary_key
        )
    )


def project_peer_selection_context(
    evidence_facts: Sequence[Mapping[str, Any]],
    source_claims: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Build a complete business-profile projection for LLM peer direction.

    Peer selection needs the issuer's business/product/economic-driver profile,
    while deterministic connectors supply all valuation numbers afterward.
    Repeating every fact and its matching source claim can exceed the provider
    context window without adding a second economic observation.  Both ledgers
    remain fully accounted by semantic groups, counts, and roster hashes.
    """

    facts = tuple(_record_dict(row) for row in evidence_facts)
    claims = tuple(_record_dict(row) for row in source_claims)
    semantic_claims = tuple(
        {
            key: value
            for key, value in row.items()
            if key not in _SOURCE_CLAIM_EXTRACTION_TRANSPORT_FIELDS
        }
        for row in claims
    )
    fact_profile = dict(
        _project_state_collection(
            facts,
            collection_name="peer_selection_evidence_facts",
            identity_fields=("fact_id",),
            group_fields=_PEER_FACT_GROUP_FIELDS,
            relation_fields=(),
            hashed_group_relation_fields=(
                "predicate",
                "source_independence_group",
            ),
            group_relation_fields=("structured_evidence_roles",),
            numeric_fields=("confidence",),
        )
    )
    fact_profile.update(
        {
            "subject_roster": _project_text_roster(
                row.get("subject") for row in facts
            ),
            "economic_mechanism_roster": _project_text_roster(
                row.get("economic_mechanism") for row in facts
            ),
            "fact_id_roster": _project_text_roster(
                row.get("fact_id") for row in facts
            ),
        }
    )
    claim_profile = dict(
        _project_state_collection(
            semantic_claims,
            collection_name="peer_selection_source_claims",
            identity_fields=("claim_id",),
            group_fields=_PEER_CLAIM_GROUP_FIELDS,
            relation_fields=(),
            hashed_group_relation_fields=("predicate",),
            numeric_fields=(),
        )
    )
    claim_profile.update(
        {
            "subject_roster": _project_text_roster(
                row.get("subject") for row in semantic_claims
            ),
            "economic_mechanism_roster": _project_text_roster(
                row.get("economic_mechanism") for row in semantic_claims
            ),
            "exact_quote_roster": _project_text_roster(
                row.get("exact_quote") for row in semantic_claims
            ),
            "claim_id_roster": _project_text_roster(
                row.get("claim_id") for row in semantic_claims
            ),
            "extraction_transport_lineage_excluded_from_provider": True,
            "excluded_extraction_transport_fields": list(
                _SOURCE_CLAIM_EXTRACTION_TRANSPORT_FIELDS
            ),
        }
    )
    return {
        "schema_version": "e2r_v5_peer_selection_context_projection_v2",
        "evidence_business_profile": fact_profile,
        "source_claim_business_profile": claim_profile,
        "every_fact_and_claim_accounted_by_hash_and_group_count": (
            fact_profile["every_record_accounted_by_hash_and_group_count"]
            and claim_profile["every_record_accounted_by_hash_and_group_count"]
        ),
        "full_fact_and_claim_records_persisted_outside_prompt": True,
        "llm_selects_peer_direction_only": True,
        "structured_values_supplied_after_selection": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def project_citable_evidence_facts(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Keep every citable fact while encoding repeated lineage only once.

    A provider cites the immutable ``fact_row_index`` and deterministic code
    resolves that row back to the exact fact id.  Repeating source, claim, and
    quote id arrays inside every semantic row made large current dossiers exceed
    the model context even though those complete relations were already stored
    in the Evidence Fact ledger.  The prompt therefore keeps every economic
    observation and fact id, dictionary-encodes its source group, and accounts
    for every omitted relation by count/hash.  This is not a top-N selection.
    """

    payloads = tuple(_record_dict(row) for row in rows)
    ordered = tuple(
        sorted(
            payloads,
            key=lambda row: (
                str(row.get("fact_id") or ""),
                _stable_hash(row),
            ),
        )
    )
    source_group_dictionary = tuple(
        sorted(
            {
                str(row.get("source_independence_group") or "")
                for row in ordered
                if str(row.get("source_independence_group") or "").strip()
            }
        )
    )
    source_group_index = {
        value: index for index, value in enumerate(source_group_dictionary)
    }
    fact_fields = (
        "fact_row_index",
        *_CITABLE_FACT_PROMPT_FIELDS,
        *_CITABLE_FACT_DERIVED_FIELDS,
    )
    facts = [
        [
            index,
            *(row.get(key) for key in _CITABLE_FACT_PROMPT_FIELDS),
            source_group_index.get(
                str(row.get("source_independence_group") or ""), -1
            ),
            len(
                {
                    str(value)
                    for value in row.get("corroborating_independence_groups")
                    or ()
                    if str(value).strip()
                }
            ),
        ]
        for index, row in enumerate(ordered)
    ]
    fact_id_index = fact_fields.index("fact_id")
    fact_ids = [str(row[fact_id_index] or "") for row in facts]
    return {
        "schema_version": "e2r_v5_citable_fact_prompt_projection_v3",
        "fact_count": len(ordered),
        "fact_roster_hash": _stable_hash(ordered),
        "fact_fields": list(fact_fields),
        "facts": facts,
        "every_fact_id_preserved": (
            len(set(fact_ids)) == len(ordered) and all(fact_ids)
        ),
        "source_independence_group_dictionary": list(
            source_group_dictionary
        ),
        "source_id_roster": _project_text_roster(
            source_id
            for row in ordered
            for source_id in row.get("source_ids") or ()
        ),
        "claim_id_roster": _project_text_roster(
            claim_id
            for row in ordered
            for claim_id in row.get("claim_ids") or ()
        ),
        "quote_id_roster": _project_text_roster(
            quote_id
            for row in ordered
            for quote_id in row.get("quote_ids") or ()
        ),
        "corroborating_independence_group_roster": _project_text_roster(
            value
            for row in ordered
            for value in row.get("corroborating_independence_groups") or ()
        ),
        "target_id_coverage": _relation_coverage(ordered, "target_id"),
        "as_of_date_coverage": _relation_coverage(ordered, "as_of_date"),
        "allowed_component_coverage": _relation_coverage(
            ordered, "allowed_component_ids"
        ),
        "question_family_tag_roster_hash": _stable_hash(
            [
                (
                    row.get("fact_id"),
                    sorted(
                        str(value)
                        for value in row.get("question_family_tags") or ()
                    ),
                )
                for row in ordered
            ]
        ),
        "primitive_tag_roster_hash": _stable_hash(
            [
                (
                    row.get("fact_id"),
                    sorted(
                        str(value) for value in row.get("primitive_tags") or ()
                    ),
                )
                for row in ordered
            ]
        ),
        "advisory_tags_are_not_score_gates": True,
        "every_fact_lineage_accounted_by_count_and_hash": True,
        "repeated_lineage_arrays_omitted_from_semantic_rows": True,
        "full_fact_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def project_current_decision_citable_facts(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Expose every current/open fact and hash-account for closed history.

    Current Researcher Mode can accumulate thousands of superseded and resolved
    facts across a long point-in-time backfill.  Replaying the full prose for
    those closed states to every business/component/red-team pass both exceeds
    the provider context window and risks letting obsolete evidence influence a
    current decision.  Current/open rows remain individually citable and retain
    every economic field through a lossless dictionary-encoded table.  Closed
    rows are not sampled: every one contributes to deterministic state groups,
    counts, and roster hashes, while its full immutable record remains in the
    Evidence Fact ledger.
    """

    payloads = tuple(_record_dict(row) for row in rows)
    ordered = tuple(
        sorted(
            payloads,
            key=lambda row: (
                str(row.get("fact_id") or ""),
                _stable_hash(row),
            ),
        )
    )
    current_rows = tuple(
        row
        for row in ordered
        if str(row.get("current_lifecycle") or "")
        not in {"RESOLVED", "SUPERSEDED"}
    )
    closed_rows = tuple(
        row
        for row in ordered
        if str(row.get("current_lifecycle") or "")
        in {"RESOLVED", "SUPERSEDED"}
    )
    semantic_fields = tuple(
        field for field in _CITABLE_FACT_PROMPT_FIELDS if field != "fact_id"
    )
    value_dictionaries: dict[str, list[Any]] = {}
    value_indices: dict[str, Mapping[str, int]] = {}
    for field in semantic_fields:
        encoded_values = {
            json.dumps(
                row.get(field),
                ensure_ascii=False,
                sort_keys=True,
                default=str,
            )
            for row in current_rows
        }
        ordered_values = sorted(encoded_values)
        value_dictionaries[field] = [
            json.loads(value) for value in ordered_values
        ]
        value_indices[field] = {
            value: index for index, value in enumerate(ordered_values)
        }
    fact_fields = (
        "fact_row_index",
        *(f"{field}_dictionary_index" for field in semantic_fields),
    )
    facts = []
    fact_ids = []
    for row_index, row in enumerate(current_rows):
        facts.append(
            [
                row_index,
                *(
                    value_indices[field][
                        json.dumps(
                            row.get(field),
                            ensure_ascii=False,
                            sort_keys=True,
                            default=str,
                        )
                    ]
                    for field in semantic_fields
                ),
            ]
        )
        fact_ids.append(str(row.get("fact_id") or ""))
    closed_projection = _project_state_collection(
        closed_rows,
        collection_name="closed_evidence_fact_history",
        identity_fields=("fact_id",),
        group_fields=(
            "business_segment",
            "product_family",
            "direction",
            "current_lifecycle",
            "allowed_component_ids",
            "structured_evidence_roles",
        ),
        relation_fields=(),
        numeric_fields=(),
    )
    return {
        "schema_version": "e2r_v5_current_decision_citable_fact_projection_v1",
        "input_fact_count": len(ordered),
        "fact_count": len(current_rows),
        "closed_fact_count": len(closed_rows),
        "input_fact_roster_hash": _stable_hash(ordered),
        "current_fact_roster_hash": _stable_hash(current_rows),
        "closed_fact_roster_hash": _stable_hash(closed_rows),
        "fact_fields": list(fact_fields),
        "fact_value_dictionaries": value_dictionaries,
        "facts": facts,
        # Deterministic citation resolution needs this private roster, but each
        # caller explicitly excludes it from the provider payload.
        "fact_id_by_row_index": fact_ids,
        "current_fact_id_roster": _project_text_roster(fact_ids),
        "closed_fact_history": closed_projection,
        "every_input_fact_accounted": (
            len(current_rows) + len(closed_rows) == len(ordered)
        ),
        "every_current_fact_individually_citable": (
            len(facts) == len(current_rows)
            and all(fact_ids)
            and len(set(fact_ids)) == len(fact_ids)
        ),
        "every_closed_fact_accounted_by_hash_and_group_count": (
            closed_projection[
                "every_record_accounted_by_hash_and_group_count"
            ]
        ),
        "dictionary_encoding_is_lossless": True,
        "closed_lifecycle_rows_cannot_drive_current_score": True,
        "full_fact_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def project_stage_gate_citable_facts(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Expose every Stage-mappable fact and account for every excluded fact.

    Stage primitive mappings can only accept CURRENT/OPEN POSITIVE facts as
    SUPPORT and CURRENT/OPEN COUNTER facts as COUNTER. Closed lifecycle rows
    and active NEUTRAL/RESOLUTION rows therefore cannot be selected by the
    Stage mapper. They are not sampled or discarded: every input fact remains
    represented in the full fact-lineage profile and in one exact eligibility
    partition count/hash, while the immutable ledger stays available to
    deterministic validation.

    Eligible rows reuse the canonical dictionary-coded citable-fact table. Its
    private row-index-to-fact-id roster is retained for deterministic
    resolution; callers must exclude that roster from provider payloads.
    """

    payloads = tuple(
        sorted(
            (_record_dict(row) for row in rows),
            key=lambda row: (
                str(row.get("fact_id") or ""),
                _stable_hash(row),
            ),
        )
    )
    eligible_rows = tuple(
        row
        for row in payloads
        if str(row.get("current_lifecycle") or "") in {"CURRENT", "OPEN"}
        and str(row.get("direction") or "") in {"POSITIVE", "COUNTER"}
    )
    closed_rows = tuple(
        row
        for row in payloads
        if str(row.get("current_lifecycle") or "")
        in {"RESOLVED", "SUPERSEDED"}
    )
    active_non_mappable_rows = tuple(
        row
        for row in payloads
        if str(row.get("current_lifecycle") or "") in {"CURRENT", "OPEN"}
        and str(row.get("direction") or "") in {"NEUTRAL", "RESOLUTION"}
    )
    accounted_ids = {
        id(row)
        for row in (
            *eligible_rows,
            *closed_rows,
            *active_non_mappable_rows,
        )
    }
    if len(accounted_ids) != len(payloads):
        raise ValueError(
            "Stage gate fact projection received unknown lifecycle/direction"
        )

    projection = dict(project_current_decision_citable_facts(eligible_rows))
    projection.update(
        {
            "schema_version": (
                "e2r_v5_stage_gate_citable_fact_projection_v1"
            ),
            "input_fact_count": len(payloads),
            "fact_count": len(eligible_rows),
            "closed_fact_count": len(closed_rows),
            "active_non_mappable_fact_count": len(
                active_non_mappable_rows
            ),
            "input_fact_roster_hash": _stable_hash(payloads),
            "current_fact_roster_hash": _stable_hash(eligible_rows),
            "closed_fact_roster_hash": _stable_hash(closed_rows),
            "active_non_mappable_fact_roster_hash": _stable_hash(
                active_non_mappable_rows
            ),
            "closed_fact_history": _project_opaque_fact_partition(
                closed_rows,
                partition_name="closed_fact_history",
                exclusion_reason="CLOSED_LIFECYCLE_CANNOT_MAP_CURRENT_STAGE",
            ),
            "active_non_mappable_fact_history": (
                _project_opaque_fact_partition(
                    active_non_mappable_rows,
                    partition_name="active_non_mappable_fact_history",
                    exclusion_reason=(
                        "NEUTRAL_OR_RESOLUTION_CANNOT_MAP_SUPPORT_OR_COUNTER"
                    ),
                )
            ),
            "all_fact_lineage_profile": (
                project_fact_extraction_evidence_context(payloads)
            ),
            "every_input_fact_accounted": (
                len(eligible_rows)
                + len(closed_rows)
                + len(active_non_mappable_rows)
                == len(payloads)
            ),
            "every_eligible_fact_individually_citable": projection[
                "every_current_fact_individually_citable"
            ],
            "every_ineligible_fact_accounted_by_count_and_hash": True,
            "stage_gate_eligibility_is_semantic_not_top_n": True,
            "closed_lifecycle_rows_cannot_drive_current_score": True,
            "active_neutral_or_resolution_rows_cannot_map_stage": True,
            "full_fact_records_persisted_outside_prompt": True,
            "fixed_top_n_used": False,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
        }
    )
    return projection


def project_claim_fact_link_profile(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Count/hash-account every immutable claim-to-fact lineage edge."""

    payloads = tuple(dict(row) for row in rows)
    ordered = tuple(
        sorted(
            payloads,
            key=lambda row: (
                str(row.get("claim_id") or ""),
                str(row.get("fact_id") or ""),
                str(row.get("link_id") or ""),
                _stable_hash(row),
            ),
        )
    )
    return {
        "schema_version": "e2r_v5_claim_fact_link_profile_v1",
        "link_count": len(ordered),
        "link_roster_hash": _stable_hash(ordered),
        "claim_id_roster": _project_text_roster(
            row.get("claim_id") for row in ordered
        ),
        "fact_id_roster": _project_text_roster(
            row.get("fact_id") for row in ordered
        ),
        "source_id_roster": _project_text_roster(
            source_id
            for row in ordered
            for source_id in row.get("source_ids") or ()
        ),
        "link_role_roster": _project_text_roster(
            row.get("link_role") for row in ordered
        ),
        "every_link_accounted_by_count_and_hash": True,
        "full_link_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def _project_opaque_fact_partition(
    rows: Sequence[Mapping[str, Any]],
    *,
    partition_name: str,
    exclusion_reason: str,
) -> Mapping[str, Any]:
    """Preserve an ineligible Stage partition without replaying its prose."""

    ordered = tuple(
        sorted(
            (dict(row) for row in rows),
            key=lambda row: (
                str(row.get("fact_id") or ""),
                _stable_hash(row),
            ),
        )
    )
    semantic_rows = tuple(
        {
            field: row.get(field)
            for field in _FACT_OBSERVATION_FIELDS
            if field in row
        }
        for row in ordered
    )
    return {
        "schema_version": "e2r_v5_opaque_fact_partition_v1",
        "partition_name": partition_name,
        "exclusion_reason": exclusion_reason,
        "fact_count": len(ordered),
        "fact_roster_hash": _stable_hash(ordered),
        "fact_id_roster": _project_text_roster(
            row.get("fact_id") for row in ordered
        ),
        "claim_id_roster": _project_text_roster(
            claim_id
            for row in ordered
            for claim_id in row.get("claim_ids") or ()
        ),
        "source_id_roster": _project_text_roster(
            source_id
            for row in ordered
            for source_id in row.get("source_ids") or ()
        ),
        "quote_id_roster": _project_text_roster(
            quote_id
            for row in ordered
            for quote_id in row.get("quote_ids") or ()
        ),
        "semantic_observation_count": len(semantic_rows),
        "semantic_observation_roster_hash": _stable_hash(semantic_rows),
        "every_fact_accounted_by_count_and_hash": True,
        "full_fact_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def project_candidate_ranking_evidence_context(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Account for every fact without replaying a second citable fact plane.

    Candidate ranking chooses which *discovery metadata* deserves a full fetch.
    It cannot cite facts or assign points, and receives the complete open
    research objectives separately.  Replaying thousands of exact narratives,
    predicates, and values here duplicates the later business/component passes
    and can crowd the candidates themselves out of the context window.

    Current/open and closed facts are therefore partitioned by lifecycle and
    passed through the same exhaustive state/count/hash projection used as the
    prior-fact context during full-document extraction.  Every economic
    observation and lineage roster remains hash-accounted; no top-N fact is
    selected.  Exact current narratives remain on disk and are reviewed through
    the citable fact chunks in the memo passes.
    """

    payloads = tuple(
        sorted(
            (_record_dict(row) for row in rows),
            key=lambda row: (
                str(row.get("fact_id") or ""),
                _stable_hash(row),
            ),
        )
    )
    current_rows = tuple(
        row
        for row in payloads
        if str(row.get("current_lifecycle") or "")
        not in {"RESOLVED", "SUPERSEDED"}
    )
    closed_rows = tuple(
        row
        for row in payloads
        if str(row.get("current_lifecycle") or "")
        in {"RESOLVED", "SUPERSEDED"}
    )
    current_profile = project_fact_extraction_evidence_context(current_rows)
    closed_profile = project_fact_extraction_evidence_context(closed_rows)
    return {
        "schema_version": "e2r_v5_candidate_ranking_fact_projection_v2",
        "input_fact_count": len(payloads),
        "fact_count": len(current_rows),
        "closed_fact_count": len(closed_rows),
        "input_fact_roster_hash": _stable_hash(payloads),
        "current_fact_roster_hash": _stable_hash(current_rows),
        "closed_fact_roster_hash": _stable_hash(closed_rows),
        "current_fact_profile": current_profile,
        "closed_fact_profile": closed_profile,
        "every_input_fact_accounted": (
            len(current_rows) + len(closed_rows) == len(payloads)
        ),
        "every_current_fact_individually_accounted": bool(
            current_profile["every_fact_accounted_by_hash_and_group_count"]
            and int(current_profile["fact_count"]) == len(current_rows)
        ),
        "every_closed_fact_accounted": bool(
            closed_profile["every_fact_accounted_by_hash_and_group_count"]
            and int(closed_profile["fact_count"]) == len(closed_rows)
        ),
        "fact_ids_exposed_to_candidate_ranker": False,
        "exact_fact_semantics_reviewed_in_later_citable_fact_chunks": True,
        "open_research_objectives_are_candidate_ranking_semantic_authority": True,
        "full_fact_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "candidate_ranking_evidence_or_score_authority": False,
        "score_authority": False,
    }


def citable_fact_id_by_row_index(
    projection: Mapping[str, Any],
) -> Mapping[int, str]:
    """Recover exact fact ids from the provider-facing row table."""

    private_roster = projection.get("fact_id_by_row_index")
    if private_roster is not None:
        if isinstance(private_roster, (str, bytes)) or not isinstance(
            private_roster, Sequence
        ):
            raise TypeError("private citable fact id roster must be an array")
        result = {
            index: str(fact_id or "").strip()
            for index, fact_id in enumerate(private_roster)
        }
        if (
            len(result) != int(projection.get("fact_count") or 0)
            or any(not fact_id for fact_id in result.values())
            or len(set(result.values())) != len(result)
        ):
            raise ValueError("private citable fact id roster is invalid")
        row_indices = {
            row[0]
            for row in projection.get("facts") or ()
            if isinstance(row, Sequence)
            and not isinstance(row, (str, bytes))
            and row
        }
        if row_indices != set(result):
            raise ValueError("citable fact projection row count mismatch")
        return result

    fields = tuple(str(value) for value in projection.get("fact_fields") or ())
    try:
        row_index_column = fields.index("fact_row_index")
        fact_id_column = fields.index("fact_id")
    except ValueError as exc:
        raise ValueError("citable fact projection lacks row index or fact id") from exc
    result: dict[int, str] = {}
    for row in projection.get("facts") or ():
        if isinstance(row, (str, bytes)) or not isinstance(row, Sequence):
            raise TypeError("citable fact projection row must be an array")
        if len(row) != len(fields):
            raise ValueError("citable fact projection row width mismatch")
        row_index = row[row_index_column]
        fact_id = str(row[fact_id_column] or "").strip()
        if (
            isinstance(row_index, bool)
            or not isinstance(row_index, int)
            or row_index < 0
            or not fact_id
            or row_index in result
        ):
            raise ValueError("citable fact projection row identity is invalid")
        result[row_index] = fact_id
    if len(result) != int(projection.get("fact_count") or 0):
        raise ValueError("citable fact projection row count mismatch")
    return result


def resolve_citable_fact_row_indices(
    value: Any,
    *,
    fact_id_by_row_index: Mapping[int, str],
    label: str,
) -> tuple[str, ...]:
    """Map provider-selected row numbers to exact immutable fact ids."""

    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise TypeError(f"{label} must be an array")
    indices: list[int] = []
    for item in value:
        if isinstance(item, bool) or not isinstance(item, int) or item < 0:
            raise TypeError(f"{label} must contain non-negative integers")
        indices.append(item)
    if len(indices) != len(set(indices)):
        raise ValueError(f"{label} must not contain duplicate row indices")
    unknown = sorted(set(indices) - set(fact_id_by_row_index))
    if unknown:
        raise ValueError(f"{label} contains unknown fact row indices: {unknown}")
    return tuple(fact_id_by_row_index[index] for index in indices)


def project_source_claims(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Keep exact quotes and claim/document/source ids without fact duplication."""

    payloads = tuple(dict(row) for row in rows)
    ordered = tuple(
        sorted(
            payloads,
            key=lambda row: (
                str(row.get("claim_id") or ""),
                _stable_hash(row),
            ),
        )
    )
    claims = [
        [row.get(key) for key in _SOURCE_CLAIM_PROMPT_FIELDS]
        for row in ordered
    ]
    claim_id_index = _SOURCE_CLAIM_PROMPT_FIELDS.index("claim_id")
    exact_quote_index = _SOURCE_CLAIM_PROMPT_FIELDS.index("exact_quote")
    return {
        "schema_version": "e2r_v5_source_claim_prompt_projection_v2",
        "claim_count": len(ordered),
        "claim_roster_hash": _stable_hash(ordered),
        "claim_fields": list(_SOURCE_CLAIM_PROMPT_FIELDS),
        "claims": claims,
        "every_claim_id_and_exact_quote_preserved": all(
            str(row[claim_id_index] or "").strip()
            and str(row[exact_quote_index] or "").strip()
            for row in claims
        ),
        "fact_semantics_are_in_current_evidence_fact_graph": True,
        "canonical_urls_are_in_source_documents": True,
        "acceptance_and_materiality_state_accounted_by_claim_roster_hash": True,
        "full_claim_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def project_source_claim_profile(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Account for all accepted claims after their facts have been compiled.

    Later research passes reason over the complete citable fact table.  Replaying
    every claim id, document id, and exact quote beside the same fact narrative
    duplicates prompt text.  This profile preserves the source/date/role state
    of every claim and hashes every exact quote and lineage roster; full claim
    rows remain in ``material_fact_claims.jsonl`` for deterministic citation.
    """

    payloads = tuple(dict(row) for row in rows)
    projection = dict(
        _project_state_collection(
            payloads,
            collection_name="citable_source_claim_profile",
            identity_fields=("claim_id",),
            group_fields=(
                "source_family",
                "source_tier",
                "published_at",
                "available_at",
            ),
            relation_fields=(),
            group_relation_fields=("structured_evidence_roles",),
            numeric_fields=(),
        )
    )
    exact_quotes = tuple(str(row.get("exact_quote") or "") for row in payloads)
    projection.update(
        {
            "schema_version": "e2r_v5_citable_source_claim_profile_v1",
            "claim_id_roster": _project_text_roster(
                row.get("claim_id") for row in payloads
            ),
            "document_id_roster": _project_text_roster(
                row.get("document_id") for row in payloads
            ),
            "source_id_roster": _project_text_roster(
                source_id
                for row in payloads
                for source_id in row.get("source_ids") or ()
            ),
            "exact_quote_roster": _project_text_roster(exact_quotes),
            "exact_quote_character_count": sum(map(len, exact_quotes)),
            "every_exact_quote_accounted_by_count_and_hash": True,
            "exact_quote_text_persisted_outside_prompt": True,
            "fact_semantics_are_in_citable_evidence_fact_graph": True,
            "full_claim_records_persisted_outside_prompt": True,
            "fixed_top_n_used": False,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
        }
    )
    return projection


def project_research_source_claim_profile(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Compact all claim provenance after exact facts have been compiled."""

    payloads = tuple(dict(row) for row in rows)
    semantic_payloads = tuple(
        {
            field: row.get(field)
            for field in _SOURCE_CLAIM_PROMPT_FIELDS
            if field in row
        }
        for row in payloads
    )
    projection = dict(
        _project_state_collection(
            semantic_payloads,
            collection_name="research_source_claim_profile",
            identity_fields=("claim_id",),
            group_fields=(
                "source_family",
                "source_tier",
                "structured_evidence_roles",
            ),
            relation_fields=(),
            numeric_fields=(),
        )
    )
    exact_quotes = tuple(str(row.get("exact_quote") or "") for row in payloads)
    projection.update(
        {
            "schema_version": "e2r_v5_research_source_claim_profile_v2",
            "claim_id_roster": _project_text_roster(
                row.get("claim_id") for row in payloads
            ),
            "document_id_roster": _project_text_roster(
                row.get("document_id") for row in payloads
            ),
            "source_id_roster": _project_text_roster(
                source_id
                for row in payloads
                for source_id in row.get("source_ids") or ()
            ),
            "published_at_roster": _project_text_roster(
                row.get("published_at") for row in payloads
            ),
            "available_at_roster": _project_text_roster(
                row.get("available_at") for row in payloads
            ),
            "exact_quote_roster": _project_text_roster(exact_quotes),
            "exact_quote_character_count": sum(map(len, exact_quotes)),
            "every_exact_quote_accounted_by_count_and_hash": True,
            "fact_semantics_are_in_current_citable_fact_rows": True,
            "extraction_lineage_excluded_from_provider": True,
            "semantic_claim_fields": list(_SOURCE_CLAIM_PROMPT_FIELDS),
            "full_claim_records_persisted_outside_prompt": True,
            "fixed_top_n_used": False,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
        }
    )
    return projection


def project_source_document_profile(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Account for every source document without replaying body-free manifests."""

    payloads = tuple(dict(row) for row in rows)
    projection = dict(
        _project_state_collection(
            payloads,
            collection_name="citable_source_document_profile",
            identity_fields=("document_id",),
            group_fields=(
                "source_family",
                "source_provider",
                "published_at",
                "available_at",
                "content_type",
                "evidence_eligible",
            ),
            relation_fields=(),
            group_relation_fields=(),
            numeric_fields=(),
        )
    )
    projection.update(
        {
            "schema_version": "e2r_v5_citable_source_document_profile_v1",
            "document_id_roster": _project_text_roster(
                row.get("document_id") for row in payloads
            ),
            "canonical_url_roster": _project_text_roster(
                row.get("canonical_url") or row.get("url") for row in payloads
            ),
            "title_roster": _project_text_roster(
                row.get("title") for row in payloads
            ),
            "content_hash_roster": _project_text_roster(
                row.get("content_hash") for row in payloads
            ),
            "query_id_roster": _project_text_roster(
                query_id
                for row in payloads
                for query_id in row.get("query_ids") or ()
            ),
            "objective_id_roster": _project_text_roster(
                objective_id
                for row in payloads
                for objective_id in row.get("objective_ids") or ()
            ),
            "document_bodies_already_consumed_by_fact_extraction": True,
            "full_document_records_persisted_outside_prompt": True,
            "fixed_top_n_used": False,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
        }
    )
    return projection


def project_research_source_document_profile(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Compact all source provenance after document bodies were consumed."""

    payloads = tuple(dict(row) for row in rows)
    semantic_payloads = tuple(
        {
            field: row.get(field)
            for field in _DOCUMENT_MANIFEST_FIELDS
            if field in row
        }
        for row in payloads
    )
    projection = dict(
        _project_state_collection(
            semantic_payloads,
            collection_name="research_source_document_profile",
            identity_fields=("document_id",),
            group_fields=(
                "source_family",
                "source_provider",
                "content_type",
                "evidence_eligible",
            ),
            relation_fields=(),
            numeric_fields=(),
        )
    )
    projection.update(
        {
            "schema_version": "e2r_v5_research_source_document_profile_v2",
            "document_id_roster": _project_text_roster(
                row.get("document_id") for row in payloads
            ),
            "canonical_url_roster": _project_text_roster(
                row.get("canonical_url") or row.get("url") for row in payloads
            ),
            "title_roster": _project_text_roster(
                row.get("title") for row in payloads
            ),
            "content_hash_roster": _project_text_roster(
                row.get("content_hash") for row in payloads
            ),
            "published_at_roster": _project_text_roster(
                row.get("published_at") for row in payloads
            ),
            "available_at_roster": _project_text_roster(
                row.get("available_at") for row in payloads
            ),
            "document_bodies_already_consumed_by_fact_extraction": True,
            "acquisition_lineage_excluded_from_provider": True,
            "semantic_document_fields": list(_DOCUMENT_MANIFEST_FIELDS),
            "excluded_acquisition_lineage_fields": list(
                _DOCUMENT_RELATION_FIELDS
            ),
            "full_document_records_persisted_outside_prompt": True,
            "fixed_top_n_used": False,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
        }
    )
    return projection


def project_supervisor_failures(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Group equivalent failures for one LLM judgment, retaining every id.

    The provider classifies each semantic group exactly once.  The supervisor
    deterministically expands that judgment back to every member failure id
    before readiness checks, so grouping is neither a failure drop nor a
    completion shortcut.
    """

    payloads = tuple(dict(row) for row in rows)
    ordered = tuple(
        sorted(
            payloads,
            key=lambda row: (
                str(row.get("failure_id") or ""),
                _stable_hash(row),
            ),
        )
    )
    grouped: dict[tuple[Any, ...], list[Mapping[str, Any]]] = {}
    for row in ordered:
        key = tuple(
            _failure_group_value(field, row.get(field))
            for field in _FAILURE_GROUP_FIELDS
        )
        grouped.setdefault(key, []).append(row)
    failures = []
    failure_group_members: dict[str, list[str]] = {}
    for key in sorted(grouped, key=lambda value: tuple(map(str, value))):
        grouped_rows = grouped[key]
        state = {
            field: key[index]
            for index, field in enumerate(_FAILURE_GROUP_FIELDS)
            if key[index] not in {None, "", ()}
        }
        member_ids = sorted(
            str(row.get("failure_id") or "") for row in grouped_rows
        )
        group_id = "FAILGROUP-" + _stable_hash(
            {
                "state": state,
                "member_failure_ids": member_ids,
            }
        )[:24]
        failure_group_members[group_id] = member_ids
        failures.append(
            {
                "failure_id": group_id,
                **state,
                "member_failure_count": len(member_ids),
                "member_failure_ids": member_ids,
                "relation_coverage": {
                    field: _relation_coverage(grouped_rows, field)
                    for field in _FAILURE_RELATION_FIELDS
                },
                "member_failure_roster_hash": _stable_hash(grouped_rows),
            }
        )
    original_ids = {
        str(row.get("failure_id") or "") for row in ordered
    }
    projected_ids = {
        failure_id
        for member_ids in failure_group_members.values()
        for failure_id in member_ids
    }
    return {
        "schema_version": "e2r_v5_supervisor_failure_prompt_projection_v1",
        "failure_count": len(ordered),
        "failure_roster_hash": _stable_hash(ordered),
        "failure_group_count": len(failures),
        "failure_group_members": failure_group_members,
        "failures": failures,
        "every_failure_id_preserved": (
            original_ids == projected_ids and len(original_ids) == len(ordered)
        ),
        "provider_assesses_each_group_once_then_code_expands_to_members": True,
        "full_failure_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def _failure_group_value(field: str, value: Any) -> Any:
    """Collapse transport detail while preserving the class LLM must judge.

    Full failure rows and ids stay outside the prompt and are deterministically
    restored after the provider classifies each group.  Literal queries, URLs,
    dates, and response excerpts do not change whether a failure is a timeout,
    unreadable document, duplicate query, or another semantic failure class.
    """

    grouped = _group_value(value)
    if field not in {
        "failure_reason",
        "reason",
        "rejection_reason",
        "provider_error",
    } or not isinstance(grouped, str):
        return grouped
    text = " ".join(grouped.split())
    if not text:
        return text
    prefix = text.split(":", 1)[0].strip()
    if re.fullmatch(r"[A-Z][A-Z0-9_]+", prefix):
        return prefix
    if re.fullmatch(r"[A-Za-z][A-Za-z0-9_.]*(?:Error|Exception)", prefix):
        return prefix
    folded = text.casefold()
    if "30x" in folded or "redirect" in folded or "object moved" in folded:
        return "HTTP_REDIRECT_FAILURE"
    return text


def project_query_planner_failures(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Give the query LLM every semantic failure without transport-wait churn.

    ``COLLABORATION_RESPONSE_PENDING`` is the asynchronous bridge's control
    signal: the same prompt is waiting for a Codex subagent response.  It is
    persisted in the Source Graph checkpoint, but it is not a new search,
    source, parser, or provider failure.  Replaying its request id into the
    next prompt would change that prompt and make the awaited response
    impossible to consume.
    """

    input_rows = tuple(dict(raw) for raw in rows)
    semantic_rows = tuple(
        projected
        for raw in input_rows
        if (
            projected := _project_failure_without_collaboration_transport_wait(
                raw
            )
        )
        is not None
    )
    ordered_inputs = sorted(
        semantic_rows,
        key=lambda row: (
            str(row.get("failure_id") or ""),
            _stable_hash(row),
        ),
    )
    normalized = []
    identity_occurrences: dict[str, int] = {}
    for raw in ordered_inputs:
        row = dict(raw)
        existing_id = str(row.get("failure_id") or "").strip()
        identity_base = existing_id or "QUERYFAIL-" + _stable_hash(row)[:24]
        occurrence = identity_occurrences.get(identity_base, 0)
        identity_occurrences[identity_base] = occurrence + 1
        row["failure_id"] = (
            identity_base if occurrence == 0 else f"{identity_base}-{occurrence}"
        )
        normalized.append(row)
    full_projection = project_supervisor_failures(normalized)
    failures = []
    for raw in full_projection.get("failures") or ():
        row = dict(raw)
        member_ids = tuple(str(value) for value in row.pop("member_failure_ids", ()))
        relations = dict(row.pop("relation_coverage", {}) or {})
        visible_relations = {
            key: value
            for key, value in relations.items()
            if key in {"objective_id", "objective_ids", "query_id"}
        }
        row["relation_coverage"] = visible_relations
        row["omitted_relation_coverage_hash"] = _stable_hash(
            {
                key: value
                for key, value in relations.items()
                if key not in visible_relations
            }
        )
        row["member_failure_count"] = int(
            row.get("member_failure_count") or len(member_ids)
        )
        row["member_failure_roster_hash"] = str(
            row.get("member_failure_roster_hash")
            or _stable_hash(member_ids)
        )
        failures.append(row)
    return {
        "schema_version": "e2r_v5_query_planner_failure_projection_v2",
        "failure_count": full_projection["failure_count"],
        "failure_group_count": full_projection["failure_group_count"],
        "failure_roster_hash": full_projection["failure_roster_hash"],
        "failure_group_member_mapping_hash": _stable_hash(
            full_projection.get("failure_group_members") or {}
        ),
        "failures": failures,
        "every_semantic_failure_accounted_by_group_count_and_hash": (
            sum(int(row["member_failure_count"]) for row in failures)
            == len(normalized)
        ),
        "full_failure_records_persisted_in_source_graph_checkpoint": True,
        "collaboration_transport_waits_excluded_from_semantic_prompt": True,
        "collaboration_transport_waits_persisted_in_source_graph_checkpoint": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def _is_collaboration_transport_wait(value: Any) -> bool:
    return bool(
        _COLLABORATION_TRANSPORT_WAIT_RE.fullmatch(
            str(value or "").strip()
        )
    )


def normalize_collaboration_transport_wait(value: Any) -> str:
    """Keep a transport-wait class stable while removing its request nonce."""

    text = " ".join(str(value or "").split())
    if not _is_collaboration_transport_wait(text):
        return text
    return _COLLABORATION_TRANSPORT_WAIT_REQUEST_ID_RE.sub(
        "COLLABREQ-<REQUEST_ID>",
        text,
    )


def _is_fact_transport_progress_feedback(value: Any) -> bool:
    """Identify only canonical fact checkpoint progress rows."""

    text = str(value or "").strip()
    if text == _FACT_CANONICAL_STATE_REFRESH_FEEDBACK:
        return True
    match = _FACT_TRANSPORT_PROGRESS_FEEDBACK_RE.fullmatch(text)
    return bool(
        match
        and int(match.group(1)) < int(match.group(2))
    )


def _project_failure_without_collaboration_transport_wait(
    row: Mapping[str, Any],
) -> Mapping[str, Any] | None:
    output = dict(row)
    reason_fields = (
        "failure_reason",
        "reason",
        "rejection_reason",
        "provider_error",
    )
    wait_fields = tuple(
        field
        for field in reason_fields
        if _is_collaboration_transport_wait(output.get(field))
    )
    if not wait_fields:
        return output
    for field in wait_fields:
        output.pop(field, None)
    if any(str(output.get(field) or "").strip() for field in reason_fields):
        return output
    return None


def _project_without_collaboration_transport_waits(value: Any) -> Any:
    if isinstance(value, str):
        if _is_collaboration_transport_wait(value):
            return _DROP_COLLABORATION_TRANSPORT_WAIT
        return value
    if isinstance(value, Mapping):
        output = {}
        for key, raw in value.items():
            projected = _project_without_collaboration_transport_waits(raw)
            if projected is not _DROP_COLLABORATION_TRANSPORT_WAIT:
                output[key] = projected
        return output
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return [
            projected
            for raw in value
            if (
                projected := _project_without_collaboration_transport_waits(
                    raw
                )
            )
            is not _DROP_COLLABORATION_TRANSPORT_WAIT
        ]
    return value


def _project_gap_reason_roster(
    reasons: Sequence[str],
    *,
    field_name: str,
) -> Mapping[str, Any]:
    """Account for a repeated run-state reason ledger without replaying it."""

    ordered = tuple(
        sorted(
            str(value)
            for value in reasons
            if not _is_collaboration_transport_wait(value)
        )
    )
    kind_rows = tuple(
        {
            "kind": (
                value.split(":", 1)[0].strip()
                if ":" in value
                else value.strip()
                if value.strip()
                else "UNCLASSIFIED"
            )
        }
        for value in ordered
    )
    return {
        "schema_version": "e2r_v5_gap_reason_roster_projection_v2",
        "field_name": field_name,
        "reason_count": len(ordered),
        "unique_reason_count": len(set(ordered)),
        "reason_roster_hash": _stable_hash(ordered),
        "reason_kind_coverage": _relation_coverage(kind_rows, "kind"),
        "every_reason_accounted_by_hash_and_kind_count": (
            sum(_relation_coverage(kind_rows, "kind").values()) == len(ordered)
        ),
        "full_reason_records_persisted_outside_prompt": True,
        "collaboration_transport_waits_excluded_from_semantic_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def project_query_score_gap_context(
    context: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Remove duplicate ledgers while preserving LLM-authored gap semantics."""

    output = dict(
        _project_without_collaboration_transport_waits(dict(context))
    )
    for field in ("source_graph_pending_reasons",):
        reasons = output.get(field)
        if isinstance(reasons, Sequence) and not isinstance(reasons, (str, bytes)):
            reason_rows = tuple(str(value) for value in reasons)
            output[field] = _project_gap_reason_roster(
                reason_rows,
                field_name=field,
            )
    feedback = output.get("prior_fact_extraction_feedback")
    if isinstance(feedback, Sequence) and not isinstance(feedback, (str, bytes)):
        feedback_rows = tuple(
            str(value)
            for value in feedback
            if not _is_collaboration_transport_wait(value)
            and not _is_fact_transport_progress_feedback(value)
        )
        output["prior_fact_extraction_feedback"] = {
            "schema_version": "e2r_v5_fact_gap_feedback_projection_v3",
            "feedback_count": len(feedback_rows),
            "feedback_roster_hash": _stable_hash(feedback_rows),
            "feedback_kind_coverage": _relation_coverage(
                (
                    {
                        "kind": value.split(":", 1)[0]
                        if ":" in value
                        else "UNCLASSIFIED"
                    }
                    for value in feedback_rows
                ),
                "kind",
            ),
            "supervisor_missing_facts_and_questions_remain_verbatim": True,
            "full_feedback_records_persisted_outside_prompt": True,
            "collaboration_transport_waits_excluded_from_semantic_prompt": True,
            "fact_transport_progress_excluded_from_semantic_prompt": True,
            "fact_transport_progress_persisted_in_fact_checkpoint": True,
            "fixed_top_n_used": False,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
        }
    supervisor = output.get("prior_supervisor_gap")
    if isinstance(supervisor, Mapping):
        projected_supervisor = dict(supervisor)
        projected_supervisor.pop("review_id", None)
        projected_supervisor.pop("supervisor_review_id", None)
        projected_supervisor.pop("epoch", None)
        failure_assessments = projected_supervisor.pop(
            "failure_assessments", ()
        )
        if isinstance(failure_assessments, Sequence) and not isinstance(
            failure_assessments, (str, bytes)
        ):
            projected_supervisor["failure_assessment_projection"] = (
                project_query_planner_failures(failure_assessments)
            )
        parser_failures = projected_supervisor.pop(
            "parser_or_extractor_failures", ()
        )
        if isinstance(parser_failures, Sequence) and not isinstance(
            parser_failures, (str, bytes)
        ):
            projected_supervisor["parser_or_extractor_failure_roster"] = (
                _project_text_roster(parser_failures)
            )
        output["prior_supervisor_gap"] = projected_supervisor
    prior_epoch = output.get("prior_research_epoch")
    if isinstance(prior_epoch, Mapping):
        projected_epoch = dict(prior_epoch)
        projected_epoch.pop("checkpoint_id", None)
        projected_epoch.pop("epoch", None)
        output["prior_research_epoch"] = projected_epoch
    semantic_context_hash = _stable_hash(output)
    return {
        **output,
        "query_score_gap_projection_audit": {
            "schema_version": "e2r_v5_query_score_gap_projection_v3",
            "semantic_context_roster_hash": semantic_context_hash,
            "checkpoint_lineage_excluded_from_provider": True,
            "excluded_checkpoint_lineage_fields": [
                "prior_research_epoch.checkpoint_id",
                "prior_research_epoch.epoch",
                "prior_supervisor_gap.review_id",
                "prior_supervisor_gap.supervisor_review_id",
                "prior_supervisor_gap.epoch",
            ],
            "llm_authored_missing_facts_questions_and_directions_preserved": True,
            "duplicate_failure_ledgers_projected": True,
            "collaboration_transport_waits_excluded_from_semantic_prompt": True,
            "full_gap_context_persisted_outside_prompt": True,
            "fixed_top_n_used": False,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
        },
    }


def project_fact_extraction_score_gap_context(
    context: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Project persisted gap ledgers before replaying them for each new document.

    The query planner and fact extractor need the same unresolved semantic facts,
    questions, and route failures.  The extractor must not, however, repeat the
    full append-only failure ledger beside every full document.  Reusing the
    loss-accounted query projection keeps those semantics while the original
    rows remain in their checkpoint artifacts.
    """

    projected = dict(project_query_score_gap_context(context))
    query_audit = dict(
        projected.pop("query_score_gap_projection_audit", {}) or {}
    )
    # Source acquisition status and its pending-reason ledger describe queue
    # transport, not the economic meaning of a fetched document.  Replaying
    # those fields into fact extraction makes an otherwise identical document,
    # objective roster, and fact state produce a different collaboration
    # request whenever Source Graph advances from query to ranking or fetch.
    # Keep the full values in the source checkpoint and make fact request
    # identity depend only on the semantic gap context.
    projected.pop("source_graph_status", None)
    projected.pop("source_graph_pending_reasons", None)
    prior_structured_source_gap = projected.get(
        "prior_structured_source_gap"
    )
    if isinstance(prior_structured_source_gap, Mapping):
        semantic_structured_gap = dict(prior_structured_source_gap)
        # These counts describe how many already-persisted claims/facts the
        # materializer replayed.  Split-document checkpoint reconciliation can
        # legitimately change them without changing the current fact roster or
        # any missing structured role.  Keep the semantic gap fields and the
        # full accounting in its own artifact, but do not let the bookkeeping
        # totals mint a new exact fact-extraction request.
        semantic_structured_gap.pop("issuer_fact_materialization", None)
        projected["prior_structured_source_gap"] = semantic_structured_gap
    return {
        **projected,
        "fact_extraction_score_gap_projection_audit": {
            "schema_version": "e2r_v5_fact_extraction_score_gap_projection_v3",
            "semantic_context_roster_hash": _stable_hash(projected),
            "shared_gap_projection_schema_version": query_audit.get(
                "schema_version"
            ),
            "source_transport_state_excluded_from_fact_identity": True,
            "excluded_source_transport_fields": [
                "source_graph_status",
                "source_graph_pending_reasons",
                (
                    "prior_structured_source_gap."
                    "issuer_fact_materialization"
                ),
            ],
            "llm_authored_missing_facts_questions_and_directions_preserved": True,
            "duplicate_failure_ledgers_projected": True,
            "full_gap_context_persisted_outside_prompt": True,
            "fixed_top_n_used": False,
            "prompt_projection_is_research_cap": False,
            "score_authority": False,
        },
    }


def project_counter_route_proof(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Summarize all verified counter-query routes already present in the ledger."""

    return _project_state_collection(
        rows,
        collection_name="counter_and_supersession_route_proof",
        identity_fields=("objective_id", "route_kind"),
        group_fields=(
            "route_kind",
            "parser_extractor_verified",
            "zero_result_only",
        ),
        relation_fields=("objective_id",),
        numeric_fields=(),
        hashed_group_relation_fields=(
            "query_ids",
            "document_ids",
            "fact_ids",
        ),
    )


def project_research_epoch_checkpoint(
    checkpoint: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Bind saturation to one epoch while accounting for every persisted row.

    The complete checkpoint contains the expanded Supervisor review, prior
    saturation attempts, and large opaque id rosters.  Saturation receives the
    current Supervisor semantics and all-fact projection separately, so this
    transport view keeps current identity fields and replaces every repeated
    collection with an exact count and full-roster hash.  Nothing is sampled.
    """

    output = {
        key: checkpoint.get(key)
        for key in (
            "schema_version",
            "checkpoint_id",
            "checkpoint_hash",
            "target_id",
            "as_of_date",
            "epoch",
            "status",
            "resumed_from_checkpoint_id",
            "source_graph_checkpoint_id",
            "component_memo_hashes",
            "semantic_saturation_certified",
            "completion_based_on_fixed_rounds",
            "zero_search_result_treated_as_saturation",
            "transport_budget_treated_as_completion",
            "production_score_authority",
            "unresolved_material_questions",
            "next_actions",
        )
        if key in checkpoint
    }
    for key in (
        "cumulative_query_ids",
        "cumulative_document_ids",
        "cumulative_fact_ids",
        "current_fact_ids",
        "retired_fact_ids",
        "queries",
        "documents",
        "new_facts",
        "retired_facts",
        "changed_component_memos",
    ):
        rows = tuple(checkpoint.get(key) or ())
        output[key] = _full_collection_roster_projection(
            rows,
            collection_name=f"research_epoch_{key}",
        )
    for key in (
        "supervisor_review",
        "saturation_reviews",
        "saturation_certificate",
    ):
        value = checkpoint.get(key)
        rows = (
            tuple(value or ())
            if isinstance(value, (list, tuple))
            else (() if value is None else (value,))
        )
        output[key] = _full_collection_roster_projection(
            rows,
            collection_name=f"research_epoch_{key}",
        )
    # Production reviewers may know only that Gold is a private post-run lane.
    output["gold_evaluation_status"] = "NOT_RUN_POST_RUN_ONLY"
    output["full_checkpoint_payload_hash"] = _stable_hash(checkpoint)
    output["research_epoch_prompt_projection"] = {
        "schema_version": "e2r_v5_research_epoch_prompt_projection_v2",
        "complete_checkpoint_persisted_outside_prompt": True,
        "every_id_roster_delta_and_nested_review_hash_accounted": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }
    return output


def _full_collection_roster_projection(
    rows: Sequence[Any],
    *,
    collection_name: str,
) -> Mapping[str, Any]:
    payloads = tuple(rows)
    return {
        "schema_version": "e2r_v5_full_collection_roster_projection_v1",
        "collection_name": collection_name,
        "record_count": len(payloads),
        "full_roster_hash": _stable_hash(payloads),
        "every_record_accounted_by_exact_count_and_full_hash": True,
        "full_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def project_structured_records(
    records: Sequence[Any],
) -> Mapping[str, Any]:
    """Summarize all rows by semantic series and hash the complete roster."""

    payloads = tuple(_record_dict(row) for row in records)
    ordered = tuple(
        sorted(payloads, key=lambda row: str(row.get("record_id") or ""))
    )
    metadata_projection = _structured_metadata_projection(ordered)
    groups: dict[tuple[Any, ...], list[Mapping[str, Any]]] = {}
    for row in ordered:
        key = (
            str(row.get("metric_id") or ""),
            str(row.get("unit") or ""),
            str(row.get("dataset") or ""),
            str(row.get("record_kind") or ""),
            str(row.get("source_route") or ""),
            tuple(sorted(str(value) for value in row.get("evidence_roles") or ())),
        )
        groups.setdefault(key, []).append(row)
    summaries = []
    for key in sorted(groups, key=lambda value: tuple(map(str, value))):
        rows = groups[key]
        chronological = sorted(
            rows,
            key=lambda row: (
                str(row.get("available_at") or row.get("observed_at") or ""),
                str(row.get("observed_at") or ""),
                str(row.get("period") or ""),
                str(row.get("record_id") or ""),
            ),
        )
        numeric_values = [
            float(row["value"])
            for row in rows
            if _finite_number(row.get("value"))
        ]
        text_counts: dict[str, int] = {}
        for row in rows:
            if _finite_number(row.get("value")):
                continue
            text = str(row.get("value"))
            text_counts[text] = text_counts.get(text, 0) + 1
        summary: dict[str, Any] = {
            "metric_id": key[0],
            "unit": key[1],
            "dataset": key[2],
            "record_kind": key[3],
            "source_route": key[4],
            "evidence_roles": list(key[5]),
            "record_count": len(rows),
            "record_roster_hash": _stable_hash(rows),
            "source_id_roster": _project_text_roster(
                source_id
                for row in rows
                for source_id in row.get("source_ids") or ()
            ),
            "earliest_record": _record_snapshot(chronological[0]),
        }
        if chronological[-1] == chronological[0]:
            summary["latest_record_same_as_earliest"] = True
        else:
            summary["latest_record"] = _record_snapshot(chronological[-1])
        if numeric_values:
            summary["numeric_distribution"] = {
                "count": len(numeric_values),
                "minimum": min(numeric_values),
                "median": median(numeric_values),
                "maximum": max(numeric_values),
            }
        if text_counts:
            categorical_observations = tuple(
                value
                for value, count in sorted(text_counts.items())
                for _ in range(count)
            )
            summary["categorical_value_projection"] = {
                "observation_count": len(categorical_observations),
                "distinct_value_roster": _project_text_roster(
                    text_counts.keys()
                ),
                "observation_roster_hash": _stable_hash(
                    categorical_observations
                ),
                "full_categorical_values_persisted_outside_prompt": True,
            }
        summaries.append(summary)
    return {
        "schema_version": "e2r_v5_structured_prompt_projection_v2",
        "record_count": len(ordered),
        "record_roster_hash": _stable_hash(ordered),
        "semantic_series_count": len(summaries),
        "semantic_series": summaries,
        "metadata_projection": metadata_projection,
        "every_record_accounted_by_hash_and_series_count": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def project_structured_result(result: Any | None) -> Mapping[str, Any] | None:
    if result is None:
        return None
    method = getattr(result, "to_prompt_projection", None)
    if callable(method):
        return method()
    payload = result.to_dict() if hasattr(result, "to_dict") else dict(result)
    records = tuple(getattr(result, "records", ()) or payload.get("records") or ())
    if not records:
        return payload
    output = {
        key: value
        for key, value in payload.items()
        if key not in {"records"}
    }
    projection = project_structured_records(records)
    output["record_projection"] = projection
    output["records"] = [
        {
            "transport_projection": True,
            "record_count": projection["record_count"],
            "record_roster_hash": projection["record_roster_hash"],
            "full_records_persisted_outside_prompt": True,
        }
    ]
    return output


def _record_dict(value: Any) -> Mapping[str, Any]:
    return value.to_dict() if hasattr(value, "to_dict") else dict(value)


def _record_snapshot(row: Mapping[str, Any]) -> Mapping[str, Any]:
    fields = (
        "value",
        "period",
        "observed_at",
        "available_at",
        "confidence",
        "provenance",
    )
    output = {key: row[key] for key in fields if key in row}
    if row.get("input_record_ids"):
        output["input_record_id_roster"] = _project_text_roster(
            row.get("input_record_ids") or ()
        )
    return output


def _structured_metadata_projection(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Hash-account all structured metadata once per record collection.

    Structured metadata often contains a second copy of connector responses,
    peer tables, or derivation diagnostics.  The canonical record keeps that
    payload.  A later supervisor needs proof that every metadata payload was
    preserved, plus the aggregate field/type shape; it does not need the same
    payload repeated in both endpoint snapshots for every semantic series.
    """

    metadata_rows = tuple(
        row.get("metadata") for row in rows if "metadata" in row
    )
    type_counts: dict[str, int] = {}
    field_names = []
    boolean_states = []
    for metadata in metadata_rows:
        if not isinstance(metadata, Mapping):
            type_name = type(metadata).__name__
            type_counts[type_name] = type_counts.get(type_name, 0) + 1
            continue
        for key, item in metadata.items():
            field_names.append(str(key))
            type_name = type(item).__name__
            type_counts[type_name] = type_counts.get(type_name, 0) + 1
            if isinstance(item, bool):
                boolean_states.append((str(key), item))
    return {
        "metadata_record_count": len(metadata_rows),
        "metadata_roster_hash": _stable_hash(metadata_rows),
        "metadata_field_observation_count": len(field_names),
        "metadata_distinct_field_count": len(set(field_names)),
        "metadata_field_roster_hash": _stable_hash(
            tuple(sorted(field_names))
        ),
        "metadata_value_type_counts": dict(sorted(type_counts.items())),
        "metadata_boolean_field_count": len(boolean_states),
        "metadata_boolean_state_hash": _stable_hash(
            tuple(sorted(boolean_states))
        ),
        "full_metadata_persisted_outside_prompt": True,
    }


def _project_text_roster(values: Sequence[Any] | Any) -> Mapping[str, Any]:
    if isinstance(values, (str, bytes)):
        raw_values = (values,)
    else:
        try:
            raw_values = tuple(values)
        except TypeError:
            raw_values = (values,)
    ordered = tuple(
        sorted({str(value) for value in raw_values if str(value)})
    )
    return {
        "count": len(ordered),
        "roster_hash": _stable_hash(ordered),
    }


def _project_state_collection(
    rows: Sequence[Mapping[str, Any]],
    *,
    collection_name: str,
    identity_fields: Sequence[str],
    group_fields: Sequence[str],
    relation_fields: Sequence[str],
    numeric_fields: Sequence[str],
    group_relation_fields: Sequence[str] = (),
    hashed_group_relation_fields: Sequence[str] = (),
) -> Mapping[str, Any]:
    """Account for every state row through deterministic groups and hashes.

    Candidate and fetch ledgers can grow without bound across resumed research
    epochs.  Their full rows remain in the Source Graph checkpoint.  Later LLM
    passes need semantic state coverage and failure context, not thousands of
    repeated snippets and URLs.  This projection therefore groups *all* rows;
    it never selects a top-N subset.
    """

    payloads = tuple(dict(row) for row in rows)
    ordered = tuple(
        sorted(
            payloads,
            key=lambda row: (
                tuple(str(row.get(key) or "") for key in identity_fields),
                _stable_hash(row),
            ),
        )
    )
    groups: dict[tuple[Any, ...], list[Mapping[str, Any]]] = {}
    for row in ordered:
        key = tuple(_group_value(row.get(field)) for field in group_fields)
        groups.setdefault(key, []).append(row)

    semantic_groups = []
    for key in sorted(groups, key=lambda value: tuple(map(str, value))):
        grouped_rows = groups[key]
        state = {
            field: key[index] for index, field in enumerate(group_fields)
        }
        numeric_distributions = {}
        for field in numeric_fields:
            values = [
                float(row[field])
                for row in grouped_rows
                if _finite_number(row.get(field))
            ]
            if values:
                numeric_distributions[field] = {
                    "count": len(values),
                    "minimum": min(values),
                    "median": median(values),
                    "maximum": max(values),
                }
        semantic_group = {
            "state": state,
            "record_count": len(grouped_rows),
            "record_roster_hash": _stable_hash(grouped_rows),
            "numeric_distributions": numeric_distributions,
        }
        if set(group_relation_fields) & set(hashed_group_relation_fields):
            raise ValueError(
                "group relation fields cannot be both expanded and hash-accounted"
            )
        if group_relation_fields or hashed_group_relation_fields:
            relation_coverage = {
                field: _relation_coverage(grouped_rows, field)
                for field in group_relation_fields
            }
            relation_coverage.update(
                {
                    field: _relation_roster_projection(grouped_rows, field)
                    for field in hashed_group_relation_fields
                }
            )
            semantic_group["relation_coverage"] = relation_coverage
        semantic_groups.append(semantic_group)

    relation_coverage = {
        field: _relation_coverage(ordered, field) for field in relation_fields
    }
    return {
        "schema_version": "e2r_v5_source_graph_collection_projection_v2",
        "collection_name": collection_name,
        "record_count": len(ordered),
        "record_roster_hash": _stable_hash(ordered),
        "semantic_group_count": len(semantic_groups),
        "semantic_groups": semantic_groups,
        "relation_coverage": relation_coverage,
        "every_record_accounted_by_hash_and_group_count": (
            sum(row["record_count"] for row in semantic_groups) == len(ordered)
        ),
        "full_records_persisted_outside_prompt": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }


def _relation_coverage(
    rows: Sequence[Mapping[str, Any]], field: str
) -> Mapping[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        value = row.get(field)
        values = value if isinstance(value, (list, tuple, set)) else (value,)
        for item in values:
            text = str(item or "").strip()
            if text:
                counts[text] = counts.get(text, 0) + 1
    return dict(sorted(counts.items()))


def _relation_roster_projection(
    rows: Sequence[Mapping[str, Any]], field: str
) -> Mapping[str, Any]:
    """Account for every relation value with counts and stable roster hashes."""

    observations = []
    for row in rows:
        value = row.get(field)
        values = value if isinstance(value, (list, tuple, set)) else (value,)
        observations.extend(
            str(item).strip() for item in values if str(item or "").strip()
        )
    ordered = tuple(sorted(observations))
    distinct = tuple(sorted(set(ordered)))
    return {
        "observation_count": len(ordered),
        "distinct_value_count": len(distinct),
        "distinct_value_roster_hash": _stable_hash(distinct),
        "observation_roster_hash": _stable_hash(ordered),
        "full_relation_values_persisted_outside_prompt": True,
    }


def _group_value(value: Any) -> Any:
    if isinstance(value, Mapping):
        return _stable_hash(value)
    if isinstance(value, (list, tuple, set)):
        return tuple(sorted(str(item) for item in value))
    return value


def _finite_number(value: Any) -> bool:
    return (
        not isinstance(value, bool)
        and isinstance(value, (int, float))
        and math.isfinite(float(value))
    )


def _stable_hash(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


__all__ = [
    "citable_fact_id_by_row_index",
    "project_candidate_ranking_evidence_context",
    "project_claim_fact_link_profile",
    "project_counter_route_proof",
    "project_citable_evidence_facts",
    "project_current_decision_citable_facts",
    "project_evidence_facts",
    "project_fact_extraction_evidence_context",
    "project_fact_extraction_score_gap_context",
    "project_generated_queries",
    "project_peer_selection_context",
    "project_query_planner_failures",
    "project_query_score_gap_context",
    "project_research_epoch_checkpoint",
    "project_source_documents",
    "project_source_graph_checkpoint",
    "project_source_claims",
    "project_source_claim_profile",
    "project_research_source_claim_profile",
    "project_research_source_document_profile",
    "project_source_document_profile",
    "project_source_document_table",
    "project_stage_gate_citable_facts",
    "project_structured_records",
    "project_structured_result",
    "project_supervisor_evidence_facts",
    "project_supervisor_failures",
    "project_supervisor_source_graph_checkpoint",
    "resolve_citable_fact_row_indices",
]
