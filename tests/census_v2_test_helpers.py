from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from e2r.census.census_runner_v2 import CensusV2RunConfig, run_census_mode_v2


_CACHE: dict[str, Any] | None = None


def census_v2_artifacts() -> dict[str, Any]:
    global _CACHE
    if _CACHE is None:
        output_root = Path("output/test_census_v2_cached")
        result = run_census_mode_v2(
            CensusV2RunConfig(
                as_of_date="2026-07-01",
                output_root=str(output_root),
                fail_on_critical_audit=True,
                write_operational_docs=False,
                test_result_summary="unit_test_cached_run",
            )
        )
        _CACHE = {
            "result": result,
            "output_root": output_root,
            "universe": read_jsonl(output_root / "universe.jsonl"),
            "events": read_jsonl(output_root / "census_assessment_events.jsonl"),
            "candidate_events": read_jsonl(output_root / "census_events.jsonl"),
            "timelines": read_jsonl(output_root / "source_timelines.jsonl"),
            "thesis_states": read_jsonl(output_root / "last_effective_thesis_states.jsonl"),
            "stage_rows": read_jsonl(output_root / "census_stage_status.jsonl"),
            "source_tasks": read_jsonl(output_root / "source_tasks.jsonl"),
            "accepted_claims": read_jsonl(output_root / "accepted_claims.jsonl"),
            "score_contributions": read_jsonl(output_root / "score_contributions.jsonl"),
            "audit": read_json(output_root / "audit_summary.json"),
            "summary": read_json(output_root / "census_stage_summary.json"),
            "baseline_summary": read_json(output_root / "baseline_inputs_summary.json"),
            "self_repair": read_json(output_root / "self_repair_log.json"),
        }
    return _CACHE


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
