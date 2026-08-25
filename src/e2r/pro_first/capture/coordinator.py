"""Capture orchestration, in-process dispatch, and restart reconciliation."""

from __future__ import annotations

from dataclasses import dataclass
import inspect
import json
from pathlib import Path
from typing import Awaitable, Callable, Mapping

from ..browser.protocol import BrowserCaptureRequest, ChatGPTWebAdapter
from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob
from .atomic_capture import AtomicCaptureResult, AtomicCaptureWriter, CaptureIdentity
from .receipt import CaptureReceipt, file_sha256, load_capture_receipt, verify_capture_bundle


@dataclass(frozen=True)
class CaptureCompleteEvent:
    job_id: str
    run_id: str
    receipt_hash: str
    job_root: Path


CaptureHandler = Callable[[CaptureCompleteEvent], object | Awaitable[object]]


class CaptureEventDispatcher:
    def __init__(self) -> None:
        self._handlers: list[CaptureHandler] = []

    def subscribe(self, handler: CaptureHandler) -> None:
        if handler not in self._handlers:
            self._handlers.append(handler)

    async def dispatch(self, event: CaptureCompleteEvent) -> None:
        for handler in tuple(self._handlers):
            result = handler(event)
            if inspect.isawaitable(result):
                await result


class ProCaptureCoordinator:
    def __init__(
        self,
        store: ProFirstJobStore,
        *,
        writer: AtomicCaptureWriter | None = None,
        dispatcher: CaptureEventDispatcher | None = None,
    ) -> None:
        self.store = store
        self.writer = writer or AtomicCaptureWriter()
        self.dispatcher = dispatcher or CaptureEventDispatcher()

    async def capture(
        self,
        job_id: str,
        *,
        run_id: str,
        expected_filename: str,
        expected_report_hash: str,
        job_root: str | Path,
        adapter: ChatGPTWebAdapter,
        capture_mode: str = "LIVE_BROWSER",
        dossier_override: Mapping[str, object] | None = None,
    ) -> tuple[ProResearchJob, AtomicCaptureResult]:
        job = self.store.get_job(job_id)
        if job.status != JobStatus.RESULT_DETECTED.value:
            raise ValueError("capture requires RESULT_DETECTED")
        if not job.packet_hash or not job.approval_prompt_hash:
            raise ValueError("capture requires packet and approved prompt hashes")
        capturing = self.store.transition(
            job_id,
            expected_version=job.state_version,
            to_status=JobStatus.CAPTURING_ARTIFACTS,
            actor="browser-capture-worker",
            idempotency_key=f"capture-start:{job_id}:{job.state_version}",
            payload={"expected_report_hash": expected_report_hash},
        )
        root = Path(job_root).resolve()
        try:
            raw = await adapter.capture_result(
                BrowserCaptureRequest(
                    job_id=job_id,
                    run_id=run_id,
                    expected_filename=expected_filename,
                    expected_report_hash=expected_report_hash,
                    staging_directory=root / "capture/.staging",
                    allow_readable_report_without_dossier=(
                        dossier_override is not None
                    ),
                )
            )
            result = self.writer.finalize(
                root,
                identity=CaptureIdentity(
                    job_id=job_id,
                    run_id=run_id,
                    target_id=capturing.symbol,
                    as_of_date=capturing.as_of_date,
                    packet_hash=capturing.packet_hash or "",
                    prompt_hash=capturing.approval_prompt_hash or "",
                    conversation_id=capturing.conversation_id,
                    capture_mode=capture_mode,
                ),
                raw_capture=raw,
                dossier_override=dossier_override,
            )
            completed = self._record_complete(capturing, result)
        except Exception as error:
            current = self.store.get_job(job_id)
            ready_exists = (root / "capture/incoming/READY.json").is_file()
            if current.status == JobStatus.CAPTURING_ARTIFACTS.value and not ready_exists:
                self.store.transition(
                    job_id,
                    expected_version=current.state_version,
                    to_status=JobStatus.USER_ATTENTION_REQUIRED,
                    actor="browser-capture-worker",
                    idempotency_key=f"capture-attention:{job_id}:{current.state_version}",
                    payload={"automatic_resubmit_allowed": False},
                    updates={
                        "last_error_class": type(error).__name__,
                        "last_error_message": str(error),
                    },
                )
            raise
        event = CaptureCompleteEvent(job_id, run_id, result.receipt.receipt_hash, root)
        await self.dispatcher.dispatch(event)
        return completed, result

    def _record_complete(
        self, job: ProResearchJob, result: AtomicCaptureResult
    ) -> ProResearchJob:
        receipt = result.receipt
        return self.store.record_capture_complete(
            job.job_id,
            expected_version=job.state_version,
            receipt=receipt.to_dict(),
            artifacts=_artifact_records(result),
            actor="browser-capture-worker",
            idempotency_key=f"capture-complete:{receipt.receipt_hash}",
        )


