"""Cheap Census baseline scanner."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, Sequence

from .schemas import BaselineScanResult, UniverseInstrument


@dataclass(frozen=True)
class BaselineScanInputs:
    provider_failed_symbols: Mapping[str, Sequence[str]] = field(default_factory=dict)
    provider_failure_by_symbol: Mapping[str, Sequence[str]] = field(default_factory=dict)
    price_anomaly_symbols: Mapping[str, int] = field(default_factory=dict)
    price_anomaly_by_symbol: Mapping[str, Sequence[Mapping[str, object]]] = field(default_factory=dict)
    recent_official_events: Mapping[str, Mapping[str, int]] = field(default_factory=dict)
    existing_claim_counts: Mapping[str, int] = field(default_factory=dict)
    existing_stage: Mapping[str, str] = field(default_factory=dict)
    historical_official_events: Mapping[str, Mapping[str, int]] = field(default_factory=dict)
    latest_regular_report_by_symbol: Mapping[str, Mapping[str, object]] = field(default_factory=dict)
    latest_material_disclosure_by_symbol: Mapping[str, Mapping[str, object]] = field(default_factory=dict)
    last_material_official_event_by_symbol: Mapping[str, Mapping[str, object]] = field(default_factory=dict)
    risk_events_by_symbol: Mapping[str, Sequence[Mapping[str, object]]] = field(default_factory=dict)
    companyguide_revision_events: Mapping[str, int] = field(default_factory=dict)
    companyguide_revision_events_by_symbol: Mapping[str, Sequence[Mapping[str, object]]] = field(default_factory=dict)
    report_radar_events: Mapping[str, int] = field(default_factory=dict)
    report_radar_events_by_symbol: Mapping[str, Sequence[Mapping[str, object]]] = field(default_factory=dict)
    issuer_ir_events: Mapping[str, int] = field(default_factory=dict)
    issuer_ir_events_by_symbol: Mapping[str, Sequence[Mapping[str, object]]] = field(default_factory=dict)
    trusted_news_events: Mapping[str, int] = field(default_factory=dict)
    trusted_news_events_by_symbol: Mapping[str, Sequence[Mapping[str, object]]] = field(default_factory=dict)
    market_anomaly_events_by_symbol: Mapping[str, Sequence[Mapping[str, object]]] = field(default_factory=dict)
    existing_claim_refs: Mapping[str, Sequence[str]] = field(default_factory=dict)
    existing_claim_refs_by_symbol: Mapping[str, Sequence[str]] = field(default_factory=dict)
    previous_watchlist_state: Mapping[str, Mapping[str, object]] = field(default_factory=dict)
    last_effective_thesis_by_symbol: Mapping[str, Mapping[str, object]] = field(default_factory=dict)
    research_memory_hints_by_symbol: Mapping[str, Sequence[Mapping[str, object]]] = field(default_factory=dict)
    source_gap_by_symbol: Mapping[str, Sequence[str]] = field(default_factory=dict)
    no_data_reason_by_symbol: Mapping[str, str] = field(default_factory=dict)


class BaselineScanner:
    """Build traceable light scan rows without creating score evidence."""

    def __init__(self, inputs: BaselineScanInputs | None = None) -> None:
        self.inputs = inputs or BaselineScanInputs()

    def scan(self, instrument: UniverseInstrument, *, as_of_date: str) -> BaselineScanResult:
        if not instrument.eligible_for_census:
            return BaselineScanResult(
                symbol=instrument.symbol,
                as_of_date=as_of_date,
                scan_status="SKIPPED",
                reason_codes=(f"excluded:{instrument.exclusion_reason}",),
            )
        provider_errors = tuple(self.inputs.provider_failed_symbols.get(instrument.symbol, ()))
        official = dict(self.inputs.recent_official_events.get(instrument.symbol, {}))
        historical = dict(self.inputs.historical_official_events.get(instrument.symbol, {}))
        price_anomaly_count = int(self.inputs.price_anomaly_symbols.get(instrument.symbol, 0))
        existing_claim_count = int(self.inputs.existing_claim_counts.get(instrument.symbol, 0))
        revision_signal_count = int(official.get("revisions", 0))
        revision_signal_count += int(self.inputs.companyguide_revision_events.get(instrument.symbol, 0))
        revision_signal_count += int(self.inputs.report_radar_events.get(instrument.symbol, 0))
        revision_signal_count += int(self.inputs.issuer_ir_events.get(instrument.symbol, 0))
        status = "PROVIDER_FAILED" if provider_errors else "SCANNED"
        reason_codes: list[str] = []
        if provider_errors:
            reason_codes.append("provider_failed")
        if price_anomaly_count:
            reason_codes.append("market_anomaly_investigation_only")
        if official:
            reason_codes.append("recent_official_event")
        if historical:
            reason_codes.append("historical_official_event_for_lifecycle_refresh")
        if revision_signal_count:
            reason_codes.append("revision_or_report_event")
        if existing_claim_count:
            reason_codes.append("existing_claim_ledger_refs")
        if self.inputs.source_gap_by_symbol.get(instrument.symbol):
            reason_codes.append("source_gap_requires_followup")
        if self.inputs.no_data_reason_by_symbol.get(instrument.symbol):
            reason_codes.append(self.inputs.no_data_reason_by_symbol[instrument.symbol])
        trigger_priority_score = _priority_score(
            official=official,
            price_anomaly_count=price_anomaly_count,
            existing_claim_count=existing_claim_count,
            provider_failed=bool(provider_errors),
            revision_signal_count=revision_signal_count,
        )
        return BaselineScanResult(
            symbol=instrument.symbol,
            as_of_date=as_of_date,
            scan_status=status,
            recent_disclosure_count=int(official.get("disclosures", 0)),
            recent_supply_contract_count=int(official.get("supply_contracts", 0)),
            recent_facility_investment_count=int(official.get("facility_investments", 0)),
            recent_earnings_event_count=int(official.get("earnings", 0)),
            recent_risk_event_count=int(official.get("risk", 0)),
            revision_signal_count=revision_signal_count,
            price_anomaly_count=price_anomaly_count,
            existing_claim_count=existing_claim_count,
            existing_stage=self.inputs.existing_stage.get(instrument.symbol),
            provider_errors=provider_errors,
            reason_codes=tuple(reason_codes),
            trigger_priority_score=trigger_priority_score,
        )

    def scan_many(self, instruments: Sequence[UniverseInstrument], *, as_of_date: str) -> tuple[BaselineScanResult, ...]:
        return tuple(self.scan(item, as_of_date=as_of_date) for item in instruments)


def _priority_score(
    *,
    official: Mapping[str, int],
    price_anomaly_count: int,
    existing_claim_count: int,
    provider_failed: bool,
    revision_signal_count: int = 0,
) -> float:
    if provider_failed:
        return 0.0
    score = 0.0
    score += min(sum(int(value) for value in official.values()) * 10.0, 60.0)
    score += min(existing_claim_count * 12.0, 36.0)
    score += min(revision_signal_count * 6.0, 24.0)
    score += min(price_anomaly_count * 5.0, 15.0)
    return round(score, 4)


__all__ = ["BaselineScanInputs", "BaselineScanner"]
