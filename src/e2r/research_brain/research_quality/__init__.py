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
from .adaptive_repair import (
    AdaptiveResearchRepairDirective,
    FAILURE_NEXT_ACTIONS,
    RESEARCH_REPAIR_FAILURE_CLASSES,
    canonical_research_failure_class,
    compile_research_repair_directive,
    audit_adaptive_repair_contract,
)

__all__ = [
    "BlindResearchBenchmarkResult",
    "BlindResearchQualityBenchmark",
    "MaterialFactComparison",
    "EvidenceSearchAdequacy",
    "audit_search_adequacy",
    "compile_dossier_search_adequacy",
    "select_research_grade_documents",
    "AdaptiveResearchRepairDirective",
    "FAILURE_NEXT_ACTIONS",
    "RESEARCH_REPAIR_FAILURE_CLASSES",
    "canonical_research_failure_class",
    "compile_research_repair_directive",
    "audit_adaptive_repair_contract",
]
