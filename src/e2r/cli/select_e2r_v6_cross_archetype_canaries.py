"""Seal five current cross-archetype canaries before deep scoring."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from e2r.production.v6_canary_selection import (
    SELECTION_PASS,
    compile_cross_archetype_canary_selection,
    load_current_live_selection_inputs,
    seal_cross_archetype_canary_selection,
    summarize_cross_archetype_canary_selection,
)
from e2r.research_brain.researcher_mode.tracked_readiness import (
    _repository_identity_is_trusted,
    canonical_repository_root,
)


CUTOVER_RELATIVE_ROOT = Path("docs/operational/e2r_v6_operational_cutover")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument(
        "--repo-root",
        default=".",
        help="repository root containing the canonical output/live_materialization tree",
    )
    return parser


def main() -> int:
    args = _parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    if repo_root != canonical_repository_root() or not _repository_identity_is_trusted(
        repo_root
    ):
        raise SystemExit("selection must run from the trusted canonical repository")
    live_root = repo_root / "output" / "live_materialization" / args.as_of_date
    candidates, trigger_events = load_current_live_selection_inputs(
        live_root,
        selection_as_of_date=args.as_of_date,
    )
    result = compile_cross_archetype_canary_selection(
        selection_as_of_date=args.as_of_date,
        candidates=candidates,
        trigger_events=trigger_events,
    )
    if result["status"] == SELECTION_PASS:
        cutover_root = repo_root / CUTOVER_RELATIVE_ROOT
        selection_path = cutover_root / "cross_archetype_canary_selection.json"
        summary_path = cutover_root / "cross_archetype_canary_summary.json"
        seal_cross_archetype_canary_selection(selection_path, result)
        summary = summarize_cross_archetype_canary_selection(result)
        seal_cross_archetype_canary_selection(summary_path, summary)
    else:
        selection_path = None
        summary_path = None
    print(
        json.dumps(
            {
                **result,
                "selection_path": str(selection_path) if selection_path else None,
                "summary_path": str(summary_path) if summary_path else None,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result["status"] == SELECTION_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())
