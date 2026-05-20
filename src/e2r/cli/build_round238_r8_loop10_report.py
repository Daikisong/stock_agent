"""Build Round-238 R8 Loop-10 platform/content/SW/security validation reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round238_r8_loop10_platform_content_sw_security_price_validation import (
    ROUND238_DEFAULT_AUDIT_PATH,
    ROUND238_DEFAULT_CASES_PATH,
    ROUND238_DEFAULT_OUTPUT_DIRECTORY,
    write_round238_r8_loop10_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND238_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND238_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND238_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round238_r8_loop10_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
