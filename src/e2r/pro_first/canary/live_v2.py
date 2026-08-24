"""Actual ChatGPT Pro V2 multi-pass canary orchestration.

The runner uses the visible ChatGPT web UI only.  The user's one initial
approval authorizes bounded same-conversation follow-ups, while every pass is
still claimed exactly once in the durable ledger.  Pro supplies research
evidence; source verification, saturation, score, and Stage authority remain
deterministic.
"""

from __future__ import annotations

import asyncio
from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import time
from typing import Any, Callable, Mapping, Sequence

from e2r.research.page_fetcher import PageFetcher
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)

from ..approval import ExactlyOnceSubmitCoordinator, ProApprovalService
from ..atomic_io import fsync_directory
from ..browser.completion_monitor import (
    BrowserCompletionMonitor,
    ProCompletionStateService,
)
from ..browser.protocol import BrowserCaptureRequest, BrowserUIState
from ..capture.atomic_capture import AtomicCaptureWriter, CaptureIdentity
from ..capture.coordinator import ProCaptureCoordinator
from ..capture.receipt import load_capture_receipt, verify_capture_bundle
from ..config import ProFirstLocalConfig
from ..dossier import (
    DossierValidationContext,
    ResearchDossierDialectAdapter,
    ResearchDossierNormalizer,
    ResearchDossierParser,
    apply_research_dossier_delta,
    bind_dossier_transport_identity,
)
from ..gaps.source_family_policy import source_family_evidence_role
from ..ids import canonical_hash, canonical_json
from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob
from ..multi_pass import (
    FollowupPassPlan,
    ProMultiPassDossierStore,
    ProMultiPassLedger,
    ProMultiPassResearchOrchestrator,
    TransportPendingDecision,
)
from ..operations import (
    PreparedV2BrowserRuntime,
    create_forced_validation_canary,
    prepare_v2_job_in_logged_in_browser,
    recover_submitted_v2_job_in_logged_in_browser,
)
from ..post_import import OperationalProScoringInputProvider
from ..repair import ProVerifierRepairService
from ..research_contracts import select_contract_bundle
from ..saturation import (
    DeterministicQuestionBound,
    ResearchSaturationAdjudicator,
    ResearchSaturationReceipt,
    compile_fixpoint_confirmations,
    compile_route_snapshot_bindings,
    compile_saturation_audit,
)
from ..scoring import ProScoringPipelineService
from ..state_machine import TransitionContext
from ..verification import ProSourceVerificationService, ProSourceVerifier
from ..verification.mechanism_scope_mapper import CodexMechanismScopeMapper
from ..verification.source_verifier import ACCEPTED_SOURCE_STATUSES
from ..dossier.importer import ProDossierImporter


LIVE_CANARY_RECEIPT_SCHEMA = "e2r_pro_first_v2_live_canary_receipt_v1"
LIVE_CANARY_SUITE_SCHEMA = "e2r_pro_first_v2_live_canary_suite_v1"
ProgressHandler = Callable[[Mapping[str, Any]], None]


@dataclass(frozen=True)
class LiveCanarySpec:
    symbol: str
    company_name: str
    archetype_id: str
    as_of_date: str

    def __post_init__(self) -> None:
        if not all(
            value.strip()
            for value in (
                self.symbol,
                self.company_name,
                self.archetype_id,
                self.as_of_date,
            )
        ):
            raise ValueError("live canary scope fields must be nonempty")


@dataclass(frozen=True)
class FollowupCaptureOutcome:
    pass_id: str
    pass_name: str
    parent_pass_id: str
    response_hash: str
    capture_source: str
    response_dossier: Mapping[str, Any]
    effective_dossier: Mapping[str, Any] | None
    semantic_progress: bool
    new_fact_count: int
    new_lineage_count: int
    new_route_count: int
    updated_question_count: int


class LiveCanaryPending(RuntimeError):
    """A safe external/provider/research boundary prevented a false PASS."""

    def __init__(self, reason: str, *, status: str = "RESEARCH_PENDING") -> None:
        super().__init__(reason)
        self.status = status
        self.reason = reason


