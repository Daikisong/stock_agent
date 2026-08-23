"""Deterministic Pro-first job state machine and progress guard."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Mapping

from .ids import canonical_hash
from .models import JobStatus, TERMINAL_JOB_STATUSES


class InvalidJobTransition(ValueError):
    pass


class NoProgressDetected(RuntimeError):
    pass


@dataclass(frozen=True)
class TransitionContext:
    approval_nonce_consumed: bool = False
    capture_receipt_verified: bool = False
    dossier_validated: bool = False
    source_verification_complete: bool = False
    research_saturation_valid: bool = False
    component_coverage_complete: bool = False
    judge_coverage_complete: bool = False
    deterministic_score_present: bool = False
    deterministic_stagecourt_present: bool = False


@dataclass(frozen=True)
class ProgressSnapshot:
    status: str
    packet_hash: str | None = None
    browser_turn_hash: str | None = None
    capture_hash: str | None = None
    dossier_hash: str | None = None
    verified_fact_roster_hash: str | None = None
    gap_disposition_hash: str | None = None
    component_vector_hash: str | None = None
    stagecourt_hash: str | None = None

    def __post_init__(self) -> None:
        JobStatus(self.status)

    @property
    def progress_hash(self) -> str:
        return canonical_hash(asdict(self))


_ALLOWED: Mapping[JobStatus, frozenset[JobStatus]] = {
    JobStatus.SCANNED: frozenset({JobStatus.CANDIDATE_SELECTED, JobStatus.CANCELLED}),
    JobStatus.CANDIDATE_SELECTED: frozenset({JobStatus.PACKET_BUILDING, JobStatus.CANCELLED}),
    JobStatus.PACKET_BUILDING: frozenset({JobStatus.PACKET_READY, JobStatus.FAILED_RETRYABLE, JobStatus.BLOCKED, JobStatus.CANCELLED}),
    JobStatus.PACKET_READY: frozenset({JobStatus.BROWSER_PREPARING, JobStatus.CANCELLED}),
    JobStatus.BROWSER_PREPARING: frozenset({JobStatus.AWAITING_USER_APPROVAL, JobStatus.USER_ATTENTION_REQUIRED, JobStatus.FAILED_RETRYABLE, JobStatus.CANCELLED}),
    JobStatus.AWAITING_USER_APPROVAL: frozenset({JobStatus.APPROVED, JobStatus.CANCELLED}),
    JobStatus.APPROVED: frozenset({JobStatus.SUBMITTING, JobStatus.CANCELLED}),
    JobStatus.SUBMITTING: frozenset({JobStatus.RESEARCH_RUNNING, JobStatus.FAILED_RETRYABLE, JobStatus.USER_ATTENTION_REQUIRED, JobStatus.CANCELLED}),
    JobStatus.RESEARCH_RUNNING: frozenset({JobStatus.AWAITING_CLARIFICATION, JobStatus.USER_ATTENTION_REQUIRED, JobStatus.QUOTA_PENDING, JobStatus.RESULT_DETECTED, JobStatus.FAILED_RETRYABLE, JobStatus.CANCELLED}),
    JobStatus.AWAITING_CLARIFICATION: frozenset({JobStatus.RESEARCH_RUNNING, JobStatus.USER_ATTENTION_REQUIRED, JobStatus.CANCELLED}),
    JobStatus.QUOTA_PENDING: frozenset({JobStatus.RESEARCH_RUNNING, JobStatus.USER_ATTENTION_REQUIRED, JobStatus.CANCELLED}),
    JobStatus.USER_ATTENTION_REQUIRED: frozenset({JobStatus.BROWSER_PREPARING, JobStatus.IMPORTING, JobStatus.VERIFYING_SOURCES, JobStatus.BLOCKED, JobStatus.CANCELLED}),
    JobStatus.RESULT_DETECTED: frozenset({JobStatus.CAPTURING_ARTIFACTS, JobStatus.FAILED_RETRYABLE, JobStatus.CANCELLED}),
    JobStatus.CAPTURING_ARTIFACTS: frozenset({JobStatus.CAPTURE_COMPLETE, JobStatus.FAILED_RETRYABLE, JobStatus.USER_ATTENTION_REQUIRED, JobStatus.CANCELLED}),
    JobStatus.CAPTURE_COMPLETE: frozenset({JobStatus.IMPORTING, JobStatus.USER_ATTENTION_REQUIRED, JobStatus.BLOCKED}),
    JobStatus.IMPORTING: frozenset({JobStatus.DOSSIER_IMPORTED, JobStatus.USER_ATTENTION_REQUIRED, JobStatus.FAILED_RETRYABLE, JobStatus.BLOCKED}),
    JobStatus.DOSSIER_IMPORTED: frozenset({JobStatus.VERIFYING_SOURCES, JobStatus.BLOCKED}),
    JobStatus.VERIFYING_SOURCES: frozenset({JobStatus.GAP_ADJUDICATION, JobStatus.USER_ATTENTION_REQUIRED, JobStatus.FAILED_RETRYABLE, JobStatus.BLOCKED}),
    JobStatus.GAP_ADJUDICATION: frozenset({JobStatus.VERIFYING_SOURCES, JobStatus.SUPPLEMENTAL_RESEARCH, JobStatus.COMPONENT_RESEARCH, JobStatus.BLOCKED}),
    JobStatus.SUPPLEMENTAL_RESEARCH: frozenset({JobStatus.VERIFYING_SOURCES, JobStatus.COMPONENT_RESEARCH, JobStatus.FAILED_RETRYABLE, JobStatus.BLOCKED}),
    JobStatus.COMPONENT_RESEARCH: frozenset({JobStatus.JUDGING, JobStatus.FAILED_RETRYABLE, JobStatus.BLOCKED}),
    JobStatus.JUDGING: frozenset({JobStatus.SCORING, JobStatus.FAILED_RETRYABLE, JobStatus.BLOCKED}),
    JobStatus.SCORING: frozenset({JobStatus.STAGECOURT, JobStatus.BLOCKED}),
    JobStatus.STAGECOURT: frozenset({JobStatus.FINAL, JobStatus.BLOCKED}),
    JobStatus.FAILED_RETRYABLE: frozenset({JobStatus.BROWSER_PREPARING, JobStatus.IMPORTING, JobStatus.VERIFYING_SOURCES, JobStatus.COMPONENT_RESEARCH, JobStatus.JUDGING, JobStatus.USER_ATTENTION_REQUIRED, JobStatus.BLOCKED, JobStatus.CANCELLED}),
    JobStatus.FINAL: frozenset(),
    JobStatus.BLOCKED: frozenset(),
    JobStatus.CANCELLED: frozenset(),
}


class ProJobStateMachine:
    def allowed_targets(self, status: str | JobStatus) -> frozenset[JobStatus]:
        source = JobStatus(status)
        if source in TERMINAL_JOB_STATUSES:
            return frozenset()
        return _ALLOWED[source] | frozenset({JobStatus.BLOCKED})

    def validate(
        self,
        from_status: str | JobStatus,
        to_status: str | JobStatus,
        *,
        context: TransitionContext | None = None,
    ) -> None:
        source = JobStatus(from_status)
        target = JobStatus(to_status)
        context = context or TransitionContext()
        if source in TERMINAL_JOB_STATUSES or target not in self.allowed_targets(source):
            raise InvalidJobTransition(f"invalid Pro-first transition: {source.value} -> {target.value}")
        if target is JobStatus.SUBMITTING and not context.approval_nonce_consumed:
            raise InvalidJobTransition("SUBMITTING requires an atomically consumed approval nonce")
        if source is JobStatus.CAPTURE_COMPLETE and target is JobStatus.IMPORTING and not context.capture_receipt_verified:
            raise InvalidJobTransition("IMPORTING requires a verified capture receipt")
        if source is JobStatus.IMPORTING and target is JobStatus.DOSSIER_IMPORTED and not context.dossier_validated:
            raise InvalidJobTransition("DOSSIER_IMPORTED requires strict dossier validation")
        if source is JobStatus.VERIFYING_SOURCES and target is JobStatus.GAP_ADJUDICATION and not context.source_verification_complete:
            raise InvalidJobTransition("gap adjudication requires completed source verification")
        if source is JobStatus.COMPONENT_RESEARCH and target is JobStatus.JUDGING:
            if not context.research_saturation_valid:
                raise InvalidJobTransition(
                    "JUDGING requires a valid V2 research saturation receipt"
                )
            if not context.component_coverage_complete:
                raise InvalidJobTransition("JUDGING requires seven component memos")
        if source is JobStatus.JUDGING and target is JobStatus.SCORING and not context.judge_coverage_complete:
            raise InvalidJobTransition("SCORING requires twenty-one judge decisions")
        if source is JobStatus.SCORING and target is JobStatus.STAGECOURT and not context.deterministic_score_present:
            raise InvalidJobTransition("STAGECOURT requires the deterministic score result")
        if source is JobStatus.STAGECOURT and target is JobStatus.FINAL and not context.deterministic_stagecourt_present:
            raise InvalidJobTransition("FINAL requires a deterministic StageCourt decision")


__all__ = [
    "InvalidJobTransition",
    "NoProgressDetected",
    "ProgressSnapshot",
    "ProJobStateMachine",
    "TransitionContext",
]
