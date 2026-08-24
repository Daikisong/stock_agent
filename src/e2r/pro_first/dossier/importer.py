"""Capture-bound ResearchDossierV1 importer with recoverable failure boundaries."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
from typing import Any, Callable, Mapping

from ..capture.coordinator import CaptureCompleteEvent
from ..capture.receipt import load_capture_receipt, verify_capture_bundle
from ..atomic_io import fsync_directory
from ..ids import canonical_hash, canonical_json, stable_id
from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob
from ..state_machine import TransitionContext
from .dialect_adapter import ResearchDossierDialectAdapter
from .identity_binding import bind_dossier_transport_identity
from .normalizer import ResearchDossierNormalizer
from .parser import ResearchDossierParser
from .validator import DossierValidationContext, ResearchDossierValidator
from ..multi_pass.models import INITIAL_PASS_NAME


@dataclass(frozen=True)
class DossierImportResult:
    job: ProResearchJob
    normalized_dossier: Mapping[str, Any]
    import_receipt: Mapping[str, Any]
    normalized_path: Path
    receipt_path: Path


class ProDossierImporter:
    def __init__(
        self,
        store: ProFirstJobStore,
        *,
        parser: ResearchDossierParser | None = None,
        dialect_adapter: ResearchDossierDialectAdapter | None = None,
        validator: ResearchDossierValidator | None = None,
        normalizer: ResearchDossierNormalizer | None = None,
        now: Callable[[], datetime] | None = None,
    ) -> None:
        self.store = store
        self.parser = parser or ResearchDossierParser()
        self.dialect_adapter = dialect_adapter or ResearchDossierDialectAdapter()
        self.validator = validator or ResearchDossierValidator()
        self.normalizer = normalizer or ResearchDossierNormalizer()
        self._now = now or (lambda: datetime.now(timezone.utc))

    async def handle_capture_event(self, event: CaptureCompleteEvent) -> DossierImportResult:
        return self.import_job(event.job_id, job_root=event.job_root)

    def import_job(
        self,
        job_id: str,
        *,
        job_root: str | Path,
        final_response_text: str | None = None,
        expected_research_pass_id: str | None = None,
        expected_parent_pass_id: str | None = None,
    ) -> DossierImportResult:
        root = Path(job_root).resolve()
        incoming = root / "capture/incoming"
        receipt = load_capture_receipt(incoming / "browser_capture_receipt.json")
        verify_capture_bundle(root, receipt)
        ready = json.loads((incoming / "READY.json").read_text(encoding="utf-8"))
        if (
            ready.get("capture_receipt_hash") != receipt.receipt_hash
            or ready.get("job_id") != job_id
            or receipt.job_id != job_id
        ):
            raise ValueError("capture READY/receipt identity does not match import job")
        job = self.store.get_job(job_id)
        if (
            receipt.target_id != job.symbol
            or receipt.as_of_date != job.as_of_date
            or receipt.packet_hash != job.packet_hash
            or receipt.prompt_hash != job.approval_prompt_hash
            or receipt.conversation_id != job.conversation_id
        ):
            raise ValueError("capture receipt no longer matches the durable job")
        import_root = root / "import"
        normalized_path = import_root / "research_dossier.normalized.json"
        import_receipt_path = import_root / "dossier_import_receipt.json"
        if job.dossier_id and job.status not in {
            JobStatus.CAPTURE_COMPLETE.value,
            JobStatus.IMPORTING.value,
            JobStatus.USER_ATTENTION_REQUIRED.value,
        }:
            stored = self.store.get_dossier_import_receipt(job_id)
            if stored is None or not normalized_path.is_file() or not import_receipt_path.is_file():
                raise ValueError("durable dossier import exists without canonical import artifacts")
            file_receipt = json.loads(import_receipt_path.read_text(encoding="utf-8"))
            normalized_payload = json.loads(normalized_path.read_text(encoding="utf-8"))
            if file_receipt != stored or canonical_hash(normalized_payload) != stored.get(
                "normalized_dossier_hash"
            ):
                raise ValueError("canonical import artifacts differ from the durable import ledger")
            return DossierImportResult(
                job=job,
                normalized_dossier=normalized_payload,
                import_receipt=stored,
                normalized_path=normalized_path,
                receipt_path=import_receipt_path,
            )
        if job.status in {
            JobStatus.CAPTURE_COMPLETE.value,
            JobStatus.USER_ATTENTION_REQUIRED.value,
        }:
            job = self.store.transition(
                job_id,
                expected_version=job.state_version,
                to_status=JobStatus.IMPORTING,
                actor="dossier-importer",
                idempotency_key=f"dossier-import-start:{receipt.receipt_hash}:{job.state_version}",
                payload={"capture_receipt_hash": receipt.receipt_hash},
                context=TransitionContext(capture_receipt_verified=True),
            )
        elif job.status != JobStatus.IMPORTING.value:
            raise ValueError(f"dossier import cannot start from {job.status}")
        try:
            parsed = self.parser.parse(
                downloaded_json_path=incoming / "research_dossier.json",
                report_md_path=incoming / "pro_report.md",
                final_response_text=final_response_text,
            )
            adapted = self.dialect_adapter.adapt(parsed.payload)
            browser_state = self.store.get_browser_session_state(job_id) or {}
            durable_browser_detail = browser_state.get("state") or {}
            durable_initial_pass_id = str(
                expected_research_pass_id
                or durable_browser_detail.get("initial_pass_id")
                or ""
            ) or None
            identity_bound = bind_dossier_transport_identity(
                adapted.payload,
                conversation_id=receipt.conversation_id or "",
                research_pass_id=durable_initial_pass_id,
                parent_pass_id=expected_parent_pass_id,
                allow_initial_conversation_placeholder=(
                    expected_parent_pass_id is None
                ),
                pass_name=(
                    INITIAL_PASS_NAME if expected_parent_pass_id is None else None
                ),
                prompt_hash=(
                    receipt.prompt_hash if expected_parent_pass_id is None else None
                ),
                response_hash=(
                    receipt.report_md_hash if expected_parent_pass_id is None else None
                ),
            )
            validation = self.validator.validate(
                identity_bound.payload,
                DossierValidationContext(
                    job_id=job_id,
                    run_id=receipt.run_id,
                    target_id=job.symbol,
                    as_of_date=job.as_of_date,
                    conversation_id=receipt.conversation_id,
                    candidate_archetype_ids=job.archetype_ids,
                    research_pass_id=durable_initial_pass_id,
                    parent_pass_id=expected_parent_pass_id,
                    enforce_parent_pass_id=True,
                ),
            )
            normalized = self.normalizer.normalize(identity_bound.payload)
            dossier_id = stable_id(
                "DOSSIER",
                {"job_id": job_id, "dossier_hash": normalized.after_hash},
            )
            import_receipt: Mapping[str, Any] = {
                "schema_version": "e2r_pro_dossier_import_receipt_v1",
                "dossier_schema_version": validation.schema_version,
                "validation_status": "PASS",
                "job_id": job_id,
                "run_id": receipt.run_id,
                "target_id": job.symbol,
                "as_of_date": job.as_of_date,
                "dossier_id": dossier_id,
                "parser_source": parsed.parser_source,
                "parser_before_hash": parsed.before_hash,
                "parser_after_hash": parsed.after_hash,
                "repair_operations": list(parsed.repair_operations),
                "dialect_before_hash": adapted.before_hash,
                "dialect_after_hash": adapted.after_hash,
                "dialect_operations": list(adapted.operations),
                "dialect_id_map": dict(adapted.id_map),
                "identity_binding_before_hash": identity_bound.before_hash,
                "identity_binding_after_hash": identity_bound.after_hash,
                "identity_binding_operations": list(identity_bound.operations),
                "normalizer_before_hash": normalized.before_hash,
                "normalized_dossier_hash": normalized.after_hash,
                "normalizer_operations": list(normalized.operations),
                "fact_ids": list(validation.fact_ids),
                "fact_count": len(validation.fact_ids),
                "source_urls": list(validation.source_urls),
                "source_document_ids": list(validation.source_document_ids),
                "source_document_count": len(validation.source_document_ids),
                "derived_metric_ids": list(validation.derived_metric_ids),
                "derived_metric_count": len(validation.derived_metric_ids),
                "component_ids": list(validation.component_ids),
                "conversation_id": validation.conversation_id,
                "research_pass_id": validation.research_pass_id,
                "selected_archetype_ids": list(validation.selected_archetype_ids),
                "question_family_ids": list(validation.question_family_ids),
                "question_family_count": len(validation.question_family_ids),
                "search_route_receipt_ids": list(
                    validation.search_route_receipt_ids
                ),
                "research_status": validation.research_status,
                "score_authority": False,
                "stage_authority": False,
                "evidence_promoted_count": 0,
                "imported_at": self._now_text(),
            }
            self._write_json_atomic(normalized_path, normalized.payload)
            self._write_json_atomic(import_receipt_path, import_receipt)
            imported = self.store.record_dossier_import(
                job_id,
                expected_version=job.state_version,
                dossier_id=dossier_id,
                dossier_hash=normalized.after_hash,
                import_receipt=import_receipt,
                actor="dossier-importer",
                idempotency_key=f"dossier-imported:{normalized.after_hash}",
            )
            return DossierImportResult(
                job=imported,
                normalized_dossier=normalized.payload,
                import_receipt=import_receipt,
                normalized_path=normalized_path,
                receipt_path=import_receipt_path,
            )
        except Exception as error:
            failure = {
                "schema_version": "e2r_pro_dossier_import_failure_v1",
                "job_id": job_id,
                "run_id": receipt.run_id,
                "capture_receipt_hash": receipt.receipt_hash,
                "error_class": "DOSSIER_INVALID",
                "cause_class": type(error).__name__,
                "message": str(error),
                "automatic_research_resubmit_allowed": False,
                "failed_at": self._now_text(),
            }
            self._write_json_atomic(import_root / "dossier_import_failure.json", failure)
            current = self.store.get_job(job_id)
            if current.status == JobStatus.IMPORTING.value:
                self.store.transition(
                    job_id,
                    expected_version=current.state_version,
                    to_status=JobStatus.USER_ATTENTION_REQUIRED,
                    actor="dossier-importer",
                    idempotency_key=f"dossier-invalid:{receipt.receipt_hash}:{current.state_version}",
                    payload={
                        "capture_receipt_hash": receipt.receipt_hash,
                        "automatic_resubmit_allowed": False,
                    },
                    updates={
                        "last_error_class": "DOSSIER_INVALID",
                        "last_error_message": str(error),
                    },
                )
            raise

    @staticmethod
    def _write_json_atomic(path: Path, payload: Mapping[str, Any]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        part = path.with_suffix(path.suffix + ".part")
        with part.open("w", encoding="utf-8") as stream:
            stream.write(canonical_json(payload) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(part, path)
        fsync_directory(path.parent)

    def _now_text(self) -> str:
        value = self._now()
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("dossier import clock must be timezone-aware")
        return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


__all__ = ["DossierImportResult", "ProDossierImporter"]
