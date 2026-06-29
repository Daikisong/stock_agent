"""Run E2R Production Cutover Gate v1 shadow audit."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from e2r.production.cutover_shadow import (
    ProductionCutoverConfig,
    build_production_cutover_bundle,
    write_production_cutover_bundle,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", default=date.today().isoformat())
    parser.add_argument(
        "--mode",
        default="production_shadow_live",
        choices=("production_shadow_live", "production_live_dry_run", "frozen_replay", "production_shadow"),
    )
    parser.add_argument("--planner-provider", default="real")
    parser.add_argument("--source-mode", default="live_official_first")
    parser.add_argument("--candidate-min-count", type=int, default=50)
    parser.add_argument("--sector-min-events", type=int, default=3)
    parser.add_argument("--max-source-tasks-per-candidate", type=int, default=5)
    parser.add_argument("--max-fetches-per-task", type=int, default=3)
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--validation-output-root", default=None)
    parser.add_argument("--frozen-snapshot-dir", default=None)
    parser.add_argument("--docs-dir", default="docs/operational")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--fail-on-critical-audit", default="true")
    args = parser.parse_args(argv)

    output_dir = args.output_dir or f"output/production_cutover/{args.as_of_date}"
    validation_output_root = args.validation_output_root or str(Path(output_dir).parent)
    config = ProductionCutoverConfig(
        as_of_date=args.as_of_date,
        mode=args.mode,
        planner_provider=args.planner_provider,
        source_mode=args.source_mode,
        candidate_min_count=args.candidate_min_count,
        sector_min_events=args.sector_min_events,
        max_source_tasks_per_candidate=args.max_source_tasks_per_candidate,
        max_fetches_per_task=args.max_fetches_per_task,
        fail_on_critical_audit=str(args.fail_on_critical_audit).lower() == "true",
        output_dir=output_dir,
        validation_output_root=validation_output_root,
        frozen_snapshot_dir=args.frozen_snapshot_dir,
    )
    command = " ".join(
        [
            "PYTHONPATH=src",
            "python",
            "-m",
            "e2r.cli.run_e2r_production_cutover_shadow",
            "--as-of-date",
            args.as_of_date,
            "--mode",
            args.mode,
            "--planner-provider",
            args.planner_provider,
            "--source-mode",
            args.source_mode,
            "--candidate-min-count",
            str(args.candidate_min_count),
            "--sector-min-events",
            str(args.sector_min_events),
            "--max-source-tasks-per-candidate",
            str(args.max_source_tasks_per_candidate),
            "--max-fetches-per-task",
            str(args.max_fetches_per_task),
            "--output-dir",
            output_dir,
            "--validation-output-root",
            validation_output_root,
            "--frozen-snapshot-dir",
            args.frozen_snapshot_dir or "",
            "--docs-dir",
            args.docs_dir,
            "--fail-on-critical-audit",
            str(args.fail_on_critical_audit).lower(),
        ]
    )
    bundle = build_production_cutover_bundle(repo_root=args.repo_root, config=config, command=command)
    paths = write_production_cutover_bundle(bundle=bundle, docs_dir=args.docs_dir, output_dir=output_dir)
    summary = bundle["shadow_latest"]
    print(
        json.dumps(
            {
                "final_status": summary["final_status"],
                "production_verdict": summary["production_verdict"],
                "production_ready": summary["production_ready"],
                "blockers": summary["blockers"],
                "paths": paths,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    if config.fail_on_critical_audit and bundle["static_logic_audit"]["summary"]["critical_count_sum"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
