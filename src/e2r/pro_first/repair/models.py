"""Typed, authority-safe records for the Pro verifier-repair loop."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping

from ..ids import canonical_hash


REJECTION_CATEGORIES = frozenset(
    {
        "QUOTE_MISMATCH",
        "WRONG_SUBJECT",
        "WRONG_TARGET",
        "WRONG_SEGMENT",
        "WRONG_PRODUCT",
        "FUTURE_SOURCE",
        "SNIPPET_ONLY",
        "SOURCE_UNAVAILABLE",
        "DATE_UNRESOLVED",
        "DUPLICATE_LINEAGE",
        "UNSUPPORTED_DERIVATION",
    }
)
REPAIR_ACTIONS = frozenset({"CORRECTED", "REPLACED", "NARROWED", "WITHDRAWN"})
REVERIFIED_ACCEPTED_STATUSES = frozenset(
    {"ACCEPTED_CURRENT", "ACCEPTED_COUNTER", "ACCEPTED_RESOLUTION"}
)


@dataclass(frozen=True)
class VerifierRejectionPacket:
    packet_id: str
    job_id: str
    conversation_id: str
    candidate_id: str
    question_family_ids: tuple[str, ...]
    rejection_category: str
    verifier_status: str
    verifier_reason: str
    source_url: str
    source_id: str
    content_hash: str | None
    document_path: str | None
    fetched_source_excerpt: str
    fetched_source_excerpt_hash: str | None
    original_candidate: Mapping[str, Any]
    original_candidate_hash: str
    material: bool = True
    status: str = "REPAIR_REQUIRED"
    score_authority: bool = False
    stage_authority: bool = False

    def __post_init__(self) -> None:
        if self.rejection_category not in REJECTION_CATEGORIES:
            raise ValueError("unknown verifier rejection category")
        if self.status != "REPAIR_REQUIRED":
            raise ValueError("rejection packet must remain repair-required")
        if not self.material:
            raise ValueError("repair packets are only issued for material facts")
        if not self.question_family_ids:
            raise ValueError("material repair packet requires a question-family binding")
        if len(self.question_family_ids) != len(set(self.question_family_ids)):
            raise ValueError("repair packet question-family ids must be unique")
        if self.original_candidate.get("dossier_fact_id") != self.candidate_id:
            raise ValueError("repair packet candidate identity mismatch")
        if canonical_hash(self.original_candidate) != self.original_candidate_hash:
            raise ValueError("repair packet original candidate hash mismatch")
        if self.fetched_source_excerpt:
            if self.fetched_source_excerpt_hash != canonical_hash(
                {"excerpt": self.fetched_source_excerpt}
            ):
                raise ValueError("repair packet source excerpt hash mismatch")
        elif self.fetched_source_excerpt_hash is not None:
            raise ValueError("empty source excerpt cannot declare a hash")
        if self.score_authority or self.stage_authority:
            raise ValueError("repair packets cannot own score or Stage authority")

    def to_dict(self) -> Mapping[str, Any]:
        payload = asdict(self)
        payload["schema_version"] = "e2r_pro_verifier_rejection_packet_v1"
        payload["question_family_ids"] = list(self.question_family_ids)
        payload["original_candidate"] = dict(self.original_candidate)
        payload["score_authority"] = False
        payload["stage_authority"] = False
        return payload

    def to_prompt_dict(self) -> Mapping[str, Any]:
        """Return only source-backed repair inputs, never score/Stage output."""

        return {
            "packet_id": self.packet_id,
            "candidate_id": self.candidate_id,
            "question_family_ids": list(self.question_family_ids),
            "rejection_category": self.rejection_category,
            "verifier_status": self.verifier_status,
            "verifier_reason": self.verifier_reason,
            "source_url": self.source_url,
            "source_id": self.source_id,
            "content_hash": self.content_hash,
            "fetched_source_excerpt": self.fetched_source_excerpt,
            "original_candidate": dict(self.original_candidate),
            "allowed_actions": sorted(REPAIR_ACTIONS),
            "accepted_fact_deletion_allowed": False,
            "deterministic_reverification_required": True,
        }


@dataclass(frozen=True)
class RepairActionDecision:
    packet_id: str
    candidate_id: str
    question_family_ids: tuple[str, ...]
    action: str
    replacement_candidate_id: str | None
    action_hash: str

    def __post_init__(self) -> None:
        if self.action not in REPAIR_ACTIONS:
            raise ValueError("unknown verifier repair action")
        if (self.action == "WITHDRAWN") != (self.replacement_candidate_id is None):
            raise ValueError("only WITHDRAWN may omit a replacement candidate")


@dataclass(frozen=True)
class RepairApplication:
    effective_dossier: Mapping[str, Any]
    actions: tuple[RepairActionDecision, ...]
    unhandled_packet_ids: tuple[str, ...]
    accepted_candidate_ids_preserved: tuple[str, ...]
    delta_hash: str


@dataclass(frozen=True)
class RepairResolution:
    packet_id: str
    candidate_id: str
    replacement_candidate_id: str | None
    action: str
    status: str
    verifier_status: str | None
    verifier_reason: str
    resolved: bool


@dataclass(frozen=True)
class VerifierRepairReceipt:
    job_id: str
    conversation_id: str
    research_pass_id: str
    parent_pass_id: str
    rejection_packet_ids: tuple[str, ...]
    resolutions: tuple[RepairResolution, ...]
    unresolved_packet_ids: tuple[str, ...]
    prior_accepted_candidate_ids: tuple[str, ...]
    preserved_accepted_candidate_ids: tuple[str, ...]
    source_verification_hash: str
    effective_dossier_hash: str
    delta_hash: str
    score_valid: bool = False
    publication_withheld: bool = True

    def __post_init__(self) -> None:
        if set(self.prior_accepted_candidate_ids) != set(
            self.preserved_accepted_candidate_ids
        ):
            raise ValueError("repair loop deleted or replaced an accepted fact")
        if self.score_valid or not self.publication_withheld:
            raise ValueError("repair receipt cannot authorize score/publication")

    @property
    def material_rejection_unresolved_count(self) -> int:
        return len(self.unresolved_packet_ids)

    @property
    def receipt_hash(self) -> str:
        return canonical_hash(self.to_dict(include_hash=False))

    def to_dict(self, *, include_hash: bool = True) -> Mapping[str, Any]:
        payload: dict[str, Any] = {
            "schema_version": "e2r_pro_verifier_repair_receipt_v1",
            "status": (
                "VERIFIER_REPAIR_COMPLETE"
                if not self.unresolved_packet_ids
                else "VERIFIER_REPAIR_REQUIRED"
            ),
            "job_id": self.job_id,
            "conversation_id": self.conversation_id,
            "research_pass_id": self.research_pass_id,
            "parent_pass_id": self.parent_pass_id,
            "rejection_packet_ids": list(self.rejection_packet_ids),
            "resolutions": [asdict(row) for row in self.resolutions],
            "unresolved_packet_ids": list(self.unresolved_packet_ids),
            "material_rejection_unresolved_count": (
                self.material_rejection_unresolved_count
            ),
            "reverified_accepted_count": sum(
                row.status == "REVERIFIED_ACCEPTED" for row in self.resolutions
            ),
            "reverified_rejected_count": sum(
                row.status == "REVERIFIED_REJECTED" for row in self.resolutions
            ),
            "withdrawn_count": sum(
                row.status == "WITHDRAWN" for row in self.resolutions
            ),
            "prior_accepted_candidate_ids": list(
                self.prior_accepted_candidate_ids
            ),
            "preserved_accepted_candidate_ids": list(
                self.preserved_accepted_candidate_ids
            ),
            "source_verification_hash": self.source_verification_hash,
            "effective_dossier_hash": self.effective_dossier_hash,
            "delta_hash": self.delta_hash,
            "score_valid": False,
            "publication_withheld": True,
            "score_authority": False,
            "stage_authority": False,
        }
        if include_hash:
            payload["receipt_hash"] = canonical_hash(payload)
        return payload


__all__ = [
    "REJECTION_CATEGORIES",
    "REPAIR_ACTIONS",
    "REVERIFIED_ACCEPTED_STATUSES",
    "RepairActionDecision",
    "RepairApplication",
    "RepairResolution",
    "VerifierRejectionPacket",
    "VerifierRepairReceipt",
]
