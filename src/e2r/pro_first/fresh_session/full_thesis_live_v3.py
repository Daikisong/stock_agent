"""Resume a verified fresh V3 canary through the same-chat full-thesis tail.

The initial ChatGPT Pro request is immutable and is never resubmitted here.
Every follow-up is derived from the deterministic question-closure receipt,
claimed exactly once in the durable pass ledger, and sent only in the already
approved conversation.  Pro may add evidence; score and Stage remain owned by
the deterministic services.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import time
from typing import Any, Callable, Mapping, Sequence

from e2r.research.page_fetcher import PageFetcher

from ..atomic_io import fsync_directory
from ..browser.protocol import (
    BrowserCaptureRequest,
    BrowserUIIncompatible,
    ChatGPTWebAdapter,
    RawBrowserCapture,
)
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
from ..capture.receipt import CaptureReceipt, load_capture_receipt, verify_capture_bundle
from ..config import ProFirstLocalConfig
from ..dossier import DossierValidationContext, ResearchDossierValidator
from ..ids import canonical_hash, canonical_json
from ..gaps.service import (
    ProGapAdjudicationService,
    compile_saturated_gap_contexts,
)
from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob
from ..multi_pass import (
    ARTIFACT_REEXPORT_PASS_NAME,
    FollowupPassPlan,
    ProMultiPassDossierStore,
    ProMultiPassLedger,
)
from ..post_import import OperationalProScoringInputProvider
from ..repair import (
    CompactRepairServiceV3,
    RepairDeltaV3Parser,
    normalize_repair_delta_v3_transport,
    reconcile_completed_repair_fail_closed,
)
from ..saturation import ResearchSaturationReceipt, compile_saturation_audit
from ..scoring import ProScoringPipelineService
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
_OPERATIONAL_GAP_PASS_NAMES = frozenset(
    {"PUBLIC_GAP_CLOSURE", "COUNTER_SUPERSESSION_CLOSURE"}
)


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
        recover_submitted_only: bool = False,
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
        self.recover_submitted_only = bool(recover_submitted_only)
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
        dossier, completed_repair_reconciliation = (
            self._reconcile_completed_compact_repair_snapshot(
                job_id=job_id,
                job_root=job_root,
                dossier=dossier,
                dossier_store=dossier_store,
                orchestrator=orchestrator,
            )
        )
        dossier, artifact_hash_reconciliation = (
            self._reconcile_artifact_reexport_initial_pass_hash(
                job_id=job_id,
                job_root=job_root,
                dossier=dossier,
                orchestrator=orchestrator,
            )
        )
        starting_job = self.store.get_job(job_id)
        if starting_job.status not in {
            JobStatus.GAP_ADJUDICATION.value,
            JobStatus.COMPONENT_RESEARCH.value,
            JobStatus.JUDGING.value,
            JobStatus.SCORING.value,
            JobStatus.STAGECOURT.value,
        }:
            raise ValueError(
                "fresh full-thesis tail must start at GAP_ADJUDICATION or the "
                "strict skipped-gap recovery boundary"
            )
        if starting_job.status == JobStatus.COMPONENT_RESEARCH.value and (
            starting_job.score_receipt_id is not None
            or starting_job.stagecourt_receipt_id is not None
        ):
            raise ValueError(
                "component recovery is forbidden after scoring output exists"
            )

        session = await ProBrowserWorker(self.config.browser).open(job_id=job_id)
        prepared: PreparedFreshV3TailRuntime | None = None
        pass_outcomes: list[Mapping[str, Any]] = [
            row
            for row in (
                completed_repair_reconciliation,
                artifact_hash_reconciliation,
            )
            if row is not None
        ]
        latest_saturation: ResearchSaturationReceipt | None = None
        verification_state: FreshVerificationState | None = None
        score_receipt: Mapping[str, Any] | None = None
        stagecourt_receipt: Mapping[str, Any] | None = None
        status = "FRESH_FULL_THESIS_PENDING"
        pending_reason: str | None = None
        try:
            durable_conversation = str(
                self.store.get_job(job_id).conversation_id or ""
            )
            recovery_source = await _ensure_durable_conversation_visible(
                session.adapter,
                job_id=job_id,
                run_id=str(built.packet_payload["run_id"]),
                durable_conversation_id=durable_conversation,
                search_terms=(
                    durable_conversation,
                    self.store.get_job(job_id).company_name,
                    self.store.get_job(job_id).symbol,
                ),
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
                recovery_source=recovery_source,
                browser_submit_delta=0,
            )

            for iteration in range(1, self.max_tail_iterations + 1):
                recovery_plan = _submitted_unsnapshotted_fresh_plan(
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
                    if recovery_plan.research_pass.pass_name == "VERIFIER_REPAIR":
                        verification_state = self._load_current_verification(
                            job_id=job_id,
                            job_root=job_root,
                            dossier=dossier,
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
                    else:
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
                        pass_outcomes.append(
                            _outcome_summary(outcome, next_dossier)
                        )
                        if (
                            recovery_plan.research_pass.pass_name
                            in {
                                "PUBLIC_GAP_CLOSURE",
                                "COUNTER_SUPERSESSION_CLOSURE",
                            }
                            and not outcome.semantic_progress
                            and not _new_no_new_route_confirmation_candidate(
                                dossier,
                                next_dossier,
                            )
                        ):
                            raise LiveCanaryPending(
                                "recovered follow-up produced no deterministic semantic progress",
                                status="RESEARCH_NO_PROGRESS_PENDING",
                            )
                        dossier = next_dossier
                    _enforce_recover_submitted_only(
                        enabled=self.recover_submitted_only,
                        recovered=True,
                    )
                    continue

                _enforce_recover_submitted_only(
                    enabled=self.recover_submitted_only,
                    recovered=False,
                )

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
                route_snapshot_bindings = _load_route_snapshot_bindings(
                    job_root
                )
                self._persist_saturation(job_root, latest_saturation)
                self._emit_fresh(
                    "FRESH_FULL_THESIS_ITERATION",
                    job_id=job_id,
                    iteration=iteration,
                    saturation=_redact_saturation(latest_saturation),
                    accepted_fact_count=len(verification_state.accepted_fact_ids),
                )

                repairable = _repairable_classifications(
                    verification_state.rejection_classifications
                )
                exhausted_gap_status: str | None = None
                public_ids = _question_ids_without_repairable_candidates(
                    _public_followup_question_ids(latest_saturation),
                    dossier=dossier,
                    repairable_classifications=repairable,
                )
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
                budgeted_public_ids = _question_ids_with_reopen_budget(
                    orchestrator.ledger,
                    job_id=job_id,
                    pass_name="PUBLIC_GAP_CLOSURE",
                    question_ids=public_ids,
                    context=public_context,
                    dossier=dossier,
                    route_snapshot_bindings=route_snapshot_bindings,
                    current_fact_snapshot_hash=(
                        latest_saturation.fact_snapshot_hash
                    ),
                    current_accepted_lineage_roster_hash=(
                        latest_saturation.accepted_lineage_roster_hash
                    ),
                )
                if budgeted_public_ids != public_ids:
                    exhausted_gap_status = (
                        "RESEARCH_GAP_REOPEN_LIMIT_PENDING"
                    )
                    public_ids = budgeted_public_ids
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
                    if _same_question_reopen_limit_reached(
                        orchestrator.ledger,
                        job_id=job_id,
                        pass_name="PUBLIC_GAP_CLOSURE",
                        question_ids=public_ids,
                    ):
                        exhausted_gap_status = (
                            "RESEARCH_GAP_REOPEN_LIMIT_PENDING"
                        )
                    elif _completed_pass_left_blockers_unchanged(
                        orchestrator.ledger,
                        job_id=job_id,
                        pass_name="PUBLIC_GAP_CLOSURE",
                        blocker_identity_hash=str(
                            public_context["pass_inputs"].get(
                                "saturation_blocker_identity_hash"
                            )
                            or ""
                        ),
                    ):
                        exhausted_gap_status = (
                            "RESEARCH_BLOCKER_FIXPOINT_PENDING"
                        )
                    else:
                        _require_operational_followup_budget(
                            orchestrator.ledger,
                            job_id=job_id,
                            pass_names=_OPERATIONAL_GAP_PASS_NAMES,
                            limit=1,
                            label="public-gap/counter",
                        )
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
                        next_dossier = dict(
                            outcome.effective_dossier or dossier
                        )
                        pass_outcomes.append(
                            _outcome_summary(outcome, next_dossier)
                        )
                        if (
                            not outcome.semantic_progress
                            and not _new_no_new_route_confirmation_candidate(
                                dossier,
                                next_dossier,
                                question_ids=public_ids,
                            )
                        ):
                            raise LiveCanaryPending(
                                "public-gap follow-up produced no "
                                "deterministic semantic progress",
                                status="RESEARCH_NO_PROGRESS_PENDING",
                            )
                        dossier = next_dossier
                        continue

                counter_ids = _question_ids_without_repairable_candidates(
                    _counter_followup_question_ids(latest_saturation),
                    dossier=dossier,
                    repairable_classifications=repairable,
                )
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
                budgeted_counter_ids = _question_ids_with_reopen_budget(
                    orchestrator.ledger,
                    job_id=job_id,
                    pass_name="COUNTER_SUPERSESSION_CLOSURE",
                    question_ids=counter_ids,
                    context=counter_context,
                    dossier=dossier,
                    route_snapshot_bindings=route_snapshot_bindings,
                    current_fact_snapshot_hash=(
                        latest_saturation.fact_snapshot_hash
                    ),
                    current_accepted_lineage_roster_hash=(
                        latest_saturation.accepted_lineage_roster_hash
                    ),
                )
                if budgeted_counter_ids != counter_ids:
                    exhausted_gap_status = (
                        exhausted_gap_status
                        or "RESEARCH_GAP_REOPEN_LIMIT_PENDING"
                    )
                    counter_ids = budgeted_counter_ids
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
                    if _same_question_reopen_limit_reached(
                        orchestrator.ledger,
                        job_id=job_id,
                        pass_name="COUNTER_SUPERSESSION_CLOSURE",
                        question_ids=counter_ids,
                    ):
                        exhausted_gap_status = (
                            exhausted_gap_status
                            or "RESEARCH_GAP_REOPEN_LIMIT_PENDING"
                        )
                    elif _completed_pass_left_blockers_unchanged(
                        orchestrator.ledger,
                        job_id=job_id,
                        pass_name="COUNTER_SUPERSESSION_CLOSURE",
                        blocker_identity_hash=str(
                            counter_context["pass_inputs"].get(
                                "saturation_blocker_identity_hash"
                            )
                            or ""
                        ),
                    ):
                        exhausted_gap_status = (
                            exhausted_gap_status
                            or "RESEARCH_BLOCKER_FIXPOINT_PENDING"
                        )
                    else:
                        _require_operational_followup_budget(
                            orchestrator.ledger,
                            job_id=job_id,
                            pass_names=_OPERATIONAL_GAP_PASS_NAMES,
                            limit=1,
                            label="public-gap/counter",
                        )
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
                        next_dossier = dict(
                            outcome.effective_dossier or dossier
                        )
                        pass_outcomes.append(
                            _outcome_summary(outcome, next_dossier)
                        )
                        if (
                            not outcome.semantic_progress
                            and not _new_no_new_route_confirmation_candidate(
                                dossier,
                                next_dossier,
                                question_ids=counter_ids,
                            )
                        ):
                            raise LiveCanaryPending(
                                "counter/supersession follow-up produced no "
                                "semantic progress",
                                status="RESEARCH_NO_PROGRESS_PENDING",
                            )
                        dossier = next_dossier
                        continue

                if repairable:
                    _require_operational_followup_budget(
                        orchestrator.ledger,
                        job_id=job_id,
                        pass_names=frozenset({"VERIFIER_REPAIR"}),
                        limit=1,
                        label="verifier-repair",
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
                    _require_operational_followup_budget(
                        orchestrator.ledger,
                        job_id=job_id,
                        pass_names=frozenset({"SATURATION_AUDIT"}),
                        limit=1,
                        label="saturation-audit",
                    )
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
                        status=(
                            exhausted_gap_status
                            or latest_saturation.deterministic_research_status
                        ),
                    )

                gap_run = ProGapAdjudicationService(self.store).adjudicate_job(
                    job_id,
                    job_root=job_root,
                    deterministic_contexts=compile_saturated_gap_contexts(
                        dossier=dossier,
                        saturation=latest_saturation,
                    ),
                    verified_dossier=dossier,
                )
                current = gap_run.job
                if (
                    current.status
                    not in {
                        JobStatus.COMPONENT_RESEARCH.value,
                        JobStatus.JUDGING.value,
                        JobStatus.SCORING.value,
                        JobStatus.STAGECOURT.value,
                    }
                    or int(gap_run.receipt.get("supplemental_task_count") or 0)
                    != 0
                ):
                    raise LiveCanaryPending(
                        "saturated gap ledger did not release component scoring",
                        status="GAP_ADJUDICATION_PENDING",
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
            if status == "OPERATIONAL_EFFICIENCY_GATE_FAILED":
                frozen = orchestrator.seal_failed_run_for_new_conversation(
                    reason=error.reason
                )
                self._emit_fresh(
                    "FRESH_FULL_THESIS_OPERATIONAL_EFFICIENCY_FAILED",
                    job_id=job_id,
                    conversation_id=frozen.conversation_id,
                    old_job_frozen=True,
                    new_conversation_required=True,
                    automatic_resubmit_allowed=False,
                )
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
            "recover_submitted_only": self.recover_submitted_only,
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

        return self._inspect_current(
            job_id=job_id,
            allow_reverification=False,
            persist_saturation=False,
            inspection_mode="READ_ONLY",
        )

    def verify_and_inspect_current(self, *, job_id: str) -> Mapping[str, Any]:
        """Reverify the current dossier without opening or sending ChatGPT."""

        return self._inspect_current(
            job_id=job_id,
            allow_reverification=True,
            persist_saturation=True,
            inspection_mode="VERIFY_CURRENT_DOSSIER_NO_BROWSER",
        )

    def _inspect_current(
        self,
        *,
        job_id: str,
        allow_reverification: bool,
        persist_saturation: bool,
        inspection_mode: str,
    ) -> Mapping[str, Any]:
        """Compute the deterministic current state with an explicit write mode."""

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
            allow_reverification=allow_reverification,
        )
        saturation = self._adjudicate_saturation(
            orchestrator.ledger,
            dossier,
            job_root=boundary.fresh_job_root,
            verified_fact_ids=verification.accepted_fact_ids,
        )
        if persist_saturation:
            self._persist_saturation(boundary.fresh_job_root, saturation)
        public_ids = _public_followup_question_ids(saturation)
        return {
            "schema_version": "e2r_pro_fresh_v3_full_thesis_inspection_v1",
            "job_id": job_id,
            "inspection_mode": inspection_mode,
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
        completed_snapshot = (
            orchestrator.ledger.latest_dossier_snapshot_for_pass(
                job_id=prepared.job.job_id,
                pass_id=plan.research_pass.pass_id,
            )
        )
        if plan.research_pass.status == "COMPLETE" and completed_snapshot is not None:
            raise LiveCanaryPending(
                "completed verifier-repair pass left the exact candidate context unchanged",
                status="VERIFIER_REPAIR_FIXPOINT_PENDING",
            )
        pass_root = (
            job_root
            / "research_passes"
            / f"{plan.research_pass.pass_ordinal:02d}_{plan.research_pass.pass_id}"
        )
        receipt_path = pass_root / "capture/incoming/browser_capture_receipt.json"
        pass_id = plan.research_pass.pass_id
        parent_id = str(plan.research_pass.parent_pass_id or "")
        repair_artifact_root = _compact_repair_artifact_root(
            job_root,
            pass_id=pass_id,
            repair_pass_ordinal=compiled.repair_pass_ordinal,
        )
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
            elif mode == "RECOVER_SUBMITTED_RESULT":
                persistence = await orchestrator.audit_submitted_followup_persistence(
                    plan,
                    prepared.session.adapter,
                )
                if not persistence.observation.persistence_confirmed:
                    disposition = (
                        "sealed after two independent fresh-view absences"
                        if persistence.sealed_unpersisted
                        else "awaiting a second independent fresh-view audit"
                    )
                    raise LiveCanaryPending(
                        "compact-repair follow-up is absent from the fresh public "
                        f"conversation; {disposition}",
                        status="TRANSPORT_PENDING",
                    )
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
            capture_receipt = _finalize_compact_repair_capture(
                pass_root=pass_root,
                raw_capture=raw,
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
                job_id=plan.scope.job_id,
                run_id=str(prepared.packet_payload["run_id"]),
                pass_id=pass_id,
                parent_pass_id=parent_id,
            )
        report_text = (
            pass_root / capture_receipt.report_md_path
        ).read_text(encoding="utf-8")
        parsed = _parse_and_validate_compact_repair_transport(
            report_text=report_text,
            capture_source=capture_receipt.capture_source,
            job_id=plan.scope.job_id,
            run_id=str(prepared.packet_payload["run_id"]),
            pass_id=pass_id,
            parent_pass_id=parent_id,
        )
        durable = orchestrator.ledger.get_pass(pass_id)
        if durable.status == "TRANSPORT_PENDING" and durable.submit_count == 1:
            orchestrator.confirm_transport_pending_result_visible(pass_id)
        normalized_delta, normalization_receipt = normalize_repair_delta_v3_transport(
            repair_delta=parsed.payload,
            dossier=dossier,
            compiled_prompt=compiled,
            performed_at=capture_receipt.captured_at,
        )
        _write_json_atomic(
            repair_artifact_root / "repair_delta_transport_normalization.json",
            normalization_receipt,
        )
        repaired = CompactRepairServiceV3(
            verifier=self.source_verifier
        ).apply_and_reverify(
            job=self.store.get_job(prepared.job.job_id),
            job_root=job_root,
            dossier=dossier,
            repair_delta=normalized_delta,
            compiled_prompt=compiled,
            prior_verification_rows=verification_state.verification_rows,
            response_hash=capture_receipt.report_md_hash,
            repair_pass_ordinal=compiled.repair_pass_ordinal,
            repair_artifact_root=repair_artifact_root,
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

    def _reconcile_completed_compact_repair_snapshot(
        self,
        *,
        job_id: str,
        job_root: Path,
        dossier: Mapping[str, Any],
        dossier_store: ProMultiPassDossierStore,
        orchestrator: FreshSessionOrchestratorV3,
    ) -> tuple[Mapping[str, Any], Mapping[str, Any] | None]:
        pass_id = str(dossier.get("research_pass_id") or "")
        research_pass = orchestrator.ledger.get_pass(pass_id)
        if research_pass.pass_name != "VERIFIER_REPAIR":
            return dossier, None
        repair_pass_ordinal = int(
            research_pass.detail.get("repair_pass_ordinal") or 1
        )
        repair_artifact_root = _compact_repair_artifact_root(
            job_root,
            pass_id=research_pass.pass_id,
            repair_pass_ordinal=repair_pass_ordinal,
        )
        reconciliation_path = (
            repair_artifact_root
            / "completed_repair_fail_closed_reconciliation.json"
        )
        if reconciliation_path.is_file():
            receipt = _read_json(reconciliation_path)
            if receipt.get("after_effective_dossier_hash") != canonical_hash(dossier):
                raise ValueError(
                    "completed repair reconciliation receipt differs from latest dossier"
                )
            return dossier, None
        repair_receipt_path = repair_artifact_root / "compact_repair_receipt.json"
        repair_delta_path = repair_artifact_root / "repair_delta_v3.json"
        if not repair_receipt_path.is_file() or not repair_delta_path.is_file():
            return dossier, None
        repair_receipt = _read_json(repair_receipt_path)
        failed_ids = tuple(
            str(value)
            for value in repair_receipt.get(
                "unresolved_replacement_candidate_ids"
            )
            or ()
        )
        if repair_receipt.get("status") != "COMPACT_REPAIR_UNRESOLVED" or not failed_ids:
            return dossier, None
        parent_pass_id = str(research_pass.parent_pass_id or "")
        parent_snapshot = dossier_store.load_latest_for_pass(
            job_id=job_id,
            pass_id=parent_pass_id,
            job_root=job_root,
        )
        if parent_snapshot is None:
            raise ValueError("completed repair reconciliation parent dossier is missing")
        effective, receipt = reconcile_completed_repair_fail_closed(
            repaired_dossier=dossier,
            parent_dossier=parent_snapshot.dossier,
            repair_delta=_read_json(repair_delta_path),
            failed_replacement_ids=failed_ids,
        )
        job = self.store.get_job(job_id)
        ResearchDossierValidator().validate(
            effective,
            DossierValidationContext(
                job_id=job_id,
                run_id=str(effective.get("run_id") or ""),
                target_id=job.symbol,
                as_of_date=job.as_of_date,
                conversation_id=job.conversation_id,
                candidate_archetype_ids=job.archetype_ids,
                research_pass_id=pass_id,
                parent_pass_id=parent_pass_id,
                enforce_parent_pass_id=True,
            ),
        )
        snapshot = dossier_store.persist(
            job_id=job_id,
            pass_id=pass_id,
            dossier=effective,
            job_root=job_root,
        )
        if snapshot.record.dossier_hash != receipt.get(
            "after_effective_dossier_hash"
        ):
            raise ValueError("completed repair reconciliation snapshot hash mismatch")
        _write_json_atomic(reconciliation_path, receipt)
        _write_json_atomic(
            repair_artifact_root / "research_dossier.reconciled.json",
            effective,
        )
        return effective, receipt

    def _reconcile_artifact_reexport_initial_pass_hash(
        self,
        *,
        job_id: str,
        job_root: Path,
        dossier: Mapping[str, Any],
        orchestrator: FreshSessionOrchestratorV3,
    ) -> tuple[Mapping[str, Any], Mapping[str, Any] | None]:
        """Repair only the historical transport hash field from the R15 bug.

        The initial visible response and the generated dossier file are two
        different byte streams.  An artifact-only re-export capture used the
        file hash while the durable pass ledger correctly retained the initial
        visible-response hash.  Reconcile that one field only when the exact
        transport-only lineage and capture bundle prove the mismatch.
        """

        scope = orchestrator.ledger.get_scope(job_id)
        if scope is None:
            return dossier, None
        initial_pass = orchestrator.ledger.get_pass(scope.initial_pass_id)
        artifact_passes = tuple(
            row
            for row in orchestrator.ledger.list_passes(job_id)
            if row.pass_name == ARTIFACT_REEXPORT_PASS_NAME
            and row.parent_pass_id == initial_pass.pass_id
        )
        capture_path = job_root / "capture/incoming/browser_capture_receipt.json"
        if not capture_path.is_file():
            return dossier, None
        capture_receipt = load_capture_receipt(capture_path)
        verify_capture_bundle(job_root, capture_receipt)
        artifact_pass = artifact_passes[0] if len(artifact_passes) == 1 else None
        reconciled, receipt = _reconcile_artifact_reexport_initial_pass_row(
            dossier=dossier,
            initial_pass=initial_pass,
            artifact_pass=artifact_pass,
            capture_receipt=capture_receipt,
        )
        if receipt is None:
            return reconciled, None
        receipt_path = (
            job_root
            / "fresh_session/initial_artifact_response_hash_reconciliation.json"
        )
        if receipt_path.is_file() and _read_json(receipt_path) != receipt:
            raise ValueError(
                "initial artifact response-hash reconciliation receipt changed"
            )
        _write_json_atomic(receipt_path, receipt)
        return reconciled, receipt

    def _emit_fresh(self, phase: str, **payload: Any) -> None:
        self.progress(
            {
                "schema_version": "e2r_pro_fresh_v3_full_thesis_progress_v1",
                "phase": phase,
                "observed_at": _utc_now(),
                **payload,
            }
        )


def _reconcile_artifact_reexport_initial_pass_row(
    *,
    dossier: Mapping[str, Any],
    initial_pass: Any,
    artifact_pass: Any | None,
    capture_receipt: CaptureReceipt,
) -> tuple[Mapping[str, Any], Mapping[str, Any] | None]:
    """Normalize one proven attachment-hash/response-hash transport mismatch."""

    rows = tuple(dossier.get("research_passes") or ())
    indexes = [
        index
        for index, row in enumerate(rows)
        if isinstance(row, Mapping)
        and str(row.get("pass_id") or "") == str(initial_pass.pass_id)
    ]
    if len(indexes) != 1:
        raise ValueError(
            "effective dossier must contain exactly one durable initial pass row"
        )
    durable_row = {
        "pass_id": initial_pass.pass_id,
        "parent_pass_id": initial_pass.parent_pass_id,
        "pass_name": initial_pass.pass_name,
        "status": "COMPLETE",
        "prompt_hash": initial_pass.prompt_hash,
        "response_hash": initial_pass.response_hash,
    }
    current = dict(rows[indexes[0]])
    mismatches = tuple(
        key for key, value in durable_row.items() if current.get(key) != value
    )
    if not mismatches:
        return dossier, None
    if mismatches != ("response_hash",):
        raise ValueError(
            "initial effective-dossier pass differs beyond the response hash"
        )
    if (
        initial_pass.status != "COMPLETE"
        or initial_pass.submit_count != 1
        or not isinstance(initial_pass.response_hash, str)
        or len(initial_pass.response_hash) != 64
        or artifact_pass is None
        or artifact_pass.pass_name != ARTIFACT_REEXPORT_PASS_NAME
        or artifact_pass.parent_pass_id != initial_pass.pass_id
        or artifact_pass.conversation_id != initial_pass.conversation_id
        or artifact_pass.status != "COMPLETE"
        or artifact_pass.submit_count != 1
        or not isinstance(artifact_pass.response_hash, str)
        or len(artifact_pass.response_hash) != 64
        or artifact_pass.score_valid
        or not artifact_pass.publication_withheld
        or capture_receipt.capture_source != "DOWNLOAD_JSON"
        or capture_receipt.conversation_id != initial_pass.conversation_id
        or capture_receipt.prompt_hash != initial_pass.prompt_hash
        or current.get("response_hash") != capture_receipt.report_md_hash
        or not (
            "ARTIFACT_REEXPORT" in capture_receipt.capture_mode
            or capture_receipt.capture_mode
            == "CHATGPT_WEB_VISIBLE_CHAT_PRO_FRESH_V3_RECOVERED_NO_SUBMIT"
        )
    ):
        raise ValueError(
            "initial response-hash mismatch lacks exact artifact re-export proof"
        )
    corrected = deepcopy(dict(dossier))
    corrected_rows = [deepcopy(dict(row)) for row in rows]
    corrected_rows[indexes[0]] = durable_row
    corrected["research_passes"] = corrected_rows
    receipt: Mapping[str, Any] = {
        "schema_version": (
            "e2r_pro_fresh_v3_initial_artifact_response_hash_reconciliation_v1"
        ),
        "status": "INITIAL_ARTIFACT_RESPONSE_HASH_RECONCILED",
        "initial_pass_id": initial_pass.pass_id,
        "artifact_reexport_pass_id": artifact_pass.pass_id,
        "capture_source": capture_receipt.capture_source,
        "capture_mode": capture_receipt.capture_mode,
        "captured_artifact_hash": capture_receipt.report_md_hash,
        "durable_initial_response_hash": initial_pass.response_hash,
        "changed_fields": ["research_passes.initial.response_hash"],
        "before_effective_dossier_hash": canonical_hash(dossier),
        "after_effective_dossier_hash": canonical_hash(corrected),
        "fact_content_mutation_allowed": False,
        "browser_submit_delta": 0,
        "score_authority": False,
        "stage_authority": False,
    }
    return corrected, receipt


def _parse_and_validate_compact_repair_transport(
    *,
    report_text: str,
    capture_source: str,
    job_id: str,
    run_id: str,
    pass_id: str,
    parent_pass_id: str,
):
    """Accept MD markers or an identity-bound raw RepairDeltaV3 JSON file."""

    parsed = RepairDeltaV3Parser().parse_text(report_text)
    if capture_source == "DOWNLOAD_JSON":
        for key, expected in (
            ("job_id", job_id),
            ("run_id", run_id),
            ("research_pass_id", pass_id),
            ("parent_pass_id", parent_pass_id),
        ):
            if str(parsed.payload.get(key) or "") != expected:
                raise LiveCanaryPending(
                    f"downloaded compact repair JSON has mismatched {key}",
                    status="TRANSPORT_PENDING",
                )
        return parsed
    markers = (
        ("run", f"[[E2R_PRO_RUN_ID:{run_id}]]"),
        ("job", f"[[E2R_PRO_JOB_ID:{job_id}]]"),
        ("pass", f"[[E2R_PRO_PASS_ID:{pass_id}]]"),
        ("parent", f"[[E2R_PRO_PARENT_PASS_ID:{parent_pass_id}]]"),
    )
    for label, marker in markers:
        if report_text.count(marker) != 1:
            raise LiveCanaryPending(
                f"compact repair lacks the exact {label} marker",
                status="TRANSPORT_PENDING",
            )
    return parsed


def _finalize_compact_repair_capture(
    *,
    pass_root: Path,
    raw_capture: RawBrowserCapture,
    identity: CaptureIdentity,
    job_id: str,
    run_id: str,
    pass_id: str,
    parent_pass_id: str,
    writer: AtomicCaptureWriter | None = None,
) -> CaptureReceipt:
    """Persist a repair response without treating it as a full dossier MD."""

    report_text = raw_capture.report_md_part_path.read_text(encoding="utf-8-sig")
    parsed = _parse_and_validate_compact_repair_transport(
        report_text=report_text,
        capture_source=raw_capture.source,
        job_id=job_id,
        run_id=run_id,
        pass_id=pass_id,
        parent_pass_id=parent_pass_id,
    )
    return (writer or AtomicCaptureWriter()).finalize(
        pass_root,
        identity=identity,
        raw_capture=raw_capture,
        dossier_override=dict(parsed.payload),
    ).receipt


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
                "deterministic_materiality": decision.get("materiality"),
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
                "question_to_source_linkage_complete": decision.get(
                    "question_to_source_linkage_complete"
                ),
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
    question_stable_gap_hashes = {
        row["question_family_id"]: canonical_hash(
            {
                "schema_version": "e2r_question_stable_gap_identity_v1",
                "pass_name": pass_name,
                "question_family_id": row["question_family_id"],
                "deterministic_materiality": row[
                    "deterministic_materiality"
                ],
                "gap_class": row["gap_class"],
                "required_source_roles_missing": sorted(
                    set(row["required_source_roles_missing"])
                ),
                "missing_core_source_roles": sorted(
                    set(row["missing_core_source_roles"])
                ),
                "missing_corroboration_source_roles": sorted(
                    set(row["missing_corroboration_source_roles"])
                ),
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
    blocker_identity_hash = canonical_hash(
        {
            "schema_version": "e2r_saturation_blocker_identity_v1",
            "pass_name": pass_name,
            "questions": [
                _saturation_blocker_identity_row(row) for row in unresolved
            ],
        }
    )
    prompt_question_state = (
        [
            _compact_saturation_audit_question_state(row)
            for row in unresolved
        ]
        if pass_name == "SATURATION_AUDIT"
        else unresolved
    )
    return {
        "question_state_schema_version": (
            "e2r_saturation_audit_question_digest_v1"
            if pass_name == "SATURATION_AUDIT"
            else "e2r_followup_question_state_v1"
        ),
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
        "unresolved_question_state": prompt_question_state,
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
            "question_stable_gap_hashes": question_stable_gap_hashes,
            "deterministic_research_status": (
                saturation.deterministic_research_status
            ),
            "research_gap_context_hash": gap_context_hash,
            "saturation_blocker_identity_hash": blocker_identity_hash,
            "new_research_fact_allowed": pass_name != "SATURATION_AUDIT",
            "score_authority": False,
            "stage_authority": False,
        },
    }


def _compact_saturation_audit_question_state(
    row: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Remove append-only route repetition from a no-new-facts audit prompt."""

    route_progress = dict(row.get("route_progress_state") or {})
    latest_outcomes = tuple(route_progress.get("latest_route_outcomes") or ())
    outcome_counts: dict[tuple[str, str, bool], int] = {}
    for outcome in latest_outcomes:
        key = (
            str(outcome.get("provider_status") or ""),
            str(outcome.get("parser_status") or ""),
            outcome.get("no_new_route_confirmed") is True,
        )
        outcome_counts[key] = outcome_counts.get(key, 0) + 1
    route_summary = {
        "route_progress_hash": canonical_hash(route_progress),
        "route_signature_count": len(
            tuple(route_progress.get("route_signatures") or ())
        ),
        "latest_outcome_count": len(latest_outcomes),
        "latest_outcome_status_counts": [
            {
                "provider_status": key[0],
                "parser_status": key[1],
                "no_new_route_confirmed": key[2],
                "count": count,
            }
            for key, count in sorted(outcome_counts.items())
        ],
        "unknown_linked_route_reference": route_progress.get(
            "unknown_linked_route_reference"
        ),
        "attempted_source_roles": list(
            route_progress.get("attempted_source_roles") or ()
        ),
        "adequate": route_progress.get("adequate"),
        "official_route_attempted": route_progress.get(
            "official_route_attempted"
        ),
        "distinct_route_count": route_progress.get("distinct_route_count"),
        "independent_no_new_route_confirmation_count": route_progress.get(
            "independent_no_new_route_confirmation_count"
        ),
        "provider_parser_normal": route_progress.get(
            "provider_parser_normal"
        ),
        "semantic_fixpoint": route_progress.get("semantic_fixpoint"),
        "failure_codes": list(route_progress.get("failure_codes") or ()),
    }
    return {
        "question_family_id": row.get("question_family_id"),
        "reported_status": row.get("reported_status"),
        "availability_class": row.get("availability_class"),
        "closure_reason": row.get("closure_reason"),
        "deterministic_status": row.get("deterministic_status"),
        "gap_class": row.get("gap_class"),
        "failure_codes": list(row.get("failure_codes") or ()),
        "verified_linked_fact_ids": list(
            row.get("verified_linked_fact_ids") or ()
        ),
        "linked_source_lineage_ids": list(
            row.get("linked_source_lineage_ids") or ()
        ),
        "missing_core_source_roles": list(
            row.get("missing_core_source_roles") or ()
        ),
        "missing_corroboration_source_roles": list(
            row.get("missing_corroboration_source_roles") or ()
        ),
        "verified_source_roles": list(
            row.get("verified_source_roles") or ()
        ),
        "deterministic_terminal": row.get("deterministic_terminal"),
        "deterministic_ready": row.get("deterministic_ready"),
        "route_progress_summary": route_summary,
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

    def route_identities(row: Mapping[str, Any]) -> tuple[str, ...]:
        """Return transport-stable route identities for progress gating.

        Pro may rephrase an objective, change a source-role label, or split a
        previously opened URL group into several receipt rows.  None of those
        presentation changes is a new public route.  Opened URLs are therefore
        compared atomically.  A query is the identity only when it produced no
        opened URL; a row with neither collapses to one no-route identity.
        """

        urls = tuple(
            sorted(
                {
                    str(value).strip()
                    for value in row.get("opened_source_urls") or ()
                    if str(value).strip()
                }
            )
        )
        if urls:
            return tuple(
                canonical_hash({"route_kind": "OPENED_URL", "url": url})
                for url in urls
            )
        query = " ".join(str(row.get("query_text") or "").split()).casefold()
        if query:
            return (
                canonical_hash(
                    {"route_kind": "QUERY_WITHOUT_OPENED_URL", "query": query}
                ),
            )
        return (canonical_hash({"route_kind": "NO_ROUTE"}),)

    route_signatures = tuple(
        sorted(
            {
                identity
                for row in linked
                for identity in route_identities(row)
            }
        )
    )
    latest_outcome_by_signature = {}
    for row in linked:
        for route_signature in route_identities(row):
            latest_outcome_by_signature[route_signature] = {
                "route_signature": route_signature,
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
    latest_outcomes = tuple(
        latest_outcome_by_signature[key]
        for key in sorted(latest_outcome_by_signature)
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
        ),
        "adequate": route_adequacy.get("adequate"),
        "official_route_attempted": route_adequacy.get(
            "official_route_attempted"
        ),
        "distinct_route_count": len(route_signatures),
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
                # A verifier-pending question without a repairable candidate
                # is an acquisition/fixpoint gap, not a compact fact repair.
                # The caller below removes questions that do have a bounded
                # repair candidate before any public follow-up is planned.
                *saturation.verifier_repair_pending_ids,
            )
        )
        if value not in blocked
    )


