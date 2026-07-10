"""Canonical ResearchMemoryGraph facade."""

from __future__ import annotations

from typing import Iterable

from e2r.research_brain.intelligence_schema import (
    EvidenceRecipe,
    HistoricalResearchCase,
    HistoricalSourceVerification,
    ResearchMemoryGraph,
)
from e2r.research_brain.retrieval import compile_semantic_memory_graph


def build_memory_graph(
    cases: Iterable[HistoricalResearchCase],
    recipes: Iterable[EvidenceRecipe],
    *,
    source_verifications: Iterable[HistoricalSourceVerification] = (),
) -> ResearchMemoryGraph:
    return compile_semantic_memory_graph(
        cases,
        recipes,
        source_verifications=source_verifications,
    ).graph


__all__ = ["build_memory_graph"]
