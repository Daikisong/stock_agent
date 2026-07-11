from __future__ import annotations

import argparse
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.scoring.claim_eligibility import audit_claim_eligibility


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--output", default="docs/operational/e2r_claim_eligibility_audit.json"
    )
    args = parser.parse_args()
    audit = audit_claim_eligibility(repo_root=args.repo_root)
    write_json(Path(args.output), audit)
    print(
        f"{audit['status']} decisions={audit['decision_count']} "
        f"critical={audit['critical_count_sum']}"
    )
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
