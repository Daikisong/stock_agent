"""One-way adapter from legacy Census baseline leaves to the canonical daily runner."""

from __future__ import annotations

from datetime import date
from typing import Any, Sequence

from e2r.production.metadata import stable_hash
from e2r.research_brain.runtime.atomic_score_stage import (
    AtomicScoreClaim,
    AtomicStageDecision,
)
from e2r.research_brain.runtime.current_operation import (
    CurrentTriggerSignal,
    CurrentTriggerType,
)
from e2r.research_brain.runtime.current_operation_runner import (
    CurrentOperationRunnerConfig,
    CurrentOperationRunnerInput,
    DailyBaselineLane,
    DailyBaselineLaneStatus,
    DailyBaselineLaneType,
    DailyDeepExecution,
    DailyUniverseMember,
)

from .last_effective_thesis import LastEffectiveThesisState
from .schemas import BaselineScanResult, UniverseInstrument
from .source_timeline import SourceTimeline, SourceTimelineEvent


CANONICAL_CURRENT_ADAPTER_SCHEMA_VERSION = "e2r_canonical_current_adapter_v1"


def adapt_census_snapshot_to_current_input(
    *,
    as_of_date: str,
    instruments: Sequence[UniverseInstrument],
    scans: Sequence[BaselineScanResult],
    source_timelines: Sequence[SourceTimeline],
    thesis_states: Sequence[LastEffectiveThesisState],
    atomic_decisions: Sequence[AtomicStageDecision] = (),
    deep_executions: Sequence[DailyDeepExecution] = (),
    config: CurrentOperationRunnerConfig,
) -> CurrentOperationRunnerInput:
    """Preserve source leaves, but never reuse legacy score or Stage hints."""

    as_of = date.fromisoformat(as_of_date)
    instrument_by_symbol = _unique_by(
        instruments,
        key=lambda item: item.symbol,
        context="adapter instrument",
    )
    scan_by_symbol = _unique_by(
        scans,
        key=lambda item: item.symbol,
        context="adapter baseline scan",
    )
    timeline_by_symbol = _unique_by(
        source_timelines,
        key=lambda item: item.symbol,
        context="adapter source timeline",
    )
    thesis_by_symbol = _unique_by(
        thesis_states,
        key=lambda item: item.symbol,
        context="adapter thesis state",
    )
    if set(scan_by_symbol) != set(instrument_by_symbol):
        raise ValueError("canonical adapter needs one baseline scan per instrument")
    if set(timeline_by_symbol) != set(instrument_by_symbol):
        raise ValueError("canonical adapter needs one source timeline per instrument")
    if set(thesis_by_symbol) != set(instrument_by_symbol):
        raise ValueError("canonical adapter needs one thesis state per instrument")
    if any(item.as_of_date != as_of_date for item in scans):
        raise ValueError("canonical adapter baseline scan as-of mismatch")
    if any(item.as_of_date != as_of_date for item in source_timelines):
        raise ValueError("canonical adapter source timeline as-of mismatch")
    if any(item.as_of_date != as_of_date for item in thesis_states):
        raise ValueError("canonical adapter thesis state as-of mismatch")

    universe = tuple(
        DailyUniverseMember(
            target_id=item.symbol,
            target_name=item.company_name,
            market=item.market,
            as_of_date=as_of_date,
            eligible=item.eligible_for_census,
            exclusion_reason=(
                None if item.eligible_for_census else item.exclusion_reason or "ineligible"
            ),
        )
        for item in instruments
    )
    decision_claims = _canonical_decision_claims(atomic_decisions)
    claims_by_target: dict[str, tuple[AtomicScoreClaim, ...]] = {}
    for claim in decision_claims:
        claims_by_target.setdefault(claim.target_id, ())
        claims_by_target[claim.target_id] = (
            *claims_by_target[claim.target_id],
            claim,
        )

    baseline_lanes: list[DailyBaselineLane] = []
    triggers: list[CurrentTriggerSignal] = []
    trigger_keys: set[tuple[str, str, str]] = set()
    for instrument in instruments:
        if not instrument.eligible_for_census:
            continue
        scan = scan_by_symbol[instrument.symbol]
        timeline = timeline_by_symbol[instrument.symbol]
        thesis = thesis_by_symbol[instrument.symbol]
        events = tuple(
            event
            for event in timeline.events
            if event.event_type != "CensusAssessmentEvent"
        )
        for event in events:
            if date.fromisoformat(event.event_date) > as_of:
                raise ValueError("future legacy timeline event entered current adapter")
        baseline_lanes.extend(
            _baseline_lanes_for_symbol(
                instrument=instrument,
                scan=scan,
                events=events,
                thesis=thesis,
                claims=claims_by_target.get(instrument.symbol, ()),
                as_of_date=as_of_date,
            )
        )
        for event in events:
            if not event.candidate_event_eligible:
                continue
            trigger_type = _trigger_type_for_event(event)
            key = (instrument.symbol, trigger_type, event.event_id)
            if key in trigger_keys:
                continue
            trigger_keys.add(key)
            triggers.append(
                _trigger_from_event(
                    target_id=instrument.symbol,
                    event=event,
                    trigger_type=trigger_type,
                )
            )
        for claim in claims_by_target.get(instrument.symbol, ()):
            if not claim.current_open or not claim.source_backed:
                continue
            key = (
                instrument.symbol,
                CurrentTriggerType.EXISTING_LEDGER.value,
                claim.claim_id,
            )
            if key in trigger_keys:
                continue
            trigger_keys.add(key)
            triggers.append(
                CurrentTriggerSignal(
                    signal_id="CURTRIG-"
                    + stable_hash(
                        {
                            "target_id": instrument.symbol,
                            "claim_id": claim.claim_id,
                            "trigger_type": CurrentTriggerType.EXISTING_LEDGER.value,
                        }
                    )[:24],
                    target_id=instrument.symbol,
                    observed_date=claim.observed_date,
                    trigger_type=CurrentTriggerType.EXISTING_LEDGER.value,
                    source_id=claim.source_ids[0],
                )
            )
        if (
            thesis.thesis_status in {"ACTIVE_THESIS", "NEEDS_REFRESH"}
            and not any(
                item.target_id == instrument.symbol
                and item.trigger_type == CurrentTriggerType.EXISTING_LEDGER.value
                for item in triggers
            )
        ):
            source_event_id = thesis.last_effective_event_id or (
                f"LEGACY-THESIS-{instrument.symbol}"
            )
            triggers.append(
                CurrentTriggerSignal(
                    signal_id="CURTRIG-"
                    + stable_hash(
                        {
                            "target_id": instrument.symbol,
                            "legacy_thesis_event_id": source_event_id,
                        }
                    )[:24],
                    target_id=instrument.symbol,
                    observed_date=as_of_date,
                    trigger_type=CurrentTriggerType.EXISTING_LEDGER.value,
                    source_id=source_event_id,
                )
            )
    triggers.sort(
        key=lambda item: (item.target_id, item.observed_date, item.signal_id)
    )
    return CurrentOperationRunnerInput(
        as_of_date=as_of_date,
        universe=universe,
        baseline_lanes=tuple(baseline_lanes),
        triggers=tuple(triggers),
        claims=decision_claims,
        source_tasks=(),
        atomic_decisions=tuple(atomic_decisions),
        deep_executions=tuple(deep_executions),
        config=config,
    )


