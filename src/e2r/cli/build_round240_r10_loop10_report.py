"""Build Round-240 R10 Loop-10 construction/real-estate/materials validation reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round240_r10_loop10_construction_real_estate_materials_price_validation import (
    ROUND240_DEFAULT_AUDIT_PATH,
    ROUND240_DEFAULT_CASES_PATH,
    ROUND240_DEFAULT_OUTPUT_DIRECTORY,
    write_round240_r10_loop10_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND240_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND240_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND240_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round240_r10_loop10_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
