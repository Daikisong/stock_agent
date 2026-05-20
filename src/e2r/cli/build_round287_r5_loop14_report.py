"""Build Round 287 R5 Loop-14 consumer/retail/brand validation reports."""

from __future__ import annotations

import argparse

from e2r.sector.round287_r5_loop14_consumer_retail_brand_price_validation import (
    ROUND287_DEFAULT_AUDIT_PATH,
    ROUND287_DEFAULT_CASES_PATH,
    ROUND287_DEFAULT_OUTPUT_DIRECTORY,
    write_round287_r5_loop14_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND287_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND287_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND287_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round287_r5_loop14_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
