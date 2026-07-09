"""Run E2R Census Mode v2."""

from __future__ import annotations

import argparse

from e2r.census.census_runner_v2 import CensusV2RunConfig, run_census_mode_v2
from e2r.research_brain.legacy_cli import print_legacy_cli_block


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--output-root")
    parser.add_argument("--universe", default="krx")
    parser.add_argument("--universe-file")
    parser.add_argument("--max-symbols", type=int, default=0)
    parser.add_argument("--fail-on-critical-audit", default="true")
    parser.add_argument("--allow-legacy-v2", action="store_true")
    args = parser.parse_args(argv)
    if not args.allow_legacy_v2:
        print_legacy_cli_block(
            command="run_e2r_census_v2",
            replacement="python -m e2r.cli.run_e2r_current_operation",
        )
        return 2
    result = run_census_mode_v2(
        CensusV2RunConfig(
            as_of_date=args.as_of_date,
            output_root=args.output_root,
            universe=args.universe,
            universe_file=args.universe_file,
            max_symbols=args.max_symbols,
            fail_on_critical_audit=str(args.fail_on_critical_audit).lower() == "true",
        )
    )
    print(f"LEGACY_V2_DIAGNOSTIC_VERDICT {result.readiness_verdict['verdict']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
