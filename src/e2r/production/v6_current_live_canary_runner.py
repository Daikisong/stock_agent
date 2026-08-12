"""Resumable Phase-106 runner for the sealed exact-five current canaries.

One invocation advances at most one semantic checkpoint per unfinished target.
An exact Codex Collaboration request is therefore returned to the caller
immediately instead of being retried in-process.  Publication is a separate
commit step: all five strong compact bundles are offline-verified in a private
staging tree before the complete directory is renamed into the tracked cutover.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
import json
import os
from pathlib import Path
import re
import secrets
import shutil
import stat
from typing import Any

from e2r.production.metadata import stable_hash, write_json
from e2r.production.v6_canary_compact_receipt import (
    build_selection_bound_canary_artifacts_from_output,
    build_selection_bound_canary_manifest,
    export_selection_bound_canary_bundle,
    verify_selection_bound_canary_directory,
)
from e2r.production.v6_canary_compact_review_adapter import (
    consume_blind_compact_review_responses,
    ensure_blind_compact_review_requests,
)
from e2r.production.v6_canary_results import (
    CANARY_COMPILATION_PASS,
    compile_cross_archetype_canary_directory,
    seal_cross_archetype_canary_summary,
)
from e2r.production.v6_canary_selection import (
    REQUIRED_ARCHETYPES,
    _open_existing_directory_no_symlinks,
    _open_or_create_directory_no_symlinks,
    validate_cross_archetype_canary_selection_manifest,
)
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode.collaboration_envelope_contract import (
    validate_collaboration_request,
)
from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    CollaborationCodexResearcherProvider,
)
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    CurrentResearchTarget,
    CurrentResearcherModeConfig,
    CurrentResearcherModeTargetRunner,
    FactExtractionCheckpointPending,
)
from e2r.research_brain.researcher_mode.canary_leaf_contract import (
    refresh_canary_target_manifest_hash,
)
from e2r.research_brain.researcher_mode.research_epoch import (
    load_research_epoch_checkpoint,
)
from e2r.research_brain.researcher_mode.source_graph_explorer import (
    load_source_graph_checkpoint,
    validate_source_graph_checkpoint,
)


PHASE106_RUN_SCHEMA = "e2r_v6_current_live_canary_runner_v1"
PHASE106_RUN_PASS = "E2R_V6_CURRENT_LIVE_CANARY_RUN_PASS"
PHASE106_RUN_PENDING = "E2R_V6_CURRENT_LIVE_CANARY_RUN_PENDING"
PHASE106_TERMINAL_RESEARCH_STATUS = (
    "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
)
PHASE106_RESUME_BINDING_SCHEMA = "e2r_v6_current_live_canary_resume_binding_v1"

CURRENT_LIVE_DIRECTORY_NAME = "current_live_canaries"
CURRENT_LIVE_SUMMARY_NAME = "cross_archetype_canary_summary.json"


CheckpointRunnerFactory = Callable[[Mapping[str, Any]], Any]


_COLLABORATION_PENDING_REQUEST_RE = re.compile(
    r"COLLABORATION_RESPONSE_PENDING:(COLLABREQ-[0-9a-f]{64})"
)


def _write_phase106_resume_binding(
    *,
    target_root: Path,
    selection: Mapping[str, Any],
    row: Mapping[str, Any],
) -> bool:
    """Bind a one-checkpoint Phase106 resume to its cumulative source head.

    The generic researcher-mode ``until-pass`` command writes its own progress
    receipt after every semantic checkpoint.  Phase106 deliberately returns
    after one checkpoint, so it needs an equivalent selection-bound receipt
    before the next invocation.  This receipt has no score or Stage authority;
    the fact loader still proves that every authoritative fact source remains
    in the current production document roster.
    """

    source_path = target_root / "source_graph_checkpoint.json"
    epoch_path = target_root / "research_epoch_checkpoint.json"
    if (
        not source_path.is_file()
        or source_path.is_symlink()
        or not epoch_path.is_file()
        or epoch_path.is_symlink()
    ):
        return False
    target_id = str(row.get("target_id") or "")
    as_of_date = str(selection.get("selection_as_of_date") or "")
    source = validate_source_graph_checkpoint(
        load_source_graph_checkpoint(source_path),
        target_id=target_id,
        as_of_date=as_of_date,
    )
    epoch = load_research_epoch_checkpoint(epoch_path)
    if epoch.target_id != target_id or epoch.as_of_date != as_of_date:
        raise ValueError("Phase106 resume research checkpoint identity drift")
    source_binding = {
        "target_id": target_id,
        "as_of_date": as_of_date,
        "checkpoint_id": str(source.get("checkpoint_id") or ""),
        "checkpoint_hash": str(source.get("checkpoint_hash") or ""),
        "epoch": int(source.get("epoch") or 0),
        "resumed_from_checkpoint_id": str(
            source.get("resumed_from_checkpoint_id") or ""
        ),
    }
    research_binding = {
        "target_id": epoch.target_id,
        "as_of_date": epoch.as_of_date,
        "checkpoint_id": epoch.checkpoint_id,
        "checkpoint_hash": epoch.checkpoint_hash,
        "epoch": epoch.epoch,
        "source_graph_checkpoint_id": str(
            epoch.source_graph_checkpoint_id or ""
        ),
    }
    if (
        not source_binding["checkpoint_id"]
        or not source_binding["checkpoint_hash"]
        or source_binding["epoch"] < 1
        or not research_binding["checkpoint_id"]
        or not research_binding["checkpoint_hash"]
        or not research_binding["source_graph_checkpoint_id"]
    ):
        raise ValueError("Phase106 resume checkpoint binding is incomplete")
    payload = {
        "schema_version": PHASE106_RESUME_BINDING_SCHEMA,
        "status": "RESEARCH_CHECKPOINT_PENDING",
        "target_id": target_id,
        "as_of_date": as_of_date,
        "archetype_id": str(row.get("archetype_id") or ""),
        "selection_id": str(row.get("selection_id") or ""),
        "selection_roster_hash": str(
            selection.get("selection_roster_hash") or ""
        ),
        "phase106_source_checkpoint_binding": source_binding,
        "research_epoch_checkpoint_binding": research_binding,
        "current_source_fact_superset_revalidation_required": True,
        "production_score_authority": False,
        "production_stage_authority": False,
    }
    write_json(
        target_root / "until_pass_progress.json",
        {**payload, "resume_binding_hash": stable_hash(payload)},
    )
    refresh_canary_target_manifest_hash(target_root)
    return True


def _mapping(value: object, *, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{context} must be an object")
    return value


def _selection_rows(
    selection: Mapping[str, Any],
    *,
    issuer_business_profile_manifest: Mapping[str, Any] | None,
) -> tuple[Mapping[str, Any], ...]:
    validate_cross_archetype_canary_selection_manifest(
        selection,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    rows = tuple(
        _mapping(row, context="Phase105 selection row")
        for row in selection.get("selections") or ()
    )
    if (
        len(rows) != len(REQUIRED_ARCHETYPES)
        or tuple(str(row.get("archetype_id") or "") for row in rows)
        != REQUIRED_ARCHETYPES
    ):
        raise ValueError("Phase106 requires the sealed canonical exact-five order")
    return rows


def _bundle_directory_name(row: Mapping[str, Any]) -> str:
    return f"{row['archetype_id']}_{row['target_id']}"


def _default_checkpoint_runner(_row: Mapping[str, Any]) -> Any:
    # Explicit construction is important: the target runner's implicit default
    # is the Codex CLI provider, which is not the Phase106 transport contract.
    return CurrentResearcherModeTargetRunner(
        provider=CollaborationCodexResearcherProvider.default()
    )


def _pending_research_request_rows(
    target_root: Path,
    *,
    active_request_ids: Sequence[str] | None = None,
) -> tuple[Mapping[str, str | None], ...]:
    """Expose unresolved requests that belong to the current stop boundary.

    The Collaboration journal is append-only.  A corrected semantic path can
    therefore leave an older request unanswered even after a newer checkpoint
    supersedes it.  Treating every unanswered historical request as *active*
    makes Phase106 route the obsolete request forever and prevents the current
    Supervisor/synthesis leaf from advancing.

    ``active_request_ids`` comes from the exact typed exception/current run
    that stopped this invocation.  ``None`` preserves the journal-only fallback
    used by isolated transports that do not materialize a researcher dossier;
    an explicit empty roster means that no Collaboration response is the
    current blocker.  Historical rows remain immutable and are still counted
    by the terminal journal audit.
    """

    journal = target_root / "collaboration_codex_subagent_provider"
    request_root = journal / "requests"
    response_root = journal / "responses"
    if not request_root.is_dir() or request_root.is_symlink():
        return ()
    active = None if active_request_ids is None else frozenset(active_request_ids)
    if active is not None and any(
        re.fullmatch(r"COLLABREQ-[0-9a-f]{64}", value) is None
        for value in active
    ):
        raise ValueError("active Collaboration request identity is invalid")
    pending: list[Mapping[str, str | None]] = []
    validated_request_ids: set[str] = set()
    for path in sorted(request_root.glob("*.json")):
        if path.is_symlink() or not path.is_file():
            raise ValueError("Collaboration request journal contains an unsafe leaf")
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise ValueError("Collaboration request journal is invalid") from exc
        request = validate_collaboration_request(
            _mapping(payload, context="Collaboration request")
        )
        request_id = str(request["request_id"])
        validated_request_ids.add(request_id)
        if path.name != f"{request_id}.json":
            raise ValueError("Collaboration request path identity is invalid")
        response_path = response_root / f"{request_id}.json"
        if not response_path.is_file() and (
            active is None or request_id in active
        ):
            # FULL_RESEARCHER_MODE is the parent execution scope, not the
            # collaboration pass that must be answered.  Expose the immutable
            # pass_name from the request envelope so an operator cannot route
            # an EVIDENCE_FACT_EXTRACTION continuation as (for example) a
            # RESEARCH_SUPERVISOR_REVIEW merely from the parent scope label.
            pending.append(
                {
                    "request_id": request_id,
                    "reviewer_slot": None,
                    "request_scope": "FULL_RESEARCHER_MODE",
                    "pass_name": str(request["pass_name"]),
                    "schema_name": str(request["schema_name"]),
                }
            )
    if active is not None and not active.issubset(validated_request_ids):
        raise ValueError("active Collaboration request is absent from the journal")
    return tuple(pending)


def _active_collaboration_request_ids(value: object) -> tuple[str, ...]:
    """Recover exact current pending identities without reading old journal rows."""

    found: set[str] = set()

    def visit(item: object) -> None:
        if isinstance(item, str):
            found.update(
                match.group(1)
                for match in _COLLABORATION_PENDING_REQUEST_RE.finditer(item)
            )
            return
        if isinstance(item, Mapping):
            for nested in item.values():
                visit(nested)
            return
        if isinstance(item, Sequence) and not isinstance(
            item, (str, bytes, bytearray)
        ):
            for nested in item:
                visit(nested)

    visit(value)
    return tuple(sorted(found))


def _pending_result(
    *,
    selection: Mapping[str, Any],
    rows: Sequence[Mapping[str, Any]],
    prepared_count: int,
    active_row: Mapping[str, Any],
    pending_kind: str,
    request_rows: Sequence[Mapping[str, Any]],
    external_wait_marker: str = "COLLABORATION_RESPONSE_PENDING",
) -> Mapping[str, Any]:
    return {
        "schema_version": PHASE106_RUN_SCHEMA,
        "status": PHASE106_RUN_PENDING,
        "selection_roster_hash": selection["selection_roster_hash"],
        "required_archetypes": list(REQUIRED_ARCHETYPES),
        "selected_target_ids": [str(row["target_id"]) for row in rows],
        "prepared_canary_count": prepared_count,
        "active_archetype_id": active_row["archetype_id"],
        "active_target_id": active_row["target_id"],
        "pending_kind": pending_kind,
        "pending_requests": [dict(row) for row in request_rows],
        "blockers": [external_wait_marker],
        "external_wait_marker": external_wait_marker,
        "completion_based_on_fixed_retries": False,
        "gold_visibility": False,
        "gold_call_count": 0,
        "local_provider_call_count": 0,
        "score_or_stage_authority": False,
        "production_readiness_authority": False,
    }


def _research_pending_result(
    *,
    selection: Mapping[str, Any],
    rows: Sequence[Mapping[str, Any]],
    prepared_count: int,
    row: Mapping[str, Any],
    target_root: Path,
    detail: str,
    active_request_ids: Sequence[str] | None = None,
) -> Mapping[str, Any]:
    request_rows = _pending_research_request_rows(
        target_root,
        active_request_ids=active_request_ids,
    )
    wait_marker = (
        "COLLABORATION_RESPONSE_PENDING" if request_rows else "SOURCE_PENDING"
    )
    return _pending_result(
        selection=selection,
        rows=rows,
        prepared_count=prepared_count,
        active_row=row,
        pending_kind="RESEARCH_COLLABORATION_RESPONSE" if request_rows else detail,
        request_rows=request_rows,
        external_wait_marker=wait_marker,
    )


def _terminal_artifacts_if_present(
    *,
    repo_root: Path,
    target_root: Path,
    selection: Mapping[str, Any],
    row: Mapping[str, Any],
    issuer_business_profile_manifest: Mapping[str, Any] | None,
) -> Mapping[str, Any] | None:
    manifest_path = target_root / "target_run_manifest.json"
    if not manifest_path.is_file() or manifest_path.is_symlink():
        return None
    try:
        manifest = _mapping(
            json.loads(manifest_path.read_text(encoding="utf-8")),
            context="target run manifest",
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("target run manifest is invalid") from exc
    if (
        manifest.get("status") != PHASE106_TERMINAL_RESEARCH_STATUS
        or manifest.get("production_research_complete") is not True
    ):
        return None
    return build_selection_bound_canary_artifacts_from_output(
        repo_root=repo_root,
        target_root=target_root,
        selection=selection,
        selection_row=row,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )


def _verify_prepared_bundle(
    *,
    path: Path,
    selection: Mapping[str, Any],
    repo_root: Path,
    issuer_business_profile_manifest: Mapping[str, Any] | None,
) -> Mapping[str, Any]:
    return verify_selection_bound_canary_directory(
        receipt_directory=path,
        selection=selection,
        repo_root=repo_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )


def _fsync_tree(root: Path) -> None:
    for path in sorted(root.rglob("*"), key=lambda item: len(item.parts), reverse=True):
        if path.is_symlink():
            raise ValueError("publication staging tree contains a symlink")
        if path.is_file():
            descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
            try:
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
        elif path.is_dir():
            descriptor = os.open(
                path,
                os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0),
            )
            try:
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
    descriptor = os.open(
        root,
        os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0),
    )
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _assert_pinned_directory(path: Path, descriptor: int) -> None:
    """Prove that a pathname still names the directory pinned by ``descriptor``."""

    reopened = _open_existing_directory_no_symlinks(path)
    try:
        pinned = os.fstat(descriptor)
        current = os.fstat(reopened)
        if (pinned.st_dev, pinned.st_ino) != (current.st_dev, current.st_ino):
            raise ValueError("Phase106 cutover parent changed during publication")
    finally:
        os.close(reopened)


def _entry_metadata(parent_fd: int, name: str) -> os.stat_result | None:
    try:
        return os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        return None


def _compile_pass(
    *,
    selection: Mapping[str, Any],
    live_root: Path,
    repo_root: Path,
    issuer_business_profile_manifest: Mapping[str, Any] | None,
) -> tuple[Mapping[str, Any], Mapping[str, Any]]:
    compilation = compile_cross_archetype_canary_directory(
        selection=selection,
        live_root=live_root,
        repo_root=repo_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    summary = compilation.get("summary")
    if compilation.get("status") != CANARY_COMPILATION_PASS or not isinstance(
        summary, Mapping
    ):
        raise ValueError("the exact five offline compact bundles did not compile")
    return compilation, summary


def _publish_exact_five(
    *,
    repo_root: Path,
    cutover_root: Path,
    work_root: Path,
    selection: Mapping[str, Any],
    rows: Sequence[Mapping[str, Any]],
    issuer_business_profile_manifest: Mapping[str, Any] | None,
) -> tuple[Path, Path, Mapping[str, Any]]:
    live_root = cutover_root / CURRENT_LIVE_DIRECTORY_NAME
    summary_path = cutover_root / CURRENT_LIVE_SUMMARY_NAME
    cutover_fd = _open_or_create_directory_no_symlinks(cutover_root)
    try:
        _assert_pinned_directory(cutover_root, cutover_fd)
        live_metadata = _entry_metadata(cutover_fd, CURRENT_LIVE_DIRECTORY_NAME)
        if live_metadata is not None:
            if not stat.S_ISDIR(live_metadata.st_mode):
                raise ValueError("existing current-live canary root is unsafe")
            compilation, summary = _compile_pass(
                selection=selection,
                live_root=live_root,
                repo_root=repo_root,
                issuer_business_profile_manifest=issuer_business_profile_manifest,
            )
            _assert_pinned_directory(cutover_root, cutover_fd)
            seal_cross_archetype_canary_summary(
                summary_path,
                summary,
                selection=selection,
                live_root=live_root,
                repo_root=repo_root,
                issuer_business_profile_manifest=issuer_business_profile_manifest,
            )
            _assert_pinned_directory(cutover_root, cutover_fd)
            return live_root, summary_path, compilation
        if _entry_metadata(cutover_fd, CURRENT_LIVE_SUMMARY_NAME) is not None:
            raise ValueError("Phase106 summary exists without its exact-five live tree")

        prepared_root = work_root / "prepared"
        staging_name = (
            f".{CURRENT_LIVE_DIRECTORY_NAME}.{secrets.token_hex(16)}.tmp"
        )
        os.mkdir(staging_name, mode=0o700, dir_fd=cutover_fd)
        staging = cutover_root / staging_name
        renamed = False
        try:
            _assert_pinned_directory(cutover_root, cutover_fd)
            for row in rows:
                source = prepared_root / _bundle_directory_name(row)
                destination = staging / _bundle_directory_name(row)
                _verify_prepared_bundle(
                    path=source,
                    selection=selection,
                    repo_root=repo_root,
                    issuer_business_profile_manifest=(
                        issuer_business_profile_manifest
                    ),
                )
                shutil.copytree(source, destination, symlinks=False)
                _verify_prepared_bundle(
                    path=destination,
                    selection=selection,
                    repo_root=repo_root,
                    issuer_business_profile_manifest=(
                        issuer_business_profile_manifest
                    ),
                )
            _staging_compilation, staged_summary = _compile_pass(
                selection=selection,
                live_root=staging,
                repo_root=repo_root,
                issuer_business_profile_manifest=issuer_business_profile_manifest,
            )
            _fsync_tree(staging)
            _assert_pinned_directory(cutover_root, cutover_fd)
            if _entry_metadata(cutover_fd, CURRENT_LIVE_DIRECTORY_NAME) is not None:
                raise ValueError("current-live canary root appeared during publication")
            os.rename(
                staging_name,
                CURRENT_LIVE_DIRECTORY_NAME,
                src_dir_fd=cutover_fd,
                dst_dir_fd=cutover_fd,
            )
            renamed = True
            os.fsync(cutover_fd)
            _assert_pinned_directory(cutover_root, cutover_fd)
            canonical_compilation, canonical_summary = _compile_pass(
                selection=selection,
                live_root=live_root,
                repo_root=repo_root,
                issuer_business_profile_manifest=issuer_business_profile_manifest,
            )
            if dict(canonical_summary) != dict(staged_summary):
                raise ValueError(
                    "canonical five-canary summary changed after atomic rename"
                )
            seal_cross_archetype_canary_summary(
                summary_path,
                canonical_summary,
                selection=selection,
                live_root=live_root,
                repo_root=repo_root,
                issuer_business_profile_manifest=issuer_business_profile_manifest,
            )
            _assert_pinned_directory(cutover_root, cutover_fd)
            return live_root, summary_path, canonical_compilation
        finally:
            if not renamed and staging.exists():
                try:
                    _assert_pinned_directory(cutover_root, cutover_fd)
                except (OSError, ValueError):
                    pass
                else:
                    shutil.rmtree(staging)
    finally:
        os.close(cutover_fd)


class V6CurrentLiveCanaryRunner:
    """Advance and publish the sealed Phase105 exact-five without Gold access."""

    def __init__(
        self,
        *,
        checkpoint_runner_factory: CheckpointRunnerFactory | None = None,
    ) -> None:
        self._checkpoint_runner_factory = (
            checkpoint_runner_factory or _default_checkpoint_runner
        )

    def run_checkpoint(
        self,
        *,
        repo_root: str | Path,
        selection: Mapping[str, Any],
        work_root: str | Path,
        cutover_root: str | Path,
        issuer_business_profile_manifest: Mapping[str, Any] | None = None,
        live_materialization_authorized: bool,
        checkpoint_resume: bool,
        fact_documents_per_call: int = 1,
    ) -> Mapping[str, Any]:
        if not live_materialization_authorized or not checkpoint_resume:
            raise ValueError(
                "Phase106 requires live authorization and checkpoint resume"
            )
        if (
            isinstance(fact_documents_per_call, bool)
            or not isinstance(fact_documents_per_call, int)
            or fact_documents_per_call <= 0
        ):
            raise ValueError("fact_documents_per_call must be positive")
        repo = Path(repo_root).resolve()
        work = Path(work_root).absolute()
        cutover = Path(cutover_root).absolute()
        rows = _selection_rows(
            selection,
            issuer_business_profile_manifest=issuer_business_profile_manifest,
        )
        work.mkdir(parents=True, exist_ok=True)
        if work.is_symlink() or not work.is_dir():
            raise ValueError("Phase106 work root is unsafe")

        live_root = cutover / CURRENT_LIVE_DIRECTORY_NAME
        if live_root.exists():
            published, summary_path, compilation = _publish_exact_five(
                repo_root=repo,
                cutover_root=cutover,
                work_root=work,
                selection=selection,
                rows=rows,
                issuer_business_profile_manifest=(
                    issuer_business_profile_manifest
                ),
            )
            return self._pass_result(
                selection=selection,
                rows=rows,
                live_root=published,
                summary_path=summary_path,
                compilation=compilation,
            )

        prepared_root = work / "prepared"
        prepared_root.mkdir(parents=True, exist_ok=True)
        prepared_count = 0
        for row in rows:
            bundle_name = _bundle_directory_name(row)
            prepared = prepared_root / bundle_name
            if prepared.exists():
                _verify_prepared_bundle(
                    path=prepared,
                    selection=selection,
                    repo_root=repo,
                    issuer_business_profile_manifest=(
                        issuer_business_profile_manifest
                    ),
                )
                prepared_count += 1
                continue

            research_parent = work / "research" / str(row["archetype_id"])
            target_root = research_parent / str(row["target_id"])
            artifacts = _terminal_artifacts_if_present(
                repo_root=repo,
                target_root=target_root,
                selection=selection,
                row=row,
                issuer_business_profile_manifest=(
                    issuer_business_profile_manifest
                ),
            )
            if artifacts is None:
                target = CurrentResearchTarget(
                    symbol=str(row["target_id"]),
                    company_name=str(row["company_name"]),
                )
                config = CurrentResearcherModeConfig(
                    as_of_date=str(selection["selection_as_of_date"]),
                    archetype_id=str(row["archetype_id"]),
                    output_root=research_parent,
                    live_materialization_authorized=True,
                    checkpoint_resume=True,
                    gold_lane_isolated=True,
                    require_researcher_parity=True,
                    latest_trading_snapshot_date=str(
                        row.get("krx_effective_date")
                        or selection["selection_as_of_date"]
                    ),
                    fact_documents_per_call=fact_documents_per_call,
                )
                _write_phase106_resume_binding(
                    target_root=target_root,
                    selection=selection,
                    row=row,
                )
                checkpoint_runner = self._checkpoint_runner_factory(row)
                try:
                    run = checkpoint_runner.run_checkpoint(
                        config=config,
                        target=target,
                        repo_root=repo,
                        source_resume_mode="REUSE_READY_CHECKPOINT",
                    )
                except FactExtractionCheckpointPending as exc:
                    return _research_pending_result(
                        selection=selection,
                        rows=rows,
                        prepared_count=prepared_count,
                        row=row,
                        target_root=target_root,
                        detail="FACT_EXTRACTION_CHECKPOINT_PENDING",
                        active_request_ids=_active_collaboration_request_ids(
                            (
                                exc.audit,
                                exc.fact_extraction.pending_reasons,
                                exc.source_graph.checkpoint.get(
                                    "pending_reasons"
                                ),
                            )
                        ),
                    )
                except StructuredProviderUnavailable as exc:
                    detail = str(exc)
                    if not detail.startswith("COLLABORATION_RESPONSE_PENDING:"):
                        raise
                    return _research_pending_result(
                        selection=selection,
                        rows=rows,
                        prepared_count=prepared_count,
                        row=row,
                        target_root=target_root,
                        detail="RESEARCH_COLLABORATION_RESPONSE",
                        active_request_ids=(
                            _active_collaboration_request_ids(detail)
                        ),
                    )
                if getattr(run, "status", None) != PHASE106_TERMINAL_RESEARCH_STATUS:
                    return _research_pending_result(
                        selection=selection,
                        rows=rows,
                        prepared_count=prepared_count,
                        row=row,
                        target_root=target_root,
                        detail="SEMANTIC_CHECKPOINT_PENDING",
                        active_request_ids=_active_collaboration_request_ids(
                            (
                                run.audit,
                                run.dossier.pending_reasons,
                                run.fact_extraction.pending_reasons,
                                run.source_graph.checkpoint.get(
                                    "pending_reasons"
                                ),
                                run.structured_materialization.pending_reasons,
                                # A Supervisor transport wait is materialized
                                # by StageCourt after dossier construction.  It
                                # is therefore absent from dossier.pending_reasons
                                # even though it is the exact current blocker.
                                run.stagecourt.decision.pending_reasons,
                                # Supervisor and independent saturation waits
                                # are owned by the ResearchEpoch result, not by
                                # the deterministic StageCourt decision.
                                run.research_epoch.to_dict(),
                            )
                        ),
                    )
                artifacts = build_selection_bound_canary_artifacts_from_output(
                    repo_root=repo,
                    target_root=target_root,
                    selection=selection,
                    selection_row=row,
                    issuer_business_profile_manifest=(
                        issuer_business_profile_manifest
                    ),
                )

            manifest = build_selection_bound_canary_manifest(
                selection=selection,
                selection_id=str(row["selection_id"]),
                artifacts=artifacts,
                repo_root=repo,
                issuer_business_profile_manifest=issuer_business_profile_manifest,
            )
            review_root = work / "reviews" / bundle_name
            roster = ensure_blind_compact_review_requests(
                journal_root=review_root,
                selection=selection,
                manifest=manifest,
                artifacts=artifacts,
                repo_root=repo,
                issuer_business_profile_manifest=(
                    issuer_business_profile_manifest
                ),
            )
            pending_reviews = tuple(
                _mapping(item, context="blind review request")
                for item in roster.get("requests") or ()
                if isinstance(item, Mapping) and item.get("status") == "PENDING"
            )
            if pending_reviews:
                return _pending_result(
                    selection=selection,
                    rows=rows,
                    prepared_count=prepared_count,
                    active_row=row,
                    pending_kind="INDEPENDENT_CODEX_REVIEWS",
                    request_rows=tuple(
                        {
                            "request_id": item["request_id"],
                            "reviewer_slot": item["reviewer_slot"],
                            "request_scope": "BLIND_COMPACT_REVIEW",
                        }
                        for item in pending_reviews
                    ),
                )
            reviews = consume_blind_compact_review_responses(
                journal_root=review_root,
                selection=selection,
                manifest=manifest,
                artifacts=artifacts,
                repo_root=repo,
                issuer_business_profile_manifest=(
                    issuer_business_profile_manifest
                ),
            )
            export_selection_bound_canary_bundle(
                output_directory=prepared,
                selection=selection,
                manifest=manifest,
                artifacts=artifacts,
                reviews=reviews,
                repo_root=repo,
                issuer_business_profile_manifest=(
                    issuer_business_profile_manifest
                ),
            )
            _verify_prepared_bundle(
                path=prepared,
                selection=selection,
                repo_root=repo,
                issuer_business_profile_manifest=(
                    issuer_business_profile_manifest
                ),
            )
            prepared_count += 1

        if prepared_count != len(REQUIRED_ARCHETYPES):
            raise ValueError("Phase106 prepared roster did not reach exact five")
        published, summary_path, compilation = _publish_exact_five(
            repo_root=repo,
            cutover_root=cutover,
            work_root=work,
            selection=selection,
            rows=rows,
            issuer_business_profile_manifest=issuer_business_profile_manifest,
        )
        return self._pass_result(
            selection=selection,
            rows=rows,
            live_root=published,
            summary_path=summary_path,
            compilation=compilation,
        )

    @staticmethod
    def _pass_result(
        *,
        selection: Mapping[str, Any],
        rows: Sequence[Mapping[str, Any]],
        live_root: Path,
        summary_path: Path,
        compilation: Mapping[str, Any],
    ) -> Mapping[str, Any]:
        return {
            "schema_version": PHASE106_RUN_SCHEMA,
            "status": PHASE106_RUN_PASS,
            "selection_roster_hash": selection["selection_roster_hash"],
            "required_archetypes": list(REQUIRED_ARCHETYPES),
            "selected_target_ids": [str(row["target_id"]) for row in rows],
            "prepared_canary_count": len(REQUIRED_ARCHETYPES),
            "independent_review_count": 2 * len(REQUIRED_ARCHETYPES),
            "live_root": str(live_root),
            "summary_path": str(summary_path),
            "summary_id": _mapping(
                compilation.get("summary"), context="Phase106 summary"
            )["summary_id"],
            "completion_based_on_fixed_retries": False,
            "gold_visibility": False,
            "gold_call_count": 0,
            "local_provider_call_count": 0,
            "score_or_stage_authority": False,
            "production_readiness_authority": False,
        }


def run_current_live_canaries_checkpoint(**kwargs: Any) -> Mapping[str, Any]:
    """Convenience entry point using the production Collaboration-only runner."""

    return V6CurrentLiveCanaryRunner().run_checkpoint(**kwargs)


__all__ = [
    "CURRENT_LIVE_DIRECTORY_NAME",
    "CURRENT_LIVE_SUMMARY_NAME",
    "PHASE106_RUN_PASS",
    "PHASE106_RUN_PENDING",
    "PHASE106_RUN_SCHEMA",
    "PHASE106_TERMINAL_RESEARCH_STATUS",
    "V6CurrentLiveCanaryRunner",
    "run_current_live_canaries_checkpoint",
]
