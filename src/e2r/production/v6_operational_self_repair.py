"""Git-recomputed Phase108 self-repair audit for operational cutover.

The journal records every concrete repair, but its PASS fields are never
trusted.  Production recompiles the touched file at the patch commit and its
first parent, checks that the commit is an ancestor of current HEAD, and only
then regards the failure as resolved.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash


SELF_REPAIR_SCHEMA = "e2r_v6_operational_self_repair_audit_v1"
SELF_REPAIR_PASS = "E2R_V6_OPERATIONAL_SELF_REPAIR_PASS"
SELF_REPAIR_FAIL = "E2R_V6_OPERATIONAL_SELF_REPAIR_FAIL"
SELF_REPAIR_JOURNAL_LEAF = "self_repair_iterations.jsonl"
SELF_REPAIR_AUDIT_LEAF = "operational_self_repair_audit.json"

FAILURE_CLASSES = (
    "RECEIPT_VALUE_MISSING",
    "RECEIPT_LINEAGE_BROKEN",
    "CLEAN_CLONE_DEPENDENCY",
    "ABSOLUTE_PATH_IDENTITY",
    "ARTIFACT_LIFECYCLE_CONTRADICTION",
    "PROVIDER_ROUTE_MISMATCH",
    "CROSS_ARCHETYPE_RESEARCH_INCOMPLETE",
    "CURRENT_UNIVERSE_MATERIALIZATION_FAILED",
    "TRIGGER_LANE_DISCONNECTED",
    "NATURAL_CANDIDATE_ZERO",
    "L5_RESEARCH_INCOMPLETE",
    "SCORE_STAGE_ATOMICITY_FAILURE",
    "FULL_TEST_STALE",
    "SECRET_LEAK",
    "TARGET_SPECIFIC_OVERFIT",
)

ITERATION_KEYS = frozenset(
    {
        "iteration_id",
        "phase",
        "target_or_scope",
        "failure_class",
        "root_cause",
        "file_function_config",
        "before_artifact_hash",
        "patch_commit",
        "focused_tests",
        "focused_test_status",
        "clean_rerun_status",
        "after_artifact_hash",
        "remaining_blockers",
    }
)
_ITERATION_ID = re.compile(r"E2RREPAIR-[0-9a-f]{24}")
_PHASE = re.compile(r"PHASE10[1-9]")
_SHA256 = re.compile(r"[0-9a-f]{64}")
_GIT_SHA = re.compile(r"[0-9a-f]{40}")
_FOCUSED_TEST = re.compile(
    r"PYTHONPATH=src python -m unittest [A-Za-z0-9_.*:-]+(?: [A-Za-z0-9_.*:-]+)*"
)
_AUDIT_KEYS = frozenset(
    {
        "schema_version",
        "status",
        "journal_path",
        "journal_sha256",
        "iteration_count",
        "iteration_roster_hash",
        "failure_class_counts",
        "unresolved_failure_class_counts",
        "iteration_audits",
        "critical_counts",
        "critical_count_sum",
        "all_failure_classes_resolved",
        "fixed_iteration_count_is_completion_authority",
        "caller_attestation_trusted",
        "production_readiness_authority",
        "score_or_stage_authority",
        "test_mode",
        "audit_hash",
    }
)


def compile_operational_self_repair_audit(
    *,
    repo_root: str | Path,
    final_root: str | Path,
    test_mode: bool = False,
) -> Mapping[str, Any]:
    """Recompute every journal row from Git and return a result-last audit."""

    if not isinstance(test_mode, bool):
        raise TypeError("test_mode must be boolean")
    repo = Path(repo_root).resolve()
    final = Path(final_root).resolve()
    journal = final / SELF_REPAIR_JOURNAL_LEAF
    parse_errors = 0
    rows: list[Mapping[str, Any]] = []
    raw = b""
    try:
        raw = journal.read_bytes()
    except OSError:
        pass
    if raw:
        for line in raw.splitlines():
            if not line.strip():
                parse_errors += 1
                continue
            try:
                value = json.loads(
                    line,
                    object_pairs_hook=_strict_object,
                )
            except (TypeError, ValueError, json.JSONDecodeError):
                parse_errors += 1
                continue
            if not isinstance(value, Mapping):
                parse_errors += 1
                continue
            rows.append(dict(value))

    audits = [_audit_iteration(repo, row) for row in rows]
    ids = [str(row.get("iteration_id") or "") for row in rows]
    duplicates = len(ids) - len(set(ids))
    class_counts = {name: 0 for name in FAILURE_CLASSES}
    unresolved_counts = {name: 0 for name in FAILURE_CLASSES}
    unknown_classes = 0
    for row, audit in zip(rows, audits):
        failure_class = str(row.get("failure_class") or "")
        if failure_class not in class_counts:
            unknown_classes += 1
            continue
        class_counts[failure_class] += 1
        if audit["resolved"] is not True:
            unresolved_counts[failure_class] += 1

    critical_counts = {
        "journal_missing_count": int(not journal.is_file()),
        "journal_empty_count": int(not rows),
        "journal_parse_error_count": parse_errors,
        "duplicate_iteration_id_count": duplicates,
        "unknown_failure_class_count": unknown_classes,
        "invalid_iteration_count": sum(not row["shape_valid"] for row in audits),
        "unverifiable_patch_commit_count": sum(
            not row["patch_commit_verified"] for row in audits
        ),
        "before_hash_mismatch_count": sum(
            not row["before_hash_verified"] for row in audits
        ),
        "after_hash_mismatch_count": sum(
            not row["after_hash_verified"] for row in audits
        ),
        "focused_test_failure_count": sum(
            not row["focused_tests_verified"] for row in audits
        ),
        "clean_rerun_failure_count": sum(
            not row["clean_rerun_verified"] for row in audits
        ),
        "remaining_blocker_count": sum(
            int(row["remaining_blocker_count"]) for row in audits
        ),
        "unresolved_failure_class_count": sum(unresolved_counts.values()),
    }
    critical_sum = sum(critical_counts.values())
    core = {
        "schema_version": SELF_REPAIR_SCHEMA,
        "status": SELF_REPAIR_PASS if critical_sum == 0 else SELF_REPAIR_FAIL,
        "journal_path": SELF_REPAIR_JOURNAL_LEAF,
        "journal_sha256": hashlib.sha256(raw).hexdigest() if raw else None,
        "iteration_count": len(rows),
        "iteration_roster_hash": stable_hash(ids),
        "failure_class_counts": class_counts,
        "unresolved_failure_class_counts": unresolved_counts,
        "iteration_audits": audits,
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
        "all_failure_classes_resolved": critical_sum == 0,
        "fixed_iteration_count_is_completion_authority": False,
        "caller_attestation_trusted": False,
        "production_readiness_authority": False,
        "score_or_stage_authority": False,
        "test_mode": test_mode,
    }
    return {**core, "audit_hash": stable_hash(core)}


def validate_operational_self_repair_audit(
    payload: Mapping[str, Any],
    *,
    recomputed: Mapping[str, Any] | None = None,
    allow_test_mode: bool = False,
) -> bool:
    if not isinstance(payload, Mapping) or set(payload) != _AUDIT_KEYS:
        return False
    if payload.get("schema_version") != SELF_REPAIR_SCHEMA:
        return False
    if payload.get("status") != SELF_REPAIR_PASS:
        return False
    if payload.get("critical_count_sum") != 0:
        return False
    if payload.get("all_failure_classes_resolved") is not True:
        return False
    if payload.get("fixed_iteration_count_is_completion_authority") is not False:
        return False
    if payload.get("caller_attestation_trusted") is not False:
        return False
    if payload.get("production_readiness_authority") is not False:
        return False
    if payload.get("score_or_stage_authority") is not False:
        return False
    if payload.get("test_mode") is True and not allow_test_mode:
        return False
    if not isinstance(payload.get("iteration_count"), int) or payload["iteration_count"] <= 0:
        return False
    core = {key: value for key, value in payload.items() if key != "audit_hash"}
    if payload.get("audit_hash") != stable_hash(core):
        return False
    return recomputed is None or stable_hash(payload) == stable_hash(recomputed)


def _audit_iteration(repo: Path, row: Mapping[str, Any]) -> Mapping[str, Any]:
    iteration_id = str(row.get("iteration_id") or "")
    failure_class = str(row.get("failure_class") or "")
    locator = str(row.get("file_function_config") or "")
    path_text = locator.split("#", 1)[0]
    relative = PurePosixPath(path_text)
    path_valid = bool(
        path_text
        and not relative.is_absolute()
        and ".." not in relative.parts
        and "\\" not in path_text
    )
    tests = row.get("focused_tests")
    blockers = row.get("remaining_blockers")
    shape_valid = bool(
        set(row) == ITERATION_KEYS
        and _ITERATION_ID.fullmatch(iteration_id)
        and _PHASE.fullmatch(str(row.get("phase") or ""))
        and str(row.get("target_or_scope") or "").strip()
        and failure_class in FAILURE_CLASSES
        and str(row.get("root_cause") or "").strip()
        and path_valid
        and _SHA256.fullmatch(str(row.get("before_artifact_hash") or ""))
        and _GIT_SHA.fullmatch(str(row.get("patch_commit") or ""))
        and _SHA256.fullmatch(str(row.get("after_artifact_hash") or ""))
        and isinstance(tests, list)
        and tests
        and all(isinstance(value, str) and _FOCUSED_TEST.fullmatch(value) for value in tests)
        and isinstance(blockers, list)
        and all(isinstance(value, str) and value.strip() for value in blockers)
    )
    commit = str(row.get("patch_commit") or "")
    commit_valid = False
    before_verified = False
    after_verified = False
    changed_path_verified = False
    parent: str | None = None
    before_actual: str | None = None
    after_actual: str | None = None
    if shape_valid:
        commit_valid = _git_ok(repo, "cat-file", "-e", f"{commit}^{{commit}}") and _git_ok(
            repo, "merge-base", "--is-ancestor", commit, "HEAD"
        )
        if commit_valid:
            parent = _git_text(repo, "rev-parse", f"{commit}^")
            changed = set(
                _git_text(repo, "diff-tree", "--no-commit-id", "--name-only", "-r", commit).splitlines()
            )
            changed_path_verified = path_text in changed
            if parent and changed_path_verified:
                before_actual = _commit_file_sha256(repo, parent, path_text, allow_absent=True)
                after_actual = _commit_file_sha256(repo, commit, path_text, allow_absent=False)
                before_verified = before_actual == row.get("before_artifact_hash")
                after_verified = after_actual == row.get("after_artifact_hash")
    focused = bool(
        shape_valid
        and row.get("focused_test_status") == "PASS"
        and isinstance(tests, list)
        and tests
    )
    clean = bool(shape_valid and row.get("clean_rerun_status") == "PASS")
    remaining_count = len(blockers) if isinstance(blockers, list) else 1
    resolved = bool(
        shape_valid
        and commit_valid
        and changed_path_verified
        and before_verified
        and after_verified
        and focused
        and clean
        and remaining_count == 0
    )
    return {
        "iteration_id": iteration_id,
        "failure_class": failure_class,
        "patch_commit": commit,
        "first_parent": parent,
        "file_path": path_text,
        "shape_valid": shape_valid,
        "patch_commit_verified": commit_valid and changed_path_verified,
        "before_hash_verified": before_verified,
        "after_hash_verified": after_verified,
        "before_hash_recomputed": before_actual,
        "after_hash_recomputed": after_actual,
        "focused_tests_verified": focused,
        "clean_rerun_verified": clean,
        "remaining_blocker_count": remaining_count,
        "resolved": resolved,
    }


def _strict_object(pairs: Sequence[tuple[str, Any]]) -> Mapping[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["/usr/bin/git", *args],
        cwd=repo,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def _git_ok(repo: Path, *args: str) -> bool:
    return _git(repo, *args).returncode == 0


def _git_text(repo: Path, *args: str) -> str:
    result = _git(repo, *args)
    return result.stdout.decode("utf-8", errors="strict").strip() if result.returncode == 0 else ""


def _commit_file_sha256(
    repo: Path,
    commit: str,
    path: str,
    *,
    allow_absent: bool,
) -> str | None:
    tree = _git(repo, "ls-tree", commit, "--", path)
    if tree.returncode != 0 or not tree.stdout:
        return hashlib.sha256(f"ABSENT:{path}".encode("utf-8")).hexdigest() if allow_absent else None
    mode = tree.stdout.split(None, 1)[0]
    if mode == b"120000":
        return None
    blob = _git(repo, "show", f"{commit}:{path}")
    if blob.returncode != 0:
        return None
    return hashlib.sha256(blob.stdout).hexdigest()


__all__ = [
    "FAILURE_CLASSES",
    "ITERATION_KEYS",
    "SELF_REPAIR_AUDIT_LEAF",
    "SELF_REPAIR_FAIL",
    "SELF_REPAIR_JOURNAL_LEAF",
    "SELF_REPAIR_PASS",
    "SELF_REPAIR_SCHEMA",
    "compile_operational_self_repair_audit",
    "validate_operational_self_repair_audit",
]
