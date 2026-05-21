"""Build Round-307 R12 Loop-15 agriculture/life-services reports."""

from __future__ import annotations

import argparse

from e2r.sector.round307_r12_loop15_agriculture_life_services_misc_trigger_validation import (
    ROUND307_DEFAULT_AUDIT_PATH,
    ROUND307_DEFAULT_CASES_PATH,
    ROUND307_DEFAULT_OUTPUT_DIRECTORY,
    ROUND307_DEFAULT_TRIGGERS_PATH,
    ROUND307_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round307_r12_loop15_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-307 R12 Loop-15 agriculture/life-services trigger reports.")
    parser.add_argument("--output-directory", default=ROUND307_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND307_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND307_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND307_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND307_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round307_r12_loop15_reports(
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
