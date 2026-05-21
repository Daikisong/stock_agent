"""Build Round-322 R1 Loop-17 industrial orders reports."""

from __future__ import annotations

import argparse

from e2r.sector.round322_r1_loop17_industrials_orders_infrastructure import (
    ROUND322_DEFAULT_AUDIT_PATH,
    ROUND322_DEFAULT_CASES_PATH,
    ROUND322_DEFAULT_OUTPUT_DIRECTORY,
    ROUND322_DEFAULT_TRIGGERS_PATH,
    ROUND322_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round322_r1_loop17_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-322 R1 Loop-17 industrial orders reports.")
    parser.add_argument("--output-directory", default=ROUND322_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND322_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND322_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND322_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND322_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round322_r1_loop17_reports(
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
