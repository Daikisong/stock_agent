"""CLI stub for official historical source backfill planning.

The command is intentionally conservative in tests and default runs: it writes
a backfill plan and creates the official history directory structure, but does
not execute live network calls without a future executor.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Sequence

from e2r.models import Market


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Plan official Korea history backfill.")
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--market", choices=[item.value for item in Market], default=Market.KR.value)
    parser.add_argument("--output-directory", default="data/historical_official")
    parser.add_argument("--max-opendart-detail-fetches-per-day", type=int, default=50)
    parser.add_argument("--execute-live", action="store_true", help="Reserved for future controlled live backfill executor.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    start = date.fromisoformat(args.start_date)
    end = date.fromisoformat(args.end_date)
    if end < start:
        raise SystemExit("end-date cannot be before start-date")
    root = Path(args.output_directory)
    for name in ("universe", "prices", "disclosures", "financials", "risks", "raw"):
        (root / name).mkdir(parents=True, exist_ok=True)
    plan = {
        "start_date": start.isoformat(),
        "end_date": end.isoformat(),
        "market": args.market,
        "execute_live": bool(args.execute_live),
        "network_calls_executed": False,
        "benchmark_labels_used": False,
        "snapshot_derived_universe_used": False,
        "max_opendart_detail_fetches_per_day": args.max_opendart_detail_fetches_per_day,
        "planned_sources": [
            "KRX/data.go.kr listed universe by date or nearest available date",
            "KRX/data.go.kr stock prices for date ranges",
            "OpenDART disclosure list by date range",
            "OpenDART detail XML for watch disclosures",
            "data.go.kr financial actuals when available",
        ],
        "notes": [
            "This checkpoint keeps live backfill as a plan/stub; tests do not call network.",
            "Universe must come from official history, not search/report snapshots.",
        ],
    }
    path = root / "backfill_plan.json"
    path.write_text(json.dumps(plan, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    print(f"backfill_plan={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
