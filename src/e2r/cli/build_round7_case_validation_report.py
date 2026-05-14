"""Build Round-7 case validation reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round7_case_validation_framework import write_round7_case_validation_reports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-7 E2R case validation reports.")
    parser.add_argument("--cases", default="data/e2r_case_library/cases_v02.jsonl")
    parser.add_argument("--output-directory", default="output/e2r_round7_case_validation")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round7_case_validation_reports(
        case_path=args.cases,
        output_directory=Path(args.output_directory),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
