"""Materialize real question-centric SourceTasks from live Brain plans."""

from __future__ import annotations

import hashlib
import json
import re
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl
from e2r.research_brain.intelligence_schema import (
    AcceptedClaimPredicate,
    CurrentEvidenceFact,
    EvidenceRecipe,
    PlannerSourceTaskDraft,
)
from e2r.research_brain.planning import (
    QueryProviderCompletion,
    QuestionQueryProvider,
    QuestionSourceTask,
    QuestionTaskPlanningResult,
    QuestionTaskPlanningStatus,
    audit_question_source_tasks,
    build_codex_question_query_provider,
    compile_question_task_context,
    plan_question_source_task,
)
from e2r.research_brain.runtime.current_operation_runner import DailySourceTaskRecord


LIVE_SOURCE_TASK_AUDIT_SCHEMA_VERSION = "e2r_live_source_task_audit_v1"
SELECTION_SCHEMA = "e2r_v6_pre_deep_canary_selection_v1"
SELECTION_RECEIPT_SCHEMA = "e2r_v6_pre_deep_selection_receipt_v1"
SELECTION_PASS = "E2R_V6_CROSS_ARCHETYPE_CANARY_SELECTION_PASS"
NATURAL_SELECTION = "NATURAL_TRIGGER_CANARY"
REQUIRED_ARCHETYPES = (
    "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
    "C15_MATERIAL_SPREAD_SUPERCYCLE",
    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
    "C24_BIO_TRIAL_DATA_EVENT_RISK",
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
)
_HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
_TARGET_RE = re.compile(r"^[0-9A-Z]{6}$")
_SELECTION_MANIFEST_KEYS = frozenset(
    {
        "schema_version",
        "status",
        "selection_as_of_date",
        "required_archetypes",
        "selections",
        "selection_count",
        "critical_counts",
        "critical_count_sum",
        "failures",
        "score_or_stage_authority",
        "selection_roster_hash",
    }
)
_SELECTION_CRITICAL_KEYS = frozenset(
    {
        "required_archetype_missing_count",
        "invalid_candidate_lineage_count",
        "post_score_target_selection_count",
        "target_specific_code_branch_count",
        "forced_canary_mislabeled_natural_count",
        "duplicate_target_count",
    }
)
_SELECTION_RECEIPT_KEYS = frozenset(
    {
        "schema_version",
        "selection_id",
        "archetype_id",
        "target_id",
        "company_name",
        "selection_mode",
        "selection_as_of_date",
        "pre_deep_input_hash",
        "krx_effective_date",
        "krx_source_url",
        "krx_source_hash",
        "krx_request_id",
        "candidate_event_hash",
        "depth_decision_hash",
        "planner_run_id",
        "blind_input_id",
        "plan_hash",
        "issuer_profile_hash",
        "business_profile_hash",
        "direct_current_supporting_fact_ids",
        "recipe_ids",
        "trigger_event_ids",
        "available_source_families",
        "selection_rationale",
        "final_score_visible_at_selection",
        "final_stage_visible_at_selection",
        "production_daily_candidate",
        "score_or_stage_authority",
    }
)
_OFFICIAL_SOURCE_CLASSES = frozenset(
    {
        "DART",
        "KIND",
        "KRX",
        "CompanyGuide",
        "IssuerIR",
        "IssuerNewsroom",
        "CompanyEarningsCall",
        "CustomerOfficial",
        "CustomerNewsroom",
        "SEC",
        "Regulator",
        "Official",
        "IR",
    }
)


@dataclass(frozen=True)
class SourceTaskMaterializationConfig:
    as_of_date: str
    max_source_tasks_per_candidate: int
    max_generation_attempts: int = 3
    max_acquisition_retries: int = 2
    max_parallel_tasks: int = 4
    test_mode: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if not 1 <= self.max_source_tasks_per_candidate <= 10:
            raise ValueError("source tasks per candidate must be bounded by ten")
        if not 1 <= self.max_generation_attempts <= 3:
            raise ValueError("query generation attempts must be bounded by three")
        if not 0 <= self.max_acquisition_retries <= 3:
            raise ValueError("source acquisition retries must be bounded by three")
        if not 1 <= self.max_parallel_tasks <= 8:
            raise ValueError("parallel source-task generation must be bounded by eight")


