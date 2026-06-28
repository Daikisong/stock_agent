"""Counterexample memory retrieval."""

from __future__ import annotations

from e2r.research_brain.memory_store import ResearchMemoryStore
from e2r.research_brain.schemas import MemoryType


def get_counterexamples(memory_store: ResearchMemoryStore, archetype_id: str):
    return memory_store.query(archetype_id=archetype_id, memory_type=MemoryType.COUNTEREXAMPLE.value, limit=None)


__all__ = ["get_counterexamples"]
