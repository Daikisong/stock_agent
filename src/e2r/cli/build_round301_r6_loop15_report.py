"""Build Round-301 R6 Loop-15 financial/capital/digital trigger reports."""

from __future__ import annotations

import argparse

from e2r.sector.round301_r6_loop15_financial_capital_digital_trigger_validation import (
    ROUND301_DEFAULT_AUDIT_PATH,
    ROUND301_DEFAULT_CASES_PATH,
    ROUND301_DEFAULT_OUTPUT_DIRECTORY,
    ROUND301_DEFAULT_TRIGGERS_PATH,
    ROUND301_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round301_r6_loop15_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-301 R6 Loop-15 financial/capital/digital trigger reports.")
    parser.add_argument("--output-directory", default=ROUND301_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND301_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND301_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND301_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND301_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round301_r6_loop15_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        triggers_path=args.triggers,
        audit_path=args.audit,
        weight_profile_path=args.weight_profile,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
