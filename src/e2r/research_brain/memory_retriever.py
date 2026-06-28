"""Memory retrieval facade."""

from __future__ import annotations

from e2r.research_brain.memory_store import ResearchMemoryStore


def retrieve_planning_memory(memory_store: ResearchMemoryStore, archetype_id: str, limit: int = 20):
    return memory_store.query(archetype_id=archetype_id, allowed_for_runtime_planning=True, limit=limit)


__all__ = ["retrieve_planning_memory"]
