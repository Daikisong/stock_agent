"""Audit operational report reproducibility metadata."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping

from e2r.production.metadata import write_json
from e2r.production.report_reproducibility import audit_report_reproducibility


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", default="docs/operational/production_cutover_shadow_latest.json")
    parser.add_argument("--output", default="docs/operational/production_cutover_report_reproducibility_audit.json")
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args(argv)
    report = _json(Path(args.report))
    audit = audit_report_reproducibility(report, repo_root=args.repo_root)
    write_json(Path(args.output), audit)
    print(json.dumps(audit["summary"], ensure_ascii=False, indent=2))
    return 0 if audit["summary"]["critical_count_sum"] == 0 else 2


def _json(path: Path) -> Mapping[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    raise SystemExit(main())
