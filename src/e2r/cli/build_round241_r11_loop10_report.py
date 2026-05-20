"""Build Round-241 R11 Loop-10 policy/geopolitical/event reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round241_r11_loop10_policy_geopolitical_event_price_validation import (
    ROUND241_DEFAULT_AUDIT_PATH,
    ROUND241_DEFAULT_CASES_PATH,
    ROUND241_DEFAULT_OUTPUT_DIRECTORY,
    write_round241_r11_loop10_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND241_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND241_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND241_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round241_r11_loop10_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
