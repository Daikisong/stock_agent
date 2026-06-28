"""Green blocker memory retrieval."""

from __future__ import annotations

from e2r.research_brain.memory_store import ResearchMemoryStore


def get_green_blockers(memory_store: ResearchMemoryStore, archetype_id: str):
    return memory_store.get_green_blockers(archetype_id)


__all__ = ["get_green_blockers"]
