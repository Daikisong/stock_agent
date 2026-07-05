"""Execution manifest for the Goal4 all-archetype next runtime attempt."""

from __future__ import annotations

import json
import shlex
from pathlib import Path
from typing import Any, Mapping


DEFAULT_OUTPUT_ROOT = "output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt"
DEFAULT_V3_OUTPUT_ROOT = "output/census_v3/2026-07-01"


def _rel(path: Path, repo_root: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(repo_root.resolve()))
    except ValueError:
        return str(path)


def _argv_from_config(config: Mapping[str, Any]) -> list[str]:
    argv = [
        "python",
        "-m",
        "e2r.cli.run_e2r_census_v4_until_pass",
        "--as-of-date",
        str(config["as_of_date"]),
        "--universe",
        str(config["universe"]),
        "--output-root",
        str(config["output_root"]),
        "--v3-output-root",
        str(config["v3_output_root"]),
        "--run-mode",
        str(config["run_mode"]),
        "--brain-web-mode",
        str(config["brain_web_mode"]),
        "--research-brain-report-dir",
        str(config["research_brain_report_dir"]),
        "--brain-planner-provider",
        str(config["brain_planner_provider"]),
        "--brain-source-acquisition",
        str(config["brain_source_acquisition"]),
        "--brain-universe-limit",
        str(config["brain_universe_limit"]),
        "--brain-planner-success-limit",
        str(config["brain_planner_success_limit"]),
        "--brain-planner-batch-size",
        str(config["brain_planner_batch_size"]),
        "--brain-max-source-tasks-per-plan",
        str(config["brain_max_source_tasks_per_plan"]),
        "--brain-max-fetches-per-task",
        str(config["brain_max_fetches_per_task"]),
        "--brain-accepted-claim-target",
        str(config["brain_accepted_claim_target"]),
        "--brain-max-distinct-candidate-attempts",
        str(config["brain_max_distinct_candidate_attempts"]),
        "--brain-retry-max",
        str(config["brain_retry_max"]),
        "--brain-claim-extractor-provider",
        str(config["brain_claim_extractor_provider"]),
        "--brain-claim-extractor-timeout-seconds",
        str(config["brain_claim_extractor_timeout_seconds"]),
        "--brain-runtime-budget-seconds",
        str(config["brain_runtime_budget_seconds"]),
        "--brain-candidate-event-seed-path",
        str(config["brain_candidate_event_seed_path"]),
        "--brain-stage-promotion-mode",
        str(config["brain_stage_promotion_mode"]),
        "--full-thesis-smoke-mode",
        str(config["full_thesis_smoke_mode"]),
        "--target-gate",
        str(config["target_gate"]),
        "--max-iterations",
        str(config["max_iterations"]),
        "--fail-on-run-mode-overclaim",
        str(config["fail_on_run_mode_overclaim"]).lower(),
        "--fail-on-atomic-mismatch",
        str(config["fail_on_atomic_mismatch"]).lower(),
        "--fail-on-semantic-guard",
        str(config["fail_on_semantic_guard"]).lower(),
        "--fail-on-critical-audit",
        str(config["fail_on_critical_audit"]).lower(),
        "--write-operational-docs",
        str(config["write_operational_docs"]).lower(),
    ]
    return argv


