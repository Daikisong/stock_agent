"""Hash-verified append-only effective-dossier snapshots for Pro V2 passes."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
from typing import Any, Mapping

from ..atomic_io import fsync_directory
from ..ids import canonical_hash, canonical_json
from .ledger import ProMultiPassLedger
from .models import ResearchDossierSnapshotRecord, ResearchPassStatus


@dataclass(frozen=True)
class EffectiveDossierSnapshot:
    record: ResearchDossierSnapshotRecord
    dossier: Mapping[str, Any]
    path: Path
    latest_receipt_path: Path


class ProMultiPassDossierStore:
    def __init__(self, ledger: ProMultiPassLedger) -> None:
        self.ledger = ledger

    def persist(
        self,
        *,
        job_id: str,
        pass_id: str,
        dossier: Mapping[str, Any],
        job_root: str | Path,
    ) -> EffectiveDossierSnapshot:
        research_pass = self.ledger.get_pass(pass_id)
        if (
            research_pass.job_id != job_id
            or research_pass.status != ResearchPassStatus.COMPLETE.value
        ):
            raise ValueError("effective dossier requires this job's completed pass")
        if dossier.get("job_id") != job_id or dossier.get("research_pass_id") != pass_id:
            raise ValueError("effective dossier identity differs from completed pass")
        root = Path(job_root).resolve()
        pass_directory = (
            root
            / "research_passes"
            / f"{research_pass.pass_ordinal:02d}_{pass_id}"
        )
        dossier_hash = canonical_hash(dossier)
        snapshots = self.ledger.list_dossier_snapshots(job_id)
        same_pass = tuple(row for row in snapshots if row.pass_id == pass_id)
        existing = next(
            (row for row in same_pass if row.dossier_hash == dossier_hash),
            None,
        )
        latest = self.ledger.latest_dossier_snapshot(job_id)
        if existing is not None:
            if latest is not None and latest.snapshot_id != existing.snapshot_id:
                raise ValueError(
                    "historical snapshot cannot replace the latest dossier pointer"
                )
            path = _resolve_runtime_path(root, existing.relative_path)
            stored = _read_hash_verified_dossier(path, existing.dossier_hash)
            return self._write_latest_pointer(
                root=root,
                record=existing,
                dossier=stored,
                path=path,
            )
        if same_pass and latest is not None and latest.pass_id != pass_id:
            raise ValueError(
                "historical pass cannot gain a revision after descendant snapshots"
            )
        path = (
            pass_directory / "effective_dossier.json"
            if not same_pass
            else pass_directory
            / (
                f"effective_dossier.r{len(same_pass) + 1}-"
                f"{dossier_hash[:24]}.json"
            )
        )
        parent_snapshot_id = latest.snapshot_id if latest is not None else None
        relative_path = path.relative_to(root).as_posix()
        if path.exists():
            _read_hash_verified_dossier(path, dossier_hash)
        else:
            _write_json_atomic(path, dossier)
        record = self.ledger.record_dossier_snapshot(
            job_id=job_id,
            pass_id=pass_id,
            parent_snapshot_id=parent_snapshot_id,
            dossier_hash=dossier_hash,
            relative_path=relative_path,
            fact_count=sum(
                len(tuple(dossier.get(key) or ()))
                for key in ("material_facts", "counterfacts", "resolution_facts")
            ),
            question_count=len(tuple(dossier.get("question_family_results") or ())),
            route_receipt_count=len(tuple(dossier.get("search_route_receipts") or ())),
        )
        return self._write_latest_pointer(
            root=root,
            record=record,
            dossier=dossier,
            path=path,
        )

    def _write_latest_pointer(
        self,
        *,
        root: Path,
        record: ResearchDossierSnapshotRecord,
        dossier: Mapping[str, Any],
        path: Path,
    ) -> EffectiveDossierSnapshot:
        latest_receipt_path = root / "research_passes/effective_dossier.latest.json"
        receipt = {
            "schema_version": "e2r_pro_effective_dossier_pointer_v1",
            "job_id": record.job_id,
            "snapshot_id": record.snapshot_id,
            "pass_id": record.pass_id,
            "revision_ordinal": record.revision_ordinal,
            "parent_snapshot_id": record.parent_snapshot_id,
            "dossier_hash": record.dossier_hash,
            "relative_path": record.relative_path,
            "fact_count": record.fact_count,
            "question_count": record.question_count,
            "route_receipt_count": record.route_receipt_count,
        }
        _write_json_atomic(latest_receipt_path, receipt)
        return EffectiveDossierSnapshot(
            record=record,
            dossier=dict(dossier),
            path=path,
            latest_receipt_path=latest_receipt_path,
        )

    def load_latest(
        self, *, job_id: str, job_root: str | Path
    ) -> EffectiveDossierSnapshot | None:
        record = self.ledger.latest_dossier_snapshot(job_id)
        if record is None:
            return None
        root = Path(job_root).resolve()
        path = _resolve_runtime_path(root, record.relative_path)
        dossier = _read_hash_verified_dossier(path, record.dossier_hash)
        receipt_path = root / "research_passes/effective_dossier.latest.json"
        if not receipt_path.is_file():
            raise ValueError("latest effective dossier pointer is missing")
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        if (
            receipt.get("snapshot_id") != record.snapshot_id
            or receipt.get("dossier_hash") != record.dossier_hash
            or receipt.get("relative_path") != record.relative_path
            or (
                receipt.get("revision_ordinal") is not None
                and int(receipt.get("revision_ordinal"))
                != record.revision_ordinal
            )
        ):
            raise ValueError("effective dossier pointer differs from durable snapshot ledger")
        return EffectiveDossierSnapshot(record, dossier, path, receipt_path)

    def load_latest_for_pass(
        self,
        *,
        job_id: str,
        pass_id: str,
        job_root: str | Path,
    ) -> EffectiveDossierSnapshot | None:
        record = self.ledger.latest_dossier_snapshot_for_pass(
            job_id=job_id,
            pass_id=pass_id,
        )
        if record is None:
            return None
        root = Path(job_root).resolve()
        path = _resolve_runtime_path(root, record.relative_path)
        dossier = _read_hash_verified_dossier(path, record.dossier_hash)
        return EffectiveDossierSnapshot(
            record=record,
            dossier=dossier,
            path=path,
            latest_receipt_path=(
                root / "research_passes/effective_dossier.latest.json"
            ),
        )


def load_effective_research_dossier(job_root: str | Path) -> Mapping[str, Any]:
    """Load the latest V2 snapshot, or the immutable initial import for V1."""

    root = Path(job_root).resolve()
    pointer = root / "research_passes/effective_dossier.latest.json"
    if pointer.is_file():
        receipt = json.loads(pointer.read_text(encoding="utf-8"))
        if receipt.get("schema_version") != "e2r_pro_effective_dossier_pointer_v1":
            raise ValueError("unsupported effective dossier pointer")
        path = _resolve_runtime_path(root, str(receipt.get("relative_path") or ""))
        return _read_hash_verified_dossier(
            path,
            str(receipt.get("dossier_hash") or ""),
        )
    path = root / "import/research_dossier.normalized.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError("initial imported dossier must be a JSON object")
    return payload


def _read_hash_verified_dossier(path: Path, expected_hash: str) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping) or canonical_hash(payload) != expected_hash:
        raise ValueError("effective dossier file differs from its durable hash")
    return payload


def _resolve_runtime_path(root: Path, relative_path: str) -> Path:
    path = (root / relative_path).resolve()
    try:
        path.relative_to(root)
    except ValueError as error:
        raise ValueError("effective dossier path escapes job root") from error
    if not path.is_file():
        raise ValueError("effective dossier file is missing")
    return path


def _write_json_atomic(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_suffix(path.suffix + ".part")
    with part.open("w", encoding="utf-8") as stream:
        stream.write(canonical_json(payload) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(part, path)
    fsync_directory(path.parent)


__all__ = [
    "EffectiveDossierSnapshot",
    "ProMultiPassDossierStore",
    "load_effective_research_dossier",
]
