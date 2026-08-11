"""Phase109 result-last operational cutover publication.

The two terminal leaves are deliberately *outputs* of Reviewer A--V.  They are
never fed back into Phase104 or Reviewer K--V, which avoids a self-hash cycle.
``verified_cutover_head`` means the clean, origin/main-matching HEAD that was
verified immediately before these two leaves were written; it does not claim
to be a future commit containing the leaves themselves.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Mapping, Sequence
import hashlib
import json
import math
import os
from pathlib import Path
import re
import secrets
import stat
import subprocess
from typing import Any

from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_results import (
    CANARY_COMPILATION_PASS,
    compile_cross_archetype_canary_directory,
)
from e2r.production.v6_canary_selection import (
    FORCED_SELECTION,
    ISSUER_PROFILE_MANIFEST_NAME,
    REQUIRED_ARCHETYPES,
    load_current_issuer_business_profile_manifest,
    load_sealed_cross_archetype_canary_selection,
)
from e2r.production.v6_current_krx_census import (
    CANONICAL_TRIGGER_LANES,
    CURRENT_KRX_CENSUS_PASS,
    CURRENT_KRX_CENSUS_SCHEMA,
    CURRENT_KRX_STAGE_ROW_SCHEMA,
)
from e2r.production.v6_operational_acceptance import (
    LEGACY_GATE_RELATIVE,
    OPERATIONAL_ACCEPTANCE_PASS,
    OPERATIONAL_ACCEPTANCE_SCHEMA,
    OPERATIONAL_REVIEWER_GATE_SCHEMA,
    REVIEWER_GATE_PASS,
    REVIEWER_IDS,
    V5_FULL_TEST_COUNT_BASELINE,
    compile_operational_acceptance,
)
from e2r.production.v6_provider_runtime_audit import (
    compile_provider_runtime_audit_from_cutover,
)
from e2r.research_brain.researcher_mode.artifact_lifecycle import (
    CLEAN_CLONE_REPRODUCTION_PASS,
    CLEAN_CLONE_REPRODUCTION_SCHEMA,
    FINAL_ROOT_RELATIVE,
    PROVIDER_RUNTIME_AUDIT_PASS,
    TERMINAL_PUBLICATION_FILES,
)
from e2r.research_brain.researcher_mode.independent_acceptance import (
    FINAL_READY_LABEL,
    REVIEWER_GATE_PASS as LEGACY_REVIEWER_GATE_PASS,
    SCHEMA_VERSION as LEGACY_REVIEWER_GATE_SCHEMA,
    compile_phase100_acceptance_bundle,
)
from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER
from e2r.research_brain.researcher_mode.tracked_readiness import (
    TRACKED_READINESS_PASS,
    TRACKED_READINESS_SCHEMA,
    _repository_identity_is_trusted,
    canonical_repository_root,
)
from e2r.research_brain.researcher_mode.tracked_receipts import (
    PHASE101_TARGET_IDS,
    PROVIDER_ROUTE,
    VERIFICATION_PASS,
    VERIFICATION_SCHEMA,
    verify_receipts,
)


PHASE109_PUBLICATION_SCHEMA = "e2r_v6_operational_cutover_publication_v1"
PHASE109_PUBLICATION_PASS = "E2R_V6_OPERATIONAL_CUTOVER_PUBLICATION_PASS"
PHASE109_PUBLICATION_TEST_PASS = (
    "E2R_V6_OPERATIONAL_CUTOVER_PUBLICATION_CONTRACT_TEST_PASS"
)
PHASE109_REVIEWER_GATE_SCHEMA = (
    "e2r_v6_operational_acceptance_reviewer_gate_a_v_v1"
)
PHASE109_REVIEWER_GATE_PASS = "E2R_V6_OPERATIONAL_REVIEWER_A_V_PASS"
FINAL_CUTOVER_VERDICT = "MEANINGFUL_E2R_OPERATIONAL_MARKET_CUTOVER_READY"
PHASE109_VERIFICATION_SCHEMA = (
    "e2r_v6_operational_cutover_publication_verification_v1"
)
PHASE109_VERIFICATION_PASS = (
    "E2R_V6_OPERATIONAL_CUTOVER_PUBLICATION_VERIFICATION_PASS"
)
PHASE109_VERIFICATION_FAIL = (
    "E2R_V6_OPERATIONAL_CUTOVER_PUBLICATION_VERIFICATION_FAIL"
)

GATE_NAME, REPORT_NAME = TERMINAL_PUBLICATION_FILES
REPORT_FIELD_ORDER = (
    "exact_final_verdict",
    "verified_cutover_head",
    "engine_readiness",
    "tracked_receipt_readiness",
    "clean_clone_readiness",
    "samsung_result",
    "hynix_result",
    "c08_result",
    "c15_result",
    "c17_result",
    "c24_result",
    "c28_result",
    "current_krx_universe_counts",
    "trigger_lane_counts",
    "depth_counts_l0_l5",
    "natural_candidate_count",
    "score_valid_final_stage_counts",
    "provider_routes_and_local_call_counts",
    "full_test_count",
    "reviewer_a_v",
    "blockers",
)

_REPORT_LABELS = (
    "최종 판정",
    "final HEAD (publication 직전 검증 기준)",
    "엔진 준비 상태",
    "tracked receipt 준비 상태",
    "clean clone 준비 상태",
    "삼성전자 7-component 결과",
    "SK하이닉스 7-component 결과",
    "C08 current canary 결과",
    "C15 current canary 결과",
    "C17 current canary 결과",
    "C24 current canary 결과",
    "C28 current canary 결과",
    "현재 KRX universe 수",
    "trigger lane 수",
    "L0~L5 depth 수",
    "자연 candidate 수",
    "score_valid 및 FINAL Stage row 수",
    "provider route 및 local 호출 수",
    "전체 test 수",
    "Reviewer A~V",
    "남은 blocker",
)

_PUBLICATION_KEYS = frozenset(
    {
        "schema_version",
        "status",
        "publication_id",
        "verified_cutover_head",
        "verified_cutover_head_semantics",
        "report_field_order",
        "report_fields",
        "report_fields_hash",
        "reviewer_gate",
        "acceptance_hash",
        "phase_evidence_index",
        "phase_evidence_tree_hash",
        "markdown_sha256",
        "terminal_files_excluded_from_phase104_and_reviewer_inputs",
        "production_readiness_authority",
        "score_or_stage_authority",
        "publication_hash",
    }
)

_HEAD_SEMANTICS = (
    "clean origin/main-matching HEAD verified immediately before Phase109 "
    "terminal publication; not a claim that this SHA contains the two "
    "terminal files"
)
_SHA40 = re.compile(r"[0-9a-f]{40}\Z")
_SHA64 = re.compile(r"[0-9a-f]{64}\Z")
_CANONICAL_STAGES = frozenset(
    {"0", "1", "2", "3-Green", "3-Yellow", "3-Red", "4A", "4B", "4C", "5"}
)

EvidenceCompiler = Callable[[Path, str | None], Mapping[str, Any]]


def _mapping(value: object, *, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{context} must be an object")
    return value


def _rows(value: object, *, context: str) -> tuple[Mapping[str, Any], ...]:
    if isinstance(value, (str, bytes, bytearray)) or not isinstance(value, Sequence):
        raise ValueError(f"{context} must be an array")
    return tuple(_mapping(row, context=f"{context} row") for row in value)


def _finite(value: object) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def _read_json(path: Path) -> Mapping[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"unsafe or missing JSON leaf: {path.name}")
    value = json.loads(path.read_text(encoding="utf-8"))
    return _mapping(value, context=path.name)


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"unsafe or missing JSONL leaf: {path.name}")
    return tuple(
        _mapping(json.loads(line), context=f"{path.name} row")
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _git_text(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=repo, text=True, stderr=subprocess.DEVNULL
    ).strip()


def _tracked_at_head(repo: Path, path: Path) -> bool:
    try:
        relative = path.absolute().relative_to(repo).as_posix()
        head_blob = _git_text(repo, "rev-parse", f"HEAD:{relative}")
        index = _git_text(repo, "ls-files", "-s", "--", relative).split()
        worktree_blob = _git_text(repo, "hash-object", "--", relative)
    except (OSError, ValueError, subprocess.CalledProcessError):
        return False
    return len(index) >= 2 and head_blob == index[1] == worktree_blob


def _terminal_git_relationship(
    repo: Path, *, verified_cutover_head: str
) -> Mapping[str, Any]:
    """Prove the current HEAD's relation to the pre-publication clean HEAD."""

    allowed = {
        (FINAL_ROOT_RELATIVE / name).as_posix()
        for name in TERMINAL_PUBLICATION_FILES
    }
    current = _git_text(repo, "rev-parse", "HEAD")
    remote_main = _git_text(repo, "rev-parse", "refs/remotes/origin/main")
    raw_status = subprocess.check_output(
        ["git", "status", "--porcelain=v1", "-z", "--untracked-files=all"],
        cwd=repo,
    )
    seen: set[str] = set()
    result_last_status_valid = True
    for encoded in raw_status.split(b"\0"):
        if not encoded:
            continue
        entry = encoded.decode("utf-8")
        if len(entry) < 4:
            result_last_status_valid = False
            continue
        code = entry[:2]
        relative = entry[3:]
        if code not in {"??", " M"} or relative not in allowed or relative in seen:
            result_last_status_valid = False
        seen.add(relative)
    if (
        current == verified_cutover_head
        and remote_main == verified_cutover_head
        and result_last_status_valid
        and seen.issubset(allowed)
    ):
        return {
            "current_repository_head": current,
            "relationship": "RESULT_LAST_TERMINAL_WORKTREE",
            "current_head_matches_verified_cutover_head": True,
            "terminal_commit_verified": False,
        }
    first_parent = _git_text(repo, "rev-parse", "HEAD^")
    raw_commit_paths = subprocess.check_output(
        [
            "git",
            "diff-tree",
            "--no-commit-id",
            "--name-only",
            "-r",
            "-z",
            "HEAD",
        ],
        cwd=repo,
    )
    commit_paths = {
        value.decode("utf-8") for value in raw_commit_paths.split(b"\0") if value
    }
    if not (
        current != verified_cutover_head
        and remote_main == current
        and first_parent == verified_cutover_head
        and raw_status == b""
        and commit_paths == allowed
    ):
        raise ValueError(
            "current Git state is neither the result-last worktree nor its "
            "exact first-parent terminal commit"
        )
    return {
        "current_repository_head": current,
        "relationship": "EXACT_TERMINAL_FIRST_PARENT_COMMIT",
        "current_head_matches_verified_cutover_head": False,
        "terminal_commit_verified": True,
    }


