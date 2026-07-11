from __future__ import annotations

import argparse
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.runtime.scoring_contracts.scoring_policy_v2 import (
    audit_scoring_schema_totality,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_scoring_schema_totality_audit.json",
    )
    args = parser.parse_args()
    audit = audit_scoring_schema_totality(repo_root=args.repo_root)
    write_json(Path(args.output), audit)
    print(
        f"{audit['status']} total={audit['total_schema_archetype_count']}/"
        f"{audit['canonical_archetype_count']} critical={audit['critical_count_sum']}"
    )
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
