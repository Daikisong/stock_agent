"""All-archetype golden replay and known-bad acceptance helpers."""

from .golden import (
    MANDATORY_MECHANISM_FAMILIES,
    build_mechanism_golden_dossier,
    run_mechanism_golden_replay,
)
from .known_bad import (
    REQUIRED_V2_KNOWN_BAD_CASE_IDS,
    audit_v2_known_bad_corpus,
)
from .audit import compile_generalization_acceptance

__all__ = [
    "MANDATORY_MECHANISM_FAMILIES",
    "REQUIRED_V2_KNOWN_BAD_CASE_IDS",
    "audit_v2_known_bad_corpus",
    "build_mechanism_golden_dossier",
    "run_mechanism_golden_replay",
    "compile_generalization_acceptance",
]
