"""Build Round-194 R3 Loop-7 battery/EV/green price-path validation reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round194_r3_loop7_battery_ev_green_price_validation import (
    ROUND194_DEFAULT_AUDIT_PATH,
    ROUND194_DEFAULT_CASES_PATH,
    ROUND194_DEFAULT_OUTPUT_DIRECTORY,
    write_round194_r3_loop7_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-194 R3 Loop-7 price-path validation reports.")
    parser.add_argument("--output-directory", default=ROUND194_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND194_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND194_DEFAULT_AUDIT_PATH)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round194_r3_loop7_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
