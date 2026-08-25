"""Run one user-authorized fresh ChatGPT Chat+Pro Initial V3 canary."""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import replace
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
from typing import Any, Mapping

from e2r.pro_first.config import load_pro_first_local_config
from e2r.pro_first.fresh_session import (
    FRESH_LIVE_AUTHORIZATION_PHRASE,
    FreshInitialCanarySpec,
    FreshV3InitialLiveCanaryRunner,
)
from e2r.pro_first.ids import canonical_json


def _progress(payload: Mapping[str, Any]) -> None:
    print(canonical_json(payload), flush=True)


async def _run(args: argparse.Namespace) -> Mapping[str, Any]:
    base = load_pro_first_local_config(args.config)
    fresh_root = Path(args.fresh_runtime_root).expanduser().resolve()
    config = replace(base, runtime_root=fresh_root)
    runner = FreshV3InitialLiveCanaryRunner(
        config,
        old_runtime_root=args.old_runtime_root,
        fresh_runtime_root=fresh_root,
        repo_root=args.repo_root,
        progress=_progress,
        max_completion_polls=args.max_completion_polls,
        state_database_path=args.state_database_path,
    )
    spec = FreshInitialCanarySpec(
        old_job_id=args.old_job_id,
        old_run_id=args.old_run_id,
        old_conversation_id=args.old_conversation_id,
        fresh_session_id=args.fresh_session_id,
        archetype_ids=tuple(args.archetype),
        old_score_values=tuple(args.old_score),
        old_stage_values=tuple(args.old_stage),
    )
    if args.resume_submitted_job_id:
        return await runner.resume_submitted(
            spec,
            commit_sha=args.commit_sha,
            submitted_job_id=args.resume_submitted_job_id,
        )
    return await runner.run(
        spec,
        commit_sha=args.commit_sha,
        resume_prepared_job_id=args.resume_prepared_job_id,
    )


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--old-runtime-root", required=True)
    parser.add_argument("--fresh-runtime-root", required=True)
    parser.add_argument(
        "--state-database-path",
        help=(
            "central durable pro_first.sqlite3 path; defaults to "
            "OLD_RUNTIME_ROOT/pro_first.sqlite3. Use this when the immediate "
            "predecessor artifacts live in a newer runtime root while all job "
            "identities remain in the original durable ledger."
        ),
    )
    parser.add_argument("--old-job-id", required=True)
    parser.add_argument("--old-run-id", required=True)
    parser.add_argument("--old-conversation-id", required=True)
    parser.add_argument(
        "--fresh-session-id",
        default=(
            "FRESH-V2-1-"
            + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        ),
    )
    parser.add_argument("--archetype", action="append", required=True)
    parser.add_argument("--old-score", action="append", default=[])
    parser.add_argument("--old-stage", action="append", default=[])
    parser.add_argument("--commit-sha", required=True)
    recovery = parser.add_mutually_exclusive_group()
    recovery.add_argument(
        "--resume-prepared-job-id",
        help=(
            "adopt one exact intact new-chat draft after preparation timed out; "
            "never uploads or fills the composer again"
        ),
    )
    recovery.add_argument(
        "--resume-submitted-job-id",
        help=(
            "reattach to one exact submit_count=1 request, canonicalize its "
            "conversation from exact job/run markers, and continue without DOM send"
        ),
    )
    parser.add_argument("--max-completion-polls", type=int, default=1_440)
    parser.add_argument(
        "--authorization",
        required=True,
        help=f"must equal {FRESH_LIVE_AUTHORIZATION_PHRASE}",
    )
    args = parser.parse_args(argv)
    if args.authorization != FRESH_LIVE_AUTHORIZATION_PHRASE:
        parser.error(
            "actual ChatGPT Chat+Pro submission requires the exact authorization phrase"
        )
    try:
        result = asyncio.run(_run(args))
    except Exception as error:
        print(
            json.dumps(
                {
                    "schema_version": "e2r_pro_fresh_initial_live_run_failure_v1",
                    "status": "FAILED_SAFE_NO_AUTOMATIC_RESUBMIT",
                    "error_class": type(error).__name__,
                    "error_message": str(error),
                    "automatic_resubmit_allowed": False,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ),
            flush=True,
        )
        return 4
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    return 0 if result["receipt"]["status"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