def _phase_evidence_index(repo: Path, final: Path) -> tuple[Mapping[str, Any], ...]:
    if final.is_symlink() or not final.is_dir():
        raise ValueError("canonical cutover root is unsafe or missing")
    terminal_paths = {final / name for name in TERMINAL_PUBLICATION_FILES}
    paths: list[Path] = []
    for path in final.rglob("*"):
        if path.is_symlink():
            raise ValueError("cutover evidence tree contains a symlink")
        if path.is_file() and path not in terminal_paths:
            paths.append(path)
    paths.append(repo / LEGACY_GATE_RELATIVE)
    if len(set(paths)) != len(paths) or any(not _tracked_at_head(repo, path) for path in paths):
        raise ValueError("every nonterminal Phase101-108 evidence leaf must match HEAD")
    return tuple(
        {
            "relative_path": path.relative_to(repo).as_posix(),
            "sha256": _sha256_bytes(path.read_bytes()),
            "size_bytes": path.stat().st_size,
        }
        for path in sorted(paths, key=lambda item: item.relative_to(repo).as_posix())
    )


def _validate_acceptance(acceptance: Mapping[str, Any]) -> Mapping[str, Any]:
    core = {key: value for key, value in acceptance.items() if key != "acceptance_hash"}
    gate = _mapping(acceptance.get("reviewer_gate"), context="Reviewer K-V gate")
    reviewers = _rows(gate.get("reviewers"), context="Reviewer K-V rows")
    phase_presence = _mapping(
        acceptance.get("phase_artifact_presence"), context="phase artifact presence"
    )
    provenance = _mapping(
        acceptance.get("repository_provenance"), context="repository provenance"
    )
    if (
        acceptance.get("schema_version") != OPERATIONAL_ACCEPTANCE_SCHEMA
        or acceptance.get("status") != OPERATIONAL_ACCEPTANCE_PASS
        or acceptance.get("ready") is not True
        or acceptance.get("contract_test_pass") is not False
        or acceptance.get("production_readiness_authority") is not True
        or acceptance.get("test_mode") is not False
        or acceptance.get("critical_count_sum") != 0
        or acceptance.get("blockers") != []
        or acceptance.get("fixed_retry_count_is_completion_authority") is not False
        or acceptance.get("score_or_stage_authority") is not False
        or acceptance.get("investment_recommendation_emitted") is not False
        or set(phase_presence) != {str(value) for value in range(101, 109)}
        or any(
            _mapping(row, context=f"Phase {phase} presence").get("complete")
            is not True
            for phase, row in phase_presence.items()
        )
        or set(provenance)
        != {
            "canonical_repository",
            "origin_main_matches_head",
            "worktree_clean",
            "all_acceptance_artifacts_tracked_at_head",
        }
        or any(value is not True for value in provenance.values())
        or acceptance.get("acceptance_hash") != stable_hash(core)
        or gate.get("schema_version") != OPERATIONAL_REVIEWER_GATE_SCHEMA
        or gate.get("status") != REVIEWER_GATE_PASS
        or tuple(gate.get("reviewer_roster") or ()) != REVIEWER_IDS
        or tuple(str(row.get("reviewer_id") or "") for row in reviewers) != REVIEWER_IDS
        or any(
            row.get("status") != "PASS"
            or row.get("critical_count_sum") != 0
            or row.get("leaf_recomputed") is not True
            for row in reviewers
        )
        or gate.get("failed_reviewers") != []
        or gate.get("critical_count_sum") != 0
        or gate.get("all_reviewers_leaf_recomputed") is not True
        or gate.get("one_critical_forces_failure") is not True
        or gate.get("production_readiness_authority") is not True
    ):
        raise ValueError("Phase108 acceptance and Reviewer K-V are not production PASS")
    return gate


