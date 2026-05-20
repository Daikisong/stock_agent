"""Build Round 296 R1 Loop-15 industrial trigger-level reports."""

from __future__ import annotations

import argparse

from e2r.sector.round296_r1_loop15_industrial_trigger_validation import (
    ROUND296_DEFAULT_AUDIT_PATH,
    ROUND296_DEFAULT_CASES_PATH,
    ROUND296_DEFAULT_OUTPUT_DIRECTORY,
    ROUND296_DEFAULT_TRIGGERS_PATH,
    write_round296_r1_loop15_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND296_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND296_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND296_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND296_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round296_r1_loop15_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        triggers_path=args.triggers,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
