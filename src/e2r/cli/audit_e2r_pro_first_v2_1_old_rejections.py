"""Generate the tracked A/B/C audit for one frozen Pro V2 runtime."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from e2r.pro_first.fresh_session.rejection_taxonomy import (
    build_old_run_rejection_taxonomy,
    render_old_run_rejection_taxonomy_markdown,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--job-root", required=True)
    parser.add_argument(
        "--json-output",
        default="docs/operational/e2r_pro_first_v2_1/old_run_rejection_taxonomy.json",
    )
    parser.add_argument(
        "--markdown-output",
        default="docs/operational/e2r_pro_first_v2_1/old_run_rejection_taxonomy.md",
    )
    args = parser.parse_args()
    payload = build_old_run_rejection_taxonomy(args.job_root)
    _write_text_atomic(
        Path(args.json_output),
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )
    _write_text_atomic(
        Path(args.markdown_output),
        render_old_run_rejection_taxonomy_markdown(payload),
    )
    print(json.dumps(payload["aggregates"], ensure_ascii=False, sort_keys=True))
    return 0


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