def _validate_legacy_gate(gate: Mapping[str, Any]) -> tuple[Mapping[str, Any], ...]:
    reviewers = _rows(gate.get("reviewers"), context="Reviewer A-J rows")
    if (
        gate.get("schema_version") != LEGACY_REVIEWER_GATE_SCHEMA
        or gate.get("status") != LEGACY_REVIEWER_GATE_PASS
        or tuple(gate.get("reviewer_roster") or ()) != tuple("ABCDEFGHIJ")
        or tuple(str(row.get("reviewer_id") or "") for row in reviewers)
        != tuple("ABCDEFGHIJ")
        or any(
            row.get("status") != "PASS"
            or row.get("critical_count_sum") != 0
            or int(row.get("detector_run_count") or 0) <= 0
            or row.get("detector_pass_count") != row.get("detector_run_count")
            for row in reviewers
        )
        or gate.get("reviewer_count") != len(reviewers)
        or gate.get("failed_reviewers") != []
        or gate.get("critical_count_sum") != 0
        or gate.get("blockers") != []
        or gate.get("all_reviewers_independently_recomputed") is not True
        or gate.get("one_critical_forces_failure") is not True
        or gate.get("production_readiness_authority") is not True
        or gate.get("exact_verdict") != FINAL_READY_LABEL
    ):
        raise ValueError("Reviewer A-J is not an exact current PASS roster")
    return reviewers


def _phase101_result(final: Path, target_id: str) -> Mapping[str, Any]:
    target = final / "canary_receipts" / "2026-07-12" / target_id
    manifest = _read_json(target / "receipt_manifest.json")
    score = _read_json(target / "score_receipt.json")
    vector = _mapping(score.get("component_score_vector"), context="component vector")
    if (
        set(vector) != set(CANONICAL_COMPONENT_ORDER)
        or any(not _finite(vector.get(key)) for key in CANONICAL_COMPONENT_ORDER)
        or not _finite(score.get("total_score_recomputed"))
        or abs(
            sum(float(vector[key]) for key in CANONICAL_COMPONENT_ORDER)
            - float(score["total_score_recomputed"])
        )
        > 1e-9
        or score.get("score_valid") is not True
        or score.get("stage_status") != "FINAL"
        or score.get("canonical_stage") not in _CANONICAL_STAGES
    ):
        raise ValueError(f"Phase101 result is not exact: {target_id}")
    return {
        "target_id": target_id,
        "company_name": manifest.get("company_name"),
        "component_score_vector": dict(vector),
        "total_score": score["total_score_recomputed"],
        "canonical_stage": score["canonical_stage"],
    }


def _load_selection_and_canaries(
    repo: Path, final: Path
) -> tuple[Mapping[str, Any], Mapping[str, Any]]:
    selection_path = final / "cross_archetype_canary_selection.json"
    header = _read_json(selection_path)
    forced = any(
        row.get("selection_mode") == FORCED_SELECTION
        for row in _rows(header.get("selections"), context="selection rows")
    )
    profile: Mapping[str, Any] | None = None
    if forced:
        profile = load_current_issuer_business_profile_manifest(
            final / ISSUER_PROFILE_MANIFEST_NAME,
            selection_as_of_date=str(header.get("selection_as_of_date") or ""),
        )
    selection = load_sealed_cross_archetype_canary_selection(
        selection_path,
        issuer_business_profile_manifest=profile,
    )
    compilation = compile_cross_archetype_canary_directory(
        selection=selection,
        live_root=final / "current_live_canaries",
        issuer_business_profile_manifest=profile,
        repo_root=repo,
    )
    summary = _mapping(compilation.get("summary"), context="canary summary")
    if compilation.get("status") != CANARY_COMPILATION_PASS:
        raise ValueError("Phase106 canary receipt directory does not recompile")
    tracked_summary = _read_json(final / "cross_archetype_canary_summary.json")
    if dict(summary) != dict(tracked_summary):
        raise ValueError("Phase106 tracked summary differs from leaf recomputation")
    return selection, summary


def _canary_results(
    selection: Mapping[str, Any], summary: Mapping[str, Any]
) -> Mapping[str, Mapping[str, Any]]:
    names = {
        str(row.get("target_id") or ""): row.get("company_name")
        for row in _rows(selection.get("selections"), context="selection rows")
    }
    result: dict[str, Mapping[str, Any]] = {}
    for row in _rows(summary.get("canaries"), context="canary summary rows"):
        archetype = str(row.get("archetype_id") or "")
        target_id = str(row.get("target_id") or "")
        if archetype not in REQUIRED_ARCHETYPES or target_id not in names:
            raise ValueError("Phase106 canary identity is absent from selection")
        if (
            row.get("score_valid") is not True
            or row.get("stage_final") is not True
            or row.get("component_count") != 7
            or row.get("judge_decision_count") != 21
            or not _finite(row.get("total_score"))
            or row.get("canonical_stage") not in _CANONICAL_STAGES
        ):
            raise ValueError("Phase106 canary score/Stage roster is incomplete")
        result[archetype] = {
            "target_id": target_id,
            "company_name": names[target_id],
            "total_score": row.get("total_score"),
            "canonical_stage": row.get("canonical_stage"),
        }
    if set(result) != set(REQUIRED_ARCHETYPES):
        raise ValueError("Phase106 exact-five result roster is incomplete")
    return result


def _census_projection(final: Path) -> Mapping[str, Any]:
    summary = _read_json(final / "current_krx_census_summary.json")
    rows = _read_jsonl(final / "current_krx_stage_map_compact.jsonl")
    core = {key: value for key, value in summary.items() if key != "summary_hash"}
    trigger_counts = {
        lane: sum(lane in tuple(row.get("trigger_lane_ids") or ()) for row in rows)
        for lane in CANONICAL_TRIGGER_LANES
    }
    depth_counts = {
        level: sum(row.get("maximum_depth") == level for row in rows)
        for level in ("L0", "L1", "L2", "L3", "L4", "L5")
    }
    score_valid = sum(
        row.get("current_score_status") == "COMPLETE"
        and row.get("stage_status") == "FINAL"
        and _finite(row.get("current_score"))
        and row.get("canonical_stage") in _CANONICAL_STAGES
        for row in rows
    )
    final_count = sum(row.get("stage_status") == "FINAL" for row in rows)
    if (
        summary.get("schema_version") != CURRENT_KRX_CENSUS_SCHEMA
        or summary.get("status") != CURRENT_KRX_CENSUS_PASS
        or summary.get("production_runtime_ready") is not True
        or summary.get("test_mode") is not False
        or summary.get("critical_count_sum") != 0
        or summary.get("summary_hash") != stable_hash(core)
        or summary.get("stage_map_hash") != stable_hash(rows)
        or int(summary.get("eligible_universe_count") or 0) != len(rows)
        or int(summary.get("stage_map_row_count") or 0) != len(rows)
        or any(row.get("schema_version") != CURRENT_KRX_STAGE_ROW_SCHEMA for row in rows)
        or summary.get("trigger_lane_counts") != trigger_counts
        or summary.get("depth_counts") != depth_counts
        or int(summary.get("score_valid_deep_row_count") or 0) != score_valid
        or int(summary.get("final_stage_deep_row_count") or 0) != final_count
        or int(summary.get("natural_candidate_count") or 0) <= 0
    ):
        raise ValueError("Phase107 Census aggregates do not recompute")
    return {
        "universe_counts": {
            "eligible_universe_count": len(rows),
            "stage_map_row_count": len(rows),
            "real_krx_universe_source": True,
        },
        "trigger_lane_counts": trigger_counts,
        "depth_counts": depth_counts,
        "natural_candidate_count": summary["natural_candidate_count"],
        "score_stage_counts": {
            "score_valid_deep_row_count": score_valid,
            "final_stage_deep_row_count": final_count,
            "natural_l5_completed_count": summary.get("natural_l5_completed_count"),
        },
    }


