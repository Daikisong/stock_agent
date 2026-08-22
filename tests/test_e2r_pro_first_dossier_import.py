from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.pro_first.browser.protocol import RawBrowserCapture
from e2r.pro_first.capture.atomic_capture import AtomicCaptureWriter, CaptureIdentity
from e2r.pro_first.capture.coordinator import CaptureFilesystemReconciler
from e2r.pro_first.dossier.importer import ProDossierImporter
from e2r.pro_first.dossier.parser import DossierParseError, ResearchDossierParser
from e2r.pro_first.dossier.validator import (
    CANONICAL_COMPONENT_IDS,
    DossierValidationError,
)
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow


class ProFirstDossierImportTest(unittest.IsolatedAsyncioTestCase):
    run_id = "PRORUN-dddddddddddddddddddddddd"
    target_id = "123456"
    as_of_date = "2026-08-22"
    packet_hash = "a" * 64
    prompt_hash = "b" * 64

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.now = datetime(2026, 8, 22, 3, 4, 5, tzinfo=timezone.utc)
        self.store = ProFirstJobStore(
            Path(self.temporary_directory.name) / "dossier.sqlite3",
            now=lambda: self.now,
        )
        candidate = self.store.create_candidate(
            symbol=self.target_id,
            company_name="검증기업",
            as_of_date=self.as_of_date,
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="dossier-trigger",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={"production_candidate": True},
        )
        self.job = self.store.create_job(candidate.candidate_id)
        self.job = self.store.transition(
            self.job.job_id,
            expected_version=self.job.state_version,
            to_status=JobStatus.PACKET_BUILDING,
            actor="test",
            idempotency_key="packet-building",
        )
        self.job = self.store.record_packet(
            self.job.job_id,
            expected_version=self.job.state_version,
            packet_id="PACKET-DOSSIER",
            packet_hash=self.packet_hash,
            manifest={"run_id": self.run_id},
            actor="test",
            idempotency_key="packet-ready",
        )
        self.job = self.store.transition(
            self.job.job_id,
            expected_version=self.job.state_version,
            to_status=JobStatus.BROWSER_PREPARING,
            actor="test",
            idempotency_key="browser-preparing",
        )
        self.job = self.store.record_browser_prepared(
            self.job.job_id,
            expected_version=self.job.state_version,
            browser_session_id="BROWSER-dossier",
            conversation_id="dossier-conversation",
            adapter_name="UnitAdapter",
            packet_hash=self.packet_hash,
            prompt_hash=self.prompt_hash,
            state={"state": "AWAITING_USER_APPROVAL"},
            actor="test",
            idempotency_key="browser-prepared",
        )
        self.job, nonce = self.store.issue_approval_nonce(
            self.job.job_id,
            expected_version=self.job.state_version,
            actor="test",
            idempotency_key="approval-issued",
            prompt_hash=self.prompt_hash,
            expires_at="2026-08-23T03:04:05Z",
        )
        self.job = self.store.consume_approval_nonce(
            self.job.job_id,
            nonce,
            expected_version=self.job.state_version,
            actor="user",
            idempotency_key="approval-consumed",
            prompt_hash=self.prompt_hash,
        )
        self.job = self.store.claim_submit(
            self.job.job_id,
            expected_version=self.job.state_version,
            actor="test",
            idempotency_key="submit",
        )
        self.job = self.store.transition(
            self.job.job_id,
            expected_version=self.job.state_version,
            to_status=JobStatus.RESEARCH_RUNNING,
            actor="test",
            idempotency_key="running",
        )
        self.job = self.store.transition(
            self.job.job_id,
            expected_version=self.job.state_version,
            to_status=JobStatus.RESULT_DETECTED,
            actor="test",
            idempotency_key="detected",
        )
        self.root = Path(self.temporary_directory.name) / "job-root"

    def _valid_dossier(self) -> dict:
        fact = {
            "dossier_fact_id": "PROFACT-001",
            "statement": "검증기업의 공식 수치가 개선됐다.",
            "direction": "POSITIVE",
            "subject": "검증기업",
            "target_id": self.target_id,
            "issuer_scoped": True,
            "business_segment": "핵심사업",
            "product_family": "주력제품",
            "economic_mechanism": "매출 증가가 현금흐름으로 전환",
            "predicate": "ISSUER_ACTUAL_IMPROVED",
            "value": 10,
            "unit": "%",
            "period": "2026Q2",
            "event_date": "2026-08-01",
            "current_status": "CURRENT",
            "candidate_components": ["eps_fcf_explosion", "earnings_visibility"],
            "source_url": "https://example.com/issuer-report",
            "source_title": "Issuer report",
            "source_publisher": "검증기업",
            "published_at": "2026-08-01",
            "supporting_excerpt": "공식 수치가 전년 대비 10% 개선됐다.",
            "confidence": 0.9,
        }
        return {
            "schema_version": "e2r_pro_research_dossier_v1",
            "job_id": self.job.job_id,
            "run_id": self.run_id,
            "target": {"target_id": self.target_id, "company_name": "검증기업"},
            "as_of_date": self.as_of_date,
            "research_status": "COMPLETE",
            "business_model": {"summary": "검증용 사업모델"},
            "candidate_archetypes": ["C06_HBM_MEMORY_CUSTOMER_CAPACITY"],
            "material_facts": [fact],
            "counterfacts": [],
            "component_research": {
                component: {"positive_fact_ids": [], "counterfact_ids": []}
                for component in CANONICAL_COMPONENT_IDS
            },
            "structured_metrics": {},
            "unresolved_gaps": [],
            "sources": [
                {
                    "source_id": "SOURCE-001",
                    "source_url": "https://example.com/issuer-report",
                    "source_title": "Issuer report",
                    "source_publisher": "검증기업",
                    "published_at": "2026-08-01",
                }
            ],
            "research_saturation": {"status": "SATURATED"},
            "proposed_score_ranges": {},
            "score_authority": False,
            "stage_authority": False,
        }

    async def _capture(self, dossier: dict, *, trailing_comma: bool = False) -> None:
        staging = self.root / "capture/.staging"
        staging.mkdir(parents=True, exist_ok=True)
        dossier_text = json.dumps(dossier, ensure_ascii=False, indent=2)
        if trailing_comma:
            dossier_text = dossier_text[:-2] + ",\n}"
        report = (
            "# Pro report\n"
            f"[[E2R_PRO_RUN_ID:{self.run_id}]]\n"
            f"[[E2R_PRO_JOB_ID:{self.job.job_id}]]\n"
            "E2R_RESEARCH_DOSSIER_JSON_BEGIN\n```json\n"
            f"{dossier_text}\n"
            "```\nE2R_RESEARCH_DOSSIER_JSON_END\n"
        )
        part = staging / "pro_report.md.part"
        part.write_text(report, encoding="utf-8")
        AtomicCaptureWriter(now=lambda: self.now).finalize(
            self.root,
            identity=CaptureIdentity(
                job_id=self.job.job_id,
                run_id=self.run_id,
                target_id=self.target_id,
                as_of_date=self.as_of_date,
                packet_hash=self.packet_hash,
                prompt_hash=self.prompt_hash,
                conversation_id="dossier-conversation",
                capture_mode="UNIT_CAPTURE",
            ),
            raw_capture=RawBrowserCapture(
                conversation_id="dossier-conversation",
                assistant_turn_id="assistant-turn-1",
                report_md_part_path=part,
                source="DIRECT_REPORT_DOM",
                downloaded_filename=None,
                attachment_key=None,
            ),
        )
        await CaptureFilesystemReconciler(self.store).reconcile(self.root)
        self.job = self.store.get_job(self.job.job_id)
        self.assertEqual(self.job.status, JobStatus.CAPTURE_COMPLETE.value)

    async def test_strict_dossier_import_success_and_duplicate_event_noop(self) -> None:
        await self._capture(self._valid_dossier())
        importer = ProDossierImporter(self.store, now=lambda: self.now)
        first = importer.import_job(self.job.job_id, job_root=self.root)
        second = importer.import_job(self.job.job_id, job_root=self.root)
        self.assertEqual(first.job.status, JobStatus.DOSSIER_IMPORTED.value)
        self.assertEqual(first.job.dossier_id, second.job.dossier_id)
        self.assertEqual(first.import_receipt["fact_count"], 1)
        self.assertEqual(first.import_receipt["evidence_promoted_count"], 0)
        self.assertFalse(first.import_receipt["score_authority"])
        self.assertIn("REMOVE_JSON_CODE_FENCE", first.import_receipt["repair_operations"])
        self.assertNotEqual(
            first.import_receipt["parser_before_hash"],
            first.import_receipt["parser_after_hash"],
        )
        matching = [
            event
            for event in self.store.list_events(self.job.job_id)
            if event.to_status == JobStatus.DOSSIER_IMPORTED.value
        ]
        self.assertEqual(len(matching), 1)

    async def test_target_mismatch_rejected(self) -> None:
        dossier = self._valid_dossier()
        dossier["target"]["target_id"] = "999999"
        dossier["material_facts"][0]["target_id"] = "999999"
        await self._capture(dossier)
        with self.assertRaisesRegex(DossierValidationError, "target mismatch"):
            ProDossierImporter(self.store, now=lambda: self.now).import_job(
                self.job.job_id, job_root=self.root
            )
        failed = self.store.get_job(self.job.job_id)
        self.assertEqual(failed.status, JobStatus.USER_ATTENTION_REQUIRED.value)
        self.assertEqual(failed.last_error_class, "DOSSIER_INVALID")

    async def test_as_of_mismatch_rejected(self) -> None:
        dossier = self._valid_dossier()
        dossier["as_of_date"] = "2026-08-21"
        await self._capture(dossier)
        with self.assertRaisesRegex(DossierValidationError, "as_of_date mismatch"):
            ProDossierImporter(self.store, now=lambda: self.now).import_job(
                self.job.job_id, job_root=self.root
            )

    async def test_run_id_mismatch_rejected(self) -> None:
        dossier = self._valid_dossier()
        dossier["run_id"] = "PRORUN-other"
        await self._capture(dossier)
        with self.assertRaisesRegex(DossierValidationError, "run_id mismatch"):
            ProDossierImporter(self.store, now=lambda: self.now).import_job(
                self.job.job_id, job_root=self.root
            )

    async def test_duplicate_fact_ids_rejected(self) -> None:
        dossier = self._valid_dossier()
        dossier["counterfacts"] = [deepcopy(dossier["material_facts"][0])]
        await self._capture(dossier)
        with self.assertRaisesRegex(DossierValidationError, "duplicate dossier fact ids"):
            ProDossierImporter(self.store, now=lambda: self.now).import_job(
                self.job.job_id, job_root=self.root
            )

    async def test_authority_or_component_roster_violation_rejected(self) -> None:
        dossier = self._valid_dossier()
        dossier["score_authority"] = True
        dossier["component_research"].pop("capital_allocation")
        await self._capture(dossier)
        with self.assertRaises(DossierValidationError):
            ProDossierImporter(self.store, now=lambda: self.now).import_job(
                self.job.job_id, job_root=self.root
            )

    async def test_invalid_source_url_rejected(self) -> None:
        dossier = self._valid_dossier()
        dossier["material_facts"][0]["source_url"] = "file:///tmp/secret"
        await self._capture(dossier)
        with self.assertRaises(DossierValidationError):
            ProDossierImporter(self.store, now=lambda: self.now).import_job(
                self.job.job_id, job_root=self.root
            )

    async def test_repair_cannot_create_new_fact(self) -> None:
        dossier = self._valid_dossier()
        await self._capture(dossier, trailing_comma=True)
        result = ProDossierImporter(self.store, now=lambda: self.now).import_job(
            self.job.job_id, job_root=self.root
        )
        self.assertEqual(result.import_receipt["fact_ids"], ["PROFACT-001"])
        self.assertIn("REMOVE_TRAILING_COMMAS:1", result.import_receipt["repair_operations"])
        self.assertEqual(len(result.normalized_dossier["material_facts"]), 1)

    def test_json_sentinel_parse(self) -> None:
        payload = self._valid_dossier()
        text = (
            "report\nE2R_RESEARCH_DOSSIER_JSON_BEGIN\n```json\n"
            + json.dumps(payload, ensure_ascii=False)
            + "\n```\nE2R_RESEARCH_DOSSIER_JSON_END"
        )
        parsed = ResearchDossierParser().parse_text(text, parser_source="MD_SENTINEL")
        self.assertEqual(parsed.payload["job_id"], self.job.job_id)
        self.assertEqual(
            parsed.repair_operations,
            ("EXTRACT_DOSSIER_SENTINEL_BLOCK", "REMOVE_JSON_CODE_FENCE"),
        )

    def test_parser_prefers_downloaded_json_then_falls_back_to_md(self) -> None:
        payload = self._valid_dossier()
        downloaded = Path(self.temporary_directory.name) / "downloaded.json"
        markdown = Path(self.temporary_directory.name) / "report.md"
        downloaded.write_text(json.dumps(payload), encoding="utf-8")
        markdown.write_text(
            f"{BEGIN}\n{json.dumps({**payload, 'job_id': 'PROJOB-md'})}\n{END}",
            encoding="utf-8",
        )
        parser = ResearchDossierParser()
        first = parser.parse(downloaded_json_path=downloaded, report_md_path=markdown)
        self.assertEqual(first.parser_source, "DOWNLOADED_JSON")
        self.assertEqual(first.payload["job_id"], self.job.job_id)
        downloaded.write_text("{invalid", encoding="utf-8")
        fallback = parser.parse(downloaded_json_path=downloaded, report_md_path=markdown)
        self.assertEqual(fallback.parser_source, "MD_SENTINEL")
        self.assertEqual(fallback.payload["job_id"], "PROJOB-md")

    def test_multiple_sentinel_blocks_rejected(self) -> None:
        text = f"{BEGIN}\n{{}}\n{END}\n{BEGIN}\n{{}}\n{END}"
        with self.assertRaisesRegex(DossierParseError, "exactly once"):
            ResearchDossierParser().parse_text(text, parser_source="MD_SENTINEL")


BEGIN = "E2R_RESEARCH_DOSSIER_JSON_BEGIN"
END = "E2R_RESEARCH_DOSSIER_JSON_END"


if __name__ == "__main__":
    unittest.main()
