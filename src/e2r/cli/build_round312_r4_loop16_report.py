"""Build Round-312 R4 Loop-16 materials/spread/strategic-resources reports."""

from __future__ import annotations

import argparse

from e2r.sector.round312_r4_loop16_materials_spread_strategic_trigger_validation import (
    ROUND312_DEFAULT_AUDIT_PATH,
    ROUND312_DEFAULT_CASES_PATH,
    ROUND312_DEFAULT_OUTPUT_DIRECTORY,
    ROUND312_DEFAULT_TRIGGERS_PATH,
    ROUND312_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round312_r4_loop16_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-312 R4 Loop-16 materials, spread and strategic-resources reports.")
    parser.add_argument("--output-directory", default=ROUND312_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND312_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND312_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND312_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND312_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round312_r4_loop16_reports(
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
