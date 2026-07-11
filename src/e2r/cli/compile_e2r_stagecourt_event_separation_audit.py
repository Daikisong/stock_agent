"""Compile the Phase-71 full-thesis/event separation audit."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.scoring.stagecourt_event_separation import (
    audit_stagecourt_event_separation,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default=(
            "docs/operational/e2r_full_thesis_event_separation_audit.json"
        ),
    )
    args = parser.parse_args()
    audit = audit_stagecourt_event_separation()
    write_json(Path(args.output), audit)
    print(
        f"{audit['status']} critical={audit['critical_count_sum']}"
    )
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
