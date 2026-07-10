"""Audit canonical E2R runtime evidence through independent A-E leaf reviewers."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Mapping

from e2r.production.metadata import git_head_sha, stable_hash, write_json
from e2r.research_brain.runtime.command_manifest import (
    REQUIRED_COMMAND_HASH_CATEGORIES,
    audit_command_run_manifest,
    build_command_run_manifest,
    command_file_hash_entry,
    command_inline_hash_entry,
    write_command_run_manifest,
)
from e2r.research_brain.runtime.independent_review import (
    run_independent_review,
    write_independent_review,
)


FINAL_AUDIT_SCHEMA_VERSION = "e2r_final_runtime_audit_v1"
_READY = "MEANINGFUL_E2R_RUNTIME_READY"
_EXTERNAL = "EXTERNAL_SOURCE_BLOCKER_NOT_READY"
_INTERNAL = "INTERNAL_E2R_RUNTIME_NOT_READY"


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
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--compile-root", default="output/research_intelligence/v1"
    )
    parser.add_argument(
        "--replay-root", default="output/historical_replay/v1"
    )
    parser.add_argument(
        "--current-root", default="output/current_operation/v1"
    )
    parser.add_argument("--census-root", default="output/census_v_next")
    parser.add_argument(
        "--funnel-root", default="output/conversion_funnel/v1"
    )
    parser.add_argument("--output-root", default="output/final_e2r_audit/v1")
    parser.add_argument("--require-live-current", type=_parse_bool, default=True)
    parser.add_argument("--fail-on-critical", type=_parse_bool, default=True)
    args = parser.parse_args(argv)
    effective_argv = tuple(argv) if argv is not None else tuple(sys.argv[1:])
    repo_root = Path(args.repo_root).resolve()
    output_root = Path(args.output_root)
    roots = {
        "compile": Path(args.compile_root),
        "replay": Path(args.replay_root),
        "current": Path(args.current_root),
        "census": Path(args.census_root),
        "funnel": Path(args.funnel_root),
    }

    review = run_independent_review(
        compile_root=roots["compile"],
        replay_root=roots["replay"],
        current_root=roots["current"],
        repo_root=repo_root,
        funnel_root=roots["funnel"],
        require_live_current=args.require_live_current,
    )
    reviewer_paths = dict(
        write_independent_review(review, output_root=output_root)
    )
    component_commands = {
        "compile": _audit_component_command(
            roots["compile"],
            expected_command="compile_e2r_research_intelligence",
            expected_status="COMPILE_RUN_PASS",
            repo_root=repo_root,
        ),
        "replay": _audit_component_command(
            roots["replay"],
            expected_command="run_e2r_historical_replay",
            expected_status="HISTORICAL_REPLAY_PARITY_PASS",
            repo_root=repo_root,
        ),
        "current": _audit_component_command(
            roots["current"],
            expected_command="run_e2r_current_operation",
            expected_status="CURRENT_OPERATIONAL_BRAIN_PASS",
            repo_root=repo_root,
        ),
        "census": _audit_component_command(
            roots["census"],
            expected_command="run_e2r_census_mode",
            expected_status="CURRENT_OPERATIONAL_BRAIN_PASS",
            repo_root=repo_root,
        ),
    }
    current_live = _live_current_contract(roots["current"])
    census_live = _live_current_contract(roots["census"])
    current_census_parity = _current_census_leaf_parity(
        roots["current"], roots["census"]
    )
    dirty_paths = _dirty_paths(repo_root)
    command_critical = sum(
        int(item["critical_count_sum"]) for item in component_commands.values()
    )
    critical = {
        "live_current_requirement_disabled": int(
            not args.require_live_current
        ),
        "independent_reviewer_critical": review.critical_count_sum,
        "component_command_critical": command_critical,
        "current_live_contract_failure": int(
            args.require_live_current and not current_live["passed"]
        ),
        "census_live_contract_failure": int(
            args.require_live_current and not census_live["passed"]
        ),
        "current_census_leaf_mismatch": int(
            args.require_live_current and not current_census_parity["passed"]
        ),
        "working_tree_dirty": int(bool(dirty_paths)),
    }
    external_blockers = tuple(
        sorted(
            {
                blocker
                for name in ("current", "census")
                for blocker in component_commands[name]["blockers"]
                if _is_external_blocker(blocker)
            }
        )
    )
    if sum(critical.values()) == 0:
        final_status = _READY
    elif external_blockers:
        final_status = _EXTERNAL
    else:
        final_status = _INTERNAL
    blockers = tuple(
        dict.fromkeys(
            (
                *external_blockers,
                *(
                    ("INDEPENDENT_REVIEWER_CRITICAL_NONZERO",)
                    if review.critical_count_sum
                    else ()
                ),
                *(
                    ("COMPONENT_COMMAND_AUDIT_NONZERO",)
                    if command_critical
                    else ()
                ),
                *(("CURRENT_LIVE_CONTRACT_NOT_PROVEN",) if not current_live["passed"] else ()),
                *(("CENSUS_LIVE_CONTRACT_NOT_PROVEN",) if not census_live["passed"] else ()),
                *(("CURRENT_CENSUS_LEAF_PARITY_NOT_PROVEN",) if not current_census_parity["passed"] else ()),
                *(("WORKTREE_DIRTY",) if dirty_paths else ()),
            )
        )
    )
    final_payload = {
        "schema_version": FINAL_AUDIT_SCHEMA_VERSION,
        "status": final_status,
        "commit_hash": git_head_sha(repo_root),
        "repo_dirty": bool(dirty_paths),
        "dirty_paths": list(dirty_paths),
        "independent_review_status": review.status,
        "reviewer_verdicts": {
            item.reviewer_id: item.verdict for item in review.reviewers
        },
        "reviewer_critical_counts": {
            item.reviewer_id: item.critical_count_sum for item in review.reviewers
        },
        "component_commands": component_commands,
        "current_live_contract": current_live,
        "census_live_contract": census_live,
        "current_census_leaf_parity": current_census_parity,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "blockers": list(blockers),
        "production_runtime_ready": final_status == _READY,
    }
    final_payload["result_hash"] = stable_hash(final_payload)
    final_path = output_root / "final_runtime_audit.json"
    write_json(final_path, final_payload)

    exit_code = (
        0
        if final_status == _READY or not args.fail_on_critical
        else 3
        if final_status == _EXTERNAL
        else 2
    )
    command_manifest = build_command_run_manifest(
        command="audit_e2r_evidence_intelligence",
        semantic_status=final_status,
        exit_code=exit_code,
        argv=effective_argv,
        output_root=output_root,
        repo_root=repo_root,
        hash_inputs={
            "config": (
                command_inline_hash_entry("final-audit-config", vars(args)),
                *(
                    command_file_hash_entry(
                        f"{name}-command-manifest",
                        root / "command_run_manifest.json",
                    )
                    for name, root in roots.items()
                    if name != "funnel"
                    and (root / "command_run_manifest.json").is_file()
                ),
            ),
            "corpus": (
                command_file_hash_entry(
                    "reviewer-a-corpus-verdict", reviewer_paths["reviewer_a"]
                ),
            ),
            "memory": (
                command_file_hash_entry(
                    "reviewer-b-memory-verdict", reviewer_paths["reviewer_b"]
                ),
            ),
            "recipe": (
                command_file_hash_entry(
                    "reviewer-b-recipe-verdict", reviewer_paths["reviewer_b"]
                ),
            ),
            "prompt": (
                command_file_hash_entry(
                    "independent-reviewer-source",
                    repo_root
                    / "src"
                    / "e2r"
                    / "research_brain"
                    / "runtime"
                    / "independent_review.py",
                ),
                command_file_hash_entry("final-audit-cli-source", Path(__file__)),
            ),
            "source": (
                command_file_hash_entry(
                    "reviewer-c-source-verdict", reviewer_paths["reviewer_c"]
                ),
                command_file_hash_entry(
                    "reviewer-d-score-verdict", reviewer_paths["reviewer_d"]
                ),
                command_file_hash_entry(
                    "reviewer-e-mode-verdict", reviewer_paths["reviewer_e"]
                ),
                command_file_hash_entry("final-runtime-audit", final_path),
            ),
        },
        blockers=blockers,
        runtime_critical_count_sum=sum(critical.values()),
        production_runtime_ready=final_status == _READY,
    )
    command_paths = write_command_run_manifest(
        command_manifest, output_root=output_root
    )
    print(
        json.dumps(
            {
                **final_payload,
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
                    **{key: str(path) for key, path in reviewer_paths.items()},
                    "final_audit": str(final_path),
                    **{key: str(path) for key, path in command_paths.items()},
                },
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return exit_code


def _audit_component_command(
    root: Path,
    *,
    expected_command: str,
    expected_status: str,
    repo_root: Path,
) -> Mapping[str, Any]:
    path = root / "command_run_manifest.json"
    if not path.is_file():
        pending = root / "current_operation_source_pending.json"
        pending_payload = _read_json(pending)
        blockers = tuple(str(item) for item in pending_payload.get("blockers") or ())
        return {
            "passed": False,
            "critical_count_sum": 1,
            "critical_counts": {"command_manifest_missing": 1},
            "semantic_status": pending_payload.get("status"),
            "blockers": list(blockers),
        }
    payload = _read_json(path)
    audit = audit_command_run_manifest(payload)
    critical = {
        "reproducibility_audit_failure": int(audit["critical_count_sum"]),
        "command_identity_mismatch": int(payload.get("command") != expected_command),
        "component_commit_mismatch": int(
            payload.get("commit_hash") != git_head_sha(repo_root)
        ),
        "semantic_status_mismatch": int(
            payload.get("semantic_status") != expected_status
        ),
        "nonzero_exit": int(payload.get("exit_code") != 0),
        "component_run_was_dirty": int(payload.get("repo_dirty") is not False),
        "component_runtime_critical": int(
            _int(payload.get("runtime_critical_count_sum")) != 0
        ),
        "six_hashes_missing": sum(
            not _is_sha256(str(payload.get(f"{category}_hash") or ""))
            for category in REQUIRED_COMMAND_HASH_CATEGORIES
        ),
    }
    return {
        "passed": sum(critical.values()) == 0,
        "critical_count_sum": sum(critical.values()),
        "critical_counts": critical,
        "semantic_status": payload.get("semantic_status"),
        "commit_hash": payload.get("commit_hash"),
        "blockers": list(payload.get("blockers") or ()),
    }


def _live_current_contract(root: Path) -> Mapping[str, Any]:
    manifest = _read_json(root / "current_daily_census_manifest.json")
    provenance = _read_jsonl(root / "current_daily_claim_provenance.jsonl")
    executions = _read_jsonl(root / "current_daily_deep_executions.jsonl")
    passed = bool(
        manifest.get("status") == "BOUNDED_DAILY_CENSUS_PASS"
        and manifest.get("test_mode") is False
        and manifest.get("live_execution_observed") is True
        and provenance
        and executions
        and any(_int(item.get("fetches")) > 0 for item in executions)
        and all(
            item.get("test_only") is False
            and item.get("extraction_provider_kind") == "CODEX"
            and item.get("mapping_provider_kind") == "CODEX"
            for item in provenance
        )
    )
    return {
        "passed": passed,
        "run_id": manifest.get("run_id"),
        "as_of_date": manifest.get("as_of_date"),
        "provenance_count": len(provenance),
        "execution_count": len(executions),
    }


def _current_census_leaf_parity(
    current_root: Path,
    census_root: Path,
) -> Mapping[str, Any]:
    names = (
        "e2r_run_mode.json",
        "current_daily_universe.jsonl",
        "current_daily_claim_provenance.jsonl",
        "current_daily_source_timelines.jsonl",
        "current_daily_deep_executions.jsonl",
        "current_daily_atomic_decisions.jsonl",
        "current_daily_census_stage_statuses.jsonl",
    )
    mismatches: list[str] = []
    hashes: dict[str, str | None] = {}
    for name in names:
        left = current_root / name
        right = census_root / name
        left_hash = _file_sha256(left) if left.is_file() else None
        right_hash = _file_sha256(right) if right.is_file() else None
        hashes[name] = left_hash
        if left_hash is None or left_hash != right_hash:
            mismatches.append(name)
    return {
        "passed": not mismatches,
        "checked_leaf_count": len(names),
        "mismatched_leaves": mismatches,
        "current_leaf_hashes": hashes,
    }


def _read_json(path: Path) -> Mapping[str, Any]:
    if not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return {}
    return dict(payload) if isinstance(payload, Mapping) else {}


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    try:
        values = tuple(
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return ()
    return tuple(item for item in values if isinstance(item, Mapping))


def _file_sha256(path: Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _dirty_paths(repo_root: Path) -> tuple[str, ...]:
    try:
        output = subprocess.check_output(
            ["git", "status", "--porcelain"], cwd=repo_root, text=True
        )
    except (OSError, subprocess.CalledProcessError):
        return ("<git-status-unavailable>",)
    return tuple(sorted(line.rstrip() for line in output.splitlines() if line.strip()))


def _is_external_blocker(value: str) -> bool:
    normalized = value.upper()
    return any(
        token in normalized
        for token in ("EXTERNAL", "PROVIDER", "NETWORK", "LIVE_SOURCE", "UNAVAILABLE")
    )


def _is_sha256(value: str) -> bool:
    return len(value) == 64 and all(char in "0123456789abcdef" for char in value)


def _int(value: Any) -> int:
    return value if isinstance(value, int) and not isinstance(value, bool) else -1


if __name__ == "__main__":
    raise SystemExit(main())