def _provider_projection(
    repo: Path,
    final: Path,
    selection: Mapping[str, Any],
) -> Mapping[str, Any]:
    recomputed = compile_provider_runtime_audit_from_cutover(
        repo_root=repo,
        final_root=FINAL_ROOT_RELATIVE,
    )
    tracked = _read_json(final / "provider_runtime_audit.json")
    if dict(recomputed) != dict(tracked) or tracked.get("status") != PROVIDER_RUNTIME_AUDIT_PASS:
        raise ValueError("provider runtime audit does not recompute")
    roots = [
        final / "canary_receipts" / "2026-07-12" / target_id
        for target_id in PHASE101_TARGET_IDS
    ]
    roots.extend(
        final
        / "current_live_canaries"
        / f"{row['archetype_id']}_{row['target_id']}"
        for row in _rows(selection.get("selections"), context="selection rows")
    )
    routes = Counter(
        str(row.get("provider_route") or "")
        for root in roots
        for row in _read_jsonl(root / "judge_decisions.jsonl")
    )
    expected_judge_count = 21 * (
        len(PHASE101_TARGET_IDS) + len(REQUIRED_ARCHETYPES)
    )
    if (
        set(routes) != {PROVIDER_ROUTE}
        or routes.get(PROVIDER_ROUTE) != expected_judge_count
    ):
        raise ValueError("judge provider routes are not the canonical Codex route")
    return {
        "route_count_scope": "PHASE101_AND_PHASE106_TRACKED_RECEIPTS",
        "expected_judge_receipt_count": expected_judge_count,
        "provider_route_counts": dict(sorted(routes.items())),
        "provider_call_counts": dict(tracked.get("provider_call_counts") or {}),
        "scored_fact_provider_lineage_counts": dict(
            tracked.get("scored_fact_provider_lineage_counts") or {}
        ),
        "provider_error_count": tracked.get("provider_error_count"),
        "unauthorized_provider_call_count": tracked.get(
            "unauthorized_provider_call_count"
        ),
        "local_provider_call_count": tracked.get("local_provider_call_count"),
        "qwen_call_count": tracked.get("qwen_call_count"),
        "ollama_call_count": tracked.get("ollama_call_count"),
        "inherited_qwen_scored_fact_count": tracked.get(
            "inherited_qwen_scored_fact_count"
        ),
        "inherited_ollama_scored_fact_count": tracked.get(
            "inherited_ollama_scored_fact_count"
        ),
    }


def _compile_publication_evidence(
    repo: Path,
    terminal_publication_verified_head: str | None,
) -> Mapping[str, Any]:
    repo = repo.resolve()
    final = repo / FINAL_ROOT_RELATIVE
    if terminal_publication_verified_head is None:
        if repo != canonical_repository_root() or not _repository_identity_is_trusted(repo):
            raise ValueError("Phase109 publisher requires the clean trusted canonical HEAD")
        verified_head = _git_text(repo, "rev-parse", "HEAD")
    else:
        verified_head = terminal_publication_verified_head
    acceptance = compile_operational_acceptance(
        repo_root=repo,
        final_root=FINAL_ROOT_RELATIVE,
        terminal_publication_verified_head=terminal_publication_verified_head,
    )
    gate = _validate_acceptance(acceptance)
    legacy_bundle = compile_phase100_acceptance_bundle(repo)
    legacy_gate = _mapping(
        legacy_bundle.get("reviewer_gate"), context="Reviewer A-J gate"
    )
    legacy_reviewers = _validate_legacy_gate(legacy_gate)
    phase101 = verify_receipts(final / "canary_receipts" / "2026-07-12")
    if phase101.get("status") != VERIFICATION_PASS or phase101.get("critical_count_sum") != 0:
        raise ValueError("Phase101 tracked receipts do not independently verify")
    selection, canary_summary = _load_selection_and_canaries(repo, final)
    provider = _provider_projection(repo, final, selection)
    census = _census_projection(final)
    readiness = _read_json(final / "clean_clone/tracked_readiness_result.json")
    clean_clone = _read_json(final / "clean_clone_reproduction.json")
    if (
        readiness.get("schema_version") != TRACKED_READINESS_SCHEMA
        or readiness.get("status") != TRACKED_READINESS_PASS
        or readiness.get("ready") is not True
        or readiness.get("offline") is not True
        or readiness.get("production_readiness_authority") is not False
        or int(readiness.get("critical_count") or 0) != 0
        or clean_clone.get("schema_version") != CLEAN_CLONE_REPRODUCTION_SCHEMA
        or clean_clone.get("status") != CLEAN_CLONE_REPRODUCTION_PASS
        or int(clean_clone.get("critical_count_sum") or 0) != 0
    ):
        raise ValueError("clean-clone or tracked readiness is not PASS")
    index = _phase_evidence_index(repo, final)
    if terminal_publication_verified_head is None:
        if (
            not _repository_identity_is_trusted(repo)
            or _git_text(repo, "rev-parse", "HEAD") != verified_head
        ):
            raise ValueError("repository changed during Phase109 pre-publication checks")
    return {
        "test_mode": False,
        "verified_cutover_head": verified_head,
        "acceptance": acceptance,
        "reviewer_gate": gate,
        "legacy_gate": legacy_gate,
        "legacy_reviewers": legacy_reviewers,
        "phase101_verification": phase101,
        "samsung_result": _phase101_result(final, "005930"),
        "hynix_result": _phase101_result(final, "000660"),
        "canary_results": _canary_results(selection, canary_summary),
        "census": census,
        "provider": provider,
        "tracked_readiness": readiness,
        "clean_clone": clean_clone,
        "phase_evidence_index": index,
    }


def _validated_target_result(
    value: object,
    *,
    context: str,
    expected_target_id: str | None = None,
    component_vector_required: bool,
) -> Mapping[str, Any]:
    result = _mapping(value, context=context)
    target_id = str(result.get("target_id") or "")
    company_name = str(result.get("company_name") or "").strip()
    total_score = result.get("total_score")
    stage = result.get("canonical_stage")
    expected_keys = {
        "target_id",
        "company_name",
        "total_score",
        "canonical_stage",
    }
    if component_vector_required:
        expected_keys.add("component_score_vector")
    if (
        set(result) != expected_keys
        or not target_id
        or (expected_target_id is not None and target_id != expected_target_id)
        or not company_name
        or not _finite(total_score)
        or not 0.0 <= float(total_score) <= 100.0
        or stage not in _CANONICAL_STAGES
    ):
        raise ValueError(f"{context} identity/score/Stage is invalid")
    if component_vector_required:
        vector = _mapping(
            result.get("component_score_vector"), context=f"{context} component vector"
        )
        if (
            set(vector) != set(CANONICAL_COMPONENT_ORDER)
            or any(not _finite(vector.get(key)) for key in CANONICAL_COMPONENT_ORDER)
            or abs(
                sum(float(vector[key]) for key in CANONICAL_COMPONENT_ORDER)
                - float(total_score)
            )
            > 1e-9
        ):
            raise ValueError(f"{context} seven-component vector is invalid")
        return {
            **result,
            "component_score_vector": {
                key: vector[key] for key in CANONICAL_COMPONENT_ORDER
            },
        }
    elif "component_score_vector" in result:
        raise ValueError(f"{context} must not imply an unreported component vector")
    return result


