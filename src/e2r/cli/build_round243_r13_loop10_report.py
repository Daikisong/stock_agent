"""Build Round-243 R13 Loop-10 cross-archetype RedTeam reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round243_r13_loop10_cross_archetype_redteam_price_validation import (
    ROUND243_DEFAULT_AUDIT_PATH,
    ROUND243_DEFAULT_CASES_PATH,
    ROUND243_DEFAULT_OUTPUT_DIRECTORY,
    write_round243_r13_loop10_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND243_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND243_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND243_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round243_r13_loop10_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
