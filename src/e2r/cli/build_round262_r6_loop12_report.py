"""Build Round-262 R6 Loop-12 financial/capital/digital reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round262_r6_loop12_financial_capital_digital_price_validation import (
    ROUND262_DEFAULT_AUDIT_PATH,
    ROUND262_DEFAULT_CASES_PATH,
    ROUND262_DEFAULT_OUTPUT_DIRECTORY,
    write_round262_r6_loop12_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND262_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND262_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND262_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round262_r6_loop12_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
