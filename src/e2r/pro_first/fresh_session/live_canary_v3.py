"""Live initial-pass execution and efficiency gate for fresh Pro V2.1 canaries.

This module intentionally stops at the first deterministic source-verification
boundary.  A failed initial response is sealed as diagnostic-only instead of
being repaired into an operational PASS.  A passing response may continue
through the bounded same-conversation tail owned by ``FreshSessionOrchestratorV3``.
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import time
from typing import Any, Callable, Mapping, Sequence
from urllib.parse import parse_qsl, urlsplit

from e2r.research.page_fetcher import PageFetcher

from ..approval import ProApprovalService
from ..browser.completion_monitor import (
    BrowserCompletionMonitor,
    ProCompletionStateService,
)
from ..browser.protocol import BrowserResultSnapshot, BrowserUIState
from ..browser.worker import ProBrowserWorker
from ..capture.coordinator import CaptureFilesystemReconciler, ProCaptureCoordinator
from ..capture.receipt import CaptureReceipt, load_capture_receipt
from ..config import ProFirstLocalConfig
from ..dossier import CodexProReportDossierStructurer, ProDossierImporter
from ..ids import canonical_hash, canonical_json
from ..job_store import ProFirstJobStore
from ..models import JobStatus
from ..state_machine import TransitionContext
from ..multi_pass import ProMultiPassDossierStore, ProMultiPassLedger
from ..verification import (
    ACCEPTED_SOURCE_STATUSES,
    CodexMechanismScopeMapper,
    ProSourceVerificationService,
    ProSourceVerifier,
)
from .boundary import (
    FreshSessionBoundaryService,
    OldAnswerLeakageManifest,
    write_runtime_json_once,
)
from .orchestrator_v3 import FreshSessionOrchestratorV3


FRESH_LIVE_AUTHORIZATION_PHRASE = "YES-I-AUTHORIZE-FRESH-LIVE-PRO"
FRESH_INITIAL_RECEIPT_SCHEMA = "e2r_pro_fresh_initial_efficiency_receipt_v1"
ProgressHandler = Callable[[Mapping[str, Any]], None]
_FACT_COLLECTIONS = ("material_facts", "counterfacts", "resolution_facts")
_TRACKING_QUERY_KEYS = frozenset(
    {"fbclid", "gclid", "mc_cid", "mc_eid", "ref", "source"}
)


@dataclass(frozen=True)
class FreshInitialCanarySpec:
    old_job_id: str
    old_run_id: str
    old_conversation_id: str
    fresh_session_id: str
    archetype_ids: tuple[str, ...]
    old_score_values: tuple[str, ...] = ()
    old_stage_values: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        required = (
            (self.old_job_id, "old_job_id"),
            (self.old_run_id, "old_run_id"),
            (self.old_conversation_id, "old_conversation_id"),
            (self.fresh_session_id, "fresh_session_id"),
        )
        for value, label in required:
            if not str(value).strip():
                raise ValueError(f"{label} is required")
        archetypes = tuple(dict.fromkeys(str(value).strip() for value in self.archetype_ids))
        if not 1 <= len(archetypes) <= 3 or any(not value for value in archetypes):
            raise ValueError("fresh canary needs one to three archetype ids")
        object.__setattr__(self, "archetype_ids", archetypes)


@dataclass(frozen=True)
class FreshInitialEfficiencyGate:
    receipt: Mapping[str, Any]

    @property
    def passed(self) -> bool:
        return self.receipt.get("status") == "PASS"


@dataclass(frozen=True)
class FreshDetectedInitialResult:
    result: BrowserResultSnapshot
    requires_codex_structuring: bool


class FreshV3InitialLiveCanaryRunner:
    """Run exactly one fresh Initial Full Research request through verification."""

    def __init__(
        self,
        config: ProFirstLocalConfig,
        *,
        old_runtime_root: str | Path,
        fresh_runtime_root: str | Path,
        repo_root: str | Path,
        progress: ProgressHandler | None = None,
        max_completion_polls: int = 1_440,
        state_database_path: str | Path | None = None,
        store: ProFirstJobStore | None = None,
        source_verifier: ProSourceVerifier | None = None,
        report_structurer: CodexProReportDossierStructurer | None = None,
    ) -> None:
        if max_completion_polls < config.browser.required_stable_observations:
            raise ValueError("completion poll bound is smaller than the stable-result gate")
        self.config = config
        self.old_runtime_root = Path(old_runtime_root).expanduser().resolve()
        self.fresh_runtime_root = Path(fresh_runtime_root).expanduser().resolve()
        self.repo_root = Path(repo_root).expanduser().resolve()
        self.progress = progress or (lambda _payload: None)
        self.max_completion_polls = max_completion_polls
        if store is not None and state_database_path is not None:
            raise ValueError("pass either store or state_database_path, not both")
        self.state_database_path = (
            Path(state_database_path).expanduser().resolve()
            if state_database_path is not None
            else self.old_runtime_root / "pro_first.sqlite3"
        )
        self.store = store or ProFirstJobStore(self.state_database_path)
        if store is not None:
            self.state_database_path = store.database_path.expanduser().resolve()
        self.source_verifier = source_verifier or ProSourceVerifier(
            page_fetcher=PageFetcher(
                live_enabled=True,
                max_body_bytes=25_000_000,
                max_text_chars=None,
            ),
            mechanism_scope_mapper=CodexMechanismScopeMapper.default(
                working_directory=self.repo_root,
                timeout_seconds=600.0,
            ),
        )
        source_repo_root = Path(__file__).resolve().parents[4]
        self.report_structurer = report_structurer or (
            CodexProReportDossierStructurer.default(
                repo_root=source_repo_root,
                working_directory=self.repo_root,
                timeout_seconds=900.0,
            )
        )

    async def run(
        self,
        spec: FreshInitialCanarySpec,
        *,
        commit_sha: str,
        resume_prepared_job_id: str | None = None,
    ) -> Mapping[str, Any]:
        started = time.monotonic()
        manifest = build_old_answer_leakage_manifest(
            self.store,
            old_job_id=spec.old_job_id,
            old_run_id=spec.old_run_id,
            old_conversation_id=spec.old_conversation_id,
            old_job_root=self.old_runtime_root / "jobs" / spec.old_job_id,
            old_score_values=spec.old_score_values,
            old_stage_values=spec.old_stage_values,
        )
        boundary_service = FreshSessionBoundaryService(self.store)
        if resume_prepared_job_id is None:
            boundary, fresh_job = boundary_service.start(
                old_job_id=spec.old_job_id,
                old_run_id=spec.old_run_id,
                old_conversation_id=spec.old_conversation_id,
                fresh_session_id=spec.fresh_session_id,
                old_runtime_root=self.old_runtime_root,
                fresh_runtime_root=self.fresh_runtime_root,
                archetype_ids=spec.archetype_ids,
                leakage_manifest=manifest,
            )
        else:
            boundary, fresh_job = boundary_service.load_existing(
                fresh_runtime_root=self.fresh_runtime_root,
                leakage_manifest=manifest,
            )
            if (
                fresh_job.job_id != resume_prepared_job_id
                or boundary.fresh_session_id != spec.fresh_session_id
                or fresh_job.archetype_ids != spec.archetype_ids
                or fresh_job.submit_count != 0
                or fresh_job.status != JobStatus.USER_ATTENTION_REQUIRED.value
            ):
                raise ValueError(
                    "prepared-draft resume identity/state differs from the durable fresh job"
                )
        _persist_runtime_manifest(boundary.fresh_runtime_root, manifest)
        orchestrator = FreshSessionOrchestratorV3(self.store, boundary)
        built = orchestrator.build_initial_packet(
            commit_sha=commit_sha,
            config_hash=self.config.config_hash,
        )
        self._emit(
            "FRESH_PACKET_READY",
            job_id=fresh_job.job_id,
            run_id=str(built.packet_payload["run_id"]),
            initial_pass_id=built.initial_pass_id,
            prompt_char_count=len(built.prompt.prompt_text),
            leakage_count=built.packet_leakage_audit.leakage_count,
        )

        runtime = (
            await orchestrator.prepare_initial_in_logged_in_browser(
                built,
                config=self.config,
            )
            if resume_prepared_job_id is None
            else await orchestrator.recover_prepared_initial_in_logged_in_browser(
                built,
                config=self.config,
            )
        )
        try:
            self._emit(
                "FRESH_NEW_CHAT_PREPARED",
                job_id=fresh_job.job_id,
                submit_count=0,
                upload_count=0 if resume_prepared_job_id else 1,
                prepared_draft_recovered=resume_prepared_job_id is not None,
                pro_mode_ready=runtime.prepared.prepared.deep_research_ready,
            )
            approval = ProApprovalService(self.store)
            grant = approval.issue(
                fresh_job.job_id,
                prompt_hash=built.prompt.prompt_hash,
                actor="fresh-v2.1-live-authorization-recorder",
            )
            approval.approve(grant, actor="user-authorized-in-master-goal")
            submitted_at = time.monotonic()
            submitted = await orchestrator.submit_initial_once(runtime.session.adapter)
            self._emit(
                "FRESH_INITIAL_SUBMITTED",
                job_id=fresh_job.job_id,
                conversation_id=submitted.submit_result.job.conversation_id,
                submit_count=submitted.submit_result.job.submit_count,
            )
            detected = await self._wait_for_result(
                job_id=fresh_job.job_id,
                run_id=str(built.packet_payload["run_id"]),
                adapter=runtime.session.adapter,
            )
            result = detected.result
            self._rebind_completed_conversation(
                job_id=fresh_job.job_id,
                run_id=str(built.packet_payload["run_id"]),
                result=result,
            )
            dossier_override = self._structure_terminal_report_if_required(
                detected=detected,
                built=built,
                boundary=boundary,
            )
            initial_research_seconds = time.monotonic() - submitted_at
            captured_job, capture = await ProCaptureCoordinator(self.store).capture(
                fresh_job.job_id,
                run_id=str(built.packet_payload["run_id"]),
                expected_filename=built.output_filename,
                expected_report_hash=result.report_hash,
                job_root=boundary.fresh_job_root,
                adapter=runtime.session.adapter,
                capture_mode=(
                    "CHATGPT_WEB_VISIBLE_CHAT_PRO_FRESH_V3_CODEX_STRUCTURED_REPORT"
                    if dossier_override is not None
                    else "CHATGPT_WEB_VISIBLE_CHAT_PRO_FRESH_V3"
                ),
                dossier_override=dossier_override,
            )
            self._emit(
                "FRESH_INITIAL_CAPTURED",
                job_id=fresh_job.job_id,
                capture_source=capture.receipt.capture_source,
                report_hash=capture.receipt.report_md_hash,
            )
        finally:
            await runtime.close()

        return self._finish_initial_verification(
            boundary=boundary,
            orchestrator=orchestrator,
            built=built,
            fresh_job_id=captured_job.job_id,
            capture_receipt=capture.receipt,
            started=started,
            initial_research_seconds=initial_research_seconds,
        )

    async def resume_submitted(
        self,
        spec: FreshInitialCanarySpec,
        *,
        commit_sha: str,
        submitted_job_id: str,
    ) -> Mapping[str, Any]:
        """Resume one exact submitted initial request without any DOM send."""

        started = time.monotonic()
        manifest = build_old_answer_leakage_manifest(
            self.store,
            old_job_id=spec.old_job_id,
            old_run_id=spec.old_run_id,
            old_conversation_id=spec.old_conversation_id,
            old_job_root=self.old_runtime_root / "jobs" / spec.old_job_id,
            old_score_values=spec.old_score_values,
            old_stage_values=spec.old_stage_values,
        )
        boundary, fresh_job = FreshSessionBoundaryService(self.store).load_existing(
            fresh_runtime_root=self.fresh_runtime_root,
            leakage_manifest=manifest,
        )
        if (
            fresh_job.job_id != submitted_job_id
            or boundary.fresh_session_id != spec.fresh_session_id
            or fresh_job.archetype_ids != spec.archetype_ids
            or fresh_job.submit_count != 1
        ):
            raise ValueError(
                "submitted-run resume identity/state differs from the durable fresh job"
            )
        _persist_runtime_manifest(boundary.fresh_runtime_root, manifest)
        orchestrator = FreshSessionOrchestratorV3(self.store, boundary)
        built = orchestrator.build_initial_packet(
            commit_sha=commit_sha,
            config_hash=self.config.config_hash,
        )
        self._emit(
            "FRESH_SUBMITTED_RUN_RECOVERY_STARTED",
            job_id=fresh_job.job_id,
            run_id=str(built.packet_payload["run_id"]),
            submit_count=fresh_job.submit_count,
            automatic_resubmit_allowed=False,
        )

        job = self.store.get_job(fresh_job.job_id)
        capture_receipt: CaptureReceipt | None = None
        if _requires_browser_result_recovery(job):
            runtime = await ProBrowserWorker(self.config.browser).open(job_id=job.job_id)
            try:
                current_conversation = runtime.adapter.conversation_id()
                if (
                    job.conversation_id
                    and not job.conversation_id.startswith("WEB:")
                    and current_conversation != job.conversation_id
                ):
                    raise ValueError(
                        "visible ChatGPT page differs from the durable canonical conversation"
                    )
                if job.status == JobStatus.RESEARCH_RUNNING.value:
                    detected = await self._wait_for_result(
                        job_id=job.job_id,
                        run_id=str(built.packet_payload["run_id"]),
                        adapter=runtime.adapter,
                    )
                elif job.status == JobStatus.USER_ATTENTION_REQUIRED.value:
                    if job.capture_count != 0:
                        raise ValueError(
                            "pre-capture result recovery requires capture_count=0"
                        )
                    detected = await self._reverify_user_attention_result(
                        job_id=job.job_id,
                        run_id=str(built.packet_payload["run_id"]),
                        adapter=runtime.adapter,
                    )
                else:
                    result = await runtime.adapter.inspect_result(
                        job_id=job.job_id,
                        run_id=str(built.packet_payload["run_id"]),
                    )
                    if not result.structurally_complete:
                        if not _readable_terminal_report(result):
                            raise ValueError(
                                "RESULT_DETECTED recovery no longer exposes the exact completed result"
                            )
                        detected = FreshDetectedInitialResult(result, True)
                    else:
                        detected = FreshDetectedInitialResult(result, False)
                result = detected.result
                self._rebind_completed_conversation(
                    job_id=job.job_id,
                    run_id=str(built.packet_payload["run_id"]),
                    result=result,
                )
                dossier_override = self._structure_terminal_report_if_required(
                    detected=detected,
                    built=built,
                    boundary=boundary,
                )
                captured_job, capture = await ProCaptureCoordinator(self.store).capture(
                    job.job_id,
                    run_id=str(built.packet_payload["run_id"]),
                    expected_filename=built.output_filename,
                    expected_report_hash=result.report_hash,
                    job_root=boundary.fresh_job_root,
                    adapter=runtime.adapter,
                    capture_mode=(
                        "CHATGPT_WEB_VISIBLE_CHAT_PRO_FRESH_V3_RECOVERED_CODEX_STRUCTURED_NO_SUBMIT"
                        if dossier_override is not None
                        else "CHATGPT_WEB_VISIBLE_CHAT_PRO_FRESH_V3_RECOVERED_NO_SUBMIT"
                    ),
                    dossier_override=dossier_override,
                )
                capture_receipt = capture.receipt
                self._emit(
                    "FRESH_INITIAL_CAPTURED_AFTER_NO_SUBMIT_RECOVERY",
                    job_id=captured_job.job_id,
                    capture_source=capture.receipt.capture_source,
                    report_hash=capture.receipt.report_md_hash,
                    submit_count=captured_job.submit_count,
                )
            finally:
                await runtime.close()
        elif job.status == JobStatus.CAPTURING_ARTIFACTS.value:
            event = await CaptureFilesystemReconciler(self.store).reconcile(
                boundary.fresh_job_root
            )
            if event is None:
                raise ValueError(
                    "capture recovery requires the immutable READY artifact"
                )

        if capture_receipt is None:
            capture_receipt_path = (
                boundary.fresh_job_root
                / "capture/incoming/browser_capture_receipt.json"
            )
            if not capture_receipt_path.is_file():
                raise ValueError(
                    f"submitted-run recovery cannot continue from {self.store.get_job(job.job_id).status}"
                )
            capture_receipt = load_capture_receipt(capture_receipt_path)

        return self._finish_initial_verification(
            boundary=boundary,
            orchestrator=orchestrator,
            built=built,
            fresh_job_id=fresh_job.job_id,
            capture_receipt=capture_receipt,
            started=started,
            initial_research_seconds=_elapsed_since_submission(
                self.store.get_job(fresh_job.job_id).submitted_at
            ),
        )

    async def _reverify_user_attention_result(
        self,
        *,
        job_id: str,
        run_id: str,
        adapter: Any,
    ) -> FreshDetectedInitialResult:
        last_hash: str | None = None
        stable = 0
        result: BrowserResultSnapshot | None = None
        for _attempt in range(self.config.browser.required_stable_observations):
            inspection = await adapter.inspect_state()
            if inspection.stop_visible or inspection.state in {
                BrowserUIState.RESEARCH_RUNNING,
                BrowserUIState.LOGIN_REQUIRED,
                BrowserUIState.AWAITING_CLARIFICATION,
                BrowserUIState.QUOTA_PENDING,
                BrowserUIState.RETRYABLE_ERROR,
                BrowserUIState.UI_INCOMPATIBLE,
            }:
                raise ValueError(
                    "user-attention recovery does not expose a terminal readable result"
                )
            result = await adapter.inspect_result(job_id=job_id, run_id=run_id)
            if not (result.structurally_complete or _readable_terminal_report(result)):
                raise ValueError(
                    "user-attention recovery result failed exact job/run/report validation"
                )
            stable = stable + 1 if result.report_hash == last_hash else 1
            last_hash = result.report_hash
            if _attempt + 1 < self.config.browser.required_stable_observations:
                await asyncio.sleep(self.config.browser.poll_interval_seconds)
        if result is None or stable < self.config.browser.required_stable_observations:
            raise ValueError("user-attention recovery result hash was not stable")
        current = self.store.get_job(job_id)
        recovered = self.store.transition(
            job_id,
            expected_version=current.state_version,
            to_status=JobStatus.RESULT_DETECTED,
            actor="v2.1-fresh-v3-result-reverification",
            idempotency_key=f"result-reverified:{job_id}:{result.report_hash}",
            payload={
                "report_hash": result.report_hash,
                "conversation_id": result.conversation_id,
                "assistant_turn_id": result.assistant_turn_id,
                "job_marker_matches": True,
                "run_marker_matches": True,
                "stable_observations": stable,
                "automatic_resubmit_allowed": False,
            },
            context=TransitionContext(completed_result_reverified=True),
        )
        self._emit(
            "FRESH_RESULT_REVERIFIED_AFTER_USER_ATTENTION",
            job_id=recovered.job_id,
            report_hash=result.report_hash,
            stable_observations=stable,
            submit_count=recovered.submit_count,
        )
        return FreshDetectedInitialResult(
            result,
            not result.structurally_complete,
        )

    def _rebind_completed_conversation(
        self,
        *,
        job_id: str,
        run_id: str,
        result: BrowserResultSnapshot,
    ) -> None:
        job = self.store.get_job(job_id)
        canonical = str(result.conversation_id or "").strip()
        if not canonical or canonical == job.conversation_id:
            return
        if job.conversation_id and not job.conversation_id.startswith("WEB:"):
            raise ValueError("completed result changed an already canonical conversation id")
        rebound = self.store.rebind_recovered_conversation(
            job_id,
            expected_version=job.state_version,
            conversation_id=canonical,
            run_id=run_id,
            report_hash=result.report_hash,
            job_marker_matches=result.job_marker_matches,
            run_marker_matches=result.run_marker_matches,
            actor="v2.1-fresh-v3-canonical-conversation-recovery",
            idempotency_key=(
                f"fresh-v3-conversation-recovered:{job_id}:"
                f"{canonical}:{result.report_hash}"
            ),
        )
        self._emit(
            "FRESH_CANONICAL_CONVERSATION_REBOUND",
            job_id=job_id,
            prior_conversation_id=job.conversation_id,
            conversation_id=rebound.conversation_id,
            submit_count=rebound.submit_count,
        )

    def _structure_terminal_report_if_required(
        self,
        *,
        detected: FreshDetectedInitialResult,
        built: Any,
        boundary: Any,
    ) -> Mapping[str, object] | None:
        if not detected.requires_codex_structuring:
            return None
        result = detected.result
        structured = self.report_structurer.structure(
            report_text=result.report_text,
            packet=built.packet_payload,
            conversation_id=str(result.conversation_id or ""),
            research_pass_id=built.initial_pass_id,
            prompt_hash=built.prompt.prompt_hash,
            response_hash=result.report_hash,
            mandatory_question_ids=built.prompt.mandatory_question_ids,
        )
        receipt_path = (
            boundary.fresh_job_root
            / (
                "preflight/codex_report_to_dossier_v3_receipt."
                f"{result.report_hash[:24]}.json"
            )
        )
        write_runtime_json_once(receipt_path, structured.receipt)
        self._emit(
            "FRESH_TERMINAL_REPORT_STRUCTURED_BY_CODEX",
            job_id=str(built.packet_payload["job_id"]),
            report_hash=result.report_hash,
            dossier_hash=structured.receipt["dossier_hash"],
            material_fact_count=structured.receipt["material_fact_count"],
            new_research_allowed=False,
        )
        return dict(structured.dossier)

    def _finish_initial_verification(
        self,
        *,
        boundary: Any,
        orchestrator: FreshSessionOrchestratorV3,
        built: Any,
        fresh_job_id: str,
        capture_receipt: CaptureReceipt,
        started: float,
        initial_research_seconds: float,
    ) -> Mapping[str, Any]:
        imported = ProDossierImporter(self.store).import_job(
            fresh_job_id,
            job_root=boundary.fresh_job_root,
            expected_research_pass_id=built.initial_pass_id,
            expected_parent_pass_id=None,
        )
        scope = orchestrator.establish_followup_scope(
            built,
            initial_response_hash=capture_receipt.report_md_hash,
        )
        ProMultiPassDossierStore(ProMultiPassLedger(self.store)).persist(
            job_id=fresh_job_id,
            pass_id=scope.initial_pass_id,
            dossier=imported.normalized_dossier,
            job_root=boundary.fresh_job_root,
        )
        self._emit(
            "FRESH_INITIAL_DOSSIER_IMPORTED",
            job_id=fresh_job_id,
            material_candidate_count=len(
                tuple(imported.normalized_dossier.get("material_facts") or ())
            ),
            source_document_count=len(
                tuple(imported.normalized_dossier.get("source_documents") or ())
            ),
            question_family_count=len(
                tuple(imported.normalized_dossier.get("question_family_results") or ())
            ),
        )

        verification = ProSourceVerificationService(
            self.store,
            verifier=self.source_verifier,
        ).verify_job(fresh_job_id, job_root=boundary.fresh_job_root)
        verification_rows = _verification_rows(
            verification.result,
            boundary.fresh_job_root / "verification/source_verifications.jsonl",
        )
        rejection_rows = _read_jsonl(
            boundary.fresh_job_root / "verification/rejection_classifications.jsonl"
        )
        gate = evaluate_initial_efficiency(
            dossier=imported.normalized_dossier,
            mandatory_question_ids=built.prompt.mandatory_question_ids,
            verification_rows=verification_rows,
            rejection_rows=rejection_rows,
            verification_receipt=verification.receipt,
            prompt_char_count=len(built.prompt.prompt_text),
            response_char_count=len(
                (
                    boundary.fresh_job_root / capture_receipt.report_md_path
                ).read_text(encoding="utf-8")
            ),
            initial_research_seconds=initial_research_seconds,
            total_elapsed_seconds=time.monotonic() - started,
            job_id=fresh_job_id,
            run_id=str(built.packet_payload["run_id"]),
            conversation_id=str(self.store.get_job(fresh_job_id).conversation_id or ""),
        )
        receipt_path = (
            boundary.fresh_job_root
            / "canary/fresh_v3_initial_efficiency_receipt.json"
        )
        write_runtime_json_once(receipt_path, gate.receipt)
        self._emit(
            "FRESH_INITIAL_EFFICIENCY_GATE",
            job_id=fresh_job_id,
            status=gate.receipt["status"],
            acceptance_ratio=gate.receipt["post_preflight_acceptance_ratio"],
            genuine_semantic_repair_count=gate.receipt[
                "genuine_semantic_repair_candidate_count"
            ],
        )
        if not gate.passed:
            failed = orchestrator.seal_failed_run_for_new_conversation(
                reason=";".join(gate.receipt["failure_reasons"])
            )
            self._emit(
                "FRESH_SESSION_DIAGNOSTIC_ONLY",
                job_id=failed.job_id,
                new_conversation_required=True,
            )
        return {
            "schema_version": "e2r_pro_fresh_initial_live_run_result_v1",
            "status": (
                "PRO_FIRST_V2_1_C06_INITIAL_EFFICIENCY_PASS"
                if gate.passed
                else "OPERATIONAL_EFFICIENCY_GATE_FAILED"
            ),
            "job_id": fresh_job_id,
            "run_id": built.packet_payload["run_id"],
            "research_pass_id": built.initial_pass_id,
            "conversation_id": self.store.get_job(fresh_job_id).conversation_id,
            "fresh_runtime_root": str(boundary.fresh_runtime_root),
            "fresh_job_root": str(boundary.fresh_job_root),
            "receipt_path": str(receipt_path),
            "receipt": gate.receipt,
            "score_authority": False,
            "stage_authority": False,
        }

    async def _wait_for_result(
        self, *, job_id: str, run_id: str, adapter: Any
    ) -> FreshDetectedInitialResult:
        monitor = BrowserCompletionMonitor(
            adapter,
            required_stable_observations=(
                self.config.browser.required_stable_observations
            ),
            poll_interval_seconds=self.config.browser.poll_interval_seconds,
        )
        service = ProCompletionStateService(self.store, monitor)
        terminal_report_hash: str | None = None
        terminal_report_stable = 0
        for poll in range(1, self.max_completion_polls + 1):
            job, observation = await service.observe_job(job_id, run_id=run_id)
            if poll == 1 or poll % 12 == 0 or job.status != JobStatus.RESEARCH_RUNNING.value:
                self._emit(
                    "FRESH_INITIAL_COMPLETION_POLL",
                    job_id=job_id,
                    poll=poll,
                    browser_state=observation.inspection.state.value,
                    stable_observations=observation.stable_observations,
                )
            if job.status == JobStatus.RESULT_DETECTED.value and observation.result:
                return FreshDetectedInitialResult(observation.result, False)
            if job.status != JobStatus.RESEARCH_RUNNING.value:
                raise RuntimeError(
                    observation.inspection.detail or f"browser stopped at {job.status}"
                )
            if (
                observation.inspection.state
                not in {BrowserUIState.RESEARCH_RUNNING}
                and not observation.inspection.stop_visible
                and observation.result is not None
                and _readable_terminal_report(observation.result)
            ):
                if observation.result.report_hash == terminal_report_hash:
                    terminal_report_stable += 1
                else:
                    terminal_report_hash = observation.result.report_hash
                    terminal_report_stable = 1
                if terminal_report_stable >= (
                    self.config.browser.required_stable_observations
                ):
                    current = self.store.get_job(job_id)
                    detected = self.store.transition(
                        job_id,
                        expected_version=current.state_version,
                        to_status=JobStatus.RESULT_DETECTED,
                        actor="v2.1-codex-report-structuring-recovery",
                        idempotency_key=(
                            f"terminal-readable-report:{job_id}:"
                            f"{observation.result.report_hash}"
                        ),
                        payload={
                            "assistant_turn_id": observation.result.assistant_turn_id,
                            "report_hash": observation.result.report_hash,
                            "conversation_id": observation.result.conversation_id,
                            "job_marker_matches": True,
                            "run_marker_matches": True,
                            "has_citations": True,
                            "has_dossier_marker": False,
                            "codex_report_structuring_required": True,
                            "automatic_resubmit_allowed": False,
                        },
                    )
                    self._emit(
                        "FRESH_TERMINAL_REPORT_REQUIRES_CODEX_STRUCTURING",
                        job_id=detected.job_id,
                        report_hash=observation.result.report_hash,
                        report_char_count=len(observation.result.report_text),
                        stable_observations=terminal_report_stable,
                        automatic_resubmit_allowed=False,
                    )
                    return FreshDetectedInitialResult(
                        observation.result,
                        True,
                    )
            else:
                terminal_report_hash = None
                terminal_report_stable = 0
            await asyncio.sleep(self.config.browser.poll_interval_seconds)
        raise TimeoutError("fresh Initial Pro completion poll bound reached")

    def _emit(self, phase: str, **payload: Any) -> None:
        self.progress(
            {
                "schema_version": "e2r_pro_fresh_v3_progress_v1",
                "phase": phase,
                "observed_at": _utc_now(),
                **payload,
            }
        )


def build_old_answer_leakage_manifest(
    store: ProFirstJobStore,
    *,
    old_job_id: str,
    old_run_id: str,
    old_conversation_id: str,
    old_job_root: str | Path,
    old_score_values: Sequence[str] = (),
    old_stage_values: Sequence[str] = (),
) -> OldAnswerLeakageManifest:
    """Build a deny-only manifest from the frozen run without copying answers."""

    old = store.get_job(old_job_id)
    if old.old_job_frozen_at is None:
        raise ValueError("old answer manifest requires a frozen diagnostic job")
    root = Path(old_job_root).expanduser().resolve()
    pointer = json.loads(
        (root / "research_passes/effective_dossier.latest.json").read_text(
            encoding="utf-8"
        )
    )
    dossier_path = (root / str(pointer.get("relative_path") or "")).resolve()
    dossier_path.relative_to(root)
    dossier = json.loads(dossier_path.read_text(encoding="utf-8"))
    if canonical_hash(dossier) != pointer.get("dossier_hash"):
        raise ValueError("old effective dossier differs from its immutable pointer")
    facts = tuple(
        row
        for collection in _FACT_COLLECTIONS
        for row in dossier.get(collection) or ()
    )
    routes = tuple(dossier.get("search_route_receipts") or ())
    question_answers = tuple(
        dict.fromkeys(
            str(row.get("closure_reason") or "").strip()
            for row in dossier.get("question_family_results") or ()
            if str(row.get("closure_reason") or "").strip()
        )
    )
    urls: list[str] = []
    for fact in facts:
        urls.extend(
            str(fact.get(key) or "").strip() for key in ("source_url", "url")
        )
    for document in dossier.get("source_documents") or ():
        urls.extend(
            str(document.get(key) or "").strip()
            for key in ("canonical_url", "opened_url")
        )
    for route in routes:
        urls.extend(str(value).strip() for value in route.get("opened_source_urls") or ())
    for lineage in dossier.get("source_lineages") or ():
        urls.extend(str(value).strip() for value in lineage.get("source_urls") or ())
    fact_ids = tuple(
        dict.fromkeys(
            str(fact.get("dossier_fact_id") or fact.get("fact_id") or "").strip()
            for fact in facts
            if str(fact.get("dossier_fact_id") or fact.get("fact_id") or "").strip()
        )
    )
    route_ids = tuple(
        dict.fromkeys(
            str(row.get("route_receipt_id") or "").strip()
            for row in routes
            if str(row.get("route_receipt_id") or "").strip()
        )
    )
    pass_ids = tuple(row.pass_id for row in ProMultiPassLedger(store).list_passes(old_job_id))
    return OldAnswerLeakageManifest(
        old_job_id=old_job_id,
        old_run_id=old_run_id,
        old_conversation_id=old_conversation_id,
        old_fact_ids=fact_ids,
        old_route_receipt_ids=tuple(dict.fromkeys(route_ids)),
        old_research_pass_ids=tuple(dict.fromkeys(pass_ids)),
        old_question_answers=question_answers,
        old_score_values=tuple(dict.fromkeys(str(value) for value in old_score_values)),
        old_stage_values=tuple(dict.fromkeys(str(value) for value in old_stage_values)),
        expected_source_urls=tuple(dict.fromkeys(value for value in urls if value)),
        expected_fact_ids=fact_ids,
    )


def evaluate_initial_efficiency(
    *,
    dossier: Mapping[str, Any],
    mandatory_question_ids: Sequence[str],
    verification_rows: Sequence[Mapping[str, Any]],
    rejection_rows: Sequence[Mapping[str, Any]],
    verification_receipt: Mapping[str, Any],
    prompt_char_count: int,
    response_char_count: int,
    initial_research_seconds: float,
    total_elapsed_seconds: float,
    job_id: str,
    run_id: str,
    conversation_id: str,
) -> FreshInitialEfficiencyGate:
    """Evaluate the initial response before any repair can affect its ratio."""

    material = tuple(dossier.get("material_facts") or ())
    material_ids = {
        str(row.get("dossier_fact_id") or "") for row in material
    }
    accepted_ids = {
        str(row.get("dossier_fact_id") or "")
        for row in verification_rows
        if str(row.get("dossier_fact_id") or "") in material_ids
        and str(row.get("status") or "") in ACCEPTED_SOURCE_STATUSES
    }
    candidate_count = len(material)
    accepted_count = len(accepted_ids)
    acceptance_ratio = (
        accepted_count / candidate_count if candidate_count else 0.0
    )
    expected_questions = set(str(value) for value in mandatory_question_ids)
    actual_questions = {
        str(row.get("question_family_id") or "")
        for row in dossier.get("question_family_results") or ()
    }
    missing_questions = tuple(sorted(expected_questions - actual_questions))
    source_missing = sum(not str(row.get("source_document_id") or "") for row in material)
    question_unbound = sum(not tuple(row.get("question_family_ids") or ()) for row in material)
    derived_mixed = sum(
        (row.get("verifier_preflight") or {}).get(
            "derived_calculation_mixed_into_fact"
        )
        is not False
        for row in material
    )
    multi_source = sum(
        isinstance(row.get("source_document_id"), (list, tuple, set))
        or len(tuple(row.get("source_document_ids") or ())) > 1
        for row in material
    )
    tracking_url_count = sum(
        _has_tracking_query(str(row.get("canonical_url") or ""))
        or bool(urlsplit(str(row.get("canonical_url") or "")).fragment)
        for row in dossier.get("source_documents") or ()
    )
    genuine_repair_ids = {
        str(row.get("candidate_id") or "")
        for row in rejection_rows
        if row.get("material") is True
        and row.get("send_to_pro_allowed") is True
        and row.get("cause_class") == "GENUINE_SEMANTIC_OR_SOURCE_DEFECT"
    }
    initial_output_defect_ids = {
        str(row.get("candidate_id") or "")
        for row in rejection_rows
        if row.get("material") is True
        and row.get("cause_class") == "INITIAL_PROMPT_OUTPUT_DEFECT"
    }
    genuine_limit = max(5, int(candidate_count * 0.10))
    local_sent = int(
        verification_receipt.get("local_normalizable_sent_to_pro_count") or 0
    )
    representation_sent = int(
        verification_receipt.get("source_representation_sent_to_pro_count") or 0
    )
    unclassified = int(
        verification_receipt.get("unclassified_rejection_count") or 0
    )
    failures: list[str] = []
    checks = (
        (not missing_questions, "MANDATORY_QUESTION_ROSTER_INCOMPLETE"),
        (source_missing == 0, "MATERIAL_SOURCE_DOCUMENT_UNBOUND"),
        (question_unbound == 0, "MATERIAL_QUESTION_UNBOUND"),
        (tracking_url_count == 0, "TRACKING_URL_RETAINED"),
        (derived_mixed == 0, "DERIVED_METRIC_MIXED_INTO_FACT"),
        (multi_source == 0, "MULTI_SOURCE_ATOMIC_FACT"),
        (local_sent == 0, "LOCAL_NORMALIZABLE_SENT_TO_PRO"),
        (representation_sent == 0, "SOURCE_REPRESENTATION_SENT_TO_PRO"),
        (unclassified == 0, "UNCLASSIFIED_REJECTION"),
        (not initial_output_defect_ids, "INITIAL_PROMPT_OUTPUT_DEFECT"),
        (candidate_count > 0, "NO_INITIAL_MATERIAL_CANDIDATES"),
        (acceptance_ratio >= 0.80, "INITIAL_ACCEPTANCE_RATIO_BELOW_80_PERCENT"),
        (
            len(genuine_repair_ids) <= genuine_limit,
            "GENUINE_SEMANTIC_REPAIR_ROSTER_TOO_LARGE",
        ),
    )
    failures.extend(code for passed, code in checks if not passed)
    unsigned = {
        "schema_version": FRESH_INITIAL_RECEIPT_SCHEMA,
        "status": "PASS" if not failures else "FAIL",
        "verdict": (
            "PRO_FIRST_V2_1_INITIAL_EFFICIENCY_PASS"
            if not failures
            else "OPERATIONAL_EFFICIENCY_GATE_FAILED"
        ),
        "job_id": job_id,
        "run_id": run_id,
        "conversation_id": conversation_id,
        "initial_prompt_char_count": int(prompt_char_count),
        "initial_response_char_count": int(response_char_count),
        "initial_research_elapsed_seconds": round(initial_research_seconds, 6),
        "total_elapsed_seconds": round(total_elapsed_seconds, 6),
        "source_document_count": len(tuple(dossier.get("source_documents") or ())),
        "initial_material_candidate_count": candidate_count,
        "post_preflight_accepted_material_count": accepted_count,
        "post_preflight_acceptance_ratio": round(acceptance_ratio, 6),
        "mandatory_question_count": len(expected_questions),
        "mandatory_question_covered_count": len(expected_questions) - len(missing_questions),
        "missing_mandatory_question_ids": list(missing_questions),
        "material_source_document_unbound_count": source_missing,
        "question_unbound_material_fact_count": question_unbound,
        "tracking_url_fact_count": tracking_url_count,
        "derived_metric_mixed_fact_count": derived_mixed,
        "multi_source_atomic_fact_count": multi_source,
        "local_normalizable_sent_to_pro_count": local_sent,
        "source_representation_sent_to_pro_count": representation_sent,
        "unclassified_rejection_count": unclassified,
        "initial_prompt_output_defect_count": len(initial_output_defect_ids),
        "genuine_semantic_repair_candidate_count": len(genuine_repair_ids),
        "genuine_semantic_repair_candidate_limit": genuine_limit,
        "repair_pass_count": 0,
        "repair_prompt_char_count": 0,
        "repair_deferred_batch_count": 0,
        "public_gap_pass_count": 0,
        "saturation_pass_count": 0,
        "old_conversation_new_submit_count": 0,
        "full_dossier_repair_response_required_count": 0,
        "second_repair_pass_count": 0,
        "partial_score_published_count": 0,
        "score_authority": False,
        "stage_authority": False,
        "publication_withheld": True,
        "failure_reasons": failures,
    }
    return FreshInitialEfficiencyGate(
        receipt={**unsigned, "receipt_hash": canonical_hash(unsigned)}
    )


def _requires_browser_result_recovery(job: Any) -> bool:
    """Open ChatGPT only while the immutable capture still does not exist.

    ``USER_ATTENTION_REQUIRED`` is shared by browser and downstream verifier
    failures.  Once capture_count is one, reopening the browser cannot repair a
    source-verifier exception and risks touching an already completed request.
    """

    return job.status in {
        JobStatus.RESEARCH_RUNNING.value,
        JobStatus.RESULT_DETECTED.value,
    } or (
        job.status == JobStatus.USER_ATTENTION_REQUIRED.value
        and job.capture_count == 0
    )


def _persist_runtime_manifest(
    fresh_runtime_root: Path,
    manifest: OldAnswerLeakageManifest,
) -> None:
    payload = {
        "schema_version": "e2r_pro_old_answer_leakage_manifest_v1",
        **{
            name: (
                list(value) if isinstance(value, tuple) else value
            )
            for name, value in manifest.__dict__.items()
        },
        "answer_input_authority": False,
    }
    write_runtime_json_once(
        fresh_runtime_root / "old_answer_leakage_manifest.runtime.json",
        {**payload, "manifest_hash": canonical_hash(payload)},
    )


def _verification_rows(result: Any, path: Path) -> tuple[Mapping[str, Any], ...]:
    if result is not None:
        return tuple(row.to_dict() for row in result.verifications)
    return _read_jsonl(path)


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def _has_tracking_query(value: str) -> bool:
    return any(
        key.casefold().startswith("utm_")
        or key.casefold() in _TRACKING_QUERY_KEYS
        for key, _ in parse_qsl(urlsplit(value).query, keep_blank_values=True)
    )


def _readable_terminal_report(result: BrowserResultSnapshot) -> bool:
    return bool(
        result.conversation_id
        and result.assistant_turn_id
        and result.report_text.strip()
        and result.has_citations
        and result.job_marker_matches
        and result.run_marker_matches
        and not result.has_dossier_marker
        and not result.has_repair_delta_marker
    )


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _elapsed_since_submission(submitted_at: str | None) -> float:
    if not submitted_at:
        return 0.0
    parsed = datetime.fromisoformat(submitted_at.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("durable submitted_at must be timezone-aware")
    return max(
        0.0,
        (datetime.now(timezone.utc) - parsed.astimezone(timezone.utc)).total_seconds(),
    )


__all__ = [
    "FRESH_LIVE_AUTHORIZATION_PHRASE",
    "FreshInitialCanarySpec",
    "FreshDetectedInitialResult",
    "FreshInitialEfficiencyGate",
    "FreshV3InitialLiveCanaryRunner",
    "build_old_answer_leakage_manifest",
    "evaluate_initial_efficiency",
]
