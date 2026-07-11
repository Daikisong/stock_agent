"""Recompute the C06 evidence-impact rubric audit artifact."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.compiler.evidence_impact_rubric_compiler import (
    audit_evidence_impact_rubrics,
    compile_evidence_impact_rubrics,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--archetype-id",
        default="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    )
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_evidence_impact_rubric_audit.json",
    )
    args = parser.parse_args()
    catalog = compile_evidence_impact_rubrics(args.archetype_id)
    audit = audit_evidence_impact_rubrics(catalog)
    write_json(Path(args.output), audit)
    print(
        f"{audit['status']} rubrics={audit['rubric_count']} "
        f"critical={audit['critical_count_sum']}"
    )
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
