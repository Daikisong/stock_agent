"""Deprecated adapter for Research Brain recipe compatibility reports."""

from __future__ import annotations

import warnings
from pathlib import Path
from typing import Any, Iterable, Mapping

from e2r.research_brain.recipes.legacy_route_recovery import (
    OFFICIAL_SOURCE_FAMILIES,
    build_source_route_patterns as _canonical_build_source_route_patterns,
    write_source_route_recovery_reports as _canonical_write_source_route_recovery_reports,
)


def build_source_route_patterns(
    *,
    repo_root: str | Path = ".",
    records: Iterable[Mapping[str, Any]] = (),
) -> dict[str, Any]:
    warnings.warn(
        "e2r.source_routing is deprecated; use e2r.research_brain.recipes",
        DeprecationWarning,
        stacklevel=2,
    )
    return _canonical_build_source_route_patterns(repo_root=repo_root, records=records)


def write_source_route_recovery_reports(
    *,
    repo_root: str | Path = ".",
    docs_dir: str | Path = "docs/operational",
    records: Iterable[Mapping[str, Any]] = (),
) -> dict[str, Any]:
    warnings.warn(
        "e2r.source_routing is deprecated; use e2r.research_brain.recipes",
        DeprecationWarning,
        stacklevel=2,
    )
    return _canonical_write_source_route_recovery_reports(
        repo_root=repo_root,
        docs_dir=docs_dir,
        records=records,
    )


__all__ = [
    "OFFICIAL_SOURCE_FAMILIES",
    "build_source_route_patterns",
    "write_source_route_recovery_reports",
]
