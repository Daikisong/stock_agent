"""Build Round-242 R12 Loop-10 agri/life-service/misc reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round242_r12_loop10_agri_life_service_misc_price_validation import (
    ROUND242_DEFAULT_AUDIT_PATH,
    ROUND242_DEFAULT_CASES_PATH,
    ROUND242_DEFAULT_OUTPUT_DIRECTORY,
    write_round242_r12_loop10_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND242_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND242_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND242_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round242_r12_loop10_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
