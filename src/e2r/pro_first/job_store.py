"""Durable SQLite ledger for Pro-first research jobs.

Every status change is guarded by an optimistic ``state_version`` predicate and
written to an append-only, idempotent event ledger in the same transaction.
"""

from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import hmac
import json
from pathlib import Path
import secrets
import sqlite3
from typing import Any, Callable, Iterator, Mapping, Sequence

from .ids import canonical_hash, canonical_json, stable_id
from .models import CandidateRecord, JobEvent, JobStatus, ProResearchJob, ResearchMode, ScanWindow
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
    candidate_id TEXT NOT NULL REFERENCES pro_candidates(candidate_id),
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
        with self._connect() as connection:
            connection.execute("PRAGMA journal_mode=WAL")
            connection.executescript(_SCHEMA)

    def pragma_snapshot(self) -> Mapping[str, Any]:
        with self._connect() as connection:
            return {
                "journal_mode": str(connection.execute("PRAGMA journal_mode").fetchone()[0]).lower(),
                "foreign_keys": int(connection.execute("PRAGMA foreign_keys").fetchone()[0]),
                "busy_timeout": int(connection.execute("PRAGMA busy_timeout").fetchone()[0]),
            }

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
            "scan_window": window,
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
        return record

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
        with self._connect() as connection:
            row = connection.execute("SELECT * FROM pro_research_jobs WHERE job_id=?", (job_id,)).fetchone()
        if row is None:
            raise RecordNotFound(f"job not found: {job_id}")
        return self._job_from_row(row)

    def list_events(self, job_id: str) -> tuple[JobEvent, ...]:
        with self._connect() as connection:
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