class ProV2LiveCanaryRunner:
    def __init__(
        self,
        config: ProFirstLocalConfig,
        *,
        repo_root: str | Path,
        progress: ProgressHandler | None = None,
        max_followup_passes: int = 8,
        max_completion_polls: int = 1_440,
        repair_pass_limit: int = 4,
        source_verifier: ProSourceVerifier | None = None,
        scoring_input_provider: OperationalProScoringInputProvider | None = None,
    ) -> None:
        if max_followup_passes < 3:
            raise ValueError("live V2 canary needs room for gap, counter, and audit passes")
        if max_completion_polls < 3:
            raise ValueError("completion poll bound is too small")
        if repair_pass_limit < 1:
            raise ValueError("repair pass limit must be positive")
        self.config = config
        self.repo_root = Path(repo_root).expanduser().resolve()
        self.progress = progress or (lambda _payload: None)
        self.max_followup_passes = max_followup_passes
        self.max_completion_polls = max_completion_polls
        self.repair_pass_limit = repair_pass_limit
        self.store = ProFirstJobStore(config.database_path)
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
        self.scoring_input_provider = scoring_input_provider or (
            OperationalProScoringInputProvider(repo_root=self.repo_root)
        )

    async def run(
        self,
        spec: LiveCanarySpec,
        *,
        existing_job_id: str | None = None,
    ) -> Mapping[str, Any]:
        started = time.monotonic()
        started_at = _utc_now()
        if existing_job_id is None:
            job = create_forced_validation_canary(
                self.store,
                symbol=spec.symbol,
                company_name=spec.company_name,
                as_of_date=spec.as_of_date,
                archetype_ids=(spec.archetype_id,),
            )
        else:
            job = self.store.get_job(existing_job_id)
            expected_scope = (
                spec.symbol,
                spec.company_name,
                spec.as_of_date,
                (spec.archetype_id,),
            )
            actual_scope = (
                job.symbol,
                job.company_name,
                job.as_of_date,
                job.archetype_ids,
            )
            if actual_scope != expected_scope:
                raise ValueError(
                    "resume spec differs from the durable submitted job scope"
                )
        job_root = self.config.runtime_root / "jobs" / job.job_id
        prepared: PreparedV2BrowserRuntime | None = None
        pass_outcomes: list[Mapping[str, Any]] = []
        stage_timings: dict[str, float] = {}
        latest_saturation: ResearchSaturationReceipt | None = None
        source_receipt: Mapping[str, Any] | None = None
        score_receipt: Mapping[str, Any] | None = None
        stagecourt_receipt: Mapping[str, Any] | None = None
        status = "FAILED"
        pending_reason: str | None = None
        try:
            phase_started = time.monotonic()
            if existing_job_id is None:
                prepared = await prepare_v2_job_in_logged_in_browser(
                    self.store,
                    job_id=job.job_id,
                    config=self.config,
                    repo_root=self.repo_root,
                    screenshot_path=job_root / "private/v2_initial_prepared.png",
                )
                stage_timings["browser_prepare_seconds"] = (
                    time.monotonic() - phase_started
                )
                self._emit(job, "INITIAL_PREPARED", prepared.receipt)

                grant = ProApprovalService(self.store).issue(
                    job.job_id,
                    prompt_hash=prepared.prompt.prompt_hash,
                    actor="live-canary-user-authorization-recorder",
                )
                ProApprovalService(self.store).approve(
                    grant,
                    actor="user-approved-in-thread",
                )
                submitted = await ExactlyOnceSubmitCoordinator(self.store).submit(
                    job.job_id,
                    prepared.session.adapter,
                    actor="pro-v2-live-canary-initial-submit",
                )
                self._emit(
                    submitted.job,
                    "INITIAL_SUBMITTED",
                    {"submit_count": submitted.job.submit_count},
                )
            else:
                prepared = await recover_submitted_v2_job_in_logged_in_browser(
                    self.store,
                    job_id=job.job_id,
                    config=self.config,
                    repo_root=self.repo_root,
                    search_terms=(spec.company_name, spec.symbol),
                    screenshot_path=(
                        job_root / "private/v2_recovered_conversation.png"
                    ),
                )
                stage_timings["browser_recovery_seconds"] = (
                    time.monotonic() - phase_started
                )
                self._emit(prepared.job, "INITIAL_CONVERSATION_RECOVERED", prepared.receipt)

            phase_started = time.monotonic()
            if prepared.job.capture_count == 1:
                capture_receipt = load_capture_receipt(
                    job_root / "capture/incoming/browser_capture_receipt.json"
                )
                verify_capture_bundle(job_root, capture_receipt)
                if (
                    capture_receipt.job_id != job.job_id
                    or capture_receipt.run_id
                    != str(prepared.packet_payload["run_id"])
                    or capture_receipt.target_id != job.symbol
                    or capture_receipt.as_of_date != job.as_of_date
                    or capture_receipt.packet_hash != job.packet_hash
                    or capture_receipt.prompt_hash != job.approval_prompt_hash
                    or capture_receipt.conversation_id != job.conversation_id
                ):
                    raise ValueError(
                        "captured initial result differs from the durable submitted job"
                    )
                stage_timings["initial_research_seconds"] = 0.0
                self._emit(
                    prepared.job,
                    "INITIAL_CAPTURE_REUSED",
                    {
                        "capture_source": capture_receipt.capture_source,
                        "report_hash": capture_receipt.report_md_hash,
                        "submit_count": prepared.job.submit_count,
                        "capture_count": prepared.job.capture_count,
                    },
                )
            else:
                if prepared.job.status == JobStatus.RESULT_DETECTED.value:
                    initial_result = await prepared.session.adapter.inspect_result(
                        job_id=job.job_id,
                        run_id=str(prepared.packet_payload["run_id"]),
                    )
                    if not initial_result.structurally_complete:
                        raise LiveCanaryPending(
                            "recovered RESULT_DETECTED page is not structurally complete",
                            status="TRANSPORT_PENDING",
                        )
                else:
                    initial_result = await self._wait_for_initial_result(prepared)
                stage_timings["initial_research_seconds"] = (
                    time.monotonic() - phase_started
                )
                captured_job, capture = await ProCaptureCoordinator(self.store).capture(
                    job.job_id,
                    run_id=str(prepared.packet_payload["run_id"]),
                    expected_filename=prepared.output_filename,
                    expected_report_hash=initial_result.report_hash,
                    job_root=job_root,
                    adapter=prepared.session.adapter,
                    capture_mode="CHATGPT_WEB_VISIBLE_PRO",
                )
                capture_receipt = capture.receipt
                self._emit(
                    captured_job,
                    "INITIAL_CAPTURED",
                    {
                        "capture_source": capture_receipt.capture_source,
                        "report_hash": capture_receipt.report_md_hash,
                    },
                )
            imported = ProDossierImporter(self.store).import_job(
                job.job_id,
                job_root=job_root,
                expected_research_pass_id=prepared.initial_pass_id,
                expected_parent_pass_id=None,
            )
            self._emit(
                imported.job,
                "INITIAL_DOSSIER_IMPORTED",
                {
                    "fact_count": imported.import_receipt["fact_count"],
                    "question_family_count": imported.import_receipt[
                        "question_family_count"
                    ],
                },
            )

            orchestrator = ProMultiPassResearchOrchestrator(
                self.store,
                max_followup_passes=self.max_followup_passes,
            )
            scope = orchestrator.record_completed_initial_pass(
                job.job_id,
                primary_archetype_ids=(spec.archetype_id,),
                response_hash=capture_receipt.report_md_hash,
                initial_pass_id=prepared.initial_pass_id,
            )
            dossier_store = ProMultiPassDossierStore(orchestrator.ledger)
            recovered_state = (
                _load_recovered_snapshot_state(
                    orchestrator.ledger,
                    job_id=job.job_id,
                    job_root=job_root,
                )
                if existing_job_id is not None
                else None
            )
            if recovered_state is None:
                dossier_store.persist(
                    job_id=job.job_id,
                    pass_id=scope.initial_pass_id,
                    dossier=imported.normalized_dossier,
                    job_root=job_root,
                )
                dossier = dict(imported.normalized_dossier)
                pass_outcomes.append(
                    _pass_summary(
                        pass_id=scope.initial_pass_id,
                        pass_name="INITIAL_FULL_RESEARCH",
                        response_hash=capture_receipt.report_md_hash,
                        capture_source=capture_receipt.capture_source,
                        dossier=dossier,
                    )
                )
            else:
                dossier, recovered_outcomes = recovered_state
                dossier = dict(dossier)
                pass_outcomes.extend(recovered_outcomes)
                self._emit(
                    self.store.get_job(job.job_id),
                    "EFFECTIVE_DOSSIER_SNAPSHOT_RECOVERED",
                    {
                        "pass_id": dossier.get("research_pass_id"),
                        "fact_count": len(_all_dossier_fact_ids(dossier)),
                        "question_count": len(
                            tuple(dossier.get("question_family_results") or ())
                        ),
                        "route_receipt_count": len(
                            tuple(dossier.get("search_route_receipts") or ())
                        ),
                        "recovered_pass_count": len(recovered_outcomes),
                    },
                )

            counter_audit_recovered = _has_snapshotted_completed_pass(
                orchestrator.ledger,
                job_id=job.job_id,
                pass_name="COUNTER_SUPERSESSION_CLOSURE",
            )
            if not counter_audit_recovered:
                dossier, public_outcomes = await self._close_public_gaps(
                    prepared=prepared,
                    orchestrator=orchestrator,
                    dossier_store=dossier_store,
                    dossier=dossier,
                    job_root=job_root,
                    phase_label="PRE_COUNTER",
                )
                pass_outcomes.extend(public_outcomes)

                counter_plan = self._plan_counter_audit(
                    orchestrator=orchestrator,
                    packet=prepared.packet_payload,
                    dossier=dossier,
                    archetype_id=spec.archetype_id,
                )
                counter_outcome = await self._execute_followup(
                    prepared=prepared,
                    orchestrator=orchestrator,
                    dossier_store=dossier_store,
                    plan=counter_plan,
                    original_dossier=dossier,
                    job_root=job_root,
                    persist_effective=True,
                )
                dossier = dict(counter_outcome.effective_dossier or dossier)
                pass_outcomes.append(_outcome_summary(counter_outcome, dossier))
            else:
                self._emit(
                    self.store.get_job(job.job_id),
                    "COUNTER_AUDIT_RECOVERED_WITHOUT_RESUBMIT",
                    {"pass_name": "COUNTER_SUPERSESSION_CLOSURE"},
                )

            completed_repair_reprocess_id = (
                _completed_current_repair_reprocess_pass_id(
                    orchestrator.ledger,
                    job_id=job.job_id,
                    dossier=dossier,
                    job_root=job_root,
                )
            )
            if completed_repair_reprocess_id is not None:
                recovery_verification_service = ProSourceVerificationService(
                    self.store,
                    verifier=self.source_verifier,
                )
                recovery_verification = recovery_verification_service.verify_job(
                    job.job_id,
                    job_root=job_root,
                )
                if (
                    recovery_verification.result is None
                    and str(
                        recovery_verification.receipt.get(
                            "verification_semantics_version"
                        )
                        or ""
                    )
                    != self.source_verifier.semantics_version
                ):
                    recovery_verification_service.request_reverification(
                        job.job_id,
                        reason=(
                            "REPAIR_REPROCESS_VERIFIER_SEMANTICS_CHANGED:"
                            f"{recovery_verification.receipt.get('verification_semantics_version')}"
                            f"->{self.source_verifier.semantics_version}"
                        ),
                        maximum_attempts=4,
                    )
                    recovery_verification = (
                        recovery_verification_service.verify_job(
                            job.job_id,
                            job_root=job_root,
                        )
                    )
                (
                    recovery_verification_rows,
                    recovery_claim_links,
                    recovery_compilation_rejections,
                ) = _verification_artifact_rows(recovery_verification)
                (
                    dossier,
                    recovery_outcomes,
                    _recovery_verification_rows,
                    _recovery_claim_links,
                    _recovery_compilation_rejections,
                ) = await self._run_repairs(
                    prepared=prepared,
                    orchestrator=orchestrator,
                    dossier_store=dossier_store,
                    dossier=dossier,
                    job_root=job_root,
                    verification_rows=recovery_verification_rows,
                    claim_links=recovery_claim_links,
                    compilation_rejections=(
                        recovery_compilation_rejections
                    ),
                    recover_completed_pass_id=(
                        completed_repair_reprocess_id
                    ),
                )
                pass_outcomes.extend(recovery_outcomes)
                self._emit(
                    self.store.get_job(job.job_id),
                    "COMPLETED_REPAIR_REPROCESSED_BEFORE_DESCENDANT_CAPTURE",
                    {
                        "pass_id": completed_repair_reprocess_id,
                        "automatic_resubmit_allowed": False,
                        "reprocessed_outcome_count": len(recovery_outcomes),
                        "latest_dossier_hash": canonical_hash(dossier),
                    },
                )

            dossier, public_outcomes = await self._close_public_gaps(
                prepared=prepared,
                orchestrator=orchestrator,
                dossier_store=dossier_store,
                dossier=dossier,
                job_root=job_root,
                phase_label="POST_COUNTER",
            )
            pass_outcomes.extend(public_outcomes)

            phase_started = time.monotonic()
            verification_service = ProSourceVerificationService(
                self.store,
                verifier=self.source_verifier,
            )
            verification = verification_service.verify_job(
                job.job_id,
                job_root=job_root,
            )
            # A recovered completed follow-up snapshot can be newer than the
            # durable verifier receipt even when this invocation produced no
            # new public-pass outcome.  Reusing rejection rows from that old
            # fact roster against the latest dossier can reference facts that
            # a prior repair withdrew or replaced.  Refresh the exact latest
            # hash-bound dossier before compiling any rejection packet.
            if _verification_needs_effective_dossier_reverification(
                verification,
                dossier=dossier,
            ):
                verification_service.request_effective_dossier_reverification(
                    job.job_id,
                    job_root=job_root,
                    reason="PRE_REPAIR_EFFECTIVE_DOSSIER_CHANGED",
                )
                verification = verification_service.verify_job(
                    job.job_id,
                    job_root=job_root,
                )
            if (
                verification.result is None
                and str(
                    verification.receipt.get(
                        "verification_semantics_version"
                    )
                    or ""
                )
                != self.source_verifier.semantics_version
            ):
                verification_service.request_reverification(
                    job.job_id,
                    reason=(
                        "LIVE_CANARY_VERIFIER_SEMANTICS_CHANGED:"
                        f"{verification.receipt.get('verification_semantics_version')}"
                        f"->{self.source_verifier.semantics_version}"
                    ),
                    maximum_attempts=4,
                )
                verification = verification_service.verify_job(
                    job.job_id,
                    job_root=job_root,
                )
            stage_timings["source_verification_seconds"] = (
                time.monotonic() - phase_started
            )
            source_receipt = verification.receipt
            (
                verification_rows,
                claim_links,
                compilation_rejections,
            ) = _verification_artifact_rows(
                verification,
            )
            accepted_ids = _accepted_dossier_fact_ids(
                verification_rows,
                claim_links,
            )
            self._emit(
                verification.job,
                "SOURCE_VERIFICATION_COMPLETE",
                {
                    "candidate_fact_count": source_receipt["candidate_fact_count"],
                    "accepted_candidate_count": len(accepted_ids),
                    "compiled_evidence_fact_count": source_receipt[
                        "compiled_evidence_fact_count"
                    ],
                },
            )

            dossier, repair_outcomes, verification_rows, claim_links, compilation_rejections = (
                await self._run_repairs(
                    prepared=prepared,
                    orchestrator=orchestrator,
                    dossier_store=dossier_store,
                    dossier=dossier,
                    job_root=job_root,
                    verification_rows=verification_rows,
                    claim_links=claim_links,
                    compilation_rejections=compilation_rejections,
                )
            )
            pass_outcomes.extend(repair_outcomes)
            accepted_ids = _accepted_dossier_fact_ids(
                verification_rows,
                claim_links,
            )

            dossier, post_repair_public = await self._close_public_gaps(
                prepared=prepared,
                orchestrator=orchestrator,
                dossier_store=dossier_store,
                dossier=dossier,
                job_root=job_root,
                phase_label="POST_VERIFIER_REPAIR",
            )
            if post_repair_public:
                pass_outcomes.extend(post_repair_public)
                verification_service.request_effective_dossier_reverification(
                    job.job_id,
                    job_root=job_root,
                    reason="POST_REPAIR_PUBLIC_GAP_CLOSURE_CHANGED_DOSSIER",
                )
                verification = verification_service.verify_job(
                    job.job_id,
                    job_root=job_root,
                )
                if verification.result is None:
                    raise RuntimeError("post-repair reverification returned no result")
                source_receipt = verification.receipt
                verification_rows = tuple(
                    row.to_dict() for row in verification.result.verifications
                )
                claim_links = tuple(
                    row.to_dict()
                    for row in verification.result.fact_compilation.claim_fact_links
                )
                compilation_rejections = tuple(
                    row.to_dict()
                    for row in verification.result.fact_compilation.rejected_claims
                )
                dossier, second_repair_outcomes, verification_rows, claim_links, compilation_rejections = (
                    await self._run_repairs(
                        prepared=prepared,
                        orchestrator=orchestrator,
                        dossier_store=dossier_store,
                        dossier=dossier,
                        job_root=job_root,
                        verification_rows=verification_rows,
                        claim_links=claim_links,
                        compilation_rejections=compilation_rejections,
                    )
                )
                pass_outcomes.extend(second_repair_outcomes)
                accepted_ids = _accepted_dossier_fact_ids(
                    verification_rows,
                    claim_links,
                )

            latest_saturation = self._adjudicate_saturation(
                orchestrator.ledger,
                dossier,
                job_root=job_root,
                verified_fact_ids=accepted_ids,
            )
            audit_plan = orchestrator.plan_followup(
                job_id=job.job_id,
                packet=prepared.packet_payload,
                primary_archetype_ids=(spec.archetype_id,),
                pass_name="SATURATION_AUDIT",
                unresolved_question_state=tuple(
                    dossier.get("question_family_results") or ()
                ),
                pass_inputs={
                    "route_reason": "DETERMINISTIC_FULL_THESIS_SATURATION_AUDIT",
                    "verified_fact_ids": list(accepted_ids),
                    "verified_fact_snapshot_hash": latest_saturation.fact_snapshot_hash,
                    "accepted_lineage_roster_hash": (
                        latest_saturation.accepted_lineage_roster_hash
                    ),
                    "deterministic_question_decisions": [
                        row.to_dict() for row in latest_saturation.question_decisions
                    ],
                    "new_research_fact_allowed": False,
                },
                existing_verified_ledger_digest={
                    "verified_fact_ids": list(accepted_ids),
                    "fact_snapshot_hash": latest_saturation.fact_snapshot_hash,
                    "accepted_lineage_roster_hash": (
                        latest_saturation.accepted_lineage_roster_hash
                    ),
                },
            )
            audit_outcome = await self._execute_followup(
                prepared=prepared,
                orchestrator=orchestrator,
                dossier_store=dossier_store,
                plan=_require_plan(audit_plan, "SATURATION_AUDIT"),
                original_dossier=dossier,
                job_root=job_root,
                persist_effective=True,
            )
            prior_fact_ids = set(_all_dossier_fact_ids(dossier))
            dossier = dict(audit_outcome.effective_dossier or dossier)
            pass_outcomes.append(_outcome_summary(audit_outcome, dossier))
            audit_added_fact_ids = set(_all_dossier_fact_ids(dossier)) - prior_fact_ids
            if audit_added_fact_ids:
                verification_service.request_effective_dossier_reverification(
                    job.job_id,
                    job_root=job_root,
                    reason="SATURATION_AUDIT_ADDED_NEW_FACT_CANDIDATES",
                )
                verification = verification_service.verify_job(
                    job.job_id,
                    job_root=job_root,
                )
                if verification.result is None:
                    raise RuntimeError("audit fact reverification returned no result")
                source_receipt = verification.receipt
                verification_rows = tuple(
                    row.to_dict() for row in verification.result.verifications
                )
                claim_links = tuple(
                    row.to_dict()
                    for row in verification.result.fact_compilation.claim_fact_links
                )
                compilation_rejections = tuple(
                    row.to_dict()
                    for row in verification.result.fact_compilation.rejected_claims
                )
                accepted_ids = _accepted_dossier_fact_ids(
                    verification_rows,
                    claim_links,
                )

            latest_saturation = self._adjudicate_saturation(
                orchestrator.ledger,
                dossier,
                job_root=job_root,
                verified_fact_ids=accepted_ids,
            )
            saturation_payload = latest_saturation.to_dict()
            _write_json_atomic(
                job_root / "saturation/research_saturation_receipt.json",
                saturation_payload,
            )
            _write_json_atomic(
                job_root / "saturation/research_saturation_audit.json",
                compile_saturation_audit(latest_saturation),
            )
            if not latest_saturation.research_saturation_valid:
                raise LiveCanaryPending(
                    "deterministic mandatory-question saturation remains incomplete: "
                    + ",".join(latest_saturation.nonterminal_mandatory_question_ids),
                    status=latest_saturation.deterministic_research_status,
                )

            current = self.store.get_job(job.job_id)
            if current.status != JobStatus.GAP_ADJUDICATION.value:
                raise RuntimeError(
                    f"full-thesis component entry requires GAP_ADJUDICATION, got {current.status}"
                )
            current = self.store.transition(
                job.job_id,
                expected_version=current.state_version,
                to_status=JobStatus.COMPONENT_RESEARCH,
                actor="pro-v2-live-canary-saturation-gate",
                idempotency_key=f"full-thesis-entry:{latest_saturation.receipt_hash}",
                context=TransitionContext(research_saturation_valid=True),
                payload={
                    "research_saturation_receipt_hash": latest_saturation.receipt_hash,
                    "component_entry_allowed": True,
                },
            )
            phase_started = time.monotonic()
            inputs = self.scoring_input_provider(current, dossier, job_root)
            scoring = ProScoringPipelineService(self.store).run_job(
                job.job_id,
                job_root=job_root,
                selected_archetype_id=inputs.selected_archetype_id,
                judge_provider=inputs.judge_provider,
                historical_anchors=inputs.historical_anchors,
                validated_impacts=inputs.validated_impacts,
                terminal_evidence=inputs.terminal_evidence or {},
                validity_evidence=inputs.validity_evidence,
                event_overlay_input=inputs.event_overlay_input,
                hard_break_claim_ids=inputs.hard_break_claim_ids,
                research_saturation_receipt=saturation_payload,
            )
            stage_timings["deterministic_scoring_seconds"] = (
                time.monotonic() - phase_started
            )
            score_receipt = scoring.score_receipt
            stagecourt_receipt = scoring.stagecourt_receipt
            if (
                scoring.job.status != JobStatus.FINAL.value
                or score_receipt is None
                or stagecourt_receipt is None
            ):
                pending = (
                    scoring.judge_result.pending_reasons
                    if scoring.judge_result is not None
                    else ("SCORING_PROVIDER_PENDING",)
                )
                raise LiveCanaryPending(
                    ";".join(pending),
                    status="SCORING_PROVIDER_PENDING",
                )
            status = "PRO_FIRST_V2_LIVE_FULL_THESIS_CANARY_PASS"
        except LiveCanaryPending as error:
            status = error.status
            pending_reason = error.reason
            self._emit(
                self.store.get_job(job.job_id),
                "LIVE_CANARY_PENDING",
                {"status": status, "reason": pending_reason},
            )
        except Exception as error:
            status = "FAILED"
            pending_reason = f"{type(error).__name__}: {error}"
            self._emit(
                self.store.get_job(job.job_id),
                "LIVE_CANARY_FAILED",
                {"reason": pending_reason},
            )
        finally:
            if prepared is not None:
                await prepared.close()

        current = self.store.get_job(job.job_id)
        receipt = {
            "schema_version": LIVE_CANARY_RECEIPT_SCHEMA,
            "status": status,
            "job_id": job.job_id,
            "target_id": spec.symbol,
            "company_name": spec.company_name,
            "as_of_date": spec.as_of_date,
            "primary_archetype_id": spec.archetype_id,
            "selection_mode": "FORCED_VALIDATION_CANARY",
            "production_candidate": False,
            "job_status": current.status,
            "submit_count": current.submit_count,
            "capture_count": current.capture_count,
            "research_passes": pass_outcomes,
            "research_pass_count": len(pass_outcomes),
            "followup_pass_count": max(0, len(pass_outcomes) - 1),
            "source_verification": _redact_source_receipt(source_receipt),
            "saturation": (
                _redact_saturation(latest_saturation)
                if latest_saturation is not None
                else None
            ),
            "score": _redact_score_receipt(score_receipt),
            "stagecourt": _redact_stagecourt_receipt(stagecourt_receipt),
            "pending_reason": pending_reason,
            "score_authority": False,
            "stage_authority": False,
            "auto_login_used": False,
            "hidden_chatgpt_api_used": False,
            "raw_report_tracked": False,
            "started_at": started_at,
            "finished_at": _utc_now(),
            "elapsed_seconds": round(time.monotonic() - started, 6),
            "stage_timings": {
                key: round(value, 6) for key, value in sorted(stage_timings.items())
            },
        }
        receipt = {**receipt, "receipt_hash": canonical_hash(receipt)}
        _write_json_atomic(job_root / "canary/live_v2_canary_receipt.json", receipt)
        return receipt

    async def _wait_for_initial_result(self, prepared: PreparedV2BrowserRuntime):
        monitor = BrowserCompletionMonitor(
            prepared.session.adapter,
            required_stable_observations=self.config.browser.required_stable_observations,
            poll_interval_seconds=self.config.browser.poll_interval_seconds,
        )
        service = ProCompletionStateService(self.store, monitor)
        for poll in range(1, self.max_completion_polls + 1):
            job, observation = await service.observe_job(
                prepared.job.job_id,
                run_id=str(prepared.packet_payload["run_id"]),
            )
            if poll == 1 or poll % 12 == 0 or job.status != JobStatus.RESEARCH_RUNNING.value:
                self._emit(
                    job,
                    "INITIAL_COMPLETION_POLL",
                    {
                        "poll": poll,
                        "browser_state": observation.inspection.state.value,
                        "stable_observations": observation.stable_observations,
                    },
                )
            if job.status == JobStatus.RESULT_DETECTED.value and observation.result:
                return observation.result
            if job.status != JobStatus.RESEARCH_RUNNING.value:
                raise LiveCanaryPending(
                    observation.inspection.detail or job.status,
                    status=job.status,
                )
            await asyncio.sleep(self.config.browser.poll_interval_seconds)
        raise LiveCanaryPending("initial Pro completion poll bound reached", status="TRANSPORT_PENDING")

    async def _close_public_gaps(
        self,
        *,
        prepared: PreparedV2BrowserRuntime,
        orchestrator: ProMultiPassResearchOrchestrator,
        dossier_store: ProMultiPassDossierStore,
        dossier: Mapping[str, Any],
        job_root: Path,
        phase_label: str,
    ) -> tuple[Mapping[str, Any], list[Mapping[str, Any]]]:
        outcomes: list[Mapping[str, Any]] = []
        current = dict(dossier)
        while True:
            recovery_plan = _submitted_unsnapshotted_followup_plan(
                orchestrator,
                job_id=prepared.job.job_id,
                pass_name="PUBLIC_GAP_CLOSURE",
            )
            if recovery_plan is not None:
                outcome = await self._execute_followup(
                    prepared=prepared,
                    orchestrator=orchestrator,
                    dossier_store=dossier_store,
                    plan=recovery_plan,
                    original_dossier=current,
                    job_root=job_root,
                    persist_effective=True,
                )
                next_dossier = dict(outcome.effective_dossier or current)
                outcomes.append(_outcome_summary(outcome, next_dossier))
                current = next_dossier
                continue
            provisional_ids = _all_dossier_fact_ids(current)
            saturation = self._adjudicate_saturation(
                orchestrator.ledger,
                current,
                job_root=job_root,
                verified_fact_ids=provisional_ids,
            )
            public_ids = _public_gap_followup_question_ids(saturation)
            if not public_ids:
                return current, outcomes
            unresolved = _question_states_for_ids(current, public_ids)
            plan = orchestrator.plan_followup(
                job_id=prepared.job.job_id,
                packet=prepared.packet_payload,
                primary_archetype_ids=tuple(
                    str(value) for value in current.get("selected_archetypes") or ()
                ),
                pass_name="PUBLIC_GAP_CLOSURE",
                unresolved_question_state=unresolved,
                pass_inputs={
                    "route_reason": "DETERMINISTIC_PUBLIC_MATERIAL_GAP",
                    "phase": phase_label,
                    "question_family_ids": list(public_ids),
                    "fact_snapshot_hash": saturation.fact_snapshot_hash,
                    "accepted_lineage_roster_hash": (
                        saturation.accepted_lineage_roster_hash
                    ),
                    "deterministic_decisions": [
                        row.to_dict()
                        for row in saturation.question_decisions
                        if row.question_family_id in set(public_ids)
                    ],
                },
            )
            outcome = await self._execute_followup(
                prepared=prepared,
                orchestrator=orchestrator,
                dossier_store=dossier_store,
                plan=_require_plan(plan, "PUBLIC_GAP_CLOSURE"),
                original_dossier=current,
                job_root=job_root,
                persist_effective=True,
            )
            next_dossier = dict(outcome.effective_dossier or current)
            outcomes.append(_outcome_summary(outcome, next_dossier))
            if not outcome.semantic_progress:
                raise LiveCanaryPending(
                    "public-gap pass returned no new fact, route, or question disposition",
                    status="TRANSPORT_PENDING",
                )
            current = next_dossier

    def _plan_counter_audit(
        self,
        *,
        orchestrator: ProMultiPassResearchOrchestrator,
        packet: Mapping[str, Any],
        dossier: Mapping[str, Any],
        archetype_id: str,
    ) -> FollowupPassPlan:
        questions = tuple(dossier.get("question_family_results") or ())
        material = tuple(
            row
            for row in questions
            if row.get("could_change_hard_break") is True
            or str(row.get("status") or "") == "CONTRADICTED_UNRESOLVED"
        ) or questions
        plan = orchestrator.plan_followup(
            job_id=str(dossier["job_id"]),
            packet=packet,
            primary_archetype_ids=(archetype_id,),
            pass_name="COUNTER_SUPERSESSION_CLOSURE",
            unresolved_question_state=material,
            pass_inputs={
                "route_reason": "MANDATORY_COUNTER_AND_SUPERSESSION_AUDIT",
                "question_family_ids": [
                    str(row.get("question_family_id") or "") for row in material
                ],
                "existing_counterfact_ids": [
                    str(row.get("dossier_fact_id") or "")
                    for row in dossier.get("counterfacts") or ()
                ],
                "existing_resolution_fact_ids": [
                    str(row.get("dossier_fact_id") or "")
                    for row in dossier.get("resolution_facts") or ()
                ],
            },
        )
        return _require_plan(plan, "COUNTER_SUPERSESSION_CLOSURE")

    async def _execute_followup(
        self,
        *,
        prepared: PreparedV2BrowserRuntime,
        orchestrator: ProMultiPassResearchOrchestrator,
        dossier_store: ProMultiPassDossierStore,
        plan: FollowupPassPlan,
        original_dossier: Mapping[str, Any],
        job_root: Path,
        persist_effective: bool,
    ) -> FollowupCaptureOutcome:
        before_semantic_hash = _research_semantic_hash(original_dossier)
        parent_id = str(plan.research_pass.parent_pass_id or "")
        pass_root = (
            job_root
            / "research_passes"
            / f"{plan.research_pass.pass_ordinal:02d}_{plan.research_pass.pass_id}"
        )
        capture_receipt_path = (
            pass_root / "capture/incoming/browser_capture_receipt.json"
        )
        execution_mode = _followup_execution_mode(
            plan.research_pass,
            pass_root=pass_root,
        )
        if execution_mode == "REUSE_CAPTURE":
            capture_receipt = load_capture_receipt(capture_receipt_path)
            verify_capture_bundle(pass_root, capture_receipt)
            if (
                capture_receipt.job_id != plan.scope.job_id
                or capture_receipt.run_id != str(prepared.packet_payload["run_id"])
                or capture_receipt.target_id != prepared.job.symbol
                or capture_receipt.as_of_date != prepared.job.as_of_date
                or capture_receipt.packet_hash != prepared.job.packet_hash
                or capture_receipt.prompt_hash != plan.prompt_hash
                or capture_receipt.conversation_id != plan.scope.conversation_id
            ):
                raise ValueError(
                    "captured follow-up differs from its durable pass scope"
                )
            report_text = (
                pass_root / capture_receipt.report_md_path
            ).read_text(encoding="utf-8")
            self._emit(
                self.store.get_job(plan.scope.job_id),
                "FOLLOWUP_CAPTURE_REUSED",
                {
                    "pass_id": plan.research_pass.pass_id,
                    "pass_name": plan.research_pass.pass_name,
                    "submit_count": plan.research_pass.submit_count,
                    "capture_source": capture_receipt.capture_source,
                    "response_hash": capture_receipt.report_md_hash,
                },
            )
        else:
            if execution_mode == "RECOVER_SUBMITTED_RESULT":
                self._emit(
                    self.store.get_job(plan.scope.job_id),
                    "FOLLOWUP_SUBMITTED_RESULT_RECOVERY",
                    {
                        "pass_id": plan.research_pass.pass_id,
                        "pass_name": plan.research_pass.pass_name,
                        "submit_count": plan.research_pass.submit_count,
                        "automatic_resubmit_allowed": False,
                    },
                )
            else:
                await orchestrator.prepare_followup(plan, prepared.session.adapter)
                submitted = await orchestrator.submit_followup(
                    plan,
                    prepared.session.adapter,
                )
                self._emit(
                    self.store.get_job(plan.scope.job_id),
                    "FOLLOWUP_SUBMITTED",
                    {
                        "pass_id": plan.research_pass.pass_id,
                        "pass_name": plan.research_pass.pass_name,
                        "pass_ordinal": submitted.research_pass.pass_ordinal,
                    },
                )
            result = await self._wait_for_followup_result(
                prepared=prepared,
                plan=plan,
            )
            report_text = result.report_text
            raw = await prepared.session.adapter.capture_result(
                BrowserCaptureRequest(
                    job_id=plan.scope.job_id,
                    run_id=str(prepared.packet_payload["run_id"]),
                    expected_filename=(
                        f"E2R_PRO_{plan.scope.job_id}_{plan.research_pass.pass_id}.md"
                    ),
                    expected_report_hash=result.report_hash,
                    staging_directory=pass_root / "capture/.staging",
                )
            )
            capture = AtomicCaptureWriter().finalize(
                pass_root,
                identity=CaptureIdentity(
                    job_id=plan.scope.job_id,
                    run_id=str(prepared.packet_payload["run_id"]),
                    target_id=prepared.job.symbol,
                    as_of_date=prepared.job.as_of_date,
                    packet_hash=str(prepared.job.packet_hash or ""),
                    prompt_hash=plan.prompt_hash,
                    conversation_id=plan.scope.conversation_id,
                    capture_mode="CHATGPT_WEB_VISIBLE_PRO_FOLLOWUP",
                ),
                raw_capture=raw,
            )
            capture_receipt = capture.receipt
            if capture_receipt.transport_normalization_operations:
                self._emit(
                    self.store.get_job(plan.scope.job_id),
                    "FOLLOWUP_TRANSPORT_NORMALIZED",
                    {
                        "pass_id": plan.research_pass.pass_id,
                        "assistant_turn_id": capture_receipt.assistant_turn_id,
                        "raw_report_md_hash": capture_receipt.raw_report_md_hash,
                        "normalized_report_md_hash": capture_receipt.report_md_hash,
                        "operations": list(
                            capture_receipt.transport_normalization_operations
                        ),
                        "fact_content_mutation_allowed": False,
                    },
                )
        if report_text.count(
            f"[[E2R_PRO_PASS_ID:{plan.research_pass.pass_id}]]"
        ) != 1:
            raise LiveCanaryPending(
                "follow-up result lacks the exact durable pass marker",
                status="TRANSPORT_PENDING",
            )
        if report_text.count(
            f"[[E2R_PRO_PARENT_PASS_ID:{parent_id}]]"
        ) != 1:
            raise LiveCanaryPending(
                "follow-up result lacks the exact parent pass marker",
                status="TRANSPORT_PENDING",
            )
        durable_after_capture = orchestrator.ledger.get_pass(
            plan.research_pass.pass_id
        )
        if (
            durable_after_capture.status == "TRANSPORT_PENDING"
            and durable_after_capture.submit_count == 1
        ):
            recovered = orchestrator.confirm_transport_pending_result_visible(
                durable_after_capture.pass_id
            )
            self._emit(
                self.store.get_job(plan.scope.job_id),
                "FOLLOWUP_TRANSPORT_TIMEOUT_RESULT_RECOVERED",
                {
                    "pass_id": recovered.pass_id,
                    "pass_name": recovered.pass_name,
                    "submit_count": recovered.submit_count,
                    "automatic_resubmit_allowed": False,
                    "pass_marker_verified": True,
                    "parent_marker_verified": True,
                },
            )
        parsed = ResearchDossierParser().parse(
            downloaded_json_path=(
                pass_root / "capture/incoming/research_dossier.json"
            ),
            report_md_path=pass_root / "capture/incoming/pro_report.md",
        )
        adapted = ResearchDossierDialectAdapter().adapt(
            parsed.payload,
            prior_dossier=original_dossier,
        )
        bound = bind_dossier_transport_identity(
            adapted.payload,
            conversation_id=plan.scope.conversation_id,
            research_pass_id=plan.research_pass.pass_id,
            parent_pass_id=plan.research_pass.parent_pass_id,
            allow_initial_conversation_placeholder=False,
            pass_name=plan.research_pass.pass_name,
            prompt_hash=plan.prompt_hash,
            response_hash=capture_receipt.report_md_hash,
        )
        response_dossier = dict(bound.payload)
        response_dossier["research_passes"] = _durable_pass_rows(
            orchestrator.ledger,
            plan.scope.job_id,
            current_pass_id=plan.research_pass.pass_id,
            current_response_hash=capture_receipt.report_md_hash,
            prior_dossier=original_dossier,
        )
        effective: Mapping[str, Any] | None = None
        new_fact_count = new_lineage_count = new_route_count = updated_question_count = 0
        if persist_effective:
            merge = apply_research_dossier_delta(
                original_dossier=original_dossier,
                response_dossier=response_dossier,
                validation_context=DossierValidationContext(
                    job_id=plan.scope.job_id,
                    run_id=str(prepared.packet_payload["run_id"]),
                    target_id=prepared.job.symbol,
                    as_of_date=prepared.job.as_of_date,
                    conversation_id=plan.scope.conversation_id,
                    candidate_archetype_ids=prepared.job.archetype_ids,
                    research_pass_id=plan.research_pass.pass_id,
                    parent_pass_id=plan.research_pass.parent_pass_id,
                    enforce_parent_pass_id=True,
                ),
            )
            normalized = ResearchDossierNormalizer().normalize(
                merge.effective_dossier
            )
            effective = normalized.payload
            new_fact_count = len(merge.new_fact_ids)
            new_lineage_count = len(merge.new_source_lineage_ids)
            new_route_count = len(merge.new_route_receipt_ids)
            updated_question_count = len(merge.updated_question_family_ids)
        orchestrator.complete_followup(
            plan.research_pass.pass_id,
            response_hash=capture_receipt.report_md_hash,
            conversation_id=plan.scope.conversation_id,
        )
        if effective is not None:
            dossier_store.persist(
                job_id=plan.scope.job_id,
                pass_id=plan.research_pass.pass_id,
                dossier=effective,
                job_root=job_root,
            )
        semantic_progress = bool(
            effective is not None
            and _research_semantic_hash(effective) != before_semantic_hash
        )
        self._emit(
            self.store.get_job(plan.scope.job_id),
            "FOLLOWUP_CAPTURED",
            {
                "pass_id": plan.research_pass.pass_id,
                "pass_name": plan.research_pass.pass_name,
                "capture_source": capture_receipt.capture_source,
                "semantic_progress": semantic_progress,
                "new_fact_count": new_fact_count,
                "new_route_count": new_route_count,
            },
        )
        return FollowupCaptureOutcome(
            pass_id=plan.research_pass.pass_id,
            pass_name=plan.research_pass.pass_name,
            parent_pass_id=parent_id,
            response_hash=capture_receipt.report_md_hash,
            capture_source=capture_receipt.capture_source,
            response_dossier=response_dossier,
            effective_dossier=effective,
            semantic_progress=semantic_progress,
            new_fact_count=new_fact_count,
            new_lineage_count=new_lineage_count,
            new_route_count=new_route_count,
            updated_question_count=updated_question_count,
        )

    async def _wait_for_followup_result(
        self,
        *,
        prepared: PreparedV2BrowserRuntime,
        plan: FollowupPassPlan,
    ):
        monitor = BrowserCompletionMonitor(
            prepared.session.adapter,
            required_stable_observations=self.config.browser.required_stable_observations,
            poll_interval_seconds=self.config.browser.poll_interval_seconds,
        )
        for poll in range(1, self.max_completion_polls + 1):
            observation = await monitor.observe(
                job_id=plan.scope.job_id,
                run_id=str(prepared.packet_payload["run_id"]),
            )
            if poll == 1 or poll % 12 == 0 or observation.completion_confirmed:
                self._emit(
                    self.store.get_job(plan.scope.job_id),
                    "FOLLOWUP_COMPLETION_POLL",
                    {
                        "pass_id": plan.research_pass.pass_id,
                        "pass_name": plan.research_pass.pass_name,
                        "poll": poll,
                        "browser_state": observation.inspection.state.value,
                        "stable_observations": observation.stable_observations,
                    },
                )
            if observation.completion_confirmed and observation.result is not None:
                if observation.result.conversation_id != plan.scope.conversation_id:
                    raise LiveCanaryPending(
                        "follow-up completion escaped the approved conversation",
                        status="TRANSPORT_PENDING",
                    )
                return observation.result
            if observation.inspection.state in {
                BrowserUIState.LOGIN_REQUIRED,
                BrowserUIState.AWAITING_CLARIFICATION,
                BrowserUIState.QUOTA_PENDING,
                BrowserUIState.RETRYABLE_ERROR,
                BrowserUIState.UI_INCOMPATIBLE,
            }:
                raise LiveCanaryPending(
                    observation.inspection.detail
                    or observation.inspection.state.value,
                    status=observation.inspection.state.value,
                )
            await asyncio.sleep(self.config.browser.poll_interval_seconds)
        raise LiveCanaryPending(
            "follow-up completion poll bound reached",
            status="TRANSPORT_PENDING",
        )

    async def _run_repairs(
        self,
        *,
        prepared: PreparedV2BrowserRuntime,
        orchestrator: ProMultiPassResearchOrchestrator,
        dossier_store: ProMultiPassDossierStore,
        dossier: Mapping[str, Any],
        job_root: Path,
        verification_rows: Sequence[Mapping[str, Any]],
        claim_links: Sequence[Mapping[str, Any]],
        compilation_rejections: Sequence[Mapping[str, Any]],
        recover_completed_pass_id: str | None = None,
    ) -> tuple[
        Mapping[str, Any],
        list[Mapping[str, Any]],
        tuple[Mapping[str, Any], ...],
        tuple[Mapping[str, Any], ...],
        tuple[Mapping[str, Any], ...],
    ]:
        current = dict(dossier)
        current_verifications = tuple(verification_rows)
        current_links = tuple(claim_links)
        current_rejections = tuple(compilation_rejections)
        outcomes: list[Mapping[str, Any]] = []
        repair_service = ProVerifierRepairService(
            orchestrator,
            verifier=self.source_verifier,
        )
        if recover_completed_pass_id is not None and (
            str(current.get("research_pass_id") or "")
            != recover_completed_pass_id
        ):
            raise RuntimeError(
                "completed repair reprocessing requires the current dossier pass"
            )
        for repair_ordinal in range(1, self.repair_pass_limit + 1):
            plan = repair_service.plan_repair(
                job_id=prepared.job.job_id,
                job_root=job_root,
                packet=prepared.packet_payload,
                dossier=current,
                verification_rows=current_verifications,
                fact_compilation_rejection_rows=current_rejections,
                primary_archetype_ids=tuple(
                    str(value) for value in current.get("selected_archetypes") or ()
                ),
                existing_verified_ledger_digest={
                    "accepted_dossier_fact_ids": list(
                        _accepted_dossier_fact_ids(
                            current_verifications,
                            current_links,
                        )
                    ),
                    "verification_row_hash": canonical_hash(current_verifications),
                    "claim_fact_link_hash": canonical_hash(current_links),
                },
                recover_research_pass_id=recover_completed_pass_id,
            )
            if not plan.rejection_packets:
                return (
                    current,
                    outcomes,
                    current_verifications,
                    current_links,
                    current_rejections,
                )
            followup = _require_plan(plan.followup, "VERIFIER_REPAIR")
            repair_base = current
            durable_followup = orchestrator.ledger.get_pass(
                followup.research_pass.pass_id
            )
            if (
                durable_followup.status == "COMPLETE"
                and str(current.get("research_pass_id") or "")
                == durable_followup.pass_id
                and durable_followup.parent_pass_id
            ):
                parent_snapshot = dossier_store.load_latest_for_pass(
                    job_id=prepared.job.job_id,
                    pass_id=durable_followup.parent_pass_id,
                    job_root=job_root,
                )
                if parent_snapshot is None:
                    raise RuntimeError(
                        "captured repair reprocessing lacks its exact parent snapshot"
                    )
                repair_base = dict(parent_snapshot.dossier)
                self._emit(
                    self.store.get_job(prepared.job.job_id),
                    "VERIFIER_REPAIR_CAPTURE_REPROCESSING_FROM_EXACT_PARENT",
                    {
                        "pass_id": durable_followup.pass_id,
                        "parent_pass_id": durable_followup.parent_pass_id,
                        "parent_snapshot_id": parent_snapshot.record.snapshot_id,
                        "parent_snapshot_revision_ordinal": (
                            parent_snapshot.record.revision_ordinal
                        ),
                        "automatic_resubmit_allowed": False,
                        "prior_effective_snapshot_preserved": True,
                    },
                )
            captured = await self._execute_followup(
                prepared=prepared,
                orchestrator=orchestrator,
                dossier_store=dossier_store,
                plan=followup,
                original_dossier=repair_base,
                job_root=job_root,
                persist_effective=False,
            )
            repaired = repair_service.apply_response_dossier_and_reverify(
                job=self.store.get_job(prepared.job.job_id),
                job_root=job_root,
                original_dossier=repair_base,
                response_dossier=captured.response_dossier,
                response_hash=captured.response_hash,
                plan=plan,
                prior_verification_rows=current_verifications,
                prior_fact_compilation_rejection_rows=current_rejections,
            )
            normalized = ResearchDossierNormalizer().normalize(
                repaired.effective_dossier
            )
            current = dict(normalized.payload)
            dossier_store.persist(
                job_id=prepared.job.job_id,
                pass_id=captured.pass_id,
                dossier=current,
                job_root=job_root,
            )
            current_verifications = tuple(repaired.source_verification_rows)
            current_links = _read_jsonl(
                repaired.repair_root / "claim_fact_links.jsonl"
            )
            current_rejections = _read_jsonl(
                repaired.repair_root / "fact_compilation_rejections.jsonl"
            )
            summary = _outcome_summary(captured, current)
            summary.update(
                {
                    "repair_ordinal": repair_ordinal,
                    "rejection_packet_count": len(plan.rejection_packets),
                    "unresolved_repair_packet_count": len(
                        repaired.receipt.unresolved_packet_ids
                    ),
                    "preserved_accepted_candidate_count": len(
                        repaired.receipt.preserved_accepted_candidate_ids
                    ),
                }
            )
            outcomes.append(summary)
            if recover_completed_pass_id is not None:
                return (
                    current,
                    outcomes,
                    current_verifications,
                    current_links,
                    current_rejections,
                )
            if not repaired.receipt.unresolved_packet_ids:
                continue
        final_plan = repair_service.plan_repair(
            job_id=prepared.job.job_id,
            job_root=job_root,
            packet=prepared.packet_payload,
            dossier=current,
            verification_rows=current_verifications,
            fact_compilation_rejection_rows=current_rejections,
            primary_archetype_ids=tuple(
                str(value) for value in current.get("selected_archetypes") or ()
            ),
        )
        if final_plan.rejection_packets:
            raise LiveCanaryPending(
                "verifier repair pass bound reached with unresolved material candidates",
                status="VERIFIER_REPAIR_PENDING",
            )
        return (
            current,
            outcomes,
            current_verifications,
            current_links,
            current_rejections,
        )

    def _adjudicate_saturation(
        self,
        ledger: ProMultiPassLedger,
        dossier: Mapping[str, Any],
        *,
        job_root: Path,
        verified_fact_ids: Sequence[str],
    ) -> ResearchSaturationReceipt:
        snapshots = _load_snapshot_dossiers(
            ledger,
            job_id=str(dossier["job_id"]),
            job_root=job_root,
        )
        bindings = compile_route_snapshot_bindings(
            snapshots,
            verified_fact_ids=verified_fact_ids,
        )
        confirmation_compilation = compile_fixpoint_confirmations(
            dossier,
            verified_fact_ids=verified_fact_ids,
            route_snapshot_bindings=bindings.bindings_by_route_receipt_id,
        )
        _write_json_atomic(
            job_root / "saturation/route_snapshot_bindings.json",
            {
                "schema_version": "e2r_pro_route_snapshot_bindings_v1",
                "job_id": dossier["job_id"],
                "bindings": dict(bindings.bindings_by_route_receipt_id),
                "bound_route_receipt_ids": list(bindings.bound_route_receipt_ids),
                "skipped_route_receipt_ids": list(
                    bindings.skipped_route_receipt_ids
                ),
                "binding_hash": canonical_hash(
                    bindings.bindings_by_route_receipt_id
                ),
            },
        )
        return ResearchSaturationAdjudicator().adjudicate(
            dossier=dossier,
            verified_fact_ids=verified_fact_ids,
            deterministic_bounds=_compile_question_bounds(
                dossier,
                verified_fact_ids=verified_fact_ids,
            ),
            fixpoint_confirmations=confirmation_compilation.confirmations,
            verifier_repair_pending_ids=_verifier_pending_question_ids(dossier),
        )

    def _emit(
        self,
        job: ProResearchJob,
        event: str,
        detail: Mapping[str, Any] | None = None,
    ) -> None:
        self.progress(
            {
                "schema_version": "e2r_pro_first_v2_live_progress_v1",
                "event": event,
                "job_id": job.job_id,
                "target_id": job.symbol,
                "job_status": job.status,
                "at": _utc_now(),
                "detail": dict(detail or {}),
            }
        )


