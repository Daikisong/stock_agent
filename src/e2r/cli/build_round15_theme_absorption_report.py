"""Build Round-15 missing-theme absorption v0.5 reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round15_theme_absorption_v05 import write_round15_theme_absorption_reports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-15 E2R missing-theme absorption reports.")
    parser.add_argument("--output-directory", default="output/e2r_round15_theme_absorption_v05")
    parser.add_argument("--score-profiles", default="data/sector_taxonomy/score_weight_profiles_round15.csv")
    parser.add_argument("--theme-map", default="data/sector_taxonomy/theme_tag_map_round15.csv")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round15_theme_absorption_reports(
        output_directory=Path(args.output_directory),
        score_profile_path=Path(args.score_profiles),
        theme_map_path=Path(args.theme_map),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
