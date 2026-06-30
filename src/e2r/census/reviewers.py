"""Independent Census v3 reviewers that read only leaf artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .leaf_artifact_auditor import audit_leaf_artifacts


def run_reviewer_a_trace(output_root: str | Path) -> dict[str, Any]:
    audit = audit_leaf_artifacts(output_root)
    critical = {
        key: audit["critical_counts"][key]
        for key in (
            "claim_to_stage_trace_missing_count",
            "claim_to_stage_unlinked_count",
            "score_contribution_unused_count",
            "accepted_claim_unused_in_stage_count",
            "stage2_without_stagecourt_trace_count",
            "stagecourt_trace_id_missing_from_leaf_count",
        )
    }
    return _review("A_TRACE", output_root, critical)


def run_reviewer_b_source(output_root: str | Path) -> dict[str, Any]:
    audit = audit_leaf_artifacts(output_root)
    critical = {
        key: audit["critical_counts"][key]
        for key in (
            "source_task_total_zero_count",
            "source_task_execution_total_zero_count",
            "source_task_fake_execution_count",
            "source_task_with_accepted_claim_zero_count",
            "source_proxy_to_score_count",
            "evidence_url_pending_to_score_count",
            "price_path_only_to_score_count",
            "market_anomaly_to_score_count",
            "news_snippet_to_score_count",
        )
    }
    return _review("B_SOURCE", output_root, critical)


def run_reviewer_c_stage(output_root: str | Path) -> dict[str, Any]:
    audit = audit_leaf_artifacts(output_root)
    critical = {
        key: audit["critical_counts"][key]
        for key in (
            "unknown_over_5pct_count",
            "provider_pending_over_30pct_count",
            "single_stage_bucket_count",
            "single_status_bucket_count",
            "all_unknown_count",
            "all_provider_pending_count",
            "all_stage0_without_source_proof_count",
            "provider_failed_final_score_count",
            "recent_lookback_used_as_stage_cutoff_count",
            "no_current_catalyst_without_timeline_count",
        )
    }
    return _review("C_STAGE", output_root, critical)


def run_all_reviewers(output_root: str | Path) -> dict[str, dict[str, Any]]:
    return {
        "reviewer_A_trace": run_reviewer_a_trace(output_root),
        "reviewer_B_source": run_reviewer_b_source(output_root),
        "reviewer_C_stage": run_reviewer_c_stage(output_root),
    }


def write_reviewer_outputs(output_root: str | Path, docs_root: str | Path = "docs/operational") -> dict[str, dict[str, Any]]:
    reviewers = run_all_reviewers(output_root)
    root = Path(output_root)
    docs = Path(docs_root)
    mapping = {
        "reviewer_A_trace": ("reviewer_A_trace_audit.json", "census_mode_v3_reviewer_A_trace_audit.json"),
        "reviewer_B_source": ("reviewer_B_source_audit.json", "census_mode_v3_reviewer_B_source_audit.json"),
        "reviewer_C_stage": ("reviewer_C_stage_audit.json", "census_mode_v3_reviewer_C_stage_audit.json"),
    }
    for key, (output_name, docs_name) in mapping.items():
        _write_json(root / output_name, reviewers[key])
        _write_json(docs / docs_name, reviewers[key])
    return reviewers


def _review(name: str, output_root: str | Path, critical: dict[str, int]) -> dict[str, Any]:
    critical_count = sum(int(value) for value in critical.values())
    return {
        "schema_version": "e2r_census_v3_independent_reviewer_v1",
        "reviewer": name,
        "leaf_artifact_root": str(output_root),
        "verdict": "PASS" if critical_count == 0 else "FAIL",
        "critical_count": critical_count,
        "critical_counts": critical,
        "leaf_artifacts_checked": [
            "census_stage_status.jsonl",
            "claim_to_stage_trace.jsonl",
            "accepted_claims.jsonl",
            "score_contributions.jsonl",
            "source_tasks.jsonl",
            "source_task_executions.jsonl",
            "stagecourt_traces.jsonl",
        ],
    }


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


__all__ = ["run_all_reviewers", "run_reviewer_a_trace", "run_reviewer_b_source", "run_reviewer_c_stage", "write_reviewer_outputs"]
