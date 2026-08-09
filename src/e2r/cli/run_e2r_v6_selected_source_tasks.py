"""Materialize bounded SourceTasks only for the sealed Phase-105 canaries."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.runtime.live_materialization.source_task_materializer import (
    CurrentQuestionSourceTaskMaterializer,
    SourceTaskMaterializationConfig,
    load_evidence_recipes,
    write_source_task_materialization,
)
from e2r.research_brain.researcher_mode.tracked_readiness import (
    _repository_identity_is_trusted,
    canonical_repository_root,
)
from e2r.production.v6_canary_selection import load_current_live_selection_inputs


SELECTION_RELATIVE_PATH = Path(
    "docs/operational/e2r_v6_operational_cutover/cross_archetype_canary_selection.json"
)
RECIPE_RELATIVE_PATH = Path(
    "output/research_intelligence/v1/recipes/evidence_recipes.jsonl"
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--max-source-tasks-per-candidate", type=int, default=10)
    parser.add_argument("--max-generation-attempts", type=int, default=3)
    parser.add_argument("--max-acquisition-retries", type=int, default=2)
    parser.add_argument("--max-parallel-tasks", type=int, default=4)
    return parser


def main() -> int:
    args = _parser().parse_args()
    repo = Path(args.repo_root).resolve()
    if repo != canonical_repository_root() or not _repository_identity_is_trusted(repo):
        raise SystemExit("selected source tasks must run from the trusted repository")
    live_root = repo / "output" / "live_materialization" / args.as_of_date
    selection_path = repo / SELECTION_RELATIVE_PATH
    recipe_path = repo / RECIPE_RELATIVE_PATH
    selection_candidates, trigger_signals = load_current_live_selection_inputs(
        live_root,
        selection_as_of_date=args.as_of_date,
    )
    planner_runs = tuple(row["planner_run"] for row in selection_candidates)
    result = CurrentQuestionSourceTaskMaterializer().materialize(
        SourceTaskMaterializationConfig(
            as_of_date=args.as_of_date,
            max_source_tasks_per_candidate=args.max_source_tasks_per_candidate,
            max_generation_attempts=args.max_generation_attempts,
            max_acquisition_retries=args.max_acquisition_retries,
            max_parallel_tasks=args.max_parallel_tasks,
            test_mode=False,
        ),
        planner_runs=planner_runs,
        trigger_signals=trigger_signals,
        recipes=load_evidence_recipes(recipe_path),
        selection_manifest_path=selection_path,
        selection_candidates=selection_candidates,
    )
    write_source_task_materialization(result, output_root=live_root)
    payload = {
        "status": result.status,
        "as_of_date": result.as_of_date,
        "source_task_count": len(result.source_tasks),
        "question_source_task_count": len(result.question_source_tasks),
        "critical_count_sum": int(result.audit.get("critical_count_sum") or 0),
        "selection_receipt_filter_applied": result.audit.get(
            "selection_receipt_filter_applied"
        ),
        "selected_planner_run_count": result.audit.get(
            "selected_planner_run_count"
        ),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result.status == "CURRENT_SOURCE_TASK_PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
