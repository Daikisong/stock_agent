"""Resume a verified fresh V3 canary through the same-chat full-thesis tail.

The initial ChatGPT Pro request is immutable and is never resubmitted here.
Every follow-up is derived from the deterministic question-closure receipt,
claimed exactly once in the durable pass ledger, and sent only in the already
approved conversation.  Pro may add evidence; score and Stage remain owned by
the deterministic services.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import time
from typing import Any, Callable, Mapping, Sequence

from e2r.research.page_fetcher import PageFetcher

from ..atomic_io import fsync_directory
from ..browser.protocol import BrowserCaptureRequest
from ..browser.worker import BrowserWorkerSession, ProBrowserWorker
from ..canary.live_v2 import (
    FollowupCaptureOutcome,
    LiveCanaryPending,
    ProV2LiveCanaryRunner,
    _accepted_dossier_fact_ids,
    _followup_execution_mode,
    _outcome_summary,
    _question_states_for_ids,
    _redact_saturation,
    _submitted_unsnapshotted_followup_plan,
    _verification_artifact_rows,
    _verification_needs_effective_dossier_reverification,
)
from ..capture.atomic_capture import AtomicCaptureWriter, CaptureIdentity
from ..capture.receipt import load_capture_receipt, verify_capture_bundle
from ..config import ProFirstLocalConfig
from ..ids import canonical_hash, canonical_json
from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob
from ..multi_pass import (
    FollowupPassPlan,
    ProMultiPassDossierStore,
    ProMultiPassLedger,
)
from ..post_import import OperationalProScoringInputProvider
from ..repair import CompactRepairServiceV3, RepairDeltaV3Parser
from ..saturation import ResearchSaturationReceipt, compile_saturation_audit
from ..scoring import ProScoringPipelineService
from ..state_machine import TransitionContext
from ..verification import (
    CodexMechanismScopeMapper,
    ProSourceVerificationService,
    ProSourceVerifier,
)
from .boundary import (
    FreshSessionBoundary,
    FreshSessionBoundaryService,
    OldAnswerLeakageManifest,
)
from .orchestrator_v3 import (
    BuiltFreshV3JobPacket,
    FreshSessionOrchestratorV3,
)


FRESH_FULL_THESIS_AUTHORIZATION_PHRASE = (
    "YES-I-AUTHORIZE-SAME-CONVERSATION-FULL-THESIS"
)
FRESH_FULL_THESIS_RECEIPT_SCHEMA = "e2r_pro_fresh_v3_full_thesis_receipt_v1"
ProgressHandler = Callable[[Mapping[str, Any]], None]


@dataclass
class PreparedFreshV3TailRuntime:
    """The three attributes shared by the generic follow-up executor."""

    job: ProResearchJob
    packet_payload: Mapping[str, Any]
    session: BrowserWorkerSession

    async def close(self) -> None:
        await self.session.close()


@dataclass(frozen=True)
class FreshVerificationState:
    receipt: Mapping[str, Any]
    verification_rows: tuple[Mapping[str, Any], ...]
    claim_links: tuple[Mapping[str, Any], ...]
    compilation_rejections: tuple[Mapping[str, Any], ...]
    rejection_classifications: tuple[Mapping[str, Any], ...]
    accepted_fact_ids: tuple[str, ...]


class FreshV3FullThesisLiveRunner(ProV2LiveCanaryRunner):
    """Continue one successful fresh initial run until final or truthfully pending."""

    def __init__(
        self,
        config: ProFirstLocalConfig,
        *,
        fresh_runtime_root: str | Path,
        state_database_path: str | Path,
        repo_root: str | Path,
        progress: ProgressHandler | None = None,
        max_completion_polls: int = 1_440,
        max_tail_iterations: int = 12,
        source_verifier: ProSourceVerifier | None = None,
        scoring_input_provider: OperationalProScoringInputProvider | None = None,
    ) -> None:
        if max_completion_polls < config.browser.required_stable_observations:
            raise ValueError("completion poll bound is smaller than the stable-result gate")
        if max_tail_iterations < 3:
            raise ValueError("full-thesis tail needs public, counter, and audit room")
        # Deliberately do not call the V2 constructor: it would create a second
        # SQLite file below the fresh artifact root before we can replace it.
        self.config = config
        self.fresh_runtime_root = Path(fresh_runtime_root).expanduser().resolve()
        self.repo_root = Path(repo_root).expanduser().resolve()
        self.progress = progress or (lambda _payload: None)
        self.max_followup_passes = max_tail_iterations
        self.max_completion_polls = max_completion_polls
        self.repair_pass_limit = 1
        self.max_tail_iterations = max_tail_iterations
        self.store = ProFirstJobStore(
            Path(state_database_path).expanduser().resolve()
        )
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

    async def run(self, *, job_id: str) -> Mapping[str, Any]:
        started = time.monotonic()
        boundary = self._load_boundary(job_id)
        job_root = boundary.fresh_job_root
        orchestrator = FreshSessionOrchestratorV3(self.store, boundary)
        packet_manifest = _read_json(
            job_root / "packet/packet_manifest.json"
        )
        built = orchestrator.load_initial_packet_for_submitted_recovery(
            commit_sha=str(packet_manifest.get("commit_sha") or ""),
            config_hash=str(packet_manifest.get("config_hash") or ""),
        )
        dossier_store = ProMultiPassDossierStore(orchestrator.ledger)
        snapshot = dossier_store.load_latest(job_id=job_id, job_root=job_root)
        if snapshot is None:
            raise ValueError("fresh full-thesis tail requires the initial dossier snapshot")
        dossier = dict(snapshot.dossier)
        if dossier.get("schema_version") != "e2r_pro_research_dossier_v3":
            raise ValueError("fresh full-thesis tail requires ResearchDossierV3")
        if self.store.get_job(job_id).status != JobStatus.GAP_ADJUDICATION.value:
            raise ValueError("fresh full-thesis tail must start at GAP_ADJUDICATION")

        session = await ProBrowserWorker(self.config.browser).open(job_id=job_id)
        prepared: PreparedFreshV3TailRuntime | None = None
        pass_outcomes: list[Mapping[str, Any]] = []
        latest_saturation: ResearchSaturationReceipt | None = None
        verification_state: FreshVerificationState | None = None
        score_receipt: Mapping[str, Any] | None = None
        stagecourt_receipt: Mapping[str, Any] | None = None
        status = "FRESH_FULL_THESIS_PENDING"
        pending_reason: str | None = None
        try:
            recovered = await session.adapter.recover_conversation_without_submit(
                job_id=job_id,
                run_id=str(built.packet_payload["run_id"]),
                search_terms=(
                    str(self.store.get_job(job_id).conversation_id or ""),
                    self.store.get_job(job_id).company_name,
                    self.store.get_job(job_id).symbol,
                ),
            )
            durable_conversation = str(
                self.store.get_job(job_id).conversation_id or ""
            )
            if recovered.conversation_id != durable_conversation:
                raise ValueError(
                    "visible ChatGPT page differs from the approved fresh conversation"
                )
            prepared = PreparedFreshV3TailRuntime(
                job=self.store.get_job(job_id),
                packet_payload=built.packet_payload,
                session=session,
            )
            self._emit_fresh(
                "FRESH_FULL_THESIS_CONVERSATION_RECOVERED",
                job_id=job_id,
                conversation_id=durable_conversation,
                browser_submit_delta=0,
            )

            for iteration in range(1, self.max_tail_iterations + 1):
                recovery_plan = _submitted_unsnapshotted_fresh_nonrepair_plan(
                    orchestrator,
                    job_id=job_id,
                )
                if recovery_plan is not None:
                    self._emit_fresh(
                        "FRESH_FULL_THESIS_SUBMITTED_PASS_RECOVERY",
                        job_id=job_id,
                        pass_id=recovery_plan.research_pass.pass_id,
                        pass_name=recovery_plan.research_pass.pass_name,
                        submit_count=recovery_plan.research_pass.submit_count,
                        browser_submit_delta=0,
                    )
                    outcome = await self._execute_followup(
                        prepared=prepared,
                        orchestrator=orchestrator,
                        dossier_store=dossier_store,
                        plan=recovery_plan,
                        original_dossier=dossier,
                        job_root=job_root,
                        persist_effective=True,
                    )
                    next_dossier = dict(outcome.effective_dossier or dossier)
                    pass_outcomes.append(_outcome_summary(outcome, next_dossier))
                    if (
                        recovery_plan.research_pass.pass_name
                        in {
                            "PUBLIC_GAP_CLOSURE",
                            "COUNTER_SUPERSESSION_CLOSURE",
                        }
                        and not outcome.semantic_progress
                    ):
                        raise LiveCanaryPending(
                            "recovered follow-up produced no deterministic semantic progress",
                            status="RESEARCH_NO_PROGRESS_PENDING",
                        )
                    dossier = next_dossier
                    continue

                verification_state = self._load_current_verification(
                    job_id=job_id,
                    job_root=job_root,
                    dossier=dossier,
                )
                latest_saturation = self._adjudicate_saturation(
                    orchestrator.ledger,
                    dossier,
                    job_root=job_root,
                    verified_fact_ids=verification_state.accepted_fact_ids,
                )
                self._persist_saturation(job_root, latest_saturation)
                self._emit_fresh(
                    "FRESH_FULL_THESIS_ITERATION",
                    job_id=job_id,
                    iteration=iteration,
                    saturation=_redact_saturation(latest_saturation),
                    accepted_fact_count=len(verification_state.accepted_fact_ids),
                )

                public_ids = _public_followup_question_ids(latest_saturation)
                public_context = _followup_context(
                    dossier=dossier,
                    saturation=latest_saturation,
                    accepted_fact_ids=verification_state.accepted_fact_ids,
                    question_ids=public_ids,
                    pass_name="PUBLIC_GAP_CLOSURE",
                )
                public_ids = _question_ids_without_completed_context(
                    orchestrator.ledger,
                    job_id=job_id,
                    pass_name="PUBLIC_GAP_CLOSURE",
                    context=public_context,
                )
                if (
                    tuple(
                        public_context["pass_inputs"]["question_family_ids"]
                    )
                    != public_ids
                ):
                    public_context = _followup_context(
                        dossier=dossier,
                        saturation=latest_saturation,
                        accepted_fact_ids=verification_state.accepted_fact_ids,
                        question_ids=public_ids,
                        pass_name="PUBLIC_GAP_CLOSURE",
                    )
                if public_ids and not _context_already_attempted(
                    orchestrator.ledger,
                    job_id=job_id,
                    pass_name="PUBLIC_GAP_CLOSURE",
                    research_gap_context_hash=str(
                        public_context["pass_inputs"][
                            "research_gap_context_hash"
                        ]
                    ),
                ):
                    plan, _compiled = orchestrator.plan_v3_followup(
                        built,
                        pass_name="PUBLIC_GAP_CLOSURE",
                        latest_dossier_digest=public_context[
                            "latest_dossier_digest"
                        ],
                        unresolved_question_state=public_context[
                            "unresolved_question_state"
                        ],
                        pass_inputs=public_context["pass_inputs"],
                    )
                    outcome = await self._execute_followup(
                        prepared=prepared,
                        orchestrator=orchestrator,
                        dossier_store=dossier_store,
                        plan=plan,
                        original_dossier=dossier,
                        job_root=job_root,
                        persist_effective=True,
                    )
                    next_dossier = dict(outcome.effective_dossier or dossier)
                    pass_outcomes.append(_outcome_summary(outcome, next_dossier))
                    if not outcome.semantic_progress:
                        raise LiveCanaryPending(
                            "public-gap follow-up produced no deterministic semantic progress",
                            status="RESEARCH_NO_PROGRESS_PENDING",
                        )
                    dossier = next_dossier
                    continue

                counter_ids = _counter_followup_question_ids(latest_saturation)
                counter_context = _followup_context(
                    dossier=dossier,
                    saturation=latest_saturation,
                    accepted_fact_ids=verification_state.accepted_fact_ids,
                    question_ids=counter_ids,
                    pass_name="COUNTER_SUPERSESSION_CLOSURE",
                )
                counter_ids = _question_ids_without_completed_context(
                    orchestrator.ledger,
                    job_id=job_id,
                    pass_name="COUNTER_SUPERSESSION_CLOSURE",
                    context=counter_context,
                )
                if (
                    tuple(
                        counter_context["pass_inputs"]["question_family_ids"]
                    )
                    != counter_ids
                ):
                    counter_context = _followup_context(
                        dossier=dossier,
                        saturation=latest_saturation,
                        accepted_fact_ids=verification_state.accepted_fact_ids,
                        question_ids=counter_ids,
                        pass_name="COUNTER_SUPERSESSION_CLOSURE",
                    )
                if counter_ids and not _context_already_attempted(
                    orchestrator.ledger,
                    job_id=job_id,
                    pass_name="COUNTER_SUPERSESSION_CLOSURE",
                    research_gap_context_hash=str(
                        counter_context["pass_inputs"][
                            "research_gap_context_hash"
                        ]
                    ),
                ):
                    plan, _compiled = orchestrator.plan_v3_followup(
                        built,
                        pass_name="COUNTER_SUPERSESSION_CLOSURE",
                        latest_dossier_digest=counter_context[
                            "latest_dossier_digest"
                        ],
                        unresolved_question_state=counter_context[
                            "unresolved_question_state"
                        ],
                        pass_inputs=counter_context["pass_inputs"],
                    )
                    outcome = await self._execute_followup(
                        prepared=prepared,
                        orchestrator=orchestrator,
                        dossier_store=dossier_store,
                        plan=plan,
                        original_dossier=dossier,
                        job_root=job_root,
                        persist_effective=True,
                    )
                    next_dossier = dict(outcome.effective_dossier or dossier)
                    pass_outcomes.append(_outcome_summary(outcome, next_dossier))
                    if not outcome.semantic_progress:
                        raise LiveCanaryPending(
                            "counter/supersession follow-up produced no semantic progress",
                            status="RESEARCH_NO_PROGRESS_PENDING",
                        )
                    dossier = next_dossier
                    continue

                repairable = _repairable_classifications(
                    verification_state.rejection_classifications
                )
                if repairable:
                    completed_repairs = tuple(
                        row
                        for row in orchestrator.ledger.list_passes(job_id)
                        if row.pass_name == "VERIFIER_REPAIR"
                        and row.status == "COMPLETE"
                    )
                    if completed_repairs:
                        raise LiveCanaryPending(
                            "one compact V3 repair was already used and material verifier candidates remain",
                            status="VERIFIER_REPAIR_PENDING",
                        )
                    dossier, repair_summary = await self._execute_compact_repair(
                        prepared=prepared,
                        orchestrator=orchestrator,
                        built=built,
                        dossier_store=dossier_store,
                        dossier=dossier,
                        job_root=job_root,
                        verification_state=verification_state,
                    )
                    pass_outcomes.append(repair_summary)
                    continue

                audit_context = _followup_context(
                    dossier=dossier,
                    saturation=latest_saturation,
                    accepted_fact_ids=verification_state.accepted_fact_ids,
                    question_ids=latest_saturation.expected_mandatory_question_ids,
                    pass_name="SATURATION_AUDIT",
                )
                if not _context_already_attempted(
                    orchestrator.ledger,
                    job_id=job_id,
                    pass_name="SATURATION_AUDIT",
                    research_gap_context_hash=str(
                        audit_context["pass_inputs"][
                            "research_gap_context_hash"
                        ]
                    ),
                ):
                    plan, _compiled = orchestrator.plan_v3_followup(
                        built,
                        pass_name="SATURATION_AUDIT",
                        latest_dossier_digest=audit_context[
                            "latest_dossier_digest"
                        ],
                        unresolved_question_state=audit_context[
                            "unresolved_question_state"
                        ],
                        pass_inputs=audit_context["pass_inputs"],
                    )
                    outcome = await self._execute_followup(
                        prepared=prepared,
                        orchestrator=orchestrator,
                        dossier_store=dossier_store,
                        plan=plan,
                        original_dossier=dossier,
                        job_root=job_root,
                        persist_effective=True,
                    )
                    dossier = dict(outcome.effective_dossier or dossier)
                    pass_outcomes.append(_outcome_summary(outcome, dossier))
                    continue

                if not latest_saturation.research_saturation_valid:
                    raise LiveCanaryPending(
                        "deterministic full-thesis conditions remain incomplete after all changed contexts were attempted",
                        status=latest_saturation.deterministic_research_status,
                    )

                current = self.store.get_job(job_id)
                if current.status != JobStatus.GAP_ADJUDICATION.value:
                    raise RuntimeError(
                        "full-thesis component entry requires GAP_ADJUDICATION"
                    )
                current = self.store.transition(
                    job_id,
                    expected_version=current.state_version,
                    to_status=JobStatus.COMPONENT_RESEARCH,
                    actor="fresh-v3-full-thesis-saturation-gate",
                    idempotency_key=(
                        f"fresh-full-thesis-entry:{latest_saturation.receipt_hash}"
                    ),
                    context=TransitionContext(research_saturation_valid=True),
                    payload={
                        "research_saturation_receipt_hash": (
                            latest_saturation.receipt_hash
                        ),
                        "component_entry_allowed": True,
                    },
                )
                inputs = self.scoring_input_provider(current, dossier, job_root)
                scoring = ProScoringPipelineService(self.store).run_job(
                    job_id,
                    job_root=job_root,
                    selected_archetype_id=inputs.selected_archetype_id,
                    judge_provider=inputs.judge_provider,
                    historical_anchors=inputs.historical_anchors,
                    validated_impacts=inputs.validated_impacts,
                    terminal_evidence=inputs.terminal_evidence or {},
                    validity_evidence=inputs.validity_evidence,
                    event_overlay_input=inputs.event_overlay_input,
                    hard_break_claim_ids=inputs.hard_break_claim_ids,
                    research_saturation_receipt=latest_saturation.to_dict(),
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
                        ";".join(pending), status="SCORING_PROVIDER_PENDING"
                    )
                status = "FRESH_V3_FULL_THESIS_FINAL"
                break
            else:
                raise LiveCanaryPending(
                    "full-thesis tail iteration bound reached without a false completion",
                    status="RESEARCH_ITERATION_BOUND_PENDING",
                )
        except LiveCanaryPending as error:
            status = error.status
            pending_reason = error.reason
        finally:
            if prepared is not None:
                await prepared.close()
            else:
                await session.close()

        current = self.store.get_job(job_id)
        receipt_payload = {
            "schema_version": FRESH_FULL_THESIS_RECEIPT_SCHEMA,
            "status": status,
            "job_id": job_id,
            "run_id": built.packet_payload["run_id"],
            "conversation_id": current.conversation_id,
            "target_id": current.symbol,
            "as_of_date": current.as_of_date,
            "job_status": current.status,
            "research_passes": pass_outcomes,
            "latest_effective_dossier_hash": canonical_hash(dossier),
            "source_verification_hash": (
                verification_state.receipt.get("verification_hash")
                if verification_state is not None
                else None
            ),
            "saturation": (
                _redact_saturation(latest_saturation)
                if latest_saturation is not None
                else None
            ),
            "score": score_receipt,
            "stagecourt": stagecourt_receipt,
            "pending_reason": pending_reason,
            "score_authority": False,
            "stage_authority": False,
            "automatic_initial_resubmit_allowed": False,
            "hidden_chatgpt_api_used": False,
            "finished_at": _utc_now(),
            "elapsed_seconds": round(time.monotonic() - started, 6),
        }
        receipt = {
            **receipt_payload,
            "receipt_hash": canonical_hash(receipt_payload),
        }
        _write_json_atomic(
            job_root / "canary/fresh_v3_full_thesis_receipt.json",
            receipt,
        )
        return receipt

    def inspect_current(self, *, job_id: str) -> Mapping[str, Any]:
        """Read-only deterministic status; this never opens or sends ChatGPT."""

        boundary = self._load_boundary(job_id)
        orchestrator = FreshSessionOrchestratorV3(self.store, boundary)
        snapshot = ProMultiPassDossierStore(orchestrator.ledger).load_latest(
            job_id=job_id,
            job_root=boundary.fresh_job_root,
        )
        if snapshot is None:
            raise ValueError("fresh canary has no effective dossier snapshot")
        dossier = dict(snapshot.dossier)
        verification = self._load_current_verification(
            job_id=job_id,
            job_root=boundary.fresh_job_root,
            dossier=dossier,
            allow_reverification=False,
        )
        saturation = self._adjudicate_saturation(
            orchestrator.ledger,
            dossier,
            job_root=boundary.fresh_job_root,
            verified_fact_ids=verification.accepted_fact_ids,
        )
        public_ids = _public_followup_question_ids(saturation)
        return {
            "schema_version": "e2r_pro_fresh_v3_full_thesis_inspection_v1",
            "job_id": job_id,
            "job_status": self.store.get_job(job_id).status,
            "effective_dossier_hash": canonical_hash(dossier),
            "accepted_fact_count": len(verification.accepted_fact_ids),
            "repairable_candidate_count": len(
                _repairable_classifications(
                    verification.rejection_classifications
                )
            ),
            "next_public_question_ids": list(public_ids),
            "saturation": _redact_saturation(saturation),
            "browser_submit_count_delta": 0,
            "score_authority": False,
            "stage_authority": False,
        }

    def _load_boundary(self, job_id: str) -> FreshSessionBoundary:
        manifest = _load_leakage_manifest(self.fresh_runtime_root)
        boundary, job = FreshSessionBoundaryService(self.store).load_existing(
            fresh_runtime_root=self.fresh_runtime_root,
            leakage_manifest=manifest,
        )
        if job.job_id != job_id:
            raise ValueError("fresh runtime boundary belongs to another job")
        return boundary

    def _load_current_verification(
        self,
        *,
        job_id: str,
        job_root: Path,
        dossier: Mapping[str, Any],
        allow_reverification: bool = True,
    ) -> FreshVerificationState:
        service = ProSourceVerificationService(
            self.store,
            verifier=self.source_verifier,
        )
        verification = service.verify_job(job_id, job_root=job_root)
        if _verification_needs_effective_dossier_reverification(
            verification,
            dossier=dossier,
        ):
            if not allow_reverification:
                raise ValueError(
                    "read-only inspection found a stale verification receipt"
                )
            service.request_effective_dossier_reverification(
                job_id,
                job_root=job_root,
                reason="FRESH_V3_FULL_THESIS_EFFECTIVE_DOSSIER_CHANGED",
            )
            verification = service.verify_job(job_id, job_root=job_root)
        rows, links, compilation_rejections = _verification_artifact_rows(
            verification
        )
        classifications = _read_jsonl(
            verification.verification_root / "rejection_classifications.jsonl"
        )
        return FreshVerificationState(
            receipt=verification.receipt,
            verification_rows=rows,
            claim_links=links,
            compilation_rejections=compilation_rejections,
            rejection_classifications=classifications,
            accepted_fact_ids=_accepted_dossier_fact_ids(rows, links),
        )

    async def _execute_compact_repair(
        self,
        *,
        prepared: PreparedFreshV3TailRuntime,
        orchestrator: FreshSessionOrchestratorV3,
        built: BuiltFreshV3JobPacket,
        dossier_store: ProMultiPassDossierStore,
        dossier: Mapping[str, Any],
        job_root: Path,
        verification_state: FreshVerificationState,
    ) -> tuple[Mapping[str, Any], Mapping[str, Any]]:
        plan, compiled = orchestrator.plan_compact_repair(
            built,
            dossier=dossier,
            rejection_classifications=(
                verification_state.rejection_classifications
            ),
            verification_rows=verification_state.verification_rows,
            job_root=job_root,
        )
        pass_root = (
            job_root
            / "research_passes"
            / f"{plan.research_pass.pass_ordinal:02d}_{plan.research_pass.pass_id}"
        )
        receipt_path = pass_root / "capture/incoming/browser_capture_receipt.json"
        mode = _followup_execution_mode(
            plan.research_pass,
            pass_root=pass_root,
        )
        if mode == "REUSE_CAPTURE":
            capture_receipt = load_capture_receipt(receipt_path)
            verify_capture_bundle(pass_root, capture_receipt)
        else:
            if mode == "PREPARE_AND_SUBMIT":
                await orchestrator.prepare_followup(plan, prepared.session.adapter)
                await orchestrator.submit_followup(plan, prepared.session.adapter)
            result = await self._wait_for_followup_result(
                prepared=prepared,
                plan=plan,
            )
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
            capture_receipt = AtomicCaptureWriter().finalize(
                pass_root,
                identity=CaptureIdentity(
                    job_id=plan.scope.job_id,
                    run_id=str(prepared.packet_payload["run_id"]),
                    target_id=prepared.job.symbol,
                    as_of_date=prepared.job.as_of_date,
                    packet_hash=str(prepared.job.packet_hash or ""),
                    prompt_hash=plan.prompt_hash,
                    conversation_id=plan.scope.conversation_id,
                    capture_mode="CHATGPT_WEB_VISIBLE_PRO_FRESH_V3_REPAIR",
                ),
                raw_capture=raw,
            ).receipt
        report_text = (
            pass_root / capture_receipt.report_md_path
        ).read_text(encoding="utf-8")
        pass_id = plan.research_pass.pass_id
        parent_id = str(plan.research_pass.parent_pass_id or "")
        if report_text.count(f"[[E2R_PRO_PASS_ID:{pass_id}]]") != 1:
            raise LiveCanaryPending(
                "compact repair lacks the exact pass marker",
                status="TRANSPORT_PENDING",
            )
        if report_text.count(f"[[E2R_PRO_PARENT_PASS_ID:{parent_id}]]") != 1:
            raise LiveCanaryPending(
                "compact repair lacks the exact parent marker",
                status="TRANSPORT_PENDING",
            )
        durable = orchestrator.ledger.get_pass(pass_id)
        if durable.status == "TRANSPORT_PENDING" and durable.submit_count == 1:
            orchestrator.confirm_transport_pending_result_visible(pass_id)
        parsed = RepairDeltaV3Parser().parse_text(report_text)
        repaired = CompactRepairServiceV3(
            verifier=self.source_verifier
        ).apply_and_reverify(
            job=self.store.get_job(prepared.job.job_id),
            job_root=job_root,
            dossier=dossier,
            repair_delta=parsed.payload,
            compiled_prompt=compiled,
            prior_verification_rows=verification_state.verification_rows,
            response_hash=capture_receipt.report_md_hash,
        )
        orchestrator.complete_followup(
            pass_id,
            response_hash=capture_receipt.report_md_hash,
            conversation_id=plan.scope.conversation_id,
        )
        effective = dict(repaired.effective_dossier)
        dossier_store.persist(
            job_id=prepared.job.job_id,
            pass_id=pass_id,
            dossier=effective,
            job_root=job_root,
        )
        return effective, {
            "pass_id": pass_id,
            "pass_name": "VERIFIER_REPAIR",
            "parent_pass_id": parent_id,
            "response_hash": capture_receipt.report_md_hash,
            "capture_source": capture_receipt.capture_source,
            "candidate_count": len(compiled.candidate_ids),
            "repair_action_count": len(repaired.application.outcomes),
            "operational_ready_allowed": repaired.receipt.get(
                "operational_ready_allowed"
            ),
            "score_authority": False,
            "stage_authority": False,
        }

    @staticmethod
    def _persist_saturation(
        job_root: Path,
        saturation: ResearchSaturationReceipt,
    ) -> None:
        _write_json_atomic(
            job_root / "saturation/research_saturation_receipt.json",
            saturation.to_dict(),
        )
        _write_json_atomic(
            job_root / "saturation/research_saturation_audit.json",
            compile_saturation_audit(saturation),
        )

    def _emit_fresh(self, phase: str, **payload: Any) -> None:
        self.progress(
            {
                "schema_version": "e2r_pro_fresh_v3_full_thesis_progress_v1",
                "phase": phase,
                "observed_at": _utc_now(),
                **payload,
            }
        )


def _load_leakage_manifest(root: Path) -> OldAnswerLeakageManifest:
    payload = _read_json(root / "old_answer_leakage_manifest.runtime.json")
    unsigned = dict(payload)
    manifest_hash = str(unsigned.pop("manifest_hash", ""))
    if canonical_hash(unsigned) != manifest_hash:
        raise ValueError("fresh old-answer leakage manifest hash mismatch")
    return OldAnswerLeakageManifest(
        old_job_id=str(payload.get("old_job_id") or ""),
        old_run_id=str(payload.get("old_run_id") or ""),
        old_conversation_id=str(payload.get("old_conversation_id") or ""),
        old_fact_ids=tuple(payload.get("old_fact_ids") or ()),
        old_route_receipt_ids=tuple(
            payload.get("old_route_receipt_ids") or ()
        ),
        old_research_pass_ids=tuple(
            payload.get("old_research_pass_ids") or ()
        ),
        old_question_answers=tuple(
            payload.get("old_question_answers") or ()
        ),
        old_score_values=tuple(payload.get("old_score_values") or ()),
        old_stage_values=tuple(payload.get("old_stage_values") or ()),
        expected_source_urls=tuple(
            payload.get("expected_source_urls") or ()
        ),
        expected_fact_ids=tuple(payload.get("expected_fact_ids") or ()),
    )


def _followup_context(
    *,
    dossier: Mapping[str, Any],
    saturation: ResearchSaturationReceipt,
    accepted_fact_ids: Sequence[str],
    question_ids: Sequence[str],
    pass_name: str,
) -> Mapping[str, Any]:
    requested = tuple(dict.fromkeys(str(value) for value in question_ids))
    verified = frozenset(str(value) for value in accepted_fact_ids)
    route_by_id = {
        str(row.get("route_receipt_id") or ""): row
        for row in dossier.get("search_route_receipts") or ()
    }
    decisions = {
        row.question_family_id: row.to_dict()
        for row in saturation.question_decisions
    }
    unresolved = []
    dossier_states = {
        str(row.get("question_family_id") or ""): dict(row)
        for row in _question_states_for_ids(dossier, requested)
    }
    for question_id in requested:
        decision = decisions.get(question_id) or {}
        state = dossier_states.get(question_id) or {}
        route_progress_state = _question_route_progress_state(
            decision=decision,
            question_state=state,
            route_by_id=route_by_id,
            verified_fact_ids=verified,
        )
        unresolved.append(
            {
                "question_family_id": question_id,
                "reported_status": state.get("status"),
                "availability_class": state.get("availability_class"),
                "closure_reason": state.get("closure_reason"),
                "required_source_roles_missing": list(
                    state.get("required_source_roles_missing") or ()
                ),
                "search_route_receipt_ids": list(
                    state.get("search_route_receipt_ids") or ()
                ),
                "deterministic_status": decision.get(
                    "deterministic_status"
                ),
                "gap_class": decision.get("gap_class"),
                "failure_codes": list(decision.get("failure_codes") or ()),
                "verified_linked_fact_ids": list(
                    decision.get("verified_linked_fact_ids") or ()
                ),
                "linked_source_lineage_ids": list(
                    decision.get("linked_source_lineage_ids") or ()
                ),
                "linked_route_receipt_ids": list(
                    (
                        decision.get("route_adequacy") or {}
                    ).get("linked_route_receipt_ids")
                    or ()
                ),
                "missing_core_source_roles": list(
                    decision.get("missing_core_source_roles") or ()
                ),
                "missing_corroboration_source_roles": list(
                    decision.get("missing_corroboration_source_roles") or ()
                ),
                "verified_source_roles": list(
                    decision.get("verified_source_roles") or ()
                ),
                "deterministic_terminal": decision.get("terminal"),
                "deterministic_ready": decision.get("ready"),
                "route_progress_state": route_progress_state,
            }
        )
    fact_count = sum(
        len(tuple(dossier.get(key) or ()))
        for key in ("material_facts", "counterfacts", "resolution_facts")
    )
    question_context_hashes = {
        row["question_family_id"]: canonical_hash(
            {
                "pass_name": pass_name,
                "question_family_id": row["question_family_id"],
                "reported_status": row["reported_status"],
                "availability_class": row["availability_class"],
                "required_source_roles_missing": row[
                    "required_source_roles_missing"
                ],
                "search_route_receipt_ids": row[
                    "search_route_receipt_ids"
                ],
                "deterministic_status": row["deterministic_status"],
                "gap_class": row["gap_class"],
                "failure_codes": row["failure_codes"],
                "verified_linked_fact_ids": row[
                    "verified_linked_fact_ids"
                ],
                "missing_core_source_roles": row[
                    "missing_core_source_roles"
                ],
                "linked_source_lineage_ids": row[
                    "linked_source_lineage_ids"
                ],
                "linked_route_receipt_ids": row[
                    "linked_route_receipt_ids"
                ],
            }
        )
        for row in unresolved
    }
    # This second identity deliberately excludes append-only receipt ids and
    # raw Pro dispositions.  A repeated route with a new receipt id is not
    # research progress; a genuinely different route signature, a changed
    # provider/parser outcome, a newly verified fact/lineage, or a
    # deterministic closure is progress.  Keep the older context hash for
    # immutable audit compatibility while routing on this semantic identity.
    question_progress_hashes = {
        row["question_family_id"]: canonical_hash(
            {
                "schema_version": "e2r_question_progress_identity_v1",
                "pass_name": pass_name,
                "question_family_id": row["question_family_id"],
                "deterministic_status": row["deterministic_status"],
                "deterministic_terminal": row["deterministic_terminal"],
                "deterministic_ready": row["deterministic_ready"],
                "gap_class": row["gap_class"],
                "failure_codes": sorted(set(row["failure_codes"])),
                "verified_linked_fact_ids": sorted(
                    set(row["verified_linked_fact_ids"])
                ),
                "missing_core_source_roles": sorted(
                    set(row["missing_core_source_roles"])
                ),
                "missing_corroboration_source_roles": sorted(
                    set(row["missing_corroboration_source_roles"])
                ),
                "verified_source_roles": sorted(
                    set(row["verified_source_roles"])
                ),
                "linked_source_lineage_ids": sorted(
                    set(row["linked_source_lineage_ids"])
                ),
                "route_progress_state": row["route_progress_state"],
            }
        )
        for row in unresolved
    }
    gap_context_hash = canonical_hash(
        {
            "pass_name": pass_name,
            "question_progress_hashes": question_progress_hashes,
        }
    )
    return {
        "latest_dossier_digest": {
            "schema_version": dossier.get("schema_version"),
            "dossier_hash": canonical_hash(dossier),
            "research_pass_id": dossier.get("research_pass_id"),
            "research_status": dossier.get("research_status"),
            "source_document_count": len(
                tuple(dossier.get("source_documents") or ())
            ),
            "fact_count": fact_count,
            "question_count": len(
                tuple(dossier.get("question_family_results") or ())
            ),
            "route_receipt_count": len(
                tuple(dossier.get("search_route_receipts") or ())
            ),
            "verified_fact_ids": list(accepted_fact_ids),
            "fact_snapshot_hash": saturation.fact_snapshot_hash,
            "accepted_lineage_roster_hash": (
                saturation.accepted_lineage_roster_hash
            ),
        },
        "unresolved_question_state": unresolved,
        "pass_inputs": {
            "route_reason": (
                "DETERMINISTIC_FULL_THESIS_SATURATION_AUDIT"
                if pass_name == "SATURATION_AUDIT"
                else "MANDATORY_COUNTER_AND_SUPERSESSION_AUDIT"
                if pass_name == "COUNTER_SUPERSESSION_CLOSURE"
                else "DETERMINISTIC_PUBLIC_PROVIDER_PARSER_OR_LINKAGE_GAP"
            ),
            "question_family_ids": list(requested),
            "question_context_hashes": question_context_hashes,
            "question_progress_hashes": question_progress_hashes,
            "deterministic_research_status": (
                saturation.deterministic_research_status
            ),
            "research_gap_context_hash": gap_context_hash,
            "new_research_fact_allowed": pass_name != "SATURATION_AUDIT",
            "score_authority": False,
            "stage_authority": False,
        },
    }


def _question_route_progress_state(
    *,
    decision: Mapping[str, Any],
    question_state: Mapping[str, Any],
    route_by_id: Mapping[str, Mapping[str, Any]],
    verified_fact_ids: frozenset[str],
) -> Mapping[str, Any]:
    """Compile receipt-id-insensitive progress for one question gap.

    Route receipts are append-only audit rows, so their ids necessarily
    change on every pass.  Progress instead follows the route signature and
    the newest cohort's deterministic outcome.  Pro-claimed accepted ids are
    intersected with the source verifier's accepted roster.
    """

    route_adequacy = decision.get("route_adequacy") or {}
    requested_ids = tuple(
        str(value)
        for value in (
            route_adequacy.get("linked_route_receipt_ids")
            or question_state.get("search_route_receipt_ids")
            or ()
        )
    )
    linked = tuple(
        route_by_id[value] for value in requested_ids if value in route_by_id
    )

    def signature(row: Mapping[str, Any]) -> str:
        return canonical_hash(
            {
                "source_role_id": row.get("source_role_id"),
                "query_or_navigation_objective": row.get(
                    "query_or_navigation_objective"
                ),
                "query_text": row.get("query_text"),
                "opened_source_urls": sorted(
                    row.get("opened_source_urls") or ()
                ),
            }
        )

    route_signatures = tuple(sorted({signature(row) for row in linked}))
    latest_pass_id = str(linked[-1].get("pass_id") or "") if linked else ""
    latest_cohort = tuple(
        row
        for row in linked
        if str(row.get("pass_id") or "") == latest_pass_id
    )
    latest_outcome_by_hash = {}
    for row in latest_cohort:
        outcome = {
            "route_signature": signature(row),
            "provider_status": row.get("provider_status"),
            "parser_status": row.get("parser_status", "SUCCESS"),
            "verified_accepted_fact_ids": sorted(
                verified_fact_ids.intersection(
                    str(value)
                    for value in row.get("accepted_fact_ids") or ()
                )
            ),
            "no_new_route_confirmed": bool(
                str(row.get("no_new_route_reason") or "").strip()
            ),
        }
        latest_outcome_by_hash[canonical_hash(outcome)] = outcome
    latest_outcomes = tuple(
        latest_outcome_by_hash[key] for key in sorted(latest_outcome_by_hash)
    )
    return {
        "route_signatures": route_signatures,
        "latest_route_outcomes": latest_outcomes,
        "unknown_linked_route_reference": len(requested_ids) != len(linked),
        "attempted_source_roles": sorted(
            {
                str(value)
                for value in question_state.get("attempted_source_role_ids")
                or ()
            }
            | {
                str(row.get("source_role_id") or "")
                for row in linked
                if str(row.get("source_role_id") or "")
            }
        ),
        "adequate": route_adequacy.get("adequate"),
        "official_route_attempted": route_adequacy.get(
            "official_route_attempted"
        ),
        "distinct_route_count": route_adequacy.get("distinct_route_count"),
        "independent_no_new_route_confirmation_count": route_adequacy.get(
            "independent_no_new_route_confirmation_count"
        ),
        "provider_parser_normal": route_adequacy.get(
            "provider_parser_normal"
        ),
        "semantic_fixpoint": route_adequacy.get("semantic_fixpoint"),
        "failure_codes": sorted(set(route_adequacy.get("failure_codes") or ())),
    }


def _public_followup_question_ids(
    saturation: ResearchSaturationReceipt,
) -> tuple[str, ...]:
    blocked = {
        *saturation.verifier_repair_pending_ids,
        *saturation.lifecycle_hard_break_pending_ids,
    }
    return tuple(
        value
        for value in dict.fromkeys(
            (
                *saturation.missing_mandatory_question_ids,
                *saturation.public_material_gap_question_ids,
                *saturation.provider_parser_core_pending_question_ids,
                *saturation.source_linkage_incomplete_question_ids,
            )
        )
        if value not in blocked
    )


def _counter_followup_question_ids(
    saturation: ResearchSaturationReceipt,
) -> tuple[str, ...]:
    hard_break = tuple(
        row.question_family_id
        for row in saturation.question_decisions
        if row.materiality == "HARD_BREAK"
        or row.status == "CONTRADICTED_UNRESOLVED"
    )
    return tuple(
        dict.fromkeys(
            (*saturation.lifecycle_hard_break_pending_ids, *hard_break)
        )
    )


def _repairable_classifications(
    rows: Sequence[Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    return tuple(
        row
        for row in rows
        if row.get("send_to_pro_allowed") is True
        and row.get("material") is True
    )


def _context_already_attempted(
    ledger: ProMultiPassLedger,
    *,
    job_id: str,
    pass_name: str,
    research_gap_context_hash: str,
) -> bool:
    return any(
        row.pass_name == pass_name
        and str(row.detail.get("research_gap_context_hash") or "")
        == research_gap_context_hash
        and row.status == "COMPLETE"
        and row.submit_count == 1
        for row in ledger.list_passes(job_id)
    )


def _question_ids_without_completed_context(
    ledger: ProMultiPassLedger,
    *,
    job_id: str,
    pass_name: str,
    context: Mapping[str, Any],
) -> tuple[str, ...]:
    """Return only question states not already sent and completed unchanged.

    A pass can contain several questions.  If one question closes while
    another remains byte-for-byte identical, the latter must not be sent
    again merely because the global dossier snapshot changed.  Completed
    per-question hashes preserve that append-only attempt identity.
    """

    pass_inputs = context.get("pass_inputs") or {}
    current_progress = pass_inputs.get("question_progress_hashes") or {}
    current_context = pass_inputs.get("question_context_hashes") or {}
    requested = tuple(
        str(value)
        for value in pass_inputs.get("question_family_ids") or ()
    )
    if not isinstance(current_progress, Mapping):
        raise ValueError("question_progress_hashes must be a mapping")
    if not isinstance(current_context, Mapping):
        raise ValueError("question_context_hashes must be a mapping")
    attempted_progress: dict[str, set[str]] = {}
    attempted_context: dict[str, set[str]] = {}
    for row in ledger.list_passes(job_id):
        if (
            row.pass_name != pass_name
            or row.status != "COMPLETE"
            or row.submit_count != 1
        ):
            continue
        stored_progress = row.detail.get("question_progress_hashes")
        if isinstance(stored_progress, Mapping):
            for question_id, progress_hash in stored_progress.items():
                attempted_progress.setdefault(str(question_id), set()).add(
                    str(progress_hash)
                )
        stored_context = row.detail.get("question_context_hashes")
        if isinstance(stored_context, Mapping):
            for question_id, context_hash in stored_context.items():
                attempted_context.setdefault(str(question_id), set()).add(
                    str(context_hash)
                )
    return tuple(
        question_id
        for question_id in requested
        if (
            str(current_progress.get(question_id) or "")
            not in attempted_progress.get(question_id, set())
            and str(current_context.get(question_id) or "")
            not in attempted_context.get(question_id, set())
        )
    )


_FRESH_NONREPAIR_FOLLOWUP_NAMES = (
    "PUBLIC_GAP_CLOSURE",
    "COUNTER_SUPERSESSION_CLOSURE",
    "SATURATION_AUDIT",
)


def _submitted_unsnapshotted_fresh_nonrepair_plan(
    orchestrator: FreshSessionOrchestratorV3,
    *,
    job_id: str,
) -> FollowupPassPlan | None:
    """Recover already-sent work before applying a newly computed route.

    A code or verification change can alter the next pass type while ChatGPT
    is still answering the already submitted pass.  The durable submitted
    pass always wins: capture and snapshot it with submit delta zero, then
    recompute the next action from the merged dossier.
    """

    matches = tuple(
        row
        for row in (
            _submitted_unsnapshotted_followup_plan(
                orchestrator,
                job_id=job_id,
                pass_name=pass_name,
            )
            for pass_name in _FRESH_NONREPAIR_FOLLOWUP_NAMES
        )
        if row is not None
    )
    if len(matches) > 1:
        raise ValueError("multiple submitted fresh follow-ups lack snapshots")
    return matches[0] if matches else None


def _read_json(path: Path) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"JSON artifact must be an object: {path}")
    return payload


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
    "FRESH_FULL_THESIS_AUTHORIZATION_PHRASE",
    "FreshV3FullThesisLiveRunner",
    "FreshVerificationState",
    "PreparedFreshV3TailRuntime",
]
