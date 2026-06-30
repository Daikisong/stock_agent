"""Build a Census deep backfill plan from a stage map."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.census.census_backfill_plan import build_deep_backfill_plan
from e2r.production.metadata import write_json


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--shard-count", type=int, default=10)
    args = parser.parse_args(argv)
    root = Path(args.output_root)
    rows = [json.loads(line) for line in (root / "census_stage_map.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    plan = build_deep_backfill_plan(rows, shard_count=args.shard_count)
    write_json(root / "deep_backfill_plan.json", plan)
    print(plan["shard_count"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
