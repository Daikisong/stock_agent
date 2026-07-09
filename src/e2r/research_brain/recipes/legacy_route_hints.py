"""Compatibility source-route hint aggregation owned by Research Brain."""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any, Iterable, Mapping


def recover_source_route_hints_by_archetype(records: Iterable[Mapping[str, Any]]) -> dict[str, list[str]]:
    counters: dict[str, Counter[str]] = defaultdict(Counter)
    for record in records:
        archetype_id = str(record["canonical_archetype_id"])
        for family in record.get("runtime_source_route_hints", []):
            counters[archetype_id][str(family)] += 1
    return {archetype_id: [family for family, _ in counter.most_common()] for archetype_id, counter in counters.items()}


__all__ = ["recover_source_route_hints_by_archetype"]
