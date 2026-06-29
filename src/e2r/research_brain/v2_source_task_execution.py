"""SourceTask planning/execution audit for Research Brain v2."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Mapping, Sequence

from e2r.research_brain.schemas import SourceTask, SourceTaskType, deterministic_id
from e2r.research_brain.source_task_bridge import audit_source_tasks
from e2r.research_brain.v2_schemas import (
    ArchetypeMemoryCard,
    CandidateEventV2,
    SourceTaskExecution,
    SourceTaskExecutionStatus,
    deterministic_claim_id_v2,
)


def plan_source_tasks_v2(
    *,
    event: CandidateEventV2,
    card: ArchetypeMemoryCard,
    max_tasks: int = 3,
) -> tuple[SourceTask, ...]:
    tasks = []
    for primitive in card.required_primitives[:max_tasks]:
        preferred = card.source_route_by_primitive.get(primitive) or ("DART", "IR", "Official")
        preferred = _official_first_sources(preferred, primitive)
        payload = {
            "candidate_event_id": event.candidate_event_id,
            "archetype_id": card.archetype_id,
            "primitive": primitive,
            "source_family": event.source_family,
        }
        tasks.append(
            SourceTask(
                task_id=deterministic_id("RSTASKV2", payload),
                candidate_event_id=event.candidate_event_id,
                symbol=event.symbol,
                company_name=event.company_name,
                archetype_id=card.archetype_id,
                primitive_gap=primitive,
                task_type=SourceTaskType.POSITIVE_VERIFY.value,
                preferred_source_classes=preferred,
                fallback_source_classes=tuple(item for item in ("Official", "BrokerPDF", "TrustedNews") if item not in preferred)[:2],
                forbidden_source_classes=_forbidden_sources(primitive),
                date_window={"end": event.event_date, "lookback_days": 540},
                max_queries=3,
                max_candidates=20,
                max_fetches=5,
                stop_condition={"accepted_claim_count": 1, "counter_claim_check_done": True},
                llm_query_allowed=True,
                general_search_allowed=False,
                reason_from_memory=f"{card.archetype_id}:{primitive}",
                memory_record_ids=card.representative_url_backed_fixture_ids[:5],
            )
        )
    return tuple(tasks)


def execute_source_tasks_from_local_evidence(
    *,
    event: CandidateEventV2,
    tasks: Sequence[SourceTask],
) -> tuple[SourceTaskExecution, ...]:
    executions = []
    evidence_ids = event.initial_evidence_document_ids
    for task in tasks:
        if evidence_ids:
            accepted = tuple(
                deterministic_claim_id_v2(
                    {
                        "task_id": task.task_id,
                        "evidence_id": evidence_id,
                        "primitive_gap": task.primitive_gap,
                    }
                )
                for evidence_id in evidence_ids[:1]
            )
            executions.append(
                SourceTaskExecution(
                    task_id=task.task_id,
                    status=SourceTaskExecutionStatus.EVIDENCE_OS_ACCEPTED.value,
                    attempted_sources=tuple(task.preferred_source_classes[:2]),
                    fetched_document_ids=evidence_ids[:1],
                    parsed_anchor_count=len(evidence_ids[:1]),
                    accepted_claim_ids=accepted,
                    stop_reason="local_snapshot_evidence_os_handoff_accepted",
                    budget_used={"queries": 1, "candidates": 1, "fetches": 1},
                )
            )
        else:
            executions.append(
                SourceTaskExecution(
                    task_id=task.task_id,
                    status=SourceTaskExecutionStatus.NO_EVIDENCE_FOUND.value,
                    attempted_sources=tuple(task.preferred_source_classes[:2]),
                    fetched_document_ids=(),
                    parsed_anchor_count=0,
                    accepted_claim_ids=(),
                    stop_reason="no_initial_source_backed_evidence_document",
                    budget_used={"queries": 1, "candidates": 0, "fetches": 0},
                )
            )
    return tuple(executions)


def build_source_task_execution_audit(
    *,
    planned_tasks: Sequence[SourceTask],
    executions: Sequence[SourceTaskExecution],
    deterministic_stage_output_count: int,
) -> Mapping[str, object]:
    task_audit = audit_source_tasks(tuple(planned_tasks))
    execution_by_task = {execution.task_id: execution for execution in executions}
    status_counts = Counter(execution.status for execution in executions)
    accepted_claim_source_task_count = sum(bool(execution.accepted_claim_ids) for execution in executions)
    planned_but_not_executed = sum(1 for task in planned_tasks if task.task_id not in execution_by_task)
    source_task_to_score_contribution_count = 0
    accepted_claim_count = sum(len(execution.accepted_claim_ids) for execution in executions)
    audit_pass = (
        task_audit["unbounded_source_task_count"] == 0
        and planned_but_not_executed == 0
        and source_task_to_score_contribution_count == 0
        and task_audit["FCF_gap_sent_to_news_count"] == 0
        and task_audit["DART_solvable_gap_sent_to_web_count"] == 0
    )
    return {
        "schema_version": "research_brain_v2_source_task_execution_audit",
        "summary": {
            **task_audit,
            "planned_source_task_count": len(planned_tasks),
            "executed_source_task_count": len(executions),
            "fetched_source_task_count": sum(bool(execution.fetched_document_ids) for execution in executions),
            "parsed_source_task_count": sum(execution.parsed_anchor_count > 0 for execution in executions),
            "accepted_claim_source_task_count": accepted_claim_source_task_count,
            "accepted_claim_count": accepted_claim_count,
            "source_task_to_score_contribution_count": source_task_to_score_contribution_count,
            "planned_but_not_executed_task_count": planned_but_not_executed,
            "provider_failed_material_task_count": status_counts[SourceTaskExecutionStatus.PROVIDER_FAILED.value],
            "budget_exhausted_material_gap_count": status_counts[SourceTaskExecutionStatus.BUDGET_EXHAUSTED.value],
            "deterministic_stage_output_count": deterministic_stage_output_count,
            "source_task_execution_audit_pass": audit_pass,
        },
        "status_counts": dict(status_counts),
        "rows": [execution.to_dict() for execution in executions],
    }


def write_source_task_execution_audit(audit: Mapping[str, object], output_directory: str | Path) -> Path:
    path = Path(output_directory) / "research_brain_v2_source_task_execution_audit.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def _official_first_sources(preferred: Sequence[str], primitive: str) -> tuple[str, ...]:
    lower = primitive.lower()
    if "cash" in lower or "fcf" in lower:
        return ("DART", "CompanyGuide", "IR")
    if "contract" in lower or "backlog" in lower or "order" in lower:
        return ("DART", "KIND", "IR")
    values = [item for item in preferred if item not in {"GeneralWeb", "Web", "NewsOnly"}]
    for item in ("DART", "IR", "Official"):
        if item not in values:
            values.append(item)
    return tuple(values[:4])


def _forbidden_sources(primitive: str) -> tuple[str, ...]:
    values = ["unbounded_general_search"]
    lower = primitive.lower()
    if "cash" in lower or "fcf" in lower:
        values.append("NewsOnlyForFCF")
    if "contract" in lower or "backlog" in lower:
        values.append("GeneralWebBeforeOfficialDisclosure")
    return tuple(values)


__all__ = [
    "build_source_task_execution_audit",
    "execute_source_tasks_from_local_evidence",
    "plan_source_tasks_v2",
    "write_source_task_execution_audit",
]
