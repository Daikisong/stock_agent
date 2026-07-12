"""Execute bounded LLM-planned source research for a full-thesis dossier."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl
from e2r.research_brain.intelligence_schema import (
    AcceptedClaimPredicate,
    EvidenceRecipe,
)
from e2r.research_brain.planning import QuestionQueryProvider
from e2r.research_brain.runtime.live_materialization import (
    CurrentQuestionSourceTaskMaterializer,
    CurrentSourceAcquisitionOrchestrator,
    SourceAcquisitionConfig,
    SourceTaskMaterializationConfig,
    write_source_acquisition_run,
)

from .orchestrator import DossierTarget


SOURCE_RESEARCH_SCHEMA_VERSION = "e2r_dossier_source_research_v1"
_ADEQUACY_ROUTE_CATEGORIES = {
    "OFFICIAL",
    "ISSUER_IR",
    "FINANCIAL_REVISION",
    "INDEPENDENT",
    "COUNTER",
    "SUPERSESSION",
}
_SOURCE_FAMILY_MAP = {
    "ISSUER_EARNINGS_IR_NEWSROOM_CALL": "IssuerIR",
    "OFFICIAL_FILING": "DART",
    "CUSTOMER_OFFICIAL": "CustomerOfficial",
    "FINANCIAL_REVISION_SOURCE": "CompanyGuide",
    "TRUSTED_INDEPENDENT": "IndustryData",
    "GENERAL_WEB_DISCOVERY_TO_ORIGINAL": "NaverSearch",
}
_OFFICIAL_FIRST = {
    "IssuerIR",
    "DART",
    "CustomerOfficial",
    "CompanyGuide",
    "IndustryData",
}


def run_dossier_source_research(
    *,
    target: DossierTarget,
    as_of_date: str,
    archetype_id: str,
    dossier_question_tasks: Sequence[Mapping[str, Any]],
    output_root: str | Path,
    query_provider: QuestionQueryProvider | None = None,
    force_web_family_ids: Sequence[str] = (),
    question_family_ids: Sequence[str] = (),
    adequacy_route_categories: Sequence[str] = (),
    test_mode: bool = False,
) -> Mapping[str, Any]:
    """Plan and execute every supplied question with explicit bounded budgets."""

    selected_family_ids = {str(value) for value in question_family_ids}
    tasks = tuple(
        row
        for row in dossier_question_tasks
        if str(row.get("target_id") or "") == target.target_id
        and (
            not selected_family_ids
            or str(row.get("question_family_id") or "") in selected_family_ids
        )
    )
    if not tasks:
        raise ValueError("dossier source research requires target question tasks")
    force_web = {str(value) for value in force_web_family_ids}
    route_categories = tuple(
        dict.fromkeys(str(value).strip().upper() for value in adequacy_route_categories)
    )
    unknown_routes = set(route_categories) - _ADEQUACY_ROUTE_CATEGORIES
    if unknown_routes:
        raise ValueError(f"unknown adequacy route categories: {sorted(unknown_routes)}")
    recipes = tuple(
        _recipe_from_task(
            row,
            archetype_id=archetype_id,
            adequacy_route_categories=route_categories,
        )
        for row in tasks
    )
    drafts = tuple(
        _draft_from_task(
            row,
            force_web=str(row["question_family_id"]) in force_web,
            adequacy_route_categories=route_categories,
        )
        for row in tasks
    )
    signal_id = "DOSSIG-" + stable_hash(
        {"target_id": target.target_id, "as_of_date": as_of_date}
    )[:24]
    trigger = {
        "trigger_signal_id": signal_id,
        "target_id": target.target_id,
        "target_name": target.company_name,
        "trigger_type": "FULL_THESIS_SOURCE_GAP",
        "effective_date": as_of_date,
        "payload": {"report_name": "bounded full-thesis investigation"},
    }
    materialized_parts = []
    for batch_index in range(0, len(drafts), 10):
        batch = drafts[batch_index : batch_index + 10]
        recipe_ids = {str(row["recipe_id"]) for row in batch}
        planner_run = {
            "target_id": target.target_id,
            "target_name": target.company_name,
            "as_of_date": as_of_date,
            "candidate_event_id": "DOSCAND-"
            + stable_hash(
                {
                    "target_id": target.target_id,
                    "as_of_date": as_of_date,
                    "batch": batch_index // 10,
                }
            )[:24],
            "trigger_signal_ids": [signal_id],
            "plan": {"critique_output": {"source_task_drafts": list(batch)}},
        }
        materialized_parts.append(
            CurrentQuestionSourceTaskMaterializer().materialize(
                SourceTaskMaterializationConfig(
                    as_of_date=as_of_date,
                    max_source_tasks_per_candidate=len(batch),
                    max_parallel_tasks=min(8, len(batch)),
                    test_mode=test_mode,
                ),
                planner_runs=(planner_run,),
                trigger_signals=(trigger,),
                recipes=tuple(
                    recipe for recipe in recipes if recipe.recipe_id in recipe_ids
                ),
                provider=query_provider,
            )
        )
    question_rows = tuple(
        {
            **row.to_dict(),
            "adequacy_route_attempts": [
                {
                    "route_category": category,
                    "status": "ATTEMPTED",
                    "proof_id": row.task_id,
                    "reason": "LLM query generation and bounded source execution requested this route.",
                }
                for category in route_categories
            ],
        }
        for part in materialized_parts
        for row in part.question_source_tasks
    )
    daily_rows = tuple(
        {
            **row.to_dict(),
            "allows_general_web": True,
            "official_first_attempted": False,
        }
        for part in materialized_parts
        for row in part.source_tasks
    )
    acquisition = CurrentSourceAcquisitionOrchestrator().acquire(
        SourceAcquisitionConfig(
            as_of_date=as_of_date,
            max_tasks=len(question_rows),
            test_mode=test_mode,
        ),
        source_tasks=daily_rows,
        question_source_tasks=question_rows,
    )
    question_rows = _finalize_adequacy_route_attempts(
        question_rows=question_rows,
        acquisition=acquisition,
        route_categories=route_categories,
    )
    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=True)
    write_jsonl(root / "source_tasks.jsonl", daily_rows)
    write_jsonl(root / "question_source_tasks.jsonl", question_rows)
    write_jsonl(
        root / "query_generation_prompts.jsonl",
        (row for part in materialized_parts for row in part.prompt_rows),
    )
    write_jsonl(
        root / "query_generation_responses.jsonl",
        (row for part in materialized_parts for row in part.response_rows),
    )
    write_source_acquisition_run(acquisition, output_root=root)
    audit = {
        "schema_version": SOURCE_RESEARCH_SCHEMA_VERSION,
        "status": (
            "DOSSIER_SOURCE_RESEARCH_PASS"
            if all(part.audit["critical_count_sum"] == 0 for part in materialized_parts)
            and acquisition.audit["critical_count_sum"] == 0
            else "DOSSIER_SOURCE_RESEARCH_PENDING"
        ),
        "target_id": target.target_id,
        "question_family_count": len(tasks),
        "planned_question_task_count": len(question_rows),
        "query_generation_call_count": sum(
            len(part.response_rows) for part in materialized_parts
        ),
        "provider_request_count": len(acquisition.provider_requests),
        "provider_fetch_result_count": len(acquisition.provider_fetch_results),
        "full_document_count": len(acquisition.evidence_documents),
        "web_search_task_count": len(acquisition.web_search_tasks),
        "web_full_document_count": len(acquisition.web_fetched_documents),
        "force_web_family_ids": sorted(force_web),
        "selected_question_family_ids": sorted(selected_family_ids),
        "adequacy_route_categories": list(route_categories),
        "materialization_critical_count": sum(
            int(part.audit["critical_count_sum"]) for part in materialized_parts
        ),
        "acquisition_critical_count": int(acquisition.audit["critical_count_sum"]),
    }
    audit["critical_count_sum"] = (
        audit["materialization_critical_count"]
        + audit["acquisition_critical_count"]
    )
    write_json(root / "dossier_source_research_audit.json", audit)
    return audit


def _recipe_from_task(
    task: Mapping[str, Any],
    *,
    archetype_id: str,
    adequacy_route_categories: Sequence[str] = (),
) -> EvidenceRecipe:
    family = str(task["question_family_id"])
    question = str(task["question_to_answer"])
    primitives = tuple(str(value) for value in task.get("primitive_ids") or ())
    if not primitives:
        raise ValueError("dossier question family requires semantic primitives")
    predicate = AcceptedClaimPredicate(
        predicate_id="DOSSPRED-" + stable_hash({"family": family})[:24],
        semantic_test=question,
        required_subject_relation="DIRECT target or explicitly identified customer",
        required_fields=("source_id", "exact_anchor", "published_date"),
        allowed_polarities=("POSITIVE", "NEGATIVE", "MIXED", "NORMAL"),
        temporal_test="Only information available on or before as_of_date is accepted.",
        lifecycle_test="Current, unresolved, or explicitly superseded state must be distinguished.",
    )
    priorities = _source_families(task)
    preferred = tuple(value for value in priorities if value in _OFFICIAL_FIRST)
    if "ISSUER_IR" in adequacy_route_categories:
        preferred = tuple(dict.fromkeys(("IssuerIR", *preferred)))
    if "FINANCIAL_REVISION" in adequacy_route_categories:
        preferred = tuple(dict.fromkeys(("CompanyGuide", *preferred)))
    if not preferred:
        preferred = ("IssuerIR",)
    preferred = tuple(dict.fromkeys((*preferred, "CustomerOfficial")))
    return EvidenceRecipe(
        recipe_id="DOSSRECIPE-" + stable_hash({"family": family})[:24],
        archetype_id=archetype_id,
        primitive_id=primitives[0],
        role="GUARD" if task.get("counter_thesis") else "POSITIVE",
        economic_mechanism=question,
        question_to_answer=question,
        accepted_claim_predicates=(predicate,),
        required_entities=("target company",),
        required_values=("the fact needed to answer the question",),
        required_units=("source-reported unit or explicit qualitative state",),
        required_time_scope=("as_of_date", "stated reporting period"),
        required_target_directness=("DIRECT",),
        required_current_lifecycle=("CURRENT", "SUPERSEDED_EXPLICITLY"),
        preferred_source_families=preferred,
        preferred_document_types=("official filing", "earnings or research document"),
        preferred_sections=("exact section answering the question",),
        discovery_sources=("NaverSearch",),
        forbidden_score_sources=("search snippet", "source proxy"),
        positive_examples=("target-direct current exact quote answering the question",),
        counterexamples=("current exact quote contradicting the proposed mechanism",),
        wrong_subject_examples=("peer or industry statement without a target bridge",),
        source_success_examples=("fetched full document with verified date and exact quote",),
        source_failure_examples=("search result title or snippet without full document",),
        rejection_conditions=("wrong subject, future date, stale or snippet-only evidence",),
        counter_questions=("What current fact weakens or contradicts this mechanism?",),
        supersession_questions=("Was the cited state later changed before as_of_date?",),
        query_intent_constraints=("Target and explicit reporting year must appear.",),
        stop_conditions=(str(task["stop_condition"]),),
        source_exhaustion_conditions=("All bounded official and allowed fallback routes were attempted.",),
        supporting_case_ids=("DOSSIER-QUESTION-FAMILY",),
        supporting_source_verification_ids=(),
        supporting_source_failure_verification_ids=(),
        planning_only_source_proxy_case_ids=(),
        freshness_max_age_days=730,
        freshness_supersession_rule="newer current source supersedes stale state",
    )


def _draft_from_task(
    task: Mapping[str, Any],
    *,
    force_web: bool,
    adequacy_route_categories: Sequence[str] = (),
) -> Mapping[str, Any]:
    family = str(task["question_family_id"])
    budget = dict(task.get("budget") or {})
    priorities = _source_families(task)
    preferred = tuple(value for value in priorities if value in _OFFICIAL_FIRST)
    if "ISSUER_IR" in adequacy_route_categories:
        preferred = ("IssuerIR",)
    elif "FINANCIAL_REVISION" in adequacy_route_categories:
        preferred = ("CompanyGuide",)
    elif force_web:
        preferred = ("CustomerOfficial",)
    if not preferred:
        preferred = ("IssuerIR",)
    return {
        "draft_id": "DOSSDRAFT-"
        + stable_hash(
            {
                "family": family,
                "web": force_web,
                "adequacy_route_categories": list(adequacy_route_categories),
            }
        )[:24],
        "recipe_id": "DOSSRECIPE-" + stable_hash({"family": family})[:24],
        "question_to_answer": str(task["question_to_answer"]),
        "why_material": (
            "This material question must be terminal before full score finalization. "
            "The bounded run must investigate these explicit evidence routes: "
            + ", ".join(adequacy_route_categories or ("configured source route",))
            + "."
        ),
        "query_intent": (
            "Generate target-specific current-source queries from the semantic question, "
            "without using deterministic query templates. Respect the requested evidence "
            "route intent, including counter or supersession checks when present: "
            + ", ".join(adequacy_route_categories or ("configured source route",))
        ),
        "preferred_source_families": list(preferred),
        "fallback_source_families": ["NaverSearch"],
        "max_queries": int(budget["max_queries"]),
        "max_candidates": int(budget["max_candidates"]),
        "max_fetches": int(budget["max_fetches"]),
        "stop_condition": str(task["stop_condition"]),
    }


def _source_families(task: Mapping[str, Any]) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(
            _SOURCE_FAMILY_MAP.get(str(value), str(value))
            for value in task.get("source_priority") or ()
        )
    )


def _finalize_adequacy_route_attempts(
    *,
    question_rows: Sequence[Mapping[str, Any]],
    acquisition: Any,
    route_categories: Sequence[str],
) -> tuple[Mapping[str, Any], ...]:
    documents_by_task: dict[str, list[Any]] = {}
    for document in acquisition.evidence_documents:
        for task_id in document.source_task_ids:
            documents_by_task.setdefault(str(task_id), []).append(document)
    web_by_task: dict[str, list[Mapping[str, Any]]] = {}
    for row in acquisition.web_search_tasks:
        web_by_task.setdefault(str(row.get("source_task_id") or ""), []).append(row)
    result = []
    for row in question_rows:
        task_id = str(row.get("task_id") or "")
        documents = tuple(documents_by_task.get(task_id, ()))
        web = tuple(web_by_task.get(task_id, ()))
        web_executed = any(item.get("search_call_executed") is True for item in web)
        web_failed = any(item.get("search_error") or item.get("provider_errors") for item in web)
        attempts = []
        for category in route_categories:
            terminal_source_classes = {
                "ISSUER_IR": {"IssuerIR", "IssuerNewsroom"},
                "FINANCIAL_REVISION": {"CompanyGuide", "FinancialRevision"},
                "OFFICIAL": {"DART", "KIND", "KRX", "Official"},
            }.get(category)
            if terminal_source_classes is not None:
                resolved_docs = tuple(
                    item
                    for item in documents
                    if item.source_class in terminal_source_classes
                )
                if resolved_docs:
                    status = "RESOLVED"
                    proof_id = resolved_docs[0].document_id
                    reason = "Verified full document resolved the requested source route."
                elif web_executed and not web_failed:
                    status = "UNAVAILABLE"
                    proof_id = str(web[0].get("web_task_id") or task_id)
                    reason = (
                        "Preferred connector did not yield score evidence and bounded "
                        "LLM-planned web fallback completed without a verified full "
                        "document for the requested source route."
                    )
                else:
                    status = "PENDING"
                    proof_id = str((web[0] if web else {}).get("web_task_id") or task_id)
                    reason = "Requested source route did not complete a usable bounded fallback."
            else:
                status = "ATTEMPTED" if web_executed and not web_failed else "PENDING"
                proof_id = str((web[0] if web else {}).get("web_task_id") or task_id)
                reason = (
                    "LLM-generated bounded query executed for this evidence route."
                    if status == "ATTEMPTED"
                    else "Requested evidence route did not complete provider execution."
                )
            attempts.append(
                {
                    "route_category": category,
                    "status": status,
                    "proof_id": proof_id,
                    "reason": reason,
                }
            )
        result.append({**dict(row), "adequacy_route_attempts": attempts})
    return tuple(result)


__all__ = ["SOURCE_RESEARCH_SCHEMA_VERSION", "run_dossier_source_research"]