def _validated_phase_evidence_index(value: object) -> tuple[Mapping[str, Any], ...]:
    rows = tuple(dict(row) for row in _rows(value, context="phase evidence index"))
    paths: list[str] = []
    for row in rows:
        path = str(row.get("relative_path") or "")
        digest = str(row.get("sha256") or "")
        size = row.get("size_bytes")
        path_parts = Path(path).parts
        if (
            set(row) != {"relative_path", "sha256", "size_bytes"}
            or not path
            or Path(path).is_absolute()
            or any(part in {"", ".", ".."} for part in path_parts)
            or _SHA64.fullmatch(digest) is None
            or isinstance(size, bool)
            or not isinstance(size, int)
            or size < 0
        ):
            raise ValueError("phase evidence index contains an invalid raw-file row")
        paths.append(path)
    if not rows or paths != sorted(paths) or len(paths) != len(set(paths)):
        raise ValueError("phase evidence index must be a nonempty unique sorted roster")
    terminal_relatives = {
        (FINAL_ROOT_RELATIVE / name).as_posix()
        for name in TERMINAL_PUBLICATION_FILES
    }
    if terminal_relatives.intersection(paths):
        raise ValueError("terminal publications cannot enter their own evidence index")
    return rows


def _reviewer_projection(evidence: Mapping[str, Any]) -> Mapping[str, Any]:
    legacy = _rows(
        _mapping(evidence.get("legacy_gate"), context="legacy gate").get("reviewers"),
        context="Reviewer A-J rows",
    )
    current = _rows(
        _mapping(evidence.get("reviewer_gate"), context="current gate").get("reviewers"),
        context="Reviewer K-V rows",
    )
    reviewers = (*legacy, *current)
    expected = tuple(chr(code) for code in range(ord("A"), ord("V") + 1))
    if tuple(str(row.get("reviewer_id") or "") for row in reviewers) != expected:
        raise ValueError("Reviewer A-V roster is not exact")
    if any(row.get("status") != "PASS" or int(row.get("critical_count_sum") or 0) != 0 for row in reviewers):
        raise ValueError("Reviewer A-V contains a failure")
    return {
        str(row["reviewer_id"]): {
            "status": row["status"],
            "critical_count_sum": row["critical_count_sum"],
        }
        for row in reviewers
    }


def _combined_reviewer_gate(evidence: Mapping[str, Any]) -> Mapping[str, Any]:
    acceptance = _mapping(evidence.get("acceptance"), context="acceptance")
    legacy_gate = _mapping(evidence.get("legacy_gate"), context="legacy gate")
    current_gate = _mapping(evidence.get("reviewer_gate"), context="current gate")
    legacy = _validate_legacy_gate(legacy_gate)
    validated_current_gate = _validate_acceptance(acceptance)
    if dict(current_gate) != dict(validated_current_gate):
        raise ValueError("Phase109 current reviewer gate diverges from acceptance")
    current = _rows(current_gate.get("reviewers"), context="Reviewer K-V rows")
    rows = tuple(
        {
            "reviewer_id": str(row["reviewer_id"]),
            "status": "PASS",
            "critical_count_sum": 0,
            "leaf_recomputed": True,
            "source_gate_schema": (
                LEGACY_REVIEWER_GATE_SCHEMA
                if index < len(legacy)
                else OPERATIONAL_REVIEWER_GATE_SCHEMA
            ),
        }
        for index, row in enumerate((*legacy, *current))
    )
    roster = tuple(chr(value) for value in range(ord("A"), ord("V") + 1))
    if tuple(row["reviewer_id"] for row in rows) != roster:
        raise ValueError("combined Reviewer A-V roster is not exact")
    body = {
        "schema_version": PHASE109_REVIEWER_GATE_SCHEMA,
        "status": PHASE109_REVIEWER_GATE_PASS,
        "reviewer_count": len(rows),
        "reviewer_roster": list(roster),
        "reviewers": list(rows),
        "failed_reviewers": [],
        "critical_count_sum": 0,
        "all_reviewers_leaf_recomputed": True,
        "one_critical_forces_failure": True,
        "phase100_gate_hash": stable_hash(legacy_gate),
        "phase108_gate_hash": stable_hash(current_gate),
        "acceptance_hash": acceptance.get("acceptance_hash"),
        "production_readiness_authority": evidence.get("test_mode") is not True,
        "score_or_stage_authority": False,
    }
    return {**body, "gate_hash": stable_hash(body)}


