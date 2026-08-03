"""Export compact, tracked E2R v6 score and Stage receipts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.researcher_mode.tracked_receipts import (
    VERIFICATION_PASS,
    export_receipts,
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--source-output-root", required=True)
    parser.add_argument("--targets", required=True)
    parser.add_argument("--destination", required=True)
    return parser


def main() -> int:
    args = _parser().parse_args()
    targets = tuple(value.strip() for value in args.targets.split(",") if value.strip())
    if not targets:
        raise SystemExit("--targets requires at least one target id")
    result = export_receipts(
        repo_root=Path(args.repo_root),
        source_output_root=Path(args.source_output_root),
        targets=targets,
        destination=Path(args.destination),
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["verification"]["status"] == VERIFICATION_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())
