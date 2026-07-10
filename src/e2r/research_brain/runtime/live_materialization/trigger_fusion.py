"""Fuse current baseline/state observations into investigation-only triggers."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import date
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl

from .baseline_materializer import BaselineLane, BaselineLaneRecord, BaselineLaneStatus
from .current_state_store import CurrentStateRecord, EventLifecycleStatus
from .universe_materializer import LiveUniverseRow


TRIGGER_SIGNAL_SCHEMA_VERSION = "e2r_live_trigger_signal_v1"
_RISK_TOKENS = (
    "관리종목",
    "상장폐지",
    "거래정지",
    "투자주의",
    "투자경고",
    "투자위험",
    "불성실공시",
    "감사의견",
)
_EARNINGS_TOKENS = ("잠정실적", "영업실적", "매출액", "손익구조")


class TriggerType(str, Enum):
    OFFICIAL = "OFFICIAL"
    EARNINGS = "EARNINGS"
    IR = "IR"
    REPORT = "REPORT"
    NEWS = "NEWS"
    MARKET = "MARKET"
    RISK = "RISK"
    EXISTING_LEDGER = "EXISTING_LEDGER"


@dataclass(frozen=True)
class TriggerFusionConfig:
    as_of_date: str
    market_abs_return_threshold_pct: float = 10.0
    market_min_trading_value: float = 1_000_000_000.0
    test_mode: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if self.market_abs_return_threshold_pct <= 0 or self.market_abs_return_threshold_pct > 100:
            raise ValueError("market return trigger threshold must be explicit and bounded")
        if self.market_min_trading_value < 0:
            raise ValueError("market trading-value threshold cannot be negative")


@dataclass(frozen=True)
class TriggerSignal:
    trigger_signal_id: str
    target_id: str
    target_name: str
    trigger_type: str
    source_event_id: str
    effective_date: str
    detected_at: str
    source_refs: tuple[str, ...]
    provider_names: tuple[str, ...]
    subject_direct: bool
    lifecycle_status: str
    investigation_required: bool
    score_evidence_eligible: bool
    headline_or_snippet_only: bool
    payload: Mapping[str, Any]
    schema_version: str = TRIGGER_SIGNAL_SCHEMA_VERSION

    def __post_init__(self) -> None:
        TriggerType(self.trigger_type)
        date.fromisoformat(self.effective_date)
        date.fromisoformat(self.detected_at)
        if not all(
            (
                self.trigger_signal_id.strip(),
                self.target_id.strip(),
                self.target_name.strip(),
                self.source_event_id.strip(),
            )
        ):
            raise ValueError("trigger signal identity required")
        if not self.source_refs or not self.provider_names:
            raise ValueError("trigger signal requires source and provider lineage")
        if not self.subject_direct:
            raise ValueError("wrong-subject trigger cannot enter the fused pool")
        if self.score_evidence_eligible:
            raise ValueError("trigger signal cannot be score evidence")
        if self.headline_or_snippet_only and self.score_evidence_eligible:
            raise ValueError("headline/snippet cannot be score evidence")

    @property
    def dedupe_key(self) -> tuple[str, str, str]:
        return (self.target_id, self.source_event_id, self.effective_date)

    def to_dict(self) -> dict[str, Any]:
        return {
            **asdict(self),
            "source_refs": list(self.source_refs),
            "provider_names": list(self.provider_names),
            "payload": dict(self.payload),
        }


@dataclass(frozen=True)
class CandidateEvent:
    candidate_event_id: str
    target_id: str
    target_name: str
    as_of_date: str
    latest_effective_date: str
    trigger_types: tuple[str, ...]
    trigger_signal_ids: tuple[str, ...]
    source_refs: tuple[str, ...]
    investigation_required: bool
    active_thesis_present: bool
    score_evidence_eligible: bool
    summary: str
    schema_version: str = "e2r_live_candidate_event_v1"

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        date.fromisoformat(self.latest_effective_date)
        if not self.trigger_signal_ids or not self.source_refs or not self.trigger_types:
            raise ValueError("candidate event requires fused trigger lineage")
        if any(item not in {value.value for value in TriggerType} for item in self.trigger_types):
            raise ValueError("candidate event trigger type invalid")
        if self.score_evidence_eligible:
            raise ValueError("candidate event cannot be score evidence")

    def to_dict(self) -> dict[str, Any]:
        return {
            **asdict(self),
            "trigger_types": list(self.trigger_types),
            "trigger_signal_ids": list(self.trigger_signal_ids),
            "source_refs": list(self.source_refs),
        }


@dataclass(frozen=True)
class TriggerFusionResult:
    as_of_date: str
    status: str
    trigger_signals: tuple[TriggerSignal, ...]
    candidate_events: tuple[CandidateEvent, ...]
    dedupe_report: Mapping[str, Any]
    source_distribution: Mapping[str, Any]
    audit: Mapping[str, Any]

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)


class CurrentTriggerFusion:
    def fuse(
        self,
        config: TriggerFusionConfig,
        *,
        universe: Sequence[LiveUniverseRow],
        baseline_lanes: Sequence[BaselineLaneRecord],
        current_state: Sequence[CurrentStateRecord] = (),
    ) -> TriggerFusionResult:
        eligible = tuple(row for row in universe if row.eligible)
        universe_by_symbol = _unique_universe(eligible)
        lanes_by_symbol: dict[str, dict[str, BaselineLaneRecord]] = {}
        for lane in baseline_lanes:
            if lane.target_id not in universe_by_symbol:
                continue
            target_lanes = lanes_by_symbol.setdefault(lane.target_id, {})
            if lane.lane in target_lanes:
                raise ValueError("duplicate baseline lane entered trigger fusion")
            target_lanes[lane.lane] = lane
        state_by_symbol = {record.target_id: record for record in current_state}
        if len(state_by_symbol) != len(current_state):
            raise ValueError("duplicate current-state target entered trigger fusion")
        raw_signals: list[TriggerSignal] = []
        scanned_symbols: set[str] = set()
        for symbol, member in sorted(universe_by_symbol.items()):
            scanned_symbols.add(symbol)
            lanes = lanes_by_symbol.get(symbol, {})
            official = lanes.get(BaselineLane.OFFICIAL.value)
            price = lanes.get(BaselineLane.PRICE.value)
            risk = lanes.get(BaselineLane.RISK.value)
            ledger = lanes.get(BaselineLane.EXISTING_LEDGER.value)
            if official:
                raw_signals.extend(
                    _official_signals(
                        member=member,
                        lane=official,
                        as_of_date=config.as_of_date,
                    )
                )
            if price:
                market = _market_signal(
                    member=member,
                    lane=price,
                    config=config,
                )
                if market:
                    raw_signals.append(market)
            if risk:
                raw_signals.extend(
                    _risk_signals(
                        member=member,
                        lane=risk,
                        as_of_date=config.as_of_date,
                    )
                )
            if ledger:
                raw_signals.extend(
                    _ledger_signals(
                        member=member,
                        lane=ledger,
                        as_of_date=config.as_of_date,
                    )
                )
            state = state_by_symbol.get(symbol)
            if state:
                raw_signals.extend(
                    _active_state_signals(
                        member=member,
                        record=state,
                        as_of_date=config.as_of_date,
                    )
                )
        signals, duplicate_rows = _dedupe_signals(raw_signals)
        candidates = _candidate_events(
            signals,
            state_by_symbol=state_by_symbol,
            as_of_date=config.as_of_date,
        )
        full_scan_attempted = scanned_symbols == set(universe_by_symbol)
        audit = _audit_trigger_fusion(
            as_of_date=config.as_of_date,
            eligible=eligible,
            lanes_by_symbol=lanes_by_symbol,
            raw_signals=tuple(raw_signals),
            signals=signals,
            candidates=candidates,
            full_scan_attempted=full_scan_attempted,
        )
        dedupe_report = {
            "schema_version": "e2r_live_trigger_dedupe_report_v1",
            "as_of_date": config.as_of_date,
            "raw_trigger_count": len(raw_signals),
            "deduped_trigger_count": len(signals),
            "duplicate_trigger_count": len(duplicate_rows),
            "duplicates": duplicate_rows,
        }
        source_distribution = _source_distribution(
            as_of_date=config.as_of_date,
            signals=signals,
        )
        return TriggerFusionResult(
            as_of_date=config.as_of_date,
            status=(
                "CURRENT_TRIGGER_FUSION_PASS"
                if audit["hard_acceptance_pass"]
                else "CURRENT_TRIGGER_FUSION_FAIL"
            ),
            trigger_signals=signals,
            candidate_events=candidates,
            dedupe_report=dedupe_report,
            source_distribution=source_distribution,
            audit=audit,
        )


def write_trigger_fusion(
    result: TriggerFusionResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "candidates": root / "candidate_events.jsonl",
        "signals": root / "trigger_signals.jsonl",
        "dedupe": root / "trigger_dedupe_report.json",
        "distribution": root / "trigger_source_distribution.json",
        "audit": root / "trigger_fusion_audit.json",
    }
    write_jsonl(paths["candidates"], (item.to_dict() for item in result.candidate_events))
    write_jsonl(paths["signals"], (item.to_dict() for item in result.trigger_signals))
    write_json(paths["dedupe"], result.dedupe_report)
    write_json(paths["distribution"], result.source_distribution)
    write_json(
        paths["audit"],
        {**dict(result.audit), "status": result.status},
    )
    return paths


def load_trigger_signals(path: str | Path) -> tuple[TriggerSignal, ...]:
    source = Path(path)
    if not source.is_file():
        return ()
    rows: list[TriggerSignal] = []
    with source.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
                source_refs = tuple(payload.pop("source_refs"))
                provider_names = tuple(payload.pop("provider_names"))
                rows.append(
                    TriggerSignal(
                        **payload,
                        source_refs=source_refs,
                        provider_names=provider_names,
                    )
                )
            except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
                raise ValueError(
                    f"invalid trigger signal row at line {line_number}: {exc}"
                ) from exc
    return tuple(rows)


def load_candidate_events(path: str | Path) -> tuple[CandidateEvent, ...]:
    source = Path(path)
    if not source.is_file():
        return ()
    rows: list[CandidateEvent] = []
    with source.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
                trigger_types = tuple(payload.pop("trigger_types"))
                trigger_signal_ids = tuple(payload.pop("trigger_signal_ids"))
                source_refs = tuple(payload.pop("source_refs"))
                rows.append(
                    CandidateEvent(
                        **payload,
                        trigger_types=trigger_types,
                        trigger_signal_ids=trigger_signal_ids,
                        source_refs=source_refs,
                    )
                )
            except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
                raise ValueError(
                    f"invalid candidate event row at line {line_number}: {exc}"
                ) from exc
    return tuple(rows)


def _official_signals(
    *,
    member: LiveUniverseRow,
    lane: BaselineLaneRecord,
    as_of_date: str,
) -> tuple[TriggerSignal, ...]:
    if lane.status in {
        BaselineLaneStatus.PROVIDER_FAILED.value,
        BaselineLaneStatus.AUTH_FAILED.value,
        BaselineLaneStatus.RATE_LIMITED.value,
        BaselineLaneStatus.BUDGET_EXHAUSTED.value,
    }:
        return ()
    signals: list[TriggerSignal] = []
    regular = lane.values.get("latest_regular_report")
    if isinstance(regular, Mapping) and regular.get("rcept_no"):
        signals.append(
            _signal_from_filing(
                member=member,
                filing=regular,
                trigger_type=TriggerType.REPORT,
                provider_names=lane.provider_names,
                as_of_date=as_of_date,
                lifecycle_status="LATEST_REGULAR_REPORT_CANDIDATE",
            )
        )
    material = lane.values.get("latest_material_event")
    if isinstance(material, Mapping) and material.get("rcept_no"):
        report_name = str(material.get("report_name") or "")
        trigger_type = (
            TriggerType.RISK
            if _contains_any(report_name, _RISK_TOKENS)
            else TriggerType.EARNINGS
            if _contains_any(report_name, _EARNINGS_TOKENS)
            else TriggerType.OFFICIAL
        )
        signals.append(
            _signal_from_filing(
                member=member,
                filing=material,
                trigger_type=trigger_type,
                provider_names=lane.provider_names,
                as_of_date=as_of_date,
                lifecycle_status="REQUIRES_CURRENT_LIFECYCLE_ADJUDICATION",
            )
        )
    return tuple(signals)


def _market_signal(
    *,
    member: LiveUniverseRow,
    lane: BaselineLaneRecord,
    config: TriggerFusionConfig,
) -> TriggerSignal | None:
    if lane.status != BaselineLaneStatus.OBSERVED.value:
        return None
    return_pct = _float(lane.values.get("return_pct"))
    trading_value = _float(lane.values.get("trading_value"))
    if abs(return_pct) < config.market_abs_return_threshold_pct:
        return None
    if trading_value < config.market_min_trading_value:
        return None
    effective_date = str(lane.values.get("price_date") or config.as_of_date)
    source_event_id = "KRX-PRICE-" + stable_hash(
        {
            "target": member.symbol,
            "date": effective_date,
            "return_pct": return_pct,
            "trading_value": trading_value,
        }
    )[:24]
    return _new_signal(
        member=member,
        trigger_type=TriggerType.MARKET,
        source_event_id=source_event_id,
        effective_date=effective_date,
        detected_at=config.as_of_date,
        source_refs=lane.source_ids,
        provider_names=lane.provider_names,
        lifecycle_status="SHORT_LIVED_INVESTIGATION_TRIGGER",
        payload={
            "return_pct": return_pct,
            "trading_value": trading_value,
            "price_score_usage": "INVESTIGATION_ONLY",
        },
    )


def _risk_signals(
    *,
    member: LiveUniverseRow,
    lane: BaselineLaneRecord,
    as_of_date: str,
) -> tuple[TriggerSignal, ...]:
    if lane.status != BaselineLaneStatus.OBSERVED.value:
        return ()
    signals: list[TriggerSignal] = []
    events = lane.values.get("risk_events") or ()
    for event in events:
        if not isinstance(event, Mapping) or not event.get("rcept_no"):
            continue
        signals.append(
            _signal_from_filing(
                member=member,
                filing=event,
                trigger_type=TriggerType.RISK,
                provider_names=lane.provider_names,
                as_of_date=as_of_date,
                lifecycle_status=str(event.get("lifecycle") or "UNKNOWN"),
            )
        )
    if not events and lane.values.get("krx_segment"):
        event_id = "KRX-RISK-" + stable_hash(
            {
                "target": member.symbol,
                "segment": lane.values.get("krx_segment"),
                "date": as_of_date,
            }
        )[:24]
        signals.append(
            _new_signal(
                member=member,
                trigger_type=TriggerType.RISK,
                source_event_id=event_id,
                effective_date=as_of_date,
                detected_at=as_of_date,
                source_refs=lane.source_ids,
                provider_names=lane.provider_names,
                lifecycle_status=str(lane.values.get("risk_lifecycle_status") or "UNKNOWN"),
                payload={"krx_segment": lane.values.get("krx_segment")},
            )
        )
    return tuple(signals)


def _ledger_signals(
    *,
    member: LiveUniverseRow,
    lane: BaselineLaneRecord,
    as_of_date: str,
) -> tuple[TriggerSignal, ...]:
    claim_ids = tuple(str(item) for item in lane.values.get("accepted_current_claim_ids") or ())
    return tuple(
        _new_signal(
            member=member,
            trigger_type=TriggerType.EXISTING_LEDGER,
            source_event_id=claim_id,
            effective_date=as_of_date,
            detected_at=as_of_date,
            source_refs=lane.source_ids,
            provider_names=lane.provider_names,
            lifecycle_status="NEEDS_CURRENT_REFRESH",
            payload={"claim_id": claim_id, "stale_needs_refresh": True},
        )
        for claim_id in claim_ids
    )


def _active_state_signals(
    *,
    member: LiveUniverseRow,
    record: CurrentStateRecord,
    as_of_date: str,
) -> tuple[TriggerSignal, ...]:
    signals: list[TriggerSignal] = []
    for event in record.material_events:
        if event.lifecycle_status != EventLifecycleStatus.OPEN.value:
            continue
        trigger_type = (
            TriggerType.RISK if event.event_type == "RISK" else TriggerType.EXISTING_LEDGER
        )
        signals.append(
            _new_signal(
                member=member,
                trigger_type=trigger_type,
                source_event_id=event.event_id,
                effective_date=event.effective_date,
                detected_at=as_of_date,
                source_refs=event.source_ids,
                provider_names=("ExistingLedger",),
                lifecycle_status=event.lifecycle_status,
                payload={"event_type": event.event_type, "active_old_event_preserved": True},
            )
        )
    return tuple(signals)


def _signal_from_filing(
    *,
    member: LiveUniverseRow,
    filing: Mapping[str, Any],
    trigger_type: TriggerType,
    provider_names: tuple[str, ...],
    as_of_date: str,
    lifecycle_status: str,
) -> TriggerSignal:
    receipt = str(filing.get("rcept_no"))
    effective_date = str(filing.get("rcept_date") or as_of_date)
    return _new_signal(
        member=member,
        trigger_type=trigger_type,
        source_event_id="DART-RCEPT-" + receipt,
        effective_date=effective_date,
        detected_at=as_of_date,
        source_refs=("DART-RCEPT-" + receipt,),
        provider_names=provider_names,
        lifecycle_status=lifecycle_status,
        payload={
            "report_name": filing.get("report_name"),
            "corp_code": filing.get("corp_code"),
            "receipt_no": receipt,
        },
    )


def _new_signal(
    *,
    member: LiveUniverseRow,
    trigger_type: TriggerType,
    source_event_id: str,
    effective_date: str,
    detected_at: str,
    source_refs: Sequence[str],
    provider_names: Sequence[str],
    lifecycle_status: str,
    payload: Mapping[str, Any],
) -> TriggerSignal:
    identity = {
        "target": member.symbol,
        "source_event": source_event_id,
        "effective_date": effective_date,
        "trigger_type": trigger_type.value,
        "lifecycle_status": lifecycle_status,
        "providers": tuple(provider_names),
        "payload": dict(payload),
    }
    return TriggerSignal(
        trigger_signal_id="TRIG-" + stable_hash(identity)[:24],
        target_id=str(member.symbol),
        target_name=str(member.company_name),
        trigger_type=trigger_type.value,
        source_event_id=source_event_id,
        effective_date=effective_date,
        detected_at=detected_at,
        source_refs=tuple(dict.fromkeys(str(item) for item in source_refs if str(item))),
        provider_names=tuple(dict.fromkeys(str(item) for item in provider_names if str(item))),
        subject_direct=True,
        lifecycle_status=lifecycle_status,
        investigation_required=True,
        score_evidence_eligible=False,
        headline_or_snippet_only=False,
        payload=payload,
    )


def _dedupe_signals(
    raw_signals: Sequence[TriggerSignal],
) -> tuple[tuple[TriggerSignal, ...], tuple[Mapping[str, Any], ...]]:
    priority = {
        TriggerType.RISK.value: 8,
        TriggerType.EARNINGS.value: 7,
        TriggerType.REPORT.value: 6,
        TriggerType.OFFICIAL.value: 5,
        TriggerType.EXISTING_LEDGER.value: 4,
        TriggerType.IR.value: 3,
        TriggerType.NEWS.value: 2,
        TriggerType.MARKET.value: 1,
    }
    selected: dict[tuple[str, str, str], TriggerSignal] = {}
    duplicates: list[Mapping[str, Any]] = []
    for signal in sorted(
        raw_signals,
        key=lambda item: (
            item.dedupe_key,
            -priority[item.trigger_type],
            -_lifecycle_priority(item.lifecycle_status),
            item.trigger_signal_id,
        ),
    ):
        existing = selected.get(signal.dedupe_key)
        if existing is None:
            selected[signal.dedupe_key] = signal
            continue
        duplicates.append(
            {
                "dedupe_key": list(signal.dedupe_key),
                "kept_trigger_signal_id": existing.trigger_signal_id,
                "dropped_trigger_signal_id": signal.trigger_signal_id,
                "reason": "same_symbol_source_event_effective_date",
            }
        )
    return (
        tuple(
            sorted(
                selected.values(),
                key=lambda item: (
                    item.target_id,
                    item.effective_date,
                    item.source_event_id,
                    item.trigger_signal_id,
                ),
            )
        ),
        tuple(duplicates),
    )


def _candidate_events(
    signals: Sequence[TriggerSignal],
    *,
    state_by_symbol: Mapping[str, CurrentStateRecord],
    as_of_date: str,
) -> tuple[CandidateEvent, ...]:
    grouped: dict[str, list[TriggerSignal]] = {}
    for signal in signals:
        grouped.setdefault(signal.target_id, []).append(signal)
    candidates: list[CandidateEvent] = []
    for symbol, rows in sorted(grouped.items()):
        ordered = tuple(sorted(rows, key=lambda item: (item.effective_date, item.trigger_signal_id)))
        trigger_types = tuple(sorted({item.trigger_type for item in ordered}))
        signal_ids = tuple(item.trigger_signal_id for item in ordered)
        source_refs = tuple(
            dict.fromkeys(source for item in ordered for source in item.source_refs)
        )
        latest = max(item.effective_date for item in ordered)
        state = state_by_symbol.get(symbol)
        active_thesis = bool(
            state
            and any(
                event.lifecycle_status == EventLifecycleStatus.OPEN.value
                for event in state.material_events
            )
        )
        identity = {
            "target": symbol,
            "as_of_date": as_of_date,
            "signals": signal_ids,
        }
        candidates.append(
            CandidateEvent(
                candidate_event_id="CAND-" + stable_hash(identity)[:24],
                target_id=symbol,
                target_name=ordered[-1].target_name,
                as_of_date=as_of_date,
                latest_effective_date=latest,
                trigger_types=trigger_types,
                trigger_signal_ids=signal_ids,
                source_refs=source_refs,
                investigation_required=True,
                active_thesis_present=active_thesis,
                score_evidence_eligible=False,
                summary=(
                    f"{ordered[-1].target_name}: {', '.join(trigger_types)} current trigger "
                    f"{len(ordered)}건 검증 필요"
                ),
            )
        )
    return tuple(candidates)


def _audit_trigger_fusion(
    *,
    as_of_date: str,
    eligible: Sequence[LiveUniverseRow],
    lanes_by_symbol: Mapping[str, Mapping[str, BaselineLaneRecord]],
    raw_signals: Sequence[TriggerSignal],
    signals: Sequence[TriggerSignal],
    candidates: Sequence[CandidateEvent],
    full_scan_attempted: bool,
) -> dict[str, Any]:
    market_to_score = sum(
        item.trigger_type == TriggerType.MARKET.value and item.score_evidence_eligible
        for item in signals
    )
    news_snippet_to_score = sum(
        item.trigger_type == TriggerType.NEWS.value
        and item.headline_or_snippet_only
        and item.score_evidence_eligible
        for item in signals
    )
    wrong_subject = sum(not item.subject_direct for item in signals)
    without_source = sum(not item.source_refs for item in signals)
    future = sum(
        date.fromisoformat(item.effective_date) > date.fromisoformat(as_of_date)
        for item in signals
    )
    symbols_without_required_lanes = sum(
        set(lanes_by_symbol.get(str(member.symbol), {}))
        != {item.value for item in BaselineLane}
        for member in eligible
    )
    critical = {
        "full_universe_trigger_scan_not_attempted": int(not full_scan_attempted),
        "symbol_without_required_baseline_for_trigger_scan": symbols_without_required_lanes,
        "market_trigger_to_score": market_to_score,
        "news_snippet_to_score": news_snippet_to_score,
        "wrong_subject_trigger": wrong_subject,
        "trigger_without_source_ref": without_source,
        "future_trigger": future,
        "duplicate_trigger_emitted": len(signals) - len({item.dedupe_key for item in signals}),
    }
    return {
        "schema_version": "e2r_live_trigger_fusion_audit_v1",
        "as_of_date": as_of_date,
        "eligible_universe_count": len(eligible),
        "full_universe_trigger_scan_attempted": full_scan_attempted,
        "raw_trigger_signal_count": len(raw_signals),
        "trigger_signal_count": len(signals),
        "candidate_event_count": len(candidates),
        "candidate_symbol_count": len({item.target_id for item in candidates}),
        "market_trigger_to_score_count": market_to_score,
        "news_snippet_to_score_count": news_snippet_to_score,
        "wrong_subject_trigger_count": wrong_subject,
        "trigger_without_source_ref_count": without_source,
        "future_trigger_count": future,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "hard_acceptance_pass": sum(critical.values()) == 0,
    }


def _source_distribution(
    *,
    as_of_date: str,
    signals: Sequence[TriggerSignal],
) -> Mapping[str, Any]:
    by_type: dict[str, int] = {}
    by_provider: dict[str, int] = {}
    by_lifecycle: dict[str, int] = {}
    for signal in signals:
        by_type[signal.trigger_type] = by_type.get(signal.trigger_type, 0) + 1
        for provider in signal.provider_names:
            by_provider[provider] = by_provider.get(provider, 0) + 1
        by_lifecycle[signal.lifecycle_status] = by_lifecycle.get(signal.lifecycle_status, 0) + 1
    return {
        "schema_version": "e2r_live_trigger_source_distribution_v1",
        "as_of_date": as_of_date,
        "trigger_signal_count": len(signals),
        "by_trigger_type": dict(sorted(by_type.items())),
        "by_provider": dict(sorted(by_provider.items())),
        "by_lifecycle": dict(sorted(by_lifecycle.items())),
    }


def _unique_universe(rows: Sequence[LiveUniverseRow]) -> dict[str, LiveUniverseRow]:
    result: dict[str, LiveUniverseRow] = {}
    for row in rows:
        symbol = str(row.symbol or "")
        if not symbol or symbol in result:
            raise ValueError("eligible trigger universe has missing or duplicate symbol")
        result[symbol] = row
    return result


def _contains_any(value: str, tokens: Sequence[str]) -> bool:
    return any(token in value for token in tokens)


def _float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _lifecycle_priority(status: str) -> int:
    if status in {"OPEN", "OPEN_CANDIDATE", "RESOLVED", "SUPERSEDED"}:
        return 3
    if "OPEN_CANDIDATE" in status or "RESOLVED" in status:
        return 2
    return 1


__all__ = [
    "TRIGGER_SIGNAL_SCHEMA_VERSION",
    "CandidateEvent",
    "CurrentTriggerFusion",
    "TriggerFusionConfig",
    "TriggerFusionResult",
    "TriggerSignal",
    "TriggerType",
    "load_candidate_events",
    "load_trigger_signals",
    "write_trigger_fusion",
]
