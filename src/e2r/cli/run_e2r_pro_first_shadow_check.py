"""Prepare real logged-in ChatGPT UI through send-ready without submitting."""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import replace
from datetime import datetime, timezone
import json
from pathlib import Path

from e2r.pro_first.acceptance import write_receipt
from e2r.pro_first.config import load_pro_first_local_config
from e2r.pro_first.job_store import ProFirstJobStore
from e2r.pro_first.operations import create_forced_validation_canary, prepare_job_in_logged_in_browser


async def _run(args: argparse.Namespace) -> dict:
    base = load_pro_first_local_config(args.config)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    config = replace(base, runtime_root=base.runtime_root / "shadow" / stamp)
    store = ProFirstJobStore(config.database_path)
    job = create_forced_validation_canary(
        store,
        symbol=args.symbol,
        company_name=args.company_name,
        as_of_date=args.as_of_date,
        archetype_ids=tuple(args.archetype_id),
    )
    screenshot = config.runtime_root / "private/live_shadow.png"
    try:
        prepared = await prepare_job_in_logged_in_browser(
            store,
            job_id=job.job_id,
            config=config,
            repo_root=args.repo_root,
            screenshot_path=screenshot,
        )
    except Exception as error:
        return {
            "schema_version": "e2r_pro_first_live_shadow_receipt_v1",
            "status": "CHATGPT_WEB_SHADOW_PENDING_USER_ENV",
            "error_class": type(error).__name__,
            "error_message": str(error),
            "submit_count": 0,
        }
    try:
        return dict(prepared.receipt)
    finally:
        await prepared.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--company-name", required=True)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--archetype-id", action="append", default=[])
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    result = asyncio.run(_run(args))
    if args.output:
        write_receipt(args.output, result)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["status"] == "CHATGPT_WEB_SHADOW_COMPATIBILITY_PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
