"""Build Round-248 R5 Loop-11 consumer/retail/brand validation reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round248_r5_loop11_consumer_retail_brand_price_validation import (
    ROUND248_DEFAULT_AUDIT_PATH,
    ROUND248_DEFAULT_CASES_PATH,
    ROUND248_DEFAULT_OUTPUT_DIRECTORY,
    write_round248_r5_loop11_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND248_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND248_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND248_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round248_r5_loop11_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
