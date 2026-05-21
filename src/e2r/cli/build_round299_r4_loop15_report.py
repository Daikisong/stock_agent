"""Build Round-299 R4 Loop-15 materials/spread/strategic-resources reports."""

from __future__ import annotations

import argparse

from e2r.sector.round299_r4_loop15_materials_spread_strategic_trigger_validation import (
    ROUND299_DEFAULT_AUDIT_PATH,
    ROUND299_DEFAULT_CASES_PATH,
    ROUND299_DEFAULT_OUTPUT_DIRECTORY,
    ROUND299_DEFAULT_TRIGGERS_PATH,
    ROUND299_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round299_r4_loop15_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-299 R4 Loop-15 materials/spread/strategic-resources reports.")
    parser.add_argument("--output-directory", default=ROUND299_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND299_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND299_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND299_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND299_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round299_r4_loop15_reports(
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
