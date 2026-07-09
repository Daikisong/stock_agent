"""Single source-of-truth declaration for reconstructed Research Brain.

This module deliberately contains no legacy imports. Compatibility packages
may import canonical modules, but canonical production code must never import
e2r.research_reverse or e2r.source_routing.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


CANONICAL_INTELLIGENCE_NAMESPACE = "e2r.research_brain"
CANONICAL_SCHEMA_MODULE = "e2r.research_brain.intelligence_schema"
CANONICAL_SCHEMA_SOURCE_COUNT = 1


class CanonicalCapability(str, Enum):
    CORPUS = "corpus"
    COMPILER = "compiler"
    RECIPES = "recipes"
    RETRIEVAL = "retrieval"
    PLANNING = "planning"
    REPLAY = "replay"
    RUNTIME = "runtime"


@dataclass(frozen=True)
class CanonicalResearchBrainArchitecture:
    namespace: str = CANONICAL_INTELLIGENCE_NAMESPACE
    schema_module: str = CANONICAL_SCHEMA_MODULE
    schema_source_count: int = CANONICAL_SCHEMA_SOURCE_COUNT
    capabilities: tuple[str, ...] = tuple(item.value for item in CanonicalCapability)
    legacy_imports_allowed: bool = False
    scoring_mutation_allowed: bool = False
    stage_mutation_allowed: bool = False
    historical_outcome_in_runtime_prompt_allowed: bool = False


def canonical_architecture() -> CanonicalResearchBrainArchitecture:
    return CanonicalResearchBrainArchitecture()


__all__ = [
    "CANONICAL_INTELLIGENCE_NAMESPACE",
    "CANONICAL_SCHEMA_MODULE",
    "CANONICAL_SCHEMA_SOURCE_COUNT",
    "CanonicalCapability",
    "CanonicalResearchBrainArchitecture",
    "canonical_architecture",
]
