from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.pro_first.browser.protocol import (
    AttachmentKey,
    RawBrowserJsonAttachment,
)
from e2r.pro_first.capture.expanded_dossier import (
    EXPANDED_READY_PATH,
    ExpandedDossierArtifactService,
    expanded_dossier_recovery_required,
    resolve_import_dossier_path,
    verify_expanded_dossier_bundle,
)
from e2r.pro_first.capture.receipt import CaptureReceipt, file_sha256
from e2r.pro_first.ids import canonical_json


class _JsonAttachmentAdapter:
    def __init__(self, payload, *, wrong_turn: bool = False) -> None:
        self.payload = payload
        self.wrong_turn = wrong_turn
        self.calls = 0

    async def download_json_attachment_without_submit(self, request):
        self.calls += 1
        request.staging_directory.mkdir(parents=True, exist_ok=True)
        path = request.staging_directory / "expanded_research_dossier.json.part"
        path.write_text(canonical_json(self.payload) + "\n", encoding="utf-8")
        turn_id = "assistant-other" if self.wrong_turn else request.assistant_turn_id
        key = AttachmentKey(
            request.conversation_id,
            turn_id,
            request.expected_filename,
        )
        return RawBrowserJsonAttachment(
            conversation_id=request.conversation_id,
            assistant_turn_id=turn_id,
            json_part_path=path,
            downloaded_filename=request.expected_filename,
            attachment_key=key,
        )


