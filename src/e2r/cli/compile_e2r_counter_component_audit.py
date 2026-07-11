"""Compile the Phase-69 support/counter/resolution component audit."""

from __future__ import annotations

import argparse
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.scoring.counter_component_math import (
    audit_counter_component_math,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_counter_component_audit.json",
    )
    args = parser.parse_args()
    audit = audit_counter_component_math()
    write_json(Path(args.output), audit)
    print(
        f"{audit['status']} scenarios={audit['scenario_count']} "
        f"critical={audit['critical_count_sum']}"
    )
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
