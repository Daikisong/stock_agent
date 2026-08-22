"""Durable GAP_ADJUDICATION handoff into supplemental or component work."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..atomic_io import fsync_directory
from ..ids import canonical_hash, canonical_json
from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob
from .adjudicator import (
    DeterministicGapContext,
    GapAdjudicationResult,
    ProGapAdjudicator,
)
from .supplemental_planner import (
    MaterialGapSupplementalPlanner,
    SupplementalPlan,
)


@dataclass(frozen=True)
class GapAdjudicationRun:
    job: ProResearchJob
    adjudication: GapAdjudicationResult | None
    supplemental_plan: SupplementalPlan | None
    receipt: Mapping[str, Any]
    gap_root: Path


class ProGapAdjudicationService:
    def __init__(
        self,
        store: ProFirstJobStore,
        *,
        adjudicator: ProGapAdjudicator | None = None,
        planner: MaterialGapSupplementalPlanner | None = None,
    ) -> None:
        self.store = store
        self.adjudicator = adjudicator or ProGapAdjudicator()
        self.planner = planner or MaterialGapSupplementalPlanner()

    def adjudicate_job(
        self,
        job_id: str,
        *,
        job_root: str | Path,
        deterministic_contexts: Mapping[str, DeterministicGapContext],
        prior_dispositions=(),
    ) -> GapAdjudicationRun:
        root = Path(job_root).resolve()
        gap_root = root / "gaps"
        receipt_path = gap_root / "gap_adjudication_receipt.json"
        job = self.store.get_job(job_id)
        if job.status != JobStatus.GAP_ADJUDICATION.value:
            if job.status not in {
                JobStatus.SUPPLEMENTAL_RESEARCH.value,
                JobStatus.COMPONENT_RESEARCH.value,
            } or not receipt_path.is_file():
                raise ValueError("job is outside the durable gap-adjudication boundary")
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            durable = self.store.get_gap_decisions(job_id)
            if tuple(receipt.get("decision_hashes") or ()) != tuple(
                row.get("decision_hash") for row in durable
            ):
                raise ValueError("gap decision files differ from the durable ledger")
            return GapAdjudicationRun(
                job=job,
                adjudication=None,
                supplemental_plan=None,
                receipt=receipt,
                gap_root=gap_root,
            )
        if not job.dossier_id:
            raise ValueError("gap adjudication requires an imported dossier")
        normalized_path = root / "import/research_dossier.normalized.json"
        verification_root = root / "verification"
        dossier = _read_json(normalized_path)
        verification_receipt = _read_json(
            verification_root / "source_verification_receipt.json"
        )
        durable_verification = self.store.get_source_verification_receipt(job_id)
        if verification_receipt != durable_verification:
            raise ValueError("source verification receipt differs from durable ledger")
        if (
            verification_receipt.get("dossier_id") != job.dossier_id
            or verification_receipt.get("normalized_dossier_hash")
            != canonical_hash(dossier)
        ):
            raise ValueError("gap adjudication dossier lineage is inconsistent")
        verified_facts = _read_jsonl(verification_root / "evidence_facts.jsonl")
        claim_fact_links = _read_jsonl(
            verification_root / "claim_fact_links.jsonl"
        )
        adjudication = self.adjudicator.adjudicate(
            dossier=dossier,
            job=job,
            verified_facts=verified_facts,
            claim_fact_links=claim_fact_links,
            deterministic_contexts=deterministic_contexts,
            prior_dispositions=prior_dispositions,
        )
        plan = self.planner.plan(adjudication=adjudication, job=job)
        decisions = [row.to_dict() for row in adjudication.decisions]
        tasks = [row.to_dict() for row in plan.tasks]
        decision_hashes = [str(row["decision_hash"]) for row in decisions]
        next_status = (
            JobStatus.SUPPLEMENTAL_RESEARCH.value
            if tasks
            else JobStatus.COMPONENT_RESEARCH.value
        )
        receipt = {
            **adjudication.receipt_payload,
            "job_id": job_id,
            "dossier_id": job.dossier_id,
            "source_verification_id": verification_receipt.get("verification_id"),
            "source_verification_hash": verification_receipt.get("verification_hash"),
            "decision_hashes": decision_hashes,
            "supplemental_task_count": len(tasks),
            "prohibited_gap_task_count": plan.receipt_payload[
                "prohibited_gap_task_count"
            ],
            "deterministic_query_template_count": plan.receipt_payload[
                "deterministic_query_template_count"
            ],
            "supplemental_plan_hash": canonical_hash(tasks),
            "next_status": next_status,
        }
        self._write_jsonl_atomic(gap_root / "gap_decisions.jsonl", decisions)
        self._write_jsonl_atomic(gap_root / "supplemental_tasks.jsonl", tasks)
        self._write_json_atomic(receipt_path, receipt)
        completed = self.store.record_gap_adjudication(
            job_id,
            expected_version=job.state_version,
            dossier_id=job.dossier_id,
            decisions=decisions,
            receipt=receipt,
            actor="pro-gap-adjudicator",
            idempotency_key=f"gap-adjudicated:{canonical_hash(receipt)}",
        )
        return GapAdjudicationRun(
            job=completed,
            adjudication=adjudication,
            supplemental_plan=plan,
            receipt=receipt,
            gap_root=gap_root,
        )

    @staticmethod
    def _write_json_atomic(path: Path, payload: Mapping[str, Any]) -> None:
        _write_atomic(path, canonical_json(payload) + "\n")

    @staticmethod
    def _write_jsonl_atomic(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
        _write_atomic(
            path,
            "".join(canonical_json(row) + "\n" for row in rows),
        )


def _read_json(path: Path) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"expected JSON object: {path}")
    return payload


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def _write_atomic(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_suffix(path.suffix + ".part")
    with part.open("w", encoding="utf-8") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(part, path)
    fsync_directory(path.parent)


__all__ = ["GapAdjudicationRun", "ProGapAdjudicationService"]
