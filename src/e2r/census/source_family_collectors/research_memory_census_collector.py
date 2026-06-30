"""Research memory Census v3 source family attempt rows."""

from __future__ import annotations

from . import attempt_row


def collect_research_memory_attempt(symbol: str, *, hint_count: int = 0) -> dict:
    return attempt_row(
        symbol=symbol,
        source_family="ResearchMemory",
        status="PLANNING_HINT_PRESENT" if hint_count else "PLANNING_MEMORY_CHECKED",
        detail={"score_evidence_allowed": False, "hint_count": hint_count},
    )


__all__ = ["collect_research_memory_attempt"]
