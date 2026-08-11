"""Resume and verify the canonical Phase 108/109 operational acceptance."""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Mapping
from zoneinfo import ZoneInfo

from e2r.cli.compile_e2r_v6_artifact_lifecycle import (
    _open_or_create_directory_no_symlinks,
    _write_json_atomic,
)
from e2r.production.v6_operational_acceptance import (
    OPERATIONAL_ACCEPTANCE_PASS,
    run_operational_acceptance_phases,
)
from e2r.research_brain.researcher_mode.artifact_lifecycle import FINAL_ROOT_RELATIVE


def _bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    normalized = value.strip().casefold()
    if normalized in {"true", "1", "yes"}:
        return True
    if normalized in {"false", "0", "no"}:
        return False
    raise argparse.ArgumentTypeError("expected true or false")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--as-of-date",
        default=datetime.now(ZoneInfo("Asia/Seoul")).date().isoformat(),
    )
    parser.add_argument("--live-materialization-authorized", type=_bool, required=True)
    parser.add_argument("--research-provider", choices=("codex-collaboration",), required=True)
    parser.add_argument("--verify-existing-c06-receipts", type=_bool, default=True)
    parser.add_argument("--run-cross-archetype-canaries", type=_bool, default=True)
    parser.add_argument("--run-current-krx-census", type=_bool, default=True)
    parser.add_argument("--checkpoint-resume", type=_bool, default=True)
    parser.add_argument("--export-tracked-receipts", type=_bool, default=True)
    parser.add_argument("--run-clean-clone-verification", type=_bool, default=True)
    parser.add_argument("--run-full-tests", type=_bool, default=True)
    parser.add_argument(
        "--run-profile",
        default="configs/e2r_census_selective_deep_v1.json",
    )
    parser.add_argument(
        "--output-root",
        default="output/e2r_v6_operational_acceptance",
    )
    return parser


def _output_path_inside_repo(repo: Path, value: str) -> Path:
    raw = Path(value)
    supplied = Path(os.path.abspath(raw if raw.is_absolute() else repo / raw))
    if supplied == repo or repo not in supplied.parents:
        raise ValueError("operational output root must remain below the repository")
    current = repo
    for part in supplied.relative_to(repo).parts:
        current /= part
        if current.is_symlink():
            raise ValueError("operational output root cannot traverse a symlink")
    return supplied


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    required_flags = {
        "live_materialization_authorized": args.live_materialization_authorized,
        "verify_existing_c06_receipts": args.verify_existing_c06_receipts,
        "run_cross_archetype_canaries": args.run_cross_archetype_canaries,
        "run_current_krx_census": args.run_current_krx_census,
        "checkpoint_resume": args.checkpoint_resume,
        "export_tracked_receipts": args.export_tracked_receipts,
        "run_clean_clone_verification": args.run_clean_clone_verification,
        "run_full_tests": args.run_full_tests,
    }
    disabled = sorted(key for key, enabled in required_flags.items() if not enabled)
    if disabled:
        raise SystemExit(
            "canonical operational acceptance requires every phase flag: "
            + ",".join(disabled)
        )
    repo = Path(args.repo_root).resolve()
    output_root = _output_path_inside_repo(repo, args.output_root)
    output_descriptor = _open_or_create_directory_no_symlinks(output_root)
    os.close(output_descriptor)
    checkpoint = output_root / "operational_acceptance_checkpoint.json"
    reviewer_gate = output_root / "operational_reviewer_gate_k_v.json"
    prior: Mapping[str, object] | None = None
    if args.checkpoint_resume and checkpoint.is_file() and not checkpoint.is_symlink():
        try:
            loaded = json.loads(checkpoint.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise SystemExit("operational checkpoint is invalid") from exc
        if not isinstance(loaded, Mapping):
            raise SystemExit("operational checkpoint must be a JSON object")
        prior = loaded
    result = run_operational_acceptance_phases(
        repo_root=repo,
        final_root=FINAL_ROOT_RELATIVE,
        output_root=output_root,
        as_of_date=args.as_of_date,
        research_provider=args.research_provider,
        run_profile=args.run_profile,
        checkpoint_resume=args.checkpoint_resume,
        prior_checkpoint=prior,
        checkpoint_writer=lambda payload: _write_json_atomic(checkpoint, payload),
    )
    rendered = {
        **result,
        "command_contract": {
            "research_provider": args.research_provider,
            "required_flags": required_flags,
            "checkpoint_resume": True,
            "fixed_retry_count_is_completion_authority": False,
        },
        "output_paths": {
            "checkpoint": str(checkpoint),
            "reviewer_gate": (
                str(reviewer_gate) if isinstance(result.get("reviewer_gate"), Mapping) else None
            ),
        },
    }
    _write_json_atomic(checkpoint, rendered)
    if isinstance(result.get("reviewer_gate"), Mapping):
        _write_json_atomic(reviewer_gate, result["reviewer_gate"])
    print(json.dumps(rendered, ensure_ascii=False, sort_keys=True, allow_nan=False))
    if result["status"] == OPERATIONAL_ACCEPTANCE_PASS:
        return 0
    return 3 if result["blockers"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
