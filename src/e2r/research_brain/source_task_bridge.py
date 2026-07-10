"""Legacy SourceTask audit bridge.

Canonical production routing uses planning.source_task_bridge and
QuestionSourceTask.  This module keeps the legacy reader/auditor only.
"""

from __future__ import annotations

from typing import Mapping

from e2r.research_brain.schemas import SourceTask


def source_task_to_router_payload(
    task: SourceTask,
    *,
    allow_legacy_diagnostic: bool = False,
) -> Mapping[str, object]:
    if not allow_legacy_diagnostic:
        raise ValueError(
            "legacy SourceTask is INVALID_LEGACY_TASK for canonical production routing"
        )
    payload = task.to_dict()
    if payload.get("max_fetches") is None or payload.get("max_queries") is None:
        raise ValueError("Research Brain SourceTask must be bounded before source routing")
    return {
        **payload,
        "official_first": True,
        "dedupe_before_fetch": True,
        "stop_on_resolution": True,
        "canonical_execution_allowed": False,
        "legacy_diagnostic_only": True,
    }


def audit_source_tasks(tasks: tuple[SourceTask, ...]) -> Mapping[str, int | float]:
    total = len(tasks)
    official = sum(1 for task in tasks if any(item in {"DART", "KIND", "KRX", "CompanyGuide", "IR", "Official"} for item in task.preferred_source_classes))
    general = sum(1 for task in tasks if task.general_search_allowed)
    unbounded = sum(
        1
        for task in tasks
        if task.max_queries is None or task.max_candidates is None or task.max_fetches is None
    )
    fcf_to_news = sum(
        1
        for task in tasks
        if ("fcf" in task.primitive_gap.lower() or "cash" in task.primitive_gap.lower())
        and task.general_search_allowed
    )
    dart_gap_to_web = sum(
        1
        for task in tasks
        if any(token in task.primitive_gap.lower() for token in ("contract", "cash", "fcf"))
        and task.general_search_allowed
    )
    return {
        "source_task_count": total,
        "official_source_task_count": official,
        "general_search_task_count": general,
        "official_task_ratio": round(official / total, 6) if total else 0.0,
        "general_search_task_ratio": round(general / total, 6) if total else 0.0,
        "unbounded_source_task_count": unbounded,
        "FCF_gap_sent_to_news_count": fcf_to_news,
        "DART_solvable_gap_sent_to_web_count": dart_gap_to_web,
        "IR_solvable_gap_sent_to_web_count": dart_gap_to_web,
        "stop_on_resolution_success_count": sum(bool(task.stop_condition) for task in tasks),
    }


__all__ = ["audit_source_tasks", "source_task_to_router_payload"]
