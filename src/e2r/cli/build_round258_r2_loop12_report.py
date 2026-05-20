"""Build Round-258 R2 Loop-12 AI/semiconductor/electronics reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round258_r2_loop12_ai_semiconductor_price_validation import (
    ROUND258_DEFAULT_AUDIT_PATH,
    ROUND258_DEFAULT_CASES_PATH,
    ROUND258_DEFAULT_OUTPUT_DIRECTORY,
    write_round258_r2_loop12_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND258_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND258_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND258_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round258_r2_loop12_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
