"""Source route memory retrieval."""

from __future__ import annotations

from e2r.research_brain.memory_store import ResearchMemoryStore


def get_source_routes(memory_store: ResearchMemoryStore, archetype_id: str, primitive_id: str | None = None):
    return memory_store.get_source_routes(archetype_id, primitive_id)


__all__ = ["get_source_routes"]
