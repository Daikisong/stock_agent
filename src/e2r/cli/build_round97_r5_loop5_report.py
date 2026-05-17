"""Build Round-97 R5 Loop-5 consumer/retail/brand reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round97_r5_loop5_consumer_retail_brand import (
    ROUND97_DEFAULT_CASES_PATH,
    ROUND97_DEFAULT_OUTPUT_DIRECTORY,
    ROUND97_DEFAULT_SCORE_PROFILE_PATH,
    write_round97_r5_loop5_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-97 R5 Loop-5 consumer/retail/brand reports.")
    parser.add_argument("--output-directory", default=ROUND97_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND97_DEFAULT_CASES_PATH)
    parser.add_argument("--score-profiles", default=ROUND97_DEFAULT_SCORE_PROFILE_PATH)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round97_r5_loop5_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        score_profile_path=Path(args.score_profiles),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
