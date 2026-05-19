"""Build Round-201 R10 Loop-7 construction/real-estate reports."""

from __future__ import annotations

import argparse

from e2r.sector.round201_r10_loop7_construction_real_estate_materials_price_validation import (
    ROUND201_DEFAULT_AUDIT_PATH,
    ROUND201_DEFAULT_CASES_PATH,
    ROUND201_DEFAULT_OUTPUT_DIRECTORY,
    write_round201_r10_loop7_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND201_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND201_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND201_DEFAULT_AUDIT_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round201_r10_loop7_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for key, path in paths.items():
        print(f"{key}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