def _baseline_lanes_for_symbol(
    *,
    instrument: UniverseInstrument,
    scan: BaselineScanResult,
    events: Sequence[SourceTimelineEvent],
    thesis: LastEffectiveThesisState,
    claims: Sequence[AtomicScoreClaim],
    as_of_date: str,
) -> tuple[DailyBaselineLane, ...]:
    provider_errors = tuple(scan.provider_errors)
    if provider_errors:
        official = DailyBaselineLane(
            target_id=instrument.symbol,
            as_of_date=as_of_date,
            lane_type=DailyBaselineLaneType.OFFICIAL.value,
            lane_status=DailyBaselineLaneStatus.PROVIDER_FAILED.value,
            provider_error="|".join(provider_errors),
        )
    else:
        official_events = tuple(
            item
            for item in events
            if _trigger_type_for_event(item)
            in {
                CurrentTriggerType.OFFICIAL.value,
                CurrentTriggerType.EARNINGS.value,
                CurrentTriggerType.IR.value,
                CurrentTriggerType.REPORT.value,
            }
        )
        official_observed = bool(official_events) or any(
            (
                scan.recent_disclosure_count,
                scan.recent_supply_contract_count,
                scan.recent_facility_investment_count,
                scan.recent_earnings_event_count,
                scan.revision_signal_count,
            )
        )
        official = _observed_or_empty_lane(
            target_id=instrument.symbol,
            as_of_date=as_of_date,
            lane_type=DailyBaselineLaneType.OFFICIAL,
            observed=official_observed,
            source_ids=tuple(item.event_id for item in official_events),
        )
    market_events = tuple(
        item
        for item in events
        if _trigger_type_for_event(item) == CurrentTriggerType.MARKET.value
    )
    price = _observed_or_empty_lane(
        target_id=instrument.symbol,
        as_of_date=as_of_date,
        lane_type=DailyBaselineLaneType.PRICE,
        observed=bool(market_events) or scan.price_anomaly_count > 0,
        source_ids=tuple(item.event_id for item in market_events),
    )
    risk_events = tuple(
        item
        for item in events
        if _trigger_type_for_event(item) == CurrentTriggerType.RISK.value
    )
    risk = _observed_or_empty_lane(
        target_id=instrument.symbol,
        as_of_date=as_of_date,
        lane_type=DailyBaselineLaneType.RISK,
        observed=bool(risk_events) or scan.recent_risk_event_count > 0,
        source_ids=tuple(item.event_id for item in risk_events),
    )
    ledger_events = tuple(
        item
        for item in events
        if _trigger_type_for_event(item)
        == CurrentTriggerType.EXISTING_LEDGER.value
    )
    ledger_observed = bool(ledger_events or claims) or thesis.thesis_status in {
        "ACTIVE_THESIS",
        "NEEDS_REFRESH",
    }
    ledger = _observed_or_empty_lane(
        target_id=instrument.symbol,
        as_of_date=as_of_date,
        lane_type=DailyBaselineLaneType.EXISTING_LEDGER,
        observed=ledger_observed,
        source_ids=tuple(
            dict.fromkeys(
                (
                    *(item.event_id for item in ledger_events),
                    *(item.source_ids[0] for item in claims if item.source_ids),
                )
            )
        ),
    )
    return official, price, risk, ledger


