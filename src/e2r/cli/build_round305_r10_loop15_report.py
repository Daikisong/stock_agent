from __future__ import annotations

import argparse

from e2r.sector.round305_r10_loop15_construction_real_estate_trigger_validation import (
    ROUND305_DEFAULT_AUDIT_PATH,
    ROUND305_DEFAULT_CASES_PATH,
    ROUND305_DEFAULT_OUTPUT_DIRECTORY,
    ROUND305_DEFAULT_TRIGGERS_PATH,
    ROUND305_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round305_r10_loop15_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round 305 R10 Loop 15 construction/real-estate calibration reports.")
    parser.add_argument("--output-directory", default=ROUND305_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND305_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND305_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND305_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND305_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round305_r10_loop15_reports(
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
