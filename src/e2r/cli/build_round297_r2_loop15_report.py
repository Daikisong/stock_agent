"""Build Round-297 R2 Loop-15 trigger-level calibration reports."""

from __future__ import annotations

import argparse

from e2r.sector.round297_r2_loop15_ai_semiconductor_trigger_validation import (
    ROUND297_DEFAULT_AUDIT_PATH,
    ROUND297_DEFAULT_CASES_PATH,
    ROUND297_DEFAULT_OUTPUT_DIRECTORY,
    ROUND297_DEFAULT_TRIGGERS_PATH,
    ROUND297_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round297_r2_loop15_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-297 R2 Loop-15 AI/semiconductor trigger reports.")
    parser.add_argument("--output-directory", default=ROUND297_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND297_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND297_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND297_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND297_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round297_r2_loop15_reports(
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
