"""Census assessment event creation."""

from __future__ import annotations

from e2r.production.metadata import stable_hash

from .schemas import CensusAssessmentEvent, UniverseInstrument


def build_census_assessment_event(
    instrument: UniverseInstrument,
    *,
    as_of_date: str,
    universe_source: str = "KRX",
    recent_candidate_events: tuple[str, ...] = (),
    recent_claim_ledger_refs: tuple[str, ...] = (),
    baseline_scan_refs: tuple[str, ...] = (),
) -> CensusAssessmentEvent:
    event_id = "CAE-" + stable_hash(
        {
            "symbol": instrument.symbol,
            "as_of_date": as_of_date,
            "assessment_type": "baseline_census",
            "universe_source": universe_source,
        }
    )[:20]
    return CensusAssessmentEvent(
        assessment_event_id=event_id,
        symbol=instrument.symbol,
        company_name=instrument.company_name,
        as_of_date=as_of_date,
        universe_source=universe_source,
        instrument_status=instrument.listing_status,
        market=instrument.market,
        large_sector_id=instrument.large_sector_id,
        recent_candidate_events=recent_candidate_events,
        recent_claim_ledger_refs=recent_claim_ledger_refs,
        baseline_scan_refs=baseline_scan_refs,
        eligible_for_deep_dossier=False,
    )


__all__ = ["build_census_assessment_event"]