def _new_no_new_route_confirmation_candidate(
    before: Mapping[str, Any],
    after: Mapping[str, Any],
    *,
    question_ids: Sequence[str] = (),
) -> bool:
    """Recognize a new normal, empty route as fixpoint *input*, not closure.

    Raw receipt growth remains non-semantic.  This narrow exception merely
    permits the next deterministic iteration when Pro recorded an actual
    normal route with no accepted fact and an explicit no-new-route reason.
    Two independent passes and identical snapshots are still required by the
    semantic fixpoint evaluator before any question can become terminal.
    """

    previous_ids = {
        str(row.get("route_receipt_id") or "")
        for row in before.get("search_route_receipts") or ()
    }
    requested = {
        str(value) for value in question_ids if str(value)
    }
    for row in after.get("search_route_receipts") or ():
        receipt_id = str(row.get("route_receipt_id") or "")
        if not receipt_id or receipt_id in previous_ids:
            continue
        if requested and str(row.get("question_family_id") or "") not in requested:
            continue
        route_attempted = bool(
            tuple(row.get("opened_source_urls") or ())
            or str(row.get("query_text") or "").strip()
            or str(row.get("query_or_navigation_objective") or "").strip()
        )
        if (
            route_attempted
            and str(row.get("provider_status") or "") == "SUCCESS"
            and str(row.get("parser_status") or "SUCCESS") == "SUCCESS"
            and not tuple(row.get("accepted_fact_ids") or ())
            and str(row.get("no_new_route_reason") or "").strip()
        ):
            return True
    return False


