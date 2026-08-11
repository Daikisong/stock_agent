"""Leaf-recomputed Phase 108/109 operational acceptance and reviewers K--V."""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_selection import (
    FORCED_SELECTION,
    ISSUER_PROFILE_MANIFEST_NAME,
    REQUIRED_ARCHETYPES,
    load_current_issuer_business_profile_manifest,
)
from e2r.production.v6_canary_selection import (
    load_sealed_cross_archetype_canary_selection,
)
from e2r.production.v6_canary_results import (
    CANARY_COMPILATION_PASS,
    CANARY_RESULT_NAME,
    compile_cross_archetype_canary_directory,
)
from e2r.production.v6_current_krx_census import (
    CURRENT_KRX_CENSUS_PASS,
    CURRENT_KRX_CENSUS_SCHEMA,
    CURRENT_KRX_STAGE_ROW_SCHEMA,
)
from e2r.production.v6_current_krx_deep_receipt_runner import (
    validate_current_krx_deep_receipt_root,
)
from e2r.production.v6_production_static_audit import (
    PRODUCTION_STATIC_AUDIT_LEAF,
    REQUIRED_ZERO_COUNT_KEYS as STATIC_AUDIT_ZERO_COUNT_KEYS,
    compile_production_static_audit,
    validate_production_static_audit,
)
from e2r.production.v6_operational_self_repair import (
    SELF_REPAIR_AUDIT_LEAF,
    SELF_REPAIR_JOURNAL_LEAF,
    compile_operational_self_repair_audit,
    validate_operational_self_repair_audit,
)
from e2r.research_brain.researcher_mode.artifact_lifecycle import (
    ARTIFACT_LIFECYCLE_AUDIT_SCHEMA,
    ARTIFACT_LIFECYCLE_PASS,
    CANARY_RECEIPT_DATE,
    CLEAN_CLONE_REPRODUCTION_PASS,
    CLEAN_CLONE_REPRODUCTION_SCHEMA,
    CLEAN_CLONE_TEST_PASS,
    CLEAN_CLONE_TEST_SCHEMA,
    CROSS_ARCHETYPE_CANARY_SUMMARY_PASS,
    CROSS_ARCHETYPE_CANARY_SUMMARY_SCHEMA,
    FINAL_ROOT_RELATIVE,
    PROVIDER_RUNTIME_AUDIT_PASS,
    PROVIDER_RUNTIME_AUDIT_SCHEMA,
    TERMINAL_PUBLICATION_FILES,
)
from e2r.research_brain.researcher_mode.independent_acceptance import (
    REVIEWER_GATE_PASS as LEGACY_REVIEWER_GATE_PASS,
    SCHEMA_VERSION as LEGACY_REVIEWER_GATE_SCHEMA,
    compile_phase100_acceptance_bundle,
)
from e2r.research_brain.researcher_mode.tracked_receipts import (
    PHASE101_TARGET_IDS,
    VERIFICATION_PASS,
    VERIFICATION_SCHEMA,
    verify_receipts,
)
from e2r.research_brain.researcher_mode.tracked_readiness import (
    TRACKED_READINESS_PASS,
    TRACKED_READINESS_SCHEMA,
    _repository_identity_is_trusted,
    canonical_repository_root,
)


OPERATIONAL_ACCEPTANCE_SCHEMA = "e2r_v6_operational_acceptance_v1"
OPERATIONAL_REVIEWER_GATE_SCHEMA = "e2r_v6_operational_reviewer_gate_k_v_v1"
OPERATIONAL_ACCEPTANCE_PASS = "MEANINGFUL_E2R_OPERATIONAL_MARKET_CUTOVER_READY"
OPERATIONAL_ACCEPTANCE_FAIL = "E2R_V6_OPERATIONAL_MARKET_CUTOVER_NOT_READY"
OPERATIONAL_ACCEPTANCE_TEST_PASS = "E2R_V6_OPERATIONAL_ACCEPTANCE_CONTRACT_TEST_PASS"
OPERATIONAL_ACCEPTANCE_PENDING = "E2R_V6_OPERATIONAL_ACCEPTANCE_PENDING"
OPERATIONAL_PHASE_DRIVER_SCHEMA = "e2r_v6_operational_phase_driver_v1"
REVIEWER_GATE_PASS = "E2R_V6_OPERATIONAL_REVIEWER_K_V_PASS"
REVIEWER_GATE_FAIL = "E2R_V6_OPERATIONAL_REVIEWER_K_V_FAIL"
REVIEWER_IDS = tuple("KLMNOPQRSTUV")
V5_FULL_TEST_COUNT_BASELINE = 6637

LEGACY_GATE_RELATIVE = Path("docs/operational/e2r_v5_reviewer_gate.json")
REQUIRED_PHASE_FILES = {
    "101": (
        f"canary_receipts/{CANARY_RECEIPT_DATE}/005930/receipt_manifest.json",
        f"canary_receipts/{CANARY_RECEIPT_DATE}/000660/receipt_manifest.json",
    ),
    "102": (
        "clean_clone/receipt_recompute_result.json",
        "clean_clone/tracked_readiness_result.json",
    ),
    "103": ("clean_clone_reproduction.json", "clean_clone/test_result.json"),
    "104": ("artifact_lifecycle_manifest.json", "artifact_lifecycle_audit.json"),
    "105": ("cross_archetype_canary_selection.json",),
    "106": ("cross_archetype_canary_summary.json", "current_live_canaries"),
    "107": ("current_krx_census_summary.json", "current_krx_stage_map_compact.jsonl"),
    "108": (
        PRODUCTION_STATIC_AUDIT_LEAF,
        SELF_REPAIR_JOURNAL_LEAF,
        SELF_REPAIR_AUDIT_LEAF,
    ),
}

ReceiptRootVerifier = Callable[[str | Path], Mapping[str, Any]]
RepositoryProbe = Callable[[Path, Sequence[Path]], Mapping[str, Any]]
TestRunner = Callable[[Path], Mapping[str, Any]]
CommandRunner = Callable[[Sequence[str], Path], subprocess.CompletedProcess[str]]
CheckpointWriter = Callable[[Mapping[str, Any]], None]
AcceptanceCompiler = Callable[..., Mapping[str, Any]]
StaticAuditCompiler = Callable[..., Mapping[str, Any]]


@dataclass(frozen=True)
class OperationalReviewer:
    reviewer_id: str
    title: str
    critical_counts: Mapping[str, int]
    metrics: Mapping[str, Any]
    evidence_hashes: Mapping[str, str | None]
    blockers: tuple[str, ...] = ()

    def to_dict(self) -> Mapping[str, Any]:
        critical_sum = sum(int(value) for value in self.critical_counts.values())
        return {
            "reviewer_id": self.reviewer_id,
            "title": self.title,
            "status": "PASS" if critical_sum == 0 else "FAIL",
            "critical_counts": dict(self.critical_counts),
            "critical_count_sum": critical_sum,
            "metrics": dict(self.metrics),
            "evidence_hashes": dict(self.evidence_hashes),
            "blockers": list(self.blockers),
            "leaf_recomputed": True,
            "caller_attestation_trusted": False,
        }


