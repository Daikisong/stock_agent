"""Audit E2R Census Mode v2 artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.census.census_audit_v2 import audit_census_mode_v2
from e2r.production.metadata import write_json


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--write", default="true")
    args = parser.parse_args(argv)
    root = Path(args.output_root)
    universe = _read_jsonl(root / "universe.jsonl")
    stage_rows = _read_jsonl(root / "census_stage_status.jsonl")
    source_tasks = _read_jsonl(root / "source_tasks.jsonl")
    metadata = _read_json(root / "run_metadata.json")
    eligible = [str(row.get("symbol")).zfill(6) for row in universe if row.get("eligible_for_census", True)]
    audit = audit_census_mode_v2(
        eligible_symbols=eligible,
        stage_rows=stage_rows,
        source_tasks=source_tasks,
        report_metadata={"git_head_sha": metadata.get("git_head_sha")},
    )
    if str(args.write).lower() == "true":
        write_json(root / "audit_summary.json", audit)
    print(audit["summary"]["status"])
    return 0 if audit["summary"]["critical_count_sum"] == 0 else 1


def _read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if text:
                rows.append(json.loads(text))
    return rows


def _read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    raise SystemExit(main())
