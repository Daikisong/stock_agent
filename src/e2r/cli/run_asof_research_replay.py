"""CLI for retrospective as-of E2R research replay."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path
from typing import Any, Iterable, Sequence

from e2r.backtest.asof_research_replay import AsOfResearchReplay, AsOfResearchReplayConfig, render_asof_replay_summary
from e2r.backtest.historical_universe_replay import ReplayFrequency
from e2r.models import Market


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run retrospective as-of E2R research replay.")
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--frequency", choices=[item.value for item in ReplayFrequency], default=ReplayFrequency.MONTHLY.value)
    parser.add_argument(
        "--extra-replay-date",
        action="append",
        default=[],
        help="Additional exact as-of date to replay inside the start/end range. Can be provided multiple times.",
    )
    parser.add_argument(
        "--extra-replay-dates-file",
        action="append",
        default=[],
        help="JSON/JSONL/CSV file containing exact fixture dates to add to the replay schedule.",
    )
    parser.add_argument("--market", choices=[item.value for item in Market], default=Market.KR.value)
    parser.add_argument("--output-directory", default="output/backtests/asof_research_replay")
    parser.add_argument("--official-root", default="data/historical_official")
    parser.add_argument("--benchmark-label-path", default="data/benchmark_labels/e2r_known_winners.json")
    parser.add_argument("--search-snapshot-root", default="data/search_snapshots")
    parser.add_argument("--report-snapshot-root", default="data/report_snapshots")
    parser.add_argument("--universe-limit", type=int)
    parser.add_argument("--max-candidates-per-date", type=int)
    parser.add_argument("--max-web-research-candidates-per-date", type=int)
    parser.add_argument("--max-queries-per-candidate", type=int)
    parser.add_argument("--max-results-per-query", type=int, default=100)
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
    parser.add_argument("--theme-rebalance", dest="theme_rebalance_enabled", action="store_true")
    parser.add_argument("--no-theme-rebalance", dest="theme_rebalance_enabled", action="store_false")
    parser.set_defaults(theme_rebalance_enabled=None)
    parser.add_argument("--max-theme-expansion-rounds", type=int)
    parser.add_argument("--theme-evidence-review", dest="theme_evidence_review_enabled", action="store_true")
    parser.add_argument("--no-theme-evidence-review", dest="theme_evidence_review_enabled", action="store_false")
    parser.set_defaults(theme_evidence_review_enabled=True)
    parser.add_argument(
        "--runtime-fixture-spec-file",
        action="append",
        default=[],
        help="Explicit V12 runtime fixture spec JSON/JSONL to convert into source-backed diagnostic replay evidence.",
    )
    return parser


def config_from_args(args: argparse.Namespace) -> AsOfResearchReplayConfig:
    start_date = date.fromisoformat(args.start_date)
    end_date = date.fromisoformat(args.end_date)
    explicit_extra_dates = tuple(date.fromisoformat(item) for item in args.extra_replay_date)
    file_extra_dates = tuple(
        replay_date
        for path in args.extra_replay_dates_file
        for replay_date in load_extra_replay_dates_file(path)
        if start_date <= replay_date <= end_date
    )
    extra_replay_dates = tuple(dict.fromkeys((*explicit_extra_dates, *file_extra_dates)))
    return AsOfResearchReplayConfig(
        start_date=start_date,
        end_date=end_date,
        frequency=args.frequency,
        extra_replay_dates=extra_replay_dates,
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
        theme_rebalance_enabled=args.theme_rebalance_enabled,
        max_theme_expansion_rounds=args.max_theme_expansion_rounds,
        theme_evidence_review_enabled=args.theme_evidence_review_enabled,
        runtime_fixture_spec_paths=tuple(Path(item) for item in args.runtime_fixture_spec_file),
    )


def load_extra_replay_dates_file(path: str | Path) -> tuple[date, ...]:
    path_obj = Path(path)
    if path_obj.suffix.lower() == ".jsonl":
        rows = []
        with path_obj.open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    rows.append(json.loads(line))
        values: Iterable[Any] = rows
    elif path_obj.suffix.lower() == ".csv":
        with path_obj.open(encoding="utf-8", newline="") as handle:
            values = list(csv.DictReader(handle))
    else:
        values = json.loads(path_obj.read_text(encoding="utf-8"))
    return tuple(sorted(set(_extract_extra_replay_dates(values))))


def _extract_extra_replay_dates(value: Any) -> tuple[date, ...]:
    dates: list[date] = []
    if isinstance(value, str):
        parsed = _parse_replay_date(value)
        return (parsed,) if parsed else ()
    if isinstance(value, list):
        for item in value:
            dates.extend(_extract_extra_replay_dates(item))
        return tuple(dates)
    if not isinstance(value, dict):
        return ()
    for key in ("as_of_date", "trigger_date", "entry_date", "date"):
        parsed = _parse_replay_date(value.get(key))
        if parsed:
            dates.append(parsed)
    candidate = value.get("candidate")
    if isinstance(candidate, dict):
        dates.extend(_extract_extra_replay_dates(candidate))
    for role_key in ("green_fixture_candidate", "guard_fixture_candidate"):
        role_payload = value.get(role_key)
        if isinstance(role_payload, dict):
            dates.extend(_extract_extra_replay_dates(role_payload))
    for collection_key in ("rows", "archetypes"):
        collection = value.get(collection_key)
        if isinstance(collection, list):
            dates.extend(_extract_extra_replay_dates(collection))
    return tuple(dates)


def _parse_replay_date(value: Any) -> date | None:
    if isinstance(value, date):
        return value
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return date.fromisoformat(text[:10])
    except ValueError:
        return None


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = AsOfResearchReplay().run(config_from_args(args))
    print(render_asof_replay_summary(result))
    if result.output_root:
        print(f"output_root={result.output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
