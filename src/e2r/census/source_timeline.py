"""Source timeline construction for Census v2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

from .baseline_input_collector import CensusBaselineBundle
from .schemas import CensusAssessmentEvent, UniverseInstrument


@dataclass(frozen=True)
class SourceTimelineEvent:
    event_id: str
    symbol: str
    event_type: str
    source_family: str
    event_date: str
    candidate_event_eligible: bool = False
    score_evidence_eligible: bool = False
    accepted_claim_ids: tuple[str, ...] = ()
    reason: str = ""
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "symbol": self.symbol,
            "event_type": self.event_type,
            "source_family": self.source_family,
            "event_date": self.event_date,
            "candidate_event_eligible": self.candidate_event_eligible,
            "score_evidence_eligible": self.score_evidence_eligible,
            "accepted_claim_ids": list(self.accepted_claim_ids),
            "reason": self.reason,
            "metadata": dict(self.metadata),
        }


@dataclass(frozen=True)
class SourceTimeline:
    symbol: str
    company_name: str
    as_of_date: str
    events: tuple[SourceTimelineEvent, ...]

    @property
    def has_candidate_event(self) -> bool:
        return any(event.candidate_event_eligible for event in self.events)

    @property
    def has_score_evidence(self) -> bool:
        return any(event.score_evidence_eligible for event in self.events)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": "e2r_census_v2_source_timeline_v1",
            "symbol": self.symbol,
            "company_name": self.company_name,
            "as_of_date": self.as_of_date,
            "event_count": len(self.events),
            "candidate_event_count": sum(1 for event in self.events if event.candidate_event_eligible),
            "score_evidence_event_count": sum(1 for event in self.events if event.score_evidence_eligible),
            "events": [event.to_dict() for event in self.events],
        }


def build_source_timelines(
    *,
    instruments: Sequence[UniverseInstrument],
    assessment_events: Sequence[CensusAssessmentEvent],
    bundle: CensusBaselineBundle,
    as_of_date: str,
) -> tuple[SourceTimeline, ...]:
    assessment_by_symbol = {event.symbol: event for event in assessment_events}
    timelines: list[SourceTimeline] = []
    for instrument in instruments:
        events: list[SourceTimelineEvent] = []
        assessment = assessment_by_symbol.get(instrument.symbol)
        if assessment is not None:
            events.append(
                SourceTimelineEvent(
                    event_id=assessment.assessment_event_id,
                    symbol=instrument.symbol,
                    event_type="CensusAssessmentEvent",
                    source_family=assessment.source_family,
                    event_date=as_of_date,
                    candidate_event_eligible=False,
                    score_evidence_eligible=False,
                    reason="administrative full-universe assessment stamp; never score evidence",
                    metadata={"assessment_type": assessment.assessment_type},
                )
            )
        for event in bundle.candidate_events_by_symbol.get(instrument.symbol, ()):
            events.append(
                SourceTimelineEvent(
                    event_id=str(event.get("candidate_event_id")),
                    symbol=instrument.symbol,
                    event_type=str(event.get("event_type") or "CandidateEvent"),
                    source_family=str(event.get("source_family") or "unknown"),
                    event_date=as_of_date,
                    candidate_event_eligible=True,
                    score_evidence_eligible=False,
                    reason=str(event.get("reason") or "candidate event opens investigation only"),
                    metadata=dict(event),
                )
            )
        for event in bundle.report_snapshot_events_by_symbol.get(instrument.symbol, ()):
            events.append(
                SourceTimelineEvent(
                    event_id=str(event.get("candidate_event_id")),
                    symbol=instrument.symbol,
                    event_type="StoredSourceEvent",
                    source_family=str(event.get("source_family") or "ReportRadar"),
                    event_date=str(event.get("published_at") or as_of_date),
                    candidate_event_eligible=True,
                    score_evidence_eligible=False,
                    reason=str(event.get("reason") or "stored source requires lifecycle refresh"),
                    metadata=dict(event),
                )
            )
        for event in bundle.price_events_by_symbol.get(instrument.symbol, ()):
            events.append(
                SourceTimelineEvent(
                    event_id=str(event.get("candidate_event_id")),
                    symbol=instrument.symbol,
                    event_type="MarketAnomaly",
                    source_family="KRXPrice",
                    event_date=str(event.get("to_date") or as_of_date),
                    candidate_event_eligible=True,
                    score_evidence_eligible=False,
                    reason="price path opens investigation only and cannot score",
                    metadata=dict(event),
                )
            )
        accepted = tuple(bundle.existing_ledger.accepted_claims_by_symbol.get(instrument.symbol, ()))
        if accepted:
            claim_ids = tuple(str(row.get("claim_id")) for row in accepted if row.get("claim_id"))
            events.append(
                SourceTimelineEvent(
                    event_id=f"AcceptedClaimLedgerEvent:{instrument.symbol}",
                    symbol=instrument.symbol,
                    event_type="AcceptedClaimLedgerEvent",
                    source_family="ExistingEvidenceOSLedger",
                    event_date=as_of_date,
                    candidate_event_eligible=True,
                    score_evidence_eligible=True,
                    accepted_claim_ids=claim_ids,
                    reason="accepted current claims with score contribution refs unlock scoring",
                    metadata={"accepted_claim_count": len(claim_ids)},
                )
            )
        timelines.append(
            SourceTimeline(
                symbol=instrument.symbol,
                company_name=instrument.company_name,
                as_of_date=as_of_date,
                events=tuple(events),
            )
        )
    return tuple(timelines)


__all__ = ["SourceTimeline", "SourceTimelineEvent", "build_source_timelines"]
