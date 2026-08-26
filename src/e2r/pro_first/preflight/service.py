"""ResearchDossierV3 local normalization and pre-verifier orchestration."""

from __future__ import annotations

from copy import deepcopy
import os
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research.page_fetcher import FetchResult, PageFetcher

from ..atomic_io import fsync_directory
from ..ids import canonical_hash, canonical_json, stable_id
from ..research_contracts import select_contract_bundle
from .atomic_fact import AtomicFactPreflight
from .canonical_url import CanonicalURLResolver
from .date_resolver import DatePrecedenceResolver
from .issuer_alias import IssuerAliasResolver
from .models import (
    EvidencePreflightResult,
    PreflightIssue,
    PreflightOperation,
    RejectionRootCauseClass,
    RejectionRouting,
    ResolvedSourceRepresentation,
    StaticPreflightNormalization,
)
from .rejection_classifier import ClassifiedRejections, RejectionClassifier
from .scope_mapper import ClosedEnumScopeMapper
from .source_representation import SourceRepresentationResolver
from .text_normalizer import TextQuoteNormalizer


PREFLIGHT_SEMANTICS_VERSION = "e2r_local_evidence_preflight_v1"
DOSSIER_V3 = "e2r_pro_research_dossier_v3"
_FACT_COLLECTIONS = ("material_facts", "counterfacts", "resolution_facts")

_SOURCE_DOCUMENT_FIELD_ALIASES = {
    "url": "canonical_url",
    "final_url": "opened_url",
    "title": "source_title",
    "publisher": "source_publisher",
    "published_at": "publication_date",
    "available_at": "availability_date",
    "source_roles": "source_role_ids",
    "source_lineage_id": "lineage_id",
}
_FACT_FIELD_ALIASES = {
    "predicate": "predicate_id",
    "candidate_components": "candidate_component_ids",
    "source_id": "source_document_id",
    "source_document_ref": "source_document_id",
    "exact_quote": "supporting_excerpt",
    "excerpt": "supporting_excerpt",
    "economic_mechanism": "economic_mechanism_id",
    "lifecycle": "current_status",
    "question_ids": "question_family_ids",
}
_LINEAGE_FIELD_ALIASES = {"source_lineage_id": "lineage_id"}
_LIFECYCLE_ALIASES = {"HISTORICAL": "HISTORICAL_ONLY"}
_DIRECTION_ALIASES = {"COUNTER": "NEGATIVE"}
_INITIAL_PASS_NAME = "INITIAL_FULL_RESEARCH"
_INITIAL_CONVERSATION_PLACEHOLDER = "PENDING_INITIAL_CONVERSATION"
_INITIAL_CONVERSATION_PLACEHOLDER_ALIASES = frozenset(
    {"PENDING_NEW_CONVERSATION"}
)
_NULL_PARENT_PASS_ALIASES = frozenset({"NONE"})


