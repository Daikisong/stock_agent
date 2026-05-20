"""Build Round-293 R11 Loop-14 policy/geopolitics/disaster reports."""

from __future__ import annotations

import argparse

from e2r.sector.round293_r11_loop14_policy_geopolitics_disaster_event_price_validation import (
    ROUND293_DEFAULT_AUDIT_PATH,
    ROUND293_DEFAULT_CASES_PATH,
    ROUND293_DEFAULT_OUTPUT_DIRECTORY,
    write_round293_r11_loop14_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND293_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND293_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND293_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round293_r11_loop14_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
