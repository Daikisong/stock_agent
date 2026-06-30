"""SourceTask creation and bounded execution stubs for Census deep dossiers."""

from __future__ import annotations

from typing import Mapping, Sequence

from e2r.production.metadata import stable_hash

from .schemas import (
    DepthDecision,
    DepthLevel,
    SourceTask,
    SourceTaskExecution,
    SourceTaskStatus,
)
from .triage import ResearchBrainPlan


def build_source_tasks(
    *,
    plan: ResearchBrainPlan | None,
    depth_decision: DepthDecision,
) -> tuple[SourceTask, ...]:
    if plan is None:
        return ()
    if depth_decision.recommended_depth not in {
        DepthLevel.L3_RESEARCH_BRAIN_TRIAGE,
        DepthLevel.L4_DEEP_DOSSIER,
        DepthLevel.L5_VERIFIED_STAGE,
    }:
        return ()
    max_tasks = int(depth_decision.source_task_budget.get("max_tasks", 0))
    if max_tasks <= 0:
        return ()
    tasks: list[SourceTask] = []
    for draft in tuple(plan.source_task_drafts)[:max_tasks]:
        source_class = str(draft.get("source_class") or "official_structured_first")
        primitive_gap = str(draft.get("primitive_gap") or "unknown_gap")
        task_id = "CST-" + stable_hash({"symbol": plan.symbol, "gap": primitive_gap, "source": source_class})[:18]
        tasks.append(
            SourceTask(
                task_id=task_id,
                symbol=plan.symbol,
                depth_level=depth_decision.recommended_depth,
                task_class="official_light_task" if depth_decision.recommended_depth == DepthLevel.L3_RESEARCH_BRAIN_TRIAGE else "deep_dossier_task",
                source_class=source_class,
                budget={
                    "max_fetches": int(depth_decision.source_task_budget.get("max_fetches_per_task", 1)),
                    "max_retries": int(depth_decision.source_task_budget.get("max_retries", 1)),
                },
                stop_condition="stop_on_resolution",
                allows_general_web=False,
                reason=primitive_gap,
            )
        )
    return tuple(tasks)


def execute_source_tasks(
    tasks: Sequence[SourceTask],
    *,
    accepted_claims_by_task: Mapping[str, Sequence[str]] | None = None,
    provider_failures_by_task: Mapping[str, Sequence[str]] | None = None,
) -> tuple[SourceTaskExecution, ...]:
    accepted_claims_by_task = accepted_claims_by_task or {}
    provider_failures_by_task = provider_failures_by_task or {}
    executions: list[SourceTaskExecution] = []
    for task in tasks:
        errors = tuple(provider_failures_by_task.get(task.task_id, ()))
        accepted = tuple(accepted_claims_by_task.get(task.task_id, ()))
        if errors:
            status = SourceTaskStatus.PROVIDER_FAILED
            stop_reason = "provider_failed"
        elif accepted:
            status = SourceTaskStatus.EVIDENCE_OS_ACCEPTED
            stop_reason = "resolved_by_accepted_claim"
        else:
            status = SourceTaskStatus.NO_EVIDENCE_FOUND
            stop_reason = "stop_on_resolution_no_evidence"
        executions.append(
            SourceTaskExecution(
                task_id=task.task_id,
                symbol=task.symbol,
                depth_level=task.depth_level,
                source_class=task.source_class,
                status=status,
                accepted_claim_ids=accepted,
                provider_errors=errors,
                budget_used={"fetches": min(int(task.budget.get("max_fetches", 0)), 1), "retries": 0},
                stop_reason=stop_reason,
            )
        )
    return tuple(executions)


def source_task_without_budget_count(tasks: Sequence[SourceTask | Mapping[str, object]]) -> int:
    count = 0
    for task in tasks:
        budget = task.budget if isinstance(task, SourceTask) else task.get("budget")
        if not budget or any(value is None for value in dict(budget).values()):
            count += 1
    return count


__all__ = ["build_source_tasks", "execute_source_tasks", "source_task_without_budget_count"]
