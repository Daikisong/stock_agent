"""Finalize E2R dossier questions from bounded real source-attempt leaves."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.dossier import finalize_dossier_question_closures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dossier-root", required=True)
    parser.add_argument("--source-research-root", action="append", required=True)
    args = parser.parse_args(argv)
    result = finalize_dossier_question_closures(
        dossier_root=args.dossier_root,
        source_research_roots=args.source_research_root,
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["status"] == "DOSSIER_QUESTION_CLOSURE_PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
