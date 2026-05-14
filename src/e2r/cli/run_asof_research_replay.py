"""CLI for retrospective as-of E2R research replay."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Sequence

from e2r.backtest.asof_research_replay import AsOfResearchReplay, AsOfResearchReplayConfig, render_asof_replay_summary
from e2r.backtest.historical_universe_replay import ReplayFrequency
from e2r.models import Market


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run retrospective as-of E2R research replay.")
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--frequency", choices=[item.value for item in ReplayFrequency], default=ReplayFrequency.MONTHLY.value)
    parser.add_argument("--market", choices=[item.value for item in Market], default=Market.KR.value)
    parser.add_argument("--output-directory", default="output/backtests/asof_research_replay")
    parser.add_argument("--official-root", default="data/historical_official")
    parser.add_argument("--benchmark-label-path", default="data/benchmark_labels/e2r_known_winners.json")
    parser.add_argument("--search-snapshot-root", default="data/search_snapshots")
    parser.add_argument("--report-snapshot-root", default="data/report_snapshots")
    parser.add_argument("--universe-limit", type=int)
    parser.add_argument("--max-candidates-per-date", type=int, default=50)
    parser.add_argument("--max-web-research-candidates-per-date", type=int, default=20)
    parser.add_argument("--max-queries-per-candidate", type=int, default=8)
    parser.add_argument("--max-results-per-query", type=int, default=5)
    parser.add_argument("--require-date-verified-for-green", dest="require_date_verified_for_green", action="store_true")
    parser.add_argument("--no-require-date-verified-for-green", dest="require_date_verified_for_green", action="store_false")
    parser.set_defaults(require_date_verified_for_green=True)
    parser.add_argument("--allow-undated-docs-for-yellow-only", dest="allow_undated_docs_for_yellow_only", action="store_true")
    parser.add_argument("--no-allow-undated-docs-for-yellow-only", dest="allow_undated_docs_for_yellow_only", action="store_false")
    parser.set_defaults(allow_undated_docs_for_yellow_only=True)
    parser.add_argument("--save-reconstructed-snapshots", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--live-search", action="store_true")
    parser.add_argument("--fixture-search", dest="fixture_search", action="store_true")
    parser.add_argument("--no-fixture-search", dest="fixture_search", action="store_false")
    parser.set_defaults(fixture_search=True)
    parser.add_argument("--allow-snapshot-derived-universe", action="store_true")
    parser.add_argument("--allow-live-historical-official-fetch", action="store_true")
    parser.add_argument("--save-official-history-cache", action="store_true")
    return parser


def config_from_args(args: argparse.Namespace) -> AsOfResearchReplayConfig:
    return AsOfResearchReplayConfig(
        start_date=date.fromisoformat(args.start_date),
        end_date=date.fromisoformat(args.end_date),
        frequency=args.frequency,
        market=args.market,
        output_directory=Path(args.output_directory),
        official_root=Path(args.official_root),
        benchmark_label_path=Path(args.benchmark_label_path),
        search_snapshot_root=Path(args.search_snapshot_root),
        report_snapshot_root=Path(args.report_snapshot_root),
        universe_limit=args.universe_limit,
        max_candidates_per_date=args.max_candidates_per_date,
        max_web_research_candidates_per_date=args.max_web_research_candidates_per_date,
        max_queries_per_candidate=args.max_queries_per_candidate,
        max_results_per_query=args.max_results_per_query,
        require_date_verified_for_green=args.require_date_verified_for_green,
        allow_undated_docs_for_yellow_only=args.allow_undated_docs_for_yellow_only,
        save_reconstructed_snapshots=args.save_reconstructed_snapshots,
        dry_run=args.dry_run,
        live_search=args.live_search,
        fixture_search=args.fixture_search,
        allow_snapshot_derived_universe=args.allow_snapshot_derived_universe,
        allow_live_historical_official_fetch=args.allow_live_historical_official_fetch,
        save_official_history_cache=args.save_official_history_cache,
    )


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = AsOfResearchReplay().run(config_from_args(args))
    print(render_asof_replay_summary(result))
    if result.output_root:
        print(f"output_root={result.output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
