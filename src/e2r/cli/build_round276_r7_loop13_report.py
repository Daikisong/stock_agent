"""Build Round 276 R7 Loop-13 biotech/healthcare/device validation reports."""

from __future__ import annotations

import argparse

from e2r.sector.round276_r7_loop13_biotech_healthcare_device_price_validation import (
    ROUND276_DEFAULT_AUDIT_PATH,
    ROUND276_DEFAULT_CASES_PATH,
    ROUND276_DEFAULT_OUTPUT_DIRECTORY,
    write_round276_r7_loop13_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND276_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND276_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND276_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round276_r7_loop13_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
