from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from e2r.research_brain.researcher_mode.canary_leaf_contract import (
    materialize_canary_checkpoint_leaves,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Materialize exact E2R v5 master canary leaf filenames."
    )
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--target-id", required=True)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument(
        "--production-research-complete",
        action="store_true",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    audit = materialize_canary_checkpoint_leaves(
        args.output_root,
        target_id=args.target_id,
        as_of_date=args.as_of_date,
        production_research_complete=args.production_research_complete,
        refresh_target_manifest=True,
    )
    print(json.dumps(audit, ensure_ascii=False, sort_keys=True))
    return 0 if int(audit["critical_count_sum"]) == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
