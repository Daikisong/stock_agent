"""Run the complete requirement-level Pro-first V2 static audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.pro_first.v2_static_audit import compile_pro_first_v2_static_audit


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    payload = compile_pro_first_v2_static_audit(args.repo_root)
    rendered = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.output:
        output = Path(args.output).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if payload["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
