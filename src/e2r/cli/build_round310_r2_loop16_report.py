"""Build Round-310 R2 Loop-16 AI semiconductor reports."""

from __future__ import annotations

import argparse

from e2r.sector.round310_r2_loop16_ai_semiconductor_electronic_components_trigger_validation import (
    ROUND310_DEFAULT_AUDIT_PATH,
    ROUND310_DEFAULT_CASES_PATH,
    ROUND310_DEFAULT_OUTPUT_DIRECTORY,
    ROUND310_DEFAULT_TRIGGERS_PATH,
    ROUND310_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round310_r2_loop16_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-310 R2 Loop-16 AI semiconductor and electronic components reports.")
    parser.add_argument("--output-directory", default=ROUND310_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND310_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND310_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND310_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND310_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round310_r2_loop16_reports(
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
