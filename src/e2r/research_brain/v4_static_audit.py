"""Static report audit for Research Brain v4."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.v4_production_orchestrator import build_static_logic_audit_from_reports_v4


def build_static_logic_audit_v4_from_report_dir(report_dir: str | Path) -> Mapping[str, Any]:
    root = Path(report_dir)
    planner = _load_json(root / "research_brain_v4_real_planner_report.json")
    source = _load_json(root / "research_brain_v4_source_acquisition_report.json")
    extraction = _load_json(root / "research_brain_v4_evidence_extraction_audit.json")
    watchlist = _load_json(root / "research_brain_v4_daily_watchlist_sample.json")
    config = _config_from_acceptance(root / "research_brain_v4_acceptance_report.md")
    return build_static_logic_audit_from_reports_v4(
        planner_report=planner,
        source_report=source,
        extraction_audit=extraction,
        watchlist_report=watchlist,
        config=config,
    )


def _load_json(path: Path) -> Mapping[str, Any]:
    if not path.exists():
        return {"summary": {}}
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        return {"summary": {}}
    return payload


def _config_from_acceptance(path: Path) -> Mapping[str, Any]:
    # Config values are also embedded in production shadow result before writing.
    # If this standalone audit is run after only JSON reports exist, use safe
    # bounded production defaults.
    return {"top_results": 20, "retry_max": 2}


__all__ = ["build_static_logic_audit_v4_from_report_dir"]
