from __future__ import annotations

from typing import Any, Mapping


def fake_v3_base(as_of_date: str = "2026-06-30", count: int = 20) -> Mapping[str, Any]:
    events = [
        {
            "candidate_event_id": f"CE-{as_of_date}-{idx}",
            "symbol": f"{idx:06d}",
            "company_name": f"회사{idx}",
            "trigger_category": "Official Positive Trigger",
            "allowed_source_families": ["DART", "KRX", "CompanyGuide"],
            "score_eligibility_policy": "accepted_claim_required",
            "investigation_only": False,
            "source_task_generation_policy": "llm_planned_official_first_bounded",
        }
        for idx in range(count)
    ]
    digest_rows = [
        {
            "candidate_event_id": row["candidate_event_id"],
            "symbol": row["symbol"],
            "company_name": row["company_name"],
            "section": "Stage1-Watch",
            "why_triggered": "official disclosure",
            "primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
            "accepted_claims": [f"CLM-{idx}"],
            "score_stage_validity": "FINAL_WITH_NONMATERIAL_GAPS",
            "missing_primitives": ["cash_or_revision_conversion"],
        }
        for idx, row in enumerate(events)
    ]
    return {
        "config": {"as_of_date": as_of_date},
        "metadata": {"source_corpus_hash": f"SRC-{as_of_date}"},
        "shadow_latest": {"daily_shadow_pass": True},
        "output_artifacts": {
            "candidate_events": events,
            "daily_watchlist": {"rows": [{"candidate_event_id": row["candidate_event_id"]} for row in events]},
            "source_tasks": [],
            "source_task_executions": [],
            "stagecourt_traces": [],
            "evidence_documents": [
                {"document_id": f"DOC-{idx}", "source_type": "API_RECORD", "content_hash": f"HASH-{idx}"}
                for idx in range(count)
            ],
            "evidence_anchors": [],
            "evidence_claim_ledger": [
                {
                    "claim_id": f"CLM-{idx}",
                    "document_id": f"DOC-{idx}",
                    "anchor_id": f"ANCH-{idx}",
                    "subject_entity_id": f"TICKER:{idx:06d}",
                    "event_date": as_of_date,
                    "primitive_id": "earnings_visibility",
                    "value": "official structured disclosure",
                    "accepted": True,
                }
                for idx in range(count)
            ],
            "primitive_states": [],
            "score_contributions": [{"contribution_id": f"SC-{idx}"} for idx in range(count)],
        },
        "operator_digest": {"rows": digest_rows},
        "score_meaning_audit": {
            "summary": {
                "deterministic_scorer_output_count": count,
                "stagecourt_trace_count": count,
                "score_without_claim_count": 0,
            }
        },
        "source_connector_report": {"summary": {"provider_failure_count": 0}, "rows": []},
        "claim_extraction_audit": {
            "summary": {
                "real_document_to_assertion_count": count,
                "accepted_claim_count": count,
            }
        },
        "sla_report": {
            "summary": {
                "total_runtime_seconds": 1,
                "max_total_runtime_seconds": 900,
                "api_call_count": count,
                "llm_call_count": 1,
                "retry_count": 0,
                "cache_hit_count": count,
                "cache_miss_count": 0,
                "unbounded_fetch_config_count": 0,
            }
        },
    }


def fake_provider_matrix(status: str = "PROVIDER_COMPLETENESS_PASS", blockers: int = 0) -> Mapping[str, Any]:
    return {
        "summary": {
            "status": status,
            "provider_blocker_count": blockers,
            "risk_provider_path_exercised_count": 1,
            "revision_report_ir_provider_path_exercised_count": 1,
        },
        "rows": [],
    }


def fake_a2(count: int = 30) -> Mapping[str, Any]:
    return {
        "report": {
            "summary": {
                "A2_REAL_REPLAY_VERIFIED_count": count,
                "source_proxy_to_A2_count": 0,
                "evidence_url_pending_to_A2_count": 0,
            }
        }
    }
