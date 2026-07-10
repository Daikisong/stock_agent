"""Run canonical bounded current E2R operation."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.runtime.command_manifest import (
    REQUIRED_COMMAND_HASH_CATEGORIES,
    build_command_run_manifest,
    command_file_hash_entry,
    command_inline_hash_entry,
    write_command_run_manifest,
)
from e2r.research_brain.runtime.current_operation_runner import (
    CurrentOperationRunnerInput,
    load_current_operation_runner_input,
    run_current_daily_census,
    write_current_daily_census,
)
from e2r.research_brain.runtime.live_materialization import (
    AuthorizationPath,
    CurrentOperationRunnerInputBuilder,
    LiveRunMode,
    load_live_run_profile,
    package_live_census_operation,
    package_live_current_operation,
    resolve_live_authorization,
    write_current_operation_input_manifest,
)


def _parse_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y"}:
        return True
    if normalized in {"0", "false", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError(f"expected boolean, got {value!r}")


def main(
    argv: list[str] | None = None,
    *,
    command_name: str = "run_e2r_current_operation",
    manifest_args: Mapping[str, Any] | None = None,
    recorded_argv: tuple[str, ...] | None = None,
) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument(
        "--mode",
        choices=("production_bounded", "test"),
        default="production_bounded",
    )
    parser.add_argument("--universe", default="krx")
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--fail-on-critical", type=_parse_bool, default=True)
    parser.add_argument("--input-manifest")
    parser.add_argument("--materialize-live-input", type=_parse_bool, default=False)
    parser.add_argument(
        "--live-materialization-authorized", type=_parse_bool, default=False
    )
    parser.add_argument("--run-profile")
    parser.add_argument(
        "--live-run-mode",
        choices=tuple(
            mode.value
            for mode in LiveRunMode
            if mode not in {LiveRunMode.MANIFEST_REPLAY, LiveRunMode.TEST_FIXTURE}
        ),
        default=LiveRunMode.LIVE_DAILY_INCREMENTAL.value,
    )
    args = parser.parse_args(argv)
    effective_argv = recorded_argv or (
        tuple(argv) if argv is not None else tuple(sys.argv[1:])
    )
    recorded_args = dict(manifest_args) if manifest_args is not None else vars(args)
    output_root = Path(args.output_root)
    authorization = resolve_live_authorization(
        input_manifest=args.input_manifest,
        materialize_live_input=args.materialize_live_input,
        live_materialization_authorized=args.live_materialization_authorized,
        run_profile=args.run_profile,
        requested_live_mode=(
            LiveRunMode.TEST_FIXTURE.value
            if args.mode == "test"
            else args.live_run_mode
        ),
    )
    if authorization.path == AuthorizationPath.REJECTED.value:
        return write_current_internal_materializer_pending_run(
            command=command_name,
            args=recorded_args,
            effective_argv=effective_argv,
            output_root=output_root,
            blockers=authorization.blocker_codes,
            authorization=authorization.to_dict(),
        )
    materialized_input_manifest: str | None = None
    materialized_live_root: Path | None = None
    if authorization.path == AuthorizationPath.LIVE_MATERIALIZATION.value:
        try:
            profile = load_live_run_profile(str(authorization.run_profile))
            if profile.run_mode != authorization.run_mode:
                raise ValueError("live run profile mode does not match CLI live mode")
            live_root = Path("output/live_materialization") / args.as_of_date
            inputs, builder_audit = CurrentOperationRunnerInputBuilder().build_from_live_root(
                as_of_date=args.as_of_date,
                live_root=live_root,
                run_profile=str(authorization.run_profile),
            )
            materialized_paths = write_current_operation_input_manifest(
                inputs,
                live_root=live_root,
            )
            builder_audit_path = live_root / "current_operation_input_builder_audit.json"
            builder_audit_path.write_text(
                json.dumps(builder_audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            materialized_input_manifest = str(materialized_paths["canonical_manifest"])
            materialized_live_root = live_root
        except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
            return write_current_internal_materializer_pending_run(
                command=command_name,
                args=recorded_args,
                effective_argv=effective_argv,
                output_root=output_root,
                blockers=("LIVE_RUN_PROFILE_INVALID",),
                authorization={
                    **authorization.to_dict(),
                    "profile_error_category": type(exc).__name__,
                },
            )
    input_manifest = materialized_input_manifest or _resolve_default_input_manifest(args)
    if input_manifest is None:
        return write_current_source_pending_run(
            command=command_name,
            args=recorded_args,
            effective_argv=effective_argv,
            output_root=output_root,
            blockers=(
                "CURRENT_KRX_UNIVERSE_AND_LIVE_SOURCE_INPUT_MANIFEST_UNAVAILABLE",
            ),
        )
    try:
        inputs = load_current_operation_runner_input(input_manifest)
        _validate_cli_input_contract(args=vars(args), inputs=inputs)
        result = run_current_daily_census(inputs)
        output_paths = dict(
            write_current_daily_census(result, output_root=output_root)
        )
        if materialized_live_root is not None:
            output_paths.update(
                package_live_current_operation(
                    result=result,
                    live_root=materialized_live_root,
                    input_manifest=input_manifest,
                    output_root=output_root,
                    run_mode=authorization.run_mode,
                )
            )
        if command_name == "run_e2r_census_mode":
            output_paths.update(
                package_live_census_operation(
                    result=result,
                    output_root=output_root,
                    shard_count=int(recorded_args.get("shard_count", 1)),
                    resume=bool(recorded_args.get("resume", False)),
                )
            )
        runtime_critical = int(result.audit["critical_count_sum"])
        exit_code = (
            2 if args.fail_on_critical and runtime_critical else 0
        )
        semantic_status = (
            "CURRENT_OPERATIONAL_BRAIN_PASS"
            if runtime_critical == 0
            else "CURRENT_OPERATIONAL_BRAIN_FAIL"
        )
        command_manifest = _build_current_command_manifest(
            command=command_name,
            args=recorded_args,
            effective_argv=effective_argv,
            input_manifest=input_manifest,
            inputs=inputs,
            output_root=output_root,
            output_paths=output_paths,
            semantic_status=semantic_status,
            exit_code=exit_code,
            runtime_critical=runtime_critical,
        )
        output_paths.update(
            write_command_run_manifest(command_manifest, output_root=output_root)
        )
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        return _write_current_rejected_run(
            command=command_name,
            args=recorded_args,
            effective_argv=effective_argv,
            output_root=output_root,
            error=f"{type(exc).__name__}: {exc}",
        )
    print(
        json.dumps(
            {
                **dict(result.manifest),
                "command": command_name,
                "command_status": semantic_status,
                "command_run_id": command_manifest["run_id"],
                "command_hashes": {
                    key: command_manifest[key]
                    for key in (
                        "commit_hash",
                        "config_hash",
                        "corpus_hash",
                        "memory_hash",
                        "recipe_hash",
                        "prompt_hash",
                        "source_hash",
                        "repo_dirty",
                        "dirty_status_hash",
                    )
                },
                "output_paths": {
                    key: str(value) for key, value in output_paths.items()
                },
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return exit_code


def write_current_source_pending_run(
    *,
    command: str,
    args: Mapping[str, Any],
    effective_argv: tuple[str, ...],
    output_root: str | Path,
    blockers: tuple[str, ...],
) -> int:
    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=True)
    pending_path = root / "current_operation_source_pending.json"
    pending_payload = {
        "schema_version": "e2r_current_operation_source_pending_v1",
        "status": "EXTERNAL_SOURCE_BLOCKER_NOT_READY",
        "as_of_date": args.get("as_of_date"),
        "universe": args.get("universe"),
        "mode": args.get("mode"),
        "blockers": list(blockers),
        "score_valid": False,
        "raw_reference_score": None,
        "canonical_stage": "0",
        "production_runtime_ready": False,
    }
    pending_path.write_text(
        json.dumps(pending_payload, ensure_ascii=False, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )
    repo_root = Path(__file__).resolve().parents[3]
    recipe_path = repo_root / "configs" / "e2r_evidence_recipe_semantics_v1.json"
    planner_path = (
        repo_root
        / "src"
        / "e2r"
        / "research_brain"
        / "planning"
        / "two_pass_brain_planner.py"
    )
    manifest = build_command_run_manifest(
        command=command,
        semantic_status="EXTERNAL_SOURCE_BLOCKER_NOT_READY",
        exit_code=3,
        argv=effective_argv,
        output_root=root,
        repo_root=repo_root,
        hash_inputs={
            "config": (
                command_inline_hash_entry("pending-current-config", dict(args)),
            ),
            "corpus": (
                command_inline_hash_entry(
                    "pending-current-universe",
                    {
                        "universe": args.get("universe"),
                        "state": "LIVE_UNIVERSE_INPUT_NOT_MATERIALIZED",
                    },
                ),
            ),
            "memory": (
                command_inline_hash_entry(
                    "pending-current-memory",
                    {"state": "NO_CURRENT_CLAIM_LEDGER_INPUT"},
                ),
            ),
            "recipe": (
                command_file_hash_entry("pending-current-recipes", recipe_path),
            ),
            "prompt": (
                command_file_hash_entry("pending-current-planner", planner_path),
            ),
            "source": (
                command_file_hash_entry("pending-current-source-leaf", pending_path),
            ),
        },
        blockers=blockers,
        runtime_critical_count_sum=0,
    )
    paths = write_command_run_manifest(manifest, output_root=root)
    print(
        json.dumps(
            {
                **pending_payload,
                "command": command,
                "command_run_id": manifest["run_id"],
                "command_hashes": {
                    key: manifest[key]
                    for key in (
                        "commit_hash",
                        "config_hash",
                        "corpus_hash",
                        "memory_hash",
                        "recipe_hash",
                        "prompt_hash",
                        "source_hash",
                        "repo_dirty",
                        "dirty_status_hash",
                    )
                },
                "output_paths": {
                    "pending": str(pending_path),
                    **{key: str(path) for key, path in paths.items()},
                },
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 3


def write_current_internal_materializer_pending_run(
    *,
    command: str,
    args: Mapping[str, Any],
    effective_argv: tuple[str, ...],
    output_root: str | Path,
    blockers: tuple[str, ...],
    authorization: Mapping[str, Any],
) -> int:
    """Record an internal live-path blocker without mislabelling it external."""

    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=True)
    pending_path = root / "live_materialization_internal_pending.json"
    pending_payload = {
        "schema_version": "e2r_live_materialization_internal_pending_v1",
        "status": "INTERNAL_E2R_RUNTIME_NOT_READY",
        "as_of_date": args.get("as_of_date"),
        "universe": args.get("universe"),
        "mode": args.get("mode"),
        "blockers": list(blockers),
        "authorization": dict(authorization),
        "materializer_called": False,
        "score_valid": False,
        "raw_reference_score": None,
        "canonical_stage": "0",
        "production_runtime_ready": False,
    }
    pending_path.write_text(
        json.dumps(pending_payload, ensure_ascii=False, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )
    repo_root = Path(__file__).resolve().parents[3]
    manifest = build_command_run_manifest(
        command=command,
        semantic_status="INTERNAL_E2R_RUNTIME_NOT_READY",
        exit_code=2,
        argv=effective_argv,
        output_root=root,
        repo_root=repo_root,
        hash_inputs={
            "config": (
                command_inline_hash_entry(
                    "live-materialization-authorization",
                    {"args": dict(args), "authorization": dict(authorization)},
                ),
            ),
            "corpus": (
                command_inline_hash_entry(
                    "live-materialization-universe-state",
                    {"state": "NOT_MATERIALIZED_INTERNAL_PATH_INCOMPLETE"},
                ),
            ),
            "memory": (
                command_inline_hash_entry(
                    "live-materialization-ledger-state",
                    {"state": "NOT_LOADED_INTERNAL_PATH_INCOMPLETE"},
                ),
            ),
            "recipe": (
                command_file_hash_entry(
                    "live-materialization-config",
                    repo_root / "configs" / "e2r_live_materialization_v1.json",
                ),
            ),
            "prompt": (
                command_file_hash_entry(
                    "live-materialization-authorization-source",
                    repo_root
                    / "src"
                    / "e2r"
                    / "research_brain"
                    / "runtime"
                    / "live_materialization"
                    / "authorization.py",
                ),
            ),
            "source": (
                command_file_hash_entry(
                    "live-materialization-internal-pending-leaf", pending_path
                ),
            ),
        },
        blockers=blockers,
        runtime_critical_count_sum=1,
    )
    paths = write_command_run_manifest(manifest, output_root=root)
    print(
        json.dumps(
            {
                **pending_payload,
                "command": command,
                "command_run_id": manifest["run_id"],
                "output_paths": {
                    "pending": str(pending_path),
                    **{key: str(path) for key, path in paths.items()},
                },
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 2


def _resolve_default_input_manifest(args: argparse.Namespace) -> Path | None:
    if args.input_manifest:
        path = Path(args.input_manifest)
        return path if path.is_file() else path
    candidates = (
        Path("output/current_operation_inputs")
        / f"{args.as_of_date}.json",
        Path("data/current_operation") / f"{args.as_of_date}.json",
    )
    return next((path for path in candidates if path.is_file()), None)


def _validate_cli_input_contract(
    *,
    args: Mapping[str, Any],
    inputs: CurrentOperationRunnerInput,
) -> None:
    if inputs.as_of_date != args["as_of_date"]:
        raise ValueError("CLI and input manifest as_of_date differ")
    if args["universe"] != "krx":
        raise ValueError("canonical current operation currently requires krx universe")
    if args["mode"] == "production_bounded" and inputs.config.test_mode:
        raise ValueError("test fixture manifest cannot run as production_bounded")
    if (
        args["mode"] == "production_bounded"
        and not inputs.config.require_claim_provenance
    ):
        raise ValueError(
            "production_bounded input must enforce source-backed claim provenance"
        )
    if args["mode"] == "test" and not inputs.config.test_mode:
        raise ValueError("production manifest cannot run under test mode")


def _build_current_command_manifest(
    *,
    command: str,
    args: Mapping[str, Any],
    effective_argv: tuple[str, ...],
    input_manifest: Path,
    inputs: CurrentOperationRunnerInput,
    output_root: Path,
    output_paths: Mapping[str, Path],
    semantic_status: str,
    exit_code: int,
    runtime_critical: int,
) -> Mapping[str, Any]:
    repo_root = Path(__file__).resolve().parents[3]
    provider_traces = tuple(
        {
            "target_id": item.target_id,
            "provider_kind": item.provider_kind,
            "provider_trace_id": item.provider_trace_id,
            "llm_calls": item.llm_calls,
        }
        for item in inputs.deep_executions
    )
    return build_command_run_manifest(
        command=command,
        semantic_status=semantic_status,
        exit_code=exit_code,
        argv=effective_argv,
        output_root=output_root,
        repo_root=repo_root,
        hash_inputs={
            "config": (
                command_inline_hash_entry(
                    "current-cli-and-runner-config",
                    {"cli": dict(args), "runner": inputs.config.to_dict()},
                ),
                command_file_hash_entry("current-input-manifest", input_manifest),
            ),
            "corpus": (
                command_file_hash_entry(
                    "current-universe-leaves", output_paths["universe"]
                ),
                command_file_hash_entry(
                    "current-baseline-leaves", output_paths["baseline"]
                ),
            ),
            "memory": (
                command_inline_hash_entry(
                    "current-claim-ledger",
                    [item.to_dict() for item in inputs.claims],
                ),
                command_file_hash_entry(
                    "current-last-effective-theses", output_paths["theses"]
                ),
            ),
            "recipe": (
                command_file_hash_entry(
                    "current-recipe-semantics",
                    repo_root / "configs" / "e2r_evidence_recipe_semantics_v1.json",
                ),
                command_file_hash_entry(
                    "current-question-source-tasks", output_paths["source_tasks"]
                ),
            ),
            "prompt": (
                command_inline_hash_entry(
                    "current-provider-traces", list(provider_traces)
                ),
                command_file_hash_entry(
                    "current-investigation-prompt-contract",
                    repo_root
                    / "src"
                    / "e2r"
                    / "research_brain"
                    / "runtime"
                    / "adaptive_investigation_controller.py",
                ),
            ),
            "source": (
                command_file_hash_entry(
                    "current-claim-provenance",
                    output_paths["claim_provenance"],
                ),
                command_file_hash_entry(
                    "current-source-timelines", output_paths["timelines"]
                ),
                command_file_hash_entry(
                    "current-atomic-decisions", output_paths["decisions"]
                ),
                command_file_hash_entry(
                    "current-terminal-executions", output_paths["executions"]
                ),
            ),
        },
        blockers=(
            ()
            if runtime_critical == 0
            else ("CURRENT_OPERATION_CRITICAL_AUDIT_NONZERO",)
        ),
        runtime_critical_count_sum=runtime_critical,
    )


def _write_current_rejected_run(
    *,
    command: str,
    args: Mapping[str, Any],
    effective_argv: tuple[str, ...],
    output_root: Path,
    error: str,
) -> int:
    output_root.mkdir(parents=True, exist_ok=True)
    error_path = output_root / "current_operation_input_error.json"
    payload = {
        "schema_version": "e2r_current_operation_cli_v2",
        "command": command,
        "status": "CURRENT_OPERATION_INPUT_REJECTED",
        "error": error,
        "production_runtime_ready": False,
    }
    error_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    hash_inputs = {
        category: (
            command_inline_hash_entry(
                f"{category}-current-rejected",
                {"category": category, "inputs": dict(args), "error": error},
            ),
        )
        for category in REQUIRED_COMMAND_HASH_CATEGORIES
    }
    hash_inputs["source"] = (
        command_file_hash_entry("current-input-error-leaf", error_path),
    )
    manifest = build_command_run_manifest(
        command=command,
        semantic_status="CURRENT_OPERATION_INPUT_REJECTED",
        exit_code=2,
        argv=effective_argv,
        output_root=output_root,
        hash_inputs=hash_inputs,
        blockers=(error,),
        runtime_critical_count_sum=1,
    )
    paths = write_command_run_manifest(manifest, output_root=output_root)
    print(
        json.dumps(
            {
                **payload,
                "command_run_id": manifest["run_id"],
                "output_paths": {
                    "error": str(error_path),
                    **{key: str(path) for key, path in paths.items()},
                },
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
