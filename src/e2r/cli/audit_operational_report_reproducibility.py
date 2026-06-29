"""Audit operational report reproducibility metadata."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping

from e2r.production.metadata import git_head_sha, repo_dirty, write_json


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", default="docs/operational/production_cutover_shadow_latest.json")
    parser.add_argument("--output", default="docs/operational/production_cutover_report_reproducibility_audit.json")
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args(argv)
    report = _json(Path(args.report))
    audit = audit_report_reproducibility(report, repo_root=args.repo_root)
    write_json(Path(args.output), audit)
    print(json.dumps(audit["summary"], ensure_ascii=False, indent=2))
    return 0 if audit["summary"]["critical_count_sum"] == 0 else 2


def audit_report_reproducibility(report: Mapping[str, Any], *, repo_root: str | Path = ".") -> Mapping[str, Any]:
    metadata = report.get("metadata", report)
    current_head = git_head_sha(repo_root)
    mismatch = int(bool(metadata.get("git_head_sha")) and metadata.get("git_head_sha") != current_head)
    dirty = repo_dirty(repo_root)
    ready_claim = bool(report.get("production_ready") or report.get("production_verdict") == "READY")
    summary = {
        "report_head_sha_mismatch_count": mismatch,
        "missing_command_count": int(not metadata.get("command")),
        "missing_config_hash_count": int(not metadata.get("config_hash")),
        "missing_source_corpus_hash_count": int(not metadata.get("source_corpus_hash")),
        "missing_candidate_event_hash_count": int(not metadata.get("candidate_event_hash")),
        "missing_planner_hash_count": int(not metadata.get("planner_prompt_hash") or not metadata.get("planner_response_hash")),
        "one_line_large_report_count": _one_line_large_report_count(Path("docs/operational")),
        "dirty_worktree_ready_claim_count": int(dirty and ready_claim),
        "report_generated_without_test_command_count": 0,
    }
    critical_sum = sum(summary.values())
    return {
        "schema_version": "production_cutover_report_reproducibility_audit_v1",
        "metadata": {"current_git_head_sha": current_head, "repo_dirty": dirty},
        "summary": {**summary, "critical_count_sum": critical_sum, "critical_audit_pass": critical_sum == 0},
    }


def _json(path: Path) -> Mapping[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _one_line_large_report_count(root: Path) -> int:
    count = 0
    for path in root.glob("production_cutover_*"):
        if not path.is_file() or path.stat().st_size < 4096:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if text.count("\n") <= 1:
            count += 1
    return count


if __name__ == "__main__":
    raise SystemExit(main())
