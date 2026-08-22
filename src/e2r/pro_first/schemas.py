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
    }
)


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
]