@dataclass(frozen=True)
class SourceTaskMaterializationResult:
    as_of_date: str
    status: str
    source_tasks: tuple[DailySourceTaskRecord, ...]
    question_source_tasks: tuple[QuestionSourceTask, ...]
    planning_results: tuple[QuestionTaskPlanningResult, ...]
    prompt_rows: tuple[Mapping[str, Any], ...]
    response_rows: tuple[Mapping[str, Any], ...]
    audit: Mapping[str, Any]

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)


@dataclass
class RecordingQuestionQueryProvider(QuestionQueryProvider):
    base: QuestionQueryProvider
    target_id: str
    draft_id: str
    prompt_rows: list[Mapping[str, Any]]
    response_rows: list[Mapping[str, Any]]

    @property
    def provider_name(self) -> str:
        return self.base.provider_name

    @property
    def generator_kind(self) -> str:
        return self.base.generator_kind

    @property
    def real_provider(self) -> bool:
        return bool(self.base.real_provider)

    @property
    def fake_provider(self) -> bool:
        return bool(self.base.fake_provider)

    def complete(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
    ) -> QueryProviderCompletion:
        prompt_hash = _sha256_text(prompt)
        call_id = "QUERYCALL-" + stable_hash(
            {
                "target_id": self.target_id,
                "draft_id": self.draft_id,
                "prompt_hash": prompt_hash,
            }
        )[:24]
        self.prompt_rows.append(
            {
                "schema_version": "e2r_live_query_prompt_v1",
                "call_id": call_id,
                "target_id": self.target_id,
                "draft_id": self.draft_id,
                "provider_name": self.provider_name,
                "prompt_hash": prompt_hash,
                "prompt_text": prompt,
            }
        )
        try:
            completion = self.base.complete(prompt=prompt, output_schema=output_schema)
        except Exception as exc:
            self.response_rows.append(
                {
                    "schema_version": "e2r_live_query_response_v1",
                    "call_id": call_id,
                    "target_id": self.target_id,
                    "draft_id": self.draft_id,
                    "provider_name": self.provider_name,
                    "status": "PROVIDER_ERROR",
                    "response_hash": _sha256_text(type(exc).__name__),
                    "response_payload": {},
                    "error_category": type(exc).__name__,
                }
            )
            raise
        self.response_rows.append(
            {
                "schema_version": "e2r_live_query_response_v1",
                "call_id": call_id,
                "target_id": self.target_id,
                "draft_id": self.draft_id,
                "provider_name": self.provider_name,
                "status": "COMPLETED",
                "response_hash": _sha256_text(completion.raw_response),
                "response_payload": dict(completion.payload),
                "error_category": None,
            }
        )
        return completion


