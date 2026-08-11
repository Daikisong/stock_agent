"""Compile and seal the five Phase-106 full Researcher Mode canaries."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from e2r.production.v6_canary_results import (
    CANARY_COMPILATION_PASS,
    compile_cross_archetype_canary_directory,
    seal_cross_archetype_canary_summary,
)
from e2r.production.v6_canary_selection import (
    load_sealed_cross_archetype_canary_selection,
)
from e2r.research_brain.researcher_mode.tracked_readiness import (
    _repository_identity_is_trusted,
    canonical_repository_root,
)


CUTOVER_RELATIVE_ROOT = Path("docs/operational/e2r_v6_operational_cutover")
SELECTION_NAME = "cross_archetype_canary_selection.json"
SUMMARY_NAME = "cross_archetype_canary_summary.json"
LIVE_DIRECTORY_NAME = "current_live_canaries"


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        default=".",
        help="trusted canonical repository; input and output paths are not caller-selectable",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    if repo_root != canonical_repository_root() or not _repository_identity_is_trusted(
        repo_root
    ):
        raise SystemExit("Phase106 must run from the clean trusted canonical repository")
    cutover_root = repo_root / CUTOVER_RELATIVE_ROOT
    selection = load_sealed_cross_archetype_canary_selection(
        cutover_root / SELECTION_NAME
    )
    result = compile_cross_archetype_canary_directory(
        selection=selection,
        live_root=cutover_root / LIVE_DIRECTORY_NAME,
    )
    output_path: Path | None = None
    if result.get("status") == CANARY_COMPILATION_PASS:
        summary = result.get("summary")
        if not isinstance(summary, dict):
            raise SystemExit("Phase106 PASS result did not contain the final summary")
        output_path = seal_cross_archetype_canary_summary(
            cutover_root / SUMMARY_NAME,
            summary,
            selection=selection,
            live_root=cutover_root / LIVE_DIRECTORY_NAME,
        )
    print(
        json.dumps(
            {
                **result,
                "summary_path": str(output_path) if output_path is not None else None,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result.get("status") == CANARY_COMPILATION_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())
