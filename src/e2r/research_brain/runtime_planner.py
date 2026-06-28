"""Runtime Research Brain planning entrypoint."""

from __future__ import annotations

from typing import Sequence

from e2r.research_brain.investigation_planner import build_research_brain_plan
from e2r.research_brain.memory_store import ResearchMemoryStore
from e2r.research_brain.schemas import CandidateEvent, ResearchBrainPlan


def plan_candidate_events(
    *,
    candidate_events: Sequence[CandidateEvent],
    memory_store: ResearchMemoryStore,
    limit: int | None = None,
) -> tuple[ResearchBrainPlan, ...]:
    selected = tuple(candidate_events if limit is None else candidate_events[:limit])
    return tuple(build_research_brain_plan(candidate_event=event, memory_store=memory_store) for event in selected)


__all__ = ["plan_candidate_events"]
