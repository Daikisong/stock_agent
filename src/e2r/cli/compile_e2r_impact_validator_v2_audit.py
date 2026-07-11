from __future__ import annotations

import argparse
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.scoring import (
    audit_impact_validator_v2,
    compile_fact_document_dedupe_audit,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_impact_validator_v2_audit.json",
    )
    parser.add_argument(
        "--dedupe-output",
        default="docs/operational/e2r_fact_document_dedupe_audit.json",
    )
    args = parser.parse_args()
    audit = audit_impact_validator_v2(repo_root=args.repo_root)
    dedupe = compile_fact_document_dedupe_audit(audit)
    write_json(Path(args.output), audit)
    write_json(Path(args.dedupe_output), dedupe)
    print(
        f"{audit['status']} critical={audit['critical_count_sum']} "
        f"dedupe={dedupe['status']}"
    )
    return 0 if audit["critical_count_sum"] + dedupe["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
