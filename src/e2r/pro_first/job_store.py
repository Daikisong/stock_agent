"""Durable SQLite ledger for Pro-first research jobs.

Every status change is guarded by an optimistic ``state_version`` predicate and
written to an append-only, idempotent event ledger in the same transaction.
"""

from __future__ import annotations

from contextlib import closing, contextmanager
from datetime import datetime, timezone
import hashlib
import hmac
import json
from pathlib import Path
import re
import secrets
import sqlite3
from typing import Any, Callable, Iterator, Mapping, Sequence

from .ids import canonical_hash, canonical_json, stable_id
from .models import (
    CandidateRecord,
    JobEvent,
    JobStatus,
    ProResearchJob,
    ResearchMode,
    ScanRunRecord,
    ScanWindow,
)
from .schemas import PRO_V2_MULTI_PASS_SCHEMA
from .state_machine import NoProgressDetected, ProgressSnapshot, ProJobStateMachine, TransitionContext


class ProFirstStoreError(RuntimeError):
    """Base error for durable ledger operations."""


class RecordNotFound(ProFirstStoreError):
    pass


class VersionConflict(ProFirstStoreError):
    pass


class IdempotencyConflict(ProFirstStoreError):
    pass


class ApprovalInvalid(ProFirstStoreError):
    pass


class DuplicateSubmitBlocked(ProFirstStoreError):
    pass


_JOB_MUTABLE_COLUMNS = frozenset(
    {
        "packet_id",
        "packet_hash",
        "browser_session_id",
        "conversation_id",
        "capture_count",
        "dossier_id",
        "score_receipt_id",
        "stagecourt_receipt_id",
        "research_completed_at",
        "published_at",
        "last_error_class",
        "last_error_message",
    }
)


_SCHEMA = """
CREATE TABLE IF NOT EXISTS pro_scan_runs (
    scan_run_id TEXT PRIMARY KEY,
    as_of_date TEXT NOT NULL,
    scan_window TEXT NOT NULL,
    window_key TEXT NOT NULL UNIQUE,
    status TEXT NOT NULL,
    scheduled_for TEXT NOT NULL,
    catchup INTEGER NOT NULL CHECK (catchup IN (0, 1)),
    receipt_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    completed_at TEXT
);

CREATE TABLE IF NOT EXISTS pro_candidates (
    candidate_id TEXT PRIMARY KEY,
    scan_run_id TEXT REFERENCES pro_scan_runs(scan_run_id),
    symbol TEXT NOT NULL,
    company_name TEXT NOT NULL,
    as_of_date TEXT NOT NULL,
    scan_window TEXT NOT NULL,
    trigger_fingerprint TEXT NOT NULL,
    research_mode TEXT NOT NULL,
    dedupe_key TEXT NOT NULL UNIQUE,
    selection_receipt_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pro_research_jobs (
    job_id TEXT PRIMARY KEY,
    candidate_id TEXT NOT NULL UNIQUE REFERENCES pro_candidates(candidate_id),
    symbol TEXT NOT NULL,
    company_name TEXT NOT NULL,
    as_of_date TEXT NOT NULL,
    mode TEXT NOT NULL,
    status TEXT NOT NULL,
    state_version INTEGER NOT NULL CHECK (state_version >= 0),
    priority INTEGER NOT NULL,
    archetype_ids_json TEXT NOT NULL,
    trigger_fingerprint TEXT NOT NULL,
    packet_id TEXT,
    packet_hash TEXT,
    approval_nonce_hash TEXT,
    approval_packet_hash TEXT,
    approval_prompt_hash TEXT,
    approval_browser_session_id TEXT,
    approval_expires_at TEXT,
    approval_consumed_at TEXT,
    browser_session_id TEXT,
    conversation_id TEXT,
    submit_count INTEGER NOT NULL DEFAULT 0 CHECK (submit_count IN (0, 1)),
    capture_count INTEGER NOT NULL DEFAULT 0 CHECK (capture_count >= 0),
    dossier_id TEXT,
    score_receipt_id TEXT,
    stagecourt_receipt_id TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    approved_at TEXT,
    submitted_at TEXT,
    research_completed_at TEXT,
    published_at TEXT,
    last_error_class TEXT,
    last_error_message TEXT,
    last_progress_actor TEXT,
    last_progress_hash TEXT
);

CREATE TABLE IF NOT EXISTS pro_job_events (
    event_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL REFERENCES pro_research_jobs(job_id),
    from_status TEXT NOT NULL,
    to_status TEXT NOT NULL,
    actor TEXT NOT NULL,
    idempotency_key TEXT NOT NULL,
    payload_hash TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(job_id, idempotency_key)
);

CREATE TABLE IF NOT EXISTS pro_packets (
    packet_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL UNIQUE REFERENCES pro_research_jobs(job_id),
    packet_hash TEXT NOT NULL,
    manifest_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pro_browser_sessions (
    browser_session_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL REFERENCES pro_research_jobs(job_id),
    adapter_name TEXT NOT NULL,
    conversation_id TEXT,
    state_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pro_artifacts (
    artifact_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL REFERENCES pro_research_jobs(job_id),
    artifact_kind TEXT NOT NULL,
    relative_path TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    byte_count INTEGER NOT NULL CHECK (byte_count >= 0),
    metadata_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(job_id, artifact_kind, content_hash)
);

CREATE TABLE IF NOT EXISTS pro_dossier_imports (
    dossier_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL UNIQUE REFERENCES pro_research_jobs(job_id),
    schema_version TEXT NOT NULL,
    dossier_hash TEXT NOT NULL,
    import_receipt_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pro_source_verifications (
    verification_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL REFERENCES pro_research_jobs(job_id),
    dossier_id TEXT NOT NULL REFERENCES pro_dossier_imports(dossier_id),
    verification_hash TEXT NOT NULL,
    receipt_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(job_id, verification_hash)
);

CREATE TABLE IF NOT EXISTS pro_gap_decisions (
    gap_decision_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL REFERENCES pro_research_jobs(job_id),
    evidence_gap_key TEXT NOT NULL,
    disposition TEXT NOT NULL,
    decision_hash TEXT NOT NULL,
    adjudication_batch_id TEXT NOT NULL DEFAULT '',
    receipt_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(job_id, evidence_gap_key, decision_hash)
);

CREATE TABLE IF NOT EXISTS pro_score_receipts (
    score_receipt_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL UNIQUE REFERENCES pro_research_jobs(job_id),
    score_hash TEXT NOT NULL,
    receipt_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pro_stagecourt_receipts (
    stagecourt_receipt_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL UNIQUE REFERENCES pro_research_jobs(job_id),
    stagecourt_hash TEXT NOT NULL,
    receipt_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pro_publications (
    publication_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL UNIQUE REFERENCES pro_research_jobs(job_id),
    publication_hash TEXT NOT NULL,
    receipt_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_pro_jobs_status_priority
    ON pro_research_jobs(status, priority DESC, created_at);
CREATE INDEX IF NOT EXISTS idx_pro_events_job_created
    ON pro_job_events(job_id, created_at, event_id);

CREATE TRIGGER IF NOT EXISTS pro_job_events_no_update
BEFORE UPDATE ON pro_job_events
BEGIN
    SELECT RAISE(ABORT, 'pro_job_events is append-only');
END;

CREATE TRIGGER IF NOT EXISTS pro_job_events_no_delete
BEFORE DELETE ON pro_job_events
BEGIN
    SELECT RAISE(ABORT, 'pro_job_events is append-only');
END;
"""

_SCHEMA += PRO_V2_MULTI_PASS_SCHEMA


def _ensure_dossier_snapshot_revision_schema(
    connection: sqlite3.Connection,
) -> None:
    """Migrate the original one-snapshot-per-pass table without rewriting rows."""

    columns = {
        str(row[1])
        for row in connection.execute(
            "PRAGMA table_info(pro_research_dossier_snapshots)"
        ).fetchall()
    }
    if "revision_ordinal" in columns:
        return
    connection.execute("PRAGMA foreign_keys=OFF")
    try:
        connection.execute("BEGIN IMMEDIATE")
        connection.execute(
            "ALTER TABLE pro_research_dossier_snapshots "
            "RENAME TO pro_research_dossier_snapshots_legacy"
        )
        connection.execute(
            """
            CREATE TABLE pro_research_dossier_snapshots (
                snapshot_id TEXT PRIMARY KEY,
                job_id TEXT NOT NULL REFERENCES pro_research_jobs(job_id),
                pass_id TEXT NOT NULL REFERENCES pro_research_passes(pass_id),
                revision_ordinal INTEGER NOT NULL DEFAULT 1
                    CHECK (revision_ordinal >= 1),
                parent_snapshot_id TEXT
                    REFERENCES pro_research_dossier_snapshots(snapshot_id),
                dossier_hash TEXT NOT NULL,
                relative_path TEXT NOT NULL,
                fact_count INTEGER NOT NULL CHECK (fact_count >= 0),
                question_count INTEGER NOT NULL CHECK (question_count >= 0),
                route_receipt_count INTEGER NOT NULL
                    CHECK (route_receipt_count >= 0),
                created_at TEXT NOT NULL,
                UNIQUE(pass_id, revision_ordinal),
                UNIQUE(job_id, dossier_hash)
            )
            """
        )
        connection.execute(
            """
            INSERT INTO pro_research_dossier_snapshots (
                snapshot_id, job_id, pass_id, revision_ordinal,
                parent_snapshot_id, dossier_hash, relative_path,
                fact_count, question_count, route_receipt_count, created_at
            )
            SELECT snapshot_id, job_id, pass_id, 1,
                   parent_snapshot_id, dossier_hash, relative_path,
                   fact_count, question_count, route_receipt_count, created_at
            FROM pro_research_dossier_snapshots_legacy
            """
        )
        connection.execute("DROP TABLE pro_research_dossier_snapshots_legacy")
        connection.execute(
            """
            CREATE INDEX idx_pro_dossier_snapshots_job_created
            ON pro_research_dossier_snapshots(
                job_id, created_at, snapshot_id
            )
            """
        )
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.execute("PRAGMA foreign_keys=ON")
    violations = connection.execute("PRAGMA foreign_key_check").fetchall()
    if violations:
        raise RuntimeError(
            "dossier snapshot revision migration broke foreign-key integrity"
        )


