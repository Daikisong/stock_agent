from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from e2r.research_brain.researcher_mode.self_repair import (
    DEFAULT_PHASE99_AUDIT_PATH,
    DEFAULT_PHASE99_SUMMARY_PATH,
    write_phase99_self_repair_artifacts,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compile E2R v5 Phase 99 internal self-repair and live-canary truth."
    )
    parser.add_argument("--workspace-root", type=Path, default=Path("."))
    parser.add_argument("--audit-output", type=Path, default=DEFAULT_PHASE99_AUDIT_PATH)
    parser.add_argument(
        "--summary-output", type=Path, default=DEFAULT_PHASE99_SUMMARY_PATH
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_phase99_self_repair_artifacts(
        workspace_root=args.workspace_root,
        audit_path=args.audit_output,
        summary_path=args.summary_output,
    )
    audit = json.loads(paths["audit"].read_text(encoding="utf-8"))
    print(json.dumps(audit, ensure_ascii=False, sort_keys=True))
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