class CurrentQuestionSourceTaskMaterializer:
    def materialize(
        self,
        config: SourceTaskMaterializationConfig,
        *,
        planner_runs: Sequence[Mapping[str, Any]],
        trigger_signals: Sequence[Mapping[str, Any]],
        recipes: Sequence[EvidenceRecipe],
        provider: QuestionQueryProvider | None = None,
        selection_manifest_path: str | Path | None = None,
        selection_candidates: Sequence[Mapping[str, Any]] | None = None,
    ) -> SourceTaskMaterializationResult:
        recipe_by_id = _unique_by(recipes, key="recipe_id", context="recipes")
        signals_by_id = _unique_mapping_rows(
            trigger_signals,
            key="trigger_signal_id",
            context="trigger signals",
        )
        base_provider = provider
        if base_provider is None and not config.test_mode:
            base_provider = build_codex_question_query_provider()

        selected_run_ids: set[str] | None = None
        selection_receipts: tuple[Mapping[str, Any], ...] | None = None
        if selection_manifest_path is not None:
            # Imported lazily because the selector validates the live trigger
            # and depth dataclasses from this package.
            from e2r.production.v6_canary_selection import (
                compile_cross_archetype_canary_selection,
                load_sealed_cross_archetype_canary_selection,
            )

            selection_manifest = load_sealed_cross_archetype_canary_selection(
                selection_manifest_path
            )
            if not config.test_mode:
                if selection_candidates is None:
                    raise ValueError(
                        "production selection requires canonical upstream candidates"
                    )
                expected_manifest = compile_cross_archetype_canary_selection(
                    selection_as_of_date=config.as_of_date,
                    candidates=selection_candidates,
                    trigger_events=trigger_signals,
                )
                if dict(selection_manifest) != dict(expected_manifest):
                    raise ValueError(
                        "sealed selection differs from canonical live upstream inputs"
                    )
                expected_runs = {
                    str(row.get("planner_run_id") or ""): dict(row)
                    for candidate in selection_candidates
                    for row in (candidate.get("planner_run"),)
                    if isinstance(row, Mapping)
                }
                supplied_runs = {
                    str(row.get("planner_run_id") or ""): dict(row)
                    for row in planner_runs
                }
                if (
                    "" in expected_runs
                    or "" in supplied_runs
                    or len(expected_runs) != len(selection_candidates)
                    or len(supplied_runs) != len(planner_runs)
                    or supplied_runs != expected_runs
                ):
                    raise ValueError(
                        "planner run roster differs from canonical selection candidates"
                    )
            selection_receipts = tuple(selection_manifest.get("selections") or ())
            selected_run_ids = _validated_selected_planner_run_ids(
                selection_manifest,
                as_of_date=config.as_of_date,
                planner_runs=planner_runs,
                trigger_signals=trigger_signals,
            )

        jobs: list[tuple[Mapping[str, Any], Mapping[str, Any]]] = []
        per_target: dict[str, int] = {}
        seen_drafts: set[str] = set()
        for run in planner_runs:
            if selected_run_ids is not None and str(
                run.get("planner_run_id") or ""
            ) not in selected_run_ids:
                continue
            if str(run.get("as_of_date") or "") != config.as_of_date:
                raise ValueError("planner run as_of_date differs from source-task run")
            critique = ((run.get("plan") or {}).get("critique_output") or {})
            for raw_draft in critique.get("source_task_drafts") or ():
                if not isinstance(raw_draft, Mapping):
                    raise ValueError("planner source-task draft must be an object")
                draft_id = str(raw_draft.get("draft_id") or "")
                if not draft_id or draft_id in seen_drafts:
                    raise ValueError("planner source-task draft identity is empty or duplicate")
                target_id = str(run.get("target_id") or "")
                count = per_target.get(target_id, 0) + 1
                if count > config.max_source_tasks_per_candidate:
                    raise ValueError("planner source-task draft count exceeds candidate budget")
                per_target[target_id] = count
                seen_drafts.add(draft_id)
                jobs.append((run, raw_draft))

        def execute(
            job: tuple[Mapping[str, Any], Mapping[str, Any]],
        ) -> tuple[
            QuestionTaskPlanningResult,
            tuple[Mapping[str, Any], ...],
            tuple[Mapping[str, Any], ...],
        ]:
            run, raw_draft = job
            draft = _draft_from_mapping(raw_draft)
            recipe = recipe_by_id.get(draft.recipe_id)
            if recipe is None:
                raise ValueError(f"planner selected unknown recipe: {draft.recipe_id}")
            current_facts = _current_facts_for_run(run, signals_by_id)
            target_id = str(run.get("target_id") or "")
            target_name = str(run.get("target_name") or "")
            context = compile_question_task_context(
                target_id=target_id,
                target_name=target_name,
                symbol=target_id,
                target_aliases=(target_id,),
                as_of_date=config.as_of_date,
                current_facts=current_facts,
                missing_information=(draft.question_to_answer,),
            )
            prompt_rows: list[Mapping[str, Any]] = []
            response_rows: list[Mapping[str, Any]] = []
            recording = (
                RecordingQuestionQueryProvider(
                    base=base_provider,
                    target_id=target_id,
                    draft_id=draft.draft_id,
                    prompt_rows=prompt_rows,
                    response_rows=response_rows,
                )
                if base_provider is not None
                else None
            )
            result = plan_question_source_task(
                draft=draft,
                recipe=recipe,
                context=context,
                candidate_event_id=str(run.get("candidate_event_id") or ""),
                task_type=(
                    "red_team"
                    if recipe.role in {"GUARD", "HARD_BREAK"}
                    else "evidence_confirmation"
                ),
                provider=recording,
                test_mode=config.test_mode,
                max_generation_attempts=config.max_generation_attempts,
            )
            return result, tuple(prompt_rows), tuple(response_rows)

        if len(jobs) <= 1 or config.max_parallel_tasks == 1:
            completed = tuple(execute(job) for job in jobs)
        else:
            with ThreadPoolExecutor(
                max_workers=min(config.max_parallel_tasks, len(jobs)),
                thread_name_prefix="e2r-query",
            ) as executor:
                completed = tuple(executor.map(execute, jobs))

        planning_results = tuple(item[0] for item in completed)
        question_tasks = tuple(
            item.task for item in planning_results if item.task is not None
        )
        daily_tasks = tuple(
            _daily_source_task(
                task,
                max_acquisition_retries=config.max_acquisition_retries,
            )
            for task in question_tasks
        )
        prompt_rows = tuple(row for item in completed for row in item[1])
        response_rows = tuple(row for item in completed for row in item[2])
        audit = {
            **_audit_live_source_tasks(
            as_of_date=config.as_of_date,
            draft_count=len(jobs),
            planning_results=planning_results,
            source_tasks=daily_tasks,
            question_tasks=question_tasks,
            prompt_rows=prompt_rows,
            response_rows=response_rows,
            test_mode=config.test_mode,
            ),
            "selection_receipt_filter_applied": selected_run_ids is not None,
            "selection_receipt_ids": (
                sorted(str(row.get("selection_id") or "") for row in selection_receipts)
                if selection_receipts is not None
                else []
            ),
            "selection_receipt_roster_hash": (
                stable_hash(list(selection_receipts))
                if selection_receipts is not None
                else None
            ),
            "selected_planner_run_count": (
                len(selected_run_ids) if selected_run_ids is not None else None
            ),
            "unselected_planner_run_count": (
                len(planner_runs) - len(selected_run_ids)
                if selected_run_ids is not None
                else None
            ),
        }
        return SourceTaskMaterializationResult(
            as_of_date=config.as_of_date,
            status=(
                "CURRENT_SOURCE_TASK_PASS"
                if audit["hard_acceptance_pass"]
                else "CURRENT_SOURCE_TASK_FAIL"
            ),
            source_tasks=daily_tasks,
            question_source_tasks=question_tasks,
            planning_results=planning_results,
            prompt_rows=prompt_rows,
            response_rows=response_rows,
            audit=audit,
        )


