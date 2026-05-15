"""Build Round-37 score-weight validation v2.2 reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round37_score_weight_v22 import write_round37_score_weight_reports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-37 score-weight validation v2.2 reports.")
    parser.add_argument("--output-directory", default="output/e2r_round37_score_weight_v22")
    parser.add_argument("--cases", default="data/e2r_case_library/cases_v19_round37.jsonl")
    parser.add_argument("--score-profiles", default="data/sector_taxonomy/score_weight_profiles_round37_v22.csv")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round37_score_weight_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        score_profile_path=Path(args.score_profiles),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