def _report_fields(evidence: Mapping[str, Any]) -> Mapping[str, Any]:
    acceptance = _mapping(evidence.get("acceptance"), context="acceptance")
    _validate_acceptance(acceptance)
    _validate_legacy_gate(
        _mapping(evidence.get("legacy_gate"), context="legacy gate")
    )
    head = str(evidence.get("verified_cutover_head") or "")
    if _SHA40.fullmatch(head) is None:
        raise ValueError("verified_cutover_head is not a Git SHA")
    if OPERATIONAL_ACCEPTANCE_PASS != FINAL_CUTOVER_VERDICT:
        raise RuntimeError("operational acceptance and final verdict labels diverged")
    canaries = _mapping(evidence.get("canary_results"), context="canary results")
    if set(canaries) != set(REQUIRED_ARCHETYPES):
        raise ValueError("exact-five canary report roster is incomplete")
    samsung = _validated_target_result(
        evidence.get("samsung_result"),
        context="Samsung result",
        expected_target_id="005930",
        component_vector_required=True,
    )
    hynix = _validated_target_result(
        evidence.get("hynix_result"),
        context="Hynix result",
        expected_target_id="000660",
        component_vector_required=True,
    )
    canary_rows = {
        archetype: _validated_target_result(
            canaries[archetype],
            context=archetype,
            component_vector_required=False,
        )
        for archetype in REQUIRED_ARCHETYPES
    }
    canary_target_ids = tuple(str(row["target_id"]) for row in canary_rows.values())
    if len(set(canary_target_ids)) != len(REQUIRED_ARCHETYPES):
        raise ValueError("exact-five canary targets must be distinct")
    census = _mapping(evidence.get("census"), context="Census projection")
    readiness = _mapping(
        evidence.get("tracked_readiness"), context="tracked readiness"
    )
    clean_clone = _mapping(evidence.get("clean_clone"), context="clean clone")
    tests = _mapping(acceptance.get("full_test_result"), context="full tests")
    executed = tests.get("executed_test_count")
    reviewer_v = next(
        row
        for row in _rows(
            _mapping(acceptance.get("reviewer_gate"), context="Reviewer K-V gate").get(
                "reviewers"
            ),
            context="Reviewer K-V rows",
        )
        if row.get("reviewer_id") == "V"
    )
    reviewer_v_metrics = _mapping(
        reviewer_v.get("metrics"), context="Reviewer V metrics"
    )
    full_test_baseline = reviewer_v_metrics.get("full_test_count_baseline")
    test_result_core = {
        key: tests.get(key)
        for key in (
            "status",
            "executed_test_count",
            "failed_test_count",
            "error_test_count",
            "exit_code",
            "output_hash_scope",
        )
    }
    if (
        set(tests) != set(test_result_core) | {"output_hash"}
        or tests.get("status") != "PASS"
        or isinstance(executed, bool)
        or not isinstance(executed, int)
        or isinstance(full_test_baseline, bool)
        or not isinstance(full_test_baseline, int)
        or full_test_baseline < V5_FULL_TEST_COUNT_BASELINE
        or executed < full_test_baseline
        or reviewer_v_metrics.get("current_test_count") != executed
        or reviewer_v_metrics.get("full_test_count_delta")
        != executed - full_test_baseline
        or tests.get("failed_test_count") != 0
        or tests.get("error_test_count") != 0
        or tests.get("output_hash_scope")
        != "DETERMINISTIC_TEST_RESULT_FIELDS"
        or tests.get("output_hash") != stable_hash(test_result_core)
    ):
        raise ValueError("full tests do not satisfy the Phase109 baseline")
    phase101 = _mapping(
        evidence.get("phase101_verification"), context="Phase101 verification"
    )
    if (
        phase101.get("schema_version") != VERIFICATION_SCHEMA
        or phase101.get("status") != VERIFICATION_PASS
        or phase101.get("critical_count_sum") != 0
        or tuple(phase101.get("target_ids") or ()) != PHASE101_TARGET_IDS
        or phase101.get("offline") is not True
        or readiness.get("schema_version") != TRACKED_READINESS_SCHEMA
        or readiness.get("status") != TRACKED_READINESS_PASS
        or readiness.get("ready") is not True
        or readiness.get("offline") is not True
        or readiness.get("production_readiness_authority") is not False
        or readiness.get("critical_count") != 0
        or readiness.get("same_receipt_replay_variance") != 0
        or tuple(readiness.get("target_ids") or ())
        != tuple(sorted(PHASE101_TARGET_IDS))
        or clean_clone.get("schema_version") != CLEAN_CLONE_REPRODUCTION_SCHEMA
        or clean_clone.get("status") != CLEAN_CLONE_REPRODUCTION_PASS
        or clean_clone.get("critical_count_sum") != 0
        or clean_clone.get("production_readiness_authority") is not False
        or any(
            _SHA64.fullmatch(str(clean_clone.get(key) or "")) is None
            for key in (
                "receipt_recompute_result_hash",
                "tracked_readiness_result_hash",
                "test_result_hash",
            )
        )
    ):
        raise ValueError("receipt/clean-clone readiness is not exact PASS")
    universe_counts = _mapping(
        census.get("universe_counts"), context="universe counts"
    )
    trigger_counts = _mapping(
        census.get("trigger_lane_counts"), context="trigger counts"
    )
    depth_counts = _mapping(census.get("depth_counts"), context="depth counts")
    score_stage_counts = _mapping(
        census.get("score_stage_counts"), context="score/Stage counts"
    )
    natural_count = census.get("natural_candidate_count")
    if (
        universe_counts.get("real_krx_universe_source") is not True
        or universe_counts.get("eligible_universe_count")
        != universe_counts.get("stage_map_row_count")
        or not isinstance(universe_counts.get("eligible_universe_count"), int)
        or isinstance(universe_counts.get("eligible_universe_count"), bool)
        or int(universe_counts["eligible_universe_count"]) <= 0
        or set(trigger_counts) != set(CANONICAL_TRIGGER_LANES)
        or any(
            isinstance(value, bool) or not isinstance(value, int) or value < 0
            for value in trigger_counts.values()
        )
        or any(
            int(value) > int(universe_counts["eligible_universe_count"])
            for value in trigger_counts.values()
        )
        or set(depth_counts) != {f"L{value}" for value in range(6)}
        or any(
            isinstance(value, bool) or not isinstance(value, int) or value < 0
            for value in depth_counts.values()
        )
        or sum(int(value) for value in depth_counts.values())
        != int(universe_counts["eligible_universe_count"])
        or isinstance(natural_count, bool)
        or not isinstance(natural_count, int)
        or natural_count <= 0
        or natural_count > int(universe_counts["eligible_universe_count"])
        or any(
            isinstance(score_stage_counts.get(key), bool)
            or not isinstance(score_stage_counts.get(key), int)
            or int(score_stage_counts[key]) <= 0
            for key in (
                "score_valid_deep_row_count",
                "final_stage_deep_row_count",
                "natural_l5_completed_count",
            )
        )
        or any(
            int(score_stage_counts[key])
            > int(universe_counts["eligible_universe_count"])
            for key in (
                "score_valid_deep_row_count",
                "final_stage_deep_row_count",
            )
        )
        or int(score_stage_counts["natural_l5_completed_count"])
        > int(natural_count)
    ):
        raise ValueError("current KRX Census report fields are invalid")
    fields = {
        "exact_final_verdict": FINAL_CUTOVER_VERDICT,
        "verified_cutover_head": {
            "sha": head,
            "meaning": _HEAD_SEMANTICS,
        },
        "engine_readiness": {
            "ready": True,
            "status": acceptance["status"],
            "acceptance_hash": acceptance["acceptance_hash"],
            "critical_count_sum": 0,
            "production_readiness_authority": True,
        },
        "tracked_receipt_readiness": {
            "receipt_verification_status": phase101.get("status"),
            "receipt_target_ids": list(phase101.get("target_ids") or ()),
            "tracked_readiness_status": readiness.get("status"),
            "ready": readiness.get("ready"),
            "same_receipt_replay_variance": readiness.get(
                "same_receipt_replay_variance"
            ),
        },
        "clean_clone_readiness": {
            "status": clean_clone.get("status"),
            "critical_count_sum": clean_clone.get("critical_count_sum"),
            "receipt_recompute_result_hash": clean_clone.get(
                "receipt_recompute_result_hash"
            ),
            "tracked_readiness_result_hash": clean_clone.get(
                "tracked_readiness_result_hash"
            ),
            "test_result_hash": clean_clone.get("test_result_hash"),
        },
        "samsung_result": dict(samsung),
        "hynix_result": dict(hynix),
        "c08_result": dict(canary_rows[REQUIRED_ARCHETYPES[0]]),
        "c15_result": dict(canary_rows[REQUIRED_ARCHETYPES[1]]),
        "c17_result": dict(canary_rows[REQUIRED_ARCHETYPES[2]]),
        "c24_result": dict(canary_rows[REQUIRED_ARCHETYPES[3]]),
        "c28_result": dict(canary_rows[REQUIRED_ARCHETYPES[4]]),
        "current_krx_universe_counts": dict(universe_counts),
        "trigger_lane_counts": dict(trigger_counts),
        "depth_counts_l0_l5": dict(depth_counts),
        "natural_candidate_count": natural_count,
        "score_valid_final_stage_counts": dict(score_stage_counts),
        "provider_routes_and_local_call_counts": dict(
            _mapping(evidence.get("provider"), context="provider projection")
        ),
        "full_test_count": {
            "status": tests.get("status"),
            "executed_test_count": executed,
            "failed_test_count": tests.get("failed_test_count"),
            "error_test_count": tests.get("error_test_count"),
            "output_hash": tests.get("output_hash"),
            "output_hash_scope": tests.get("output_hash_scope"),
            "minimum_baseline": full_test_baseline,
        },
        "reviewer_a_v": _reviewer_projection(evidence),
        "blockers": list(acceptance.get("blockers") or ()),
    }
    if tuple(fields) != REPORT_FIELD_ORDER:
        raise AssertionError("Phase109 report field order drift")
    if fields["blockers"]:
        raise ValueError("Phase109 cannot publish with blockers")
    provider = _mapping(
        fields["provider_routes_and_local_call_counts"], context="provider report"
    )
    route_counts = _mapping(
        provider.get("provider_route_counts"), context="provider route counts"
    )
    if (
        provider.get("route_count_scope")
        != "PHASE101_AND_PHASE106_TRACKED_RECEIPTS"
        or provider.get("expected_judge_receipt_count")
        != 21 * (len(PHASE101_TARGET_IDS) + len(REQUIRED_ARCHETYPES))
        or set(route_counts) != {PROVIDER_ROUTE}
        or isinstance(route_counts.get(PROVIDER_ROUTE), bool)
        or not isinstance(route_counts.get(PROVIDER_ROUTE), int)
        or int(route_counts[PROVIDER_ROUTE])
        != 21 * (len(PHASE101_TARGET_IDS) + len(REQUIRED_ARCHETYPES))
        or any(
            int(provider.get(key) or 0) != 0
            for key in (
                "provider_error_count",
                "unauthorized_provider_call_count",
                "local_provider_call_count",
                "qwen_call_count",
                "ollama_call_count",
                "inherited_qwen_scored_fact_count",
                "inherited_ollama_scored_fact_count",
            )
        )
    ):
        raise ValueError("Phase109 provider report contains forbidden calls")
    return fields


