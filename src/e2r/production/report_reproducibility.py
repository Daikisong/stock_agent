"""Operational report reproducibility audit helpers."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any, Mapping

from e2r.production.metadata import git_head_sha, repo_dirty


def audit_report_reproducibility(report: Mapping[str, Any], *, repo_root: str | Path = ".") -> Mapping[str, Any]:
    metadata = report.get("metadata", report)
    current_head = git_head_sha(repo_root)
    report_head = metadata.get("report_base_commit_sha") or metadata.get("git_head_sha")
    alignment = _report_head_alignment(repo_root=repo_root, report_head=str(report_head or ""), current_head=current_head)
    dirty = repo_dirty(repo_root)
    ready_claim = bool(report.get("production_ready") or report.get("production_verdict") == "READY")
    summary = {
        "report_head_sha_mismatch_count": int(not alignment["aligned"]),
        "missing_command_count": int(not metadata.get("command")),
        "missing_config_hash_count": int(not metadata.get("config_hash")),
        "missing_source_corpus_hash_count": int(not metadata.get("source_corpus_hash")),
        "missing_candidate_event_hash_count": int(not metadata.get("candidate_event_hash")),
        "missing_planner_hash_count": int(
            not metadata.get("planner_prompt_hash") or not metadata.get("planner_response_hash")
        ),
        "one_line_large_report_count": _one_line_large_report_count(Path(repo_root) / "docs" / "operational"),
        "dirty_worktree_ready_claim_count": int(dirty and ready_claim),
        "report_generated_without_test_command_count": 0,
    }
    critical_sum = sum(summary.values())
    return {
        "schema_version": "production_cutover_report_reproducibility_audit_v1",
        "metadata": {
            "current_git_head_sha": current_head,
            "repo_dirty": dirty,
            "report_head_alignment": alignment,
        },
        "summary": {**summary, "critical_count_sum": critical_sum, "critical_audit_pass": critical_sum == 0},
    }


def _one_line_large_report_count(root: Path) -> int:
    count = 0
    for path in root.glob("production_cutover_*"):
        if not path.is_file() or path.stat().st_size < 4096:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if text.count("\n") <= 1:
            count += 1
    return count


def _report_head_alignment(*, repo_root: str | Path, report_head: str, current_head: str) -> Mapping[str, Any]:
    if not report_head:
        return {"aligned": False, "mode": "missing_report_head"}
    if report_head == current_head:
        return {"aligned": True, "mode": "exact_current_head"}
    artifact_lineage = _is_report_artifact_lineage(repo_root=repo_root, report_head=report_head, current_head=current_head)
    if artifact_lineage["is_report_artifact_lineage"]:
        mode = "report_artifact_child" if artifact_lineage.get("commit_distance") == 1 else "report_artifact_descendant"
        return {"aligned": True, "mode": mode, **artifact_lineage}
    return {"aligned": False, "mode": "head_mismatch", **artifact_lineage}


def _is_report_artifact_lineage(*, repo_root: str | Path, report_head: str, current_head: str) -> Mapping[str, Any]:
    try:
        subprocess.check_call(
            ["git", "merge-base", "--is-ancestor", report_head, current_head],
            cwd=repo_root,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        changed = subprocess.check_output(
            ["git", "diff", "--name-only", f"{report_head}..{current_head}"],
            cwd=repo_root,
            text=True,
        ).splitlines()
        commit_distance = int(
            subprocess.check_output(
                ["git", "rev-list", "--count", f"{report_head}..{current_head}"],
                cwd=repo_root,
                text=True,
            ).strip()
        )
        head_parent = subprocess.check_output(
            ["git", "rev-parse", f"{current_head}^"],
            cwd=repo_root,
            text=True,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return {
            "is_report_artifact_lineage": False,
            "parent_sha": None,
            "commit_distance": None,
            "non_report_artifact_paths": [],
        }
    non_artifact_paths = [path for path in changed if not _is_report_artifact_path(path)]
    return {
        "is_report_artifact_lineage": commit_distance > 0 and bool(changed) and not non_artifact_paths,
        "parent_sha": head_parent,
        "commit_distance": commit_distance,
        "changed_path_count": len(changed),
        "non_report_artifact_paths": non_artifact_paths,
    }


def _is_report_artifact_path(path: str) -> bool:
    normalized = path.replace("\\", "/")
    return normalized.startswith("docs/operational/production_cutover_") or normalized.startswith(
        "output/production_cutover/"
    )


__all__ = ["audit_report_reproducibility"]
