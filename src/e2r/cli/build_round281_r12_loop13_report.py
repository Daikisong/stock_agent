"""Build Round 281 R12 Loop-13 agriculture/life-service/other reports."""

from __future__ import annotations

import argparse

from e2r.sector.round281_r12_loop13_agriculture_life_service_other_price_validation import (
    ROUND281_DEFAULT_AUDIT_PATH,
    ROUND281_DEFAULT_CASES_PATH,
    ROUND281_DEFAULT_OUTPUT_DIRECTORY,
    write_round281_r12_loop13_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND281_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND281_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND281_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round281_r12_loop13_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
