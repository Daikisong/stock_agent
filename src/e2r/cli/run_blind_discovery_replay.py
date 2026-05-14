"""CLI for E2R_STANDARD blind discovery replay."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Sequence

from e2r.backtest.blind_discovery_replay import BlindDiscoveryConfig, BlindDiscoveryReplay, render_blind_discovery_summary
from e2r.backtest.historical_universe_replay import ReplayFrequency
from e2r.models import Market
from e2r.pipeline.e2r_standard_flow import E2R_STANDARD


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run E2R_STANDARD blind discovery replay.")
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--frequency", choices=[item.value for item in ReplayFrequency], default=ReplayFrequency.MONTHLY.value)
    parser.add_argument("--market", choices=[item.value for item in Market], default=Market.KR.value)
    parser.add_argument("--flow", default=E2R_STANDARD)
    parser.add_argument("--output-directory", default="output/backtests/blind_discovery")
    parser.add_argument("--universe-limit", type=int)
    parser.add_argument("--max-candidates-per-date", type=int, default=50)
    parser.add_argument("--case-root", default="data/historical_cases")
    parser.add_argument("--benchmark-label-path", default="data/benchmark_labels/e2r_known_winners.json")
    parser.add_argument("--search-snapshot-root", default="data/search_snapshots")
    parser.add_argument("--report-snapshot-root", default="data/report_snapshots")
    parser.add_argument("--allow-fixture-source-proxy", dest="allow_fixture_source_proxy", action="store_true")
    parser.add_argument("--no-fixture-source-proxy", dest="allow_fixture_source_proxy", action="store_false")
    parser.set_defaults(allow_fixture_source_proxy=False)
    parser.add_argument("--use-search-snapshots", dest="use_search_snapshots", action="store_true")
    parser.add_argument("--no-use-search-snapshots", dest="use_search_snapshots", action="store_false")
    parser.set_defaults(use_search_snapshots=True)
    parser.add_argument("--use-report-snapshots", dest="use_report_snapshots", action="store_true")
    parser.add_argument("--no-use-report-snapshots", dest="use_report_snapshots", action="store_false")
    parser.set_defaults(use_report_snapshots=True)
    parser.add_argument("--llm-enabled", action="store_true")
    return parser


def config_from_args(args: argparse.Namespace) -> BlindDiscoveryConfig:
    return BlindDiscoveryConfig(
        start_date=date.fromisoformat(args.start_date),
        end_date=date.fromisoformat(args.end_date),
        frequency=args.frequency,
        market=args.market,
        flow=args.flow,
        output_directory=Path(args.output_directory),
        universe_limit=args.universe_limit,
        max_candidates_per_date=args.max_candidates_per_date,
        case_root=Path(args.case_root),
        benchmark_label_path=Path(args.benchmark_label_path),
        search_snapshot_root=Path(args.search_snapshot_root),
        report_snapshot_root=Path(args.report_snapshot_root),
        use_search_snapshots=args.use_search_snapshots,
        use_report_snapshots=args.use_report_snapshots,
        allow_fixture_source_proxy=args.allow_fixture_source_proxy,
        llm_enabled=args.llm_enabled,
    )


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = BlindDiscoveryReplay().run(config_from_args(args))
    print(render_blind_discovery_summary(result))
    if result.output_root:
        print(f"output_root={result.output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