def _observed_or_empty_lane(
    *,
    target_id: str,
    as_of_date: str,
    lane_type: DailyBaselineLaneType,
    observed: bool,
    source_ids: Sequence[str],
) -> DailyBaselineLane:
    if not observed:
        return DailyBaselineLane(
            target_id=target_id,
            as_of_date=as_of_date,
            lane_type=lane_type.value,
            lane_status=DailyBaselineLaneStatus.NO_RESULT.value,
        )
    normalized_sources = tuple(
        dict.fromkeys(str(item) for item in source_ids if str(item).strip())
    ) or (f"BASELINE-SCAN-{target_id}-{lane_type.value}",)
    return DailyBaselineLane(
        target_id=target_id,
        as_of_date=as_of_date,
        lane_type=lane_type.value,
        lane_status=DailyBaselineLaneStatus.OBSERVED.value,
        source_ids=normalized_sources,
        observed_date=as_of_date,
    )


def _trigger_from_event(
    *,
    target_id: str,
    event: SourceTimelineEvent,
    trigger_type: str,
) -> CurrentTriggerSignal:
    return CurrentTriggerSignal(
        signal_id="CURTRIG-"
        + stable_hash(
            {
                "target_id": target_id,
                "event_id": event.event_id,
                "trigger_type": trigger_type,
            }
        )[:24],
        target_id=target_id,
        observed_date=event.event_date,
        trigger_type=trigger_type,
        source_id=event.event_id,
        historical_replay=False,
        expected_or_outcome_context=False,
        counts_as_score_evidence=False,
    )


def _trigger_type_for_event(event: SourceTimelineEvent) -> str:
    text = " ".join(
        (event.event_type, event.source_family, event.reason)
    ).casefold()
    if event.event_type == "MarketAnomaly" or "price" in text or "market" in text:
        return CurrentTriggerType.MARKET.value
    if event.event_type == "AcceptedClaimLedgerEvent" or "ledger" in text:
        return CurrentTriggerType.EXISTING_LEDGER.value
    if "risk" in text or "red" in text or "counter" in text:
        return CurrentTriggerType.RISK.value
    if "earning" in text or "실적" in text:
        return CurrentTriggerType.EARNINGS.value
    if "investor relation" in text or "issuerir" in text or event.event_type == "IR":
        return CurrentTriggerType.IR.value
    if "report" in text or event.event_type == "StoredSourceEvent":
        return CurrentTriggerType.REPORT.value
    if "news" in text:
        return CurrentTriggerType.NEWS.value
    return CurrentTriggerType.OFFICIAL.value


def _canonical_decision_claims(
    decisions: Sequence[AtomicStageDecision],
) -> tuple[AtomicScoreClaim, ...]:
    claims: dict[str, AtomicScoreClaim] = {}
    for decision in decisions:
        for claim in decision.claims:
            existing = claims.get(claim.claim_id)
            if existing is not None and existing.to_dict() != claim.to_dict():
                raise ValueError("canonical adapter claim id collision")
            claims[claim.claim_id] = claim
    return tuple(claims.values())


def _unique_by(
    values: Sequence[Any],
    *,
    key: Any,
    context: str,
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for item in values:
        identity = str(key(item))
        if not identity or identity in result:
            raise ValueError(f"duplicate or empty {context}: {identity}")
        result[identity] = item
    return result


__all__ = [
    "CANONICAL_CURRENT_ADAPTER_SCHEMA_VERSION",
    "adapt_census_snapshot_to_current_input",
]
