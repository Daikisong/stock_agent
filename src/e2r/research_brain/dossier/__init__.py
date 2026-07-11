"""Generic full-thesis evidence dossier orchestration."""

from .orchestrator import (
    DOSSIER_ORCHESTRATOR_SCHEMA_VERSION,
    DossierRunConfig,
    DossierTarget,
    FullThesisDossierOrchestrator,
    load_question_family_catalog,
)
from .adaptive_closure import (
    ADAPTIVE_CLOSURE_SCHEMA_VERSION,
    OrganicClaimClosureResult,
    next_action_for_failure,
    run_organic_claim_closure,
)
from .scoring_pipeline import (
    COMPONENT_QUESTION_FAMILIES,
    run_dossier_scoring_pipeline,
)
from .source_research import (
    SOURCE_RESEARCH_SCHEMA_VERSION,
    run_dossier_source_research,
)
from .source_merge import (
    MERGED_SOURCE_SCHEMA_VERSION,
    merge_dossier_source_runs,
)
from .question_finalizer import (
    QUESTION_FINALIZER_SCHEMA_VERSION,
    finalize_dossier_question_closures,
)
from .acceptance import (
    TARGET_ACCEPTANCE_SCHEMA_VERSION,
    compile_target_full_thesis_acceptance,
)

__all__ = [
    "DOSSIER_ORCHESTRATOR_SCHEMA_VERSION",
    "DossierRunConfig",
    "DossierTarget",
    "FullThesisDossierOrchestrator",
    "load_question_family_catalog",
    "ADAPTIVE_CLOSURE_SCHEMA_VERSION",
    "OrganicClaimClosureResult",
    "next_action_for_failure",
    "run_organic_claim_closure",
    "COMPONENT_QUESTION_FAMILIES",
    "run_dossier_scoring_pipeline",
    "SOURCE_RESEARCH_SCHEMA_VERSION",
    "run_dossier_source_research",
    "MERGED_SOURCE_SCHEMA_VERSION",
    "merge_dossier_source_runs",
    "QUESTION_FINALIZER_SCHEMA_VERSION",
    "finalize_dossier_question_closures",
    "TARGET_ACCEPTANCE_SCHEMA_VERSION",
    "compile_target_full_thesis_acceptance",
]
