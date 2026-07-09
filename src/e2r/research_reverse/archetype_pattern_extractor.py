"""Deprecated adapter for canonical Research Brain case aggregation."""

from e2r.research_brain.compiler.legacy_pattern_aggregator import (
    build_archetype_coverage_matrix,
    build_source_quality_matrix,
)

__all__ = ["build_archetype_coverage_matrix", "build_source_quality_matrix"]