def run_operational_acceptance_phases(
    *,
    repo_root: str | Path,
    final_root: str | Path = FINAL_ROOT_RELATIVE,
    output_root: str | Path,
    as_of_date: str,
    research_provider: str,
    run_profile: str | Path = "configs/e2r_census_selective_deep_v1.json",
    checkpoint_resume: bool = True,
    prior_checkpoint: Mapping[str, Any] | None = None,
    checkpoint_writer: CheckpointWriter | None = None,
    command_runner: CommandRunner | None = None,
    acceptance_compiler: AcceptanceCompiler | None = None,
    test_mode: bool = False,
) -> Mapping[str, Any]:
    """Run the real Phase-108 leaves in dependency order.

    Existing leaves are revalidated and skipped.  A missing leaf is delegated
    only to its canonical CLI.  Every nonzero or invalid canonical result stays
    pending instead of manufacturing a PASS.
    """

    date.fromisoformat(as_of_date)
    if research_provider != "codex-collaboration":
        raise ValueError("operational acceptance requires Codex Collaboration")
    if not isinstance(checkpoint_resume, bool) or not isinstance(test_mode, bool):
        raise TypeError("checkpoint_resume and test_mode must be boolean")
    custom = command_runner is not None or acceptance_compiler is not None
    if custom and not test_mode:
        raise ValueError("production phase driver cannot replace canonical executors")
    repo = Path(repo_root).resolve()
    final = _resolve_canonical_final(repo, final_root)
    output = Path(output_root)
    output = output.resolve() if output.is_absolute() else (repo / output).resolve()
    profile = Path(run_profile)
    profile = profile.resolve() if profile.is_absolute() else (repo / profile).resolve()
    previous = dict(prior_checkpoint or {}) if checkpoint_resume else {}
    if previous:
        driver = previous.get("phase_driver") if isinstance(previous.get("phase_driver"), Mapping) else previous
        if (
            driver.get("schema_version") != OPERATIONAL_PHASE_DRIVER_SCHEMA
            or driver.get("repo_root_hash") != stable_hash(str(repo))
            or driver.get("as_of_date") != as_of_date
            or driver.get("research_provider") != research_provider
        ):
            raise ValueError("operational checkpoint identity drift")
        attempts = list(driver.get("command_attempts") or ())
        iteration = int(driver.get("resume_iteration") or 0) + 1
    else:
        attempts = []
        iteration = 1
    steps: list[Mapping[str, Any]] = []
    runner = command_runner or _run_phase_subprocess
    compiler = acceptance_compiler or compile_operational_acceptance

    def snapshot(
        *,
        pending_reason: str | None = None,
        acceptance: Mapping[str, Any] | None = None,
    ) -> Mapping[str, Any]:
        driver_core = {
            "schema_version": OPERATIONAL_PHASE_DRIVER_SCHEMA,
            "status": "PHASE_DRIVER_COMPLETE" if acceptance is not None else "PHASE_DRIVER_PENDING",
            "as_of_date": as_of_date,
            "research_provider": research_provider,
            "repo_root_hash": stable_hash(str(repo)),
            "final_root": str(FINAL_ROOT_RELATIVE),
            "resume_iteration": iteration,
            "resumed_from_checkpoint": bool(previous),
            "steps": list(steps),
            "command_attempts": list(attempts),
            "pending_reason": pending_reason,
            "fixed_retry_count_is_completion_authority": False,
            "score_or_stage_authority": False,
            "production_score_authority": False,
        }
        driver_row = {**driver_core, "driver_hash": stable_hash(driver_core)}
        if acceptance is not None:
            return {**dict(acceptance), "phase_driver": driver_row}
        return {
            "schema_version": OPERATIONAL_ACCEPTANCE_SCHEMA,
            "status": OPERATIONAL_ACCEPTANCE_PENDING,
            "ready": False,
            "production_readiness_authority": False,
            "blockers": [pending_reason] if pending_reason else [],
            "score_or_stage_authority": False,
            "phase_driver": driver_row,
        }

    def persist(*, pending_reason: str | None = None) -> None:
        if checkpoint_writer is not None:
            checkpoint_writer(snapshot(pending_reason=pending_reason))

    def skip(step_id: str, evidence: Any) -> None:
        steps.append(_driver_step(step_id, "VALIDATED_CHECKPOINT", "SKIPPED_VALIDATED", evidence))
        persist()

    def invoke_argv(step_id: str, argv: Sequence[str]) -> Mapping[str, Any]:
        exact_argv = list(map(str, argv))
        completed = runner(exact_argv, repo)
        attempt = _command_attempt(
            step_id=step_id,
            argv=exact_argv,
            completed=completed,
        )
        attempts.append(attempt)
        steps.append(
            _driver_step(
                step_id,
                "COMMAND_PASS" if completed.returncode == 0 else "COMMAND_PENDING",
                "CLI_EXECUTED",
                attempt,
            )
        )
        persist()
        return attempt

    def invoke(step_id: str, module: str, args: Sequence[str]) -> Mapping[str, Any]:
        return invoke_argv(
            step_id,
            [sys.executable, "-m", module, *map(str, args)],
        )

    fingerprint = _current_operational_fingerprint(repo, profile, research_provider)
    steps.append(_driver_step("current_fingerprint", "VALIDATED_CHECKPOINT", "RECOMPUTED", fingerprint))
    persist()

    receipt_root = final / "canary_receipts" / CANARY_RECEIPT_DATE
    if _phase101_receipts_ready(receipt_root):
        skip("c06_receipt_verification", {"receipt_root_hash": stable_hash(str(receipt_root))})
    else:
        source_root = (
            repo / "output" / "researcher_mode" / "c06" / CANARY_RECEIPT_DATE
        )
        research_attempt = invoke(
            "c06_canonical_research",
            "e2r.cli.run_e2r_researcher_mode_until_pass",
            [
                "--as-of-date", CANARY_RECEIPT_DATE,
                "--symbols", ",".join(PHASE101_TARGET_IDS),
                "--archetype", "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "--live-materialization-authorized", "true",
                "--checkpoint-resume", "true",
                "--gold-lane-isolated", "true",
                "--require-researcher-parity", "true",
                "--output-root", str(source_root),
                "--research-provider", "codex-collaboration",
            ],
        )
        if _attempt_is_external_wait(research_attempt):
            result = snapshot(pending_reason="PHASE101_C06_COLLABORATION_PENDING")
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result
        if research_attempt["exit_code"] != 0:
            result = snapshot(pending_reason="PHASE101_C06_CANONICAL_RUN_PENDING")
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result
        export_attempt = invoke(
            "tracked_receipt_export",
            "e2r.cli.export_e2r_v6_tracked_receipts",
            [
                "--repo-root", str(repo),
                "--source-output-root", str(source_root),
                "--targets", ",".join(PHASE101_TARGET_IDS),
                "--destination", str(receipt_root),
            ],
        )
        if export_attempt["exit_code"] != 0:
            result = snapshot(pending_reason="PHASE101_TRACKED_RECEIPT_EXPORT_PENDING")
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result
        verify_attempt = invoke(
            "c06_receipt_verification",
            "e2r.cli.verify_e2r_v6_tracked_receipts",
            ["--receipt-root", str(receipt_root), "--offline", "true"],
        )
        if verify_attempt["exit_code"] != 0 or not _phase101_receipts_ready(receipt_root):
            result = snapshot(pending_reason="PHASE101_RECEIPT_VERIFICATION_PENDING")
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result

    selection_path = final / "cross_archetype_canary_selection.json"
    issuer_profile_path = final / ISSUER_PROFILE_MANIFEST_NAME
    if _phase105_selection_ready(
        selection_path,
        as_of_date,
        issuer_profile_path=issuer_profile_path,
    ):
        skip("cross_archetype_canary_selection", _safe_json(selection_path))
    else:
        # First let the canonical selector close the phase from natural,
        # fully COMPLETE planner runs.  This read-only attempt avoids fetching
        # five official issuer profiles when the natural roster already meets
        # the exact archetype contract.
        natural_attempt = invoke(
            "cross_archetype_canary_selection_natural_attempt",
            "e2r.cli.select_e2r_v6_cross_archetype_canaries",
            ["--as-of-date", as_of_date, "--repo-root", str(repo)],
        )
        if (
            natural_attempt["exit_code"] != 0
            or not _phase105_selection_ready(
                selection_path,
                as_of_date,
                issuer_profile_path=issuer_profile_path,
            )
        ):
            if _phase105_profile_ready(issuer_profile_path, as_of_date):
                skip(
                    "issuer_business_profile_materialization",
                    _safe_json(issuer_profile_path),
                )
            else:
                profile_attempt = invoke(
                    "issuer_business_profile_materialization",
                    "e2r.cli.materialize_e2r_v6_issuer_business_profiles",
                    ["--as-of-date", as_of_date, "--repo-root", str(repo)],
                )
                if _attempt_is_external_wait(profile_attempt):
                    result = snapshot(
                        pending_reason="PHASE105_ISSUER_PROFILE_COLLABORATION_PENDING"
                    )
                    if checkpoint_writer is not None:
                        checkpoint_writer(result)
                    return result
                if (
                    profile_attempt["exit_code"] != 0
                    or not _phase105_profile_ready(issuer_profile_path, as_of_date)
                ):
                    result = snapshot(
                        pending_reason="PHASE105_ISSUER_PROFILE_PENDING"
                    )
                    if checkpoint_writer is not None:
                        checkpoint_writer(result)
                    return result
            profiled_attempt = invoke(
                "cross_archetype_canary_selection",
                "e2r.cli.select_e2r_v6_cross_archetype_canaries",
                [
                    "--as-of-date",
                    as_of_date,
                    "--repo-root",
                    str(repo),
                    "--issuer-profile-manifest",
                    str(issuer_profile_path),
                ],
            )
            if (
                profiled_attempt["exit_code"] != 0
                or not _phase105_selection_ready(
                    selection_path,
                    as_of_date,
                    issuer_profile_path=issuer_profile_path,
                )
            ):
                result = snapshot(pending_reason="PHASE105_SELECTION_PENDING")
                if checkpoint_writer is not None:
                    checkpoint_writer(result)
                return result

    live_canary_root = final / "current_live_canaries"
    if _phase106_canaries_ready(
        repo,
        final,
        selection_path,
        issuer_profile_path=issuer_profile_path,
    ):
        skip("current_live_canary_runs", {"live_tree_hash": _tree_hash(tuple(live_canary_root.rglob("*")))})
    else:
        attempt = invoke(
            "current_live_canary_runs",
            "e2r.cli.run_e2r_v6_current_live_canaries_until_pass",
            [
                "--repo-root", str(repo),
                "--live-materialization-authorized", "true",
                "--checkpoint-resume", "true",
                "--research-provider", "codex-collaboration",
                "--fact-documents-per-call", "1",
                "--work-root", str(output / "phase106"),
            ],
        )
        if _attempt_is_external_wait(attempt):
            result = snapshot(
                pending_reason="PHASE106_LIVE_CANARY_COLLABORATION_PENDING"
            )
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result
        if attempt["exit_code"] != 0 or not _phase106_canaries_ready(
            repo,
            final,
            selection_path,
            issuer_profile_path=issuer_profile_path,
        ):
            result = snapshot(pending_reason="PHASE106_LIVE_CANARY_PENDING")
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result

    if _phase107_census_ready(final):
        skip("current_krx_census", _safe_json(final / "current_krx_census_summary.json"))
    else:
        census_output = output / "current_krx_census_run"
        attempt = invoke(
            "current_krx_census",
            "e2r.cli.run_e2r_census_mode",
            [
                "--as-of-date", as_of_date,
                "--mode", "census_selective_deep",
                "--brain", "canonical_v1",
                "--universe", "krx",
                "--output-root", str(census_output),
                "--fail-on-critical", "true",
                "--materialize-live-input", "true",
                "--live-materialization-authorized", "true",
                "--run-profile", str(profile),
                "--resume", "true",
            ],
        )
        live_root = repo / "output" / "live_materialization" / as_of_date
        if _attempt_is_external_wait(attempt):
            reason = "PHASE107_SOURCE_OR_PROVIDER_PENDING"
            result = snapshot(pending_reason=reason)
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result
        if (
            attempt["exit_code"] != 0
            and (
                not live_root.is_dir()
                or live_root.is_symlink()
            )
        ):
            result = snapshot(pending_reason="PHASE107_CENSUS_PENDING")
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result
        if not _phase107_census_ready(final):
            deep_receipts = census_output / "deep_receipts"
            if not live_root.is_dir() or live_root.is_symlink():
                result = snapshot(pending_reason="PHASE107_SOURCE_OR_PROVIDER_PENDING")
                if checkpoint_writer is not None:
                    checkpoint_writer(result)
                return result
            if not _phase107_deep_receipts_ready(
                repo=repo,
                live_root=live_root,
                deep_receipts=deep_receipts,
                as_of_date=as_of_date,
            ):
                deep_attempt = invoke(
                    "current_krx_natural_deep_receipt",
                    "e2r.cli.run_e2r_v6_current_krx_deep_receipts_until_pass",
                    [
                        "--as-of-date", as_of_date,
                        "--repo-root", str(repo),
                        "--live-root", str(live_root),
                        "--work-root", str(output / "phase107"),
                        "--deep-receipt-root", str(deep_receipts),
                        "--live-materialization-authorized", "true",
                        "--checkpoint-resume", "true",
                        "--research-provider", "codex-collaboration",
                        "--fact-documents-per-call", "1",
                    ],
                )
                if "COLLABORATION_RESPONSE_PENDING" in tuple(
                    deep_attempt.get("pending_markers") or ()
                ):
                    result = snapshot(
                        pending_reason=(
                            "PHASE107_DEEP_RECEIPT_COLLABORATION_PENDING"
                        )
                    )
                    if checkpoint_writer is not None:
                        checkpoint_writer(result)
                    return result
                if _attempt_is_external_wait(deep_attempt):
                    result = snapshot(
                        pending_reason="PHASE107_SOURCE_OR_PROVIDER_PENDING"
                    )
                    if checkpoint_writer is not None:
                        checkpoint_writer(result)
                    return result
                if (
                    deep_attempt["exit_code"] != 0
                    or not _phase107_deep_receipts_ready(
                        repo=repo,
                        live_root=live_root,
                        deep_receipts=deep_receipts,
                        as_of_date=as_of_date,
                    )
                ):
                    result = snapshot(
                        pending_reason="PHASE107_DEEP_RECEIPT_PENDING"
                    )
                    if checkpoint_writer is not None:
                        checkpoint_writer(result)
                    return result
            compile_attempt = invoke(
                "current_krx_census_publish",
                "e2r.cli.compile_e2r_v6_current_krx_census",
                [
                    "--as-of-date", as_of_date,
                    "--repo-root", str(repo),
                    "--live-root", str(live_root),
                    "--deep-receipt-root", str(deep_receipts),
                    "--check-only", "false",
                ],
            )
            if compile_attempt["exit_code"] != 0 or not _phase107_census_ready(final):
                result = snapshot(pending_reason="PHASE107_CENSUS_PUBLISH_PENDING")
                if checkpoint_writer is not None:
                    checkpoint_writer(result)
                return result

    if _phase101_receipts_ready(receipt_root):
        skip("tracked_receipt_export", {"receipt_root_hash": stable_hash(str(receipt_root))})
    else:
        attempt = invoke(
            "tracked_receipt_export",
            "e2r.cli.export_e2r_v6_tracked_receipts",
            [
                "--repo-root", str(repo),
                "--source-output-root", str(repo / "output" / "researcher_mode" / "c06" / CANARY_RECEIPT_DATE),
                "--targets", ",".join(PHASE101_TARGET_IDS),
                "--destination", str(receipt_root),
            ],
        )
        if attempt["exit_code"] != 0 or not _phase101_receipts_ready(receipt_root):
            result = snapshot(pending_reason="PHASE101_TRACKED_RECEIPT_EXPORT_PENDING")
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result

    static_audit_path = final / PRODUCTION_STATIC_AUDIT_LEAF
    if _phase108_static_audit_ready(repo, static_audit_path):
        skip("production_static_audit", _safe_json(static_audit_path))
    else:
        static_attempt = invoke(
            "production_static_audit",
            "e2r.cli.compile_e2r_v6_production_static_audit",
            [
                "--repo-root",
                str(repo),
                "--final-root",
                str(FINAL_ROOT_RELATIVE),
            ],
        )
        if (
            static_attempt["exit_code"] != 0
            or not _phase108_static_audit_ready(repo, static_audit_path)
        ):
            result = snapshot(pending_reason="PHASE108_PRODUCTION_STATIC_AUDIT_PENDING")
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result

    phase102_ready = _phase102_reproduction_ready(final)
    phase103_ready = _phase103_clean_clone_ready(final)
    if not phase102_ready or not phase103_ready:
        clean_clone_attempt = invoke_argv(
            "clean_clone_reproduction",
            [
                "/usr/bin/python3",
                "-I",
                "-S",
                "-B",
                str(repo / "scripts/run_e2r_v6_clean_clone_reproduction.py"),
                "--repo-root",
                str(repo),
            ],
        )
        phase102_ready = _phase102_reproduction_ready(final)
        phase103_ready = _phase103_clean_clone_ready(final)
        if (
            clean_clone_attempt["exit_code"] != 0
            or not phase102_ready
            or not phase103_ready
        ):
            result = snapshot(
                pending_reason="PHASE102_103_CLEAN_CLONE_REPRODUCTION_PENDING"
            )
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result
    skip("clean_clone_verification", _safe_json(final / "clean_clone_reproduction.json"))

    self_repair_path = final / SELF_REPAIR_AUDIT_LEAF
    if _phase108_self_repair_ready(repo, final, self_repair_path):
        skip("operational_self_repair", _safe_json(self_repair_path))
    else:
        repair_attempt = invoke(
            "operational_self_repair",
            "e2r.cli.compile_e2r_v6_operational_self_repair",
            [
                "--repo-root",
                str(repo),
                "--final-root",
                str(FINAL_ROOT_RELATIVE),
            ],
        )
        if (
            repair_attempt["exit_code"] != 0
            or not _phase108_self_repair_ready(repo, final, self_repair_path)
        ):
            result = snapshot(pending_reason="PHASE108_OPERATIONAL_SELF_REPAIR_PENDING")
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result

    if not _phase104_lifecycle_ready(final):
        provider_audit_path = final / "provider_runtime_audit.json"
        if not _phase104_provider_audit_ready(provider_audit_path, as_of_date):
            provider_attempt = invoke(
                "provider_runtime_audit",
                "e2r.cli.compile_e2r_v6_provider_runtime_audit",
                [
                    "--repo-root",
                    str(repo),
                    "--final-root",
                    str(FINAL_ROOT_RELATIVE),
                ],
            )
            if (
                provider_attempt["exit_code"] != 0
                or not _phase104_provider_audit_ready(
                    provider_audit_path,
                    as_of_date,
                )
            ):
                result = snapshot(
                    pending_reason="PHASE104_PROVIDER_RUNTIME_AUDIT_PENDING"
                )
                if checkpoint_writer is not None:
                    checkpoint_writer(result)
                return result
        manifest = final / "artifact_lifecycle_manifest.json"
        if not manifest.is_file() or manifest.is_symlink():
            result = snapshot(pending_reason="PHASE104_LIFECYCLE_MANIFEST_PENDING")
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result
        attempt = invoke(
            "artifact_lifecycle",
            "e2r.cli.compile_e2r_v6_artifact_lifecycle",
            [
                "--manifest", str(manifest),
                "--repo-root", str(repo),
                "--final-root", str(FINAL_ROOT_RELATIVE),
                "--output", str(final / "artifact_lifecycle_audit.json"),
            ],
        )
        if attempt["exit_code"] != 0 or not _phase104_lifecycle_ready(final):
            result = snapshot(pending_reason="PHASE104_LIFECYCLE_PENDING")
            if checkpoint_writer is not None:
                checkpoint_writer(result)
            return result
    else:
        skip("artifact_lifecycle", _safe_json(final / "artifact_lifecycle_audit.json"))

    acceptance = compiler(
        repo_root=repo,
        final_root=FINAL_ROOT_RELATIVE,
        test_mode=test_mode,
    )
    gate = acceptance.get("reviewer_gate") or {}
    steps.append(
        _driver_step(
            "reviewer_gate",
            "VALIDATED_CHECKPOINT" if gate.get("status") == REVIEWER_GATE_PASS else "CHECKPOINT_PENDING",
            "LEAF_RECOMPUTED",
            gate,
        )
    )
    tests = acceptance.get("full_test_result") or {}
    steps.append(
        _driver_step(
            "full_tests",
            "VALIDATED_CHECKPOINT" if tests.get("status") == "PASS" else "CHECKPOINT_PENDING",
            "EXECUTED_AFTER_ALL_LEAVES_READY",
            tests,
        )
    )
    result = snapshot(acceptance=acceptance)
    if checkpoint_writer is not None:
        checkpoint_writer(result)
    return result


