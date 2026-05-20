"""Build Round 275 R6 Loop-13 financial/capital/digital validation reports."""

from __future__ import annotations

import argparse

from e2r.sector.round275_r6_loop13_financial_capital_digital_price_validation import (
    ROUND275_DEFAULT_AUDIT_PATH,
    ROUND275_DEFAULT_CASES_PATH,
    ROUND275_DEFAULT_OUTPUT_DIRECTORY,
    write_round275_r6_loop13_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND275_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND275_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND275_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round275_r6_loop13_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
