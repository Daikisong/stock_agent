"""Query pattern memory retrieval."""

from __future__ import annotations

from e2r.research_brain.memory_store import ResearchMemoryStore


def get_query_pattern_hints(memory_store: ResearchMemoryStore, archetype_id: str) -> tuple[str, ...]:
    profile = memory_store.get_archetype_profile(archetype_id)
    return profile.query_pattern_hints


__all__ = ["get_query_pattern_hints"]
