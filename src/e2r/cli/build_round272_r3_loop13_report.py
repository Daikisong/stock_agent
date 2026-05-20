"""Build Round 272 R3 Loop-13 battery/EV/green validation reports."""

from __future__ import annotations

import argparse

from e2r.sector.round272_r3_loop13_battery_ev_green_price_validation import (
    ROUND272_DEFAULT_AUDIT_PATH,
    ROUND272_DEFAULT_CASES_PATH,
    ROUND272_DEFAULT_OUTPUT_DIRECTORY,
    write_round272_r3_loop13_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND272_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND272_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND272_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round272_r3_loop13_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
