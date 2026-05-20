"""Build Round-232 R2 Loop-10 AI semiconductor reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round232_r2_loop10_ai_semiconductor_price_validation import (
    ROUND232_DEFAULT_AUDIT_PATH,
    ROUND232_DEFAULT_CASES_PATH,
    ROUND232_DEFAULT_OUTPUT_DIRECTORY,
    write_round232_r2_loop10_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND232_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND232_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND232_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round232_r2_loop10_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