def build_all_archetype_runtime_execution_manifest(
    *,
    next_attempt_plan: Mapping[str, Any],
    seed_event_path: str | Path,
    source_task_path: str | Path,
    repo_root: str | Path = ".",
    output_root: str = DEFAULT_OUTPUT_ROOT,
    v3_output_root: str = DEFAULT_V3_OUTPUT_ROOT,
) -> dict[str, Any]:
    repo = Path(repo_root).resolve()
    seed_path = Path(seed_event_path)
    source_path = Path(source_task_path)
    as_of_date = str(next_attempt_plan.get("as_of_date") or "2026-07-05")
    seed_count = int(next_attempt_plan.get("seed_event_count") or 0)
    source_task_count = int(next_attempt_plan.get("source_task_count") or 0)
    candidate_attempt_count = max(seed_count, int(next_attempt_plan.get("plan_row_count") or 0))
    config = {
        "as_of_date": as_of_date,
        "output_root": output_root,
        "v3_output_root": v3_output_root,
        "universe": "krx",
        "max_symbols": 0,
        "run_mode": "BRAIN_AND_WEB_ACQUISITION_ENABLED",
        "brain_web_mode": "enabled",
        "research_brain_report_dir": "docs/operational",
        "brain_planner_provider": "real",
        "brain_source_acquisition": "live_full_bounded",
        "brain_universe_limit": candidate_attempt_count,
        "brain_planner_success_limit": candidate_attempt_count,
        "brain_planner_batch_size": 5,
        "brain_max_source_tasks_per_plan": 5,
        "brain_max_fetches_per_task": 3,
        "brain_accepted_claim_target": int(next_attempt_plan.get("plan_row_count") or 0),
        "brain_max_distinct_candidate_attempts": candidate_attempt_count,
        "brain_retry_max": 1,
        "brain_claim_extractor_provider": "auto",
        "brain_claim_extractor_timeout_seconds": 180.0,
        "brain_runtime_budget_seconds": 7200.0,
        "brain_candidate_event_seed_path": _rel(seed_path, repo),
        "brain_stage_promotion_mode": "strict",
        "full_thesis_smoke_mode": "disabled",
        "full_thesis_smoke_artifact_root": None,
        "target_gate": "full_thesis",
        "max_iterations": 1,
        "fail_on_run_mode_overclaim": True,
        "fail_on_atomic_mismatch": True,
        "fail_on_semantic_guard": True,
        "fail_on_critical_audit": True,
        "write_operational_docs": True,
    }
    argv = _argv_from_config(config)
    return {
        "schema_version": "e2r_all_archetype_runtime_execution_manifest_v1",
        "execution_status": "READY_FOR_RESEARCH_BRAIN_INPUT_NOT_EXECUTED_BY_PARITY_CLI",
        "as_of_date": as_of_date,
        "seed_event_path": _rel(seed_path, repo),
        "seed_event_count": seed_count,
        "source_task_shell_path": _rel(source_path, repo),
        "source_task_shell_count": source_task_count,
        "next_attempt_plan_row_count": int(next_attempt_plan.get("plan_row_count") or 0),
        "next_attempt_attempt_type_counts": next_attempt_plan.get("attempt_type_counts") or {},
        "census_v4_config_kwargs": config,
        "run_command_env": {"PYTHONPATH": "src"},
        "run_command_argv": argv,
        "run_command": "PYTHONPATH=src " + " ".join(shlex.quote(part) for part in argv),
        "safety_assertions": {
            "seed_path_is_external_candidate_event_input": True,
            "source_tasks_are_planner_shells_not_score_inputs": True,
            "score_allowed_before_execution": False,
            "stage_promotion_allowed_before_execution": False,
            "llm_query_generation_required": bool(next_attempt_plan.get("all_tasks_require_llm_query_generation")),
            "hardcoded_query_count": 0 if next_attempt_plan.get("all_tasks_have_no_hardcoded_queries") else None,
            "finite_budget_required": bool(next_attempt_plan.get("all_tasks_have_finite_budget")),
        },
        "expected_first_runtime_leaf": "research_brain_candidate_seed_events_used.jsonl",
        "expected_seed_source_in_census_v4": "external_candidate_event_seed_path",
    }


def render_all_archetype_runtime_execution_manifest_markdown(manifest: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# All Archetype Runtime Execution Manifest - 2026-07-05",
            "",
            "이 문서는 next runtime attempt plan을 실제 Census v4 Research Brain 입력으로 연결하는 실행 장부다.",
            "",
            "쉬운 예: 이전 문서가 병원 예약 목록이라면, 이 문서는 실제 접수 창구에 내는 예약 파일 경로와 실행 명령이다.",
            "",
            "## Summary",
            "",
            f"- execution_status: `{manifest['execution_status']}`",
            f"- seed_event_path: `{manifest['seed_event_path']}`",
            f"- seed_event_count: `{manifest['seed_event_count']}`",
            f"- source_task_shell_path: `{manifest['source_task_shell_path']}`",
            f"- source_task_shell_count: `{manifest['source_task_shell_count']}`",
            f"- output_root: `{manifest['census_v4_config_kwargs']['output_root']}`",
            f"- brain_candidate_event_seed_path: `{manifest['census_v4_config_kwargs']['brain_candidate_event_seed_path']}`",
            f"- expected_seed_source_in_census_v4: `{manifest['expected_seed_source_in_census_v4']}`",
            "",
            "## Command",
            "",
            "```bash",
            str(manifest["run_command"]),
            "```",
            "",
            "## Safety",
            "",
            "- 이 manifest는 parity CLI에서 실행하지 않는다.",
            "- 실행 전 source-task shell은 점수/Stage 입력이 아니다.",
            "- Research Brain이 source-backed Evidence OS claim을 만든 뒤에만 score/stage promotion을 검토한다.",
            "",
        ]
    )


def write_all_archetype_runtime_execution_manifest(
    *,
    next_attempt_plan: Mapping[str, Any],
    seed_event_path: str | Path,
    source_task_path: str | Path,
    docs_dir: str | Path = "docs/operational",
    repo_root: str | Path = ".",
) -> dict[str, Any]:
    docs_path = Path(docs_dir)
    docs_path.mkdir(parents=True, exist_ok=True)
    manifest = build_all_archetype_runtime_execution_manifest(
        next_attempt_plan=next_attempt_plan,
        seed_event_path=seed_event_path,
        source_task_path=source_task_path,
        repo_root=repo_root,
    )
    json_path = docs_path / "all_archetype_runtime_execution_manifest_2026-07-05.json"
    alias_json_path = docs_path / "all_archetype_runtime_execution_manifest.json"
    markdown_path = docs_path / "all_archetype_runtime_execution_manifest_2026-07-05.md"
    json_text = json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    json_path.write_text(json_text, encoding="utf-8")
    alias_json_path.write_text(json_text, encoding="utf-8")
    markdown_path.write_text(render_all_archetype_runtime_execution_manifest_markdown(manifest), encoding="utf-8")
    return {
        "manifest": manifest,
        "json_path": json_path,
        "alias_json_path": alias_json_path,
        "markdown_path": markdown_path,
    }


__all__ = [
    "build_all_archetype_runtime_execution_manifest",
    "render_all_archetype_runtime_execution_manifest_markdown",
    "write_all_archetype_runtime_execution_manifest",
]
