"""Canonical runtime records for the Pro-first platform."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from enum import Enum
from typing import Any, Mapping


class JobStatus(str, Enum):
    SCANNED = "SCANNED"
    CANDIDATE_SELECTED = "CANDIDATE_SELECTED"
    PACKET_BUILDING = "PACKET_BUILDING"
    PACKET_READY = "PACKET_READY"
    BROWSER_PREPARING = "BROWSER_PREPARING"
    AWAITING_USER_APPROVAL = "AWAITING_USER_APPROVAL"
    APPROVED = "APPROVED"
    SUBMITTING = "SUBMITTING"
    RESEARCH_RUNNING = "RESEARCH_RUNNING"
    AWAITING_CLARIFICATION = "AWAITING_CLARIFICATION"
    USER_ATTENTION_REQUIRED = "USER_ATTENTION_REQUIRED"
    QUOTA_PENDING = "QUOTA_PENDING"
    RESULT_DETECTED = "RESULT_DETECTED"
    CAPTURING_ARTIFACTS = "CAPTURING_ARTIFACTS"
    CAPTURE_COMPLETE = "CAPTURE_COMPLETE"
    IMPORTING = "IMPORTING"
    DOSSIER_IMPORTED = "DOSSIER_IMPORTED"
    VERIFYING_SOURCES = "VERIFYING_SOURCES"
    GAP_ADJUDICATION = "GAP_ADJUDICATION"
    SUPPLEMENTAL_RESEARCH = "SUPPLEMENTAL_RESEARCH"
    COMPONENT_RESEARCH = "COMPONENT_RESEARCH"
    JUDGING = "JUDGING"
    SCORING = "SCORING"
    STAGECOURT = "STAGECOURT"
    FINAL = "FINAL"
    FAILED_RETRYABLE = "FAILED_RETRYABLE"
    BLOCKED = "BLOCKED"
    CANCELLED = "CANCELLED"


TERMINAL_JOB_STATUSES = frozenset(
    {JobStatus.FINAL, JobStatus.BLOCKED, JobStatus.CANCELLED}
)


class ResearchMode(str, Enum):
    FULL_RESEARCH = "FULL_RESEARCH"
    DELTA_RESEARCH = "DELTA_RESEARCH"
    FORCED_VALIDATION_CANARY = "FORCED_VALIDATION_CANARY"


class ScanWindow(str, Enum):
    MORNING = "MORNING"
    EVENING = "EVENING"


@dataclass(frozen=True)
class CandidateRecord:
    candidate_id: str
    scan_run_id: str | None
    symbol: str
    company_name: str
    as_of_date: str
    scan_window: str
    trigger_fingerprint: str
    research_mode: str
    dedupe_key: str
    selection_receipt: Mapping[str, Any]
    created_at: str

    def __post_init__(self) -> None:
        _required(self.candidate_id, "candidate_id")
        _required(self.symbol, "symbol")
        _required(self.company_name, "company_name")
        date.fromisoformat(self.as_of_date)
        ScanWindow(self.scan_window)
        ResearchMode(self.research_mode)
        _required(self.trigger_fingerprint, "trigger_fingerprint")
        _required(self.dedupe_key, "dedupe_key")


@dataclass(frozen=True)
class ProResearchJob:
    job_id: str
    candidate_id: str
    symbol: str
    company_name: str
    as_of_date: str
    mode: str
    status: str
    state_version: int
    priority: int
    archetype_ids: tuple[str, ...]
    trigger_fingerprint: str
    packet_id: str | None
    packet_hash: str | None
    approval_nonce_hash: str | None
    approval_packet_hash: str | None
    approval_prompt_hash: str | None
    approval_browser_session_id: str | None
    approval_expires_at: str | None
    approval_consumed_at: str | None
    browser_session_id: str | None
    conversation_id: str | None
    submit_count: int
    capture_count: int
    dossier_id: str | None
    score_receipt_id: str | None
    stagecourt_receipt_id: str | None
    created_at: str
    updated_at: str
    approved_at: str | None
    submitted_at: str | None
    research_completed_at: str | None
    published_at: str | None
    last_error_class: str | None
    last_error_message: str | None
    last_progress_actor: str | None = None
    last_progress_hash: str | None = None

    def __post_init__(self) -> None:
        for value, label in (
            (self.job_id, "job_id"),
            (self.candidate_id, "candidate_id"),
            (self.symbol, "symbol"),
            (self.company_name, "company_name"),
            (self.trigger_fingerprint, "trigger_fingerprint"),
        ):
            _required(value, label)
        date.fromisoformat(self.as_of_date)
        ResearchMode(self.mode)
        JobStatus(self.status)
        if self.state_version < 0:
            raise ValueError("state_version must be nonnegative")
        if self.submit_count not in {0, 1}:
            raise ValueError("submit_count must remain exactly-once")
        if self.capture_count < 0:
            raise ValueError("capture_count must be nonnegative")
        if len(self.archetype_ids) != len(set(self.archetype_ids)):
            raise ValueError("archetype ids must be unique")

    def to_dict(self) -> Mapping[str, Any]:
        payload = asdict(self)
        payload["archetype_ids"] = list(self.archetype_ids)
        return payload


@dataclass(frozen=True)
class JobEvent:
    event_id: str
    job_id: str
    from_status: str
    to_status: str
    actor: str
    idempotency_key: str
    payload_hash: str
    payload: Mapping[str, Any]
    created_at: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.event_id, "event_id"),
            (self.job_id, "job_id"),
            (self.actor, "actor"),
            (self.idempotency_key, "idempotency_key"),
            (self.payload_hash, "payload_hash"),
        ):
            _required(value, label)
        JobStatus(self.from_status)
        JobStatus(self.to_status)
        if len(self.payload_hash) != 64:
            raise ValueError("event payload hash must be sha256")


def _required(value: str, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} is required")


__all__ = [
    "CandidateRecord",
    "JobEvent",
    "JobStatus",
    "ProResearchJob",
    "ResearchMode",
    "ScanWindow",
    "TERMINAL_JOB_STATUSES",
]
