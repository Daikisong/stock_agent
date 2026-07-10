"""Canonical memory retrieval facade.

The pre-reconstruction facade returned the first ``limit`` records from the
JSONL store. Canonical callers now have to provide a semantic index and a
balanced request; count/order based retrieval is intentionally unavailable.
"""

from __future__ import annotations

from e2r.research_brain.intelligence_schema import (
    BalancedRetrievalRequest,
    BalancedRetrievalResult,
)
from e2r.research_brain.retrieval import (
    SemanticMemoryIndex,
    retrieve_balanced_memory,
)


def retrieve_planning_memory(
    memory_index: SemanticMemoryIndex,
    request: BalancedRetrievalRequest,
) -> BalancedRetrievalResult:
    return retrieve_balanced_memory(memory_index, request)


__all__ = ["retrieve_planning_memory"]
