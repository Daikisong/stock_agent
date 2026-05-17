"""Build Round-157 R12 Loop-9 agriculture/life/misc reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round157_r12_loop9_agri_life_misc import write_round157_r12_loop9_reports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-157 R12 Loop-9 agriculture/life/misc reports.")
    parser.add_argument("--output-directory", default="output/e2r_round157_r12_loop9_agri_life_misc")
    parser.add_argument("--cases", default="data/e2r_case_library/cases_r12_loop9_round157.jsonl")
    parser.add_argument("--score-profiles", default="data/sector_taxonomy/score_weight_profiles_round157_r12_loop9_v9.csv")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round157_r12_loop9_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        score_profile_path=Path(args.score_profiles),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
