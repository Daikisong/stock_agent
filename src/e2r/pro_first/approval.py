"""One-time approval service and exactly-once browser submission coordinator."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any, Callable

from .browser.protocol import BrowserInspection, BrowserUIState, ChatGPTWebAdapter
from .job_store import ApprovalInvalid, ProFirstJobStore
from .models import JobStatus, ProResearchJob


_SUBMIT_CAPABILITY = object()


@dataclass(frozen=True)
class ApprovalGrant:
    job_id: str
    approval_nonce: str = field(repr=False)
    packet_hash: str
    prompt_hash: str
    browser_session_id: str
    expires_at: str
    state_version: int


@dataclass(frozen=True)
class ConsumedApprovalProof:
    job_id: str
    packet_hash: str
    prompt_hash: str
    browser_session_id: str
    conversation_id: str | None
    approval_consumed_at: str
    submit_count: int
    _capability: object = field(repr=False, compare=False)

    @property
    def ledger_verified(self) -> bool:
        return self._capability is _SUBMIT_CAPABILITY and self.submit_count == 1


@dataclass(frozen=True)
class SubmitResult:
    job: ProResearchJob
    inspection: BrowserInspection


class ProApprovalService:
    def __init__(
        self,
        store: ProFirstJobStore,
        *,
        now: Callable[[], datetime] | None = None,
        nonce_ttl: timedelta = timedelta(minutes=15),
    ) -> None:
        if nonce_ttl.total_seconds() <= 0:
            raise ValueError("approval nonce TTL must be positive")
        self.store = store
        self._now = now or (lambda: datetime.now(timezone.utc))
        self.nonce_ttl = nonce_ttl

    def issue(self, job_id: str, *, prompt_hash: str, actor: str = "dashboard") -> ApprovalGrant:
        job = self.store.get_job(job_id)
        if job.status != JobStatus.AWAITING_USER_APPROVAL.value:
            raise ApprovalInvalid("job is not awaiting user approval")
        if not job.packet_hash or not job.browser_session_id:
            raise ApprovalInvalid("prepared packet and browser session are required")
        expires = self._now_value() + self.nonce_ttl
        expires_at = expires.isoformat().replace("+00:00", "Z")
        updated, raw_nonce = self.store.issue_approval_nonce(
            job_id,
            expected_version=job.state_version,
            actor=actor,
            idempotency_key=f"approval-issued:{job_id}:{job.state_version}",
            prompt_hash=prompt_hash,
            expires_at=expires_at,
        )
        return ApprovalGrant(
            job_id=job_id,
            approval_nonce=raw_nonce,
            packet_hash=job.packet_hash,
            prompt_hash=prompt_hash,
            browser_session_id=job.browser_session_id,
            expires_at=expires_at,
            state_version=updated.state_version,
        )

    def approve(
        self,
        grant: ApprovalGrant,
        *,
        actor: str = "user",
    ) -> ProResearchJob:
        job = self.store.get_job(grant.job_id)
        if job.state_version != grant.state_version:
            raise ApprovalInvalid("job changed after approval grant issuance")
        return self.store.consume_approval_nonce(
            grant.job_id,
            grant.approval_nonce,
            expected_version=job.state_version,
            actor=actor,
            idempotency_key=f"approval-consumed:{grant.job_id}:{job.state_version}",
            prompt_hash=grant.prompt_hash,
        )

    def _now_value(self) -> datetime:
        value = self._now()
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("approval clock must be timezone-aware")
        return value.astimezone(timezone.utc)


class ExactlyOnceSubmitCoordinator:
    """The only production service allowed to invoke the DOM send action."""

    def __init__(self, store: ProFirstJobStore) -> None:
        self.store = store

    async def submit(
        self,
        job_id: str,
        adapter: ChatGPTWebAdapter,
        *,
        actor: str = "browser-worker",
    ) -> SubmitResult:
        job = self.store.get_job(job_id)
        claimed = self.store.claim_submit(
            job_id,
            expected_version=job.state_version,
            actor=actor,
            idempotency_key=f"submit-claimed:{job_id}",
        )
        proof = self._proof_from_claimed_job(claimed)
        try:
            inspection = await adapter.submit_once(proof)
            if inspection.state is not BrowserUIState.RESEARCH_RUNNING:
                raise RuntimeError(
                    f"send click did not produce RESEARCH_RUNNING: {inspection.state.value}"
                )
        except Exception as error:
            self.store.transition(
                job_id,
                expected_version=claimed.state_version,
                to_status=JobStatus.USER_ATTENTION_REQUIRED,
                actor=actor,
                idempotency_key=f"submit-attention:{job_id}",
                payload={
                    "submit_count": 1,
                    "error_class": type(error).__name__,
                    "automatic_resubmit_allowed": False,
                },
                updates={
                    "last_error_class": type(error).__name__,
                    "last_error_message": str(error),
                },
            )
            raise
        running = self.store.transition(
            job_id,
            expected_version=claimed.state_version,
            to_status=JobStatus.RESEARCH_RUNNING,
            actor=actor,
            idempotency_key=f"research-running:{job_id}",
            payload={"submit_count": 1, "conversation_id": claimed.conversation_id},
        )
        return SubmitResult(job=running, inspection=inspection)

    @staticmethod
    def _proof_from_claimed_job(job: ProResearchJob) -> ConsumedApprovalProof:
        if (
            job.status != JobStatus.SUBMITTING.value
            or job.submit_count != 1
            or not job.approval_consumed_at
            or not job.approval_packet_hash
            or not job.approval_prompt_hash
            or not job.approval_browser_session_id
        ):
            raise ApprovalInvalid("durable claimed job is missing consumed approval lineage")
        return ConsumedApprovalProof(
            job_id=job.job_id,
            packet_hash=job.approval_packet_hash,
            prompt_hash=job.approval_prompt_hash,
            browser_session_id=job.approval_browser_session_id,
            conversation_id=job.conversation_id,
            approval_consumed_at=job.approval_consumed_at,
            submit_count=job.submit_count,
            _capability=_SUBMIT_CAPABILITY,
        )


__all__ = [
    "ApprovalGrant",
    "ExactlyOnceSubmitCoordinator",
    "ProApprovalService",
    "SubmitResult",
]
