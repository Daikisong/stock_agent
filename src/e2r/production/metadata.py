"""Reproducible report metadata for production cutover reports."""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

from e2r.agentic.evidence_os import EVIDENCE_OS_SCHEMA_VERSION


SCORING_SCHEMA_VERSION = "e2r-deterministic-scorer-v2"
STAGE_SCHEMA_VERSION = "e2r-stage-court-v2"


def stable_hash(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def git_head_sha(repo_root: str | Path = ".") -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def repo_dirty(repo_root: str | Path = ".") -> bool:
    try:
        status = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo_root, text=True)
        return bool(status.strip())
    except (OSError, subprocess.CalledProcessError):
        return True


def build_report_metadata(
    *,
    repo_root: str | Path,
    report_generator: str,
    command: str,
    config: Mapping[str, Any],
    source_corpus: Any,
    candidate_events: Any,
    planner_runs: Any,
) -> Mapping[str, Any]:
    return {
        "git_head_sha": git_head_sha(repo_root),
        "report_base_commit_sha": git_head_sha(repo_root),
        "report_generated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "report_generator": report_generator,
        "command": command,
        "config_hash": stable_hash(config),
        "source_corpus_hash": stable_hash(source_corpus),
        "candidate_event_hash": stable_hash(candidate_events),
        "planner_prompt_hash": stable_hash({"planner_inputs": candidate_events}),
        "planner_response_hash": stable_hash(planner_runs),
        "evidence_os_schema_version": EVIDENCE_OS_SCHEMA_VERSION,
        "scoring_schema_version": SCORING_SCHEMA_VERSION,
        "stage_schema_version": STAGE_SCHEMA_VERSION,
        "repo_dirty": repo_dirty(repo_root),
    }


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


__all__ = [
    "SCORING_SCHEMA_VERSION",
    "STAGE_SCHEMA_VERSION",
    "build_report_metadata",
    "git_head_sha",
    "repo_dirty",
    "stable_hash",
    "write_json",
    "write_jsonl",
    "write_text",
]