def compile_operational_acceptance(
    *,
    repo_root: str | Path = ".",
    final_root: str | Path = FINAL_ROOT_RELATIVE,
    receipt_verifier: ReceiptRootVerifier = verify_receipts,
    repository_probe: RepositoryProbe | None = None,
    test_runner: TestRunner | None = None,
    static_audit_compiler: StaticAuditCompiler = compile_production_static_audit,
    test_mode: bool = False,
    terminal_publication_verified_head: str | None = None,
) -> Mapping[str, Any]:
    """Recompute Phase 101--108 evidence and independent reviewers K--V.

    Dependency injection is a contract-test facility only.  Production always
    uses the canonical receipt verifier, Git probe, and full unittest command.
    """

    if not isinstance(test_mode, bool):
        raise TypeError("test_mode must be boolean")
    if terminal_publication_verified_head is not None and re.fullmatch(
        r"[0-9a-f]{40}", terminal_publication_verified_head
    ) is None:
        raise ValueError("terminal publication verified HEAD must be a Git SHA")
    custom = (
        receipt_verifier is not verify_receipts
        or repository_probe is not None
        or test_runner is not None
        or static_audit_compiler is not compile_production_static_audit
    )
    if custom and not test_mode:
        raise ValueError("production operational acceptance cannot replace verifiers")
    repo = Path(repo_root).resolve()
    requested_final = Path(final_root)
    canonical_final = (repo / FINAL_ROOT_RELATIVE).resolve()
    resolved_final = (
        requested_final.resolve()
        if requested_final.is_absolute()
        else (repo / requested_final).resolve()
    )
    canonical_path = resolved_final == canonical_final
    final = resolved_final

    phase_presence = _phase_presence(final)
    phase_missing_count = sum(not row["complete"] for row in phase_presence.values())
    receipt_root = final / "canary_receipts" / CANARY_RECEIPT_DATE
    receipt_report = receipt_verifier(receipt_root)
    selection_path = final / "cross_archetype_canary_selection.json"
    issuer_profile_path = final / ISSUER_PROFILE_MANIFEST_NAME
    try:
        selection, issuer_profile = _load_selection_and_profile(
            selection_path,
            issuer_profile_path=issuer_profile_path,
        )
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        # Keep the malformed leaf visible to the independent reviewers.  It is
        # evidence of failure, never a substitute for the sealed selection.
        selection = _safe_json(selection_path)
        issuer_profile = None
    canary_summary = _safe_json(final / "cross_archetype_canary_summary.json")
    canary_compilation, canary_reports, canary_paths = _current_canary_reports(
        repo=repo,
        final=final,
        selection=selection,
        issuer_business_profile_manifest=issuer_profile,
    )
    census = _safe_json(final / "current_krx_census_summary.json")
    stage_rows = _safe_jsonl(final / "current_krx_stage_map_compact.jsonl")
    lifecycle_manifest = _safe_json(final / "artifact_lifecycle_manifest.json")
    lifecycle = _safe_json(final / "artifact_lifecycle_audit.json")
    clean_clone = _safe_json(final / "clean_clone_reproduction.json")
    clean_receipts = _safe_json(final / "clean_clone/receipt_recompute_result.json")
    clean_readiness = _safe_json(final / "clean_clone/tracked_readiness_result.json")
    clean_tests = _safe_json(final / "clean_clone/test_result.json")
    provider_audit = _safe_json(final / "provider_runtime_audit.json")
    stored_static_audit = _safe_json(final / PRODUCTION_STATIC_AUDIT_LEAF)
    stored_self_repair = _safe_json(final / SELF_REPAIR_AUDIT_LEAF)
    try:
        recomputed_static_audit = dict(static_audit_compiler(repo_root=repo))
    except Exception as exc:
        recomputed_static_audit = {
            "schema_version": "STATIC_AUDIT_RECOMPUTE_ERROR",
            "status": "FAIL",
            "critical_count_sum": 1,
            "critical_counts": {},
            "error_type": type(exc).__name__,
        }
    if test_mode:
        recomputed_self_repair = dict(stored_self_repair)
    else:
        try:
            recomputed_self_repair = dict(
                compile_operational_self_repair_audit(
                    repo_root=repo,
                    final_root=final,
                )
            )
        except Exception as exc:
            recomputed_self_repair = {
                "schema_version": "SELF_REPAIR_RECOMPUTE_ERROR",
                "status": "FAIL",
                "critical_count_sum": 1,
                "error_type": type(exc).__name__,
            }
    starting_state = _safe_json(final / "starting_state.json")
    tracked_legacy_gate = _safe_json(repo / LEGACY_GATE_RELATIVE)
    # Contract fixtures may supply a compact tracked A--J packet, but a real
    # cutover must rerun all A--J detector suites and leaf checks now.  A stale
    # historical PASS file is therefore unable to authorize production.
    legacy_gate = (
        tracked_legacy_gate
        if test_mode
        else dict(compile_phase100_acceptance_bundle(repo)["reviewer_gate"])
    )
    current_tests = (test_runner or _run_full_tests)(repo)

    terminal_publications = {
        final / name for name in TERMINAL_PUBLICATION_FILES
    }
    artifact_paths = tuple(
        sorted(
            path
            for path in final.rglob("*")
            if (
                path.is_file()
                and not path.is_symlink()
                and path not in terminal_publications
            )
        )
    ) if final.is_dir() and not final.is_symlink() else ()
    provenance_paths = (*artifact_paths, repo / LEGACY_GATE_RELATIVE)
    if repository_probe is not None:
        provenance = repository_probe(repo, provenance_paths)
    elif terminal_publication_verified_head is not None:
        provenance = _terminal_publication_repository_probe(
            repo,
            provenance_paths,
            verified_head=terminal_publication_verified_head,
        )
    else:
        provenance = _production_repository_probe(repo, provenance_paths)

    provider_rows = _provider_rows(
        receipt_root,
        canary_paths,
        allow_contract_fixture_summary=test_mode,
    )
    reviewers = (
        _reviewer_k(receipt_report),
        _reviewer_l(receipt_report),
        _reviewer_m(
            clean_clone,
            clean_receipts,
            clean_readiness,
            clean_tests,
            content_hashes={
                "receipt_recompute_result_hash": _content_sha256(
                    final / "clean_clone/receipt_recompute_result.json"
                ),
                "tracked_readiness_result_hash": _content_sha256(
                    final / "clean_clone/tracked_readiness_result.json"
                ),
                "test_result_hash": _content_sha256(
                    final / "clean_clone/test_result.json"
                ),
            },
        ),
        _reviewer_n(provider_rows, provider_audit),
        _reviewer_o(lifecycle_manifest, lifecycle),
        _reviewer_p(selection, canary_summary, canary_compilation, canary_reports),
        _reviewer_q(census, stage_rows),
        _reviewer_r(census, stage_rows, provider_rows),
        _reviewer_s(census, stage_rows),
        _reviewer_t(receipt_report, canary_reports),
        _reviewer_u(
            final,
            artifact_paths,
            stored_static_audit=stored_static_audit,
            recomputed_static_audit=recomputed_static_audit,
            stored_self_repair=stored_self_repair,
            recomputed_self_repair=recomputed_self_repair,
            allow_test_mode=test_mode,
        ),
    )
    reviewer_rows = [row.to_dict() for row in reviewers]
    pre_v_critical = sum(int(row["critical_count_sum"]) for row in reviewer_rows)
    reviewer_v = _reviewer_v(
        legacy_gate=legacy_gate,
        tracked_legacy_gate=tracked_legacy_gate,
        previous_reviewers=reviewer_rows,
        current_tests=current_tests,
        starting_state=starting_state,
        provenance=provenance,
        canonical_path=canonical_path,
        phase_missing_count=phase_missing_count,
    ).to_dict()
    reviewer_rows.append(reviewer_v)
    reviewer_critical = sum(int(row["critical_count_sum"]) for row in reviewer_rows)
    roster_valid = tuple(row["reviewer_id"] for row in reviewer_rows) == REVIEWER_IDS
    critical_counts = {
        "phase101_108_missing_count": phase_missing_count,
        "canonical_final_root_mismatch_count": int(not canonical_path),
        "reviewer_roster_mismatch_count": int(not roster_valid),
        "reviewer_critical_count": reviewer_critical,
        "production_verifier_replaced_count": int(custom and not test_mode),
        "pre_v_critical_count": pre_v_critical,
    }
    critical_sum = sum(critical_counts.values())
    contract_pass = critical_sum == 0
    production_pass = contract_pass and not test_mode
    gate = {
        "schema_version": OPERATIONAL_REVIEWER_GATE_SCHEMA,
        "status": REVIEWER_GATE_PASS if contract_pass else REVIEWER_GATE_FAIL,
        "reviewer_roster": list(REVIEWER_IDS),
        "reviewers": reviewer_rows,
        "failed_reviewers": [row["reviewer_id"] for row in reviewer_rows if row["status"] != "PASS"],
        "critical_count_sum": reviewer_critical,
        "all_reviewers_leaf_recomputed": all(row["leaf_recomputed"] for row in reviewer_rows),
        "one_critical_forces_failure": True,
        "production_readiness_authority": production_pass,
    }
    orchestration_steps = [
        _step("repository_fingerprint", all(provenance.values()), provenance),
        _step("phase101_c06_receipt_verification", receipt_report.get("status") == VERIFICATION_PASS, receipt_report),
        _step("phase105_selection_checkpoint", phase_presence["105"]["complete"], selection),
        _step("phase106_current_live_canaries", canary_compilation.get("status") == CANARY_COMPILATION_PASS, canary_compilation),
        _step("phase107_current_krx_census", census.get("status") == CURRENT_KRX_CENSUS_PASS, census),
        _step(
            "phase108_production_static_audit",
            validate_production_static_audit(
                stored_static_audit,
                recomputed=recomputed_static_audit,
                allow_test_mode=test_mode,
            ),
            recomputed_static_audit,
        ),
        _step("tracked_receipt_export_checkpoint", phase_presence["101"]["complete"], {"receipt_root": receipt_root.name}),
        _step("reviewer_k_v_gate", reviewer_critical == 0, gate),
        _step("full_tests", current_tests.get("status") == "PASS", current_tests),
        _step("final_cutover_verdict", production_pass, {"production_pass": production_pass}),
    ]
    core = {
        "schema_version": OPERATIONAL_ACCEPTANCE_SCHEMA,
        "status": (
            OPERATIONAL_ACCEPTANCE_PASS
            if production_pass
            else OPERATIONAL_ACCEPTANCE_TEST_PASS
            if contract_pass and test_mode
            else OPERATIONAL_ACCEPTANCE_FAIL
        ),
        "ready": production_pass,
        "contract_test_pass": contract_pass and test_mode,
        "production_readiness_authority": production_pass,
        "phase_artifact_presence": phase_presence,
        "reviewer_gate": gate,
        "orchestration_steps": orchestration_steps,
        "full_test_result": dict(current_tests),
        "repository_provenance": dict(provenance),
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
        "blockers": sorted(
            {
                blocker
                for row in reviewer_rows
                for blocker in row.get("blockers", ())
            }
        ),
        "fixed_retry_count_is_completion_authority": False,
        "score_or_stage_authority": False,
        "investment_recommendation_emitted": False,
        "test_mode": test_mode,
    }
    return {**core, "acceptance_hash": stable_hash(core)}


