from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from e2r.pro_first.browser.protocol import (
    BrowserInspection,
    BrowserSubmittedTurnPersistence,
    BrowserUIState,
    PreparedFollowupPass,
)
from e2r.pro_first.browser.chatgpt_adapter import PlaywrightChatGPTWebAdapter
from e2r.pro_first.browser.mock_chatgpt_app import MockChatGPTServer
from e2r.pro_first.ids import canonical_hash
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.multi_pass import (
    FollowupPassPlan,
    FollowupSubmitBlocked,
    ProMultiPassResearchOrchestrator,
    RepeatedGapReopenHardFail,
    ResearchPassStatus,
    ScopeApprovalRequired,
    TransportPendingDecision,
)


ARCHETYPE = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
INTERCEPTED_CLICK_REASON = (
    "TimeoutError: Locator.click: Timeout 30000ms exceeded; "
    '<div role="dialog" data-testid="modal-global-search"> '
    "intercepts pointer events"
)
UNSTABLE_SEND_REASON = (
    "TimeoutError: Locator.click: Timeout 30000ms exceeded; "
    "waiting for element to be visible, enabled and stable; "
    'locator(\'[data-testid="composer-submit-button"]\')'
)


class _FakeSameConversationAdapter:
    def __init__(
        self,
        conversation_id: str,
        *,
        persistence_results: tuple[bool, ...] = (True,),
    ) -> None:
        self.conversation_id = conversation_id
        self.persistence_results = persistence_results
        self.prepared: PreparedFollowupPass | None = None
        self.submit_count = 0
        self.persistence_count = 0
        self.proofs: list[object] = []

    async def prepare_followup_without_submit(self, **kwargs) -> PreparedFollowupPass:
        if kwargs["conversation_id"] != self.conversation_id:
            raise RuntimeError("conversation mismatch")
        self.prepared = PreparedFollowupPass(
            browser_session_id=kwargs["browser_session_id"],
            conversation_id=self.conversation_id,
            state=BrowserUIState.AWAITING_USER_APPROVAL,
            job_id=kwargs["job_id"],
            pass_id=kwargs["pass_id"],
            parent_pass_id=kwargs["parent_pass_id"],
            prompt_hash=kwargs["prompt_hash"],
            prompt_preview=kwargs["prompt"][:500],
            send_ready=True,
            preexisting_attachment_keys=(),
        )
        return self.prepared

    async def submit_once(self, proof) -> BrowserInspection:
        if not proof.ledger_verified:
            raise PermissionError("durable pass claim required")
        if self.prepared is None or proof.pass_id != self.prepared.pass_id:
            raise PermissionError("proof differs from prepared pass")
        self.submit_count += 1
        self.proofs.append(proof)
        return BrowserInspection(
            state=BrowserUIState.RESEARCH_RUNNING,
            conversation_id=self.conversation_id,
            editor_ready=True,
            deep_research_ready=True,
            packet_uploaded=True,
            prompt_ready=False,
            send_ready=False,
            stop_visible=True,
        )

    async def inspect_submitted_turn_persistence(
        self,
        *,
        conversation_id: str,
        job_id: str,
        run_id: str | None = None,
        pass_id: str | None = None,
        parent_pass_id: str | None = None,
    ) -> BrowserSubmittedTurnPersistence:
        self.persistence_count += 1
        required = [f"[[E2R_PRO_JOB_ID:{job_id}]]"]
        if run_id is not None:
            required.append(f"[[E2R_PRO_RUN_ID:{run_id}]]")
        if pass_id is not None:
            required.extend(
                (
                    f"[[E2R_PRO_PASS_ID:{pass_id}]]",
                    f"[[E2R_PRO_PARENT_PASS_ID:{parent_pass_id}]]",
                )
            )
        confirmed = self.persistence_results[
            min(self.persistence_count - 1, len(self.persistence_results) - 1)
        ]
        return BrowserSubmittedTurnPersistence(
            observation_id=f"PROSERVERVIEW-FAKE-{self.persistence_count}",
            observed_at="2026-08-22T01:02:03Z",
            conversation_id=conversation_id,
            job_id=job_id,
            run_id=run_id,
            pass_id=pass_id,
            parent_pass_id=parent_pass_id,
            persistence_confirmed=confirmed,
            user_turn_id=(f"user-turn-{self.submit_count}" if confirmed else None),
            required_markers=tuple(required),
            missing_markers=(() if confirmed else tuple(required)),
            observed_user_turn_count=(1 if confirmed else 0),
            fresh_page_url=f"https://chatgpt.com/c/{conversation_id}",
            fresh_page_loaded=True,
        )

    async def inspect_state(self) -> BrowserInspection:
        return BrowserInspection(
            state=BrowserUIState.RESEARCH_RUNNING,
            conversation_id=self.conversation_id,
            editor_ready=True,
            deep_research_ready=True,
            packet_uploaded=True,
            prompt_ready=False,
            send_ready=False,
            stop_visible=True,
        )

    async def prepare_intercepted_followup_submit_recovery(
        self,
        proof,
        *,
        transport_pending_reason: str,
    ) -> None:
        if not proof.ledger_verified or proof.submit_count != 1:
            raise PermissionError("durable claimed proof required")
        if transport_pending_reason not in {
            INTERCEPTED_CLICK_REASON,
            UNSTABLE_SEND_REASON,
        }:
            raise PermissionError("transport proof changed")


