"""Build Round 292 R10 Loop-14 construction/real-estate/materials reports."""

from __future__ import annotations

import argparse

from e2r.sector.round292_r10_loop14_construction_real_estate_building_materials_price_validation import (
    ROUND292_DEFAULT_AUDIT_PATH,
    ROUND292_DEFAULT_CASES_PATH,
    ROUND292_DEFAULT_OUTPUT_DIRECTORY,
    write_round292_r10_loop14_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND292_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND292_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND292_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round292_r10_loop14_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
