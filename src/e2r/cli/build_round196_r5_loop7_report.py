"""Build Round-196 R5 Loop-7 consumer/retail/brand price-path validation reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round196_r5_loop7_consumer_retail_brand_price_validation import (
    ROUND196_DEFAULT_AUDIT_PATH,
    ROUND196_DEFAULT_CASES_PATH,
    ROUND196_DEFAULT_OUTPUT_DIRECTORY,
    write_round196_r5_loop7_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-196 R5 Loop-7 price-path validation reports.")
    parser.add_argument("--output-directory", default=ROUND196_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND196_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND196_DEFAULT_AUDIT_PATH)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round196_r5_loop7_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
