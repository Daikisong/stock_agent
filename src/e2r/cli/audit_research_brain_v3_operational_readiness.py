"""Audit generated Research Brain v3 operational readiness reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.v3_static_audit import build_static_logic_audit_v3, write_static_logic_audit_v3


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audit Research Brain v3 operational readiness.")
    parser.add_argument("--report-dir", default="docs/operational")
    parser.add_argument("--output", default="docs/operational/research_brain_v3_static_logic_audit.json")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    root = Path(args.report_dir)
    result = {
        "source_task_audit": _read_json(root / "research_brain_v3_source_task_execution_audit.json"),
        "watchlist_report": _read_json(root / "research_brain_v3_daily_watchlist_sample.json"),
        "planner_report": _read_json(root / "research_brain_v3_real_planner_provider_report.json"),
        "raw_router_matrix": _read_json(root / "research_brain_v3_raw_event_router_matrix.json"),
        "readiness": _readiness_from_markdown(root / "research_brain_v3_production_readiness_verdict.md"),
    }
    source_quality = _read_json(root / "research_brain_v3_source_quality_promotion_report.json")
    frozen = _read_json(root / "research_brain_v3_frozen_daily_runs.json")
    audit = build_static_logic_audit_v3(result=result, source_quality_promotion=source_quality, frozen_daily_runs=frozen)
    path = write_static_logic_audit_v3(audit, args.output)
    print(path)
    return 0


def _read_json(path: Path) -> Mapping[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _readiness_from_markdown(path: Path) -> Mapping[str, Any]:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    production_ready = "production_ready: True" in text
    return {"summary": {"production_ready": production_ready}}


if __name__ == "__main__":
    raise SystemExit(main())
