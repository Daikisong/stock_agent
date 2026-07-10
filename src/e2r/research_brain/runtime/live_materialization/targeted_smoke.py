"""Targeted live validation for Samsung, SK hynix, and large-sector samples."""

from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, replace
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Mapping, Protocol, Sequence
from urllib.parse import urlencode, urlparse

from e2r.agentic import EvidenceDocument, SourceType
from e2r.production.metadata import stable_hash, write_json, write_jsonl
from e2r.research.naver_search_provider import NaverFreeSearchProvider
from e2r.research.search_provider import SearchResult
from e2r.research_brain.intelligence_schema import (
    CurrentEvidenceFact,
    EvidenceRecipe,
    PlannerSourceTaskDraft,
)
from e2r.research_brain.planning import (
    QuestionQueryProvider,
    build_codex_question_query_provider,
    compile_question_task_context,
    plan_question_source_task,
)
from e2r.research_brain.replay.source_backed import (
    HistoricalSourceTransport,
    UrllibHistoricalSourceTransport,
    extract_source_full_text,
)
from e2r.research_brain.runtime.atomic_score_stage import (
    AtomicPrimitiveAssessment,
    AtomicPrimitiveStatus,
    AtomicScoreRule,
    AtomicScoringInput,
    AtomicScoringScope,
    decide_atomic_score_stage,
)
from e2r.research_brain.runtime.current_operation_runner import DailyClaimProvenance

from .baseline_materializer import load_baseline_lanes
from .brain_planner_runner import (
    BrainPlannerConfig,
    BrainPlannerRunResult,
    CurrentBrainPlannerRunner,
    write_brain_planner_run,
)
from .current_claim_compiler import (
    CurrentClaimCompilationResult,
    CurrentClaimCompiler,
    CurrentClaimCompilerConfig,
    SourceTaskSatisfactionRecord,
    write_current_claim_compilation,
)
from .current_state_store import load_current_state_store
from .depth_selector import LiveDepth, load_depth_decisions
from .source_task_materializer import (
    RecordingQuestionQueryProvider,
    load_evidence_recipes,
)
from .trigger_fusion import load_candidate_events, load_trigger_signals


TARGETED_SMOKE_SCHEMA_VERSION = "e2r_targeted_live_smoke_v1"
TARGETED_SMOKE_CONFIG_SCHEMA_VERSION = "e2r_targeted_live_smoke_config_v1"
_DATE_PATTERNS = (
    re.compile(r"\b(20\d{2})[-./](0?[1-9]|1[0-2])[-./](0?[1-9]|[12]\d|3[01])\b"),
    re.compile(r"\b(20\d{2})년\s*(0?[1-9]|1[0-2])월\s*(0?[1-9]|[12]\d|3[01])일"),
)
_MONTHS = {
    name.casefold(): index
    for index, name in enumerate(
        (
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ),
        start=1,
    )
}
_ENGLISH_DATE_RE = re.compile(
    r"\b(" + "|".join(_MONTHS) + r")\s+(\d{1,2}),\s+(20\d{2})\b",
    re.IGNORECASE,
)
_ISSUER_SITE_QUERY_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["input_id", "site_search_query", "rationale"],
    "properties": {
        "input_id": {"type": "string"},
        "site_search_query": {"type": "string"},
        "rationale": {"type": "string"},
    },
}


class LiveSearchProvider(Protocol):
    errors: list[str]

    def search(
        self,
        query: str,
        as_of_date: date,
        max_results: int = 100,
    ) -> tuple[SearchResult, ...]:
        ...


class IssuerNewsroomFeedSearchProvider:
    """Execute an LLM-produced short query on an issuer's official RSS search."""

    def __init__(
        self,
        *,
        feed_url: str,
        transport: HistoricalSourceTransport,
        timeout_seconds: int,
        max_attempts: int = 2,
    ) -> None:
        self.feed_url = feed_url
        self.transport = transport
        self.timeout_seconds = timeout_seconds
        self.max_attempts = max_attempts
        self.errors: list[str] = []
        self.built_requests: list[Mapping[str, Any]] = []

    def search(
        self,
        query: str,
        as_of_date: date,
        max_results: int = 100,
    ) -> tuple[SearchResult, ...]:
        url = self.feed_url + ("&" if "?" in self.feed_url else "?") + urlencode({"s": query})
        self.built_requests.append(
            {
                "url": url,
                "query": query,
                "as_of_date": as_of_date.isoformat(),
                "max_results": max_results,
            }
        )
        response = None
        for _ in range(self.max_attempts):
            response = self.transport.fetch(url=url, timeout_seconds=self.timeout_seconds)
            if response.error is None and response.status_code == 200 and response.body:
                break
        if response is None:
            self.errors.append("ISSUER_FEED_NOT_ATTEMPTED")
            return ()
        if response.error or response.status_code != 200 or not response.body:
            self.errors.append(response.error or f"ISSUER_FEED_HTTP_{response.status_code}")
            return ()
        try:
            root = ET.fromstring(response.body)
        except ET.ParseError as exc:
            self.errors.append(f"ISSUER_FEED_XML_INVALID:{exc}")
            return ()
        results: list[SearchResult] = []
        for rank, item in enumerate(root.findall("./channel/item"), start=1):
            title = str(item.findtext("title") or "").strip()
            link = str(item.findtext("link") or "").strip()
            published_text = str(item.findtext("pubDate") or "").strip()
            if not title or not link or not published_text:
                continue
            try:
                published = parsedate_to_datetime(published_text).replace(tzinfo=None)
            except (TypeError, ValueError):
                continue
            if published.date() > as_of_date:
                continue
            results.append(
                SearchResult(
                    title=title,
                    url=link,
                    source="IssuerNewsroomRSS",
                    published_at=published,
                    query=query,
                    rank=rank,
                    confidence=1.0,
                    date_verified=True,
                )
            )
            if len(results) >= max_results:
                break
        return tuple(results)


@dataclass(frozen=True)
class TargetedSmokeRunResult:
    status: str
    report: Mapping[str, Any]
    planner_result: BrainPlannerRunResult
    planning_rows: tuple[Mapping[str, Any], ...]
    question_task_rows: tuple[Mapping[str, Any], ...]
    query_prompt_rows: tuple[Mapping[str, Any], ...]
    query_response_rows: tuple[Mapping[str, Any], ...]
    search_rows: tuple[Mapping[str, Any], ...]
    fetch_rows: tuple[Mapping[str, Any], ...]
    evidence_documents: tuple[Mapping[str, Any], ...]
    claim_result: CurrentClaimCompilationResult