def _phase_presence(final: Path) -> Mapping[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    for phase, relatives in REQUIRED_PHASE_FILES.items():
        rows = []
        for relative in relatives:
            path = final / relative
            valid = (
                path.is_dir() and not path.is_symlink()
                if relative == "current_live_canaries"
                else path.is_file() and not path.is_symlink()
            )
            rows.append({"path": relative, "present": valid})
        result[phase] = {
            "complete": all(row["present"] for row in rows),
            "artifacts": rows,
        }
    return result


def _reviewer_k(report: Mapping[str, Any]) -> OperationalReviewer:
    targets = tuple(report.get("targets") or ())
    metrics = [row.get("metrics") or {} for row in targets if isinstance(row, Mapping)]
    counts = {
        "receipt_verification_failure_count": int(report.get("status") != VERIFICATION_PASS),
        "actual_score_or_stage_missing_count": sum(
            not _finite(row.get("total_score_recomputed"))
            or not str(row.get("canonical_stage_recomputed") or "")
            for row in metrics
        ),
        "seven_component_missing_count": sum(row.get("component_count") != 7 for row in metrics),
        "score_fact_missing_count": sum(int(row.get("scoring_fact_count") or 0) <= 0 for row in metrics),
        "phase101_target_roster_mismatch_count": int(
            tuple(sorted(str(row.get("target_id") or "") for row in targets))
            != tuple(sorted(PHASE101_TARGET_IDS))
        ),
    }
    return _review("K", "Receipt Completeness", counts, {"target_count": len(targets)}, report)


def _reviewer_l(report: Mapping[str, Any]) -> OperationalReviewer:
    targets = tuple(report.get("targets") or ())
    counts = {
        "receipt_referential_verification_failure_count": int(report.get("status") != VERIFICATION_PASS),
        "orphan_or_hash_failure_count": sum(int(row.get("critical_count") or 0) for row in targets),
        "forbidden_runtime_input_count": sum(len(row.get("forbidden_runtime_inputs_read") or ()) for row in targets),
    }
    return _review("L", "Receipt Referential Integrity", counts, {"verified_target_count": len(targets)}, report)


def _reviewer_m(
    clean: Mapping[str, Any],
    receipts: Mapping[str, Any],
    readiness: Mapping[str, Any],
    tests: Mapping[str, Any],
    *,
    content_hashes: Mapping[str, str | None],
) -> OperationalReviewer:
    hashes_match = bool(
        all(
            digest is not None and clean.get(key) == digest
            for key, digest in content_hashes.items()
        )
    )
    counts = {
        "clean_clone_contract_failure_count": int(
            clean.get("schema_version") != CLEAN_CLONE_REPRODUCTION_SCHEMA
            or clean.get("status") != CLEAN_CLONE_REPRODUCTION_PASS
            or int(clean.get("critical_count_sum") or 0) != 0
        ),
        "receipt_recompute_failure_count": int(
            receipts.get("schema_version") != VERIFICATION_SCHEMA
            or receipts.get("status") != VERIFICATION_PASS
            or int(receipts.get("critical_count_sum") or 0) != 0
            or tuple(sorted(str(value) for value in receipts.get("target_ids") or ()))
            != tuple(sorted(PHASE101_TARGET_IDS))
        ),
        "tracked_readiness_failure_count": int(
            readiness.get("schema_version") != TRACKED_READINESS_SCHEMA
            or readiness.get("status") != TRACKED_READINESS_PASS
            or readiness.get("ready") is not True
            or readiness.get("offline") is not True
            or int(readiness.get("critical_count") or 0) != 0
            or readiness.get("same_receipt_replay_variance") != 0
        ),
        "clean_test_failure_count": int(
            tests.get("schema_version") != CLEAN_CLONE_TEST_SCHEMA
            or tests.get("status") != CLEAN_CLONE_TEST_PASS
            or int(tests.get("failed_test_count") or 0) != 0
            or int(tests.get("error_test_count") or 0) != 0
        ),
        "clean_clone_hash_mismatch_count": int(not hashes_match),
    }
    return _review("M", "Clean Clone Reproduction", counts, {"hashes_match": hashes_match}, clean)


def _reviewer_n(rows: Sequence[Mapping[str, Any]], audit: Mapping[str, Any]) -> OperationalReviewer:
    serialized = json.dumps(rows, ensure_ascii=False, sort_keys=True)
    successful = sum(
        str(row.get("status") or "").upper()
        in {"SUCCESS", "COMPLETE", "COMPLETED"}
        for row in rows
    )
    names = tuple(str(row.get("provider_name") or "") for row in rows)
    unauthorized = sum(not _authorized_codex_provider(name) for name in names)
    # The only operational provider family is Codex.  Therefore every
    # non-Codex row is both unauthorized and a prohibited provider-route row;
    # there is no reason to preserve executable-provider product names here.
    prohibited_route_count = unauthorized
    authority = sum(row.get("score_or_stage_authority") is not False for row in rows)
    forbidden_audit_count = sum(
        int(value)
        for key, value in audit.items()
        if (
            str(key).endswith("_call_count")
            or str(key).endswith("_scored_fact_count")
        )
        and isinstance(value, int)
        and not isinstance(value, bool)
    )
    counts = {
        "actual_provider_call_missing_count": int(not rows or successful <= 0),
        "unauthorized_provider_call_count": unauthorized,
        "local_provider_call_count": prohibited_route_count,
        "provider_score_stage_authority_count": authority,
        "provider_audit_leaf_mismatch_count": int(
            audit.get("schema_version") != PROVIDER_RUNTIME_AUDIT_SCHEMA
            or audit.get("status") != PROVIDER_RUNTIME_AUDIT_PASS
            or int(audit.get("critical_count_sum") or 0) != 0
            or forbidden_audit_count != 0
            or not isinstance(audit.get("provider_call_counts"), Mapping)
            or sum(int(value) for value in (audit.get("provider_call_counts") or {}).values()) != len(rows)
        ),
    }
    return _review("N", "Provider Honesty", counts, {"call_count": len(rows), "successful_call_count": successful}, {"rows_hash": stable_hash(rows), "audit": audit, "serialized_hash": hashlib.sha256(serialized.encode()).hexdigest()})


def _reviewer_o(manifest: Mapping[str, Any], audit: Mapping[str, Any]) -> OperationalReviewer:
    counts = {
        "lifecycle_manifest_missing_count": int(not manifest),
        "lifecycle_audit_failure_count": int(
            audit.get("schema_version") != ARTIFACT_LIFECYCLE_AUDIT_SCHEMA
            or audit.get("status") != ARTIFACT_LIFECYCLE_PASS
            or audit.get("ready") is not True
            or int(audit.get("critical_count_sum") or 0) != 0
        ),
        "lifecycle_manifest_hash_mismatch_count": int(audit.get("manifest_hash") != stable_hash(manifest)),
        "pending_after_final_count": _pending_after_final_count(manifest),
    }
    return _review("O", "Artifact Lifecycle", counts, {"artifact_count": len(manifest.get("artifacts") or ())}, audit)


def _reviewer_p(selection: Mapping[str, Any], summary: Mapping[str, Any], compilation: Mapping[str, Any], reports: Sequence[Mapping[str, Any]]) -> OperationalReviewer:
    rows = tuple(selection.get("selections") or ())
    report_by_target = {str(row.get("target_id") or ""): row for row in reports}
    selection_by_arch = {str(row.get("archetype_id") or ""): row for row in rows if isinstance(row, Mapping)}
    missing = set(REQUIRED_ARCHETYPES) - set(selection_by_arch)
    summary_rows = tuple(summary.get("canaries") or ())
    summary_by_arch = {
        str(row.get("archetype_id") or ""): row
        for row in summary_rows
        if isinstance(row, Mapping)
    }
    invalid = 0
    for archetype in REQUIRED_ARCHETYPES:
        selected = selection_by_arch.get(archetype, {})
        report = report_by_target.get(str(selected.get("target_id") or ""), {})
        metrics = report.get("metrics") or {}
        summary_row = summary_by_arch.get(archetype, {})
        invalid += int(
            report.get("status") != VERIFICATION_PASS
            or metrics.get("component_count") != 7
            or not _finite(metrics.get("total_score_recomputed"))
            or not str(metrics.get("canonical_stage_recomputed") or "")
            or summary_row.get("target_id") != selected.get("target_id")
            or not _numbers_match(
                summary_row.get("total_score"), metrics.get("total_score_recomputed")
            )
            or summary_row.get("canonical_stage")
            != metrics.get("canonical_stage_recomputed")
            or summary_row.get("score_valid") is not True
            or summary_row.get("stage_final") is not True
        )
    counts = {
        "required_archetype_missing_count": len(missing),
        "current_canary_receipt_invalid_count": invalid,
        "selection_visibility_violation_count": sum(
            row.get("final_score_visible_at_selection") is not False
            or row.get("final_stage_visible_at_selection") is not False
            or row.get("score_or_stage_authority") is not False
            for row in rows if isinstance(row, Mapping)
        ),
        "canary_summary_failure_count": int(
            compilation.get("status") != CANARY_COMPILATION_PASS
            or compilation.get("summary") != summary
            or summary.get("schema_version") != CROSS_ARCHETYPE_CANARY_SUMMARY_SCHEMA
            or summary.get("status") != CROSS_ARCHETYPE_CANARY_SUMMARY_PASS
            or int(summary.get("critical_count_sum") or 0) != 0
            or tuple(summary.get("required_archetypes") or ()) != REQUIRED_ARCHETYPES
            or int(summary.get("canary_count") or 0) != len(REQUIRED_ARCHETYPES)
            or set(summary_by_arch) != set(REQUIRED_ARCHETYPES)
        ),
    }
    return _review("P", "Cross-Archetype Generalization", counts, {"canary_count": len(reports), "archetypes": sorted(selection_by_arch)}, summary)


def _reviewer_q(census: Mapping[str, Any], rows: Sequence[Mapping[str, Any]]) -> OperationalReviewer:
    symbols = [str(row.get("symbol") or "") for row in rows]
    safe_dates = all(_date_not_after(row.get("latest_trading_snapshot_date"), census.get("assessment_as_of_date")) for row in rows)
    census_core = {key: value for key, value in census.items() if key != "summary_hash"}
    counts = {
        "census_schema_or_status_failure_count": int(
            census.get("schema_version") != CURRENT_KRX_CENSUS_SCHEMA
            or census.get("status") != CURRENT_KRX_CENSUS_PASS
            or census.get("production_runtime_ready") is not True
            or census.get("test_mode") is not False
            or int(census.get("critical_count_sum") or 0) != 0
            or census.get("summary_hash") != stable_hash(census_core)
        ),
        "real_krx_universe_missing_count": int(census.get("real_krx_universe_source") is not True),
        "universe_coverage_mismatch_count": int(int(census.get("eligible_universe_count") or 0) != len(rows) or len(rows) <= 1000),
        "stage_map_hash_mismatch_count": int(census.get("stage_map_hash") != stable_hash(tuple(rows))),
        "symbol_identity_failure_count": sum(re.fullmatch(r"[0-9A-Z]{6}", symbol) is None for symbol in symbols) + len(symbols) - len(set(symbols)),
        "future_snapshot_count": int(not safe_dates),
        "stage_row_schema_failure_count": sum(
            row.get("schema_version") != CURRENT_KRX_STAGE_ROW_SCHEMA for row in rows
        ),
        "live_input_tree_hash_missing_count": int(
            re.fullmatch(r"[0-9a-f]{64}", str(census.get("live_input_tree_hash") or ""))
            is None
        ),
    }
    return _review("Q", "Current KRX Universe", counts, {"universe_count": len(rows)}, census)


def _reviewer_r(census: Mapping[str, Any], rows: Sequence[Mapping[str, Any]], provider_rows: Sequence[Mapping[str, Any]]) -> OperationalReviewer:
    lanes = {str(lane) for row in rows for lane in row.get("trigger_lane_ids") or ()}
    non_dart = lanes - {"OFFICIAL_DISCLOSURE"}
    counts = {
        "multi_lane_trigger_shortfall_count": max(0, 3 - len(lanes)),
        "dart_only_trigger_count": int(bool(lanes) and not non_dart),
        "llm_research_route_missing_count": int(
            not any(
                _authorized_codex_provider(str(row.get("provider_name") or ""))
                for row in provider_rows
            )
        ),
        "census_trigger_summary_mismatch_count": int(int(census.get("natural_trigger_lane_count") or 0) != len(lanes)),
    }
    return _review("R", "Trigger and Routing", counts, {"trigger_lanes": sorted(lanes)}, census)


def _reviewer_s(census: Mapping[str, Any], rows: Sequence[Mapping[str, Any]]) -> OperationalReviewer:
    depth = {level: sum(row.get("maximum_depth") == level for row in rows) for level in ("L3", "L4", "L5")}
    score_rows = [row for row in rows if row.get("current_score") is not None and row.get("stage_status") == "FINAL"]
    counts = {
        "natural_candidate_missing_count": int(int(census.get("natural_candidate_count") or 0) <= 0),
        "l3_missing_count": int(depth["L3"] <= 0),
        "l4_missing_count": int(depth["L4"] <= 0),
        "l5_missing_count": int(depth["L5"] <= 0),
        "accepted_fact_missing_count": int(int(census.get("accepted_scoring_fact_count") or 0) <= 0),
        "final_score_stage_missing_count": int(not score_rows),
        "deep_receipt_lineage_missing_count": int(
            not census.get("deep_receipt_ids")
            or any(
                not str(row.get("dossier_receipt_id") or "")
                for row in score_rows
            )
        ),
    }
    return _review("S", "Census Deep Path", counts, {"depth_counts_recomputed": depth, "final_rows": len(score_rows)}, census)


def _reviewer_t(receipt_report: Mapping[str, Any], canary_reports: Sequence[Mapping[str, Any]]) -> OperationalReviewer:
    reports = tuple(receipt_report.get("targets") or ()) + tuple(canary_reports)
    counts = {
        "receipt_atomic_verification_failure_count": sum(row.get("status") != VERIFICATION_PASS for row in reports),
        "component_vector_incomplete_count": sum((row.get("metrics") or {}).get("component_count") != 7 for row in reports),
        "score_stage_recompute_missing_count": sum(not _finite((row.get("metrics") or {}).get("total_score_recomputed")) or not str((row.get("metrics") or {}).get("canonical_stage_recomputed") or "") for row in reports),
    }
    return _review("T", "Score/Stage Atomicity", counts, {"receipt_count": len(reports)}, reports)


def _reviewer_u(
    final: Path,
    paths: Sequence[Path],
    *,
    stored_static_audit: Mapping[str, Any],
    recomputed_static_audit: Mapping[str, Any],
    stored_self_repair: Mapping[str, Any],
    recomputed_self_repair: Mapping[str, Any],
    allow_test_mode: bool,
) -> OperationalReviewer:
    symlinks = tuple(path for path in final.rglob("*") if path.is_symlink()) if final.is_dir() else ()
    secret_count = 0
    absolute_count = 0
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            secret_count += 1
            continue
        without_urls = re.sub(r"https?://[^\s\"']+", "URL", text)
        absolute_count += int(bool(re.search(r"(?:^|[\s\"'=:(])/(?:root|home|tmp|mnt)/|[A-Za-z]:[\\/]", without_urls)))
        secret_count += int(bool(re.search(r'(?i)"(?:api[_-]?key|secret|access[_-]?token|password)"\s*:\s*"(?!\s*\")', text)))
    counts = {
        "symlink_count": len(symlinks),
        "secret_material_count": secret_count,
        "absolute_path_identity_count": absolute_count,
        "production_static_audit_contract_failure_count": int(
            not validate_production_static_audit(
                stored_static_audit,
                recomputed=recomputed_static_audit,
                allow_test_mode=allow_test_mode,
            )
        ),
        "production_static_audit_integrity_failure_count": sum(
            max(0, int(value))
            for key, value in (
                recomputed_static_audit.get("critical_counts") or {}
            ).items()
            if key not in STATIC_AUDIT_ZERO_COUNT_KEYS
            and isinstance(value, int)
            and not isinstance(value, bool)
        ),
        "operational_self_repair_contract_failure_count": int(
            not validate_operational_self_repair_audit(
                stored_self_repair,
                recomputed=recomputed_self_repair,
                allow_test_mode=allow_test_mode,
            )
        ),
        "operational_self_repair_unresolved_count": (
            int(recomputed_self_repair.get("critical_count_sum"))
            if isinstance(recomputed_self_repair.get("critical_count_sum"), int)
            and not isinstance(recomputed_self_repair.get("critical_count_sum"), bool)
            and int(recomputed_self_repair.get("critical_count_sum")) >= 0
            else 1
        ),
        **{
            f"recomputed_{key}": (
                int((recomputed_static_audit.get("critical_counts") or {}).get(key))
                if isinstance(
                    (recomputed_static_audit.get("critical_counts") or {}).get(key),
                    int,
                )
                and not isinstance(
                    (recomputed_static_audit.get("critical_counts") or {}).get(key),
                    bool,
                )
                and int(
                    (recomputed_static_audit.get("critical_counts") or {}).get(key)
                )
                >= 0
                else 1
            )
            for key in STATIC_AUDIT_ZERO_COUNT_KEYS
        },
    }
    return _review(
        "U",
        "Security, Portability, and Production Static Audit",
        counts,
        {
            "scanned_artifact_file_count": len(paths),
            "scanned_production_file_count": recomputed_static_audit.get(
                "scanned_file_count"
            ),
            "production_file_roster_hash": recomputed_static_audit.get(
                "file_roster_hash"
            ),
            "self_repair_iteration_count": recomputed_self_repair.get(
                "iteration_count"
            ),
        },
        {
            "tree_hash": _tree_hash(paths),
            "stored_static_audit": stored_static_audit,
            "recomputed_static_audit": recomputed_static_audit,
            "stored_self_repair": stored_self_repair,
            "recomputed_self_repair": recomputed_self_repair,
        },
    )


def _reviewer_v(*, legacy_gate: Mapping[str, Any], tracked_legacy_gate: Mapping[str, Any], previous_reviewers: Sequence[Mapping[str, Any]], current_tests: Mapping[str, Any], starting_state: Mapping[str, Any], provenance: Mapping[str, Any], canonical_path: bool, phase_missing_count: int) -> OperationalReviewer:
    legacy_reviewers = tuple(legacy_gate.get("reviewers") or ())
    declared_baseline = starting_state.get("v5_full_test_count")
    baseline = max(
        V5_FULL_TEST_COUNT_BASELINE,
        declared_baseline
        if isinstance(declared_baseline, int)
        and not isinstance(declared_baseline, bool)
        and declared_baseline > 0
        else 0,
    )
    executed = current_tests.get("executed_test_count")
    executed_is_valid = (
        isinstance(executed, int)
        and not isinstance(executed, bool)
        and executed >= 0
    )
    failed = current_tests.get("failed_test_count")
    errors = current_tests.get("error_test_count")
    counts = {
        "legacy_a_j_gate_failure_count": int(legacy_gate.get("schema_version") != LEGACY_REVIEWER_GATE_SCHEMA or legacy_gate.get("status") != LEGACY_REVIEWER_GATE_PASS or tuple(legacy_gate.get("reviewer_roster") or ()) != tuple("ABCDEFGHIJ") or any(row.get("status") != "PASS" or int(row.get("critical_count_sum") or 0) != 0 or int(row.get("detector_run_count") or 0) <= 0 or row.get("detector_pass_count") != row.get("detector_run_count") for row in legacy_reviewers)),
        "tracked_legacy_gate_stale_count": int(
            not tracked_legacy_gate
            or stable_hash(tracked_legacy_gate) != stable_hash(legacy_gate)
        ),
        "reviewer_k_u_failure_count": sum(row.get("status") != "PASS" for row in previous_reviewers),
        "full_test_failure_count": int(
            current_tests.get("status") != "PASS"
            or not executed_is_valid
            or int(executed) < baseline
            or isinstance(failed, bool)
            or not isinstance(failed, int)
            or failed != 0
            or isinstance(errors, bool)
            or not isinstance(errors, int)
            or errors != 0
        ),
        "repository_provenance_failure_count": int(not all(provenance.get(key) is True for key in ("canonical_repository", "origin_main_matches_head", "worktree_clean", "all_acceptance_artifacts_tracked_at_head"))),
        "canonical_final_root_failure_count": int(not canonical_path),
        "phase101_108_missing_count": phase_missing_count,
    }
    return _review(
        "V",
        "Final Operational Cutover",
        counts,
        {
            "legacy_reviewer_count": len(legacy_reviewers),
            "current_test_count": executed,
            "full_test_count_baseline": baseline,
            "full_test_count_delta": (
                int(executed) - baseline if executed_is_valid else None
            ),
        },
        {
            "legacy_gate": legacy_gate,
            "tracked_legacy_gate": tracked_legacy_gate,
            "tests": current_tests,
            "starting_state": starting_state,
            "provenance": provenance,
        },
    )


def _review(reviewer_id: str, title: str, counts: Mapping[str, int], metrics: Mapping[str, Any], evidence: Any) -> OperationalReviewer:
    blockers = tuple(key for key, value in counts.items() if int(value) > 0)
    return OperationalReviewer(reviewer_id, title, counts, metrics, {"leaf_evidence_hash": stable_hash(evidence)}, blockers)


def _step(step_id: str, passed: bool, evidence: Any) -> Mapping[str, Any]:
    return {
        "step_id": step_id,
        "status": "VALIDATED_CHECKPOINT" if passed else "CHECKPOINT_PENDING",
        "evidence_hash": stable_hash(evidence),
        "caller_attestation_trusted": False,
    }


def _current_canary_reports(
    *,
    repo: Path,
    final: Path,
    selection: Mapping[str, Any],
    issuer_business_profile_manifest: Mapping[str, Any] | None,
) -> tuple[Mapping[str, Any], tuple[Mapping[str, Any], ...], tuple[Path, ...]]:
    root = final / "current_live_canaries"
    try:
        compilation = compile_cross_archetype_canary_directory(
            selection=selection,
            live_root=root,
            repo_root=repo,
            issuer_business_profile_manifest=(
                issuer_business_profile_manifest
            ),
        )
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        compilation = {"status": "FAIL", "failures": [{"detail": str(exc)}]}
    summary = compilation.get("summary")
    summary_rows = tuple(summary.get("canaries") or ()) if isinstance(summary, Mapping) else ()
    reports = tuple(
        {
            "target_id": row.get("target_id"),
            "status": VERIFICATION_PASS,
            "critical_count": 0,
            "metrics": {
                "total_score_recomputed": row.get("total_score"),
                "canonical_stage_recomputed": row.get("canonical_stage"),
                "component_count": len(row.get("component_score_vector") or {}),
            },
        }
        for row in summary_rows
        if isinstance(row, Mapping)
    )
    paths = tuple(
        sorted(
            (path for path in root.iterdir() if path.is_dir() and not path.is_symlink()),
            key=lambda path: path.name,
        )
    ) if root.is_dir() and not root.is_symlink() else ()
    return dict(compilation), reports, paths


def _provider_rows(
    receipt_root: Path,
    canary_paths: Sequence[Path],
    *,
    allow_contract_fixture_summary: bool = False,
) -> tuple[Mapping[str, Any], ...]:
    rows: list[Mapping[str, Any]] = []
    phase101_roots = [receipt_root / target for target in PHASE101_TARGET_IDS]
    for root in phase101_roots:
        rows.extend(_safe_jsonl(root / "provider_calls.jsonl"))
    for root in canary_paths:
        leaf_rows = _safe_jsonl(root / "provider_calls.jsonl")
        rows.extend(leaf_rows)
        if not leaf_rows and allow_contract_fixture_summary:
            # Old bounded contract fixtures predate the strong eight-artifact
            # bundle.  They may exercise reviewer orchestration in test mode,
            # but this summary fallback is unreachable for production PASS.
            result = _safe_json(root / CANARY_RESULT_NAME)
            for provider_name, count in (
                result.get("provider_call_counts") or {}
            ).items():
                rows.extend(
                    {
                        "provider_name": str(provider_name),
                        "status": "COMPLETED",
                        "score_or_stage_authority": False,
                    }
                    for _ in range(int(count))
                )
    return tuple(rows)


def _production_repository_probe(repo: Path, paths: Sequence[Path]) -> Mapping[str, Any]:
    canonical = repo == canonical_repository_root() and _repository_identity_is_trusted(repo)
    tracked = canonical and all(_tracked_at_head(repo, path) for path in paths)
    return {
        "canonical_repository": canonical,
        "origin_main_matches_head": canonical,
        "worktree_clean": canonical,
        "all_acceptance_artifacts_tracked_at_head": tracked,
    }


def _terminal_publication_repository_probe(
    repo: Path,
    paths: Sequence[Path],
    *,
    verified_head: str,
) -> Mapping[str, Any]:
    """Trust either result-last worktree leaves or their exact final commit.

    Phase109 necessarily makes the worktree dirty when it writes its two
    terminal leaves.  They are deliberately excluded from Phase104 and
    Reviewer K--V inputs, so post-publication verification may ignore exactly
    those two unstaged paths while every underlying acceptance leaf still
    equals ``verified_head``.  After commit/push, one clean first-parent child
    of ``verified_head`` is also accepted, but only when that commit changes
    exactly the two terminal leaves and current HEAD equals ``origin/main``.
    """

    allowed = {
        (FINAL_ROOT_RELATIVE / name).as_posix()
        for name in TERMINAL_PUBLICATION_FILES
    }
    try:
        top = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], cwd=repo, text=True
        ).strip()
        head = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=repo, text=True
        ).strip()
        remote_main = subprocess.check_output(
            ["git", "rev-parse", "refs/remotes/origin/main"],
            cwd=repo,
            text=True,
        ).strip()
        raw_status = subprocess.check_output(
            ["git", "status", "--porcelain=v1", "-z", "--untracked-files=all"],
            cwd=repo,
        )
    except (OSError, subprocess.CalledProcessError):
        top = ""
        head = ""
        remote_main = ""
        raw_status = b"INVALID\0"
    try:
        first_parent = subprocess.check_output(
            ["git", "rev-parse", "HEAD^"],
            cwd=repo,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
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
            value.decode("utf-8")
            for value in raw_commit_paths.split(b"\0")
            if value
        }
    except (OSError, UnicodeDecodeError, subprocess.CalledProcessError):
        first_parent = ""
        commit_paths = set()
    status_valid = True
    seen: set[str] = set()
    for encoded in raw_status.split(b"\0"):
        if not encoded:
            continue
        try:
            entry = encoded.decode("utf-8")
        except UnicodeDecodeError:
            status_valid = False
            continue
        if len(entry) < 4:
            status_valid = False
            continue
        code = entry[:2]
        relative = entry[3:]
        if (
            code not in {"??", " M"}
            or relative not in allowed
            or relative in seen
        ):
            status_valid = False
        seen.add(relative)
    terminal_leaves_safe = all(
        (repo / relative).is_file() and not (repo / relative).is_symlink()
        for relative in allowed
    )
    result_last_worktree = bool(
        head == verified_head
        and remote_main == verified_head
        and status_valid
        and seen.issubset(allowed)
    )
    exact_terminal_commit = bool(
        head != verified_head
        and remote_main == head
        and first_parent == verified_head
        and raw_status == b""
        and commit_paths == allowed
    )
    canonical = bool(
        repo == canonical_repository_root()
        and Path(top).resolve() == repo
        and (result_last_worktree or exact_terminal_commit)
        and terminal_leaves_safe
    )
    tracked = canonical and all(_tracked_at_head(repo, path) for path in paths)
    return {
        "canonical_repository": canonical,
        "origin_main_matches_head": canonical,
        "worktree_clean": canonical,
        "all_acceptance_artifacts_tracked_at_head": tracked,
    }


