from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.pro_first.job_store import (
    ApprovalInvalid,
    DuplicateSubmitBlocked,
    ProFirstJobStore,
    VersionConflict,
)
from e2r.pro_first.models import JobStatus, ResearchMode, ScanWindow
from e2r.pro_first.schemas import (
    PRO_FIRST_TABLES,
    PRO_JOB_EVENT_REQUIRED_FIELDS,
    PRO_RESEARCH_JOB_REQUIRED_FIELDS,
)
from e2r.pro_first.state_machine import (
    InvalidJobTransition,
    NoProgressDetected,
    ProgressSnapshot,
    TransitionContext,
)


class ProFirstStateMachineTest(unittest.TestCase):
    prompt_hash = "b" * 64
    approval_expires_at = "2026-08-23T01:02:03Z"

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.store = ProFirstJobStore(
            Path(self.temporary_directory.name) / "pro-first.sqlite3",
            now=lambda: datetime(2026, 8, 22, 1, 2, 3, tzinfo=timezone.utc),
        )
        candidate = self.store.create_candidate(
            symbol="123456",
            company_name="검증기업",
            as_of_date="2026-08-22",
            scan_window=ScanWindow.MORNING,
            trigger_fingerprint="trigger-001",
            research_mode=ResearchMode.FULL_RESEARCH,
            selection_receipt={"production_deep_candidate": True},
        )
        self.job = self.store.create_job(
            candidate.candidate_id,
            archetype_ids=("C06",),
            priority=10,
        )

    def _transition(
        self,
        status: JobStatus,
        key: str,
        *,
        context: TransitionContext | None = None,
        updates: dict[str, object] | None = None,
    ):
        self.job = self.store.transition(
            self.job.job_id,
            expected_version=self.job.state_version,
            to_status=status,
            actor="unit-worker",
            idempotency_key=key,
            context=context,
            updates=updates,
        )
        return self.job

    def _reach_approval(self) -> str:
        self._transition(JobStatus.PACKET_BUILDING, "packet-building")
        self.job = self.store.record_packet(
            self.job.job_id,
            expected_version=self.job.state_version,
            packet_id="packet-1",
            packet_hash="a" * 64,
            manifest={"packet_hash": "a" * 64},
            actor="unit-worker",
            idempotency_key="packet-ready",
        )
        self._transition(JobStatus.BROWSER_PREPARING, "browser-preparing")
        self.job = self.store.record_browser_prepared(
            self.job.job_id,
            expected_version=self.job.state_version,
            browser_session_id="browser-session-1",
            conversation_id="conversation-1",
            adapter_name="UnitBrowserAdapter",
            packet_hash="a" * 64,
            prompt_hash=self.prompt_hash,
            state={"state": JobStatus.AWAITING_USER_APPROVAL.value},
            actor="unit-worker",
            idempotency_key="approval-wait",
        )
        self.job, nonce = self.store.issue_approval_nonce(
            self.job.job_id,
            expected_version=self.job.state_version,
            actor="approval-service",
            idempotency_key="nonce-issued",
            prompt_hash=self.prompt_hash,
            expires_at=self.approval_expires_at,
        )
        return nonce

    def _approve(self) -> None:
        nonce = self._reach_approval()
        self.job = self.store.consume_approval_nonce(
            self.job.job_id,
            nonce,
            expected_version=self.job.state_version,
            actor="user",
            idempotency_key="nonce-consumed",
            prompt_hash=self.prompt_hash,
        )

    def test_job_state_transition_happy_path(self) -> None:
        self._approve()
        self.job = self.store.claim_submit(
            self.job.job_id,
            expected_version=self.job.state_version,
            actor="browser-worker",
            idempotency_key="submit-claimed",
        )
        self._transition(JobStatus.RESEARCH_RUNNING, "research-running")
        self._transition(JobStatus.RESULT_DETECTED, "result-detected")
        self._transition(JobStatus.CAPTURING_ARTIFACTS, "capturing")
        self._transition(
            JobStatus.CAPTURE_COMPLETE,
            "capture-complete",
            updates={"capture_count": 1, "research_completed_at": "2026-08-22T01:02:03Z"},
        )
        self._transition(
            JobStatus.IMPORTING,
            "importing",
            context=TransitionContext(capture_receipt_verified=True),
        )
        self._transition(
            JobStatus.DOSSIER_IMPORTED,
            "dossier-imported",
            context=TransitionContext(dossier_validated=True),
            updates={"dossier_id": "dossier-1"},
        )
        self._transition(JobStatus.VERIFYING_SOURCES, "verifying")
        self._transition(
            JobStatus.GAP_ADJUDICATION,
            "gap-adjudication",
            context=TransitionContext(source_verification_complete=True),
        )
        self._transition(JobStatus.COMPONENT_RESEARCH, "component-research")
        self._transition(
            JobStatus.JUDGING,
            "judging",
            context=TransitionContext(component_coverage_complete=True),
        )
        self._transition(
            JobStatus.SCORING,
            "scoring",
            context=TransitionContext(judge_coverage_complete=True),
        )
        self._transition(
            JobStatus.STAGECOURT,
            "stagecourt",
            context=TransitionContext(deterministic_score_present=True),
            updates={"score_receipt_id": "score-1"},
        )
        self._transition(
            JobStatus.FINAL,
            "final",
            context=TransitionContext(deterministic_stagecourt_present=True),
            updates={"stagecourt_receipt_id": "stagecourt-1"},
        )

        self.assertEqual(self.job.status, JobStatus.FINAL.value)
        self.assertEqual(self.job.submit_count, 1)
        self.assertEqual(self.job.capture_count, 1)
        self.assertEqual(len(self.store.list_events(self.job.job_id)), 21)

    def test_submit_requires_approval(self) -> None:
        self._reach_approval()
        with self.assertRaises(InvalidJobTransition):
            self.store.transition(
                self.job.job_id,
                expected_version=self.job.state_version,
                to_status=JobStatus.SUBMITTING,
                actor="browser-worker",
                idempotency_key="illegal-submit",
            )

    def test_approval_nonce_single_use(self) -> None:
        nonce = self._reach_approval()
        self.job = self.store.consume_approval_nonce(
            self.job.job_id,
            nonce,
            expected_version=self.job.state_version,
            actor="user",
            idempotency_key="first-consume",
            prompt_hash=self.prompt_hash,
        )
        with self.assertRaises(ApprovalInvalid):
            self.store.consume_approval_nonce(
                self.job.job_id,
                nonce,
                expected_version=self.job.state_version,
                actor="user",
                idempotency_key="second-consume",
                prompt_hash=self.prompt_hash,
            )

    def test_duplicate_submit_blocked(self) -> None:
        self._approve()
        self.job = self.store.claim_submit(
            self.job.job_id,
            expected_version=self.job.state_version,
            actor="browser-worker",
            idempotency_key="first-submit",
        )
        with self.assertRaises(DuplicateSubmitBlocked):
            self.store.claim_submit(
                self.job.job_id,
                expected_version=self.job.state_version,
                actor="browser-worker",
                idempotency_key="second-submit",
            )
        self.assertEqual(self.store.get_job(self.job.job_id).submit_count, 1)

    def test_capture_event_idempotent(self) -> None:
        self._approve()
        self.job = self.store.claim_submit(
            self.job.job_id,
            expected_version=self.job.state_version,
            actor="browser-worker",
            idempotency_key="submit",
        )
        self._transition(JobStatus.RESEARCH_RUNNING, "running")
        self._transition(JobStatus.RESULT_DETECTED, "detected")
        original_version = self.job.state_version
        first = self.store.transition(
            self.job.job_id,
            expected_version=original_version,
            to_status=JobStatus.CAPTURING_ARTIFACTS,
            actor="capture-worker",
            idempotency_key="capture-start-once",
            payload={"turn": "turn-1"},
        )
        second = self.store.transition(
            self.job.job_id,
            expected_version=original_version,
            to_status=JobStatus.CAPTURING_ARTIFACTS,
            actor="capture-worker",
            idempotency_key="capture-start-once",
            payload={"turn": "turn-1"},
        )
        matching = [
            event
            for event in self.store.list_events(self.job.job_id)
            if event.idempotency_key == "capture-start-once"
        ]
        self.assertEqual(first.state_version, second.state_version)
        self.assertEqual(len(matching), 1)

    def test_no_progress_hash_stops_loop(self) -> None:
        self._transition(JobStatus.PACKET_BUILDING, "packet-building")
        snapshot = ProgressSnapshot(status=JobStatus.PACKET_BUILDING.value)
        self.job = self.store.observe_progress(
            self.job.job_id,
            snapshot,
            expected_version=self.job.state_version,
            actor="packet-worker",
            idempotency_key="progress-1",
        )
        with self.assertRaises(NoProgressDetected):
            self.store.observe_progress(
                self.job.job_id,
                snapshot,
                expected_version=self.job.state_version,
                actor="packet-worker",
                idempotency_key="progress-2",
            )
        blocked = self.store.get_job(self.job.job_id)
        self.assertEqual(blocked.status, JobStatus.BLOCKED.value)
        self.assertEqual(blocked.last_error_class, "NO_PROGRESS_DETECTED")

    def test_invalid_transition_rejected(self) -> None:
        with self.assertRaises(InvalidJobTransition):
            self._transition(JobStatus.RESEARCH_RUNNING, "skip-packet-and-approval")
        unchanged = self.store.get_job(self.job.job_id)
        self.assertEqual(unchanged.status, JobStatus.CANDIDATE_SELECTED.value)
        self.assertEqual(unchanged.state_version, 0)

    def test_optimistic_version_conflict_does_not_overwrite(self) -> None:
        self._transition(JobStatus.PACKET_BUILDING, "first-writer")
        with self.assertRaises(VersionConflict):
            self.store.transition(
                self.job.job_id,
                expected_version=0,
                to_status=JobStatus.PACKET_READY,
                actor="stale-worker",
                idempotency_key="stale-write",
            )
        current = self.store.get_job(self.job.job_id)
        self.assertEqual(current.status, JobStatus.PACKET_BUILDING.value)
        self.assertEqual(current.state_version, 1)

    def test_sqlite_durability_pragmas_and_required_tables(self) -> None:
        self.assertEqual(
            self.store.pragma_snapshot(),
            {"journal_mode": "wal", "foreign_keys": 1, "busy_timeout": 5000},
        )
        with self.store._connect() as connection:
            tables = {
                row[0]
                for row in connection.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'pro_%'"
                )
            }
        self.assertEqual(
            tables,
            PRO_FIRST_TABLES,
        )
        with self.store._connect() as connection:
            job_columns = {
                row[1] for row in connection.execute("PRAGMA table_info(pro_research_jobs)")
            }
            event_columns = {
                row[1] for row in connection.execute("PRAGMA table_info(pro_job_events)")
            }
        self.assertTrue(set(PRO_RESEARCH_JOB_REQUIRED_FIELDS).issubset(job_columns))
        self.assertTrue(set(PRO_JOB_EVENT_REQUIRED_FIELDS).issubset(event_columns))

    def test_approval_is_bound_to_prompt_packet_and_browser_session(self) -> None:
        nonce = self._reach_approval()
        with self.assertRaisesRegex(ApprovalInvalid, "prompt hash changed"):
            self.store.consume_approval_nonce(
                self.job.job_id,
                nonce,
                expected_version=self.job.state_version,
                actor="user",
                idempotency_key="wrong-prompt",
                prompt_hash="c" * 64,
            )
        current = self.store.get_job(self.job.job_id)
        self.assertEqual(current.status, JobStatus.AWAITING_USER_APPROVAL.value)
        self.assertIsNone(current.approval_consumed_at)

    def test_event_ledger_is_append_only(self) -> None:
        event_id = self.store.list_events(self.job.job_id)[0].event_id
        with self.assertRaisesRegex(Exception, "append-only"):
            with self.store._transaction() as connection:
                connection.execute(
                    "UPDATE pro_job_events SET actor='tampered' WHERE event_id=?",
                    (event_id,),
                )
        with self.assertRaisesRegex(Exception, "append-only"):
            with self.store._transaction() as connection:
                connection.execute("DELETE FROM pro_job_events WHERE event_id=?", (event_id,))


if __name__ == "__main__":
    unittest.main()
