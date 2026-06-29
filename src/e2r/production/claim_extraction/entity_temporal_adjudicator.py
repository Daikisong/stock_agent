"""Entity and temporal adjudication for production claims."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from typing import Sequence

from .contract_blind_extractor import RawAssertionRecord


@dataclass(frozen=True)
class AdjudicationResult:
    target_scope_status: str
    directness: str
    temporal_status: str
    polarity: str
    semantic_status: str
    reasons: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def adjudicate_entity_temporal_scope(
    assertion: RawAssertionRecord,
    *,
    target_aliases: Sequence[str],
    as_of_date: date,
    source_published_at: date | None = None,
) -> AdjudicationResult:
    reasons: list[str] = []
    direct = assertion.subject in set(target_aliases)
    if not direct:
        reasons.append("wrong_or_unknown_subject")
    event_date = _parse_date(assertion.event_date) or source_published_at
    temporal_status = "CURRENT"
    if event_date is None:
        temporal_status = "UNKNOWN"
        reasons.append("missing_event_or_source_date")
    elif event_date > as_of_date:
        temporal_status = "UNKNOWN"
        reasons.append("future_event_date")
    elif event_date and (as_of_date - event_date).days > 540:
        temporal_status = "HISTORICAL"
        reasons.append("historical_only")
    semantic_status = "PASS" if direct and temporal_status == "CURRENT" else "REJECTED"
    return AdjudicationResult(
        target_scope_status="DIRECT" if direct else "UNRELATED",
        directness="DIRECT" if direct else "NOT_TARGET_SCOPED",
        temporal_status=temporal_status,
        polarity=assertion.polarity_proposal,
        semantic_status=semantic_status,
        reasons=tuple(reasons),
    )


def _parse_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return None


__all__ = ["AdjudicationResult", "adjudicate_entity_temporal_scope"]
