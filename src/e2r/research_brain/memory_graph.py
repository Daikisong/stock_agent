"""Lightweight memory relation graph."""

from __future__ import annotations

from collections import defaultdict
from typing import Mapping, Sequence

from e2r.research_brain.schemas import ResearchMemoryRecord


def build_memory_graph(records: Sequence[ResearchMemoryRecord]) -> Mapping[str, object]:
    by_archetype: dict[str, list[str]] = defaultdict(list)
    by_primitive: dict[str, list[str]] = defaultdict(list)
    for record in records:
        if record.canonical_archetype_id:
            by_archetype[record.canonical_archetype_id].append(record.record_id)
        for primitive_id in record.primitive_ids:
            by_primitive[primitive_id].append(record.record_id)
    return {
        "schema_version": "research_brain_memory_graph_v1",
        "archetype_edges": dict(by_archetype),
        "primitive_edges": dict(by_primitive),
    }


__all__ = ["build_memory_graph"]
