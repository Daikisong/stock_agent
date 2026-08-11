"""Publish the canonical Phase109 reviewer gate and final Markdown report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
from typing import Sequence

from e2r.production.v6_operational_cutover_publication import (
    PHASE109_PUBLICATION_PASS,
    publish_operational_cutover,
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        result = publish_operational_cutover(repo_root=Path(args.repo_root))
    except (
        OSError,
        UnicodeError,
        RuntimeError,
        TypeError,
        ValueError,
        KeyError,
        json.JSONDecodeError,
        subprocess.CalledProcessError,
    ) as exc:
        result = {
            "schema_version": "e2r_v6_operational_cutover_publication_cli_v1",
            "status": "E2R_V6_OPERATIONAL_CUTOVER_PUBLICATION_FAIL",
            "error": f"{type(exc).__name__}:{' '.join(str(exc).split())}",
            "terminal_publication_written": None,
            "terminal_publication_verified": False,
            "production_readiness_authority": False,
            "score_or_stage_authority": False,
        }
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, allow_nan=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, allow_nan=False))
    return 0 if result.get("status") == PHASE109_PUBLICATION_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())
