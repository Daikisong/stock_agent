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
    BrowserSubmittedTurnPersistence,
    BrowserUIIncompatible,
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
from e2r.pro_first.canary.live_v2 import LiveCanaryPending, _research_semantic_hash
from e2r.pro_first.fresh_session.full_thesis_live_v3 import (
    FreshV3FullThesisLiveRunner,
    _completed_pass_left_blockers_unchanged,
    _context_already_attempted,
    _counter_followup_question_ids,
    _enforce_recover_submitted_only,
    _followup_context,
    _new_no_new_route_confirmation_candidate,
    _parse_and_validate_compact_repair_transport,
    _public_followup_question_ids,
    _question_ids_without_completed_context,
    _question_ids_without_repairable_candidates,
    _question_ids_with_reopen_budget,
    _question_route_progress_state,
    _reconcile_artifact_reexport_initial_pass_row,
    _repairable_classifications,
    _require_operational_followup_budget,
    _same_question_reopen_limit_reached,
    _ensure_durable_conversation_visible,
    _submitted_unsnapshotted_fresh_plan,
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
INTERCEPTED_CLICK_REASON = (
    "TimeoutError: Locator.click: Timeout 30000ms exceeded; "
    "modal-global-search intercepts pointer events"
)


class _FreshAdapter:
    def __init__(self, *, submitted_conversation_id: str) -> None:
        self.current_conversation_id: str | None = None
        self.submitted_conversation_id = submitted_conversation_id
        self.prepared_initial: PreparedBrowserJob | None = None
        self.prepared_followup: PreparedFollowupPass | None = None
        self.submit_count = 0
        self.persistence_count = 0
        self.persistence_results: tuple[bool, ...] = (True,)

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
            observation_id=f"PROSERVERVIEW-FRESH-{self.persistence_count}",
            observed_at="2026-08-25T01:02:03Z",
            conversation_id=conversation_id,
            job_id=job_id,
            run_id=run_id,
            pass_id=pass_id,
            parent_pass_id=parent_pass_id,
            persistence_confirmed=confirmed,
            user_turn_id=(
                f"fresh-user-{self.persistence_count}" if confirmed else None
            ),
            required_markers=tuple(required),
            missing_markers=(() if confirmed else tuple(required)),
            observed_user_turn_count=(1 if confirmed else 0),
            fresh_page_url=f"https://chatgpt.com/c/{conversation_id}",
            fresh_page_loaded=True,
        )

    async def inspect_state(self) -> BrowserInspection:
        return self._inspection(BrowserUIState.RESEARCH_RUNNING)

    async def open_exact_conversation_without_submit(
        self,
        *,
        conversation_id: str,
    ) -> BrowserInspection:
        self.current_conversation_id = conversation_id
        return self._inspection(BrowserUIState.READY_FOR_INPUT)

    async def prepare_intercepted_followup_submit_recovery(
        self,
        proof,
        *,
        transport_pending_reason: str,
    ) -> None:
        if not proof.ledger_verified or proof.submit_count != 1:
            raise PermissionError("durable claimed proof required")
        if transport_pending_reason != INTERCEPTED_CLICK_REASON:
            raise PermissionError("transport interception evidence changed")

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

    def test_recover_submitted_only_never_allows_new_pass_planning(self) -> None:
        _enforce_recover_submitted_only(enabled=False, recovered=False)
        _enforce_recover_submitted_only(enabled=False, recovered=True)

        with self.assertRaisesRegex(
            Exception,
            "recovery-only mode sent nothing",
        ) as missing:
            _enforce_recover_submitted_only(enabled=True, recovered=False)
        self.assertEqual(
            getattr(missing.exception, "status", None),
            "SUBMITTED_PASS_RECOVERY_REQUIRED",
        )

        with self.assertRaisesRegex(
            Exception,
            "additional pass planning is disabled",
        ) as recovered:
            _enforce_recover_submitted_only(enabled=True, recovered=True)
        self.assertEqual(
            getattr(recovered.exception, "status", None),
            "SUBMITTED_PASS_RECOVERED_PENDING",
        )

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

    def test_live_initial_transport_envelope_uses_complete_packet_contract(self) -> None:
        packet = self.built.packet_payload
        protocol = packet["initial_research_protocol"]
        contracts = packet["research_contract_snapshot"]
        schema = packet["dossier_output_schema"]
        prompt = self.built.prompt.prompt_text

        self.assertEqual(
            protocol["protocol_hash"],
            canonical_hash(
                {"instructions_markdown": protocol["instructions_markdown"]}
            ),
        )
        self.assertEqual(
            contracts["snapshot_hash"],
            canonical_hash(
                {
                    key: value
                    for key, value in contracts.items()
                    if key != "snapshot_hash"
                }
            ),
        )
        self.assertEqual(
            packet["dossier_output_schema_hash"],
            canonical_hash(schema),
        )
        self.assertEqual(
            schema["properties"]["schema_version"]["const"],
            "e2r_pro_research_dossier_v3",
        )
        self.assertLess(len(prompt), 10_000)
        for field_path in (
            "initial_research_protocol.instructions_markdown",
            "research_contract_snapshot.contracts",
            "dossier_output_schema",
        ):
            self.assertIn(field_path, prompt)
        self.assertIn("`ID-PLACEHOLDER`", prompt)
        self.assertIn("source와 atomic fact가 모두 0인 빈 스캐폴드", prompt)
        self.assertIn("원래 언어 문장을 그대로 복사", prompt)
        self.assertIn("문자 그대로 다시 찾으라", prompt)
        self.assertIn("표 cell 재조립", prompt)
        self.assertIn("unresolved gap으로 남겨라", prompt)
        self.assertIn(self.fresh_job.job_id, prompt)
        self.assertIn(str(self.built.packet_payload["run_id"]), prompt)
        self.assertNotIn(f"`{ARCHETYPE}_Q01`", prompt)

        transport_receipt = json.loads(
            (
                self.boundary.fresh_job_root
                / "fresh_session/initial_prompt_v3_receipt.json"
            ).read_text(encoding="utf-8")
        )
        contract_receipt = json.loads(
            (
                self.boundary.fresh_job_root
                / "fresh_session/initial_prompt_v3_contract_receipt.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(
            transport_receipt["delivery_mode"],
            "ATTACHMENT_BACKED_TRANSPORT_ENVELOPE",
        )
        self.assertEqual(
            contract_receipt["delivery_mode"],
            "HASH_BOUND_RESEARCH_PACKET_FIELDS",
        )

    def test_transport_envelope_rejects_tampered_packet_schema(self) -> None:
        tampered = json.loads(
            json.dumps(self.built.packet_payload, ensure_ascii=False)
        )
        tampered["dossier_output_schema_hash"] = "0" * 64

        with self.assertRaisesRegex(ValueError, "dossier output schema differs"):
            self.orchestrator.initial_compiler.compile_transport_envelope(
                packet=tampered,
                primary_archetype_ids=self.fresh_job.archetype_ids,
                conversation_id="PENDING_NEW_CONVERSATION",
                research_pass_id=self.built.initial_pass_id,
            )

    async def test_live_initial_prompt_over_public_composer_boundary_stops_before_browser(
        self,
    ) -> None:
        oversized = replace(
            self.built,
            prompt=replace(self.built.prompt, prompt_text="x" * 59_801),
        )
        config = replace(
            load_pro_first_local_config(
                Path(__file__).parents[1]
                / "configs/e2r_pro_first_local.example.yaml"
            ),
            runtime_root=self.boundary.fresh_runtime_root,
        )

        with self.assertRaisesRegex(
            FreshSessionBoundaryError,
            "public-composer safety boundary",
        ):
            await self.orchestrator.prepare_initial_in_logged_in_browser(
                oversized,
                config=config,
            )

        self.assertEqual(
            self.store.get_job(self.fresh_job.job_id).status,
            JobStatus.PACKET_READY.value,
        )

    async def test_exact_open_conversation_bypasses_changed_history_search_ui(
        self,
    ) -> None:
        conversation_id = "fresh-conversation-already-open"
        adapter = _FreshAdapter(submitted_conversation_id=conversation_id)
        adapter.current_conversation_id = conversation_id

        source = await _ensure_durable_conversation_visible(
            adapter,
            job_id=self.fresh_job.job_id,
            run_id=str(self.built.packet_payload["run_id"]),
            durable_conversation_id=conversation_id,
            search_terms=(conversation_id, self.fresh_job.company_name),
        )

        self.assertEqual(source, "CURRENT_EXACT_CONVERSATION")
        self.assertEqual(adapter.submit_count, 0)

    async def test_library_page_opens_exact_durable_url_without_submit(self) -> None:
        conversation_id = "fresh-conversation-from-library"

        class LibraryAdapter(_FreshAdapter):
            async def ensure_logged_in(self) -> BrowserInspection:
                if self.current_conversation_id is None:
                    raise BrowserUIIncompatible("composer absent on Library")
                return self._inspection(BrowserUIState.READY_FOR_INPUT)

        adapter = LibraryAdapter(submitted_conversation_id=conversation_id)

        source = await _ensure_durable_conversation_visible(
            adapter,
            job_id=self.fresh_job.job_id,
            run_id=str(self.built.packet_payload["run_id"]),
            durable_conversation_id=conversation_id,
            search_terms=(conversation_id, self.fresh_job.company_name),
        )

        self.assertEqual(source, "PUBLIC_EXACT_CONVERSATION_URL")
        self.assertEqual(adapter.current_conversation_id, conversation_id)
        self.assertEqual(adapter.submit_count, 0)

    async def test_other_open_chat_uses_exact_durable_url_without_history(self) -> None:
        conversation_id = "fresh-conversation-durable-target"
        adapter = _FreshAdapter(submitted_conversation_id=conversation_id)
        adapter.current_conversation_id = "unrelated-open-conversation"

        source = await _ensure_durable_conversation_visible(
            adapter,
            job_id=self.fresh_job.job_id,
            run_id=str(self.built.packet_payload["run_id"]),
            durable_conversation_id=conversation_id,
            search_terms=("ignored mutable history hint",),
        )

        self.assertEqual(source, "PUBLIC_EXACT_CONVERSATION_URL")
        self.assertEqual(adapter.current_conversation_id, conversation_id)
        self.assertEqual(adapter.submit_count, 0)

    async def test_fresh_wrapper_resumes_proven_intercepted_claim(self) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-intercepted")
        await self.orchestrator.submit_initial_once(adapter)
        adapter.persistence_count = 0
        adapter.persistence_results = (False, True)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="d" * 64,
        )
        plan, _compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="PUBLIC_GAP_CLOSURE",
            latest_dossier_digest={"dossier_hash": "e" * 64},
            unresolved_question_state=(
                {
                    "question_family_id": (
                        self.built.prompt.mandatory_question_ids[0]
                    ),
                    "deterministic_status": "PUBLIC_SEARCHABLE",
                },
            ),
            pass_inputs={"research_gap_context_hash": "f" * 64},
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        claimed = self.orchestrator.ledger.claim_submit(
            plan.research_pass.pass_id
        )
        self.orchestrator.ledger.mark_transport_pending(
            claimed.pass_id,
            reason=INTERCEPTED_CLICK_REASON,
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

    def test_downloaded_repair_json_uses_exact_payload_lineage_without_md_markers(
        self,
    ) -> None:
        payload = {
            "schema_version": "e2r_pro_repair_delta_v3",
            "job_id": self.fresh_job.job_id,
            "run_id": self.built.packet_payload["run_id"],
            "research_pass_id": "PROPASS-REPAIR-DOWNLOAD",
            "parent_pass_id": self.built.initial_pass_id,
        }
        parsed = _parse_and_validate_compact_repair_transport(
            report_text=json.dumps(payload),
            capture_source="DOWNLOAD_JSON",
            job_id=self.fresh_job.job_id,
            run_id=self.built.packet_payload["run_id"],
            pass_id="PROPASS-REPAIR-DOWNLOAD",
            parent_pass_id=self.built.initial_pass_id,
        )
        self.assertEqual(parsed.payload, payload)

        payload["parent_pass_id"] = "PROPASS-WRONG-PARENT"
        with self.assertRaisesRegex(Exception, "mismatched parent_pass_id"):
            _parse_and_validate_compact_repair_transport(
                report_text=json.dumps(payload),
                capture_source="DOWNLOAD_JSON",
                job_id=self.fresh_job.job_id,
                run_id=self.built.packet_payload["run_id"],
                pass_id="PROPASS-REPAIR-DOWNLOAD",
                parent_pass_id=self.built.initial_pass_id,
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

    async def test_frozen_submitted_boundary_allows_read_only_recovery(self) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-late-frozen")
        submitted = await self.orchestrator.submit_initial_once(adapter)
        job = submitted.submit_result.job
        frozen = self.store.seal_fresh_efficiency_failure(
            job.job_id,
            expected_version=job.state_version,
            reason="public conversation hydrated after the persistence poll bound",
            actor="test-late-frozen-recovery",
            idempotency_key="test-late-frozen-recovery",
        )

        service = FreshSessionBoundaryService(self.store)
        with self.assertRaisesRegex(FreshSessionBoundaryError, "not recoverable"):
            service.load_existing(
                fresh_runtime_root=self.boundary.fresh_runtime_root,
                leakage_manifest=self.manifest,
            )
        loaded, recovered = service.load_existing(
            fresh_runtime_root=self.boundary.fresh_runtime_root,
            leakage_manifest=self.manifest,
            allow_frozen_submitted_recovery=True,
        )

        self.assertEqual(loaded.fresh_job_id, frozen.job_id)
        self.assertEqual(recovered.submit_count, 1)
        self.assertIsNotNone(recovered.old_job_frozen_at)
        self.assertEqual(adapter.submit_count, 1)

    async def test_late_server_persistence_waits_for_terminal_without_resubmit(
        self,
    ) -> None:
        conversation_id = "fresh-conversation-late-persistence"
        submitted_adapter = await self._prepare_and_approve(conversation_id)
        await self.orchestrator.submit_initial_once(submitted_adapter)
        running = self.store.get_job(self.fresh_job.job_id)
        self.store.transition(
            running.job_id,
            expected_version=running.state_version,
            to_status=JobStatus.USER_ATTENTION_REQUIRED,
            actor="test-late-persistence-timeout",
            idempotency_key="test-late-persistence-timeout",
            payload={
                "submit_count": 1,
                "automatic_resubmit_allowed": False,
            },
            updates={
                "last_error_class": "RuntimeError",
                "last_error_message": "fresh public render arrived after poll bound",
            },
        )

        terminal = BrowserResultSnapshot(
            conversation_id=conversation_id,
            assistant_turn_id="assistant-late-persisted-terminal",
            report_text=(
                "[[E2R_PRO_JOB_ID:"
                + self.fresh_job.job_id
                + "]]\n[[E2R_PRO_RUN_ID:"
                + str(self.built.packet_payload["run_id"])
                + "]]\nterminal dossier"
            ),
            report_hash="9" * 64,
            has_citations=True,
            has_dossier_marker=True,
            job_marker_matches=True,
            run_marker_matches=True,
            new_attachment_keys=(),
        )

        class LatePersistenceAdapter(_FreshAdapter):
            def __init__(self) -> None:
                super().__init__(submitted_conversation_id=conversation_id)
                self.current_conversation_id = conversation_id
                self.submit_count = 1
                self.inspection_count = 0

            def conversation_id(self) -> str:
                return str(self.current_conversation_id)

            async def inspect_state(self) -> BrowserInspection:
                self.inspection_count += 1
                return self._inspection(
                    BrowserUIState.RESEARCH_RUNNING
                    if self.inspection_count == 1
                    else BrowserUIState.RESEARCH_COMPLETE
                )

            async def inspect_result(self, **_kwargs) -> BrowserResultSnapshot:
                return terminal

        adapter = LatePersistenceAdapter()
        base = load_pro_first_local_config(
            Path(__file__).parents[1]
            / "configs/e2r_pro_first_local.example.yaml"
        )
        runner = FreshV3InitialLiveCanaryRunner(
            replace(
                base,
                runtime_root=self.boundary.fresh_runtime_root,
                browser=replace(
                    base.browser,
                    poll_interval_seconds=0.001,
                    required_stable_observations=2,
                ),
            ),
            old_runtime_root=self.boundary.old_runtime_root,
            fresh_runtime_root=self.boundary.fresh_runtime_root,
            repo_root=self.root,
            store=self.store,
            source_verifier=object(),
            report_structurer=object(),
            max_completion_polls=4,
        )

        recovered = await runner._reverify_user_attention_result(
            job_id=self.fresh_job.job_id,
            run_id=str(self.built.packet_payload["run_id"]),
            initial_pass_id=self.built.initial_pass_id,
            adapter=adapter,
        )

        self.assertEqual(recovered.result.report_hash, "9" * 64)
        self.assertEqual(
            self.store.get_job(self.fresh_job.job_id).status,
            JobStatus.RESULT_DETECTED.value,
        )
        self.assertEqual(self.store.get_job(self.fresh_job.job_id).submit_count, 1)
        self.assertEqual(adapter.submit_count, 1)
        self.assertEqual(adapter.persistence_count, 1)

        detected = self.store.get_job(self.fresh_job.job_id)
        capturing = self.store.transition(
            detected.job_id,
            expected_version=detected.state_version,
            to_status=JobStatus.CAPTURING_ARTIFACTS,
            actor="test-capture-retry-start",
            idempotency_key="test-capture-retry-start",
        )
        self.store.transition(
            capturing.job_id,
            expected_version=capturing.state_version,
            to_status=JobStatus.USER_ATTENTION_REQUIRED,
            actor="test-empty-download",
            idempotency_key="test-empty-download",
            updates={
                "last_error_class": "BrowserUIIncompatible",
                "last_error_message": "empty report attachment",
            },
        )

        repeated = await runner._reverify_user_attention_result(
            job_id=self.fresh_job.job_id,
            run_id=str(self.built.packet_payload["run_id"]),
            initial_pass_id=self.built.initial_pass_id,
            adapter=adapter,
        )

        self.assertEqual(repeated.result.report_hash, "9" * 64)
        self.assertEqual(
            self.store.get_job(self.fresh_job.job_id).status,
            JobStatus.RESULT_DETECTED.value,
        )
        self.assertEqual(self.store.get_job(self.fresh_job.job_id).submit_count, 1)
        self.assertEqual(adapter.submit_count, 1)
        self.assertEqual(adapter.persistence_count, 2)
        reverified_keys = [
            event.idempotency_key
            for event in self.store.list_events(self.fresh_job.job_id)
            if event.idempotency_key.startswith("result-reverified:")
        ]
        self.assertEqual(len(reverified_keys), 2)
        self.assertEqual(len(set(reverified_keys)), 2)

    async def test_late_persisted_network_error_is_sealed_without_retry(
        self,
    ) -> None:
        conversation_id = "fresh-conversation-late-network-error"
        submitted_adapter = await self._prepare_and_approve(conversation_id)
        await self.orchestrator.submit_initial_once(submitted_adapter)
        running = self.store.get_job(self.fresh_job.job_id)
        self.store.transition(
            running.job_id,
            expected_version=running.state_version,
            to_status=JobStatus.USER_ATTENTION_REQUIRED,
            actor="test-late-network-persistence-timeout",
            idempotency_key="test-late-network-persistence-timeout",
            updates={
                "last_error_class": "RuntimeError",
                "last_error_message": "fresh public render arrived after poll bound",
            },
        )

        invalid = BrowserResultSnapshot(
            conversation_id=conversation_id,
            assistant_turn_id="assistant-late-network-error",
            report_text="",
            report_hash="8" * 64,
            has_citations=False,
            has_dossier_marker=False,
            job_marker_matches=False,
            run_marker_matches=False,
            new_attachment_keys=(),
        )

        class LateNetworkErrorAdapter(_FreshAdapter):
            def __init__(self) -> None:
                super().__init__(submitted_conversation_id=conversation_id)
                self.current_conversation_id = conversation_id
                self.submit_count = 1
                self.inspection_count = 0

            def conversation_id(self) -> str:
                return str(self.current_conversation_id)

            async def inspect_state(self) -> BrowserInspection:
                self.inspection_count += 1
                if self.inspection_count == 1:
                    return self._inspection(BrowserUIState.RESEARCH_COMPLETE)
                return BrowserInspection(
                    state=BrowserUIState.RETRYABLE_ERROR,
                    conversation_id=conversation_id,
                    editor_ready=True,
                    deep_research_ready=True,
                    packet_uploaded=True,
                    prompt_ready=False,
                    send_ready=True,
                    stop_visible=False,
                    detail="A network error occurred. Please check your connection.",
                )

            async def inspect_result(self, **_kwargs) -> BrowserResultSnapshot:
                return invalid

        adapter = LateNetworkErrorAdapter()
        base = load_pro_first_local_config(
            Path(__file__).parents[1]
            / "configs/e2r_pro_first_local.example.yaml"
        )
        runner = FreshV3InitialLiveCanaryRunner(
            replace(
                base,
                runtime_root=self.boundary.fresh_runtime_root,
                browser=replace(
                    base.browser,
                    poll_interval_seconds=0.001,
                    required_stable_observations=2,
                ),
            ),
            old_runtime_root=self.boundary.old_runtime_root,
            fresh_runtime_root=self.boundary.fresh_runtime_root,
            repo_root=self.root,
            store=self.store,
            source_verifier=object(),
            report_structurer=object(),
            max_completion_polls=4,
        )

        with self.assertRaisesRegex(
            ValueError,
            "provider failure was sealed without retry",
        ):
            await runner._reverify_user_attention_result(
                job_id=self.fresh_job.job_id,
                run_id=str(self.built.packet_payload["run_id"]),
                initial_pass_id=self.built.initial_pass_id,
                adapter=adapter,
            )

        frozen = self.store.get_job(self.fresh_job.job_id)
        self.assertIsNotNone(frozen.old_job_frozen_at)
        self.assertEqual(frozen.conversation_id, conversation_id)
        self.assertEqual(
            frozen.last_error_class,
            "CHATGPT_RETRYABLE_PROVIDER_ERROR",
        )
        self.assertEqual(frozen.submit_count, 1)
        self.assertEqual(frozen.capture_count, 0)
        self.assertEqual(adapter.submit_count, 1)
        self.assertEqual(adapter.persistence_count, 1)

        receipt_path = (
            self.boundary.fresh_job_root
            / "fresh_session/fresh_efficiency_failure_receipt.json"
        )
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        self.assertEqual(
            receipt["disposition"],
            "PROVIDER_ERROR_NEW_CONVERSATION_REQUIRED",
        )
        receipt_hash = receipt.pop("receipt_hash")
        self.assertEqual(receipt_hash, canonical_hash(receipt))

        manifest = build_old_answer_leakage_manifest(
            self.store,
            old_job_id=frozen.job_id,
            old_run_id=str(self.built.packet_payload["run_id"]),
            old_conversation_id=conversation_id,
            old_job_root=self.boundary.fresh_job_root,
        )
        self.assertIn(self.built.initial_pass_id, manifest.old_research_pass_ids)
        self.assertEqual(manifest.old_fact_ids, ())
        self.assertEqual(manifest.old_route_receipt_ids, ())

        tampered = json.loads(receipt_path.read_text(encoding="utf-8"))
        tampered["conversation_id"] = "tampered-conversation"
        receipt_path.write_text(
            json.dumps(tampered, ensure_ascii=False),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValueError, "identity or hash mismatch"):
            build_old_answer_leakage_manifest(
                self.store,
                old_job_id=frozen.job_id,
                old_run_id=str(self.built.packet_payload["run_id"]),
                old_conversation_id=conversation_id,
                old_job_root=self.boundary.fresh_job_root,
            )

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

    async def test_artifact_reexport_is_transport_only_and_not_semantic_parent(self) -> None:
        conversation_id = "fresh-conversation-artifact-reexport"
        adapter = await self._prepare_and_approve(conversation_id)
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="d" * 64,
        )
        plan, compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="ARTIFACT_REEXPORT",
            latest_dossier_digest={
                "initial_response_hash": "d" * 64,
                "transport_only": True,
            },
            pass_inputs={
                "route_reason": "CHATGPT_SANDBOX_ARTIFACT_FILE_NOT_FOUND",
                "expected_artifact_filename": "ResearchDossierV3.json",
                "initial_research_pass_id": self.built.initial_pass_id,
                "new_research_allowed": False,
            },
        )

        self.assertIn("웹 검색, 새 자료 수집, 새 사실 판단은 전부 금지", compiled.prompt_text)
        self.assertIn("실제 저장", compiled.prompt_text)
        self.assertIn(self.built.initial_pass_id, compiled.prompt_text)
        self.assertNotIn("ResearchDossierV3 **delta JSON**", compiled.prompt_text)
        await self.orchestrator.prepare_followup(plan, adapter)
        await self.orchestrator.submit_followup(plan, adapter)
        self.orchestrator.complete_followup(
            plan.research_pass.pass_id,
            response_hash="e" * 64,
            conversation_id=conversation_id,
        )

        saturation, _compiled_saturation = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="SATURATION_AUDIT",
            latest_dossier_digest={"dossier_hash": "f" * 64},
            pass_inputs={"transport_reexport_completed": True},
        )
        self.assertEqual(
            saturation.research_pass.parent_pass_id,
            self.built.initial_pass_id,
        )

    async def test_artifact_reexport_capture_hash_reconciles_only_initial_pass_metadata(
        self,
    ) -> None:
        conversation_id = "fresh-conversation-artifact-hash"
        adapter = await self._prepare_and_approve(conversation_id)
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="d" * 64,
        )
        plan, _compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="ARTIFACT_REEXPORT",
            latest_dossier_digest={
                "initial_response_hash": "d" * 64,
                "transport_only": True,
            },
            pass_inputs={
                "route_reason": "CHATGPT_SANDBOX_ARTIFACT_FILE_NOT_FOUND",
                "expected_artifact_filename": "ResearchDossierV3.json",
                "initial_research_pass_id": self.built.initial_pass_id,
                "new_research_allowed": False,
            },
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        await self.orchestrator.submit_followup(plan, adapter)
        artifact = self.orchestrator.complete_followup(
            plan.research_pass.pass_id,
            response_hash="e" * 64,
            conversation_id=conversation_id,
        )
        initial = self.orchestrator.ledger.get_pass(self.built.initial_pass_id)
        captured_file_hash = "f" * 64
        dossier = {
            "schema_version": "e2r_pro_research_dossier_v3",
            "material_facts": [{"dossier_fact_id": "PROFACT-UNCHANGED"}],
            "research_passes": [
                {
                    "pass_id": initial.pass_id,
                    "parent_pass_id": None,
                    "pass_name": initial.pass_name,
                    "status": "COMPLETE",
                    "prompt_hash": initial.prompt_hash,
                    "response_hash": captured_file_hash,
                }
            ],
        }
        capture = CaptureReceipt(
            schema_version="e2r_pro_capture_receipt_v1",
            event_type="PRO_RESEARCH_CAPTURE_COMPLETE",
            job_id=self.fresh_job.job_id,
            run_id=str(self.built.packet_payload["run_id"]),
            target_id=self.fresh_job.symbol,
            as_of_date=self.fresh_job.as_of_date,
            packet_hash=str(self.built.job.packet_hash),
            prompt_hash=initial.prompt_hash,
            conversation_id=conversation_id,
            assistant_turn_id="artifact-file-turn",
            report_md_hash=captured_file_hash,
            report_pdf_hash=None,
            dossier_json_hash="9" * 64,
            submit_count=1,
            capture_count=1,
            captured_at="2026-08-25T01:02:03Z",
            capture_mode=(
                "CHATGPT_WEB_VISIBLE_CHAT_PRO_FRESH_V3_RECOVERED_NO_SUBMIT"
            ),
            capture_source="DOWNLOAD_JSON",
            optional_pdf_error=None,
        )

        corrected, receipt = _reconcile_artifact_reexport_initial_pass_row(
            dossier=dossier,
            initial_pass=initial,
            artifact_pass=artifact,
            capture_receipt=capture,
        )

        self.assertEqual(
            corrected["research_passes"][0]["response_hash"],
            "d" * 64,
        )
        self.assertEqual(
            corrected["material_facts"],
            dossier["material_facts"],
        )
        self.assertEqual(
            dossier["research_passes"][0]["response_hash"],
            captured_file_hash,
        )
        self.assertEqual(receipt["browser_submit_delta"], 0)
        self.assertFalse(receipt["fact_content_mutation_allowed"])

        with self.assertRaisesRegex(ValueError, "exact artifact re-export proof"):
            _reconcile_artifact_reexport_initial_pass_row(
                dossier=dossier,
                initial_pass=initial,
                artifact_pass=None,
                capture_receipt=capture,
            )

    async def test_visible_artifact_reexport_reconciles_without_second_send(self) -> None:
        conversation_id = "fresh-conversation-visible-artifact-reexport"
        adapter = await self._prepare_and_approve(conversation_id)
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="d" * 64,
        )
        plan, _compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="ARTIFACT_REEXPORT",
            latest_dossier_digest={
                "initial_response_hash": "d" * 64,
                "transport_only": True,
            },
            pass_inputs={
                "route_reason": "CHATGPT_SANDBOX_ARTIFACT_FILE_NOT_FOUND",
                "expected_artifact_filename": "ResearchDossierV3.json",
                "initial_research_pass_id": self.built.initial_pass_id,
                "new_research_allowed": False,
            },
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        claimed = self.orchestrator.ledger.claim_submit(plan.research_pass.pass_id)
        self.orchestrator.ledger.mark_transport_pending(
            claimed.pass_id,
            reason=(
                "TimeoutError: Locator.click: Timeout 30000ms exceeded; "
                "waiting for element to be visible, enabled and stable; "
                "composer-submit-button"
            ),
        )
        response_hash = "e" * 64
        result = BrowserResultSnapshot(
            conversation_id=conversation_id,
            assistant_turn_id="artifact-reexport-turn",
            report_text="\n".join(
                (
                    f"[[E2R_PRO_JOB_ID:{self.fresh_job.job_id}]]",
                    f"[[E2R_PRO_RUN_ID:{self.built.packet_payload['run_id']}]]",
                    f"[[E2R_PRO_PASS_ID:{plan.research_pass.pass_id}]]",
                    f"[[E2R_PRO_PARENT_PASS_ID:{self.built.initial_pass_id}]]",
                    "ARTIFACT_REEXPORT 완료",
                )
            ),
            report_hash=response_hash,
            has_citations=False,
            has_dossier_marker=False,
            job_marker_matches=True,
            run_marker_matches=True,
            new_attachment_keys=(),
        )
        base = load_pro_first_local_config(
            Path(__file__).parents[1]
            / "configs/e2r_pro_first_local.example.yaml"
        )
        runner = FreshV3InitialLiveCanaryRunner(
            replace(base, runtime_root=self.boundary.fresh_runtime_root),
            old_runtime_root=self.boundary.old_runtime_root,
            fresh_runtime_root=self.boundary.fresh_runtime_root,
            repo_root=self.root,
            store=self.store,
            source_verifier=object(),
            report_structurer=object(),
        )

        reconciled = runner._reconcile_visible_artifact_reexport(
            orchestrator=self.orchestrator,
            built=self.built,
            result=result,
        )

        current = self.orchestrator.ledger.get_pass(plan.research_pass.pass_id)
        self.assertTrue(reconciled)
        self.assertEqual(current.status, "COMPLETE")
        self.assertEqual(current.submit_count, 1)
        self.assertEqual(current.response_hash, response_hash)
        self.assertEqual(current.detail["research_status"], "COMPLETE")
        self.assertEqual(adapter.submit_count, 1)

    async def test_failed_hard_followup_does_not_block_later_compact_repair(self) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-failed-before-repair")
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="d" * 64,
        )
        failed, _compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="PUBLIC_GAP_CLOSURE",
            latest_dossier_digest={
                "dossier_hash": "e" * 64,
                "mandatory_question_nonterminal_count": 1,
            },
            unresolved_question_state=(
                {
                    "question_family_id": self.built.prompt.mandatory_question_ids[0],
                    "deterministic_status": "PUBLIC_SEARCHABLE",
                },
            ),
            pass_inputs={"research_gap_context_hash": "f" * 64},
        )
        await self.orchestrator.prepare_followup(failed, adapter)
        await self.orchestrator.submit_followup(failed, adapter)
        self.orchestrator.ledger.mark_failed_hard(
            failed.research_pass.pass_id,
            response_hash="1" * 64,
            failure_class="CHATGPT_VISIBLE_RESPONSE_FAILURE",
            reason="sealed provider response cannot be reused",
        )

        dossier, classifications, verifications, job_root = self._repair_inputs()
        repair, _compiled_repair = self.orchestrator.plan_compact_repair(
            self.built,
            dossier=dossier,
            rejection_classifications=classifications,
            verification_rows=verifications,
            job_root=job_root,
        )

        self.assertEqual(repair.research_pass.pass_name, "VERIFIER_REPAIR")
        self.assertEqual(repair.research_pass.submit_count, 0)
        self.assertEqual(
            repair.research_pass.parent_pass_id,
            self.built.initial_pass_id,
        )

    async def test_visible_provider_failure_gets_one_feedback_retry_then_blocks(self) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-failure")
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="d" * 64,
        )
        digest = {
            "dossier_hash": "e" * 64,
            "mandatory_question_nonterminal_count": 2,
        }
        unresolved = (
            {
                "question_family_id": self.built.prompt.mandatory_question_ids[0],
                "deterministic_status": "PUBLIC_SEARCHABLE",
            },
        )
        inputs = {"research_gap_context_hash": "f" * 64}
        first, _ = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="PUBLIC_GAP_CLOSURE",
            latest_dossier_digest=digest,
            unresolved_question_state=unresolved,
            pass_inputs=inputs,
        )
        await self.orchestrator.prepare_followup(first, adapter)
        await self.orchestrator.submit_followup(first, adapter)
        self.orchestrator.ledger.mark_failed_hard(
            first.research_pass.pass_id,
            response_hash="1" * 64,
            failure_class="CHATGPT_VISIBLE_THINKING_FAILED",
            reason="thinking failed before JSON output",
        )

        retry, compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="PUBLIC_GAP_CLOSURE",
            latest_dossier_digest=digest,
            unresolved_question_state=unresolved,
            pass_inputs=inputs,
        )
        self.assertNotEqual(retry.research_pass.pass_id, first.research_pass.pass_id)
        self.assertEqual(
            retry.research_pass.detail["supersedes_failed_pass_id"],
            first.research_pass.pass_id,
        )
        self.assertIn("provider_failure_feedback", compiled.prompt_text)
        await self.orchestrator.prepare_followup(retry, adapter)
        await self.orchestrator.submit_followup(retry, adapter)
        self.orchestrator.ledger.mark_failed_hard(
            retry.research_pass.pass_id,
            response_hash="2" * 64,
            failure_class="CHATGPT_VISIBLE_THINKING_FAILED",
            reason="same context failed a second time",
        )

        with self.assertRaisesRegex(
            FreshSessionBoundaryError,
            "same fresh V3 context failed twice",
        ):
            self.orchestrator.plan_v3_followup(
                self.built,
                pass_name="PUBLIC_GAP_CLOSURE",
                latest_dossier_digest=digest,
                unresolved_question_state=unresolved,
                pass_inputs=inputs,
            )

    async def test_unpersisted_turn_gets_one_distinct_replacement_then_blocks(self) -> None:
        adapter = await self._prepare_and_approve("fresh-conversation-transport")
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="a" * 64,
        )
        digest = {
            "dossier_hash": "b" * 64,
            "mandatory_question_nonterminal_count": 1,
        }
        unresolved = (
            {
                "question_family_id": self.built.prompt.mandatory_question_ids[0],
                "deterministic_status": "PUBLIC_SEARCHABLE",
            },
        )
        inputs = {"research_gap_context_hash": "c" * 64}

        def absence(pass_id: str, parent_pass_id: str, ordinal: int):
            return BrowserSubmittedTurnPersistence(
                observation_id=f"PROSERVERVIEW-ABSENT-{pass_id}-{ordinal}",
                observed_at=f"2026-08-25T01:02:0{ordinal}Z",
                conversation_id="fresh-conversation-transport",
                job_id=self.fresh_job.job_id,
                run_id=str(self.built.packet_payload["run_id"]),
                pass_id=pass_id,
                parent_pass_id=parent_pass_id,
                persistence_confirmed=False,
                user_turn_id=None,
                required_markers=(
                    f"[[E2R_PRO_JOB_ID:{self.fresh_job.job_id}]]",
                    f"[[E2R_PRO_PASS_ID:{pass_id}]]",
                    f"[[E2R_PRO_PARENT_PASS_ID:{parent_pass_id}]]",
                ),
                missing_markers=(f"[[E2R_PRO_PASS_ID:{pass_id}]]",),
                observed_user_turn_count=4,
                fresh_page_url=(
                    "https://chatgpt.com/c/fresh-conversation-transport"
                ),
                fresh_page_loaded=True,
            )

        first, _ = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="PUBLIC_GAP_CLOSURE",
            latest_dossier_digest=digest,
            unresolved_question_state=unresolved,
            pass_inputs=inputs,
        )
        self.orchestrator.ledger.mark_prepared(first.research_pass.pass_id)
        first_claimed = self.orchestrator.ledger.claim_submit(
            first.research_pass.pass_id
        )
        for ordinal in (1, 2):
            self.orchestrator.ledger.record_server_persistence_observation(
                first_claimed.pass_id,
                observation=absence(
                    first_claimed.pass_id,
                    str(first_claimed.parent_pass_id),
                    ordinal,
                ),
            )
        first_failed = self.orchestrator.ledger.seal_unpersisted_dispatch(
            first_claimed.pass_id
        )

        replacement, compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="PUBLIC_GAP_CLOSURE",
            latest_dossier_digest=digest,
            unresolved_question_state=unresolved,
            pass_inputs=inputs,
        )

        self.assertNotEqual(replacement.research_pass.pass_id, first_failed.pass_id)
        self.assertEqual(
            replacement.research_pass.detail["supersedes_unpersisted_pass_id"],
            first_failed.pass_id,
        )
        self.assertIn("transport_persistence_feedback", compiled.prompt_text)
        self.assertEqual(first_failed.submit_count, 1)

        self.orchestrator.ledger.mark_prepared(replacement.research_pass.pass_id)
        second_claimed = self.orchestrator.ledger.claim_submit(
            replacement.research_pass.pass_id
        )
        for ordinal in (1, 2):
            self.orchestrator.ledger.record_server_persistence_observation(
                second_claimed.pass_id,
                observation=absence(
                    second_claimed.pass_id,
                    str(second_claimed.parent_pass_id),
                    ordinal,
                ),
            )
        self.orchestrator.ledger.seal_unpersisted_dispatch(second_claimed.pass_id)

        with self.assertRaisesRegex(
            FreshSessionBoundaryError,
            "failed server persistence twice",
        ):
            self.orchestrator.plan_v3_followup(
                self.built,
                pass_name="PUBLIC_GAP_CLOSURE",
                latest_dossier_digest=digest,
                unresolved_question_state=unresolved,
                pass_inputs=inputs,
            )

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
        self.assertIn("subject는 source 원문에 실제로 연속 등장", compiled.prompt_text)
        self.assertIn("401/403·로그인·anti-bot", compiled.prompt_text)
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

    async def test_large_public_followup_context_is_losslessly_compacted(self) -> None:
        adapter = await self._prepare_and_approve(
            "fresh-conversation-large-public-context"
        )
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="7" * 64,
        )
        unresolved = []
        question_ids = []
        for question_index in range(25):
            question_id = f"QUESTION-LARGE-{question_index:02}"
            question_ids.append(question_id)
            route_ids = [
                f"ROUTE-{question_index:02}-{route_index:02}-" + "x" * 24
                for route_index in range(6)
            ]
            unresolved.append(
                {
                    "question_family_id": question_id,
                    "reported_status": "PUBLIC_SEARCHABLE",
                    "availability_class": "PUBLIC_SEARCHABLE",
                    "closure_reason": "",
                    "required_source_roles_missing": [
                        "ISSUER_OFFICIAL",
                        "OFFICIAL_FILING",
                    ],
                    "search_route_receipt_ids": route_ids,
                    "deterministic_status": "PUBLIC_SEARCHABLE",
                    "gap_class": "CORE_SCORE_BLOCKER",
                    "failure_codes": [
                        "PUBLIC_MATERIAL_GAP",
                        "SOURCE_LINKAGE_INCOMPLETE",
                    ],
                    "verified_linked_fact_ids": route_ids,
                    "linked_source_lineage_ids": route_ids,
                    "linked_route_receipt_ids": route_ids,
                    "missing_core_source_roles": ["OFFICIAL_FILING"],
                    "missing_corroboration_source_roles": [],
                    "verified_source_roles": ["ISSUER_OFFICIAL"],
                    "deterministic_terminal": False,
                    "deterministic_ready": False,
                    "route_progress_state": {
                        "route_signatures": route_ids,
                        "latest_route_outcomes": [
                            {
                                "route_signature": route_id,
                                "provider_status": "SUCCESS",
                                "parser_status": "SUCCESS",
                                "verified_accepted_fact_ids": [],
                                "no_new_route_confirmed": False,
                            }
                            for route_id in route_ids
                        ],
                        "failure_codes": [],
                    },
                }
            )
        latest_digest = {
            "dossier_hash": "a" * 64,
            "verified_fact_ids": [f"FACT-{index:02}" for index in range(30)],
        }
        pass_inputs = {
            "question_family_ids": question_ids,
            "question_context_hashes": {
                question_id: "b" * 64 for question_id in question_ids
            },
            "question_progress_hashes": {
                question_id: "c" * 64 for question_id in question_ids
            },
            "research_gap_context_hash": "d" * 64,
        }
        expected_context = {
            "latest_dossier_digest": latest_digest,
            "unresolved_question_state": unresolved,
            "pass_inputs": pass_inputs,
        }
        pretty_context = json.dumps(
            expected_context,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )

        _plan, compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="PUBLIC_GAP_CLOSURE",
            latest_dossier_digest=latest_digest,
            unresolved_question_state=unresolved,
            pass_inputs=pass_inputs,
        )
        embedded_context = compiled.prompt_text.split("```json\n", 1)[1].split(
            "\n```", 1
        )[0]

        self.assertGreater(len(pretty_context), 100_000)
        self.assertLess(len(compiled.prompt_text), 100_000)
        self.assertEqual(json.loads(embedded_context), expected_context)

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

    async def test_new_fact_id_without_blocker_change_reaches_fixpoint(self) -> None:
        adapter = await self._prepare_and_approve(
            "fresh-conversation-blocker-fixpoint"
        )
        await self.orchestrator.submit_initial_once(adapter)
        self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash="4" * 64,
        )
        question_id = self.built.prompt.mandatory_question_ids[0]
        dossier = self._tail_dossier(question_id)
        first = _followup_context(
            dossier=dossier,
            saturation=self._tail_saturation(
                (self._question_decision(question_id, linked_fact_id="FACT-A"),),
                fact_hash="1" * 64,
            ),
            accepted_fact_ids=("FACT-A",),
            question_ids=(question_id,),
            pass_name="PUBLIC_GAP_CLOSURE",
        )
        plan, _compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="PUBLIC_GAP_CLOSURE",
            latest_dossier_digest=first["latest_dossier_digest"],
            unresolved_question_state=first["unresolved_question_state"],
            pass_inputs=first["pass_inputs"],
        )
        await self.orchestrator.prepare_followup(plan, adapter)
        await self.orchestrator.submit_followup(plan, adapter)
        self.orchestrator.complete_followup(
            plan.research_pass.pass_id,
            response_hash="5" * 64,
            conversation_id="fresh-conversation-blocker-fixpoint",
        )

        fact_only = _followup_context(
            dossier={
                **dossier,
                "material_facts": [
                    *dossier["material_facts"],
                    {"dossier_fact_id": "FACT-B"},
                ],
            },
            saturation=self._tail_saturation(
                (self._question_decision(question_id, linked_fact_id="FACT-B"),),
                fact_hash="2" * 64,
            ),
            accepted_fact_ids=("FACT-A", "FACT-B"),
            question_ids=(question_id,),
            pass_name="PUBLIC_GAP_CLOSURE",
        )
        self.assertNotEqual(
            first["pass_inputs"]["research_gap_context_hash"],
            fact_only["pass_inputs"]["research_gap_context_hash"],
        )
        self.assertEqual(
            first["pass_inputs"]["saturation_blocker_identity_hash"],
            fact_only["pass_inputs"]["saturation_blocker_identity_hash"],
        )
        self.assertTrue(
            _completed_pass_left_blockers_unchanged(
                self.orchestrator.ledger,
                job_id=self.fresh_job.job_id,
                pass_name="PUBLIC_GAP_CLOSURE",
                blocker_identity_hash=fact_only["pass_inputs"][
                    "saturation_blocker_identity_hash"
                ],
            )
        )

        changed_route = _followup_context(
            dossier=dossier,
            saturation=self._tail_saturation(
                (
                    self._question_decision(
                        question_id,
                        linked_fact_id="FACT-B",
                        provider_parser_normal=False,
                    ),
                ),
                fact_hash="2" * 64,
            ),
            accepted_fact_ids=("FACT-A", "FACT-B"),
            question_ids=(question_id,),
            pass_name="PUBLIC_GAP_CLOSURE",
        )
        self.assertNotEqual(
            first["pass_inputs"]["saturation_blocker_identity_hash"],
            changed_route["pass_inputs"]["saturation_blocker_identity_hash"],
        )
        self.assertFalse(
            _completed_pass_left_blockers_unchanged(
                self.orchestrator.ledger,
                job_id=self.fresh_job.job_id,
                pass_name="PUBLIC_GAP_CLOSURE",
                blocker_identity_hash=changed_route["pass_inputs"][
                    "saturation_blocker_identity_hash"
                ],
            )
        )

    def test_same_question_set_is_not_reopened_a_third_time(self) -> None:
        question_id = self.built.prompt.mandatory_question_ids[0]
        rows = (
            SimpleNamespace(
                pass_name="PUBLIC_GAP_CLOSURE",
                status="COMPLETE",
                submit_count=1,
                detail={"question_family_ids": [question_id]},
            ),
            SimpleNamespace(
                pass_name="PUBLIC_GAP_CLOSURE",
                status="COMPLETE",
                submit_count=1,
                detail={"question_family_ids": [question_id]},
            ),
        )
        ledger = SimpleNamespace(list_passes=lambda _job_id: rows)

        self.assertTrue(
            _same_question_reopen_limit_reached(
                ledger,
                job_id="PROJOB-REOPEN-LIMIT",
                pass_name="PUBLIC_GAP_CLOSURE",
                question_ids=(question_id,),
            )
        )
        self.assertFalse(
            _same_question_reopen_limit_reached(
                ledger,
                job_id="PROJOB-REOPEN-LIMIT",
                pass_name="PUBLIC_GAP_CLOSURE",
                question_ids=(question_id, "QUESTION-SIBLING"),
            )
        )

    def test_reopen_budget_is_question_scoped_across_changed_batches(self) -> None:
        question_a, question_b = self.built.prompt.mandatory_question_ids[:2]
        rows = (
            SimpleNamespace(
                pass_name="PUBLIC_GAP_CLOSURE",
                status="COMPLETE",
                submit_count=1,
                detail={"question_family_ids": [question_a, question_b]},
            ),
            SimpleNamespace(
                pass_name="PUBLIC_GAP_CLOSURE",
                status="COMPLETE",
                submit_count=1,
                detail={"question_family_ids": [question_a]},
            ),
        )
        ledger = SimpleNamespace(list_passes=lambda _job_id: rows)
        context = {
            "pass_inputs": {
                "question_stable_gap_hashes": {
                    question_a: "a" * 64,
                    question_b: "b" * 64,
                }
            }
        }

        self.assertEqual(
            _question_ids_with_reopen_budget(
                ledger,
                job_id="PROJOB-QUESTION-BUDGET",
                pass_name="PUBLIC_GAP_CLOSURE",
                question_ids=(question_a, question_b),
                context=context,
            ),
            (question_b,),
        )

        rows_with_new_identity = (
            *rows,
            SimpleNamespace(
                pass_name="PUBLIC_GAP_CLOSURE",
                status="COMPLETE",
                submit_count=1,
                detail={
                    "question_family_ids": [question_b],
                    "question_stable_gap_hashes": {question_b: "c" * 64},
                },
            ),
        )
        changed_ledger = SimpleNamespace(
            list_passes=lambda _job_id: rows_with_new_identity
        )
        self.assertEqual(
            _question_ids_with_reopen_budget(
                changed_ledger,
                job_id="PROJOB-QUESTION-BUDGET",
                pass_name="PUBLIC_GAP_CLOSURE",
                question_ids=(question_b,),
                context=context,
            ),
            (question_b,),
        )

    def test_reopen_budget_ignores_requested_question_without_returned_route(
        self,
    ) -> None:
        question_a, question_b = self.built.prompt.mandatory_question_ids[:2]
        rows = (
            SimpleNamespace(
                pass_id="PASS-ONE",
                pass_name="PUBLIC_GAP_CLOSURE",
                status="COMPLETE",
                submit_count=1,
                detail={
                    "question_family_ids": [question_a, question_b],
                    "question_stable_gap_hashes": {
                        question_a: "a" * 64,
                        question_b: "b" * 64,
                    },
                },
            ),
            SimpleNamespace(
                pass_id="PASS-TWO",
                pass_name="PUBLIC_GAP_CLOSURE",
                status="COMPLETE",
                submit_count=1,
                detail={
                    "question_family_ids": [question_a, question_b],
                    "question_stable_gap_hashes": {
                        question_a: "a" * 64,
                        question_b: "b" * 64,
                    },
                },
            ),
        )
        ledger = SimpleNamespace(list_passes=lambda _job_id: rows)
        context = {
            "pass_inputs": {
                "question_stable_gap_hashes": {
                    question_a: "a" * 64,
                    question_b: "b" * 64,
                }
            }
        }
        dossier = {
            "search_route_receipts": [
                {
                    "route_receipt_id": "ROUTE-A-ONE",
                    "pass_id": "PASS-ONE",
                    "question_family_id": question_a,
                },
                {
                    "route_receipt_id": "ROUTE-A-TWO",
                    "pass_id": "PASS-TWO",
                    "question_family_id": question_a,
                },
            ]
        }

        self.assertEqual(
            _question_ids_with_reopen_budget(
                ledger,
                job_id="PROJOB-ACTUAL-ROUTE-BUDGET",
                pass_name="PUBLIC_GAP_CLOSURE",
                question_ids=(question_a, question_b),
                context=context,
                dossier=dossier,
            ),
            (question_b,),
        )

    def test_reopen_budget_counts_only_routes_on_current_verified_snapshot(
        self,
    ) -> None:
        question_id = self.built.prompt.mandatory_question_ids[0]
        stable_hash = "a" * 64
        current_fact_hash = "b" * 64
        current_lineage_hash = "c" * 64

        def pass_row(pass_id: str):
            return SimpleNamespace(
                pass_id=pass_id,
                pass_name="PUBLIC_GAP_CLOSURE",
                status="COMPLETE",
                submit_count=1,
                detail={
                    "question_family_ids": [question_id],
                    "question_stable_gap_hashes": {
                        question_id: stable_hash
                    },
                },
            )

        old_pass = pass_row("PASS-OLD-SNAPSHOT")
        current_pass = pass_row("PASS-CURRENT-SNAPSHOT-ONE")
        context = {
            "pass_inputs": {
                "question_stable_gap_hashes": {
                    question_id: stable_hash
                }
            }
        }
        dossier = {
            "search_route_receipts": [
                {
                    "route_receipt_id": "ROUTE-OLD-SNAPSHOT",
                    "pass_id": old_pass.pass_id,
                    "question_family_id": question_id,
                },
                {
                    "route_receipt_id": "ROUTE-CURRENT-SNAPSHOT-ONE",
                    "pass_id": current_pass.pass_id,
                    "question_family_id": question_id,
                },
            ]
        }
        bindings = {
            "ROUTE-OLD-SNAPSHOT": {
                "pass_id": old_pass.pass_id,
                "question_family_id": question_id,
                "fact_snapshot_hash": "d" * 64,
                "accepted_lineage_roster_hash": "e" * 64,
            },
            "ROUTE-CURRENT-SNAPSHOT-ONE": {
                "pass_id": current_pass.pass_id,
                "question_family_id": question_id,
                "fact_snapshot_hash": current_fact_hash,
                "accepted_lineage_roster_hash": current_lineage_hash,
            },
        }
        ledger = SimpleNamespace(
            list_passes=lambda _job_id: (old_pass, current_pass)
        )

        self.assertEqual(
            _question_ids_with_reopen_budget(
                ledger,
                job_id="PROJOB-EXACT-SNAPSHOT-BUDGET",
                pass_name="PUBLIC_GAP_CLOSURE",
                question_ids=(question_id,),
                context=context,
                dossier=dossier,
                route_snapshot_bindings=bindings,
                current_fact_snapshot_hash=current_fact_hash,
                current_accepted_lineage_roster_hash=(
                    current_lineage_hash
                ),
            ),
            (question_id,),
        )

        second_current = pass_row("PASS-CURRENT-SNAPSHOT-TWO")
        dossier["search_route_receipts"].append(
            {
                "route_receipt_id": "ROUTE-CURRENT-SNAPSHOT-TWO",
                "pass_id": second_current.pass_id,
                "question_family_id": question_id,
            }
        )
        bindings["ROUTE-CURRENT-SNAPSHOT-TWO"] = {
            "pass_id": second_current.pass_id,
            "question_family_id": question_id,
            "fact_snapshot_hash": current_fact_hash,
            "accepted_lineage_roster_hash": current_lineage_hash,
        }
        exhausted_ledger = SimpleNamespace(
            list_passes=lambda _job_id: (
                old_pass,
                current_pass,
                second_current,
            )
        )
        self.assertEqual(
            _question_ids_with_reopen_budget(
                exhausted_ledger,
                job_id="PROJOB-EXACT-SNAPSHOT-BUDGET",
                pass_name="PUBLIC_GAP_CLOSURE",
                question_ids=(question_id,),
                context=context,
                dossier=dossier,
                route_snapshot_bindings=bindings,
                current_fact_snapshot_hash=current_fact_hash,
                current_accepted_lineage_roster_hash=(
                    current_lineage_hash
                ),
            ),
            (),
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

    def test_saturation_audit_compacts_append_only_route_history(self) -> None:
        question_ids = self.built.prompt.mandatory_question_ids
        dossier = self._tail_dossier(*question_ids)
        decisions = []
        for question_index, question_id in enumerate(question_ids):
            route_ids = []
            for route_index in range(40):
                route_id = f"ROUTE-AUDIT-{question_index}-{route_index}"
                route_ids.append(route_id)
                dossier["search_route_receipts"].append(
                    {
                        "route_receipt_id": route_id,
                        "pass_id": f"PROPASS-AUDIT-{route_index}",
                        "source_role_id": "ISSUER_OFFICIAL",
                        "query_text": f"audit query {question_index} {route_index}",
                        "opened_source_urls": [
                            f"https://issuer.example/audit/{question_index}/{route_index}"
                        ],
                        "provider_status": "SUCCESS",
                        "parser_status": "SUCCESS",
                        "accepted_fact_ids": [f"FACT-{question_index + 1}"],
                        "no_new_route_reason": "no newer public route",
                    }
                )
            dossier["question_family_results"][question_index][
                "search_route_receipt_ids"
            ] = route_ids
            base = self._question_decision(
                question_id,
                linked_fact_id=f"FACT-{question_index + 1}",
            )
            payload = base.to_dict()
            payload["route_adequacy"]["linked_route_receipt_ids"] = route_ids
            decisions.append(
                SimpleNamespace(
                    question_family_id=question_id,
                    materiality="CORE_SCORE",
                    status="SUPPORTED_SCORING",
                    to_dict=lambda payload=payload: dict(payload),
                )
            )

        context = _followup_context(
            dossier=dossier,
            saturation=self._tail_saturation(
                tuple(decisions),
                fact_hash="5" * 64,
            ),
            accepted_fact_ids=tuple(
                f"FACT-{index + 1}" for index in range(len(question_ids))
            ),
            question_ids=question_ids,
            pass_name="SATURATION_AUDIT",
        )
        serialized = json.dumps(
            context,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        first = context["unresolved_question_state"][0]

        self.assertLess(len(serialized), 100_000)
        self.assertEqual(
            context["question_state_schema_version"],
            "e2r_saturation_audit_question_digest_v1",
        )
        self.assertNotIn("search_route_receipt_ids", first)
        self.assertNotIn("linked_route_receipt_ids", first)
        self.assertNotIn("route_progress_state", first)
        self.assertEqual(
            first["route_progress_summary"]["route_signature_count"],
            40,
        )
        self.assertEqual(
            len(first["route_progress_summary"]["route_progress_hash"]),
            64,
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

        recovered = _submitted_unsnapshotted_fresh_plan(
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

    def test_submitted_verifier_repair_is_visible_to_recovery_only_mode(self) -> None:
        scope = SimpleNamespace(job_id="PROJOB-REPAIR-RECOVERY")
        research_pass = SimpleNamespace(
            pass_id="PROPASS-REPAIR-RUNNING",
            pass_name="VERIFIER_REPAIR",
            submit_count=1,
            status="TRANSPORT_PENDING",
            prompt_hash="a" * 64,
        )
        ledger = SimpleNamespace(
            list_passes=lambda _job_id: (research_pass,),
            latest_dossier_snapshot_for_pass=lambda **_kwargs: None,
            get_scope=lambda _job_id: scope,
        )
        orchestrator = SimpleNamespace(ledger=ledger)

        recovered = _submitted_unsnapshotted_fresh_plan(
            orchestrator,
            job_id="PROJOB-REPAIR-RECOVERY",
        )

        self.assertIsNotNone(recovered)
        assert recovered is not None
        self.assertIs(recovered.scope, scope)
        self.assertIs(recovered.research_pass, research_pass)
        self.assertEqual(recovered.prompt_text, "")
        self.assertEqual(recovered.prompt_hash, "a" * 64)

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

    def test_operational_gap_budget_counts_every_submitted_attempt(self) -> None:
        rows = (
            SimpleNamespace(
                pass_name="INITIAL_FULL_RESEARCH",
                submit_count=1,
                status="COMPLETE",
                response_hash="a" * 64,
                detail={},
            ),
            SimpleNamespace(
                pass_name="PUBLIC_GAP_CLOSURE",
                submit_count=1,
                status="RESEARCH_RUNNING",
                response_hash=None,
                detail={},
            ),
            SimpleNamespace(
                pass_name="COUNTER_SUPERSESSION_CLOSURE",
                submit_count=0,
                status="PREPARED",
                response_hash=None,
                detail={},
            ),
        )
        ledger = SimpleNamespace(list_passes=lambda _job_id: rows)

        with self.assertRaises(LiveCanaryPending) as captured:
            _require_operational_followup_budget(
                ledger,
                job_id="PROJOB-EFFICIENCY",
                pass_names=frozenset(
                    {
                        "PUBLIC_GAP_CLOSURE",
                        "COUNTER_SUPERSESSION_CLOSURE",
                    }
                ),
                limit=1,
                label="public-gap/counter",
            )

        self.assertEqual(
            captured.exception.status,
            "OPERATIONAL_EFFICIENCY_GATE_FAILED",
        )

    def test_operational_gap_budget_ignores_unsubmitted_plan(self) -> None:
        ledger = SimpleNamespace(
            list_passes=lambda _job_id: (
                SimpleNamespace(
                    pass_name="PUBLIC_GAP_CLOSURE",
                    submit_count=0,
                    status="PREPARED",
                    response_hash=None,
                    detail={},
                ),
            )
        )

        _require_operational_followup_budget(
            ledger,
            job_id="PROJOB-EFFICIENCY",
            pass_names=frozenset({"PUBLIC_GAP_CLOSURE"}),
            limit=1,
            label="public-gap/counter",
        )

    def test_operational_gap_budget_allows_one_exact_unpersisted_replacement(self) -> None:
        sealed = SimpleNamespace(
            pass_name="PUBLIC_GAP_CLOSURE",
            submit_count=1,
            status="FAILED_HARD",
            response_hash=None,
            detail={
                "failure_domain": "TRANSPORT",
                "failure_class": (
                    "CHATGPT_SUBMITTED_TURN_NOT_SERVER_PERSISTED"
                ),
                "server_persistence_confirmed": False,
                "server_persistence_absence_confirmation_count": 2,
                "server_persistence_failure_evidence_hash": "a" * 64,
                "transport_failure_root_input_hash": "b" * 64,
                "replacement_pass_allowed": True,
            },
        )
        replacement = SimpleNamespace(
            pass_name="PUBLIC_GAP_CLOSURE",
            submit_count=1,
            status="RESEARCH_RUNNING",
            response_hash=None,
            detail={
                "supersedes_unpersisted_pass_id": "PROPASS-SEALED",
            },
        )

        _require_operational_followup_budget(
            SimpleNamespace(list_passes=lambda _job_id: (sealed,)),
            job_id="PROJOB-EFFICIENCY",
            pass_names=frozenset({"PUBLIC_GAP_CLOSURE"}),
            limit=1,
            label="public-gap/counter",
        )

        with self.assertRaises(LiveCanaryPending) as captured:
            _require_operational_followup_budget(
                SimpleNamespace(
                    list_passes=lambda _job_id: (sealed, replacement)
                ),
                job_id="PROJOB-EFFICIENCY",
                pass_names=frozenset({"PUBLIC_GAP_CLOSURE"}),
                limit=1,
                label="public-gap/counter",
            )

        self.assertEqual(
            captured.exception.status,
            "OPERATIONAL_EFFICIENCY_GATE_FAILED",
        )

    def test_repairable_linked_fact_is_repaired_before_question_research(self) -> None:
        dossier = {
            "question_family_results": [
                {
                    "question_family_id": "Q-REPAIR-FIRST",
                    "support_fact_ids": ["FACT-ACCEPTED"],
                    "counter_fact_ids": ["FACT-WRONG-SUBJECT"],
                    "resolution_fact_ids": [],
                },
                {
                    "question_family_id": "Q-REAL-PUBLIC-GAP",
                    "support_fact_ids": ["FACT-OTHER"],
                    "counter_fact_ids": [],
                    "resolution_fact_ids": [],
                },
            ]
        }
        classifications = (
            {
                "candidate_id": "FACT-WRONG-SUBJECT",
                "material": True,
                "send_to_pro_allowed": True,
                "routing": "COMPACT_PRO_REPAIR_ALLOWED",
            },
        )

        self.assertEqual(
            _question_ids_without_repairable_candidates(
                ("Q-REPAIR-FIRST", "Q-REAL-PUBLIC-GAP"),
                dossier=dossier,
                repairable_classifications=_repairable_classifications(
                    classifications
                ),
            ),
            ("Q-REAL-PUBLIC-GAP",),
        )

    def test_nonrepairable_rejection_does_not_hide_public_question(self) -> None:
        dossier = {
            "question_family_results": [
                {
                    "question_family_id": "Q-STILL-PUBLIC",
                    "support_fact_ids": ["FACT-LOCAL-ONLY"],
                    "counter_fact_ids": [],
                    "resolution_fact_ids": [],
                }
            ]
        }
        classifications = (
            {
                "candidate_id": "FACT-LOCAL-ONLY",
                "material": True,
                "send_to_pro_allowed": False,
            },
        )

        self.assertEqual(
            _question_ids_without_repairable_candidates(
                ("Q-STILL-PUBLIC",),
                dossier=dossier,
                repairable_classifications=_repairable_classifications(
                    classifications
                ),
            ),
            ("Q-STILL-PUBLIC",),
        )

    def test_verifier_pending_without_candidate_routes_to_public_followup(self) -> None:
        saturation = SimpleNamespace(
            missing_mandatory_question_ids=(),
            public_material_gap_question_ids=(),
            provider_parser_core_pending_question_ids=(),
            source_linkage_incomplete_question_ids=(),
            verifier_repair_pending_ids=("Q-FIXPOINT",),
            lifecycle_hard_break_pending_ids=(),
        )
        dossier = {
            "question_family_results": [
                {
                    "question_family_id": "Q-FIXPOINT",
                    "support_fact_ids": [],
                    "counter_fact_ids": [],
                    "resolution_fact_ids": [],
                }
            ]
        }

        public_ids = _public_followup_question_ids(saturation)

        self.assertEqual(public_ids, ("Q-FIXPOINT",))
        self.assertEqual(
            _question_ids_without_repairable_candidates(
                public_ids,
                dossier=dossier,
                repairable_classifications=(),
            ),
            ("Q-FIXPOINT",),
        )

    def test_new_normal_empty_route_is_fixpoint_input_not_semantic_hash(self) -> None:
        before = {"search_route_receipts": []}
        after = {
            "search_route_receipts": [
                {
                    "route_receipt_id": "ROUTE-FIXPOINT-ONE",
                    "question_family_id": "Q-FIXPOINT",
                    "query_text": "issuer official cancellation check",
                    "opened_source_urls": ["https://issuer.example/filing"],
                    "accepted_fact_ids": [],
                    "provider_status": "SUCCESS",
                    "parser_status": "SUCCESS",
                    "no_new_route_reason": "No current cancellation was found.",
                }
            ]
        }

        self.assertTrue(
            _new_no_new_route_confirmation_candidate(
                before,
                after,
                question_ids=("Q-FIXPOINT",),
            )
        )
        self.assertFalse(
            _new_no_new_route_confirmation_candidate(
                before,
                after,
                question_ids=("Q-OTHER",),
            )
        )
        after["search_route_receipts"][0]["no_new_route_reason"] = ""
        self.assertFalse(
            _new_no_new_route_confirmation_candidate(before, after)
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

    async def test_new_semantic_repair_context_reuses_same_conversation(self) -> None:
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
        second_plan, second_compiled = self.orchestrator.plan_compact_repair(
            self.built,
            dossier=dossier,
            rejection_classifications=second_classification,
            verification_rows=second_verification,
            job_root=job_root,
        )

        self.assertNotEqual(second_plan.research_pass.pass_id, plan.research_pass.pass_id)
        self.assertEqual(second_plan.research_pass.conversation_id, plan.research_pass.conversation_id)
        self.assertEqual(second_plan.research_pass.detail["repair_pass_ordinal"], 2)
        self.assertEqual(second_compiled.repair_pass_ordinal, 2)
        self.assertEqual(second_plan.research_pass.submit_count, 0)

    async def test_completed_exact_repair_context_stops_at_fixpoint(self) -> None:
        research_pass = SimpleNamespace(
            pass_id="PROPASS-COMPLETED-REPAIR",
            status="COMPLETE",
        )
        plan = SimpleNamespace(research_pass=research_pass)
        ledger = SimpleNamespace(
            latest_dossier_snapshot_for_pass=lambda **_kwargs: {
                "snapshot_hash": "a" * 64
            }
        )
        orchestrator = SimpleNamespace(
            ledger=ledger,
            plan_compact_repair=lambda *_args, **_kwargs: (
                plan,
                SimpleNamespace(repair_pass_ordinal=2),
            ),
        )
        runner = object.__new__(FreshV3FullThesisLiveRunner)

        with self.assertRaises(LiveCanaryPending) as captured:
            await runner._execute_compact_repair(
                prepared=SimpleNamespace(
                    job=SimpleNamespace(job_id="PROJOB-FIXPOINT")
                ),
                orchestrator=orchestrator,
                built=SimpleNamespace(),
                dossier_store=SimpleNamespace(),
                dossier={},
                job_root=self.root / "repair-fixpoint",
                verification_state=SimpleNamespace(
                    rejection_classifications=(),
                    verification_rows=(),
                ),
            )

        self.assertEqual(
            captured.exception.status,
            "VERIFIER_REPAIR_FIXPOINT_PENDING",
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
