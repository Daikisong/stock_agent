"""Conservative ChatGPT completion monitor with stable-result observations."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Awaitable, Callable

from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob
from .protocol import (
    BrowserInspection,
    BrowserResultSnapshot,
    BrowserUIState,
    ChatGPTWebAdapter,
)


@dataclass(frozen=True)
class CompletionObservation:
    inspection: BrowserInspection
    result: BrowserResultSnapshot | None
    stable_observations: int
    completion_confirmed: bool


class BrowserCompletionMonitor:
    def __init__(
        self,
        adapter: ChatGPTWebAdapter,
        *,
        required_stable_observations: int = 3,
        poll_interval_seconds: float = 5.0,
    ) -> None:
        if required_stable_observations < 2:
            raise ValueError("completion requires at least two stable observations")
        if poll_interval_seconds <= 0:
            raise ValueError("poll interval must be positive")
        self.adapter = adapter
        self.required_stable_observations = required_stable_observations
        self.poll_interval_seconds = poll_interval_seconds
        self._last_hash: str | None = None
        self._stable_observations = 0

    async def observe(self, *, job_id: str, run_id: str) -> CompletionObservation:
        inspection = await self.adapter.inspect_state()
        if inspection.stop_visible or inspection.state is BrowserUIState.RESEARCH_RUNNING:
            self._reset()
            return CompletionObservation(inspection, None, 0, False)
        if inspection.state in {
            BrowserUIState.LOGIN_REQUIRED,
            BrowserUIState.AWAITING_CLARIFICATION,
            BrowserUIState.QUOTA_PENDING,
            BrowserUIState.RETRYABLE_ERROR,
            BrowserUIState.UI_INCOMPATIBLE,
        }:
            self._reset()
            return CompletionObservation(inspection, None, 0, False)
        result = await self.adapter.inspect_result(job_id=job_id, run_id=run_id)
        if not result.structurally_complete:
            self._reset()
            return CompletionObservation(inspection, result, 0, False)
        if result.report_hash == self._last_hash:
            self._stable_observations += 1
        else:
            self._last_hash = result.report_hash
            self._stable_observations = 1
        confirmed = self._stable_observations >= self.required_stable_observations
        return CompletionObservation(
            inspection=inspection,
            result=result,
            stable_observations=self._stable_observations,
            completion_confirmed=confirmed,
        )

    async def wait_until_actionable(
        self,
        *,
        job_id: str,
        run_id: str,
        max_polls: int | None = None,
        sleep: Callable[[float], Awaitable[None]] | None = None,
    ) -> CompletionObservation:
        polls = 0
        while max_polls is None or polls < max_polls:
            observation = await self.observe(job_id=job_id, run_id=run_id)
            polls += 1
            if observation.completion_confirmed or observation.inspection.state in {
                BrowserUIState.LOGIN_REQUIRED,
                BrowserUIState.AWAITING_CLARIFICATION,
                BrowserUIState.QUOTA_PENDING,
                BrowserUIState.RETRYABLE_ERROR,
                BrowserUIState.UI_INCOMPATIBLE,
            }:
                return observation
            delay = sleep or asyncio.sleep
            await delay(self.poll_interval_seconds)
        raise TimeoutError("ChatGPT completion monitor exhausted max_polls")

    def _reset(self) -> None:
        self._last_hash = None
        self._stable_observations = 0


class ProCompletionStateService:
    """Maps browser observations onto durable states without any resubmission."""

    def __init__(self, store: ProFirstJobStore, monitor: BrowserCompletionMonitor) -> None:
        self.store = store
        self.monitor = monitor

    async def observe_job(
        self, job_id: str, *, run_id: str
    ) -> tuple[ProResearchJob, CompletionObservation]:
        job = self.store.get_job(job_id)
        if job.status != JobStatus.RESEARCH_RUNNING.value:
            raise ValueError("completion monitoring requires RESEARCH_RUNNING")
        observation = await self.monitor.observe(job_id=job_id, run_id=run_id)
        target: JobStatus | None = None
        payload: dict[str, object] = {
            "browser_state": observation.inspection.state.value,
            "stable_observations": observation.stable_observations,
            "automatic_resubmit_allowed": False,
        }
        updates: dict[str, object] = {}
        if observation.completion_confirmed and observation.result is not None:
            target = JobStatus.RESULT_DETECTED
            payload.update(
                {
                    "assistant_turn_id": observation.result.assistant_turn_id,
                    "report_hash": observation.result.report_hash,
                    "conversation_id": observation.result.conversation_id,
                }
            )
        elif observation.inspection.state is BrowserUIState.AWAITING_CLARIFICATION:
            target = JobStatus.AWAITING_CLARIFICATION
            payload["question"] = observation.inspection.detail
        elif observation.inspection.state is BrowserUIState.QUOTA_PENDING:
            target = JobStatus.QUOTA_PENDING
        elif observation.inspection.state is BrowserUIState.RETRYABLE_ERROR:
            target = JobStatus.FAILED_RETRYABLE
            updates = {
                "last_error_class": "CHATGPT_RETRYABLE_ERROR",
                "last_error_message": (
                    observation.inspection.detail or "ChatGPT retryable UI error"
                ),
            }
        elif observation.inspection.state in {
            BrowserUIState.LOGIN_REQUIRED,
            BrowserUIState.UI_INCOMPATIBLE,
        }:
            target = JobStatus.USER_ATTENTION_REQUIRED
            updates = {
                "last_error_class": observation.inspection.state.value,
                "last_error_message": (
                    observation.inspection.detail or observation.inspection.state.value
                ),
            }
        if target is None:
            return job, observation
        updated = self.store.transition(
            job_id,
            expected_version=job.state_version,
            to_status=target,
            actor="browser-completion-monitor",
            idempotency_key=f"browser-state:{job_id}:{job.state_version}:{target.value}",
            payload=payload,
            updates=updates,
        )
        return updated, observation


__all__ = [
    "BrowserCompletionMonitor",
    "CompletionObservation",
    "ProCompletionStateService",
]