class ProFirstJobStore:
    """SQLite-backed source of truth for Pro-first orchestration state."""

    def __init__(
        self,
        database_path: str | Path,
        *,
        busy_timeout_ms: int = 5_000,
        now: Callable[[], datetime] | None = None,
        state_machine: ProJobStateMachine | None = None,
    ) -> None:
        if busy_timeout_ms <= 0:
            raise ValueError("busy_timeout_ms must be positive")
        self.database_path = Path(database_path)
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self.busy_timeout_ms = busy_timeout_ms
        self._now = now or (lambda: datetime.now(timezone.utc))
        self.state_machine = state_machine or ProJobStateMachine()
        self.initialize()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(
            str(self.database_path),
            timeout=self.busy_timeout_ms / 1_000,
            isolation_level=None,
        )
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys=ON")
        connection.execute(f"PRAGMA busy_timeout={self.busy_timeout_ms}")
        return connection

    @contextmanager
    def _transaction(self) -> Iterator[sqlite3.Connection]:
        connection = self._connect()
        try:
            connection.execute("BEGIN IMMEDIATE")
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def initialize(self) -> None:
        with closing(self._connect()) as connection:
            connection.execute("PRAGMA journal_mode=WAL")
            connection.executescript(_SCHEMA)
            _ensure_dossier_snapshot_revision_schema(connection)
            columns = {
                str(row[1])
                for row in connection.execute(
                    "PRAGMA table_info(pro_gap_decisions)"
                ).fetchall()
            }
            if "adjudication_batch_id" not in columns:
                connection.execute(
                    "ALTER TABLE pro_gap_decisions ADD COLUMN "
                    "adjudication_batch_id TEXT NOT NULL DEFAULT ''"
                )

    def pragma_snapshot(self) -> Mapping[str, Any]:
        with closing(self._connect()) as connection:
            return {
                "journal_mode": str(connection.execute("PRAGMA journal_mode").fetchone()[0]).lower(),
                "foreign_keys": int(connection.execute("PRAGMA foreign_keys").fetchone()[0]),
                "busy_timeout": int(connection.execute("PRAGMA busy_timeout").fetchone()[0]),
            }

    def claim_scan_run(
        self,
        *,
        as_of_date: str,
        scan_window: str | ScanWindow,
        scheduled_for: str,
        catchup: bool,
    ) -> ScanRunRecord | None:
        window = ScanWindow(scan_window).value
        window_key = f"{as_of_date}:{window}"
        scan_run_id = stable_id("SCAN", {"window_key": window_key})
        created_at = self._now_text()
        with self._transaction() as connection:
            try:
                connection.execute(
                    """
                    INSERT INTO pro_scan_runs (
                        scan_run_id, as_of_date, scan_window, window_key, status,
                        scheduled_for, catchup, receipt_json, created_at
                    ) VALUES (?, ?, ?, ?, 'CLAIMED', ?, ?, '{}', ?)
                    """,
                    (
                        scan_run_id,
                        as_of_date,
                        window,
                        window_key,
                        scheduled_for,
                        int(catchup),
                        created_at,
                    ),
                )
            except sqlite3.IntegrityError as error:
                if "window_key" in str(error) or "UNIQUE constraint" in str(error):
                    return None
                raise
            row = connection.execute(
                "SELECT * FROM pro_scan_runs WHERE scan_run_id=?", (scan_run_id,)
            ).fetchone()
        return self._scan_run_from_row(row)

    def complete_scan_run(
        self,
        scan_run_id: str,
        *,
        receipt: Mapping[str, Any],
        failed: bool = False,
    ) -> ScanRunRecord:
        completed_at = self._now_text()
        with self._transaction() as connection:
            cursor = connection.execute(
                """
                UPDATE pro_scan_runs
                SET status=?, receipt_json=?, completed_at=?
                WHERE scan_run_id=? AND status='CLAIMED'
                """,
                (
                    "FAILED" if failed else "COMPLETED",
                    canonical_json(receipt),
                    completed_at,
                    scan_run_id,
                ),
            )
            if cursor.rowcount != 1:
                raise VersionConflict("scan run was already completed or does not exist")
            row = connection.execute(
                "SELECT * FROM pro_scan_runs WHERE scan_run_id=?", (scan_run_id,)
            ).fetchone()
        return self._scan_run_from_row(row)

    def get_scan_run_by_window(
        self, as_of_date: str, scan_window: str | ScanWindow
    ) -> ScanRunRecord | None:
        window_key = f"{as_of_date}:{ScanWindow(scan_window).value}"
        with closing(self._connect()) as connection:
            row = connection.execute(
                "SELECT * FROM pro_scan_runs WHERE window_key=?", (window_key,)
            ).fetchone()
        return None if row is None else self._scan_run_from_row(row)

    def list_scan_runs(self, *, limit: int = 200) -> tuple[ScanRunRecord, ...]:
        if not 1 <= limit <= 1_000:
            raise ValueError("scan list limit must be between 1 and 1000")
        with closing(self._connect()) as connection:
            rows = connection.execute(
                """
                SELECT * FROM pro_scan_runs
                ORDER BY scheduled_for DESC, scan_run_id DESC LIMIT ?
                """,
                (limit,),
            ).fetchall()
        return tuple(self._scan_run_from_row(row) for row in rows)

    def create_candidate(
        self,
        *,
        symbol: str,
        company_name: str,
        as_of_date: str,
        scan_window: str | ScanWindow,
        trigger_fingerprint: str,
        research_mode: str | ResearchMode,
        selection_receipt: Mapping[str, Any],
        scan_run_id: str | None = None,
        candidate_id: str | None = None,
        dedupe_key: str | None = None,
    ) -> CandidateRecord:
        window = ScanWindow(scan_window).value
        mode = ResearchMode(research_mode).value
        identity = {
            "symbol": symbol,
            "as_of_date": as_of_date,
            "trigger_fingerprint": trigger_fingerprint,
            "mode": mode,
        }
        dedupe_key = dedupe_key or canonical_hash(identity)
        candidate_id = candidate_id or stable_id("CAND", {**identity, "dedupe_key": dedupe_key})
        created_at = self._now_text()
        record = CandidateRecord(
            candidate_id=candidate_id,
            scan_run_id=scan_run_id,
            symbol=symbol,
            company_name=company_name,
            as_of_date=as_of_date,
            scan_window=window,
            trigger_fingerprint=trigger_fingerprint,
            research_mode=mode,
            dedupe_key=dedupe_key,
            selection_receipt=dict(selection_receipt),
            created_at=created_at,
        )
        with self._transaction() as connection:
            try:
                connection.execute(
                    """
                    INSERT INTO pro_candidates (
                        candidate_id, scan_run_id, symbol, company_name, as_of_date,
                        scan_window, trigger_fingerprint, research_mode, dedupe_key,
                        selection_receipt_json, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        record.candidate_id,
                        record.scan_run_id,
                        record.symbol,
                        record.company_name,
                        record.as_of_date,
                        record.scan_window,
                        record.trigger_fingerprint,
                        record.research_mode,
                        record.dedupe_key,
                        canonical_json(record.selection_receipt),
                        record.created_at,
                    ),
                )
            except sqlite3.IntegrityError as error:
                if "dedupe_key" not in str(error) and "UNIQUE constraint" not in str(error):
                    raise
                row = connection.execute(
                    "SELECT * FROM pro_candidates WHERE dedupe_key=?", (dedupe_key,)
                ).fetchone()
                if row is None:
                    raise
                return self._candidate_from_row(row)
        return record

    def get_candidate_by_dedupe(self, dedupe_key: str) -> CandidateRecord | None:
        with closing(self._connect()) as connection:
            row = connection.execute(
                "SELECT * FROM pro_candidates WHERE dedupe_key=?", (dedupe_key,)
            ).fetchone()
        return None if row is None else self._candidate_from_row(row)

    def get_candidate(self, candidate_id: str) -> CandidateRecord:
        with closing(self._connect()) as connection:
            row = connection.execute(
                "SELECT * FROM pro_candidates WHERE candidate_id=?",
                (candidate_id,),
            ).fetchone()
        if row is None:
            raise RecordNotFound(f"candidate not found: {candidate_id}")
        return self._candidate_from_row(row)

    def list_candidates(self, *, limit: int = 200) -> tuple[CandidateRecord, ...]:
        if not 1 <= limit <= 1_000:
            raise ValueError("candidate list limit must be between 1 and 1000")
        with closing(self._connect()) as connection:
            rows = connection.execute(
                """
                SELECT * FROM pro_candidates
                ORDER BY created_at DESC, candidate_id DESC LIMIT ?
                """,
                (limit,),
            ).fetchall()
        return tuple(self._candidate_from_row(row) for row in rows)

    def get_job_by_candidate(self, candidate_id: str) -> ProResearchJob | None:
        with closing(self._connect()) as connection:
            row = connection.execute(
                "SELECT * FROM pro_research_jobs WHERE candidate_id=? ORDER BY created_at LIMIT 1",
                (candidate_id,),
            ).fetchone()
        return None if row is None else self._job_from_row(row)

    def create_job(
        self,
        candidate_id: str,
        *,
        priority: int = 0,
        archetype_ids: Sequence[str] = (),
        job_id: str | None = None,
        actor: str = "candidate-selector",
        idempotency_key: str | None = None,
    ) -> ProResearchJob:
        with self._transaction() as connection:
            candidate_row = connection.execute(
                "SELECT * FROM pro_candidates WHERE candidate_id=?", (candidate_id,)
            ).fetchone()
            if candidate_row is None:
                raise RecordNotFound(f"candidate not found: {candidate_id}")
            created_at = self._now_text()
            job_id = job_id or stable_id(
                "PROJOB",
                {
                    "candidate_id": candidate_id,
                    "trigger_fingerprint": candidate_row["trigger_fingerprint"],
                    "mode": candidate_row["research_mode"],
                },
            )
            unique_archetypes = tuple(dict.fromkeys(str(value) for value in archetype_ids))
            try:
                connection.execute(
                    """
                    INSERT INTO pro_research_jobs (
                        job_id, candidate_id, symbol, company_name, as_of_date, mode,
                        status, state_version, priority, archetype_ids_json,
                        trigger_fingerprint, submit_count, capture_count, created_at,
                        updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?, ?, ?, 0, 0, ?, ?)
                    """,
                    (
                        job_id,
                        candidate_id,
                        candidate_row["symbol"],
                        candidate_row["company_name"],
                        candidate_row["as_of_date"],
                        candidate_row["research_mode"],
                        JobStatus.CANDIDATE_SELECTED.value,
                        priority,
                        canonical_json(list(unique_archetypes)),
                        candidate_row["trigger_fingerprint"],
                        created_at,
                        created_at,
                    ),
                )
            except sqlite3.IntegrityError as error:
                if "UNIQUE constraint" not in str(error):
                    raise
                existing = connection.execute(
                    "SELECT * FROM pro_research_jobs WHERE candidate_id=?", (candidate_id,)
                ).fetchone()
                if existing is None:
                    raise
                return self._job_from_row(existing)
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=JobStatus.SCANNED,
                to_status=JobStatus.CANDIDATE_SELECTED,
                actor=actor,
                idempotency_key=idempotency_key or f"job-created:{job_id}",
                payload={"candidate_id": candidate_id},
                created_at=created_at,
            )
            row = connection.execute("SELECT * FROM pro_research_jobs WHERE job_id=?", (job_id,)).fetchone()
        return self._job_from_row(row)

    def get_job(self, job_id: str) -> ProResearchJob:
        with closing(self._connect()) as connection:
            row = connection.execute("SELECT * FROM pro_research_jobs WHERE job_id=?", (job_id,)).fetchone()
        if row is None:
            raise RecordNotFound(f"job not found: {job_id}")
        return self._job_from_row(row)

    def list_jobs(
        self,
        *,
        statuses: Sequence[str | JobStatus] = (),
        limit: int = 500,
    ) -> tuple[ProResearchJob, ...]:
        if not 1 <= limit <= 2_000:
            raise ValueError("job list limit must be between 1 and 2000")
        status_values = tuple(dict.fromkeys(JobStatus(value).value for value in statuses))
        with closing(self._connect()) as connection:
            if status_values:
                placeholders = ",".join("?" for _ in status_values)
                rows = connection.execute(
                    f"""
                    SELECT * FROM pro_research_jobs
                    WHERE status IN ({placeholders})
                    ORDER BY priority DESC, updated_at DESC, job_id DESC LIMIT ?
                    """,
                    (*status_values, limit),
                ).fetchall()
            else:
                rows = connection.execute(
                    """
                    SELECT * FROM pro_research_jobs
                    ORDER BY priority DESC, updated_at DESC, job_id DESC LIMIT ?
                    """,
                    (limit,),
                ).fetchall()
        return tuple(self._job_from_row(row) for row in rows)

    def get_packet_manifest(self, job_id: str) -> Mapping[str, Any] | None:
        with closing(self._connect()) as connection:
            row = connection.execute(
                "SELECT manifest_json FROM pro_packets WHERE job_id=?",
                (job_id,),
            ).fetchone()
        return None if row is None else json.loads(row["manifest_json"])

    def get_browser_session_state(self, job_id: str) -> Mapping[str, Any] | None:
        with closing(self._connect()) as connection:
            row = connection.execute(
                """
                SELECT browser_session_id, adapter_name, conversation_id,
                       state_json, created_at, updated_at
                FROM pro_browser_sessions WHERE job_id=?
                ORDER BY updated_at DESC LIMIT 1
                """,
                (job_id,),
            ).fetchone()
        if row is None:
            return None
        return {
            "browser_session_id": row["browser_session_id"],
            "adapter_name": row["adapter_name"],
            "conversation_id": row["conversation_id"],
            "state": json.loads(row["state_json"]),
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
        }

    def list_artifacts(self, job_id: str) -> tuple[Mapping[str, Any], ...]:
        self.get_job(job_id)
        with closing(self._connect()) as connection:
            rows = connection.execute(
                """
                SELECT artifact_id, artifact_kind, relative_path, content_hash,
                       byte_count, metadata_json, created_at
                FROM pro_artifacts WHERE job_id=?
                ORDER BY created_at, artifact_id
                """,
                (job_id,),
            ).fetchall()
        return tuple(
            {
                "artifact_id": row["artifact_id"],
                "artifact_kind": row["artifact_kind"],
                "relative_path": row["relative_path"],
                "content_hash": row["content_hash"],
                "byte_count": int(row["byte_count"]),
                "metadata": json.loads(row["metadata_json"]),
                "created_at": row["created_at"],
            }
            for row in rows
        )

    def cancel_job(
        self,
        job_id: str,
        *,
        actor: str = "dashboard-user",
        reason: str = "USER_CANCELLED",
    ) -> ProResearchJob:
        job = self.get_job(job_id)
        return self.transition(
            job_id,
            expected_version=job.state_version,
            to_status=JobStatus.CANCELLED,
            actor=actor,
            idempotency_key=f"cancelled:{job_id}:{job.state_version}",
            payload={"reason": str(reason or "USER_CANCELLED")},
        )

    def record_packet(
        self,
        job_id: str,
        *,
        expected_version: int,
        packet_id: str,
        packet_hash: str,
        manifest: Mapping[str, Any],
        actor: str,
        idempotency_key: str,
    ) -> ProResearchJob:
        if len(packet_hash) != 64:
            raise ValueError("packet_hash must be sha256")
        payload = {
            "packet_id": packet_id,
            "packet_hash": packet_hash,
            "manifest_hash": canonical_hash(manifest),
        }
        with self._transaction() as connection:
            if self._existing_idempotent_event(
                connection,
                job_id,
                idempotency_key,
                JobStatus.PACKET_READY,
                payload,
            ):
                return self._job_from_row(self._require_job_row(connection, job_id))
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            self.state_machine.validate(JobStatus(row["status"]), JobStatus.PACKET_READY)
            created_at = self._now_text()
            connection.execute(
                """
                INSERT INTO pro_packets (
                    packet_id, job_id, packet_hash, manifest_json, created_at
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (
                    packet_id,
                    job_id,
                    packet_hash,
                    canonical_json(manifest),
                    created_at,
                ),
            )
            cursor = connection.execute(
                """
                UPDATE pro_research_jobs
                SET status=?, packet_id=?, packet_hash=?,
                    state_version=state_version+1, updated_at=?
                WHERE job_id=? AND state_version=?
                """,
                (
                    JobStatus.PACKET_READY.value,
                    packet_id,
                    packet_hash,
                    created_at,
                    job_id,
                    expected_version,
                ),
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"job version changed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=JobStatus.PACKET_BUILDING,
                to_status=JobStatus.PACKET_READY,
                actor=actor,
                idempotency_key=idempotency_key,
                payload=payload,
                created_at=created_at,
            )
            result = self._require_job_row(connection, job_id)
        return self._job_from_row(result)

    def record_browser_prepared(
        self,
        job_id: str,
        *,
        expected_version: int,
        browser_session_id: str,
        conversation_id: str | None,
        adapter_name: str,
        packet_hash: str,
        prompt_hash: str,
        state: Mapping[str, Any],
        actor: str,
        idempotency_key: str,
    ) -> ProResearchJob:
        if len(packet_hash) != 64 or len(prompt_hash) != 64:
            raise ValueError("packet and prompt hashes must be sha256")
        durable_browser_state = {
            **dict(state),
            "packet_hash": packet_hash,
            "prompt_hash": prompt_hash,
        }
        payload = {
            "browser_session_id": browser_session_id,
            "conversation_id": conversation_id,
            "packet_hash": packet_hash,
            "prompt_hash": prompt_hash,
            "state_hash": canonical_hash(durable_browser_state),
        }
        with self._transaction() as connection:
            if self._existing_idempotent_event(
                connection,
                job_id,
                idempotency_key,
                JobStatus.AWAITING_USER_APPROVAL,
                payload,
            ):
                return self._job_from_row(self._require_job_row(connection, job_id))
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            source = JobStatus(row["status"])
            self.state_machine.validate(source, JobStatus.AWAITING_USER_APPROVAL)
            if row["packet_hash"] != packet_hash:
                raise ApprovalInvalid("prepared browser packet hash differs from durable packet")
            created_at = self._now_text()
            connection.execute(
                """
                INSERT INTO pro_browser_sessions (
                    browser_session_id, job_id, adapter_name, conversation_id,
                    state_json, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    browser_session_id,
                    job_id,
                    adapter_name,
                    conversation_id,
                    canonical_json(durable_browser_state),
                    created_at,
                    created_at,
                ),
            )
            cursor = connection.execute(
                """
                UPDATE pro_research_jobs
                SET status=?, browser_session_id=?, conversation_id=?,
                    state_version=state_version+1, updated_at=?
                WHERE job_id=? AND state_version=?
                """,
                (
                    JobStatus.AWAITING_USER_APPROVAL.value,
                    browser_session_id,
                    conversation_id,
                    created_at,
                    job_id,
                    expected_version,
                ),
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"job version changed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=source,
                to_status=JobStatus.AWAITING_USER_APPROVAL,
                actor=actor,
                idempotency_key=idempotency_key,
                payload=payload,
                created_at=created_at,
            )
            result = self._require_job_row(connection, job_id)
        return self._job_from_row(result)

    def rebind_recovered_conversation(
        self,
        job_id: str,
        *,
        expected_version: int,
        conversation_id: str,
        run_id: str,
        report_hash: str,
        job_marker_matches: bool,
        run_marker_matches: bool,
        actor: str,
        idempotency_key: str,
    ) -> ProResearchJob:
        """Bind a recovered canonical chat without changing job status.

        A browser restart can leave the durable job bound to ChatGPT's
        transient ``WEB:...`` URL even though the completed chat later appears
        under a canonical ``/c/<id>`` URL.  Recovery is deliberately narrower
        than submission: it may only update identity after both durable
        markers have been observed in the completed assistant result.
        """

        canonical_conversation_id = conversation_id.strip()
        if not re.fullmatch(
            r"[A-Za-z0-9][A-Za-z0-9_-]{7,127}", canonical_conversation_id
        ) or canonical_conversation_id.startswith("WEB:"):
            raise ApprovalInvalid("recovered conversation id is not canonical")
        if not run_id.strip():
            raise ApprovalInvalid("recovered conversation run id is required")
        if len(report_hash) != 64 or not re.fullmatch(r"[0-9a-f]{64}", report_hash):
            raise ApprovalInvalid("recovered result hash must be sha256")
        if not job_marker_matches or not run_marker_matches:
            raise ApprovalInvalid("recovered result markers do not match the durable job")
        payload = {
            "conversation_id": canonical_conversation_id,
            "run_id": run_id,
            "report_hash": report_hash,
            "job_marker_matches": True,
            "run_marker_matches": True,
            "automatic_resubmit_allowed": False,
            "submit_count": 1,
        }
        with self._transaction() as connection:
            row = self._require_job_row(connection, job_id)
            if row["conversation_id"] == canonical_conversation_id:
                existing = connection.execute(
                    "SELECT to_status, payload_hash FROM pro_job_events "
                    "WHERE job_id=? AND idempotency_key=?",
                    (job_id, idempotency_key),
                ).fetchone()
                if existing is not None and (
                    existing["to_status"] != row["status"]
                    or existing["payload_hash"] != canonical_hash(payload)
                ):
                    raise IdempotencyConflict(
                        "conversation recovery idempotency key was reused"
                    )
                return self._job_from_row(row)
            self._require_version(row, expected_version)
            status = JobStatus(row["status"])
            if status not in {JobStatus.RESEARCH_RUNNING, JobStatus.RESULT_DETECTED}:
                raise ApprovalInvalid(
                    "conversation recovery requires RESEARCH_RUNNING or RESULT_DETECTED"
                )
            if int(row["submit_count"]) != 1:
                raise ApprovalInvalid("conversation recovery requires exactly one prior submit")
            prior_conversation_id = str(row["conversation_id"] or "")
            if prior_conversation_id and not prior_conversation_id.startswith("WEB:"):
                raise ApprovalInvalid(
                    "only an empty or transient WEB conversation id may be rebound"
                )
            existing = connection.execute(
                "SELECT to_status, payload_hash FROM pro_job_events "
                "WHERE job_id=? AND idempotency_key=?",
                (job_id, idempotency_key),
            ).fetchone()
            if existing is not None:
                if (
                    existing["to_status"] != status.value
                    or existing["payload_hash"] != canonical_hash(payload)
                ):
                    raise IdempotencyConflict(
                        "conversation recovery idempotency key was reused"
                    )
                return self._job_from_row(row)
            browser_session_id = str(row["browser_session_id"] or "")
            session = connection.execute(
                "SELECT state_json FROM pro_browser_sessions "
                "WHERE browser_session_id=? AND job_id=?",
                (browser_session_id, job_id),
            ).fetchone()
            if session is None:
                raise ApprovalInvalid("durable browser session is missing")
            state = json.loads(session["state_json"])
            state["conversation_recovery"] = {
                "canonical_conversation_id": canonical_conversation_id,
                "run_id": run_id,
                "report_hash": report_hash,
                "marker_proof": "EXACT_JOB_AND_RUN_MARKERS",
                "automatic_resubmit_allowed": False,
            }
            updated_at = self._now_text()
            connection.execute(
                "UPDATE pro_browser_sessions "
                "SET conversation_id=?, state_json=?, updated_at=? "
                "WHERE browser_session_id=? AND job_id=?",
                (
                    canonical_conversation_id,
                    canonical_json(state),
                    updated_at,
                    browser_session_id,
                    job_id,
                ),
            )
            cursor = connection.execute(
                "UPDATE pro_research_jobs "
                "SET conversation_id=?, state_version=state_version+1, updated_at=? "
                "WHERE job_id=? AND state_version=?",
                (
                    canonical_conversation_id,
                    updated_at,
                    job_id,
                    expected_version,
                ),
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"job version changed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=status,
                to_status=status,
                actor=actor,
                idempotency_key=idempotency_key,
                payload=payload,
                created_at=updated_at,
            )
            result = self._require_job_row(connection, job_id)
        return self._job_from_row(result)

    def record_capture_complete(
        self,
        job_id: str,
        *,
        expected_version: int,
        receipt: Mapping[str, Any],
        artifacts: Sequence[Mapping[str, Any]],
        actor: str,
        idempotency_key: str,
    ) -> ProResearchJob:
        required_kinds = {"REPORT_MD", "DOSSIER_JSON", "CAPTURE_RECEIPT", "READY"}
        artifact_kinds = {str(row.get("artifact_kind")) for row in artifacts}
        if (
            len(artifact_kinds) != len(artifacts)
            or not required_kinds.issubset(artifact_kinds)
            or not (artifact_kinds - required_kinds).issubset({"REPORT_PDF"})
        ):
            raise ValueError("capture completion requires MD, dossier, receipt, and READY artifacts")
        if (
            receipt.get("schema_version") != "e2r_pro_capture_receipt_v1"
            or receipt.get("event_type") != "PRO_RESEARCH_CAPTURE_COMPLETE"
        ):
            raise ValueError("unsupported capture receipt identity")
        artifacts_by_kind = {str(row["artifact_kind"]): row for row in artifacts}
        if (
            artifacts_by_kind["REPORT_MD"].get("content_hash")
            != receipt.get("report_md_hash")
            or artifacts_by_kind["DOSSIER_JSON"].get("content_hash")
            != receipt.get("dossier_json_hash")
        ):
            raise ValueError("capture artifact hashes differ from the receipt")
        if "REPORT_PDF" in artifacts_by_kind:
            if artifacts_by_kind["REPORT_PDF"].get("content_hash") != receipt.get(
                "report_pdf_hash"
            ):
                raise ValueError("capture PDF hash differs from the receipt")
        elif receipt.get("report_pdf_hash") is not None:
            raise ValueError("capture receipt declares a missing PDF artifact")
        payload = {
            "receipt_hash": canonical_hash(receipt),
            "artifact_roster_hash": canonical_hash(list(artifacts)),
            "capture_count": receipt.get("capture_count"),
        }
        with self._transaction() as connection:
            if self._existing_idempotent_event(
                connection,
                job_id,
                idempotency_key,
                JobStatus.CAPTURE_COMPLETE,
                payload,
            ):
                return self._job_from_row(self._require_job_row(connection, job_id))
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            source = JobStatus(row["status"])
            self.state_machine.validate(source, JobStatus.CAPTURE_COMPLETE)
            if source is not JobStatus.CAPTURING_ARTIFACTS:
                raise ValueError("capture receipt may only close CAPTURING_ARTIFACTS")
            bindings = {
                "job_id": job_id,
                "target_id": row["symbol"],
                "as_of_date": row["as_of_date"],
                "packet_hash": row["packet_hash"],
                "prompt_hash": row["approval_prompt_hash"],
                "conversation_id": row["conversation_id"],
                "submit_count": row["submit_count"],
                "capture_count": 1,
            }
            for key, expected in bindings.items():
                if receipt.get(key) != expected:
                    raise ValueError(f"capture receipt binding mismatch: {key}")
            created_at = self._now_text()
            for artifact in artifacts:
                content_hash = str(artifact.get("content_hash", ""))
                byte_count = int(artifact.get("byte_count", -1))
                relative_path = str(artifact.get("relative_path", ""))
                artifact_kind = str(artifact.get("artifact_kind", ""))
                if len(content_hash) != 64 or byte_count < 0 or not relative_path:
                    raise ValueError("invalid capture artifact record")
                artifact_id = stable_id(
                    "ARTIFACT",
                    {
                        "job_id": job_id,
                        "artifact_kind": artifact_kind,
                        "content_hash": content_hash,
                    },
                )
                connection.execute(
                    """
                    INSERT INTO pro_artifacts (
                        artifact_id, job_id, artifact_kind, relative_path,
                        content_hash, byte_count, metadata_json, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        artifact_id,
                        job_id,
                        artifact_kind,
                        relative_path,
                        content_hash,
                        byte_count,
                        canonical_json(dict(artifact.get("metadata", {}))),
                        created_at,
                    ),
                )
            cursor = connection.execute(
                """
                UPDATE pro_research_jobs
                SET status=?, capture_count=1, research_completed_at=?,
                    state_version=state_version+1, updated_at=?
                WHERE job_id=? AND state_version=? AND capture_count=0 AND submit_count=1
                """,
                (
                    JobStatus.CAPTURE_COMPLETE.value,
                    receipt["captured_at"],
                    created_at,
                    job_id,
                    expected_version,
                ),
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"capture was completed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=source,
                to_status=JobStatus.CAPTURE_COMPLETE,
                actor=actor,
                idempotency_key=idempotency_key,
                payload=payload,
                created_at=created_at,
            )
            result = self._require_job_row(connection, job_id)
        return self._job_from_row(result)

    def record_dossier_import(
        self,
        job_id: str,
        *,
        expected_version: int,
        dossier_id: str,
        dossier_hash: str,
        import_receipt: Mapping[str, Any],
        actor: str,
        idempotency_key: str,
    ) -> ProResearchJob:
        if len(dossier_hash) != 64:
            raise ValueError("dossier_hash must be sha256")
        if (
            import_receipt.get("schema_version") != "e2r_pro_dossier_import_receipt_v1"
            or import_receipt.get("job_id") != job_id
            or import_receipt.get("normalized_dossier_hash") != dossier_hash
            or import_receipt.get("validation_status") != "PASS"
            or import_receipt.get("score_authority") is not False
            or import_receipt.get("stage_authority") is not False
            or import_receipt.get("evidence_promoted_count") != 0
            or len(import_receipt.get("component_ids") or ()) != 7
        ):
            raise ValueError("invalid dossier import receipt")
        payload = {
            "dossier_id": dossier_id,
            "dossier_hash": dossier_hash,
            "import_receipt_hash": canonical_hash(import_receipt),
        }
        with self._transaction() as connection:
            if self._existing_idempotent_event(
                connection,
                job_id,
                idempotency_key,
                JobStatus.DOSSIER_IMPORTED,
                payload,
            ):
                return self._job_from_row(self._require_job_row(connection, job_id))
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            source = JobStatus(row["status"])
            if source is not JobStatus.IMPORTING:
                raise ValueError("dossier import may only close IMPORTING")
            self.state_machine.validate(
                source,
                JobStatus.DOSSIER_IMPORTED,
                context=TransitionContext(dossier_validated=True),
            )
            created_at = self._now_text()
            connection.execute(
                """
                INSERT INTO pro_dossier_imports (
                    dossier_id, job_id, schema_version, dossier_hash,
                    import_receipt_json, created_at
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    dossier_id,
                    job_id,
                    "e2r_pro_research_dossier_v1",
                    dossier_hash,
                    canonical_json(import_receipt),
                    created_at,
                ),
            )
            cursor = connection.execute(
                """
                UPDATE pro_research_jobs
                SET status=?, dossier_id=?, last_error_class=NULL,
                    last_error_message=NULL, state_version=state_version+1, updated_at=?
                WHERE job_id=? AND state_version=?
                """,
                (
                    JobStatus.DOSSIER_IMPORTED.value,
                    dossier_id,
                    created_at,
                    job_id,
                    expected_version,
                ),
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"dossier import changed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=source,
                to_status=JobStatus.DOSSIER_IMPORTED,
                actor=actor,
                idempotency_key=idempotency_key,
                payload=payload,
                created_at=created_at,
            )
            result = self._require_job_row(connection, job_id)
        return self._job_from_row(result)

    def get_dossier_import_receipt(self, job_id: str) -> Mapping[str, Any] | None:
        with closing(self._connect()) as connection:
            row = connection.execute(
                "SELECT import_receipt_json FROM pro_dossier_imports WHERE job_id=?",
                (job_id,),
            ).fetchone()
        return None if row is None else json.loads(row["import_receipt_json"])

    def record_source_verification(
        self,
        job_id: str,
        *,
        expected_version: int,
        verification_id: str,
        dossier_id: str,
        verification_hash: str,
        receipt: Mapping[str, Any],
        actor: str,
        idempotency_key: str,
    ) -> ProResearchJob:
        if len(verification_hash) != 64:
            raise ValueError("verification_hash must be sha256")
        if (
            receipt.get("schema_version")
            != "e2r_pro_source_verification_receipt_v1"
            or receipt.get("status") != "SOURCE_VERIFICATION_COMPLETE"
            or receipt.get("job_id") != job_id
            or receipt.get("dossier_id") != dossier_id
            or receipt.get("verification_hash") != verification_hash
            or receipt.get("terminal_fact_count") != receipt.get("candidate_fact_count")
            or receipt.get("pro_score_authority") is not False
            or receipt.get("pro_stage_authority") is not False
            or receipt.get("query_count") != 0
            or receipt.get("search_count") != 0
        ):
            raise ValueError("invalid source verification receipt")
        payload = {
            "verification_id": verification_id,
            "verification_hash": verification_hash,
            "candidate_fact_count": receipt.get("candidate_fact_count"),
            "compiled_evidence_fact_count": receipt.get(
                "compiled_evidence_fact_count"
            ),
        }
        with self._transaction() as connection:
            if self._existing_idempotent_event(
                connection,
                job_id,
                idempotency_key,
                JobStatus.GAP_ADJUDICATION,
                payload,
            ):
                return self._job_from_row(self._require_job_row(connection, job_id))
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            source = JobStatus(row["status"])
            if source is not JobStatus.VERIFYING_SOURCES or row["dossier_id"] != dossier_id:
                raise ValueError("source verification must match VERIFYING_SOURCES dossier")
            self.state_machine.validate(
                source,
                JobStatus.GAP_ADJUDICATION,
                context=TransitionContext(source_verification_complete=True),
            )
            created_at = self._now_text()
            connection.execute(
                """
                INSERT INTO pro_source_verifications (
                    verification_id, job_id, dossier_id, verification_hash,
                    receipt_json, created_at
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    verification_id,
                    job_id,
                    dossier_id,
                    verification_hash,
                    canonical_json(receipt),
                    created_at,
                ),
            )
            cursor = connection.execute(
                """
                UPDATE pro_research_jobs
                SET status=?, last_error_class=NULL, last_error_message=NULL,
                    state_version=state_version+1, updated_at=?
                WHERE job_id=? AND state_version=?
                """,
                (
                    JobStatus.GAP_ADJUDICATION.value,
                    created_at,
                    job_id,
                    expected_version,
                ),
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"source verification changed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=source,
                to_status=JobStatus.GAP_ADJUDICATION,
                actor=actor,
                idempotency_key=idempotency_key,
                payload=payload,
                created_at=created_at,
            )
            result = self._require_job_row(connection, job_id)
        return self._job_from_row(result)

    def get_source_verification_receipt(self, job_id: str) -> Mapping[str, Any] | None:
        with closing(self._connect()) as connection:
            row = connection.execute(
                "SELECT receipt_json FROM pro_source_verifications "
                "WHERE job_id=? ORDER BY rowid DESC LIMIT 1",
                (job_id,),
            ).fetchone()
        return None if row is None else json.loads(row["receipt_json"])

    def source_verification_attempt_count(self, job_id: str) -> int:
        with closing(self._connect()) as connection:
            row = connection.execute(
                "SELECT COUNT(*) AS attempt_count FROM pro_source_verifications "
                "WHERE job_id=?",
                (job_id,),
            ).fetchone()
        return int(row["attempt_count"] if row is not None else 0)

    def record_gap_adjudication(
        self,
        job_id: str,
        *,
        expected_version: int,
        dossier_id: str,
        decisions: Sequence[Mapping[str, Any]],
        receipt: Mapping[str, Any],
        actor: str,
        idempotency_key: str,
    ) -> ProResearchJob:
        decision_rows = tuple(dict(row) for row in decisions)
        decision_hashes = tuple(str(row.get("decision_hash") or "") for row in decision_rows)
        evidence_gap_keys = tuple(
            str(row.get("evidence_gap_key") or "") for row in decision_rows
        )
        supplemental_count = int(receipt.get("supplemental_task_count") or 0)
        if (
            receipt.get("schema_version")
            != "e2r_pro_gap_adjudication_receipt_v1"
            or receipt.get("status") != "GAP_ADJUDICATION_COMPLETE"
            or receipt.get("job_id") != job_id
            or receipt.get("dossier_id") != dossier_id
            or receipt.get("decision_count") != len(decision_rows)
            or receipt.get("gap_count") != len(decision_rows)
            or receipt.get("supplemental_gap_count") != supplemental_count
            or receipt.get("full_research_restart_count") != 0
            or receipt.get("prohibited_gap_task_count") != 0
            or receipt.get("pro_gap_class_authority") is not False
            or receipt.get("pro_score_authority") is not False
            or receipt.get("pro_stage_authority") is not False
            or tuple(receipt.get("decision_hashes") or ()) != decision_hashes
            or not all(len(value) == 64 for value in decision_hashes)
            or not all(evidence_gap_keys)
            or len(evidence_gap_keys) != len(set(evidence_gap_keys))
        ):
            raise ValueError("invalid gap adjudication receipt")
        allowed_labels = {
            "CORE_SCORE_BLOCKER",
            "STAGE_BOUNDARY_GAP",
            "HARD_BREAK_GAP",
        }
        prohibited_labels = {"CORROBORATION_CAP", "MONITORING_GAP"}
        for row in decision_rows:
            without_hash = {key: value for key, value in row.items() if key != "decision_hash"}
            label = str(row.get("planner_label") or "")
            supplemental_allowed = row.get("supplemental_allowed") is True
            if (
                row.get("schema_version") != "e2r_pro_gap_decision_v1"
                or canonical_hash(without_hash) != row.get("decision_hash")
                or label not in allowed_labels | prohibited_labels
                or supplemental_allowed != (label in allowed_labels)
                or row.get("pro_proposal_authoritative") is not False
                or row.get("production_score_authority") is not False
                or row.get("production_stage_authority") is not False
                or row.get("full_research_restart_allowed") is not False
            ):
                raise ValueError("invalid durable gap decision")
        target = (
            JobStatus.SUPPLEMENTAL_RESEARCH
            if supplemental_count
            else JobStatus.COMPONENT_RESEARCH
        )
        if receipt.get("next_status") != target.value:
            raise ValueError("gap adjudication next status disagrees with tasks")
        payload = {
            "dossier_id": dossier_id,
            "gap_receipt_hash": canonical_hash(receipt),
            "decision_roster_hash": canonical_hash(list(decision_hashes)),
            "supplemental_task_count": supplemental_count,
        }
        adjudication_batch_id = canonical_hash(receipt)
        with self._transaction() as connection:
            if self._existing_idempotent_event(
                connection,
                job_id,
                idempotency_key,
                target,
                payload,
            ):
                return self._job_from_row(self._require_job_row(connection, job_id))
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            source = JobStatus(row["status"])
            if source is not JobStatus.GAP_ADJUDICATION or row["dossier_id"] != dossier_id:
                raise ValueError("gap adjudication must match the verified dossier")
            self.state_machine.validate(source, target)
            created_at = self._now_text()
            for decision in decision_rows:
                decision_id = stable_id(
                    "PROGAPDECISION",
                    {
                        "job_id": job_id,
                        "evidence_gap_key": decision["evidence_gap_key"],
                        "decision_hash": decision["decision_hash"],
                    },
                )
                connection.execute(
                    """
                    INSERT INTO pro_gap_decisions (
                        gap_decision_id, job_id, evidence_gap_key, disposition,
                        decision_hash, adjudication_batch_id, receipt_json, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        decision_id,
                        job_id,
                        decision["evidence_gap_key"],
                        decision["planner_label"],
                        decision["decision_hash"],
                        adjudication_batch_id,
                        canonical_json(decision),
                        created_at,
                    ),
                )
            cursor = connection.execute(
                """
                UPDATE pro_research_jobs
                SET status=?, last_error_class=NULL, last_error_message=NULL,
                    state_version=state_version+1, updated_at=?
                WHERE job_id=? AND state_version=?
                """,
                (target.value, created_at, job_id, expected_version),
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"gap adjudication changed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=source,
                to_status=target,
                actor=actor,
                idempotency_key=idempotency_key,
                payload=payload,
                created_at=created_at,
            )
            result = self._require_job_row(connection, job_id)
        return self._job_from_row(result)

    def get_gap_decisions(self, job_id: str) -> tuple[Mapping[str, Any], ...]:
        with closing(self._connect()) as connection:
            rows = connection.execute(
                """
                SELECT receipt_json FROM pro_gap_decisions
                WHERE job_id=? AND adjudication_batch_id=(
                    SELECT adjudication_batch_id FROM pro_gap_decisions
                    WHERE job_id=? ORDER BY rowid DESC LIMIT 1
                )
                ORDER BY rowid
                """,
                (job_id, job_id),
            ).fetchall()
        return tuple(json.loads(row["receipt_json"]) for row in rows)

    def record_score_result(
        self,
        job_id: str,
        *,
        expected_version: int,
        score_receipt_id: str,
        score_hash: str,
        receipt: Mapping[str, Any],
        actor: str,
        idempotency_key: str,
    ) -> ProResearchJob:
        score = receipt.get("score") or {}
        assessments = receipt.get("component_assessments") or ()
        full_thesis_eligibility = receipt.get("full_thesis_eligibility") or {}
        from .scoring.publication_gate import (
            validate_full_thesis_eligibility_receipt,
        )

        if isinstance(full_thesis_eligibility, Mapping):
            validate_full_thesis_eligibility_receipt(
                full_thesis_eligibility,
                expected_job_id=job_id,
            )
        receipt_without_identity = {
            key: value
            for key, value in receipt.items()
            if key not in {"score_receipt_id", "score_hash"}
        }
        if (
            len(score_hash) != 64
            or receipt.get("schema_version")
            != "e2r_pro_calibrated_score_bridge_receipt_v1"
            or receipt.get("job_id") != job_id
            or receipt.get("score_receipt_id") != score_receipt_id
            or receipt.get("score_hash") != score_hash
            or canonical_hash(receipt_without_identity) != score_hash
            or receipt.get("scorer_class") != "ResearchCalibratedComponentScorer"
            or receipt.get("new_score_engine_count") != 0
            or receipt.get("pro_score_ignored") is not True
            or receipt.get("pro_stage_ignored") is not True
            or receipt.get("production_score_authority") is not True
            or receipt.get("production_stage_authority") is not False
            or len(assessments) != 7
            or set(row.get("component_id") for row in assessments)
            != {
                "eps_fcf_explosion",
                "earnings_visibility",
                "bottleneck_pricing",
                "market_mispricing",
                "valuation_rerating",
                "capital_allocation",
                "information_confidence",
            }
            or not isinstance(score, Mapping)
            or score.get("full_score_valid") is not True
            or receipt.get("score_valid") is not True
            or not isinstance(full_thesis_eligibility, Mapping)
            or receipt.get("full_thesis_eligibility_hash")
            != full_thesis_eligibility.get("eligibility_hash")
        ):
            raise ValueError("invalid calibrated score receipt")
        payload = {
            "score_receipt_id": score_receipt_id,
            "score_hash": score_hash,
            "score_valid": receipt.get("score_valid") is True,
        }
        with self._transaction() as connection:
            if self._existing_idempotent_event(
                connection,
                job_id,
                idempotency_key,
                JobStatus.STAGECOURT,
                payload,
            ):
                return self._job_from_row(self._require_job_row(connection, job_id))
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            source = JobStatus(row["status"])
            if source is not JobStatus.SCORING:
                raise ValueError("score receipt may only close SCORING")
            self.state_machine.validate(
                source,
                JobStatus.STAGECOURT,
                context=TransitionContext(deterministic_score_present=True),
            )
            created_at = self._now_text()
            connection.execute(
                """
                INSERT INTO pro_score_receipts (
                    score_receipt_id, job_id, score_hash, receipt_json, created_at
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (
                    score_receipt_id,
                    job_id,
                    score_hash,
                    canonical_json(receipt),
                    created_at,
                ),
            )
            cursor = connection.execute(
                """
                UPDATE pro_research_jobs
                SET status=?, score_receipt_id=?, state_version=state_version+1,
                    updated_at=? WHERE job_id=? AND state_version=?
                """,
                (
                    JobStatus.STAGECOURT.value,
                    score_receipt_id,
                    created_at,
                    job_id,
                    expected_version,
                ),
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"score result changed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=source,
                to_status=JobStatus.STAGECOURT,
                actor=actor,
                idempotency_key=idempotency_key,
                payload=payload,
                created_at=created_at,
            )
            result = self._require_job_row(connection, job_id)
        return self._job_from_row(result)

    def get_score_receipt(self, job_id: str) -> Mapping[str, Any] | None:
        with closing(self._connect()) as connection:
            row = connection.execute(
                "SELECT receipt_json FROM pro_score_receipts WHERE job_id=?",
                (job_id,),
            ).fetchone()
        return None if row is None else json.loads(row["receipt_json"])

    def record_stagecourt_result(
        self,
        job_id: str,
        *,
        expected_version: int,
        stagecourt_receipt_id: str,
        stagecourt_hash: str,
        receipt: Mapping[str, Any],
        actor: str,
        idempotency_key: str,
    ) -> ProResearchJob:
        decision = receipt.get("decision") or {}
        receipt_without_identity = {
            key: value
            for key, value in receipt.items()
            if key not in {"stagecourt_receipt_id", "stagecourt_hash"}
        }
        canonical_stages = {
            "0",
            "1",
            "2",
            "3-Green",
            "3-Yellow",
            "3-Red",
            "4A",
            "4B",
            "4C",
            "5",
        }
        if (
            len(stagecourt_hash) != 64
            or receipt.get("schema_version")
            != "e2r_pro_atomic_stagecourt_bridge_receipt_v1"
            or receipt.get("status") != "ATOMIC_STAGECOURT_COMPLETE"
            or receipt.get("job_id") != job_id
            or receipt.get("stagecourt_receipt_id") != stagecourt_receipt_id
            or receipt.get("stagecourt_hash") != stagecourt_hash
            or canonical_hash(receipt_without_identity) != stagecourt_hash
            or receipt.get("stagecourt_class") != "AtomicStageCourtV2"
            or receipt.get("new_stage_engine_count") != 0
            or receipt.get("pro_stage_ignored") is not True
            or receipt.get("production_score_authority") is not False
            or receipt.get("production_stage_authority") is not True
            or not isinstance(decision, Mapping)
            or decision.get("canonical_stage") not in canonical_stages
            or len(decision.get("component_assessment_ids") or ()) != 7
            or decision.get("full_score_valid") is not True
            or not isinstance(receipt.get("full_thesis_eligibility_hash"), str)
            or len(str(receipt.get("full_thesis_eligibility_hash") or "")) != 64
        ):
            raise ValueError("invalid AtomicStageCourtV2 receipt")
        payload = {
            "stagecourt_receipt_id": stagecourt_receipt_id,
            "stagecourt_hash": stagecourt_hash,
            "canonical_stage": decision.get("canonical_stage"),
            "decision_status": decision.get("decision_status"),
        }
        with self._transaction() as connection:
            if self._existing_idempotent_event(
                connection,
                job_id,
                idempotency_key,
                JobStatus.FINAL,
                payload,
            ):
                return self._job_from_row(self._require_job_row(connection, job_id))
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            source = JobStatus(row["status"])
            if source is not JobStatus.STAGECOURT:
                raise ValueError("StageCourt receipt may only close STAGECOURT")
            score_row = connection.execute(
                "SELECT receipt_json FROM pro_score_receipts WHERE job_id=?",
                (job_id,),
            ).fetchone()
            if score_row is None:
                raise ValueError("StageCourt requires the durable full-thesis score")
            score_receipt = json.loads(score_row["receipt_json"])
            if (
                score_receipt.get("full_thesis_eligibility_hash")
                != receipt.get("full_thesis_eligibility_hash")
                or score_receipt.get("score_valid") is not True
            ):
                raise ValueError("StageCourt is detached from full-thesis eligibility")
            self.state_machine.validate(
                source,
                JobStatus.FINAL,
                context=TransitionContext(deterministic_stagecourt_present=True),
            )
            created_at = self._now_text()
            connection.execute(
                """
                INSERT INTO pro_stagecourt_receipts (
                    stagecourt_receipt_id, job_id, stagecourt_hash,
                    receipt_json, created_at
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (
                    stagecourt_receipt_id,
                    job_id,
                    stagecourt_hash,
                    canonical_json(receipt),
                    created_at,
                ),
            )
            cursor = connection.execute(
                """
                UPDATE pro_research_jobs
                SET status=?, stagecourt_receipt_id=?, state_version=state_version+1,
                    updated_at=? WHERE job_id=? AND state_version=?
                """,
                (
                    JobStatus.FINAL.value,
                    stagecourt_receipt_id,
                    created_at,
                    job_id,
                    expected_version,
                ),
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"StageCourt result changed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=source,
                to_status=JobStatus.FINAL,
                actor=actor,
                idempotency_key=idempotency_key,
                payload=payload,
                created_at=created_at,
            )
            result = self._require_job_row(connection, job_id)
        return self._job_from_row(result)

    def get_stagecourt_receipt(self, job_id: str) -> Mapping[str, Any] | None:
        with closing(self._connect()) as connection:
            row = connection.execute(
                "SELECT receipt_json FROM pro_stagecourt_receipts WHERE job_id=?",
                (job_id,),
            ).fetchone()
        return None if row is None else json.loads(row["receipt_json"])

    def record_publication(
        self,
        job_id: str,
        *,
        expected_version: int,
        publication_id: str,
        publication_hash: str,
        receipt: Mapping[str, Any],
    ) -> ProResearchJob:
        receipt_without_identity = {
            key: value
            for key, value in receipt.items()
            if key not in {"publication_id", "publication_hash"}
        }
        result = receipt.get("result") or {}
        canonical_stages = {
            "0",
            "1",
            "2",
            "3-Green",
            "3-Yellow",
            "3-Red",
            "4A",
            "4B",
            "4C",
            "5",
        }
        if (
            len(publication_hash) != 64
            or receipt.get("schema_version")
            != "e2r_pro_result_publication_receipt_v1"
            or receipt.get("status") != "PUBLISHED"
            or receipt.get("job_id") != job_id
            or receipt.get("publication_id") != publication_id
            or receipt.get("publication_hash") != publication_hash
            or canonical_hash(receipt_without_identity) != publication_hash
            or receipt.get("investment_recommendation_count") != 0
            or receipt.get("score_authority") != "ResearchCalibratedComponentScorer"
            or receipt.get("stage_authority") != "AtomicStageCourtV2"
            or not isinstance(result, Mapping)
            or result.get("schema_version") != "e2r_pro_published_result_v1"
            or result.get("job_id") != job_id
            or result.get("investment_recommendation") is not False
            or len(result.get("component_vector") or {}) != 7
            or result.get("judge_coverage") != "21/21"
            or result.get("component_coverage") != "7/7"
            or result.get("canonical_stage") not in canonical_stages
            or not isinstance(result.get("score_valid"), bool)
            or result.get("score_valid") is not True
            or result.get("research_saturation_valid") is not True
            or result.get("research_status") != "FULL_THESIS_READY"
            or result.get("publication_status") != "FULL_THESIS_PUBLISHED"
            or receipt.get("full_thesis_eligibility_hash")
            != result.get("full_thesis_eligibility_hash")
        ):
            raise ValueError("invalid Pro-first result publication")
        created_at = self._now_text()
        with self._transaction() as connection:
            existing = connection.execute(
                "SELECT * FROM pro_publications WHERE job_id=?",
                (job_id,),
            ).fetchone()
            if existing is not None:
                if (
                    existing["publication_id"] != publication_id
                    or existing["publication_hash"] != publication_hash
                    or canonical_json(json.loads(existing["receipt_json"]))
                    != canonical_json(receipt)
                ):
                    raise IdempotencyConflict(
                        "published result changed for an already published job"
                    )
                return self._job_from_row(
                    self._require_job_row(connection, job_id)
                )
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            if JobStatus(row["status"]) is not JobStatus.FINAL:
                raise ValueError("only a FINAL deterministic result may be published")
            score_row = connection.execute(
                "SELECT receipt_json FROM pro_score_receipts WHERE job_id=?",
                (job_id,),
            ).fetchone()
            stage_row = connection.execute(
                "SELECT receipt_json FROM pro_stagecourt_receipts WHERE job_id=?",
                (job_id,),
            ).fetchone()
            if score_row is None or stage_row is None:
                raise ValueError("publication requires score and StageCourt receipts")
            score_receipt = json.loads(score_row["receipt_json"])
            stage_receipt = json.loads(stage_row["receipt_json"])
            if (
                receipt.get("score_receipt_id") != row["score_receipt_id"]
                or receipt.get("stagecourt_receipt_id")
                != row["stagecourt_receipt_id"]
                or result.get("score_receipt_id") != row["score_receipt_id"]
                or result.get("stagecourt_receipt_id")
                != row["stagecourt_receipt_id"]
                or score_receipt.get("score_receipt_id")
                != row["score_receipt_id"]
                or stage_receipt.get("stagecourt_receipt_id")
                != row["stagecourt_receipt_id"]
                or score_receipt.get("full_thesis_eligibility_hash")
                != receipt.get("full_thesis_eligibility_hash")
                or stage_receipt.get("full_thesis_eligibility_hash")
                != receipt.get("full_thesis_eligibility_hash")
                or score_receipt.get("score_valid") is not True
            ):
                raise ValueError("publication receipt lineage differs from FINAL")
            connection.execute(
                """
                INSERT INTO pro_publications (
                    publication_id, job_id, publication_hash,
                    receipt_json, created_at
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (
                    publication_id,
                    job_id,
                    publication_hash,
                    canonical_json(receipt),
                    created_at,
                ),
            )
            cursor = connection.execute(
                """
                UPDATE pro_research_jobs
                SET published_at=?, state_version=state_version+1, updated_at=?
                WHERE job_id=? AND state_version=? AND status=?
                """,
                (
                    created_at,
                    created_at,
                    job_id,
                    expected_version,
                    JobStatus.FINAL.value,
                ),
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"publication changed concurrently: {job_id}")
            result_row = self._require_job_row(connection, job_id)
        return self._job_from_row(result_row)

    def get_publication(self, job_id: str) -> Mapping[str, Any] | None:
        with closing(self._connect()) as connection:
            row = connection.execute(
                "SELECT receipt_json FROM pro_publications WHERE job_id=?",
                (job_id,),
            ).fetchone()
        return None if row is None else json.loads(row["receipt_json"])

    def list_events(self, job_id: str) -> tuple[JobEvent, ...]:
        with closing(self._connect()) as connection:
            rows = connection.execute(
                "SELECT * FROM pro_job_events WHERE job_id=? ORDER BY created_at, event_id",
                (job_id,),
            ).fetchall()
        return tuple(self._event_from_row(row) for row in rows)

    def transition(
        self,
        job_id: str,
        *,
        expected_version: int,
        to_status: str | JobStatus,
        actor: str,
        idempotency_key: str,
        payload: Mapping[str, Any] | None = None,
        context: TransitionContext | None = None,
        updates: Mapping[str, Any] | None = None,
    ) -> ProResearchJob:
        target = JobStatus(to_status)
        payload = dict(payload or {})
        updates = dict(updates or {})
        unsupported = set(updates) - _JOB_MUTABLE_COLUMNS
        if unsupported:
            raise ValueError(f"unsupported job update columns: {sorted(unsupported)}")
        with self._transaction() as connection:
            duplicate = self._existing_idempotent_event(
                connection, job_id, idempotency_key, target, payload
            )
            if duplicate:
                row = self._require_job_row(connection, job_id)
                return self._job_from_row(row)
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            source = JobStatus(row["status"])
            self.state_machine.validate(source, target, context=context)
            updated_at = self._now_text()
            assignments = ["status=?", "state_version=state_version+1", "updated_at=?"]
            values: list[Any] = [target.value, updated_at]
            for column, value in sorted(updates.items()):
                assignments.append(f"{column}=?")
                values.append(value)
            values.extend([job_id, expected_version])
            cursor = connection.execute(
                f"UPDATE pro_research_jobs SET {', '.join(assignments)} "
                "WHERE job_id=? AND state_version=?",
                values,
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"job version changed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=source,
                to_status=target,
                actor=actor,
                idempotency_key=idempotency_key,
                payload=payload,
                created_at=updated_at,
            )
            result = self._require_job_row(connection, job_id)
        return self._job_from_row(result)

    def issue_approval_nonce(
        self,
        job_id: str,
        *,
        expected_version: int,
        actor: str,
        idempotency_key: str,
        prompt_hash: str,
        expires_at: str,
    ) -> tuple[ProResearchJob, str]:
        raw_nonce = secrets.token_urlsafe(32)
        nonce_hash = self._nonce_hash(raw_nonce)
        with self._transaction() as connection:
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            if JobStatus(row["status"]) is not JobStatus.AWAITING_USER_APPROVAL:
                raise ApprovalInvalid("approval nonce may only be issued while awaiting approval")
            if row["approval_consumed_at"] is not None:
                raise ApprovalInvalid("approval nonce has already been consumed")
            if not row["packet_hash"] or not row["browser_session_id"]:
                raise ApprovalInvalid("approval requires a prepared packet and browser session")
            if len(prompt_hash) != 64:
                raise ApprovalInvalid("approval prompt hash must be sha256")
            browser_row = connection.execute(
                "SELECT state_json FROM pro_browser_sessions WHERE browser_session_id=? AND job_id=?",
                (row["browser_session_id"], job_id),
            ).fetchone()
            if browser_row is None:
                raise ApprovalInvalid("approval requires a durable prepared browser binding")
            browser_state = json.loads(browser_row["state_json"])
            if (
                browser_state.get("packet_hash") != row["packet_hash"]
                or browser_state.get("prompt_hash") != prompt_hash
            ):
                raise ApprovalInvalid("approval hashes differ from prepared browser content")
            if self._parse_timestamp(expires_at) <= self._now_value():
                raise ApprovalInvalid("approval nonce expiry must be in the future")
            existing = connection.execute(
                "SELECT * FROM pro_job_events WHERE job_id=? AND idempotency_key=?",
                (job_id, idempotency_key),
            ).fetchone()
            if existing is not None:
                raise IdempotencyConflict("a plaintext approval nonce cannot be replayed")
            updated_at = self._now_text()
            cursor = connection.execute(
                """
                UPDATE pro_research_jobs
                SET approval_nonce_hash=?, approval_packet_hash=?,
                    approval_prompt_hash=?, approval_browser_session_id=?,
                    approval_expires_at=?, state_version=state_version+1, updated_at=?
                WHERE job_id=? AND state_version=?
                """,
                (
                    nonce_hash,
                    row["packet_hash"],
                    prompt_hash,
                    row["browser_session_id"],
                    expires_at,
                    updated_at,
                    job_id,
                    expected_version,
                ),
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"job version changed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=JobStatus.AWAITING_USER_APPROVAL,
                to_status=JobStatus.AWAITING_USER_APPROVAL,
                actor=actor,
                idempotency_key=idempotency_key,
                payload={
                    "nonce_hash": nonce_hash,
                    "packet_hash": row["packet_hash"],
                    "prompt_hash": prompt_hash,
                    "browser_session_id": row["browser_session_id"],
                    "expires_at": expires_at,
                },
                created_at=updated_at,
            )
            result = self._require_job_row(connection, job_id)
        return self._job_from_row(result), raw_nonce

    def consume_approval_nonce(
        self,
        job_id: str,
        raw_nonce: str,
        *,
        expected_version: int,
        actor: str,
        idempotency_key: str,
        prompt_hash: str,
    ) -> ProResearchJob:
        supplied_hash = self._nonce_hash(raw_nonce)
        with self._transaction() as connection:
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            if JobStatus(row["status"]) is not JobStatus.AWAITING_USER_APPROVAL:
                raise ApprovalInvalid("job is not awaiting user approval")
            stored_hash = row["approval_nonce_hash"]
            if (
                not stored_hash
                or row["approval_consumed_at"] is not None
                or not hmac.compare_digest(stored_hash, supplied_hash)
            ):
                raise ApprovalInvalid("approval nonce is invalid or already consumed")
            if row["approval_packet_hash"] != row["packet_hash"]:
                raise ApprovalInvalid("packet hash changed after approval nonce issuance")
            if row["approval_prompt_hash"] != prompt_hash:
                raise ApprovalInvalid("prompt hash changed after approval nonce issuance")
            if row["approval_browser_session_id"] != row["browser_session_id"]:
                raise ApprovalInvalid("browser session changed after approval nonce issuance")
            if self._parse_timestamp(row["approval_expires_at"]) <= self._now_value():
                raise ApprovalInvalid("approval nonce has expired")
            approved_at = self._now_text()
            cursor = connection.execute(
                """
                UPDATE pro_research_jobs
                SET status=?, approval_nonce_hash=NULL, approval_consumed_at=?,
                    approved_at=?, state_version=state_version+1, updated_at=?
                WHERE job_id=? AND state_version=? AND approval_consumed_at IS NULL
                """,
                (
                    JobStatus.APPROVED.value,
                    approved_at,
                    approved_at,
                    approved_at,
                    job_id,
                    expected_version,
                ),
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"approval was consumed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=JobStatus.AWAITING_USER_APPROVAL,
                to_status=JobStatus.APPROVED,
                actor=actor,
                idempotency_key=idempotency_key,
                payload={"approval_nonce_consumed": True},
                created_at=approved_at,
            )
            result = self._require_job_row(connection, job_id)
        return self._job_from_row(result)

    def claim_submit(
        self,
        job_id: str,
        *,
        expected_version: int,
        actor: str,
        idempotency_key: str,
    ) -> ProResearchJob:
        with self._transaction() as connection:
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            if row["submit_count"] != 0 or JobStatus(row["status"]) is not JobStatus.APPROVED:
                raise DuplicateSubmitBlocked("job has already been submitted or is not approved")
            if row["approval_consumed_at"] is None:
                raise ApprovalInvalid("submission requires a consumed approval nonce")
            self.state_machine.validate(
                JobStatus.APPROVED,
                JobStatus.SUBMITTING,
                context=TransitionContext(approval_nonce_consumed=True),
            )
            submitted_at = self._now_text()
            cursor = connection.execute(
                """
                UPDATE pro_research_jobs
                SET status=?, submit_count=1, submitted_at=?,
                    state_version=state_version+1, updated_at=?
                WHERE job_id=? AND state_version=? AND submit_count=0
                """,
                (
                    JobStatus.SUBMITTING.value,
                    submitted_at,
                    submitted_at,
                    job_id,
                    expected_version,
                ),
            )
            if cursor.rowcount != 1:
                raise DuplicateSubmitBlocked(f"submission was claimed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=JobStatus.APPROVED,
                to_status=JobStatus.SUBMITTING,
                actor=actor,
                idempotency_key=idempotency_key,
                payload={"submit_count": 1},
                created_at=submitted_at,
            )
            result = self._require_job_row(connection, job_id)
        return self._job_from_row(result)

    def observe_progress(
        self,
        job_id: str,
        snapshot: ProgressSnapshot,
        *,
        expected_version: int,
        actor: str,
        idempotency_key: str,
    ) -> ProResearchJob:
        progress_hash = snapshot.progress_hash
        repeated = False
        with self._transaction() as connection:
            row = self._require_job_row(connection, job_id)
            self._require_version(row, expected_version)
            source = JobStatus(row["status"])
            if source.value != snapshot.status:
                raise ValueError("progress snapshot status must match the durable job status")
            repeated = row["last_progress_actor"] == actor and row["last_progress_hash"] == progress_hash
            updated_at = self._now_text()
            if repeated:
                self.state_machine.validate(source, JobStatus.BLOCKED)
                target = JobStatus.BLOCKED
                error_class = "NO_PROGRESS_DETECTED"
                error_message = f"same progress hash repeated by {actor}: {progress_hash}"
            else:
                target = source
                error_class = row["last_error_class"]
                error_message = row["last_error_message"]
            cursor = connection.execute(
                """
                UPDATE pro_research_jobs
                SET status=?, last_progress_actor=?, last_progress_hash=?,
                    last_error_class=?, last_error_message=?,
                    state_version=state_version+1, updated_at=?
                WHERE job_id=? AND state_version=?
                """,
                (
                    target.value,
                    actor,
                    progress_hash,
                    error_class,
                    error_message,
                    updated_at,
                    job_id,
                    expected_version,
                ),
            )
            if cursor.rowcount != 1:
                raise VersionConflict(f"job version changed concurrently: {job_id}")
            self._insert_event(
                connection,
                job_id=job_id,
                from_status=source,
                to_status=target,
                actor=actor,
                idempotency_key=idempotency_key,
                payload={
                    "event": "NO_PROGRESS_DETECTED" if repeated else "PROGRESS_RECORDED",
                    "progress_hash": progress_hash,
                },
                created_at=updated_at,
            )
            result = self._require_job_row(connection, job_id)
        job = self._job_from_row(result)
        if repeated:
            raise NoProgressDetected(job.last_error_message or "no progress detected")
        return job

    def _existing_idempotent_event(
        self,
        connection: sqlite3.Connection,
        job_id: str,
        idempotency_key: str,
        target: JobStatus,
        payload: Mapping[str, Any],
    ) -> bool:
        row = connection.execute(
            "SELECT * FROM pro_job_events WHERE job_id=? AND idempotency_key=?",
            (job_id, idempotency_key),
        ).fetchone()
        if row is None:
            return False
        if row["to_status"] != target.value or row["payload_hash"] != canonical_hash(payload):
            raise IdempotencyConflict(
                f"idempotency key reused with different transition or payload: {idempotency_key}"
            )
        return True

    def _insert_event(
        self,
        connection: sqlite3.Connection,
        *,
        job_id: str,
        from_status: str | JobStatus,
        to_status: str | JobStatus,
        actor: str,
        idempotency_key: str,
        payload: Mapping[str, Any],
        created_at: str,
    ) -> None:
        payload_hash = canonical_hash(payload)
        event_id = stable_id(
            "EVENT",
            {
                "job_id": job_id,
                "idempotency_key": idempotency_key,
                "payload_hash": payload_hash,
            },
        )
        connection.execute(
            """
            INSERT INTO pro_job_events (
                event_id, job_id, from_status, to_status, actor,
                idempotency_key, payload_hash, payload_json, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event_id,
                job_id,
                JobStatus(from_status).value,
                JobStatus(to_status).value,
                actor,
                idempotency_key,
                payload_hash,
                canonical_json(payload),
                created_at,
            ),
        )

    @staticmethod
    def _require_job_row(connection: sqlite3.Connection, job_id: str) -> sqlite3.Row:
        row = connection.execute("SELECT * FROM pro_research_jobs WHERE job_id=?", (job_id,)).fetchone()
        if row is None:
            raise RecordNotFound(f"job not found: {job_id}")
        return row

    @staticmethod
    def _require_version(row: sqlite3.Row, expected_version: int) -> None:
        if int(row["state_version"]) != expected_version:
            raise VersionConflict(
                f"expected state_version={expected_version}, current={row['state_version']}"
            )

    @staticmethod
    def _nonce_hash(raw_nonce: str) -> str:
        if not raw_nonce:
            raise ApprovalInvalid("approval nonce is required")
        return hashlib.sha256(raw_nonce.encode("utf-8")).hexdigest()

    def _now_text(self) -> str:
        value = self._now_value()
        return value.isoformat().replace("+00:00", "Z")

    def _now_value(self) -> datetime:
        value = self._now()
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("now provider must return a timezone-aware datetime")
        return value.astimezone(timezone.utc)

    @staticmethod
    def _parse_timestamp(value: str | None) -> datetime:
        if not value:
            raise ApprovalInvalid("approval expiry is required")
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            raise ApprovalInvalid("approval expiry must be timezone-aware")
        return parsed.astimezone(timezone.utc)

    @staticmethod
    def _scan_run_from_row(row: sqlite3.Row) -> ScanRunRecord:
        return ScanRunRecord(
            scan_run_id=row["scan_run_id"],
            as_of_date=row["as_of_date"],
            scan_window=row["scan_window"],
            window_key=row["window_key"],
            status=row["status"],
            scheduled_for=row["scheduled_for"],
            catchup=bool(row["catchup"]),
            receipt=json.loads(row["receipt_json"]),
            created_at=row["created_at"],
            completed_at=row["completed_at"],
        )

    @staticmethod
    def _candidate_from_row(row: sqlite3.Row) -> CandidateRecord:
        return CandidateRecord(
            candidate_id=row["candidate_id"],
            scan_run_id=row["scan_run_id"],
            symbol=row["symbol"],
            company_name=row["company_name"],
            as_of_date=row["as_of_date"],
            scan_window=row["scan_window"],
            trigger_fingerprint=row["trigger_fingerprint"],
            research_mode=row["research_mode"],
            dedupe_key=row["dedupe_key"],
            selection_receipt=json.loads(row["selection_receipt_json"]),
            created_at=row["created_at"],
        )

    @staticmethod
    def _job_from_row(row: sqlite3.Row) -> ProResearchJob:
        return ProResearchJob(
            job_id=row["job_id"],
            candidate_id=row["candidate_id"],
            symbol=row["symbol"],
            company_name=row["company_name"],
            as_of_date=row["as_of_date"],
            mode=row["mode"],
            status=row["status"],
            state_version=int(row["state_version"]),
            priority=int(row["priority"]),
            archetype_ids=tuple(json.loads(row["archetype_ids_json"])),
            trigger_fingerprint=row["trigger_fingerprint"],
            packet_id=row["packet_id"],
            packet_hash=row["packet_hash"],
            approval_nonce_hash=row["approval_nonce_hash"],
            approval_packet_hash=row["approval_packet_hash"],
            approval_prompt_hash=row["approval_prompt_hash"],
            approval_browser_session_id=row["approval_browser_session_id"],
            approval_expires_at=row["approval_expires_at"],
            approval_consumed_at=row["approval_consumed_at"],
            browser_session_id=row["browser_session_id"],
            conversation_id=row["conversation_id"],
            submit_count=int(row["submit_count"]),
            capture_count=int(row["capture_count"]),
            dossier_id=row["dossier_id"],
            score_receipt_id=row["score_receipt_id"],
            stagecourt_receipt_id=row["stagecourt_receipt_id"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
            approved_at=row["approved_at"],
            submitted_at=row["submitted_at"],
            research_completed_at=row["research_completed_at"],
            published_at=row["published_at"],
            last_error_class=row["last_error_class"],
            last_error_message=row["last_error_message"],
            last_progress_actor=row["last_progress_actor"],
            last_progress_hash=row["last_progress_hash"],
        )

    @staticmethod
    def _event_from_row(row: sqlite3.Row) -> JobEvent:
        return JobEvent(
            event_id=row["event_id"],
            job_id=row["job_id"],
            from_status=row["from_status"],
            to_status=row["to_status"],
            actor=row["actor"],
            idempotency_key=row["idempotency_key"],
            payload_hash=row["payload_hash"],
            payload=json.loads(row["payload_json"]),
            created_at=row["created_at"],
        )


__all__ = [
    "ApprovalInvalid",
    "DuplicateSubmitBlocked",
    "IdempotencyConflict",
    "ProFirstJobStore",
    "ProFirstStoreError",
    "RecordNotFound",
    "VersionConflict",
]
