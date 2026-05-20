"""Build Round-245 R2 Loop-11 AI/semiconductor price-validation reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round245_r2_loop11_ai_semiconductor_price_validation import (
    ROUND245_DEFAULT_AUDIT_PATH,
    ROUND245_DEFAULT_CASES_PATH,
    ROUND245_DEFAULT_OUTPUT_DIRECTORY,
    write_round245_r2_loop11_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND245_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND245_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND245_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round245_r2_loop11_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