class PreSchemaV3Normalizer:
    """Apply only explicit mechanical fixes before strict V3 validation."""

    def __init__(
        self,
        *,
        url_resolver: CanonicalURLResolver | None = None,
        text_normalizer: TextQuoteNormalizer | None = None,
        issuer_alias_resolver: IssuerAliasResolver | None = None,
        scope_mapper: ClosedEnumScopeMapper | None = None,
    ) -> None:
        self.url_resolver = url_resolver or CanonicalURLResolver()
        self.text_normalizer = text_normalizer or TextQuoteNormalizer()
        self.issuer_alias_resolver = issuer_alias_resolver or IssuerAliasResolver()
        self.scope_mapper = scope_mapper or ClosedEnumScopeMapper()

    def normalize(
        self,
        payload: Mapping[str, Any],
        *,
        archetype_ids: Sequence[str],
    ) -> StaticPreflightNormalization:
        before_hash = canonical_hash(payload)
        normalized = deepcopy(dict(payload))
        if normalized.get("schema_version") != DOSSIER_V3:
            return StaticPreflightNormalization(
                payload=normalized,
                before_hash=before_hash,
                after_hash=before_hash,
                operations=(),
            )
        operations: list[PreflightOperation] = []
        _normalize_initial_transport_aliases(normalized, operations)
        source_aliases = _consume_identity_aliases(
            normalized,
            "source_document_aliases",
        )
        lineage_aliases = _consume_identity_aliases(
            normalized,
            "source_lineage_aliases",
        )
        if source_aliases:
            normalized = _rewrite_exact_values(normalized, source_aliases)
            operations.append(
                _operation(
                    "RESOLVE_SOURCE_DOCUMENT_ID_ALIASES",
                    "DOSSIER",
                    str(normalized.get("job_id") or ""),
                    detail=f"alias_count={len(source_aliases)}",
                )
            )
        if lineage_aliases:
            normalized = _rewrite_exact_values(normalized, lineage_aliases)
            operations.append(
                _operation(
                    "RESOLVE_SOURCE_LINEAGE_ID_ALIASES",
                    "DOSSIER",
                    str(normalized.get("job_id") or ""),
                    detail=f"alias_count={len(lineage_aliases)}",
                )
            )

        for document in normalized.get("source_documents") or ():
            if not isinstance(document, dict):
                continue
            document_id = str(document.get("source_document_id") or "")
            _apply_field_aliases(
                document,
                _SOURCE_DOCUMENT_FIELD_ALIASES,
                object_type="SOURCE_DOCUMENT",
                object_id=document_id,
                operations=operations,
            )
            for field in ("canonical_url", "opened_url"):
                if not str(document.get(field) or "").strip():
                    continue
                before = str(document[field])
                resolved = self.url_resolver.resolve(before)
                if resolved.changed:
                    document[field] = resolved.canonical_url
                    operations.append(
                        _operation(
                            "CANONICALIZE_SOURCE_URL",
                            "SOURCE_DOCUMENT",
                            document_id,
                            field_name=field,
                            before=before,
                            after=resolved.canonical_url,
                            detail=(
                                "removed_query_keys="
                                + ",".join(resolved.removed_query_keys)
                            ),
                        )
                    )
            publisher, changed = self.issuer_alias_resolver.normalize_publisher(
                str(document.get("source_publisher") or "")
            )
            if changed:
                before = document.get("source_publisher")
                document["source_publisher"] = publisher
                operations.append(
                    _operation(
                        "NORMALIZE_KNOWN_SOURCE_PUBLISHER_ALIAS",
                        "SOURCE_DOCUMENT",
                        document_id,
                        field_name="source_publisher",
                        before=before,
                        after=publisher,
                    )
                )
            _normalize_text_fields(
                document,
                ("source_title", "locator_value"),
                object_type="SOURCE_DOCUMENT",
                object_id=document_id,
                normalizer=self.text_normalizer,
                operations=operations,
            )

        source_by_id = {
            str(row.get("source_document_id") or ""): row
            for row in normalized.get("source_documents") or ()
            if isinstance(row, Mapping)
        }
        expected_kind = {
            "material_facts": "MATERIAL",
            "counterfacts": "COUNTER",
            "resolution_facts": "RESOLUTION",
        }
        for collection in _FACT_COLLECTIONS:
            for fact in normalized.get(collection) or ():
                if not isinstance(fact, dict):
                    continue
                fact_id = str(fact.get("dossier_fact_id") or "")
                _apply_field_aliases(
                    fact,
                    _FACT_FIELD_ALIASES,
                    object_type="ATOMIC_FACT",
                    object_id=fact_id,
                    operations=operations,
                )
                if not fact.get("fact_kind"):
                    fact["fact_kind"] = expected_kind[collection]
                    operations.append(
                        _operation(
                            "INFER_FACT_KIND_FROM_COLLECTION",
                            "ATOMIC_FACT",
                            fact_id,
                            field_name="fact_kind",
                            before=None,
                            after=expected_kind[collection],
                        )
                    )
                lifecycle = str(fact.get("current_status") or "").upper()
                if lifecycle in _LIFECYCLE_ALIASES:
                    fact["current_status"] = _LIFECYCLE_ALIASES[lifecycle]
                    operations.append(
                        _operation(
                            "MAP_CLOSED_LIFECYCLE_ENUM",
                            "ATOMIC_FACT",
                            fact_id,
                            field_name="current_status",
                            before=lifecycle,
                            after=fact["current_status"],
                        )
                    )
                direction = str(fact.get("direction") or "").upper()
                if direction in _DIRECTION_ALIASES:
                    fact["direction"] = _DIRECTION_ALIASES[direction]
                    operations.append(
                        _operation(
                            "MAP_CLOSED_DIRECTION_ENUM",
                            "ATOMIC_FACT",
                            fact_id,
                            field_name="direction",
                            before=direction,
                            after=fact["direction"],
                        )
                    )
                _normalize_text_fields(
                    fact,
                    ("statement", "supporting_excerpt", "source_locator"),
                    object_type="ATOMIC_FACT",
                    object_id=fact_id,
                    normalizer=self.text_normalizer,
                    operations=operations,
                )
                source_document = source_by_id.get(
                    str(fact.get("source_document_id") or "")
                )
                if source_document is not None:
                    document_scope = source_document.get("target_scope") or {}
                    if (
                        fact.get("issuer_scoped") is True
                        and isinstance(document_scope, Mapping)
                        and document_scope.get("issuer_scoped") is False
                    ):
                        fact["issuer_scoped"] = False
                        operations.append(
                            _operation(
                                "DOWNGRADE_FACT_TO_NONISSUER_SOURCE_SCOPE",
                                "ATOMIC_FACT",
                                fact_id,
                                field_name="issuer_scoped",
                                before=True,
                                after=False,
                                detail=(
                                    "fact cannot claim stronger issuer scope than "
                                    "its bound source document"
                                ),
                            )
                        )
                    mapping = self.scope_mapper.map_fact(
                        fact=fact,
                        source_document=source_document,
                        archetype_ids=archetype_ids,
                    )
                    for field, value, changed, code in (
                        (
                            "business_segment",
                            mapping.business_segment,
                            mapping.segment_changed,
                            "MAP_SEGMENT_CLOSED_ENUM",
                        ),
                        (
                            "product_family",
                            mapping.product_family,
                            mapping.product_changed,
                            "MAP_PRODUCT_CLOSED_ENUM",
                        ),
                    ):
                        if changed:
                            before = fact.get(field)
                            fact[field] = value
                            operations.append(
                                _operation(
                                    code,
                                    "ATOMIC_FACT",
                                    fact_id,
                                    field_name=field,
                                    before=before,
                                    after=value,
                                )
                            )

        fact_ids_by_question_field = {
            "support_fact_ids": {
                str(row.get("dossier_fact_id") or "")
                for row in normalized.get("material_facts") or ()
                if isinstance(row, Mapping)
            },
            "counter_fact_ids": {
                str(row.get("dossier_fact_id") or "")
                for row in normalized.get("counterfacts") or ()
                if isinstance(row, Mapping)
            },
            "resolution_fact_ids": {
                str(row.get("dossier_fact_id") or "")
                for row in normalized.get("resolution_facts") or ()
                if isinstance(row, Mapping)
            },
        }
        known_fact_ids = set().union(*fact_ids_by_question_field.values())
        fact_by_id = {
            str(row.get("dossier_fact_id") or ""): row
            for collection in _FACT_COLLECTIONS
            for row in normalized.get(collection) or ()
            if isinstance(row, Mapping)
        }
        for question in normalized.get("question_family_results") or ():
            if not isinstance(question, dict):
                continue
            question_id = str(question.get("question_family_id") or "")
            for field_name, allowed_fact_ids in fact_ids_by_question_field.items():
                before = list(question.get(field_name) or ())
                after = [
                    value
                    for value in before
                    if str(value) not in known_fact_ids
                    or str(value) in allowed_fact_ids
                ]
                if after == before:
                    continue
                question[field_name] = after
                dropped_ids = tuple(
                    str(value) for value in before if value not in after
                )
                operations.append(
                    _operation(
                        "DROP_WRONG_KIND_QUESTION_FACT_REFERENCE",
                        "QUESTION_FAMILY_RESULT",
                        question_id,
                        field_name=field_name,
                        before=before,
                        after=after,
                        detail=(
                            "removed known facts whose global fact kind does not "
                            f"match the question reference field: {','.join(dropped_ids)}"
                        ),
                    )
                )
            for field_name in fact_ids_by_question_field:
                before = list(question.get(field_name) or ())
                after = [
                    value
                    for value in before
                    if str(value) not in fact_by_id
                    or question_id
                    in set(
                        fact_by_id[str(value)].get("question_family_ids") or ()
                    )
                ]
                if after == before:
                    continue
                question[field_name] = after
                dropped_ids = tuple(
                    str(value) for value in before if value not in after
                )
                operations.append(
                    _operation(
                        "DROP_UNBOUND_QUESTION_FACT_REFERENCE",
                        "QUESTION_FAMILY_RESULT",
                        question_id,
                        field_name=field_name,
                        before=before,
                        after=after,
                        detail=(
                            "removed known facts that do not bind back to the "
                            f"question family: {','.join(dropped_ids)}"
                        ),
                    )
                )

        for lineage in normalized.get("source_lineages") or ():
            if isinstance(lineage, dict):
                _apply_field_aliases(
                    lineage,
                    _LINEAGE_FIELD_ALIASES,
                    object_type="SOURCE_LINEAGE",
                    object_id=str(
                        lineage.get("lineage_id")
                        or lineage.get("source_lineage_id")
                        or ""
                    ),
                    operations=operations,
                )
        for route in normalized.get("search_route_receipts") or ():
            if not isinstance(route, dict):
                continue
            rewritten: list[str] = []
            changed = False
            for url in route.get("opened_source_urls") or ():
                resolved = self.url_resolver.resolve(str(url))
                rewritten.append(resolved.canonical_url)
                changed = changed or resolved.changed
            if changed:
                before = route.get("opened_source_urls")
                route["opened_source_urls"] = list(dict.fromkeys(rewritten))
                operations.append(
                    _operation(
                        "CANONICALIZE_ROUTE_SOURCE_URLS",
                        "SEARCH_ROUTE_RECEIPT",
                        str(route.get("route_receipt_id") or ""),
                        field_name="opened_source_urls",
                        before=before,
                        after=route["opened_source_urls"],
                    )
                )
        _drop_invalid_question_route_references(normalized, operations)
        _downgrade_unproven_terminal_absence_claims(normalized, operations)
        return StaticPreflightNormalization(
            payload=normalized,
            before_hash=before_hash,
            after_hash=canonical_hash(normalized),
            operations=tuple(operations),
        )


