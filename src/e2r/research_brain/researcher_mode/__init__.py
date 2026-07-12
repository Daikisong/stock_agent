"""Canonical open-ended Researcher Mode for E2R v5.

Phase 80 starts this namespace with whole-repository forensics.  Later phases
add the historical atlas, source graph, component researchers, judges, and
deterministic aggregation here so production has one future authority.
"""

from .audits import (
    PHASE80_ARTIFACT_PATHS,
    compile_phase80_forensics,
    write_phase80_forensics,
)
from .historical_atlas import (
    ATLAS_OUTPUT_FILES,
    ATLAS_PASS,
    HistoricalJudgmentAtlasResult,
    compile_historical_judgment_atlas,
    compile_historical_judgment_atlas_from_semantic,
    write_historical_judgment_atlas,
)
from .component_anchor_atlas import (
    C06_MANDATORY_ANCHOR_FAMILIES,
    COMPONENT_ANCHOR_PASS,
    compile_component_anchor_atlas,
    compile_component_anchor_atlas_from_files,
    write_component_anchor_atlas,
)
from .schemas import (
    AnchorConfidence,
    ComponentAnchor,
    HistoricalResearchJudgment,
    HistoricalScoreSchemaType,
)
from .research_question_seed_catalog import (
    ResearchQuestionSeed,
    ResearchQuestionSeedCatalog,
    load_research_question_seed_catalog,
)
from .question_authority_audit import (
    QUESTION_AUTHORITY_PASS,
    audit_research_question_seed_authority,
)

__all__ = [
    "PHASE80_ARTIFACT_PATHS",
    "compile_phase80_forensics",
    "write_phase80_forensics",
    "ATLAS_OUTPUT_FILES",
    "ATLAS_PASS",
    "AnchorConfidence",
    "C06_MANDATORY_ANCHOR_FAMILIES",
    "COMPONENT_ANCHOR_PASS",
    "ComponentAnchor",
    "HistoricalJudgmentAtlasResult",
    "HistoricalResearchJudgment",
    "HistoricalScoreSchemaType",
    "QUESTION_AUTHORITY_PASS",
    "ResearchQuestionSeed",
    "ResearchQuestionSeedCatalog",
    "compile_historical_judgment_atlas",
    "compile_historical_judgment_atlas_from_semantic",
    "compile_component_anchor_atlas",
    "compile_component_anchor_atlas_from_files",
    "write_component_anchor_atlas",
    "audit_research_question_seed_authority",
    "load_research_question_seed_catalog",
    "write_historical_judgment_atlas",
]
