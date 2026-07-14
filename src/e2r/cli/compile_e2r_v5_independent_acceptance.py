from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from e2r.research_brain.researcher_mode.independent_acceptance import (
    write_phase100_acceptance_artifacts,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compile E2R v5 Phase 100 independent reviewer artifacts."
    )
    parser.add_argument("--workspace-root", type=Path, default=Path("."))
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_phase100_acceptance_artifacts(workspace_root=args.workspace_root)
    payload = json.loads(paths["reviewer_gate"].read_text(encoding="utf-8"))
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    # A truthful NOT_READY packet is a successful compile.  The JSON status is
    # the acceptance verdict; CLI failure is reserved for artifact generation.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
