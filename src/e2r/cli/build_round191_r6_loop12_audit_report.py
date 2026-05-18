"""Build Round-191 R6 Loop-12 financial/capital/digital audit reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round191_r6_loop12_financial_capital_digital_audit import (
    ROUND191_DEFAULT_AUDIT_PATH,
    ROUND191_DEFAULT_OUTPUT_DIRECTORY,
    write_round191_r6_loop12_audit_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-191 R6 Loop-12 financial/capital/digital audit reports.")
    parser.add_argument("--output-directory", default=ROUND191_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--audit", default=ROUND191_DEFAULT_AUDIT_PATH)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round191_r6_loop12_audit_reports(
        output_directory=Path(args.output_directory),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