def _counter_followup_question_ids(
    saturation: ResearchSaturationReceipt,
) -> tuple[str, ...]:
    unresolved_counter = tuple(
        row.question_family_id
        for row in saturation.question_decisions
        if row.status == "CONTRADICTED_UNRESOLVED" and not row.terminal
    )
    return tuple(
        dict.fromkeys(
            (
                *saturation.lifecycle_hard_break_pending_ids,
                *unresolved_counter,
            )
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


def _question_ids_without_repairable_candidates(
    question_ids: Sequence[str],
    *,
    dossier: Mapping[str, Any],
    repairable_classifications: Sequence[Mapping[str, Any]],
) -> tuple[str, ...]:
    """Route a verifier defect to compact repair before searching again.

    A terminal question can still expose a missing deterministic source role
    when one of its linked facts was rejected for a repairable semantic or
    source defect.  Sending that question back to public research merely adds
    more append-only facts and route receipts while the verifier defect stays
    unresolved.  Keep unrelated acquisition gaps eligible, but hold the
    affected question for the bounded compact-repair branch below.
    """

    repairable_candidate_ids = {
        str(row.get("candidate_id") or "")
        for row in repairable_classifications
        if str(row.get("candidate_id") or "")
    }
    if not repairable_candidate_ids:
        return tuple(dict.fromkeys(str(value) for value in question_ids))
    blocked_question_ids = {
        str(row.get("question_family_id") or "")
        for row in dossier.get("question_family_results") or ()
        if repairable_candidate_ids.intersection(
            str(value)
            for field in (
                "support_fact_ids",
                "counter_fact_ids",
                "resolution_fact_ids",
            )
            for value in row.get(field) or ()
        )
    }
    return tuple(
        value
        for value in dict.fromkeys(str(value) for value in question_ids)
        if value not in blocked_question_ids
    )


async def _ensure_durable_conversation_visible(
    adapter: ChatGPTWebAdapter,
    *,
    job_id: str,
    run_id: str,
    durable_conversation_id: str,
    search_terms: tuple[str, ...],
) -> str:
    """Keep an already-open exact conversation without requiring history UI.

    ChatGPT's sidebar/search controls can change independently of the
    conversation URL.  An exact durable conversation ID already visible in a
    logged-in browser is therefore the strongest zero-navigation recovery
    path.  History search is used only when another page is open.
    """

    if not durable_conversation_id:
        raise ValueError("durable fresh conversation id is missing")
    try:
        inspection = await adapter.ensure_logged_in()
    except BrowserUIIncompatible:
        inspection = await adapter.open_exact_conversation_without_submit(
            conversation_id=durable_conversation_id,
        )
        if inspection.conversation_id != durable_conversation_id:
            raise ValueError(
                "exact public navigation differs from the approved conversation"
        )
        return "PUBLIC_EXACT_CONVERSATION_URL"
    if inspection.conversation_id == durable_conversation_id:
        return "CURRENT_EXACT_CONVERSATION"
    # The ledger already owns the exact durable conversation id.  If another
    # valid ChatGPT page or conversation is active, opening that public URL is
    # deterministic and avoids depending on mutable history-search snippets.
    inspection = await adapter.open_exact_conversation_without_submit(
        conversation_id=durable_conversation_id,
    )
    if inspection.conversation_id != durable_conversation_id:
        raise ValueError(
            "visible ChatGPT page differs from the approved fresh conversation"
        )
    return "PUBLIC_EXACT_CONVERSATION_URL"


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


def _completed_pass_left_blockers_unchanged(
    ledger: ProMultiPassLedger,
    *,
    job_id: str,
    pass_name: str,
    blocker_identity_hash: str,
) -> bool:
    """Detect a durable follow-up that returned to the same blocker state.

    Evidence IDs and prose are deliberately absent from this identity.  A new
    fact is useful only when it changes a deterministic question state,
    missing source role, linkage disposition, or route-adequacy condition.
    """

    if not blocker_identity_hash:
        return False
    return any(
        row.pass_name == pass_name
        and row.status == "COMPLETE"
        and row.submit_count == 1
        and str(
            row.detail.get("saturation_blocker_identity_hash") or ""
        )
        == blocker_identity_hash
        for row in ledger.list_passes(job_id)
    )


def _same_question_reopen_limit_reached(
    ledger: ProMultiPassLedger,
    *,
    job_id: str,
    pass_name: str,
    question_ids: Sequence[str],
    completed_attempt_limit: int = 2,
) -> bool:
    """Stop a third consecutive reopen of the same exact question set.

    Route/provider wording can oscillate even when the economic gap is the
    same.  The richer blocker identity remains the primary fixpoint guard;
    this transport-independent ceiling prevents that oscillation from
    manufacturing an unlimited series of nominally changed contexts.
    """

    requested = tuple(str(value) for value in question_ids if str(value))
    if not requested:
        return False
    if completed_attempt_limit < 1:
        raise ValueError("completed attempt limit must be positive")
    matched = 0
    completed = tuple(
        row
        for row in ledger.list_passes(job_id)
        if row.pass_name == pass_name
        and row.status == "COMPLETE"
        and row.submit_count == 1
    )
    for row in reversed(completed):
        stored = tuple(
            str(value)
            for value in row.detail.get("question_family_ids") or ()
            if str(value)
        )
        if stored != requested:
            break
        matched += 1
        if matched >= completed_attempt_limit:
            return True
    return False


def _question_ids_with_reopen_budget(
    ledger: ProMultiPassLedger,
    *,
    job_id: str,
    pass_name: str,
    question_ids: Sequence[str],
    context: Mapping[str, Any],
    dossier: Mapping[str, Any] | None = None,
    route_snapshot_bindings: Mapping[str, Mapping[str, Any]] | None = None,
    current_fact_snapshot_hash: str | None = None,
    current_accepted_lineage_roster_hash: str | None = None,
    completed_attempt_limit: int = 2,
) -> tuple[str, ...]:
    """Drop questions whose same stable economic gap actually ran twice.

    A multi-question prompt does not spend a question's reopen budget when
    Pro omits every route receipt for that question.  The durable requested
    roster remains audit evidence, while the effective dossier proves which
    question routes were actually attempted in each completed pass.
    """

    if completed_attempt_limit < 1:
        raise ValueError("completed attempt limit must be positive")
    requested = tuple(str(value) for value in question_ids if str(value))
    stable = dict(
        (context.get("pass_inputs") or {}).get(
            "question_stable_gap_hashes"
        )
        or {}
    )
    attempts = {question_id: 0 for question_id in requested}
    exact_snapshot_requested = any(
        value is not None
        for value in (
            route_snapshot_bindings,
            current_fact_snapshot_hash,
            current_accepted_lineage_roster_hash,
        )
    )
    if exact_snapshot_requested and (
        route_snapshot_bindings is None
        or not current_fact_snapshot_hash
        or not current_accepted_lineage_roster_hash
    ):
        raise ValueError(
            "exact reopen accounting requires route bindings and both current hashes"
        )
    actual_route_questions: set[tuple[str, str]] | None = None
    if dossier is not None:
        actual_route_questions = set()
        for route in dossier.get("search_route_receipts") or ():
            pass_id = str(route.get("pass_id") or "")
            question_id = str(route.get("question_family_id") or "")
            if not pass_id or not question_id:
                continue
            if exact_snapshot_requested:
                receipt_id = str(route.get("route_receipt_id") or "")
                binding = (route_snapshot_bindings or {}).get(receipt_id)
                if (
                    not isinstance(binding, Mapping)
                    or str(binding.get("pass_id") or "") != pass_id
                    or str(binding.get("question_family_id") or "")
                    != question_id
                    or str(binding.get("fact_snapshot_hash") or "")
                    != current_fact_snapshot_hash
                    or str(
                        binding.get("accepted_lineage_roster_hash") or ""
                    )
                    != current_accepted_lineage_roster_hash
                ):
                    continue
            actual_route_questions.add((pass_id, question_id))
    for row in ledger.list_passes(job_id):
        if (
            row.pass_name != pass_name
            or row.status != "COMPLETE"
            or row.submit_count != 1
        ):
            continue
        stored_ids = {
            str(value)
            for value in row.detail.get("question_family_ids") or ()
            if str(value)
        }
        stored_stable = dict(
            row.detail.get("question_stable_gap_hashes") or {}
        )
        for question_id in requested:
            if question_id not in stored_ids:
                continue
            if (
                actual_route_questions is not None
                and (row.pass_id, question_id) not in actual_route_questions
            ):
                continue
            current_hash = str(stable.get(question_id) or "")
            stored_hash = str(stored_stable.get(question_id) or "")
            # Older durable passes predate this field.  Conservatively treat
            # their same question identity as the same stable gap; this is a
            # fail-closed migration boundary, not a score or Stage decision.
            if not stored_hash or stored_hash == current_hash:
                attempts[question_id] += 1
    return tuple(
        question_id
        for question_id in requested
        if attempts[question_id] < completed_attempt_limit
    )


def _load_route_snapshot_bindings(
    job_root: Path,
) -> Mapping[str, Mapping[str, Any]]:
    path = job_root / "saturation/route_snapshot_bindings.json"
    if not path.is_file():
        raise ValueError("current route snapshot binding receipt is missing")
    payload = json.loads(path.read_text(encoding="utf-8"))
    bindings = payload.get("bindings")
    if not isinstance(bindings, Mapping):
        raise ValueError("route snapshot binding receipt has no binding map")
    return {
        str(receipt_id): dict(binding)
        for receipt_id, binding in bindings.items()
        if isinstance(binding, Mapping)
    }


def _saturation_blocker_identity_row(
    row: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Project only state that can actually reduce a saturation blocker."""

    route = dict(row.get("route_progress_state") or {})
    return {
        "question_family_id": row.get("question_family_id"),
        "reported_status": row.get("reported_status"),
        "availability_class": row.get("availability_class"),
        "required_source_roles_missing": sorted(
            set(row.get("required_source_roles_missing") or ())
        ),
        "deterministic_status": row.get("deterministic_status"),
        "deterministic_materiality": row.get("deterministic_materiality"),
        "gap_class": row.get("gap_class"),
        "failure_codes": sorted(set(row.get("failure_codes") or ())),
        "missing_core_source_roles": sorted(
            set(row.get("missing_core_source_roles") or ())
        ),
        "missing_corroboration_source_roles": sorted(
            set(row.get("missing_corroboration_source_roles") or ())
        ),
        "verified_source_roles": sorted(
            set(row.get("verified_source_roles") or ())
        ),
        "deterministic_terminal": row.get("deterministic_terminal"),
        "deterministic_ready": row.get("deterministic_ready"),
        "question_to_source_linkage_complete": row.get(
            "question_to_source_linkage_complete"
        ),
        "route_progress": {
            "unknown_linked_route_reference": route.get(
                "unknown_linked_route_reference"
            ),
            "attempted_source_roles": sorted(
                set(route.get("attempted_source_roles") or ())
            ),
            "adequate": route.get("adequate"),
            "official_route_attempted": route.get(
                "official_route_attempted"
            ),
            "distinct_route_count": route.get("distinct_route_count"),
            "independent_no_new_route_confirmation_count": route.get(
                "independent_no_new_route_confirmation_count"
            ),
            "provider_parser_normal": route.get("provider_parser_normal"),
            "semantic_fixpoint": route.get("semantic_fixpoint"),
            "failure_codes": sorted(set(route.get("failure_codes") or ())),
        },
    }


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


_FRESH_RECOVERABLE_FOLLOWUP_NAMES = (
    "PUBLIC_GAP_CLOSURE",
    "COUNTER_SUPERSESSION_CLOSURE",
    "SATURATION_AUDIT",
    "VERIFIER_REPAIR",
)


def _require_operational_followup_budget(
    ledger: ProMultiPassLedger,
    *,
    job_id: str,
    pass_names: frozenset[str],
    limit: int,
    label: str,
) -> None:
    """Fail a fresh operational canary before it becomes repair-heavy.

    The broader research state machine may continue investigating without a
    fixed semantic cap.  A V2.1 *operational efficiency canary* has a narrower
    proof contract: one gap/counter delta, one repair, and one saturation
    audit.  Every submitted attempt consumes that proof budget, including a
    visible provider failure, because the user still paid the browser turn.
    """

    if limit < 1 or not pass_names or not label.strip():
        raise ValueError("operational follow-up budget requires names/label/limit")
    submitted = tuple(
        row
        for row in ledger.list_passes(job_id)
        if row.pass_name in pass_names and int(row.submit_count) > 0
    )
    if len(submitted) < limit:
        return
    raise LiveCanaryPending(
        f"{label} submitted pass budget exceeded: "
        f"allowed={limit}, already_submitted={len(submitted)}; "
        "seal this diagnostic run and start a new conversation",
        status="OPERATIONAL_EFFICIENCY_GATE_FAILED",
    )


def _enforce_recover_submitted_only(
    *,
    enabled: bool,
    recovered: bool,
) -> None:
    """Keep a recovery invocation incapable of planning a new Pro turn."""

    if not enabled:
        return
    if recovered:
        raise LiveCanaryPending(
            "submitted follow-up recovered; additional pass planning is disabled",
            status="SUBMITTED_PASS_RECOVERED_PENDING",
        )
    raise LiveCanaryPending(
        "no submitted unsnapshotted follow-up exists; recovery-only mode sent nothing",
        status="SUBMITTED_PASS_RECOVERY_REQUIRED",
    )


def _submitted_unsnapshotted_fresh_plan(
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
            for pass_name in _FRESH_RECOVERABLE_FOLLOWUP_NAMES
        )
        if row is not None
    )
    if len(matches) > 1:
        raise ValueError("multiple submitted fresh follow-ups lack snapshots")
    return matches[0] if matches else None


def _compact_repair_artifact_root(
    job_root: Path,
    *,
    pass_id: str,
    repair_pass_ordinal: int,
) -> Path:
    """Preserve the legacy first receipt and append later repairs by pass."""

    if repair_pass_ordinal < 1:
        raise ValueError("repair pass ordinal must be positive")
    if not pass_id:
        raise ValueError("repair artifact root requires a pass id")
    if repair_pass_ordinal == 1:
        return job_root / "repair_v3"
    return (
        job_root
        / "repair_v3/passes"
        / f"{repair_pass_ordinal:02d}_{pass_id}"
    )


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
