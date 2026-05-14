"""CLI for Checkpoint 21 historical universe replay."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Sequence

from e2r.backtest.historical_universe_replay import (
    HistoricalReplayConfig,
    HistoricalReplayMode,
    HistoricalUniverseReplay,
    ReplayFrequency,
    render_historical_replay_summary,
)
from e2r.models import Market


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run E2R historical universe replay from local fixtures.")
    parser.add_argument("--start-date", required=True, help="Replay start date, YYYY-MM-DD.")
    parser.add_argument("--end-date", required=True, help="Replay end date, YYYY-MM-DD.")
    parser.add_argument(
        "--mode",
        choices=[item.value for item in HistoricalReplayMode],
        default=HistoricalReplayMode.CASE_FIXTURE.value,
        help="Historical source mode.",
    )
    parser.add_argument(
        "--frequency",
        choices=[item.value for item in ReplayFrequency],
        default=ReplayFrequency.MONTHLY.value,
        help="Replay cadence.",
    )
    parser.add_argument("--output-directory", default="output/backtests/historical_replay")
    parser.add_argument("--case-root", default="data/historical_cases")
    parser.add_argument("--market", choices=[item.value for item in Market], default=Market.KR.value)
    parser.add_argument("--universe-limit", type=int)
    parser.add_argument("--max-candidates-per-date", type=int, default=50)
    parser.add_argument("--max-report-radar-queries-per-date", type=int, default=0)
    parser.add_argument("--no-write", action="store_true", help="Run replay without writing report files.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = HistoricalReplayConfig(
        start_date=date.fromisoformat(args.start_date),
        end_date=date.fromisoformat(args.end_date),
        replay_frequency=args.frequency,
        mode=args.mode,
        market=args.market,
        universe_limit=args.universe_limit,
        max_candidates_per_date=args.max_candidates_per_date,
        max_report_radar_queries_per_date=args.max_report_radar_queries_per_date,
        output_directory=Path(args.output_directory),
        case_root=Path(args.case_root),
    )
    result = HistoricalUniverseReplay().run(config, write_outputs=not args.no_write)
    print(render_historical_replay_summary(result))
    if result.summary_json_path:
        print(f"summary_json={result.summary_json_path}")
    if result.summary_md_path:
        print(f"summary_md={result.summary_md_path}")
    if result.lifecycle_csv_path:
        print(f"stage_lifecycle_csv={result.lifecycle_csv_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
