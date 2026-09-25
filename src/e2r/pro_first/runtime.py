"""Long-running local stack over the durable Pro-first ledger."""

from __future__ import annotations

import asyncio
from dataclasses import asdict
from datetime import date
from pathlib import Path
import secrets
from typing import Any, Mapping

from e2r.cheap_scan.korea_scanner import KoreaCheapScanConfig, KoreaCheapScanner

from .approval import ExactlyOnceSubmitCoordinator
from .browser.completion_monitor import BrowserCompletionMonitor, ProCompletionStateService
from .candidate_selector import ProCandidateSelector
from .capture.coordinator import CaptureFilesystemReconciler, ProCaptureCoordinator
from .config import ProFirstLocalConfig
from .dashboard import DashboardActions, LocalDashboardConfig, create_pro_first_dashboard_app
from .dossier import ProDossierImporter
from .job_store import ProFirstJobStore
from .models import JobStatus, ScanWindow
from .operations import PreparedBrowserRuntime, build_job_packet, prepare_job_in_logged_in_browser
from .post_import import ProFirstPostImportCoordinator
from .scheduler import (
    KoreaScanToProQueue,
    PersistentKrxScheduler,
    ProFirstScheduleService,
    ProSchedulerConfig,
    SchedulerWindowConfig,
)


