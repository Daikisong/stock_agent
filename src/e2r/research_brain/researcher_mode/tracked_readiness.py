"""Compile E2R v6 readiness from tracked receipts only.

This module deliberately has no production-output, cache, environment-file, or
collaboration-journal input.  A clean clone can therefore recompute the same
score/Stage readiness projection from the committed receipt tree alone.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
from typing import Any, Mapping

from e2r.production.metadata import stable_hash
from e2r.research_brain.researcher_mode.tracked_receipts import (
    PHASE101_TARGET_IDS,
    VERIFICATION_PASS,
    verify_receipts,
)


TRACKED_READINESS_SCHEMA = "e2r_v6_tracked_readiness_v1"
TRACKED_READINESS_PASS = "E2R_V6_TRACKED_READINESS_PASS"
TRACKED_READINESS_FAIL = "E2R_V6_TRACKED_READINESS_FAIL"
TRACKED_RECEIPT_RELATIVE_ROOT = Path(
    "docs/operational/e2r_v6_operational_cutover/canary_receipts/2026-07-12"
)
TRUSTED_ORIGIN_IDENTITY = "github.com/Daikisong/stock_agent"
TRUSTED_BASELINE_COMMIT_SHA = "575228b95a070beda8145c1623efcce26ddaa0e9"


def canonical_repository_root() -> Path:
    """Return the repository that owns this verifier implementation."""

    return Path(__file__).resolve().parents[4]


def _normalized_origin_identity(value: str) -> str:
    text = value.strip().removesuffix("/").removesuffix(".git")
    if text.startswith("git@") and ":" in text:
        host, path = text[4:].split(":", 1)
        return f"{host.casefold()}/{path.strip('/')}"
    for prefix in ("https://", "http://", "ssh://git@"):
        if text.startswith(prefix):
            return text[len(prefix) :].strip("/")
    return text


def _git_blob_roster(encoded: bytes, *, index: bool) -> dict[str, str]:
    roster: dict[str, str] = {}
    for raw in encoded.split(b"\0"):
        if not raw:
            continue
        try:
            header, raw_path = raw.split(b"\t", 1)
            fields = header.decode("ascii").split()
            path = raw_path.decode("utf-8", errors="surrogateescape")
        except (UnicodeDecodeError, ValueError) as exc:
            raise ValueError("git blob roster is malformed") from exc
        if index:
            if len(fields) != 3 or fields[2] != "0":
                raise ValueError("git index contains a noncanonical stage")
            blob = fields[1]
        else:
            if len(fields) != 3 or fields[1] != "blob":
                continue
            blob = fields[2]
        if path in roster:
            raise ValueError("git blob roster path is duplicated")
        roster[path] = blob
    return roster


def _verifier_dependencies_match_head(repo: Path) -> bool:
    """Hash every executable verifier dependency against HEAD and the index."""

    try:
        tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=repo).split(
            b"\0"
        )
        tracked_paths = tuple(
            sorted(
                raw.decode("utf-8", errors="surrogateescape")
                for raw in tracked
                if raw
            )
        )
        dependencies = tuple(
            path
            for path in tracked_paths
            if (path.startswith("src/e2r/") and path.endswith(".py"))
            or path.startswith("configs/")
            or path
            == "docs/operational/e2r_v5_component_anchor_atlas.json"
        )
        if not dependencies or any("\n" in path or "\r" in path for path in dependencies):
            return False
        head = _git_blob_roster(
            subprocess.check_output(
                ["git", "ls-tree", "-r", "-z", "HEAD"], cwd=repo
            ),
            index=False,
        )
        index = _git_blob_roster(
            subprocess.check_output(["git", "ls-files", "-s", "-z"], cwd=repo),
            index=True,
        )
        worktree = subprocess.run(
            ["git", "hash-object", "--stdin-paths"],
            cwd=repo,
            input="".join(f"{path}\n" for path in dependencies),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        worktree_hashes = tuple(worktree.stdout.splitlines())
    except (OSError, ValueError, subprocess.CalledProcessError):
        return False
    return (
        worktree.returncode == 0
        and len(worktree_hashes) == len(dependencies)
        and all(
            head.get(path) == index.get(path) == worktree_hash
            for path, worktree_hash in zip(dependencies, worktree_hashes)
        )
    )


def _repository_identity_is_trusted(repo_root: str | Path) -> bool:
    """Bind clean-clone evidence to this repository and its known history."""

    repo = Path(repo_root).resolve()
    if repo != canonical_repository_root():
        return False
    try:
        top = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], cwd=repo, text=True
        ).strip()
        origin = subprocess.check_output(
            ["git", "remote", "get-url", "origin"], cwd=repo, text=True
        ).strip()
        if _normalized_origin_identity(origin) != TRUSTED_ORIGIN_IDENTITY:
            return False
        head = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=repo, text=True
        ).strip()
        remote_main = subprocess.check_output(
            ["git", "rev-parse", "refs/remotes/origin/main"],
            cwd=repo,
            text=True,
        ).strip()
        repository_status = subprocess.check_output(
            ["git", "status", "--porcelain=v1", "--untracked-files=all"],
            cwd=repo,
            text=True,
        ).strip()
        if repository_status:
            return False
        module_relative = Path(__file__).resolve().relative_to(repo).as_posix()
        module_head_blob = subprocess.check_output(
            ["git", "rev-parse", f"HEAD:{module_relative}"], cwd=repo, text=True
        ).strip()
        module_index_line = subprocess.check_output(
            ["git", "ls-files", "-s", "--", module_relative], cwd=repo, text=True
        ).strip()
        module_worktree_blob = subprocess.check_output(
            ["git", "hash-object", "--", module_relative], cwd=repo, text=True
        ).strip()
        baseline_exists = subprocess.run(
            ["git", "cat-file", "-e", f"{TRUSTED_BASELINE_COMMIT_SHA}^{{commit}}"],
            cwd=repo,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ).returncode == 0
        baseline_is_ancestor = subprocess.run(
            [
                "git",
                "merge-base",
                "--is-ancestor",
                TRUSTED_BASELINE_COMMIT_SHA,
                "HEAD",
            ],
            cwd=repo,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ).returncode == 0
    except (OSError, ValueError, subprocess.CalledProcessError):
        return False
    module_index_fields = module_index_line.split()
    return (
        Path(top).resolve() == repo
        and len(head) == 40
        and remote_main == head
        and len(module_index_fields) >= 2
        and module_head_blob == module_index_fields[1] == module_worktree_blob
        and _verifier_dependencies_match_head(repo)
        and baseline_exists
        and baseline_is_ancestor
    )


def _score_stage_projection(
    verification: Mapping[str, Any],
) -> tuple[Mapping[str, Any], ...]:
    rows: list[Mapping[str, Any]] = []
    for target in verification.get("targets", ()):
        metrics = target.get("metrics", {})
        rows.append(
            {
                "target_id": str(target.get("target_id") or ""),
                "total_score": metrics.get("total_score_recomputed"),
                "canonical_stage": metrics.get("canonical_stage_recomputed"),
                "component_count": metrics.get("component_count"),
                "judge_count": metrics.get("judge_count"),
                "scoring_fact_count": metrics.get("scoring_fact_count"),
                "source_count": metrics.get("source_count"),
                "anchor_count": metrics.get("anchor_count"),
                "provider_call_receipt_count": metrics.get(
                    "provider_call_receipt_count"
                ),
            }
        )
    return tuple(sorted(rows, key=lambda row: str(row["target_id"])))


def _tracked_receipt_root_is_current(
    receipt_root: str | Path,
    *,
    repo_root: str | Path,
) -> bool:
    repo = Path(repo_root).resolve()
    if not _repository_identity_is_trusted(repo):
        return False
    raw_root = Path(receipt_root)
    if raw_root.is_symlink():
        return False
    root = raw_root.resolve()
    if root != (repo / TRACKED_RECEIPT_RELATIVE_ROOT).resolve():
        return False
    try:
        tracked = subprocess.check_output(
            ["git", "ls-files", "--", str(TRACKED_RECEIPT_RELATIVE_ROOT)],
            cwd=repo,
            text=True,
        ).splitlines()
    except (OSError, subprocess.CalledProcessError):
        return False
    entries = tuple(root.rglob("*"))
    if any(path.is_symlink() for path in entries):
        return False
    expected = {
        str(path.relative_to(repo)) for path in entries if path.is_file()
    }
    if not expected or expected != set(tracked):
        return False
    for relative in sorted(expected):
        try:
            head_blob = subprocess.check_output(
                ["git", "rev-parse", f"HEAD:{relative}"],
                cwd=repo,
                text=True,
            ).strip()
            index_line = subprocess.check_output(
                ["git", "ls-files", "-s", "--", relative],
                cwd=repo,
                text=True,
            ).strip()
            current_blob = subprocess.check_output(
                ["git", "hash-object", "--", relative],
                cwd=repo,
                text=True,
            ).strip()
        except (OSError, subprocess.CalledProcessError):
            return False
        fields = index_line.split()
        if len(fields) < 2 or not head_blob or not current_blob:
            return False
        if head_blob != fields[1] or head_blob != current_blob:
            return False
    return True


def compile_tracked_readiness(
    receipt_root: str | Path,
    *,
    repo_root: str | Path = ".",
) -> Mapping[str, Any]:
    """Recompute readiness twice from the same receipt-only input.

    The second verification is intentional: it makes replay stability an
    explicit acceptance datum instead of merely assuming deterministic code.
    """

    trusted_before = _tracked_receipt_root_is_current(
        receipt_root, repo_root=repo_root
    )
    if not trusted_before:
        criteria = {
            "receipt_root_is_exact_git_tracked_root": False,
            "receipt_verification_pass": False,
            "exact_target_roster": False,
            "target_count_is_two": False,
            "same_receipt_replay_variance_is_zero": False,
            "offline": True,
            "forbidden_runtime_inputs_read_is_zero": False,
        }
        return {
            "schema_version": TRACKED_READINESS_SCHEMA,
            "status": TRACKED_READINESS_FAIL,
            "ready": False,
            "production_readiness_authority": False,
            "receipt_root_identity": None,
            "target_ids": [],
            "expected_target_ids": list(sorted(PHASE101_TARGET_IDS)),
            "score_stage_values": [],
            "criteria": criteria,
            "critical_count": sum(1 for value in criteria.values() if not value),
            "receipt_verification_hash": None,
            "receipt_replay_verification_hash": None,
            "same_receipt_replay_variance": None,
            "verification_status": None,
            "verification_critical_count_sum": None,
            "offline": True,
            "allowed_inputs": ["TRACKED_RECEIPTS", "TRACKED_VERIFIER_SOURCE"],
        }

    first = verify_receipts(receipt_root)
    second = verify_receipts(receipt_root)
    trusted_after = _tracked_receipt_root_is_current(
        receipt_root, repo_root=repo_root
    )
    first_hash = stable_hash(first)
    second_hash = stable_hash(second)
    first_projection = _score_stage_projection(first)
    second_projection = _score_stage_projection(second)
    expected_targets = tuple(sorted(PHASE101_TARGET_IDS))
    actual_targets = tuple(sorted(str(row["target_id"]) for row in first_projection))
    replay_stable = first_hash == second_hash and first_projection == second_projection
    criteria = {
        "receipt_root_is_exact_git_tracked_root": (
            trusted_before and trusted_after
        ),
        "receipt_verification_pass": first.get("status") == VERIFICATION_PASS,
        "exact_target_roster": actual_targets == expected_targets,
        "target_count_is_two": len(first_projection) == len(PHASE101_TARGET_IDS),
        "same_receipt_replay_variance_is_zero": replay_stable,
        "offline": first.get("offline") is True and second.get("offline") is True,
        "forbidden_runtime_inputs_read_is_zero": all(
            not target.get("forbidden_runtime_inputs_read")
            for verification in (first, second)
            for target in verification.get("targets", ())
        ),
    }
    passed = all(criteria.values())
    return {
        "schema_version": TRACKED_READINESS_SCHEMA,
        "status": TRACKED_READINESS_PASS if passed else TRACKED_READINESS_FAIL,
        "ready": passed,
        "production_readiness_authority": False,
        "receipt_root_identity": first.get("receipt_root_identity"),
        "target_ids": list(actual_targets),
        "expected_target_ids": list(expected_targets),
        "score_stage_values": list(first_projection),
        "criteria": criteria,
        "critical_count": sum(1 for value in criteria.values() if not value),
        "receipt_verification_hash": first_hash,
        "receipt_replay_verification_hash": second_hash,
        "same_receipt_replay_variance": 0 if replay_stable else 1,
        "verification_status": first.get("status"),
        "verification_critical_count_sum": first.get("critical_count_sum"),
        "offline": True,
        "allowed_inputs": [
            "TRACKED_RECEIPTS",
            "CURRENT_SOURCE_CODE",
            "CURRENT_TRACKED_CONFIG",
        ],
        "forbidden_inputs": [
            "output",
            "data/cache",
            ".env",
            "home_cache",
            "collaboration_journal",
            "untracked_files",
        ],
    }


__all__ = [
    "TRACKED_READINESS_FAIL",
    "TRACKED_READINESS_PASS",
    "TRACKED_READINESS_SCHEMA",
    "TRACKED_RECEIPT_RELATIVE_ROOT",
    "TRUSTED_BASELINE_COMMIT_SHA",
    "TRUSTED_ORIGIN_IDENTITY",
    "compile_tracked_readiness",
]
