"""Build Round-12 theme refinement reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round12_theme_refinement import write_round12_theme_refinement_reports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-12 E2R theme refinement reports.")
    parser.add_argument("--output-directory", default="output/e2r_round12_theme_refinement")
    parser.add_argument("--theme-map", default="data/sector_taxonomy/theme_tag_map_round12.csv")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round12_theme_refinement_reports(
        output_directory=Path(args.output_directory),
        theme_map_path=Path(args.theme_map),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
