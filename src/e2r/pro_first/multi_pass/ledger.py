"""SQLite ledger for bounded, same-conversation Pro research passes."""

from __future__ import annotations

from contextlib import contextmanager
import json
import sqlite3
from typing import Any, Iterator, Mapping, Sequence

from ..ids import canonical_hash, canonical_json, stable_id
from ..job_store import ProFirstJobStore
from ..research_contracts import select_contract_bundle
from ..schemas import PRO_V2_MULTI_PASS_SCHEMA
from .models import (
    BOUNDED_FOLLOWUP_PASS_NAMES,
    FollowupSubmitBlocked,
    INITIAL_PASS_NAME,
    RepeatedGapReopenHardFail,
    ResearchApprovalScope,
    ResearchPassRecord,
    ResearchPassStatus,
    ScopeApprovalRequired,
)


class ProMultiPassLedger:
    def __init__(self, store: ProFirstJobStore) -> None:
        self.store = store
        self.database_path = store.database_path
        self.busy_timeout_ms = store.busy_timeout_ms
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
            connection.executescript(PRO_V2_MULTI_PASS_SCHEMA)

    def establish_initial_scope(
        self,
        job_id: str,
        *,
        primary_archetype_ids: Sequence[str],
        initial_response_hash: str,
    ) -> ResearchApprovalScope:
        job = self.store.get_job(job_id)
        primary_ids = tuple(dict.fromkeys(str(value) for value in primary_archetype_ids))
        if len(initial_response_hash) != 64:
            raise ValueError("initial response hash must be sha256")
        if (
            job.submit_count != 1
            or not job.approval_consumed_at
            or not job.approval_prompt_hash
            or not job.browser_session_id
            or not job.conversation_id
        ):
            raise ScopeApprovalRequired(
                "bounded follow-ups require the consumed initial job approval and conversation"
            )
        if not set(primary_ids).issubset(job.archetype_ids):
            raise ScopeApprovalRequired(
                "selected contracts escape the candidate roster approved for the initial job"
            )
        bundle = select_contract_bundle(primary_ids)
        initial_pass_id = stable_id(
            "PROPASS",
            {
                "job_id": job_id,
                "pass_name": INITIAL_PASS_NAME,
                "prompt_hash": job.approval_prompt_hash,
            },
        )
        scope_payload = {
            "job_id": job_id,
            "target_id": job.symbol,
            "as_of_date": job.as_of_date,
            "primary_archetype_ids": list(primary_ids),
            "contract_ids": list(bundle.contract_ids),
            "allowed_followup_pass_names": sorted(BOUNDED_FOLLOWUP_PASS_NAMES),
            "browser_session_id": job.browser_session_id,
            "conversation_id": job.conversation_id,
            "initial_pass_id": initial_pass_id,
            "initial_prompt_hash": job.approval_prompt_hash,
            "initial_response_hash": initial_response_hash,
        }
        scope_hash = canonical_hash(scope_payload)
        approval_scope_id = stable_id("PROSCOPE", {"scope_hash": scope_hash})
        created_at = self.store._now_text()
        with self._transaction() as connection:
            existing = connection.execute(
                "SELECT * FROM pro_research_approval_scopes WHERE job_id=?",
                (job_id,),
            ).fetchone()
            if existing is not None:
                if existing["scope_hash"] != scope_hash:
                    raise ScopeApprovalRequired(
                        "the existing approval cannot be widened or rebound without new user approval"
                    )
                return self._scope_from_row(existing)
            connection.execute(
                """
                INSERT INTO pro_research_approval_scopes (
                    approval_scope_id, job_id, target_id, as_of_date,
                    primary_archetype_ids_json, contract_ids_json,
                    allowed_followup_pass_names_json, browser_session_id,
                    conversation_id, initial_pass_id, initial_prompt_hash,
                    initial_response_hash, scope_hash, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    approval_scope_id,
                    job_id,
                    job.symbol,
                    job.as_of_date,
                    canonical_json(list(primary_ids)),
                    canonical_json(list(bundle.contract_ids)),
                    canonical_json(sorted(BOUNDED_FOLLOWUP_PASS_NAMES)),
                    job.browser_session_id,
                    job.conversation_id,
                    initial_pass_id,
                    job.approval_prompt_hash,
                    initial_response_hash,
                    scope_hash,
                    created_at,
                ),
            )
            connection.execute(
                """
                INSERT INTO pro_research_passes (
                    pass_id, job_id, approval_scope_id, pass_name, pass_ordinal,
                    parent_pass_id, conversation_id, prompt_hash, response_hash,
                    pass_input_hash, status, submit_count, score_valid,
                    publication_withheld, detail_json, created_at, prepared_at,
                    submitted_at, completed_at
                ) VALUES (?, ?, ?, ?, 1, NULL, ?, ?, ?, ?, ?, 1, 0, 1, ?, ?, ?, ?, ?)
                """,
                (
                    initial_pass_id,
                    job_id,
                    approval_scope_id,
                    INITIAL_PASS_NAME,
                    job.conversation_id,
                    job.approval_prompt_hash,
                    initial_response_hash,
                    canonical_hash({"initial": True}),
                    ResearchPassStatus.COMPLETE.value,
                    canonical_json({"initial_user_approval_consumed": True}),
                    created_at,
                    job.approved_at or created_at,
                    job.submitted_at or created_at,
                    created_at,
                ),
            )
            row = connection.execute(
                "SELECT * FROM pro_research_approval_scopes WHERE approval_scope_id=?",
                (approval_scope_id,),
            ).fetchone()
        return self._scope_from_row(row)

    def get_scope(self, job_id: str) -> ResearchApprovalScope | None:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT * FROM pro_research_approval_scopes WHERE job_id=?",
                (job_id,),
            ).fetchone()
        return None if row is None else self._scope_from_row(row)

    def require_authorized_scope(
        self,
        job_id: str,
        *,
        target_id: str,
        as_of_date: str,
        primary_archetype_ids: Sequence[str],
        pass_name: str,
        conversation_id: str,
    ) -> ResearchApprovalScope:
        scope = self.get_scope(job_id)
        requested_primary = tuple(dict.fromkeys(str(value) for value in primary_archetype_ids))
        if scope is None:
            raise ScopeApprovalRequired("initial user approval scope is not recorded")
        if (
            target_id != scope.target_id
            or as_of_date != scope.as_of_date
            or requested_primary != scope.primary_archetype_ids
            or conversation_id != scope.conversation_id
            or pass_name not in scope.allowed_followup_pass_names
        ):
            raise ScopeApprovalRequired(
                "target, as_of_date, selected contracts, conversation, or pass type changed"
            )
        requested_contracts = select_contract_bundle(requested_primary).contract_ids
        if requested_contracts != scope.contract_ids:
            raise ScopeApprovalRequired("research contract scope changed")
        return scope

    def create_followup_pass(
        self,
        *,
        scope: ResearchApprovalScope,
        pass_id: str,
        pass_name: str,
        parent_pass_id: str,
        prompt_hash: str,
        pass_input_hash: str,
        detail: Mapping[str, Any],
        status: str | ResearchPassStatus = ResearchPassStatus.PLANNED,
    ) -> ResearchPassRecord:
        status_value = ResearchPassStatus(status).value
        if pass_name not in scope.allowed_followup_pass_names:
            raise ScopeApprovalRequired("follow-up pass is outside initial approval scope")
        if len(prompt_hash) != 64 or len(pass_input_hash) != 64:
            raise ValueError("pass prompt/input hashes must be sha256")
        created_at = self.store._now_text()
        with self._transaction() as connection:
            existing = connection.execute(
                "SELECT * FROM pro_research_passes WHERE pass_id=?",
                (pass_id,),
            ).fetchone()
            if existing is not None:
                if (
                    existing["prompt_hash"] != prompt_hash
                    or existing["pass_input_hash"] != pass_input_hash
                    or existing["parent_pass_id"] != parent_pass_id
                ):
                    raise FollowupSubmitBlocked("pass id is bound to different content")
                return self._pass_from_row(existing)
            parent = connection.execute(
                "SELECT * FROM pro_research_passes WHERE pass_id=? AND job_id=?",
                (parent_pass_id, scope.job_id),
            ).fetchone()
            if parent is None or parent["status"] != ResearchPassStatus.COMPLETE.value:
                raise FollowupSubmitBlocked("follow-up parent must be a completed pass in this job")
            ordinal = int(
                connection.execute(
                    "SELECT COALESCE(MAX(pass_ordinal), 0) + 1 FROM pro_research_passes WHERE job_id=?",
                    (scope.job_id,),
                ).fetchone()[0]
            )
            connection.execute(
                """
                INSERT INTO pro_research_passes (
                    pass_id, job_id, approval_scope_id, pass_name, pass_ordinal,
                    parent_pass_id, conversation_id, prompt_hash, response_hash,
                    pass_input_hash, status, submit_count, score_valid,
                    publication_withheld, detail_json, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, NULL, ?, ?, 0, 0, 1, ?, ?)
                """,
                (
                    pass_id,
                    scope.job_id,
                    scope.approval_scope_id,
                    pass_name,
                    ordinal,
                    parent_pass_id,
                    scope.conversation_id,
                    prompt_hash,
                    pass_input_hash,
                    status_value,
                    canonical_json(detail),
                    created_at,
                ),
            )
            row = connection.execute(
                "SELECT * FROM pro_research_passes WHERE pass_id=?",
                (pass_id,),
            ).fetchone()
        return self._pass_from_row(row)

    def mark_prepared(self, pass_id: str) -> ResearchPassRecord:
        return self._advance_pass(
            pass_id,
            allowed_from={ResearchPassStatus.PLANNED.value},
            target=ResearchPassStatus.PREPARED,
            timestamp_column="prepared_at",
        )

    def claim_submit(self, pass_id: str) -> ResearchPassRecord:
        now = self.store._now_text()
        with self._transaction() as connection:
            row = self._require_pass(connection, pass_id)
            if (
                row["status"] != ResearchPassStatus.PREPARED.value
                or int(row["submit_count"]) != 0
            ):
                raise FollowupSubmitBlocked("follow-up pass was already claimed or is not prepared")
            cursor = connection.execute(
                """
                UPDATE pro_research_passes
                SET status=?, submit_count=1, submitted_at=?
                WHERE pass_id=? AND status=? AND submit_count=0
                """,
                (
                    ResearchPassStatus.SUBMITTING.value,
                    now,
                    pass_id,
                    ResearchPassStatus.PREPARED.value,
                ),
            )
            if cursor.rowcount != 1:
                raise FollowupSubmitBlocked("follow-up pass was claimed concurrently")
            result = self._require_pass(connection, pass_id)
        return self._pass_from_row(result)

    def mark_running(self, pass_id: str) -> ResearchPassRecord:
        return self._advance_pass(
            pass_id,
            allowed_from={ResearchPassStatus.SUBMITTING.value},
            target=ResearchPassStatus.RESEARCH_RUNNING,
        )

    def complete_pass(self, pass_id: str, *, response_hash: str) -> ResearchPassRecord:
        if len(response_hash) != 64:
            raise ValueError("pass response hash must be sha256")
        now = self.store._now_text()
        with self._transaction() as connection:
            row = self._require_pass(connection, pass_id)
            if row["status"] == ResearchPassStatus.COMPLETE.value:
                if row["response_hash"] != response_hash:
                    raise FollowupSubmitBlocked("completed pass response hash changed")
                return self._pass_from_row(row)
            if row["status"] != ResearchPassStatus.RESEARCH_RUNNING.value:
                raise FollowupSubmitBlocked("only a running pass can complete")
            connection.execute(
                "UPDATE pro_research_passes SET status=?, response_hash=?, completed_at=? WHERE pass_id=?",
                (ResearchPassStatus.COMPLETE.value, response_hash, now, pass_id),
            )
            result = self._require_pass(connection, pass_id)
        return self._pass_from_row(result)

    def mark_transport_pending(
        self,
        pass_id: str,
        *,
        reason: str,
    ) -> ResearchPassRecord:
        now = self.store._now_text()
        with self._transaction() as connection:
            row = self._require_pass(connection, pass_id)
            if row["status"] == ResearchPassStatus.COMPLETE.value:
                raise FollowupSubmitBlocked("a completed research pass cannot become transport-pending")
            detail = json.loads(row["detail_json"])
            detail["transport_pending_reason"] = reason
            detail["research_status"] = "TRANSPORT_PENDING"
            detail["score_valid"] = False
            detail["publication_withheld"] = True
            connection.execute(
                "UPDATE pro_research_passes SET status=?, detail_json=?, completed_at=? WHERE pass_id=?",
                (
                    ResearchPassStatus.TRANSPORT_PENDING.value,
                    canonical_json(detail),
                    now,
                    pass_id,
                ),
            )
            result = self._require_pass(connection, pass_id)
        return self._pass_from_row(result)

    def get_pass(self, pass_id: str) -> ResearchPassRecord:
        with self._connect() as connection:
            row = self._require_pass(connection, pass_id)
        return self._pass_from_row(row)

    def list_passes(self, job_id: str) -> tuple[ResearchPassRecord, ...]:
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT * FROM pro_research_passes WHERE job_id=? ORDER BY pass_ordinal",
                (job_id,),
            ).fetchall()
        return tuple(self._pass_from_row(row) for row in rows)

    def register_gap_reopen(
        self,
        job_id: str,
        *,
        stable_gap_key: str,
        fact_snapshot_hash: str,
        accepted_lineage_roster_hash: str,
        attempted_source_roles_hash: str,
        supervisor_text: str,
    ) -> int:
        hashes = (
            fact_snapshot_hash,
            accepted_lineage_roster_hash,
            attempted_source_roles_hash,
        )
        if not stable_gap_key.strip() or any(len(value) != 64 for value in hashes):
            raise ValueError("stable gap key and three sha256 snapshots are required")
        supervisor_hash = canonical_hash({"supervisor_text": supervisor_text})
        hard_fail = False
        ordinal = 0
        with self._transaction() as connection:
            duplicate = connection.execute(
                """
                SELECT reopen_ordinal FROM pro_gap_reopen_ledger
                WHERE job_id=? AND stable_gap_key=? AND fact_snapshot_hash=?
                  AND accepted_lineage_roster_hash=? AND attempted_source_roles_hash=?
                  AND supervisor_text_hash=?
                """,
                (
                    job_id,
                    stable_gap_key,
                    fact_snapshot_hash,
                    accepted_lineage_roster_hash,
                    attempted_source_roles_hash,
                    supervisor_hash,
                ),
            ).fetchone()
            if duplicate is not None:
                return int(duplicate["reopen_ordinal"])
            ordinal = int(
                connection.execute(
                    """
                    SELECT COALESCE(MAX(reopen_ordinal), 0) + 1
                    FROM pro_gap_reopen_ledger WHERE job_id=? AND stable_gap_key=?
                    """,
                    (job_id, stable_gap_key),
                ).fetchone()[0]
            )
            hard_fail = ordinal >= 3
            disposition = "THIRD_REOPEN_HARD_FAIL" if hard_fail else "REOPENED"
            reopen_id = stable_id(
                "GAPREOPEN",
                {"job_id": job_id, "stable_gap_key": stable_gap_key, "ordinal": ordinal},
            )
            connection.execute(
                """
                INSERT INTO pro_gap_reopen_ledger (
                    reopen_id, job_id, stable_gap_key, reopen_ordinal,
                    fact_snapshot_hash, accepted_lineage_roster_hash,
                    attempted_source_roles_hash, supervisor_text_hash,
                    disposition, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    reopen_id,
                    job_id,
                    stable_gap_key,
                    ordinal,
                    fact_snapshot_hash,
                    accepted_lineage_roster_hash,
                    attempted_source_roles_hash,
                    supervisor_hash,
                    disposition,
                    self.store._now_text(),
                ),
            )
        if hard_fail:
            raise RepeatedGapReopenHardFail(
                "the same stable gap was reopened a third time; supervisor wording cannot reset identity"
            )
        return ordinal

    def _advance_pass(
        self,
        pass_id: str,
        *,
        allowed_from: set[str],
        target: ResearchPassStatus,
        timestamp_column: str | None = None,
    ) -> ResearchPassRecord:
        now = self.store._now_text()
        with self._transaction() as connection:
            row = self._require_pass(connection, pass_id)
            if row["status"] == target.value:
                return self._pass_from_row(row)
            if row["status"] not in allowed_from:
                raise FollowupSubmitBlocked(
                    f"invalid research pass transition: {row['status']} -> {target.value}"
                )
            assignments = ["status=?"]
            values: list[Any] = [target.value]
            if timestamp_column:
                assignments.append(f"{timestamp_column}=?")
                values.append(now)
            values.append(pass_id)
            connection.execute(
                f"UPDATE pro_research_passes SET {', '.join(assignments)} WHERE pass_id=?",
                values,
            )
            result = self._require_pass(connection, pass_id)
        return self._pass_from_row(result)

    @staticmethod
    def _require_pass(connection: sqlite3.Connection, pass_id: str) -> sqlite3.Row:
        row = connection.execute(
            "SELECT * FROM pro_research_passes WHERE pass_id=?", (pass_id,)
        ).fetchone()
        if row is None:
            raise FollowupSubmitBlocked(f"research pass not found: {pass_id}")
        return row

    @staticmethod
    def _scope_from_row(row: sqlite3.Row) -> ResearchApprovalScope:
        return ResearchApprovalScope(
            approval_scope_id=row["approval_scope_id"],
            job_id=row["job_id"],
            target_id=row["target_id"],
            as_of_date=row["as_of_date"],
            primary_archetype_ids=tuple(json.loads(row["primary_archetype_ids_json"])),
            contract_ids=tuple(json.loads(row["contract_ids_json"])),
            allowed_followup_pass_names=tuple(
                json.loads(row["allowed_followup_pass_names_json"])
            ),
            browser_session_id=row["browser_session_id"],
            conversation_id=row["conversation_id"],
            initial_pass_id=row["initial_pass_id"],
            initial_prompt_hash=row["initial_prompt_hash"],
            initial_response_hash=row["initial_response_hash"],
            scope_hash=row["scope_hash"],
            created_at=row["created_at"],
        )

    @staticmethod
    def _pass_from_row(row: sqlite3.Row) -> ResearchPassRecord:
        return ResearchPassRecord(
            pass_id=row["pass_id"],
            job_id=row["job_id"],
            approval_scope_id=row["approval_scope_id"],
            pass_name=row["pass_name"],
            pass_ordinal=int(row["pass_ordinal"]),
            parent_pass_id=row["parent_pass_id"],
            conversation_id=row["conversation_id"],
            prompt_hash=row["prompt_hash"],
            response_hash=row["response_hash"],
            pass_input_hash=row["pass_input_hash"],
            status=row["status"],
            submit_count=int(row["submit_count"]),
            score_valid=bool(row["score_valid"]),
            publication_withheld=bool(row["publication_withheld"]),
            detail=json.loads(row["detail_json"]),
            created_at=row["created_at"],
            prepared_at=row["prepared_at"],
            submitted_at=row["submitted_at"],
            completed_at=row["completed_at"],
        )


__all__ = ["ProMultiPassLedger"]
