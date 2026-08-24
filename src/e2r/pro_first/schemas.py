"""Stable relational schema contracts for the Pro-first runtime ledger."""

from __future__ import annotations


PRO_FIRST_TABLES = frozenset(
    {
        "pro_scan_runs",
        "pro_candidates",
        "pro_research_jobs",
        "pro_job_events",
        "pro_packets",
        "pro_browser_sessions",
        "pro_artifacts",
        "pro_dossier_imports",
        "pro_source_verifications",
        "pro_gap_decisions",
        "pro_score_receipts",
        "pro_stagecourt_receipts",
        "pro_publications",
        "pro_research_approval_scopes",
        "pro_research_passes",
        "pro_research_dossier_snapshots",
        "pro_gap_reopen_ledger",
    }
)


PRO_V2_MULTI_PASS_SCHEMA = """
CREATE TABLE IF NOT EXISTS pro_research_approval_scopes (
    approval_scope_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL UNIQUE REFERENCES pro_research_jobs(job_id),
    target_id TEXT NOT NULL,
    as_of_date TEXT NOT NULL,
    primary_archetype_ids_json TEXT NOT NULL,
    contract_ids_json TEXT NOT NULL,
    allowed_followup_pass_names_json TEXT NOT NULL,
    browser_session_id TEXT NOT NULL,
    conversation_id TEXT NOT NULL,
    initial_pass_id TEXT NOT NULL,
    initial_prompt_hash TEXT NOT NULL,
    initial_response_hash TEXT NOT NULL,
    scope_hash TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pro_research_passes (
    pass_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL REFERENCES pro_research_jobs(job_id),
    approval_scope_id TEXT NOT NULL REFERENCES pro_research_approval_scopes(approval_scope_id),
    pass_name TEXT NOT NULL,
    pass_ordinal INTEGER NOT NULL CHECK (pass_ordinal >= 1),
    parent_pass_id TEXT REFERENCES pro_research_passes(pass_id),
    conversation_id TEXT NOT NULL,
    prompt_hash TEXT NOT NULL,
    response_hash TEXT,
    pass_input_hash TEXT NOT NULL,
    status TEXT NOT NULL,
    submit_count INTEGER NOT NULL DEFAULT 0 CHECK (submit_count IN (0, 1)),
    score_valid INTEGER NOT NULL DEFAULT 0 CHECK (score_valid = 0),
    publication_withheld INTEGER NOT NULL DEFAULT 1 CHECK (publication_withheld = 1),
    detail_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    prepared_at TEXT,
    submitted_at TEXT,
    completed_at TEXT,
    UNIQUE(job_id, pass_ordinal),
    UNIQUE(job_id, pass_name, parent_pass_id, pass_input_hash)
);

CREATE TABLE IF NOT EXISTS pro_gap_reopen_ledger (
    reopen_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL REFERENCES pro_research_jobs(job_id),
    stable_gap_key TEXT NOT NULL,
    reopen_ordinal INTEGER NOT NULL,
    fact_snapshot_hash TEXT NOT NULL,
    accepted_lineage_roster_hash TEXT NOT NULL,
    attempted_source_roles_hash TEXT NOT NULL,
    supervisor_text_hash TEXT NOT NULL,
    disposition TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(job_id, stable_gap_key, reopen_ordinal),
    UNIQUE(job_id, stable_gap_key, fact_snapshot_hash,
           accepted_lineage_roster_hash, attempted_source_roles_hash,
           supervisor_text_hash)
);

CREATE TABLE IF NOT EXISTS pro_research_dossier_snapshots (
    snapshot_id TEXT PRIMARY KEY,
    job_id TEXT NOT NULL REFERENCES pro_research_jobs(job_id),
    pass_id TEXT NOT NULL UNIQUE REFERENCES pro_research_passes(pass_id),
    parent_snapshot_id TEXT REFERENCES pro_research_dossier_snapshots(snapshot_id),
    dossier_hash TEXT NOT NULL,
    relative_path TEXT NOT NULL,
    fact_count INTEGER NOT NULL CHECK (fact_count >= 0),
    question_count INTEGER NOT NULL CHECK (question_count >= 0),
    route_receipt_count INTEGER NOT NULL CHECK (route_receipt_count >= 0),
    created_at TEXT NOT NULL,
    UNIQUE(job_id, dossier_hash)
);

CREATE INDEX IF NOT EXISTS idx_pro_research_passes_job_ordinal
    ON pro_research_passes(job_id, pass_ordinal);
CREATE INDEX IF NOT EXISTS idx_pro_gap_reopen_job_gap
    ON pro_gap_reopen_ledger(job_id, stable_gap_key, reopen_ordinal);
CREATE INDEX IF NOT EXISTS idx_pro_dossier_snapshots_job_created
    ON pro_research_dossier_snapshots(job_id, created_at, snapshot_id);
"""


PRO_RESEARCH_JOB_REQUIRED_FIELDS = (
    "job_id",
    "candidate_id",
    "symbol",
    "company_name",
    "as_of_date",
    "mode",
    "status",
    "state_version",
    "priority",
    "archetype_ids_json",
    "trigger_fingerprint",
    "packet_id",
    "packet_hash",
    "approval_nonce_hash",
    "approval_consumed_at",
    "browser_session_id",
    "conversation_id",
    "submit_count",
    "capture_count",
    "dossier_id",
    "score_receipt_id",
    "stagecourt_receipt_id",
    "created_at",
    "updated_at",
    "approved_at",
    "submitted_at",
    "research_completed_at",
    "published_at",
    "last_error_class",
    "last_error_message",
)


PRO_JOB_EVENT_REQUIRED_FIELDS = (
    "event_id",
    "job_id",
    "from_status",
    "to_status",
    "actor",
    "idempotency_key",
    "payload_hash",
    "created_at",
)


__all__ = [
    "PRO_FIRST_TABLES",
    "PRO_JOB_EVENT_REQUIRED_FIELDS",
    "PRO_RESEARCH_JOB_REQUIRED_FIELDS",
    "PRO_V2_MULTI_PASS_SCHEMA",
]
