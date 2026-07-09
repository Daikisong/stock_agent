"""Generate the research-to-runtime parity audit for Census V4 artifacts."""

from __future__ import annotations

import argparse
import os
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from e2r.census.research_to_runtime_parity import write_research_to_runtime_parity_artifacts
from e2r.research_brain.legacy_cli import print_legacy_cli_block

PARTIAL_OUTPUT_SUMMARY_FILES = (
    "brain_web_runtime_progress.json",
    "planner_runs.jsonl",
    "llm_prompts.jsonl",
    "llm_responses.jsonl",
    "source_tasks.jsonl",
    "source_task_executions.jsonl",
    "accepted_claims.jsonl",
    "claim_extractor_runs.jsonl",
    "raw_assertions.jsonl",
    "adjudicated_claims.jsonl",
    "stagecourt_traces.jsonl",
    "readiness_verdict.json",
)


def _parse_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    text = value.strip().lower()
    if text in {"1", "true", "yes", "y"}:
        return True
    if text in {"0", "false", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError(f"invalid boolean value: {value}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--docs-dir", default="docs/operational")
    parser.add_argument("--output-root", default=None)
    parser.add_argument("--as-of-date", default=None)
    parser.add_argument("--mode", default="full_thesis_balanced")
    parser.add_argument("--mandatory-archetypes", default="C06,C08,C15,C17,C24,C28")
    parser.add_argument("--max-iterations", type=int, default=1)
    parser.add_argument("--allow-legacy-diagnostic", action="store_true")
    parser.add_argument("--fail-on-c05-monoculture", type=_parse_bool, default=False)
    parser.add_argument("--fail-on-unknown-target-promoted", type=_parse_bool, default=False)
    parser.add_argument("--fail-on-required-positive-missing-over-threshold", type=_parse_bool, default=False)
    parser.add_argument("--fail-on-research-proxy-score", type=_parse_bool, default=False)
    parser.add_argument(
        "--allow-repeated-runtime-attempts",
        type=_parse_bool,
        default=False,
        help=(
            "Allow more than one child Census runtime attempt in one parent invocation. "
            "The default is false because unchanged blockers require code/source-route repair before another long run."
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not args.allow_legacy_diagnostic:
        print_legacy_cli_block(
            command="run_research_to_runtime_parity_until_pass",
            replacement="python -m e2r.cli.audit_e2r_evidence_intelligence",
        )
        return 2
    repo_root = Path(args.repo_root).resolve()
    mandatory = tuple(part.strip() for part in args.mandatory_archetypes.split(",") if part.strip())
    current_output_root = args.output_root
    paths: dict[str, Any] | None = None
    audit: dict[str, Any] | None = None
    self_repair_history: list[dict[str, Any]] = []
    self_repair_enabled = args.max_iterations > 1

    def _audit_current_output() -> dict[str, Any]:
        return write_research_to_runtime_parity_artifacts(
            repo_root=repo_root,
            output_root=current_output_root,
            docs_dir=Path(args.docs_dir),
            as_of_date=args.as_of_date,
            mandatory_archetype_prefixes=mandatory,
        )

    paths = _audit_current_output()
    audit = paths["audit"]
    self_repair_history.append(_history_audit_snapshot(audit=audit, output_root=current_output_root))
    self_repair_stop_reason: str | None = None

    if self_repair_enabled:
        for iteration in range(1, args.max_iterations + 1):
            if audit["meaningful_full_thesis_evidence_pass"]:
                break
            if iteration > 1 and not args.allow_repeated_runtime_attempts:
                self_repair_stop_reason = "SELF_REPAIR_REQUIRES_CODE_OR_SOURCE_ROUTE_REPAIR_AFTER_RUNTIME_ATTEMPT"
                self_repair_history[-1]["self_repair_stop_reason"] = self_repair_stop_reason
                break
            execution = _run_next_runtime_attempt(
                repo_root=repo_root,
                manifest=paths["execution_manifest_reports"]["manifest"],
                as_of_date=args.as_of_date or audit.get("as_of_date") or "2026-07-05",
                iteration=iteration,
            )
            self_repair_history[-1]["next_runtime_execution"] = execution
            if execution.get("partial_run_invalid"):
                self_repair_stop_reason = "RUNTIME_ATTEMPT_PARTIAL_OUTPUT_INVALID"
                self_repair_history[-1]["self_repair_stop_reason"] = self_repair_stop_reason
                break
            current_output_root = execution["output_root"]
            paths = _audit_current_output()
            audit = paths["audit"]
            self_repair_history.append(_history_audit_snapshot(audit=audit, output_root=current_output_root))
            if execution["returncode"] == 130:
                self_repair_stop_reason = "RUNTIME_ATTEMPT_INTERRUPTED"
                break

    assert paths is not None and audit is not None
    result = {
        "mode": args.mode,
        "status": "LEGACY_DIAGNOSTIC_ONLY",
        "canonical_readiness_eligible": False,
        "canonical_ready_label_allowed": False,
        "max_iterations_requested": args.max_iterations,
        "self_repair_enabled": self_repair_enabled,
        "self_repair_stop_reason": self_repair_stop_reason,
        "self_repair_iteration_count": sum(
            1 for row in self_repair_history if row.get("next_runtime_execution") is not None
        ),
        "self_repair_history": [_legacy_safe_history_row(row) for row in self_repair_history],
        "legacy_internal_meaningful_pass": bool(audit["meaningful_full_thesis_evidence_pass"]),
        "blockers": audit["blockers"],
        "matrix_path": str(paths["matrix_path"]),
        "summary_path": str(paths["summary_path"]),
        "root_cause_path": str(paths["root_cause_path"]),
        "v2_audit_path": str(paths["v2_audit_path"]),
        "candidate_selection_status": paths["candidate_selection_audit"]["status"],
        "planner_bias_status": paths["planner_bias_audit"]["status"],
        "research_case_count": paths["research_reverse_bundle"]["inventory"]["record_count"],
        "research_memory_card_count": paths["research_reverse_bundle"]["cards"]["card_count"],
        "source_route_pattern_count": paths["source_route_reports"]["source_route_matrix"]["pattern_count"],
        "all_archetype_runtime_status_matrix_path": str(paths["all_status_reports"]["json_path"]),
        "all_archetype_runtime_status_row_count": paths["all_status_reports"]["matrix"]["registry_contract_count"],
        "all_archetype_next_attempt_plan_path": str(paths["next_attempt_reports"]["json_path"]),
        "all_archetype_next_attempt_plan_row_count": paths["next_attempt_reports"]["plan"]["plan_row_count"],
        "all_archetype_next_source_task_count": paths["next_attempt_reports"]["plan"]["source_task_count"],
        "all_archetype_runtime_execution_manifest_path": str(paths["execution_manifest_reports"]["json_path"]),
        "all_archetype_runtime_execution_seed_event_count": paths["execution_manifest_reports"]["manifest"]["seed_event_count"],
        "research_memory_followup_task_count": paths["followup_audit"]["task_count"],
        "mandatory_replay_accepted_claim_count": paths["replay_reports"]["replay_matrix"]["accepted_claim_replay_count"],
        "mandatory_replay_source_proxy_repair_task_count": paths["replay_reports"]["replay_matrix"][
            "source_proxy_repair_task_count"
        ],
        "legacy_internal_meaningful_acceptance_pass": bool(
            audit["meaningful_full_thesis_evidence_pass"]
        ),
        "acceptance_report_path": str(paths["acceptance_report_path"]),
        "readiness_verdict_path": str(paths["readiness_verdict_path"]),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))

    if _history_has_interrupted_runtime(self_repair_history):
        return 130

    failure_reasons: list[str] = []
    if args.fail_on_c05_monoculture and "C05_FULL_THESIS_MONOCULTURE" in audit["blockers"]:
        failure_reasons.append("C05_FULL_THESIS_MONOCULTURE")
    if args.fail_on_unknown_target_promoted and "TARGET_ARCHETYPE_UNKNOWN_PROMOTED" in audit["blockers"]:
        failure_reasons.append("TARGET_ARCHETYPE_UNKNOWN_PROMOTED")
    if (
        args.fail_on_required_positive_missing_over_threshold
        and "REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS" in audit["blockers"]
    ):
        failure_reasons.append("REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS")
    if args.fail_on_research_proxy_score:
        proxy_score_rows = [
            row
            for row in audit["rows"]
            if row["source_proxy_leak_count"] > 0 and row["runtime_full_thesis_row_count"] > 0
        ]
        if proxy_score_rows:
            failure_reasons.append("RESEARCH_PROXY_SCORE_LEAK")

    if failure_reasons:
        print(json.dumps({"failed_on": sorted(set(failure_reasons))}, ensure_ascii=False, sort_keys=True))
        return 2
    return 0 if audit["meaningful_full_thesis_evidence_pass"] else 1


def _legacy_safe_history_row(row: dict[str, Any]) -> dict[str, Any]:
    safe = dict(row)
    safe["legacy_internal_meaningful_pass"] = bool(
        safe.pop("meaningful_full_thesis_evidence_pass", False)
    )
    safe.pop("final_status", None)
    return safe


def _history_audit_snapshot(*, audit: dict[str, Any], output_root: str | Path | None) -> dict[str, Any]:
    return {
        "output_root": str(output_root or audit.get("output_root") or ""),
        "final_status": audit.get("final_status"),
        "meaningful_full_thesis_evidence_pass": bool(audit.get("meaningful_full_thesis_evidence_pass")),
        "archetype_balanced_full_thesis_pass": bool(audit.get("archetype_balanced_full_thesis_pass")),
        "full_thesis_row_count": int(audit.get("full_thesis_row_count") or 0),
        "distinct_full_thesis_archetype_count": int(audit.get("distinct_full_thesis_archetype_count") or 0),
        "mandatory_archetype_full_thesis_missing": list(audit.get("mandatory_archetype_full_thesis_missing") or []),
        "required_positive_missing_rate": audit.get("required_positive_missing_full_thesis_row_rate"),
        "green_gap_rate": audit.get("green_gap_full_thesis_row_rate"),
        "blockers": list(audit.get("blockers") or []),
    }


def _run_next_runtime_attempt(
    *,
    repo_root: Path,
    manifest: dict[str, Any],
    as_of_date: str,
    iteration: int,
) -> dict[str, Any]:
    output_root = _self_repair_output_root(as_of_date=as_of_date, iteration=iteration)
    argv = _manifest_argv_for_self_repair(manifest=manifest, output_root=output_root)
    env = os.environ.copy()
    env["PYTHONPATH"] = str(repo_root / "src")
    try:
        completed = subprocess.run(
            argv,
            cwd=repo_root,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
    except KeyboardInterrupt as exc:
        _write_invalid_partial_run_marker(
            output_root=Path(output_root),
            status="INTERRUPTED",
            reason="keyboard_interrupt",
            exc=exc,
            argv=argv,
        )
        return {
            "iteration": iteration,
            "output_root": output_root,
            "returncode": 130,
            "argv": argv,
            "stdout_tail": "",
            "stderr_tail": "keyboard_interrupt",
            "partial_run_invalid": True,
            "partial_run_invalid_path": str(Path(output_root) / "partial_run_invalid.json"),
        }
    partial_run_invalid = (Path(output_root) / "partial_run_invalid.json").exists()
    if completed.returncode == 130 and not partial_run_invalid:
        _write_invalid_partial_run_marker(
            output_root=Path(output_root),
            status="INTERRUPTED",
            reason="child_returned_130_without_marker",
            exc=None,
            argv=argv,
        )
        partial_run_invalid = True
    return {
        "iteration": iteration,
        "output_root": output_root,
        "returncode": int(completed.returncode),
        "argv": argv,
        "stdout_tail": _tail(completed.stdout),
        "stderr_tail": _tail(completed.stderr),
        "partial_run_invalid": partial_run_invalid,
        "partial_run_invalid_path": str(Path(output_root) / "partial_run_invalid.json") if partial_run_invalid else "",
    }


def _self_repair_output_root(*, as_of_date: str, iteration: int) -> str:
    safe_date = "".join(ch if ch.isdigit() or ch == "-" else "-" for ch in str(as_of_date))
    created_at = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"output/census_v4/{safe_date}-research-to-runtime-parity-self-repair-{iteration:02d}-{created_at}"


def _manifest_argv_for_self_repair(*, manifest: dict[str, Any], output_root: str) -> list[str]:
    argv = list(manifest.get("run_command_argv") or [])
    if not argv:
        raise ValueError("execution manifest does not contain run_command_argv")
    argv[0] = sys.executable
    if "--output-root" in argv:
        index = argv.index("--output-root")
        if index + 1 >= len(argv):
            raise ValueError("execution manifest has --output-root without value")
        argv[index + 1] = output_root
    else:
        argv.extend(["--output-root", output_root])
    return argv


def _tail(value: str, *, max_chars: int = 4000) -> str:
    text = value or ""
    if len(text) <= max_chars:
        return text
    return text[-max_chars:]


def _history_has_interrupted_runtime(history: list[dict[str, Any]]) -> bool:
    for row in history:
        execution = row.get("next_runtime_execution")
        if isinstance(execution, dict) and int(execution.get("returncode") or 0) == 130:
            return True
    return False


def _write_invalid_partial_run_marker(
    *,
    output_root: Path,
    status: str,
    reason: str,
    exc: BaseException | None,
    argv: list[str],
) -> None:
    output_root.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": "e2r_research_to_runtime_invalid_partial_run_v1",
        "status": status,
        "verdict": "INVALID_PARTIAL_OUTPUT",
        "reason": reason,
        "exception_type": type(exc).__name__ if exc is not None else None,
        "exception_message": str(exc) if exc is not None else "",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "output_root": str(output_root),
        "argv": argv,
        "partial_output_summary": _partial_output_summary(output_root),
        "readiness_evidence_allowed": False,
        "score_or_stage_evidence_allowed": False,
        "full_thesis_promotion_allowed": False,
        "operator_rule": (
            "This directory may contain partial runtime files, but it is not a completed research-to-runtime parity run. "
            "Do not use it as readiness, score, Stage, or Goal4 evidence."
        ),
        "next_action": "repair the code/source-route blocker or rerun from a clean output root after confirming the manifest changed",
    }
    (output_root / "partial_run_invalid.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (output_root / "PARTIAL_RUN_INVALID.md").write_text(
        "\n".join(
            [
                "# INVALID_PARTIAL_OUTPUT",
                "",
                f"status: {status}",
                f"reason: {reason}",
                f"exception_type: {payload['exception_type']}",
                "",
                "This output directory is not readiness, score, Stage, or Goal4 evidence.",
                "Use the previous completed attempt or rerun after repairing the blocker.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def _partial_output_summary(output_root: Path) -> dict[str, Any]:
    files: dict[str, dict[str, Any]] = {}
    for name in PARTIAL_OUTPUT_SUMMARY_FILES:
        path = output_root / name
        if not path.exists():
            files[name] = {"exists": False}
            continue
        stat = path.stat()
        row_count = None
        if path.suffix == ".jsonl":
            row_count = _line_count(path)
        files[name] = {
            "exists": True,
            "size_bytes": stat.st_size,
            "row_count": row_count,
            "modified_at_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
        }
    existing = [item for item in files.values() if item.get("exists")]
    nonempty = [item for item in existing if int(item.get("size_bytes") or 0) > 0]
    return {
        "schema_version": "e2r_research_to_runtime_partial_output_summary_v1",
        "existing_file_count": len(existing),
        "nonempty_file_count": len(nonempty),
        "files": files,
    }


def _line_count(path: Path) -> int:
    with path.open("r", encoding="utf-8") as handle:
        return sum(1 for _ in handle)


if __name__ == "__main__":
    sys.exit(main())