def _validated_selected_planner_run_ids(
    manifest: Mapping[str, Any],
    *,
    as_of_date: str,
    planner_runs: Sequence[Mapping[str, Any]],
    trigger_signals: Sequence[Mapping[str, Any]],
) -> set[str]:
    critical_counts = manifest.get("critical_counts")
    if (
        set(manifest) != _SELECTION_MANIFEST_KEYS
        or manifest.get("schema_version") != SELECTION_SCHEMA
        or manifest.get("status") != SELECTION_PASS
        or str(manifest.get("selection_as_of_date") or "") != as_of_date
        or int(manifest.get("critical_count_sum") or 0) != 0
        or tuple(manifest.get("required_archetypes") or ()) != REQUIRED_ARCHETYPES
        or manifest.get("failures") != []
        or manifest.get("score_or_stage_authority") is not False
        or not isinstance(critical_counts, Mapping)
        or set(critical_counts) != _SELECTION_CRITICAL_KEYS
        or any(
            isinstance(value, bool) or not isinstance(value, int) or value != 0
            for value in critical_counts.values()
        )
    ):
        raise ValueError("selection manifest is not an accepted sealed roster")
    receipts = tuple(manifest.get("selections") or ())
    if (
        len(receipts) != len(REQUIRED_ARCHETYPES)
        or int(manifest.get("selection_count") or -1) != len(receipts)
    ):
        raise ValueError("selection receipts must contain the exact five-target roster")
    if manifest.get("selection_roster_hash") != stable_hash(list(receipts)):
        raise ValueError("selection receipt roster hash mismatch")
    run_ids = [str(run.get("planner_run_id") or "") for run in planner_runs]
    if not all(run_ids) or len(run_ids) != len(set(run_ids)):
        raise ValueError("planner run identities must be nonempty and unique")
    run_by_id = {str(run["planner_run_id"]): run for run in planner_runs}
    signal_by_id = {
        str(row.get("trigger_signal_id") or ""): row for row in trigger_signals
    }
    if "" in signal_by_id or len(signal_by_id) != len(trigger_signals):
        raise ValueError("trigger signal identities must be nonempty and unique")
    selected: list[str] = []
    targets: list[str] = []
    archetypes: list[str] = []
    for receipt in receipts:
        if set(receipt) != _SELECTION_RECEIPT_KEYS:
            raise ValueError("selection receipt keys are not exact")
        if receipt.get("schema_version") != SELECTION_RECEIPT_SCHEMA:
            raise ValueError("selection receipt schema is invalid")
        pre_deep_hash = str(receipt.get("pre_deep_input_hash") or "")
        if _HEX64_RE.fullmatch(pre_deep_hash) is None:
            raise ValueError("selection receipt pre-deep hash is invalid")
        if str(receipt.get("selection_id") or "") != "SELREC-" + pre_deep_hash[:24]:
            raise ValueError("selection receipt identity is invalid")
        if str(receipt.get("selection_as_of_date") or "") != as_of_date:
            raise ValueError("selection receipt as_of_date differs from source-task run")
        if receipt.get("final_score_visible_at_selection") is not False:
            raise ValueError("selection receipt must be blind to final score")
        if receipt.get("final_stage_visible_at_selection") is not False:
            raise ValueError("selection receipt must be blind to final Stage")
        if receipt.get("score_or_stage_authority") is not False:
            raise ValueError("selection receipt cannot carry score or Stage authority")
        expected_daily = receipt.get("selection_mode") == NATURAL_SELECTION
        if receipt.get("production_daily_candidate") is not expected_daily:
            raise ValueError("selection receipt natural/forced daily label mismatch")
        hash_fields = (
            "krx_source_hash",
            "candidate_event_hash",
            "depth_decision_hash",
            "plan_hash",
            "issuer_profile_hash",
            "business_profile_hash",
        )
        if any(
            _HEX64_RE.fullmatch(str(receipt.get(field) or "")) is None
            for field in hash_fields
        ):
            raise ValueError("selection receipt lineage hash is invalid")
        run_id = str(receipt.get("planner_run_id") or "")
        target_id = str(receipt.get("target_id") or "")
        if target_id != target_id.strip() or _TARGET_RE.fullmatch(target_id) is None:
            raise ValueError("selection receipt target identity is not canonical")
        if not run_id:
            raise ValueError("selection receipt planner run identity is empty")
        run = run_by_id.get(run_id)
        if run is None:
            raise ValueError(f"selected planner run is unavailable: {run_id}")
        if target_id != str(run.get("target_id") or ""):
            raise ValueError("selection receipt target/planner run mismatch")
        if str(receipt.get("company_name") or "") != str(run.get("target_name") or ""):
            raise ValueError("selection receipt company/planner run mismatch")
        critique = ((run.get("plan") or {}).get("critique_output") or {})
        top = tuple(critique.get("top_k_archetypes") or ())
        leading = str((top[0] if top else {}).get("archetype_id") or "")
        if str(receipt.get("archetype_id") or "") != leading:
            raise ValueError("selection receipt archetype/planner top-one mismatch")
        if str(receipt.get("plan_hash") or "") != stable_hash(run.get("plan") or {}):
            raise ValueError("selection receipt plan hash mismatch")
        if str(receipt.get("blind_input_id") or "") != str(
            run.get("blind_input_id") or ""
        ):
            raise ValueError("selection receipt blind input/planner run mismatch")
        supporting = sorted(
            {
                str(value)
                for value in critique.get("supporting_current_fact_ids") or ()
                if str(value)
            }
        )
        drafts = tuple(
            row
            for row in critique.get("source_task_drafts") or ()
            if isinstance(row, Mapping)
        )
        recipes = sorted(
            {
                str(row.get("recipe_id") or "")
                for row in drafts
                if str(row.get("recipe_id") or "")
            }
        )
        source_families = sorted(
            {
                str(value)
                for row in drafts
                for field in ("preferred_source_families", "fallback_source_families")
                for value in row.get(field) or ()
                if str(value)
            }
        )
        expected_business_hash = stable_hash(
            {
                "target_id": str(run.get("target_id") or ""),
                "leading_archetype_id": leading,
                "direct_current_supporting_fact_ids": supporting,
                "recipe_ids": recipes,
                "available_source_families": source_families,
            }
        )
        if (
            list(receipt.get("direct_current_supporting_fact_ids") or ())
            != supporting
            or list(receipt.get("recipe_ids") or ()) != recipes
            or list(receipt.get("available_source_families") or ())
            != source_families
            or str(receipt.get("business_profile_hash") or "")
            != expected_business_hash
        ):
            raise ValueError("selection receipt business/planner projection mismatch")
        trigger_ids = list(receipt.get("trigger_event_ids") or ())
        if receipt.get("selection_mode") == NATURAL_SELECTION:
            if not trigger_ids:
                raise ValueError("natural selection requires current trigger lineage")
            for signal_id in trigger_ids:
                signal = signal_by_id.get(str(signal_id))
                if (
                    signal is None
                    or str(signal.get("target_id") or "") != str(run.get("target_id") or "")
                    or str(signal_id) not in set(run.get("trigger_signal_ids") or ())
                    or not set(signal.get("source_refs") or ())
                    <= set(run.get("source_refs") or ())
                ):
                    raise ValueError("selection receipt trigger/planner lineage mismatch")
        elif trigger_ids:
            raise ValueError("forced selection cannot claim natural trigger lineage")
        krx_date = date.fromisoformat(str(receipt.get("krx_effective_date") or ""))
        selection_date = date.fromisoformat(as_of_date)
        url = str(receipt.get("krx_source_url") or "")
        endpoint = url.rsplit("/", 1)[-1]
        market = {"stk_isu_base_info": "KOSPI", "ksq_isu_base_info": "KOSDAQ"}.get(
            endpoint
        )
        expected_request = (
            "KRXREQ-"
            + stable_hash(
                {
                    "market": market,
                    "effective_date": krx_date.isoformat(),
                    "endpoint": endpoint,
                }
            )[:24]
            if market
            else ""
        )
        if (
            market is None
            or krx_date > selection_date
            or krx_date < selection_date - timedelta(days=7)
            or str(receipt.get("krx_request_id") or "") != expected_request
        ):
            raise ValueError("selection receipt KRX lineage is stale or invalid")
        selected.append(run_id)
        targets.append(target_id)
        archetypes.append(str(receipt.get("archetype_id") or ""))
    if len(selected) != len(set(selected)):
        raise ValueError("selection receipt planner run identity is duplicate")
    if len(targets) != len(set(targets)):
        raise ValueError("selection receipt target identity is duplicate")
    if tuple(archetypes) != REQUIRED_ARCHETYPES:
        raise ValueError("selection receipt archetype roster mismatch")
    available = set(run_ids)
    missing = set(selected) - available
    if missing:
        raise ValueError(f"selected planner run is unavailable: {sorted(missing)}")
    return set(selected)


