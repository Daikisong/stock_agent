"""Audit E2R v5 Phase 86 structured financial/consensus/valuation engine."""

from __future__ import annotations

import argparse

from e2r.research_brain.researcher_mode import (
    compile_phase86_structured_financial_engine_audit,
    write_phase86_structured_financial_engine_audit,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    audit = compile_phase86_structured_financial_engine_audit(args.repo_root)
    path = write_phase86_structured_financial_engine_audit(
        repo_root=args.repo_root, output_path=args.output
    )
    counts = audit["record_counts"]
    print(
        f"{audit['status']} financial={counts['structured_financial_records']} "
        f"revision={counts['consensus_revision_records']} "
        f"valuation={counts['valuation_records']} "
        f"critical={audit['critical_count_sum']} output={path}"
    )
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
