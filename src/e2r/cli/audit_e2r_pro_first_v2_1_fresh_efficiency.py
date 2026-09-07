"""Recompute the Pro-first V2.1 fresh-session P9 efficiency audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.pro_first.fresh_session.efficiency_audit import (
    DEFAULT_COMPARISON_PATH,
    compile_fresh_session_efficiency_audit,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--comparison", default=str(DEFAULT_COMPARISON_PATH))
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    payload = compile_fresh_session_efficiency_audit(
        args.repo_root, args.comparison
    )
    rendered = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.output:
        output = Path(args.output).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if payload["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
