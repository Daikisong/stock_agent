"""Compile all 36 contract prompt snapshots and audit actual job attachment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.pro_first.research_contracts.snapshot_audit import (
    compile_prompt_snapshot_audit,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output-root")
    parser.add_argument("--audit-output")
    args = parser.parse_args(argv)
    payload = compile_prompt_snapshot_audit(
        args.repo_root,
        output_root=args.output_root,
    )
    rendered = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.audit_output:
        path = Path(args.audit_output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if payload["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
