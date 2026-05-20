"""Build Round-259 R3 Loop-12 battery/EV/green reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round259_r3_loop12_battery_ev_green_price_validation import (
    ROUND259_DEFAULT_AUDIT_PATH,
    ROUND259_DEFAULT_CASES_PATH,
    ROUND259_DEFAULT_OUTPUT_DIRECTORY,
    write_round259_r3_loop12_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND259_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND259_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND259_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round259_r3_loop12_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
