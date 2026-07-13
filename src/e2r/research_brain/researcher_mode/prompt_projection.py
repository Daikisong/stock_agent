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

    output = {
        key: checkpoint.get(key)
        for key in (
            "checkpoint_id",
            "epoch",
            "quarantined_documents",
            "resolved_objective_ids",
            "transport_budget_can_complete_research",
            "semantic_saturation_certified",
        )
        if key in checkpoint
    }
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
    document_projection = dict(
        _project_state_collection(
            documents,
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
            relation_fields=(
                "objective_ids",
                "query_ids",
                "source_independence_group",
                "published_at",
            ),
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
            "verified_official_discovery_url_roster": _project_text_roster(
                value
                for row in documents
                for value in row.get("verified_official_discovery_urls") or ()
            ),
            "full_document_bodies_omitted_after_fact_extraction": True,
        }
    )
    output["evidence_documents"] = document_projection
    output["source_graph_prompt_projection"] = {
        "schema_version": "e2r_v5_supervisor_source_graph_projection_v1",
        "complete_artifact_persisted_outside_prompt": True,
        "every_query_document_and_state_row_accounted": True,
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


def project_supervisor_evidence_facts(
    rows: Sequence[Mapping[str, Any]],
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
                "predicate",
                "structured_evidence_roles",
                "allowed_component_ids",
                "source_independence_group",
                "corroborating_independence_groups",
            ),
            numeric_fields=("confidence",),
        )
    )
    projection.update(
        {
            "schema_version": "e2r_v5_supervisor_fact_prompt_projection_v1",
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
    fact_profile = dict(
        _project_state_collection(
            facts,
            collection_name="peer_selection_evidence_facts",
            identity_fields=("fact_id",),
            group_fields=_PEER_FACT_GROUP_FIELDS,
            relation_fields=(),
            group_relation_fields=(
                "predicate",
                "structured_evidence_roles",
                "source_independence_group",
            ),
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
            claims,
            collection_name="peer_selection_source_claims",
            identity_fields=("claim_id",),
            group_fields=_PEER_CLAIM_GROUP_FIELDS,
            relation_fields=(),
            group_relation_fields=("predicate",),
            numeric_fields=(),
        )
    )
    claim_profile.update(
        {
            "subject_roster": _project_text_roster(
                row.get("subject") for row in claims
            ),
            "economic_mechanism_roster": _project_text_roster(
                row.get("economic_mechanism") for row in claims
            ),
            "exact_quote_roster": _project_text_roster(
                row.get("exact_quote") for row in claims
            ),
            "claim_id_roster": _project_text_roster(
                row.get("claim_id") for row in claims
            ),
        }
    )
    return {
        "schema_version": "e2r_v5_peer_selection_context_projection_v1",
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


def citable_fact_id_by_row_index(
    projection: Mapping[str, Any],
) -> Mapping[int, str]:
    """Recover exact fact ids from the provider-facing row table."""

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
        key = tuple(_group_value(row.get(field)) for field in _FAILURE_GROUP_FIELDS)
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


def project_counter_route_proof(
    rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    """Summarize all verified counter-query routes already present in the ledger."""

    return _project_state_collection(
        rows,
        collection_name="counter_and_supersession_route_proof",
        identity_fields=("query_id",),
        group_fields=(
            "execution_status",
            "counter_or_supersession_search",
        ),
        relation_fields=("objective_id", "source_families", "query_id"),
        numeric_fields=("search_result_count",),
    )


def project_research_epoch_checkpoint(
    checkpoint: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Remove repeated document bodies from an already-persisted epoch delta."""

    output = dict(checkpoint)
    if "documents" in output:
        documents = tuple(output.get("documents") or ())
        output["documents"] = list(project_source_documents(documents))
        output["document_delta_count"] = len(documents)
        output["document_delta_manifest_hash"] = _stable_hash(documents)
        output["full_document_bodies_omitted_after_fact_extraction"] = True
    output["research_epoch_prompt_projection"] = {
        "schema_version": "e2r_v5_research_epoch_prompt_projection_v1",
        "complete_checkpoint_persisted_outside_prompt": True,
        "document_delta_hash_accounted": True,
        "fixed_top_n_used": False,
        "prompt_projection_is_research_cap": False,
        "score_authority": False,
    }
    return output


def project_structured_records(
    records: Sequence[Any],
) -> Mapping[str, Any]:
    """Summarize all rows by semantic series and hash the complete roster."""

    payloads = tuple(_record_dict(row) for row in records)
    ordered = tuple(
        sorted(payloads, key=lambda row: str(row.get("record_id") or ""))
    )
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
            summary["categorical_value_counts"] = dict(sorted(text_counts.items()))
        summaries.append(summary)
    return {
        "schema_version": "e2r_v5_structured_prompt_projection_v1",
        "record_count": len(ordered),
        "record_roster_hash": _stable_hash(ordered),
        "semantic_series_count": len(summaries),
        "semantic_series": summaries,
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
        "record_id",
        "value",
        "period",
        "observed_at",
        "available_at",
        "confidence",
        "provenance",
        "metadata",
    )
    output = {key: row[key] for key in fields if key in row}
    if row.get("input_record_ids"):
        output["input_record_id_roster"] = _project_text_roster(
            row.get("input_record_ids") or ()
        )
    return output


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
        if group_relation_fields:
            semantic_group["relation_coverage"] = {
                field: _relation_coverage(grouped_rows, field)
                for field in group_relation_fields
            }
        semantic_groups.append(semantic_group)

    relation_coverage = {
        field: _relation_coverage(ordered, field) for field in relation_fields
    }
    return {
        "schema_version": "e2r_v5_source_graph_collection_projection_v1",
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
    "project_counter_route_proof",
    "project_citable_evidence_facts",
    "project_evidence_facts",
    "project_generated_queries",
    "project_peer_selection_context",
    "project_research_epoch_checkpoint",
    "project_source_documents",
    "project_source_graph_checkpoint",
    "project_source_claims",
    "project_source_claim_profile",
    "project_source_document_profile",
    "project_source_document_table",
    "project_structured_records",
    "project_structured_result",
    "project_supervisor_evidence_facts",
    "project_supervisor_failures",
    "project_supervisor_source_graph_checkpoint",
    "resolve_citable_fact_row_indices",
]
