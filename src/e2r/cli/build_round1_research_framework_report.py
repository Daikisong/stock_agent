"""Build Round-1 research framework reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.research_framework import write_round1_framework_reports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-1 E2R research framework reports.")
    parser.add_argument("--cases", default="data/e2r_case_library/cases_v02.jsonl")
    parser.add_argument("--output-directory", default="output/e2r_research_framework")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round1_framework_reports(case_path=args.cases, output_directory=Path(args.output_directory))
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