def load_evidence_recipes(path: str | Path) -> tuple[EvidenceRecipe, ...]:
    return tuple(_recipe_from_mapping(row) for row in _read_jsonl(Path(path)))


def write_source_task_materialization(
    result: SourceTaskMaterializationResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "source_tasks": root / "source_tasks.jsonl",
        "question_source_tasks": root / "question_source_tasks.jsonl",
        "planning_results": root / "source_task_planning_results.jsonl",
        "prompts": root / "query_generation_prompts.jsonl",
        "responses": root / "query_generation_responses.jsonl",
        "audit": root / "source_task_audit.json",
    }
    write_jsonl(paths["source_tasks"], (item.to_dict() for item in result.source_tasks))
    write_jsonl(
        paths["question_source_tasks"],
        (item.to_dict() for item in result.question_source_tasks),
    )
    write_jsonl(
        paths["planning_results"],
        (item.to_dict() for item in result.planning_results),
    )
    write_jsonl(paths["prompts"], result.prompt_rows)
    write_jsonl(paths["responses"], result.response_rows)
    write_json(paths["audit"], {**dict(result.audit), "status": result.status})
    return paths


def _daily_source_task(
    task: QuestionSourceTask,
    *,
    max_acquisition_retries: int,
) -> DailySourceTaskRecord:
    acceptance = task.acceptance_contract
    route = task.source_route
    query = task.query_intent
    return DailySourceTaskRecord(
        task_id="DAILYSRC-" + stable_hash({"question_task_id": task.task_id})[:24],
        target_id=task.target_id,
        question_task_id=task.task_id,
        source_class=route.preferred_source_families[0],
        max_queries=task.budget.max_queries,
        max_candidates=task.budget.max_candidates,
        max_fetches=task.budget.max_fetches,
        max_retries=max_acquisition_retries,
        recipe_id=task.recipe_id,
        question_to_answer=task.question_to_answer,
        why_material=task.why_material,
        accepted_predicates=tuple(
            item.to_dict() for item in acceptance.accepted_predicates
        ),
        required_entities=acceptance.required_entities,
        required_values_units=tuple(
            dict.fromkeys((*acceptance.required_values, *acceptance.required_units))
        ),
        time_scope=acceptance.required_time_scope,
        counter_questions=acceptance.counter_questions,
        rejection_conditions=acceptance.rejection_conditions,
        preferred_document_types=route.preferred_document_types,
        preferred_sections=route.preferred_sections,
        fallback_source_classes=route.fallback_source_families,
        literal_queries=query.literal_queries,
        query_provider_name=query.provider_name,
        query_prompt_hash=query.prompt_hash,
        query_response_hash=query.response_hash,
        resolution_conditions=task.stop_condition.resolution_conditions,
        allows_general_web=False,
        official_first_attempted=False,
        official_gap_reasons=(),
        test_only=task.test_only,
    )