def _drop_invalid_question_route_references(
    dossier: dict[str, Any],
    operations: list[PreflightOperation],
) -> None:
    """Remove route links that cannot prove the exact owning question.

    A route receipt is an audit record for one exact archetype/question pair.
    Reusing it as a convenient citation on another question overstates that
    second question's search coverage.  The safe mechanical projection keeps
    the global receipt and every fact untouched, but removes the foreign or
    unknown link and revokes adequate-search proof on the referencing row.
    """

    receipt_by_id = {
        str(row.get("route_receipt_id") or ""): row
        for row in dossier.get("search_route_receipts") or ()
        if isinstance(row, Mapping)
    }
    for question in dossier.get("question_family_results") or ():
        if not isinstance(question, dict):
            continue
        question_id = str(question.get("question_family_id") or "")
        archetype_id = str(question.get("archetype_id") or "")
        before = [
            str(value)
            for value in question.get("search_route_receipt_ids") or ()
        ]
        after: list[str] = []
        failure_codes: list[str] = []
        dropped_ids: list[str] = []
        for receipt_id in before:
            receipt = receipt_by_id.get(receipt_id)
            if receipt is None:
                failure_codes.append("UNKNOWN_ROUTE_RECEIPT")
                dropped_ids.append(receipt_id)
                continue
            if (
                str(receipt.get("question_family_id") or "") != question_id
                or str(receipt.get("archetype_id") or "") != archetype_id
            ):
                failure_codes.append("FOREIGN_QUESTION_ROUTE_RECEIPT")
                dropped_ids.append(receipt_id)
                continue
            if receipt_id in after:
                failure_codes.append("DUPLICATE_QUESTION_ROUTE_RECEIPT")
                dropped_ids.append(receipt_id)
                continue
            after.append(receipt_id)
        if after == before:
            continue

        adequate_before = question.get("adequate_search_proven")
        question["search_route_receipt_ids"] = after
        question["adequate_search_proven"] = False
        operations.append(
            _operation(
                "DROP_INVALID_QUESTION_ROUTE_REFERENCE",
                "QUESTION_FAMILY_RESULT",
                question_id,
                field_name="search_route_receipt_ids",
                before={
                    "route_receipt_ids": before,
                    "adequate_search_proven": adequate_before,
                },
                after={
                    "route_receipt_ids": after,
                    "adequate_search_proven": False,
                },
                detail=(
                    "failure_codes="
                    + ",".join(dict.fromkeys(failure_codes))
                    + ";dropped_ids="
                    + ",".join(dropped_ids)
                ),
            )
        )


