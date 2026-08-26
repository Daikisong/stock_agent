"""Resume one fresh V3 canary through same-conversation full-thesis closure."""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import replace
import json
from pathlib import Path
import sys
from typing import Any, Mapping

from e2r.pro_first.config import load_pro_first_local_config
from e2r.pro_first.fresh_session import (
    FRESH_FULL_THESIS_AUTHORIZATION_PHRASE,
    FreshV3FullThesisLiveRunner,
)
from e2r.pro_first.ids import canonical_json


def _progress(payload: Mapping[str, Any]) -> None:
    print(canonical_json(payload), flush=True)


async def _run(args: argparse.Namespace) -> Mapping[str, Any]:
    fresh_root = Path(args.fresh_runtime_root).expanduser().resolve()
    config = replace(
        load_pro_first_local_config(args.config),
        runtime_root=fresh_root,
    )
    runner = FreshV3FullThesisLiveRunner(
        config,
        fresh_runtime_root=fresh_root,
        state_database_path=args.state_database_path,
        repo_root=args.repo_root,
        progress=_progress,
        max_completion_polls=args.max_completion_polls,
        max_tail_iterations=args.max_tail_iterations,
    )
    if args.inspect_only:
        return runner.inspect_current(job_id=args.job_id)
    return await runner.run(job_id=args.job_id)


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--fresh-runtime-root", required=True)
    parser.add_argument("--state-database-path", required=True)
    parser.add_argument("--job-id", required=True)
    parser.add_argument("--max-completion-polls", type=int, default=1_440)
    parser.add_argument("--max-tail-iterations", type=int, default=12)
    parser.add_argument(
        "--inspect-only",
        action="store_true",
        help="read deterministic current status without opening or sending ChatGPT",
    )
    parser.add_argument(
        "--authorization",
        help=(
            "live execution must equal "
            + FRESH_FULL_THESIS_AUTHORIZATION_PHRASE
        ),
    )
    args = parser.parse_args(argv)
    if (
        not args.inspect_only
        and args.authorization != FRESH_FULL_THESIS_AUTHORIZATION_PHRASE
    ):
        parser.error(
            "actual same-conversation ChatGPT Pro follow-ups require the exact authorization phrase"
        )
    try:
        result = asyncio.run(_run(args))
    except Exception as error:
        print(
            json.dumps(
                {
                    "schema_version": (
                        "e2r_pro_fresh_v3_full_thesis_failure_v1"
                    ),
                    "status": "FAILED_SAFE_NO_AUTOMATIC_RESUBMIT",
                    "error_class": type(error).__name__,
                    "error_message": str(error),
                    "automatic_initial_resubmit_allowed": False,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ),
            flush=True,
        )
        return 4
    print(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True),
        flush=True,
    )
    if args.inspect_only:
        return 0
    return 0 if result.get("status") == "FRESH_V3_FULL_THESIS_FINAL" else 3


if __name__ == "__main__":
    raise SystemExit(main())
