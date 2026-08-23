from __future__ import annotations

from typing import Any, Mapping, Sequence

from e2r.pro_first.ids import canonical_hash
from e2r.pro_first.models import ProResearchJob
from e2r.pro_first.research_contracts import select_contract_bundle


def v2_scoring_dossier(
    base: Mapping[str, Any],
    *,
    job: ProResearchJob,
    selected_archetype_ids: Sequence[str],
) -> dict[str, Any]:
    selected = list(dict.fromkeys(str(value) for value in selected_archetype_ids))
    return {
        **dict(base),
        "schema_version": "e2r_pro_research_dossier_v2",
        "job_id": job.job_id,
        "run_id": f"RUN-{job.job_id}",
        "conversation_id": f"CONVERSATION-{job.job_id}",
        "research_pass_id": f"PASS-{job.job_id}",
        "parent_pass_id": None,
        "target": {
            "target_id": job.symbol,
            "symbol": job.symbol,
            "company_name": job.company_name,
        },
        "as_of_date": job.as_of_date,
        "candidate_archetypes": list(job.archetype_ids),
        "selected_archetypes": selected,
        "research_status": "COMPLETE",
    }


def passing_research_saturation_receipt(
    *,
    job: ProResearchJob,
    dossier: Mapping[str, Any],
    selected_archetype_ids: Sequence[str],
) -> Mapping[str, Any]:
    selected = tuple(dict.fromkeys(str(value) for value in selected_archetype_ids))
    bundle = select_contract_bundle(selected)
    questions = tuple(
        (str(contract["archetype_id"]), str(question["question_family_id"]))
        for contract in bundle.contracts
        for question in contract["question_families"]
        if question.get("mandatory_for_full_thesis") is True
    )
    decisions = [
        {
            "archetype_id": archetype_id,
            "question_family_id": question_id,
            "mandatory": True,
            "status": "SUPPORTED_SCORING",
            "deterministic_status": "SUPPORTED_SCORING",
            "terminal": True,
            "ready": True,
            "materiality": "CORE_SCORE",
            "gap_class": "NO_GAP",
            "component_ids": [],
            "required_source_roles": ["ISSUER_OFFICIAL"],
            "verified_source_roles": ["ISSUER_OFFICIAL"],
            "missing_core_source_roles": [],
            "missing_corroboration_source_roles": [],
            "linked_fact_ids": [],
            "verified_linked_fact_ids": [],
            "linked_source_lineage_ids": [],
            "question_to_source_linkage_complete": True,
            "availability": {"monitoring_only": False},
            "failure_codes": [],
        }
        for archetype_id, question_id in questions
    ]
    payload = {
        "schema_version": "e2r_pro_research_saturation_receipt_v2",
        "status": "FULL_THESIS_READY",
        "job_id": job.job_id,
        "run_id": str(dossier.get("run_id") or f"RUN-{job.job_id}"),
        "target_id": job.symbol,
        "as_of_date": job.as_of_date,
        "conversation_id": str(
            dossier.get("conversation_id") or f"CONVERSATION-{job.job_id}"
        ),
        "selected_archetype_ids": list(selected),
        "selected_contract_ids": list(bundle.contract_ids),
        "question_decisions": decisions,
        "expected_mandatory_question_ids": [question_id for _arch, question_id in questions],
        "missing_mandatory_question_ids": [],
        "nonterminal_mandatory_question_ids": [],
        "public_material_gap_question_ids": [],
        "verifier_repair_pending_ids": [],
        "provider_parser_core_pending_question_ids": [],
        "lifecycle_hard_break_pending_ids": [],
        "source_linkage_incomplete_question_ids": [],
        "likely_nonpublic_question_ids": [],
        "deterministic_research_status": "COMPLETE",
        "pro_claimed_research_status": str(dossier.get("research_status") or ""),
        "pro_status_diverged": False,
        "fact_snapshot_hash": canonical_hash(dossier.get("material_facts") or []),
        "accepted_lineage_roster_hash": canonical_hash(
            dossier.get("source_lineages") or []
        ),
        "research_saturation_valid": True,
        "component_entry_allowed": True,
        "score_authority": False,
        "stage_authority": False,
    }
    return {**payload, "receipt_hash": canonical_hash(payload)}


__all__ = [
    "passing_research_saturation_receipt",
    "v2_scoring_dossier",
]