def _downgrade_unproven_terminal_absence_claims(
    dossier: dict[str, Any],
    operations: list[PreflightOperation],
) -> None:
    """Turn unsupported absence/nonpublic assertions back into open research gaps.

    This is deliberately one-way and conservative.  It never invents an
    adequate-search proof or a ``no_new_route_reason``.  If the dossier claims
    terminal absence without the receipts required by the strict schema, the
    question remains usable only as ``PUBLIC_SEARCHABLE``.
    """

    receipts = tuple(
        row
        for row in dossier.get("search_route_receipts") or ()
        if isinstance(row, Mapping)
    )
    receipt_by_id = {
        str(row.get("route_receipt_id") or ""): row for row in receipts
    }
    downgraded_question_ids: list[str] = []
    for question in dossier.get("question_family_results") or ():
        if not isinstance(question, dict):
            continue
        status = str(question.get("status") or "")
        if status not in {
            "EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH",
            "LIKELY_NONPUBLIC",
        }:
            continue
        route_ids = tuple(
            str(value) for value in question.get("search_route_receipt_ids") or ()
        )
        linked = tuple(
            receipt_by_id[value] for value in route_ids if value in receipt_by_id
        )
        failure_codes: list[str] = []
        if question.get("adequate_search_proven") is not True:
            failure_codes.append("ADEQUATE_SEARCH_NOT_PROVEN")
        if len(route_ids) < 2:
            failure_codes.append("INSUFFICIENT_ROUTE_RECEIPTS")
        if len(linked) != len(route_ids):
            failure_codes.append("UNKNOWN_ROUTE_RECEIPT")
        if any(row.get("provider_status") != "SUCCESS" for row in linked):
            failure_codes.append("PROVIDER_OR_PARSER_NOT_SUCCESS")
        if status == "LIKELY_NONPUBLIC" and any(
            not str(row.get("no_new_route_reason") or "").strip()
            for row in linked
        ):
            failure_codes.append("MISSING_NO_NEW_ROUTE_REASON")
        if not failure_codes:
            continue

        question_id = str(question.get("question_family_id") or "")
        before = {
            "status": question.get("status"),
            "availability_class": question.get("availability_class"),
            "adequate_search_proven": question.get("adequate_search_proven"),
        }
        question["status"] = "PUBLIC_SEARCHABLE"
        question["availability_class"] = "PUBLIC_SEARCHABLE"
        question["adequate_search_proven"] = False
        after = {
            "status": question["status"],
            "availability_class": question["availability_class"],
            "adequate_search_proven": question["adequate_search_proven"],
        }
        operations.append(
            _operation(
                "DOWNGRADE_UNPROVEN_TERMINAL_ABSENCE_CLAIM",
                "QUESTION_FAMILY_RESULT",
                question_id,
                field_name="status",
                before=before,
                after=after,
                detail="failure_codes=" + ",".join(failure_codes),
            )
        )
        downgraded_question_ids.append(question_id)

    if not downgraded_question_ids:
        return
    reconciled_status = _research_status_after_terminal_downgrade(
        dossier,
        downgraded_question_ids=tuple(downgraded_question_ids),
    )
    before_status = dossier.get("research_status")
    if reconciled_status is None or before_status == reconciled_status:
        return
    dossier["research_status"] = reconciled_status
    operations.append(
        _operation(
            "RECONCILE_RESEARCH_STATUS_AFTER_TERMINAL_DOWNGRADE",
            "DOSSIER",
            str(dossier.get("job_id") or ""),
            field_name="research_status",
            before=before_status,
            after=reconciled_status,
            detail="downgraded_question_ids=" + ",".join(downgraded_question_ids),
        )
    )


