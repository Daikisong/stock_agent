"""Audit production cutover readiness from generated reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping

from e2r.production.metadata import write_json


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shadow-report", default="docs/operational/production_cutover_shadow_latest.json")
    parser.add_argument("--static-audit", default="docs/operational/production_cutover_static_logic_audit.json")
    parser.add_argument("--output", default="docs/operational/production_cutover_static_logic_audit.json")
    args = parser.parse_args(argv)
    shadow = _json(Path(args.shadow_report))
    static = _json(Path(args.static_audit))
    audit = audit_production_cutover_readiness(shadow=shadow, static=static)
    write_json(Path(args.output), audit)
    print(json.dumps(audit["summary"], ensure_ascii=False, indent=2))
    return 0 if audit["summary"]["critical_count_sum"] == 0 else 2


def audit_production_cutover_readiness(
    *,
    shadow: Mapping[str, Any],
    static: Mapping[str, Any],
) -> Mapping[str, Any]:
    summary = dict(static.get("summary", {}))
    ready_claim = bool(shadow.get("production_ready") or shadow.get("production_verdict") == "READY")
    blockers = list(shadow.get("blockers") or summary.get("production_blockers") or ())
    summary["production_ready_with_blockers_count"] = int(ready_claim and bool(blockers))
    summary["critical_count_sum"] = sum(
        int(value)
        for key, value in summary.items()
        if key.endswith("_count") and key not in {"warning_count"}
    )
    summary["critical_audit_pass"] = summary["critical_count_sum"] == 0
    return {
        "schema_version": "production_cutover_static_logic_audit_v1",
        "summary": summary,
    }


def _json(path: Path) -> Mapping[str, Any]:
    if not path.exists():
        return {"summary": {}}
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    raise SystemExit(main())
