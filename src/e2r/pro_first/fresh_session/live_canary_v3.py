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
from ..browser.protocol import (
    BrowserArtifactUnavailable,
    BrowserResultSnapshot,
    BrowserUIState,
)
from ..browser.worker import ProBrowserWorker
from ..capture.coordinator import CaptureFilesystemReconciler, ProCaptureCoordinator
from ..capture.expanded_dossier import (
    ExpandedDossierArtifactService,
    expanded_dossier_recovery_required,
)
from ..capture.receipt import (
    CaptureReceipt,
    load_capture_receipt,
    verify_capture_bundle,
)
from ..config import ProFirstLocalConfig
from ..dossier import (
    CodexProReportDossierStructurer,
    ProDossierImporter,
    ResearchDossierParser,
)
from ..ids import canonical_hash, canonical_json
from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob
from ..state_machine import TransitionContext
from ..multi_pass import (
    ARTIFACT_REEXPORT_PASS_NAME,
    ProMultiPassDossierStore,
    ProMultiPassLedger,
    ResearchPassStatus,
)
from ..verification import (
    ACCEPTED_SOURCE_STATUSES,
    CodexMechanismScopeMapper,
    EvidenceLifecycleBridge,
    ProSourceVerificationService,
    ProSourceVerifier,
)
from .boundary import (
    FreshSessionBoundary,
    FreshSessionBoundaryService,
    OldAnswerLeakageManifest,
    build_independent_leakage_manifest,
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
        archetypes = tuple(
            dict.fromkeys(str(value).strip() for value in self.archetype_ids)
        )
        if not 1 <= len(archetypes) <= 3 or any(not value for value in archetypes):
            raise ValueError("fresh canary needs one to three archetype ids")
        object.__setattr__(self, "archetype_ids", archetypes)


@dataclass(frozen=True)
class IndependentFreshInitialCanarySpec:
    """A fresh cross-archetype canary that has no old target run to inherit."""

    fresh_session_id: str
    symbol: str
    company_name: str
    as_of_date: str
    archetype_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        for value, label in (
            (self.fresh_session_id, "fresh_session_id"),
            (self.symbol, "symbol"),
            (self.company_name, "company_name"),
            (self.as_of_date, "as_of_date"),
        ):
            normalized = str(value).strip()
            if not normalized:
                raise ValueError(f"{label} is required")
            object.__setattr__(self, label, normalized)
        archetypes = tuple(
            dict.fromkeys(str(value).strip() for value in self.archetype_ids)
        )
        if not 1 <= len(archetypes) <= 3 or any(not value for value in archetypes):
            raise ValueError("fresh canary needs one to three archetype ids")
        object.__setattr__(self, "archetype_ids", archetypes)


FreshCanarySpec = FreshInitialCanarySpec | IndependentFreshInitialCanarySpec


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
        spec: FreshCanarySpec,
        *,
        commit_sha: str,
        resume_prepared_job_id: str | None = None,
    ) -> Mapping[str, Any]:
        started = time.monotonic()
        manifest = self._build_leakage_manifest(spec)
        boundary_service = FreshSessionBoundaryService(self.store)
        if resume_prepared_job_id is None:
            boundary, fresh_job = self._start_boundary(
                boundary_service,
                spec,
                manifest=manifest,
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
            captured_job, capture = await self._capture_initial_with_artifact_reexport(
                boundary=boundary,
                orchestrator=orchestrator,
                built=built,
                result=result,
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
            expanded = await ExpandedDossierArtifactService().recover(
                job_root=boundary.fresh_job_root,
                capture_receipt=capture.receipt,
                adapter=runtime.session.adapter,
            )
            if expanded is not None:
                self._emit(
                    "FRESH_EXPANDED_DOSSIER_CAPTURED_NO_SUBMIT",
                    job_id=fresh_job.job_id,
                    expanded_dossier_hash=expanded.receipt[
                        "expanded_dossier_hash"
                    ],
                    expanded_counts=expanded.receipt["expanded_counts"],
                    browser_submit_delta=0,
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
        spec: FreshCanarySpec,
        *,
        commit_sha: str,
        submitted_job_id: str,
    ) -> Mapping[str, Any]:
        """Resume one exact submitted initial request without any DOM send."""

        started = time.monotonic()
        manifest = self._build_leakage_manifest(spec)
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
        built = orchestrator.load_initial_packet_for_submitted_recovery(
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
                captured_job, capture = await self._capture_initial_with_artifact_reexport(
                    boundary=boundary,
                    orchestrator=orchestrator,
                    built=built,
                    result=result,
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

        if expanded_dossier_recovery_required(
            boundary.fresh_job_root,
            capture_receipt,
        ):
            runtime = await ProBrowserWorker(self.config.browser).open(job_id=job.job_id)
            try:
                current_conversation = runtime.adapter.conversation_id()
                if current_conversation != capture_receipt.conversation_id:
                    recovered = await runtime.adapter.recover_conversation_without_submit(
                        job_id=job.job_id,
                        run_id=str(built.packet_payload["run_id"]),
                        search_terms=(
                            str(capture_receipt.conversation_id or ""),
                        ),
                    )
                    if recovered.conversation_id != capture_receipt.conversation_id:
                        raise ValueError(
                            "recovered JSON attachment conversation differs from capture"
                        )
                expanded = await ExpandedDossierArtifactService().recover(
                    job_root=boundary.fresh_job_root,
                    capture_receipt=capture_receipt,
                    adapter=runtime.adapter,
                )
                if expanded is None:
                    raise ValueError(
                        "expanded dossier recovery was required but produced no bundle"
                    )
                self._emit(
                    "FRESH_EXPANDED_DOSSIER_RECOVERED_NO_SUBMIT",
                    job_id=fresh_job.job_id,
                    expanded_dossier_hash=expanded.receipt[
                        "expanded_dossier_hash"
                    ],
                    expanded_counts=expanded.receipt["expanded_counts"],
                    browser_submit_delta=0,
                )
            finally:
                await runtime.close()

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

    def _build_leakage_manifest(
        self,
        spec: FreshCanarySpec,
    ) -> OldAnswerLeakageManifest:
        if isinstance(spec, IndependentFreshInitialCanarySpec):
            return build_independent_leakage_manifest(
                fresh_session_id=spec.fresh_session_id,
                symbol=spec.symbol,
                as_of_date=spec.as_of_date,
            )
        return build_old_answer_leakage_manifest(
            self.store,
            old_job_id=spec.old_job_id,
            old_run_id=spec.old_run_id,
            old_conversation_id=spec.old_conversation_id,
            old_job_root=self.old_runtime_root / "jobs" / spec.old_job_id,
            old_score_values=spec.old_score_values,
            old_stage_values=spec.old_stage_values,
        )

    def _start_boundary(
        self,
        service: FreshSessionBoundaryService,
        spec: FreshCanarySpec,
        *,
        manifest: OldAnswerLeakageManifest,
    ) -> tuple[FreshSessionBoundary, ProResearchJob]:
        if isinstance(spec, IndependentFreshInitialCanarySpec):
            return service.start_independent(
                symbol=spec.symbol,
                company_name=spec.company_name,
                as_of_date=spec.as_of_date,
                fresh_session_id=spec.fresh_session_id,
                reference_runtime_root=self.old_runtime_root,
                fresh_runtime_root=self.fresh_runtime_root,
                archetype_ids=spec.archetype_ids,
                leakage_manifest=manifest,
            )
        return service.start(
            old_job_id=spec.old_job_id,
            old_run_id=spec.old_run_id,
            old_conversation_id=spec.old_conversation_id,
            fresh_session_id=spec.fresh_session_id,
            old_runtime_root=self.old_runtime_root,
            fresh_runtime_root=self.fresh_runtime_root,
            archetype_ids=spec.archetype_ids,
            leakage_manifest=manifest,
        )

    async def _reverify_user_attention_result(
        self,
        *,
        job_id: str,
        run_id: str,
        adapter: Any,
    ) -> FreshDetectedInitialResult:
        """Recover one already submitted turn without another DOM send.

        A large ChatGPT user turn can appear in a freshly opened public page
        after the submit-time persistence poll expires.  In that case the
        durable ledger is already at ``submit_count=1`` and must never click
        again.  Re-prove the exact job/run turn from another public page, then
        wait read-only for its terminal result while the durable job remains
        in ``USER_ATTENTION_REQUIRED``.
        """

        current = self.store.get_job(job_id)
        if (
            current.status != JobStatus.USER_ATTENTION_REQUIRED.value
            or current.submit_count != 1
            or current.capture_count != 0
        ):
            raise ValueError(
                "late persistence recovery requires one pre-capture submitted job"
            )
        conversation_id = str(adapter.conversation_id() or "").strip()
        if not conversation_id:
            raise ValueError(
                "late persistence recovery requires the visible canonical conversation"
            )
        persistence = await adapter.inspect_submitted_turn_persistence(
            conversation_id=conversation_id,
            job_id=job_id,
            run_id=run_id,
        )
        if not persistence.persistence_confirmed:
            raise ValueError(
                "user-attention recovery still lacks the exact durable job/run turn: "
                f"observation_id={persistence.observation_id}, "
                f"missing_markers={list(persistence.missing_markers)}"
            )
        self._emit(
            "FRESH_LATE_SERVER_PERSISTENCE_CONFIRMED_NO_SUBMIT",
            job_id=job_id,
            run_id=run_id,
            conversation_id=conversation_id,
            observation_id=persistence.observation_id,
            user_turn_id=persistence.user_turn_id,
            submit_count=current.submit_count,
            browser_submit_delta=0,
        )
        last_hash: str | None = None
        stable = 0
        result: BrowserResultSnapshot | None = None
        for poll in range(1, self.max_completion_polls + 1):
            inspection = await adapter.inspect_state()
            if inspection.stop_visible or inspection.state in {
                BrowserUIState.RESEARCH_RUNNING,
            }:
                if poll == 1 or poll % 12 == 0:
                    self._emit(
                        "FRESH_LATE_PERSISTED_COMPLETION_POLL_NO_SUBMIT",
                        job_id=job_id,
                        poll=poll,
                        browser_state=inspection.state.value,
                        submit_count=current.submit_count,
                        browser_submit_delta=0,
                    )
                await asyncio.sleep(self.config.browser.poll_interval_seconds)
                continue
            if inspection.state in {
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
            if stable >= self.config.browser.required_stable_observations:
                break
            await asyncio.sleep(self.config.browser.poll_interval_seconds)
        if result is None or stable < self.config.browser.required_stable_observations:
            raise TimeoutError(
                "late-persisted user-attention result did not become stably terminal"
            )
        current = self.store.get_job(job_id)
        recovered = self.store.transition(
            job_id,
            expected_version=current.state_version,
            to_status=JobStatus.RESULT_DETECTED,
            actor="v2.1-fresh-v3-result-reverification",
            idempotency_key=(
                f"result-reverified:{job_id}:{result.report_hash}:"
                f"{persistence.observation_id}"
            ),
            payload={
                "report_hash": result.report_hash,
                "conversation_id": result.conversation_id,
                "assistant_turn_id": result.assistant_turn_id,
                "job_marker_matches": True,
                "run_marker_matches": True,
                "stable_observations": stable,
                "server_persistence_observation_id": persistence.observation_id,
                "server_persistence_user_turn_id": persistence.user_turn_id,
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

    async def _capture_initial_with_artifact_reexport(
        self,
        *,
        boundary: Any,
        orchestrator: FreshSessionOrchestratorV3,
        built: Any,
        result: BrowserResultSnapshot,
        adapter: Any,
        capture_mode: str,
        dossier_override: Mapping[str, object] | None,
    ):
        """Capture once, or re-export one missing generated file in-place.

        This is not a research retry.  The exact completed initial response is
        already hash-bound and becomes the completed parent pass.  A single
        same-conversation pass may only recreate its missing transport file;
        it cannot browse, add evidence, alter score, or change Stage.
        """

        run_id = str(built.packet_payload["run_id"])
        self._reconcile_visible_artifact_reexport(
            orchestrator=orchestrator,
            built=built,
            result=result,
        )
        try:
            return await ProCaptureCoordinator(self.store).capture(
                built.job.job_id,
                run_id=run_id,
                expected_filename=built.output_filename,
                expected_report_hash=result.report_hash,
                job_root=boundary.fresh_job_root,
                adapter=adapter,
                capture_mode=capture_mode,
                dossier_override=dossier_override,
            )
        except BrowserArtifactUnavailable as error:
            if dossier_override is not None:
                raise
            scope = orchestrator.ledger.get_scope(built.job.job_id)
            if scope is None:
                scope = orchestrator.establish_followup_scope(
                    built,
                    initial_response_hash=result.report_hash,
                )
            expected_artifact = (
                f"E2R_ResearchDossierV3_{scope.target_id}_{scope.as_of_date}.json"
            )
            plan, _compiled = orchestrator.plan_v3_followup(
                built,
                pass_name=ARTIFACT_REEXPORT_PASS_NAME,
                latest_dossier_digest={
                    "initial_response_hash": result.report_hash,
                    "initial_research_pass_id": built.initial_pass_id,
                    "transport_only": True,
                },
                pass_inputs={
                    "route_reason": "CHATGPT_SANDBOX_ARTIFACT_FILE_NOT_FOUND",
                    "failed_artifact_error": str(error),
                    "expected_artifact_filename": expected_artifact,
                    "initial_research_pass_id": built.initial_pass_id,
                    "new_research_allowed": False,
                    "score_authority": False,
                    "stage_authority": False,
                },
            )
            current = orchestrator.ledger.get_pass(plan.research_pass.pass_id)
            if current.submit_count == 0:
                if current.status == ResearchPassStatus.PLANNED.value:
                    await orchestrator.prepare_followup(plan, adapter)
                elif current.status != ResearchPassStatus.PREPARED.value:
                    raise RuntimeError(
                        "artifact re-export has an invalid zero-submit state"
                    )
                await orchestrator.submit_followup(plan, adapter)
                self._emit(
                    "FRESH_ARTIFACT_REEXPORT_SUBMITTED_SAME_CONVERSATION",
                    job_id=built.job.job_id,
                    pass_id=plan.research_pass.pass_id,
                    parent_pass_id=plan.research_pass.parent_pass_id,
                    conversation_id=scope.conversation_id,
                    new_research_allowed=False,
                )
            elif current.status not in {
                ResearchPassStatus.RESEARCH_RUNNING.value,
                ResearchPassStatus.TRANSPORT_PENDING.value,
                ResearchPassStatus.COMPLETE.value,
            }:
                raise RuntimeError(
                    "artifact re-export has no unambiguous exactly-once recovery path"
                )
            elif current.status == ResearchPassStatus.TRANSPORT_PENDING.value:
                await orchestrator.resume_intercepted_followup_submit(
                    plan,
                    adapter,
                )
                self._emit(
                    "FRESH_ARTIFACT_REEXPORT_PREDISPATCH_CLAIM_RECOVERED",
                    job_id=built.job.job_id,
                    pass_id=plan.research_pass.pass_id,
                    conversation_id=scope.conversation_id,
                    submit_count=1,
                )

            reexported = await self._wait_for_artifact_reexport_result(
                plan=plan,
                run_id=run_id,
                adapter=adapter,
            )
            current = orchestrator.ledger.get_pass(plan.research_pass.pass_id)
            if current.status == ResearchPassStatus.TRANSPORT_PENDING.value:
                orchestrator.confirm_transport_pending_result_visible(current.pass_id)
                current = orchestrator.ledger.get_pass(current.pass_id)
            if current.status != ResearchPassStatus.COMPLETE.value:
                orchestrator.complete_followup(
                    current.pass_id,
                    response_hash=reexported.report_hash,
                    conversation_id=scope.conversation_id,
                )
            self._emit(
                "FRESH_ARTIFACT_REEXPORT_COMPLETED_NO_NEW_RESEARCH",
                job_id=built.job.job_id,
                pass_id=plan.research_pass.pass_id,
                report_hash=reexported.report_hash,
                conversation_id=scope.conversation_id,
            )

            detected = await self._reverify_user_attention_result(
                job_id=built.job.job_id,
                run_id=run_id,
                adapter=adapter,
            )
            return await ProCaptureCoordinator(self.store).capture(
                built.job.job_id,
                run_id=run_id,
                expected_filename=built.output_filename,
                expected_report_hash=detected.result.report_hash,
                job_root=boundary.fresh_job_root,
                adapter=adapter,
                capture_mode=f"{capture_mode}_ARTIFACT_REEXPORT",
                dossier_override=None,
            )

    def _reconcile_visible_artifact_reexport(
        self,
        *,
        orchestrator: FreshSessionOrchestratorV3,
        built: Any,
        result: BrowserResultSnapshot,
    ) -> bool:
        """Bind an already visible transport-only result without another send.

        A process can restart after the browser dispatched ARTIFACT_REEXPORT
        but before the ledger recorded persistence.  The latest assistant turn
        is sufficient only when it contains the exact pass and parent markers
        in the exact durable conversation.  This transition never touches the
        composer or browser send control.
        """

        artifact_passes = tuple(
            record
            for record in orchestrator.ledger.list_passes(built.job.job_id)
            if record.pass_name == ARTIFACT_REEXPORT_PASS_NAME
        )
        if not artifact_passes:
            return False
        if len(artifact_passes) != 1:
            raise RuntimeError(
                "artifact re-export recovery requires exactly one transport pass"
            )
        current = artifact_passes[0]
        pass_marker = f"[[E2R_PRO_PASS_ID:{current.pass_id}]]"
        parent_marker = (
            f"[[E2R_PRO_PARENT_PASS_ID:{current.parent_pass_id}]]"
        )
        if (
            pass_marker not in result.report_text
            or parent_marker not in result.report_text
        ):
            return False
        if (
            result.conversation_id != current.conversation_id
            or current.parent_pass_id != built.initial_pass_id
        ):
            raise RuntimeError(
                "visible artifact re-export differs from its durable lineage"
            )
        if current.status == ResearchPassStatus.TRANSPORT_PENDING.value:
            current = orchestrator.confirm_transport_pending_result_visible(
                current.pass_id
            )
        if current.status == ResearchPassStatus.RESEARCH_RUNNING.value:
            current = orchestrator.complete_followup(
                current.pass_id,
                response_hash=result.report_hash,
                conversation_id=str(result.conversation_id),
            )
        elif current.status == ResearchPassStatus.COMPLETE.value:
            if current.response_hash != result.report_hash:
                raise RuntimeError(
                    "completed artifact re-export response hash changed"
                )
            current = orchestrator.complete_followup(
                current.pass_id,
                response_hash=result.report_hash,
                conversation_id=str(result.conversation_id),
            )
        else:
            raise RuntimeError(
                "visible artifact re-export has no recoverable durable status"
            )
        self._emit(
            "FRESH_VISIBLE_ARTIFACT_REEXPORT_RECONCILED_NO_SUBMIT",
            job_id=built.job.job_id,
            pass_id=current.pass_id,
            report_hash=result.report_hash,
            conversation_id=result.conversation_id,
            submit_count=current.submit_count,
            browser_submit_delta=0,
        )
        return True

    async def _wait_for_artifact_reexport_result(
        self,
        *,
        plan: Any,
        run_id: str,
        adapter: Any,
    ) -> BrowserResultSnapshot:
        monitor = BrowserCompletionMonitor(
            adapter,
            required_stable_observations=(
                self.config.browser.required_stable_observations
            ),
            poll_interval_seconds=self.config.browser.poll_interval_seconds,
        )
        for poll in range(1, self.max_completion_polls + 1):
            observation = await monitor.observe(
                job_id=plan.scope.job_id,
                run_id=run_id,
                expected_pass_id=plan.research_pass.pass_id,
            )
            if poll == 1 or poll % 12 == 0 or observation.completion_confirmed:
                self._emit(
                    "FRESH_ARTIFACT_REEXPORT_COMPLETION_POLL",
                    job_id=plan.scope.job_id,
                    pass_id=plan.research_pass.pass_id,
                    poll=poll,
                    browser_state=observation.inspection.state.value,
                    stable_observations=observation.stable_observations,
                )
            if observation.completion_confirmed and observation.result is not None:
                if observation.result.conversation_id != plan.scope.conversation_id:
                    raise RuntimeError(
                        "artifact re-export escaped the approved conversation"
                    )
                return observation.result
            if observation.inspection.state in {
                BrowserUIState.LOGIN_REQUIRED,
                BrowserUIState.AWAITING_CLARIFICATION,
                BrowserUIState.QUOTA_PENDING,
                BrowserUIState.RETRYABLE_ERROR,
                BrowserUIState.UI_INCOMPATIBLE,
            }:
                raise RuntimeError(
                    observation.inspection.detail
                    or observation.inspection.state.value
                )
            await asyncio.sleep(self.config.browser.poll_interval_seconds)
        raise TimeoutError("artifact re-export completion poll bound reached")

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
        scope = orchestrator.ledger.get_scope(fresh_job_id)
        initial_response_hash = (
            scope.initial_response_hash
            if scope is not None
            else capture_receipt.report_md_hash
        )
        imported = ProDossierImporter(self.store).import_job(
            fresh_job_id,
            job_root=boundary.fresh_job_root,
            expected_research_pass_id=built.initial_pass_id,
            expected_parent_pass_id=None,
            expected_response_hash=initial_response_hash,
        )
        if scope is None:
            scope = orchestrator.establish_followup_scope(
                built,
                initial_response_hash=initial_response_hash,
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
                _initial_efficiency_pass_status(
                    self.store.get_job(fresh_job_id).archetype_ids
                )
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
    dossier = _load_old_dossier_for_deny_manifest(
        root,
        old_job_id=old_job_id,
        old_run_id=old_run_id,
        old_conversation_id=old_conversation_id,
    )
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
    pass_ids = tuple(
        dict.fromkeys(
            (
                *(
                    row.pass_id
                    for row in ProMultiPassLedger(store).list_passes(old_job_id)
                ),
                *_collect_pro_pass_ids(dossier),
            )
        )
    )
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


def _collect_pro_pass_ids(value: Any) -> tuple[str, ...]:
    collected: list[str] = []

    def visit(current: Any) -> None:
        if isinstance(current, Mapping):
            for key, nested in current.items():
                if key in {"research_pass_id", "pass_id", "parent_pass_id"}:
                    token = str(nested or "").strip()
                    if token.startswith("PROPASS-"):
                        collected.append(token)
                visit(nested)
        elif isinstance(current, (list, tuple)):
            for nested in current:
                visit(nested)

    visit(value)
    return tuple(dict.fromkeys(collected))


def _load_old_dossier_for_deny_manifest(
    root: Path,
    *,
    old_job_id: str,
    old_run_id: str,
    old_conversation_id: str,
) -> Mapping[str, Any]:
    """Load old answer tokens without granting the old dossier any authority.

    A verifier-complete predecessor has the canonical effective-dossier pointer.
    A diagnostic predecessor can fail at schema import after an exactly-once
    browser capture, so it has no effective dossier.  In that case only the
    READY-certified, hash-verified capture is read to build the deny-only
    leakage manifest.  The captured dossier never becomes a scoring or source-
    verification input through this path.
    """

    pointer_path = root / "research_passes/effective_dossier.latest.json"
    if pointer_path.is_file():
        pointer = json.loads(pointer_path.read_text(encoding="utf-8"))
        dossier_path = (root / str(pointer.get("relative_path") or "")).resolve()
        dossier_path.relative_to(root)
        dossier = json.loads(dossier_path.read_text(encoding="utf-8"))
        if canonical_hash(dossier) != pointer.get("dossier_hash"):
            raise ValueError("old effective dossier differs from its immutable pointer")
        if not isinstance(dossier, dict):
            raise ValueError("old effective dossier must be a JSON object")
        return dossier

    ready_path = root / "capture/incoming/READY.json"
    receipt_path = root / "capture/incoming/browser_capture_receipt.json"
    if not ready_path.is_file() or not receipt_path.is_file():
        raise FileNotFoundError(
            "old answer manifest requires an effective dossier or a READY-certified capture"
        )
    ready = json.loads(ready_path.read_text(encoding="utf-8"))
    receipt = load_capture_receipt(receipt_path)
    if (
        not isinstance(ready, dict)
        or ready.get("schema_version") != "e2r_pro_capture_ready_v1"
        or ready.get("written_last") is not True
        or ready.get("capture_receipt_path")
        != "capture/incoming/browser_capture_receipt.json"
        or ready.get("capture_receipt_hash") != receipt.receipt_hash
        or ready.get("job_id") != old_job_id
        or ready.get("run_id") != old_run_id
    ):
        raise ValueError("old capture READY identity or receipt hash mismatch")
    if (
        receipt.job_id != old_job_id
        or receipt.run_id != old_run_id
        or receipt.conversation_id != old_conversation_id
    ):
        raise ValueError("old capture receipt differs from frozen predecessor identity")
    verify_capture_bundle(root, receipt)
    dossier_path = (root / receipt.dossier_json_path).resolve()
    dossier_path.relative_to(root)
    return ResearchDossierParser().parse(
        downloaded_json_path=dossier_path
    ).payload


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

    serialized_material = tuple(dossier.get("material_facts") or ())
    lifecycle_bridge = EvidenceLifecycleBridge()
    material = tuple(
        row
        for row in serialized_material
        if lifecycle_bridge.classify(row).compile_as_evidence
    )
    excluded_noncurrent_material = tuple(
        row
        for row in serialized_material
        if not lifecycle_bridge.classify(row).compile_as_evidence
    )
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
        if str(row.get("candidate_id") or "") in material_ids
        and row.get("material") is True
        and row.get("send_to_pro_allowed") is True
        and row.get("cause_class") == "GENUINE_SEMANTIC_OR_SOURCE_DEFECT"
    }
    initial_output_defect_ids = {
        str(row.get("candidate_id") or "")
        for row in rejection_rows
        if str(row.get("candidate_id") or "") in material_ids
        and row.get("material") is True
        and row.get("cause_class") == "INITIAL_PROMPT_OUTPUT_DEFECT"
    }
    self_reported_withheld_candidate_count = int(
        (dossier.get("research_saturation") or {}).get(
            "candidate_fact_count_withheld"
        )
        or 0
    )
    if candidate_count == 0 and self_reported_withheld_candidate_count > 0:
        initial_output_defect_ids.add(
            "SELF_REPORTED_BULK_WITHHELD_CANDIDATE_ROSTER"
        )
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
        "serialized_material_fact_count": len(serialized_material),
        "initial_material_candidate_count": candidate_count,
        "excluded_noncurrent_material_fact_count": len(
            excluded_noncurrent_material
        ),
        "excluded_noncurrent_material_fact_ids": [
            str(row.get("dossier_fact_id") or "")
            for row in excluded_noncurrent_material
        ],
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
        "self_reported_withheld_candidate_count": (
            self_reported_withheld_candidate_count
        ),
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


def _initial_efficiency_pass_status(archetype_ids: Sequence[str]) -> str:
    if len(archetype_ids) == 1:
        prefix = str(archetype_ids[0]).split("_", 1)[0]
        if prefix.startswith("C") and prefix[1:].isdigit():
            return f"PRO_FIRST_V2_1_{prefix}_INITIAL_EFFICIENCY_PASS"
    return "PRO_FIRST_V2_1_MULTI_ARCHETYPE_INITIAL_EFFICIENCY_PASS"


__all__ = [
    "FRESH_LIVE_AUTHORIZATION_PHRASE",
    "FreshInitialCanarySpec",
    "IndependentFreshInitialCanarySpec",
    "FreshDetectedInitialResult",
    "FreshInitialEfficiencyGate",
    "FreshV3InitialLiveCanaryRunner",
    "build_old_answer_leakage_manifest",
    "evaluate_initial_efficiency",
]
