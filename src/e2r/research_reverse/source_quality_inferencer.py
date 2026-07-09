"""Deprecated adapter for Research Brain source-quality inference."""

from e2r.research_brain.compiler.legacy_source_quality import (
    URL_RE,
    extract_urls,
    infer_source_families,
    infer_source_quality,
    source_quality_flags,
)

__all__ = [
    "URL_RE",
    "extract_urls",
    "infer_source_families",
    "infer_source_quality",
    "source_quality_flags",
]
