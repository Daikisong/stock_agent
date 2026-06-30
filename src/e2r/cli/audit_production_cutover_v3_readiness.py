"""Audit generated Production Cutover Gate v3 reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping

from e2r.production.metadata import write_json


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--static-audit", default="docs/operational/production_cutover_v3_static_logic_audit.json")
    parser.add_argument("--readiness-verdict", default="docs/operational/production_cutover_v3_readiness_verdict.md")
    parser.add_argument("--output", default="docs/operational/production_cutover_v3_static_logic_audit.json")
    args = parser.parse_args(argv)
    static = _json(Path(args.static_audit))
    audit = audit_production_cutover_v3_readiness(static=static, verdict_text=_text(Path(args.readiness_verdict)))
    write_json(Path(args.output), audit)
    print(json.dumps(audit["summary"], ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if audit["summary"]["critical_count_sum"] == 0 else 2


def audit_production_cutover_v3_readiness(*, static: Mapping[str, Any], verdict_text: str) -> Mapping[str, Any]:
    summary = dict(static.get("summary") or {})
    blockers = list(summary.get("production_blockers") or ())
    cutover_claim = "production_verdict: CUTOVER_READY" in verdict_text or "production_verdict: PRODUCTION_READY" in verdict_text
    production_claim = "production_verdict: PRODUCTION_READY" in verdict_text or "production_ready: True" in verdict_text
    summary["production_ready_with_blockers_count"] = int(production_claim and bool(blockers))
    summary["cutover_ready_with_blockers_count"] = int(cutover_claim and bool(blockers))
    summary["critical_count_sum"] = sum(
        int(value)
        for key, value in summary.items()
        if key.endswith("_count") and key not in {"warning_count"}
    )
    summary["critical_audit_pass"] = summary["critical_count_sum"] == 0
    return {"schema_version": "production_cutover_v3_static_logic_audit_v1", "summary": summary}


def _json(path: Path) -> Mapping[str, Any]:
    if not path.exists():
        return {"summary": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def _text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
