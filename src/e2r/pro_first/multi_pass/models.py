"""Durable approval-scope and same-conversation research-pass records."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping


INITIAL_PASS_NAME = "INITIAL_FULL_RESEARCH"
COUNTER_SUPERSESSION_PASS_NAME = "COUNTER_SUPERSESSION_CLOSURE"
BOUNDED_FOLLOWUP_PASS_NAMES = frozenset(
    {
        "PUBLIC_GAP_CLOSURE",
        COUNTER_SUPERSESSION_PASS_NAME,
        "VERIFIER_REPAIR",
        "SATURATION_AUDIT",
    }
)


class ResearchPassStatus(str, Enum):
    COMPLETE = "COMPLETE"
    PLANNED = "PLANNED"
    PREPARED = "PREPARED"
    SUBMITTING = "SUBMITTING"
    RESEARCH_RUNNING = "RESEARCH_RUNNING"
    TRANSPORT_PENDING = "TRANSPORT_PENDING"
    FAILED_HARD = "FAILED_HARD"


class ScopeApprovalRequired(PermissionError):
    """A requested follow-up escapes the user's durable initial approval."""


class FollowupSubmitBlocked(RuntimeError):
    """A pass was already sent or has no valid durable claim."""


class RepeatedGapReopenHardFail(RuntimeError):
    """The same stable gap was reopened for a forbidden third time."""


@dataclass(frozen=True)
class ResearchApprovalScope:
    approval_scope_id: str
    job_id: str
    target_id: str
    as_of_date: str
    primary_archetype_ids: tuple[str, ...]
    contract_ids: tuple[str, ...]
    allowed_followup_pass_names: tuple[str, ...]
    browser_session_id: str
    conversation_id: str
    initial_pass_id: str
    initial_prompt_hash: str
    initial_response_hash: str
    scope_hash: str
    created_at: str


@dataclass(frozen=True)
class ResearchPassRecord:
    pass_id: str
    job_id: str
    approval_scope_id: str
    pass_name: str
    pass_ordinal: int
    parent_pass_id: str | None
    conversation_id: str
    prompt_hash: str
    response_hash: str | None
    pass_input_hash: str
    status: str
    submit_count: int
    score_valid: bool
    publication_withheld: bool
    detail: Mapping[str, Any]
    created_at: str
    prepared_at: str | None
    submitted_at: str | None
    completed_at: str | None

    def __post_init__(self) -> None:
        ResearchPassStatus(self.status)
        if self.pass_ordinal < 1:
            raise ValueError("research pass ordinal must be positive")
        if self.submit_count not in {0, 1}:
            raise ValueError("each research pass must remain exactly-once")
        if self.score_valid:
            raise ValueError("research passes never hold deterministic score authority")
        if not self.publication_withheld:
            raise ValueError("research pass records cannot authorize publication")


@dataclass(frozen=True)
class FollowupPassPlan:
    scope: ResearchApprovalScope
    research_pass: ResearchPassRecord
    prompt_text: str
    prompt_hash: str


@dataclass(frozen=True)
class TransportPendingDecision:
    job_id: str
    requested_pass_name: str
    research_status: str
    reason: str
    score_valid: bool = False
    publication_withheld: bool = True

    def __post_init__(self) -> None:
        if self.research_status != "TRANSPORT_PENDING":
            raise ValueError("transport limit must remain pending, never complete")
        if self.score_valid or not self.publication_withheld:
            raise ValueError("transport pending cannot authorize score/publication")


@dataclass(frozen=True)
class ResearchDossierSnapshotRecord:
    snapshot_id: str
    job_id: str
    pass_id: str
    revision_ordinal: int
    parent_snapshot_id: str | None
    dossier_hash: str
    relative_path: str
    fact_count: int
    question_count: int
    route_receipt_count: int
    created_at: str

    def __post_init__(self) -> None:
        if self.revision_ordinal < 1:
            raise ValueError("dossier snapshot revision ordinal must be positive")
        if len(self.dossier_hash) != 64:
            raise ValueError("dossier snapshot hash must be sha256")
        if min(self.fact_count, self.question_count, self.route_receipt_count) < 0:
            raise ValueError("dossier snapshot counts must be nonnegative")


__all__ = [
    "BOUNDED_FOLLOWUP_PASS_NAMES",
    "COUNTER_SUPERSESSION_PASS_NAME",
    "FollowupPassPlan",
    "FollowupSubmitBlocked",
    "INITIAL_PASS_NAME",
    "RepeatedGapReopenHardFail",
    "ResearchApprovalScope",
    "ResearchDossierSnapshotRecord",
    "ResearchPassRecord",
    "ResearchPassStatus",
    "ScopeApprovalRequired",
    "TransportPendingDecision",
]
