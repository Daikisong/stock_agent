"""CLI for Checkpoint 22 monthly historical replay suite."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Sequence

from e2r.backtest.historical_universe_replay import HistoricalReplayMode, ReplayFrequency
from e2r.backtest.monthly_replay_suite import MonthlyReplaySuiteConfig, MonthlyReplaySuiteRunner, render_suite_summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the monthly E2R historical replay suite.")
    parser.add_argument("--start-date", required=True, help="Suite start date, YYYY-MM-DD.")
    parser.add_argument("--end-date", required=True, help="Suite end date, YYYY-MM-DD.")
    parser.add_argument("--output-directory", default="output/backtests/monthly_replay_suite")
    parser.add_argument("--modes", default="case_fixture,official_only,hybrid")
    parser.add_argument("--skip-official-only", action="store_true")
    parser.add_argument("--skip-case-fixture", action="store_true")
    parser.add_argument("--skip-hybrid", action="store_true")
    parser.add_argument("--frequency", choices=[item.value for item in ReplayFrequency], default=ReplayFrequency.MONTHLY.value)
    parser.add_argument("--universe-limit", type=int)
    parser.add_argument("--max-candidates-per-date", type=int)
    parser.add_argument("--case-root", default="data/historical_cases")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--write-json", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--write-md", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--write-csv", action=argparse.BooleanOptionalAction, default=True)
    return parser


def config_from_args(args: argparse.Namespace) -> MonthlyReplaySuiteConfig:
    modes = _parse_modes(args.modes)
    if args.skip_case_fixture:
        modes = tuple(mode for mode in modes if mode != HistoricalReplayMode.CASE_FIXTURE)
    if args.skip_official_only:
        modes = tuple(mode for mode in modes if mode != HistoricalReplayMode.OFFICIAL_ONLY)
    if args.skip_hybrid:
        modes = tuple(mode for mode in modes if mode != HistoricalReplayMode.HYBRID)
    return MonthlyReplaySuiteConfig(
        start_date=date.fromisoformat(args.start_date),
        end_date=date.fromisoformat(args.end_date),
        output_directory=Path(args.output_directory),
        modes=modes,
        frequency=args.frequency,
        universe_limit=args.universe_limit,
        max_candidates_per_date=args.max_candidates_per_date,
        strict=args.strict,
        write_json=args.write_json,
        write_md=args.write_md,
        write_csv=args.write_csv,
        case_root=Path(args.case_root),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    config = config_from_args(args)
    result = MonthlyReplaySuiteRunner().run(config)
    print(render_suite_summary(result))
    print(f"output_root={result.output_root}")
    if config.strict and not result.readiness_assessment["ready_for_larger_backtest"]:
        return 2
    return 0


def _parse_modes(value: str) -> tuple[HistoricalReplayMode, ...]:
    modes = []
    for item in value.split(","):
        stripped = item.strip()
        if not stripped:
            continue
        modes.append(HistoricalReplayMode(stripped))
    return tuple(dict.fromkeys(modes))


if __name__ == "__main__":
    raise SystemExit(main())
