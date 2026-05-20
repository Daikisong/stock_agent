"""Build Round-261 R5 Loop-12 consumer/retail/brand reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round261_r5_loop12_consumer_retail_brand_price_validation import (
    ROUND261_DEFAULT_AUDIT_PATH,
    ROUND261_DEFAULT_CASES_PATH,
    ROUND261_DEFAULT_OUTPUT_DIRECTORY,
    write_round261_r5_loop12_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND261_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND261_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND261_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round261_r5_loop12_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
