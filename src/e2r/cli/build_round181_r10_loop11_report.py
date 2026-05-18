"""Build Round-181 R10 Loop-11 Korea construction/real-estate/materials reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round181_r10_loop11_construction_real_estate_materials import (
    ROUND181_DEFAULT_CASES_PATH,
    ROUND181_DEFAULT_OUTPUT_DIRECTORY,
    ROUND181_DEFAULT_SCORE_PROFILE_PATH,
    write_round181_r10_loop11_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-181 R10 Loop-11 Korea construction/real-estate/materials reports.")
    parser.add_argument("--output-directory", default=ROUND181_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND181_DEFAULT_CASES_PATH)
    parser.add_argument("--score-profiles", default=ROUND181_DEFAULT_SCORE_PROFILE_PATH)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round181_r10_loop11_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        score_profile_path=Path(args.score_profiles),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
