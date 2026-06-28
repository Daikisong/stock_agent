"""Stage transition memory retrieval."""

from __future__ import annotations

from e2r.research_brain.memory_store import ResearchMemoryStore
from e2r.research_brain.schemas import MemoryType


def get_stage_transition_patterns(memory_store: ResearchMemoryStore, archetype_id: str):
    rows = []
    for memory_type in (
        MemoryType.STAGE2_ACTIONABLE_UNLOCK.value,
        MemoryType.STAGE2_WATCH_CAP.value,
        MemoryType.FOUR_B_WATCH_CONDITION.value,
        MemoryType.FOUR_C_THESIS_BREAK_CONDITION.value,
    ):
        rows.extend(memory_store.query(archetype_id=archetype_id, memory_type=memory_type, limit=None))
    return tuple(rows)


__all__ = ["get_stage_transition_patterns"]
