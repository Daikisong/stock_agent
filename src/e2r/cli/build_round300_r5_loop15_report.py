"""Build Round-300 R5 Loop-15 consumer/retail/brand trigger reports."""

from __future__ import annotations

import argparse

from e2r.sector.round300_r5_loop15_consumer_retail_brand_trigger_validation import (
    ROUND300_DEFAULT_AUDIT_PATH,
    ROUND300_DEFAULT_CASES_PATH,
    ROUND300_DEFAULT_OUTPUT_DIRECTORY,
    ROUND300_DEFAULT_TRIGGERS_PATH,
    ROUND300_DEFAULT_WEIGHT_PROFILE_PATH,
    write_round300_r5_loop15_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Round-300 R5 Loop-15 consumer/retail/brand trigger reports.")
    parser.add_argument("--output-directory", default=ROUND300_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND300_DEFAULT_CASES_PATH)
    parser.add_argument("--triggers", default=ROUND300_DEFAULT_TRIGGERS_PATH)
    parser.add_argument("--audit", default=ROUND300_DEFAULT_AUDIT_PATH)
    parser.add_argument("--weight-profile", default=ROUND300_DEFAULT_WEIGHT_PROFILE_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round300_r5_loop15_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        triggers_path=args.triggers,
        audit_path=args.audit,
        weight_profile_path=args.weight_profile,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
