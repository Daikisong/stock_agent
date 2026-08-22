"""Capture receipt schema and filesystem hash verification."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date, datetime
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from ..ids import canonical_hash


CAPTURE_RECEIPT_SCHEMA = "e2r_pro_capture_receipt_v1"
CAPTURE_EVENT_TYPE = "PRO_RESEARCH_CAPTURE_COMPLETE"


def file_sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


@dataclass(frozen=True)
class CaptureReceipt:
    schema_version: str
    event_type: str
    job_id: str
    run_id: str
    target_id: str
    as_of_date: str
    packet_hash: str
    prompt_hash: str
    conversation_id: str | None
    assistant_turn_id: str
    report_md_hash: str
    report_pdf_hash: str | None
    dossier_json_hash: str
    submit_count: int
    capture_count: int
    captured_at: str
    capture_mode: str
    capture_source: str
    optional_pdf_error: str | None
    report_md_path: str = "capture/incoming/pro_report.md"
    report_pdf_path: str | None = None
    dossier_json_path: str = "capture/incoming/research_dossier.json"

    def __post_init__(self) -> None:
        if self.schema_version != CAPTURE_RECEIPT_SCHEMA:
            raise ValueError("unsupported capture receipt schema")
        if self.event_type != CAPTURE_EVENT_TYPE:
            raise ValueError("unsupported capture event type")
        if not self.job_id or not self.run_id or not self.target_id or not self.assistant_turn_id:
            raise ValueError("capture identity fields must be nonempty")
        date.fromisoformat(self.as_of_date)
        parsed = datetime.fromisoformat(self.captured_at.replace("Z", "+00:00"))
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            raise ValueError("captured_at must be timezone-aware")
        for value, label in (
            (self.packet_hash, "packet_hash"),
            (self.prompt_hash, "prompt_hash"),
            (self.report_md_hash, "report_md_hash"),
            (self.dossier_json_hash, "dossier_json_hash"),
        ):
            if len(value) != 64:
                raise ValueError(f"{label} must be sha256")
        if self.report_pdf_hash is not None and len(self.report_pdf_hash) != 64:
            raise ValueError("report_pdf_hash must be sha256 or null")
        if self.submit_count != 1 or self.capture_count != 1:
            raise ValueError("live research capture must remain exactly once")
        if self.report_pdf_hash is None and self.report_pdf_path is not None:
            raise ValueError("PDF path cannot exist without a PDF hash")
        if self.report_pdf_hash is not None and self.report_pdf_path is None:
            raise ValueError("PDF hash cannot exist without a PDF path")

    @property
    def receipt_hash(self) -> str:
        return canonical_hash(self.to_dict())

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "CaptureReceipt":
        return cls(**dict(value))


def load_capture_receipt(path: str | Path) -> CaptureReceipt:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("capture receipt must be a JSON object")
    return CaptureReceipt.from_dict(payload)


def verify_capture_bundle(job_root: str | Path, receipt: CaptureReceipt) -> None:
    root = Path(job_root).resolve()
    checks = (
        (receipt.report_md_path, receipt.report_md_hash),
        (receipt.dossier_json_path, receipt.dossier_json_hash),
    )
    for relative, expected_hash in checks:
        path = (root / relative).resolve()
        if root not in path.parents or not path.is_file():
            raise ValueError(f"capture artifact missing or outside job root: {relative}")
        if file_sha256(path) != expected_hash:
            raise ValueError(f"capture artifact hash mismatch: {relative}")
    if receipt.report_pdf_path is not None and receipt.report_pdf_hash is not None:
        path = (root / receipt.report_pdf_path).resolve()
        if root not in path.parents or not path.is_file():
            raise ValueError("capture PDF missing or outside job root")
        if file_sha256(path) != receipt.report_pdf_hash:
            raise ValueError("capture PDF hash mismatch")


__all__ = [
    "CAPTURE_EVENT_TYPE",
    "CAPTURE_RECEIPT_SCHEMA",
    "CaptureReceipt",
    "file_sha256",
    "load_capture_receipt",
    "verify_capture_bundle",
]
