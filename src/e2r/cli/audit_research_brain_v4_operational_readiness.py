"""Audit Research Brain v4 operational readiness reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.v4_static_audit import build_static_logic_audit_v4_from_report_dir


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report-dir", default="docs/operational")
    parser.add_argument("--output", default="docs/operational/research_brain_v4_static_logic_audit.json")
    args = parser.parse_args(argv)
    audit = build_static_logic_audit_v4_from_report_dir(args.report_dir)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(audit["summary"], ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
