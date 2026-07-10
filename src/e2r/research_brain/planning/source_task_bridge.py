"""Migration and router bridges for canonical QuestionSourceTask."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Mapping

from e2r.research_brain.intelligence_schema import PlannerSourceTaskDraft
from e2r.research_brain.planning.source_task import QuestionSourceTask
from e2r.research_brain.schemas import SourceTask


class LegacySourceTaskAdapterStatus(str, Enum):
    READY_FOR_QUERY_GENERATION = "READY_FOR_QUERY_GENERATION"
    INVALID_LEGACY_TASK = "INVALID_LEGACY_TASK"


@dataclass(frozen=True)
class InvalidLegacySourceTask:
    legacy_task_id: str
    status: str
    reason_codes: tuple[str, ...]
    legacy_payload_hash: str
    production_execution_allowed: bool = False

    def __post_init__(self) -> None:
        if self.status != LegacySourceTaskAdapterStatus.INVALID_LEGACY_TASK.value:
            raise ValueError("invalid legacy task requires INVALID_LEGACY_TASK status")
        if not self.legacy_task_id.strip() or not self.reason_codes:
            raise ValueError("invalid legacy task requires identity and exact reasons")
        if self.production_execution_allowed:
            raise ValueError("invalid legacy task cannot execute in production")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class LegacySourceTaskAdapterResult:
    legacy_task_id: str
    status: str
    draft: PlannerSourceTaskDraft | None
    invalid: InvalidLegacySourceTask | None

    def __post_init__(self) -> None:
        LegacySourceTaskAdapterStatus(self.status)
        if self.status == LegacySourceTaskAdapterStatus.READY_FOR_QUERY_GENERATION.value:
            if self.draft is None or self.invalid is not None:
                raise ValueError("ready legacy adaptation requires only a draft")
        elif self.invalid is None or self.draft is not None:
            raise ValueError("invalid legacy adaptation requires only invalid detail")

    def to_dict(self) -> dict[str, Any]:
        return {
            "legacy_task_id": self.legacy_task_id,
            "status": self.status,
            "draft": self.draft.to_dict() if self.draft else None,
            "invalid": self.invalid.to_dict() if self.invalid else None,
        }


def adapt_legacy_source_task(
    task: SourceTask,
    *,
    recipe_id: str | None = None,
    question_to_answer: str | None = None,
    why_material: str | None = None,
    llm_query_intent: str | None = None,
) -> LegacySourceTaskAdapterResult:
    required = {
        "MISSING_RECIPE_ID": recipe_id,
        "MISSING_QUESTION_TO_ANSWER": question_to_answer,
        "MISSING_WHY_MATERIAL": why_material,
        "MISSING_LLM_QUERY_INTENT": llm_query_intent,
    }
    reasons = tuple(code for code, value in required.items() if not str(value or "").strip())
    if reasons:
        payload_hash = hashlib.sha256(
            _stable_json(task.to_dict()).encode("utf-8")
        ).hexdigest()
        invalid = InvalidLegacySourceTask(
            legacy_task_id=task.task_id,
            status=LegacySourceTaskAdapterStatus.INVALID_LEGACY_TASK.value,
            reason_codes=reasons,
            legacy_payload_hash=payload_hash,
        )
        return LegacySourceTaskAdapterResult(
            legacy_task_id=task.task_id,
            status=LegacySourceTaskAdapterStatus.INVALID_LEGACY_TASK.value,
            draft=None,
            invalid=invalid,
        )

    stop_condition = _stable_json(dict(task.stop_condition))
    draft = PlannerSourceTaskDraft(
        draft_id=f"legacy-draft:{task.task_id}",
        recipe_id=str(recipe_id).strip(),
        question_to_answer=str(question_to_answer).strip(),
        why_material=str(why_material).strip(),
        query_intent=str(llm_query_intent).strip(),
        preferred_source_families=tuple(task.preferred_source_classes),
        fallback_source_families=tuple(task.fallback_source_classes),
        max_queries=task.max_queries,
        max_candidates=task.max_candidates,
        max_fetches=task.max_fetches,
        stop_condition=stop_condition,
    )
    return LegacySourceTaskAdapterResult(
        legacy_task_id=task.task_id,
        status=LegacySourceTaskAdapterStatus.READY_FOR_QUERY_GENERATION.value,
        draft=draft,
        invalid=None,
    )


def question_source_task_to_router_payload(
    task: QuestionSourceTask,
    *,
    production_mode: bool = True,
) -> Mapping[str, Any]:
    if production_mode and not task.production_execution_allowed:
        raise ValueError(
            "QuestionSourceTask is test-only or lacks a real LLM query provider"
        )
    payload = task.to_dict()
    return {
        **payload,
        "preferred_source_classes": list(
            task.source_route.preferred_source_families
        ),
        "fallback_source_classes": list(
            task.source_route.fallback_source_families
        ),
        "forbidden_source_classes": list(
            task.source_route.forbidden_source_families
        ),
        "preferred_document_types": list(
            task.source_route.preferred_document_types
        ),
        "preferred_sections": list(task.source_route.preferred_sections),
        "query_intents": list(task.query_intent.literal_queries),
        "max_queries": task.budget.max_queries,
        "max_candidates": task.budget.max_candidates,
        "max_fetches": task.budget.max_fetches,
        "official_first": True,
        "dedupe_before_fetch": True,
        "stop_on_resolution": True,
        "canonical_question_task": True,
    }


def _stable_json(value: Mapping[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


__all__ = [
    "InvalidLegacySourceTask",
    "LegacySourceTaskAdapterResult",
    "LegacySourceTaskAdapterStatus",
    "adapt_legacy_source_task",
    "question_source_task_to_router_payload",
]
