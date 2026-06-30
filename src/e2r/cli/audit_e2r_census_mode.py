"""Audit a Census output directory."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.census.census_audit import audit_census_mode
from e2r.production.metadata import write_json


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", required=True)
    args = parser.parse_args(argv)
    root = Path(args.output_root)
    universe = _read_jsonl(root / "universe.jsonl")
    rows = _read_jsonl(root / "census_stage_status.jsonl")
    eligible = [row["symbol"] for row in universe if row.get("eligible_for_census")]
    audit = audit_census_mode(eligible_symbols=eligible, stage_status_rows=rows)
    write_json(root / "audit_summary.json", audit)
    print(audit["summary"]["status"])
    return 0 if audit["summary"]["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
