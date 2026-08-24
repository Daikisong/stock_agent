"""Apply one compact V3 repair, reverify it, and persist deterministic receipts."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
import os
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..atomic_io import fsync_directory
from ..dossier import DossierValidationContext, ResearchDossierValidator
from ..dossier.v2 import compile_dossier_v2_closure_summary
from ..ids import canonical_hash, canonical_json
from ..models import ProResearchJob
from ..preflight import LocalEvidencePreflightService
from ..research_contracts.validator import TERMINAL_STATUSES
from ..verification import ProSourceVerifier
from ..verification.source_verifier import ACCEPTED_SOURCE_STATUSES
from .delta_v3 import apply_repair_delta_v3
from .models_v3 import (
    CompiledCompactRepairPromptV3,
    RepairApplicationV3,
)


@dataclass(frozen=True)
class CompactRepairRunV3:
    application: RepairApplicationV3
    effective_dossier: Mapping[str, Any]
    source_verification_rows: tuple[Mapping[str, Any], ...]
    receipt: Mapping[str, Any]
    repair_root: Path


class CompactRepairServiceV3:
    def __init__(
        self,
        *,
        verifier: ProSourceVerifier | None = None,
        preflight_service: LocalEvidencePreflightService | None = None,
        dossier_validator: ResearchDossierValidator | None = None,
    ) -> None:
        self.verifier = verifier or ProSourceVerifier()
        self.preflight_service = preflight_service or LocalEvidencePreflightService(
            page_fetcher=self.verifier.page_fetcher
        )
        self.dossier_validator = dossier_validator or ResearchDossierValidator()

    def apply_and_reverify(
        self,
        *,
        job: ProResearchJob,
        job_root: str | Path,
        dossier: Mapping[str, Any],
        repair_delta: Mapping[str, Any],
        compiled_prompt: CompiledCompactRepairPromptV3,
        prior_verification_rows: Sequence[Mapping[str, Any]],
        response_hash: str,
        repair_pass_ordinal: int = 1,
    ) -> CompactRepairRunV3:
        prior_accepted = tuple(
            str(row.get("dossier_fact_id") or "")
            for row in prior_verification_rows
            if str(row.get("status") or "") in ACCEPTED_SOURCE_STATUSES
        )
        application = apply_repair_delta_v3(
            dossier=dossier,
            repair_delta=repair_delta,
            compiled_prompt=compiled_prompt,
            prior_accepted_candidate_ids=prior_accepted,
            prompt_hash=compiled_prompt.prompt_hash,
            response_hash=response_hash,
            repair_pass_ordinal=repair_pass_ordinal,
            dossier_validator=self.dossier_validator,
        )
        root = Path(job_root).resolve()
        preflight = self.preflight_service.run(
            dossier=application.effective_dossier,
            target_id=job.symbol,
            company_name=job.company_name,
            target_aliases=tuple(
                (application.effective_dossier.get("target") or {}).get("aliases")
                or ()
            ),
            as_of_date=job.as_of_date,
            archetype_ids=job.archetype_ids,
            job_root=root,
        )
        verification = self.verifier.verify(
            dossier=preflight.verifier_dossier,
            job=job,
            job_root=root,
            preflight=preflight,
        )
        rows = tuple(row.to_dict() for row in verification.verifications)
        by_candidate = {
            str(row.get("dossier_fact_id") or ""): row for row in rows
        }
        unresolved_replacements = tuple(
            candidate_id
            for candidate_id in application.replacement_candidate_ids
            if str((by_candidate.get(candidate_id) or {}).get("status") or "")
            not in ACCEPTED_SOURCE_STATUSES
        )
        prior_accepted_not_preserved = tuple(
            candidate_id
            for candidate_id in application.prior_accepted_candidate_ids
            if str((by_candidate.get(candidate_id) or {}).get("status") or "")
            not in ACCEPTED_SOURCE_STATUSES
        )

        effective = deepcopy(dict(application.effective_dossier))
        _resolve_question_states_after_reverification(
            effective,
            application=application,
            verification_by_candidate=by_candidate,
        )
        closure = compile_dossier_v2_closure_summary(effective)
        effective["research_status"] = closure.expected_research_status
        self.dossier_validator.validate(
            effective,
            DossierValidationContext(
                job_id=job.job_id,
                run_id=str(effective.get("run_id") or ""),
                target_id=job.symbol,
                as_of_date=job.as_of_date,
                conversation_id=job.conversation_id,
                candidate_archetype_ids=job.archetype_ids,
                research_pass_id=compiled_prompt.research_pass_id,
                parent_pass_id=compiled_prompt.parent_pass_id,
                enforce_parent_pass_id=True,
            ),
        )
        operational_ready_allowed = not (
            unresolved_replacements
            or prior_accepted_not_preserved
            or repair_pass_ordinal != 1
        )
        receipt_payload = {
            "schema_version": "e2r_compact_repair_v3_receipt_v1",
            "status": (
                "COMPACT_REPAIR_REVERIFIED"
                if operational_ready_allowed
                else "COMPACT_REPAIR_UNRESOLVED"
            ),
            "job_id": job.job_id,
            "conversation_id": job.conversation_id,
            "research_pass_id": compiled_prompt.research_pass_id,
            "parent_pass_id": compiled_prompt.parent_pass_id,
            "repair_pass_ordinal": repair_pass_ordinal,
            "prompt_hash": compiled_prompt.prompt_hash,
            "response_hash": response_hash,
            "delta_hash": application.delta_hash,
            "effective_dossier_hash": canonical_hash(effective),
            "preflight_receipt_hash": preflight.receipt.get("receipt_hash"),
            "source_verification_hash": canonical_hash(rows),
            "action_count": len(application.outcomes),
            "replacement_candidate_ids": list(
                application.replacement_candidate_ids
            ),
            "withdrawn_candidate_ids": [
                row.candidate_id
                for row in application.outcomes
                if row.action == "WITHDRAW"
            ],
            "unresolved_replacement_candidate_ids": list(
                unresolved_replacements
            ),
            "prior_accepted_candidate_ids": list(
                application.prior_accepted_candidate_ids
            ),
            "preserved_accepted_candidate_ids": list(
                application.preserved_accepted_candidate_ids
            ),
            "prior_accepted_reverification_failures": list(
                prior_accepted_not_preserved
            ),
            "full_dossier_reoutput_count": 0,
            "query_count": 0,
            "search_count": 0,
            "second_repair_pass_blocked": repair_pass_ordinal != 1,
            "operational_ready_allowed": operational_ready_allowed,
            "score_authority": False,
            "stage_authority": False,
        }
        receipt = {
            **receipt_payload,
            "receipt_hash": canonical_hash(receipt_payload),
        }
        repair_root = root / "repair_v3"
        _write_atomic(
            repair_root / "compact_repair_prompt.md",
            compiled_prompt.prompt_text,
        )
        _write_atomic(
            repair_root / "compact_repair_prompt_receipt.json",
            canonical_json(compiled_prompt.to_receipt()) + "\n",
        )
        _write_atomic(
            repair_root / "repair_delta_v3.json",
            canonical_json(repair_delta) + "\n",
        )
        _write_atomic(
            repair_root / "repair_actions.jsonl",
            "".join(
                canonical_json(row.to_dict()) + "\n"
                for row in application.outcomes
            ),
        )
        _write_atomic(
            repair_root / "reverification_rows.jsonl",
            "".join(canonical_json(row) + "\n" for row in rows),
        )
        _write_atomic(
            repair_root / "research_dossier.repaired.json",
            canonical_json(effective) + "\n",
        )
        _write_atomic(
            repair_root / "compact_repair_receipt.json",
            canonical_json(receipt) + "\n",
        )
        return CompactRepairRunV3(
            application=application,
            effective_dossier=effective,
            source_verification_rows=rows,
            receipt=receipt,
            repair_root=repair_root,
        )


def _resolve_question_states_after_reverification(
    dossier: dict[str, Any],
    *,
    application: RepairApplicationV3,
    verification_by_candidate: Mapping[str, Mapping[str, Any]],
) -> None:
    outcomes_by_question: dict[str, list[Any]] = {}
    for outcome in application.outcomes:
        for question_id in outcome.question_family_ids:
            outcomes_by_question.setdefault(question_id, []).append(outcome)
    for question in dossier.get("question_family_results") or ():
        question_id = str(question.get("question_family_id") or "")
        outcomes = outcomes_by_question.get(question_id) or ()
        if not outcomes:
            continue
        if any(row.action == "WITHDRAW" for row in outcomes):
            question["status"] = "PUBLIC_SEARCHABLE"
            question["availability_class"] = "PUBLIC_SEARCHABLE"
            question["adequate_search_proven"] = False
            question["closure_reason"] = (
                "one or more rejected facts were withdrawn; public gap reopened"
            )
            continue
        all_accepted = all(
            row.replacement_candidate_id is not None
            and str(
                (
                    verification_by_candidate.get(
                        str(row.replacement_candidate_id)
                    )
                    or {}
                ).get("status")
                or ""
            )
            in ACCEPTED_SOURCE_STATUSES
            for row in outcomes
        )
        prior = application.prior_question_states.get(question_id) or {}
        prior_status = str(prior.get("status") or "")
        if all_accepted and prior_status in TERMINAL_STATUSES:
            for field in (
                "status",
                "availability_class",
                "adequate_search_proven",
                "closure_reason",
            ):
                if field in prior:
                    question[field] = deepcopy(prior[field])
        else:
            question["status"] = "VERIFIER_REPAIR_REQUIRED"
            question["closure_reason"] = (
                "compact replacement failed deterministic reverification"
                if not all_accepted
                else "prior question state was not terminal"
            )


def _write_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_suffix(path.suffix + f".{os.getpid()}.part")
    try:
        with part.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(part, path)
        fsync_directory(path.parent)
    finally:
        part.unlink(missing_ok=True)


__all__ = ["CompactRepairRunV3", "CompactRepairServiceV3"]
