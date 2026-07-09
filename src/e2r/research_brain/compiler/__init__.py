"""Canonical research intelligence compilers."""

from e2r.research_brain.compiler.case_source_verifier import (
    SourceVerificationCompilationResult,
    compile_case_level_source_verification,
    load_historical_case_source_links,
    load_historical_provider_snapshots,
    write_case_level_source_verification,
)
from e2r.research_brain.compiler.semantic_case_compiler import (
    SemanticCompilationResult,
    compile_research_intelligence,
    discover_historical_research_paths,
    write_research_intelligence,
)

__all__ = [
    "SemanticCompilationResult",
    "SourceVerificationCompilationResult",
    "compile_case_level_source_verification",
    "compile_research_intelligence",
    "discover_historical_research_paths",
    "load_historical_case_source_links",
    "load_historical_provider_snapshots",
    "write_case_level_source_verification",
    "write_research_intelligence",
]
