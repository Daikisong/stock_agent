"""Run E2R Census Mode v1."""

from __future__ import annotations

import argparse

from e2r.census.census_runner import CensusRunConfig, run_census_mode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--mode", choices=["census_light", "census_selective_deep"], default="census_light")
    parser.add_argument("--universe", default="krx")
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--max-symbols", type=int, default=0)
    parser.add_argument("--shard-count", type=int, default=1)
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--planner-provider", choices=["real", "none"], default="none")
    parser.add_argument("--source-mode", default="live_official_first")
    parser.add_argument("--depth-policy", default="configs/e2r_census_depth_policy_v1.json")
    parser.add_argument("--sla", default="configs/e2r_census_sla_v1.json")
    parser.add_argument("--universe-file")
    parser.add_argument("--fail-on-critical-audit", default="true")
    args = parser.parse_args(argv)
    result = run_census_mode(
        CensusRunConfig(
            as_of_date=args.as_of_date,
            mode=args.mode,
            universe=args.universe,
            output_root=args.output_root,
            max_symbols=args.max_symbols,
            shard_count=args.shard_count,
            shard_index=args.shard_index,
            planner_provider=args.planner_provider,
            source_mode=args.source_mode,
            depth_policy_path=args.depth_policy,
            sla_path=args.sla,
            universe_file=args.universe_file,
            fail_on_critical_audit=str(args.fail_on_critical_audit).lower() == "true",
        )
    )
    print(result.readiness_verdict["verdict"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