async def run_live_canary_suite(
    runner: ProV2LiveCanaryRunner,
    specs: Sequence[LiveCanarySpec],
    *,
    existing_job_ids: Sequence[str | None] | None = None,
) -> Mapping[str, Any]:
    if existing_job_ids is None:
        durable_jobs: tuple[str | None, ...] = (None,) * len(specs)
    else:
        durable_jobs = tuple(existing_job_ids)
        if len(durable_jobs) != len(specs):
            raise ValueError("existing job roster must align exactly with canary specs")
    rows = []
    for spec, existing_job_id in zip(specs, durable_jobs, strict=True):
        rows.append(
            await runner.run(spec, existing_job_id=existing_job_id)
        )
    pass_count = sum(
        row.get("status") == "PRO_FIRST_V2_LIVE_FULL_THESIS_CANARY_PASS"
        for row in rows
    )
    mechanisms = {
        str(row.get("primary_archetype_id") or "")
        for row in rows
        if row.get("status") == "PRO_FIRST_V2_LIVE_FULL_THESIS_CANARY_PASS"
    }
    payload = {
        "schema_version": LIVE_CANARY_SUITE_SCHEMA,
        "status": (
            "PRO_FIRST_V2_OPERATIONAL_RESEARCH_READY"
            if pass_count >= 3 and len(mechanisms) >= 3
            else "PRO_FIRST_V2_LIVE_CANARY_SUITE_PENDING"
        ),
        "canary_count": len(rows),
        "full_thesis_pass_count": pass_count,
        "distinct_mechanism_pass_count": len(mechanisms),
        "canaries": rows,
        "score_authority": False,
        "stage_authority": False,
    }
    return {**payload, "suite_hash": canonical_hash(payload)}


