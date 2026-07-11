"""Blind research-quality benchmark primitives."""

from .blind_benchmark import (
    BlindResearchBenchmarkResult,
    BlindResearchQualityBenchmark,
    MaterialFactComparison,
)
from .search_adequacy import (
    EvidenceSearchAdequacy,
    audit_search_adequacy,
    compile_dossier_search_adequacy,
    select_research_grade_documents,
)

__all__ = [
    "BlindResearchBenchmarkResult",
    "BlindResearchQualityBenchmark",
    "MaterialFactComparison",
    "EvidenceSearchAdequacy",
    "audit_search_adequacy",
    "compile_dossier_search_adequacy",
    "select_research_grade_documents",
]
