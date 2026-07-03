from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from e2r.census.census_runner_v4 import CensusV4RunConfig, run_census_mode_v4


_CACHE: dict[str, Any] | None = None


def census_v4_artifacts() -> dict[str, Any]:
    global _CACHE
    if _CACHE is None:
        output_root = Path("output/test_census_v4_cached")
        result = run_census_mode_v4(
            CensusV4RunConfig(
                as_of_date="2026-07-01",
                output_root=str(output_root),
                v3_output_root="output/census_v3/2026-07-01",
                fail_on_critical_audit=True,
                write_operational_docs=False,
                test_result_summary="unit_test_cached_run",
                full_thesis_smoke_mode="controlled_replay",
            )
        )
        _CACHE = {
            "result": result,
            "output_root": output_root,
            "leaf_audit": read_json(output_root / "leaf_artifact_audit.json"),
            "artifact_manifest": read_json(output_root / "artifact_manifest.json"),
            "stage_summary": read_json(output_root / "census_stage_summary.json"),
            "stage_rows": read_jsonl(output_root / "census_stage_status.jsonl"),
            "sample_rows": read_jsonl(output_root / "sample_leaf_bundle.jsonl"),
            "atomic_rows": read_jsonl(output_root / "atomic_stage_decisions.jsonl"),
            "readiness": read_json(output_root / "readiness_verdict.json"),
        }
    return _CACHE


def by_symbol(rows: list[dict[str, Any]], symbol: str) -> dict[str, Any]:
    for row in rows:
        if row.get("symbol") == symbol:
            return row
    raise AssertionError(f"symbol not found: {symbol}")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if text:
                rows.append(json.loads(text))
    return rows