def _research_status_after_terminal_downgrade(
    dossier: Mapping[str, Any],
    *,
    downgraded_question_ids: Sequence[str],
) -> str | None:
    try:
        bundle = select_contract_bundle(
            tuple(str(value) for value in dossier.get("selected_archetypes") or ())
        )
    except (KeyError, ValueError):
        # Unknown contract identity remains the strict schema validator's job.
        return None
    mandatory_ids = {
        str(question.get("question_family_id") or "")
        for contract in bundle.contracts
        for question in contract.get("question_families") or ()
        if question.get("mandatory_for_full_thesis") is True
    }
    if not mandatory_ids.intersection(downgraded_question_ids):
        return str(dossier.get("research_status") or "") or None
    mandatory_rows = tuple(
        row
        for row in dossier.get("question_family_results") or ()
        if isinstance(row, Mapping)
        and str(row.get("question_family_id") or "") in mandatory_ids
    )
    if any(
        row.get("status") in {"PROVIDER_PENDING", "PARSER_PENDING"}
        or row.get("availability_class") in {"PROVIDER_BLOCKED", "PARSER_BLOCKED"}
        for row in mandatory_rows
    ):
        return "PROVIDER_PENDING"
    if any(row.get("status") == "VERIFIER_REPAIR_REQUIRED" for row in mandatory_rows):
        return "NEEDS_VERIFIER_REPAIR"
    return "NEEDS_PUBLIC_GAP_CLOSURE"


def _normalize_initial_transport_aliases(
    dossier: dict[str, Any],
    operations: list[PreflightOperation],
) -> None:
    """Canonicalize only exact, self-consistent initial-pass transport aliases.

    The visible prompt uses ``NONE`` in its marker because a marker cannot
    carry JSON null, and Pro can copy that marker spelling into the dossier.
    Likewise, the initial conversation does not exist before submit and Pro
    can spell the required placeholder as ``PENDING_NEW_CONVERSATION``.  These
    values describe transport identity, not evidence.  Normalize them only
    when the top-level current pass has exactly one matching
    ``INITIAL_FULL_RESEARCH`` row whose parent uses the same null alias.
    Follow-up pass lineage remains fail-closed.
    """

    current_pass_id = str(dossier.get("research_pass_id") or "")
    rows = dossier.get("research_passes") or ()
    matching_rows = [
        row
        for row in rows
        if isinstance(row, dict)
        and str(row.get("pass_id") or "") == current_pass_id
        and str(row.get("pass_name") or "") == _INITIAL_PASS_NAME
        and _is_explicit_initial_null_parent(row)
    ]
    if (
        not current_pass_id
        or len(matching_rows) != 1
        or not _is_explicit_initial_null_parent(dossier)
    ):
        return

    if dossier["parent_pass_id"] is not None:
        dossier["parent_pass_id"] = None
        matching_rows[0]["parent_pass_id"] = None
        operations.append(
            _operation(
                "NORMALIZE_INITIAL_PARENT_PASS_NULL_ALIAS",
                "RESEARCH_PASS",
                current_pass_id,
                field_name="parent_pass_id",
                before="NONE",
                after=None,
            )
        )
    conversation_id = str(dossier.get("conversation_id") or "")
    if conversation_id in _INITIAL_CONVERSATION_PLACEHOLDER_ALIASES:
        dossier["conversation_id"] = _INITIAL_CONVERSATION_PLACEHOLDER
        operations.append(
            _operation(
                "NORMALIZE_INITIAL_CONVERSATION_PLACEHOLDER_ALIAS",
                "DOSSIER",
                str(dossier.get("job_id") or ""),
                field_name="conversation_id",
                before=conversation_id,
                after=_INITIAL_CONVERSATION_PLACEHOLDER,
            )
        )


