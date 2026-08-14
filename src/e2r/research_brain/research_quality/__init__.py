"""Blind research-quality benchmark primitives."""

from .blind_benchmark import (
    BlindResearchBenchmarkResult,
    BlindResearchQualityBenchmark,
    MaterialFactComparison,
    POST_RUN_SEMANTIC_MATCH_CONTRACT,
    build_post_run_reviewer_identity,
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
from .material_fact_lane import (
    PRODUCTION_MATERIAL_FACT_SCHEMA_VERSION,
    ProductionMaterialFactLane,
    combine_production_material_fact_lanes,
    compile_production_material_fact_lane,
    write_production_material_fact_lane,
)

__all__ = [
    "BlindResearchBenchmarkResult",
    "BlindResearchQualityBenchmark",
    "MaterialFactComparison",
    "POST_RUN_SEMANTIC_MATCH_CONTRACT",
    "build_post_run_reviewer_identity",
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
    "PRODUCTION_MATERIAL_FACT_SCHEMA_VERSION",
    "ProductionMaterialFactLane",
    "combine_production_material_fact_lanes",
    "compile_production_material_fact_lane",
    "write_production_material_fact_lane",
]
