from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path
from typing import Any

from e2r.census.census_runner_v3 import CensusV3RunConfig, run_census_mode_v3


_CACHE: dict[str, Any] | None = None


def census_v3_artifacts() -> dict[str, Any]:
    global _CACHE
    if _CACHE is None:
        output_root = Path("output/test_census_v3_cached")
        result = run_census_mode_v3(
            CensusV3RunConfig(
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
            "leaf_audit": read_json(output_root / "leaf_artifact_audit.json"),
            "stage_rows": read_jsonl(output_root / "census_stage_status.jsonl"),
            "trace_rows": read_jsonl(output_root / "claim_to_stage_trace.jsonl"),
            "source_tasks": read_jsonl(output_root / "source_tasks.jsonl"),
            "source_task_executions": read_jsonl(output_root / "source_task_executions.jsonl"),
            "accepted_claims": read_jsonl(output_root / "accepted_claims.jsonl"),
            "score_contributions": read_jsonl(output_root / "score_contributions.jsonl"),
            "timelines": read_jsonl(output_root / "source_timelines.jsonl"),
            "thesis_states": read_jsonl(output_root / "last_effective_thesis_states.jsonl"),
            "events": read_jsonl(output_root / "census_events.jsonl"),
            "reviewer_a": read_json(output_root / "reviewer_A_trace_audit.json"),
            "reviewer_b": read_json(output_root / "reviewer_B_source_audit.json"),
            "reviewer_c": read_json(output_root / "reviewer_C_stage_audit.json"),
            "self_repair": read_json(output_root / "self_repair_log.json"),
        }
    return _CACHE


def temp_census_v3_copy() -> tuple[tempfile.TemporaryDirectory, Path]:
    artifacts = census_v3_artifacts()
    tmp = tempfile.TemporaryDirectory()
    dst = Path(tmp.name) / "census_v3"
    shutil.copytree(artifacts["output_root"], dst)
    return tmp, dst


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if text:
                rows.append(json.loads(text))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
