"""Run E2R Census v3 until pass or blocker."""

from __future__ import annotations

import argparse

from e2r.census.census_runner_v3 import CensusV3RunConfig, run_census_mode_v3


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--universe", default="krx")
    parser.add_argument("--mode", default="census_selective_deep")
    parser.add_argument("--max-iterations", type=int, default=10)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--universe-file")
    parser.add_argument("--max-symbols", type=int, default=0)
    parser.add_argument("--fail-on-external-blocker", default="true")
    parser.add_argument("--fail-on-report-overclaim", default="true")
    parser.add_argument("--fail-on-critical-audit", default="true")
    args = parser.parse_args(argv)
    result = run_census_mode_v3(
        CensusV3RunConfig(
            as_of_date=args.as_of_date,
            output_root=args.output_root,
            universe=args.universe,
            universe_file=args.universe_file,
            max_symbols=args.max_symbols,
            max_iterations=args.max_iterations,
            fail_on_external_blocker=str(args.fail_on_external_blocker).lower() == "true",
            fail_on_report_overclaim=str(args.fail_on_report_overclaim).lower() == "true",
            fail_on_critical_audit=str(args.fail_on_critical_audit).lower() == "true",
        )
    )
    print(result.readiness_verdict["verdict"])
    return 0 if result.readiness_verdict["verdict"] == "FULL_UNIVERSE_STAGE_MAP_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
