"""Local, deterministic Evidence Preflight before source verification."""

from .atomic_fact import (
    AtomicFactPreflight,
    AtomicFactPreflightResult,
    CompoundFactSplitResult,
    split_compound_fact,
)
from .canonical_url import CanonicalURLResolution, CanonicalURLResolver
from .date_resolver import DatePrecedenceResolution, DatePrecedenceResolver
from .issuer_alias import IssuerAliasResolution, IssuerAliasResolver
from .models import (
    EvidencePreflightResult,
    PreflightIssue,
    PreflightOperation,
    RejectionRootCauseClass,
    RejectionRouting,
    ResolvedSourceRepresentation,
    StaticPreflightNormalization,
)
from .rejection_classifier import ClassifiedRejections, RejectionClassifier
from .scope_mapper import ClosedEnumScopeMapper, ClosedScopeMapping
from .service import (
    LocalEvidencePreflightService,
    PREFLIGHT_SEMANTICS_VERSION,
    PreSchemaV3Normalizer,
)
from .source_representation import (
    SourceRepresentationResolution,
    SourceRepresentationResolver,
)
from .text_normalizer import LiteralQuoteMatch, TextNormalization, TextQuoteNormalizer

__all__ = [
    "AtomicFactPreflight",
    "AtomicFactPreflightResult",
    "CanonicalURLResolution",
    "CanonicalURLResolver",
    "ClassifiedRejections",
    "ClosedEnumScopeMapper",
    "ClosedScopeMapping",
    "CompoundFactSplitResult",
    "DatePrecedenceResolution",
    "DatePrecedenceResolver",
    "EvidencePreflightResult",
    "IssuerAliasResolution",
    "IssuerAliasResolver",
    "LiteralQuoteMatch",
    "LocalEvidencePreflightService",
    "PREFLIGHT_SEMANTICS_VERSION",
    "PreSchemaV3Normalizer",
    "PreflightIssue",
    "PreflightOperation",
    "RejectionClassifier",
    "RejectionRootCauseClass",
    "RejectionRouting",
    "ResolvedSourceRepresentation",
    "SourceRepresentationResolution",
    "SourceRepresentationResolver",
    "StaticPreflightNormalization",
    "TextNormalization",
    "TextQuoteNormalizer",
    "split_compound_fact",
]
