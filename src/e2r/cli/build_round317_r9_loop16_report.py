"""Build Round-317 R9 Loop-16 mobility/transport/leisure reports."""

from __future__ import annotations

import argparse

from e2r.sector.round317_r9_loop16_mobility_transport_leisure_trigger_validation import (
    ROUND317_DEFAULT_AUDIT_PATH,
    ROUND317_DEFAULT_CASES_PATH,
    ROUND317_DEFAULT_OUTPUT_DIRECTORY,
    ROUND317_DEFAULT_TRIGGERS_PATH,
    ROUND317_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round317_r9_loop16_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-317 R9 Loop-16 mobility, transport and leisure reports.")
    parser.add_argument("--output-directory", default=ROUND317_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND317_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND317_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND317_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND317_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round317_r9_loop16_reports(
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
