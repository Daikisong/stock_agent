"""Build Round 290 R8 Loop-14 platform/content/software/security validation reports."""

from __future__ import annotations

import argparse

from e2r.sector.round290_r8_loop14_platform_content_sw_security_price_validation import (
    ROUND290_DEFAULT_AUDIT_PATH,
    ROUND290_DEFAULT_CASES_PATH,
    ROUND290_DEFAULT_OUTPUT_DIRECTORY,
    write_round290_r8_loop14_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND290_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND290_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND290_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round290_r8_loop14_reports(
        output_directory=args.output_directory,
        cases_path=args.cases,
        audit_path=args.audit,
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
