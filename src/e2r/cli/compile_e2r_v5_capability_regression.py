from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from e2r.research_brain.researcher_mode.capability_regression import (
    DEFAULT_PHASE98_OUTPUT_PATH,
    write_phase98_capability_regression_audit,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compile the E2R v5 Phase 98 capability/known-bad audit."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_PHASE98_OUTPUT_PATH,
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    destination = write_phase98_capability_regression_audit(args.output)
    payload = json.loads(destination.read_text(encoding="utf-8"))
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 0 if payload["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
