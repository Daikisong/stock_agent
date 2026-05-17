"""Build Round-102 R10 Loop-5 construction/real-estate/materials reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round102_r10_loop5_construction_real_estate_materials import write_round102_r10_reports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-102 R10 Loop-5 construction/real-estate/materials reports.")
    parser.add_argument("--output-directory", default="output/e2r_round102_r10_loop5_construction_real_estate_materials")
    parser.add_argument("--cases", default="data/e2r_case_library/cases_r10_loop5_round102.jsonl")
    parser.add_argument("--score-profiles", default="data/sector_taxonomy/score_weight_profiles_round102_r10_loop5_v5.csv")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round102_r10_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        score_profile_path=Path(args.score_profiles),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
