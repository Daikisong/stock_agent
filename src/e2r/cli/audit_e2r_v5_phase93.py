from __future__ import annotations

import argparse
from pathlib import Path

from e2r.research_brain.researcher_mode import (
    PHASE93_READY,
    compile_phase93_gold_research_recall_audit,
    write_phase93_gold_research_recall_audit,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Phase 93 전체-thesis Gold 연구 benchmark 감사"
    )
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    audit = compile_phase93_gold_research_recall_audit(root)
    path = write_phase93_gold_research_recall_audit(
        root,
        output_path=args.output,
    )
    print(
        f"{audit['status']} facts={audit['gold_fact_count']} "
        f"queries={audit['gold_query_count']} "
        f"memos={audit['gold_component_memo_count']} "
        f"post_run={audit['post_run_comparison']['status']} output={path}"
    )
    return 0 if audit["status"] == PHASE93_READY else 1


if __name__ == "__main__":
    raise SystemExit(main())
