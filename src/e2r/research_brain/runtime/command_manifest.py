"""Canonical command-run provenance and reproducibility manifests."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import (
    git_head_sha,
    stable_hash,
    write_json,
)


CANONICAL_COMMAND_RUN_SCHEMA_VERSION = "e2r_canonical_command_run_v1"
COMMAND_REPRODUCIBILITY_AUDIT_SCHEMA_VERSION = (
    "e2r_command_reproducibility_audit_v1"
)
REQUIRED_COMMAND_HASH_CATEGORIES = (
    "config",
    "corpus",
    "memory",
    "recipe",
    "prompt",
    "source",
)
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class CommandHashEntryKind(str, Enum):
    FILE = "FILE"
    INLINE = "INLINE"


@dataclass(frozen=True)
class CommandHashEntry:
    entry_id: str
    kind: str
    sha256: str
    path: str | None = None
    payload: Any = None

    def __post_init__(self) -> None:
        kind = CommandHashEntryKind(self.kind)
        if not self.entry_id.strip() or not _SHA256_RE.fullmatch(self.sha256):
            raise ValueError("command hash entry identity/hash is invalid")
        if kind == CommandHashEntryKind.FILE:
            if not str(self.path or "").strip() or self.payload is not None:
                raise ValueError("file hash entry requires path and no payload")
        elif self.path is not None or stable_hash(self.payload) != self.sha256:
            raise ValueError("inline hash entry payload/hash mismatch")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def command_file_hash_entry(
    entry_id: str,
    path: str | Path,
) -> CommandHashEntry:
    resolved = Path(path).resolve()
    if not resolved.is_file():
        raise FileNotFoundError(resolved)
    return CommandHashEntry(
        entry_id=entry_id,
        kind=CommandHashEntryKind.FILE.value,
        path=str(resolved),
        sha256=_file_sha256(resolved),
    )


def command_inline_hash_entry(entry_id: str, payload: Any) -> CommandHashEntry:
    return CommandHashEntry(
        entry_id=entry_id,
        kind=CommandHashEntryKind.INLINE.value,
        payload=payload,
        sha256=stable_hash(payload),
    )


def build_command_run_manifest(
    *,
    command: str,
    semantic_status: str,
    exit_code: int,
    argv: Sequence[str],
    output_root: str | Path,
    hash_inputs: Mapping[str, Sequence[CommandHashEntry]],
    repo_root: str | Path = ".",
    blockers: Sequence[str] = (),
    runtime_critical_count_sum: int = 0,
    production_runtime_ready: bool = False,
) -> Mapping[str, Any]:
    if not command.strip() or not semantic_status.strip():
        raise ValueError("command run identity/status is required")
    if isinstance(exit_code, bool) or not isinstance(exit_code, int) or exit_code < 0:
        raise ValueError("command exit code must be a nonnegative integer")
    if (
        isinstance(runtime_critical_count_sum, bool)
        or not isinstance(runtime_critical_count_sum, int)
        or runtime_critical_count_sum < 0
    ):
        raise ValueError("command runtime critical count must be nonnegative")
    if not isinstance(production_runtime_ready, bool):
        raise ValueError("command production readiness must be boolean")
    if any(not isinstance(item, str) or not item.strip() for item in argv):
        raise ValueError("command argv contains empty text")
    normalized_blockers = tuple(str(item).strip() for item in blockers)
    _require_unique_text(
        normalized_blockers,
        context="command blockers",
        required=False,
    )
    missing_categories = set(REQUIRED_COMMAND_HASH_CATEGORIES) - set(hash_inputs)
    unexpected_categories = set(hash_inputs) - set(REQUIRED_COMMAND_HASH_CATEGORIES)
    if missing_categories or unexpected_categories:
        raise ValueError(
            "command hash categories mismatch: "
            f"missing={sorted(missing_categories)}, "
            f"unexpected={sorted(unexpected_categories)}"
        )
    ledger: dict[str, list[dict[str, Any]]] = {}
    category_hashes: dict[str, str] = {}
    for category in REQUIRED_COMMAND_HASH_CATEGORIES:
        entries = tuple(hash_inputs[category])
        if not entries or any(not isinstance(item, CommandHashEntry) for item in entries):
            raise ValueError(f"command {category} hash ledger cannot be empty")
        entry_ids = tuple(item.entry_id for item in entries)
        _require_unique_text(entry_ids, context=f"command {category} entry ids")
        rows = [item.to_dict() for item in entries]
        ledger[category] = rows
        category_hashes[f"{category}_hash"] = stable_hash(rows)

    dirty_paths = _git_dirty_paths(repo_root)
    dirty_status_hash = stable_hash(list(dirty_paths))
    commit_hash = git_head_sha(repo_root)
    identity = {
        "command": command,
        "semantic_status": semantic_status,
        "exit_code": exit_code,
        "commit_hash": commit_hash,
        "dirty_status_hash": dirty_status_hash,
        "category_hashes": category_hashes,
        "blockers": list(normalized_blockers),
        "runtime_critical_count_sum": runtime_critical_count_sum,
        "production_runtime_ready": production_runtime_ready,
    }
    manifest = {
        "schema_version": CANONICAL_COMMAND_RUN_SCHEMA_VERSION,
        "run_id": "COMMAND-" + stable_hash(identity)[:24],
        "command": command,
        "semantic_status": semantic_status,
        "exit_code": exit_code,
        "argv": list(argv),
        "output_root": str(Path(output_root).resolve()),
        "commit_hash": commit_hash,
        "repo_dirty": bool(dirty_paths),
        "dirty_paths": list(dirty_paths),
        "dirty_status_hash": dirty_status_hash,
        **category_hashes,
        "hash_ledger": ledger,
        "blockers": list(normalized_blockers),
        "runtime_critical_count_sum": runtime_critical_count_sum,
        "production_runtime_ready": production_runtime_ready,
    }
    audit = audit_command_run_manifest(
        manifest,
        repo_root=repo_root,
        verify_current_repo_state=True,
    )
    if audit["critical_count_sum"]:
        raise ValueError(
            f"command run reproducibility audit failed: {audit['critical_counts']}"
        )
    return {**manifest, "reproducibility_audit": audit}


def audit_command_run_manifest(
    manifest: Mapping[str, Any],
    *,
    repo_root: str | Path = ".",
    verify_current_repo_state: bool = False,
) -> Mapping[str, Any]:
    payload = dict(manifest)
    ledger_raw = payload.get("hash_ledger")
    ledger = dict(ledger_raw) if isinstance(ledger_raw, Mapping) else {}
    categories = set(REQUIRED_COMMAND_HASH_CATEGORIES)
    missing_categories = categories - set(ledger)
    unexpected_categories = set(ledger) - categories
    entry_contract_error = 0
    duplicate_entry_id = 0
    entry_hash_mismatch = 0
    category_hash_mismatch = 0
    recomputed_category_hashes: dict[str, str] = {}
    for category in REQUIRED_COMMAND_HASH_CATEGORIES:
        raw_entries = ledger.get(category)
        if not isinstance(raw_entries, (list, tuple)) or not raw_entries:
            continue
        entries: list[Mapping[str, Any]] = []
        ids: list[str] = []
        for raw in raw_entries:
            if not isinstance(raw, Mapping):
                entry_contract_error += 1
                continue
            row = dict(raw)
            try:
                entry = CommandHashEntry(**row)
            except (TypeError, ValueError):
                entry_contract_error += 1
                continue
            entries.append(row)
            ids.append(entry.entry_id)
            if entry.kind == CommandHashEntryKind.FILE.value:
                path = Path(str(entry.path))
                if not path.is_file() or _file_sha256(path) != entry.sha256:
                    entry_hash_mismatch += 1
            elif stable_hash(entry.payload) != entry.sha256:
                entry_hash_mismatch += 1
        duplicate_entry_id += len(ids) - len(set(ids))
        recomputed = stable_hash(entries)
        recomputed_category_hashes[f"{category}_hash"] = recomputed
        if payload.get(f"{category}_hash") != recomputed:
            category_hash_mismatch += 1

    dirty_paths = tuple(str(item) for item in payload.get("dirty_paths") or ())
    expected_dirty_hash = stable_hash(list(dirty_paths))
    identity = {
        "command": payload.get("command"),
        "semantic_status": payload.get("semantic_status"),
        "exit_code": payload.get("exit_code"),
        "commit_hash": payload.get("commit_hash"),
        "dirty_status_hash": payload.get("dirty_status_hash"),
        "category_hashes": {
            key: payload.get(key)
            for key in (
                "config_hash",
                "corpus_hash",
                "memory_hash",
                "recipe_hash",
                "prompt_hash",
                "source_hash",
            )
        },
        "blockers": list(payload.get("blockers") or ()),
        "runtime_critical_count_sum": payload.get("runtime_critical_count_sum"),
        "production_runtime_ready": payload.get("production_runtime_ready"),
    }
    expected_run_id = "COMMAND-" + stable_hash(identity)[:24]
    status = str(payload.get("semantic_status") or "")
    exit_code = payload.get("exit_code")
    blockers = payload.get("blockers")
    ready = payload.get("production_runtime_ready") is True
    repo_state_mismatch = 0
    if verify_current_repo_state:
        current_paths = _git_dirty_paths(repo_root)
        repo_state_mismatch = int(
            payload.get("commit_hash") != git_head_sha(repo_root)
            or dirty_paths != current_paths
            or payload.get("repo_dirty") != bool(current_paths)
        )
    critical = {
        "schema_version_mismatch": int(
            payload.get("schema_version")
            != CANONICAL_COMMAND_RUN_SCHEMA_VERSION
        ),
        "required_field_missing": sum(
            not payload.get(key)
            for key in (
                "run_id",
                "command",
                "semantic_status",
                "output_root",
                "commit_hash",
                "dirty_status_hash",
            )
        ),
        "hash_category_missing": len(missing_categories),
        "unexpected_hash_category": len(unexpected_categories),
        "hash_entry_contract_error": entry_contract_error,
        "duplicate_hash_entry_id": duplicate_entry_id,
        "hash_entry_content_mismatch": entry_hash_mismatch,
        "category_hash_mismatch": category_hash_mismatch,
        "dirty_status_hash_mismatch": int(
            payload.get("dirty_status_hash") != expected_dirty_hash
            or payload.get("repo_dirty") != bool(dirty_paths)
        ),
        "run_id_mismatch": int(payload.get("run_id") != expected_run_id),
        "pass_status_exit_code_mismatch": int(
            status.endswith("_PASS") and exit_code != 0
        ),
        "external_blocker_without_reason": int(
            status == "EXTERNAL_SOURCE_BLOCKER_NOT_READY"
            and (not isinstance(blockers, (list, tuple)) or not blockers)
        ),
        "runtime_critical_count_invalid": int(
            isinstance(payload.get("runtime_critical_count_sum"), bool)
            or not isinstance(payload.get("runtime_critical_count_sum"), int)
            or int(payload.get("runtime_critical_count_sum") or 0) < 0
        ),
        "production_readiness_overclaim": int(
            ready
            and (
                exit_code != 0
                or bool(dirty_paths)
                or bool(blockers)
                or int(payload.get("runtime_critical_count_sum") or 0) != 0
            )
        ),
        "current_repo_state_mismatch": repo_state_mismatch,
    }
    result_payload = {
        "command_run_id": payload.get("run_id"),
        "recomputed_category_hashes": recomputed_category_hashes,
        "critical_counts": critical,
    }
    return {
        "schema_version": COMMAND_REPRODUCIBILITY_AUDIT_SCHEMA_VERSION,
        "status": (
            "COMMAND_REPRODUCIBILITY_PASS"
            if sum(critical.values()) == 0
            else "COMMAND_REPRODUCIBILITY_FAIL"
        ),
        **result_payload,
        "critical_count_sum": sum(critical.values()),
        "result_hash": stable_hash(result_payload),
    }


def write_command_run_manifest(
    manifest: Mapping[str, Any],
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    audit = audit_command_run_manifest(manifest)
    if audit["critical_count_sum"]:
        raise ValueError("cannot write invalid command run manifest")
    root = Path(output_root)
    paths = {
        "command_manifest": root / "command_run_manifest.json",
        "command_audit": root / "command_run_reproducibility_audit.json",
    }
    write_json(paths["command_manifest"], dict(manifest))
    write_json(paths["command_audit"], dict(audit))
    return paths


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _git_dirty_paths(repo_root: str | Path) -> tuple[str, ...]:
    try:
        output = subprocess.check_output(
            ["git", "status", "--porcelain"],
            cwd=repo_root,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return ("<git-status-unavailable>",)
    return tuple(sorted(line.rstrip() for line in output.splitlines() if line.strip()))


def _require_unique_text(
    values: Sequence[str],
    *,
    context: str,
    required: bool = True,
) -> None:
    if required and not values:
        raise ValueError(f"{context} is required")
    if any(not isinstance(item, str) or not item.strip() for item in values):
        raise ValueError(f"{context} contains empty text")
    if len(values) != len(set(values)):
        raise ValueError(f"{context} contains duplicates")


__all__ = [
    "CANONICAL_COMMAND_RUN_SCHEMA_VERSION",
    "COMMAND_REPRODUCIBILITY_AUDIT_SCHEMA_VERSION",
    "REQUIRED_COMMAND_HASH_CATEGORIES",
    "CommandHashEntry",
    "CommandHashEntryKind",
    "audit_command_run_manifest",
    "build_command_run_manifest",
    "command_file_hash_entry",
    "command_inline_hash_entry",
    "write_command_run_manifest",
]
