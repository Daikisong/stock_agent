"""Build Round-327 R6 Loop-17 financials/capital/digital-finance reports."""

from __future__ import annotations

import argparse

from e2r.sector.round327_r6_loop17_financials_capital_digital_trigger_validation import (
    ROUND327_DEFAULT_AUDIT_PATH,
    ROUND327_DEFAULT_CASES_PATH,
    ROUND327_DEFAULT_OUTPUT_DIRECTORY,
    ROUND327_DEFAULT_TRIGGERS_PATH,
    ROUND327_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round327_r6_loop17_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-327 R6 Loop-17 financials/capital/digital-finance reports.")
    parser.add_argument("--output-directory", default=ROUND327_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND327_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND327_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND327_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND327_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round327_r6_loop17_reports(
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
