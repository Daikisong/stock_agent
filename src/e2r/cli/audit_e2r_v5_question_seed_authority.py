"""Audit Phase 83 QuestionImpactContract scoring-authority demotion."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.researcher_mode import (
    audit_research_question_seed_authority,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_v5_question_seed_authority_audit.json",
    )
    args = parser.parse_args(argv)
    audit = audit_research_question_seed_authority(repo_root=args.repo_root)
    write_json(Path(args.output), audit)
    print(
        json.dumps(
            {
                "status": audit["status"],
                "critical_count_sum": audit["critical_count_sum"],
                "seed_count": audit["seed_count"],
                "output": args.output,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if audit["critical_count_sum"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
