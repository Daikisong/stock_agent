"""Deprecated adapter for canonical Research Brain corpus discovery."""

from __future__ import annotations

import warnings
from pathlib import Path

from e2r.research_brain.corpus.legacy_file_scanner import (
    DEFAULT_RESEARCH_GLOBS,
    GENERATED_GOAL4_DOC_PREFIXES,
    GENERATED_GOAL4_FILENAMES,
    GENERATED_GOAL4_PREFIXES,
    scan_research_files as _canonical_scan_research_files,
)


def scan_research_files(
    repo_root: str | Path = ".",
    patterns: tuple[str, ...] = DEFAULT_RESEARCH_GLOBS,
) -> list[Path]:
    warnings.warn(
        "e2r.research_reverse is deprecated; use e2r.research_brain.corpus",
        DeprecationWarning,
        stacklevel=2,
    )
    return _canonical_scan_research_files(repo_root, patterns)


__all__ = [
    "DEFAULT_RESEARCH_GLOBS",
    "GENERATED_GOAL4_DOC_PREFIXES",
    "GENERATED_GOAL4_FILENAMES",
    "GENERATED_GOAL4_PREFIXES",
    "scan_research_files",
]
