"""Durable GAP_ADJUDICATION handoff into supplemental or component work."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, Mapping, Sequence

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

if TYPE_CHECKING:
    from ..saturation.models import ResearchSaturationReceipt


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
        verified_dossier: Mapping[str, Any] | None = None,
        prior_dispositions=(),
    ) -> GapAdjudicationRun:
        root = Path(job_root).resolve()
        gap_root = root / "gaps"
        receipt_path = gap_root / "gap_adjudication_receipt.json"
        job = self.store.get_job(job_id)
        legacy_component_recovery = False
        if job.status != JobStatus.GAP_ADJUDICATION.value:
            durable = self.store.get_gap_decisions(job_id)
            if (
                job.status == JobStatus.COMPONENT_RESEARCH.value
                and not receipt_path.is_file()
                and not durable
            ):
                # Older fresh full-thesis code moved directly through the
                # saturation gate before writing the mandatory gap ledger.
                # The store independently verifies that exact historical
                # transition and that no scoring output exists before it
                # permits this in-place recovery.
                legacy_component_recovery = True
            elif job.status not in {
                JobStatus.SUPPLEMENTAL_RESEARCH.value,
                JobStatus.COMPONENT_RESEARCH.value,
                JobStatus.JUDGING.value,
                JobStatus.SCORING.value,
                JobStatus.STAGECOURT.value,
                JobStatus.FINAL.value,
            } or not receipt_path.is_file():
                raise ValueError("job is outside the durable gap-adjudication boundary")
            else:
                receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
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
        dossier = (
            dict(verified_dossier)
            if verified_dossier is not None
            else _read_json(normalized_path)
        )
        verification_receipt = _read_json(
            verification_root / "source_verification_receipt.json"
        )
        durable_verification = self.store.get_source_verification_receipt(job_id)
        if verification_receipt != durable_verification:
            raise ValueError("source verification receipt differs from durable ledger")
        if (
            verification_receipt.get("dossier_id") != job.dossier_id
            or (
                verification_receipt.get("effective_dossier_hash")
                or verification_receipt.get("normalized_dossier_hash")
            )
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
            "legacy_saturation_gate_recovery": legacy_component_recovery,
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
            recover_legacy_component_transition=legacy_component_recovery,
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


def compile_saturated_gap_contexts(
    *,
    dossier: Mapping[str, Any],
    saturation: ResearchSaturationReceipt,
) -> Mapping[str, DeterministicGapContext]:
    """Bind append-only V3 gap rows to the latest deterministic closure.

    Pro gap labels are historical proposals, not authority.  A gap is
    nonblocking here only when the exact question has a current ready/NO_GAP
    decision in a valid saturation receipt.  The zero delta records that this
    *historical row* has no remaining score or Stage effect; it does not award
    points or calculate Stage.
    """

    if not (
        saturation.research_saturation_valid
        and saturation.component_entry_allowed
    ):
        raise ValueError("saturated gap contexts require a valid component gate")
    decisions_by_question = {
        row.question_family_id: row for row in saturation.question_decisions
    }
    if len(decisions_by_question) != len(saturation.question_decisions):
        raise ValueError("saturation receipt contains duplicate question decisions")

    contexts: dict[str, DeterministicGapContext] = {}
    for gap in dossier.get("unresolved_gaps") or ():
        gap_id = str(gap.get("dossier_gap_id") or gap.get("gap_id") or "")
        question_id = str(gap.get("question_family_id") or "")
        if not gap_id or gap_id in contexts or not question_id:
            raise ValueError("saturated dossier gaps require unique ids and questions")
        decision = decisions_by_question.get(question_id)
        if decision is None:
            raise ValueError("dossier gap lacks an exact saturation question decision")
        if not decision.ready or decision.gap_class != "NO_GAP":
            raise ValueError("nonterminal or material saturation gap cannot be bypassed")

        affected = tuple(
            dict.fromkeys(
                str(value)
                for value in gap.get("affected_component_ids") or ()
                if str(value)
            )
        )
        required_roles = tuple(decision.required_source_roles)
        verified_roles = tuple(
            value
            for value in required_roles
            if value in set(decision.verified_source_roles)
        )
        contexts[gap_id] = DeterministicGapContext(
            dossier_gap_id=gap_id,
            component_lower_delta={value: 0.0 for value in affected},
            component_upper_delta={value: 0.0 for value in affected},
            executable_new_source_route_signatures=(),
            could_change_score=False,
            monitoring_only=True,
            official_first_attempted=(
                decision.route_adequacy.official_route_attempted
            ),
            question_family_id=question_id,
            mandatory_primary_source_roles=required_roles,
            verified_primary_source_roles=verified_roles,
            missing_route_is_independent_corroboration=False,
            missing_predicate_is_new_core=False,
            public_route_fixpoint_reached=(
                decision.route_adequacy.semantic_fixpoint
            ),
            hard_break_polarity_resolved=True,
            score_stage_range_bounded=True,
            rationale=(
                "latest deterministic full-thesis receipt marks the exact "
                "question ready with NO_GAP; the append-only Pro gap row is "
                "retained for audit only and has zero remaining score/Stage effect"
            ),
        )
    return contexts

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


__all__ = [
    "GapAdjudicationRun",
    "ProGapAdjudicationService",
    "compile_saturated_gap_contexts",
]