def _render_markdown(
    *, publication_id: str, report_fields: Mapping[str, Any]
) -> bytes:
    lines = [
        "# E2R v6 운영 컷오버 최종 보고",
        "",
        f"- publication_id: `{publication_id}`",
        "- `verified_cutover_head`는 terminal 파일을 쓰기 직전 검증된 clean HEAD입니다.",
        "- terminal 문서를 커밋한 뒤의 actual final HEAD는 검증 CLI가 별도로 출력하고,",
        "  그 커밋의 first-parent와 exact-two-file diff 관계를 다시 검사합니다.",
        "- 직접적인 투자 권고를 포함하지 않습니다.",
        "",
    ]
    for index, (key, label) in enumerate(
        zip(REPORT_FIELD_ORDER, _REPORT_LABELS), start=1
    ):
        lines.extend(
            (
                f"## {index}. {label} (`{key}`)",
                "",
                "```json",
                json.dumps(
                    report_fields[key],
                    ensure_ascii=False,
                    sort_keys=True,
                    allow_nan=False,
                ),
                "```",
                "",
            )
        )
    return ("\n".join(lines).rstrip() + "\n").encode("utf-8")


def _build_publication(evidence: Mapping[str, Any]) -> tuple[Mapping[str, Any], bytes]:
    report_fields = _report_fields(evidence)
    index = _validated_phase_evidence_index(evidence.get("phase_evidence_index"))
    acceptance = _mapping(evidence.get("acceptance"), context="acceptance")
    head = str(evidence.get("verified_cutover_head") or "")
    publication_id = "E2R6CUTOVER-" + stable_hash(
        {
            "verified_cutover_head": head,
            "acceptance_hash": acceptance.get("acceptance_hash"),
            "report_fields_hash": stable_hash(report_fields),
            "phase_evidence_tree_hash": stable_hash(index),
        }
    )[:24]
    markdown = _render_markdown(
        publication_id=publication_id,
        report_fields=report_fields,
    )
    test_mode = evidence.get("test_mode") is True
    body = {
        "schema_version": PHASE109_PUBLICATION_SCHEMA,
        "status": (
            PHASE109_PUBLICATION_TEST_PASS if test_mode else PHASE109_PUBLICATION_PASS
        ),
        "publication_id": publication_id,
        "verified_cutover_head": head,
        "verified_cutover_head_semantics": _HEAD_SEMANTICS,
        "report_field_order": list(REPORT_FIELD_ORDER),
        "report_fields": report_fields,
        "report_fields_hash": stable_hash(report_fields),
        "reviewer_gate": _combined_reviewer_gate(evidence),
        "acceptance_hash": acceptance.get("acceptance_hash"),
        "phase_evidence_index": list(index),
        "phase_evidence_tree_hash": stable_hash(index),
        "markdown_sha256": _sha256_bytes(markdown),
        "terminal_files_excluded_from_phase104_and_reviewer_inputs": True,
        "production_readiness_authority": not test_mode,
        "score_or_stage_authority": False,
    }
    return {**body, "publication_hash": stable_hash(body)}, markdown


def _encode_publication(payload: Mapping[str, Any]) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def _validate_publication(
    payload: Mapping[str, Any],
    markdown: bytes,
    *,
    evidence: Mapping[str, Any],
) -> None:
    expected, expected_markdown = _build_publication(evidence)
    body = {key: value for key, value in payload.items() if key != "publication_hash"}
    if (
        set(payload) != _PUBLICATION_KEYS
        or payload.get("publication_hash") != stable_hash(body)
        or dict(payload) != dict(expected)
        or markdown != expected_markdown
        or payload.get("markdown_sha256") != _sha256_bytes(markdown)
        or tuple(payload.get("report_field_order") or ()) != REPORT_FIELD_ORDER
        or set(_mapping(payload.get("report_fields"), context="report fields"))
        != set(REPORT_FIELD_ORDER)
    ):
        raise ValueError("Phase109 terminal publication does not leaf-recompute")


def _open_existing_directory_no_symlinks(path: Path) -> int:
    absolute = path.absolute()
    descriptor = os.open(absolute.anchor, os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in absolute.parts[1:]:
            descriptor_next = os.open(
                part,
                os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0),
                dir_fd=descriptor,
            )
            os.close(descriptor)
            descriptor = descriptor_next
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _assert_pinned_directory(path: Path, descriptor: int) -> None:
    reopened = _open_existing_directory_no_symlinks(path)
    try:
        left = os.fstat(descriptor)
        right = os.fstat(reopened)
        if (left.st_dev, left.st_ino) != (right.st_dev, right.st_ino):
            raise ValueError("Phase109 publication parent changed during write")
    finally:
        os.close(reopened)


def _write_private(parent_fd: int, name: str, encoded: bytes) -> None:
    descriptor = os.open(
        name,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
        0o600,
        dir_fd=parent_fd,
    )
    try:
        offset = 0
        while offset < len(encoded):
            offset += os.write(descriptor, encoded[offset:])
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _read_regular(parent_fd: int, name: str) -> bytes:
    descriptor = os.open(
        name,
        os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0),
        dir_fd=parent_fd,
    )
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode) or metadata.st_nlink != 1:
            raise ValueError("Phase109 terminal leaf must be one regular file")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        return b"".join(chunks)
    finally:
        os.close(descriptor)


def _publication_root(repo: Path) -> Path:
    final = repo / FINAL_ROOT_RELATIVE
    if final.is_symlink() or not final.is_dir():
        raise ValueError("Phase109 requires the real canonical cutover directory")
    return final


