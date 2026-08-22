"""Durable DOSSIER_IMPORTED → VERIFYING_SOURCES → GAP_ADJUDICATION bridge."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..ids import canonical_hash, canonical_json, stable_id
from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob
from .source_verifier import ProSourceVerifier, SourceVerificationResult


@dataclass(frozen=True)
class SourceVerificationRun:
    job: ProResearchJob
    result: SourceVerificationResult | None
    receipt: Mapping[str, Any]
    verification_root: Path


class ProSourceVerificationService:
    def __init__(
        self,
        store: ProFirstJobStore,
        *,
        verifier: ProSourceVerifier | None = None,
    ) -> None:
        self.store = store
        self.verifier = verifier or ProSourceVerifier()

    def verify_job(self, job_id: str, *, job_root: str | Path) -> SourceVerificationRun:
        root = Path(job_root).resolve()
        verification_root = root / "verification"
        normalized_path = root / "import/research_dossier.normalized.json"
        dossier = json.loads(normalized_path.read_text(encoding="utf-8"))
        job = self.store.get_job(job_id)
        if not job.dossier_id:
            raise ValueError("source verification requires a durable dossier import")
        import_receipt = self.store.get_dossier_import_receipt(job_id)
        if (
            import_receipt is None
            or canonical_hash(dossier) != import_receipt.get("normalized_dossier_hash")
        ):
            raise ValueError("normalized dossier differs from the durable import ledger")
        receipt_path = verification_root / "source_verification_receipt.json"
        if job.status not in {
            JobStatus.DOSSIER_IMPORTED.value,
            JobStatus.VERIFYING_SOURCES.value,
            JobStatus.USER_ATTENTION_REQUIRED.value,
        }:
            stored = self.store.get_source_verification_receipt(job_id)
            if stored is None or not receipt_path.is_file():
                raise ValueError("durable source verification lacks canonical artifacts")
            file_receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            if file_receipt != stored:
                raise ValueError("source verification file differs from durable ledger")
            return SourceVerificationRun(
                job=job,
                result=None,
                receipt=stored,
                verification_root=verification_root,
            )
        if job.status in {
            JobStatus.DOSSIER_IMPORTED.value,
            JobStatus.USER_ATTENTION_REQUIRED.value,
        }:
            job = self.store.transition(
                job_id,
                expected_version=job.state_version,
                to_status=JobStatus.VERIFYING_SOURCES,
                actor="pro-source-verifier",
                idempotency_key=f"source-verification-start:{job.dossier_id}:{job.state_version}",
                payload={"dossier_id": job.dossier_id},
            )
        try:
            result = self.verifier.verify(dossier=dossier, job=job, job_root=root)
            verification_rows = [row.to_dict() for row in result.verifications]
            compilation = result.fact_compilation.to_dict()
            verification_hash = canonical_hash(
                {
                    "job_id": job_id,
                    "dossier_id": job.dossier_id,
                    "verifications": verification_rows,
                    "fact_compilation": compilation,
                }
            )
            verification_id = stable_id(
                "PROVERIFY",
                {"job_id": job_id, "verification_hash": verification_hash},
            )
            receipt = {
                **result.receipt_payload,
                "job_id": job_id,
                "dossier_id": job.dossier_id,
                "verification_id": verification_id,
                "verification_hash": verification_hash,
                "normalized_dossier_hash": canonical_hash(dossier),
            }
            self._write_jsonl_atomic(
                verification_root / "source_verifications.jsonl", verification_rows
            )
            self._write_jsonl_atomic(
                verification_root / "evidence_facts.jsonl",
                [row.to_dict() for row in result.fact_compilation.facts],
            )
            self._write_jsonl_atomic(
                verification_root / "claim_fact_links.jsonl",
                [row.to_dict() for row in result.fact_compilation.claim_fact_links],
            )
            self._write_jsonl_atomic(
                verification_root / "fact_compilation_rejections.jsonl",
                [row.to_dict() for row in result.fact_compilation.rejected_claims],
            )
            self._write_json_atomic(
                verification_root / "fact_compilation_receipt.json", compilation
            )
            self._write_json_atomic(receipt_path, receipt)
            completed = self.store.record_source_verification(
                job_id,
                expected_version=job.state_version,
                verification_id=verification_id,
                dossier_id=job.dossier_id,
                verification_hash=verification_hash,
                receipt=receipt,
                actor="pro-source-verifier",
                idempotency_key=f"source-verified:{verification_hash}",
            )
            return SourceVerificationRun(
                job=completed,
                result=result,
                receipt=receipt,
                verification_root=verification_root,
            )
        except Exception as error:
            current = self.store.get_job(job_id)
            if current.status == JobStatus.VERIFYING_SOURCES.value:
                self.store.transition(
                    job_id,
                    expected_version=current.state_version,
                    to_status=JobStatus.USER_ATTENTION_REQUIRED,
                    actor="pro-source-verifier",
                    idempotency_key=f"source-verification-attention:{job.dossier_id}:{current.state_version}",
                    payload={"automatic_research_resubmit_allowed": False},
                    updates={
                        "last_error_class": type(error).__name__,
                        "last_error_message": str(error),
                    },
                )
            raise

    @staticmethod
    def _write_json_atomic(path: Path, payload: Mapping[str, Any]) -> None:
        _write_atomic(path, canonical_json(payload) + "\n")

    @staticmethod
    def _write_jsonl_atomic(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
        payload = "".join(canonical_json(row) + "\n" for row in rows)
        _write_atomic(path, payload)

def _write_atomic(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_suffix(path.suffix + ".part")
    with part.open("w", encoding="utf-8") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(part, path)
    descriptor = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


__all__ = ["ProSourceVerificationService", "SourceVerificationRun"]
