"""Deprecated adapter for canonical Research Brain memory projection."""

from __future__ import annotations

import warnings
from pathlib import Path
from typing import Any, Iterable, Mapping

from e2r.research_brain.retrieval.legacy_runtime_memory import (
    build_memory_card_matrix,
    build_runtime_memory_cards as _canonical_build_runtime_memory_cards,
)


def build_runtime_memory_cards(
    *,
    repo_root: str | Path = ".",
    records: Iterable[Mapping[str, Any]],
) -> dict[str, Any]:
    warnings.warn(
        "e2r.research_reverse is deprecated; use e2r.research_brain.retrieval",
        DeprecationWarning,
        stacklevel=2,
    )
    return _canonical_build_runtime_memory_cards(repo_root=repo_root, records=records)


__all__ = ["build_memory_card_matrix", "build_runtime_memory_cards"]
