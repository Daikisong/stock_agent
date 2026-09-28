"""Run or catch up the bounded local KRX scan into the durable Pro queue."""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import asdict
from datetime import datetime
import json
from zoneinfo import ZoneInfo

from e2r.pro_first.config import load_pro_first_local_config
from e2r.pro_first.models import ScanWindow
from e2r.pro_first.runtime import ProFirstLocalStack


async def _run(args: argparse.Namespace) -> list[dict]:
    config = load_pro_first_local_config(args.config)
    stack = ProFirstLocalStack(config, repo_root=args.repo_root)
    if args.as_of_date:
        window = ScanWindow(args.window)
        local = datetime.fromisoformat(
            f"{args.as_of_date}T{config.scheduler.morning_at if window is ScanWindow.MORNING else config.scheduler.evening_at}:00"
        ).replace(tzinfo=ZoneInfo("Asia/Seoul"))
        claimed = stack.store.claim_scan_run(
            as_of_date=args.as_of_date,
            scan_window=window,
            scheduled_for=local.isoformat(),
            catchup=True,
        )
        if claimed is None:
            return []
        receipt = await asyncio.to_thread(stack.schedule_service.pipeline.run_claimed_window, claimed)
        return [asdict(receipt)]
    return [asdict(row) for row in await stack.schedule_service.run_once()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--as-of-date")
    parser.add_argument("--window", choices=[row.value for row in ScanWindow], default="MORNING")
    args = parser.parse_args(argv)
    rows = asyncio.run(_run(args))
    print(json.dumps({"scan_receipts": rows}, ensure_ascii=False, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
