"""MD-first atomic capture writer; READY.json is committed last."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import os
from pathlib import Path
import re
from typing import Callable, Mapping

from ..browser.protocol import RawBrowserCapture
from ..ids import canonical_json
from .receipt import CaptureReceipt, file_sha256, verify_capture_bundle


DOSSIER_BLOCK = re.compile(
    r"E2R_RESEARCH_DOSSIER_JSON_BEGIN\s*(.*?)\s*E2R_RESEARCH_DOSSIER_JSON_END",
    re.DOTALL,
)


@dataclass(frozen=True)
class CaptureIdentity:
    job_id: str
    run_id: str
    target_id: str
    as_of_date: str
    packet_hash: str
    prompt_hash: str
    conversation_id: str | None
    capture_mode: str = "LIVE_BROWSER"


@dataclass(frozen=True)
class AtomicCaptureResult:
    job_root: Path
    receipt: CaptureReceipt
    receipt_path: Path
    ready_path: Path


class AtomicCaptureWriter:
    def __init__(self, *, now: Callable[[], datetime] | None = None) -> None:
        self._now = now or (lambda: datetime.now(timezone.utc))

    def finalize(
        self,
        job_root: str | Path,
        *,
        identity: CaptureIdentity,
        raw_capture: RawBrowserCapture,
    ) -> AtomicCaptureResult:
        root = Path(job_root).resolve()
        staging = root / "capture/.staging"
        incoming = root / "capture/incoming"
        staging.mkdir(parents=True, exist_ok=True)
        incoming.mkdir(parents=True, exist_ok=True)
        report_part = raw_capture.report_md_part_path.resolve()
        if report_part != (staging / "pro_report.md.part").resolve():
            raise ValueError("browser capture must use the job staging MD path")
        if not report_part.is_file() or report_part.stat().st_size == 0:
            raise ValueError("mandatory staged MD report is missing or empty")
        report_text = report_part.read_text(encoding="utf-8-sig")
        dossier_text = self._extract_dossier(report_text)
        dossier_part = staging / "research_dossier.json.part"
        self._write_bytes_durable(dossier_part, (dossier_text + "\n").encode("utf-8"))

        report_final = incoming / "pro_report.md"
        dossier_final = incoming / "research_dossier.json"
        os.replace(report_part, report_final)
        os.replace(dossier_part, dossier_final)
        pdf_final = None
        if raw_capture.report_pdf_part_path is not None:
            pdf_part = raw_capture.report_pdf_part_path.resolve()
            if pdf_part != (staging / "pro_report.pdf.part").resolve():
                raise ValueError("browser capture must use the job staging PDF path")
            if not pdf_part.is_file() or not pdf_part.read_bytes().startswith(b"%PDF-"):
                raise ValueError("optional staged PDF is invalid")
            pdf_final = incoming / "pro_report.pdf"
            os.replace(pdf_part, pdf_final)
        self._fsync_directory(incoming)

        captured_at = self._now_value().isoformat().replace("+00:00", "Z")
        receipt = CaptureReceipt(
            schema_version="e2r_pro_capture_receipt_v1",
            event_type="PRO_RESEARCH_CAPTURE_COMPLETE",
            job_id=identity.job_id,
            run_id=identity.run_id,
            target_id=identity.target_id,
            as_of_date=identity.as_of_date,
            packet_hash=identity.packet_hash,
            prompt_hash=identity.prompt_hash,
            conversation_id=identity.conversation_id,
            assistant_turn_id=raw_capture.assistant_turn_id,
            report_md_hash=file_sha256(report_final),
            report_pdf_hash=file_sha256(pdf_final) if pdf_final is not None else None,
            dossier_json_hash=file_sha256(dossier_final),
            submit_count=1,
            capture_count=1,
            captured_at=captured_at,
            capture_mode=identity.capture_mode,
            capture_source=raw_capture.source,
            optional_pdf_error=raw_capture.optional_pdf_error,
            report_pdf_path=(
                "capture/incoming/pro_report.pdf" if pdf_final is not None else None
            ),
        )
        receipt_part = staging / "browser_capture_receipt.json.part"
        receipt_final = incoming / "browser_capture_receipt.json"
        self._write_json_durable(receipt_part, receipt.to_dict())
        os.replace(receipt_part, receipt_final)
        self._fsync_directory(incoming)
        verify_capture_bundle(root, receipt)

        ready_payload = {
            "schema_version": "e2r_pro_capture_ready_v1",
            "job_id": identity.job_id,
            "run_id": identity.run_id,
            "capture_receipt_hash": receipt.receipt_hash,
            "capture_receipt_path": "capture/incoming/browser_capture_receipt.json",
            "written_last": True,
        }
        ready_part = staging / "READY.json.part"
        ready_final = incoming / "READY.json"
        self._write_json_durable(ready_part, ready_payload)
        os.replace(ready_part, ready_final)
        self._fsync_directory(incoming)
        return AtomicCaptureResult(root, receipt, receipt_final, ready_final)

    @staticmethod
    def _extract_dossier(report_text: str) -> str:
        match = DOSSIER_BLOCK.search(report_text)
        if match is None:
            raise ValueError("MD report is missing the required dossier sentinel block")
        block = match.group(1).strip()
        if block.startswith("```"):
            lines = block.splitlines()
            if len(lines) < 3 or not lines[-1].strip().startswith("```"):
                raise ValueError("dossier code fence is incomplete")
            block = "\n".join(lines[1:-1]).strip()
        if not block:
            raise ValueError("dossier sentinel block is empty")
        return block

    @staticmethod
    def _write_json_durable(path: Path, value: Mapping[str, object]) -> None:
        AtomicCaptureWriter._write_bytes_durable(
            path, (canonical_json(value) + "\n").encode("utf-8")
        )

    @staticmethod
    def _write_bytes_durable(path: Path, payload: bytes) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())

    @staticmethod
    def _fsync_directory(path: Path) -> None:
        descriptor = os.open(path, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)

    def _now_value(self) -> datetime:
        value = self._now()
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("capture clock must be timezone-aware")
        return value.astimezone(timezone.utc)


__all__ = [
    "AtomicCaptureResult",
    "AtomicCaptureWriter",
    "CaptureIdentity",
    "DOSSIER_BLOCK",
]
