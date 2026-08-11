"""Fail-closed lifecycle validation for the tracked E2R v6 cutover dossier.

The lifecycle layer does not create authority.  It verifies a caller-supplied
declaration against files that already exist in Git, projects the canonical
production/Gold/score/Stage status, and reports contradictions.  In
particular, an absent final receipt stays absent and makes the audit fail; it
is never synthesized from an untracked production output.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date, datetime
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_results import (
    CANARY_COMPILATION_PASS,
    CANARY_SUMMARY_PASS,
    CANARY_SUMMARY_SCHEMA,
    compile_cross_archetype_canary_directory,
    validate_cross_archetype_canary_summary,
)
from e2r.production.v6_canary_selection import (
    FORCED_SELECTION,
    ISSUER_PROFILE_MANIFEST_NAME,
    validate_cross_archetype_canary_selection_manifest,
)
from e2r.production.v6_issuer_business_profile import (
    PROFILE_PASS as ISSUER_PROFILE_PASS,
    validate_issuer_business_profile_result,
)
from e2r.production.v6_production_static_audit import (
    PRODUCTION_STATIC_AUDIT_LEAF,
    validate_production_static_audit,
)
from e2r.research_brain.researcher_mode.tracked_receipts import (
    PHASE101_TARGET_IDS,
    VERIFICATION_PASS,
    VERIFICATION_SCHEMA,
)
from e2r.research_brain.researcher_mode.tracked_readiness import (
    TRACKED_READINESS_PASS,
    TRACKED_READINESS_SCHEMA,
    _repository_identity_is_trusted,
)


ARTIFACT_LIFECYCLE_MANIFEST_SCHEMA = (
    "e2r_v6_artifact_lifecycle_manifest_v1"
)
ARTIFACT_LIFECYCLE_AUDIT_SCHEMA = "e2r_v6_artifact_lifecycle_audit_v1"
ARTIFACT_LIFECYCLE_PASS = "E2R_V6_ARTIFACT_LIFECYCLE_PASS"
ARTIFACT_LIFECYCLE_FAIL = "E2R_V6_ARTIFACT_LIFECYCLE_FAIL"

CURRENT_AUTHORITY = "CURRENT_AUTHORITY"
HISTORICAL_SNAPSHOT = "HISTORICAL_SNAPSHOT"
SUPERSEDED = "SUPERSEDED"
ARTIFACT_ROLES = frozenset(
    {CURRENT_AUTHORITY, HISTORICAL_SNAPSHOT, SUPERSEDED}
)

FINAL_ROOT_RELATIVE = Path("docs/operational/e2r_v6_operational_cutover")
FINAL_ROOT_REQUIRED_FILES = (
    "README.md",
    "starting_state.json",
    "artifact_lifecycle_manifest.json",
    "artifact_lifecycle_audit.json",
    "clean_clone_reproduction.json",
    "provider_runtime_audit.json",
    PRODUCTION_STATIC_AUDIT_LEAF,
    "cross_archetype_canary_selection.json",
    "cross_archetype_canary_summary.json",
    "current_krx_census_summary.json",
    "current_krx_stage_map_compact.jsonl",
)
# Phase 109 publishes these two terminal documents only after Reviewer K--V
# has consumed the Phase-104 lifecycle audit.  Requiring their own hashes in
# that earlier manifest creates an impossible self-reference: the reviewer
# gate hashes the lifecycle audit while the lifecycle manifest would hash the
# reviewer gate.  They are therefore final publications, not Phase-104 input
# artifacts.  The Phase-109 publisher and final repository probe validate
# them separately.
TERMINAL_PUBLICATION_FILES = (
    "operational_acceptance_reviewer_gate.json",
    "operational_cutover_final.md",
)
CANARY_RECEIPT_DATE = "2026-07-12"
CANARY_TARGET_IDS = ("005930", "000660")
CANARY_TARGET_REQUIRED_FILES = (
    "receipt_manifest.json",
    "score_receipt.json",
    "component_decisions.jsonl",
    "scoring_facts.jsonl",
    "judge_decisions.jsonl",
    "source_manifest.jsonl",
    "anchor_manifest.jsonl",
    "provider_calls.jsonl",
    "stagecourt_receipt.json",
)
CURRENT_LIVE_CANARY_PREFIXES = ("C08_", "C15_", "C17_", "C24_", "C28_")
CLEAN_CLONE_REQUIRED_FILES = (
    "receipt_recompute_result.json",
    "tracked_readiness_result.json",
    "test_result.json",
)

STATUS_PROJECTION_KEYS = frozenset(
    {
        "production_research_status",
        "gold_evaluation_status",
        "score_status",
        "stagecourt_status",
        "score_valid",
        "stage_final",
    }
)
FINAL_STATUS_PROJECTION: Mapping[str, Any] = {
    "production_research_status": "COMPLETE",
    "gold_evaluation_status": "PASS",
    "score_status": "COMPLETE",
    "stagecourt_status": "FINAL",
    "score_valid": True,
    "stage_final": True,
}
PRE_GOLD_PENDING_STATUS = "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
CANONICAL_MANIFEST_NAME = "artifact_lifecycle_manifest.json"
CLEAN_CLONE_REPRODUCTION_SCHEMA = "e2r_v6_clean_clone_reproduction_v1"
CLEAN_CLONE_REPRODUCTION_PASS = "E2R_V6_CLEAN_CLONE_REPRODUCTION_PASS"
CLEAN_CLONE_TEST_SCHEMA = "e2r_v6_clean_clone_test_result_v1"
CLEAN_CLONE_TEST_PASS = "E2R_V6_CLEAN_CLONE_TEST_PASS"
PROVIDER_RUNTIME_AUDIT_SCHEMA = "e2r_v6_provider_runtime_audit_v1"
PROVIDER_RUNTIME_AUDIT_PASS = "E2R_V6_PROVIDER_RUNTIME_AUDIT_PASS"
CROSS_ARCHETYPE_CANARY_SUMMARY_SCHEMA = CANARY_SUMMARY_SCHEMA
CROSS_ARCHETYPE_CANARY_SUMMARY_PASS = CANARY_SUMMARY_PASS

_CLEAN_CLONE_REPRODUCTION_KEYS = frozenset(
    {
        "schema_version",
        "status",
        "as_of_date",
        "receipt_recompute_result_hash",
        "tracked_readiness_result_hash",
        "test_result_hash",
        "critical_count_sum",
        "production_readiness_authority",
    }
)
_CLEAN_CLONE_TEST_KEYS = frozenset(
    {
        "schema_version",
        "status",
        "executed_test_count",
        "failed_test_count",
        "error_test_count",
        "critical_count_sum",
        "production_readiness_authority",
    }
)
_PROVIDER_RUNTIME_AUDIT_KEYS = frozenset(
    {
        "schema_version",
        "status",
        "as_of_date",
        "provider_call_counts",
        "scored_fact_provider_lineage_counts",
        "provider_error_count",
        "unauthorized_provider_call_count",
        "local_provider_call_count",
        "qwen_call_count",
        "ollama_call_count",
        "inherited_qwen_scored_fact_count",
        "inherited_ollama_scored_fact_count",
        "critical_count_sum",
        "production_readiness_authority",
    }
)
ARTIFACT_ENTRY_KEYS = frozenset(
    {
        "artifact_id",
        "artifact_path",
        "artifact_role",
        "authority_scope",
        "as_of_date",
        "generated_at",
        "commit_sha",
        "content_hash",
        "supersedes",
        "superseded_by",
        "production_readiness_authority",
    }
)

_HEX_40 = re.compile(r"[0-9a-f]{40}\Z")
_HEX_64 = re.compile(r"[0-9a-f]{64}\Z")
_PENDING = re.compile(r"PENDING", flags=re.IGNORECASE)
_MARKDOWN_BOOL = re.compile(
    r"\b(score_valid|stage_final)\s*[:=]\s*(true|false)\b",
    flags=re.IGNORECASE,
)
_MARKDOWN_STATUS = re.compile(
    r"\b(production_research_status|gold_evaluation_status|score_status|"
    r"stagecourt_status)\s*[:=]\s*([A-Za-z0-9_-]+)",
    flags=re.IGNORECASE,
)


def _strict_json_loads(text: str) -> Any:
    def reject_constant(value: str) -> None:
        raise ValueError(f"non-finite JSON constant is forbidden: {value}")

    return json.loads(text, parse_constant=reject_constant)


def load_artifact_lifecycle_manifest(path: str | Path) -> Mapping[str, Any]:
    """Load a finite JSON object without following an input-file symlink."""

    manifest_path = Path(path)
    if manifest_path.is_symlink():
        raise ValueError("artifact lifecycle manifest cannot be a symlink")
    try:
        payload = _strict_json_loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("artifact lifecycle manifest is not valid JSON") from exc
    if not isinstance(payload, Mapping):
        raise ValueError("artifact lifecycle manifest must be a JSON object")
    return dict(payload)


def _safe_relative_path(value: Any) -> str | None:
    raw = str(value or "")
    if (
        not raw
        or raw.strip() != raw
        or "\\" in raw
        or any(ord(char) < 32 or ord(char) == 127 for char in raw)
    ):
        return None
    path = PurePosixPath(raw)
    if path.is_absolute() or raw != path.as_posix():
        return None
    if any(part in {"", ".", ".."} for part in path.parts):
        return None
    return path.as_posix()


def _is_within(relative_path: str, relative_root: str) -> bool:
    path = PurePosixPath(relative_path)
    root = PurePosixPath(relative_root)
    return path == root or root in path.parents


def _path_has_symlink(repo: Path, relative_path: str) -> bool:
    current = repo
    for part in PurePosixPath(relative_path).parts:
        current = current / part
        if current.is_symlink():
            return True
    return False


def _git_output(repo: Path, *args: str) -> str | None:
    try:
        return subprocess.check_output(
            ["git", *args],
            cwd=repo,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def _git_ok(repo: Path, *args: str) -> bool:
    try:
        return (
            subprocess.run(
                ["git", *args],
                cwd=repo,
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode
            == 0
        )
    except OSError:
        return False


def _repository_head(repo: Path) -> str | None:
    top = _git_output(repo, "rev-parse", "--show-toplevel")
    head = _git_output(repo, "rev-parse", "HEAD")
    if top is None or head is None:
        return None
    try:
        if Path(top).resolve() != repo:
            return None
    except OSError:
        return None
    return head if _HEX_40.fullmatch(head) else None


def _valid_timestamp(value: Any) -> bool:
    text = str(value or "")
    if not text:
        return False
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _valid_date(value: Any) -> bool:
    try:
        return date.fromisoformat(str(value or "")) is not None
    except ValueError:
        return False


def _valid_identifier(value: Any) -> bool:
    text = str(value or "")
    return bool(
        text
        and len(text) <= 256
        and text.strip() == text
        and not any(ord(char) < 32 for char in text)
    )


def _artifact_content(path: Path) -> Any:
    if path.suffix == ".json":
        try:
            return _strict_json_loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
            return None
    if path.suffix == ".jsonl":
        rows: list[Any] = []
        try:
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    rows.append(_strict_json_loads(line))
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
            return None
        return rows
    if path.suffix.lower() == ".md":
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            return None
    return None


def _status_observations(content: Any) -> Mapping[str, tuple[Any, ...]]:
    observations: dict[str, list[Any]] = defaultdict(list)
    if isinstance(content, str):
        for match in _MARKDOWN_BOOL.finditer(content):
            observations[match.group(1).casefold()].append(
                match.group(2).casefold() == "true"
            )
        for match in _MARKDOWN_STATUS.finditer(content):
            observations[match.group(1).casefold()].append(match.group(2))
        return {key: tuple(values) for key, values in observations.items()}

    def visit(value: Any) -> None:
        if isinstance(value, Mapping):
            for key, child in value.items():
                if key in STATUS_PROJECTION_KEYS:
                    observations[str(key)].append(child)
                visit(child)
        elif isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
            for child in value:
                visit(child)

    visit(content)
    return {key: tuple(values) for key, values in observations.items()}


def _top_level_mapping(content: Any) -> Mapping[str, Any] | None:
    return content if isinstance(content, Mapping) else None


def _content_sha256(path: Path) -> str | None:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def _canonical_manifest_binding(
    *,
    repo: Path,
    final_root: str,
    payload: Mapping[str, Any],
    head: str | None,
) -> Mapping[str, Any]:
    """Bind the caller payload to the canonical tracked manifest file."""

    relative = f"{final_root}/{CANONICAL_MANIFEST_NAME}"
    path = repo / relative
    digest = _content_sha256(path)
    binding = (
        _validate_git_binding(
            repo=repo,
            relative_path=relative,
            declared_commit=head or "",
            declared_content_hash=digest or "",
            head=head,
        )
        if digest is not None
        else {}
    )
    content = _artifact_content(path)
    exact_payload = isinstance(content, Mapping) and dict(content) == dict(payload)
    return {
        "canonical_path": relative,
        "payload_matches_canonical_file": exact_payload,
        "git_binding": dict(binding),
        "valid": bool(exact_payload and binding and all(binding.values())),
    }


def _zero_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value == 0


def _nonnegative_count_mapping(value: Any) -> bool:
    return bool(
        isinstance(value, Mapping)
        and value
        and all(
            isinstance(item, int) and not isinstance(item, bool) and item >= 0
            for item in value.values()
        )
    )


def _authorized_provider_count_mapping(value: Any) -> bool:
    return bool(
        _nonnegative_count_mapping(value)
        and set(value) <= {"CODEX", "COLLABORATION_CODEX"}
        and sum(value.values()) > 0
    )


def _semantic_final_artifact_failures(
    *,
    repo: Path,
    final_root: str,
    current_contents_by_path: Mapping[str, Any],
) -> tuple[Mapping[str, Any], ...]:
    """Validate hard-gate artifacts by their real schema and PASS contract."""

    failures: list[Mapping[str, Any]] = []

    def content(relative_suffix: str) -> Any:
        relative = f"{final_root}/{relative_suffix}"
        value = current_contents_by_path.get(relative)
        if value is None:
            failures.append(
                {"code": "CURRENT_SEMANTIC_ARTIFACT_MISSING", "artifact_path": relative}
            )
        return value

    selection = content("cross_archetype_canary_selection.json")
    summary = content("cross_archetype_canary_summary.json")
    forced_selection = bool(
        isinstance(selection, Mapping)
        and any(
            isinstance(row, Mapping)
            and row.get("selection_mode") == FORCED_SELECTION
            for row in selection.get("selections") or ()
        )
    )
    issuer_profile: Mapping[str, Any] | None = None
    if forced_selection:
        profile_relative = f"{final_root}/{ISSUER_PROFILE_MANIFEST_NAME}"
        raw_profile = current_contents_by_path.get(profile_relative)
        if isinstance(raw_profile, Mapping):
            try:
                validated_profile = validate_issuer_business_profile_result(
                    raw_profile
                )
                if validated_profile.get("status") != ISSUER_PROFILE_PASS:
                    raise ValueError("issuer profile is not COMPLETE")
                issuer_profile = validated_profile
            except (TypeError, ValueError) as exc:
                failures.append(
                    {
                        "code": "ISSUER_BUSINESS_PROFILE_CONTRACT_INVALID",
                        "artifact_path": profile_relative,
                        "detail": str(exc),
                    }
                )
        else:
            failures.append(
                {
                    "code": "ISSUER_BUSINESS_PROFILE_CURRENT_AUTHORITY_MISSING",
                    "artifact_path": profile_relative,
                }
            )
    selection_valid = False
    if isinstance(selection, Mapping):
        try:
            validate_cross_archetype_canary_selection_manifest(
                selection,
                issuer_business_profile_manifest=issuer_profile,
            )
            selection_valid = True
        except (TypeError, ValueError) as exc:
            failures.append(
                {
                    "code": "CANARY_SELECTION_CONTRACT_INVALID",
                    "artifact_path": f"{final_root}/cross_archetype_canary_selection.json",
                    "detail": str(exc),
                }
            )
    summary_contract_valid = False
    if selection_valid and isinstance(selection, Mapping) and isinstance(summary, Mapping):
        try:
            validate_cross_archetype_canary_summary(
                summary,
                selection=selection,
                issuer_business_profile_manifest=issuer_profile,
            )
            recomputed = compile_cross_archetype_canary_directory(
                selection=selection,
                live_root=repo / final_root / "current_live_canaries",
                issuer_business_profile_manifest=issuer_profile,
                repo_root=repo,
            )
            summary_contract_valid = bool(
                recomputed.get("status") == CANARY_COMPILATION_PASS
                and isinstance(recomputed.get("summary"), Mapping)
                and dict(recomputed["summary"]) == dict(summary)
            )
        except (OSError, TypeError, ValueError):
            summary_contract_valid = False
    if not summary_contract_valid:
        failures.append({"code": "CROSS_ARCHETYPE_CANARY_RESULT_SUMMARY_INVALID"})

    receipt_result = content("clean_clone/receipt_recompute_result.json")
    readiness_result = content("clean_clone/tracked_readiness_result.json")
    test_result = content("clean_clone/test_result.json")
    clean_clone = content("clean_clone_reproduction.json")
    expected_targets = tuple(sorted(PHASE101_TARGET_IDS))
    if not (
        isinstance(receipt_result, Mapping)
        and receipt_result.get("schema_version") == VERIFICATION_SCHEMA
        and receipt_result.get("status") == VERIFICATION_PASS
        and receipt_result.get("offline") is True
        and _zero_int(receipt_result.get("critical_count_sum"))
        and receipt_result.get("target_count") == len(expected_targets)
        and tuple(sorted(str(value) for value in receipt_result.get("target_ids") or ()))
        == expected_targets
    ):
        failures.append({"code": "CLEAN_CLONE_RECEIPT_RECOMPUTE_NOT_PASS"})
    if not (
        isinstance(readiness_result, Mapping)
        and readiness_result.get("schema_version") == TRACKED_READINESS_SCHEMA
        and readiness_result.get("status") == TRACKED_READINESS_PASS
        and readiness_result.get("ready") is True
        and readiness_result.get("offline") is True
        and readiness_result.get("production_readiness_authority") is False
        and _zero_int(readiness_result.get("critical_count"))
        and readiness_result.get("same_receipt_replay_variance") == 0
        and tuple(sorted(str(value) for value in readiness_result.get("target_ids") or ()))
        == expected_targets
    ):
        failures.append({"code": "CLEAN_CLONE_TRACKED_READINESS_NOT_PASS"})
    if not (
        isinstance(test_result, Mapping)
        and set(test_result) == _CLEAN_CLONE_TEST_KEYS
        and test_result.get("schema_version") == CLEAN_CLONE_TEST_SCHEMA
        and test_result.get("status") == CLEAN_CLONE_TEST_PASS
        and isinstance(test_result.get("executed_test_count"), int)
        and not isinstance(test_result.get("executed_test_count"), bool)
        and test_result.get("executed_test_count") > 0
        and all(
            _zero_int(test_result.get(key))
            for key in ("failed_test_count", "error_test_count", "critical_count_sum")
        )
        and test_result.get("production_readiness_authority") is False
    ):
        failures.append({"code": "CLEAN_CLONE_TEST_RESULT_NOT_PASS"})
    clean_clone_hashes = {
        "receipt_recompute_result_hash": _content_sha256(
            repo / final_root / "clean_clone" / "receipt_recompute_result.json"
        ),
        "tracked_readiness_result_hash": _content_sha256(
            repo / final_root / "clean_clone" / "tracked_readiness_result.json"
        ),
        "test_result_hash": _content_sha256(
            repo / final_root / "clean_clone" / "test_result.json"
        ),
    }
    if not (
        isinstance(clean_clone, Mapping)
        and set(clean_clone) == _CLEAN_CLONE_REPRODUCTION_KEYS
        and clean_clone.get("schema_version") == CLEAN_CLONE_REPRODUCTION_SCHEMA
        and clean_clone.get("status") == CLEAN_CLONE_REPRODUCTION_PASS
        and clean_clone.get("as_of_date") == CANARY_RECEIPT_DATE
        and _zero_int(clean_clone.get("critical_count_sum"))
        and clean_clone.get("production_readiness_authority") is False
        and all(
            digest is not None and clean_clone.get(key) == digest
            for key, digest in clean_clone_hashes.items()
        )
    ):
        failures.append({"code": "CLEAN_CLONE_REPRODUCTION_CONTRACT_INVALID"})

    provider = content("provider_runtime_audit.json")
    provider_audit_as_of = (
        str(selection.get("selection_as_of_date") or "")
        if isinstance(selection, Mapping)
        and _valid_date(selection.get("selection_as_of_date"))
        else CANARY_RECEIPT_DATE
    )
    if not (
        isinstance(provider, Mapping)
        and set(provider) == _PROVIDER_RUNTIME_AUDIT_KEYS
        and provider.get("schema_version") == PROVIDER_RUNTIME_AUDIT_SCHEMA
        and provider.get("status") == PROVIDER_RUNTIME_AUDIT_PASS
        and provider.get("as_of_date") == provider_audit_as_of
        and _authorized_provider_count_mapping(provider.get("provider_call_counts"))
        and _authorized_provider_count_mapping(
            provider.get("scored_fact_provider_lineage_counts")
        )
        and all(
            _zero_int(provider.get(key))
            for key in (
                "provider_error_count",
                "unauthorized_provider_call_count",
                "local_provider_call_count",
                "qwen_call_count",
                "ollama_call_count",
                "inherited_qwen_scored_fact_count",
                "inherited_ollama_scored_fact_count",
                "critical_count_sum",
            )
        )
        and provider.get("production_readiness_authority") is False
    ):
        failures.append({"code": "PROVIDER_RUNTIME_AUDIT_CONTRACT_INVALID"})
    production_static_audit = content(PRODUCTION_STATIC_AUDIT_LEAF)
    if not (
        isinstance(production_static_audit, Mapping)
        and validate_production_static_audit(production_static_audit)
    ):
        failures.append({"code": "PRODUCTION_STATIC_AUDIT_CONTRACT_INVALID"})
    return tuple(failures)


def _validate_git_binding(
    *,
    repo: Path,
    relative_path: str,
    declared_commit: str,
    declared_content_hash: str,
    head: str | None,
) -> Mapping[str, Any]:
    path = repo / relative_path
    result: dict[str, Any] = {
        "exists_regular_file": False,
        "no_symlink_in_path": False,
        "git_tracked": False,
        "head_index_worktree_match": False,
        "declared_commit_exists_and_is_ancestor": False,
        "declared_commit_blob_matches": False,
        "content_hash_matches": False,
    }
    if _path_has_symlink(repo, relative_path):
        return result
    result["no_symlink_in_path"] = True
    if not path.is_file():
        return result
    result["exists_regular_file"] = True
    tracked = _git_output(repo, "ls-files", "--error-unmatch", "--", relative_path)
    index_line = _git_output(repo, "ls-files", "-s", "--", relative_path)
    if tracked != relative_path or not index_line:
        return result
    index_rows = [line for line in index_line.splitlines() if line.strip()]
    if len(index_rows) != 1:
        return result
    fields = index_rows[0].split(maxsplit=3)
    if len(fields) != 4 or fields[2] != "0" or fields[3] != relative_path:
        return result
    index_blob = fields[1]
    result["git_tracked"] = True
    head_blob = _git_output(repo, "rev-parse", f"HEAD:{relative_path}")
    worktree_blob = _git_output(repo, "hash-object", "--", relative_path)
    result["head_index_worktree_match"] = bool(
        head_blob and head_blob == index_blob == worktree_blob
    )
    commit_valid = bool(
        _HEX_40.fullmatch(declared_commit)
        and head
        and _git_ok(repo, "cat-file", "-e", f"{declared_commit}^{{commit}}")
        and _git_ok(repo, "merge-base", "--is-ancestor", declared_commit, head)
    )
    result["declared_commit_exists_and_is_ancestor"] = commit_valid
    declared_blob = (
        _git_output(repo, "rev-parse", f"{declared_commit}:{relative_path}")
        if commit_valid
        else None
    )
    result["declared_commit_blob_matches"] = bool(
        declared_blob and declared_blob == head_blob == index_blob
    )
    actual_content_hash = _content_sha256(path)
    result["content_hash_matches"] = bool(
        _HEX_64.fullmatch(declared_content_hash)
        and actual_content_hash == declared_content_hash
    )
    return result


def _required_paths(final_root: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
    files = [f"{final_root}/{name}" for name in FINAL_ROOT_REQUIRED_FILES]
    directories = [
        final_root,
        f"{final_root}/canary_receipts",
        f"{final_root}/canary_receipts/{CANARY_RECEIPT_DATE}",
        f"{final_root}/current_live_canaries",
        f"{final_root}/clean_clone",
    ]
    for target_id in CANARY_TARGET_IDS:
        target_root = (
            f"{final_root}/canary_receipts/{CANARY_RECEIPT_DATE}/{target_id}"
        )
        directories.append(target_root)
        files.extend(
            f"{target_root}/{name}" for name in CANARY_TARGET_REQUIRED_FILES
        )
    files.extend(
        f"{final_root}/clean_clone/{name}"
        for name in CLEAN_CLONE_REQUIRED_FILES
    )
    return tuple(sorted(files)), tuple(sorted(directories))


def _supersession_cycles(
    rows_by_id: Mapping[str, Mapping[str, Any]],
) -> tuple[tuple[str, ...], ...]:
    graph = {
        artifact_id: tuple(
            target
            for target in row.get("supersedes", ())
            if target in rows_by_id
        )
        for artifact_id, row in rows_by_id.items()
    }
    color: dict[str, int] = {}
    stack: list[str] = []
    cycles: set[tuple[str, ...]] = set()

    def visit(node: str) -> None:
        color[node] = 1
        stack.append(node)
        for child in graph.get(node, ()):
            state = color.get(child, 0)
            if state == 0:
                visit(child)
            elif state == 1 and child in stack:
                cycle = stack[stack.index(child) :]
                rotations = [
                    tuple(cycle[index:] + cycle[:index])
                    for index in range(len(cycle))
                ]
                cycles.add(min(rotations))
        stack.pop()
        color[node] = 2

    for artifact_id in sorted(graph):
        if color.get(artifact_id, 0) == 0:
            visit(artifact_id)
    return tuple(sorted(cycles))


def _score_stage_mismatches(
    current_contents: Mapping[str, tuple[Mapping[str, Any], Any]],
    projection: Mapping[str, Any],
) -> tuple[Mapping[str, Any], ...]:
    scores: dict[str, list[tuple[str, Mapping[str, Any]]]] = defaultdict(list)
    stages: dict[str, list[tuple[str, Mapping[str, Any]]]] = defaultdict(list)
    for artifact_id, (_row, content) in current_contents.items():
        payload = _top_level_mapping(content)
        if payload is None:
            continue
        target_id = str(payload.get("target_id") or "")
        schema = str(payload.get("schema_version") or "")
        if not target_id:
            continue
        if schema == "e2r_v6_score_receipt_v1":
            scores[target_id].append((artifact_id, payload))
        elif schema == "e2r_v6_stagecourt_receipt_v1":
            stages[target_id].append((artifact_id, payload))

    failures: list[Mapping[str, Any]] = []
    for target_id in sorted(set(scores) | set(stages)):
        target_scores = scores.get(target_id, ())
        target_stages = stages.get(target_id, ())
        reasons: list[str] = []
        if len(target_scores) != 1:
            reasons.append("CURRENT_SCORE_RECEIPT_COUNT_NOT_ONE")
        if len(target_stages) != 1:
            reasons.append("CURRENT_STAGECOURT_RECEIPT_COUNT_NOT_ONE")
        if len(target_scores) == 1 and len(target_stages) == 1:
            _score_id, score = target_scores[0]
            _stage_id, stage = target_stages[0]
            vector = score.get("component_score_vector")
            comparisons = {
                "TARGET_ID_MISMATCH": stage.get("target_id") == score.get("target_id"),
                "SCORE_RECEIPT_ID_MISMATCH": (
                    stage.get("score_receipt_id") == score.get("receipt_id")
                ),
                "COMPONENT_VECTOR_HASH_MISMATCH": (
                    isinstance(vector, Mapping)
                    and stage.get("component_score_vector_hash")
                    == stable_hash(vector)
                ),
                "TOTAL_SCORE_MISMATCH": _numbers_match(
                    stage.get("total_score"), score.get("total_score")
                ),
                "CANONICAL_STAGE_MISMATCH": (
                    stage.get("canonical_stage") == score.get("canonical_stage")
                ),
                "SCORE_VALID_MISMATCH": (
                    stage.get("score_valid") == score.get("score_valid")
                    == projection.get("score_valid")
                ),
                "STAGECOURT_STATUS_MISMATCH": (
                    stage.get("decision_status")
                    == score.get("stagecourt_status")
                    == projection.get("stagecourt_status")
                ),
                "PRODUCTION_STATUS_MISMATCH": (
                    score.get("production_research_status")
                    == projection.get("production_research_status")
                ),
                "GOLD_STATUS_MISMATCH": (
                    score.get("gold_evaluation_status")
                    == projection.get("gold_evaluation_status")
                ),
                "SCORE_STATUS_MISMATCH": (
                    score.get("score_status") == projection.get("score_status")
                ),
            }
            reasons.extend(
                reason for reason, matched in comparisons.items() if not matched
            )
        if reasons:
            failures.append(
                {
                    "target_id": target_id,
                    "reasons": sorted(set(reasons)),
                    "score_artifact_ids": sorted(row[0] for row in target_scores),
                    "stagecourt_artifact_ids": sorted(
                        row[0] for row in target_stages
                    ),
                }
            )
    return tuple(failures)


def _numbers_match(left: Any, right: Any) -> bool:
    if isinstance(left, bool) or isinstance(right, bool):
        return False
    try:
        left_number = float(left)
        right_number = float(right)
    except (TypeError, ValueError):
        return False
    return abs(left_number - right_number) <= max(
        1e-9, abs(right_number) * 1e-9
    )


def _required_current_authority_paths(final_root: str) -> frozenset[str]:
    result = {
        f"{final_root}/clean_clone_reproduction.json",
        f"{final_root}/provider_runtime_audit.json",
        f"{final_root}/{PRODUCTION_STATIC_AUDIT_LEAF}",
        f"{final_root}/cross_archetype_canary_selection.json",
        f"{final_root}/cross_archetype_canary_summary.json",
        f"{final_root}/current_krx_census_summary.json",
        f"{final_root}/current_krx_stage_map_compact.jsonl",
    }
    for target_id in CANARY_TARGET_IDS:
        target_root = (
            f"{final_root}/canary_receipts/{CANARY_RECEIPT_DATE}/{target_id}"
        )
        result.add(f"{target_root}/score_receipt.json")
        result.add(f"{target_root}/stagecourt_receipt.json")
    return frozenset(result)


def compile_artifact_lifecycle(
    manifest: Mapping[str, Any] | str | Path,
    *,
    repo_root: str | Path = ".",
    final_root: str | Path = FINAL_ROOT_RELATIVE,
    prospective_audit_path: str | Path | None = None,
) -> Mapping[str, Any]:
    """Compile a deterministic lifecycle audit without creating artifacts."""

    payload = (
        load_artifact_lifecycle_manifest(manifest)
        if isinstance(manifest, (str, Path))
        else dict(manifest)
    )
    manifest_hash = stable_hash(payload)
    repo = Path(repo_root).resolve()
    head = _repository_head(repo)
    repository_identity_trusted = _repository_identity_is_trusted(repo)
    canonical_final_root = FINAL_ROOT_RELATIVE.as_posix()
    requested_final_root = _safe_relative_path(Path(final_root).as_posix())
    final_root_argument_valid = requested_final_root == canonical_final_root
    safe_final_root = canonical_final_root
    canonical_manifest_binding = _canonical_manifest_binding(
        repo=repo,
        final_root=safe_final_root,
        payload=payload,
        head=head,
    )

    top_level_valid = (
        set(payload) == {"schema_version", "artifacts", "status_projection"}
        and payload.get("schema_version") == ARTIFACT_LIFECYCLE_MANIFEST_SCHEMA
        and isinstance(payload.get("artifacts"), list)
        and isinstance(payload.get("status_projection"), Mapping)
    )
    raw_rows = payload.get("artifacts") if isinstance(payload.get("artifacts"), list) else []
    projection = (
        dict(payload.get("status_projection") or {})
        if isinstance(payload.get("status_projection"), Mapping)
        else {}
    )

    invalid_rows: list[Mapping[str, Any]] = []
    validated_rows: list[Mapping[str, Any]] = []
    artifact_audits: list[Mapping[str, Any]] = []
    contents_by_id: dict[str, tuple[Mapping[str, Any], Any]] = {}
    artifact_ids: list[str] = []
    artifact_paths: list[str] = []

    for index, raw_row in enumerate(raw_rows):
        errors: list[str] = []
        if not isinstance(raw_row, Mapping):
            invalid_rows.append({"row_index": index, "errors": ["ROW_NOT_OBJECT"]})
            continue
        row = dict(raw_row)
        if set(row) != ARTIFACT_ENTRY_KEYS:
            errors.append("ARTIFACT_KEY_ROSTER_MISMATCH")
        artifact_id = str(row.get("artifact_id") or "")
        artifact_path = _safe_relative_path(row.get("artifact_path"))
        role = str(row.get("artifact_role") or "")
        authority_scope = str(row.get("authority_scope") or "")
        commit_sha = str(row.get("commit_sha") or "")
        content_hash = str(row.get("content_hash") or "")
        supersedes = row.get("supersedes")
        superseded_by = row.get("superseded_by")
        production_authority = row.get("production_readiness_authority")
        if not _valid_identifier(artifact_id):
            errors.append("ARTIFACT_ID_INVALID")
        if artifact_path is None or not _is_within(artifact_path, safe_final_root):
            errors.append("ARTIFACT_PATH_INVALID_OR_OUTSIDE_FINAL_ROOT")
        if role not in ARTIFACT_ROLES:
            errors.append("ARTIFACT_ROLE_INVALID")
        if not _valid_identifier(authority_scope):
            errors.append("AUTHORITY_SCOPE_INVALID")
        if not _valid_date(row.get("as_of_date")):
            errors.append("AS_OF_DATE_INVALID")
        if not _valid_timestamp(row.get("generated_at")):
            errors.append("GENERATED_AT_INVALID_OR_TIMEZONE_MISSING")
        if _HEX_40.fullmatch(commit_sha) is None:
            errors.append("COMMIT_SHA_INVALID")
        if _HEX_64.fullmatch(content_hash) is None:
            errors.append("CONTENT_HASH_INVALID")
        if (
            not isinstance(supersedes, list)
            or any(not _valid_identifier(value) for value in supersedes)
            or len(set(str(value) for value in supersedes)) != len(supersedes)
        ):
            errors.append("SUPERSEDES_INVALID")
        if superseded_by is not None and not _valid_identifier(superseded_by):
            errors.append("SUPERSEDED_BY_INVALID")
        if not isinstance(production_authority, bool):
            errors.append("PRODUCTION_READINESS_AUTHORITY_NOT_BOOLEAN")
        if role == CURRENT_AUTHORITY and production_authority is not True:
            errors.append("CURRENT_AUTHORITY_MUST_HAVE_PRODUCTION_AUTHORITY")
        if role != CURRENT_AUTHORITY and production_authority is not False:
            errors.append("NONCURRENT_ARTIFACT_CANNOT_HAVE_PRODUCTION_AUTHORITY")
        if role == CURRENT_AUTHORITY and superseded_by is not None:
            errors.append("CURRENT_AUTHORITY_CANNOT_BE_SUPERSEDED")
        if role == SUPERSEDED and superseded_by is None:
            errors.append("SUPERSEDED_ARTIFACT_REQUIRES_SUCCESSOR")

        binding: Mapping[str, Any] = {}
        content: Any = None
        if artifact_path is not None and _is_within(artifact_path, safe_final_root):
            binding = _validate_git_binding(
                repo=repo,
                relative_path=artifact_path,
                declared_commit=commit_sha,
                declared_content_hash=content_hash,
                head=head,
            )
            for key, passed in binding.items():
                if not passed:
                    errors.append(f"GIT_BINDING:{key}")
            if binding.get("exists_regular_file") and binding.get(
                "no_symlink_in_path"
            ):
                content = _artifact_content(repo / artifact_path)
                if (repo / artifact_path).suffix in {".json", ".jsonl", ".md"} and content is None:
                    errors.append("ARTIFACT_CONTENT_UNREADABLE_OR_INVALID")

        normalized = {
            **row,
            "artifact_id": artifact_id,
            "artifact_path": artifact_path or str(row.get("artifact_path") or ""),
            "artifact_role": role,
            "authority_scope": authority_scope,
            "supersedes": [str(value) for value in supersedes]
            if isinstance(supersedes, list)
            else [],
        }
        artifact_ids.append(artifact_id)
        artifact_paths.append(normalized["artifact_path"])
        validated_rows.append(normalized)
        if artifact_id and content is not None:
            contents_by_id.setdefault(artifact_id, (normalized, content))
        artifact_audits.append(
            {
                "artifact_id": artifact_id,
                "artifact_path": normalized["artifact_path"],
                "artifact_role": role,
                "authority_scope": authority_scope,
                "binding": dict(binding),
                "valid": not errors,
                "errors": sorted(set(errors)),
            }
        )
        if errors:
            invalid_rows.append(
                {
                    "row_index": index,
                    "artifact_id": artifact_id,
                    "errors": sorted(set(errors)),
                }
            )

    duplicate_ids = sorted(
        artifact_id for artifact_id, count in Counter(artifact_ids).items() if count > 1
    )
    duplicate_paths = sorted(
        artifact_path
        for artifact_path, count in Counter(artifact_paths).items()
        if artifact_path and count > 1
    )
    rows_by_id = {
        str(row["artifact_id"]): row
        for row in validated_rows
        if str(row.get("artifact_id") or "") not in duplicate_ids
    }

    current_by_scope: dict[str, list[str]] = defaultdict(list)
    for row in validated_rows:
        if row.get("artifact_role") == CURRENT_AUTHORITY:
            current_by_scope[str(row.get("authority_scope") or "")].append(
                str(row.get("artifact_id") or "")
            )
    duplicate_current_scopes = {
        scope: sorted(ids)
        for scope, ids in sorted(current_by_scope.items())
        if scope and len(ids) > 1
    }

    unknown_supersession: list[Mapping[str, str]] = []
    bidirectional_mismatches: list[Mapping[str, str]] = []
    for artifact_id, row in rows_by_id.items():
        for older_id in row.get("supersedes", ()):
            older = rows_by_id.get(str(older_id))
            if older is None:
                unknown_supersession.append(
                    {"artifact_id": artifact_id, "unknown_artifact_id": str(older_id)}
                )
            elif older.get("superseded_by") != artifact_id:
                bidirectional_mismatches.append(
                    {
                        "newer_artifact_id": artifact_id,
                        "older_artifact_id": str(older_id),
                    }
                )
        successor_id = row.get("superseded_by")
        if successor_id is not None:
            successor = rows_by_id.get(str(successor_id))
            if successor is None:
                unknown_supersession.append(
                    {
                        "artifact_id": artifact_id,
                        "unknown_artifact_id": str(successor_id),
                    }
                )
            elif artifact_id not in successor.get("supersedes", ()):
                bidirectional_mismatches.append(
                    {
                        "newer_artifact_id": str(successor_id),
                        "older_artifact_id": artifact_id,
                    }
                )
    cycles = _supersession_cycles(rows_by_id)

    prospective_is_audit = False
    if prospective_audit_path is not None:
        try:
            prospective_is_audit = (
                Path(prospective_audit_path).resolve()
                == (repo / safe_final_root / "artifact_lifecycle_audit.json").resolve()
            )
        except OSError:
            prospective_is_audit = False
    audit_relative = f"{safe_final_root}/artifact_lifecycle_audit.json"
    existing_audit_hash = _content_sha256(repo / audit_relative)
    existing_audit_binding = (
        _validate_git_binding(
            repo=repo,
            relative_path=audit_relative,
            declared_commit=head or "",
            declared_content_hash=existing_audit_hash or "",
            head=head,
        )
        if existing_audit_hash is not None
        else {}
    )
    existing_audit_content = _artifact_content(repo / audit_relative)
    existing_audit_is_safe_file = bool(
        existing_audit_binding and all(existing_audit_binding.values())
        and isinstance(existing_audit_content, Mapping)
        and existing_audit_content.get("schema_version")
        == ARTIFACT_LIFECYCLE_AUDIT_SCHEMA
        and existing_audit_content.get("status") == ARTIFACT_LIFECYCLE_PASS
        and existing_audit_content.get("ready") is True
        and existing_audit_content.get("production_readiness_authority") is False
        and existing_audit_content.get("manifest_hash") == manifest_hash
        and existing_audit_content.get("final_root") == safe_final_root
    )
    audit_output_contract_satisfied = bool(
        prospective_is_audit or existing_audit_is_safe_file
    )

    required_files, required_directories = _required_paths(safe_final_root)
    missing_files: list[str] = []
    for relative in required_files:
        if (
            relative == audit_relative
            and prospective_is_audit
        ):
            continue
        if _path_has_symlink(repo, relative) or not (repo / relative).is_file():
            missing_files.append(relative)
    missing_directories = [
        relative
        for relative in required_directories
        if _path_has_symlink(repo, relative) or not (repo / relative).is_dir()
    ]
    live_root = repo / safe_final_root / "current_live_canaries"
    missing_live_prefixes: list[str] = []
    for prefix in CURRENT_LIVE_CANARY_PREFIXES:
        matches = (
            [
                path
                for path in live_root.iterdir()
                if path.name.startswith(prefix)
                and path.is_dir()
                and not path.is_symlink()
            ]
            if live_root.is_dir() and not live_root.is_symlink()
            else []
        )
        if not matches:
            missing_live_prefixes.append(prefix)

    final_root_path = repo / safe_final_root
    symlink_entries: list[str] = []
    actual_final_files: set[str] = set()
    if final_root_path.is_dir() and not final_root_path.is_symlink():
        for path in final_root_path.rglob("*"):
            relative = path.relative_to(repo).as_posix()
            if path.is_symlink():
                symlink_entries.append(relative)
            elif path.is_file():
                actual_final_files.add(relative)
    declared_paths = {
        str(row.get("artifact_path") or "") for row in validated_rows
    }
    required_undeclared = sorted(
        relative
        for relative in required_files
        if relative
        not in {
            audit_relative,
            f"{safe_final_root}/{CANONICAL_MANIFEST_NAME}",
        }
        and relative not in declared_paths
    )
    unaccounted_final_files = sorted(
        relative
        for relative in actual_final_files
        if relative
        not in {
            audit_relative,
            f"{safe_final_root}/{CANONICAL_MANIFEST_NAME}",
            *(
                f"{safe_final_root}/{name}"
                for name in TERMINAL_PUBLICATION_FILES
            ),
        }
        and relative not in declared_paths
    )

    required_current_paths = _required_current_authority_paths(safe_final_root)
    current_path_role_failures = sorted(
        relative
        for relative in required_current_paths
        if not any(
            row.get("artifact_path") == relative
            and row.get("artifact_role") == CURRENT_AUTHORITY
            and row.get("production_readiness_authority") is True
            for row in validated_rows
        )
    )

    projection_valid = (
        set(projection) == STATUS_PROJECTION_KEYS
        and all(
            projection.get(key) == value
            for key, value in FINAL_STATUS_PROJECTION.items()
        )
    )
    current_contents = {
        artifact_id: material
        for artifact_id, material in contents_by_id.items()
        if material[0].get("artifact_role") == CURRENT_AUTHORITY
    }
    current_contents_by_path = {
        str(row.get("artifact_path") or ""): content
        for row, content in current_contents.values()
    }
    semantic_artifact_failures = _semantic_final_artifact_failures(
        repo=repo,
        final_root=safe_final_root,
        current_contents_by_path=current_contents_by_path,
    )
    observations: dict[str, list[tuple[str, Any]]] = defaultdict(list)
    markdown_pending_artifacts: set[str] = set()
    stale_masquerades: set[str] = set()
    for artifact_id, (row, content) in contents_by_id.items():
        if row.get("artifact_role") == CURRENT_AUTHORITY:
            for key, values in _status_observations(content).items():
                observations[key].extend((artifact_id, value) for value in values)
            if isinstance(content, str) and PRE_GOLD_PENDING_STATUS in content:
                markdown_pending_artifacts.add(artifact_id)
        top = _top_level_mapping(content)
        role = row.get("artifact_role")
        declared_authority = row.get("production_readiness_authority")
        stale = bool(
            (role != CURRENT_AUTHORITY and declared_authority is True)
            or (role == CURRENT_AUTHORITY and declared_authority is not True)
            or (role == CURRENT_AUTHORITY and row.get("superseded_by") is not None)
        )
        if top is not None:
            content_role = top.get("artifact_role")
            content_successor = top.get("superseded_by")
            snapshot_status = str(top.get("snapshot_status") or "")
            stale = stale or bool(
                role == CURRENT_AUTHORITY
                and (
                    snapshot_status.startswith("SUPERSEDED")
                    or content_role in {HISTORICAL_SNAPSHOT, SUPERSEDED}
                    or content_successor not in (None, "")
                )
            )
            stale = stale or bool(
                role != CURRENT_AUTHORITY
                and (
                    content_role == CURRENT_AUTHORITY
                    or top.get("production_readiness_authority") is True
                )
            )
        if stale:
            stale_masquerades.add(artifact_id)

    contradiction_details: list[Mapping[str, Any]] = []
    for scope, ids in duplicate_current_scopes.items():
        contradiction_details.append(
            {"kind": "DUPLICATE_CURRENT_AUTHORITY_SCOPE", "scope": scope, "artifact_ids": ids}
        )
    for key, rows in sorted(observations.items()):
        expected = projection.get(key)
        for artifact_id, value in rows:
            if value != expected:
                contradiction_details.append(
                    {
                        "kind": "CURRENT_STATUS_DISAGREES_WITH_PROJECTION",
                        "artifact_id": artifact_id,
                        "field": key,
                        "observed": value,
                        "expected": expected,
                    }
                )

    gold_pass = projection.get("gold_evaluation_status") == "PASS" or any(
        key == "gold_evaluation_status" and value == "PASS"
        for key, rows in observations.items()
        for _artifact_id, value in rows
    )
    pending_details: list[Mapping[str, Any]] = []
    if gold_pass:
        for key in (
            "production_research_status",
            "score_status",
            "stagecourt_status",
        ):
            value = projection.get(key)
            if isinstance(value, str) and (
                _PENDING.search(value) or value == PRE_GOLD_PENDING_STATUS
            ):
                pending_details.append(
                    {"source": "STATUS_PROJECTION", "field": key, "value": value}
                )
        for key, rows in observations.items():
            for artifact_id, value in rows:
                if isinstance(value, str) and (
                    _PENDING.search(value) or value == PRE_GOLD_PENDING_STATUS
                ):
                    pending_details.append(
                        {
                            "source": artifact_id,
                            "field": key,
                            "value": value,
                        }
                    )
        pending_details.extend(
            {
                "source": artifact_id,
                "field": "MARKDOWN_COMPLETION_STATUS",
                "value": PRE_GOLD_PENDING_STATUS,
            }
            for artifact_id in sorted(markdown_pending_artifacts)
        )
    pending_details = [
        dict(row)
        for row in {
            (row["source"], row["field"], str(row["value"])): row
            for row in pending_details
        }.values()
    ]

    score_stage_failures = _score_stage_mismatches(current_contents, projection)
    current_receipt_targets = {
        str(content.get("target_id") or "")
        for _row, content in current_contents.values()
        if isinstance(content, Mapping)
        and content.get("schema_version")
        in {"e2r_v6_score_receipt_v1", "e2r_v6_stagecourt_receipt_v1"}
    }
    for target_id in CANARY_TARGET_IDS:
        if target_id not in current_receipt_targets:
            score_stage_failures = (
                *score_stage_failures,
                {
                    "target_id": target_id,
                    "reasons": ["CURRENT_SCORE_STAGE_RECEIPT_PAIR_MISSING"],
                    "score_artifact_ids": [],
                    "stagecourt_artifact_ids": [],
                },
            )

    hard_acceptance_counts = {
        "current_authority_contradiction_count": len(contradiction_details),
        "stale_snapshot_masquerading_current_count": len(stale_masquerades),
        "pending_status_after_gold_pass_count": len(pending_details),
        "score_stage_receipt_mismatch_count": len(score_stage_failures),
    }
    critical_counts = {
        **hard_acceptance_counts,
        "manifest_schema_or_shape_error_count": int(not top_level_valid),
        "repository_head_unverified_count": int(head is None),
        "repository_identity_untrusted_count": int(not repository_identity_trusted),
        "canonical_lifecycle_manifest_unbound_count": int(
            not canonical_manifest_binding.get("valid")
        ),
        "final_root_argument_invalid_count": int(not final_root_argument_valid),
        "invalid_artifact_row_count": len(invalid_rows),
        "duplicate_artifact_id_count": len(duplicate_ids),
        "duplicate_artifact_path_count": len(duplicate_paths),
        "unknown_supersession_reference_count": len(unknown_supersession),
        "supersession_bidirectional_mismatch_count": len(
            bidirectional_mismatches
        ),
        "supersession_cycle_count": len(cycles),
        "status_projection_invalid_count": int(not projection_valid),
        "missing_required_final_file_count": len(missing_files),
        "missing_required_final_directory_count": len(missing_directories),
        "missing_current_live_canary_prefix_count": len(missing_live_prefixes),
        "required_final_file_undeclared_count": len(required_undeclared),
        "unaccounted_final_file_count": len(unaccounted_final_files),
        "final_tree_symlink_count": len(symlink_entries),
        "required_current_authority_missing_or_wrong_role_count": len(
            current_path_role_failures
        ),
        "semantic_final_artifact_contract_failure_count": len(
            semantic_artifact_failures
        ),
    }
    criteria = {
        "manifest_schema_and_shape_valid": top_level_valid,
        "repository_head_verified": head is not None,
        "repository_identity_trusted": repository_identity_trusted,
        "canonical_lifecycle_manifest_is_tracked_and_exact": bool(
            canonical_manifest_binding.get("valid")
        ),
        "final_root_argument_valid": final_root_argument_valid,
        "all_artifact_rows_valid": not invalid_rows,
        "artifact_ids_unique": not duplicate_ids,
        "artifact_paths_unique": not duplicate_paths,
        "current_authority_scope_unique": not duplicate_current_scopes,
        "supersession_references_known": not unknown_supersession,
        "supersession_bidirectional": not bidirectional_mismatches,
        "supersession_acyclic": not cycles,
        "status_projection_is_final": projection_valid,
        "hard_acceptance_counts_zero": not any(hard_acceptance_counts.values()),
        "required_final_files_present": not missing_files,
        "required_final_directories_present": not missing_directories,
        "all_required_live_canary_archetypes_present": not missing_live_prefixes,
        "required_final_files_declared": not required_undeclared,
        "every_final_file_lifecycle_accounted": not unaccounted_final_files,
        "final_tree_contains_no_symlinks": not symlink_entries,
        "required_final_authorities_are_current": not current_path_role_failures,
        "semantic_final_artifact_contracts_pass": not semantic_artifact_failures,
        "lifecycle_audit_output_contract_satisfied": (
            audit_output_contract_satisfied
        ),
    }
    passed = all(criteria.values()) and not any(critical_counts.values())
    role_counts = Counter(
        str(row.get("artifact_role") or "") for row in validated_rows
    )
    return {
        "schema_version": ARTIFACT_LIFECYCLE_AUDIT_SCHEMA,
        "status": ARTIFACT_LIFECYCLE_PASS if passed else ARTIFACT_LIFECYCLE_FAIL,
        "ready": passed,
        "production_readiness_authority": False,
        "repo_head_commit_sha": head,
        "final_root": safe_final_root,
        "manifest_hash": manifest_hash,
        "canonical_lifecycle_manifest_binding": canonical_manifest_binding,
        "artifact_count": len(validated_rows),
        "artifact_role_counts": dict(sorted(role_counts.items())),
        "status_projection": projection,
        "hard_acceptance_counts": hard_acceptance_counts,
        "critical_counts": critical_counts,
        "critical_count_sum": sum(critical_counts.values()),
        "criteria": criteria,
        "missing_required_final_files": sorted(missing_files),
        "missing_required_final_directories": sorted(missing_directories),
        "missing_current_live_canary_prefixes": sorted(missing_live_prefixes),
        "required_final_files_without_lifecycle": required_undeclared,
        "unaccounted_final_files": unaccounted_final_files,
        "final_tree_symlinks": sorted(symlink_entries),
        "required_current_authority_failures": current_path_role_failures,
        "semantic_final_artifact_failures": list(semantic_artifact_failures),
        "duplicate_artifact_ids": duplicate_ids,
        "duplicate_artifact_paths": duplicate_paths,
        "duplicate_current_authority_scopes": duplicate_current_scopes,
        "unknown_supersession_references": unknown_supersession,
        "supersession_bidirectional_mismatches": bidirectional_mismatches,
        "supersession_cycles": [list(row) for row in cycles],
        "current_authority_contradictions": contradiction_details,
        "stale_snapshot_masquerades": sorted(stale_masquerades),
        "pending_status_after_gold_pass": pending_details,
        "score_stage_receipt_mismatches": list(score_stage_failures),
        "invalid_artifact_rows": invalid_rows,
        "artifact_validations": artifact_audits,
        "authority_not_synthesized": True,
        "score_or_stage_authority": False,
    }


__all__ = [
    "ARTIFACT_LIFECYCLE_AUDIT_SCHEMA",
    "ARTIFACT_LIFECYCLE_FAIL",
    "ARTIFACT_LIFECYCLE_MANIFEST_SCHEMA",
    "ARTIFACT_LIFECYCLE_PASS",
    "ARTIFACT_ROLES",
    "CANARY_RECEIPT_DATE",
    "CANARY_TARGET_IDS",
    "CANONICAL_MANIFEST_NAME",
    "CLEAN_CLONE_REPRODUCTION_PASS",
    "CLEAN_CLONE_REPRODUCTION_SCHEMA",
    "CLEAN_CLONE_TEST_PASS",
    "CLEAN_CLONE_TEST_SCHEMA",
    "CROSS_ARCHETYPE_CANARY_SUMMARY_PASS",
    "CROSS_ARCHETYPE_CANARY_SUMMARY_SCHEMA",
    "CURRENT_AUTHORITY",
    "CURRENT_LIVE_CANARY_PREFIXES",
    "FINAL_ROOT_RELATIVE",
    "FINAL_STATUS_PROJECTION",
    "HISTORICAL_SNAPSHOT",
    "PRE_GOLD_PENDING_STATUS",
    "PROVIDER_RUNTIME_AUDIT_PASS",
    "PROVIDER_RUNTIME_AUDIT_SCHEMA",
    "SUPERSEDED",
    "TERMINAL_PUBLICATION_FILES",
    "compile_artifact_lifecycle",
    "load_artifact_lifecycle_manifest",
]
