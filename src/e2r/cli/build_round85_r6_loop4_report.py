"""Build Round-85 R6 Loop-4 financial/capital/digital reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round85_r6_loop4_financial_capital_digital import (
    ROUND85_DEFAULT_CASES_PATH,
    ROUND85_DEFAULT_OUTPUT_DIRECTORY,
    ROUND85_DEFAULT_SCORE_PROFILE_PATH,
    write_round85_r6_loop4_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-85 R6 Loop-4 financial/capital/digital reports.")
    parser.add_argument("--output-directory", default=ROUND85_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND85_DEFAULT_CASES_PATH)
    parser.add_argument("--score-profiles", default=ROUND85_DEFAULT_SCORE_PROFILE_PATH)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round85_r6_loop4_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        score_profile_path=Path(args.score_profiles),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
