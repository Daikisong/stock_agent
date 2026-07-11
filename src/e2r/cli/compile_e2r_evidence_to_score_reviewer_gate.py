from __future__ import annotations

import argparse
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.scoring.evidence_to_score_reviewer_gate import (
    compile_evidence_to_score_reviewer_gate,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_evidence_to_score_reviewer_gate.json",
    )
    args = parser.parse_args()
    audit = compile_evidence_to_score_reviewer_gate(repo_root=args.repo_root)
    write_json(Path(args.output), audit)
    print(f"{audit['status']} reviewers={audit['reviewer_count']} critical={audit['critical_count_sum']}")
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
