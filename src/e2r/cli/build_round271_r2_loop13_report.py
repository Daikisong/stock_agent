"""Build Round-271 R2 Loop-13 AI semiconductor/electronics reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round271_r2_loop13_ai_semiconductor_electronics_price_validation import (
    ROUND271_DEFAULT_AUDIT_PATH,
    ROUND271_DEFAULT_CASES_PATH,
    ROUND271_DEFAULT_OUTPUT_DIRECTORY,
    write_round271_r2_loop13_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND271_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND271_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND271_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round271_r2_loop13_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