class ProFirstLocalStack:
    """Own scheduler, dashboard, browser worker and capture reconciler tasks.

    The worker never issues or consumes approval.  It only observes a durable
    ``APPROVED`` state produced by the loopback dashboard before calling the
    exactly-once coordinator.
    """

    def __init__(
        self,
        config: ProFirstLocalConfig,
        *,
        repo_root: str | Path = ".",
        post_import_coordinator: ProFirstPostImportCoordinator | None = None,
    ) -> None:
        self.config = config
        self.repo_root = Path(repo_root).expanduser().resolve()
        self.config.runtime_root.mkdir(parents=True, exist_ok=True)
        self.store = ProFirstJobStore(config.database_path)
        self.post_import = post_import_coordinator or ProFirstPostImportCoordinator(
            self.store,
            runtime_root=config.runtime_root,
            repo_root=self.repo_root,
        )
        self.stop_event = asyncio.Event()
        self.sessions: dict[str, PreparedBrowserRuntime] = {}
        self.monitors: dict[str, ProCompletionStateService] = {}
        self._job_lock = asyncio.Lock()
        self._post_import_waiting: dict[str, tuple[str, int]] = {}
        self.local_token = secrets.token_urlsafe(32)
        self.scheduler = PersistentKrxScheduler(
            self.store,
            config=ProSchedulerConfig(
                timezone_name=config.scheduler.timezone,
                morning=SchedulerWindowConfig(
                    enabled=config.scheduler.morning_enabled,
                    at=config.scheduler.morning_at,
                ),
                evening=SchedulerWindowConfig(
                    enabled=config.scheduler.evening_enabled,
                    at=config.scheduler.evening_at,
                ),
            ),
        )
        scanner = KoreaCheapScanner()
        selector = ProCandidateSelector()
        pipeline = KoreaScanToProQueue(
            store=self.store,
            scanner=scanner,
            selector=selector,
            config_factory=self._scan_config,
        )
        self.schedule_service = ProFirstScheduleService(
            self.scheduler,
            pipeline,
            maximum_idle_poll_seconds=config.scheduler.maximum_idle_poll_seconds,
        )
        dashboard_config = LocalDashboardConfig(
            runtime_root=config.runtime_root,
            host=config.dashboard.host,
            port=config.dashboard.port,
            local_token=self.local_token,
        )
        self.dashboard_app = create_pro_first_dashboard_app(
            store=self.store,
            config=dashboard_config,
            actions=DashboardActions(
                run_scan=self._dashboard_scan,
                prepare_job=self._dashboard_prepare,
            ),
        )

    def readiness_snapshot(self) -> Mapping[str, Any]:
        return {
            "schema_version": "e2r_pro_first_stack_readiness_v1",
            "runtime_root": str(self.config.runtime_root),
            "database_path": str(self.config.database_path),
            "database_pragmas": dict(self.store.pragma_snapshot()),
            "dashboard_url": f"http://{self.config.dashboard.host}:{self.config.dashboard.port}",
            "dashboard_loopback_only": True,
            "scheduler_timezone": self.config.scheduler.timezone,
            "morning": self.config.scheduler.morning_at,
            "evening": self.config.scheduler.evening_at,
            "browser_mode": self.config.browser.mode.value,
            "manual_login_required": self.config.browser.require_manual_login,
            "user_approval_required": self.config.browser.require_user_start_approval,
            "hidden_api_access": self.config.browser.hidden_api_access,
            "pro_score_authority": self.config.authority.pro_score_authority,
            "pro_stage_authority": self.config.authority.pro_stage_authority,
        }

    async def run_forever(self) -> None:
        try:
            import uvicorn
        except ImportError as error:
            raise RuntimeError("uvicorn is required; install project[pro-first]") from error
        server = uvicorn.Server(
            uvicorn.Config(
                self.dashboard_app,
                host=self.config.dashboard.host,
                port=self.config.dashboard.port,
                log_level="info",
                access_log=False,
            )
        )
        tasks = (
            asyncio.create_task(server.serve(), name="pro-first-dashboard"),
            asyncio.create_task(
                self.schedule_service.run_forever(self.stop_event),
                name="pro-first-scheduler",
            ),
            asyncio.create_task(self._browser_loop(), name="pro-first-browser-worker"),
            asyncio.create_task(self._reconciliation_loop(), name="pro-first-reconciler"),
        )
        try:
            await asyncio.gather(*tasks)
        finally:
            self.stop_event.set()
            server.should_exit = True
            for task in tasks:
                if not task.done():
                    task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
            for prepared in tuple(self.sessions.values()):
                await prepared.close()

    async def process_job_once(self, job_id: str) -> Mapping[str, Any]:
        async with self._job_lock:
            job = self.store.get_job(job_id)
            if job.status == JobStatus.CANDIDATE_SELECTED.value:
                job, bundle, prompt = await asyncio.to_thread(
                    build_job_packet,
                    self.store,
                    job_id=job_id,
                    runtime_root=self.config.runtime_root,
                    config_hash=self.config.config_hash,
                    repo_root=self.repo_root,
                )
                return {
                    "job_id": job_id,
                    "status": job.status,
                    "packet_hash": bundle.packet_hash,
                    "prompt_hash": prompt.prompt_hash,
                }
            if job.status in {
                JobStatus.PACKET_READY.value,
                JobStatus.USER_ATTENTION_REQUIRED.value,
            }:
                prepared = await prepare_job_in_logged_in_browser(
                    self.store,
                    job_id=job_id,
                    config=self.config,
                    repo_root=self.repo_root,
                )
                self.sessions[job_id] = prepared
                self.monitors[job_id] = ProCompletionStateService(
                    self.store,
                    BrowserCompletionMonitor(
                        prepared.session.adapter,
                        required_stable_observations=self.config.browser.required_stable_observations,
                        poll_interval_seconds=self.config.browser.poll_interval_seconds,
                    ),
                )
                return dict(prepared.receipt)
            if job.status == JobStatus.APPROVED.value:
                prepared = self._required_session(job_id)
                submitted = await ExactlyOnceSubmitCoordinator(self.store).submit(
                    job_id, prepared.session.adapter
                )
                return {"job_id": job_id, "status": submitted.job.status, "submit_count": submitted.job.submit_count}
            if job.status == JobStatus.RESEARCH_RUNNING.value:
                prepared = self._required_session(job_id)
                packet = _read_json(prepared.packet_bundle.research_packet_json)
                observed_job, observation = await self.monitors[job_id].observe_job(
                    job_id, run_id=str(packet["run_id"])
                )
                return {
                    "job_id": job_id,
                    "status": observed_job.status,
                    "completion_confirmed": observation.completion_confirmed,
                }
            if job.status == JobStatus.RESULT_DETECTED.value:
                prepared = self._required_session(job_id)
                packet = _read_json(prepared.packet_bundle.research_packet_json)
                snapshot = await prepared.session.adapter.inspect_result(
                    job_id=job_id, run_id=str(packet["run_id"])
                )
                completed, capture = await ProCaptureCoordinator(self.store).capture(
                    job_id,
                    run_id=str(packet["run_id"]),
                    expected_filename=prepared.prompt.output_filename,
                    expected_report_hash=snapshot.report_hash,
                    job_root=self.config.runtime_root / "jobs" / job_id,
                    adapter=prepared.session.adapter,
                    capture_mode="CHATGPT_WEB_CDP_ATTACH",
                )
                return {
                    "job_id": job_id,
                    "status": completed.status,
                    "capture_receipt_hash": capture.receipt.receipt_hash,
                }
            if job.status == JobStatus.CAPTURE_COMPLETE.value:
                imported = await asyncio.to_thread(
                    ProDossierImporter(self.store).import_job,
                    job_id,
                    job_root=self.config.runtime_root / "jobs" / job_id,
                )
                prepared = self.sessions.pop(job_id, None)
                self.monitors.pop(job_id, None)
                if prepared is not None:
                    await prepared.close()
                return {"job_id": job_id, "status": imported.job.status, "dossier_id": imported.job.dossier_id}
            if job.status in {
                JobStatus.DOSSIER_IMPORTED.value,
                JobStatus.VERIFYING_SOURCES.value,
                JobStatus.GAP_ADJUDICATION.value,
                JobStatus.SUPPLEMENTAL_RESEARCH.value,
                JobStatus.COMPONENT_RESEARCH.value,
                JobStatus.JUDGING.value,
                JobStatus.SCORING.value,
                JobStatus.STAGECOURT.value,
                JobStatus.FINAL.value,
            }:
                advance = self.post_import.advance_once(job_id)
                current = self.store.get_job(job_id)
                if advance.wait_reason is not None:
                    self._post_import_waiting[job_id] = (
                        current.status,
                        current.state_version,
                    )
                else:
                    self._post_import_waiting.pop(job_id, None)
                return dict(advance.to_dict())
            return {"job_id": job_id, "status": job.status, "action": "NONE"}

    async def _browser_loop(self) -> None:
        actionable = {
            JobStatus.CANDIDATE_SELECTED.value,
            JobStatus.PACKET_READY.value,
            JobStatus.APPROVED.value,
            JobStatus.RESEARCH_RUNNING.value,
            JobStatus.RESULT_DETECTED.value,
            JobStatus.CAPTURE_COMPLETE.value,
            JobStatus.DOSSIER_IMPORTED.value,
            JobStatus.VERIFYING_SOURCES.value,
            JobStatus.GAP_ADJUDICATION.value,
            JobStatus.SUPPLEMENTAL_RESEARCH.value,
            JobStatus.COMPONENT_RESEARCH.value,
            JobStatus.SCORING.value,
            JobStatus.STAGECOURT.value,
        }
        if self.post_import.judge_provider_available:
            actionable.add(JobStatus.JUDGING.value)
        while not self.stop_event.is_set():
            for job in self.store.list_jobs(limit=200):
                if (
                    job.status == JobStatus.FINAL.value
                    and self.store.get_publication(job.job_id) is None
                ):
                    actionable.add(JobStatus.FINAL.value)
                if job.status not in actionable:
                    continue
                if self._post_import_waiting.get(job.job_id) == (
                    job.status,
                    job.state_version,
                ):
                    continue
                try:
                    await self.process_job_once(job.job_id)
                except Exception:
                    # Lifecycle services already persist actionable failures. A
                    # transient CDP absence must not kill scheduler/dashboard.
                    continue
            try:
                await asyncio.wait_for(
                    self.stop_event.wait(), timeout=self.config.browser.poll_interval_seconds
                )
            except asyncio.TimeoutError:
                continue

    async def _reconciliation_loop(self) -> None:
        reconciler = CaptureFilesystemReconciler(self.store)
        while not self.stop_event.is_set():
            jobs_root = self.config.runtime_root / "jobs"
            if jobs_root.is_dir():
                for job_root in sorted(path for path in jobs_root.iterdir() if path.is_dir()):
                    try:
                        await reconciler.reconcile(job_root)
                    except Exception:
                        continue
            try:
                await asyncio.wait_for(
                    self.stop_event.wait(), timeout=self.config.reconciliation_poll_seconds
                )
            except asyncio.TimeoutError:
                continue

    async def _dashboard_scan(self, _body: Mapping[str, Any]) -> Any:
        return [asdict(receipt) for receipt in await self.schedule_service.run_once()]

    async def _dashboard_prepare(self, job_id: str, _body: Mapping[str, Any]) -> Any:
        return await self.process_job_once(job_id)

    def _scan_config(self, as_of_date: date, _window: ScanWindow) -> KoreaCheapScanConfig:
        return KoreaCheapScanConfig(
            as_of_date=as_of_date,
            universe_limit=self.config.scan.universe_limit,
            top_n=self.config.scan.top_n,
            deep_research_min_score=self.config.scan.deep_research_min_score,
            report_radar_enabled=False,
        )

    def _required_session(self, job_id: str) -> PreparedBrowserRuntime:
        try:
            return self.sessions[job_id]
        except KeyError as error:
            raise RuntimeError(
                "prepared browser session is not in this worker process; return the job to BROWSER_PREPARING"
            ) from error


def _read_json(path: Path) -> Mapping[str, Any]:
    import json

    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"expected JSON object: {path}")
    return payload


__all__ = ["ProFirstLocalStack"]
