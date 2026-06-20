"""CLI for Checkpoint 27 stage-promotion autopsy."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from e2r.backtest.asof_stage_promotion_autopsy import (
    AsOfStagePromotionAutopsy,
    AsOfStagePromotionAutopsyConfig,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze as-of replay stage promotion gates.")
    parser.add_argument("--asof-output", required=True, help="Path to an as-of replay output directory.")
    parser.add_argument("--output-directory", default="output/backtests/asof_stage_promotion_autopsy")
    parser.add_argument("--official-root", default="data/historical_official")
    parser.add_argument("--search-snapshot-root", default="data/search_snapshots")
    parser.add_argument("--report-snapshot-root", default="data/report_snapshots")
    parser.add_argument("--top-candidates", type=int)
    parser.add_argument("--max-queries-per-candidate", type=int)
    parser.add_argument("--max-results-per-query", type=int, default=100)
    parser.add_argument("--report-date", type=date.fromisoformat)
    parser.add_argument(
        "--runtime-fixture-spec-file",
        action="append",
        default=[],
        help="Explicit V12 runtime fixture spec JSON/JSONL to use while recomputing autopsy rows.",
    )
    return parser


def config_from_args(args: argparse.Namespace) -> AsOfStagePromotionAutopsyConfig:
    return AsOfStagePromotionAutopsyConfig(
        asof_output=Path(args.asof_output),
        output_directory=Path(args.output_directory),
        official_root=Path(args.official_root),
        search_snapshot_root=Path(args.search_snapshot_root),
        report_snapshot_root=Path(args.report_snapshot_root),
        top_candidates=args.top_candidates,
        max_queries_per_candidate=args.max_queries_per_candidate,
        max_results_per_query=args.max_results_per_query,
        report_date=args.report_date,
        runtime_fixture_spec_paths=tuple(Path(item) for item in args.runtime_fixture_spec_file),
    )


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = AsOfStagePromotionAutopsy().run(config_from_args(args))
    for name, path in result.output_paths.items():
        print(f"{name}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
