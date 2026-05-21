"""Build Round-325 R4 Loop-17 materials, spreads, and strategic resources reports."""

from __future__ import annotations

import argparse

from e2r.sector.round325_r4_loop17_materials_spreads_strategic import (
    ROUND325_DEFAULT_AUDIT_PATH,
    ROUND325_DEFAULT_CASES_PATH,
    ROUND325_DEFAULT_OUTPUT_DIRECTORY,
    ROUND325_DEFAULT_TRIGGERS_PATH,
    ROUND325_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round325_r4_loop17_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-325 R4 Loop-17 materials, spreads, and strategic resources reports.")
    parser.add_argument("--output-directory", default=ROUND325_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND325_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND325_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND325_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND325_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round325_r4_loop17_reports(
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