def _tracked_at_head(repo: Path, path: Path) -> bool:
    try:
        relative = path.resolve().relative_to(repo).as_posix()
        head = subprocess.check_output(["git", "rev-parse", f"HEAD:{relative}"], cwd=repo, text=True, stderr=subprocess.DEVNULL).strip()
        index = subprocess.check_output(["git", "ls-files", "-s", "--", relative], cwd=repo, text=True, stderr=subprocess.DEVNULL).split()
        worktree = subprocess.check_output(["git", "hash-object", "--", relative], cwd=repo, text=True, stderr=subprocess.DEVNULL).strip()
    except (OSError, ValueError, subprocess.CalledProcessError):
        return False
    return len(index) >= 2 and head == index[1] == worktree


def _run_full_tests(repo: Path) -> Mapping[str, Any]:
    completed = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], cwd=repo, env={**__import__("os").environ, "PYTHONPATH": "src"}, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    output = completed.stdout
    matches = re.findall(r"^Ran\s+(\d+)\s+tests?", output, re.M)
    executed = int(matches[-1]) if matches else 0
    passed = completed.returncode == 0 and bool(re.search(r"^OK(?:\s|$)", output, re.M))
    result_core = {
        "status": "PASS" if passed else "FAIL",
        "executed_test_count": executed,
        "failed_test_count": 0 if passed else 1,
        "error_test_count": 0,
        "exit_code": completed.returncode,
        "output_hash_scope": "DETERMINISTIC_TEST_RESULT_FIELDS",
    }
    # Wall-clock duration in unittest's console footer is nondeterministic.
    # Hash the leaf result fields so an identical suite replay has an identical
    # acceptance hash while any count/status/exit-code change still diverges.
    return {**result_core, "output_hash": stable_hash(result_core)}


