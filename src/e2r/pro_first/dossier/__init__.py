"""Strict ResearchDossier V1/V2 parsing, validation, normalization, and import."""

from .importer import DossierImportResult, ProDossierImporter
from .identity_binding import (
    BoundDossierIdentity,
    DossierIdentityBindingError,
    INITIAL_CONVERSATION_PLACEHOLDER,
    bind_dossier_transport_identity,
)
from .delta_merge import (
    DossierDeltaMergeError,
    DossierDeltaMergeResult,
    apply_research_dossier_delta,
)
from .dialect_adapter import (
    AdaptedDossier,
    DossierDialectError,
    ResearchDossierDialectAdapter,
)
from .normalizer import NormalizedDossier, ResearchDossierNormalizer
from .parser import DossierParseError, ParsedDossier, ResearchDossierParser
from .validator import (
    CANONICAL_COMPONENT_IDS,
    DossierValidationContext,
    DossierValidationError,
    ResearchDossierValidator,
)
from .v2 import (
    AvailabilityClass,
    DossierV2ClosureSummary,
    QuestionStatus,
    ResearchPassName,
    compile_dossier_v2_closure_summary,
    validate_research_status,
    validate_route_bindings,
)

__all__ = [
    "BoundDossierIdentity",
    "DossierIdentityBindingError",
    "CANONICAL_COMPONENT_IDS",
    "AdaptedDossier",
    "AvailabilityClass",
    "DossierDialectError",
    "DossierDeltaMergeError",
    "DossierDeltaMergeResult",
    "DossierImportResult",
    "DossierParseError",
    "DossierValidationContext",
    "DossierValidationError",
    "DossierV2ClosureSummary",
    "INITIAL_CONVERSATION_PLACEHOLDER",
    "NormalizedDossier",
    "ParsedDossier",
    "ProDossierImporter",
    "QuestionStatus",
    "ResearchDossierNormalizer",
    "ResearchDossierDialectAdapter",
    "ResearchDossierParser",
    "ResearchDossierValidator",
    "ResearchPassName",
    "compile_dossier_v2_closure_summary",
    "validate_research_status",
    "validate_route_bindings",
    "bind_dossier_transport_identity",
    "apply_research_dossier_delta",
]