class ExpandedDossierCaptureTest(unittest.IsolatedAsyncioTestCase):
    job_id = "PROJOB-expanded-test"
    run_id = "PRORUN-expanded-test"
    conversation_id = "conversation-expanded-test"
    assistant_turn_id = "assistant-expanded-test"
    target_id = "123456"
    as_of_date = "2026-08-23"
    pass_id = "PROPASS-expanded-test"
    filename = "ResearchDossierV3_generic_123456_asof_2026-08-23.json"

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        incoming = self.root / "capture/incoming"
        incoming.mkdir(parents=True)
        self.inline = self._inline_manifest()
        self.full = self._full_dossier()
        (incoming / "pro_report.md").write_text(
            "same-turn visible report\n",
            encoding="utf-8",
        )
        (incoming / "research_dossier.json").write_text(
            canonical_json(self.inline) + "\n",
            encoding="utf-8",
        )
        self.receipt = CaptureReceipt(
            schema_version="e2r_pro_capture_receipt_v1",
            event_type="PRO_RESEARCH_CAPTURE_COMPLETE",
            job_id=self.job_id,
            run_id=self.run_id,
            target_id=self.target_id,
            as_of_date=self.as_of_date,
            packet_hash="a" * 64,
            prompt_hash="b" * 64,
            conversation_id=self.conversation_id,
            assistant_turn_id=self.assistant_turn_id,
            report_md_hash=file_sha256(incoming / "pro_report.md"),
            report_pdf_hash=None,
            dossier_json_hash=file_sha256(incoming / "research_dossier.json"),
            submit_count=1,
            capture_count=1,
            captured_at="2026-08-26T01:02:03Z",
            capture_mode="TEST_VISIBLE_BROWSER",
            capture_source="DIRECT_REPORT_DOM",
            optional_pdf_error=None,
        )

    def _identity(self):
        return {
            "schema_version": "e2r_pro_research_dossier_v3",
            "job_id": self.job_id,
            "run_id": self.run_id,
            "conversation_id": "PENDING_NEW_CONVERSATION",
            "research_pass_id": self.pass_id,
            "parent_pass_id": "NONE",
            "target": {"target_id": self.target_id},
            "as_of_date": self.as_of_date,
            "score_authority": False,
            "stage_authority": False,
        }

    def _inline_manifest(self):
        return {
            **self._identity(),
            "business_model": {
                "expanded_dossier_artifact": f"sandbox:/mnt/data/{self.filename}"
            },
            "source_documents": [],
            "material_facts": [],
            "counterfacts": [],
            "resolution_facts": [],
            "derived_metrics": [],
            "question_family_results": [],
            "search_route_receipts": [],
            "unresolved_gaps": [],
            "research_saturation": {
                "inline_transport_manifest": True,
                "expanded_artifact_required_for_verification": True,
                "expanded_dossier_schema_error_count": 0,
                "expanded_source_document_count": 1,
                "expanded_accepted_fact_count": 3,
                "expanded_derived_metric_count": 1,
                "expanded_question_family_count": 1,
                "expanded_search_route_receipt_count": 1,
                "expanded_unresolved_gap_count": 1,
                "expanded_post_cutoff_source_count": 0,
                "expanded_duplicate_lineage_credit_count": 0,
            },
        }

    def _full_dossier(self):
        return {
            **self._identity(),
            "business_model": {},
            "source_documents": [{"source_document_id": "SRC-1"}],
            "material_facts": [{"dossier_fact_id": "FACT-M-1"}],
            "counterfacts": [{"dossier_fact_id": "FACT-C-1"}],
            "resolution_facts": [{"dossier_fact_id": "FACT-R-1"}],
            "derived_metrics": [{"derived_metric_id": "METRIC-1"}],
            "question_family_results": [{"question_family_id": "Q-1"}],
            "search_route_receipts": [{"route_receipt_id": "ROUTE-1"}],
            "unresolved_gaps": [{"gap_id": "GAP-1"}],
            "research_saturation": {
                "source_document_count": 1,
                "accepted_fact_count": 3,
                "search_route_receipt_count": 1,
                "unresolved_gap_count": 1,
                "post_cutoff_source_count": 0,
                "duplicate_lineage_credit_count": 0,
                "schema_validation": {
                    "schema_error_count": 0,
                    "json_roundtrip_equal": True,
                },
            },
        }

    def test_manifest_cannot_be_imported_as_zero_fact_dossier(self) -> None:
        self.assertTrue(
            expanded_dossier_recovery_required(self.root, self.receipt)
        )
        with self.assertRaisesRegex(FileNotFoundError, "READY"):
            resolve_import_dossier_path(self.root, self.receipt)

    async def test_same_turn_json_is_separately_sealed_and_idempotent(self) -> None:
        adapter = _JsonAttachmentAdapter(self.full)
        original_report_hash = file_sha256(
            self.root / self.receipt.report_md_path
        )
        original_inline_hash = file_sha256(
            self.root / self.receipt.dossier_json_path
        )
        service = ExpandedDossierArtifactService(
            now=lambda: datetime(2026, 8, 26, 2, 3, 4, tzinfo=timezone.utc)
        )

        first = await service.recover(
            job_root=self.root,
            capture_receipt=self.receipt,
            adapter=adapter,
        )
        self.assertIsNotNone(first)
        self.assertEqual(adapter.calls, 1)
        self.assertEqual(first.receipt["browser_submit_delta"], 0)  # type: ignore[union-attr]
        self.assertEqual(
            first.receipt["expanded_counts"]["expanded_accepted_fact_count"],  # type: ignore[union-attr]
            3,
        )
        self.assertEqual(
            resolve_import_dossier_path(self.root, self.receipt),
            first.dossier_path,  # type: ignore[union-attr]
        )
        self.assertEqual(
            file_sha256(self.root / self.receipt.report_md_path),
            original_report_hash,
        )
        self.assertEqual(
            file_sha256(self.root / self.receipt.dossier_json_path),
            original_inline_hash,
        )

        second = await service.recover(
            job_root=self.root,
            capture_receipt=self.receipt,
            adapter=adapter,
        )
        self.assertEqual(adapter.calls, 1)
        self.assertEqual(first.receipt, second.receipt)  # type: ignore[union-attr]

    async def test_other_turn_attachment_is_rejected_without_ready(self) -> None:
        adapter = _JsonAttachmentAdapter(self.full, wrong_turn=True)
        with self.assertRaisesRegex(ValueError, "identity mismatch"):
            await ExpandedDossierArtifactService().recover(
                job_root=self.root,
                capture_receipt=self.receipt,
                adapter=adapter,
            )
        self.assertFalse((self.root / EXPANDED_READY_PATH).exists())

    async def test_manifest_count_mismatch_is_rejected(self) -> None:
        bad = dict(self.full)
        bad["material_facts"] = []
        adapter = _JsonAttachmentAdapter(bad)
        with self.assertRaisesRegex(ValueError, "count differs"):
            await ExpandedDossierArtifactService().recover(
                job_root=self.root,
                capture_receipt=self.receipt,
                adapter=adapter,
            )
        self.assertFalse((self.root / EXPANDED_READY_PATH).exists())

    async def test_post_ready_file_tamper_is_detected(self) -> None:
        await ExpandedDossierArtifactService().recover(
            job_root=self.root,
            capture_receipt=self.receipt,
            adapter=_JsonAttachmentAdapter(self.full),
        )
        path = resolve_import_dossier_path(self.root, self.receipt)
        path.write_text("{}\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            verify_expanded_dossier_bundle(self.root, self.receipt)


if __name__ == "__main__":
    unittest.main()