def _is_explicit_initial_null_parent(value: Mapping[str, Any]) -> bool:
    if "parent_pass_id" not in value:
        return False
    parent = value.get("parent_pass_id")
    return parent is None or str(parent).upper() in _NULL_PARENT_PASS_ALIASES


class LocalEvidencePreflightService:
    def __init__(
        self,
        *,
        page_fetcher: PageFetcher | None = None,
        static_normalizer: PreSchemaV3Normalizer | None = None,
        issuer_alias_resolver: IssuerAliasResolver | None = None,
        scope_mapper: ClosedEnumScopeMapper | None = None,
        date_resolver: DatePrecedenceResolver | None = None,
        atomic_preflight: AtomicFactPreflight | None = None,
        classifier: RejectionClassifier | None = None,
    ) -> None:
        self.page_fetcher = page_fetcher or PageFetcher(
            live_enabled=False, max_text_chars=None
        )
        self.issuer_alias_resolver = issuer_alias_resolver or IssuerAliasResolver()
        self.scope_mapper = scope_mapper or ClosedEnumScopeMapper()
        self.static_normalizer = static_normalizer or PreSchemaV3Normalizer(
            issuer_alias_resolver=self.issuer_alias_resolver,
            scope_mapper=self.scope_mapper,
        )
        self.date_resolver = date_resolver or DatePrecedenceResolver()
        self.atomic_preflight = atomic_preflight or AtomicFactPreflight()
        self.classifier = classifier or RejectionClassifier()

    def run(
        self,
        *,
        dossier: Mapping[str, Any],
        target_id: str,
        company_name: str,
        target_aliases: Sequence[str],
        as_of_date: str,
        archetype_ids: Sequence[str],
        job_root: str | Path,
    ) -> EvidencePreflightResult:
        root = Path(job_root).resolve() / "verification/preflight"
        static = self.static_normalizer.normalize(
            dossier,
            archetype_ids=archetype_ids,
        )
        canonical = static.payload
        if canonical.get("schema_version") != DOSSIER_V3:
            receipt = self._receipt(
                applicable=False,
                canonical_dossier=canonical,
                verifier_dossier=canonical,
                operations=(),
                issues=(),
                representation_counts={},
            )
            self._persist(root, canonical, canonical, (), (), receipt)
            return EvidencePreflightResult(
                applicable=False,
                canonical_dossier=canonical,
                verifier_dossier=canonical,
                resolved_fact_documents={},
                operations=(),
                issues=(),
                receipt=receipt,
            )
        source_documents = tuple(canonical.get("source_documents") or ())
        source_by_id = {
            str(row.get("source_document_id") or ""): row
            for row in source_documents
        }
        facts_with_collections = tuple(
            (collection, fact)
            for collection in _FACT_COLLECTIONS
            for fact in canonical.get(collection) or ()
        )
        facts = tuple(fact for _, fact in facts_with_collections)
        representations = SourceRepresentationResolver(
            fetcher=self.page_fetcher
        ).resolve(
            source_documents=source_documents,
            facts=facts,
            as_of_date=as_of_date,
        )
        operations = list(static.operations)
        issues = [_local_issue(row) for row in static.operations]
        verifier = deepcopy(dict(canonical))
        projected_by_collection: dict[str, list[Mapping[str, Any]]] = {
            key: [] for key in _FACT_COLLECTIONS
        }
        for collection, fact in facts_with_collections:
            fact_id = str(fact.get("dossier_fact_id") or "")
            source_document_id = str(fact.get("source_document_id") or "")
            source_document = source_by_id.get(source_document_id)
            representation = representations.representations_by_fact_id.get(fact_id)
            if source_document is None or representation is None:
                failed = FetchResult(
                    url="",
                    ok=False,
                    reason="fact references an unresolved source document",
                )
                representation = ResolvedSourceRepresentation(
                    source_document_id=source_document_id,
                    lineage_id="",
                    requested_url="",
                    resolved_url="",
                    representation_source_document_id=source_document_id,
                    fetch_result=failed,
                    normalized_text="",
                    text_hash=None,
                )
                source_document = source_document or {}
            date_resolution = self.date_resolver.resolve(
                source_document=source_document,
                fetch_result=representation.fetch_result,
                as_of_date=as_of_date,
            )
            alias_resolution = self.issuer_alias_resolver.resolve(
                target_id=target_id,
                company_name=company_name,
                target_aliases=target_aliases,
                fact=fact,
                source_document=source_document,
                document_text=representation.normalized_text,
            )
            scope_mapping = self.scope_mapper.map_fact(
                fact=fact,
                source_document=source_document,
                archetype_ids=archetype_ids,
            )
            result = self.atomic_preflight.project_and_check(
                fact=fact,
                source_document=source_document,
                representation=representation,
                alias_resolution=alias_resolution,
                scope_mapping=scope_mapping,
                date_resolution=date_resolution,
                material=True,
            )
            projected_by_collection[collection].append(result.verifier_fact)
            operations.extend(result.operations)
            issues.extend(_local_issue(row) for row in result.operations)
            issues.extend(result.issues)
            if representation.fetch_result.url and (
                representation.resolved_url != representation.requested_url
            ):
                operation = _operation(
                    "RESOLVE_REDIRECT_FINAL_URL",
                    "SOURCE_DOCUMENT",
                    source_document_id,
                    field_name="canonical_url",
                    before=representation.requested_url,
                    after=representation.resolved_url,
                )
                operations.append(operation)
                issues.append(_local_issue(operation))
            if date_resolution.last_modified_ignored:
                operation = _operation(
                    "PUBLISHED_DATE_PRECEDES_HTTP_LAST_MODIFIED",
                    "SOURCE_DOCUMENT",
                    source_document_id,
                    field_name="publication_date",
                    detail=(
                        f"published={date_resolution.publication_date};"
                        f"last_modified={date_resolution.last_modified_date}"
                    ),
                )
                operations.append(operation)
                issues.append(_local_issue(operation))
        for collection, rows in projected_by_collection.items():
            verifier[collection] = rows
        receipt = self._receipt(
            applicable=True,
            canonical_dossier=canonical,
            verifier_dossier=verifier,
            operations=tuple(operations),
            issues=tuple(issues),
            representation_counts={
                "source_fetch_count": representations.attempted_url_count,
                "source_fetch_success_count": representations.successful_url_count,
                "redirect_resolution_count": representations.redirect_resolution_count,
                "alternate_representation_fact_count": (
                    representations.alternate_representation_fact_count
                ),
            },
        )
        self._persist(
            root,
            canonical,
            verifier,
            tuple(operations),
            tuple(issues),
            receipt,
        )
        return EvidencePreflightResult(
            applicable=True,
            canonical_dossier=canonical,
            verifier_dossier=verifier,
            resolved_fact_documents=(
                representations.representations_by_fact_id
            ),
            operations=tuple(operations),
            issues=tuple(issues),
            receipt=receipt,
        )

    def classify_verifications(
        self,
        *,
        preflight: EvidencePreflightResult,
        verification_rows: Sequence[Mapping[str, Any]],
    ) -> ClassifiedRejections:
        facts_by_id = {
            str(row.get("dossier_fact_id") or ""): row
            for collection in _FACT_COLLECTIONS
            for row in preflight.verifier_dossier.get(collection) or ()
        }
        material_ids = tuple(facts_by_id)
        return self.classifier.classify(
            verifications=verification_rows,
            facts_by_id=facts_by_id,
            preflight_issues=preflight.issues,
            material_fact_ids=material_ids,
        )

    @staticmethod
    def _receipt(
        *,
        applicable: bool,
        canonical_dossier: Mapping[str, Any],
        verifier_dossier: Mapping[str, Any],
        operations: Sequence[PreflightOperation],
        issues: Sequence[PreflightIssue],
        representation_counts: Mapping[str, int],
    ) -> Mapping[str, Any]:
        resolved_issues = tuple(row for row in issues if row.locally_resolved)
        unresolved_issues = tuple(row for row in issues if not row.locally_resolved)
        payload = {
            "schema_version": "e2r_local_evidence_preflight_receipt_v1",
            "semantics_version": PREFLIGHT_SEMANTICS_VERSION,
            "status": "PREFLIGHT_COMPLETE" if applicable else "LEGACY_NOT_APPLICABLE",
            "applicable": applicable,
            "canonical_dossier_hash": canonical_hash(canonical_dossier),
            "verifier_dossier_hash": canonical_hash(verifier_dossier),
            "operation_count": len(operations),
            "local_normalized_count": sum(
                row.operation_code
                not in {
                    "RESOLVE_REDIRECT_FINAL_URL",
                    "PUBLISHED_DATE_PRECEDES_HTTP_LAST_MODIFIED",
                }
                for row in operations
            ),
            "source_representation_resolved_count": sum(
                row.cause_class
                is RejectionRootCauseClass.SOURCE_REPRESENTATION_RESOLVABLE
                and row.locally_resolved
                for row in issues
            ),
            "resolved_issue_count": len(resolved_issues),
            "unresolved_issue_count": len(unresolved_issues),
            "local_normalizable_sent_to_pro_count": 0,
            "source_representation_sent_to_pro_count": 0,
            "query_count": 0,
            "search_count": 0,
            "score_authority": False,
            "stage_authority": False,
            **dict(representation_counts),
        }
        return {**payload, "receipt_hash": canonical_hash(payload)}

    @staticmethod
    def _persist(
        root: Path,
        canonical: Mapping[str, Any],
        verifier: Mapping[str, Any],
        operations: Sequence[PreflightOperation],
        issues: Sequence[PreflightIssue],
        receipt: Mapping[str, Any],
    ) -> None:
        _write_atomic(
            root / "research_dossier.preflight.json",
            canonical_json(canonical) + "\n",
        )
        _write_atomic(
            root / "verifier_projection.json",
            canonical_json(verifier) + "\n",
        )
        _write_atomic(
            root / "preflight_operations.jsonl",
            "".join(canonical_json(row.to_dict()) + "\n" for row in operations),
        )
        _write_atomic(
            root / "preflight_issues.jsonl",
            "".join(canonical_json(row.to_dict()) + "\n" for row in issues),
        )
        _write_atomic(root / "preflight_receipt.json", canonical_json(receipt) + "\n")


