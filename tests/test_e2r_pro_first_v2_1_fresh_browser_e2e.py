from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from urllib.parse import urlencode

from e2r.pro_first.approval import ProApprovalService
from e2r.pro_first.browser.chatgpt_adapter import PlaywrightChatGPTWebAdapter
from e2r.pro_first.browser.mock_chatgpt_app import MockChatGPTServer
from e2r.pro_first.browser.protocol import BrowserCaptureRequest
from e2r.pro_first.capture.atomic_capture import AtomicCaptureWriter, CaptureIdentity
from e2r.pro_first.fresh_session import (
    FreshSessionBoundaryService,
    FreshSessionOrchestratorV3,
    OldAnswerLeakageManifest,
)
from e2r.pro_first.fresh_session.full_thesis_live_v3 import (
    _finalize_compact_repair_capture,
)
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.preflight import LocalEvidencePreflightService


ARCHETYPE = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
OLD_RUN = "PRORUN-a7dacadb7088fc23535bfdde"
OLD_CONVERSATION = "6a8b09c3-bfcc-83ee-b15b-9f76eca52249"


class ProFirstV21FreshBrowserE2ETest(unittest.IsolatedAsyncioTestCase):
    now = datetime(2026, 8, 25, 2, 3, 4, tzinfo=timezone.utc)

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        self.store = ProFirstJobStore(
            self.root / "fresh-browser.sqlite3",
            now=lambda: self.now,
        )
        old = self._old_job()
        old = self.store.freeze_old_diagnostic_job(
            old.job_id,
            expected_version=old.state_version,
            actor="test",
            idempotency_key="fresh-browser-freeze-old",
        )
        manifest = OldAnswerLeakageManifest(
            old_job_id=old.job_id,
            old_run_id=OLD_RUN,
            old_conversation_id=OLD_CONVERSATION,
            old_fact_ids=("PROFACT-OLD-BROWSER-ANSWER",),
            old_route_receipt_ids=("PROROUTE-OLD-BROWSER-ANSWER",),
            old_research_pass_ids=("PROPASS-OLD-BROWSER-ANSWER",),
            old_score_values=("70.2",),
            old_stage_values=("Stage 2 FINAL",),
        )
        boundary, _fresh = FreshSessionBoundaryService(self.store).start(
            old_job_id=old.job_id,
            old_run_id=OLD_RUN,
            old_conversation_id=OLD_CONVERSATION,
            fresh_session_id="FRESH-BROWSER-E2E-ONE",
            old_runtime_root=self.root / "old-runtime",
            fresh_runtime_root=self.root / "fresh-runtime",
            archetype_ids=(ARCHETYPE,),
            leakage_manifest=manifest,
        )
        self.boundary = boundary
        self.orchestrator = FreshSessionOrchestratorV3(self.store, boundary)
        self.built = self.orchestrator.build_initial_packet(
            commit_sha="a" * 40,
            config_hash="b" * 64,
        )
        self.server = MockChatGPTServer()
        self.server.__enter__()
        self.addCleanup(self.server.__exit__, None, None, None)

    async def asyncSetUp(self) -> None:
        from playwright.async_api import async_playwright

        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.page = await self.browser.new_page(accept_downloads=True)

    async def asyncTearDown(self) -> None:
        await self.browser.close()
        await self.playwright.stop()

    async def test_frozen_old_to_v3_initial_preflight_repair_and_saturation(self) -> None:
        query = urlencode(
            {
                "job_id": self.built.job.job_id,
                "run_id": self.built.packet_payload["run_id"],
                "target_id": self.built.job.symbol,
                "as_of_date": self.built.job.as_of_date,
                "filename": self.built.output_filename,
            }
        )
        await self.page.goto(
            f"{self.server.base_url}/?{query}",
            wait_until="domcontentloaded",
        )
        adapter = PlaywrightChatGPTWebAdapter(self.page)
        prepared = await self.orchestrator.prepare_initial_with_adapter(
            self.built,
            adapter,
            browser_session_id="BROWSER-FRESH-PRODUCTION-ADAPTER",
        )
        self.assertIsNone(prepared.prepared.conversation_id)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

        approval = ProApprovalService(self.store, now=lambda: self.now)
        grant = approval.issue(
            self.built.job.job_id,
            prompt_hash=self.built.prompt.prompt_hash,
        )
        approval.approve(grant)
        submitted = await self.orchestrator.submit_initial_once(adapter)
        conversation_id = submitted.submit_result.job.conversation_id
        self.assertIsNotNone(conversation_id)
        self.assertNotEqual(conversation_id, OLD_CONVERSATION)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 1)

        initial_report = self._dossier_report(
            pass_id=self.built.initial_pass_id,
            parent_pass_id="NONE",
            research_status="NEEDS_VERIFIER_REPAIR",
        )
        await self._show_report(initial_report)
        initial_result = await adapter.inspect_result(
            job_id=self.built.job.job_id,
            run_id=self.built.packet_payload["run_id"],
        )
        self.assertTrue(initial_result.structurally_complete)
        self.assertTrue(initial_result.has_dossier_marker)
        scope = self.orchestrator.establish_followup_scope(
            self.built,
            initial_response_hash=initial_result.report_hash,
        )
        self.assertEqual(scope.conversation_id, conversation_id)

        preflight_dossier = self._empty_initial_dossier(
            conversation_id=conversation_id,
        )
        preflight = LocalEvidencePreflightService().run(
            dossier=preflight_dossier,
            target_id=self.built.job.symbol,
            company_name=self.built.job.company_name,
            target_aliases=(self.built.job.company_name,),
            as_of_date=self.built.job.as_of_date,
            archetype_ids=self.built.job.archetype_ids,
            job_root=self.boundary.fresh_job_root,
        )
        self.assertTrue(preflight.applicable)
        self.assertEqual(preflight.receipt["local_normalizable_sent_to_pro_count"], 0)
        self.assertEqual(
            preflight.receipt["source_representation_sent_to_pro_count"],
            0,
        )

        dossier, classifications, verifications = self._repair_inputs(
            conversation_id=conversation_id,
        )
        repair_plan, repair_prompt = self.orchestrator.plan_compact_repair(
            self.built,
            dossier=dossier,
            rejection_classifications=classifications,
            verification_rows=verifications,
            job_root=self.boundary.fresh_job_root,
        )
        await self.orchestrator.prepare_followup(repair_plan, adapter)
        await self.orchestrator.submit_followup(repair_plan, adapter)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 2)
        repair_report = self._repair_report(
            pass_id=repair_plan.research_pass.pass_id,
            parent_pass_id=repair_plan.research_pass.parent_pass_id or "",
        )
        await self._show_report(repair_report)
        repair_result = await adapter.inspect_result(
            job_id=self.built.job.job_id,
            run_id=self.built.packet_payload["run_id"],
        )
        self.assertTrue(repair_result.structurally_complete)
        self.assertTrue(repair_result.has_repair_delta_marker)
        repair_pass_root = self.root / "repair-pass"
        capture = await adapter.capture_result(
            BrowserCaptureRequest(
                job_id=self.built.job.job_id,
                run_id=self.built.packet_payload["run_id"],
                expected_filename="compact_repair_delta.md",
                expected_report_hash=repair_result.report_hash,
                staging_directory=repair_pass_root / "capture/.staging",
            )
        )
        self.assertEqual(capture.source, "DIRECT_REPORT_DOM_NORMALIZED")
        self.assertIn(
            "APPEND_VISIBLE_CITATION_HREF_REGISTRY",
            capture.transport_normalization_operations,
        )
        self.assertIn(
            "E2R_REPAIR_DELTA_JSON_BEGIN",
            capture.report_md_part_path.read_text(encoding="utf-8"),
        )
        capture_receipt = _finalize_compact_repair_capture(
            pass_root=repair_pass_root,
            raw_capture=capture,
            identity=CaptureIdentity(
                job_id=self.built.job.job_id,
                run_id=self.built.packet_payload["run_id"],
                target_id=self.built.job.symbol,
                as_of_date=self.built.job.as_of_date,
                packet_hash=str(self.built.job.packet_hash or ""),
                prompt_hash=repair_plan.prompt_hash,
                conversation_id=conversation_id,
                capture_mode="FRESH_V3_REPAIR_E2E",
            ),
            job_id=self.built.job.job_id,
            run_id=self.built.packet_payload["run_id"],
            pass_id=repair_plan.research_pass.pass_id,
            parent_pass_id=repair_plan.research_pass.parent_pass_id or "",
            writer=AtomicCaptureWriter(now=lambda: self.now),
        )
        persisted_repair = json.loads(
            (repair_pass_root / capture_receipt.dossier_json_path).read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(
            persisted_repair["schema_version"],
            "e2r_pro_repair_delta_v3",
        )
        self.assertEqual(
            persisted_repair["research_pass_id"],
            repair_plan.research_pass.pass_id,
        )
        self.orchestrator.complete_followup(
            repair_plan.research_pass.pass_id,
            response_hash=repair_result.report_hash,
            conversation_id=conversation_id,
        )

        saturation_plan, _compiled = self.orchestrator.plan_v3_followup(
            self.built,
            pass_name="SATURATION_AUDIT",
            latest_dossier_digest={
                "dossier_hash": "f" * 64,
                "mandatory_question_nonterminal_count": 0,
                "public_searchable_material_gap_count": 0,
                "verifier_repair_pending_count": 0,
                "accepted_fact_ids": ["FACT-REPLACEMENT"],
            },
            pass_inputs={
                "preflight_complete": True,
                "repair_pass_count": 1,
            },
        )
        await self.orchestrator.prepare_followup(saturation_plan, adapter)
        await self.orchestrator.submit_followup(saturation_plan, adapter)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 3)
        saturation_report = self._dossier_report(
            pass_id=saturation_plan.research_pass.pass_id,
            parent_pass_id=saturation_plan.research_pass.parent_pass_id or "",
            research_status="COMPLETE",
        )
        await self._show_report(saturation_report)
        saturation_result = await adapter.inspect_result(
            job_id=self.built.job.job_id,
            run_id=self.built.packet_payload["run_id"],
        )
        self.assertTrue(saturation_result.structurally_complete)
        self.orchestrator.complete_followup(
            saturation_plan.research_pass.pass_id,
            response_hash=saturation_result.report_hash,
            conversation_id=conversation_id,
        )

        passes = self.orchestrator.ledger.list_passes(self.built.job.job_id)
        self.assertEqual(
            [row.pass_name for row in passes],
            ["INITIAL_FULL_RESEARCH", "VERIFIER_REPAIR", "SATURATION_AUDIT"],
        )
        self.assertTrue(all(row.submit_count == 1 for row in passes))
        self.assertTrue(all(row.conversation_id == conversation_id for row in passes))
        self.assertIsNotNone(
            self.store.get_job(self.boundary.old_job_id).old_job_frozen_at
        )

    async def test_intact_prepared_draft_is_recovered_without_second_upload(self) -> None:
        query = urlencode(
            {
                "job_id": self.built.job.job_id,
                "run_id": self.built.packet_payload["run_id"],
                "target_id": self.built.job.symbol,
                "as_of_date": self.built.job.as_of_date,
                "filename": self.built.output_filename,
            }
        )
        await self.page.goto(
            f"{self.server.base_url}/?{query}",
            wait_until="domcontentloaded",
        )
        original = PlaywrightChatGPTWebAdapter(self.page)
        prepared = await original.prepare_without_submit(
            browser_session_id="BROWSER-ORIGINAL-DRAFT",
            packet_path=self.built.packet_bundle.research_packet_json,
            packet_hash=self.built.packet_bundle.packet_hash,
            prompt=self.built.prompt.prompt_text,
            prompt_hash=self.built.prompt.prompt_hash,
        )
        selected_before = await self.page.locator('input[type="file"]').first.evaluate(
            "input => Array.from(input.files || []).map(file => file.name)"
        )
        await self.page.evaluate(
            "document.querySelector('#attachments').replaceChildren()"
        )
        recovered = await PlaywrightChatGPTWebAdapter(
            self.page
        ).recover_initial_prepared_without_mutation(
            browser_session_id="BROWSER-RECOVERED-DRAFT",
            packet_path=self.built.packet_bundle.research_packet_json,
            packet_hash=self.built.packet_bundle.packet_hash,
            prompt=self.built.prompt.prompt_text,
            prompt_hash=self.built.prompt.prompt_hash,
        )
        selected_after = await self.page.locator('input[type="file"]').first.evaluate(
            "input => Array.from(input.files || []).map(file => file.name)"
        )
        self.assertEqual(selected_before, selected_after)
        self.assertEqual(recovered.uploaded_filename, prepared.uploaded_filename)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

    async def _show_report(self, report: str) -> None:
        await self.page.evaluate(
            """({report, context}) => {
                window.__setSuppliedReport(report);
                window.__setMockState('COMPLETE_WITH_DIRECT_REPORT', context);
            }""",
            {
                "report": report,
                "context": {
                    "job_id": self.built.job.job_id,
                    "run_id": self.built.packet_payload["run_id"],
                    "target_id": self.built.job.symbol,
                    "as_of_date": self.built.job.as_of_date,
                    "filename": self.built.output_filename,
                },
            },
        )

    def _dossier_report(
        self,
        *,
        pass_id: str,
        parent_pass_id: str,
        research_status: str,
    ) -> str:
        dossier = self._empty_initial_dossier(
            conversation_id="PENDING_OR_CURRENT",
        )
        dossier.update(
            {
                "research_pass_id": pass_id,
                "parent_pass_id": None if parent_pass_id == "NONE" else parent_pass_id,
                "research_status": research_status,
            }
        )
        return "\n".join(
            (
                f"[[E2R_PRO_RUN_ID:{self.built.packet_payload['run_id']}]]",
                f"[[E2R_PRO_JOB_ID:{self.built.job.job_id}]]",
                f"[[E2R_PRO_PASS_ID:{pass_id}]]",
                f"[[E2R_PRO_PARENT_PASS_ID:{parent_pass_id}]]",
                "E2R_RESEARCH_DOSSIER_JSON_BEGIN",
                "```json",
                json.dumps(dossier, ensure_ascii=False, sort_keys=True),
                "```",
                "E2R_RESEARCH_DOSSIER_JSON_END",
            )
        )

    def _repair_report(self, *, pass_id: str, parent_pass_id: str) -> str:
        delta = {
            "schema_version": "e2r_pro_repair_delta_v3",
            "job_id": self.built.job.job_id,
            "run_id": self.built.packet_payload["run_id"],
            "research_pass_id": pass_id,
            "parent_pass_id": parent_pass_id,
            "target": {
                "target_id": self.built.job.symbol,
                "symbol": self.built.job.symbol,
                "company_name": self.built.job.company_name,
            },
            "as_of_date": self.built.job.as_of_date,
            "repair_actions": [
                {
                    "candidate_id": "FACT-BROWSER-DEFECT",
                    "question_family_ids": [
                        "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01"
                    ],
                    "rejection_category": "GENUINE_SEMANTIC_OR_SOURCE_DEFECT",
                    "original_statement": "과장된 statement",
                    "source_document_id": "SRC-BROWSER",
                    "canonical_url": "https://example.com/hbm",
                    "fetched_excerpt": "HBM 조건을 설명했다.",
                    "allowed_action": "CORRECT|REPLACE|NARROW|WITHDRAW",
                    "action": "WITHDRAW",
                    "replacement_source_document": None,
                    "replacement_fact": None,
                    "reason": "원문이 수치를 직접 지지하지 않는다.",
                }
            ],
            "new_source_documents": [],
            "new_route_receipts": [],
            "score_authority": False,
            "stage_authority": False,
        }
        return "\n".join(
            (
                f"[[E2R_PRO_RUN_ID:{self.built.packet_payload['run_id']}]]",
                f"[[E2R_PRO_JOB_ID:{self.built.job.job_id}]]",
                f"[[E2R_PRO_PASS_ID:{pass_id}]]",
                f"[[E2R_PRO_PARENT_PASS_ID:{parent_pass_id}]]",
                "E2R_REPAIR_DELTA_JSON_BEGIN",
                "```json",
                json.dumps(delta, ensure_ascii=False, sort_keys=True),
                "```",
                "E2R_REPAIR_DELTA_JSON_END",
            )
        )

    def _empty_initial_dossier(self, *, conversation_id: str) -> dict:
        return {
            "schema_version": "e2r_pro_research_dossier_v3",
            "job_id": self.built.job.job_id,
            "run_id": self.built.packet_payload["run_id"],
            "conversation_id": conversation_id,
            "research_pass_id": self.built.initial_pass_id,
            "parent_pass_id": None,
            "target": {
                "target_id": self.built.job.symbol,
                "symbol": self.built.job.symbol,
                "company_name": self.built.job.company_name,
                "aliases": [self.built.job.company_name],
            },
            "as_of_date": self.built.job.as_of_date,
            "candidate_archetypes": [ARCHETYPE],
            "selected_archetypes": [ARCHETYPE],
            "research_status": "NEEDS_VERIFIER_REPAIR",
            "business_model": {},
            "source_documents": [],
            "material_facts": [],
            "counterfacts": [],
            "resolution_facts": [],
            "derived_metrics": [],
            "question_family_results": [],
            "source_lineages": [],
            "search_route_receipts": [],
            "unresolved_gaps": [],
            "research_saturation": {},
            "score_authority": False,
            "stage_authority": False,
        }

    def _repair_inputs(self, *, conversation_id: str):
        document = (
            "SK하이닉스 공식 보고서. HBM 조건을 설명했다. 검증 가능한 충분한 "
            "본문 길이를 갖는 테스트 source representation이다."
        )
        path = self.boundary.fresh_job_root / "verification/source_pages/browser.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(document, encoding="utf-8")
        dossier = self._empty_initial_dossier(conversation_id=conversation_id)
        dossier["source_documents"] = [
            {
                "source_document_id": "SRC-BROWSER",
                "canonical_url": "https://example.com/hbm",
            }
        ]
        dossier["material_facts"] = [
            {
                "dossier_fact_id": "FACT-BROWSER-DEFECT",
                "statement": "HBM 가격이 99% 올랐다.",
                "source_document_id": "SRC-BROWSER",
                "question_family_ids": [
                    "C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q01"
                ],
                "supporting_excerpt": "HBM 조건을 설명했다.",
            }
        ]
        classifications = [
            {
                "candidate_id": "FACT-BROWSER-DEFECT",
                "cause_class": "GENUINE_SEMANTIC_OR_SOURCE_DEFECT",
                "cause_code": "STATEMENT_BROADER_THAN_EXCERPT",
                "verifier_status": "REJECTED_QUOTE_MISMATCH",
                "detail": "literal support mismatch",
                "material": True,
                "send_to_pro_allowed": True,
            }
        ]
        verifications = [
            {
                "dossier_fact_id": "FACT-BROWSER-DEFECT",
                "status": "REJECTED_QUOTE_MISMATCH",
                "reason": "literal support mismatch",
                "document_path": str(path.relative_to(self.boundary.fresh_job_root)),
                "content_hash": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        ]
        return dossier, classifications, verifications

    def _old_job(self):
        candidate = self.store.create_candidate(
            symbol="000660",
            company_name="SK하이닉스",
            as_of_date="2026-08-23",
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="old-browser-diagnostic",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={"production_candidate": True},
        )
        job = self.store.create_job(candidate.candidate_id, archetype_ids=(ARCHETYPE,))
        job = self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.PACKET_BUILDING,
            actor="test",
            idempotency_key="old-browser-packet-building",
        )
        job = self.store.record_packet(
            job.job_id,
            expected_version=job.state_version,
            packet_id="PROPACKET-OLD-BROWSER",
            packet_hash="a" * 64,
            manifest={"packet_hash": "a" * 64},
            actor="test",
            idempotency_key="old-browser-packet-ready",
        )
        job = self.store.transition(
            job.job_id,
            expected_version=job.state_version,
            to_status=JobStatus.BROWSER_PREPARING,
            actor="test",
            idempotency_key="old-browser-preparing",
        )
        return self.store.record_browser_prepared(
            job.job_id,
            expected_version=job.state_version,
            browser_session_id="BROWSER-OLD",
            conversation_id=OLD_CONVERSATION,
            adapter_name="OldBrowserAdapter",
            packet_hash="a" * 64,
            prompt_hash="b" * 64,
            state={"state": "AWAITING_USER_APPROVAL"},
            actor="test",
            idempotency_key="old-browser-prepared",
        )


if __name__ == "__main__":
    unittest.main()
