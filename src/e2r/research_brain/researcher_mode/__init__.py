"""Canonical open-ended Researcher Mode for E2R v5.

Phase 80 starts this namespace with whole-repository forensics.  Later phases
add the historical atlas, source graph, component researchers, judges, and
deterministic aggregation here so production has one future authority.
"""

from .audits import (
    PHASE80_ARTIFACT_PATHS,
    compile_phase80_forensics,
    write_phase80_forensics,
)

__all__ = [
    "PHASE80_ARTIFACT_PATHS",
    "compile_phase80_forensics",
    "write_phase80_forensics",
]