def run_targeted_live_smoke(
    *,
    config_path: str | Path,
    live_root: str | Path,
    current_state_path: str | Path,
    recipe_path: str | Path,
    query_provider: QuestionQueryProvider | None = None,
    search_provider: LiveSearchProvider | None = None,
    source_transport: HistoricalSourceTransport | None = None,
    claim_provider_bundle: Any | None = None,
    test_mode: bool = False,
) -> TargetedSmokeRunResult:
    config = _load_config(config_path)
    as_of = str(config["as_of_date"])
    as_of_value = date.fromisoformat(as_of)
    root = Path(live_root)
    universe = _read_jsonl(root / "universe_eligible.jsonl")
    universe_by_symbol = {str(row.get("symbol") or ""): row for row in universe}
    candidates = load_candidate_events(root / "candidate_events.jsonl")
    signals = load_trigger_signals(root / "trigger_signals.jsonl")
    lanes = load_baseline_lanes(root / "baseline_lanes.jsonl")
    decisions = load_depth_decisions(root / "depth_decisions.jsonl")
    current_state = load_current_state_store(current_state_path)
    mandatory = tuple(dict(item) for item in config["mandatory_targets"])
    mandatory_ids = tuple(str(item["symbol"]) for item in mandatory)
    _validate_mandatory_live_inputs(
        mandatory=mandatory,
        universe_by_symbol=universe_by_symbol,
        candidates=candidates,
        decisions=decisions,
    )

    candidate_by_id = {item.target_id: item for item in candidates}
    forced_decisions = tuple(
        _force_targeted_l3(
            next(item for item in decisions if item.target_id == target_id),
            config=config,
        )
        for target_id in mandatory_ids
    )
    daily_planner = CurrentBrainPlannerRunner().run(
        BrainPlannerConfig(
            as_of_date=as_of,
            max_brain_candidates=len(mandatory_ids),
            max_llm_calls_per_candidate=int(
                config["budgets"]["planner_calls_per_target"]
            ),
            max_parallel_candidates=1,
            attempt_id="phase35-targeted-daily-event",
            test_mode=test_mode,
        ),
        depth_decisions=forced_decisions,
        candidate_events=candidates,
        trigger_signals=signals,
        baseline_lanes=lanes,
        current_state=current_state,
    )

    recipes = tuple(
        item
        for item in load_evidence_recipes(recipe_path)
        if item.archetype_id == config["c06_archetype_id"]
    )
    if not recipes:
        raise ValueError("targeted smoke has no canonical C06 EvidenceRecipes")
    effective_query_provider = query_provider
    if effective_query_provider is None and not test_mode:
        effective_query_provider = build_codex_question_query_provider(
            working_directory=Path.cwd()
        )
    planning_rows: list[Mapping[str, Any]] = []
    tasks: list[Any] = []
    query_prompts: list[Mapping[str, Any]] = []
    query_responses: list[Mapping[str, Any]] = []
    signals_by_id = {item.trigger_signal_id: item for item in signals}
    facts_by_target: dict[str, CurrentEvidenceFact] = {}
    targets_by_id = {str(item["symbol"]): item for item in mandatory}
    recipes_by_id = {item.recipe_id: item for item in recipes}
    for target in mandatory:
        symbol = str(target["symbol"])
        candidate = candidate_by_id[symbol]
        fact = _target_event_fact(candidate, signals_by_id)
        facts_by_target[symbol] = fact
        existing_queries: list[str] = []
        for recipe in recipes:
            draft = _recipe_draft(recipe, target_id=symbol, config=config)
            context = compile_question_task_context(
                target_id=symbol,
                target_name=str(target["company_name"]),
                symbol=symbol,
                target_aliases=tuple(str(item) for item in target["aliases"]),
                as_of_date=as_of,
                current_facts=(fact,),
                missing_information=(
                    recipe.question_to_answer,
                    "current qualification, shipment, revenue mix, cash-flow bridge, conventional-memory drag, and lifecycle evidence",
                    "Use a concise discovery query constrained to the explicit issuer newsroom domains: "
                    + ", ".join(str(item) for item in target["official_domains"]),
                ),
                existing_queries=tuple(existing_queries),
            )
            recording = (
                RecordingQuestionQueryProvider(
                    base=effective_query_provider,
                    target_id=symbol,
                    draft_id=draft.draft_id,
                    prompt_rows=query_prompts,
                    response_rows=query_responses,
                )
                if effective_query_provider is not None
                else None
            )
            planned = plan_question_source_task(
                draft=draft,
                recipe=recipe,
                context=context,
                candidate_event_id=candidate.candidate_event_id,
                task_type=(
                    "red_team"
                    if recipe.role in {"GUARD", "HARD_BREAK"}
                    else "evidence_confirmation"
                ),
                provider=recording,
                test_mode=test_mode,
                max_generation_attempts=int(
                    config["budgets"]["query_generation_attempts"]
                ),
            )
            planning_rows.append(_planning_result_row(planned, symbol, recipe))
            if planned.task is not None:
                tasks.append(planned.task)
                existing_queries.extend(planned.task.query_intent.literal_queries)

    effective_search = search_provider or NaverFreeSearchProvider(
        fixture_mode=test_mode,
        live_enabled=not test_mode,
    )
    effective_transport = source_transport or UrllibHistoricalSourceTransport(
        user_agent="E2R-Targeted-Live-Smoke/1.0"
    )
    search_rows, fetch_rows, evidence_documents = _search_and_fetch(
        config=config,
        targets=mandatory,
        tasks=tasks,
        as_of=as_of_value,
        provider=effective_search,
        transport=effective_transport,
    )
    for repair_round in range(1, int(config["budgets"]["query_search_repair_rounds"]) + 1):
        resolved_task_ids = {
            str(task_id)
            for document in evidence_documents
            for task_id in document.get("source_task_ids") or ()
        }
        unresolved = tuple(item for item in tasks if item.task_id not in resolved_task_ids)
        if not unresolved:
            break
        repair_tasks: list[Any] = []
        for prior_task in unresolved:
            target = targets_by_id[prior_task.target_id]
            recipe = recipes_by_id[prior_task.recipe_id]
            draft = replace(
                _recipe_draft(recipe, target_id=prior_task.target_id, config=config),
                draft_id="SMOKEREPAIR-"
                + stable_hash(
                    {
                        "target": prior_task.target_id,
                        "recipe": recipe.recipe_id,
                        "repair_round": repair_round,
                    }
                )[:24],
            )
            context = compile_question_task_context(
                target_id=prior_task.target_id,
                target_name=str(target["company_name"]),
                symbol=prior_task.target_id,
                target_aliases=tuple(str(item) for item in target["aliases"]),
                as_of_date=as_of,
                current_facts=(facts_by_target[prior_task.target_id],),
                missing_information=(
                    recipe.question_to_answer,
                    "Deterministic search feedback: the previous query yielded no fetchable full document on the allowed issuer newsroom domain.",
                    "Generate one materially different concise discovery query constrained to: "
                    + ", ".join(str(item) for item in target["official_domains"]),
                ),
                existing_queries=prior_task.query_intent.literal_queries,
            )
            recording = (
                RecordingQuestionQueryProvider(
                    base=effective_query_provider,
                    target_id=prior_task.target_id,
                    draft_id=draft.draft_id,
                    prompt_rows=query_prompts,
                    response_rows=query_responses,
                )
                if effective_query_provider is not None
                else None
            )
            planned = plan_question_source_task(
                draft=draft,
                recipe=recipe,
                context=context,
                candidate_event_id=prior_task.candidate_event_id,
                task_type=prior_task.task_type,
                provider=recording,
                test_mode=test_mode,
                max_generation_attempts=int(
                    config["budgets"]["query_generation_attempts"]
                ),
            )
            row = dict(_planning_result_row(planned, prior_task.target_id, recipe))
            row["search_repair_round"] = repair_round
            row["rejected_source_task_id"] = prior_task.task_id
            row["search_feedback_code"] = "OFFICIAL_FULL_DOCUMENT_NOT_FETCHED"
            planning_rows.append(row)
            if planned.task is not None:
                repair_tasks.append(planned.task)
        if not repair_tasks:
            break
        tasks.extend(repair_tasks)
        repair_search, repair_fetch, repair_documents = _search_and_fetch(
            config=config,
            targets=mandatory,
            tasks=repair_tasks,
            as_of=as_of_value,
            provider=effective_search,
            transport=effective_transport,
        )
        search_rows = (*search_rows, *repair_search)
        fetch_rows = (*fetch_rows, *repair_fetch)
        evidence_documents = (*evidence_documents, *repair_documents)
    issuer_feed_errors: list[str] = []
    if effective_query_provider is not None:
        latest_task_by_recipe: dict[tuple[str, str], Any] = {}
        for item in tasks:
            latest_task_by_recipe[(item.target_id, item.recipe_id)] = item
        resolved_task_ids = {
            str(task_id)
            for document in evidence_documents
            for task_id in document.get("source_task_ids") or ()
        }
        site_queries_seen: dict[str, set[str]] = {}
        site_tasks_by_target: dict[str, list[Any]] = {}
        for prior_task in latest_task_by_recipe.values():
            if prior_task.task_id in resolved_task_ids:
                continue
            target = targets_by_id[prior_task.target_id]
            site_query, site_row = _plan_issuer_site_query(
                provider=effective_query_provider,
                target=target,
                task=prior_task,
                as_of_date=as_of,
                seen_queries=site_queries_seen.setdefault(prior_task.target_id, set()),
                prompt_rows=query_prompts,
                response_rows=query_responses,
            )
            planning_rows.append(site_row)
            if site_query is None:
                continue
            site_tasks_by_target.setdefault(prior_task.target_id, []).append(
                SimpleNamespace(
                    target_id=prior_task.target_id,
                    task_id=prior_task.task_id,
                    query_intent=SimpleNamespace(literal_queries=(site_query,)),
                )
            )
        for target_id, site_tasks in site_tasks_by_target.items():
            target = targets_by_id[target_id]
            feed_provider = IssuerNewsroomFeedSearchProvider(
                feed_url=str(target["official_feed_search_url"]),
                transport=effective_transport,
                timeout_seconds=int(config["budgets"]["fetch_timeout_seconds"]),
                max_attempts=int(config["budgets"]["official_feed_search_attempts"]),
            )
            feed_search, feed_fetch, feed_documents = _search_and_fetch(
                config=config,
                targets=(target,),
                tasks=site_tasks,
                as_of=as_of_value,
                provider=feed_provider,
                transport=effective_transport,
            )
            search_rows = (*search_rows, *feed_search)
            fetch_rows = (*fetch_rows, *feed_fetch)
            evidence_documents = (*evidence_documents, *feed_documents)
            issuer_feed_errors.extend(feed_provider.errors)
    task_rows = tuple(item.to_dict() for item in tasks)
    claim_result = CurrentClaimCompiler().compile(
        CurrentClaimCompilerConfig(
            as_of_date=as_of,
            max_documents=max(1, len(evidence_documents)),
            max_raw_assertions_per_document=int(
                config["budgets"]["max_raw_assertions_per_document"]
            ),
            test_mode=test_mode,
        ),
        evidence_documents=evidence_documents,
        question_source_tasks=task_rows,
        provider_fetch_results=fetch_rows,
        provider_bundle=claim_provider_bundle,
    )
    report = _compile_report(
        config=config,
        universe=universe,
        candidates=candidates,
        signals=signals,
        lanes=lanes,
        decisions=decisions,
        planner_result=daily_planner,
        planning_rows=tuple(planning_rows),
        task_rows=task_rows,
        search_rows=search_rows,
        fetch_rows=fetch_rows,
        documents=evidence_documents,
        claim_result=claim_result,
        search_errors=(
            *tuple(getattr(effective_search, "errors", ())),
            *tuple(issuer_feed_errors),
        ),
    )
    return TargetedSmokeRunResult(
        status=str(report["status"]),
        report=report,
        planner_result=daily_planner,
        planning_rows=tuple(planning_rows),
        question_task_rows=task_rows,
        query_prompt_rows=tuple(query_prompts),
        query_response_rows=tuple(query_responses),
        search_rows=search_rows,
        fetch_rows=fetch_rows,
        evidence_documents=evidence_documents,
        claim_result=claim_result,
    )