def _compile_question_bounds(
    dossier: Mapping[str, Any],
    *,
    verified_fact_ids: Sequence[str],
) -> Mapping[str, DeterministicQuestionBound]:
    """Compile conservative source-role bounds without target/archetype branches."""

    selected = tuple(str(value) for value in dossier.get("selected_archetypes") or ())
    bundle = select_contract_bundle(selected)
    facts = {
        str(row.get("dossier_fact_id") or ""): row
        for collection in ("material_facts", "counterfacts", "resolution_facts")
        for row in dossier.get(collection) or ()
    }
    verified = frozenset(str(value) for value in verified_fact_ids)
    result_by_id = {
        str(row.get("question_family_id") or ""): row
        for row in dossier.get("question_family_results") or ()
    }
    maxima_by_archetype: dict[str, Mapping[str, float]] = {}
    for archetype_id in selected:
        try:
            contract = load_archetype_scoring_contract(archetype_id)
            maxima_by_archetype[archetype_id] = {
                key: float(value)
                for key, value in contract.component_max_points.items()
            }
        except (FileNotFoundError, KeyError, ValueError):
            maxima_by_archetype[archetype_id] = {}
    bounds: dict[str, DeterministicQuestionBound] = {}
    for contract in bundle.contracts:
        archetype_id = str(contract["archetype_id"])
        maxima = maxima_by_archetype.get(archetype_id, {})
        for question in contract["question_families"]:
            if question.get("mandatory_for_full_thesis") is not True:
                continue
            question_id = str(question["question_family_id"])
            result = result_by_id.get(question_id) or {}
            linked_ids = {
                str(value)
                for key in (
                    "support_fact_ids",
                    "counter_fact_ids",
                    "resolution_fact_ids",
                )
                for value in result.get(key) or ()
            }.intersection(verified)
            verified_roles = {
                str(value)
                for fact_id in linked_ids
                for value in (
                    *(facts.get(fact_id, {}).get("source_role_ids") or ()),
                    facts.get(fact_id, {}).get("source_role_id"),
                    facts.get(fact_id, {}).get("source_family"),
                )
                if str(value or "")
            }
            required_roles = {
                str(value) for value in question.get("required_source_roles") or ()
            }
            missing_roles = required_roles - verified_roles
            missing_core = {
                value
                for value in missing_roles
                if source_family_evidence_role(value) != "SUPPORTING"
            }
            core_verified = any(
                source_family_evidence_role(value) != "SUPPORTING"
                for value in verified_roles
            )
            hard_break = question.get("could_change_hard_break") is True
            stage_boundary = question.get("could_change_stage") is True
            score_material = question.get("could_change_score") is True
            materiality = (
                "HARD_BREAK"
                if hard_break
                else "STAGE_BOUNDARY"
                if stage_boundary
                else "CORE_SCORE"
                if score_material
                else "MONITORING"
            )
            components = tuple(
                str(value) for value in question.get("affected_component_ids") or ()
            )
            bounds[question_id] = DeterministicQuestionBound(
                question_family_id=question_id,
                materiality=materiality,
                component_lower_delta={value: 0.0 for value in components},
                component_upper_delta={
                    value: float(maxima.get(value, 100.0)) for value in components
                },
                deterministic_lower_stage="NO_STAGE_EFFECT",
                deterministic_upper_stage="NO_STAGE_EFFECT",
                hard_break_polarity_resolved=(
                    str(result.get("status") or "") != "CONTRADICTED_UNRESOLVED"
                ),
                missing_predicate_is_new_core=bool(
                    missing_core
                    or not core_verified
                    or hard_break
                    or stage_boundary
                ),
            )
    return bounds


