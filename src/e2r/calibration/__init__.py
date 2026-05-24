"""Historical Stock-Web calibration ingest and scoring-profile promotion."""

from .aggregate import aggregate_validated_rows
from .dedupe import dedupe_trigger_rows
from .md_discovery import discover_markdown_documents
from .md_parser import parse_markdown_document
from .promotion import promote_calibrated_profile
from .scoring_profile import ScoringProfile, get_active_scoring_profile, load_scoring_profile
from .validation import validate_trigger_rows

__all__ = [
    "ScoringProfile",
    "aggregate_validated_rows",
    "dedupe_trigger_rows",
    "discover_markdown_documents",
    "get_active_scoring_profile",
    "load_scoring_profile",
    "parse_markdown_document",
    "promote_calibrated_profile",
    "validate_trigger_rows",
]