def write_targeted_live_smoke(
    result: TargetedSmokeRunResult,
    *,
    output_root: str | Path,
    operational_report_path: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths: dict[str, Path] = {
        "planning": root / "source_task_planning_results.jsonl",
        "tasks": root / "question_source_tasks.jsonl",
        "query_prompts": root / "query_generation_prompts.jsonl",
        "query_responses": root / "query_generation_responses.jsonl",
        "search": root / "web_search_results.jsonl",
        "fetch": root / "provider_fetch_results.jsonl",
        "documents": root / "evidence_documents.jsonl",
        "report": root / "targeted_smoke_report.json",
        "operational_report": Path(operational_report_path),
    }
    write_brain_planner_run(result.planner_result, output_root=root / "daily_planner")
    write_jsonl(paths["planning"], result.planning_rows)
    write_jsonl(paths["tasks"], result.question_task_rows)
    write_jsonl(paths["query_prompts"], result.query_prompt_rows)
    write_jsonl(paths["query_responses"], result.query_response_rows)
    write_jsonl(paths["search"], result.search_rows)
    write_jsonl(paths["fetch"], result.fetch_rows)
    write_jsonl(paths["documents"], result.evidence_documents)
    write_current_claim_compilation(result.claim_result, output_root=root / "claims")
    write_json(paths["report"], result.report)
    write_json(paths["operational_report"], result.report)
    return paths


def resume_targeted_smoke_claims(
    *,
    config_path: str | Path,
    snapshot_root: str | Path,
    operational_report_path: str | Path,
    source_transport: HistoricalSourceTransport | None = None,
    query_provider: QuestionQueryProvider | None = None,
    claim_provider_bundle: Any | None = None,
    test_mode: bool = False,
) -> Mapping[str, Any]:
    """Resume official feed acquisition and claim compilation from frozen LLM queries."""

    config = _load_config(config_path)
    root = Path(snapshot_root)
    as_of = str(config["as_of_date"])
    as_of_value = date.fromisoformat(as_of)
    tasks = _read_jsonl(root / "question_source_tasks.jsonl")
    planning = _read_jsonl(root / "source_task_planning_results.jsonl")
    planning = list(planning)
    query_prompts = list(_read_jsonl(root / "query_generation_prompts.jsonl"))
    query_responses = list(_read_jsonl(root / "query_generation_responses.jsonl"))
    search_rows = list(_read_jsonl(root / "web_search_results.jsonl"))
    fetch_rows = list(_read_jsonl(root / "provider_fetch_results.jsonl"))
    documents = list(_read_jsonl(root / "evidence_documents.jsonl"))
    report = json.loads(Path(operational_report_path).read_text(encoding="utf-8"))
    task_by_id = {str(item["task_id"]): item for item in tasks}
    targets = tuple(dict(item) for item in config["mandatory_targets"])
    target_by_id = {str(item["symbol"]): item for item in targets}
    transport = source_transport or UrllibHistoricalSourceTransport(
        user_agent="E2R-Targeted-Live-Smoke-Resume/1.0"
    )
    feed_errors: list[str] = []
    site_rows_by_target: dict[str, list[Mapping[str, Any]]] = {}
    for row in planning:
        if (
            row.get("query_generation_route") == "ISSUER_NEWSROOM_NATIVE_SEARCH"
            and row.get("status") == "COMPLETE"
            and str(row.get("site_search_query") or "").strip()
        ):
            site_rows_by_target.setdefault(str(row["target_id"]), []).append(row)
    effective_query_provider = query_provider
    for target_id, rows in site_rows_by_target.items():
        target = target_by_id[target_id]
        wrappers = []
        for row in rows:
            task = task_by_id.get(str(row["task_id"]))
            if task is None:
                raise ValueError("resume site query references unknown QuestionSourceTask")
            wrappers.append(
                SimpleNamespace(
                    target_id=target_id,
                    task_id=task["task_id"],
                    query_intent=SimpleNamespace(
                        literal_queries=(str(row["site_search_query"]),)
                    ),
                )
            )
        provider = IssuerNewsroomFeedSearchProvider(
            feed_url=str(target["official_feed_search_url"]),
            transport=transport,
            timeout_seconds=int(config["budgets"]["fetch_timeout_seconds"]),
            max_attempts=int(config["budgets"]["official_feed_search_attempts"]),
        )
        new_search, new_fetch, new_documents = _search_and_fetch(
            config=config,
            targets=(target,),
            tasks=tuple(wrappers),
            as_of=as_of_value,
            provider=provider,
            transport=transport,
        )
        if not new_documents:
            if effective_query_provider is None and not test_mode:
                effective_query_provider = build_codex_question_query_provider(
                    working_directory=Path.cwd()
                )
            if effective_query_provider is not None:
                seen_queries = {
                    str(item.get("site_search_query") or "").casefold()
                    for item in rows
                    if str(item.get("site_search_query") or "").strip()
                }
                latest_task_by_recipe: dict[str, Mapping[str, Any]] = {}
                for item in tasks:
                    if item.get("target_id") == target_id:
                        latest_task_by_recipe[str(item["recipe_id"])] = item
                regenerated_tasks = []
                for task_row in latest_task_by_recipe.values():
                    prior_queries = tuple(
                        str(item.get("site_search_query") or "")
                        for item in rows
                        if item.get("recipe_id") == task_row["recipe_id"]
                        and str(item.get("site_search_query") or "").strip()
                    ) or tuple(task_row["query_intent"]["literal_queries"])
                    task_object = SimpleNamespace(
                        target_id=target_id,
                        task_id=task_row["task_id"],
                        recipe_id=task_row["recipe_id"],
                        primitive_id=task_row["primitive_id"],
                        question_to_answer=task_row["question_to_answer"],
                        query_intent=SimpleNamespace(literal_queries=prior_queries),
                    )
                    site_query, site_row = _plan_issuer_site_query(
                        provider=effective_query_provider,
                        target=target,
                        task=task_object,
                        as_of_date=as_of,
                        seen_queries=seen_queries,
                        prompt_rows=query_prompts,
                        response_rows=query_responses,
                    )
                    repair_row = dict(site_row)
                    repair_row["search_repair_round"] = "RESUME_OFFICIAL_FEED_TITLE_MATCH_ZERO"
                    repair_row["search_feedback_code"] = "OFFICIAL_FEED_TITLE_MATCH_ZERO"
                    planning.append(repair_row)
                    if site_query is not None:
                        regenerated_tasks.append(
                            SimpleNamespace(
                                target_id=target_id,
                                task_id=task_row["task_id"],
                                query_intent=SimpleNamespace(
                                    literal_queries=(site_query,)
                                ),
                            )
                        )
                repaired_search, repaired_fetch, repaired_documents = _search_and_fetch(
                    config=config,
                    targets=(target,),
                    tasks=tuple(regenerated_tasks),
                    as_of=as_of_value,
                    provider=provider,
                    transport=transport,
                )
                new_search = (*new_search, *repaired_search)
                new_fetch = (*new_fetch, *repaired_fetch)
                new_documents = (*new_documents, *repaired_documents)
        search_rows.extend(new_search)
        fetch_rows.extend(new_fetch)
        documents.extend(new_documents)
        feed_errors.extend(provider.errors)
    merged_documents = _merge_evidence_documents(documents)
    selected_documents = _select_claim_documents(
        documents=merged_documents,
        target_ids=tuple(target_by_id),
        max_per_target=int(config["budgets"]["claim_documents_per_target"]),
        as_of_date=as_of,
    )
    claim_result = CurrentClaimCompiler().compile(
        CurrentClaimCompilerConfig(
            as_of_date=as_of,
            max_documents=max(1, len(selected_documents)),
            max_raw_assertions_per_document=int(
                config["budgets"]["max_raw_assertions_per_document"]
            ),
            test_mode=test_mode,
        ),
        evidence_documents=selected_documents,
        question_source_tasks=tasks,
        provider_fetch_results=tuple(fetch_rows),
        provider_bundle=claim_provider_bundle,
    )
    refreshed = _refresh_report_claim_section(
        report=report,
        config=config,
        planning_rows=tuple(planning),
        documents=selected_documents,
        claim_result=claim_result,
        resume_feed_errors=tuple(feed_errors),
    )
    write_jsonl(root / "web_search_results.jsonl", search_rows)
    write_jsonl(root / "provider_fetch_results.jsonl", fetch_rows)
    write_jsonl(root / "evidence_documents.jsonl", merged_documents)
    write_jsonl(root / "claim_selected_documents.jsonl", selected_documents)
    write_jsonl(root / "source_task_planning_results.jsonl", planning)
    write_jsonl(root / "query_generation_prompts.jsonl", query_prompts)
    write_jsonl(root / "query_generation_responses.jsonl", query_responses)
    write_current_claim_compilation(claim_result, output_root=root / "claims")
    write_json(root / "targeted_smoke_report.json", refreshed)
    write_json(Path(operational_report_path), refreshed)
    return refreshed


def audit_targeted_smoke_snapshot(
    *,
    config_path: str | Path,
    snapshot_root: str | Path,
    operational_report_path: str | Path,
) -> Mapping[str, Any]:
    """Re-audit frozen Phase 35 leaves without provider or network calls."""

    config = _load_config(config_path)
    root = Path(snapshot_root)
    report = json.loads(Path(operational_report_path).read_text(encoding="utf-8"))
    planning = _read_jsonl(root / "source_task_planning_results.jsonl")
    selected_path = root / "claim_selected_documents.jsonl"
    documents = _read_jsonl(
        selected_path if selected_path.is_file() else root / "evidence_documents.jsonl"
    )
    claim_root = root / "claims"
    provenance = tuple(
        DailyClaimProvenance(
            **{
                **dict(row),
                "source_ids": tuple(row.get("source_ids") or ()),
                "anchor_ids": tuple(row.get("anchor_ids") or ()),
                "mapping_ids": tuple(row.get("mapping_ids") or ()),
            }
        )
        for row in _read_jsonl(claim_root / "daily_claim_provenance.jsonl")
    )
    satisfaction = tuple(
        SourceTaskSatisfactionRecord(
            **{
                **dict(row),
                "document_ids": tuple(row.get("document_ids") or ()),
                "raw_assertion_ids": tuple(row.get("raw_assertion_ids") or ()),
                "accepted_claim_ids": tuple(row.get("accepted_claim_ids") or ()),
                "accepted_mapping_ids": tuple(row.get("accepted_mapping_ids") or ()),
                "rerouted_mapping_ids": tuple(row.get("rerouted_mapping_ids") or ()),
            }
        )
        for row in _read_jsonl(claim_root / "source_task_satisfaction.jsonl")
    )
    audit = json.loads((claim_root / "claim_compiler_audit.json").read_text(encoding="utf-8"))
    claim_result = CurrentClaimCompilationResult(
        as_of_date=str(config["as_of_date"]),
        status=str(audit.get("status") or "CURRENT_CLAIM_COMPILER_PASS"),
        evidence_anchors=_read_jsonl(claim_root / "evidence_anchors.jsonl"),
        raw_assertions=_read_jsonl(claim_root / "raw_assertions.jsonl"),
        adjudicated_claims=_read_jsonl(claim_root / "adjudicated_claims.jsonl"),
        primitive_mappings=_read_jsonl(claim_root / "primitive_mappings.jsonl"),
        accepted_current_claims=_read_jsonl(
            claim_root / "accepted_current_claims.jsonl"
        ),
        daily_claim_provenance=provenance,
        source_task_satisfaction=satisfaction,
        compilation_pending=_read_jsonl(claim_root / "claim_compilation_pending.jsonl"),
        audit=audit,
    )
    refreshed = _refresh_report_claim_section(
        report=report,
        config=config,
        planning_rows=planning,
        documents=documents,
        claim_result=claim_result,
        resume_feed_errors=(),
    )
    refreshed["frozen_snapshot_audit"] = {
        "provider_calls": 0,
        "network_calls": 0,
        "claim_leaf_hash": stable_hash(claim_result.accepted_current_claims),
        "provenance_leaf_hash": stable_hash(
            [item.to_dict() for item in claim_result.daily_claim_provenance]
        ),
        "audited_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    write_json(root / "targeted_smoke_report.json", refreshed)
    write_json(Path(operational_report_path), refreshed)
    return refreshed


def _merge_evidence_documents(
    rows: Sequence[Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    merged: dict[tuple[str, str], dict[str, Any]] = {}
    for row in rows:
        key = (str(row.get("target_id") or ""), str(row.get("document_id") or ""))
        if not all(key):
            raise ValueError("evidence document merge identity is incomplete")
        existing = merged.get(key)
        if existing is None:
            merged[key] = dict(row)
            continue
        if existing.get("content_hash") != row.get("content_hash"):
            raise ValueError("same evidence document identity has different content hash")
        existing["source_task_ids"] = list(
            dict.fromkeys(
                (*existing.get("source_task_ids", ()), *row.get("source_task_ids", ()))
            )
        )
    return tuple(
        merged[key] for key in sorted(merged, key=lambda item: (item[0], item[1]))
    )


def _select_claim_documents(
    *,
    documents: Sequence[Mapping[str, Any]],
    target_ids: Sequence[str],
    max_per_target: int,
    as_of_date: str,
) -> tuple[Mapping[str, Any], ...]:
    as_of = date.fromisoformat(as_of_date)
    selected: list[Mapping[str, Any]] = []
    for target_id in target_ids:
        candidates = [item for item in documents if item.get("target_id") == target_id]
        candidates.sort(
            key=lambda item: (
                -int(date.fromisoformat(str(item["published_at"])).year == as_of.year),
                -len(tuple(item.get("source_task_ids") or ())),
                -date.fromisoformat(str(item["published_at"])).toordinal(),
                str(item["document_id"]),
            )
        )
        selected.extend(candidates[:max_per_target])
    return tuple(selected)


def _refresh_report_claim_section(
    *,
    report: Mapping[str, Any],
    config: Mapping[str, Any],
    planning_rows: Sequence[Mapping[str, Any]],
    documents: Sequence[Mapping[str, Any]],
    claim_result: CurrentClaimCompilationResult,
    resume_feed_errors: Sequence[str],
) -> Mapping[str, Any]:
    refreshed = json.loads(json.dumps(report, ensure_ascii=False))
    accepted_by_target: dict[str, list[Mapping[str, Any]]] = {}
    for item in claim_result.accepted_current_claims:
        accepted_by_target.setdefault(
            str(item.get("target_id") or item.get("target_entity_id") or ""), []
        ).append(item)
    provenance_by_target: dict[str, list[Any]] = {}
    for item in claim_result.daily_claim_provenance:
        provenance_by_target.setdefault(item.target_id, []).append(item)
    satisfaction_by_target: dict[str, list[Any]] = {}
    for item in claim_result.source_task_satisfaction:
        satisfaction_by_target.setdefault(item.target_id, []).append(item)
    for target_report in refreshed["mandatory_targets"]:
        target_id = str(target_report["symbol"])
        target_documents = [item for item in documents if item.get("target_id") == target_id]
        target_claims = accepted_by_target.get(target_id, [])
        target_provenance = provenance_by_target.get(target_id, [])
        target_satisfaction = satisfaction_by_target.get(target_id, [])
        provider_pending = any(
            item.get("target_id") == target_id and item.get("status") == "PENDING"
            for item in planning_rows
        )
        source_pending = not target_documents or any(
            item.original_gap_open for item in target_satisfaction
        )
        atomic = _pending_atomic_decision(
            as_of_date=str(config["as_of_date"]),
            target_id=target_id,
            satisfaction=target_satisfaction,
            provider_pending=provider_pending,
            source_pending=source_pending,
        )
        target_report["full_thesis_status"] = _full_thesis_status(
            provider_pending=provider_pending,
            documents=target_documents,
            satisfaction=target_satisfaction,
        )
        target_report["diagnostic_slots"] = _diagnostic_slots(
            slots=tuple(config["full_thesis_diagnostic_slots"]),
            documents=target_documents,
            satisfaction=target_satisfaction,
        )
        target_report["accepted_current_claims"] = [
            {
                "claim_id": item.get("claim_id"),
                "document_id": item.get("document_id"),
                "polarity": item.get("polarity"),
                "temporal_status": item.get("temporal_status"),
                "exact_quote": (item.get("raw_assertion") or {}).get("exact_quote"),
                "mapping_ids": item.get("mapping_ids"),
            }
            for item in target_claims
        ]
        target_report["claim_provenance"] = [
            {
                "provenance_id": item.provenance_id,
                "claim_id": item.claim_id,
                "document_id": item.document_id,
                "source_url": item.source_url,
                "published_date": item.published_date,
                "content_sha256": item.content_sha256,
                "anchor_ids": list(item.anchor_ids),
                "mapping_ids": list(item.mapping_ids),
            }
            for item in target_provenance
        ]
        target_report["source_task_satisfaction"] = [
            item.to_dict() for item in target_satisfaction
        ]
        target_report["fetched_documents"] = [
            {
                "document_id": item["document_id"],
                "canonical_url": item["canonical_url"],
                "published_at": item["published_at"],
                "content_hash": item["content_hash"],
                "source_task_ids": item["source_task_ids"],
                "actual_live_full_document": True,
            }
            for item in target_documents
        ]
        target_report["provider_source_gaps"]["open_primitives"] = [
            item.primitive_id for item in target_satisfaction if item.original_gap_open
        ]
        target_report["score_type"] = atomic.score_type
        target_report["score_valid"] = atomic.score_valid
        target_report["score_value"] = atomic.score_value
        target_report["canonical_stage"] = atomic.canonical_stage
        target_report["stage_court_trace"] = atomic.stage_court_trace.to_dict()
    aggregate = refreshed["aggregate"]
    aggregate["actual_live_full_document_count"] = len(documents)
    aggregate["accepted_current_claim_count"] = len(claim_result.accepted_current_claims)
    aggregate["claim_provenance_count"] = len(claim_result.daily_claim_provenance)
    aggregate["source_task_satisfaction_count"] = len(claim_result.source_task_satisfaction)
    aggregate["question_planning_count"] = len(planning_rows)
    aggregate["resume_official_feed_errors"] = list(resume_feed_errors)
    previous_provider_errors = list(aggregate.get("search_provider_errors") or ())
    if previous_provider_errors:
        aggregate["recovered_provider_error_history"] = list(
            dict.fromkeys(
                (*aggregate.get("recovered_provider_error_history", ()), *previous_provider_errors)
            )
        )
    aggregate["search_provider_errors"] = list(resume_feed_errors)
    hard = refreshed["hard_acceptance_counts"]
    target_ids = [str(item["symbol"]) for item in refreshed["mandatory_targets"]]
    hard["actual_live_full_document_missing_count"] = sum(
        not any(item.get("target_id") == target_id for item in documents)
        for target_id in target_ids
    )
    hard["claim_provenance_missing_count"] = sum(
        bool(accepted_by_target.get(target_id, ()))
        and not bool(provenance_by_target.get(target_id, ()))
        for target_id in target_ids
    )
    hard["accepted_claim_without_provenance_count"] = int(
        claim_result.audit["critical_counts"]["accepted_claim_without_provenance"]
    )
    hard["future_document_count"] = sum(
        str(item["published_at"]) > str(config["as_of_date"]) for item in documents
    )
    hard["snippet_used_as_evidence_count"] = sum(
        bool(item.get("search_snippet_used_as_evidence")) for item in documents
    )
    critical = sum(int(value) for value in hard.values())
    refreshed["critical_count_sum"] = critical
    refreshed["hard_acceptance_pass"] = critical == 0
    refreshed["status"] = (
        "TARGETED_LIVE_SMOKE_PASS" if critical == 0 else "TARGETED_LIVE_SMOKE_FAIL"
    )
    refreshed.setdefault("safety", {})[
        "accepted_claim_provenance_contract_complete"
    ] = (
        claim_result.audit["critical_counts"]["accepted_claim_without_provenance"]
        == 0
    )
    refreshed["resume"] = {
        "resumed_from_frozen_llm_queries": True,
        "claim_extractor_max_assertions": 12,
        "selected_document_count": len(documents),
        "refreshed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    return refreshed


def select_sector_samples(
    *,
    as_of_date: str,
    universe: Sequence[Mapping[str, Any]],
    candidate_pools: Mapping[str, Sequence[str]],
) -> tuple[Mapping[str, Any], ...]:
    eligible = {
        str(row.get("symbol") or ""): row
        for row in universe
        if row.get("eligible") is True
    }
    selected: list[Mapping[str, Any]] = []
    for sector in (f"L{index}" for index in range(1, 10)):
        candidates = [
            eligible[symbol]
            for symbol in candidate_pools.get(sector, ())
            if symbol in eligible
        ]
        if not candidates:
            raise ValueError(f"sector smoke pool has no eligible current symbol: {sector}")
        winner = min(
            candidates,
            key=lambda row: stable_hash(
                {
                    "as_of_date": as_of_date,
                    "sector": sector,
                    "symbol": row["symbol"],
                }
            ),
        )
        selected.append(
            {
                "sector": sector,
                "selection_rule": "MIN_STABLE_HASH_WITHIN_EXPLICIT_VALIDATION_POOL",
                "selection_hash": stable_hash(
                    {
                        "as_of_date": as_of_date,
                        "sector": sector,
                        "symbol": winner["symbol"],
                    }
                ),
                "symbol": winner["symbol"],
                "company_name": winner["company_name"],
                "market": winner["market"],
            }
        )
    return tuple(selected)


def _load_config(path: str | Path) -> Mapping[str, Any]:
    config = json.loads(Path(path).read_text(encoding="utf-8"))
    if config.get("schema_version") != TARGETED_SMOKE_CONFIG_SCHEMA_VERSION:
        raise ValueError("targeted smoke config schema mismatch")
    date.fromisoformat(str(config.get("as_of_date") or ""))
    mandatory = config.get("mandatory_targets")
    if not isinstance(mandatory, list) or len(mandatory) != 2:
        raise ValueError("targeted smoke requires exactly two mandatory targets")
    if {str(item.get("symbol") or "") for item in mandatory} != {"005930", "000660"}:
        raise ValueError("targeted smoke mandatory symbols differ from Goal")
    if tuple(sorted(config.get("sector_candidate_pools") or {})) != tuple(
        f"L{index}" for index in range(1, 10)
    ):
        raise ValueError("targeted smoke requires sector pools L1 through L9")
    return config


def _validate_mandatory_live_inputs(
    *,
    mandatory: Sequence[Mapping[str, Any]],
    universe_by_symbol: Mapping[str, Mapping[str, Any]],
    candidates: Sequence[Any],
    decisions: Sequence[Any],
) -> None:
    candidate_ids = {item.target_id for item in candidates}
    decision_ids = {item.target_id for item in decisions}
    for target in mandatory:
        symbol = str(target["symbol"])
        row = universe_by_symbol.get(symbol)
        if row is None or row.get("eligible") is not True:
            raise ValueError(f"mandatory smoke target absent from live KRX universe: {symbol}")
        if symbol not in candidate_ids or symbol not in decision_ids:
            raise ValueError(f"mandatory smoke target lacks current trigger/depth: {symbol}")


def _force_targeted_l3(decision: Any, *, config: Mapping[str, Any]) -> Any:
    fetches = int(config["budgets"]["fetches_per_target"])
    return replace(
        decision,
        depth_decision_id="SMOKEDEPTH-"
        + stable_hash({"base": decision.depth_decision_id, "phase": 35})[:24],
        completed_depths=tuple(item.value for item in tuple(LiveDepth)[:4]),
        maximum_depth=LiveDepth.L3_RESEARCH_BRAIN.value,
        selected_for_deep=True,
        selected_for_brain=True,
        acquisition_eligible=True,
        selection_reasons=("EXPLICIT_PHASE35_VALIDATION_TARGET",),
        not_selected_reason=None,
        source_task_budget={"max_tasks": 6, "max_fetches": fetches, "max_retries": 1},
        llm_budget={
            "max_calls": int(config["budgets"]["planner_calls_per_target"])
        },
        general_web_budget={"max_fetches": fetches},
    )


def _target_event_fact(candidate: Any, signals_by_id: Mapping[str, Any]) -> CurrentEvidenceFact:
    target_signals = [signals_by_id[item] for item in candidate.trigger_signal_ids]
    descriptions = tuple(
        str((signal.payload or {}).get("report_name") or signal.trigger_type)
        for signal in target_signals
    )
    return CurrentEvidenceFact(
        fact_id="SMOKEFACT-" + stable_hash(candidate.candidate_event_id)[:24],
        text=(
            f"{candidate.target_name}의 {candidate.as_of_date} 현재 공식 이벤트는 "
            + ", ".join(descriptions)
            + ". 이 이벤트 자체가 장기 사업 논리를 입증하는지는 별도 원문 조사가 필요하다."
        ),
        observed_date=candidate.as_of_date,
        target_relation="DIRECT",
        current_status="CURRENT_UNADJUDICATED",
    )


def _recipe_draft(
    recipe: EvidenceRecipe,
    *,
    target_id: str,
    config: Mapping[str, Any],
) -> PlannerSourceTaskDraft:
    official = tuple(
        item
        for item in recipe.preferred_source_families
        if item in {"DART", "IssuerIR", "CompanyEarningsCall", "IssuerNewsroom"}
    ) or ("IssuerIR",)
    fallback = tuple(
        item for item in recipe.discovery_sources if item not in set(official)
    ) or ("NaverSearch",)
    return PlannerSourceTaskDraft(
        draft_id="SMOKEDRAFT-"
        + stable_hash({"target": target_id, "recipe": recipe.recipe_id})[:24],
        recipe_id=recipe.recipe_id,
        question_to_answer=recipe.question_to_answer,
        why_material=recipe.economic_mechanism,
        query_intent=(
            "Find current, target-direct, full official documents that answer the semantic "
            "question and its counter/supersession checks."
        ),
        preferred_source_families=official,
        fallback_source_families=fallback,
        max_queries=int(config["budgets"]["queries_per_task"]),
        max_candidates=int(config["budgets"]["search_candidates_per_query"]),
        max_fetches=int(config["budgets"]["fetches_per_target"]),
        stop_condition=recipe.stop_conditions[0],
    )


def _planning_result_row(result: Any, target_id: str, recipe: EvidenceRecipe) -> Mapping[str, Any]:
    return {
        "schema_version": TARGETED_SMOKE_SCHEMA_VERSION,
        "input_id": result.input_id,
        "target_id": target_id,
        "recipe_id": recipe.recipe_id,
        "primitive_id": recipe.primitive_id,
        "status": result.status,
        "task_id": result.task.task_id if result.task else None,
        "pending": result.pending.to_dict() if result.pending else None,
        "abstention_reason": result.abstention_reason,
        "traces": [item.to_dict() for item in result.traces],
    }


def _plan_issuer_site_query(
    *,
    provider: QuestionQueryProvider,
    target: Mapping[str, Any],
    task: Any,
    as_of_date: str,
    seen_queries: set[str],
    prompt_rows: list[Mapping[str, Any]],
    response_rows: list[Mapping[str, Any]],
) -> tuple[str | None, Mapping[str, Any]]:
    feedback: list[str] = []
    input_id = "issuer-site-query-" + stable_hash(
        {
            "target_id": task.target_id,
            "task_id": task.task_id,
            "question": task.question_to_answer,
            "as_of_date": as_of_date,
        }
    )[:24]
    for attempt in range(1, 4):
        prompt_payload = {
            "input_id": input_id,
            "target_id": task.target_id,
            "target_name": target["company_name"],
            "target_aliases": list(target["aliases"]),
            "official_domain": target["official_domains"][0],
            "official_feed_language": target["official_feed_language"],
            "as_of_date": as_of_date,
            "question_to_answer": task.question_to_answer,
            "previous_general_search_queries": list(task.query_intent.literal_queries),
            "validation_feedback": list(feedback),
            "instruction": (
                "Create one native issuer-newsroom search phrase of one to three whitespace-separated terms. "
                "The issuer domain is already scoped, so do not emit site:, dates, Boolean operators, quotes, URLs, "
                "or the company name. Use only the configured official_feed_language. Select the terms semantically; "
                "deterministic code will only validate and execute them."
            ),
        }
        prompt = (
            "You generate a short official newsroom search phrase. Return only JSON matching the schema.\n"
            + json.dumps(prompt_payload, ensure_ascii=False, sort_keys=True)
        )
        prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        call_id = "SITEQUERYCALL-" + stable_hash(
            {"input_id": input_id, "attempt": attempt, "prompt_hash": prompt_hash}
        )[:24]
        prompt_rows.append(
            {
                "schema_version": TARGETED_SMOKE_SCHEMA_VERSION,
                "call_id": call_id,
                "input_id": input_id,
                "target_id": task.target_id,
                "source_task_id": task.task_id,
                "query_generation_route": "ISSUER_NEWSROOM_NATIVE_SEARCH",
                "provider_name": provider.provider_name,
                "prompt_hash": prompt_hash,
                "prompt_text": prompt,
            }
        )
        try:
            completion = provider.complete(prompt=prompt, output_schema=_ISSUER_SITE_QUERY_SCHEMA)
            payload = dict(completion.payload)
            response_hash = hashlib.sha256(completion.raw_response.encode("utf-8")).hexdigest()
            query = str(payload.get("site_search_query") or "").strip()
            error = _issuer_site_query_validation_error(
                payload=payload,
                expected_input_id=input_id,
                query=query,
                seen_queries=seen_queries,
                as_of_date=as_of_date,
            )
            response_rows.append(
                {
                    "schema_version": TARGETED_SMOKE_SCHEMA_VERSION,
                    "call_id": call_id,
                    "input_id": input_id,
                    "target_id": task.target_id,
                    "source_task_id": task.task_id,
                    "query_generation_route": "ISSUER_NEWSROOM_NATIVE_SEARCH",
                    "provider_name": provider.provider_name,
                    "status": "COMPLETED" if error is None else "VALIDATION_REJECTED",
                    "response_hash": response_hash,
                    "response_payload": payload,
                    "validation_error": error,
                }
            )
            if error is None:
                seen_queries.add(query.casefold())
                return query, {
                    "schema_version": TARGETED_SMOKE_SCHEMA_VERSION,
                    "input_id": input_id,
                    "target_id": task.target_id,
                    "recipe_id": task.recipe_id,
                    "primitive_id": task.primitive_id,
                    "status": "COMPLETE",
                    "task_id": task.task_id,
                    "query_generation_route": "ISSUER_NEWSROOM_NATIVE_SEARCH",
                    "site_search_query": query,
                    "provider_name": provider.provider_name,
                    "generator_kind": provider.generator_kind,
                    "attempt_count": attempt,
                    "prompt_hash": prompt_hash,
                    "response_hash": response_hash,
                    "validation_feedback": list(feedback),
                }
            feedback.append(f"attempt_{attempt}:{error}")
        except Exception as exc:
            response_rows.append(
                {
                    "schema_version": TARGETED_SMOKE_SCHEMA_VERSION,
                    "call_id": call_id,
                    "input_id": input_id,
                    "target_id": task.target_id,
                    "source_task_id": task.task_id,
                    "query_generation_route": "ISSUER_NEWSROOM_NATIVE_SEARCH",
                    "provider_name": provider.provider_name,
                    "status": "PROVIDER_ERROR",
                    "response_hash": hashlib.sha256(type(exc).__name__.encode()).hexdigest(),
                    "response_payload": {},
                    "validation_error": f"{type(exc).__name__}:{exc}",
                }
            )
            feedback.append(f"attempt_{attempt}:PROVIDER_ERROR:{type(exc).__name__}")
    return None, {
        "schema_version": TARGETED_SMOKE_SCHEMA_VERSION,
        "input_id": input_id,
        "target_id": task.target_id,
        "recipe_id": task.recipe_id,
        "primitive_id": task.primitive_id,
        "status": "PENDING",
        "task_id": task.task_id,
        "query_generation_route": "ISSUER_NEWSROOM_NATIVE_SEARCH",
        "site_search_query": None,
        "provider_name": provider.provider_name,
        "generator_kind": provider.generator_kind,
        "attempt_count": 3,
        "validation_feedback": feedback,
        "pending_reason": "ISSUER_SITE_QUERY_RETRY_EXHAUSTED",
    }


def _issuer_site_query_validation_error(
    *,
    payload: Mapping[str, Any],
    expected_input_id: str,
    query: str,
    seen_queries: set[str],
    as_of_date: str,
) -> str | None:
    if set(payload) != {"input_id", "site_search_query", "rationale"}:
        return "OUTPUT_KEYS_MISMATCH"
    if str(payload.get("input_id") or "") != expected_input_id:
        return "INPUT_ID_MISMATCH"
    if not str(payload.get("rationale") or "").strip():
        return "RATIONALE_MISSING"
    terms = query.split()
    if not 1 <= len(terms) <= 3:
        return "QUERY_MUST_HAVE_ONE_TO_THREE_TERMS"
    lowered = query.casefold()
    if lowered in seen_queries:
        return "DUPLICATE_ALREADY_EXECUTED_QUERY"
    if any(token in lowered for token in ("site:", "http://", "https://", " or ", " and ", '"')):
        return "QUERY_CONTAINS_FORBIDDEN_SEARCH_SYNTAX"
    for year in re.findall(r"\b20\d{2}\b", query):
        if int(year) > int(as_of_date[:4]):
            return "QUERY_CONTAINS_FUTURE_YEAR"
    return None


def _search_and_fetch(
    *,
    config: Mapping[str, Any],
    targets: Sequence[Mapping[str, Any]],
    tasks: Sequence[Any],
    as_of: date,
    provider: LiveSearchProvider,
    transport: HistoricalSourceTransport,
) -> tuple[
    tuple[Mapping[str, Any], ...],
    tuple[Mapping[str, Any], ...],
    tuple[Mapping[str, Any], ...],
]:
    target_by_id = {str(item["symbol"]): item for item in targets}
    search_rows: list[Mapping[str, Any]] = []
    candidates_by_target: dict[str, dict[str, dict[str, Any]]] = {}
    for task in tasks:
        target = target_by_id[task.target_id]
        if len(candidates_by_target.get(task.target_id, {})) >= int(
            config["budgets"]["fetches_per_target"]
        ):
            continue
        for query in task.query_intent.literal_queries:
            results = provider.search(
                query,
                as_of,
                int(config["budgets"]["search_candidates_per_query"]),
            )
            added_for_query = 0
            for result in results:
                official = _url_on_allowed_domain(
                    result.url,
                    tuple(str(item) for item in target["official_domains"]),
                )
                visible = result.published_at is None or result.published_at.date() <= as_of
                direct_query_title_match = _search_result_matches_llm_query(
                    query=query,
                    title=result.title,
                )
                issuer_current_top_rank_fallback = (
                    result.source == "IssuerNewsroomRSS"
                    and result.published_at is not None
                    and result.published_at.date().year == as_of.year
                    and 0 < result.rank <= 2
                )
                query_title_match = (
                    direct_query_title_match or issuer_current_top_rank_fallback
                )
                row = {
                    "schema_version": TARGETED_SMOKE_SCHEMA_VERSION,
                    "target_id": task.target_id,
                    "source_task_id": task.task_id,
                    "query": query,
                    "title": result.title,
                    "url": result.url,
                    "published_at": (
                        result.published_at.date().isoformat()
                        if result.published_at
                        else None
                    ),
                    "rank": result.rank,
                    "source": result.source,
                    "official_domain_match": official,
                    "as_of_visible": visible,
                    "query_title_match": query_title_match,
                    "direct_query_title_match": direct_query_title_match,
                    "issuer_current_top_rank_fallback": (
                        issuer_current_top_rank_fallback
                    ),
                    "snippet_score_eligible": False,
                }
                search_rows.append(row)
                if not official or not visible or not query_title_match:
                    continue
                target_candidates = candidates_by_target.setdefault(task.target_id, {})
                selected = target_candidates.setdefault(
                    result.url,
                    {"result": result, "task_ids": [], "best_rank": result.rank or 9999},
                )
                selected["task_ids"].append(task.task_id)
                selected["best_rank"] = min(selected["best_rank"], result.rank or 9999)
                added_for_query += 1
                if added_for_query >= int(
                    config["budgets"]["fetch_candidates_per_query"]
                ):
                    break
            if len(candidates_by_target.get(task.target_id, {})) >= int(
                config["budgets"]["fetches_per_target"]
            ):
                break

    fetch_rows: list[Mapping[str, Any]] = []
    documents: list[Mapping[str, Any]] = []
    for target_id, url_items in sorted(candidates_by_target.items()):
        target = target_by_id[target_id]
        ordered = sorted(
            url_items.items(),
            key=lambda item: (item[1]["best_rank"], item[0]),
        )[: int(config["budgets"]["fetches_per_target"])]
        for url, metadata in ordered:
            response = transport.fetch(
                url=url,
                timeout_seconds=int(config["budgets"]["fetch_timeout_seconds"]),
            )
            base = {
                "schema_version": TARGETED_SMOKE_SCHEMA_VERSION,
                "target_id": target_id,
                "source_task_ids": list(dict.fromkeys(metadata["task_ids"])),
                "requested_url": url,
                "canonical_url": response.url,
                "http_status": response.status_code,
                "content_type": response.content_type,
                "raw_content_hash": hashlib.sha256(response.body).hexdigest(),
                "raw_byte_count": len(response.body),
                "error": response.error,
                "actual_live_fetch": True,
            }
            try:
                if response.error or response.status_code != 200 or not response.body:
                    raise ValueError(response.error or f"HTTP_{response.status_code}")
                if not _url_on_allowed_domain(
                    response.url,
                    tuple(str(item) for item in target["official_domains"]),
                ):
                    raise ValueError("OFFICIAL_DOMAIN_REDIRECT_VIOLATION")
                text, _ = extract_source_full_text(
                    response.body,
                    content_type=response.content_type,
                )
                if len(text) < 200:
                    raise ValueError("FULL_DOCUMENT_TEXT_TOO_SHORT")
                if not _target_marker_present(text, target):
                    raise ValueError("TARGET_MARKER_MISSING")
                search_result = metadata["result"]
                page_published = _published_date_from_text(text, as_of=as_of)
                search_published = (
                    search_result.published_at.date()
                    if search_result.published_at is not None
                    else None
                )
                published = (
                    search_published
                    if search_result.date_verified is True
                    else page_published or search_published
                )
                if published is None:
                    raise ValueError("PUBLISHED_DATE_UNVERIFIED")
                if published > as_of:
                    raise ValueError("FUTURE_DATE_REJECTED")
                evidence = EvidenceDocument.from_text(
                    text=text,
                    canonical_url=response.url,
                    source_type=SourceType.IR,
                    source_name="IssuerNewsroom",
                    published_at=published,
                    available_at=published,
                    fetched_at=date.today(),
                    parser_version="e2r-targeted-live-smoke-v1",
                    source_lineage_id="SMOKEFETCH-" + stable_hash(response.url)[:20],
                    source_proxy_only=False,
                )
                document = {
                    "schema_version": TARGETED_SMOKE_SCHEMA_VERSION,
                    "document_id": evidence.document_id,
                    "target_id": target_id,
                    "target_name": target["company_name"],
                    "source_task_ids": list(dict.fromkeys(metadata["task_ids"])),
                    "source_class": "IssuerIR",
                    "provider_name": "IssuerNewsroom",
                    "canonical_url": response.url,
                    "official_document_id": "issuer-newsroom:"
                    + stable_hash(response.url)[:24],
                    "published_at": published.isoformat(),
                    "available_at": published.isoformat(),
                    "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    "content_hash": evidence.content_hash,
                    "content_text": text,
                    "structured_payload": {},
                    "source_lineage_id": evidence.source_lineage_id,
                    "acquisition_class": "ACTUAL_LIVE_FULL_DOCUMENT",
                    "search_snippet_used_as_evidence": False,
                }
                documents.append(document)
                fetch_rows.append(
                    {
                        **base,
                        "document_id": evidence.document_id,
                        "published_at": published.isoformat(),
                        "content_hash": evidence.content_hash,
                        "extracted_char_count": len(text),
                        "acquisition_class": "FETCHED_FULL_DOCUMENT",
                        "score_created": False,
                    }
                )
            except (OSError, TypeError, ValueError) as exc:
                fetch_rows.append(
                    {
                        **base,
                        "document_id": None,
                        "published_at": None,
                        "content_hash": None,
                        "extracted_char_count": 0,
                        "acquisition_class": "SOURCE_REJECTED",
                        "blocker_code": str(exc),
                        "score_created": False,
                    }
                )
    return tuple(search_rows), tuple(fetch_rows), tuple(documents)


def _compile_report(
    *,
    config: Mapping[str, Any],
    universe: Sequence[Mapping[str, Any]],
    candidates: Sequence[Any],
    signals: Sequence[Any],
    lanes: Sequence[Any],
    decisions: Sequence[Any],
    planner_result: BrainPlannerRunResult,
    planning_rows: Sequence[Mapping[str, Any]],
    task_rows: Sequence[Mapping[str, Any]],
    search_rows: Sequence[Mapping[str, Any]],
    fetch_rows: Sequence[Mapping[str, Any]],
    documents: Sequence[Mapping[str, Any]],
    claim_result: CurrentClaimCompilationResult,
    search_errors: Sequence[str],
) -> Mapping[str, Any]:
    as_of = str(config["as_of_date"])
    mandatory = tuple(dict(item) for item in config["mandatory_targets"])
    sector_samples = select_sector_samples(
        as_of_date=as_of,
        universe=universe,
        candidate_pools=config["sector_candidate_pools"],
    )
    candidate_by_id = {item.target_id: item for item in candidates}
    signals_by_id = {item.trigger_signal_id: item for item in signals}
    decision_by_id = {item.target_id: item for item in decisions}
    lanes_by_id: dict[str, list[Any]] = {}
    for lane in lanes:
        lanes_by_id.setdefault(lane.target_id, []).append(lane)
    planner_by_id = {item.target_id: item for item in planner_result.planner_runs}
    satisfaction_by_target: dict[str, list[Any]] = {}
    for item in claim_result.source_task_satisfaction:
        satisfaction_by_target.setdefault(item.target_id, []).append(item)
    accepted_by_target: dict[str, list[Mapping[str, Any]]] = {}
    for item in claim_result.accepted_current_claims:
        accepted_by_target.setdefault(
            str(item.get("target_id") or item.get("target_entity_id") or ""), []
        ).append(item)
    provenance_by_target: dict[str, list[Any]] = {}
    for item in claim_result.daily_claim_provenance:
        provenance_by_target.setdefault(item.target_id, []).append(item)
    target_reports: list[Mapping[str, Any]] = []
    for target in mandatory:
        target_id = str(target["symbol"])
        candidate = candidate_by_id[target_id]
        target_signals = [signals_by_id[item] for item in candidate.trigger_signal_ids]
        target_tasks = [item for item in task_rows if item["target_id"] == target_id]
        target_planning = [item for item in planning_rows if item["target_id"] == target_id]
        target_docs = [item for item in documents if item["target_id"] == target_id]
        target_fetches = [item for item in fetch_rows if item["target_id"] == target_id]
        target_claims = accepted_by_target.get(target_id, [])
        target_provenance = provenance_by_target.get(target_id, [])
        target_satisfaction = satisfaction_by_target.get(target_id, [])
        provider_pending = any(item["status"] == "PENDING" for item in target_planning)
        source_pending = not target_docs or any(
            item.original_gap_open for item in target_satisfaction
        )
        atomic = _pending_atomic_decision(
            as_of_date=as_of,
            target_id=target_id,
            satisfaction=target_satisfaction,
            provider_pending=provider_pending,
            source_pending=source_pending,
        )
        daily_plan = planner_by_id[target_id]
        diagnostics = _diagnostic_slots(
            slots=tuple(config["full_thesis_diagnostic_slots"]),
            documents=target_docs,
            satisfaction=target_satisfaction,
        )
        target_reports.append(
            {
                "symbol": target_id,
                "company_name": target["company_name"],
                "daily_event_status": {
                    "status": "PARTIAL_OFFICIAL_EVENT_NOT_FULL_THESIS",
                    "candidate_event_id": candidate.candidate_event_id,
                    "official_events": [
                        {
                            "trigger_signal_id": item.trigger_signal_id,
                            "report_name": (item.payload or {}).get("report_name"),
                            "source_refs": list(item.source_refs),
                            "score_evidence_eligible": item.score_evidence_eligible,
                        }
                        for item in target_signals
                    ],
                    "planner_run_id": daily_plan.planner_run_id,
                    "planner_terminal_status": daily_plan.terminal_status,
                    "provider_name": daily_plan.provider_name,
                    "provider_real": daily_plan.provider_real,
                    "provider_call_count": daily_plan.provider_call_count,
                    "real_provider_success": daily_plan.real_provider_success,
                    "abstention_reason": (
                        daily_plan.plan.critique_output.abstention_reason
                        if daily_plan.plan.critique_output
                        and daily_plan.plan.critique_output.abstain
                        else None
                    ),
                    "called_hbm_full_thesis": False,
                },
                "full_thesis_status": _full_thesis_status(
                    provider_pending=provider_pending,
                    documents=target_docs,
                    satisfaction=target_satisfaction,
                ),
                "diagnostic_slots": diagnostics,
                "accepted_current_claims": [
                    {
                        "claim_id": item.get("claim_id"),
                        "document_id": item.get("document_id"),
                        "polarity": item.get("polarity"),
                        "temporal_status": item.get("temporal_status"),
                        "exact_quote": (item.get("raw_assertion") or {}).get("exact_quote"),
                        "mapping_ids": item.get("mapping_ids"),
                    }
                    for item in target_claims
                ],
                "claim_provenance": [
                    {
                        "provenance_id": item.provenance_id,
                        "claim_id": item.claim_id,
                        "document_id": item.document_id,
                        "source_url": item.source_url,
                        "published_date": item.published_date,
                        "content_sha256": item.content_sha256,
                        "anchor_ids": list(item.anchor_ids),
                        "mapping_ids": list(item.mapping_ids),
                    }
                    for item in target_provenance
                ],
                "source_tasks": [
                    {
                        "task_id": item["task_id"],
                        "recipe_id": item["recipe_id"],
                        "primitive_id": item["primitive_id"],
                        "question_to_answer": item["question_to_answer"],
                        "literal_queries": item["query_intent"]["literal_queries"],
                        "query_generator_kind": item["query_intent"]["generator_kind"],
                        "production_execution_allowed": item[
                            "production_execution_allowed"
                        ],
                    }
                    for item in target_tasks
                ],
                "source_task_satisfaction": [item.to_dict() for item in target_satisfaction],
                "fetched_documents": [
                    {
                        "document_id": item["document_id"],
                        "canonical_url": item["canonical_url"],
                        "published_at": item["published_at"],
                        "content_hash": item["content_hash"],
                        "source_task_ids": item["source_task_ids"],
                        "actual_live_full_document": True,
                    }
                    for item in target_docs
                ],
                "provider_source_gaps": {
                    "query_pending": [
                        item for item in target_planning if item["status"] != "COMPLETE"
                    ],
                    "fetch_rejections": [
                        item for item in target_fetches if item.get("document_id") is None
                    ],
                    "open_primitives": [
                        item.primitive_id
                        for item in target_satisfaction
                        if item.original_gap_open
                    ],
                },
                "score_type": atomic.score_type,
                "score_valid": atomic.score_valid,
                "score_value": atomic.score_value,
                "canonical_stage": atomic.canonical_stage,
                "stage_court_trace": atomic.stage_court_trace.to_dict(),
            }
        )

    sector_rows = []
    for sample in sector_samples:
        target_id = str(sample["symbol"])
        lane_rows = lanes_by_id.get(target_id, [])
        candidate = candidate_by_id.get(target_id)
        decision = decision_by_id.get(target_id)
        sector_rows.append(
            {
                **sample,
                "baseline_lane_status": {
                    item.lane: item.status for item in sorted(lane_rows, key=lambda row: row.lane)
                },
                "baseline_source_ids": sorted(
                    {source for item in lane_rows for source in item.source_ids}
                ),
                "candidate_event_id": candidate.candidate_event_id if candidate else None,
                "depth": decision.maximum_depth if decision else None,
                "selected_for_brain": decision.selected_for_brain if decision else False,
                "terminal_status": (
                    "CURRENT_TRIGGER_OBSERVED"
                    if candidate
                    else "LIVE_BASELINE_OBSERVED_NO_CURRENT_TRIGGER"
                ),
            }
        )

    hard = {
        "mandatory_target_missing_count": 2 - len(target_reports),
        "sector_sample_missing_count": 9 - len(sector_rows),
        "real_planner_trace_missing_count": sum(
            not item.real_provider_success for item in planner_result.planner_runs
        ),
        "llm_query_task_missing_count": sum(
            not any(row["target_id"] == str(item["symbol"]) for row in task_rows)
            for item in mandatory
        ),
        "actual_live_full_document_missing_count": sum(
            not any(row["target_id"] == str(item["symbol"]) for row in documents)
            for item in mandatory
        ),
        "claim_provenance_missing_count": sum(
            bool(accepted_by_target.get(str(target["symbol"]), ()))
            and not bool(provenance_by_target.get(str(target["symbol"]), ()))
            for target in mandatory
        ),
        "future_document_count": sum(
            str(item["published_at"]) > as_of for item in documents
        ),
        "snippet_used_as_evidence_count": sum(
            bool(item.get("search_snippet_used_as_evidence")) for item in documents
        ),
        "dart_partial_called_full_thesis_count": sum(
            item["daily_event_status"]["called_hbm_full_thesis"] for item in target_reports
        ),
        "accepted_claim_without_provenance_count": int(
            claim_result.audit["critical_counts"]["accepted_claim_without_provenance"]
        ),
        "non_deterministic_terminal_status_count": sum(
            not str(item["full_thesis_status"]["status"]) for item in target_reports
        ),
    }
    critical = sum(hard.values())
    return {
        "schema_version": TARGETED_SMOKE_SCHEMA_VERSION,
        "status": "TARGETED_LIVE_SMOKE_PASS" if critical == 0 else "TARGETED_LIVE_SMOKE_FAIL",
        "as_of_date": as_of,
        "executed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "live_input_root": "output/live_materialization/2026-07-10",
        "mandatory_targets": target_reports,
        "sector_samples": sector_rows,
        "aggregate": {
            "eligible_universe_count": len(universe),
            "mandatory_target_count": len(target_reports),
            "sector_sample_count": len(sector_rows),
            "daily_planner_run_count": len(planner_result.planner_runs),
            "daily_real_planner_call_count": sum(
                item.provider_call_count for item in planner_result.planner_runs
            ),
            "question_planning_count": len(planning_rows),
            "question_source_task_count": len(task_rows),
            "search_result_count": len(search_rows),
            "actual_live_full_document_count": len(documents),
            "accepted_current_claim_count": len(claim_result.accepted_current_claims),
            "claim_provenance_count": len(claim_result.daily_claim_provenance),
            "source_task_satisfaction_count": len(claim_result.source_task_satisfaction),
            "search_provider_errors": list(search_errors),
        },
        "safety": {
            "daily_event_and_full_thesis_separated": True,
            "literal_queries_generated_by_llm_only": all(
                item["query_intent"]["generator_kind"]
                in {"REAL_LLM", "TEST_FIXTURE_LLM"}
                for item in task_rows
            ),
            "official_domain_full_documents_only": all(
                item["source_class"] == "IssuerIR" for item in documents
            ),
            "search_snippets_score_eligible": False,
            "green_required": False,
            "investment_recommendation_emitted": False,
            "accepted_claim_provenance_contract_complete": (
                claim_result.audit["critical_counts"][
                    "accepted_claim_without_provenance"
                ]
                == 0
            ),
        },
        "hard_acceptance_counts": hard,
        "critical_count_sum": critical,
        "hard_acceptance_pass": critical == 0,
    }


def _pending_atomic_decision(
    *,
    as_of_date: str,
    target_id: str,
    satisfaction: Sequence[Any],
    provider_pending: bool,
    source_pending: bool,
) -> Any:
    primitives = tuple(dict.fromkeys(item.primitive_id for item in satisfaction))
    if not primitives:
        primitives = ("full_thesis_source_materialization",)
    points = [round(100.0 / len(primitives), 6)] * len(primitives)
    points[-1] = round(100.0 - sum(points[:-1]), 6)
    return decide_atomic_score_stage(
        AtomicScoringInput(
            target_id=target_id,
            as_of_date=as_of_date,
            scope=AtomicScoringScope.FULL_THESIS.value,
            claims=(),
            primitive_assessments=tuple(
                AtomicPrimitiveAssessment(
                    primitive_id=primitive,
                    status=AtomicPrimitiveStatus.MISSING.value,
                    evidence_strength=0.0,
                )
                for primitive in primitives
            ),
            rules=tuple(
                AtomicScoreRule(
                    primitive_id=primitive,
                    component_key=f"targeted_smoke:{primitive}",
                    max_points=point,
                    material=True,
                    green_required=True,
                )
                for primitive, point in zip(primitives, points)
            ),
            provider_pending=provider_pending,
            source_pending=source_pending,
        )
    )


def _full_thesis_status(
    *,
    provider_pending: bool,
    documents: Sequence[Mapping[str, Any]],
    satisfaction: Sequence[Any],
) -> Mapping[str, Any]:
    if provider_pending:
        status = "PROVIDER_PENDING"
    elif not documents:
        status = "SOURCE_PENDING"
    elif not satisfaction or any(item.original_gap_open for item in satisfaction):
        status = "FULL_THESIS_EVIDENCE_PENDING"
    else:
        status = "FULL_THESIS_SOURCE_RESOLVED"
    return {
        "status": status,
        "deterministic": True,
        "green_forced": False,
        "score_finalized": False,
        "reason": (
            "C06 전체 논리의 모든 material slot이 닫히기 전에는 Stage 0 NO_SCORE로 보류한다."
        ),
    }


def _diagnostic_slots(
    *,
    slots: Sequence[str],
    documents: Sequence[Mapping[str, Any]],
    satisfaction: Sequence[Any],
) -> Mapping[str, Mapping[str, Any]]:
    satisfied = {
        item.primitive_id: item
        for item in satisfaction
        if not item.original_gap_open
    }
    primitive_map = {
        "customer_allocation": ("customer_preorder_or_allocation",),
        "sold_out_or_pre_sold_capacity": (
            "hbm_capacity_constraint",
            "hbm_capacity_pre_sold",
        ),
        "revenue_mix": ("revenue_visibility_contract",),
        "margin_fcf_revision_bridge": ("medium_term_revision_visibility",),
    }
    text = "\n".join(str(item.get("content_text") or "") for item in documents).casefold()
    keyword_map = {
        "qualification": ("qualification", "qualified", "인증"),
        "shipment": ("shipment", "shipments", "출하"),
        "conventional_memory_drag": (
            "conventional dram",
            "legacy memory",
            "commodity memory",
            "범용 d램",
        ),
        "current_lifecycle": ("2026",),
    }
    result: dict[str, Mapping[str, Any]] = {}
    for slot in slots:
        primitives = primitive_map.get(slot, ())
        accepted = [item for item in primitives if item in satisfied]
        observed = [word for word in keyword_map.get(slot, ()) if word.casefold() in text]
        if accepted:
            status = "ACCEPTED_CURRENT_CLAIM"
        elif observed:
            status = "DOCUMENT_OBSERVED_CLAIM_NOT_ACCEPTED"
        else:
            status = "OPEN"
        result[slot] = {
            "status": status,
            "accepted_primitive_ids": accepted,
            "document_markers": observed,
            "score_eligible": bool(accepted),
        }
    return result


def _url_on_allowed_domain(url: str, domains: Sequence[str]) -> bool:
    host = (urlparse(url).hostname or "").casefold().rstrip(".")
    return any(host == item.casefold() or host.endswith("." + item.casefold()) for item in domains)


def _search_result_matches_llm_query(*, query: str, title: str) -> bool:
    stopwords = {
        "site",
        "news",
        "global",
        "samsung",
        "electronics",
        "hynix",
        "sk",
        "or",
        "and",
        "the",
        "published",
        "through",
        "before",
        "after",
        "원문",
        "공시",
        "실적발표",
    }
    terms = {
        token.casefold()
        for token in re.findall(r"[A-Za-z0-9가-힣]+", query)
        if len(token) >= 3
        and token.casefold() not in stopwords
        and re.fullmatch(r"20\d{2}", token) is None
    }
    if not terms:
        return False
    lowered_title = title.casefold()
    return any(term in lowered_title for term in terms)


def _target_marker_present(text: str, target: Mapping[str, Any]) -> bool:
    haystack = text.casefold()
    markers = (str(target["company_name"]), *tuple(str(item) for item in target["aliases"]))
    return any(marker.casefold() in haystack for marker in markers)


def _published_date_from_text(text: str, *, as_of: date) -> date | None:
    prefix = text[:5000]
    candidates: list[tuple[int, date]] = []
    for pattern in _DATE_PATTERNS:
        for match in pattern.finditer(prefix):
            try:
                candidates.append(
                    (match.start(), date(int(match[1]), int(match[2]), int(match[3])))
                )
            except ValueError:
                continue
    for match in _ENGLISH_DATE_RE.finditer(prefix):
        try:
            candidates.append(
                (
                    match.start(),
                    date(int(match[3]), _MONTHS[match[1].casefold()], int(match[2])),
                )
            )
        except ValueError:
            continue
    visible = [
        (position, item)
        for position, item in candidates
        if date(as_of.year - 2, 1, 1) <= item <= as_of
    ]
    return min(visible, key=lambda item: item[0])[1] if visible else None


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    with path.open(encoding="utf-8") as handle:
        rows = tuple(json.loads(line) for line in handle if line.strip())
    if any(not isinstance(item, Mapping) for item in rows):
        raise ValueError(f"JSONL contains non-object row: {path}")
    return rows


__all__ = [
    "TARGETED_SMOKE_CONFIG_SCHEMA_VERSION",
    "TARGETED_SMOKE_SCHEMA_VERSION",
    "TargetedSmokeRunResult",
    "audit_targeted_smoke_snapshot",
    "run_targeted_live_smoke",
    "resume_targeted_smoke_claims",
    "select_sector_samples",
    "write_targeted_live_smoke",
]