def _question_states_for_ids(
    dossier: Mapping[str, Any],
    question_ids: Sequence[str],
) -> tuple[Mapping[str, Any], ...]:
    requested = tuple(dict.fromkeys(str(value) for value in question_ids))
    by_id = {
        str(row.get("question_family_id") or ""): dict(row)
        for row in dossier.get("question_family_results") or ()
    }
    contract_questions = {
        str(question["question_family_id"]): (contract, question)
        for contract in select_contract_bundle(
            tuple(str(value) for value in dossier.get("selected_archetypes") or ())
        ).contracts
        for question in contract["question_families"]
    }
    rows: list[Mapping[str, Any]] = []
    for question_id in requested:
        if question_id in by_id:
            rows.append(by_id[question_id])
            continue
        contract, question = contract_questions[question_id]
        rows.append(
            {
                "archetype_id": contract["archetype_id"],
                "question_family_id": question_id,
                "status": "UNKNOWN_ROUTE_NOT_YET_TESTED",
                "required_source_roles_missing": list(
                    question["required_source_roles"]
                ),
                "affected_component_ids": list(
                    question["affected_component_ids"]
                ),
                "closure_reason": "initial pass omitted this mandatory question",
            }
        )
    return tuple(rows)


def _durable_pass_rows(
    ledger: ProMultiPassLedger,
    job_id: str,
    *,
    current_pass_id: str,
    current_response_hash: str,
    prior_dossier: Mapping[str, Any] | None = None,
) -> list[Mapping[str, Any]]:
    prior_by_id = {
        str(row.get("pass_id") or ""): row
        for row in (prior_dossier or {}).get("research_passes") or ()
        if isinstance(row, Mapping)
    }
    rows = []
    for record in ledger.list_passes(job_id):
        if record.pass_ordinal > ledger.get_pass(current_pass_id).pass_ordinal:
            continue
        # A zero-submit TRANSPORT_PENDING row is an immutable browser-plan
        # audit record, not a completed research response.  It remains in the
        # SQL pass ledger but must not be fabricated into the dossier's list
        # of actually executed passes.
        if record.status == "TRANSPORT_PENDING" and record.submit_count == 0:
            continue
        response_hash = (
            current_response_hash
            if record.pass_id == current_pass_id
            else record.response_hash
        )
        if not response_hash:
            raise ValueError("durable prior pass is missing its response hash")
        durable_row = {
            "pass_id": record.pass_id,
            "parent_pass_id": record.parent_pass_id,
            "pass_name": record.pass_name,
            "status": "COMPLETE",
            "prompt_hash": record.prompt_hash,
            "response_hash": response_hash,
        }
        prior = prior_by_id.get(record.pass_id)
        if prior is not None and record.pass_id != current_pass_id:
            for key, value in durable_row.items():
                if prior.get(key) != value:
                    raise ValueError(
                        "effective dossier pass row differs from durable ledger: "
                        f"{record.pass_id}.{key}"
                    )
            rows.append(deepcopy(dict(prior)))
            continue
        rows.append(durable_row)
    return rows


