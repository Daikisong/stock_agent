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
        failed_replacements = tuple(
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
        _withdraw_failed_replacements(
            effective,
            failed_replacement_ids=failed_replacements,
        )
        _resolve_local_reverification_routes(
            effective,
            application=application,
            verification_by_candidate=by_candidate,
        )
        _resolve_question_states_after_reverification(
            effective,
            application=application,
            verification_by_candidate=by_candidate,
            failed_replacement_ids=failed_replacements,
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
        unresolved_replacements: tuple[str, ...] = ()
        operational_ready_allowed = not (
            prior_accepted_not_preserved or repair_pass_ordinal != 1
        )
        receipt_payload = {
            "schema_version": "e2r_compact_repair_v3_receipt_v1",
            "status": (
                "COMPACT_REPAIR_REVERIFIED_WITH_FAILED_REPLACEMENTS_WITHDRAWN"
                if operational_ready_allowed and failed_replacements
                else "COMPACT_REPAIR_REVERIFIED"
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
            "reverification_failed_replacement_candidate_ids": list(
                failed_replacements
            ),
            "failed_replacement_withdrawn_candidate_ids": list(
                failed_replacements
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
            "local_reverification_route_success_count": sum(
                1
                for row in effective.get("search_route_receipts") or ()
                if str(row.get("route_receipt_id") or "").startswith(
                    "PROREPAIRROUTE-"
                )
                and row.get("pass_id") == compiled_prompt.research_pass_id
                and row.get("provider_status") == "SUCCESS"
            ),
            "local_reverification_route_pending_count": sum(
                1
                for row in effective.get("search_route_receipts") or ()
                if str(row.get("route_receipt_id") or "").startswith(
                    "PROREPAIRROUTE-"
                )
                and row.get("pass_id") == compiled_prompt.research_pass_id
                and row.get("provider_status") != "SUCCESS"
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


def reconcile_completed_repair_fail_closed(
    *,
    repaired_dossier: Mapping[str, Any],
    parent_dossier: Mapping[str, Any],
    repair_delta: Mapping[str, Any],
    failed_replacement_ids: Sequence[str],
) -> tuple[Mapping[str, Any], Mapping[str, Any]]:
    """Append-only rematerialization for a completed pre-fix repair snapshot."""

    pass_id = str(repaired_dossier.get("research_pass_id") or "")
    parent_pass_id = str(repaired_dossier.get("parent_pass_id") or "")
    if (
        repair_delta.get("research_pass_id") != pass_id
        or repair_delta.get("parent_pass_id") != parent_pass_id
        or parent_dossier.get("research_pass_id") != parent_pass_id
    ):
        raise ValueError("completed repair reconciliation lineage mismatch")
    failed = {str(value) for value in failed_replacement_ids}
    replacement_ids = {
        str((row.get("replacement_fact") or {}).get("dossier_fact_id") or "")
        for row in repair_delta.get("repair_actions") or ()
        if isinstance(row.get("replacement_fact"), Mapping)
    }
    if not failed or not failed.issubset(replacement_ids):
        raise ValueError("completed repair reconciliation failure roster mismatch")
    retained = replacement_ids - failed
    locally_accepted = {
        str(value)
        for row in repaired_dossier.get("search_route_receipts") or ()
        if row.get("pass_id") == pass_id
        and row.get("provider_status") == "SUCCESS"
        for value in row.get("accepted_fact_ids") or ()
    }
    if not retained.issubset(locally_accepted):
        raise ValueError(
            "completed repair reconciliation cannot retain an unverified replacement"
        )

    effective = deepcopy(dict(repaired_dossier))
    before_hash = canonical_hash(effective)
    _withdraw_failed_replacements(
        effective,
        failed_replacement_ids=tuple(sorted(failed)),
    )
    prior_questions = {
        str(row.get("question_family_id") or ""): row
        for row in parent_dossier.get("question_family_results") or ()
    }
    affected_question_ids = {
        str(value)
        for row in repair_delta.get("repair_actions") or ()
        for value in row.get("question_family_ids") or ()
    }
    restored_question_ids: list[str] = []
    for question in effective.get("question_family_results") or ():
        question_id = str(question.get("question_family_id") or "")
        prior = prior_questions.get(question_id)
        if (
            question_id not in affected_question_ids
            or prior is None
            or str(prior.get("status") or "") not in TERMINAL_STATUSES
        ):
            continue
        for field in (
            "status",
            "availability_class",
            "adequate_search_proven",
            "closure_reason",
        ):
            if field in prior:
                question[field] = deepcopy(prior[field])
        restored_question_ids.append(question_id)
    effective["research_status"] = compile_dossier_v2_closure_summary(
        effective
    ).expected_research_status
    after_hash = canonical_hash(effective)
    receipt_payload = {
        "schema_version": "e2r_completed_compact_repair_reconciliation_v1",
        "status": "FAILED_REPLACEMENTS_WITHDRAWN_APPEND_ONLY",
        "job_id": str(effective.get("job_id") or ""),
        "research_pass_id": pass_id,
        "parent_pass_id": parent_pass_id,
        "before_effective_dossier_hash": before_hash,
        "after_effective_dossier_hash": after_hash,
        "failed_replacement_ids": sorted(failed),
        "retained_locally_verified_replacement_ids": sorted(retained),
        "restored_terminal_question_ids": sorted(restored_question_ids),
        "new_query_count": 0,
        "new_search_count": 0,
        "new_pro_submit_count": 0,
        "score_authority": False,
        "stage_authority": False,
    }
    return effective, {
        **receipt_payload,
        "receipt_hash": canonical_hash(receipt_payload),
    }


def _resolve_question_states_after_reverification(
    dossier: dict[str, Any],
    *,
    application: RepairApplicationV3,
    verification_by_candidate: Mapping[str, Mapping[str, Any]],
    failed_replacement_ids: Sequence[str] = (),
) -> None:
    failed = {str(value) for value in failed_replacement_ids}
    outcomes_by_question: dict[str, list[Any]] = {}
    for outcome in application.outcomes:
        for question_id in outcome.question_family_ids:
            outcomes_by_question.setdefault(question_id, []).append(outcome)
    for question in dossier.get("question_family_results") or ():
        question_id = str(question.get("question_family_id") or "")
        outcomes = outcomes_by_question.get(question_id) or ()
        if not outcomes:
            continue
        all_retained_replacements_accepted = all(
            row.action == "WITHDRAW"
            or str(row.replacement_candidate_id or "") in failed
            or (
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
            )
            for row in outcomes
        )
        prior = application.prior_question_states.get(question_id) or {}
        prior_status = str(prior.get("status") or "")
        if (
            all_retained_replacements_accepted
            and prior_status in TERMINAL_STATUSES
        ):
            for field in (
                "status",
                "availability_class",
                "adequate_search_proven",
                "closure_reason",
            ):
                if field in prior:
                    question[field] = deepcopy(prior[field])
        elif any(
            row.action == "WITHDRAW"
            or str(row.replacement_candidate_id or "") in failed
            for row in outcomes
        ):
            question["status"] = "PUBLIC_SEARCHABLE"
            question["availability_class"] = "PUBLIC_SEARCHABLE"
            question["adequate_search_proven"] = False
            question["closure_reason"] = (
                "one or more rejected facts were withdrawn from a nonterminal question"
            )
        else:
            question["status"] = "VERIFIER_REPAIR_REQUIRED"
            question["closure_reason"] = (
                "compact replacement failed deterministic reverification"
                if not all_retained_replacements_accepted
                else "prior question state was not terminal"
            )


def _withdraw_failed_replacements(
    dossier: dict[str, Any],
    *,
    failed_replacement_ids: Sequence[str],
) -> None:
    failed = {str(value) for value in failed_replacement_ids}
    if not failed:
        return
    for collection in ("material_facts", "counterfacts", "resolution_facts"):
        dossier[collection] = [
            row
            for row in dossier.get(collection) or ()
            if str(row.get("dossier_fact_id") or "") not in failed
        ]
    for lineage in dossier.get("source_lineages") or ():
        lineage["fact_ids"] = [
            str(value)
            for value in lineage.get("fact_ids") or ()
            if str(value) not in failed
        ]
    dropped_route_ids: set[str] = set()
    retained_routes: list[Mapping[str, Any]] = []
    for route in dossier.get("search_route_receipts") or ():
        accepted = [
            str(value)
            for value in route.get("accepted_fact_ids") or ()
            if str(value) not in failed
        ]
        if not accepted and str(route.get("route_receipt_id") or "").startswith(
            "PROREPAIRROUTE-"
        ):
            dropped_route_ids.add(str(route.get("route_receipt_id") or ""))
            continue
        route["accepted_fact_ids"] = accepted
        retained_routes.append(route)
    dossier["search_route_receipts"] = retained_routes
    for question in dossier.get("question_family_results") or ():
        for field in ("support_fact_ids", "counter_fact_ids", "resolution_fact_ids"):
            question[field] = [
                str(value)
                for value in question.get(field) or ()
                if str(value) not in failed
            ]
        question["search_route_receipt_ids"] = [
            str(value)
            for value in question.get("search_route_receipt_ids") or ()
            if str(value) not in dropped_route_ids
        ]
    dossier["derived_metrics"] = [
        row
        for row in dossier.get("derived_metrics") or ()
        if not failed.intersection(
            {str(value) for value in row.get("input_fact_ids") or ()}
        )
    ]


def _resolve_local_reverification_routes(
    dossier: dict[str, Any],
    *,
    application: RepairApplicationV3,
    verification_by_candidate: Mapping[str, Mapping[str, Any]],
) -> None:
    replacement_ids = set(application.replacement_candidate_ids)
    for route in dossier.get("search_route_receipts") or ():
        if not str(route.get("route_receipt_id") or "").startswith(
            "PROREPAIRROUTE-"
        ):
            continue
        accepted_ids = {
            str(value) for value in route.get("accepted_fact_ids") or ()
        }
        if not accepted_ids or not accepted_ids.issubset(replacement_ids):
            continue
        all_accepted = all(
            str((verification_by_candidate.get(value) or {}).get("status") or "")
            in ACCEPTED_SOURCE_STATUSES
            for value in accepted_ids
        )
        route["provider_status"] = "SUCCESS" if all_accepted else "FAILED"
        route["no_new_route_reason"] = (
            None
            if all_accepted
            else "Deterministic local source re-verification did not accept the fact"
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


__all__ = [
    "CompactRepairRunV3",
    "CompactRepairServiceV3",
    "reconcile_completed_repair_fail_closed",
]