def _safe_json(path: Path) -> Mapping[str, Any]:
    if path.is_symlink() or not path.is_file():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return dict(value) if isinstance(value, Mapping) else {}


def _safe_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if path.is_symlink() or not path.is_file():
        return ()
    try:
        rows = tuple(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
    except (OSError, UnicodeError, json.JSONDecodeError):
        return ()
    return tuple(dict(row) for row in rows if isinstance(row, Mapping)) if all(isinstance(row, Mapping) for row in rows) else ()


def _content_sha256(path: Path) -> str | None:
    if path.is_symlink() or not path.is_file():
        return None
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def _pending_after_final_count(manifest: Mapping[str, Any]) -> int:
    projection = manifest.get("status_projection") or {}
    final = projection.get("score_valid") is True and projection.get("stage_final") is True
    return int(final and "PENDING" in json.dumps(manifest, ensure_ascii=False).upper())


def _finite(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def _numbers_match(left: Any, right: Any) -> bool:
    return _finite(left) and _finite(right) and abs(float(left) - float(right)) <= 1e-9


def _authorized_codex_provider(value: str) -> bool:
    """Accept only the exact portable provider identities used by receipts."""

    return value.strip().upper() in {
        "CODEX",
        "COLLABORATION_CODEX",
        "COLLABORATION_CODEX_SUBAGENT",
        "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE",
    }


def _date_not_after(value: Any, upper: Any) -> bool:
    try:
        return date.fromisoformat(str(value)) <= date.fromisoformat(str(upper))
    except ValueError:
        return False


def _tree_hash(paths: Sequence[Path]) -> str:
    return stable_hash([{"path": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path in sorted(paths) if path.is_file()])


def _resolve_canonical_final(repo: Path, final_root: str | Path) -> Path:
    requested = Path(final_root)
    resolved = requested.resolve() if requested.is_absolute() else (repo / requested).resolve()
    canonical = (repo / FINAL_ROOT_RELATIVE).resolve()
    if resolved != canonical:
        raise ValueError("operational phase driver requires the canonical final root")
    return resolved


def _run_phase_subprocess(
    argv: Sequence[str],
    cwd: Path,
) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    source = str(cwd / "src")
    env["PYTHONPATH"] = (
        source
        if not env.get("PYTHONPATH")
        else source + os.pathsep + str(env["PYTHONPATH"])
    )
    return subprocess.run(
        list(argv),
        cwd=cwd,
        env=env,
        shell=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def _command_attempt(
    *,
    step_id: str,
    argv: Sequence[str],
    completed: subprocess.CompletedProcess[str],
) -> Mapping[str, Any]:
    stdout = completed.stdout or ""
    stderr = completed.stderr or ""
    semantic_status = _stdout_semantic_status(stdout)
    combined = (stdout + "\n" + stderr).upper()
    pending_markers = tuple(
        marker
        for marker in (
            "COLLABORATION_RESPONSE_PENDING",
            "SOURCE_PENDING",
            "PROVIDER_PENDING",
            "PROVIDER_ERROR",
            "EXTERNAL_SOURCE_BLOCKER",
        )
        if marker in combined
    )
    return {
        "step_id": step_id,
        "argv": list(argv),
        "shell": False,
        "exit_code": int(completed.returncode),
        "semantic_status": semantic_status,
        "stdout_sha256": hashlib.sha256(stdout.encode("utf-8")).hexdigest(),
        "stderr_sha256": hashlib.sha256(stderr.encode("utf-8")).hexdigest(),
        "pending_markers": list(pending_markers),
        "fixed_retry_count_is_completion_authority": False,
        "score_or_stage_authority": False,
    }


def _stdout_semantic_status(stdout: str) -> str | None:
    try:
        payload = json.loads(stdout)
    except (TypeError, json.JSONDecodeError):
        return None
    if not isinstance(payload, Mapping):
        return None
    direct = payload.get("status") or payload.get("command_status")
    if direct:
        return str(direct)
    verification = payload.get("verification")
    if isinstance(verification, Mapping) and verification.get("status"):
        return str(verification["status"])
    return None


def _attempt_is_external_wait(attempt: Mapping[str, Any]) -> bool:
    return bool(attempt.get("pending_markers"))


def _driver_step(
    step_id: str,
    status: str,
    action: str,
    evidence: Any,
) -> Mapping[str, Any]:
    return {
        "step_id": step_id,
        "status": status,
        "action": action,
        "evidence_hash": stable_hash(evidence),
        "score_or_stage_authority": False,
        "caller_attestation_trusted": False,
    }


def _current_operational_fingerprint(
    repo: Path,
    run_profile: Path,
    research_provider: str,
) -> Mapping[str, Any]:
    try:
        head = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        ).stdout.strip()
        dirty = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=repo,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        ).stdout
    except OSError:
        head = ""
        dirty = ""
    config_paths = (
        repo / "configs" / "e2r_live_materialization_v1.json",
        run_profile,
    )
    config_rows = [
        {
            "path": path.relative_to(repo).as_posix()
            if path == repo or repo in path.parents
            else path.name,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()
            if path.is_file() and not path.is_symlink()
            else None,
        }
        for path in config_paths
    ]
    return {
        "head": head or None,
        "dirty_status_hash": hashlib.sha256(dirty.encode("utf-8")).hexdigest(),
        "repo_dirty": bool(dirty),
        "config_hash": stable_hash(config_rows),
        "provider_route": research_provider,
        "provider_hash": stable_hash(
            {
                "provider_route": research_provider,
                "automatic_local_fallback": False,
                "score_or_stage_authority": False,
            }
        ),
        "automatic_local_fallback": False,
    }


def _phase101_receipts_ready(receipt_root: Path) -> bool:
    try:
        report = verify_receipts(receipt_root)
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return False
    return (
        report.get("status") == VERIFICATION_PASS
        and int(report.get("critical_count_sum") or 0) == 0
        and tuple(sorted(str(value) for value in report.get("target_ids") or ()))
        == tuple(sorted(PHASE101_TARGET_IDS))
    )


def _load_selection_and_profile(
    path: Path,
    *,
    issuer_profile_path: Path,
) -> tuple[Mapping[str, Any], Mapping[str, Any] | None]:
    header = _safe_json(path)
    if not header:
        raise ValueError("sealed Phase105 selection is missing")
    rows = tuple(
        row
        for row in header.get("selections") or ()
        if isinstance(row, Mapping)
    )
    forced = any(row.get("selection_mode") == FORCED_SELECTION for row in rows)
    profile: Mapping[str, Any] | None = None
    if forced:
        profile = load_current_issuer_business_profile_manifest(
            issuer_profile_path,
            selection_as_of_date=str(header.get("selection_as_of_date") or ""),
        )
    selection = load_sealed_cross_archetype_canary_selection(
        path,
        issuer_business_profile_manifest=profile,
    )
    return selection, profile


def _phase105_selection_ready(
    path: Path,
    as_of_date: str,
    *,
    issuer_profile_path: Path | None = None,
) -> bool:
    try:
        selection, _profile = _load_selection_and_profile(
            path,
            issuer_profile_path=(
                issuer_profile_path
                or path.parent / ISSUER_PROFILE_MANIFEST_NAME
            ),
        )
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return False
    return str(selection.get("selection_as_of_date") or "") == as_of_date


def _phase105_profile_ready(path: Path, as_of_date: str) -> bool:
    try:
        profile = load_current_issuer_business_profile_manifest(
            path,
            selection_as_of_date=as_of_date,
        )
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return False
    return (
        str(profile.get("as_of_date") or "") == as_of_date
        and len(tuple(profile.get("profiles") or ())) == len(REQUIRED_ARCHETYPES)
    )


def _phase106_canaries_ready(
    repo: Path,
    final: Path,
    selection_path: Path,
    *,
    issuer_profile_path: Path | None = None,
) -> bool:
    summary_path = final / "cross_archetype_canary_summary.json"
    if not summary_path.is_file() or summary_path.is_symlink():
        return False
    try:
        selection, profile = _load_selection_and_profile(
            selection_path,
            issuer_profile_path=(
                issuer_profile_path
                or final / ISSUER_PROFILE_MANIFEST_NAME
            ),
        )
        compilation = compile_cross_archetype_canary_directory(
            selection=selection,
            live_root=final / "current_live_canaries",
            repo_root=repo,
            issuer_business_profile_manifest=profile,
        )
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return False
    return (
        compilation.get("status") == CANARY_COMPILATION_PASS
        and compilation.get("summary") == _safe_json(summary_path)
    )


def _phase107_census_ready(final: Path) -> bool:
    summary = _safe_json(final / "current_krx_census_summary.json")
    rows = _safe_jsonl(final / "current_krx_stage_map_compact.jsonl")
    core = {key: value for key, value in summary.items() if key != "summary_hash"}
    return bool(rows) and (
        summary.get("schema_version") == CURRENT_KRX_CENSUS_SCHEMA
        and summary.get("status") == CURRENT_KRX_CENSUS_PASS
        and summary.get("production_runtime_ready") is True
        and summary.get("test_mode") is False
        and int(summary.get("critical_count_sum") or 0) == 0
        and summary.get("summary_hash") == stable_hash(core)
        and summary.get("stage_map_hash") == stable_hash(tuple(rows))
        and all(row.get("schema_version") == CURRENT_KRX_STAGE_ROW_SCHEMA for row in rows)
    )


def _phase107_deep_receipts_ready(
    *,
    repo: Path,
    live_root: Path,
    deep_receipts: Path,
    as_of_date: str,
) -> bool:
    try:
        report = validate_current_krx_deep_receipt_root(
            live_root=live_root,
            deep_receipt_root=deep_receipts,
            as_of_date=as_of_date,
            repo_root=repo,
        )
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return False
    return bool(
        report.get("status") == VERIFICATION_PASS
        and int(report.get("critical_count") or 0) == 0
    )


def _phase102_reproduction_ready(final: Path) -> bool:
    receipts = _safe_json(final / "clean_clone" / "receipt_recompute_result.json")
    readiness = _safe_json(final / "clean_clone" / "tracked_readiness_result.json")
    return (
        receipts.get("schema_version") == VERIFICATION_SCHEMA
        and receipts.get("status") == VERIFICATION_PASS
        and int(receipts.get("critical_count_sum") or 0) == 0
        and tuple(sorted(str(value) for value in receipts.get("target_ids") or ()))
        == tuple(sorted(PHASE101_TARGET_IDS))
        and readiness.get("schema_version") == TRACKED_READINESS_SCHEMA
        and readiness.get("status") == TRACKED_READINESS_PASS
        and readiness.get("ready") is True
        and readiness.get("offline") is True
        and int(readiness.get("critical_count") or 0) == 0
    )


def _phase103_clean_clone_ready(final: Path) -> bool:
    result = _safe_json(final / "clean_clone_reproduction.json")
    receipts = _safe_json(final / "clean_clone" / "receipt_recompute_result.json")
    readiness = _safe_json(final / "clean_clone" / "tracked_readiness_result.json")
    tests = _safe_json(final / "clean_clone" / "test_result.json")
    return (
        result.get("schema_version") == CLEAN_CLONE_REPRODUCTION_SCHEMA
        and result.get("status") == CLEAN_CLONE_REPRODUCTION_PASS
        and int(result.get("critical_count_sum") or 0) == 0
        and result.get("receipt_recompute_result_hash")
        == _content_sha256(final / "clean_clone/receipt_recompute_result.json")
        and result.get("tracked_readiness_result_hash")
        == _content_sha256(final / "clean_clone/tracked_readiness_result.json")
        and result.get("test_result_hash")
        == _content_sha256(final / "clean_clone/test_result.json")
        and tests.get("schema_version") == CLEAN_CLONE_TEST_SCHEMA
        and tests.get("status") == CLEAN_CLONE_TEST_PASS
        and int(tests.get("failed_test_count") or 0) == 0
        and int(tests.get("error_test_count") or 0) == 0
    )


def _phase104_lifecycle_ready(final: Path) -> bool:
    manifest = _safe_json(final / "artifact_lifecycle_manifest.json")
    audit = _safe_json(final / "artifact_lifecycle_audit.json")
    static_audit = _safe_json(final / PRODUCTION_STATIC_AUDIT_LEAF)
    return bool(manifest) and validate_production_static_audit(static_audit) and (
        audit.get("schema_version") == ARTIFACT_LIFECYCLE_AUDIT_SCHEMA
        and audit.get("status") == ARTIFACT_LIFECYCLE_PASS
        and audit.get("ready") is True
        and int(audit.get("critical_count_sum") or 0) == 0
        and audit.get("manifest_hash") == stable_hash(manifest)
    )


def _phase108_static_audit_ready(repo: Path, path: Path) -> bool:
    stored = _safe_json(path)
    try:
        recomputed = compile_production_static_audit(repo_root=repo)
    except Exception:
        return False
    return validate_production_static_audit(stored, recomputed=recomputed)


def _phase108_self_repair_ready(repo: Path, final: Path, path: Path) -> bool:
    stored = _safe_json(path)
    try:
        recomputed = compile_operational_self_repair_audit(
            repo_root=repo,
            final_root=final,
        )
    except Exception:
        return False
    return validate_operational_self_repair_audit(stored, recomputed=recomputed)


def _phase104_provider_audit_ready(path: Path, as_of_date: str) -> bool:
    audit = _safe_json(path)
    return bool(
        audit.get("schema_version") == PROVIDER_RUNTIME_AUDIT_SCHEMA
        and audit.get("status") == PROVIDER_RUNTIME_AUDIT_PASS
        and audit.get("as_of_date") == as_of_date
        and int(audit.get("critical_count_sum") or 0) == 0
        and audit.get("production_readiness_authority") is False
        and isinstance(audit.get("provider_call_counts"), Mapping)
        and sum(
            int(value)
            for value in (audit.get("provider_call_counts") or {}).values()
        )
        > 0
    )


__all__ = [
    "OPERATIONAL_ACCEPTANCE_FAIL",
    "OPERATIONAL_ACCEPTANCE_PENDING",
    "OPERATIONAL_ACCEPTANCE_PASS",
    "OPERATIONAL_ACCEPTANCE_SCHEMA",
    "OPERATIONAL_ACCEPTANCE_TEST_PASS",
    "OPERATIONAL_REVIEWER_GATE_SCHEMA",
    "REVIEWER_GATE_FAIL",
    "REVIEWER_GATE_PASS",
    "REVIEWER_IDS",
    "compile_operational_acceptance",
    "run_operational_acceptance_phases",
]