def _load_snapshot_dossiers(
    ledger: ProMultiPassLedger,
    *,
    job_id: str,
    job_root: Path,
) -> tuple[Mapping[str, Any], ...]:
    rows = []
    root = job_root.resolve()
    for record in ledger.list_dossier_snapshots(job_id):
        path = (root / record.relative_path).resolve()
        try:
            path.relative_to(root)
        except ValueError as error:
            raise ValueError("dossier snapshot path escapes the job root") from error
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, Mapping) or canonical_hash(payload) != record.dossier_hash:
            raise ValueError("dossier snapshot differs from durable ledger hash")
        rows.append(payload)
    return tuple(rows)


def _verification_artifact_rows(
    verification: Any,
) -> tuple[
    tuple[Mapping[str, Any], ...],
    tuple[Mapping[str, Any], ...],
    tuple[Mapping[str, Any], ...],
]:
    if verification.result is not None:
        return (
            tuple(row.to_dict() for row in verification.result.verifications),
            tuple(
                row.to_dict()
                for row in verification.result.fact_compilation.claim_fact_links
            ),
            tuple(
                row.to_dict()
                for row in verification.result.fact_compilation.rejected_claims
            ),
        )
    root = Path(verification.verification_root)
    rows = _read_jsonl(root / "source_verifications.jsonl")
    links = _read_jsonl(root / "claim_fact_links.jsonl")
    rejections = _read_jsonl(root / "fact_compilation_rejections.jsonl")
    compilation_path = root / "fact_compilation_receipt.json"
    if not compilation_path.is_file():
        raise ValueError("durable verification compilation receipt is missing")
    compilation = json.loads(compilation_path.read_text(encoding="utf-8"))
    expected = canonical_hash(
        {
            "job_id": verification.receipt.get("job_id"),
            "dossier_id": verification.receipt.get("dossier_id"),
            "verification_semantics_version": verification.receipt.get(
                "verification_semantics_version"
            ),
            "verifications": rows,
            "fact_compilation": compilation,
        }
    )
    if expected != verification.receipt.get("verification_hash"):
        raise ValueError("durable verification artifacts differ from their receipt")
    return rows, links, rejections


