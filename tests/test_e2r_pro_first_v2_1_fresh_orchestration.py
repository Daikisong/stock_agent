from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest

from e2r.pro_first.approval import ProApprovalService
from e2r.pro_first.browser.protocol import (
    BrowserInspection,
    BrowserResultSnapshot,
    BrowserUIState,
    PreparedBrowserJob,
    PreparedFollowupPass,
)
from e2r.pro_first.config import load_pro_first_local_config
from e2r.pro_first.capture.receipt import CaptureReceipt, file_sha256
from e2r.pro_first.fresh_session import (
    FreshV3InitialLiveCanaryRunner,
    FreshSessionBoundaryError,
    FreshSessionBoundaryService,
    FreshSessionOrchestratorV3,
    FreshSessionRerunRequired,
    OldAnswerLeakageManifest,
    audit_fresh_blind_payload,
)
from e2r.pro_first.fresh_session.live_canary_v3 import (
    _requires_browser_result_recovery,
    build_old_answer_leakage_manifest,
)
from e2r.pro_first.canary.live_v2 import _research_semantic_hash
from e2r.pro_first.fresh_session.full_thesis_live_v3 import (
    _context_already_attempted,
    _counter_followup_question_ids,
    _followup_context,
    _question_ids_without_completed_context,
    _question_route_progress_state,
    _repairable_classifications,
    _submitted_unsnapshotted_fresh_nonrepair_plan,
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

    def test_terminal_hard_break_materiality_does_not_reopen_counter_search(
        self,
    ) -> None:
        terminal_hard_break = SimpleNamespace(
            question_family_id="Q-TERMINAL-HARD-BREAK",
            materiality="HARD_BREAK",
            status="SUPPORTED_NON_SCORING",
            terminal=True,
        )
        unresolved_counter = SimpleNamespace(
            question_family_id="Q-UNRESOLVED-COUNTER",
            materiality="HARD_BREAK",
            status="CONTRADICTED_UNRESOLVED",
            terminal=False,
        )
        saturation = SimpleNamespace(
            lifecycle_hard_break_pending_ids=("Q-LIFECYCLE-PENDING",),
            question_decisions=(terminal_hard_break, unresolved_counter),
        )

        self.assertEqual(
            _counter_followup_question_ids(saturation),
            ("Q-LIFECYCLE-PENDING", "Q-UNRESOLVED-COUNTER"),
        )

    def test_independent_cross_archetype_boundary_uses_exact_target_without_fake_old_job(
        self,
    ) -> None:
        service = FreshSessionBoundaryService(self.store)
        boundary, job = service.start_independent(
            symbol="011170",
            company_name="롯데케미칼",
            as_of_date="2026-08-23",
            fresh_session_id="FRESH-SESSION-C17-INDEPENDENT",
            reference_runtime_root=self.root / "ledger-runtime",
            fresh_runtime_root=self.root / "fresh-runtime-c17",
            archetype_ids=("C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",),
        )
        self.assertFalse(boundary.predecessor_required)
        self.assertEqual(job.symbol, "011170")
        self.assertEqual(job.company_name, "롯데케미칼")
        self.assertEqual(job.as_of_date, "2026-08-23")
        self.assertEqual(
            job.archetype_ids,
            ("C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",),
        )
        self.assertNotIn(
            boundary.old_job_id,
            {row.job_id for row in self.store.list_jobs(limit=100)},
        )

        built = FreshSessionOrchestratorV3(self.store, boundary).build_initial_packet(
            commit_sha="c" * 40,
            config_hash="d" * 64,
        )
        self.assertEqual(built.packet_payload["target"]["symbol"], "011170")
        self.assertEqual(
            built.packet_payload["candidate_archetypes"],
            ["C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"],
        )
        self.assertTrue(built.packet_leakage_audit.passed)

        loaded, loaded_job = service.load_existing(
            fresh_runtime_root=boundary.fresh_runtime_root,
            leakage_manifest=boundary.leakage_manifest,
        )
        self.assertFalse(loaded.predecessor_required)
        self.assertEqual(loaded_job.job_id, job.job_id)

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

    async def test_submitted_recovery_reuses_packet_without_second_submit(self) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-recovery")
        submitted = await self.orchestrator.submit_initial_once(adapter)

        recovered = self.orchestrator.build_initial_packet(
            commit_sha="a" * 40,
            config_hash="b" * 64,
        )

        self.assertEqual(
            recovered.packet_bundle.packet_hash,
            self.built.packet_bundle.packet_hash,
        )
        self.assertEqual(recovered.initial_pass_id, self.built.initial_pass_id)
        self.assertEqual(submitted.submit_result.job.submit_count, 1)
        self.assertEqual(self.store.get_job(self.fresh_job.job_id).submit_count, 1)
        self.assertEqual(adapter.submit_count, 1)

    async def test_submitted_recovery_loads_receipt_without_prompt_recompile(self) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-receipt-load")
        submitted = await self.orchestrator.submit_initial_once(adapter)

        class _CompilerMustNotRun:
            def compile(self, **_kwargs):
                raise AssertionError("submitted recovery must not recompile prompt")

        self.orchestrator.initial_compiler = _CompilerMustNotRun()
        recovered = self.orchestrator.load_initial_packet_for_submitted_recovery(
            commit_sha="a" * 40,
            config_hash="b" * 64,
        )

        self.assertEqual(recovered.prompt.prompt_hash, self.built.prompt.prompt_hash)
        self.assertEqual(
            len(recovered.prompt.prompt_text),
            len(self.built.prompt.prompt_text),
        )
        self.assertEqual(
            recovered.prompt.mandatory_question_ids,
            self.built.prompt.mandatory_question_ids,
        )
        self.assertEqual(submitted.submit_result.job.submit_count, 1)
        self.assertEqual(adapter.submit_count, 1)

    def test_post_capture_verifier_attention_does_not_reopen_browser(self) -> None:
        pre_capture = replace(
            self.fresh_job,
            status=JobStatus.USER_ATTENTION_REQUIRED.value,
            capture_count=0,
        )
        post_capture = replace(pre_capture, capture_count=1)

        self.assertTrue(_requires_browser_result_recovery(pre_capture))
        self.assertFalse(_requires_browser_result_recovery(post_capture))

    def test_successor_can_use_predecessor_artifacts_and_central_ledger_separately(self) -> None:
        central_database = self.root / "central-ledger" / "pro_first.sqlite3"
        runner = FreshV3InitialLiveCanaryRunner(
            replace(
                load_pro_first_local_config(
                    Path(__file__).parents[1]
                    / "configs/e2r_pro_first_local.example.yaml"
                ),
                runtime_root=self.root / "successor-runtime",
            ),
            old_runtime_root=self.boundary.fresh_runtime_root,
            fresh_runtime_root=self.root / "successor-runtime",
            repo_root=self.root,
            state_database_path=central_database,
            source_verifier=object(),
            report_structurer=object(),
        )

        self.assertEqual(runner.old_runtime_root, self.boundary.fresh_runtime_root)
        self.assertEqual(runner.state_database_path, central_database.resolve())
        self.assertEqual(runner.store.database_path.resolve(), central_database.resolve())

    def test_schema_failed_predecessor_uses_only_hash_verified_capture_for_denylist(
        self,
    ) -> None:
        job_root = self.root / "schema-failed-predecessor"
        incoming = job_root / "capture/incoming"
        incoming.mkdir(parents=True)
        dossier = {
            "research_pass_id": OLD_PASS,
            "material_facts": [
                {
                    "dossier_fact_id": OLD_FACT,
                    "source_url": EXPECTED_URL,
                    "supporting_excerpt": "OLD EXCERPT\nLINE",
                }
            ],
            "counterfacts": [],
            "resolution_facts": [],
            "source_documents": [
                {"canonical_url": EXPECTED_URL, "opened_url": EXPECTED_URL}
            ],
            "search_route_receipts": [
                {
                    "route_receipt_id": OLD_ROUTE,
                    "opened_source_urls": [EXPECTED_URL],
                }
            ],
            "source_lineages": [],
            "question_family_results": [
                {"closure_reason": "OLD TERMINAL ANSWER"}
            ],
        }
        report_path = incoming / "pro_report.md"
        dossier_path = incoming / "research_dossier.json"
        report_path.write_text("schema-failed captured report", encoding="utf-8")
        captured_dossier_text = json.dumps(
            dossier, ensure_ascii=False, sort_keys=True
        ).replace(r"OLD EXCERPT\nLINE", "OLD EXCERPT\nLINE")
        dossier_path.write_text(captured_dossier_text, encoding="utf-8")
        receipt = CaptureReceipt(
            schema_version="e2r_pro_capture_receipt_v1",
            event_type="PRO_RESEARCH_CAPTURE_COMPLETE",
            job_id=self.old_job.job_id,
            run_id=OLD_RUN,
            target_id=self.old_job.symbol,
            as_of_date=self.old_job.as_of_date,
            packet_hash="a" * 64,
            prompt_hash="b" * 64,
            conversation_id=OLD_CONVERSATION,
            assistant_turn_id="assistant-turn-schema-failed",
            report_md_hash=file_sha256(report_path),
            report_pdf_hash=None,
            dossier_json_hash=file_sha256(dossier_path),
            submit_count=1,
            capture_count=1,
            captured_at="2026-08-25T01:02:03Z",
            capture_mode="CHATGPT_WEB_VISIBLE_CHAT_PRO_FRESH_V3",
            capture_source="DIRECT_REPORT_DOM_NORMALIZED",
            optional_pdf_error=None,
        )
        receipt_path = incoming / "browser_capture_receipt.json"
        receipt_path.write_text(
            json.dumps(receipt.to_dict(), ensure_ascii=False, sort_keys=True),
            encoding="utf-8",
        )
        (incoming / "READY.json").write_text(
            json.dumps(
                {
                    "schema_version": "e2r_pro_capture_ready_v1",
                    "capture_receipt_hash": receipt.receipt_hash,
                    "capture_receipt_path": (
                        "capture/incoming/browser_capture_receipt.json"
                    ),
                    "job_id": self.old_job.job_id,
                    "run_id": OLD_RUN,
                    "written_last": True,
                },
                ensure_ascii=False,
                sort_keys=True,
            ),
            encoding="utf-8",
        )

        manifest = build_old_answer_leakage_manifest(
            self.store,
            old_job_id=self.old_job.job_id,
            old_run_id=OLD_RUN,
            old_conversation_id=OLD_CONVERSATION,
            old_job_root=job_root,
        )

        self.assertEqual(manifest.old_fact_ids, (OLD_FACT,))
        self.assertEqual(manifest.old_route_receipt_ids, (OLD_ROUTE,))
        self.assertEqual(manifest.old_research_pass_ids, (OLD_PASS,))
        self.assertEqual(manifest.old_question_answers, ("OLD TERMINAL ANSWER",))
        self.assertEqual(manifest.expected_source_urls, (EXPECTED_URL,))

        dossier_path.write_text("{}", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "capture artifact hash mismatch"):
            build_old_answer_leakage_manifest(
                self.store,
                old_job_id=self.old_job.job_id,
                old_run_id=OLD_RUN,
                old_conversation_id=OLD_CONVERSATION,
                old_job_root=job_root,
            )

    async def test_completed_markers_rebind_transient_conversation_without_submit(self) -> None:
        adapter = await self._prepare_and_approve("WEB:temporary-conversation")
        await self.orchestrator.submit_initial_once(adapter)
        runner = FreshV3InitialLiveCanaryRunner(
            replace(
                load_pro_first_local_config(
                    Path(__file__).parents[1]
                    / "configs/e2r_pro_first_local.example.yaml"
                ),
                runtime_root=self.boundary.fresh_runtime_root,
            ),
            old_runtime_root=self.boundary.old_runtime_root,
            fresh_runtime_root=self.boundary.fresh_runtime_root,
            repo_root=self.root,
            store=self.store,
            source_verifier=object(),
        )
        result = BrowserResultSnapshot(
            conversation_id="canonical-conversation-0001",
            assistant_turn_id="assistant-turn-1",
            report_text="complete dossier",
            report_hash="d" * 64,
            has_citations=True,
            has_dossier_marker=True,
            job_marker_matches=True,
            run_marker_matches=True,
            new_attachment_keys=(),
        )

        runner._rebind_completed_conversation(
            job_id=self.fresh_job.job_id,
            run_id=str(self.built.packet_payload["run_id"]),
            result=result,
        )

        rebound = self.store.get_job(self.fresh_job.job_id)
        self.assertEqual(rebound.conversation_id, "canonical-conversation-0001")
        self.assertEqual(rebound.submit_count, 1)
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
        rebuilt = self.orchestrator.build_initial_packet(
            commit_sha="a" * 40,
            config_hash="b" * 64,
        )
        self.assertEqual(rebuilt.packet_bundle.packet_hash, self.built.packet_bundle.packet_hash)
        self.assertEqual(rebuilt.prompt.prompt_hash, self.built.prompt.prompt_hash)
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

    async def test_distinct_gap_and_reaudit_passes_remain_in_same_conversation(self) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-multipass")
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="7" * 64,
        )
        planned_names = (
            "PUBLIC_GAP_CLOSURE",
            "COUNTER_SUPERSESSION_CLOSURE",
            "SATURATION_AUDIT",
            "PUBLIC_GAP_CLOSURE",
            "SATURATION_AUDIT",
        )
        pass_ids = []
        for ordinal, pass_name in enumerate(planned_names, start=1):
            plan, _compiled = self.orchestrator.plan_v3_followup(
                self.built,
                pass_name=pass_name,
                latest_dossier_digest={
                    "dossier_hash": f"{ordinal:064x}",
                    "mandatory_question_nonterminal_count": max(0, 5 - ordinal),
                },
                unresolved_question_state=(
                    {
                        "question_family_id": (
                            self.built.prompt.mandatory_question_ids[0]
                        ),
                        "deterministic_status": "PUBLIC_SEARCHABLE",
                    },
                ),
                pass_inputs={"iteration": ordinal},
            )
            await self.orchestrator.prepare_followup(plan, adapter)
            await self.orchestrator.submit_followup(plan, adapter)
            self.orchestrator.complete_followup(
                plan.research_pass.pass_id,
                response_hash=f"{ordinal + 10:064x}",
                conversation_id="fresh-conversation-multipass",
            )
            pass_ids.append(plan.research_pass.pass_id)

        self.assertEqual(len(pass_ids), len(set(pass_ids)))
        passes = self.orchestrator.ledger.list_passes(self.fresh_job.job_id)
        self.assertEqual(
            [row.pass_name for row in passes[1:]],
            list(planned_names),
        )
        self.assertTrue(
            all(
                row.conversation_id == "fresh-conversation-multipass"
                for row in passes
            )
        )

    async def test_full_thesis_tail_uses_delta_prompt_and_gap_identity_dedup(self) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-gap-dedup")
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="8" * 64,
        )
        gap_hash = "9" * 64
        plan, compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="PUBLIC_GAP_CLOSURE",
            latest_dossier_digest={
                "dossier_hash": "a" * 64,
                "fact_snapshot_hash": "b" * 64,
            },
            unresolved_question_state=(
                {
                    "question_family_id": self.built.prompt.mandatory_question_ids[0],
                    "deterministic_status": "PUBLIC_SEARCHABLE",
                },
            ),
            pass_inputs={"research_gap_context_hash": gap_hash},
        )
        self.assertIn("ResearchDossierV3 **delta JSON**", compiled.prompt_text)
        self.assertIn("이전 전체 dossier를", compiled.prompt_text)
        self.assertEqual(
            plan.research_pass.detail["research_gap_context_hash"],
            gap_hash,
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        await self.orchestrator.submit_followup(plan, adapter)
        self.assertFalse(
            _context_already_attempted(
                self.orchestrator.ledger,
                job_id=self.fresh_job.job_id,
                pass_name="PUBLIC_GAP_CLOSURE",
                research_gap_context_hash=gap_hash,
            )
        )
        self.orchestrator.complete_followup(
            plan.research_pass.pass_id,
            response_hash="c" * 64,
            conversation_id="fresh-conversation-gap-dedup",
        )
        self.assertTrue(
            _context_already_attempted(
                self.orchestrator.ledger,
                job_id=self.fresh_job.job_id,
                pass_name="PUBLIC_GAP_CLOSURE",
                research_gap_context_hash=gap_hash,
            )
        )
        self.assertFalse(
            _context_already_attempted(
                self.orchestrator.ledger,
                job_id=self.fresh_job.job_id,
                pass_name="PUBLIC_GAP_CLOSURE",
                research_gap_context_hash="d" * 64,
            )
        )

    async def test_unchanged_question_is_not_resent_after_sibling_closes(self) -> None:
        adapter = await self._prepare_and_approve(
            "fresh-conversation-question-dedup"
        )
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="e" * 64,
        )
        question_a, question_b = self.built.prompt.mandatory_question_ids[:2]
        decisions = (
            self._question_decision(question_a, linked_fact_id="FACT-A"),
            self._question_decision(question_b, linked_fact_id="FACT-B"),
        )
        saturation = self._tail_saturation(decisions, fact_hash="1" * 64)
        dossier = self._tail_dossier(question_a, question_b)
        first_context = _followup_context(
            dossier=dossier,
            saturation=saturation,
            accepted_fact_ids=("FACT-A", "FACT-B"),
            question_ids=(question_a, question_b),
            pass_name="PUBLIC_GAP_CLOSURE",
        )
        plan, _compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="PUBLIC_GAP_CLOSURE",
            latest_dossier_digest=first_context["latest_dossier_digest"],
            unresolved_question_state=first_context[
                "unresolved_question_state"
            ],
            pass_inputs=first_context["pass_inputs"],
        )
        self.assertEqual(
            plan.research_pass.detail["question_context_hashes"],
            first_context["pass_inputs"]["question_context_hashes"],
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        await self.orchestrator.submit_followup(plan, adapter)
        self.orchestrator.complete_followup(
            plan.research_pass.pass_id,
            response_hash="f" * 64,
            conversation_id=(
                self.orchestrator.ledger.get_pass(
                    plan.research_pass.pass_id
                ).conversation_id
                or ""
            ),
        )

        # A closed elsewhere and the global fact snapshot changed.  B itself
        # is identical, so B must not be submitted again.
        unchanged_b = _followup_context(
            dossier={
                **dossier,
                "material_facts": [
                    *dossier["material_facts"],
                    {"dossier_fact_id": "FACT-UNRELATED"},
                ],
            },
            saturation=self._tail_saturation(
                (decisions[1],),
                fact_hash="2" * 64,
            ),
            accepted_fact_ids=("FACT-A", "FACT-B", "FACT-UNRELATED"),
            question_ids=(question_b,),
            pass_name="PUBLIC_GAP_CLOSURE",
        )
        self.assertEqual(
            _question_ids_without_completed_context(
                self.orchestrator.ledger,
                job_id=self.fresh_job.job_id,
                pass_name="PUBLIC_GAP_CLOSURE",
                context=unchanged_b,
            ),
            (),
        )

        changed_b_decision = self._question_decision(
            question_b,
            linked_fact_id="FACT-B-NEW",
        )
        changed_b = _followup_context(
            dossier=dossier,
            saturation=self._tail_saturation(
                (changed_b_decision,),
                fact_hash="3" * 64,
            ),
            accepted_fact_ids=("FACT-A", "FACT-B-NEW"),
            question_ids=(question_b,),
            pass_name="PUBLIC_GAP_CLOSURE",
        )
        self.assertEqual(
            _question_ids_without_completed_context(
                self.orchestrator.ledger,
                job_id=self.fresh_job.job_id,
                pass_name="PUBLIC_GAP_CLOSURE",
                context=changed_b,
            ),
            (question_b,),
        )

    async def test_same_route_with_new_receipt_id_is_not_research_progress(
        self,
    ) -> None:
        adapter = await self._prepare_and_approve(
            "fresh-conversation-route-semantic-dedup"
        )
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="9" * 64,
        )
        question_id = self.built.prompt.mandatory_question_ids[0]

        def dossier_for(
            receipt_id: str,
            *,
            pass_id: str,
            url: str,
            provider_status: str = "PARSER_PENDING",
            source_role_id: str = "ISSUER_OFFICIAL",
            objective: str = "same audited objective",
            query_text: str = "same audited query",
        ) -> dict[str, object]:
            dossier = self._tail_dossier(question_id)
            dossier["question_family_results"][0][
                "search_route_receipt_ids"
            ] = [receipt_id]
            dossier["search_route_receipts"] = [
                {
                    "route_receipt_id": receipt_id,
                    "pass_id": pass_id,
                    "source_role_id": source_role_id,
                    "query_or_navigation_objective": objective,
                    "query_text": query_text,
                    "opened_source_urls": [url],
                    "provider_status": provider_status,
                    "parser_status": "SUCCESS",
                    "accepted_fact_ids": [],
                    "no_new_route_reason": "same audited no-new-route result",
                }
            ]
            return dossier

        first_decision = self._question_decision(
            question_id,
            linked_fact_id="FACT-1",
            route_receipt_id="ROUTE-P1",
            provider_parser_normal=False,
        )
        first_context = _followup_context(
            dossier=dossier_for(
                "ROUTE-P1",
                pass_id="PROPASS-P1",
                url="https://issuer.example.com/same",
            ),
            saturation=self._tail_saturation(
                (first_decision,), fact_hash="4" * 64
            ),
            accepted_fact_ids=("FACT-1",),
            question_ids=(question_id,),
            pass_name="PUBLIC_GAP_CLOSURE",
        )
        plan, _compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="PUBLIC_GAP_CLOSURE",
            latest_dossier_digest=first_context["latest_dossier_digest"],
            unresolved_question_state=first_context[
                "unresolved_question_state"
            ],
            pass_inputs=first_context["pass_inputs"],
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        await self.orchestrator.submit_followup(plan, adapter)
        self.orchestrator.complete_followup(
            plan.research_pass.pass_id,
            response_hash="8" * 64,
            conversation_id="fresh-conversation-route-semantic-dedup",
        )

        repeated_decision = self._question_decision(
            question_id,
            linked_fact_id="FACT-1",
            route_receipt_id="ROUTE-P2",
            provider_parser_normal=False,
        )
        repeated_context = _followup_context(
            dossier=dossier_for(
                "ROUTE-P2",
                pass_id="PROPASS-P2",
                url="https://issuer.example.com/same",
                source_role_id="OFFICIAL_FILING",
                objective="rephrased objective for the same opened page",
                query_text="differently worded query for the same opened page",
            ),
            saturation=self._tail_saturation(
                (repeated_decision,), fact_hash="4" * 64
            ),
            accepted_fact_ids=("FACT-1",),
            question_ids=(question_id,),
            pass_name="PUBLIC_GAP_CLOSURE",
        )
        self.assertNotEqual(
            first_context["pass_inputs"]["question_context_hashes"],
            repeated_context["pass_inputs"]["question_context_hashes"],
        )
        self.assertEqual(
            first_context["pass_inputs"]["question_progress_hashes"],
            repeated_context["pass_inputs"]["question_progress_hashes"],
        )
        self.assertEqual(
            _question_ids_without_completed_context(
                self.orchestrator.ledger,
                job_id=self.fresh_job.job_id,
                pass_name="PUBLIC_GAP_CLOSURE",
                context=repeated_context,
            ),
            (),
        )

        different_route_context = _followup_context(
            dossier=dossier_for(
                "ROUTE-P3",
                pass_id="PROPASS-P3",
                url="https://regulator.example.com/genuinely-new",
            ),
            saturation=self._tail_saturation(
                (
                    self._question_decision(
                        question_id,
                        linked_fact_id="FACT-1",
                        route_receipt_id="ROUTE-P3",
                        provider_parser_normal=False,
                    ),
                ),
                fact_hash="4" * 64,
            ),
            accepted_fact_ids=("FACT-1",),
            question_ids=(question_id,),
            pass_name="PUBLIC_GAP_CLOSURE",
        )
        self.assertEqual(
            _question_ids_without_completed_context(
                self.orchestrator.ledger,
                job_id=self.fresh_job.job_id,
                pass_name="PUBLIC_GAP_CLOSURE",
                context=different_route_context,
            ),
            (question_id,),
        )

    async def test_running_legacy_pass_can_bind_progress_hashes_once(self) -> None:
        adapter = await self._prepare_and_approve(
            "fresh-conversation-progress-hash-migration"
        )
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="7" * 64,
        )
        question_id = self.built.prompt.mandatory_question_ids[0]
        plan, _compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="PUBLIC_GAP_CLOSURE",
            latest_dossier_digest={"dossier_hash": "6" * 64},
            unresolved_question_state=(),
            pass_inputs={
                "research_gap_context_hash": "5" * 64,
                "question_family_ids": [question_id],
                "question_context_hashes": {question_id: "4" * 64},
            },
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        await self.orchestrator.submit_followup(plan, adapter)
        bound = self.orchestrator.ledger.record_question_progress_hashes(
            plan.research_pass.pass_id,
            question_progress_hashes={question_id: "3" * 64},
        )
        self.assertEqual(
            bound.detail["question_progress_hashes"],
            {question_id: "3" * 64},
        )
        same = self.orchestrator.ledger.record_question_progress_hashes(
            plan.research_pass.pass_id,
            question_progress_hashes={question_id: "3" * 64},
        )
        self.assertEqual(same.detail, bound.detail)
        with self.assertRaisesRegex(Exception, "already bound differently"):
            self.orchestrator.ledger.record_question_progress_hashes(
                plan.research_pass.pass_id,
                question_progress_hashes={question_id: "2" * 64},
            )

    def test_grouped_route_split_and_relabel_are_not_progress(self) -> None:
        question_state = {
            "search_route_receipt_ids": ["ROUTE-P1"],
            "attempted_source_role_ids": ["REGULATOR_OFFICIAL"],
        }

        def decision(*route_ids: str) -> dict[str, object]:
            return {
                "route_adequacy": {
                    "linked_route_receipt_ids": list(route_ids),
                    "adequate": False,
                    "official_route_attempted": True,
                    "distinct_route_count": len(route_ids),
                    "independent_no_new_route_confirmation_count": 1,
                    "provider_parser_normal": False,
                    "semantic_fixpoint": False,
                    "failure_codes": ["PROVIDER_OR_PARSER_NOT_NORMAL"],
                }
            }

        grouped = {
            "ROUTE-P1": {
                "route_receipt_id": "ROUTE-P1",
                "source_role_id": "REGULATOR_OFFICIAL",
                "query_or_navigation_objective": "감사 원문 두 주소 확인",
                "query_text": None,
                "opened_source_urls": [
                    "https://regulator.example.com/a",
                    "https://regulator.example.com/b",
                ],
                "provider_status": "PARSER_PENDING",
                "parser_status": "PARSER_PENDING",
                "accepted_fact_ids": [],
                "no_new_route_reason": "동일 parser 한계",
            }
        }
        split = {
            **grouped,
            "ROUTE-P2": {
                **grouped["ROUTE-P1"],
                "route_receipt_id": "ROUTE-P2",
                "source_role_id": "OFFICIAL_FILING",
                "query_or_navigation_objective": "rephrased objective A",
                "opened_source_urls": ["https://regulator.example.com/a"],
            },
            "ROUTE-P3": {
                **grouped["ROUTE-P1"],
                "route_receipt_id": "ROUTE-P3",
                "query_or_navigation_objective": "rephrased objective B",
                "opened_source_urls": ["https://regulator.example.com/b"],
            },
        }

        before = _question_route_progress_state(
            decision=decision("ROUTE-P1"),
            question_state=question_state,
            route_by_id=grouped,
            verified_fact_ids=frozenset(),
        )
        after = _question_route_progress_state(
            decision=decision("ROUTE-P1", "ROUTE-P2", "ROUTE-P3"),
            question_state={
                **question_state,
                "search_route_receipt_ids": [
                    "ROUTE-P1",
                    "ROUTE-P2",
                    "ROUTE-P3",
                ],
            },
            route_by_id=split,
            verified_fact_ids=frozenset(),
        )

        self.assertEqual(before, after)

    async def test_submitted_followup_is_recovered_before_changed_routing_context(
        self,
    ) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-recovery")
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="4" * 64,
        )
        plan, _compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="PUBLIC_GAP_CLOSURE",
            latest_dossier_digest={"dossier_hash": "5" * 64},
            unresolved_question_state=(),
            pass_inputs={"research_gap_context_hash": "6" * 64},
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        await self.orchestrator.submit_followup(plan, adapter)
        self.orchestrator.ledger.mark_transport_pending(
            plan.research_pass.pass_id,
            reason="visible result recovery must precede changed routing",
        )

        recovered = _submitted_unsnapshotted_fresh_nonrepair_plan(
            self.orchestrator,
            job_id=self.fresh_job.job_id,
        )

        self.assertIsNotNone(recovered)
        assert recovered is not None
        self.assertEqual(recovered.research_pass.pass_id, plan.research_pass.pass_id)
        self.assertEqual(recovered.research_pass.status, "TRANSPORT_PENDING")
        self.assertEqual(recovered.research_pass.submit_count, 1)
        self.assertEqual(recovered.prompt_text, "")
        self.assertEqual(adapter.submit_count, 2)  # initial one + follow-up one

    def test_full_thesis_tail_routes_only_material_pro_repair_candidates(self) -> None:
        rows = (
            {
                "candidate_id": "FACT-YES",
                "material": True,
                "send_to_pro_allowed": True,
            },
            {
                "candidate_id": "FACT-NONMATERIAL",
                "material": False,
                "send_to_pro_allowed": True,
            },
            {
                "candidate_id": "FACT-LOCAL",
                "material": True,
                "send_to_pro_allowed": False,
            },
        )
        self.assertEqual(
            tuple(row["candidate_id"] for row in _repairable_classifications(rows)),
            ("FACT-YES",),
        )

    def test_route_receipt_only_is_not_semantic_progress(self) -> None:
        before = {
            "material_facts": [],
            "counterfacts": [],
            "resolution_facts": [],
            "question_family_results": [],
            "source_lineages": [],
            "search_route_receipts": [],
        }
        route_only = {
            **before,
            "search_route_receipts": [
                {
                    "route_receipt_id": "ROUTE-NO-FACT-NO-CLOSURE",
                    "provider_status": "SUCCESS",
                }
            ],
        }
        new_lineage = {
            **route_only,
            "source_lineages": [
                {"source_lineage_id": "LINEAGE-MEANINGFUL"}
            ],
        }

        self.assertEqual(
            _research_semantic_hash(before),
            _research_semantic_hash(route_only),
        )
        self.assertNotEqual(
            _research_semantic_hash(before),
            _research_semantic_hash(new_lineage),
        )

    def test_question_receipt_and_closure_rephrase_are_not_progress(self) -> None:
        before = {
            "question_family_results": [
                {
                    "question_family_id": "R13_AUDIT_Q01",
                    "status": "PARSER_PENDING",
                    "availability_class": "PARSER_BLOCKED",
                    "closure_reason": "감사보고서 원문 확인이 남았다.",
                    "search_route_receipt_ids": ["ROUTE-P1"],
                    "support_fact_ids": ["FACT-AUDIT", "FACT-GOVERNANCE"],
                }
            ],
            "unresolved_gaps": [
                {
                    "gap_id": "GAP-AUDIT",
                    "stable_gap_key": "issuer:audit:q01",
                    "question_family_id": "R13_AUDIT_Q01",
                    "status": "PARSER_PENDING",
                    "availability_class": "PARSER_BLOCKED",
                    "closure_note": "감사 원문 parser가 남았다.",
                    "search_route_receipt_ids": ["ROUTE-P1"],
                    "attempted_source_role_ids": [
                        "REGULATOR_OFFICIAL",
                        "AUDITOR_FILING",
                    ],
                }
            ],
        }
        receipt_and_prose_only = {
            "question_family_results": [
                {
                    "question_family_id": "R13_AUDIT_Q01",
                    "status": "PARSER_PENDING",
                    "availability_class": "PARSER_BLOCKED",
                    "closure_reason": "동일한 감사 원문의 parser 문제가 아직 남아 있다.",
                    "search_route_receipt_ids": ["ROUTE-P1", "ROUTE-P2"],
                    "support_fact_ids": ["FACT-GOVERNANCE", "FACT-AUDIT"],
                }
            ],
            "unresolved_gaps": [
                {
                    **before["unresolved_gaps"][0],
                    "closure_note": "동일 parser 한계를 다른 문장으로 표현했다.",
                    "search_route_receipt_ids": ["ROUTE-P1", "ROUTE-P2"],
                    "attempted_source_role_ids": [
                        "AUDITOR_FILING",
                        "REGULATOR_OFFICIAL",
                    ],
                }
            ],
        }
        changed_status = {
            **receipt_and_prose_only,
            "question_family_results": [
                {
                    **receipt_and_prose_only["question_family_results"][0],
                    "status": "ANSWERED",
                    "availability_class": "PUBLIC_CONFIRMED",
                }
            ]
        }

        self.assertEqual(
            _research_semantic_hash(before),
            _research_semantic_hash(receipt_and_prose_only),
        )
        self.assertNotEqual(
            _research_semantic_hash(before),
            _research_semantic_hash(changed_status),
        )

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

    def test_existing_boundary_loads_without_creating_another_job(self) -> None:
        jobs_before = tuple(
            row.job_id for row in self.store.list_jobs(limit=100)
        )
        loaded, job = FreshSessionBoundaryService(self.store).load_existing(
            fresh_runtime_root=self.boundary.fresh_runtime_root,
            leakage_manifest=self.manifest,
        )
        jobs_after = tuple(
            row.job_id for row in self.store.list_jobs(limit=100)
        )

        self.assertEqual(loaded.fresh_job_id, self.boundary.fresh_job_id)
        self.assertEqual(job.job_id, self.fresh_job.job_id)
        self.assertEqual(jobs_after, jobs_before)

    @staticmethod
    def _question_decision(
        question_id: str,
        *,
        linked_fact_id: str,
        route_receipt_id: str | None = None,
        provider_parser_normal: bool = True,
    ) -> SimpleNamespace:
        route_receipt_id = route_receipt_id or f"ROUTE-{question_id}"
        payload = {
            "question_family_id": question_id,
            "deterministic_status": "PUBLIC_SEARCHABLE",
            "gap_class": "CORE_SCORE_BLOCKER",
            "failure_codes": ["QUESTION_NONTERMINAL"],
            "verified_linked_fact_ids": [linked_fact_id],
            "linked_source_lineage_ids": [f"LINEAGE-{linked_fact_id}"],
            "missing_core_source_roles": ["ISSUER_OFFICIAL"],
            "missing_corroboration_source_roles": [],
            "verified_source_roles": ["ISSUER_OFFICIAL"],
            "terminal": False,
            "ready": False,
            "route_adequacy": {
                "linked_route_receipt_ids": [route_receipt_id],
                "adequate": False,
                "official_route_attempted": True,
                "distinct_route_count": 1,
                "independent_no_new_route_confirmation_count": 0,
                "provider_parser_normal": provider_parser_normal,
                "semantic_fixpoint": False,
                "failure_codes": (
                    []
                    if provider_parser_normal
                    else ["PROVIDER_OR_PARSER_NOT_NORMAL"]
                ),
            },
        }
        return SimpleNamespace(
            question_family_id=question_id,
            materiality="HARD_BREAK",
            status="PUBLIC_SEARCHABLE",
            to_dict=lambda: dict(payload),
        )

    @staticmethod
    def _tail_saturation(
        decisions: tuple[SimpleNamespace, ...],
        *,
        fact_hash: str,
    ) -> SimpleNamespace:
        return SimpleNamespace(
            question_decisions=decisions,
            fact_snapshot_hash=fact_hash,
            accepted_lineage_roster_hash="a" * 64,
            deterministic_research_status="SOURCE_PENDING",
        )

    @staticmethod
    def _tail_dossier(*question_ids: str) -> dict[str, object]:
        return {
            "schema_version": "e2r_pro_research_dossier_v3",
            "selected_archetypes": [ARCHETYPE],
            "research_pass_id": "PROPASS-CONTEXT-BASE",
            "research_status": "SOURCE_PENDING",
            "source_documents": [],
            "material_facts": [
                {"dossier_fact_id": f"FACT-{index}"}
                for index, _question_id in enumerate(question_ids, start=1)
            ],
            "counterfacts": [],
            "resolution_facts": [],
            "search_route_receipts": [],
            "question_family_results": [
                {
                    "question_family_id": question_id,
                    "status": "PUBLIC_SEARCHABLE",
                    "availability_class": "PUBLIC_SEARCHABLE",
                    "closure_reason": None,
                    "required_source_roles_missing": ["ISSUER_OFFICIAL"],
                    "search_route_receipt_ids": [f"ROUTE-{question_id}"],
                }
                for question_id in question_ids
            ],
        }

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
