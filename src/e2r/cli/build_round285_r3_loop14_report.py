"""Build Round 285 R3 Loop-14 battery/EV/green-energy reports."""

from __future__ import annotations

import argparse

from e2r.sector.round285_r3_loop14_secondary_battery_ev_green_energy_price_validation import (
    ROUND285_DEFAULT_AUDIT_PATH,
    ROUND285_DEFAULT_CASES_PATH,
    ROUND285_DEFAULT_OUTPUT_DIRECTORY,
    write_round285_r3_loop14_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND285_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND285_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND285_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round285_r3_loop14_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
