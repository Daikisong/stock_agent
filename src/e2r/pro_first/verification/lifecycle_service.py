"""Durable DOSSIER_IMPORTED → VERIFYING_SOURCES → GAP_ADJUDICATION bridge."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..atomic_io import fsync_directory
from ..ids import canonical_hash, canonical_json, stable_id
from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob
from ..state_machine import NoProgressDetected
from ..multi_pass import load_effective_research_dossier
from ..preflight import LocalEvidencePreflightService
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
        preflight_service: LocalEvidencePreflightService | None = None,
    ) -> None:
        self.store = store
        self.verifier = verifier or ProSourceVerifier()
        self.preflight_service = preflight_service or LocalEvidencePreflightService(
            page_fetcher=self.verifier.page_fetcher
        )

    def request_reverification(
        self,
        job_id: str,
        *,
        reason: str,
        maximum_attempts: int = 3,
    ) -> ProResearchJob:
        """Reopen source verification only after a verifier semantics change."""

        if not reason.strip():
            raise ValueError("source reverification requires an explicit reason")
        job = self.store.get_job(job_id)
        if job.status not in {
            JobStatus.GAP_ADJUDICATION.value,
            JobStatus.SUPPLEMENTAL_RESEARCH.value,
            JobStatus.USER_ATTENTION_REQUIRED.value,
            JobStatus.FAILED_RETRYABLE.value,
        }:
            raise ValueError("job is outside the source-reverification recovery boundary")
        previous = self.store.get_source_verification_receipt(job_id)
        if previous is None:
            raise ValueError("source reverification requires a prior durable receipt")
        current_semantics = str(self.verifier.semantics_version)
        previous_semantics = str(previous.get("verification_semantics_version") or "")
        if previous_semantics == current_semantics:
            raise NoProgressDetected(
                "source verification semantics are unchanged; repeat is forbidden"
            )
        attempts = self.store.source_verification_attempt_count(job_id)
        if attempts >= maximum_attempts:
            raise NoProgressDetected("source verification attempt bound reached")
        return self.store.transition(
            job_id,
            expected_version=job.state_version,
            to_status=JobStatus.VERIFYING_SOURCES,
            actor="pro-source-verifier-recovery",
            idempotency_key=(
                f"source-reverification:{previous.get('verification_hash')}:"
                f"{current_semantics}"
            ),
            payload={
                "reason": reason,
                "prior_verification_hash": previous.get("verification_hash"),
                "prior_semantics_version": previous_semantics or None,
                "next_semantics_version": current_semantics,
                "next_attempt": attempts + 1,
                "automatic_research_resubmit_allowed": False,
            },
        )

    def request_effective_dossier_reverification(
        self,
        job_id: str,
        *,
        job_root: str | Path,
        reason: str,
        maximum_attempts: int = 4,
    ) -> ProResearchJob:
        """Reverify when a later completed Pro pass added a new dossier snapshot.

        This is distinct from a verifier-semantics retry.  The same verifier is
        allowed only when the hash-bound effective dossier changed after the
        prior receipt; an unchanged snapshot remains a forbidden no-progress
        loop.
        """

        if not reason.strip():
            raise ValueError("effective-dossier reverification requires a reason")
        root = Path(job_root).resolve()
        job = self.store.get_job(job_id)
        if job.status not in {
            JobStatus.GAP_ADJUDICATION.value,
            JobStatus.SUPPLEMENTAL_RESEARCH.value,
            JobStatus.USER_ATTENTION_REQUIRED.value,
            JobStatus.FAILED_RETRYABLE.value,
        }:
            raise ValueError("job is outside the effective-dossier reverification boundary")
        previous = self.store.get_source_verification_receipt(job_id)
        if previous is None:
            raise ValueError("effective-dossier reverification requires a prior receipt")
        pointer_path = root / "research_passes/effective_dossier.latest.json"
        if not pointer_path.is_file():
            raise ValueError("effective-dossier reverification requires a latest snapshot")
        pointer = json.loads(pointer_path.read_text(encoding="utf-8"))
        latest_hash = str(pointer.get("dossier_hash") or "")
        prior_hash = str(
            previous.get("effective_dossier_hash")
            or previous.get("normalized_dossier_hash")
            or ""
        )
        if len(latest_hash) != 64 or latest_hash == prior_hash:
            raise NoProgressDetected(
                "effective dossier is unchanged; same-semantics repeat is forbidden"
            )
        total_attempts = self.store.source_verification_attempt_count(job_id)
        input_attempts = (
            self.store.source_verification_attempt_count_for_dossier_hash(
                job_id,
                latest_hash,
            )
        )
        if input_attempts >= maximum_attempts:
            raise NoProgressDetected(
                "effective dossier source verification attempt bound reached"
            )
        return self.store.transition(
            job_id,
            expected_version=job.state_version,
            to_status=JobStatus.VERIFYING_SOURCES,
            actor="pro-effective-dossier-verifier",
            idempotency_key=(
                f"effective-dossier-reverification:"
                f"{previous.get('verification_hash')}:{latest_hash}"
            ),
            payload={
                "reason": reason,
                "prior_verification_hash": previous.get("verification_hash"),
                "prior_effective_dossier_hash": prior_hash,
                "next_effective_dossier_hash": latest_hash,
                "next_effective_dossier_snapshot_id": pointer.get("snapshot_id"),
                "next_attempt": total_attempts + 1,
                "next_effective_dossier_attempt": input_attempts + 1,
                "automatic_research_resubmit_allowed": False,
            },
        )

    def verify_job(self, job_id: str, *, job_root: str | Path) -> SourceVerificationRun:
        root = Path(job_root).resolve()
        verification_root = root / "verification"
        dossier = load_effective_research_dossier(root)
        job = self.store.get_job(job_id)
        if not job.dossier_id:
            raise ValueError("source verification requires a durable dossier import")
        import_receipt = self.store.get_dossier_import_receipt(job_id)
        latest_pointer_path = root / "research_passes/effective_dossier.latest.json"
        latest_pointer = (
            json.loads(latest_pointer_path.read_text(encoding="utf-8"))
            if latest_pointer_path.is_file()
            else None
        )
        if import_receipt is None:
            raise ValueError("source verification requires a durable import receipt")
        if latest_pointer is None:
            if canonical_hash(dossier) != import_receipt.get("normalized_dossier_hash"):
                raise ValueError("normalized dossier differs from the durable import ledger")
        elif (
            latest_pointer.get("job_id") != job_id
            or latest_pointer.get("dossier_hash") != canonical_hash(dossier)
        ):
            raise ValueError("effective V2 dossier differs from its latest snapshot pointer")
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
            target = dossier.get("target") or {}
            preflight = self.preflight_service.run(
                dossier=dossier,
                target_id=job.symbol,
                company_name=job.company_name,
                target_aliases=tuple(target.get("aliases") or ()),
                as_of_date=job.as_of_date,
                archetype_ids=job.archetype_ids,
                job_root=root,
            )
            result = self.verifier.verify(
                dossier=preflight.verifier_dossier,
                job=job,
                job_root=root,
                preflight=preflight,
            )
            verification_rows = [row.to_dict() for row in result.verifications]
            rejection_classification = (
                self.preflight_service.classify_verifications(
                    preflight=preflight,
                    verification_rows=verification_rows,
                )
            )
            rejection_rows = [
                row.to_dict() for row in rejection_classification.rows
            ]
            compilation = result.fact_compilation.to_dict()
            verification_hash = canonical_hash(
                {
                    "job_id": job_id,
                    "dossier_id": job.dossier_id,
                    "verification_semantics_version": (
                        self.verifier.semantics_version
                    ),
                    "preflight_receipt_hash": preflight.receipt.get(
                        "receipt_hash"
                    ),
                    "verifications": verification_rows,
                    "rejection_classifications": rejection_rows,
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
                "preflight_receipt_hash": preflight.receipt.get(
                    "receipt_hash"
                ),
                "preflight_semantics_version": preflight.receipt.get(
                    "semantics_version"
                ),
                "preflight_applicable": preflight.applicable,
                "preflight_operation_count": preflight.receipt.get(
                    "operation_count", 0
                ),
                "preflight_local_normalized_count": preflight.receipt.get(
                    "local_normalized_count", 0
                ),
                "preflight_source_representation_resolved_count": (
                    preflight.receipt.get(
                        "source_representation_resolved_count", 0
                    )
                ),
                "rejection_root_cause_counts": dict(
                    rejection_classification.root_cause_counts
                ),
                "local_normalizable_sent_to_pro_count": (
                    rejection_classification.local_normalizable_sent_to_pro_count
                ),
                "source_representation_sent_to_pro_count": (
                    rejection_classification.source_representation_sent_to_pro_count
                ),
                "unclassified_rejection_count": (
                    rejection_classification.unclassified_rejection_count
                ),
                "verification_semantics_version": self.verifier.semantics_version,
                "verification_attempt": (
                    self.store.source_verification_attempt_count(job_id) + 1
                ),
            }
            if latest_pointer is not None:
                receipt.update(
                    {
                        "effective_dossier_snapshot_id": latest_pointer.get(
                            "snapshot_id"
                        ),
                        "effective_dossier_pass_id": latest_pointer.get("pass_id"),
                        "effective_dossier_hash": latest_pointer.get("dossier_hash"),
                    }
                )
            self._write_jsonl_atomic(
                verification_root / "source_verifications.jsonl", verification_rows
            )
            self._write_jsonl_atomic(
                verification_root / "rejection_classifications.jsonl",
                rejection_rows,
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
            self._write_jsonl_atomic(
                verification_root / "mechanism_scope_mappings.jsonl",
                [
                    {
                        "dossier_fact_id": fact_id,
                        **dict(mapping),
                    }
                    for fact_id, mapping in (
                        result.mechanism_scope_mapping.mappings_by_fact_id.items()
                        if result.mechanism_scope_mapping is not None
                        else ()
                    )
                ],
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
    fsync_directory(path.parent)


__all__ = ["ProSourceVerificationService", "SourceVerificationRun"]