def _verification_needs_effective_dossier_reverification(
    verification: Any,
    *,
    dossier: Mapping[str, Any],
) -> bool:
    """Detect a stale durable verifier roster before repair compilation."""

    if verification.result is not None:
        return False
    receipt = verification.receipt
    verified_hash = str(
        receipt.get("effective_dossier_hash")
        or receipt.get("normalized_dossier_hash")
        or ""
    )
    return verified_hash != canonical_hash(dossier)


def _load_recovered_snapshot_state(
    ledger: ProMultiPassLedger,
    *,
    job_id: str,
    job_root: Path,
) -> tuple[Mapping[str, Any], tuple[Mapping[str, Any], ...]] | None:
    records = ledger.list_dossier_snapshots(job_id)
    if not records:
        return None
    dossiers = _load_snapshot_dossiers(
        ledger,
        job_id=job_id,
        job_root=job_root,
    )
    if len(records) != len(dossiers):
        raise ValueError("snapshot ledger and dossier roster lengths differ")
    outcomes: list[Mapping[str, Any]] = []
    for record, dossier in zip(records, dossiers, strict=True):
        research_pass = ledger.get_pass(record.pass_id)
        if not research_pass.response_hash:
            raise ValueError("snapshotted pass lacks its durable response hash")
        if research_pass.pass_ordinal == 1:
            capture_path = job_root / "capture/incoming/browser_capture_receipt.json"
        else:
            capture_path = (
                job_root
                / "research_passes"
                / f"{research_pass.pass_ordinal:02d}_{research_pass.pass_id}"
                / "capture/incoming/browser_capture_receipt.json"
            )
        capture_source = "DURABLE_EFFECTIVE_DOSSIER_SNAPSHOT"
        if capture_path.is_file():
            capture_source = load_capture_receipt(capture_path).capture_source
        outcomes.append(
            {
                **_pass_summary(
                    pass_id=research_pass.pass_id,
                    pass_name=research_pass.pass_name,
                    response_hash=research_pass.response_hash,
                    capture_source=capture_source,
                    dossier=dossier,
                ),
                "parent_pass_id": research_pass.parent_pass_id,
                "recovered_from_durable_snapshot": True,
            }
        )
    return dossiers[-1], tuple(outcomes)


def _has_snapshotted_completed_pass(
    ledger: ProMultiPassLedger,
    *,
    job_id: str,
    pass_name: str,
) -> bool:
    snapshotted = {
        record.pass_id for record in ledger.list_dossier_snapshots(job_id)
    }
    return any(
        row.pass_id in snapshotted
        and row.pass_name == pass_name
        and row.status == "COMPLETE"
        for row in ledger.list_passes(job_id)
    )


def _all_dossier_fact_ids(dossier: Mapping[str, Any]) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(
            str(row.get("dossier_fact_id") or "")
            for collection in ("material_facts", "counterfacts", "resolution_facts")
            for row in dossier.get(collection) or ()
            if str(row.get("dossier_fact_id") or "")
        )
    )


def _accepted_dossier_fact_ids(
    verification_rows: Sequence[Mapping[str, Any]],
    claim_fact_links: Sequence[Mapping[str, Any]],
) -> tuple[str, ...]:
    compiled_claim_ids = {
        str(row.get("claim_id") or "")
        for row in claim_fact_links
        if str(row.get("claim_id") or "")
    }
    return tuple(
        dict.fromkeys(
            str(row.get("dossier_fact_id") or "")
            for row in verification_rows
            if str(row.get("status") or "") in ACCEPTED_SOURCE_STATUSES
            and str(row.get("compiled_claim_id") or "") in compiled_claim_ids
            and str(row.get("dossier_fact_id") or "")
        )
    )


