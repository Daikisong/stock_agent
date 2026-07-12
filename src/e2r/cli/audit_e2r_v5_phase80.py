"""Compile the E2R v5 Phase 80 whole-repository forensic baseline."""

from __future__ import annotations

import argparse

from e2r.research_brain.researcher_mode import (
    compile_phase80_forensics,
    write_phase80_forensics,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output-root")
    args = parser.parse_args(argv)
    audit = compile_phase80_forensics(args.repo_root)
    outputs = write_phase80_forensics(
        repo_root=args.repo_root, output_root=args.output_root
    )
    call_graph = audit["call_graph"]
    print(
        f"{call_graph['status']} modules={call_graph['module_count']} "
        f"edges={call_graph['import_edge_count']} "
        f"critical={call_graph['critical_count_sum']} "
        f"outputs={len(outputs)}"
    )
    return 0 if call_graph["critical_count_sum"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
