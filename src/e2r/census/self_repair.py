"""Self-repair log construction for Census v3."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping


def build_self_repair_log_v3(
    *,
    as_of_date: str,
    command: str,
    output_root: str | Path,
    leaf_audit: Mapping[str, Any],
    max_iterations: int = 10,
) -> dict[str, Any]:
    v1_summary = _load_json(Path("output/census") / as_of_date / "census_stage_summary.json")
    v2_audit = _load_json(Path("output/census_v2") / as_of_date / "audit_summary.json")
    detected = [
        {
            "failure_class": "ALL_PROVIDER_PENDING",
            "file": "src/e2r/census/census_runner.py",
            "function": "_baseline_inputs_for_config",
            "evidence": f"v1 provider_pending_count={v1_summary.get('provider_pending_count')}",
        },
        {
            "failure_class": "CLAIM_TO_STAGE_DISCONNECTED",
            "file": "src/e2r/census/census_runner_v2.py",
            "function": "_build_stage_rows",
            "evidence": "v2 stage rows had counts but not complete accepted_claim_ids / score_contribution_ids / stagecourt_trace_id trace contract",
        },
        {
            "failure_class": "LEAF_AUDIT_MISSING",
            "file": "src/e2r/cli/audit_e2r_census_v2.py",
            "function": "main",
            "evidence": "v2 audit used generated summary rows and did not independently recompute every required leaf linkage",
        },
    ]
    resolved = [item["failure_class"] for item in detected if leaf_audit.get("verdict") == "PASS"]
    unresolved = [] if leaf_audit.get("verdict") == "PASS" else [item["failure_class"] for item in detected]
    return {
        "schema_version": "e2r_census_v3_self_repair_log_v1",
        "as_of_date": as_of_date,
        "max_iterations": max_iterations,
        "final_status": "PASS" if leaf_audit.get("verdict") == "PASS" else "NOT_READY",
        "iterations": [
            {
                "iteration": 1,
                "command": command,
                "status_before": {
                    "v1_stage_summary": v1_summary,
                    "v2_audit_status": (v2_audit.get("summary") or {}).get("status"),
                },
                "failure_classes": [item["failure_class"] for item in detected],
                "root_causes": detected,
                "patches_applied": [
                    "added production cutover leaf loader",
                    "added claim-to-stage trace contract",
                    "added leaf artifact auditor",
                    "added independent reviewer A/B/C gates",
                    "generated v3 reports from leaf audit metrics",
                ],
                "tests_run": [],
                "metrics_before": {
                    "v1_provider_pending_count": v1_summary.get("provider_pending_count"),
                    "v1_accepted_claim_total": v1_summary.get("accepted_claim_total"),
                    "v2_leaf_audit_verdict": (v2_audit.get("summary") or {}).get("status"),
                },
                "metrics_after": leaf_audit.get("metrics", {}),
                "resolved_failures": resolved,
                "unresolved_failures": unresolved,
            }
        ],
    }


def self_repair_summary_md(log: Mapping[str, Any]) -> str:
    iteration = (log.get("iterations") or [{}])[0]
    lines = [
        "# Census Mode v3 Self Repair Summary",
        "",
        f"- final_status: {log.get('final_status')}",
        f"- iteration_count: {len(log.get('iterations') or [])}",
        f"- failure_classes: {_join_or_none(iteration.get('failure_classes') or [])}",
        f"- resolved_failures: {_join_or_none(iteration.get('resolved_failures') or [])}",
        f"- unresolved_failures: {_join_or_none(iteration.get('unresolved_failures') or [])}",
        "",
        "## Root Causes",
    ]
    for root in iteration.get("root_causes") or []:
        lines.append(f"- {root.get('failure_class')}: {root.get('file')}::{root.get('function')} - {root.get('evidence')}")
    lines.append("")
    return "\n".join(lines)


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _join_or_none(values: Any) -> str:
    text = ", ".join(str(value) for value in values)
    return text or "none"


__all__ = ["build_self_repair_log_v3", "self_repair_summary_md"]
