"""Merge multiple real E2R source runs for one target."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.dossier import merge_dossier_source_runs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", action="append", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--target-id", required=True)
    args = parser.parse_args(argv)
    result = merge_dossier_source_runs(
        source_roots=args.source_root,
        output_root=args.output_root,
        target_id=args.target_id,
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["status"] == "DOSSIER_SOURCE_MERGE_PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
