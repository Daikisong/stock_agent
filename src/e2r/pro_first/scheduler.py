"""Persisted Asia/Seoul morning/evening scheduler for the existing KRX scan."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from typing import Callable, Protocol
from zoneinfo import ZoneInfo

from e2r.cheap_scan.korea_scanner import (
    KoreaCheapScanConfig,
    KoreaCheapScanner,
    KoreaCheapScanResult,
)

from .candidate_selector import ExistingDossierContext, ProCandidateSelector
from .job_store import ProFirstJobStore
from .models import ScanRunRecord, ScanWindow


SEOUL = ZoneInfo("Asia/Seoul")


class ClockProtocol(Protocol):
    def now(self) -> datetime:
        """Return one timezone-aware instant."""


class SystemClock:
    def now(self) -> datetime:
        return datetime.now(timezone.utc)


class FrozenClock:
    def __init__(self, current: datetime) -> None:
        self._current = self._validate(current)

    def now(self) -> datetime:
        return self._current

    def set(self, value: datetime) -> None:
        self._current = self._validate(value)

    def advance(self, delta: timedelta) -> None:
        self._current = self._current + delta

    @staticmethod
    def _validate(value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("clock values must be timezone-aware")
        return value


@dataclass(frozen=True)
class SchedulerWindowConfig:
    enabled: bool
    at: str

    def parsed_time(self) -> time:
        try:
            parsed = time.fromisoformat(self.at)
        except ValueError as error:
            raise ValueError("scheduler time must be HH:MM") from error
        if parsed.second or parsed.microsecond or parsed.tzinfo is not None:
            raise ValueError("scheduler time must be local HH:MM without seconds or timezone")
        return parsed


@dataclass(frozen=True)
class ProSchedulerConfig:
    timezone_name: str = "Asia/Seoul"
    morning: SchedulerWindowConfig = SchedulerWindowConfig(enabled=True, at="05:30")
    evening: SchedulerWindowConfig = SchedulerWindowConfig(enabled=True, at="18:30")

    def timezone(self) -> ZoneInfo:
        zone = ZoneInfo(self.timezone_name)
        if self.timezone_name != "Asia/Seoul":
            raise ValueError("KRX Pro scheduler timezone must remain Asia/Seoul")
        self.morning.parsed_time()
        self.evening.parsed_time()
        return zone


@dataclass(frozen=True)
class DueScanWindow:
    as_of_date: str
    scan_window: ScanWindow
    scheduled_for: str
    catchup: bool


class PersistentKrxScheduler:
    """Claims each configured KST window at most once in SQLite."""

    def __init__(
        self,
        store: ProFirstJobStore,
        *,
        clock: ClockProtocol | None = None,
        config: ProSchedulerConfig | None = None,
    ) -> None:
        self.store = store
        self.clock = clock or SystemClock()
        self.config = config or ProSchedulerConfig()
        self._timezone = self.config.timezone()

    def due_windows(self) -> tuple[DueScanWindow, ...]:
        now = self._now_local()
        definitions = (
            (ScanWindow.MORNING, self.config.morning),
            (ScanWindow.EVENING, self.config.evening),
        )
        due: list[DueScanWindow] = []
        for scan_window, window_config in definitions:
            if not window_config.enabled:
                continue
            scheduled = datetime.combine(
                now.date(), window_config.parsed_time(), tzinfo=self._timezone
            )
            if scheduled > now:
                continue
            due.append(
                DueScanWindow(
                    as_of_date=scheduled.date().isoformat(),
                    scan_window=scan_window,
                    scheduled_for=scheduled.isoformat(),
                    catchup=now > scheduled,
                )
            )
        return tuple(due)

    def claim_due_windows(self) -> tuple[ScanRunRecord, ...]:
        claimed: list[ScanRunRecord] = []
        for due in self.due_windows():
            record = self.store.claim_scan_run(
                as_of_date=due.as_of_date,
                scan_window=due.scan_window,
                scheduled_for=due.scheduled_for,
                catchup=due.catchup,
            )
            if record is not None:
                claimed.append(record)
        return tuple(claimed)

    def next_scheduled_instant(self) -> datetime:
        now = self._now_local()
        candidates: list[datetime] = []
        for config in (self.config.morning, self.config.evening):
            if not config.enabled:
                continue
            scheduled = datetime.combine(now.date(), config.parsed_time(), tzinfo=self._timezone)
            if scheduled <= now:
                scheduled += timedelta(days=1)
            candidates.append(scheduled)
        if not candidates:
            raise RuntimeError("both scheduler windows are disabled")
        return min(candidates)

    def _now_local(self) -> datetime:
        value = self.clock.now()
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("clock must return a timezone-aware datetime")
        return value.astimezone(self._timezone)


ExistingContextProvider = Callable[[str], ExistingDossierContext]
ScanConfigFactory = Callable[[date, ScanWindow], KoreaCheapScanConfig]


@dataclass(frozen=True)
class ScanPipelineReceipt:
    scan_run: ScanRunRecord
    instruments_scanned: int
    cheap_candidate_count: int
    pro_candidate_count: int
    pro_job_count: int
    rejection_counts: dict[str, int]


class KoreaScanToProQueue:
    """Connect the reused ``KoreaCheapScanner`` to the durable Pro queue."""

    def __init__(
        self,
        *,
        store: ProFirstJobStore,
        scanner: KoreaCheapScanner,
        selector: ProCandidateSelector,
        config_factory: ScanConfigFactory,
        existing_context_provider: ExistingContextProvider | None = None,
    ) -> None:
        self.store = store
        self.scanner = scanner
        self.selector = selector
        self.config_factory = config_factory
        self.existing_context_provider = existing_context_provider or (
            lambda _symbol: ExistingDossierContext()
        )

    def run_claimed_window(self, scan_run: ScanRunRecord) -> ScanPipelineReceipt:
        if scan_run.status != "CLAIMED":
            raise ValueError("scan window must be atomically claimed before execution")
        as_of_date = date.fromisoformat(scan_run.as_of_date)
        scan_window = ScanWindow(scan_run.scan_window)
        config = self.config_factory(as_of_date, scan_window)
        if config.as_of_date != as_of_date:
            raise ValueError("scan config as_of_date differs from the claimed window")
        try:
            result = self.scanner.run(config)
            receipt = self._select_enqueue_complete(scan_run, result)
        except Exception as error:
            self.store.complete_scan_run(
                scan_run.scan_run_id,
                failed=True,
                receipt={
                    "error_class": type(error).__name__,
                    "error_message": str(error),
                },
            )
            raise
        return receipt

    def _select_enqueue_complete(
        self,
        scan_run: ScanRunRecord,
        result: KoreaCheapScanResult,
    ) -> ScanPipelineReceipt:
        existing = {
            candidate.symbol: self.existing_context_provider(candidate.symbol)
            for candidate in result.candidates
        }
        batch = self.selector.select_result(
            result,
            scan_window=scan_run.scan_window,
            scan_run_id=scan_run.scan_run_id,
            existing_by_symbol=existing,
        )
        enqueued = self.selector.enqueue(self.store, batch)
        completed = self.store.complete_scan_run(
            scan_run.scan_run_id,
            receipt={
                "instruments_scanned": result.instruments_scanned,
                "cheap_candidate_count": len(result.candidates),
                "pro_candidate_count": len(batch.selected),
                "pro_job_count": sum(item.created for item in enqueued),
                "rejection_counts": batch.rejection_counts,
            },
        )
        return ScanPipelineReceipt(
            scan_run=completed,
            instruments_scanned=result.instruments_scanned,
            cheap_candidate_count=len(result.candidates),
            pro_candidate_count=len(batch.selected),
            pro_job_count=sum(item.created for item in enqueued),
            rejection_counts=dict(batch.rejection_counts),
        )


class ProFirstScheduleService:
    """Async local-service loop; durable claims make restarts idempotent."""

    def __init__(
        self,
        scheduler: PersistentKrxScheduler,
        pipeline: KoreaScanToProQueue,
        *,
        maximum_idle_poll_seconds: float = 60.0,
    ) -> None:
        if maximum_idle_poll_seconds <= 0:
            raise ValueError("maximum_idle_poll_seconds must be positive")
        self.scheduler = scheduler
        self.pipeline = pipeline
        self.maximum_idle_poll_seconds = maximum_idle_poll_seconds

    async def run_once(self) -> tuple[ScanPipelineReceipt, ...]:
        receipts: list[ScanPipelineReceipt] = []
        for scan_run in self.scheduler.claim_due_windows():
            receipt = await asyncio.to_thread(self.pipeline.run_claimed_window, scan_run)
            receipts.append(receipt)
        return tuple(receipts)

    async def run_forever(self, stop_event: asyncio.Event) -> None:
        while not stop_event.is_set():
            await self.run_once()
            now = self.scheduler.clock.now()
            next_at = self.scheduler.next_scheduled_instant()
            seconds = max(0.01, (next_at - now.astimezone(next_at.tzinfo)).total_seconds())
            timeout = min(seconds, self.maximum_idle_poll_seconds)
            try:
                await asyncio.wait_for(stop_event.wait(), timeout=timeout)
            except asyncio.TimeoutError:
                continue


__all__ = [
    "ClockProtocol",
    "DueScanWindow",
    "FrozenClock",
    "KoreaScanToProQueue",
    "PersistentKrxScheduler",
    "ProFirstScheduleService",
    "ProSchedulerConfig",
    "ScanPipelineReceipt",
    "SchedulerWindowConfig",
    "SystemClock",
]
