"""Build Round 286 R4 Loop-14 materials/spreads/strategic-resources reports."""

from __future__ import annotations

import argparse

from e2r.sector.round286_r4_loop14_materials_spreads_strategic_resources_price_validation import (
    ROUND286_DEFAULT_AUDIT_PATH,
    ROUND286_DEFAULT_CASES_PATH,
    ROUND286_DEFAULT_OUTPUT_DIRECTORY,
    write_round286_r4_loop14_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND286_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND286_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND286_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round286_r4_loop14_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
