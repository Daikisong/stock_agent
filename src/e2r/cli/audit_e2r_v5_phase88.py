"""Audit E2R v5 Phase 88 EvidenceFact graph and claim utilization."""

from __future__ import annotations

import argparse

from e2r.research_brain.researcher_mode import (
    compile_phase88_evidence_fact_graph_audit,
    write_phase88_evidence_fact_graph_audit,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    audit = compile_phase88_evidence_fact_graph_audit(args.repo_root)
    path = write_phase88_evidence_fact_graph_audit(
        repo_root=args.repo_root,
        output_path=args.output,
    )
    counts = audit["canary_counts"]
    print(
        f"{audit['status']} claims={counts['claims']} facts={counts['facts']} "
        f"impacts={counts['validated_impacts']} "
        f"critical={audit['critical_count_sum']} output={path}"
    )
    return 0 if audit["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
