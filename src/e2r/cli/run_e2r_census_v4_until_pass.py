"""Run E2R Census v4 until honest pass or blocker."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Any

from e2r.census.census_runner_v4 import CensusV4RunConfig, run_census_mode_v4


RUN_MODES = (
    "LEDGER_REFRESH_CENSUS",
    "OFFICIAL_BASELINE_ONLY",
    "BRAIN_TRIAGE_ENABLED",
    "BRAIN_AND_WEB_ACQUISITION_ENABLED",
    "FULL_LIVE_BRAIN_CENSUS",
    "HYBRID_CENSUS",
)

PARTIAL_OUTPUT_SUMMARY_FILES = (
    "planner_runs.jsonl",
    "llm_prompts.jsonl",
    "llm_responses.jsonl",
    "source_tasks.jsonl",
    "source_task_executions.jsonl",
    "claim_extractor_runs.jsonl",
    "raw_assertions.jsonl",
    "accepted_claims.jsonl",
    "brain_to_claim_trace.jsonl",
    "score_contributions.jsonl",
    "stagecourt_traces.jsonl",
    "research_brain_full_thesis_seed_events.jsonl",
    "full_thesis_blocker_follow_up_seed_events.jsonl",
    "full_thesis_blocker_follow_up_source_tasks.jsonl",
    "full_thesis_follow_up_iterations_audit.json",
    "brain_web_runtime_progress.json",
    "brain_web_readiness_gate_audit.json",
    "goal_requirement_matrix_audit.json",
    "goal_completion_audit.json",
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--universe", default="krx")
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--v3-output-root")
    parser.add_argument("--max-symbols", type=int, default=0)
    parser.add_argument("--run-mode", "--mode", dest="run_mode", default="LEDGER_REFRESH_CENSUS", choices=RUN_MODES)
    parser.add_argument("--brain-web-mode", choices=["enabled", "disabled"], default="disabled")
    parser.add_argument("--research-brain-report-dir", default="docs/operational")
    parser.add_argument("--brain-planner-provider", default="none", choices=("real", "codex", "codex_cli", "none"))
    parser.add_argument(
        "--brain-source-acquisition",
        default="live_official_first",
        choices=("live_official_first", "frozen_real_source_snapshot", "live_official_only", "live_full_bounded", "test_fake"),
    )
    parser.add_argument("--brain-universe-limit", type=int, default=30)
    parser.add_argument("--brain-planner-success-limit", type=int, default=30)
    parser.add_argument("--brain-planner-batch-size", type=int, default=5)
    parser.add_argument("--brain-max-source-tasks-per-plan", type=int, default=5)
    parser.add_argument("--brain-max-fetches-per-task", type=int, default=3)
    parser.add_argument("--brain-accepted-claim-target", type=int, default=0)
    parser.add_argument("--brain-max-distinct-candidate-attempts", type=int, default=30)
    parser.add_argument("--brain-retry-max", type=int, default=2)
    parser.add_argument("--brain-claim-extractor-provider", default="auto", choices=("auto", "codex_cli", "rule_fallback"))
    parser.add_argument("--brain-claim-extractor-timeout-seconds", type=float, default=60.0)
    parser.add_argument("--brain-runtime-budget-seconds", type=float, default=None)
    parser.add_argument(
        "--brain-candidate-event-seed-path",
        help=(
            "Optional JSONL seed file to feed Research Brain from this Census run, "
            "for example a previous full_thesis_blocker_follow_up_seed_events.jsonl."
        ),
    )
    parser.add_argument("--brain-stage-promotion-mode", default="disabled", choices=("disabled", "strict"))
    parser.add_argument("--full-thesis-smoke-mode", default="disabled", choices=("disabled", "controlled_replay"))
    parser.add_argument(
        "--full-thesis-smoke-artifact-root",
        help=(
            "Optional output directory or samsung_hynix_full_thesis_smoke.json file from a separate "
            "controlled full-thesis smoke run. Used only as goal audit evidence; it never promotes "
            "production score/stage rows."
        ),
    )
    parser.add_argument("--target-gate", default="anti_fake", choices=("anti_fake", "meaningful", "brain_web", "full_thesis", "full_thesis_smoke"))
    parser.add_argument("--max-iterations", type=int, default=1)
    parser.add_argument("--fail-on-run-mode-overclaim", default="false")
    parser.add_argument("--fail-on-atomic-mismatch", default="false")
    parser.add_argument("--fail-on-semantic-guard", default="false")
    parser.add_argument("--fail-on-critical-audit", default="true")
    parser.add_argument("--test-result-summary", default="not_run_by_census_v4_runner")
    parser.add_argument("--test-result-artifact")
    parser.add_argument("--write-operational-docs", choices=["auto", "true", "false"], default="auto")
    args = parser.parse_args(argv)
    config = CensusV4RunConfig(
        as_of_date=args.as_of_date,
        output_root=args.output_root,
        v3_output_root=args.v3_output_root,
        universe=args.universe,
        max_symbols=args.max_symbols,
        run_mode=args.run_mode,
        brain_web_mode=args.brain_web_mode,
        research_brain_report_dir=args.research_brain_report_dir,
        brain_planner_provider=args.brain_planner_provider,
        brain_source_acquisition=args.brain_source_acquisition,
        brain_universe_limit=args.brain_universe_limit,
        brain_planner_success_limit=args.brain_planner_success_limit,
        brain_planner_batch_size=args.brain_planner_batch_size,
        brain_max_source_tasks_per_plan=args.brain_max_source_tasks_per_plan,
        brain_max_fetches_per_task=args.brain_max_fetches_per_task,
        brain_accepted_claim_target=args.brain_accepted_claim_target,
        brain_max_distinct_candidate_attempts=args.brain_max_distinct_candidate_attempts,
        brain_retry_max=args.brain_retry_max,
        brain_claim_extractor_provider=args.brain_claim_extractor_provider,
        brain_claim_extractor_timeout_seconds=args.brain_claim_extractor_timeout_seconds,
        brain_runtime_budget_seconds=args.brain_runtime_budget_seconds,
        brain_candidate_event_seed_path=args.brain_candidate_event_seed_path,
        brain_stage_promotion_mode=args.brain_stage_promotion_mode,
        full_thesis_smoke_mode=args.full_thesis_smoke_mode,
        full_thesis_smoke_artifact_root=args.full_thesis_smoke_artifact_root,
        target_gate=args.target_gate,
        max_iterations=args.max_iterations,
        fail_on_run_mode_overclaim=_parse_bool(args.fail_on_run_mode_overclaim),
        fail_on_atomic_mismatch=_parse_bool(args.fail_on_atomic_mismatch),
        fail_on_semantic_guard=_parse_bool(args.fail_on_semantic_guard),
        fail_on_critical_audit=_parse_bool(args.fail_on_critical_audit),
        write_operational_docs=_resolve_write_operational_docs(
            as_of_date=args.as_of_date,
            output_root=args.output_root,
            value=args.write_operational_docs,
        ),
        test_result_summary=args.test_result_summary,
        test_result_artifact=args.test_result_artifact,
    )
    try:
        result = run_census_mode_v4(config)
    except KeyboardInterrupt as exc:
        _write_invalid_partial_run_marker(config=config, status="INTERRUPTED", reason="keyboard_interrupt", exc=exc)
        print("INVALID_PARTIAL_OUTPUT")
        return 130
    except Exception as exc:
        _write_invalid_partial_run_marker(config=config, status="FAILED", reason="runner_exception", exc=exc)
        print("INVALID_PARTIAL_OUTPUT")
        return 1
    print(result.readiness_verdict["verdict"])
    return _exit_code_for_target_gate(result=result, target_gate=args.target_gate)


def _write_invalid_partial_run_marker(*, config: CensusV4RunConfig, status: str, reason: str, exc: BaseException) -> None:
    output_root = Path(config.resolved_output_root())
    output_root.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": "e2r_census_v4_invalid_partial_run_v1",
        "status": status,
        "verdict": "INVALID_PARTIAL_OUTPUT",
        "reason": reason,
        "exception_type": type(exc).__name__,
        "exception_message": str(exc),
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "output_root": str(output_root),
        "config": config.to_dict(),
        "partial_output_summary": _partial_output_summary(output_root),
        "readiness_evidence_allowed": False,
        "score_or_stage_evidence_allowed": False,
        "full_thesis_promotion_allowed": False,
        "operator_rule": (
            "This directory may contain partial leaf files, but it is not a completed census run. "
            "Do not use it as readiness, score, or Stage evidence."
        ),
        "next_action": "rerun after resolving the provider/runtime failure; if provider failure persists, report ProviderPending/NotReady",
    }
    (output_root / "partial_run_invalid.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (output_root / "PARTIAL_RUN_INVALID.md").write_text(
        "\n".join(
            [
                "# INVALID_PARTIAL_OUTPUT",
                "",
                f"status: {status}",
                f"reason: {reason}",
                f"exception_type: {type(exc).__name__}",
                "",
                "This output directory is not readiness, score, or Stage evidence.",
                "Rerun after resolving the provider/runtime failure.",
                "",
            ]
        )
        + "\n",
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
        "schema_version": "e2r_census_v4_partial_output_summary_v1",
        "existing_file_count": len(existing),
        "nonempty_file_count": len(nonempty),
        "files": files,
    }


def _line_count(path: Path) -> int:
    with path.open("r", encoding="utf-8") as handle:
        return sum(1 for _ in handle)


def _exit_code_for_target_gate(*, result, target_gate: str) -> int:
    if result.leaf_audit.get("verdict") != "PASS":
        return 1
    readiness = result.readiness_verdict
    if target_gate == "anti_fake":
        return 0 if readiness.get("verdict") != "NOT_READY" else 1
    if target_gate == "meaningful":
        return 0 if readiness.get("meaningful_operational_stage_pass") is True else 1
    if target_gate == "brain_web":
        gate = readiness.get("brain_web_readiness_gate") or {}
        return 0 if readiness.get("brain_web_evidence_pass") is True and gate.get("brain_web_evidence_pass_allowed") is True else 1
    if target_gate == "full_thesis":
        return 0 if readiness.get("full_thesis_production_pass") is True else 1
    if target_gate == "full_thesis_smoke":
        return 0 if readiness.get("full_thesis_smoke_pass") is True else 1
    return 1


def _parse_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    normalized = str(value).strip().lower()
    if normalized in {"1", "true", "yes", "y"}:
        return True
    if normalized in {"0", "false", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError(f"expected boolean value, got {value!r}")


def _resolve_write_operational_docs(*, as_of_date: str, output_root: str, value: str) -> bool:
    if value == "true":
        return True
    if value == "false":
        return False
    canonical = Path(f"output/census_v4/{as_of_date}").resolve()
    return Path(output_root).resolve() == canonical


if __name__ == "__main__":
    raise SystemExit(main())