def _audit_live_source_tasks(
    *,
    as_of_date: str,
    draft_count: int,
    planning_results: Sequence[QuestionTaskPlanningResult],
    source_tasks: Sequence[DailySourceTaskRecord],
    question_tasks: Sequence[QuestionSourceTask],
    prompt_rows: Sequence[Mapping[str, Any]],
    response_rows: Sequence[Mapping[str, Any]],
    test_mode: bool,
) -> Mapping[str, Any]:
    canonical = audit_question_source_tasks(question_tasks)
    empty_question = sum(not item.question_to_answer.strip() for item in source_tasks)
    empty_success = sum(
        not item.accepted_predicates
        or not item.rejection_conditions
        or not item.resolution_conditions
        for item in source_tasks
    )
    official_violation = sum(
        item.source_class not in _OFFICIAL_SOURCE_CLASSES
        or (item.allows_general_web and not item.official_gap_reasons)
        for item in source_tasks
    )
    unbounded = sum(
        min(item.max_queries, item.max_candidates, item.max_fetches) <= 0
        or not 0 <= item.max_retries <= 3
        for item in source_tasks
    )
    hardcoded_query = sum(
        not item.test_only
        and (
            item.query_provider_name != "codex_cli_question_query_provider"
            or not item.literal_queries
            or not item.query_prompt_hash
            or not item.query_response_hash
        )
        for item in source_tasks
    )
    pending = sum(
        item.status == QuestionTaskPlanningStatus.PENDING.value
        for item in planning_results
    )
    abstained = sum(
        item.status == QuestionTaskPlanningStatus.ABSTAINED.value
        for item in planning_results
    )
    critical = {
        "source_task_draft_empty": int(draft_count <= 0),
        "completed_source_task_empty": int(len(source_tasks) <= 0),
        "generic_verify_primitive_task": int(
            canonical["critical_counts"]["generic_verify_primitive_task"]
        ),
        "empty_question_task": empty_question,
        "empty_success_condition": empty_success,
        "official_first_violation": official_violation,
        "hardcoded_query_template_used_in_canonical_path": hardcoded_query,
        "unbounded_source_task": unbounded,
    }
    status_counts: dict[str, int] = {}
    for item in planning_results:
        status_counts[item.status] = status_counts.get(item.status, 0) + 1
    return {
        "schema_version": LIVE_SOURCE_TASK_AUDIT_SCHEMA_VERSION,
        "as_of_date": as_of_date,
        "draft_count": draft_count,
        "source_task_count": len(source_tasks),
        "planning_result_count": len(planning_results),
        "planning_status_counts": dict(sorted(status_counts.items())),
        "query_generation_call_count": len(response_rows),
        "real_query_provider_task_count": sum(
            item.query_intent.real_provider for item in question_tasks
        ),
        "pending_query_task_count": pending,
        "abstained_query_task_count": abstained,
        "official_first_pending_execution_count": sum(
            not item.official_first_attempted for item in source_tasks
        ),
        "general_web_open_count": sum(item.allows_general_web for item in source_tasks),
        "prompt_response_count_mismatch": abs(len(prompt_rows) - len(response_rows)),
        "test_mode": test_mode,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "hard_acceptance_pass": sum(critical.values()) == 0,
        "production_runtime_ready": False,
        "result_hash": hashlib.sha256(
            json.dumps(
                [item.to_dict() for item in source_tasks],
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest(),
    }


def _current_facts_for_run(
    run: Mapping[str, Any],
    signals_by_id: Mapping[str, Mapping[str, Any]],
) -> tuple[CurrentEvidenceFact, ...]:
    target_id = str(run.get("target_id") or "")
    target_name = str(run.get("target_name") or "")
    facts: list[CurrentEvidenceFact] = []
    for signal_id in run.get("trigger_signal_ids") or ():
        signal = signals_by_id.get(str(signal_id))
        if signal is None or str(signal.get("target_id") or "") != target_id:
            raise ValueError("source-task trigger lineage is missing or wrong-subject")
        effective_date = str(signal.get("effective_date") or "")
        payload = signal.get("payload") or {}
        report_name = str(payload.get("report_name") or "").strip()
        trigger_type = str(signal.get("trigger_type") or "")
        detail = f"'{report_name}' 공식 문서" if report_name else f"{trigger_type} 직접 관측"
        facts.append(
            CurrentEvidenceFact(
                fact_id="CURRENT-" + str(signal_id),
                text=(
                    f"{target_name}에 대해 {effective_date} 기준 {detail}이 있으며, "
                    "구체적 경제 의미는 원문에서 추가 확인해야 한다."
                ),
                observed_date=effective_date,
                target_relation="DIRECT",
                current_status="CURRENT",
            )
        )
    if not facts:
        raise ValueError("source-task context requires current trigger facts")
    return tuple(facts)


def _draft_from_mapping(payload: Mapping[str, Any]) -> PlannerSourceTaskDraft:
    return PlannerSourceTaskDraft(
        draft_id=str(payload.get("draft_id") or ""),
        recipe_id=str(payload.get("recipe_id") or ""),
        question_to_answer=str(payload.get("question_to_answer") or ""),
        why_material=str(payload.get("why_material") or ""),
        query_intent=str(payload.get("query_intent") or ""),
        preferred_source_families=tuple(payload.get("preferred_source_families") or ()),
        fallback_source_families=tuple(payload.get("fallback_source_families") or ()),
        max_queries=int(payload.get("max_queries") or 0),
        max_candidates=int(payload.get("max_candidates") or 0),
        max_fetches=int(payload.get("max_fetches") or 0),
        stop_condition=str(payload.get("stop_condition") or ""),
    )


def _recipe_from_mapping(payload: Mapping[str, Any]) -> EvidenceRecipe:
    data = dict(payload)
    data["accepted_claim_predicates"] = tuple(
        AcceptedClaimPredicate(
            predicate_id=str(item.get("predicate_id") or ""),
            semantic_test=str(item.get("semantic_test") or ""),
            required_subject_relation=str(item.get("required_subject_relation") or ""),
            required_fields=tuple(item.get("required_fields") or ()),
            allowed_polarities=tuple(item.get("allowed_polarities") or ()),
            temporal_test=str(item.get("temporal_test") or ""),
            lifecycle_test=str(item.get("lifecycle_test") or ""),
        )
        for item in payload.get("accepted_claim_predicates") or ()
    )
    tuple_fields = (
        "required_entities",
        "required_values",
        "required_units",
        "required_time_scope",
        "required_target_directness",
        "required_current_lifecycle",
        "preferred_source_families",
        "preferred_document_types",
        "preferred_sections",
        "discovery_sources",
        "forbidden_score_sources",
        "positive_examples",
        "counterexamples",
        "wrong_subject_examples",
        "source_success_examples",
        "source_failure_examples",
        "rejection_conditions",
        "counter_questions",
        "supersession_questions",
        "query_intent_constraints",
        "stop_conditions",
        "source_exhaustion_conditions",
        "supporting_case_ids",
        "supporting_source_verification_ids",
        "supporting_source_failure_verification_ids",
        "planning_only_source_proxy_case_ids",
        "literal_queries",
    )
    for field in tuple_fields:
        data[field] = tuple(payload.get(field) or ())
    return EvidenceRecipe(**data)


def _unique_by(rows: Sequence[Any], *, key: str, context: str) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for row in rows:
        identity = str(getattr(row, key))
        if not identity or identity in result:
            raise ValueError(f"duplicate or empty identity in {context}")
        result[identity] = row
    return result


def _unique_mapping_rows(
    rows: Sequence[Mapping[str, Any]],
    *,
    key: str,
    context: str,
) -> dict[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        identity = str(row.get(key) or "")
        if not identity or identity in result:
            raise ValueError(f"duplicate or empty identity in {context}")
        result[identity] = row
    return result


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    rows: list[Mapping[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if text:
                payload = json.loads(text)
                if not isinstance(payload, Mapping):
                    raise ValueError(f"JSONL row must be an object: {path}")
                rows.append(payload)
    return tuple(rows)


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


__all__ = [
    "LIVE_SOURCE_TASK_AUDIT_SCHEMA_VERSION",
    "CurrentQuestionSourceTaskMaterializer",
    "RecordingQuestionQueryProvider",
    "SourceTaskMaterializationConfig",
    "SourceTaskMaterializationResult",
    "load_evidence_recipes",
    "write_source_task_materialization",
]