class ProFirstV2MultiPassTest(unittest.IsolatedAsyncioTestCase):
    now = datetime(2026, 8, 22, 1, 2, 3, tzinfo=timezone.utc)

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.store = ProFirstJobStore(
            Path(self.temporary_directory.name) / "multi-pass.sqlite3",
            now=lambda: self.now,
        )
        self.job = self._running_approved_job()
        self.orchestrator = ProMultiPassResearchOrchestrator(self.store)
        self.scope = self.orchestrator.record_completed_initial_pass(
            self.job.job_id,
            primary_archetype_ids=(ARCHETYPE,),
            response_hash="c" * 64,
        )
        self.packet = {
            "job_id": self.job.job_id,
            "run_id": "RUN-MULTIPASS",
            "conversation_id": self.scope.conversation_id,
            "target": {
                "symbol": self.job.symbol,
                "company_name": self.job.company_name,
            },
            "as_of_date": self.job.as_of_date,
            "candidate_archetypes": [ARCHETYPE],
            "research_mode": "FULL_RESEARCH",
        }
        self.question = {
            "archetype_id": ARCHETYPE,
            "question_family_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01",
            "status": "PUBLIC_SEARCHABLE",
            "could_change_score": True,
            "could_change_stage": False,
            "could_change_hard_break": False,
        }

    def _running_approved_job(self):
        candidate = self.store.create_candidate(
            symbol="000660",
            company_name="검증기업",
            as_of_date="2026-08-22",
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="multi-pass-trigger",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={"production_candidate": True},
        )
        job = self.store.create_job(
            candidate.candidate_id,
            archetype_ids=(ARCHETYPE,),
        )
        job = self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.PACKET_BUILDING,
            actor="test",
            idempotency_key="packet-building",
        )
        job = self.store.record_packet(
            job.job_id,
            expected_version=job.state_version,
            packet_id="PACKET-MULTIPASS",
            packet_hash="a" * 64,
            manifest={"packet_hash": "a" * 64},
            actor="test",
            idempotency_key="packet-ready",
        )
        job = self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.BROWSER_PREPARING,
            actor="test",
            idempotency_key="browser-preparing",
        )
        job = self.store.record_browser_prepared(
            job.job_id,
            expected_version=job.state_version,
            browser_session_id="BROWSER-MULTIPASS",
            conversation_id="CONVERSATION-MULTIPASS",
            adapter_name="FakeAdapter",
            packet_hash="a" * 64,
            prompt_hash="b" * 64,
            state={"state": "AWAITING_USER_APPROVAL"},
            actor="test",
            idempotency_key="browser-prepared",
        )
        job, nonce = self.store.issue_approval_nonce(
            job.job_id,
            expected_version=job.state_version,
            actor="test",
            idempotency_key="approval-issued",
            prompt_hash="b" * 64,
            expires_at="2026-08-23T01:02:03Z",
        )
        job = self.store.consume_approval_nonce(
            job.job_id,
            nonce,
            expected_version=job.state_version,
            actor="user",
            idempotency_key="approval-consumed",
            prompt_hash="b" * 64,
        )
        job = self.store.claim_submit(
            job.job_id,
            expected_version=job.state_version,
            actor="test",
            idempotency_key="initial-submit",
        )
        return self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.RESEARCH_RUNNING,
            actor="test",
            idempotency_key="initial-running",
        )

    def _public_plan(self) -> FollowupPassPlan:
        result = self.orchestrator.plan_next_material_pass(
            job_id=self.job.job_id,
            packet=self.packet,
            dossier={"question_family_results": [self.question]},
            primary_archetype_ids=(ARCHETYPE,),
        )
        self.assertIsInstance(result, FollowupPassPlan)
        return result

    def test_initial_pass_routes_public_gap_to_followup(self) -> None:
        plan = self._public_plan()
        self.assertEqual(plan.research_pass.pass_name, "PUBLIC_GAP_CLOSURE")
        self.assertEqual(plan.research_pass.parent_pass_id, self.scope.initial_pass_id)
        self.assertIn(self.question["question_family_id"], plan.prompt_text)

    def test_initial_pass_then_public_gap_followup_same_conversation(self) -> None:
        plan = self._public_plan()
        self.assertEqual(plan.research_pass.conversation_id, self.scope.conversation_id)
        self.assertIn(self.scope.conversation_id, plan.prompt_text)

    async def test_same_conversation_is_reused(self) -> None:
        plan = self._public_plan()
        adapter = _FakeSameConversationAdapter(self.scope.conversation_id)
        prepared = await self.orchestrator.prepare_followup(plan, adapter)
        submitted = await self.orchestrator.submit_followup(plan, adapter)
        self.assertEqual(prepared.conversation_id, self.scope.conversation_id)
        self.assertEqual(submitted.inspection.conversation_id, self.scope.conversation_id)
        self.assertEqual(adapter.submit_count, 1)

    async def test_browser_mock_followup_click_reuses_same_conversation(self) -> None:
        from playwright.async_api import async_playwright

        plan = self._public_plan()
        with MockChatGPTServer() as server:
            playwright = await async_playwright().start()
            browser = await playwright.chromium.launch(headless=True)
            try:
                page = await browser.new_page()
                await page.goto(
                    f"{server.base_url}/c/{self.scope.conversation_id}",
                    wait_until="domcontentloaded",
                )
                adapter = PlaywrightChatGPTWebAdapter(page)
                prepared = await self.orchestrator.prepare_followup(plan, adapter)
                submitted = await self.orchestrator.submit_followup(plan, adapter)
                self.assertEqual(prepared.conversation_id, self.scope.conversation_id)
                self.assertEqual(
                    submitted.inspection.conversation_id,
                    self.scope.conversation_id,
                )
                self.assertEqual(await page.evaluate("window.__submitCount"), 1)
            finally:
                await browser.close()
                await playwright.stop()

    async def test_stale_prior_pass_marker_cannot_confirm_current_pass(self) -> None:
        from playwright.async_api import async_playwright

        plan = self._public_plan()
        old_pass_id = "PROPASS-stale-prior-turn"
        parent_pass_id = str(plan.research_pass.parent_pass_id)
        with MockChatGPTServer() as server:
            playwright = await async_playwright().start()
            browser = await playwright.chromium.launch(headless=True)
            try:
                page = await browser.new_page()
                await page.goto(
                    f"{server.base_url}/c/{self.scope.conversation_id}",
                    wait_until="domcontentloaded",
                )
                stale_prompt = "\n".join(
                    (
                        f"[[E2R_PRO_JOB_ID:{self.job.job_id}]]",
                        f"[[E2R_PRO_PASS_ID:{old_pass_id}]]",
                        f"[[E2R_PRO_PARENT_PASS_ID:{parent_pass_id}]]",
                    )
                )
                await page.locator("#prompt-textarea").fill(stale_prompt)
                await page.locator("#composer-submit-button").click()
                adapter = PlaywrightChatGPTWebAdapter(
                    page,
                    server_persistence_max_polls=2,
                    server_persistence_poll_interval_ms=10,
                )
                original_page_count = len(page.context.pages)

                stale = await adapter.inspect_submitted_turn_persistence(
                    conversation_id=self.scope.conversation_id,
                    job_id=self.job.job_id,
                    pass_id=old_pass_id,
                    parent_pass_id=parent_pass_id,
                )
                current = await adapter.inspect_submitted_turn_persistence(
                    conversation_id=self.scope.conversation_id,
                    job_id=self.job.job_id,
                    pass_id=plan.research_pass.pass_id,
                    parent_pass_id=parent_pass_id,
                )

                self.assertTrue(stale.persistence_confirmed)
                self.assertFalse(current.persistence_confirmed)
                self.assertIn(
                    f"[[E2R_PRO_PASS_ID:{plan.research_pass.pass_id}]]",
                    current.missing_markers,
                )
                self.assertEqual(len(page.context.pages), original_page_count)
                self.assertEqual(await page.evaluate("window.__submitCount"), 1)
            finally:
                await browser.close()
                await playwright.stop()

    async def test_browser_recovers_modal_intercepted_click_under_same_claim(
        self,
    ) -> None:
        from playwright.async_api import async_playwright

        plan = self._public_plan()
        with MockChatGPTServer() as server:
            playwright = await async_playwright().start()
            browser = await playwright.chromium.launch(headless=True)
            try:
                page = await browser.new_page()
                await page.goto(
                    f"{server.base_url}/c/{self.scope.conversation_id}",
                    wait_until="domcontentloaded",
                )
                adapter = PlaywrightChatGPTWebAdapter(page)
                await self.orchestrator.prepare_followup(plan, adapter)
                claimed = self.orchestrator.ledger.claim_submit(
                    plan.research_pass.pass_id
                )
                self.orchestrator.ledger.mark_transport_pending(
                    claimed.pass_id,
                    reason=INTERCEPTED_CLICK_REASON,
                )
                await page.evaluate(
                    """() => {
                        const modal = document.createElement('div');
                        modal.setAttribute('role', 'dialog');
                        modal.dataset.testid = 'modal-global-search';
                        modal.style.cssText = 'position:fixed;inset:0;z-index:9999';
                        document.body.appendChild(modal);
                        document.addEventListener('keydown', event => {
                            if (event.key === 'Escape') modal.remove();
                        }, {once: true});
                    }"""
                )

                resumed = await self.orchestrator.resume_intercepted_followup_submit(
                    plan,
                    adapter,
                )

                self.assertEqual(resumed.research_pass.status, "RESEARCH_RUNNING")
                self.assertEqual(resumed.research_pass.submit_count, 1)
                self.assertTrue(
                    resumed.research_pass.detail["intercepted_submit_recovered"]
                )
                self.assertEqual(await page.evaluate("window.__submitCount"), 1)
                self.assertEqual(
                    await page.locator(
                        '[data-testid="modal-global-search"]'
                    ).count(),
                    0,
                )
            finally:
                await browser.close()
                await playwright.stop()

    async def test_followup_is_authorized_by_initial_job_approval(self) -> None:
        plan = self._public_plan()
        adapter = _FakeSameConversationAdapter(self.scope.conversation_id)
        await self.orchestrator.prepare_followup(plan, adapter)
        submitted = await self.orchestrator.submit_followup(plan, adapter)
        proof = adapter.proofs[0]
        self.assertEqual(proof.approval_scope_id, self.scope.approval_scope_id)
        self.assertTrue(proof.ledger_verified)
        self.assertEqual(submitted.research_pass.submit_count, 1)

    def test_user_approval_covers_bounded_same_scope_followups(self) -> None:
        public = self._public_plan()
        self.assertEqual(public.scope.approval_scope_id, self.scope.approval_scope_id)
        self.assertIn("PUBLIC_GAP_CLOSURE", self.scope.allowed_followup_pass_names)
        self.assertIn("VERIFIER_REPAIR", self.scope.allowed_followup_pass_names)

    def test_scope_change_requires_new_approval(self) -> None:
        changed_date = dict(self.packet)
        changed_date["as_of_date"] = "2026-08-23"
        changed_target = {
            **self.packet,
            "target": {"symbol": "005930", "company_name": "다른기업"},
        }
        for changed in (changed_date, changed_target):
            with self.subTest(changed=changed["target"], as_of=changed["as_of_date"]):
                with self.assertRaises(ScopeApprovalRequired):
                    self.orchestrator.plan_followup(
                        job_id=self.job.job_id,
                        packet=changed,
                        primary_archetype_ids=(ARCHETYPE,),
                        pass_name="PUBLIC_GAP_CLOSURE",
                    )
        with self.assertRaises(ScopeApprovalRequired):
            self.orchestrator.plan_followup(
                job_id=self.job.job_id,
                packet=self.packet,
                primary_archetype_ids=(ARCHETYPE,),
                pass_name="PUBLIC_GAP_CLOSURE",
                pass_inputs={"requires_private_account": True},
            )
        with self.assertRaises(ScopeApprovalRequired):
            self.orchestrator.plan_followup(
                job_id=self.job.job_id,
                packet=self.packet,
                primary_archetype_ids=(ARCHETYPE,),
                pass_name="PUBLIC_GAP_CLOSURE",
                pass_inputs={"investment_assumption_required": True},
            )

    def test_counter_supersession_pass_same_conversation(self) -> None:
        counter = dict(self.question)
        counter["status"] = "CONTRADICTED_UNRESOLVED"
        result = self.orchestrator.plan_next_material_pass(
            job_id=self.job.job_id,
            packet=self.packet,
            dossier={"question_family_results": [counter]},
            primary_archetype_ids=(ARCHETYPE,),
        )
        self.assertIsInstance(result, FollowupPassPlan)
        self.assertEqual(
            result.research_pass.pass_name,
            "COUNTER_SUPERSESSION_CLOSURE",
        )
        self.assertEqual(result.research_pass.conversation_id, self.scope.conversation_id)

    def test_prompt_response_parent_lineage_persisted(self) -> None:
        plan = self._public_plan()
        persisted = self.orchestrator.ledger.get_pass(plan.research_pass.pass_id)
        self.assertEqual(persisted.prompt_hash, plan.prompt_hash)
        self.assertEqual(persisted.parent_pass_id, self.scope.initial_pass_id)
        initial = self.orchestrator.ledger.get_pass(self.scope.initial_pass_id)
        self.assertEqual(initial.response_hash, "c" * 64)

    def test_followup_pass_plan_is_idempotent(self) -> None:
        first = self._public_plan()
        second = self._public_plan()
        self.assertEqual(first.research_pass.pass_id, second.research_pass.pass_id)
        self.assertEqual(len(self.orchestrator.ledger.list_passes(self.job.job_id)), 2)

    def test_submitted_pass_recovery_keeps_durable_prompt_after_template_change(
        self,
    ) -> None:
        first = self._public_plan()
        pass_id = first.research_pass.pass_id
        self.orchestrator.ledger.mark_prepared(pass_id)
        self.orchestrator.ledger.claim_submit(pass_id)
        self.orchestrator.ledger.mark_running(pass_id)
        self.orchestrator.ledger.complete_pass(pass_id, response_hash="d" * 64)
        original_compile = self.orchestrator.compiler.compile

        def changed_compile(**kwargs):
            compiled = original_compile(**kwargs)
            changed_text = compiled.prompt_text + "\n계약 템플릿 새 버전\n"
            return replace(
                compiled,
                prompt_text=changed_text,
                prompt_hash=canonical_hash({"prompt": changed_text}),
            )

        with patch.object(
            self.orchestrator.compiler,
            "compile",
            side_effect=changed_compile,
        ):
            recovered = self._public_plan()

        self.assertEqual(recovered.research_pass.pass_id, pass_id)
        self.assertEqual(recovered.prompt_hash, first.prompt_hash)
        self.assertEqual(recovered.prompt_text, "")
        self.assertEqual(recovered.research_pass.submit_count, 1)

    async def test_followup_submit_is_exactly_once_per_pass(self) -> None:
        plan = self._public_plan()
        adapter = _FakeSameConversationAdapter(self.scope.conversation_id)
        await self.orchestrator.prepare_followup(plan, adapter)
        await self.orchestrator.submit_followup(plan, adapter)
        with self.assertRaises(FollowupSubmitBlocked):
            await self.orchestrator.submit_followup(plan, adapter)
        self.assertEqual(adapter.submit_count, 1)

    async def test_optimistic_followup_without_server_turn_stays_pending(self) -> None:
        plan = self._public_plan()
        adapter = _FakeSameConversationAdapter(
            self.scope.conversation_id,
            persistence_results=(False, False),
        )
        await self.orchestrator.prepare_followup(plan, adapter)

        with self.assertRaisesRegex(FollowupSubmitBlocked, "fresh public"):
            await self.orchestrator.submit_followup(plan, adapter)

        pending = self.orchestrator.ledger.get_pass(plan.research_pass.pass_id)
        self.assertEqual(pending.status, ResearchPassStatus.TRANSPORT_PENDING.value)
        self.assertEqual(pending.submit_count, 1)
        self.assertEqual(
            pending.detail["server_persistence_absence_confirmation_count"],
            1,
        )
        self.assertEqual(adapter.submit_count, 1)
        with self.assertRaises(FollowupSubmitBlocked):
            await self.orchestrator.submit_followup(plan, adapter)
        self.assertEqual(adapter.submit_count, 1)

    async def test_two_fresh_absences_seal_without_resubmitting_same_pass(self) -> None:
        plan = self._public_plan()
        adapter = _FakeSameConversationAdapter(
            self.scope.conversation_id,
            persistence_results=(False, False),
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        with self.assertRaises(FollowupSubmitBlocked):
            await self.orchestrator.submit_followup(plan, adapter)

        audited = await self.orchestrator.audit_submitted_followup_persistence(
            plan,
            adapter,
        )

        self.assertTrue(audited.sealed_unpersisted)
        self.assertEqual(audited.research_pass.status, ResearchPassStatus.FAILED_HARD.value)
        self.assertEqual(
            audited.research_pass.detail["failure_domain"],
            "TRANSPORT",
        )
        self.assertEqual(
            audited.research_pass.detail["failure_class"],
            "CHATGPT_SUBMITTED_TURN_NOT_SERVER_PERSISTED",
        )
        self.assertEqual(adapter.submit_count, 1)
        self.assertEqual(adapter.persistence_count, 2)
        with self.assertRaises(FollowupSubmitBlocked):
            await self.orchestrator.audit_submitted_followup_persistence(
                plan,
                adapter,
            )
        self.assertEqual(adapter.submit_count, 1)

    def test_claimed_transport_timeout_is_recovery_only_and_can_complete(self) -> None:
        plan = self._public_plan()
        self.orchestrator.ledger.mark_prepared(plan.research_pass.pass_id)
        claimed = self.orchestrator.ledger.claim_submit(
            plan.research_pass.pass_id
        )
        pending = self.orchestrator.ledger.mark_transport_pending(
            claimed.pass_id,
            reason="TimeoutError after DOM click",
        )

        recovered_plan = self.orchestrator.plan_next_material_pass(
            job_id=self.job.job_id,
            packet=self.packet,
            dossier={"question_family_results": [self.question]},
            primary_archetype_ids=(ARCHETYPE,),
        )
        self.assertIsInstance(recovered_plan, FollowupPassPlan)
        self.assertEqual(recovered_plan.research_pass.pass_id, pending.pass_id)
        self.assertEqual(recovered_plan.prompt_text, "")
        running = self.orchestrator.confirm_transport_pending_result_visible(
            pending.pass_id
        )
        self.assertEqual(running.status, "RESEARCH_RUNNING")
        self.assertEqual(running.submit_count, 1)
        self.assertTrue(
            running.detail["transport_pending_result_recovered"]
        )
        completed = self.orchestrator.complete_followup(
            running.pass_id,
            response_hash="f" * 64,
            conversation_id=self.scope.conversation_id,
        )
        self.assertEqual(completed.status, "COMPLETE")
        self.assertEqual(completed.submit_count, 1)

    async def test_modal_interception_resumes_existing_claim_exactly_once(self) -> None:
        plan = self._public_plan()
        adapter = _FakeSameConversationAdapter(
            self.scope.conversation_id,
            persistence_results=(False, True),
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        claimed = self.orchestrator.ledger.claim_submit(
            plan.research_pass.pass_id
        )
        pending = self.orchestrator.ledger.mark_transport_pending(
            claimed.pass_id,
            reason=INTERCEPTED_CLICK_REASON,
        )

        resumed = await self.orchestrator.resume_intercepted_followup_submit(
            plan,
            adapter,
        )

        self.assertEqual(pending.submit_count, 1)
        self.assertEqual(resumed.research_pass.submit_count, 1)
        self.assertEqual(resumed.research_pass.status, "RESEARCH_RUNNING")
        self.assertEqual(adapter.submit_count, 1)
        with self.assertRaises(FollowupSubmitBlocked):
            await self.orchestrator.resume_intercepted_followup_submit(
                plan,
                adapter,
            )

    async def test_unstable_send_control_resumes_existing_claim_once(self) -> None:
        plan = self._public_plan()
        adapter = _FakeSameConversationAdapter(
            self.scope.conversation_id,
            persistence_results=(False, True),
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        claimed = self.orchestrator.ledger.claim_submit(
            plan.research_pass.pass_id
        )
        self.orchestrator.ledger.mark_transport_pending(
            claimed.pass_id,
            reason=UNSTABLE_SEND_REASON,
        )

        resumed = await self.orchestrator.resume_intercepted_followup_submit(
            plan,
            adapter,
        )

        self.assertEqual(resumed.research_pass.status, "RESEARCH_RUNNING")
        self.assertEqual(resumed.research_pass.submit_count, 1)
        self.assertEqual(adapter.submit_count, 1)
        self.assertTrue(resumed.research_pass.detail["predispatch_submit_recovered"])
        self.assertEqual(
            resumed.research_pass.detail["predispatch_failure_kind"],
            "UNSTABLE_SEND_CONTROL",
        )

    async def test_late_persistence_reconciles_without_second_click(self) -> None:
        plan = self._public_plan()
        adapter = _FakeSameConversationAdapter(
            self.scope.conversation_id,
            persistence_results=(True,),
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        claimed = self.orchestrator.ledger.claim_submit(
            plan.research_pass.pass_id
        )
        self.orchestrator.ledger.mark_transport_pending(
            claimed.pass_id,
            reason=UNSTABLE_SEND_REASON,
        )

        resumed = await self.orchestrator.resume_intercepted_followup_submit(
            plan,
            adapter,
        )

        self.assertEqual(resumed.research_pass.status, "RESEARCH_RUNNING")
        self.assertEqual(resumed.research_pass.submit_count, 1)
        self.assertEqual(adapter.submit_count, 0)
        self.assertTrue(
            resumed.research_pass.detail["server_persistence_confirmed"]
        )

    def test_visible_provider_failure_closes_claimed_pass_without_resubmit(self) -> None:
        plan = self._public_plan()
        pass_id = plan.research_pass.pass_id
        self.orchestrator.ledger.mark_prepared(pass_id)
        self.orchestrator.ledger.claim_submit(pass_id)
        self.orchestrator.ledger.mark_running(pass_id)

        failed = self.orchestrator.ledger.mark_failed_hard(
            pass_id,
            response_hash="9" * 64,
            failure_class="CHATGPT_VISIBLE_THINKING_FAILED",
            reason="latest assistant turn showed 생각 실패",
        )
        repeated = self.orchestrator.ledger.mark_failed_hard(
            pass_id,
            response_hash="9" * 64,
            failure_class="CHATGPT_VISIBLE_THINKING_FAILED",
            reason="same immutable failure",
        )

        self.assertEqual(failed.status, ResearchPassStatus.FAILED_HARD.value)
        self.assertEqual(repeated.response_hash, "9" * 64)
        self.assertEqual(failed.submit_count, 1)
        self.assertFalse(failed.detail["automatic_resubmit_allowed"])
        self.assertFalse(failed.detail["score_valid"])
        with self.assertRaises(FollowupSubmitBlocked):
            self.orchestrator.ledger.claim_submit(pass_id)

    def test_exact_same_turn_late_result_reconciles_failed_pass_without_resubmit(
        self,
    ) -> None:
        plan = self._public_plan()
        pass_id = plan.research_pass.pass_id
        self.orchestrator.ledger.mark_prepared(pass_id)
        self.orchestrator.ledger.claim_submit(pass_id)
        self.orchestrator.ledger.mark_running(pass_id)
        self.orchestrator.ledger.mark_failed_hard(
            pass_id,
            response_hash="9" * 64,
            failure_class="CHATGPT_VISIBLE_THINKING_FAILED",
            reason="ready-state cutoff preceded late hydration",
        )

        completed = self.orchestrator.ledger.complete_failed_hard_late_result(
            pass_id,
            failed_response_hash="9" * 64,
            late_response_hash="8" * 64,
            assistant_turn_id="same-assistant-turn",
            reconciliation_receipt_hash="7" * 64,
        )
        repeated = self.orchestrator.ledger.complete_failed_hard_late_result(
            pass_id,
            failed_response_hash="9" * 64,
            late_response_hash="8" * 64,
            assistant_turn_id="same-assistant-turn",
            reconciliation_receipt_hash="7" * 64,
        )

        self.assertEqual(completed.status, ResearchPassStatus.COMPLETE.value)
        self.assertEqual(completed.submit_count, 1)
        self.assertEqual(completed.response_hash, "8" * 64)
        self.assertEqual(repeated.response_hash, "8" * 64)
        self.assertEqual(
            completed.detail["provisional_provider_failure_response_hash"],
            "9" * 64,
        )
        self.assertEqual(
            completed.detail["failure_disposition"],
            "SUPERSEDED_BY_EXACT_SAME_TURN_LATE_HYDRATION",
        )
        self.assertFalse(completed.detail["automatic_resubmit_allowed"])
        self.assertFalse(completed.detail["score_valid"])
        with self.assertRaises(FollowupSubmitBlocked):
            self.orchestrator.ledger.complete_failed_hard_late_result(
                pass_id,
                failed_response_hash="9" * 64,
                late_response_hash="6" * 64,
                assistant_turn_id="same-assistant-turn",
                reconciliation_receipt_hash="7" * 64,
            )

    def test_late_result_is_blocked_after_a_successor_pass_exists(self) -> None:
        plan = self._public_plan()
        failed_id = plan.research_pass.pass_id
        self.orchestrator.ledger.mark_prepared(failed_id)
        self.orchestrator.ledger.claim_submit(failed_id)
        self.orchestrator.ledger.mark_running(failed_id)
        self.orchestrator.ledger.mark_failed_hard(
            failed_id,
            response_hash="9" * 64,
            failure_class="CHATGPT_VISIBLE_THINKING_FAILED",
            reason="ready-state cutoff preceded late hydration",
        )
        self.orchestrator.ledger.create_followup_pass(
            scope=self.scope,
            pass_id="PROPASS-successor-after-provider-failure",
            pass_name="PUBLIC_GAP_CLOSURE",
            parent_pass_id=self.scope.initial_pass_id,
            prompt_hash="5" * 64,
            pass_input_hash="4" * 64,
            detail={"supersedes_failed_pass_id": failed_id},
        )

        with self.assertRaisesRegex(
            FollowupSubmitBlocked,
            "after a descendant pass was created",
        ):
            self.orchestrator.ledger.complete_failed_hard_late_result(
                failed_id,
                failed_response_hash="9" * 64,
                late_response_hash="8" * 64,
                assistant_turn_id="same-assistant-turn",
                reconciliation_receipt_hash="7" * 64,
            )

    def test_same_gap_third_reopen_hard_fails(self) -> None:
        values = {
            "job_id": self.job.job_id,
            "stable_gap_key": "C06:Q01:ISSUER_OFFICIAL",
            "fact_snapshot_hash": "1" * 64,
            "accepted_lineage_roster_hash": "2" * 64,
            "attempted_source_roles_hash": "3" * 64,
        }
        self.assertEqual(
            self.orchestrator.ledger.register_gap_reopen(
                **values, supervisor_text="첫 재개방"
            ),
            1,
        )
        self.assertEqual(
            self.orchestrator.ledger.register_gap_reopen(
                **values, supervisor_text="문구만 바꾼 두 번째 재개방"
            ),
            2,
        )
        with self.assertRaises(RepeatedGapReopenHardFail):
            self.orchestrator.ledger.register_gap_reopen(
                **values, supervisor_text="문구만 바꾼 세 번째 재개방"
            )

    def test_third_same_gap_reopen_hard_fails(self) -> None:
        self.test_same_gap_third_reopen_hard_fails()

    def test_transport_limit_does_not_mark_complete(self) -> None:
        bounded = ProMultiPassResearchOrchestrator(
            self.store,
            ledger=self.orchestrator.ledger,
            max_followup_passes=1,
        )
        first = bounded.plan_followup(
            job_id=self.job.job_id,
            packet=self.packet,
            primary_archetype_ids=(ARCHETYPE,),
            pass_name="PUBLIC_GAP_CLOSURE",
            pass_inputs={"round": 1},
        )
        self.assertIsInstance(first, FollowupPassPlan)
        limited = bounded.plan_followup(
            job_id=self.job.job_id,
            packet=self.packet,
            primary_archetype_ids=(ARCHETYPE,),
            pass_name="SATURATION_AUDIT",
            pass_inputs={"round": 2},
        )
        self.assertIsInstance(limited, TransportPendingDecision)
        self.assertEqual(limited.research_status, "TRANSPORT_PENDING")
        self.assertFalse(limited.score_valid)
        self.assertTrue(limited.publication_withheld)

    def test_transport_limit_is_pending_not_complete(self) -> None:
        self.test_transport_limit_does_not_mark_complete()

    def test_explicitly_raised_limit_appends_pass_after_cap_pending(self) -> None:
        bounded = ProMultiPassResearchOrchestrator(
            self.store,
            ledger=self.orchestrator.ledger,
            max_followup_passes=1,
        )
        first = bounded.plan_followup(
            job_id=self.job.job_id,
            packet=self.packet,
            primary_archetype_ids=(ARCHETYPE,),
            pass_name="PUBLIC_GAP_CLOSURE",
            pass_inputs={"round": 1},
        )
        self.assertIsInstance(first, FollowupPassPlan)
        pending = bounded.plan_followup(
            job_id=self.job.job_id,
            packet=self.packet,
            primary_archetype_ids=(ARCHETYPE,),
            pass_name="VERIFIER_REPAIR",
            pass_inputs={"round": 2},
        )
        self.assertIsInstance(pending, TransportPendingDecision)
        cap_receipt = self.orchestrator.ledger.list_passes(self.job.job_id)[-1]
        self.assertEqual(cap_receipt.status, "TRANSPORT_PENDING")
        self.assertEqual(cap_receipt.submit_count, 0)

        expanded = ProMultiPassResearchOrchestrator(
            self.store,
            ledger=self.orchestrator.ledger,
            max_followup_passes=2,
        )
        resumed = expanded.plan_followup(
            job_id=self.job.job_id,
            packet=self.packet,
            primary_archetype_ids=(ARCHETYPE,),
            pass_name="VERIFIER_REPAIR",
            pass_inputs={"round": 2},
        )
        resumed_again = expanded.plan_followup(
            job_id=self.job.job_id,
            packet=self.packet,
            primary_archetype_ids=(ARCHETYPE,),
            pass_name="VERIFIER_REPAIR",
            pass_inputs={"round": 2},
        )

        self.assertIsInstance(resumed, FollowupPassPlan)
        self.assertIsInstance(resumed_again, FollowupPassPlan)
        self.assertNotEqual(resumed.research_pass.pass_id, cap_receipt.pass_id)
        self.assertEqual(
            resumed.research_pass.detail[
                "resumed_from_transport_pending_pass_id"
            ],
            cap_receipt.pass_id,
        )
        self.assertEqual(
            resumed_again.research_pass.pass_id,
            resumed.research_pass.pass_id,
        )
        cap_after = self.orchestrator.ledger.get_pass(cap_receipt.pass_id)
        self.assertEqual(cap_after.status, "TRANSPORT_PENDING")
        self.assertEqual(cap_after.submit_count, 0)

    def test_raised_limit_does_not_retry_real_transport_failure(self) -> None:
        bounded = ProMultiPassResearchOrchestrator(
            self.store,
            ledger=self.orchestrator.ledger,
            max_followup_passes=1,
        )
        planned = bounded.plan_followup(
            job_id=self.job.job_id,
            packet=self.packet,
            primary_archetype_ids=(ARCHETYPE,),
            pass_name="VERIFIER_REPAIR",
            pass_inputs={"batch": "too-large"},
        )
        self.assertIsInstance(planned, FollowupPassPlan)
        failed = bounded.ledger.mark_transport_pending(
            planned.research_pass.pass_id,
            reason="visible composer payload exceeded the transport budget",
        )
        expanded = ProMultiPassResearchOrchestrator(
            self.store,
            ledger=self.orchestrator.ledger,
            max_followup_passes=8,
        )

        still_pending = expanded.plan_followup(
            job_id=self.job.job_id,
            packet=self.packet,
            primary_archetype_ids=(ARCHETYPE,),
            pass_name="VERIFIER_REPAIR",
            pass_inputs={"batch": "too-large"},
        )

        self.assertIsInstance(still_pending, TransportPendingDecision)
        self.assertEqual(
            self.orchestrator.ledger.get_pass(failed.pass_id).status,
            "TRANSPORT_PENDING",
        )

    def test_unsubmitted_transport_pending_plan_does_not_consume_followup_budget(self) -> None:
        bounded = ProMultiPassResearchOrchestrator(
            self.store,
            ledger=self.orchestrator.ledger,
            max_followup_passes=1,
        )
        oversized = bounded.plan_followup(
            job_id=self.job.job_id,
            packet=self.packet,
            primary_archetype_ids=(ARCHETYPE,),
            pass_name="VERIFIER_REPAIR",
            pass_inputs={"batch": "oversized"},
        )
        self.assertIsInstance(oversized, FollowupPassPlan)
        pending = bounded.ledger.mark_transport_pending(
            oversized.research_pass.pass_id,
            reason="visible composer payload exceeded the transport budget",
        )
        self.assertEqual(pending.submit_count, 0)
        replacement = bounded.plan_followup(
            job_id=self.job.job_id,
            packet=self.packet,
            primary_archetype_ids=(ARCHETYPE,),
            pass_name="VERIFIER_REPAIR",
            pass_inputs={"batch": 1},
        )
        self.assertIsInstance(replacement, FollowupPassPlan)


if __name__ == "__main__":
    unittest.main()
