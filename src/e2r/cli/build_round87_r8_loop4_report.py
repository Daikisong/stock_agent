"""Build Round-87 R8 Loop-4 platform/content/software/security reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round87_r8_loop4_platform_content_sw_security import write_round87_r8_loop4_reports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-87 R8 Loop-4 platform/content/software/security reports.")
    parser.add_argument("--output-directory", default="output/e2r_round87_r8_loop4_platform_content_sw_security")
    parser.add_argument("--cases", default="data/e2r_case_library/cases_r8_loop4_round87.jsonl")
    parser.add_argument("--score-profiles", default="data/sector_taxonomy/score_weight_profiles_round87_r8_loop4_v4.csv")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round87_r8_loop4_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        score_profile_path=Path(args.score_profiles),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
