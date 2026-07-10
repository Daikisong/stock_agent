"""QuestionSourceTask satisfaction as a leaf separate from claim acceptance."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, replace
from datetime import date
from enum import Enum
from typing import Any, Sequence

from e2r.agentic.evidence_os import (
    Directness,
    MappingStatus,
    SupportDirection,
    TemporalStatus,
)
from e2r.research_brain.planning.source_task import QuestionSourceTask
from e2r.research_brain.runtime.claim_compiler import (
    ClaimLedgerEvent,
    ClaimLifecycleKind,
)


TASK_SATISFACTION_SCHEMA_VERSION = "e2r_question_task_satisfaction_v1"


class TaskSatisfactionStatus(str, Enum):
    DIRECT_TASK_SATISFIED = "DIRECT_TASK_SATISFIED"
    REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN = (
        "REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN"
    )
    BASELINE_CLAIM_REUSED = "BASELINE_CLAIM_REUSED"
    LIFECYCLE_REFRESH_ONLY = "LIFECYCLE_REFRESH_ONLY"
    COUNTER_CLAIM_FOUND = "COUNTER_CLAIM_FOUND"
    NO_RELEVANT_CLAIM = "NO_RELEVANT_CLAIM"
    WRONG_SUBJECT = "WRONG_SUBJECT"
    STALE_ONLY = "STALE_ONLY"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    SOURCE_EXHAUSTED = "SOURCE_EXHAUSTED"


@dataclass(frozen=True)
class TaskSatisfactionResult:
    satisfaction_id: str
    task_id: str
    recipe_id: str
    primitive_id: str
    status: str
    direct_claim_ids: tuple[str, ...]
    rerouted_claim_ids: tuple[str, ...]
    baseline_claim_ids: tuple[str, ...]
    lifecycle_refresh_claim_ids: tuple[str, ...]
    counter_claim_ids: tuple[str, ...]
    score_eligible_claim_ids: tuple[str, ...]
    original_gap_closed: bool
    material_gap_open: bool
    provider_failed: bool
    source_exhausted: bool
    reasons: tuple[str, ...]
    schema_version: str = TASK_SATISFACTION_SCHEMA_VERSION

    def __post_init__(self) -> None:
        status = TaskSatisfactionStatus(self.status)
        if not all(
            item.strip()
            for item in (
                self.satisfaction_id,
                self.task_id,
                self.recipe_id,
                self.primitive_id,
            )
        ):
            raise ValueError("task satisfaction identity is required")
        for values in (
            self.direct_claim_ids,
            self.rerouted_claim_ids,
            self.baseline_claim_ids,
            self.lifecycle_refresh_claim_ids,
            self.counter_claim_ids,
            self.score_eligible_claim_ids,
            self.reasons,
        ):
            if any(not str(item).strip() for item in values):
                raise ValueError("task satisfaction contains empty provenance")
            if len(values) != len(set(values)):
                raise ValueError("task satisfaction contains duplicate provenance")
        if self.original_gap_closed != (
            status
            in {
                TaskSatisfactionStatus.DIRECT_TASK_SATISFIED,
                TaskSatisfactionStatus.BASELINE_CLAIM_REUSED,
            }
        ):
            raise ValueError("task satisfaction original-gap closure is inconsistent")
        if self.material_gap_open == self.original_gap_closed:
            raise ValueError("task material gap must be the inverse of closure")
        if (
            status == TaskSatisfactionStatus.DIRECT_TASK_SATISFIED
            and not self.direct_claim_ids
        ):
            raise ValueError("direct task satisfaction requires direct claims")
        if (
            status
            == TaskSatisfactionStatus.REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN
            and not self.rerouted_claim_ids
        ):
            raise ValueError("rerouted task status requires rerouted claims")
        if (
            status == TaskSatisfactionStatus.BASELINE_CLAIM_REUSED
            and not self.baseline_claim_ids
        ):
            raise ValueError("baseline reuse requires baseline claim IDs")
        if (
            status == TaskSatisfactionStatus.LIFECYCLE_REFRESH_ONLY
            and not self.lifecycle_refresh_claim_ids
        ):
            raise ValueError("lifecycle refresh requires refresh claim IDs")
        if (
            status == TaskSatisfactionStatus.COUNTER_CLAIM_FOUND
            and not self.counter_claim_ids
        ):
            raise ValueError("counter status requires counter claim IDs")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def evaluate_task_satisfaction(
    *,
    task: QuestionSourceTask,
    events: Sequence[ClaimLedgerEvent],
    baseline_events: Sequence[ClaimLedgerEvent] = (),
    provider_failed: bool = False,
    source_exhausted: bool = False,
) -> TaskSatisfactionResult:
    current = tuple(events)
    baseline = tuple(baseline_events)
    direct = _unique_claim_ids(
        event for event in current if _is_direct_support(event, task=task)
    )
    baseline_direct = _unique_claim_ids(
        event for event in baseline if _is_direct_support(event, task=task)
    )
    counter = _unique_claim_ids(
        event
        for event in (*current, *baseline)
        if _is_counter_claim(event, task=task)
    )
    rerouted = _unique_claim_ids(
        event for event in current if _is_rerouted_claim(event, task=task)
    )
    lifecycle = _unique_claim_ids(
        event
        for event in current
        if event.lifecycle_kind == ClaimLifecycleKind.LIFECYCLE_REFRESH.value
        and event.claim_accepted
    )
    score_eligible = _unique_claim_ids(
        event for event in (*current, *baseline) if event.score_eligible
    )

    reasons: list[str] = []
    if counter:
        status = TaskSatisfactionStatus.COUNTER_CLAIM_FOUND
        reasons.append("counter claim matched the original task recipe")
    elif direct:
        status = TaskSatisfactionStatus.DIRECT_TASK_SATISFIED
        reasons.append("new source-backed claim satisfied the exact task recipe")
    elif baseline_direct:
        status = TaskSatisfactionStatus.BASELINE_CLAIM_REUSED
        reasons.append("current source-backed baseline claim satisfied the exact recipe")
    elif rerouted:
        status = TaskSatisfactionStatus.REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN
        reasons.append("accepted claim mapped elsewhere; original question remains open")
    elif lifecycle:
        status = TaskSatisfactionStatus.LIFECYCLE_REFRESH_ONLY
        reasons.append("new evidence refreshed lifecycle without closing the question")
    elif current and all(_is_wrong_subject(event) for event in current):
        status = TaskSatisfactionStatus.WRONG_SUBJECT
        reasons.append("all compiled claims were about another or unresolved subject")
    elif current and all(_is_stale(event) for event in current):
        status = TaskSatisfactionStatus.STALE_ONLY
        reasons.append("only old, expired, superseded, or unknown claims were found")
    elif provider_failed:
        status = TaskSatisfactionStatus.PROVIDER_FAILED
        reasons.append("claim or source provider failed before direct closure")
    elif source_exhausted:
        status = TaskSatisfactionStatus.SOURCE_EXHAUSTED
        reasons.append("bounded source routes ended without a relevant claim")
    else:
        status = TaskSatisfactionStatus.NO_RELEVANT_CLAIM
        reasons.append("no accepted mapping answered the original task")

    original_gap_closed = status in {
        TaskSatisfactionStatus.DIRECT_TASK_SATISFIED,
        TaskSatisfactionStatus.BASELINE_CLAIM_REUSED,
    }
    payload = {
        "task_id": task.task_id,
        "status": status.value,
        "direct": list(direct),
        "rerouted": list(rerouted),
        "baseline": list(baseline_direct),
        "lifecycle": list(lifecycle),
        "counter": list(counter),
    }
    return TaskSatisfactionResult(
        satisfaction_id=f"TSAT-{_sha256(_stable_json(payload))[:24]}",
        task_id=task.task_id,
        recipe_id=task.recipe_id,
        primitive_id=task.primitive_id,
        status=status.value,
        direct_claim_ids=direct,
        rerouted_claim_ids=rerouted,
        baseline_claim_ids=baseline_direct,
        lifecycle_refresh_claim_ids=lifecycle,
        counter_claim_ids=counter,
        score_eligible_claim_ids=score_eligible,
        original_gap_closed=original_gap_closed,
        material_gap_open=not original_gap_closed,
        provider_failed=provider_failed,
        source_exhausted=source_exhausted,
        reasons=tuple(reasons),
    )


def tag_claim_events_with_satisfaction(
    *,
    events: Sequence[ClaimLedgerEvent],
    satisfaction: TaskSatisfactionResult,
) -> tuple[ClaimLedgerEvent, ...]:
    direct_ids = set(satisfaction.direct_claim_ids)
    rerouted_ids = set(satisfaction.rerouted_claim_ids)
    counter_ids = set(satisfaction.counter_claim_ids)
    lifecycle_ids = set(satisfaction.lifecycle_refresh_claim_ids)
    tagged: list[ClaimLedgerEvent] = []
    for event in events:
        status = _fallback_event_status(event, satisfaction=satisfaction)
        closes = False
        if event.claim_id in counter_ids and _event_matches_original(event):
            status = TaskSatisfactionStatus.COUNTER_CLAIM_FOUND.value
        elif event.claim_id in direct_ids and _event_matches_original(event):
            status = TaskSatisfactionStatus.DIRECT_TASK_SATISFIED.value
            closes = True
        elif event.claim_id in rerouted_ids:
            status = (
                TaskSatisfactionStatus.REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN.value
            )
        elif event.claim_id in lifecycle_ids:
            status = TaskSatisfactionStatus.LIFECYCLE_REFRESH_ONLY.value
        tagged.append(
            replace(
                event,
                satisfaction_status=status,
                closes_original_gap=closes,
            )
        )
    return tuple(tagged)


def _is_direct_support(
    event: ClaimLedgerEvent, *, task: QuestionSourceTask
) -> bool:
    return (
        event.score_eligible
        and _visible_for_task(event, task=task)
        and event.mapping_status == MappingStatus.ACCEPTED.value
        and event.support_direction == SupportDirection.SUPPORT.value
        and event.mapped_recipe_id == task.recipe_id
        and event.mapped_primitive_id == task.primitive_id
        and event.lifecycle_kind != ClaimLifecycleKind.LIFECYCLE_REFRESH.value
    )


def _is_counter_claim(
    event: ClaimLedgerEvent, *, task: QuestionSourceTask
) -> bool:
    return (
        event.claim_accepted
        and _visible_for_task(event, task=task)
        and event.temporal_status == TemporalStatus.CURRENT.value
        and event.mapping_status == MappingStatus.ACCEPTED.value
        and event.support_direction == SupportDirection.COUNTER.value
        and event.mapped_recipe_id == task.recipe_id
        and event.mapped_primitive_id == task.primitive_id
    )


def _is_rerouted_claim(
    event: ClaimLedgerEvent, *, task: QuestionSourceTask
) -> bool:
    return (
        event.score_eligible
        and _visible_for_task(event, task=task)
        and event.mapping_status == MappingStatus.ACCEPTED.value
        and event.support_direction == SupportDirection.SUPPORT.value
        and bool(event.mapped_recipe_id)
        and (
            event.mapped_recipe_id != task.recipe_id
            or event.mapped_primitive_id != task.primitive_id
        )
    )


def _is_wrong_subject(event: ClaimLedgerEvent) -> bool:
    return (
        event.directness != Directness.DIRECT.value
        or "wrong_or_indirect_subject" in event.eligibility_reasons
        or "target_scope_not_eligible" in event.eligibility_reasons
    )


def _is_stale(event: ClaimLedgerEvent) -> bool:
    return event.temporal_status != TemporalStatus.CURRENT.value


def _event_matches_original(event: ClaimLedgerEvent) -> bool:
    return (
        event.mapped_recipe_id == event.original_recipe_id
        and event.mapped_primitive_id == event.original_primitive_id
    )


def _visible_for_task(
    event: ClaimLedgerEvent,
    *,
    task: QuestionSourceTask,
) -> bool:
    as_of = date.fromisoformat(task.as_of_date)
    return (
        event.target_entity_id == task.target_id
        and date.fromisoformat(event.source_published_at) <= as_of
        and date.fromisoformat(event.source_available_at) <= as_of
    )


def _fallback_event_status(
    event: ClaimLedgerEvent,
    *,
    satisfaction: TaskSatisfactionResult,
) -> str:
    if _is_wrong_subject(event):
        return TaskSatisfactionStatus.WRONG_SUBJECT.value
    if _is_stale(event):
        return TaskSatisfactionStatus.STALE_ONLY.value
    if satisfaction.status == TaskSatisfactionStatus.PROVIDER_FAILED.value:
        return TaskSatisfactionStatus.PROVIDER_FAILED.value
    return TaskSatisfactionStatus.NO_RELEVANT_CLAIM.value


def _unique_claim_ids(events: Sequence[ClaimLedgerEvent] | Any) -> tuple[str, ...]:
    return tuple(dict.fromkeys(event.claim_id for event in events))


def _stable_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


__all__ = [
    "TASK_SATISFACTION_SCHEMA_VERSION",
    "TaskSatisfactionResult",
    "TaskSatisfactionStatus",
    "evaluate_task_satisfaction",
    "tag_claim_events_with_satisfaction",
]
