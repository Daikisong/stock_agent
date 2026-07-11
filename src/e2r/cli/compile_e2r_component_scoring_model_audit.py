from __future__ import annotations

import argparse
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.scoring import audit_component_scoring_model


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_component_scoring_model_audit.json",
    )
    args = parser.parse_args()
    audit = audit_component_scoring_model()
    write_json(Path(args.output), audit)
    print(
        f"{audit['status']} components={audit['component_count']} "
        f"subcriteria={audit['subcriterion_count']} "
        f"critical={audit['critical_count_sum']}"
    )
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
