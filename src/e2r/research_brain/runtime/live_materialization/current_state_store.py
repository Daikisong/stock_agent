"""Versioned current-state bootstrap and source lifecycle preservation."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import date, timedelta
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl

from .universe_materializer import LiveUniverseRow


CURRENT_STATE_STORE_SCHEMA_VERSION = "e2r_current_state_store_v1"


class BootstrapCompleteness(str, Enum):
    COMPLETE = "COMPLETE"
    PARTIAL_HISTORY_PENDING = "PARTIAL_HISTORY_PENDING"
    PROVIDER_PENDING = "PROVIDER_PENDING"
    SOURCE_GAP = "SOURCE_GAP"


class SourceAttemptStatus(str, Enum):
    OBSERVED = "OBSERVED"
    NO_RESULT = "NO_RESULT"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    AUTH_FAILED = "AUTH_FAILED"
    RATE_LIMITED = "RATE_LIMITED"
    NO_PRIOR_LEDGER = "NO_PRIOR_LEDGER"
    NOT_ATTEMPTED = "NOT_ATTEMPTED"


class EventLifecycleStatus(str, Enum):
    OPEN = "OPEN"
    RESOLVED = "RESOLVED"
    SUPERSEDED = "SUPERSEDED"
    HISTORICAL_ONLY = "HISTORICAL_ONLY"
    UNKNOWN = "UNKNOWN"


class ThesisStatus(str, Enum):
    ACTIVE_THESIS = "ACTIVE_THESIS"
    NEEDS_REFRESH = "NEEDS_REFRESH"
    PARTIAL_HISTORY_PENDING = "PARTIAL_HISTORY_PENDING"
    PROVIDER_PENDING = "PROVIDER_PENDING"
    SOURCE_GAP = "SOURCE_GAP"
    NO_CURRENT_THESIS = "NO_CURRENT_THESIS"


@dataclass(frozen=True)
class CurrentStateSourceAttempt:
    attempt_id: str
    target_id: str
    provider_name: str
    source_class: str
    status: str
    observed_date: str
    source_id: str | None = None
    source_url: str | None = None
    content_hash: str | None = None
    provider_error_category: str | None = None

    def __post_init__(self) -> None:
        SourceAttemptStatus(self.status)
        date.fromisoformat(self.observed_date)
        if not all((self.attempt_id.strip(), self.target_id.strip(), self.provider_name.strip())):
            raise ValueError("current-state source attempt identity required")
        if self.status == SourceAttemptStatus.OBSERVED.value and not self.source_id:
            raise ValueError("observed source attempt requires source ID")
        if self.status in {
            SourceAttemptStatus.PROVIDER_FAILED.value,
            SourceAttemptStatus.AUTH_FAILED.value,
            SourceAttemptStatus.RATE_LIMITED.value,
        } and not self.provider_error_category:
            raise ValueError("provider failure attempt requires error category")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CurrentStateEvent:
    event_id: str
    target_id: str
    event_type: str
    effective_date: str
    lifecycle_status: str
    source_ids: tuple[str, ...]
    end_date: str | None = None
    resolved_date: str | None = None
    superseded_by_event_id: str | None = None
    target_direct: bool = True
    source_backed: bool = True
    material: bool = True
    score_eligible: bool = False

    def __post_init__(self) -> None:
        EventLifecycleStatus(self.lifecycle_status)
        date.fromisoformat(self.effective_date)
        if self.end_date:
            date.fromisoformat(self.end_date)
        if self.resolved_date:
            date.fromisoformat(self.resolved_date)
        if not all((self.event_id.strip(), self.target_id.strip(), self.event_type.strip())):
            raise ValueError("current-state event identity required")
        if not self.source_ids:
            raise ValueError("current-state event requires source lineage")
        expected_score_eligible = (
            self.lifecycle_status == EventLifecycleStatus.OPEN.value
            and self.target_direct
            and self.source_backed
            and self.material
        )
        if self.score_eligible != expected_score_eligible:
            raise ValueError("current-state event score eligibility/lifecycle mismatch")

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["source_ids"] = list(self.source_ids)
        return payload


@dataclass(frozen=True)
class CurrentStateRecord:
    target_id: str
    target_name: str
    market: str
    as_of_date: str
    universe_source_ids: tuple[str, ...]
    source_attempts: tuple[CurrentStateSourceAttempt, ...]
    material_events: tuple[CurrentStateEvent, ...]
    accepted_current_claim_ids: tuple[str, ...]
    historical_only_claim_ids: tuple[str, ...]
    pending_source_task_ids: tuple[str, ...]
    last_effective_thesis_status: str
    last_effective_event_id: str | None
    bootstrap_completeness: str
    last_updated_source_corpus_hash: str
    schema_version: str = CURRENT_STATE_STORE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        BootstrapCompleteness(self.bootstrap_completeness)
        ThesisStatus(self.last_effective_thesis_status)
        if not all((self.target_id.strip(), self.target_name.strip(), self.market.strip())):
            raise ValueError("current-state target identity required")
        if not self.universe_source_ids or not self.source_attempts:
            raise ValueError("current-state record requires universe and source attempts")
        if any(attempt.target_id != self.target_id for attempt in self.source_attempts):
            raise ValueError("current-state source attempt target mismatch")
        if any(event.target_id != self.target_id for event in self.material_events):
            raise ValueError("current-state event target mismatch")

    def to_dict(self) -> dict[str, Any]:
        return {
            **asdict(self),
            "universe_source_ids": list(self.universe_source_ids),
            "source_attempts": [item.to_dict() for item in self.source_attempts],
            "material_events": [item.to_dict() for item in self.material_events],
            "accepted_current_claim_ids": list(self.accepted_current_claim_ids),
            "historical_only_claim_ids": list(self.historical_only_claim_ids),
            "pending_source_task_ids": list(self.pending_source_task_ids),
        }


@dataclass(frozen=True)
class CurrentStateBootstrapResult:
    as_of_date: str
    status: str
    records: tuple[CurrentStateRecord, ...]
    source_timelines: tuple[Mapping[str, Any], ...]
    last_effective_theses: tuple[Mapping[str, Any], ...]
    source_corpus_hash: str
    audit: Mapping[str, Any]

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if len(self.records) != len(self.source_timelines) or len(self.records) != len(
            self.last_effective_theses
        ):
            raise ValueError("current-state bootstrap leaf count mismatch")


class CurrentStateBootstrapper:
    def bootstrap(
        self,
        *,
        as_of_date: str,
        universe: Sequence[LiveUniverseRow],
        prior_records: Sequence[CurrentStateRecord] = (),
        discovered_events: Sequence[CurrentStateEvent] = (),
        provider_attempts_by_target: Mapping[
            str, Sequence[CurrentStateSourceAttempt]
        ] | None = None,
        history_complete_target_ids: Sequence[str] = (),
    ) -> CurrentStateBootstrapResult:
        as_of = date.fromisoformat(as_of_date)
        eligible = tuple(row for row in universe if row.eligible)
        if not eligible:
            raise ValueError("current-state bootstrap requires eligible universe")
        by_symbol = _unique_by_target(eligible)
        prior_by_target = {record.target_id: record for record in prior_records}
        if len(prior_by_target) != len(prior_records):
            raise ValueError("duplicate prior current-state target")
        events_by_target: dict[str, list[CurrentStateEvent]] = {}
        for event in discovered_events:
            if event.target_id not in by_symbol:
                continue
            if date.fromisoformat(event.effective_date) > as_of:
                raise ValueError("future event entered current-state bootstrap")
            events_by_target.setdefault(event.target_id, []).append(
                refresh_event_lifecycle(event, as_of_date=as_of_date)
            )
        complete_ids = set(history_complete_target_ids)
        attempts_map = provider_attempts_by_target or {}
        records: list[CurrentStateRecord] = []
        for target_id, member in sorted(by_symbol.items()):
            prior = prior_by_target.get(target_id)
            events = _merge_events(
                prior.material_events if prior else (),
                events_by_target.get(target_id, ()),
                as_of_date=as_of_date,
            )
            attempts = (
                _universe_attempt(member, as_of_date=as_of_date),
                _ledger_attempt(member, prior=prior, as_of_date=as_of_date),
                *tuple(attempts_map.get(target_id, ())),
            )
            provider_pending = any(
                item.status
                in {
                    SourceAttemptStatus.PROVIDER_FAILED.value,
                    SourceAttemptStatus.AUTH_FAILED.value,
                    SourceAttemptStatus.RATE_LIMITED.value,
                }
                for item in attempts
            )
            completeness = (
                BootstrapCompleteness.PROVIDER_PENDING.value
                if provider_pending
                else BootstrapCompleteness.COMPLETE.value
                if target_id in complete_ids
                else BootstrapCompleteness.PARTIAL_HISTORY_PENDING.value
            )
            thesis_status, last_event_id = _last_effective_thesis(
                events,
                completeness=completeness,
            )
            accepted_ids = tuple(prior.accepted_current_claim_ids) if prior else ()
            historical_ids = tuple(prior.historical_only_claim_ids) if prior else ()
            pending_task_ids = tuple(prior.pending_source_task_ids) if prior else ()
            corpus_hash = stable_hash(
                {
                    "universe": member.to_dict(),
                    "attempts": [attempt.to_dict() for attempt in attempts],
                    "events": [event.to_dict() for event in events],
                    "accepted_current_claim_ids": accepted_ids,
                    "historical_only_claim_ids": historical_ids,
                }
            )
            records.append(
                CurrentStateRecord(
                    target_id=target_id,
                    target_name=str(member.company_name),
                    market=member.market,
                    as_of_date=as_of_date,
                    universe_source_ids=(member.source_document_id,),
                    source_attempts=tuple(attempts),
                    material_events=events,
                    accepted_current_claim_ids=accepted_ids,
                    historical_only_claim_ids=historical_ids,
                    pending_source_task_ids=pending_task_ids,
                    last_effective_thesis_status=thesis_status,
                    last_effective_event_id=last_event_id,
                    bootstrap_completeness=completeness,
                    last_updated_source_corpus_hash=corpus_hash,
                )
            )
        source_timelines = tuple(_timeline(record) for record in records)
        theses = tuple(_thesis(record) for record in records)
        audit = _audit_bootstrap(
            as_of_date=as_of_date,
            records=tuple(records),
            input_events=tuple(discovered_events),
        )
        return CurrentStateBootstrapResult(
            as_of_date=as_of_date,
            status=(
                "CURRENT_STATE_BOOTSTRAP_PASS"
                if audit["hard_acceptance_pass"]
                else "CURRENT_STATE_BOOTSTRAP_FAIL"
            ),
            records=tuple(records),
            source_timelines=source_timelines,
            last_effective_theses=theses,
            source_corpus_hash=stable_hash(
                [record.last_updated_source_corpus_hash for record in records]
            ),
            audit=audit,
        )


def refresh_event_lifecycle(
    event: CurrentStateEvent,
    *,
    as_of_date: str,
) -> CurrentStateEvent:
    as_of = date.fromisoformat(as_of_date)
    effective = date.fromisoformat(event.effective_date)
    if effective > as_of:
        raise ValueError("future event cannot be lifecycle-refreshed")
    status = EventLifecycleStatus(event.lifecycle_status)
    if event.superseded_by_event_id:
        status = EventLifecycleStatus.SUPERSEDED
    elif event.resolved_date and date.fromisoformat(event.resolved_date) <= as_of:
        status = EventLifecycleStatus.RESOLVED
    elif event.end_date and date.fromisoformat(event.end_date) < as_of:
        status = EventLifecycleStatus.RESOLVED
    elif status in {EventLifecycleStatus.RESOLVED, EventLifecycleStatus.SUPERSEDED}:
        status = status
    elif event.event_type in {
        "SUPPLY_CONTRACT",
        "FACILITY_INVESTMENT",
        "RISK",
        "FINANCING",
    }:
        status = EventLifecycleStatus.OPEN
    return CurrentStateEvent(
        event_id=event.event_id,
        target_id=event.target_id,
        event_type=event.event_type,
        effective_date=event.effective_date,
        lifecycle_status=status.value,
        source_ids=event.source_ids,
        end_date=event.end_date,
        resolved_date=event.resolved_date,
        superseded_by_event_id=event.superseded_by_event_id,
        target_direct=event.target_direct,
        source_backed=event.source_backed,
        material=event.material,
        score_eligible=(
            status == EventLifecycleStatus.OPEN
            and event.target_direct
            and event.source_backed
            and event.material
        ),
    )


def write_current_state_bootstrap(
    result: CurrentStateBootstrapResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "store": root / "current_state_store.jsonl",
        "timelines": root / "source_timelines.jsonl",
        "theses": root / "last_effective_thesis.jsonl",
        "completeness": root / "bootstrap_completeness.json",
    }
    write_jsonl(paths["store"], (record.to_dict() for record in result.records))
    write_jsonl(paths["timelines"], result.source_timelines)
    write_jsonl(paths["theses"], result.last_effective_theses)
    write_json(
        paths["completeness"],
        {
            **dict(result.audit),
            "status": result.status,
            "source_corpus_hash": result.source_corpus_hash,
        },
    )
    return paths


def load_current_state_store(path: str | Path) -> tuple[CurrentStateRecord, ...]:
    """Load the versioned leaf store without weakening nested schema checks."""

    source = Path(path)
    if not source.is_file():
        return ()
    records: list[CurrentStateRecord] = []
    with source.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
                attempts = tuple(
                    CurrentStateSourceAttempt(**dict(item))
                    for item in payload.pop("source_attempts")
                )
                events = tuple(
                    CurrentStateEvent(
                        **{
                            **dict(item),
                            "source_ids": tuple(item.get("source_ids") or ()),
                        }
                    )
                    for item in payload.pop("material_events")
                )
                universe_source_ids = tuple(payload.pop("universe_source_ids"))
                accepted_current_claim_ids = tuple(
                    payload.pop("accepted_current_claim_ids")
                )
                historical_only_claim_ids = tuple(
                    payload.pop("historical_only_claim_ids")
                )
                pending_source_task_ids = tuple(
                    payload.pop("pending_source_task_ids")
                )
                records.append(
                    CurrentStateRecord(
                        **payload,
                        universe_source_ids=universe_source_ids,
                        source_attempts=attempts,
                        material_events=events,
                        accepted_current_claim_ids=accepted_current_claim_ids,
                        historical_only_claim_ids=historical_only_claim_ids,
                        pending_source_task_ids=pending_source_task_ids,
                    )
                )
            except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
                raise ValueError(
                    f"invalid current-state store row at line {line_number}: {exc}"
                ) from exc
    if len({record.target_id for record in records}) != len(records):
        raise ValueError("duplicate target in current-state store")
    return tuple(records)


def _merge_events(
    prior: Sequence[CurrentStateEvent],
    discovered: Sequence[CurrentStateEvent],
    *,
    as_of_date: str,
) -> tuple[CurrentStateEvent, ...]:
    by_id = {event.event_id: refresh_event_lifecycle(event, as_of_date=as_of_date) for event in prior}
    for event in discovered:
        by_id[event.event_id] = refresh_event_lifecycle(event, as_of_date=as_of_date)
    regular = sorted(
        (event for event in by_id.values() if event.event_type == "REGULAR_REPORT"),
        key=lambda item: (item.effective_date, item.event_id),
    )
    if regular:
        latest_id = regular[-1].event_id
        for event in regular[:-1]:
            by_id[event.event_id] = CurrentStateEvent(
                **{
                    **event.to_dict(),
                    "source_ids": tuple(event.source_ids),
                    "lifecycle_status": EventLifecycleStatus.SUPERSEDED.value,
                    "superseded_by_event_id": latest_id,
                    "score_eligible": False,
                }
            )
    return tuple(sorted(by_id.values(), key=lambda item: (item.effective_date, item.event_id)))


def _last_effective_thesis(
    events: Sequence[CurrentStateEvent],
    *,
    completeness: str,
) -> tuple[str, str | None]:
    active = [event for event in events if event.lifecycle_status == EventLifecycleStatus.OPEN.value]
    if active:
        latest = max(active, key=lambda item: (item.effective_date, item.event_id))
        return ThesisStatus.ACTIVE_THESIS.value, latest.event_id
    if completeness == BootstrapCompleteness.PROVIDER_PENDING.value:
        return ThesisStatus.PROVIDER_PENDING.value, None
    if completeness == BootstrapCompleteness.PARTIAL_HISTORY_PENDING.value:
        return ThesisStatus.PARTIAL_HISTORY_PENDING.value, None
    if completeness == BootstrapCompleteness.SOURCE_GAP.value:
        return ThesisStatus.SOURCE_GAP.value, None
    return ThesisStatus.NO_CURRENT_THESIS.value, None


def _universe_attempt(
    member: LiveUniverseRow,
    *,
    as_of_date: str,
) -> CurrentStateSourceAttempt:
    return CurrentStateSourceAttempt(
        attempt_id="STATEATTEMPT-"
        + stable_hash({"target": member.symbol, "source": member.source_document_id})[:24],
        target_id=str(member.symbol),
        provider_name="KRX",
        source_class="UNIVERSE",
        status=SourceAttemptStatus.OBSERVED.value,
        observed_date=as_of_date,
        source_id=member.source_document_id,
        source_url=member.source_url,
        content_hash=member.source_content_hash,
    )


def _ledger_attempt(
    member: LiveUniverseRow,
    *,
    prior: CurrentStateRecord | None,
    as_of_date: str,
) -> CurrentStateSourceAttempt:
    source_id = f"current-state-ledger:{member.symbol}" if prior else None
    return CurrentStateSourceAttempt(
        attempt_id="STATEATTEMPT-"
        + stable_hash({"target": member.symbol, "provider": "ExistingLedger"})[:24],
        target_id=str(member.symbol),
        provider_name="ExistingLedger",
        source_class="EXISTING_LEDGER",
        status=(
            SourceAttemptStatus.OBSERVED.value
            if prior
            else SourceAttemptStatus.NO_PRIOR_LEDGER.value
        ),
        observed_date=as_of_date,
        source_id=source_id,
    )


def _timeline(record: CurrentStateRecord) -> Mapping[str, Any]:
    return {
        "schema_version": "e2r_current_state_source_timeline_v1",
        "target_id": record.target_id,
        "as_of_date": record.as_of_date,
        "source_attempt_ids": [item.attempt_id for item in record.source_attempts],
        "event_ids": [item.event_id for item in record.material_events],
        "active_event_ids": [
            item.event_id
            for item in record.material_events
            if item.lifecycle_status == EventLifecycleStatus.OPEN.value
        ],
        "bootstrap_completeness": record.bootstrap_completeness,
        "source_corpus_hash": record.last_updated_source_corpus_hash,
    }


def _thesis(record: CurrentStateRecord) -> Mapping[str, Any]:
    return {
        "schema_version": "e2r_current_state_last_effective_thesis_v1",
        "target_id": record.target_id,
        "as_of_date": record.as_of_date,
        "thesis_status": record.last_effective_thesis_status,
        "last_effective_event_id": record.last_effective_event_id,
        "accepted_current_claim_ids": list(record.accepted_current_claim_ids),
        "pending_source_task_ids": list(record.pending_source_task_ids),
        "bootstrap_completeness": record.bootstrap_completeness,
    }


def _audit_bootstrap(
    *,
    as_of_date: str,
    records: Sequence[CurrentStateRecord],
    input_events: Sequence[CurrentStateEvent],
) -> dict[str, Any]:
    as_of = date.fromisoformat(as_of_date)
    old_boundary = as_of - timedelta(days=365)
    record_by_target = {record.target_id: record for record in records}
    old_active = [
        event
        for event in input_events
        if date.fromisoformat(event.effective_date) < old_boundary
        and refresh_event_lifecycle(event, as_of_date=as_of_date).lifecycle_status
        == EventLifecycleStatus.OPEN.value
    ]
    dropped_old_active = sum(
        not any(
            candidate.event_id == event.event_id
            and candidate.lifecycle_status == EventLifecycleStatus.OPEN.value
            for candidate in record_by_target.get(event.target_id, _EMPTY_RECORD).material_events
        )
        for event in old_active
    )
    resolved_risk_scored = sum(
        event.event_type == "RISK"
        and event.lifecycle_status == EventLifecycleStatus.RESOLVED.value
        and event.score_eligible
        for record in records
        for event in record.material_events
    )
    provider_failure_no_thesis = sum(
        any(
            attempt.status
            in {
                SourceAttemptStatus.PROVIDER_FAILED.value,
                SourceAttemptStatus.AUTH_FAILED.value,
                SourceAttemptStatus.RATE_LIMITED.value,
            }
            for attempt in record.source_attempts
        )
        and record.last_effective_thesis_status == ThesisStatus.NO_CURRENT_THESIS.value
        for record in records
    )
    completeness_counts: dict[str, int] = {}
    for record in records:
        completeness_counts[record.bootstrap_completeness] = (
            completeness_counts.get(record.bootstrap_completeness, 0) + 1
        )
    critical = {
        "source_timeline_count_mismatch": 0,
        "last_effective_thesis_count_mismatch": 0,
        "symbol_without_any_source_attempt": sum(not record.source_attempts for record in records),
        "recent_window_used_as_stage_cutoff": 0,
        "old_active_contract_dropped": dropped_old_active,
        "old_resolved_risk_scored": resolved_risk_scored,
        "provider_failure_mapped_no_thesis": provider_failure_no_thesis,
    }
    return {
        "schema_version": "e2r_live_current_state_bootstrap_audit_v1",
        "as_of_date": as_of_date,
        "eligible_universe_count": len(records),
        "current_state_record_count": len(records),
        "source_timeline_count": len(records),
        "last_effective_thesis_count": len(records),
        "symbol_without_any_source_attempt_count": critical[
            "symbol_without_any_source_attempt"
        ],
        "recent_window_used_as_stage_cutoff_count": 0,
        "old_active_contract_dropped_count": dropped_old_active,
        "old_resolved_risk_scored_count": resolved_risk_scored,
        "provider_failure_mapped_no_thesis_count": provider_failure_no_thesis,
        "bootstrap_completeness_counts": dict(sorted(completeness_counts.items())),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "hard_acceptance_pass": sum(critical.values()) == 0,
    }


def _unique_by_target(rows: Sequence[LiveUniverseRow]) -> dict[str, LiveUniverseRow]:
    result: dict[str, LiveUniverseRow] = {}
    for row in rows:
        if not row.symbol:
            raise ValueError("eligible universe row missing target")
        if row.symbol in result:
            raise ValueError("duplicate eligible universe target")
        result[row.symbol] = row
    return result


_EMPTY_RECORD = CurrentStateRecord(
    target_id="EMPTY",
    target_name="EMPTY",
    market="EMPTY",
    as_of_date="1970-01-01",
    universe_source_ids=("EMPTY",),
    source_attempts=(
        CurrentStateSourceAttempt(
            attempt_id="EMPTY",
            target_id="EMPTY",
            provider_name="EMPTY",
            source_class="EMPTY",
            status=SourceAttemptStatus.NO_PRIOR_LEDGER.value,
            observed_date="1970-01-01",
        ),
    ),
    material_events=(),
    accepted_current_claim_ids=(),
    historical_only_claim_ids=(),
    pending_source_task_ids=(),
    last_effective_thesis_status=ThesisStatus.NO_CURRENT_THESIS.value,
    last_effective_event_id=None,
    bootstrap_completeness=BootstrapCompleteness.COMPLETE.value,
    last_updated_source_corpus_hash="EMPTY",
)


__all__ = [
    "CURRENT_STATE_STORE_SCHEMA_VERSION",
    "BootstrapCompleteness",
    "CurrentStateBootstrapResult",
    "CurrentStateBootstrapper",
    "CurrentStateEvent",
    "CurrentStateRecord",
    "CurrentStateSourceAttempt",
    "EventLifecycleStatus",
    "SourceAttemptStatus",
    "ThesisStatus",
    "refresh_event_lifecycle",
    "load_current_state_store",
    "write_current_state_bootstrap",
]
