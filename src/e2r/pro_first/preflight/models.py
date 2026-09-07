"""Typed receipts for the local Evidence Preflight boundary."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Mapping

from e2r.research.page_fetcher import FetchResult


class RejectionRootCauseClass(str, Enum):
    LOCAL_NORMALIZABLE = "LOCAL_NORMALIZABLE"
    SOURCE_REPRESENTATION_RESOLVABLE = "SOURCE_REPRESENTATION_RESOLVABLE"
    INITIAL_PROMPT_OUTPUT_DEFECT = "INITIAL_PROMPT_OUTPUT_DEFECT"
    GENUINE_SEMANTIC_OR_SOURCE_DEFECT = "GENUINE_SEMANTIC_OR_SOURCE_DEFECT"
    NONMATERIAL_AUXILIARY_REJECTION = "NONMATERIAL_AUXILIARY_REJECTION"


class RejectionRouting(str, Enum):
    LOCAL_FIX_AND_REVERIFY = "LOCAL_FIX_AND_REVERIFY"
    ALTERNATE_REPRESENTATION_AND_REVERIFY = (
        "ALTERNATE_REPRESENTATION_AND_REVERIFY"
    )
    COMPACT_PRO_REPAIR_ALLOWED = "COMPACT_PRO_REPAIR_ALLOWED"
    DIAGNOSTICS_ONLY = "DIAGNOSTICS_ONLY"


@dataclass(frozen=True)
class PreflightOperation:
    operation_code: str
    object_type: str
    object_id: str
    field_name: str | None = None
    before_hash: str | None = None
    after_hash: str | None = None
    detail: str | None = None

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class PreflightIssue:
    issue_id: str
    candidate_id: str | None
    source_document_id: str | None
    cause_class: RejectionRootCauseClass
    cause_code: str
    detail: str
    routing: RejectionRouting
    locally_resolved: bool
    material: bool
    verifier_status: str | None = None

    @property
    def send_to_pro_allowed(self) -> bool:
        return self.routing is RejectionRouting.COMPACT_PRO_REPAIR_ALLOWED

    def to_dict(self) -> Mapping[str, Any]:
        return {
            **asdict(self),
            "cause_class": self.cause_class.value,
            "routing": self.routing.value,
            "send_to_pro_allowed": self.send_to_pro_allowed,
        }


@dataclass(frozen=True)
class ResolvedSourceRepresentation:
    source_document_id: str
    lineage_id: str
    requested_url: str
    resolved_url: str
    representation_source_document_id: str
    fetch_result: FetchResult
    normalized_text: str
    text_hash: str | None
    quote_match_mode: str | None = None
    alternate_representation_used: bool = False

    @property
    def available(self) -> bool:
        return bool(self.fetch_result.ok and self.normalized_text.strip())

    def to_receipt_dict(self) -> Mapping[str, Any]:
        return {
            "source_document_id": self.source_document_id,
            "lineage_id": self.lineage_id,
            "requested_url": self.requested_url,
            "resolved_url": self.resolved_url,
            "representation_source_document_id": (
                self.representation_source_document_id
            ),
            "available": self.available,
            "text_hash": self.text_hash,
            "quote_match_mode": self.quote_match_mode,
            "alternate_representation_used": (
                self.alternate_representation_used
            ),
            "fetch_reason": self.fetch_result.reason,
            "content_type": self.fetch_result.content_type,
            "text_complete": self.fetch_result.text_complete,
            "response_last_modified_at": (
                self.fetch_result.response_last_modified_at.isoformat()
                if self.fetch_result.response_last_modified_at is not None
                else None
            ),
        }


@dataclass(frozen=True)
class StaticPreflightNormalization:
    payload: Mapping[str, Any]
    before_hash: str
    after_hash: str
    operations: tuple[PreflightOperation, ...]


@dataclass(frozen=True)
class EvidencePreflightResult:
    applicable: bool
    canonical_dossier: Mapping[str, Any]
    verifier_dossier: Mapping[str, Any]
    resolved_fact_documents: Mapping[str, ResolvedSourceRepresentation]
    operations: tuple[PreflightOperation, ...]
    issues: tuple[PreflightIssue, ...]
    receipt: Mapping[str, Any]


__all__ = [
    "EvidencePreflightResult",
    "PreflightIssue",
    "PreflightOperation",
    "RejectionRootCauseClass",
    "RejectionRouting",
    "ResolvedSourceRepresentation",
    "StaticPreflightNormalization",
]
