from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import unittest

from e2r.pro_first.approval import (
    ConsumedApprovalProof,
    ExactlyOnceSubmitCoordinator,
    ProApprovalService,
)
from e2r.pro_first.browser.chatgpt_adapter import PlaywrightChatGPTWebAdapter
from e2r.pro_first.browser.mock_chatgpt_app import MockChatGPTServer
from e2r.pro_first.browser.protocol import SubmitAuthorizationRequired
from e2r.pro_first.browser.protocol import BrowserUIIncompatible
from e2r.pro_first.ids import canonical_hash
from e2r.pro_first.job_store import (
    ApprovalInvalid,
    DuplicateSubmitBlocked,
    ProFirstJobStore,
)
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow


class ProFirstApprovalSubmitTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.server = MockChatGPTServer()
        self.server.__enter__()
        self.addCleanup(self.server.__exit__, None, None, None)
        self.now = datetime(2026, 8, 22, 1, 0, tzinfo=timezone.utc)
        self.store = ProFirstJobStore(
            Path(self.temporary_directory.name) / "approval.sqlite3",
            now=lambda: self.now,
        )
        self.packet_path = Path(self.temporary_directory.name) / "research_packet.json"
        self.packet_payload = {"schema_version": "e2r_pro_research_packet_v1"}
        self.packet_path.write_text(json.dumps(self.packet_payload), encoding="utf-8")
        self.packet_hash = canonical_hash(self.packet_payload)
        self.prompt = (
            "독립적으로 조사하라.\n"
            "[[E2R_PRO_RUN_ID:PRORUN-bbbbbbbbbbbbbbbbbbbbbbbb]]\n"
            "[[E2R_PRO_JOB_ID:{job_id}]]"
        )

    async def asyncSetUp(self) -> None:
        from playwright.async_api import async_playwright

        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.page = await self.browser.new_page()
        await self.page.goto(
            f"{self.server.base_url}/c/approval-conversation",
            wait_until="domcontentloaded",
        )
        self.adapter = PlaywrightChatGPTWebAdapter(self.page)

    async def asyncTearDown(self) -> None:
        await self.browser.close()
        await self.playwright.stop()

    async def _prepare_durable_job(self):
        candidate = self.store.create_candidate(
            symbol="123456",
            company_name="검증기업",
            as_of_date="2026-08-22",
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="approval-trigger",
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
            packet_id="PACKET-APPROVAL",
            packet_hash=self.packet_hash,
            manifest={"packet_hash": self.packet_hash},
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
        prompt = self.prompt.format(job_id=job.job_id)
        prompt_hash = canonical_hash({"prompt": prompt})
        prepared = await self.adapter.prepare_without_submit(
            browser_session_id="BROWSER-approval",
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
            state={
                "state": prepared.state.value,
                "uploaded_filename": prepared.uploaded_filename,
                "submit_count": prepared.submit_count,
            },
            actor="browser-worker",
            idempotency_key="browser-prepared",
        )
        return job, prompt_hash

    async def test_send_exactly_once_after_approval(self) -> None:
        job, prompt_hash = await self._prepare_durable_job()
        service = ProApprovalService(self.store, now=lambda: self.now)
        grant = service.issue(job.job_id, prompt_hash=prompt_hash)
        approved = service.approve(grant)
        self.assertEqual(approved.status, JobStatus.APPROVED.value)

        result = await ExactlyOnceSubmitCoordinator(self.store).submit(
            job.job_id, self.adapter
        )
        self.assertEqual(result.job.status, JobStatus.RESEARCH_RUNNING.value)
        self.assertEqual(result.job.submit_count, 1)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 1)

        with self.assertRaises(DuplicateSubmitBlocked):
            await ExactlyOnceSubmitCoordinator(self.store).submit(job.job_id, self.adapter)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 1)

    async def test_first_submit_persists_new_conversation_id(self) -> None:
        await self.page.goto(
            f"{self.server.base_url}/",
            wait_until="domcontentloaded",
        )
        self.adapter = PlaywrightChatGPTWebAdapter(self.page)
        job, prompt_hash = await self._prepare_durable_job()
        self.assertIsNone(job.conversation_id)
        await self.page.locator("#composer-submit-button").evaluate(
            """button => button.addEventListener(
                'click',
                () => history.pushState({}, '', '/c/new-conversation-id'),
                {once: true}
            )"""
        )
        service = ProApprovalService(self.store, now=lambda: self.now)
        grant = service.issue(job.job_id, prompt_hash=prompt_hash)
        service.approve(grant)

        result = await ExactlyOnceSubmitCoordinator(self.store).submit(
            job.job_id, self.adapter
        )
        self.assertEqual(result.job.conversation_id, "new-conversation-id")
        self.assertEqual(result.inspection.conversation_id, "new-conversation-id")
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 1)

    async def test_forged_or_missing_approval_proof_cannot_click_send(self) -> None:
        job, _prompt_hash = await self._prepare_durable_job()
        forged = ConsumedApprovalProof(
            job_id=job.job_id,
            packet_hash=self.packet_hash,
            prompt_hash="f" * 64,
            browser_session_id="BROWSER-approval",
            conversation_id="approval-conversation",
            approval_consumed_at="2026-08-22T01:00:00Z",
            submit_count=1,
            _capability=object(),
        )
        with self.assertRaises(SubmitAuthorizationRequired):
            await self.adapter.submit_once(forged)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

    async def test_packet_change_invalidates_approval(self) -> None:
        job, prompt_hash = await self._prepare_durable_job()
        service = ProApprovalService(self.store, now=lambda: self.now)
        grant = service.issue(job.job_id, prompt_hash=prompt_hash)
        with self.store._transaction() as connection:
            connection.execute(
                "UPDATE pro_research_jobs SET packet_hash=? WHERE job_id=?",
                ("d" * 64, job.job_id),
            )
        with self.assertRaisesRegex(ApprovalInvalid, "packet hash changed"):
            service.approve(grant)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

    async def test_approval_issue_rejects_prompt_not_prepared_in_browser(self) -> None:
        job, _prompt_hash = await self._prepare_durable_job()
        service = ProApprovalService(self.store, now=lambda: self.now)
        with self.assertRaisesRegex(ApprovalInvalid, "prepared browser content"):
            service.issue(job.job_id, prompt_hash="a" * 64)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

    async def test_click_failure_never_auto_resubmits(self) -> None:
        job, prompt_hash = await self._prepare_durable_job()
        service = ProApprovalService(self.store, now=lambda: self.now)
        grant = service.issue(job.job_id, prompt_hash=prompt_hash)
        service.approve(grant)
        await self.page.locator('#composer-submit-button').evaluate(
            "button => button.disabled = true"
        )
        with self.assertRaises(BrowserUIIncompatible):
            await ExactlyOnceSubmitCoordinator(self.store).submit(job.job_id, self.adapter)
        attention = self.store.get_job(job.job_id)
        self.assertEqual(attention.status, JobStatus.USER_ATTENTION_REQUIRED.value)
        self.assertEqual(attention.submit_count, 1)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)
        await self.page.locator('#composer-submit-button').evaluate(
            "button => button.disabled = false"
        )
        with self.assertRaises(DuplicateSubmitBlocked):
            await ExactlyOnceSubmitCoordinator(self.store).submit(job.job_id, self.adapter)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)


if __name__ == "__main__":
    unittest.main()
