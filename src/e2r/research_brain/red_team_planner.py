"""Red-team planning helpers for Research Brain."""

from __future__ import annotations

from e2r.research_brain.memory_store import ResearchMemoryStore
from e2r.research_brain.schemas import MemoryType


def red_team_patterns_for_archetype(memory_store: ResearchMemoryStore, archetype_id: str) -> tuple[str, ...]:
    records = list(memory_store.get_false_positive_patterns(archetype_id))
    records.extend(memory_store.query(archetype_id=archetype_id, memory_type=MemoryType.HARD_BREAK_PATTERN.value, limit=20))
    values: list[str] = []
    for record in records:
        values.extend(record.false_positive_patterns)
        values.extend(record.guard_primitives)
        values.extend(record.hard_break_primitives)
        if not (record.false_positive_patterns or record.guard_primitives or record.hard_break_primitives):
            values.append(record.memory_type)
    return tuple(dict.fromkeys(values))


__all__ = ["red_team_patterns_for_archetype"]
