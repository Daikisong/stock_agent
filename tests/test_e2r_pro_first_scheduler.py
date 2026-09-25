from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from zoneinfo import ZoneInfo

from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.models import ScanWindow
from e2r.pro_first.scheduler import FrozenClock, PersistentKrxScheduler


KST = ZoneInfo("Asia/Seoul")


class ProFirstSchedulerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.clock = FrozenClock(datetime(2026, 8, 22, 5, 29, tzinfo=KST))
        self.database_path = Path(self.temporary_directory.name) / "scheduler.sqlite3"
        self.store = ProFirstJobStore(
            self.database_path,
            now=self.clock.now,
        )
        self.scheduler = PersistentKrxScheduler(self.store, clock=self.clock)

    def test_morning_schedule_kst(self) -> None:
        self.assertEqual(self.scheduler.due_windows(), ())
        self.clock.set(datetime(2026, 8, 22, 5, 30, tzinfo=KST))
        due = self.scheduler.due_windows()
        self.assertEqual(len(due), 1)
        self.assertEqual(due[0].scan_window, ScanWindow.MORNING)
        self.assertEqual(due[0].scheduled_for, "2026-08-22T05:30:00+09:00")
        self.assertFalse(due[0].catchup)

    def test_evening_schedule_kst(self) -> None:
        self.clock.set(datetime(2026, 8, 22, 5, 30, tzinfo=KST))
        morning = self.scheduler.claim_due_windows()
        self.assertEqual([item.scan_window for item in morning], [ScanWindow.MORNING.value])
        self.clock.set(datetime(2026, 8, 22, 18, 30, tzinfo=KST))
        evening = self.scheduler.claim_due_windows()
        self.assertEqual([item.scan_window for item in evening], [ScanWindow.EVENING.value])
        self.assertFalse(evening[0].catchup)

    def test_missed_window_catchup_once(self) -> None:
        self.clock.set(datetime(2026, 8, 22, 7, 0, tzinfo=KST))
        first_process = self.scheduler.claim_due_windows()
        self.assertEqual(len(first_process), 1)
        self.assertTrue(first_process[0].catchup)

        reopened_store = ProFirstJobStore(self.database_path, now=self.clock.now)
        restarted = PersistentKrxScheduler(reopened_store, clock=self.clock)
        self.assertEqual(restarted.claim_due_windows(), ())

    def test_duplicate_scan_window_blocked(self) -> None:
        self.clock.set(datetime(2026, 8, 22, 5, 30, tzinfo=KST))
        first = self.scheduler.claim_due_windows()
        second = self.scheduler.claim_due_windows()
        self.assertEqual(len(first), 1)
        self.assertEqual(second, ())
        persisted = self.store.get_scan_run_by_window("2026-08-22", ScanWindow.MORNING)
        self.assertIsNotNone(persisted)
        self.assertEqual(persisted.scan_run_id, first[0].scan_run_id)

    def test_frozen_clock(self) -> None:
        before = self.clock.now()
        self.clock.advance(timedelta(minutes=1))
        self.assertEqual(self.clock.now(), before + timedelta(minutes=1))
        self.assertEqual(
            self.scheduler.next_scheduled_instant(),
            datetime(2026, 8, 22, 18, 30, tzinfo=KST),
        )


if __name__ == "__main__":
    unittest.main()
