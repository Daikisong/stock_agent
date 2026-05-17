"""Build Round-123 R4 Loop-7 materials/spread/strategic-resources reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round123_r4_loop7_materials_spread_strategic import write_round123_r4_loop7_reports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-123 R4 Loop-7 materials/spread/strategic-resources reports.")
    parser.add_argument("--output-directory", default="output/e2r_round123_r4_loop7_materials_spread_strategic")
    parser.add_argument("--cases", default="data/e2r_case_library/cases_r4_loop7_round123.jsonl")
    parser.add_argument("--score-profiles", default="data/sector_taxonomy/score_weight_profiles_round123_r4_loop7_v7.csv")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round123_r4_loop7_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        score_profile_path=Path(args.score_profiles),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
