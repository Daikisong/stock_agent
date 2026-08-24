from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
import hashlib
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.pro_first.approval import ProApprovalService
from e2r.pro_first.browser.protocol import (
    BrowserInspection,
    BrowserUIState,
    PreparedBrowserJob,
    PreparedFollowupPass,
)
from e2r.pro_first.fresh_session import (
    FreshSessionBoundaryError,
    FreshSessionBoundaryService,
    FreshSessionOrchestratorV3,
    FreshSessionRerunRequired,
    OldAnswerLeakageManifest,
    audit_fresh_blind_payload,
)
from e2r.pro_first.ids import canonical_hash
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.multi_pass import (
    ProMultiPassResearchOrchestrator,
    TransportPendingDecision,
)


ARCHETYPE = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
OLD_RUN = "PRORUN-a7dacadb7088fc23535bfdde"
OLD_CONVERSATION = "6a8b09c3-bfcc-83ee-b15b-9f76eca52249"
OLD_PASS = "PROPASS-old-diagnostic-pass"
OLD_FACT = "PROFACT-OLD-ANSWER-001"
OLD_ROUTE = "PROROUTE-OLD-ANSWER-001"
EXPECTED_URL = "https://old.example.com/expected-answer"


class _FreshAdapter:
    def __init__(self, *, submitted_conversation_id: str) -> None:
        self.current_conversation_id: str | None = None
        self.submitted_conversation_id = submitted_conversation_id
        self.prepared_initial: PreparedBrowserJob | None = None
        self.prepared_followup: PreparedFollowupPass | None = None
        self.submit_count = 0

    async def ensure_logged_in(self) -> BrowserInspection:
        return self._inspection(BrowserUIState.READY_FOR_INPUT)

    async def prepare_without_submit(self, **kwargs) -> PreparedBrowserJob:
        self.prepared_initial = PreparedBrowserJob(
            browser_session_id=kwargs["browser_session_id"],
            conversation_id=self.current_conversation_id,
            state=BrowserUIState.AWAITING_USER_APPROVAL,
            packet_path=Path(kwargs["packet_path"]),
            packet_hash=kwargs["packet_hash"],
            prompt_hash=kwargs["prompt_hash"],
            uploaded_filename=Path(kwargs["packet_path"]).name,
            prompt_preview=kwargs["prompt"][:500],
            deep_research_ready=True,
            send_ready=True,
            preexisting_attachment_keys=(),
        )
        return self.prepared_initial

    async def prepare_followup_without_submit(self, **kwargs) -> PreparedFollowupPass:
        if kwargs["conversation_id"] != self.current_conversation_id:
            raise RuntimeError("follow-up escaped the fresh conversation")
        self.prepared_followup = PreparedFollowupPass(
            browser_session_id=kwargs["browser_session_id"],
            conversation_id=kwargs["conversation_id"],
            state=BrowserUIState.AWAITING_USER_APPROVAL,
            job_id=kwargs["job_id"],
            pass_id=kwargs["pass_id"],
            parent_pass_id=kwargs["parent_pass_id"],
            prompt_hash=kwargs["prompt_hash"],
            prompt_preview=kwargs["prompt"][:500],
            send_ready=True,
            preexisting_attachment_keys=(),
        )
        return self.prepared_followup

    async def submit_once(self, proof) -> BrowserInspection:
        if not proof.ledger_verified:
            raise PermissionError("durable approval proof required")
        self.submit_count += 1
        if self.prepared_followup is None:
            self.current_conversation_id = self.submitted_conversation_id
        return self._inspection(BrowserUIState.RESEARCH_RUNNING)

    def _inspection(self, state: BrowserUIState) -> BrowserInspection:
        return BrowserInspection(
            state=state,
            conversation_id=self.current_conversation_id,
            editor_ready=True,
            deep_research_ready=True,
            packet_uploaded=self.prepared_initial is not None,
            prompt_ready=state is BrowserUIState.READY_FOR_INPUT,
            send_ready=state is not BrowserUIState.RESEARCH_RUNNING,
            stop_visible=state is BrowserUIState.RESEARCH_RUNNING,
        )


