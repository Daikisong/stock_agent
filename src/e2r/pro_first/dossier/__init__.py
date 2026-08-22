"""Strict ResearchDossier V1/V2 parsing, validation, normalization, and import."""

from .importer import DossierImportResult, ProDossierImporter
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
    "CANONICAL_COMPONENT_IDS",
    "AdaptedDossier",
    "AvailabilityClass",
    "DossierDialectError",
    "DossierImportResult",
    "DossierParseError",
    "DossierValidationContext",
    "DossierValidationError",
    "DossierV2ClosureSummary",
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
]
