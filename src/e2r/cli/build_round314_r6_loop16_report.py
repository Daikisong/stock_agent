"""Build Round-314 R6 Loop-16 financial/capital/digital-finance reports."""

from __future__ import annotations

import argparse

from e2r.sector.round314_r6_loop16_financial_capital_digital_trigger_validation import (
    ROUND314_DEFAULT_AUDIT_PATH,
    ROUND314_DEFAULT_CASES_PATH,
    ROUND314_DEFAULT_OUTPUT_DIRECTORY,
    ROUND314_DEFAULT_TRIGGERS_PATH,
    ROUND314_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round314_r6_loop16_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-314 R6 Loop-16 financial, capital allocation and digital-finance reports.")
    parser.add_argument("--output-directory", default=ROUND314_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND314_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND314_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND314_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND314_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round314_r6_loop16_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        triggers_path=args.triggers,
        audit_path=args.audit,
        weight_profile_path=args.weight_profile,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
