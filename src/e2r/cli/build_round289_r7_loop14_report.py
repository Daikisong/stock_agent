"""Build Round 289 R7 Loop-14 biotech/healthcare/device validation reports."""

from __future__ import annotations

import argparse

from e2r.sector.round289_r7_loop14_biotech_healthcare_device_price_validation import (
    ROUND289_DEFAULT_AUDIT_PATH,
    ROUND289_DEFAULT_CASES_PATH,
    ROUND289_DEFAULT_OUTPUT_DIRECTORY,
    write_round289_r7_loop14_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND289_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND289_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND289_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round289_r7_loop14_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
