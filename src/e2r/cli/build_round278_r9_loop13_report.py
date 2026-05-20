"""Build Round 278 R9 Loop-13 mobility/transport/leisure reports."""

from __future__ import annotations

import argparse

from e2r.sector.round278_r9_loop13_mobility_transport_leisure_price_validation import (
    ROUND278_DEFAULT_AUDIT_PATH,
    ROUND278_DEFAULT_CASES_PATH,
    ROUND278_DEFAULT_OUTPUT_DIRECTORY,
    write_round278_r9_loop13_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND278_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND278_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND278_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round278_r9_loop13_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
