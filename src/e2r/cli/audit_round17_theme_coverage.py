"""Build Round-17 theme absorption audit reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from e2r.sector.round17_theme_absorption_audit import (
    ROUND17_DEFAULT_ALIAS_PATH,
    ROUND17_DEFAULT_OUTPUT_DIRECTORY,
    ROUND17_DEFAULT_THEME_MAP_PATH,
    ROUND17_SOURCE_ROUND_PATH,
    write_round17_theme_absorption_reports,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audit Round-17 E2R theme absorption coverage.")
    parser.add_argument("--round-doc", default=ROUND17_SOURCE_ROUND_PATH)
    parser.add_argument("--output-directory", default=ROUND17_DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--theme-map", default=ROUND17_DEFAULT_THEME_MAP_PATH)
    parser.add_argument("--aliases", default=ROUND17_DEFAULT_ALIAS_PATH)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = write_round17_theme_absorption_reports(
        round_doc_path=Path(args.round_doc),
        output_directory=Path(args.output_directory),
        theme_map_path=Path(args.theme_map),
        alias_path=Path(args.aliases),
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
