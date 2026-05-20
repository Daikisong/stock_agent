"""Build Round-244 R1 Loop-11 industrial orders/infrastructure reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round244_r1_loop11_industrial_orders_infra_price_validation import (
    ROUND244_DEFAULT_AUDIT_PATH,
    ROUND244_DEFAULT_CASES_PATH,
    ROUND244_DEFAULT_OUTPUT_DIRECTORY,
    write_round244_r1_loop11_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND244_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND244_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND244_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round244_r1_loop11_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
