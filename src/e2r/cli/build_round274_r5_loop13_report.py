"""Build Round 274 R5 Loop-13 consumer/retail/brand validation reports."""

from __future__ import annotations

import argparse

from e2r.sector.round274_r5_loop13_consumer_retail_brand_price_validation import (
    ROUND274_DEFAULT_AUDIT_PATH,
    ROUND274_DEFAULT_CASES_PATH,
    ROUND274_DEFAULT_OUTPUT_DIRECTORY,
    write_round274_r5_loop13_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND274_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND274_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND274_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round274_r5_loop13_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