class ProFirstV21FreshOrchestrationTest(unittest.IsolatedAsyncioTestCase):
    now = datetime(2026, 8, 25, 1, 2, 3, tzinfo=timezone.utc)

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        self.store = ProFirstJobStore(
            self.root / "fresh.sqlite3",
            now=lambda: self.now,
        )
        self.old_job = self._old_running_job()
        self.old_job = self.store.freeze_old_diagnostic_job(
            self.old_job.job_id,
            expected_version=self.old_job.state_version,
            actor="test",
            idempotency_key="freeze-old-for-fresh-v3",
        )
        self.manifest = OldAnswerLeakageManifest(
            old_job_id=self.old_job.job_id,
            old_run_id=OLD_RUN,
            old_conversation_id=OLD_CONVERSATION,
            old_fact_ids=(OLD_FACT,),
            old_route_receipt_ids=(OLD_ROUTE,),
            old_research_pass_ids=(OLD_PASS,),
            old_question_answers=("OLD TERMINAL ANSWER",),
            old_score_values=("70.2", "23.202275"),
            old_stage_values=("Stage 2 FINAL",),
            expected_source_urls=(EXPECTED_URL,),
            expected_fact_ids=("PROFACT-EXPECTED-001",),
        )
        self.boundary, self.fresh_job = FreshSessionBoundaryService(
            self.store
        ).start(
            old_job_id=self.old_job.job_id,
            old_run_id=OLD_RUN,
            old_conversation_id=OLD_CONVERSATION,
            fresh_session_id="FRESH-SESSION-000660-ONE",
            old_runtime_root=self.root / "old-runtime",
            fresh_runtime_root=self.root / "fresh-runtime-one",
            archetype_ids=(ARCHETYPE,),
            leakage_manifest=self.manifest,
        )
        self.orchestrator = FreshSessionOrchestratorV3(
            self.store,
            self.boundary,
        )
        self.built = self.orchestrator.build_initial_packet(
            commit_sha="a" * 40,
            config_hash="b" * 64,
            business_snapshot={"mechanism": "memory capacity and customer allocation"},
            structured_financial_snapshot={"period": "2026H1"},
            revision_valuation_snapshot={"snapshot_date": "2026-08-23"},
        )

    def test_new_runtime_job_run_and_pass_are_distinct(self) -> None:
        self.assertNotEqual(
            self.boundary.old_runtime_root,
            self.boundary.fresh_runtime_root,
        )
        self.assertNotEqual(self.fresh_job.job_id, self.old_job.job_id)
        self.assertNotEqual(self.built.packet_payload["run_id"], OLD_RUN)
        self.assertNotEqual(self.built.initial_pass_id, OLD_PASS)
        self.assertEqual(
            self.store.get_job(self.old_job.job_id).superseded_by_fresh_job_id,
            self.fresh_job.job_id,
        )

    def test_fresh_packet_has_no_old_fact_answer_score_or_stage(self) -> None:
        packet = self.built.packet_payload
        serialized = str(packet)
        for token in (
            OLD_FACT,
            OLD_ROUTE,
            OLD_PASS,
            "OLD TERMINAL ANSWER",
            EXPECTED_URL,
            "Stage 2 FINAL",
        ):
            self.assertNotIn(token, serialized)
        self.assertNotIn("known_positive_facts", packet)
        self.assertNotIn("known_counterfacts", packet)
        self.assertNotIn("proposed_score_ranges", packet)
        self.assertIs(packet["score_authority"], False)
        self.assertIs(packet["stage_authority"], False)
        self.assertTrue(self.built.packet_leakage_audit.passed)
        self.assertEqual(
            self.built.packet_payload["fresh_blind_boundary"],
            {
                "old_pro_fact_input_count": 0,
                "old_route_receipt_input_count": 0,
                "old_rejection_input_count": 0,
                "old_question_answer_input_count": 0,
                "old_score_stage_input_count": 0,
                "expected_source_input_count": 0,
                "expected_fact_id_input_count": 0,
            },
        )

    def test_leakage_audit_rejects_exact_old_answer(self) -> None:
        poisoned = dict(self.built.packet_payload)
        poisoned["business_snapshot"] = {
            "old_pro_accepted_facts": [OLD_FACT]
        }
        audit = audit_fresh_blind_payload(poisoned, self.manifest)
        self.assertFalse(audit.passed)
        self.assertGreater(audit.old_pro_fact_input_count, 0)
        self.assertGreater(audit.forbidden_answer_field_count, 0)

    def test_answer_bearing_packet_inputs_are_rejected(self) -> None:
        from e2r.pro_first.packet import PacketBuildInput, ResearchPacketV3Builder

        with self.assertRaisesRegex(ValueError, "answer-bearing prior inputs"):
            ResearchPacketV3Builder().build(
                PacketBuildInput(
                    job_id=self.fresh_job.job_id,
                    symbol=self.fresh_job.symbol,
                    company_name=self.fresh_job.company_name,
                    as_of_date=self.fresh_job.as_of_date,
                    latest_trading_snapshot_date=self.fresh_job.as_of_date,
                    research_mode=self.fresh_job.mode,
                    candidate_archetypes=(ARCHETYPE,),
                    known_positive_facts=({"fact_id": OLD_FACT},),
                )
            )

    def test_old_conversation_followup_remains_blocked(self) -> None:
        decision = ProMultiPassResearchOrchestrator(self.store).plan_followup(
            job_id=self.old_job.job_id,
            packet={
                "target": {"symbol": self.old_job.symbol},
                "as_of_date": self.old_job.as_of_date,
            },
            primary_archetype_ids=(ARCHETYPE,),
            pass_name="PUBLIC_GAP_CLOSURE",
        )
        self.assertIsInstance(decision, TransportPendingDecision)
        self.assertIn("frozen", decision.reason)

    async def test_exactly_once_initial_submit_creates_new_conversation(self) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-one")
        submitted = await self.orchestrator.submit_initial_once(adapter)
        self.assertTrue(submitted.receipt["new_conversation"])
        self.assertEqual(adapter.submit_count, 1)
        self.assertEqual(
            submitted.submit_result.job.conversation_id,
            "fresh-conversation-one",
        )
        with self.assertRaises(Exception):
            await self.orchestrator.submit_initial_once(adapter)
        self.assertEqual(adapter.submit_count, 1)

    async def test_existing_chat_prepare_is_blocked_then_new_chat_retry_works(self) -> None:
        adapter = _FreshAdapter(submitted_conversation_id="fresh-after-retry")
        adapter.current_conversation_id = OLD_CONVERSATION
        with self.assertRaisesRegex(
            FreshSessionBoundaryError,
            "new-chat route",
        ):
            await self.orchestrator.prepare_initial_with_adapter(
                self.built,
                adapter,
                browser_session_id="BROWSER-FRESH-RETRY",
            )
        attention = self.store.get_job(self.fresh_job.job_id)
        self.assertEqual(
            attention.status,
            JobStatus.USER_ATTENTION_REQUIRED.value,
        )
        self.assertEqual(attention.submit_count, 0)
        adapter.current_conversation_id = None
        prepared = await self.orchestrator.prepare_initial_with_adapter(
            self.built,
            adapter,
            browser_session_id="BROWSER-FRESH-RETRY",
        )
        self.assertEqual(
            prepared.job.status,
            JobStatus.AWAITING_USER_APPROVAL.value,
        )

    async def test_initial_approval_allows_only_bounded_same_chat_followups(self) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-scope")
        submitted = await self.orchestrator.submit_initial_once(adapter)
        scope = self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="c" * 64,
        )
        self.assertEqual(
            scope.conversation_id,
            submitted.submit_result.job.conversation_id,
        )
        self.assertIn("PUBLIC_GAP_CLOSURE", scope.allowed_followup_pass_names)
        self.assertIn("VERIFIER_REPAIR", scope.allowed_followup_pass_names)
        self.assertIn("SATURATION_AUDIT", scope.allowed_followup_pass_names)

    async def test_wrong_or_old_conversation_requires_another_fresh_session(self) -> None:
        adapter = await self._prepare_and_approve(OLD_CONVERSATION)
        with self.assertRaisesRegex(
            FreshSessionRerunRequired,
            "start another fresh_session_id",
        ):
            await self.orchestrator.submit_initial_once(adapter)
        self.assertEqual(adapter.submit_count, 1)
        with self.assertRaises(Exception):
            await self.orchestrator.submit_initial_once(adapter)
        failed = self.orchestrator.seal_failed_run_for_new_conversation(
            reason="NEW_CONVERSATION_ID_EQUALS_OLD_CONVERSATION"
        )
        self.assertIsNotNone(failed.old_job_frozen_at)
        successor_manifest = OldAnswerLeakageManifest(
            old_job_id=failed.job_id,
            old_run_id=self.built.packet_payload["run_id"],
            old_conversation_id=OLD_CONVERSATION,
            old_fact_ids=self.manifest.old_fact_ids,
            old_route_receipt_ids=self.manifest.old_route_receipt_ids,
            old_research_pass_ids=(
                *self.manifest.old_research_pass_ids,
                self.built.initial_pass_id,
            ),
            old_question_answers=self.manifest.old_question_answers,
            old_score_values=self.manifest.old_score_values,
            old_stage_values=self.manifest.old_stage_values,
            expected_source_urls=self.manifest.expected_source_urls,
            expected_fact_ids=self.manifest.expected_fact_ids,
        )
        successor_boundary, successor_job = FreshSessionBoundaryService(
            self.store
        ).start(
            old_job_id=failed.job_id,
            old_run_id=self.built.packet_payload["run_id"],
            old_conversation_id=OLD_CONVERSATION,
            fresh_session_id="FRESH-SESSION-000660-TWO",
            old_runtime_root=self.boundary.fresh_runtime_root,
            fresh_runtime_root=self.root / "fresh-runtime-two",
            archetype_ids=(ARCHETYPE,),
            leakage_manifest=successor_manifest,
        )
        successor = FreshSessionOrchestratorV3(
            self.store,
            successor_boundary,
        ).build_initial_packet(
            commit_sha="a" * 40,
            config_hash="b" * 64,
        )
        self.assertNotEqual(successor_job.job_id, failed.job_id)
        self.assertNotEqual(
            successor.packet_payload["run_id"],
            self.built.packet_payload["run_id"],
        )
        self.assertNotEqual(
            successor.initial_pass_id,
            self.built.initial_pass_id,
        )

    async def test_one_compact_repair_then_saturation_in_same_conversation(self) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-tail")
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="d" * 64,
        )
        dossier, classifications, verifications, job_root = self._repair_inputs()
        repair_plan, compiled = self.orchestrator.plan_compact_repair(
            self.built,
            dossier=dossier,
            rejection_classifications=classifications,
            verification_rows=verifications,
            job_root=job_root,
        )
        repeated_plan, repeated_compiled = self.orchestrator.plan_compact_repair(
            self.built,
            dossier=dossier,
            rejection_classifications=classifications,
            verification_rows=verifications,
            job_root=job_root,
        )
        self.assertEqual(
            repeated_plan.research_pass.pass_id,
            repair_plan.research_pass.pass_id,
        )
        self.assertEqual(repeated_compiled.prompt_hash, compiled.prompt_hash)
        self.assertLess(compiled.prompt_char_count, 100_000)
        self.assertNotIn('"material_facts"', compiled.prompt_text)
        await self.orchestrator.prepare_followup(repair_plan, adapter)
        await self.orchestrator.submit_followup(repair_plan, adapter)
        self.orchestrator.complete_followup(
            repair_plan.research_pass.pass_id,
            response_hash="e" * 64,
            conversation_id="fresh-conversation-tail",
        )

        saturation_plan, saturation = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="SATURATION_AUDIT",
            latest_dossier_digest={
                "dossier_hash": "f" * 64,
                "mandatory_question_nonterminal_count": 0,
                "accepted_fact_ids": ["FACT-ACCEPTED", "FACT-REPLACEMENT"],
            },
            pass_inputs={"repair_pass_count": 1},
        )
        self.assertIn("ResearchDossierV3", saturation.prompt_text)
        await self.orchestrator.prepare_followup(saturation_plan, adapter)
        await self.orchestrator.submit_followup(saturation_plan, adapter)
        self.orchestrator.complete_followup(
            saturation_plan.research_pass.pass_id,
            response_hash="1" * 64,
            conversation_id="fresh-conversation-tail",
        )
        passes = self.orchestrator.ledger.list_passes(self.fresh_job.job_id)
        self.assertEqual(
            [row.pass_name for row in passes],
            ["INITIAL_FULL_RESEARCH", "VERIFIER_REPAIR", "SATURATION_AUDIT"],
        )
        self.assertTrue(
            all(row.conversation_id == "fresh-conversation-tail" for row in passes)
        )
        self.assertTrue(all(row.submit_count == 1 for row in passes))

    async def test_second_semantic_repair_requires_new_conversation(self) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-repair-limit")
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="2" * 64,
        )
        dossier, classifications, verifications, job_root = self._repair_inputs()
        plan, _compiled = self.orchestrator.plan_compact_repair(
            self.built,
            dossier=dossier,
            rejection_classifications=classifications,
            verification_rows=verifications,
            job_root=job_root,
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        await self.orchestrator.submit_followup(plan, adapter)
        self.orchestrator.complete_followup(
            plan.research_pass.pass_id,
            response_hash="3" * 64,
            conversation_id="fresh-conversation-repair-limit",
        )
        second = dict(dossier["material_facts"][0])
        second["dossier_fact_id"] = "FACT-SECOND-DEFECT"
        dossier["material_facts"].append(second)
        second_classification = [
            {
                **classifications[0],
                "candidate_id": "FACT-SECOND-DEFECT",
            }
        ]
        second_verification = [
            {
                **verifications[0],
                "dossier_fact_id": "FACT-SECOND-DEFECT",
            }
        ]
        with self.assertRaisesRegex(
            FreshSessionRerunRequired,
            "SECOND_REPAIR_PASS",
        ):
            self.orchestrator.plan_compact_repair(
                self.built,
                dossier=dossier,
                rejection_classifications=second_classification,
                verification_rows=second_verification,
                job_root=job_root,
            )

    def test_nonempty_unrelated_runtime_root_is_rejected(self) -> None:
        occupied = self.root / "occupied-fresh-runtime"
        occupied.mkdir()
        (occupied / "unrelated.txt").write_text("not this run", encoding="utf-8")
        with self.assertRaisesRegex(
            FreshSessionBoundaryError,
            "not empty",
        ):
            FreshSessionBoundaryService(self.store).start(
                old_job_id=self.old_job.job_id,
                old_run_id=OLD_RUN,
                old_conversation_id=OLD_CONVERSATION,
                fresh_session_id="FRESH-SESSION-TWO",
                old_runtime_root=self.root / "old-runtime-two",
                fresh_runtime_root=occupied,
                archetype_ids=(ARCHETYPE,),
                leakage_manifest=self.manifest,
            )

    def test_mismatched_manifest_is_rejected_before_runtime_creation(self) -> None:
        destination = self.root / "manifest-mismatch-runtime"
        mismatched = replace(self.manifest, old_run_id="PRORUN-wrong-old-run")
        with self.assertRaisesRegex(
            FreshSessionBoundaryError,
            "different old run",
        ):
            FreshSessionBoundaryService(self.store).start(
                old_job_id=self.old_job.job_id,
                old_run_id=OLD_RUN,
                old_conversation_id=OLD_CONVERSATION,
                fresh_session_id="FRESH-SESSION-MANIFEST-MISMATCH",
                old_runtime_root=self.root / "old-runtime-mismatch",
                fresh_runtime_root=destination,
                archetype_ids=(ARCHETYPE,),
                leakage_manifest=mismatched,
            )
        self.assertFalse(destination.exists())

    async def _prepare_and_approve(self, conversation_id: str) -> _FreshAdapter:
        adapter = _FreshAdapter(submitted_conversation_id=conversation_id)
        prepared = await self.orchestrator.prepare_initial_with_adapter(
            self.built,
            adapter,
            browser_session_id="BROWSER-FRESH-V3-ONE",
        )
        approval = ProApprovalService(self.store, now=lambda: self.now)
        grant = approval.issue(
            prepared.job.job_id,
            prompt_hash=self.built.prompt.prompt_hash,
        )
        approval.approve(grant)
        return adapter

    def _old_running_job(self):
        candidate = self.store.create_candidate(
            symbol="000660",
            company_name="SK하이닉스",
            as_of_date="2026-08-23",
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="old-diagnostic-trigger",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={"production_candidate": True},
        )
        job = self.store.create_job(candidate.candidate_id, archetype_ids=(ARCHETYPE,))
        job = self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.PACKET_BUILDING,
            actor="test",
            idempotency_key="old-packet-building",
        )
        job = self.store.record_packet(
            job.job_id,
            expected_version=job.state_version,
            packet_id="PROPACKET-OLD-DIAGNOSTIC",
            packet_hash="a" * 64,
            manifest={"packet_hash": "a" * 64},
            actor="test",
            idempotency_key="old-packet-ready",
        )
        job = self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.BROWSER_PREPARING,
            actor="test",
            idempotency_key="old-browser-preparing",
        )
        job = self.store.record_browser_prepared(
            job.job_id,
            expected_version=job.state_version,
            browser_session_id="BROWSER-OLD-DIAGNOSTIC",
            conversation_id=OLD_CONVERSATION,
            adapter_name="OldDiagnosticAdapter",
            packet_hash="a" * 64,
            prompt_hash="b" * 64,
            state={"state": "AWAITING_USER_APPROVAL"},
            actor="test",
            idempotency_key="old-browser-prepared",
        )
        job, nonce = self.store.issue_approval_nonce(
            job.job_id,
            expected_version=job.state_version,
            actor="test",
            idempotency_key="old-approval-issued",
            prompt_hash="b" * 64,
            expires_at="2026-08-26T01:02:03Z",
        )
        job = self.store.consume_approval_nonce(
            job.job_id,
            nonce,
            expected_version=job.state_version,
            actor="user",
            idempotency_key="old-approval-consumed",
            prompt_hash="b" * 64,
        )
        job = self.store.claim_submit(
            job.job_id,
            expected_version=job.state_version,
            actor="test",
            idempotency_key="old-submit",
        )
        return self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.RESEARCH_RUNNING,
            actor="test",
            idempotency_key="old-running",
        )

    def _repair_inputs(self):
        job_root = self.boundary.fresh_job_root
        document = (
            "SK하이닉스 공식 HBM 보고서. HBM capacity 배정과 가격 조건을 "
            "설명하는 충분히 긴 source 본문이다."
        )
        path = job_root / "verification/source_pages/source.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(document, encoding="utf-8")
        document_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        dossier = {
            "schema_version": "e2r_pro_research_dossier_v3",
            "job_id": self.fresh_job.job_id,
            "run_id": self.built.packet_payload["run_id"],
            "target": {
                "target_id": "000660",
                "symbol": "000660",
                "company_name": "SK하이닉스",
            },
            "as_of_date": "2026-08-23",
            "source_documents": [
                {
                    "source_document_id": "SRC-DEFECT",
                    "canonical_url": "https://example.com/hbm",
                }
            ],
            "material_facts": [
                {
                    "dossier_fact_id": "FACT-SEMANTIC-DEFECT",
                    "statement": "HBM 가격이 99% 상승했다.",
                    "source_document_id": "SRC-DEFECT",
                    "question_family_ids": [
                        "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01"
                    ],
                    "supporting_excerpt": "HBM 가격 조건을 설명했다.",
                }
            ],
            "counterfacts": [],
            "resolution_facts": [],
        }
        classifications = [
            {
                "candidate_id": "FACT-SEMANTIC-DEFECT",
                "cause_class": "GENUINE_SEMANTIC_OR_SOURCE_DEFECT",
                "cause_code": "STATEMENT_BROADER_THAN_EXCERPT",
                "verifier_status": "REJECTED_QUOTE_MISMATCH",
                "detail": "statement is broader than literal support",
                "material": True,
                "send_to_pro_allowed": True,
            }
        ]
        verifications = [
            {
                "dossier_fact_id": "FACT-SEMANTIC-DEFECT",
                "status": "REJECTED_QUOTE_MISMATCH",
                "reason": "literal support mismatch",
                "document_path": str(path.relative_to(job_root)),
                "content_hash": document_hash,
            }
        ]
        return dossier, classifications, verifications, job_root


if __name__ == "__main__":
    unittest.main()
