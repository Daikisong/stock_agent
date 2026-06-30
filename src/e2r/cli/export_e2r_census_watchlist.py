"""Export watchlist seed candidates from a Census stage map."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.census.watchlist_seed_exporter import export_watchlist_seed
from e2r.production.metadata import write_json


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--as-of-date", required=True)
    args = parser.parse_args(argv)
    root = Path(args.output_root)
    rows = [json.loads(line) for line in (root / "census_stage_map.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    seed = export_watchlist_seed(rows, as_of_date=args.as_of_date)
    write_json(root / "watchlist_seed_candidates.json", seed)
    print(seed["seed_count"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
