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
    digest_rows = []
    for idx, row in enumerate(events):
        section = "Stage2-Watch" if idx < max(count // 2, 1) else "Stage1-Watch"
        score = 7.0 if idx < max(count // 2, 1) else 4.0
        validity = "FINAL_WITH_NONMATERIAL_GAPS"
        if idx == count - 1 and count >= 2:
            section = "Reject/Red"
            score = 0.0
            validity = "FINAL_RISK_REVIEW"
        digest_rows.append(
            {
                "candidate_event_id": row["candidate_event_id"],
                "symbol": row["symbol"],
                "company_name": row["company_name"],
                "trigger_category": row["trigger_category"],
                "section": section,
                "why_triggered": "official disclosure",
                "primary_archetype": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
                "verified_score": score,
                "accepted_claims": [f"CLM-{idx}"],
                "score_stage_validity": validity,
                "missing_primitives": ["cash_or_revision_conversion"],
                "provider_source_gaps": [],
                "operator_note": "fixture operator note",
            }
        )
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
        "candidate_purity": {
            "sector_coverage": {
                "summary": {
                    "unknown_sector_candidate_count": 0,
                }
            }
        },
        "score_meaning_audit": {
            "summary": {
                "deterministic_scorer_output_count": count,
                "stagecourt_trace_count": count,
                "score_without_claim_count": 0,
            }
        },
        "source_connector_report": {
            "summary": {
                "provider_failure_count": 1,
                "real_source_document_fetched_count": count,
            },
            "rows": [
                {
                    "provider_name": "IssuerIR",
                    "status": "PROVIDER_FAILED",
                    "mode": "live",
                    "provider_error": "IR page unavailable",
                    "provider_request_id": f"SRCREQ-ISSUERIR-{as_of_date}",
                    "request_id": f"SRCREQ-ISSUERIR-{as_of_date}",
                    "request_params": {"symbol": "000000", "company_name": "회사0"},
                }
            ],
        },
        "static_logic_audit": {"summary": {"critical_count_sum": 0}},
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


def fake_v3_frozen_base(as_of_date: str = "2026-06-30", count: int = 20, run_index: int = 1) -> Mapping[str, Any]:
    base = dict(fake_v3_base(as_of_date=as_of_date, count=count))
    base["config"] = {
        "as_of_date": as_of_date,
        "mode": "frozen_replay",
        "frozen_snapshot_dir": f"output/production_cutover_v3/_v3_frozen_inputs/{as_of_date}",
        "output_dir": f"output/production_cutover_v3/_v3_frozen_replays/{as_of_date}/run-{run_index}",
    }
    base["metadata"] = {**base["metadata"], "source_corpus_hash": f"FROZEN-SRC-{as_of_date}"}
    return base


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


def fake_rollup_metadata() -> Mapping[str, Any]:
    return {
        "git_head_sha": "HEAD",
        "report_base_commit_sha": "HEAD",
        "command": "PYTHONPATH=src python -m e2r.cli.run_e2r_production_cutover_v3",
        "config_hash": "CONFIG",
        "source_corpus_hash": "SOURCE",
        "candidate_event_hash": "EVENT",
        "planner_prompt_hash": "PROMPT",
        "planner_response_hash": "RESPONSE",
        "evidence_os_schema_version": "EOS",
        "scoring_schema_version": "SCORING",
        "stage_schema_version": "STAGE",
        "accepted_current_head_alignment": "exact_current_head_or_report_artifact_child",
    }
