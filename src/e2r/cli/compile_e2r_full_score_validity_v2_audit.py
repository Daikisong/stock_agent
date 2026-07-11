"""Compile the Phase-72 semantic full-score validity audit."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.scoring.full_score_validity_audit import (
    audit_full_score_validity_v2,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_full_score_validity_v2_audit.json",
    )
    args = parser.parse_args()
    audit = audit_full_score_validity_v2()
    write_json(Path(args.output), audit)
    print(f"{audit['status']} critical={audit['critical_count_sum']}")
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
