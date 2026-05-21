"""Build Round-331 R10 Loop-17 construction/real-estate reports."""

from __future__ import annotations

import argparse

from e2r.sector.round331_r10_loop17_construction_real_estate_building_materials_trigger_validation import (
    ROUND331_DEFAULT_AUDIT_PATH,
    ROUND331_DEFAULT_CASES_PATH,
    ROUND331_DEFAULT_OUTPUT_DIRECTORY,
    ROUND331_DEFAULT_TRIGGERS_PATH,
    ROUND331_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round331_r10_loop17_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-331 R10 Loop-17 construction and real-estate reports.")
    parser.add_argument("--output-directory", default=ROUND331_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND331_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND331_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND331_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND331_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round331_r10_loop17_reports(
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