def _apply_field_aliases(
    row: dict[str, Any],
    aliases: Mapping[str, str],
    *,
    object_type: str,
    object_id: str,
    operations: list[PreflightOperation],
) -> None:
    for alias, canonical in aliases.items():
        if alias not in row:
            continue
        alias_value = row[alias]
        if canonical in row and row[canonical] != alias_value:
            raise ValueError(
                f"conflicting V3 field alias {alias!r}/{canonical!r}: {object_id}"
            )
        if canonical not in row:
            row[canonical] = alias_value
        row.pop(alias)
        operations.append(
            _operation(
                "MAP_V2_V3_FIELD_ALIAS",
                object_type,
                object_id,
                field_name=canonical,
                before={alias: alias_value},
                after={canonical: alias_value},
            )
        )


def _normalize_text_fields(
    row: dict[str, Any],
    fields: Sequence[str],
    *,
    object_type: str,
    object_id: str,
    normalizer: TextQuoteNormalizer,
    operations: list[PreflightOperation],
) -> None:
    for field in fields:
        if field not in row or not isinstance(row[field], str):
            continue
        before = row[field]
        result = normalizer.normalize_text(before)
        if result.normalized_text != before:
            row[field] = result.normalized_text
            operations.append(
                _operation(
                    "+".join(result.operations),
                    object_type,
                    object_id,
                    field_name=field,
                    before=before,
                    after=result.normalized_text,
                )
            )


