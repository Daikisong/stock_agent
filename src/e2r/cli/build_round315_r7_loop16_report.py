"""Build Round-315 R7 Loop-16 bio/healthcare/medical-device reports."""

from __future__ import annotations

import argparse

from e2r.sector.round315_r7_loop16_biotech_healthcare_device_trigger_validation import (
    ROUND315_DEFAULT_AUDIT_PATH,
    ROUND315_DEFAULT_CASES_PATH,
    ROUND315_DEFAULT_OUTPUT_DIRECTORY,
    ROUND315_DEFAULT_TRIGGERS_PATH,
    ROUND315_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round315_r7_loop16_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-315 R7 Loop-16 bio, healthcare and medical-device reports.")
    parser.add_argument("--output-directory", default=ROUND315_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND315_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND315_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND315_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND315_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round315_r7_loop16_reports(
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
