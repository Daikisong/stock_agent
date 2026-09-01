"""Run user-authorized actual ChatGPT Pro V2 multi-pass canaries."""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import replace
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
from typing import Any, Mapping

from e2r.pro_first.canary import (
    LiveCanarySpec,
    ProV2LiveCanaryRunner,
    run_live_canary_suite,
)
from e2r.pro_first.config import load_pro_first_local_config
from e2r.pro_first.ids import canonical_json


AUTHORIZATION_PHRASE = "YES-I-AUTHORIZE-LIVE-PRO"


def _progress(payload: Mapping[str, Any]) -> None:
    print(canonical_json(payload), flush=True)


def _parse_spec(value: str, *, as_of_date: str) -> LiveCanarySpec:
    # WSL -> ``cmd.exe /C`` can preserve the protective outer quotes as
    # literal argument bytes.  Remove only one balanced shell-quote pair;
    # quotes inside company names or archetype ids remain untouched.
    normalized = value.strip()
    if (
        len(normalized) >= 2
        and normalized[0] in {'"', "'"}
        and normalized[-1] == normalized[0]
    ):
        normalized = normalized[1:-1].strip()
    pieces = [piece.strip() for piece in normalized.split("|", 2)]
    if len(pieces) != 3 or not all(pieces):
        raise argparse.ArgumentTypeError(
            "--canary must be SYMBOL|COMPANY_NAME|ARCHETYPE_ID"
        )
    return LiveCanarySpec(
        symbol=pieces[0],
        company_name=pieces[1],
        archetype_id=pieces[2],
        as_of_date=as_of_date,
    )


async def _run(args: argparse.Namespace) -> Mapping[str, Any]:
    base = load_pro_first_local_config(args.config)
    if args.runtime_root:
        runtime_root = Path(args.runtime_root).expanduser().resolve()
    else:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        runtime_root = base.runtime_root / "live_v2" / stamp
    config = replace(base, runtime_root=runtime_root)
    specs = tuple(
        _parse_spec(value, as_of_date=args.as_of_date)
        for value in args.canary
    )
    runner = ProV2LiveCanaryRunner(
        config,
        repo_root=args.repo_root,
        progress=_progress,
        max_followup_passes=args.max_followup_passes,
        max_completion_polls=args.max_completion_polls,
        repair_pass_limit=args.repair_pass_limit,
    )
    if args.resume_job_id:
        if len(specs) != 1:
            raise ValueError("--resume-job-id requires exactly one --canary")
        if not args.runtime_root:
            raise ValueError("--resume-job-id requires the original --runtime-root")
        existing_job_ids = (args.resume_job_id,)
    else:
        existing_job_ids = None
    suite = await run_live_canary_suite(
        runner,
        specs,
        existing_job_ids=existing_job_ids,
    )
    output = runtime_root / "canary/live_v2_suite.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(canonical_json(suite) + "\n", encoding="utf-8")
    return {
        **suite,
        "runtime_root": str(runtime_root),
        "suite_receipt_path": str(output),
    }


def main(argv: list[str] | None = None) -> int:
    # Windows console defaults can still be cp949 even though all runtime
    # artifacts are UTF-8.  Progress logging must never turn a recoverable
    # browser error into a second UnicodeEncodeError.
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument(
        "--canary",
        action="append",
        required=True,
        help="SYMBOL|COMPANY_NAME|ARCHETYPE_ID; repeat for each mechanism",
    )
    parser.add_argument("--runtime-root")
    parser.add_argument(
        "--resume-job-id",
        help=(
            "resume one already-submitted durable job through visible chat "
            "history; never uploads or submits the initial prompt again"
        ),
    )
    parser.add_argument("--max-followup-passes", type=int, default=8)
    parser.add_argument("--max-completion-polls", type=int, default=1_440)
    parser.add_argument("--repair-pass-limit", type=int, default=4)
    parser.add_argument(
        "--authorization",
        required=True,
        help=f"must equal {AUTHORIZATION_PHRASE}",
    )
    args = parser.parse_args(argv)
    if args.authorization != AUTHORIZATION_PHRASE:
        parser.error("actual ChatGPT Pro submission requires the exact authorization phrase")
    result = asyncio.run(_run(args))
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    all_passed = bool(result.get("canary_count")) and result.get(
        "full_thesis_pass_count"
    ) == result.get("canary_count")
    return 0 if all_passed else 3


if __name__ == "__main__":
    raise SystemExit(main())
