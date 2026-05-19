"""Build Round-202 R11 Loop-7 policy/geopolitical/event reports."""

from __future__ import annotations

import argparse

from e2r.sector.round202_r11_loop7_policy_geopolitical_event_price_validation import (
    ROUND202_DEFAULT_AUDIT_PATH,
    ROUND202_DEFAULT_CASES_PATH,
    ROUND202_DEFAULT_OUTPUT_DIRECTORY,
    write_round202_r11_loop7_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND202_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND202_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND202_DEFAULT_AUDIT_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round202_r11_loop7_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for key, path in paths.items():
        print(f"{key}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
