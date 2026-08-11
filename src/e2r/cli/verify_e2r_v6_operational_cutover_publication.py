"""Reverify Phase109 terminal files against current Git and phase evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from e2r.production.v6_operational_cutover_publication import (
    PHASE109_VERIFICATION_PASS,
    verify_operational_cutover_publication,
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    result = verify_operational_cutover_publication(
        repo_root=Path(args.repo_root)
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, allow_nan=False))
    return 0 if result.get("status") == PHASE109_VERIFICATION_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())
