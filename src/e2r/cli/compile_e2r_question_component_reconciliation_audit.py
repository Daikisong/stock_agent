"""Compile the Phase-70 semantic closure reconciliation audit."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.scoring.semantic_closure_reconciler import (
    audit_question_component_reconciliation,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default=(
            "docs/operational/"
            "e2r_question_component_reconciliation_audit.json"
        ),
    )
    args = parser.parse_args()
    audit = audit_question_component_reconciliation()
    write_json(Path(args.output), audit)
    print(
        f"{audit['status']} questions={audit['question_count']} "
        f"critical={audit['critical_count_sum']}"
    )
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
