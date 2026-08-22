from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from e2r.pro_first.approval import ExactlyOnceSubmitCoordinator, ProApprovalService
from e2r.pro_first.browser.chatgpt_adapter import PlaywrightChatGPTWebAdapter
from e2r.pro_first.browser.completion_monitor import (
    BrowserCompletionMonitor,
    ProCompletionStateService,
)
from e2r.pro_first.browser.mock_chatgpt_app import MockChatGPTServer
from e2r.pro_first.browser.protocol import BrowserCaptureRequest, BrowserUIState
from e2r.pro_first.capture.atomic_capture import AtomicCaptureWriter, CaptureIdentity
from e2r.pro_first.capture.coordinator import (
    CaptureEventDispatcher,
    CaptureFilesystemReconciler,
    ProCaptureCoordinator,
)
from e2r.pro_first.capture.receipt import file_sha256, load_capture_receipt
from e2r.pro_first.ids import canonical_hash
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow


class ProFirstCompletionCaptureTest(unittest.IsolatedAsyncioTestCase):
    run_id = "PRORUN-cccccccccccccccccccccccc"
    symbol = "123456"
    as_of_date = "2026-08-22"

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.server = MockChatGPTServer()
        self.server.__enter__()
        self.addCleanup(self.server.__exit__, None, None, None)
        self.now = datetime(2026, 8, 22, 2, 3, 4, tzinfo=timezone.utc)
        self.database_path = Path(self.temporary_directory.name) / "capture.sqlite3"
        self.store = ProFirstJobStore(self.database_path, now=lambda: self.now)
        self.packet_path = Path(self.temporary_directory.name) / "research_packet.json"
        self.packet_payload = {"schema_version": "e2r_pro_research_packet_v1"}
        self.packet_path.write_text(json.dumps(self.packet_payload), encoding="utf-8")
        self.packet_hash = canonical_hash(self.packet_payload)

    async def asyncSetUp(self) -> None:
        from playwright.async_api import async_playwright

        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.page = await self.browser.new_page(accept_downloads=True)
        await self.page.goto(
            f"{self.server.base_url}/c/capture-conversation",
            wait_until="domcontentloaded",
        )
        self.adapter = PlaywrightChatGPTWebAdapter(self.page)

    async def asyncTearDown(self) -> None:
        await self.browser.close()
        await self.playwright.stop()

    async def _running_job(self):
        candidate = self.store.create_candidate(
            symbol=self.symbol,
            company_name="검증기업",
            as_of_date=self.as_of_date,
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="capture-trigger",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={"production_candidate": True},
        )
        job = self.store.create_job(candidate.candidate_id)
        job = self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.PACKET_BUILDING,
            actor="packet-worker",
            idempotency_key="packet-building",
        )
        job = self.store.record_packet(
            job.job_id,
            expected_version=job.state_version,
            packet_id="PACKET-CAPTURE",
            packet_hash=self.packet_hash,
            manifest={"packet_hash": self.packet_hash, "run_id": self.run_id},
            actor="packet-worker",
            idempotency_key="packet-ready",
        )
        job = self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.BROWSER_PREPARING,
            actor="browser-worker",
            idempotency_key="browser-preparing",
        )
        prompt = (
            "독립적으로 조사하라.\n"
            f"[[E2R_PRO_RUN_ID:{self.run_id}]]\n"
            f"[[E2R_PRO_JOB_ID:{job.job_id}]]"
        )
        prompt_hash = canonical_hash({"prompt": prompt})
        prepared = await self.adapter.prepare_without_submit(
            browser_session_id="BROWSER-capture",
            packet_path=self.packet_path,
            packet_hash=self.packet_hash,
            prompt=prompt,
            prompt_hash=prompt_hash,
        )
        job = self.store.record_browser_prepared(
            job.job_id,
            expected_version=job.state_version,
            browser_session_id=prepared.browser_session_id,
            conversation_id=prepared.conversation_id,
            adapter_name="PlaywrightChatGPTWebAdapter",
            packet_hash=prepared.packet_hash,
            prompt_hash=prepared.prompt_hash,
            state={"state": prepared.state.value},
            actor="browser-worker",
            idempotency_key="browser-prepared",
        )
        approvals = ProApprovalService(self.store, now=lambda: self.now)
        grant = approvals.issue(job.job_id, prompt_hash=prompt_hash)
        approvals.approve(grant, actor="user-thread-approved")
        running = await ExactlyOnceSubmitCoordinator(self.store).submit(job.job_id, self.adapter)
        return running.job, prompt_hash

    def _filename(self, job_id: str) -> str:
        return f"E2R_PRO_{job_id}_{self.symbol}_{self.as_of_date}.md"

    async def _complete_page(
        self, job_id: str, *, direct: bool = False, with_pdf: bool = False
    ) -> None:
        await self.page.evaluate(
            "([state, context]) => window.__setMockState(state, context)",
            [
                (
                    "COMPLETE_WITH_DIRECT_REPORT"
                    if direct
                    else "COMPLETE_WITH_MD_AND_PDF"
                    if with_pdf
                    else "COMPLETE_WITH_MD"
                ),
                {
                    "job_id": job_id,
                    "run_id": self.run_id,
                    "target_id": self.symbol,
                    "as_of_date": self.as_of_date,
                    "filename": self._filename(job_id),
                },
            ],
        )

    async def _stable_completion(self, job_id: str):
        monitor = BrowserCompletionMonitor(
            self.adapter, required_stable_observations=3, poll_interval_seconds=0.01
        )
        observations = [
            await monitor.observe(job_id=job_id, run_id=self.run_id) for _ in range(3)
        ]
        self.assertFalse(observations[0].completion_confirmed)
        self.assertFalse(observations[1].completion_confirmed)
        self.assertTrue(observations[2].completion_confirmed)
        return observations[-1]

    async def test_running_not_misclassified_complete(self) -> None:
        job, _prompt_hash = await self._running_job()
        monitor = BrowserCompletionMonitor(self.adapter, required_stable_observations=3)
        for _ in range(4):
            observed = await monitor.observe(job_id=job.job_id, run_id=self.run_id)
            self.assertFalse(observed.completion_confirmed)
            self.assertEqual(observed.inspection.state, BrowserUIState.RESEARCH_RUNNING)

    async def test_stable_hash_completion(self) -> None:
        job, _prompt_hash = await self._running_job()
        await self._complete_page(job.job_id)
        observed = await self._stable_completion(job.job_id)
        self.assertEqual(observed.stable_observations, 3)
        self.assertTrue(observed.result and observed.result.structurally_complete)

    async def test_wrong_job_or_run_marker_never_completes(self) -> None:
        job, _prompt_hash = await self._running_job()
        await self._complete_page(job.job_id)
        monitor = BrowserCompletionMonitor(self.adapter, required_stable_observations=2)
        for _ in range(3):
            observed = await monitor.observe(job_id="PROJOB-wrong", run_id=self.run_id)
            self.assertFalse(observed.completion_confirmed)
            self.assertEqual(observed.stable_observations, 0)
        observed = await monitor.observe(job_id=job.job_id, run_id="PRORUN-wrong")
        self.assertFalse(observed.completion_confirmed)

    async def test_changed_hash_restarts_stability_count(self) -> None:
        job, _prompt_hash = await self._running_job()
        await self._complete_page(job.job_id)
        monitor = BrowserCompletionMonitor(self.adapter, required_stable_observations=3)
        await monitor.observe(job_id=job.job_id, run_id=self.run_id)
        second = await monitor.observe(job_id=job.job_id, run_id=self.run_id)
        self.assertEqual(second.stable_observations, 2)
        await self.page.locator('[data-message-id="final-turn"] pre').evaluate(
            "node => node.textContent += '\\nlate mutation'"
        )
        changed = await monitor.observe(job_id=job.job_id, run_id=self.run_id)
        self.assertEqual(changed.stable_observations, 1)
        self.assertFalse(changed.completion_confirmed)

    async def test_clarification_state(self) -> None:
        job, _prompt_hash = await self._running_job()
        await self.page.evaluate("window.__setMockState('CLARIFICATION')")
        service = ProCompletionStateService(
            self.store, BrowserCompletionMonitor(self.adapter, required_stable_observations=2)
        )
        updated, observed = await service.observe_job(job.job_id, run_id=self.run_id)
        self.assertEqual(observed.inspection.state, BrowserUIState.AWAITING_CLARIFICATION)
        self.assertEqual(updated.status, JobStatus.AWAITING_CLARIFICATION.value)

    async def test_quota_state(self) -> None:
        job, _prompt_hash = await self._running_job()
        await self.page.evaluate("window.__setMockState('QUOTA')")
        service = ProCompletionStateService(
            self.store, BrowserCompletionMonitor(self.adapter, required_stable_observations=2)
        )
        updated, _observed = await service.observe_job(job.job_id, run_id=self.run_id)
        self.assertEqual(updated.status, JobStatus.QUOTA_PENDING.value)

    async def test_retryable_error_does_not_auto_resubmit(self) -> None:
        job, _prompt_hash = await self._running_job()
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 1)
        await self.page.evaluate("window.__setMockState('ERROR')")
        service = ProCompletionStateService(
            self.store, BrowserCompletionMonitor(self.adapter, required_stable_observations=2)
        )
        updated, _observed = await service.observe_job(job.job_id, run_id=self.run_id)
        self.assertEqual(updated.status, JobStatus.FAILED_RETRYABLE.value)
        self.assertEqual(updated.submit_count, 1)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 1)

    async def test_ui_incompatible_safe_stop(self) -> None:
        job, _prompt_hash = await self._running_job()
        await self.page.set_content("<body><p>unknown UI</p></body>")
        service = ProCompletionStateService(
            self.store, BrowserCompletionMonitor(self.adapter, required_stable_observations=2)
        )
        updated, _observed = await service.observe_job(job.job_id, run_id=self.run_id)
        self.assertEqual(updated.status, JobStatus.USER_ATTENTION_REQUIRED.value)
        self.assertEqual(updated.submit_count, 1)

    async def test_old_md_button_not_downloaded_and_new_preview_downloaded(self) -> None:
        job, _prompt_hash = await self._running_job()
        await self._complete_page(job.job_id)
        observed = await self._stable_completion(job.job_id)
        root = Path(self.temporary_directory.name) / "new-md"
        raw = await self.adapter.capture_result(
            BrowserCaptureRequest(
                job_id=job.job_id,
                run_id=self.run_id,
                expected_filename=self._filename(job.job_id),
                expected_report_hash=observed.result.report_hash,  # type: ignore[union-attr]
                staging_directory=root / "capture/.staging",
            )
        )
        self.assertEqual(raw.source, "DOWNLOAD_MD")
        self.assertGreater(raw.report_md_part_path.stat().st_size, 0)
        clicks = await self.page.evaluate("window.__downloadClicks")
        self.assertEqual(clicks, [self._filename(job.job_id)])
        self.assertNotIn("old_result.md", clicks)

    async def test_direct_report_fallback(self) -> None:
        job, _prompt_hash = await self._running_job()
        await self._complete_page(job.job_id, direct=True)
        observed = await self._stable_completion(job.job_id)
        root = Path(self.temporary_directory.name) / "direct"
        raw = await self.adapter.capture_result(
            BrowserCaptureRequest(
                job_id=job.job_id,
                run_id=self.run_id,
                expected_filename=self._filename(job.job_id),
                expected_report_hash=observed.result.report_hash,  # type: ignore[union-attr]
                staging_directory=root / "capture/.staging",
            )
        )
        self.assertEqual(raw.source, "DIRECT_REPORT_DOM")
        self.assertIn("E2R_RESEARCH_DOSSIER_JSON_BEGIN", raw.report_md_part_path.read_text())
        self.assertEqual(await self.page.evaluate("window.__downloadClicks"), [])

    async def test_optional_pdf_is_captured_when_matching_export_exists(self) -> None:
        job, prompt_hash = await self._running_job()
        await self._complete_page(job.job_id, with_pdf=True)
        observed = await self._stable_completion(job.job_id)
        root = Path(self.temporary_directory.name) / "with-pdf"
        raw = await self.adapter.capture_result(
            BrowserCaptureRequest(
                job_id=job.job_id,
                run_id=self.run_id,
                expected_filename=self._filename(job.job_id),
                expected_report_hash=observed.result.report_hash,  # type: ignore[union-attr]
                staging_directory=root / "capture/.staging",
            )
        )
        self.assertIsNotNone(raw.report_pdf_part_path)
        self.assertTrue(raw.report_pdf_part_path.read_bytes().startswith(b"%PDF-"))
        self.assertIsNone(raw.optional_pdf_error)
        self.assertEqual(
            await self.page.evaluate("window.__downloadClicks"),
            [self._filename(job.job_id), self._filename(job.job_id).replace(".md", ".pdf")],
        )
        result = AtomicCaptureWriter(now=lambda: self.now).finalize(
            root,
            identity=CaptureIdentity(
                job_id=job.job_id,
                run_id=self.run_id,
                target_id=self.symbol,
                as_of_date=self.as_of_date,
                packet_hash=self.packet_hash,
                prompt_hash=prompt_hash,
                conversation_id=job.conversation_id,
                capture_mode="DOM_CONTRACT_MOCK",
            ),
            raw_capture=raw,
        )
        self.assertIsNotNone(result.receipt.report_pdf_hash)
        self.assertTrue((root / "capture/incoming/pro_report.pdf").is_file())

    async def test_download_expectation_hashes_ready_last_and_dispatch(self) -> None:
        job, _prompt_hash = await self._running_job()
        await self._complete_page(job.job_id)
        monitor = BrowserCompletionMonitor(self.adapter, required_stable_observations=3)
        service = ProCompletionStateService(self.store, monitor)
        for _ in range(3):
            detected, observed = await service.observe_job(job.job_id, run_id=self.run_id)
        self.assertEqual(detected.status, JobStatus.RESULT_DETECTED.value)
        events = []
        dispatcher = CaptureEventDispatcher()
        dispatcher.subscribe(events.append)
        root = Path(self.temporary_directory.name) / "coordinated"
        replace_order: list[str] = []
        real_replace = os.replace

        def recording_replace(source, destination):
            replace_order.append(Path(destination).name)
            return real_replace(source, destination)

        with patch("e2r.pro_first.capture.atomic_capture.os.replace", side_effect=recording_replace):
            completed, result = await ProCaptureCoordinator(
                self.store,
                writer=AtomicCaptureWriter(now=lambda: self.now),
                dispatcher=dispatcher,
            ).capture(
                job.job_id,
                run_id=self.run_id,
                expected_filename=self._filename(job.job_id),
                expected_report_hash=observed.result.report_hash,  # type: ignore[union-attr]
                job_root=root,
                adapter=self.adapter,
                capture_mode="DOM_CONTRACT_MOCK",
            )
        self.assertEqual(replace_order[-1], "READY.json")
        self.assertEqual(completed.status, JobStatus.CAPTURE_COMPLETE.value)
        self.assertEqual(completed.capture_count, 1)
        self.assertEqual(len(events), 1)
        receipt = load_capture_receipt(result.receipt_path)
        self.assertEqual(file_sha256(root / receipt.report_md_path), receipt.report_md_hash)
        self.assertEqual(file_sha256(root / receipt.dossier_json_path), receipt.dossier_json_hash)
        self.assertTrue(result.ready_path.is_file())
        self.assertEqual(await self.page.evaluate("window.__downloadClicks"), [self._filename(job.job_id)])

    async def test_partial_file_not_reconciled(self) -> None:
        root = Path(self.temporary_directory.name) / "partial"
        part = root / "capture/.staging/pro_report.md.part"
        part.parent.mkdir(parents=True)
        part.write_text("partial", encoding="utf-8")
        reconciled = await CaptureFilesystemReconciler(self.store).reconcile(root)
        self.assertIsNone(reconciled)

    async def test_backend_restart_recovers_ready_capture_idempotently(self) -> None:
        job, prompt_hash = await self._running_job()
        await self._complete_page(job.job_id, direct=True)
        observed = await self._stable_completion(job.job_id)
        detected = self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.RESULT_DETECTED,
            actor="test-monitor",
            idempotency_key="detected-before-crash",
        )
        capturing = self.store.transition(
            job.job_id,
            expected_version=detected.state_version,
            to_status=JobStatus.CAPTURING_ARTIFACTS,
            actor="test-capture",
            idempotency_key="capturing-before-crash",
        )
        root = Path(self.temporary_directory.name) / "restart"
        raw = await self.adapter.capture_result(
            BrowserCaptureRequest(
                job_id=job.job_id,
                run_id=self.run_id,
                expected_filename=self._filename(job.job_id),
                expected_report_hash=observed.result.report_hash,  # type: ignore[union-attr]
                staging_directory=root / "capture/.staging",
            )
        )
        AtomicCaptureWriter(now=lambda: self.now).finalize(
            root,
            identity=CaptureIdentity(
                job_id=job.job_id,
                run_id=self.run_id,
                target_id=self.symbol,
                as_of_date=self.as_of_date,
                packet_hash=self.packet_hash,
                prompt_hash=prompt_hash,
                conversation_id=capturing.conversation_id,
                capture_mode="DOM_CONTRACT_MOCK",
            ),
            raw_capture=raw,
        )
        restarted_store = ProFirstJobStore(self.database_path, now=lambda: self.now)
        reconciler = CaptureFilesystemReconciler(restarted_store)
        first = await reconciler.reconcile(root)
        second = await reconciler.reconcile(root)
        self.assertIsNotNone(first)
        self.assertEqual(first, second)
        recovered = restarted_store.get_job(job.job_id)
        self.assertEqual(recovered.status, JobStatus.CAPTURE_COMPLETE.value)
        self.assertEqual(recovered.capture_count, 1)
        matching = [
            event
            for event in restarted_store.list_events(job.job_id)
            if event.to_status == JobStatus.CAPTURE_COMPLETE.value
        ]
        self.assertEqual(len(matching), 1)


if __name__ == "__main__":
    unittest.main()
