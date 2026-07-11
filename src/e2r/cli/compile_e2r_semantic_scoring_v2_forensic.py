from __future__ import annotations

import argparse

from e2r.research_brain.scoring.semantic_v2_forensic import (
    compile_semantic_scoring_v2_forensic_baseline,
    write_semantic_scoring_v2_forensic_baseline,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--docs-root", default="docs/operational")
    args = parser.parse_args()
    audit = compile_semantic_scoring_v2_forensic_baseline(
        repo_root=args.repo_root
    )
    paths = write_semantic_scoring_v2_forensic_baseline(
        audit, docs_root=args.docs_root
    )
    print(
        f"{audit['status']} missing_support_types="
        f"{audit['metrics']['missing_support_type_count']} "
        f"positive_zero="
        f"{audit['metrics']['positive_proposal_zeroed_by_missing_cap_count']} "
        f"artifacts={len(paths)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
