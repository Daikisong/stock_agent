"""Deprecated adapter for the canonical Research Brain case inventory."""

from __future__ import annotations

import warnings
from pathlib import Path

from e2r.research_brain.compiler.legacy_case_inventory import (
    ResearchCaseRecord,
    extract_research_cases as _canonical_extract_research_cases,
)


def extract_research_cases(
    *,
    repo_root: str | Path = ".",
    max_chars_per_file: int = 24000,
) -> list[ResearchCaseRecord]:
    warnings.warn(
        "e2r.research_reverse is deprecated; use e2r.research_brain.compiler",
        DeprecationWarning,
        stacklevel=2,
    )
    return _canonical_extract_research_cases(
        repo_root=repo_root,
        max_chars_per_file=max_chars_per_file,
    )


__all__ = ["ResearchCaseRecord", "extract_research_cases"]
