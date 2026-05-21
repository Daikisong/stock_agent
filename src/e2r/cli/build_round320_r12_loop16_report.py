"""Build Round-320 R12 Loop-16 agriculture/life-service/misc reports."""

from __future__ import annotations

import argparse

from e2r.sector.round320_r12_loop16_agriculture_life_services_misc_trigger_validation import (
    ROUND320_DEFAULT_AUDIT_PATH,
    ROUND320_DEFAULT_CASES_PATH,
    ROUND320_DEFAULT_OUTPUT_DIRECTORY,
    ROUND320_DEFAULT_TRIGGERS_PATH,
    ROUND320_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round320_r12_loop16_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-320 R12 Loop-16 agriculture, life-service and misc trigger reports.")
    parser.add_argument("--output-directory", default=ROUND320_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND320_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND320_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND320_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND320_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round320_r12_loop16_reports(
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
