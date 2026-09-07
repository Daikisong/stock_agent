"""Regenerate and audit all 36 verifier-ready Initial Prompt V3 snapshots."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from e2r.pro_first.research_contracts.snapshot_audit_v3 import (
    compile_initial_prompt_v3_snapshot_audit,
    render_initial_prompt_v3_audit_markdown,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--snapshot-output-root")
    parser.add_argument(
        "--json-output",
        default=(
            "docs/operational/e2r_pro_first_v2_1/"
            "initial_prompt_v3_snapshot_audit.json"
        ),
    )
    parser.add_argument(
        "--markdown-output",
        default=(
            "docs/operational/e2r_pro_first_v2_1/"
            "initial_prompt_v3_snapshot_audit.md"
        ),
    )
    args = parser.parse_args(argv)
    payload = compile_initial_prompt_v3_snapshot_audit(
        args.repo_root,
        output_root=args.snapshot_output_root,
    )
    _write_text_atomic(
        Path(args.json_output),
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )
    _write_text_atomic(
        Path(args.markdown_output),
        render_initial_prompt_v3_audit_markdown(payload),
    )
    print(
        json.dumps(
            {
                "status": payload["status"],
                "critical_count": payload["critical_count"],
                "prompt_snapshot_count": payload["prompt_snapshot_count"],
                "counters": payload["counters"],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if payload["status"] == "PASS" else 2


def _write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
