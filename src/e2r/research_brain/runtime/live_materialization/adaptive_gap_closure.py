"""Append-only current ledger and LLM-driven adaptive gap closure."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl
from e2r.research_brain.intelligence_schema import CurrentEvidenceFact, PlannerSourceTaskDraft
from e2r.research_brain.planning import (
    QuestionQueryProvider,
    QuestionTaskPlanningStatus,
    build_codex_question_query_provider,
    compile_question_task_context,
    plan_question_source_task,
)
from e2r.research_brain.research_quality import (
    canonical_research_failure_class,
    compile_research_repair_directive,
)

from .source_task_materializer import RecordingQuestionQueryProvider, load_evidence_recipes


@dataclass(frozen=True)
class AdaptiveGapClosureConfig:
    as_of_date: str
    max_gap_attempts: int
    max_generation_attempts: int = 3
    test_mode: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if not 1 <= self.max_gap_attempts <= 100:
            raise ValueError("adaptive gap attempt budget must be bounded by 100")
        if not 1 <= self.max_generation_attempts <= 3:
            raise ValueError("adaptive query generation must be bounded by three")


@dataclass(frozen=True)
class AppendOnlyLedgerEntry:
    sequence: int
    entry_id: str
    entry_type: str
    target_id: str
    source_task_id: str | None
    claim_id: str | None
    status: str
    reason_code: str
    reason_detail: str
    previous_entry_hash: str
    entry_hash: str
    invalidation_reason: str | None = None
    supersedes_claim_ids: tuple[str, ...] = ()

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AdaptiveGapAttempt:
    attempt_id: str
    source_task_id: str
    target_id: str
    failure_reason_code: str
    next_action: str
    previous_queries: tuple[str, ...]
    suggested_queries: tuple[str, ...]
    planning_status: str
    terminal_status: str
    provider_name: str
    prompt_hash: str
    response_hash: str
    identical_query: bool
    repair_directive_id: str = ""
    score_gap_context: Mapping[str, Any] | None = None
    preserved_evidence_ids: tuple[str, ...] = ()
    query_generation_owner: str = "LLM"
    deterministic_fallback_query_used: bool = False
    score_valid: bool = False
    canonical_stage: str = "0"

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AdaptiveGapClosureResult:
    as_of_date: str
    status: str
    ledger_entries: tuple[AppendOnlyLedgerEntry, ...]
    attempts: tuple[AdaptiveGapAttempt, ...]
    prompt_rows: tuple[Mapping[str, Any], ...]
    response_rows: tuple[Mapping[str, Any], ...]
    gap_status_rows: tuple[Mapping[str, Any], ...]
    audit: Mapping[str, Any]


class CurrentAdaptiveGapClosure:
    def close(
        self,
        config: AdaptiveGapClosureConfig,
        *,
        question_source_tasks: Sequence[Mapping[str, Any]],
        source_task_satisfaction: Sequence[Mapping[str, Any]],
        adjudicated_claims: Sequence[Mapping[str, Any]],
        evidence_documents: Sequence[Mapping[str, Any]],
        recipe_path: str | Path,
        provider: QuestionQueryProvider | None = None,
    ) -> AdaptiveGapClosureResult:
        satisfaction_by_task = _unique_mapping(
            source_task_satisfaction, key="source_task_id", context="satisfaction"
        )
        tasks_by_id = _unique_mapping(
            question_source_tasks, key="task_id", context="question tasks"
        )
        if set(tasks_by_id) != set(satisfaction_by_task):
            raise ValueError("gap closure task and satisfaction identities differ")
        if len(tasks_by_id) > config.max_gap_attempts:
            raise ValueError("open material gap count exceeds bounded attempt budget")
        recipes = {item.recipe_id: item for item in load_evidence_recipes(recipe_path)}
        effective_provider = provider
        if effective_provider is None and not config.test_mode:
            effective_provider = build_codex_question_query_provider()
        if effective_provider is None:
            raise ValueError("adaptive gap query provider is not configured")
        documents_by_id = {
            str(item.get("document_id") or ""): item for item in evidence_documents
        }
        claims_by_target: dict[str, list[Mapping[str, Any]]] = {}
        for claim in adjudicated_claims:
            claims_by_target.setdefault(str(claim.get("target_id") or ""), []).append(claim)

        ledger_payloads: list[Mapping[str, Any]] = []
        for claim in adjudicated_claims:
            ledger_payloads.append(
                {
                    "entry_type": "CLAIM_ADJUDICATED",
                    "target_id": str(claim.get("target_id") or ""),
                    "source_task_id": None,
                    "claim_id": str(claim.get("claim_id") or ""),
                    "status": str(claim.get("investigation_status") or "UNKNOWN"),
                    "reason_code": "ADJUDICATED_NOT_ACCEPTED",
                    "reason_detail": "claim preserved without accepted primitive mapping",
                }
            )
        attempts: list[AdaptiveGapAttempt] = []
        prompts: list[Mapping[str, Any]] = []
        responses: list[Mapping[str, Any]] = []
        gap_rows: list[Mapping[str, Any]] = []
        for task_id, task in tasks_by_id.items():
            satisfaction = satisfaction_by_task[task_id]
            if satisfaction.get("original_gap_open") is not True:
                continue
            failure_code = _failure_code(str(satisfaction.get("status") or ""))
            preserved_evidence_ids = tuple(
                dict.fromkeys(
                    str(value)
                    for name in (
                        "rerouted_claim_ids",
                        "rerouted_mapping_ids",
                        "counter_claim_ids",
                        "preserved_evidence_ids",
                    )
                    for value in satisfaction.get(name) or ()
                    if str(value)
                )
            )
            directive = compile_research_repair_directive(
                failure_class=failure_code,
                question_family_id=str(
                    task.get("question_family_id")
                    or task.get("primitive_id")
                    or "UNKNOWN_QUESTION"
                ),
                original_question=str(task.get("question_to_answer") or ""),
                failure_reason=str(satisfaction.get("reason") or failure_code),
                missing_route_categories=tuple(
                    satisfaction.get("missing_route_categories") or ()
                ),
                rejected_document_reasons=tuple(
                    satisfaction.get("rejected_document_reasons") or ()
                ),
                preserved_evidence_ids=preserved_evidence_ids,
                validation_feedback=tuple(
                    (task.get("query_intent") or {}).get(
                        "validation_feedback", ()
                    )
                ),
            )
            failure_code = directive.failure_class
            next_action = directive.next_action
            recipe = recipes.get(str(task.get("recipe_id") or ""))
            if recipe is None:
                raise ValueError("adaptive gap task references unknown recipe")
            query_intent = task.get("query_intent") or {}
            previous_queries = tuple(query_intent.get("literal_queries") or ())
            facts = _current_gap_facts(
                task=task,
                claims=claims_by_target.get(str(task.get("target_id") or ""), ()),
                documents_by_id=documents_by_id,
                as_of_date=config.as_of_date,
                failure_code=failure_code,
            )
            context = compile_question_task_context(
                target_id=str(task.get("target_id") or ""),
                target_name=str(task.get("company_name") or ""),
                symbol=str(task.get("symbol") or task.get("target_id") or ""),
                target_aliases=(str(task.get("target_id") or ""),),
                as_of_date=config.as_of_date,
                current_facts=facts,
                missing_information=(
                    (
                        f"failure={failure_code}; reason="
                        f"{directive.score_gap_context['failure_reason']}; "
                        f"next action={next_action}; missing routes="
                        f"{','.join(directive.score_gap_context['missing_route_categories']) or 'none'}; "
                        "propose a new target-specific query without repeating an executed query"
                    ),
                ),
                existing_queries=previous_queries,
            )
            route = task.get("source_route") or {}
            budget = task.get("budget") or {}
            stop = task.get("stop_condition") or {}
            draft = PlannerSourceTaskDraft(
                draft_id=f"adaptive:{task_id}",
                recipe_id=recipe.recipe_id,
                question_to_answer=str(task.get("question_to_answer") or ""),
                why_material=str(task.get("why_material") or ""),
                query_intent=str(query_intent.get("semantic_intent") or ""),
                preferred_source_families=tuple(route.get("preferred_source_families") or ()),
                fallback_source_families=tuple(route.get("fallback_source_families") or ()),
                max_queries=int(budget.get("max_queries") or 0),
                max_candidates=int(budget.get("max_candidates") or 0),
                max_fetches=int(budget.get("max_fetches") or 0),
                stop_condition=str((stop.get("resolution_conditions") or ["resolve current gap"])[0]),
            )
            local_prompts: list[Mapping[str, Any]] = []
            local_responses: list[Mapping[str, Any]] = []
            recording = RecordingQuestionQueryProvider(
                base=effective_provider,
                target_id=str(task.get("target_id") or ""),
                draft_id=draft.draft_id,
                prompt_rows=local_prompts,
                response_rows=local_responses,
            )
            result = plan_question_source_task(
                draft=draft,
                recipe=recipe,
                context=context,
                candidate_event_id=str(task.get("candidate_event_id") or ""),
                task_type=str(task.get("task_type") or "evidence_confirmation"),
                provider=recording,
                test_mode=config.test_mode,
                max_generation_attempts=config.max_generation_attempts,
            )
            prompts.extend(local_prompts)
            responses.extend(local_responses)
            suggested = (
                tuple(result.task.query_intent.literal_queries)
                if result.task is not None
                else ()
            )
            identical = bool(
                {_normalize(item) for item in previous_queries}
                & {_normalize(item) for item in suggested}
            )
            trace = result.trace
            pending_detail = result.pending
            terminal = directive.terminal_status_if_unresolved
            if pending_detail is not None and pending_detail.reason_code in {
                "QUERY_PROVIDER_NOT_CONFIGURED",
                "INVALID_QUERY_PROVIDER_IDENTITY",
                "FAKE_QUERY_PROVIDER_NOT_ALLOWED",
                "QUERY_PROVIDER_UNAVAILABLE",
                "QUERY_PROVIDER_REJECTED",
                "QUERY_PROVIDER_OR_OUTPUT_ERROR",
            }:
                terminal = "PROVIDER_PENDING"
            attempt = AdaptiveGapAttempt(
                attempt_id="GAPATTEMPT-" + stable_hash(
                    {"task_id": task_id, "input_id": result.input_id}
                )[:24],
                source_task_id=task_id,
                target_id=str(task.get("target_id") or ""),
                failure_reason_code=failure_code,
                next_action=next_action,
                previous_queries=previous_queries,
                suggested_queries=suggested,
                planning_status=result.status,
                terminal_status=terminal,
                provider_name=(
                    trace.provider_name
                    if trace is not None
                    else pending_detail.provider_name
                    if pending_detail is not None
                    else effective_provider.provider_name
                ),
                prompt_hash=(
                    trace.prompt_hash
                    if trace is not None
                    else pending_detail.prompt_hash
                    if pending_detail is not None
                    else "0" * 64
                ),
                response_hash=(
                    trace.response_hash
                    if trace is not None
                    else pending_detail.response_hash
                    if pending_detail is not None
                    else "0" * 64
                ),
                identical_query=identical,
                repair_directive_id=directive.directive_id,
                score_gap_context=directive.score_gap_context,
                preserved_evidence_ids=preserved_evidence_ids,
                query_generation_owner=directive.query_generation_owner,
                deterministic_fallback_query_used=False,
            )
            attempts.append(attempt)
            gap_rows.append(
                {
                    "source_task_id": task_id,
                    "target_id": attempt.target_id,
                    "terminal_status": terminal,
                    "score_valid": False,
                    "raw_reference_score": None,
                    "canonical_stage": "0",
                    "material_gap_open": True,
                    "failure_reason_code": failure_code,
                    "next_action": next_action,
                    "repair_directive_id": directive.directive_id,
                    "preserved_evidence_ids": list(preserved_evidence_ids),
                    "original_gap_open": True,
                }
            )
            ledger_payloads.extend(
                (
                    {
                        "entry_type": "MATERIAL_GAP_OPEN",
                        "target_id": attempt.target_id,
                        "source_task_id": task_id,
                        "claim_id": None,
                        "status": terminal,
                        "reason_code": failure_code,
                        "reason_detail": str(satisfaction.get("reason") or ""),
                    },
                    {
                        "entry_type": "ADAPTIVE_RETRY_PLANNED",
                        "target_id": attempt.target_id,
                        "source_task_id": task_id,
                        "claim_id": None,
                        "status": result.status,
                        "reason_code": next_action,
                        "reason_detail": " | ".join(suggested) or "LLM query generation pending",
                    },
                )
            )
        ledger = _append_only_entries(ledger_payloads)
        audit = _audit_adaptive_gap(
            as_of_date=config.as_of_date,
            ledger=ledger,
            attempts=attempts,
            gaps=gap_rows,
        )
        return AdaptiveGapClosureResult(
            as_of_date=config.as_of_date,
            status="ADAPTIVE_GAP_CLOSURE_PASS" if audit["hard_acceptance_pass"] else "ADAPTIVE_GAP_CLOSURE_FAIL",
            ledger_entries=ledger,
            attempts=tuple(attempts),
            prompt_rows=tuple(prompts),
            response_rows=tuple(responses),
            gap_status_rows=tuple(gap_rows),
            audit=audit,
        )


def write_adaptive_gap_closure(
    result: AdaptiveGapClosureResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "ledger": root / "current_claim_ledger.jsonl",
        "attempts": root / "adaptive_gap_attempts.jsonl",
        "prompts": root / "adaptive_gap_prompts.jsonl",
        "responses": root / "adaptive_gap_responses.jsonl",
        "statuses": root / "gap_closure_status.jsonl",
        "audit": root / "adaptive_gap_audit.json",
    }
    write_jsonl(paths["ledger"], (item.to_dict() for item in result.ledger_entries))
    write_jsonl(paths["attempts"], (item.to_dict() for item in result.attempts))
    write_jsonl(paths["prompts"], result.prompt_rows)
    write_jsonl(paths["responses"], result.response_rows)
    write_jsonl(paths["statuses"], result.gap_status_rows)
    write_json(paths["audit"], {**dict(result.audit), "status": result.status})
    return paths


def _current_gap_facts(
    *,
    task: Mapping[str, Any],
    claims: Sequence[Mapping[str, Any]],
    documents_by_id: Mapping[str, Mapping[str, Any]],
    as_of_date: str,
    failure_code: str,
) -> tuple[CurrentEvidenceFact, ...]:
    facts: list[CurrentEvidenceFact] = []
    for claim in claims[:3]:
        document = documents_by_id.get(str(claim.get("document_id") or ""))
        raw_text = str((claim.get("raw_assertion") or {}).get("exact_quote") or "")
        if not raw_text or document is None:
            continue
        facts.append(
            CurrentEvidenceFact(
                fact_id="GAPFACT-" + str(claim.get("claim_id") or stable_hash(claim))[:24],
                text=raw_text,
                observed_date=str(document.get("published_at") or as_of_date),
                target_relation="DIRECT",
                current_status="CURRENT",
            )
        )
    if not facts:
        facts.append(
            CurrentEvidenceFact(
                fact_id="GAPFACT-" + stable_hash(
                    {"task_id": task.get("task_id"), "failure": failure_code}
                )[:24],
                text=(
                    f"{task.get('company_name')}의 공식 조사 경로는 {as_of_date} 기준 "
                    f"{failure_code} 상태이며 질문을 닫을 source-backed claim이 없다."
                ),
                observed_date=as_of_date,
                target_relation="DIRECT",
                current_status="UNKNOWN",
            )
        )
    return tuple(facts)


def _append_only_entries(payloads: Sequence[Mapping[str, Any]]) -> tuple[AppendOnlyLedgerEntry, ...]:
    entries: list[AppendOnlyLedgerEntry] = []
    previous = "0" * 64
    for sequence, payload in enumerate(payloads, 1):
        body = {"sequence": sequence, **dict(payload), "previous_entry_hash": previous}
        digest = hashlib.sha256(
            json.dumps(body, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        entry = AppendOnlyLedgerEntry(
            sequence=sequence,
            entry_id="LEDGER-" + digest[:24],
            entry_type=str(payload["entry_type"]),
            target_id=str(payload["target_id"]),
            source_task_id=payload.get("source_task_id"),
            claim_id=payload.get("claim_id"),
            status=str(payload["status"]),
            reason_code=str(payload["reason_code"]),
            reason_detail=str(payload["reason_detail"]),
            previous_entry_hash=previous,
            entry_hash=digest,
        )
        entries.append(entry)
        previous = digest
    return tuple(entries)


def _audit_adaptive_gap(
    *,
    as_of_date: str,
    ledger: Sequence[AppendOnlyLedgerEntry],
    attempts: Sequence[AdaptiveGapAttempt],
    gaps: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    critical = {
        "silent_claim_overwrite": 0,
        "identical_retry": sum(item.identical_query for item in attempts),
        "deterministic_fallback_query_count": sum(
            item.deterministic_fallback_query_used for item in attempts
        ),
        "repair_without_llm_query_owner_count": sum(
            item.query_generation_owner != "LLM" for item in attempts
        ),
        "retry_without_failure_reason": sum(not item.failure_reason_code for item in attempts),
        "unresolved_material_gap_final_score": sum(
            item.get("material_gap_open") is True and item.get("score_valid") is True for item in gaps
        ),
        "provider_failure_low_score": sum(
            item.get("failure_reason_code") == "PROVIDER_FAILED"
            and item.get("raw_reference_score") is not None for item in gaps
        ),
        "round_limit_score_valid_true": 0,
    }
    terminal_counts: dict[str, int] = {}
    for item in gaps:
        status = str(item.get("terminal_status") or "")
        terminal_counts[status] = terminal_counts.get(status, 0) + 1
    return {
        "schema_version": "e2r_live_adaptive_gap_audit_v1",
        "as_of_date": as_of_date,
        "ledger_entry_count": len(ledger),
        "adaptive_attempt_count": len(attempts),
        "new_llm_query_count": sum(len(item.suggested_queries) for item in attempts),
        "planning_complete_count": sum(item.planning_status == "COMPLETE" for item in attempts),
        "terminal_status_counts": dict(sorted(terminal_counts.items())),
        "score_valid_true_count": sum(item.get("score_valid") is True for item in gaps),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "hard_acceptance_pass": sum(critical.values()) == 0,
        "production_runtime_ready": False,
    }


def _failure_code(status: str) -> str:
    return canonical_research_failure_class(status)


def _next_action(failure_code: str) -> str:
    return compile_research_repair_directive(
        failure_class=failure_code,
        question_family_id="COMPATIBILITY_QUESTION",
        original_question="Resolve the current material evidence gap.",
        failure_reason=failure_code,
    ).next_action


def _normalize(value: str) -> str:
    return " ".join(str(value).casefold().split())


def _unique_mapping(rows: Sequence[Mapping[str, Any]], *, key: str, context: str):
    result: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        identity = str(row.get(key) or "")
        if not identity or identity in result:
            raise ValueError(f"duplicate or empty identity in {context}")
        result[identity] = row
    return result


__all__ = [
    "AdaptiveGapAttempt",
    "AdaptiveGapClosureConfig",
    "AdaptiveGapClosureResult",
    "AppendOnlyLedgerEntry",
    "CurrentAdaptiveGapClosure",
    "write_adaptive_gap_closure",
]
