"""Build Round-239 R9 Loop-10 mobility/transport/leisure validation reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.sector.round239_r9_loop10_mobility_transport_leisure_price_validation import (
    ROUND239_DEFAULT_AUDIT_PATH,
    ROUND239_DEFAULT_CASES_PATH,
    ROUND239_DEFAULT_OUTPUT_DIRECTORY,
    write_round239_r9_loop10_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", default=ROUND239_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--cases", default=ROUND239_DEFAULT_CASES_PATH)
    parser.add_argument("--audit", default=ROUND239_DEFAULT_AUDIT_PATH)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    paths = write_round239_r9_loop10_reports(
        output_directory=Path(args.output_directory),
        cases_path=Path(args.cases),
        audit_path=Path(args.audit),
    )
    for name, path in paths.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()
