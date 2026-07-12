from __future__ import annotations

import argparse
from pathlib import Path

from e2r.production.metadata import write_json, write_text
from e2r.research_brain.scoring.semantic_self_repair import (
    compile_semantic_scoring_self_repair_audit,
    render_semantic_scoring_self_repair_summary,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--audit-output",
        default="docs/operational/e2r_semantic_scoring_self_repair_audit.json",
    )
    parser.add_argument(
        "--summary-output",
        default="docs/operational/e2r_semantic_scoring_self_repair_summary.md",
    )
    args = parser.parse_args()
    audit = compile_semantic_scoring_self_repair_audit()
    write_json(Path(args.audit_output), audit)
    write_text(
        Path(args.summary_output),
        render_semantic_scoring_self_repair_summary(audit),
    )
    print(
        f"{audit['status']} iterations={audit['iteration_count']} "
        f"critical={audit['critical_count_sum']}"
    )
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