def _consume_identity_aliases(
    payload: dict[str, Any], key: str
) -> Mapping[str, str]:
    raw = payload.pop(key, {})
    if not raw:
        return {}
    if not isinstance(raw, Mapping):
        raise ValueError(f"{key} must be an alias-to-canonical object")
    aliases = {str(alias): str(canonical) for alias, canonical in raw.items()}
    if any(not alias or not canonical or alias == canonical for alias, canonical in aliases.items()):
        raise ValueError(f"{key} contains an invalid identity alias")
    return aliases


def _rewrite_exact_values(value: Any, aliases: Mapping[str, str]) -> Any:
    if isinstance(value, Mapping):
        return {
            key: _rewrite_exact_values(child, aliases)
            for key, child in value.items()
        }
    if isinstance(value, list):
        return [_rewrite_exact_values(child, aliases) for child in value]
    if isinstance(value, str):
        return aliases.get(value, value)
    return value


def _operation(
    code: str,
    object_type: str,
    object_id: str,
    *,
    field_name: str | None = None,
    before: object | None = None,
    after: object | None = None,
    detail: str | None = None,
) -> PreflightOperation:
    return PreflightOperation(
        operation_code=code,
        object_type=object_type,
        object_id=object_id,
        field_name=field_name,
        before_hash=canonical_hash(before) if before is not None else None,
        after_hash=canonical_hash(after) if after is not None else None,
        detail=detail,
    )


def _local_issue(operation: PreflightOperation) -> PreflightIssue:
    return PreflightIssue(
        issue_id=stable_id(
            "PREFLIGHTISSUE",
            {
                "operation": operation.operation_code,
                "object_type": operation.object_type,
                "object_id": operation.object_id,
                "field": operation.field_name,
            },
        ),
        candidate_id=(
            operation.object_id if operation.object_type == "ATOMIC_FACT" else None
        ),
        source_document_id=(
            operation.object_id
            if operation.object_type == "SOURCE_DOCUMENT"
            else None
        ),
        cause_class=RejectionRootCauseClass.LOCAL_NORMALIZABLE,
        cause_code=operation.operation_code,
        detail=operation.detail or "deterministic local normalization applied",
        routing=RejectionRouting.LOCAL_FIX_AND_REVERIFY,
        locally_resolved=True,
        material=operation.object_type == "ATOMIC_FACT",
    )


def _write_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_suffix(path.suffix + f".{os.getpid()}.part")
    try:
        with part.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(part, path)
        fsync_directory(path.parent)
    finally:
        part.unlink(missing_ok=True)


__all__ = [
    "DOSSIER_V3",
    "LocalEvidencePreflightService",
    "PREFLIGHT_SEMANTICS_VERSION",
    "PreSchemaV3Normalizer",
]
