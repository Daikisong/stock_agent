"""Deprecated adapter for canonical Research Brain compatibility reports."""

from __future__ import annotations

import warnings
from pathlib import Path
from typing import Any

from e2r.research_brain.compiler.legacy_compatibility_reports import (
    build_research_reverse_bundle as _canonical_build_bundle,
    write_research_reverse_bundle as _canonical_write_bundle,
)


def build_research_reverse_bundle(*, repo_root: str | Path = ".") -> dict[str, Any]:
    warnings.warn(
        "e2r.research_reverse is deprecated; use e2r.research_brain.compiler",
        DeprecationWarning,
        stacklevel=2,
    )
    return _canonical_build_bundle(repo_root=repo_root)


def write_research_reverse_bundle(
    *,
    repo_root: str | Path = ".",
    docs_dir: str | Path = "docs/operational",
) -> dict[str, Any]:
    warnings.warn(
        "e2r.research_reverse is deprecated; use e2r.research_brain.compiler",
        DeprecationWarning,
        stacklevel=2,
    )
    return _canonical_write_bundle(repo_root=repo_root, docs_dir=docs_dir)


__all__ = ["build_research_reverse_bundle", "write_research_reverse_bundle"]
