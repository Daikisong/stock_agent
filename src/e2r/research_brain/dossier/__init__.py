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
]
