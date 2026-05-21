"""Build Round-306 R11 Loop-15 policy/geopolitical event reports."""

from __future__ import annotations

import argparse

from e2r.sector.round306_r11_loop15_policy_geopolitical_event_trigger_validation import (
    ROUND306_DEFAULT_AUDIT_PATH,
    ROUND306_DEFAULT_CASES_PATH,
    ROUND306_DEFAULT_OUTPUT_DIRECTORY,
    ROUND306_DEFAULT_TRIGGERS_PATH,
    ROUND306_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round306_r11_loop15_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-306 R11 Loop-15 policy/geopolitical trigger reports.")
    parser.add_argument("--output-directory", default=ROUND306_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND306_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND306_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND306_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND306_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round306_r11_loop15_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        triggers_path=args.triggers,
        audit_path=args.audit,
        weight_profile_path=args.weight_profile,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
