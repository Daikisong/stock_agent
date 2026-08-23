"""Durable same-conversation planning and deterministic repair reverification."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..atomic_io import fsync_directory
from ..dossier.validator import DossierValidationContext, ResearchDossierValidator
from ..ids import canonical_hash, canonical_json
from ..models import ProResearchJob
from ..multi_pass import (
    FollowupPassPlan,
    ProMultiPassResearchOrchestrator,
    TransportPendingDecision,
)
from ..multi_pass.models import ResearchPassStatus
from ..verification.source_verifier import ProSourceVerifier
from .delta import apply_repair_delta
from .models import (
    REVERIFIED_ACCEPTED_STATUSES,
    RepairApplication,
    RepairResolution,
    VerifierRejectionPacket,
    VerifierRepairReceipt,
)
from .rejection_packet import compile_rejection_packets
from .response_delta import derive_repair_delta_from_dossier_response


@dataclass(frozen=True)
class VerifierRepairPlan:
    rejection_packets: tuple[VerifierRejectionPacket, ...]
    followup: FollowupPassPlan | TransportPendingDecision | None
    receipt: Mapping[str, Any]


@dataclass(frozen=True)
class VerifierRepairRun:
    application: RepairApplication
    receipt: VerifierRepairReceipt
    source_verification_rows: tuple[Mapping[str, Any], ...]
    effective_dossier: Mapping[str, Any]
    repair_root: Path


class ProVerifierRepairService:
    def __init__(
        self,
        orchestrator: ProMultiPassResearchOrchestrator,
        *,
        verifier: ProSourceVerifier | None = None,
    ) -> None:
        self.orchestrator = orchestrator
        self.verifier = verifier or ProSourceVerifier()

    def plan_repair(
        self,
        *,
        job_id: str,
        job_root: str | Path,
        packet: Mapping[str, Any],
        dossier: Mapping[str, Any],
        verification_rows: Sequence[Mapping[str, Any]],
        fact_compilation_rejection_rows: Sequence[Mapping[str, Any]] = (),
        primary_archetype_ids: Sequence[str],
        existing_verified_ledger_digest: Mapping[str, Any] | None = None,
    ) -> VerifierRepairPlan:
        job = self.orchestrator.store.get_job(job_id)
        conversation_id = str(dossier.get("conversation_id") or "")
        if conversation_id != job.conversation_id:
            raise ValueError("verifier repair must reuse the durable Pro conversation")
        packets = compile_rejection_packets(
            dossier=dossier,
            verification_rows=verification_rows,
            fact_compilation_rejection_rows=fact_compilation_rejection_rows,
            job_root=job_root,
            conversation_id=conversation_id,
        )
        question_ids = {
            value for row in packets for value in row.question_family_ids
        }
        unresolved = []
        for row in dossier.get("question_family_results") or ():
            if str(row.get("question_family_id") or "") not in question_ids:
                continue
            unresolved.append(
                {
                    **dict(row),
                    "status": "VERIFIER_REPAIR_REQUIRED",
                    "closure_reason": (
                        "deterministic verifier rejected a material linked fact"
                    ),
                }
            )
        followup: FollowupPassPlan | TransportPendingDecision | None = None
        if packets:
            followup = self.orchestrator.plan_followup(
                job_id=job_id,
                packet=packet,
                primary_archetype_ids=primary_archetype_ids,
                pass_name="VERIFIER_REPAIR",
                unresolved_question_state=unresolved,
                pass_inputs={
                    "route_reason": "MATERIAL_FACT_VERIFIER_REJECTION",
                    "rejection_packets": [row.to_prompt_dict() for row in packets],
                    "deterministic_reverification_required": True,
                    "accepted_fact_deletion_allowed": False,
                },
                existing_verified_ledger_digest=(
                    existing_verified_ledger_digest or {}
                ),
            )
        repair_root = Path(job_root).resolve() / "repair"
        receipt = {
            "schema_version": "e2r_pro_verifier_repair_plan_receipt_v1",
            "status": (
                "VERIFIER_REPAIR_PLANNED" if packets else "NO_VERIFIER_REPAIR_REQUIRED"
            ),
            "job_id": job_id,
            "conversation_id": conversation_id,
            "rejection_packet_ids": [row.packet_id for row in packets],
            "rejection_packet_count": len(packets),
            "question_family_ids": sorted(question_ids),
            "research_pass_id": (
                followup.research_pass.pass_id
                if isinstance(followup, FollowupPassPlan)
                else None
            ),
            "transport_pending": isinstance(followup, TransportPendingDecision),
            "same_conversation_required": True,
            "score_valid": False,
            "publication_withheld": True,
            "score_authority": False,
            "stage_authority": False,
        }
        _write_jsonl_atomic(
            repair_root / "rejection_packets.jsonl",
            [row.to_dict() for row in packets],
        )
        _write_json_atomic(repair_root / "repair_plan_receipt.json", receipt)
        return VerifierRepairPlan(
            rejection_packets=packets,
            followup=followup,
            receipt=receipt,
        )

    def apply_and_reverify(
        self,
        *,
        job: ProResearchJob,
        job_root: str | Path,
        dossier: Mapping[str, Any],
        plan: VerifierRepairPlan,
        repair_delta: Mapping[str, Any],
        prior_verification_rows: Sequence[Mapping[str, Any]],
        prior_fact_compilation_rejection_rows: Sequence[Mapping[str, Any]] = (),
    ) -> VerifierRepairRun:
        if not isinstance(plan.followup, FollowupPassPlan):
            raise ValueError("repair reverification requires a planned research pass")
        research_pass = self.orchestrator.ledger.get_pass(
            plan.followup.research_pass.pass_id
        )
        if (
            research_pass.status != ResearchPassStatus.COMPLETE.value
            or not research_pass.response_hash
        ):
            raise ValueError("repair delta requires a completed same-conversation pass")
        if repair_delta.get("response_hash") != research_pass.response_hash:
            raise ValueError("repair delta response hash differs from durable pass")
        if repair_delta.get("research_pass_id") != research_pass.pass_id:
            raise ValueError("repair delta belongs to another durable research pass")
        if repair_delta.get("parent_pass_id") != research_pass.parent_pass_id:
            raise ValueError("repair delta parent lineage mismatch")
        prior_rejected_claim_ids = {
            str(row.get("claim_id") or "")
            for row in prior_fact_compilation_rejection_rows
        }
        prior_accepted = tuple(
            str(row.get("dossier_fact_id") or "")
            for row in prior_verification_rows
            if str(row.get("status") or "") in REVERIFIED_ACCEPTED_STATUSES
            and str(row.get("compiled_claim_id") or "")
            not in prior_rejected_claim_ids
        )
        application = apply_repair_delta(
            dossier=dossier,
            rejection_packets=plan.rejection_packets,
            repair_delta=repair_delta,
            prior_accepted_candidate_ids=prior_accepted,
        )
        _append_completed_repair_pass(
            application.effective_dossier,
            research_pass=research_pass,
        )
        verification = self.verifier.verify(
            dossier=application.effective_dossier,
            job=job,
            job_root=job_root,
        )
        verification_rows = tuple(row.to_dict() for row in verification.verifications)
        verification_by_candidate = {
            str(row.get("dossier_fact_id") or ""): row
            for row in verification_rows
        }
        compiled_claim_ids = {
            row.claim_id for row in verification.fact_compilation.claim_fact_links
        }
        compilation_rejection_by_claim = {
            row.claim_id: row for row in verification.fact_compilation.rejected_claims
        }
        preserved = tuple(
            candidate_id
            for candidate_id in prior_accepted
            if (
                str(
                    (verification_by_candidate.get(candidate_id) or {}).get(
                        "status"
                    )
                    or ""
                )
                in REVERIFIED_ACCEPTED_STATUSES
                and str(
                    (verification_by_candidate.get(candidate_id) or {}).get(
                        "compiled_claim_id"
                    )
                    or ""
                )
                in compiled_claim_ids
            )
        )
        resolutions: list[RepairResolution] = []
        unresolved = list(application.unhandled_packet_ids)
        for action in application.actions:
            if action.action == "WITHDRAWN":
                resolutions.append(
                    RepairResolution(
                        packet_id=action.packet_id,
                        candidate_id=action.candidate_id,
                        replacement_candidate_id=None,
                        action=action.action,
                        status="WITHDRAWN",
                        verifier_status=None,
                        verifier_reason="rejected candidate explicitly withdrawn",
                        resolved=True,
                    )
                )
                continue
            row = verification_by_candidate.get(
                str(action.replacement_candidate_id or "")
            )
            compiled_claim_id = str((row or {}).get("compiled_claim_id") or "")
            compilation_rejection = compilation_rejection_by_claim.get(
                compiled_claim_id
            )
            accepted = bool(
                row
                and str(row.get("status") or "") in REVERIFIED_ACCEPTED_STATUSES
                and compiled_claim_id in compiled_claim_ids
            )
            if not accepted:
                unresolved.append(action.packet_id)
            resolutions.append(
                RepairResolution(
                    packet_id=action.packet_id,
                    candidate_id=action.candidate_id,
                    replacement_candidate_id=action.replacement_candidate_id,
                    action=action.action,
                    status=(
                        "REVERIFIED_ACCEPTED" if accepted else "REVERIFIED_REJECTED"
                    ),
                    verifier_status=(
                        _compilation_rejection_status(
                            str(compilation_rejection.reason)
                        )
                        if compilation_rejection is not None
                        else str(row.get("status") or "")
                        if row
                        else None
                    ),
                    verifier_reason=(
                        str(compilation_rejection.reason)
                        if compilation_rejection is not None
                        else str(row.get("reason") or "")
                        if row
                        else "replacement candidate is absent from verifier output"
                    ),
                    resolved=accepted,
                )
            )
        unresolved_ids = tuple(dict.fromkeys(unresolved))
        effective = application.effective_dossier
        _update_effective_repair_statuses(
            effective,
            resolutions=resolutions,
            unresolved_packet_ids=unresolved_ids,
            original_research_status=str(dossier.get("research_status") or ""),
        )
        ResearchDossierValidator().validate(
            effective,
            DossierValidationContext(
                job_id=job.job_id,
                run_id=str(effective.get("run_id") or ""),
                target_id=job.symbol,
                as_of_date=job.as_of_date,
                conversation_id=research_pass.conversation_id,
                candidate_archetype_ids=job.archetype_ids,
            ),
        )
        source_verification_hash = canonical_hash(
            {
                "verification_semantics_version": self.verifier.semantics_version,
                "verifications": verification_rows,
                "fact_compilation": verification.fact_compilation.to_dict(),
            }
        )
        receipt = VerifierRepairReceipt(
            job_id=job.job_id,
            conversation_id=str(repair_delta.get("conversation_id") or ""),
            research_pass_id=research_pass.pass_id,
            parent_pass_id=str(research_pass.parent_pass_id or ""),
            rejection_packet_ids=tuple(
                row.packet_id for row in plan.rejection_packets
            ),
            resolutions=tuple(resolutions),
            unresolved_packet_ids=unresolved_ids,
            prior_accepted_candidate_ids=prior_accepted,
            preserved_accepted_candidate_ids=preserved,
            source_verification_hash=source_verification_hash,
            effective_dossier_hash=canonical_hash(effective),
            delta_hash=application.delta_hash,
        )
        repair_root = Path(job_root).resolve() / "repair"
        _write_json_atomic(repair_root / "repair_delta.json", repair_delta)
        _write_json_atomic(
            repair_root / "effective_repaired_dossier.json", effective
        )
        _write_jsonl_atomic(
            repair_root / "repair_source_verifications.jsonl",
            verification_rows,
        )
        _write_json_atomic(
            repair_root / "repair_fact_compilation_receipt.json",
            verification.fact_compilation.to_dict(),
        )
        _write_json_atomic(
            repair_root / "verifier_repair_receipt.json", receipt.to_dict()
        )
        return VerifierRepairRun(
            application=application,
            receipt=receipt,
            source_verification_rows=verification_rows,
            effective_dossier=effective,
            repair_root=repair_root,
        )

    def apply_response_dossier_and_reverify(
        self,
        *,
        job: ProResearchJob,
        job_root: str | Path,
        original_dossier: Mapping[str, Any],
        response_dossier: Mapping[str, Any],
        response_hash: str,
        plan: VerifierRepairPlan,
        prior_verification_rows: Sequence[Mapping[str, Any]],
        prior_fact_compilation_rejection_rows: Sequence[Mapping[str, Any]] = (),
    ) -> VerifierRepairRun:
        if not isinstance(plan.followup, FollowupPassPlan):
            raise ValueError("repair response requires a planned research pass")
        research_pass = self.orchestrator.ledger.get_pass(
            plan.followup.research_pass.pass_id
        )
        if response_hash != research_pass.response_hash:
            raise ValueError("captured repair response hash differs from durable pass")
        ResearchDossierValidator().validate(
            response_dossier,
            DossierValidationContext(
                job_id=job.job_id,
                run_id=str(response_dossier.get("run_id") or ""),
                target_id=job.symbol,
                as_of_date=job.as_of_date,
                conversation_id=research_pass.conversation_id,
                candidate_archetype_ids=job.archetype_ids,
            ),
        )
        repair_delta = derive_repair_delta_from_dossier_response(
            original_dossier=original_dossier,
            response_dossier=response_dossier,
            rejection_packets=plan.rejection_packets,
            response_hash=response_hash,
        )
        return self.apply_and_reverify(
            job=job,
            job_root=job_root,
            dossier=original_dossier,
            plan=plan,
            repair_delta=repair_delta,
            prior_verification_rows=prior_verification_rows,
            prior_fact_compilation_rejection_rows=(
                prior_fact_compilation_rejection_rows
            ),
        )


def _update_effective_repair_statuses(
    dossier: Mapping[str, Any],
    *,
    resolutions: Sequence[RepairResolution],
    unresolved_packet_ids: Sequence[str],
    original_research_status: str,
) -> None:
    if not isinstance(dossier, dict):
        raise TypeError("effective repair dossier must be mutable")
    status_by_packet = {row.packet_id: row.status for row in resolutions}
    for row in dossier.get("verification_repair_register") or ():
        packet_id = str(row.get("packet_id") or "")
        if packet_id in status_by_packet:
            row["status"] = status_by_packet[packet_id]
    unresolved = set(unresolved_packet_ids)
    unresolved_questions = {
        str(row.get("question_family_id") or "")
        for row in dossier.get("verification_repair_register") or ()
        if str(row.get("packet_id") or "") in unresolved
    }
    for question in dossier.get("question_family_results") or ():
        if str(question.get("question_family_id") or "") in unresolved_questions:
            question["status"] = "VERIFIER_REPAIR_REQUIRED"
            question["closure_reason"] = (
                "corrected fact did not pass deterministic reverification"
            )
    if unresolved:
        dossier["research_status"] = "NEEDS_VERIFIER_REPAIR"
    elif any(row.status == "WITHDRAWN" for row in resolutions):
        dossier["research_status"] = "NEEDS_PUBLIC_GAP_CLOSURE"
    else:
        dossier["research_status"] = original_research_status


def _compilation_rejection_status(reason: str) -> str:
    normalized = reason.upper()
    if any(value in normalized for value in ("DUPLICATE", "CYCLIC", "LINEAGE")):
        return "REJECTED_DUPLICATE_LINEAGE"
    return "REJECTED_UNSUPPORTED_DERIVATION"


def _append_completed_repair_pass(
    dossier: Mapping[str, Any], *, research_pass: Any
) -> None:
    if not isinstance(dossier, dict):
        raise TypeError("effective repair dossier must be mutable")
    rows = dossier.setdefault("research_passes", [])
    existing = next(
        (
            row
            for row in rows
            if str(row.get("pass_id") or "") == research_pass.pass_id
        ),
        None,
    )
    payload = {
        "pass_id": research_pass.pass_id,
        "parent_pass_id": research_pass.parent_pass_id,
        "pass_name": "VERIFIER_REPAIR",
        "status": "COMPLETE",
        "prompt_hash": research_pass.prompt_hash,
        "response_hash": research_pass.response_hash,
        "conversation_id": research_pass.conversation_id,
    }
    if existing is None:
        rows.append(payload)
    elif dict(existing) != payload:
        raise ValueError("repair dossier pass ledger differs from durable research pass")


def _write_json_atomic(path: Path, payload: Mapping[str, Any]) -> None:
    _write_atomic(path, canonical_json(payload) + "\n")


def _write_jsonl_atomic(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    _write_atomic(path, "".join(canonical_json(row) + "\n" for row in rows))


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
    "ProVerifierRepairService",
    "VerifierRepairPlan",
    "VerifierRepairRun",
]
