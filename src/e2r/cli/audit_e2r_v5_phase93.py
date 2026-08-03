from __future__ import annotations

import argparse
from pathlib import Path

from e2r.research_brain.researcher_mode import (
    PHASE93_BASELINE_PRODUCTION_ROOT,
    PHASE93_READY,
    compile_phase93_gold_research_recall_audit,
    write_phase93_gold_research_recall_audit,
    write_phase94_tracked_post_run_receipt,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Phase 93 전체-thesis Gold 연구 benchmark 감사"
    )
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    parser.add_argument(
        "--production-root",
        default=PHASE93_BASELINE_PRODUCTION_ROOT,
    )
    parser.add_argument("--post-run-audit")
    parser.add_argument(
        "--publish-tracked-post-run-receipt",
        action="store_true",
    )
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    post_run_audit = args.post_run_audit
    if args.publish_tracked_post_run_receipt:
        receipt = write_phase94_tracked_post_run_receipt(
            root,
            production_root=args.production_root,
        )
        post_run_audit = str(receipt["audit"])
    audit = compile_phase93_gold_research_recall_audit(
        root,
        production_root=args.production_root,
        post_run_audit_path=post_run_audit,
    )
    path = write_phase93_gold_research_recall_audit(
        root,
        output_path=args.output,
        production_root=args.production_root,
        post_run_audit_path=post_run_audit,
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
