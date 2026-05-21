from __future__ import annotations

import argparse

from e2r.sector.round303_r8_loop15_platform_content_sw_security_trigger_validation import (
    ROUND303_DEFAULT_AUDIT_PATH,
    ROUND303_DEFAULT_CASES_PATH,
    ROUND303_DEFAULT_OUTPUT_DIRECTORY,
    ROUND303_DEFAULT_TRIGGERS_PATH,
    ROUND303_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round303_r8_loop15_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round 303 R8 Loop 15 platform/content/SW/security calibration reports.")
    parser.add_argument("--output-directory", default=ROUND303_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND303_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND303_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND303_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND303_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round303_r8_loop15_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        triggers_path=args.triggers,
        audit_path=args.audit,
        weight_profile_path=args.weight_profile,
    )
    for label, path in sorted(paths.items()):
        print(f"{label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
