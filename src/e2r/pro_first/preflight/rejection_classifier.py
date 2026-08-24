"""Exhaustive verifier rejection root-cause classification and routing."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from ..ids import stable_id
from .models import (
    PreflightIssue,
    RejectionRootCauseClass,
    RejectionRouting,
)


_NON_REJECTION_STATUSES = frozenset(
    {
        "ACCEPTED_CURRENT",
        "ACCEPTED_COUNTER",
        "ACCEPTED_RESOLUTION",
        "HISTORICAL_ONLY",
        "SUPERSEDED",
    }
)


@dataclass(frozen=True)
class ClassifiedRejections:
    rows: tuple[PreflightIssue, ...]
    root_cause_counts: Mapping[str, int]
    local_normalizable_sent_to_pro_count: int
    source_representation_sent_to_pro_count: int
    unclassified_rejection_count: int


class RejectionClassifier:
    def classify(
        self,
        *,
        verifications: Sequence[Mapping[str, Any]],
        facts_by_id: Mapping[str, Mapping[str, Any]],
        preflight_issues: Sequence[PreflightIssue] = (),
        material_fact_ids: Sequence[str] = (),
    ) -> ClassifiedRejections:
        material_ids = set(str(value) for value in material_fact_ids)
        unresolved_preflight = {
            str(row.candidate_id): row
            for row in preflight_issues
            if row.candidate_id and not row.locally_resolved
        }
        rows: list[PreflightIssue] = []
        unclassified = 0
        for verification in verifications:
            status = str(verification.get("status") or "")
            if status in _NON_REJECTION_STATUSES:
                continue
            candidate_id = str(verification.get("dossier_fact_id") or "")
            fact = facts_by_id.get(candidate_id) or {}
            material = candidate_id in material_ids
            if not material:
                row = self._row(
                    candidate_id,
                    fact,
                    status,
                    RejectionRootCauseClass.NONMATERIAL_AUXILIARY_REJECTION,
                    "NONMATERIAL_VERIFIER_REJECTION",
                    "nonmaterial auxiliary candidate remains diagnostic only",
                    RejectionRouting.DIAGNOSTICS_ONLY,
                    material=False,
                )
            elif candidate_id in unresolved_preflight:
                prior = unresolved_preflight[candidate_id]
                row = PreflightIssue(
                    issue_id=prior.issue_id,
                    candidate_id=prior.candidate_id,
                    source_document_id=prior.source_document_id,
                    cause_class=prior.cause_class,
                    cause_code=prior.cause_code,
                    detail=prior.detail,
                    routing=prior.routing,
                    locally_resolved=False,
                    material=True,
                    verifier_status=status,
                )
            else:
                row = self._classify_status(
                    candidate_id=candidate_id,
                    fact=fact,
                    status=status,
                    reason=str(verification.get("reason") or ""),
                )
            if not row.cause_class.value:
                unclassified += 1
            rows.append(row)
        counts = {
            cause.value: sum(row.cause_class is cause for row in rows)
            for cause in RejectionRootCauseClass
        }
        return ClassifiedRejections(
            rows=tuple(rows),
            root_cause_counts=counts,
            local_normalizable_sent_to_pro_count=sum(
                row.send_to_pro_allowed
                and row.cause_class is RejectionRootCauseClass.LOCAL_NORMALIZABLE
                for row in rows
            ),
            source_representation_sent_to_pro_count=sum(
                row.send_to_pro_allowed
                and row.cause_class
                is RejectionRootCauseClass.SOURCE_REPRESENTATION_RESOLVABLE
                for row in rows
            ),
            unclassified_rejection_count=unclassified,
        )

    def _classify_status(
        self,
        *,
        candidate_id: str,
        fact: Mapping[str, Any],
        status: str,
        reason: str,
    ) -> PreflightIssue:
        source_document_id = str(fact.get("source_document_id") or "")
        if status == "REJECTED_FUTURE":
            cause = RejectionRootCauseClass.INITIAL_PROMPT_OUTPUT_DEFECT
            code = "INITIAL_FUTURE_SOURCE"
        elif status == "UNVERIFIED_PENDING" and (
            not fact.get("period")
            or str(fact.get("current_status") or "") in {"", "UNKNOWN"}
        ):
            cause = RejectionRootCauseClass.INITIAL_PROMPT_OUTPUT_DEFECT
            code = "INITIAL_REQUIRED_FIELD_MISSING"
        elif status in {
            "REJECTED_SOURCE_UNAVAILABLE",
            "REJECTED_SNIPPET_ONLY",
            "REJECTED_QUOTE_MISMATCH",
            "REJECTED_WRONG_SUBJECT",
            "REJECTED_WRONG_SEGMENT",
            "REJECTED_WRONG_PRODUCT",
            "UNVERIFIED_PENDING",
        }:
            cause = RejectionRootCauseClass.GENUINE_SEMANTIC_OR_SOURCE_DEFECT
            code = {
                "REJECTED_SOURCE_UNAVAILABLE": "SOURCE_UNAVAILABLE_AFTER_LOCAL_ATTEMPTS",
                "REJECTED_SNIPPET_ONLY": "FULL_DOCUMENT_UNAVAILABLE",
                "REJECTED_QUOTE_MISMATCH": "LITERAL_QUOTE_MISMATCH_AFTER_LOCAL_ATTEMPTS",
                "REJECTED_WRONG_SUBJECT": "SUBJECT_SCOPE_MISMATCH_AFTER_ALIAS_RESOLUTION",
                "REJECTED_WRONG_SEGMENT": "SEGMENT_SCOPE_MISMATCH_AFTER_ENUM_MAPPING",
                "REJECTED_WRONG_PRODUCT": "PRODUCT_SCOPE_MISMATCH_AFTER_ENUM_MAPPING",
                "UNVERIFIED_PENDING": "VERIFIER_PENDING_AFTER_LOCAL_PREFLIGHT",
            }[status]
        else:
            cause = RejectionRootCauseClass.GENUINE_SEMANTIC_OR_SOURCE_DEFECT
            code = "UNKNOWN_VERIFIER_REJECTION_STATUS"
        return self._row(
            candidate_id,
            fact,
            status,
            cause,
            code,
            reason or status,
            RejectionRouting.COMPACT_PRO_REPAIR_ALLOWED,
            material=True,
        )

    @staticmethod
    def _row(
        candidate_id: str,
        fact: Mapping[str, Any],
        status: str,
        cause: RejectionRootCauseClass,
        code: str,
        detail: str,
        routing: RejectionRouting,
        *,
        material: bool,
    ) -> PreflightIssue:
        return PreflightIssue(
            issue_id=stable_id(
                "PREFLIGHTISSUE",
                {
                    "candidate_id": candidate_id,
                    "status": status,
                    "code": code,
                },
            ),
            candidate_id=candidate_id,
            source_document_id=str(fact.get("source_document_id") or ""),
            cause_class=cause,
            cause_code=code,
            detail=detail,
            routing=routing,
            locally_resolved=False,
            material=material,
            verifier_status=status,
        )


__all__ = ["ClassifiedRejections", "RejectionClassifier"]
