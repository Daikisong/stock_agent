"""Run canonical frozen historical replay."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.replay import (
    CANONICAL_FROZEN_REPLAY_RUNNER_SCHEMA_VERSION,
    compile_canonical_frozen_replay,
    write_historical_replay_parity,
)
from e2r.research_brain.runtime.command_manifest import (
    REQUIRED_COMMAND_HASH_CATEGORIES,
    build_command_run_manifest,
    command_file_hash_entry,
    command_inline_hash_entry,
    write_command_run_manifest,
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default="canonical")
    parser.add_argument("--mode", default="blind_frozen_replay")
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--fail-on-critical", type=_parse_bool, default=True)
    args = parser.parse_args(argv)
    output_root = Path(args.output_root)
    effective_argv = tuple(argv) if argv is not None else (
        "--registry",
        args.registry,
        "--mode",
        args.mode,
        "--output-root",
        args.output_root,
        "--fail-on-critical",
        str(args.fail_on_critical).lower(),
    )
    if args.registry != "canonical" or args.mode != "blind_frozen_replay":
        return _write_rejected_run(
            args=vars(args),
            effective_argv=effective_argv,
            output_root=output_root,
            blocker="ONLY_CANONICAL_BLIND_FROZEN_REPLAY_IS_SUPPORTED",
        )
    try:
        bundle = compile_canonical_frozen_replay(repo_root=".")
        result = bundle.result
        output_paths = dict(
            write_historical_replay_parity(result, output_root=output_root)
        )
        runtime_critical = int(result.manifest["critical_count_sum"])
        passed = (
            result.manifest["status"] == "HISTORICAL_REPLAY_PARITY_PASS"
            and runtime_critical == 0
        )
        exit_code = 0 if passed or not args.fail_on_critical else 2
        semantic_status = (
            "HISTORICAL_REPLAY_PARITY_PASS"
            if passed
            else "HISTORICAL_REPLAY_PARITY_FAIL"
        )
        hash_inputs = {
            "config": (
                command_inline_hash_entry(
                    "historical-replay-cli-config",
                    {
                        **vars(args),
                        "runner_schema": (
                            CANONICAL_FROZEN_REPLAY_RUNNER_SCHEMA_VERSION
                        ),
                    },
                ),
            ),
            "corpus": (
                command_inline_hash_entry(
                    "canonical-corpus-artifacts",
                    list(bundle.input_artifact_hashes),
                ),
                command_inline_hash_entry(
                    "canonical-corpus-manifest",
                    dict(bundle.corpus_manifest),
                ),
            ),
            "memory": (
                command_inline_hash_entry(
                    "canonical-memory-manifest",
                    dict(bundle.memory_manifest),
                ),
                command_inline_hash_entry(
                    "canonical-retrieval-manifest",
                    dict(bundle.retrieval_manifest),
                ),
            ),
            "recipe": (
                command_inline_hash_entry(
                    "canonical-recipe-manifest",
                    dict(bundle.recipe_manifest),
                ),
            ),
            "prompt": (
                command_file_hash_entry(
                    "canonical-replay-runner-source",
                    Path(__file__).resolve().parents[1]
                    / "research_brain"
                    / "replay"
                    / "canonical_runner.py",
                ),
                command_file_hash_entry(
                    "blind-planner-input-leaves",
                    output_paths["planner_inputs"],
                ),
            ),
            "source": (
                command_inline_hash_entry(
                    "historical-source-manifest",
                    dict(bundle.source_manifest),
                ),
                command_file_hash_entry(
                    "historical-source-guard-leaves",
                    output_paths["guard_probes"],
                ),
                command_file_hash_entry(
                    "historical-source-resolution-leaves",
                    output_paths["archetype_rows"],
                ),
            ),
        }
        command_manifest = build_command_run_manifest(
            command="run_e2r_historical_replay",
            semantic_status=semantic_status,
            exit_code=exit_code,
            argv=effective_argv,
            output_root=output_root,
            hash_inputs=hash_inputs,
            blockers=(
                ()
                if passed
                else ("HISTORICAL_REPLAY_CRITICAL_AUDIT_NONZERO",)
            ),
            runtime_critical_count_sum=runtime_critical,
        )
        output_paths.update(
            write_command_run_manifest(command_manifest, output_root=output_root)
        )
    except (FileNotFoundError, OSError, TypeError, ValueError) as exc:
        return _write_rejected_run(
            args=vars(args),
            effective_argv=effective_argv,
            output_root=output_root,
            blocker=f"{type(exc).__name__}:{exc}",
        )

    payload = {
        **dict(result.manifest),
        "command": "run_e2r_historical_replay",
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
    }
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return exit_code


def _write_rejected_run(
    *,
    args: dict[str, object],
    effective_argv: tuple[str, ...],
    output_root: Path,
    blocker: str,
) -> int:
    output_root.mkdir(parents=True, exist_ok=True)
    error_path = output_root / "historical_replay_command_error.json"
    error_payload = {
        "schema_version": "e2r_historical_replay_command_error_v1",
        "status": "HISTORICAL_REPLAY_RUNTIME_FAIL",
        "blocker": blocker,
        "inputs": args,
        "production_runtime_ready": False,
    }
    error_path.write_text(
        json.dumps(error_payload, ensure_ascii=False, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )
    inline = {
        category: (
            command_inline_hash_entry(
                f"{category}-rejected-run",
                {
                    "category": category,
                    "inputs": args,
                    "blocker": blocker,
                },
            ),
        )
        for category in REQUIRED_COMMAND_HASH_CATEGORIES
    }
    inline["source"] = (
        command_file_hash_entry("historical-replay-error-leaf", error_path),
    )
    manifest = build_command_run_manifest(
        command="run_e2r_historical_replay",
        semantic_status="HISTORICAL_REPLAY_RUNTIME_FAIL",
        exit_code=2,
        argv=effective_argv,
        output_root=output_root,
        hash_inputs=inline,
        blockers=(blocker,),
        runtime_critical_count_sum=1,
    )
    paths = write_command_run_manifest(manifest, output_root=output_root)
    print(
        json.dumps(
            {
                **error_payload,
                "command_run_id": manifest["run_id"],
                "output_paths": {
                    "error": str(error_path),
                    **{key: str(value) for key, value in paths.items()},
                },
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