def _material_rejected_rows(
    verification_rows: Sequence[Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    return tuple(
        row
        for row in verification_rows
        if str(row.get("status") or "") not in ACCEPTED_SOURCE_STATUSES
    )


def _verifier_pending_question_ids(dossier: Mapping[str, Any]) -> tuple[str, ...]:
    return tuple(
        str(row.get("question_family_id") or "")
        for row in dossier.get("question_family_results") or ()
        if str(row.get("status") or "") == "VERIFIER_REPAIR_REQUIRED"
    )


def _public_gap_followup_question_ids(
    saturation: ResearchSaturationReceipt,
) -> tuple[str, ...]:
    """Route only missing/public questions, never verifier work, to gap search."""

    blocked = {
        *saturation.verifier_repair_pending_ids,
        *saturation.provider_parser_core_pending_question_ids,
        *saturation.lifecycle_hard_break_pending_ids,
    }
    candidates = dict.fromkeys(
        (
            *saturation.missing_mandatory_question_ids,
            *saturation.public_material_gap_question_ids,
        )
    )
    return tuple(value for value in candidates if value not in blocked)


def _submitted_unsnapshotted_followup_plan(
    orchestrator: ProMultiPassResearchOrchestrator,
    *,
    job_id: str,
    pass_name: str,
) -> FollowupPassPlan | None:
    """Recover a transmitted pass before applying newer routing semantics."""

    for research_pass in reversed(orchestrator.ledger.list_passes(job_id)):
        if (
            research_pass.pass_name != pass_name
            or research_pass.submit_count != 1
            or research_pass.status not in {"RESEARCH_RUNNING", "COMPLETE"}
            or orchestrator.ledger.latest_dossier_snapshot_for_pass(
                job_id=job_id,
                pass_id=research_pass.pass_id,
            )
            is not None
        ):
            continue
        scope = orchestrator.ledger.get_scope(job_id)
        if scope is None:
            raise RuntimeError("submitted follow-up lacks its durable approval scope")
        return FollowupPassPlan(
            scope=scope,
            research_pass=research_pass,
            prompt_text="",
            prompt_hash=research_pass.prompt_hash,
        )
    return None


def _completed_current_repair_reprocess_pass_id(
    ledger: ProMultiPassLedger,
    *,
    job_id: str,
    dossier: Mapping[str, Any],
    job_root: Path,
) -> str | None:
    """Find one captured repair whose proposals were applied as a no-op.

    The repair must still be the latest snapshot.  Once a descendant snapshot
    exists, revising the historical pass would violate append-only lineage.
    """

    pass_id = str(dossier.get("research_pass_id") or "")
    if not pass_id:
        return None
    research_pass = ledger.get_pass(pass_id)
    if (
        research_pass.job_id != job_id
        or research_pass.pass_name != "VERIFIER_REPAIR"
        or research_pass.status != "COMPLETE"
        or research_pass.submit_count != 1
        or not research_pass.response_hash
    ):
        return None
    pass_snapshot = ledger.latest_dossier_snapshot_for_pass(
        job_id=job_id,
        pass_id=pass_id,
    )
    latest_snapshot = ledger.latest_dossier_snapshot(job_id)
    if (
        pass_snapshot is None
        or latest_snapshot is None
        or pass_snapshot.snapshot_id != latest_snapshot.snapshot_id
        or pass_snapshot.revision_ordinal != 1
    ):
        return None
    repair_receipt_path = job_root / "repair/verifier_repair_receipt.json"
    if not repair_receipt_path.is_file():
        return None
    repair_receipt = json.loads(repair_receipt_path.read_text(encoding="utf-8"))
    if str(repair_receipt.get("research_pass_id") or "") != pass_id:
        return None
    resolutions = tuple(repair_receipt.get("resolutions") or ())
    if resolutions:
        repaired_path = job_root / "repair/effective_repaired_dossier.json"
        if not repaired_path.is_file():
            raise RuntimeError(
                "completed repair receipt exists without its effective dossier"
            )
        repaired = json.loads(repaired_path.read_text(encoding="utf-8"))
        if canonical_hash(repaired) != str(
            repair_receipt.get("effective_dossier_hash") or ""
        ):
            raise RuntimeError(
                "completed repair artifact differs from its durable receipt"
            )
        normalized_repaired = ResearchDossierNormalizer().normalize(
            repaired
        ).payload
        if canonical_hash(normalized_repaired) == pass_snapshot.dossier_hash:
            return None
    pass_root = (
        job_root
        / "research_passes"
        / f"{research_pass.pass_ordinal:02d}_{pass_id}"
    )
    captured_path = pass_root / "capture/incoming/research_dossier.json"
    if not captured_path.is_file():
        return None
    captured = ResearchDossierParser().parse(
        downloaded_json_path=captured_path
    ).payload
    proposals = tuple(captured.get("verification_repair_register") or ())
    if not proposals:
        return None
    return pass_id


def _research_semantic_hash(dossier: Mapping[str, Any]) -> str:
    return canonical_hash(
        {
            key: dossier.get(key)
            for key in (
                "business_model",
                "material_facts",
                "counterfacts",
                "resolution_facts",
                "question_family_results",
                "component_research",
                "structured_metrics",
                "unresolved_gaps",
                "source_lineages",
                "search_route_receipts",
                "verification_repair_register",
            )
        }
    )


def _followup_execution_mode(research_pass: Any, *, pass_root: Path) -> str:
    """Choose a crash-safe follow-up path without ever guessing about submit.

    A durable running pass with ``submit_count=1`` is already transmitted.
    Missing capture files therefore mean "recover the visible result", never
    "prepare and send again".
    """

    ready = (pass_root / "capture/incoming/READY.json").is_file()
    receipt = (
        pass_root / "capture/incoming/browser_capture_receipt.json"
    ).is_file()
    if ready != receipt:
        raise RuntimeError("follow-up capture bundle is only partially committed")
    status = str(research_pass.status)
    submit_count = int(research_pass.submit_count)
    if status in {"RESEARCH_RUNNING", "TRANSPORT_PENDING"} and submit_count == 1:
        return "REUSE_CAPTURE" if ready else "RECOVER_SUBMITTED_RESULT"
    if status == "COMPLETE" and submit_count == 1 and ready:
        return "REUSE_CAPTURE"
    if status in {"PLANNED", "PREPARED"} and submit_count == 0 and not ready:
        return "PREPARE_AND_SUBMIT"
    raise RuntimeError(
        "follow-up pass has no unambiguous exactly-once execution path: "
        f"status={status}, submit_count={submit_count}, capture_ready={ready}"
    )


def _require_plan(
    value: FollowupPassPlan | TransportPendingDecision | None,
    pass_name: str,
) -> FollowupPassPlan:
    if isinstance(value, TransportPendingDecision):
        raise LiveCanaryPending(value.reason, status=value.research_status)
    if not isinstance(value, FollowupPassPlan):
        raise LiveCanaryPending(
            f"{pass_name} had no executable bounded follow-up plan",
            status="TRANSPORT_PENDING",
        )
    return value


def _pass_summary(
    *,
    pass_id: str,
    pass_name: str,
    response_hash: str,
    capture_source: str,
    dossier: Mapping[str, Any],
) -> Mapping[str, Any]:
    return {
        "pass_id": pass_id,
        "pass_name": pass_name,
        "response_hash": response_hash,
        "capture_source": capture_source,
        "fact_count": len(_all_dossier_fact_ids(dossier)),
        "question_count": len(tuple(dossier.get("question_family_results") or ())),
        "route_receipt_count": len(tuple(dossier.get("search_route_receipts") or ())),
        "score_authority": False,
        "stage_authority": False,
    }


def _outcome_summary(
    outcome: FollowupCaptureOutcome,
    dossier: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        **_pass_summary(
            pass_id=outcome.pass_id,
            pass_name=outcome.pass_name,
            response_hash=outcome.response_hash,
            capture_source=outcome.capture_source,
            dossier=dossier,
        ),
        "parent_pass_id": outcome.parent_pass_id,
        "semantic_progress": outcome.semantic_progress,
        "new_fact_count": outcome.new_fact_count,
        "new_lineage_count": outcome.new_lineage_count,
        "new_route_count": outcome.new_route_count,
        "updated_question_count": outcome.updated_question_count,
    }


def _redact_source_receipt(
    receipt: Mapping[str, Any] | None,
) -> Mapping[str, Any] | None:
    if receipt is None:
        return None
    allowed = (
        "status",
        "verification_id",
        "verification_hash",
        "verification_semantics_version",
        "verification_attempt",
        "candidate_fact_count",
        "accepted_fact_candidate_count",
        "compiled_evidence_fact_count",
        "full_document_fetch_count",
        "document_cache_reuse_count",
        "source_document_count",
        "query_count",
        "search_count",
        "fact_graph_ready",
        "effective_dossier_snapshot_id",
        "effective_dossier_pass_id",
        "effective_dossier_hash",
    )
    return {key: receipt.get(key) for key in allowed}


def _redact_saturation(
    receipt: ResearchSaturationReceipt,
) -> Mapping[str, Any]:
    return {
        "status": (
            "FULL_THESIS_READY"
            if receipt.research_saturation_valid
            else "RESEARCH_SATURATION_PENDING"
        ),
        "receipt_hash": receipt.receipt_hash,
        "expected_mandatory_question_count": len(
            receipt.expected_mandatory_question_ids
        ),
        "nonterminal_mandatory_question_count": len(
            receipt.nonterminal_mandatory_question_ids
        ),
        "public_material_gap_count": len(
            receipt.public_material_gap_question_ids
        ),
        "verifier_repair_pending_count": len(
            receipt.verifier_repair_pending_ids
        ),
        "provider_parser_core_pending_count": len(
            receipt.provider_parser_core_pending_question_ids
        ),
        "lifecycle_hard_break_pending_count": len(
            receipt.lifecycle_hard_break_pending_ids
        ),
        "source_linkage_incomplete_count": len(
            receipt.source_linkage_incomplete_question_ids
        ),
        "research_saturation_valid": receipt.research_saturation_valid,
        "component_entry_allowed": receipt.component_entry_allowed,
    }


def _redact_score_receipt(
    receipt: Mapping[str, Any] | None,
) -> Mapping[str, Any] | None:
    if receipt is None:
        return None
    return {
        key: receipt.get(key)
        for key in (
            "score_receipt_id",
            "score_hash",
            "score",
            "total_points",
            "score_interval_lower",
            "score_interval_upper",
            "score_valid",
            "component_count",
            "judge_decision_count",
        )
    }


def _redact_stagecourt_receipt(
    receipt: Mapping[str, Any] | None,
) -> Mapping[str, Any] | None:
    if receipt is None:
        return None
    return {
        key: receipt.get(key)
        for key in (
            "stagecourt_receipt_id",
            "stagecourt_hash",
            "canonical_stage",
            "stage",
            "stage_status",
            "publication_status",
        )
    }


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def _write_json_atomic(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_suffix(path.suffix + ".part")
    with part.open("w", encoding="utf-8") as stream:
        stream.write(canonical_json(payload) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(part, path)
    fsync_directory(path.parent)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


__all__ = [
    "LIVE_CANARY_RECEIPT_SCHEMA",
    "LIVE_CANARY_SUITE_SCHEMA",
    "LiveCanaryPending",
    "LiveCanarySpec",
    "ProV2LiveCanaryRunner",
    "run_live_canary_suite",
]
