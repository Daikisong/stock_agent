"""Atomic fact projection and deterministic pre-verifier checks."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from ..ids import canonical_hash, stable_id
from .date_resolver import DatePrecedenceResolution
from .issuer_alias import IssuerAliasResolution
from .models import (
    PreflightIssue,
    PreflightOperation,
    RejectionRootCauseClass,
    RejectionRouting,
    ResolvedSourceRepresentation,
)
from .scope_mapper import ClosedScopeMapping


_TRUE_PREFLIGHT_FIELDS = (
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


@dataclass(frozen=True)
class AtomicFactPreflightResult:
    verifier_fact: Mapping[str, Any]
    operations: tuple[PreflightOperation, ...]
    issues: tuple[PreflightIssue, ...]


@dataclass(frozen=True)
class CompoundFactSplitResult:
    facts: tuple[Mapping[str, Any], ...]
    deterministically_separable: bool
    rejection_code: str | None


class AtomicFactPreflight:
    def project_and_check(
        self,
        *,
        fact: Mapping[str, Any],
        source_document: Mapping[str, Any],
        representation: ResolvedSourceRepresentation,
        alias_resolution: IssuerAliasResolution,
        scope_mapping: ClosedScopeMapping,
        date_resolution: DatePrecedenceResolution,
        material: bool,
    ) -> AtomicFactPreflightResult:
        fact_id = str(fact.get("dossier_fact_id") or "")
        source_document_id = str(fact.get("source_document_id") or "")
        projected = deepcopy(dict(fact))
        operations: list[PreflightOperation] = []
        issues: list[PreflightIssue] = []

        _replace_field(
            projected,
            "business_segment",
            scope_mapping.business_segment,
            "MAP_SEGMENT_CLOSED_ENUM",
            fact_id,
            operations,
        )
        _replace_field(
            projected,
            "product_family",
            scope_mapping.product_family,
            "MAP_PRODUCT_CLOSED_ENUM",
            fact_id,
            operations,
        )
        projected.update(
            {
                "predicate": str(fact.get("predicate_id") or ""),
                "economic_mechanism": str(
                    fact.get("economic_mechanism_id") or ""
                ),
                "candidate_components": list(
                    fact.get("candidate_component_ids") or ()
                ),
                "source_url": representation.resolved_url
                or str(source_document.get("canonical_url") or ""),
                "source_title": str(source_document.get("source_title") or ""),
                "source_publisher": alias_resolution.canonical_publisher,
                "published_at": date_resolution.effective_publication_date,
                "source_role_ids": list(
                    source_document.get("source_role_ids") or ()
                ),
                "source_lineage_id": str(source_document.get("lineage_id") or ""),
                "preflight_subject_aliases": list(
                    alias_resolution.subject_aliases
                ),
                "period": (
                    fact.get("period")
                    or fact.get("event_date")
                    or date_resolution.effective_publication_date
                ),
            }
        )
        if str(projected.get("current_status") or "") == "HISTORICAL_ONLY":
            projected["current_status"] = "HISTORICAL"
            operations.append(
                _operation(
                    "MAP_V3_HISTORICAL_ONLY_TO_VERIFIER_ENUM",
                    fact_id,
                    "current_status",
                    "HISTORICAL_ONLY",
                    "HISTORICAL",
                )
            )

        preflight = fact.get("verifier_preflight") or {}
        failed_fields = [
            key for key in _TRUE_PREFLIGHT_FIELDS if preflight.get(key) is not True
        ]
        if preflight.get("derived_calculation_mixed_into_fact") is not False:
            failed_fields.append("derived_calculation_mixed_into_fact")
        if failed_fields:
            issues.append(
                _issue(
                    fact_id,
                    source_document_id,
                    RejectionRootCauseClass.INITIAL_PROMPT_OUTPUT_DEFECT,
                    "FAILED_VERIFIER_PREFLIGHT",
                    "Initial V3 candidate failed: " + ",".join(failed_fields),
                    material=material,
                )
            )
        if not fact.get("question_family_ids"):
            issues.append(
                _issue(
                    fact_id,
                    source_document_id,
                    RejectionRootCauseClass.INITIAL_PROMPT_OUTPUT_DEFECT,
                    "MISSING_QUESTION_BINDING",
                    "atomic fact has no question family binding",
                    material=material,
                )
            )
        if len(str(fact.get("supporting_excerpt") or "").strip()) < 8:
            issues.append(
                _issue(
                    fact_id,
                    source_document_id,
                    RejectionRootCauseClass.INITIAL_PROMPT_OUTPUT_DEFECT,
                    "QUOTE_TOO_SHORT",
                    "exact supporting excerpt is shorter than eight characters",
                    material=material,
                )
            )
        if not date_resolution.accepted:
            issues.append(
                _issue(
                    fact_id,
                    source_document_id,
                    RejectionRootCauseClass.INITIAL_PROMPT_OUTPUT_DEFECT,
                    date_resolution.status,
                    "source date failed the deterministic as-of preflight",
                    material=material,
                )
            )
        if not representation.available:
            issues.append(
                _issue(
                    fact_id,
                    source_document_id,
                    RejectionRootCauseClass.GENUINE_SEMANTIC_OR_SOURCE_DEFECT,
                    "SOURCE_REPRESENTATION_UNRESOLVED",
                    "canonical/opened/same-lineage official representations were unavailable",
                    material=material,
                )
            )
        elif representation.quote_match_mode is None:
            issues.append(
                _issue(
                    fact_id,
                    source_document_id,
                    RejectionRootCauseClass.GENUINE_SEMANTIC_OR_SOURCE_DEFECT,
                    "LITERAL_QUOTE_UNRESOLVED",
                    "quote did not match any attempted official representation literally",
                    material=material,
                )
            )
        elif representation.alternate_representation_used:
            issues.append(
                PreflightIssue(
                    issue_id=stable_id(
                        "PREFLIGHTISSUE",
                        {
                            "candidate_id": fact_id,
                            "code": "ALTERNATE_OFFICIAL_REPRESENTATION_RESOLVED",
                        },
                    ),
                    candidate_id=fact_id,
                    source_document_id=source_document_id,
                    cause_class=(
                        RejectionRootCauseClass.SOURCE_REPRESENTATION_RESOLVABLE
                    ),
                    cause_code="ALTERNATE_OFFICIAL_REPRESENTATION_RESOLVED",
                    detail="same-lineage official representation supplied the exact quote",
                    routing=(
                        RejectionRouting.ALTERNATE_REPRESENTATION_AND_REVERIFY
                    ),
                    locally_resolved=True,
                    material=material,
                )
            )
        blocking = tuple(
            row
            for row in issues
            if not row.locally_resolved
            and row.cause_class
            is RejectionRootCauseClass.INITIAL_PROMPT_OUTPUT_DEFECT
        )
        if blocking:
            projected["preflight_blocked_reason"] = ";".join(
                row.cause_code for row in blocking
            )
        return AtomicFactPreflightResult(
            verifier_fact=projected,
            operations=tuple(operations),
            issues=tuple(issues),
        )


def split_compound_fact(fact: Mapping[str, Any]) -> CompoundFactSplitResult:
    """Split only explicit structured parts with their own literal quote span."""

    preflight = fact.get("verifier_preflight") or {}
    if preflight.get("single_atomic_predicate") is True:
        return CompoundFactSplitResult((dict(fact),), True, None)
    parts = fact.get("atomic_parts")
    source_excerpt = str(fact.get("supporting_excerpt") or "")
    if not isinstance(parts, Sequence) or isinstance(parts, (str, bytes)):
        return CompoundFactSplitResult(
            (), False, "GENUINE_SEMANTIC_OR_SOURCE_DEFECT"
        )
    split: list[Mapping[str, Any]] = []
    for index, part in enumerate(parts, 1):
        if not isinstance(part, Mapping):
            return CompoundFactSplitResult(
                (), False, "GENUINE_SEMANTIC_OR_SOURCE_DEFECT"
            )
        statement = str(part.get("statement") or "").strip()
        predicate = str(part.get("predicate_id") or "").strip()
        excerpt = str(part.get("supporting_excerpt") or "").strip()
        if (
            not statement
            or not predicate
            or len(excerpt) < 8
            or excerpt not in source_excerpt
        ):
            return CompoundFactSplitResult(
                (), False, "GENUINE_SEMANTIC_OR_SOURCE_DEFECT"
            )
        row = deepcopy(dict(fact))
        row.pop("atomic_parts", None)
        row["dossier_fact_id"] = f"{fact.get('dossier_fact_id')}:{index}"
        row["statement"] = statement
        row["predicate_id"] = predicate
        row["supporting_excerpt"] = excerpt
        row["verifier_preflight"] = {
            **dict(preflight),
            "single_atomic_predicate": True,
            "exact_excerpt_copied_from_source": True,
        }
        split.append(row)
    if len(split) < 2:
        return CompoundFactSplitResult(
            (), False, "GENUINE_SEMANTIC_OR_SOURCE_DEFECT"
        )
    return CompoundFactSplitResult(tuple(split), True, None)


def _replace_field(
    payload: dict[str, Any],
    field_name: str,
    replacement: str,
    operation_code: str,
    fact_id: str,
    operations: list[PreflightOperation],
) -> None:
    before = str(payload.get(field_name) or "")
    if replacement and replacement != before:
        payload[field_name] = replacement
        operations.append(
            _operation(
                operation_code,
                fact_id,
                field_name,
                before,
                replacement,
            )
        )


def _operation(
    code: str,
    object_id: str,
    field: str,
    before: object,
    after: object,
) -> PreflightOperation:
    return PreflightOperation(
        operation_code=code,
        object_type="ATOMIC_FACT",
        object_id=object_id,
        field_name=field,
        before_hash=canonical_hash(before),
        after_hash=canonical_hash(after),
    )


def _issue(
    candidate_id: str,
    source_document_id: str,
    cause_class: RejectionRootCauseClass,
    code: str,
    detail: str,
    *,
    material: bool,
) -> PreflightIssue:
    return PreflightIssue(
        issue_id=stable_id(
            "PREFLIGHTISSUE",
            {"candidate_id": candidate_id, "code": code},
        ),
        candidate_id=candidate_id,
        source_document_id=source_document_id,
        cause_class=cause_class,
        cause_code=code,
        detail=detail,
        routing=RejectionRouting.COMPACT_PRO_REPAIR_ALLOWED,
        locally_resolved=False,
        material=material,
    )


__all__ = [
    "AtomicFactPreflight",
    "AtomicFactPreflightResult",
    "CompoundFactSplitResult",
    "split_compound_fact",
]
