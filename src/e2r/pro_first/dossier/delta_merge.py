"""Append-only merge of same-conversation ResearchDossierV2/V3 deltas."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from ..ids import canonical_hash
from .validator import DossierValidationContext, ResearchDossierValidator
from .v2 import compile_dossier_v2_closure_summary
from .v3 import v3_atomic_fact_identity


class DossierDeltaMergeError(ValueError):
    """A follow-up attempted to rewrite accepted dossier history or scope."""


@dataclass(frozen=True)
class DossierDeltaMergeResult:
    effective_dossier: Mapping[str, Any]
    original_hash: str
    response_hash: str
    effective_hash: str
    new_fact_ids: tuple[str, ...]
    new_source_lineage_ids: tuple[str, ...]
    new_route_receipt_ids: tuple[str, ...]
    updated_question_family_ids: tuple[str, ...]


def apply_research_dossier_delta(
    *,
    original_dossier: Mapping[str, Any],
    response_dossier: Mapping[str, Any],
    validation_context: DossierValidationContext,
) -> DossierDeltaMergeResult:
    """Accept cumulative or delta-shaped V2/V3 responses under one strict rule.

    Existing fact/lineage/route/pass rows are immutable.  A follow-up may add
    rows and may advance its question closure row, but it cannot delete prior
    fact/route links.  The resulting full ledger is then validated as ordinary
    ResearchDossierV2/V3 before it can reach verification or saturation.
    """

    _validate_scope_identity(original_dossier, response_dossier, validation_context)
    schema_version = str(original_dossier.get("schema_version") or "")
    response = deepcopy(dict(response_dossier))
    if schema_version == "e2r_pro_research_dossier_v3":
        response = _coalesce_prior_v3_source_document_duplicates(
            original_dossier,
            response,
        )
        response = _coalesce_prior_v3_atomic_fact_duplicates(
            original_dossier,
            response,
        )
    effective = deepcopy(dict(original_dossier))
    new_fact_ids: list[str] = []
    for collection in ("material_facts", "counterfacts", "resolution_facts"):
        new_fact_ids.extend(
            _append_immutable_rows(
                effective,
                response,
                collection=collection,
                id_key="dossier_fact_id",
                required_new_pass_id=validation_context.research_pass_id,
            )
        )
    new_source_document_ids: tuple[str, ...] = ()
    if schema_version == "e2r_pro_research_dossier_v3":
        new_source_document_ids = _append_immutable_rows(
            effective,
            response,
            collection="source_documents",
            id_key="source_document_id",
        )
    new_lineages = _merge_source_lineages(
        effective,
        response,
        schema_version=schema_version,
    )
    new_routes = _append_immutable_rows(
        effective,
        response,
        collection="search_route_receipts",
        id_key="route_receipt_id",
        required_new_pass_id=validation_context.research_pass_id,
    )
    _append_immutable_rows(
        effective,
        response,
        collection="research_passes",
        id_key="pass_id",
        required_new_pass_id=validation_context.research_pass_id,
    )
    if schema_version == "e2r_pro_research_dossier_v3":
        _append_immutable_rows(
            effective,
            response,
            collection="derived_metrics",
            id_key="derived_metric_id",
        )
    updated_questions = _merge_question_results(effective, response)
    _merge_gap_state(effective, response)
    if schema_version == "e2r_pro_research_dossier_v2":
        _append_repair_register(effective, response)

    for key in (
        "research_pass_id",
        "parent_pass_id",
        "research_saturation",
    ):
        effective[key] = deepcopy(response.get(key))
    for key in ("component_research", "structured_metrics"):
        incoming = response.get(key)
        if isinstance(incoming, Mapping):
            current = dict(effective.get(key) or {})
            current.update(deepcopy(dict(incoming)))
            effective[key] = current
    if schema_version == "e2r_pro_research_dossier_v3":
        _extend_v3_lineage_rosters_from_graph(effective)
        _drop_unbound_v3_question_fact_references(effective)
    _project_overclaimed_route_closures(effective)
    reported_research_status = response.get("research_status")
    if not isinstance(reported_research_status, str) or not reported_research_status:
        raise DossierDeltaMergeError(
            "follow-up response lacks its reported research status"
        )
    deterministic_research_status = (
        compile_dossier_v2_closure_summary(effective).expected_research_status
    )
    effective["research_status"] = deterministic_research_status
    saturation = dict(effective.get("research_saturation") or {})
    saturation["pro_reported_followup_research_status"] = reported_research_status
    saturation["deterministic_effective_research_status"] = (
        deterministic_research_status
    )
    effective["research_saturation"] = saturation
    if schema_version == "e2r_pro_research_dossier_v2":
        effective["proposed_score_ranges"] = []
    effective["score_authority"] = False
    effective["stage_authority"] = False
    if schema_version == "e2r_pro_research_dossier_v3":
        _validate_new_v3_source_documents_are_route_bound(
            effective,
            new_source_document_ids=new_source_document_ids,
            current_pass_id=validation_context.research_pass_id,
        )
    try:
        ResearchDossierValidator().validate(effective, validation_context)
    except Exception as error:
        raise DossierDeltaMergeError(
            f"merged ResearchDossierV2/V3 failed strict validation: {error}"
        ) from error
    return DossierDeltaMergeResult(
        effective_dossier=effective,
        original_hash=canonical_hash(original_dossier),
        response_hash=canonical_hash(response_dossier),
        effective_hash=canonical_hash(effective),
        new_fact_ids=tuple(new_fact_ids),
        new_source_lineage_ids=tuple(new_lineages),
        new_route_receipt_ids=tuple(new_routes),
        updated_question_family_ids=tuple(updated_questions),
    )


_V3_FACT_COLLECTIONS = (
    "material_facts",
    "counterfacts",
    "resolution_facts",
)
_V3_FACT_REFERENCE_FIELDS = frozenset(
    {
        "support_fact_ids",
        "counter_fact_ids",
        "resolution_fact_ids",
        "accepted_fact_ids",
        "input_fact_ids",
        "fact_ids",
        "new_verified_fact_ids_expected",
    }
)


def _coalesce_prior_v3_source_document_duplicates(
    original: Mapping[str, Any],
    response: dict[str, Any],
) -> dict[str, Any]:
    """Reuse a prior canonical URL only when its target scope is compatible.

    V3 gives one canonical URL one document identity.  A later pass may repeat
    that URL under another id.  Matching target/issuer scope can safely reuse
    the prior immutable document.  Conflicting scope cannot be upgraded or
    downgraded deterministically, so the duplicate document and only its
    dependent incoming facts are excluded from the effective graph while the
    raw capture and route receipt remain intact.
    """

    prior_by_url: dict[str, Mapping[str, Any]] = {}
    for raw_document in original.get("source_documents") or ():
        if not isinstance(raw_document, Mapping):
            continue
        url = str(raw_document.get("canonical_url") or "")
        if url and url not in prior_by_url:
            prior_by_url[url] = raw_document

    incoming_url_counts: dict[str, int] = {}
    for raw_document in response.get("source_documents") or ():
        if isinstance(raw_document, Mapping):
            url = str(raw_document.get("canonical_url") or "")
            incoming_url_counts[url] = incoming_url_counts.get(url, 0) + 1

    replacements: dict[str, str] = {}
    removed_document_ids: set[str] = set()
    projections: list[dict[str, Any]] = []
    retained_documents: list[Any] = []
    for raw_document in response.get("source_documents") or ():
        if not isinstance(raw_document, Mapping):
            retained_documents.append(deepcopy(raw_document))
            continue
        incoming = deepcopy(dict(raw_document))
        duplicate_id = str(incoming.get("source_document_id") or "")
        url = str(incoming.get("canonical_url") or "")
        prior = prior_by_url.get(url)
        if prior is None or incoming_url_counts.get(url) != 1:
            retained_documents.append(incoming)
            continue
        canonical_id = str(prior.get("source_document_id") or "")
        if not duplicate_id or not canonical_id or duplicate_id == canonical_id:
            retained_documents.append(incoming)
            continue
        incoming_scope = incoming.get("target_scope") or {}
        prior_scope = prior.get("target_scope") or {}
        scope_compatible = (
            str(incoming_scope.get("target_id") or "")
            == str(prior_scope.get("target_id") or "")
            and incoming_scope.get("issuer_scoped")
            is prior_scope.get("issuer_scoped")
        )
        action = "REUSE_PRIOR_CANONICAL_DOCUMENT"
        if scope_compatible:
            replacements[duplicate_id] = canonical_id
        else:
            action = "DROP_SCOPE_CONFLICTING_DUPLICATE_DOCUMENT_AND_FACTS"
            removed_document_ids.add(duplicate_id)
        projections.append(
            {
                "duplicate_source_document_id": duplicate_id,
                "canonical_source_document_id": canonical_id,
                "canonical_url_hash": canonical_hash(url),
                "action": action,
                "incoming_document_content_adopted": False,
                "target_scope_compatible": scope_compatible,
            }
        )
    response["source_documents"] = retained_documents

    removed_fact_ids: set[str] = set()
    removed_fact_ids_by_document: dict[str, set[str]] = {
        document_id: set() for document_id in removed_document_ids
    }
    if removed_document_ids:
        for collection in _V3_FACT_COLLECTIONS:
            retained_facts: list[Any] = []
            for raw_fact in response.get(collection) or ():
                if (
                    isinstance(raw_fact, Mapping)
                    and str(raw_fact.get("source_document_id") or "")
                    in removed_document_ids
                ):
                    fact_id = str(raw_fact.get("dossier_fact_id") or "")
                    if fact_id:
                        removed_fact_ids.add(fact_id)
                        removed_fact_ids_by_document[
                            str(raw_fact.get("source_document_id") or "")
                        ].add(fact_id)
                    continue
                retained_facts.append(deepcopy(raw_fact))
            response[collection] = retained_facts

    if replacements or removed_document_ids:
        _rewrite_v3_source_document_references(
            response,
            replacements,
            removed_document_ids=removed_document_ids,
        )
    removed_metric_ids_by_document: dict[str, set[str]] = {
        document_id: set() for document_id in removed_document_ids
    }
    if removed_fact_ids:
        retained_metrics: list[Any] = []
        for raw_metric in response.get("derived_metrics") or ():
            inputs = {
                str(value) for value in (raw_metric or {}).get("input_fact_ids") or ()
            } if isinstance(raw_metric, Mapping) else set()
            if inputs.intersection(removed_fact_ids):
                metric_id = str(raw_metric.get("derived_metric_id") or "")
                if metric_id:
                    for document_id, document_fact_ids in (
                        removed_fact_ids_by_document.items()
                    ):
                        if inputs.intersection(document_fact_ids):
                            removed_metric_ids_by_document[document_id].add(
                                metric_id
                            )
                continue
            retained_metrics.append(deepcopy(raw_metric))
        response["derived_metrics"] = retained_metrics
        _rewrite_v3_fact_references(
            response,
            {},
            removed_fact_ids=removed_fact_ids,
        )
    if removed_document_ids or removed_fact_ids:
        _prune_empty_v3_response_lineages(response)
    if not projections:
        return response
    for row in projections:
        document_id = row["duplicate_source_document_id"]
        if document_id in removed_document_ids:
            row["dropped_fact_ids"] = sorted(
                removed_fact_ids_by_document[document_id]
            )
            row["dropped_derived_metric_ids"] = sorted(
                removed_metric_ids_by_document[document_id]
            )
    saturation = dict(response.get("research_saturation") or {})
    saturation["v3_duplicate_source_document_projections"] = projections
    response["research_saturation"] = saturation
    return response


def _rewrite_v3_source_document_references(
    response: dict[str, Any],
    replacements: Mapping[str, str],
    *,
    removed_document_ids: set[str] | frozenset[str] = frozenset(),
) -> None:
    for collection in _V3_FACT_COLLECTIONS:
        for raw_fact in response.get(collection) or ():
            if isinstance(raw_fact, dict):
                source_id = str(raw_fact.get("source_document_id") or "")
                if source_id in replacements:
                    raw_fact["source_document_id"] = replacements[source_id]
    for raw_lineage in response.get("source_lineages") or ():
        if isinstance(raw_lineage, dict):
            raw_lineage["source_document_ids"] = list(
                dict.fromkeys(
                    replacements.get(str(value), str(value))
                    for value in raw_lineage.get("source_document_ids") or ()
                    if str(value) not in removed_document_ids
                )
            )
    saturation = response.get("research_saturation")
    if isinstance(saturation, dict):
        for field_name in ("new_source_document_ids_expected",):
            values = saturation.get(field_name)
            if isinstance(values, list):
                saturation[field_name] = list(
                    dict.fromkeys(
                        replacements.get(str(value), str(value))
                        for value in values
                        if str(value) not in removed_document_ids
                    )
                )


def _prune_empty_v3_response_lineages(response: dict[str, Any]) -> None:
    response["source_lineages"] = [
        deepcopy(raw_lineage)
        for raw_lineage in response.get("source_lineages") or ()
        if not isinstance(raw_lineage, Mapping)
        or raw_lineage.get("source_document_ids")
        or raw_lineage.get("fact_ids")
    ]


def _coalesce_prior_v3_atomic_fact_duplicates(
    original: Mapping[str, Any],
    response: dict[str, Any],
) -> dict[str, Any]:
    """Project a later-pass duplicate onto the immutable canonical fact.

    The V3 validator intentionally forbids two fact ids for one exact atomic
    source/predicate/subject/excerpt identity.  A follow-up can nevertheless
    repeat an already accepted atom under a new id.  Only duplicates against
    the prior valid graph are coalesced.  Same-pass duplicates and cross-kind
    conflicts remain in place so strict validation still rejects them.
    """

    prior_by_identity: dict[tuple[str, str, str, str], tuple[str, str]] = {}
    for collection in _V3_FACT_COLLECTIONS:
        for raw_fact in original.get(collection) or ():
            if not isinstance(raw_fact, Mapping):
                continue
            fact_id = str(raw_fact.get("dossier_fact_id") or "")
            identity = v3_atomic_fact_identity(raw_fact)
            if fact_id and identity not in prior_by_identity:
                prior_by_identity[identity] = (collection, fact_id)

    incoming_identity_counts: dict[tuple[str, str, str, str], int] = {}
    for collection in _V3_FACT_COLLECTIONS:
        for raw_fact in response.get(collection) or ():
            if isinstance(raw_fact, Mapping):
                identity = v3_atomic_fact_identity(raw_fact)
                incoming_identity_counts[identity] = (
                    incoming_identity_counts.get(identity, 0) + 1
                )

    replacements: dict[str, str] = {}
    projections: list[dict[str, Any]] = []
    for collection in _V3_FACT_COLLECTIONS:
        retained: list[Any] = []
        for raw_fact in response.get(collection) or ():
            if not isinstance(raw_fact, Mapping):
                retained.append(deepcopy(raw_fact))
                continue
            incoming = deepcopy(dict(raw_fact))
            duplicate_id = str(incoming.get("dossier_fact_id") or "")
            identity = v3_atomic_fact_identity(incoming)
            prior = prior_by_identity.get(identity)
            if (
                prior is None
                or prior[0] != collection
                or incoming_identity_counts.get(identity) != 1
            ):
                retained.append(incoming)
                continue
            canonical_id = prior[1]
            if not duplicate_id or duplicate_id == canonical_id:
                retained.append(incoming)
                continue
            replacements[duplicate_id] = canonical_id
            projections.append(
                {
                    "duplicate_fact_id": duplicate_id,
                    "canonical_fact_id": canonical_id,
                    "fact_collection": collection,
                    "atomic_identity_hash": canonical_hash(identity),
                    "incoming_fact_content_adopted": False,
                    "reason": "EXACT_PRIOR_ATOMIC_IDENTITY",
                }
            )
        response[collection] = retained

    if not replacements:
        return response
    _rewrite_v3_fact_references(response, replacements)
    saturation = dict(response.get("research_saturation") or {})
    saturation["v3_duplicate_atomic_fact_projections"] = projections
    response["research_saturation"] = saturation
    return response


def _rewrite_v3_fact_references(
    value: Any,
    replacements: Mapping[str, str],
    *,
    removed_fact_ids: set[str] | frozenset[str] = frozenset(),
) -> None:
    if isinstance(value, dict):
        for key, child in tuple(value.items()):
            if key in _V3_FACT_REFERENCE_FIELDS and isinstance(child, list):
                value[key] = list(
                    dict.fromkeys(
                        replacements.get(str(fact_id), str(fact_id))
                        for fact_id in child
                        if str(fact_id) not in removed_fact_ids
                    )
                )
            else:
                _rewrite_v3_fact_references(
                    child,
                    replacements,
                    removed_fact_ids=removed_fact_ids,
                )
    elif isinstance(value, list):
        for child in value:
            _rewrite_v3_fact_references(
                child,
                replacements,
                removed_fact_ids=removed_fact_ids,
            )


def _validate_scope_identity(
    original: Mapping[str, Any],
    response: Mapping[str, Any],
    context: DossierValidationContext,
) -> None:
    original_version = str(original.get("schema_version") or "")
    response_version = str(response.get("schema_version") or "")
    if (
        original_version
        not in {
            "e2r_pro_research_dossier_v2",
            "e2r_pro_research_dossier_v3",
        }
        or response_version != original_version
    ):
        raise DossierDeltaMergeError(
            "follow-up merge requires two dossiers of the same V2/V3 schema"
        )
    for key in ("job_id", "run_id", "conversation_id", "as_of_date"):
        if response.get(key) != original.get(key):
            raise DossierDeltaMergeError(f"follow-up changed immutable scope field: {key}")
    original_target = original.get("target") or {}
    response_target = response.get("target") or {}
    for key in ("target_id", "symbol", "company_name"):
        before = original_target.get(key)
        after = response_target.get(key)
        if before is not None and after != before:
            raise DossierDeltaMergeError(f"follow-up changed immutable target field: {key}")
    for key in ("candidate_archetypes", "selected_archetypes"):
        # A delta-shaped follow-up must carry the required schema arrays, but
        # an empty array means "no scope update".  A non-empty roster still has
        # to match exactly, so a follow-up cannot select a new mechanism.
        incoming = set(str(value) for value in response.get(key) or ())
        if incoming and incoming != set(
            str(value) for value in original.get(key) or ()
        ):
            raise DossierDeltaMergeError(f"follow-up changed contract scope: {key}")
    if response.get("score_authority") is not False or response.get(
        "stage_authority"
    ) is not False:
        raise DossierDeltaMergeError("follow-up dossier cannot own score or Stage")
    if (
        context.research_pass_id
        and response.get("research_pass_id") != context.research_pass_id
    ):
        raise DossierDeltaMergeError("follow-up response belongs to another pass")
    if (
        context.enforce_parent_pass_id
        and response.get("parent_pass_id") != context.parent_pass_id
    ):
        raise DossierDeltaMergeError("follow-up response has wrong parent lineage")


def _append_immutable_rows(
    effective: dict[str, Any],
    response: Mapping[str, Any],
    *,
    collection: str,
    id_key: str,
    required_new_pass_id: str | None = None,
) -> tuple[str, ...]:
    rows = list(effective.get(collection) or ())
    existing = {str(row.get(id_key) or ""): row for row in rows}
    if len(existing) != len(rows):
        raise DossierDeltaMergeError(f"original {collection} contains duplicate ids")
    added: list[str] = []
    for incoming in response.get(collection) or ():
        identity = str(incoming.get(id_key) or "")
        if not identity:
            raise DossierDeltaMergeError(f"follow-up {collection} row lacks {id_key}")
        prior = existing.get(identity)
        if prior is not None:
            if canonical_hash(prior) != canonical_hash(incoming):
                # The current pass receipt is capture-bound transport metadata;
                # the bound row may safely replace Pro's non-authoritative row.
                if collection == "research_passes" and identity == required_new_pass_id:
                    rows[rows.index(prior)] = deepcopy(dict(incoming))
                    existing[identity] = rows[rows.index(prior)]
                    continue
                raise DossierDeltaMergeError(
                    f"follow-up rewrote immutable {collection} row: {identity}"
                )
            continue
        if required_new_pass_id is not None and str(
            incoming.get("research_pass_id")
            if collection.endswith("facts")
            else incoming.get("pass_id")
            or ""
        ) != required_new_pass_id:
            raise DossierDeltaMergeError(
                f"new {collection} row is detached from the current pass"
            )
        copied = deepcopy(dict(incoming))
        rows.append(copied)
        existing[identity] = copied
        added.append(identity)
    effective[collection] = rows
    return tuple(added)


V2_SOURCE_LINEAGE_UNION_FIELDS = frozenset(
    {
        "source_urls",
        "canonical_source_urls",
        "fact_ids",
        "publisher_roster",
        "same_fact_reprints_collapsed",
        "existing_fact_ids_referenced",
        "source_document_ids",
    }
)
V2_SOURCE_LINEAGE_IDENTITY_FIELDS = frozenset(
    {
        "source_lineage_id",
        "independence_group_id",
        "lineage_subject",
        "status",
    }
)
V2_SOURCE_LINEAGE_CURRENT_STATE_FIELDS = frozenset(
    {"lineage_status", "lineage_operation"}
)
V3_SOURCE_LINEAGE_UNION_FIELDS = frozenset(
    {"source_document_ids", "fact_ids"}
)
V3_SOURCE_LINEAGE_IDENTITY_FIELDS = frozenset(
    {"lineage_id", "independence_group_id", "status"}
)


def _merge_source_lineages(
    effective: dict[str, Any],
    response: Mapping[str, Any],
    *,
    schema_version: str,
) -> tuple[str, ...]:
    """Append evidence to an existing lineage without rewriting its identity.

    A later pass often finds a newer document in an already known publisher or
    event lineage.  The lineage entity therefore keeps immutable identity
    fields while URL/fact/publisher rosters grow monotonically.  Current-state
    diagnostics retain an explicit value history before advancing.
    """

    id_key = (
        "lineage_id"
        if schema_version == "e2r_pro_research_dossier_v3"
        else "source_lineage_id"
    )
    if schema_version == "e2r_pro_research_dossier_v3":
        union_fields = V3_SOURCE_LINEAGE_UNION_FIELDS
        identity_fields = V3_SOURCE_LINEAGE_IDENTITY_FIELDS
        current_state_fields: frozenset[str] = frozenset()
    else:
        union_fields = V2_SOURCE_LINEAGE_UNION_FIELDS
        identity_fields = V2_SOURCE_LINEAGE_IDENTITY_FIELDS
        current_state_fields = V2_SOURCE_LINEAGE_CURRENT_STATE_FIELDS
    rows = list(effective.get("source_lineages") or ())
    index = {
        str(row.get(id_key) or ""): position
        for position, row in enumerate(rows)
    }
    if len(index) != len(rows):
        raise DossierDeltaMergeError(
            "original source_lineages contains duplicate ids"
        )
    added: list[str] = []
    for incoming_raw in response.get("source_lineages") or ():
        if not isinstance(incoming_raw, Mapping):
            raise DossierDeltaMergeError(
                "follow-up source lineage row must be an object"
            )
        incoming = deepcopy(dict(incoming_raw))
        lineage_id = str(incoming.get(id_key) or "")
        if not lineage_id:
            raise DossierDeltaMergeError(
                f"follow-up source lineage lacks {id_key}"
            )
        if lineage_id not in index:
            index[lineage_id] = len(rows)
            rows.append(incoming)
            added.append(lineage_id)
            continue

        prior = deepcopy(dict(rows[index[lineage_id]]))
        for key in identity_fields:
            before = prior.get(key)
            after = incoming.get(key)
            if before is not None and after is not None and before != after:
                raise DossierDeltaMergeError(
                    f"follow-up rewrote source lineage identity: {lineage_id}.{key}"
                )
        merged = deepcopy(prior)
        for key in union_fields:
            merged[key] = list(
                dict.fromkeys(
                    str(value)
                    for value in (
                        *(prior.get(key) or ()),
                        *(incoming.get(key) or ()),
                    )
                    if str(value)
                )
            )
        for key in current_state_fields:
            before = prior.get(key)
            after = incoming.get(key)
            history_key = f"{key}_history"
            merged[history_key] = list(
                dict.fromkeys(
                    str(value)
                    for value in (
                        *(prior.get(history_key) or ()),
                        before,
                        after,
                    )
                    if value is not None and str(value)
                )
            )
            if after is not None:
                merged[key] = deepcopy(after)
        handled = (
            union_fields
            | identity_fields
            | current_state_fields
            | {
                f"{key}_history"
                for key in current_state_fields
            }
        )
        for key, value in incoming.items():
            if key in handled:
                continue
            if key not in merged:
                merged[key] = deepcopy(value)
                continue
            if canonical_hash(merged[key]) != canonical_hash(value):
                raise DossierDeltaMergeError(
                    f"follow-up rewrote source lineage metadata: {lineage_id}.{key}"
                )
        rows[index[lineage_id]] = merged
    effective["source_lineages"] = rows
    return tuple(added)


def _project_overclaimed_route_closures(effective: dict[str, Any]) -> None:
    """Keep new evidence while refusing terminal closure over blocked routes.

    Pro's raw response remains immutable in the capture bundle.  The effective
    dossier may nevertheless have to demote a reported absence/non-public
    closure when its exact route roster still contains a provider/parser
    failure, lacks two routes, or lacks a no-new-route reason.  Rejecting the
    whole delta would discard otherwise valid new documents and facts; marking
    the exact question pending preserves both the evidence and fail-closed
    score semantics.
    """

    receipt_by_id = {
        str(row.get("route_receipt_id") or ""): row
        for row in effective.get("search_route_receipts") or ()
        if isinstance(row, Mapping)
    }
    projections: list[dict[str, Any]] = []
    question_rows = list(effective.get("question_family_results") or ())
    for index, raw_row in enumerate(question_rows):
        if not isinstance(raw_row, Mapping):
            continue
        row = deepcopy(dict(raw_row))
        reported_status = str(row.get("status") or "")
        if reported_status not in {
            "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
            "LIKELY_NONPUBLIC",
        }:
            continue
        route_ids = tuple(
            str(value)
            for value in row.get("search_route_receipt_ids") or ()
            if str(value)
        )
        linked = tuple(receipt_by_id.get(value) for value in route_ids)
        non_success = tuple(
            (route_id, str((receipt or {}).get("provider_status") or "MISSING"))
            for route_id, receipt in zip(route_ids, linked)
            if receipt is None or receipt.get("provider_status") != "SUCCESS"
        )
        missing_no_new_reason = tuple(
            route_id
            for route_id, receipt in zip(route_ids, linked)
            if reported_status == "LIKELY_NONPUBLIC"
            and receipt is not None
            and receipt.get("provider_status") == "SUCCESS"
            and not str(receipt.get("no_new_route_reason") or "").strip()
        )
        failure_codes: list[str] = []
        if row.get("adequate_search_proven") is not True:
            failure_codes.append("ADEQUATE_SEARCH_NOT_PROVEN")
        if len(route_ids) < 2:
            failure_codes.append("INSUFFICIENT_ROUTE_RECEIPTS")
        if non_success:
            failure_codes.append("NON_NORMAL_PROVIDER_OR_PARSER_RECEIPT")
        if missing_no_new_reason:
            failure_codes.append("MISSING_NO_NEW_ROUTE_REASON")
        if not failure_codes:
            continue
        blocking_statuses = {status for _route_id, status in non_success}
        if "PARSER_PENDING" in blocking_statuses:
            projected_status = "PARSER_PENDING"
            availability_class = "PARSER_BLOCKED"
        elif blocking_statuses:
            projected_status = "PROVIDER_PENDING"
            availability_class = "PROVIDER_BLOCKED"
        else:
            projected_status = "SOURCE_PENDING"
            availability_class = "PUBLIC_SEARCHABLE"
        row["status"] = projected_status
        row["availability_class"] = availability_class
        row["adequate_search_proven"] = False
        prior_reason = str(row.get("closure_reason") or "").strip()
        row["closure_reason"] = (
            f"{prior_reason} " if prior_reason else ""
        ) + "Deterministic route audit kept this question pending."
        question_rows[index] = row
        projections.append(
            {
                "question_family_id": str(row.get("question_family_id") or ""),
                "reported_status": reported_status,
                "projected_status": projected_status,
                "failure_codes": failure_codes,
                "blocking_route_receipts": [
                    {"route_receipt_id": route_id, "provider_status": status}
                    for route_id, status in non_success
                ],
                "missing_no_new_route_reason_ids": list(missing_no_new_reason),
            }
        )
    effective["question_family_results"] = question_rows
    if projections:
        saturation = dict(effective.get("research_saturation") or {})
        saturation["route_truth_question_status_projections"] = projections
        effective["research_saturation"] = saturation


def _extend_v3_lineage_rosters_from_graph(effective: dict[str, Any]) -> None:
    """Fill only omitted V3 lineage roster members from immutable graph edges.

    ``source_lineages`` duplicates relationships already fixed by
    ``source_documents[*].lineage_id`` and each atomic fact's
    ``source_document_id``.  A delta may add a fact against a prior document
    while omitting the unchanged lineage row.  In that case the exact missing
    roster member is derivable without inventing source identity or content.
    Existing extra/wrong members are never removed, so strict validation still
    rejects contradictory graphs.
    """

    source_documents = tuple(effective.get("source_documents") or ())
    source_by_id = {
        str(row.get("source_document_id") or ""): row
        for row in source_documents
        if isinstance(row, Mapping)
    }
    facts = tuple(
        row
        for collection in ("material_facts", "counterfacts", "resolution_facts")
        for row in effective.get(collection) or ()
        if isinstance(row, Mapping)
    )
    expected_documents: dict[str, list[str]] = {}
    for document in source_documents:
        if not isinstance(document, Mapping):
            continue
        lineage_id = str(document.get("lineage_id") or "")
        document_id = str(document.get("source_document_id") or "")
        if lineage_id and document_id:
            expected_documents.setdefault(lineage_id, []).append(document_id)
    expected_facts: dict[str, list[str]] = {}
    for fact in facts:
        document = source_by_id.get(str(fact.get("source_document_id") or ""))
        lineage_id = str((document or {}).get("lineage_id") or "")
        fact_id = str(fact.get("dossier_fact_id") or "")
        if lineage_id and fact_id:
            expected_facts.setdefault(lineage_id, []).append(fact_id)

    extensions: list[dict[str, Any]] = []
    lineage_rows = list(effective.get("source_lineages") or ())
    for index, raw_row in enumerate(lineage_rows):
        if not isinstance(raw_row, Mapping):
            continue
        row = deepcopy(dict(raw_row))
        lineage_id = str(row.get("lineage_id") or "")
        actual_documents = list(row.get("source_document_ids") or ())
        actual_facts = list(row.get("fact_ids") or ())
        missing_documents = [
            value
            for value in expected_documents.get(lineage_id, ())
            if value not in set(actual_documents)
        ]
        missing_facts = [
            value
            for value in expected_facts.get(lineage_id, ())
            if value not in set(actual_facts)
        ]
        if not missing_documents and not missing_facts:
            continue
        row["source_document_ids"] = [*actual_documents, *missing_documents]
        row["fact_ids"] = [*actual_facts, *missing_facts]
        lineage_rows[index] = row
        extensions.append(
            {
                "lineage_id": lineage_id,
                "added_source_document_ids": missing_documents,
                "added_fact_ids": missing_facts,
                "derivation": (
                    "SOURCE_DOCUMENT_LINEAGE_AND_FACT_SOURCE_DOCUMENT_EDGES"
                ),
            }
        )
    effective["source_lineages"] = lineage_rows
    if extensions:
        saturation = dict(effective.get("research_saturation") or {})
        saturation["v3_graph_lineage_roster_extensions"] = extensions
        effective["research_saturation"] = saturation


def _drop_unbound_v3_question_fact_references(
    effective: dict[str, Any],
) -> None:
    """Drop only redundant question edges not authorized by the fact roster.

    A follow-up can cite an earlier-pass fact without repeating that immutable
    fact row.  The delta-only pre-schema boundary therefore cannot know whether
    the cited fact binds back to the current question.  Once the cumulative
    graph has been assembled, this projection applies the same conservative
    rule as initial V3 preflight: keep the fact unchanged and remove only the
    unsupported question-to-fact edge.  Unknown fact ids remain untouched so
    strict validation still rejects fabricated references.
    """

    fact_by_id: dict[str, Mapping[str, Any]] = {}
    expected_collection_by_id: dict[str, str] = {}
    for collection, reference_field in (
        ("material_facts", "support_fact_ids"),
        ("counterfacts", "counter_fact_ids"),
        ("resolution_facts", "resolution_fact_ids"),
    ):
        for raw_fact in effective.get(collection) or ():
            if not isinstance(raw_fact, Mapping):
                continue
            fact_id = str(raw_fact.get("dossier_fact_id") or "")
            if not fact_id:
                continue
            fact_by_id[fact_id] = raw_fact
            expected_collection_by_id[fact_id] = reference_field

    projections: list[dict[str, Any]] = []
    question_rows = list(effective.get("question_family_results") or ())
    for index, raw_question in enumerate(question_rows):
        if not isinstance(raw_question, Mapping):
            continue
        question = deepcopy(dict(raw_question))
        question_id = str(question.get("question_family_id") or "")
        changed = False
        for field_name in (
            "support_fact_ids",
            "counter_fact_ids",
            "resolution_fact_ids",
        ):
            before = [str(value) for value in question.get(field_name) or ()]
            after: list[str] = []
            dropped: list[dict[str, str]] = []
            for fact_id in before:
                fact = fact_by_id.get(fact_id)
                if fact is None:
                    after.append(fact_id)
                    continue
                if expected_collection_by_id[fact_id] != field_name:
                    dropped.append(
                        {"fact_id": fact_id, "reason": "WRONG_FACT_KIND"}
                    )
                    continue
                if question_id not in {
                    str(value)
                    for value in fact.get("question_family_ids") or ()
                }:
                    dropped.append(
                        {"fact_id": fact_id, "reason": "MISSING_FACT_BACKLINK"}
                    )
                    continue
                after.append(fact_id)
            if not dropped:
                continue
            question[field_name] = after
            changed = True
            projections.append(
                {
                    "question_family_id": question_id,
                    "reference_field": field_name,
                    "dropped_references": dropped,
                }
            )
        if changed:
            question_rows[index] = question
    effective["question_family_results"] = question_rows
    if projections:
        saturation = dict(effective.get("research_saturation") or {})
        saturation["v3_question_fact_reference_projections"] = projections
        effective["research_saturation"] = saturation


def _validate_new_v3_source_documents_are_route_bound(
    effective: Mapping[str, Any],
    *,
    new_source_document_ids: Sequence[str],
    current_pass_id: str | None,
) -> None:
    """Reject unattached V3 documents without inventing pass metadata.

    V3 source documents do not carry a pass id.  A new document is therefore
    admitted only when the current pass added a fact that cites it or opened
    its exact canonical/opened URL in a durable route receipt.
    """

    if not new_source_document_ids:
        return
    current_pass = str(current_pass_id or "")
    referenced_document_ids = {
        str(fact.get("source_document_id") or "")
        for collection in ("material_facts", "counterfacts", "resolution_facts")
        for fact in effective.get(collection) or ()
        if str(fact.get("research_pass_id") or "") == current_pass
    }
    current_route_urls = {
        str(url)
        for route in effective.get("search_route_receipts") or ()
        if str(route.get("pass_id") or "") == current_pass
        for url in route.get("opened_source_urls") or ()
        if str(url)
    }
    documents = {
        str(row.get("source_document_id") or ""): row
        for row in effective.get("source_documents") or ()
    }
    unattached = []
    for document_id in new_source_document_ids:
        document = documents.get(document_id) or {}
        document_urls = {
            str(value)
            for value in (
                document.get("canonical_url"),
                document.get("opened_url"),
            )
            if str(value or "")
        }
        if (
            document_id not in referenced_document_ids
            and not document_urls.intersection(current_route_urls)
        ):
            unattached.append(document_id)
    if unattached:
        raise DossierDeltaMergeError(
            "new V3 source document is detached from the current pass: "
            + ",".join(sorted(unattached))
        )


def _merge_question_results(
    effective: dict[str, Any], response: Mapping[str, Any]
) -> tuple[str, ...]:
    rows = list(effective.get("question_family_results") or ())
    index = {
        str(row.get("question_family_id") or ""): position
        for position, row in enumerate(rows)
    }
    if len(index) != len(rows):
        raise DossierDeltaMergeError("original question results contain duplicate ids")
    updated: list[str] = []
    cumulative_keys = (
        "support_fact_ids",
        "counter_fact_ids",
        "resolution_fact_ids",
        "attempted_source_role_ids",
        "search_route_receipt_ids",
    )
    for incoming in response.get("question_family_results") or ():
        question_id = str(incoming.get("question_family_id") or "")
        if not question_id:
            raise DossierDeltaMergeError("follow-up question result lacks identity")
        if question_id in index:
            prior = rows[index[question_id]]
            merged = deepcopy(dict(incoming))
            for key in cumulative_keys:
                # Follow-up output may be cumulative or a true delta.  Unioning
                # the immutable prior links with incoming links supports both
                # shapes and makes deletion impossible by construction.
                merged[key] = list(
                    dict.fromkeys(
                        str(value)
                        for value in (
                            *(prior.get(key) or ()),
                            *(incoming.get(key) or ()),
                        )
                        if str(value)
                    )
                )
            rows[index[question_id]] = merged
        else:
            index[question_id] = len(rows)
            rows.append(deepcopy(dict(incoming)))
        updated.append(question_id)
    effective["question_family_results"] = rows
    return tuple(dict.fromkeys(updated))


def _merge_gap_state(effective: dict[str, Any], response: Mapping[str, Any]) -> None:
    rows = list(effective.get("unresolved_gaps") or ())
    index = {
        str(row.get("stable_gap_key") or row.get("gap_id") or ""): position
        for position, row in enumerate(rows)
    }
    for incoming in response.get("unresolved_gaps") or ():
        key = str(incoming.get("stable_gap_key") or incoming.get("gap_id") or "")
        if not key:
            raise DossierDeltaMergeError("follow-up gap lacks stable identity")
        if key in index:
            rows[index[key]] = deepcopy(dict(incoming))
        else:
            index[key] = len(rows)
            rows.append(deepcopy(dict(incoming)))
    effective["unresolved_gaps"] = rows


def _append_repair_register(
    effective: dict[str, Any], response: Mapping[str, Any]
) -> None:
    rows = list(effective.get("verification_repair_register") or ())
    identities = {
        (str(row.get("candidate_id") or ""), str(row.get("question_family_id") or ""))
        for row in rows
    }
    for incoming in response.get("verification_repair_register") or ():
        identity = (
            str(incoming.get("candidate_id") or ""),
            str(incoming.get("question_family_id") or ""),
        )
        if identity not in identities:
            rows.append(deepcopy(dict(incoming)))
            identities.add(identity)
    effective["verification_repair_register"] = rows


__all__ = [
    "DossierDeltaMergeError",
    "DossierDeltaMergeResult",
    "apply_research_dossier_delta",
]