def publish_operational_cutover(
    *,
    repo_root: str | Path = ".",
    evidence_compiler: EvidenceCompiler | None = None,
    test_mode: bool = False,
) -> Mapping[str, Any]:
    """Publish the gate first and Markdown last after all preconditions pass."""

    if not isinstance(test_mode, bool):
        raise TypeError("test_mode must be boolean")
    if evidence_compiler is not None and not test_mode:
        raise ValueError("production publisher cannot replace leaf recomputation")
    repo = Path(repo_root).resolve()
    compiler = evidence_compiler or _compile_publication_evidence
    final = _publication_root(repo)
    parent_fd = _open_existing_directory_no_symlinks(final)
    gate_tmp = f".{GATE_NAME}.{secrets.token_hex(16)}.tmp"
    report_tmp = f".{REPORT_NAME}.{secrets.token_hex(16)}.tmp"
    try:
        # Pin the canonical directory before any long leaf/test recomputation.
        # A path swap at any point therefore fails before the first rename.
        _assert_pinned_directory(final, parent_fd)
        evidence = dict(compiler(repo, None))
        if test_mode:
            evidence["test_mode"] = True
        payload, markdown = _build_publication(evidence)
        encoded_json = _encode_publication(payload)
        # Validate both complete byte payloads before the first canonical rename.
        _validate_publication(payload, markdown, evidence=evidence)
        _assert_pinned_directory(final, parent_fd)
        for name in TERMINAL_PUBLICATION_FILES:
            try:
                metadata = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
            except FileNotFoundError:
                continue
            if not stat.S_ISREG(metadata.st_mode) or metadata.st_nlink != 1:
                raise ValueError("existing Phase109 terminal path is unsafe")
        _write_private(parent_fd, gate_tmp, encoded_json)
        _write_private(parent_fd, report_tmp, markdown)
        _assert_pinned_directory(final, parent_fd)
        os.replace(gate_tmp, GATE_NAME, src_dir_fd=parent_fd, dst_dir_fd=parent_fd)
        os.fsync(parent_fd)
        _assert_pinned_directory(final, parent_fd)
        # The Markdown report is the result-last commit marker.
        os.replace(report_tmp, REPORT_NAME, src_dir_fd=parent_fd, dst_dir_fd=parent_fd)
        os.fsync(parent_fd)
        _assert_pinned_directory(final, parent_fd)
    finally:
        for name in (gate_tmp, report_tmp):
            try:
                os.unlink(name, dir_fd=parent_fd)
            except FileNotFoundError:
                pass
        os.close(parent_fd)
    verification = verify_operational_cutover_publication(
        repo_root=repo,
        evidence_compiler=compiler if evidence_compiler is not None else None,
        test_mode=test_mode,
    )
    if verification.get("status") != PHASE109_VERIFICATION_PASS:
        raise ValueError("published Phase109 leaves did not reverify")
    return {
        "schema_version": PHASE109_PUBLICATION_SCHEMA,
        "status": payload["status"],
        "publication_id": payload["publication_id"],
        "verified_cutover_head": payload["verified_cutover_head"],
        "gate_path": str(final / GATE_NAME),
        "report_path": str(final / REPORT_NAME),
        "verification_status": verification["status"],
        "current_repository_head": verification["current_repository_head"],
        "publication_head_relationship": verification[
            "publication_head_relationship"
        ],
        "terminal_commit_verified": verification["terminal_commit_verified"],
        "production_readiness_authority": payload[
            "production_readiness_authority"
        ],
        "score_or_stage_authority": False,
    }


def verify_operational_cutover_publication(
    *,
    repo_root: str | Path = ".",
    evidence_compiler: EvidenceCompiler | None = None,
    test_mode: bool = False,
) -> Mapping[str, Any]:
    """Recompute current Git/phase evidence and verify both terminal leaves."""

    failures: list[Mapping[str, Any]] = []
    publication_id: str | None = None
    head: str | None = None
    current_head: str | None = None
    relationship: str | None = None
    current_matches_verified = False
    terminal_commit_verified = False
    try:
        if not isinstance(test_mode, bool):
            raise TypeError("test_mode must be boolean")
        if evidence_compiler is not None and not test_mode:
            raise ValueError("production verifier cannot replace leaf recomputation")
        repo = Path(repo_root).resolve()
        final = _publication_root(repo)
        parent_fd = _open_existing_directory_no_symlinks(final)
        try:
            _assert_pinned_directory(final, parent_fd)
            encoded_json = _read_regular(parent_fd, GATE_NAME)
            markdown = _read_regular(parent_fd, REPORT_NAME)
            payload = _mapping(
                json.loads(encoded_json.decode("utf-8")), context=GATE_NAME
            )
            if encoded_json != _encode_publication(payload):
                raise ValueError("published reviewer gate JSON is not canonical bytes")
            publication_id = str(payload.get("publication_id") or "")
            head = str(payload.get("verified_cutover_head") or "")
            if _SHA40.fullmatch(head) is None:
                raise ValueError("published verified_cutover_head is invalid")
            compiler = evidence_compiler or _compile_publication_evidence
            evidence = dict(compiler(repo, head))
            if test_mode:
                evidence["test_mode"] = True
                current_head = str(
                    evidence.get("current_repository_head") or head
                )
                if _SHA40.fullmatch(current_head) is None:
                    raise ValueError("contract-test current HEAD is invalid")
                relationship = "CONTRACT_TEST_INJECTED"
                current_matches_verified = current_head == head
                terminal_commit_verified = current_head != head
            else:
                git_relation = _terminal_git_relationship(
                    repo, verified_cutover_head=head
                )
                current_head = str(git_relation["current_repository_head"])
                relationship = str(git_relation["relationship"])
                current_matches_verified = bool(
                    git_relation["current_head_matches_verified_cutover_head"]
                )
                terminal_commit_verified = bool(
                    git_relation["terminal_commit_verified"]
                )
            _validate_publication(payload, markdown, evidence=evidence)
            if (
                _read_regular(parent_fd, GATE_NAME) != encoded_json
                or _read_regular(parent_fd, REPORT_NAME) != markdown
            ):
                raise ValueError(
                    "Phase109 terminal leaves changed during reverification"
                )
            _assert_pinned_directory(final, parent_fd)
        finally:
            os.close(parent_fd)
    except (
        OSError,
        UnicodeError,
        RuntimeError,
        TypeError,
        ValueError,
        KeyError,
        json.JSONDecodeError,
        subprocess.CalledProcessError,
    ) as exc:
        failures.append(
            {
                "code": "PHASE109_TERMINAL_PUBLICATION_INVALID",
                "detail": f"{type(exc).__name__}:{' '.join(str(exc).split())}",
            }
        )
    return {
        "schema_version": PHASE109_VERIFICATION_SCHEMA,
        "status": (
            PHASE109_VERIFICATION_PASS
            if not failures
            else PHASE109_VERIFICATION_FAIL
        ),
        "publication_id": publication_id,
        "verified_cutover_head": head,
        "current_repository_head": current_head,
        "publication_head_relationship": relationship,
        "current_head_matches_verified_cutover_head": current_matches_verified,
        "terminal_commit_verified": terminal_commit_verified,
        "critical_count": len(failures),
        "critical_count_sum": len(failures),
        "failures": failures,
        "current_git_and_phase_evidence_recomputed": not failures,
        "terminal_files_excluded_from_phase104_and_reviewer_inputs": True,
        "production_readiness_authority": False,
        "score_or_stage_authority": False,
    }


__all__ = [
    "FINAL_CUTOVER_VERDICT",
    "GATE_NAME",
    "PHASE109_PUBLICATION_PASS",
    "PHASE109_PUBLICATION_SCHEMA",
    "PHASE109_PUBLICATION_TEST_PASS",
    "PHASE109_REVIEWER_GATE_PASS",
    "PHASE109_REVIEWER_GATE_SCHEMA",
    "PHASE109_VERIFICATION_FAIL",
    "PHASE109_VERIFICATION_PASS",
    "PHASE109_VERIFICATION_SCHEMA",
    "REPORT_FIELD_ORDER",
    "REPORT_NAME",
    "publish_operational_cutover",
    "verify_operational_cutover_publication",
]
