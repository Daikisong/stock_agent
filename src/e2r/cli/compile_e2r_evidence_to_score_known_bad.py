from __future__ import annotations

import argparse
from pathlib import Path

from e2r.production.metadata import write_json
from e2r.research_brain.scoring.evidence_to_score_known_bad import (
    compile_evidence_to_score_known_bad_audit,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="docs/operational/e2r_semantic_scoring_known_bad_audit.json",
    )
    args = parser.parse_args()
    audit = compile_evidence_to_score_known_bad_audit()
    write_json(Path(args.output), audit)
    print(f"{audit['status']} cases={audit['case_count']} critical={audit['critical_count_sum']}")
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