class CaptureFilesystemReconciler:
    def __init__(
        self,
        store: ProFirstJobStore,
        *,
        dispatcher: CaptureEventDispatcher | None = None,
    ) -> None:
        self.store = store
        self.dispatcher = dispatcher or CaptureEventDispatcher()

    async def reconcile(self, job_root: str | Path) -> CaptureCompleteEvent | None:
        root = Path(job_root).resolve()
        ready_path = root / "capture/incoming/READY.json"
        if not ready_path.is_file():
            return None
        ready = json.loads(ready_path.read_text(encoding="utf-8"))
        if not isinstance(ready, dict) or ready.get("schema_version") != "e2r_pro_capture_ready_v1":
            raise ValueError("invalid capture READY schema")
        if (
            ready.get("capture_receipt_path")
            != "capture/incoming/browser_capture_receipt.json"
            or ready.get("written_last") is not True
        ):
            raise ValueError("capture READY does not certify the canonical final receipt")
        receipt_path = root / "capture/incoming/browser_capture_receipt.json"
        receipt = load_capture_receipt(receipt_path)
        if ready.get("job_id") != receipt.job_id or ready.get("run_id") != receipt.run_id:
            raise ValueError("READY identity differs from capture receipt")
        if ready.get("capture_receipt_hash") != receipt.receipt_hash:
            raise ValueError("READY capture receipt hash mismatch")
        verify_capture_bundle(root, receipt)
        job = self.store.get_job(receipt.job_id)
        if job.status == JobStatus.RESULT_DETECTED.value:
            job = self.store.transition(
                job.job_id,
                expected_version=job.state_version,
                to_status=JobStatus.CAPTURING_ARTIFACTS,
                actor="capture-reconciler",
                idempotency_key=f"capture-recovered-start:{receipt.receipt_hash}",
                payload={"ready_recovered": True},
            )
        if job.status == JobStatus.CAPTURING_ARTIFACTS.value:
            result = AtomicCaptureResult(root, receipt, receipt_path, ready_path)
            job = self.store.record_capture_complete(
                job.job_id,
                expected_version=job.state_version,
                receipt=receipt.to_dict(),
                artifacts=_artifact_records(result),
                actor="capture-reconciler",
                idempotency_key=f"capture-complete:{receipt.receipt_hash}",
            )
        if job.capture_count != 1:
            raise ValueError("READY exists but durable capture_count is not one")
        event = CaptureCompleteEvent(receipt.job_id, receipt.run_id, receipt.receipt_hash, root)
        await self.dispatcher.dispatch(event)
        return event


def _artifact_records(result: AtomicCaptureResult) -> tuple[dict[str, object], ...]:
    paths = [
        ("REPORT_MD", result.job_root / result.receipt.report_md_path),
        ("DOSSIER_JSON", result.job_root / result.receipt.dossier_json_path),
        ("CAPTURE_RECEIPT", result.receipt_path),
        ("READY", result.ready_path),
    ]
    if result.receipt.report_pdf_path is not None:
        paths.append(("REPORT_PDF", result.job_root / result.receipt.report_pdf_path))
    return tuple(
        {
            "artifact_kind": kind,
            "relative_path": path.relative_to(result.job_root).as_posix(),
            "content_hash": file_sha256(path),
            "byte_count": path.stat().st_size,
            "metadata": {"capture_receipt_hash": result.receipt.receipt_hash},
        }
        for kind, path in paths
    )


__all__ = [
    "CaptureCompleteEvent",
    "CaptureEventDispatcher",
    "CaptureFilesystemReconciler",
    "ProCaptureCoordinator",
]
