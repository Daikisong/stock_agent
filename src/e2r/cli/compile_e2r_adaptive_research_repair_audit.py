from __future__ import annotations

import argparse
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.research_quality import (
    audit_adaptive_repair_contract,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_adaptive_research_repair_audit.json",
    )
    args = parser.parse_args()
    audit = audit_adaptive_repair_contract()
    write_json(Path(args.output), audit)
    print(
        f"{audit['status']} failures={audit['failure_class_count']} "
        f"critical={audit['critical_count_sum']}"
    )
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
