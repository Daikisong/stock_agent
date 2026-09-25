"""Recompute the Pro-first production security and authority audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.pro_first.static_audit import compile_pro_first_static_audit, write_static_audit


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    result = compile_pro_first_static_audit(args.repo_root)
    if args.output:
        write_static_audit(args.output, result)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if int(result["critical_count_sum"]) == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
