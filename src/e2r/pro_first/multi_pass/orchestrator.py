"""Contract-scoped, same-conversation Pro V2 follow-up orchestration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

from ..browser.protocol import (
    BrowserInspection,
    BrowserSubmittedTurnPersistence,
    BrowserUIState,
    ChatGPTWebAdapter,
    PreparedFollowupPass,
)
from ..ids import canonical_hash, stable_id
from ..job_store import ProFirstJobStore
from ..research_contracts import ProResearchPromptCompilerV2
from .ledger import ProMultiPassLedger
from .models import (
    COUNTER_SUPERSESSION_PASS_NAME,
    FollowupPassPlan,
    FollowupSubmitBlocked,
    ResearchApprovalScope,
    ResearchPassRecord,
    ResearchPassStatus,
    ScopeApprovalRequired,
    TransportPendingDecision,
)


_FOLLOWUP_CAPABILITY = object()
_PUBLIC_GAP_STATUSES = frozenset(
    {"PUBLIC_SEARCHABLE", "UNKNOWN_ROUTE_NOT_YET_TESTED", "SOURCE_PENDING"}
)


@dataclass(frozen=True)
class ScopedFollowupProof:
    job_id: str
    pass_id: str
    parent_pass_id: str
    approval_scope_id: str
    browser_session_id: str
    conversation_id: str
    prompt_hash: str
    submit_count: int
    _capability: object = field(repr=False, compare=False)

    @property
    def ledger_verified(self) -> bool:
        return self._capability is _FOLLOWUP_CAPABILITY and self.submit_count == 1


@dataclass(frozen=True)
class FollowupSubmitResult:
    research_pass: ResearchPassRecord
    inspection: BrowserInspection


@dataclass(frozen=True)
class FollowupPersistenceAuditResult:
    research_pass: ResearchPassRecord
    observation: BrowserSubmittedTurnPersistence
    sealed_unpersisted: bool


class ProMultiPassResearchOrchestrator:
    def __init__(
        self,
        store: ProFirstJobStore,
        *,
        compiler: ProResearchPromptCompilerV2 | None = None,
        ledger: ProMultiPassLedger | None = None,
        max_followup_passes: int = 8,
    ) -> None:
        if max_followup_passes < 1:
            raise ValueError("max_followup_passes must be positive")
        self.store = store
        self.compiler = compiler or ProResearchPromptCompilerV2()
        self.ledger = ledger or ProMultiPassLedger(store)
        self.max_followup_passes = max_followup_passes

    def record_completed_initial_pass(
        self,
        job_id: str,
        *,
        primary_archetype_ids: Sequence[str],
        response_hash: str,
        initial_pass_id: str | None = None,
    ) -> ResearchApprovalScope:
        return self.ledger.establish_initial_scope(
            job_id,
            primary_archetype_ids=primary_archetype_ids,
            initial_response_hash=response_hash,
            initial_pass_id=initial_pass_id,
        )

    def plan_next_material_pass(
        self,
        *,
        job_id: str,
        packet: Mapping[str, Any],
        dossier: Mapping[str, Any],
        primary_archetype_ids: Sequence[str],
    ) -> FollowupPassPlan | TransportPendingDecision | None:
        questions = tuple(dossier.get("question_family_results") or ())
        repair = tuple(
            row
            for row in questions
            if str(row.get("status") or "") == "VERIFIER_REPAIR_REQUIRED"
        )
        if repair:
            return self.plan_followup(
                job_id=job_id,
                packet=packet,
                primary_archetype_ids=primary_archetype_ids,
                pass_name="VERIFIER_REPAIR",
                unresolved_question_state=repair,
                pass_inputs={
                    "route_reason": "MATERIAL_FACT_VERIFIER_REJECTION",
                    "question_family_ids": [
                        str(row.get("question_family_id") or "") for row in repair
                    ],
                    "verification_repair_register": list(
                        dossier.get("verification_repair_register") or ()
                    ),
                },
            )
        public = tuple(
            row
            for row in questions
            if str(row.get("status") or "") in _PUBLIC_GAP_STATUSES
            and any(
                row.get(key) is True
                for key in ("could_change_score", "could_change_stage", "could_change_hard_break")
            )
        )
        if public:
            return self.plan_followup(
                job_id=job_id,
                packet=packet,
                primary_archetype_ids=primary_archetype_ids,
                pass_name="PUBLIC_GAP_CLOSURE",
                unresolved_question_state=public,
                pass_inputs={
                    "route_reason": "PUBLIC_SEARCHABLE_MATERIAL_GAP",
                    "question_family_ids": [
                        str(row.get("question_family_id") or "") for row in public
                    ],
                },
            )
        contradicted = tuple(
            row
            for row in questions
            if str(row.get("status") or "") == "CONTRADICTED_UNRESOLVED"
        )
        if contradicted:
            return self.plan_followup(
                job_id=job_id,
                packet=packet,
                primary_archetype_ids=primary_archetype_ids,
                pass_name=COUNTER_SUPERSESSION_PASS_NAME,
                unresolved_question_state=contradicted,
                pass_inputs={
                    "route_reason": "COUNTER_OR_SUPERSESSION_UNRESOLVED",
                    "question_family_ids": [
                        str(row.get("question_family_id") or "") for row in contradicted
                    ],
                },
            )
        return None

    def plan_followup(
        self,
        *,
        job_id: str,
        packet: Mapping[str, Any],
        primary_archetype_ids: Sequence[str],
        pass_name: str,
        unresolved_question_state: Sequence[Mapping[str, Any]] = (),
        pass_inputs: Mapping[str, Any] | None = None,
        existing_verified_ledger_digest: Mapping[str, Any] | None = None,
    ) -> FollowupPassPlan | TransportPendingDecision:
        job = self.store.get_job(job_id)
        if job.old_job_frozen_at is not None:
            return TransportPendingDecision(
                job_id=job_id,
                requested_pass_name=pass_name,
                research_status="TRANSPORT_PENDING",
                reason=(
                    "SUPERSEDED_BY_FRESH_SESSION_EFFICIENCY_VALIDATION: "
                    "old diagnostic conversation is frozen"
                ),
            )
        scope = self.ledger.require_authorized_scope(
            job_id,
            target_id=str(
                (packet.get("target") or {}).get("symbol")
                or (packet.get("target") or {}).get("target_id")
                or ""
            ),
            as_of_date=str(packet.get("as_of_date") or ""),
            primary_archetype_ids=primary_archetype_ids,
            pass_name=pass_name,
            conversation_id=scope_conversation(packet, fallback=self._job_conversation(job_id)),
        )
        _reject_scope_expansion_inputs(pass_inputs or {})
        passes = self.ledger.list_passes(job_id)
        normalized_inputs = dict(pass_inputs or {})
        pass_input_hash = canonical_hash(
            {
                "pass_name": pass_name,
                "unresolved_question_state": list(unresolved_question_state),
                "pass_inputs": normalized_inputs,
            }
        )
        logical_pass_input_hash = pass_input_hash
        matching = tuple(
            row
            for row in passes
            if row.pass_name == pass_name
            and (
                row.pass_input_hash == pass_input_hash
                or str(row.detail.get("logical_pass_input_hash") or "")
                == pass_input_hash
            )
        )
        existing = next(
            (
                row
                for row in reversed(matching)
                if row.status != ResearchPassStatus.TRANSPORT_PENDING.value
                or row.submit_count == 1
            ),
            None,
        )
        pending_existing = next(
            (
                row
                for row in reversed(matching)
                if row.status == ResearchPassStatus.TRANSPORT_PENDING.value
            ),
            None,
        )
        if (
            existing is not None
            and existing.pass_input_hash != pass_input_hash
            and str(existing.detail.get("logical_pass_input_hash") or "")
            == pass_input_hash
        ):
            stored_inputs = existing.detail.get("pass_inputs")
            if not isinstance(stored_inputs, Mapping):
                raise RuntimeError(
                    "resumed transport pass lacks its immutable compiled inputs"
                )
            normalized_inputs = dict(stored_inputs)
            pass_input_hash = existing.pass_input_hash
        # Zero-submit cap receipts remain append-only evidence.  If a later
        # invocation explicitly raises the browser-pass budget, it may create
        # one new pass that supersedes only that policy-cap receipt.  A real UI
        # transport failure (for example composer size) remains pending and is
        # never auto-retried by changing this accounting bound.
        followup_count = sum(
            row.pass_name != "INITIAL_FULL_RESEARCH"
            and not (
                row.status == ResearchPassStatus.TRANSPORT_PENDING.value
                and row.submit_count == 0
            )
            for row in passes
        )
        resumed_from_transport_pending: ResearchPassRecord | None = None
        if existing is None and pending_existing is not None:
            pending_reason = str(
                pending_existing.detail.get("transport_pending_reason") or ""
            )
            cap_was_explicitly_raised = bool(
                pending_existing.submit_count == 0
                and pending_reason.startswith("bounded browser pass limit ")
                and followup_count < self.max_followup_passes
            )
            if cap_was_explicitly_raised:
                resumed_from_transport_pending = pending_existing
                normalized_inputs = {
                    **normalized_inputs,
                    "transport_resume_receipt": {
                        "supersedes_pass_id": pending_existing.pass_id,
                        "prior_reason": pending_reason,
                        "new_max_followup_passes": self.max_followup_passes,
                    },
                }
                pass_input_hash = canonical_hash(
                    {
                        "pass_name": pass_name,
                        "unresolved_question_state": list(
                            unresolved_question_state
                        ),
                        "pass_inputs": normalized_inputs,
                    }
                )
                existing = next(
                    (
                        row
                        for row in reversed(passes)
                        if row.pass_name == pass_name
                        and row.pass_input_hash == pass_input_hash
                        and row.status
                        != ResearchPassStatus.TRANSPORT_PENDING.value
                    ),
                    None,
                )
            else:
                existing = pending_existing
        if existing is not None:
            if not existing.parent_pass_id:
                raise RuntimeError("follow-up pass is missing parent lineage")
            parent = self.ledger.get_pass(existing.parent_pass_id)
            pass_id = existing.pass_id
        else:
            completed = [
                row for row in passes if row.status == ResearchPassStatus.COMPLETE.value
            ]
            if not completed:
                raise RuntimeError("follow-up requires a completed parent pass")
            parent = completed[-1]
            pass_identity = {
                "job_id": job_id,
                "parent_pass_id": parent.pass_id,
                "pass_name": pass_name,
                "pass_input_hash": pass_input_hash,
            }
            if resumed_from_transport_pending is not None:
                pass_identity["resumed_from_transport_pending_pass_id"] = (
                    resumed_from_transport_pending.pass_id
                )
            pass_id = stable_id("PROPASS", pass_identity)
        compiled = self.compiler.compile(
            packet=packet,
            primary_archetype_ids=primary_archetype_ids,
            pass_name=pass_name,
            existing_verified_ledger_digest=existing_verified_ledger_digest or {},
            unresolved_question_state=unresolved_question_state,
            pass_inputs=normalized_inputs,
            conversation_id=scope.conversation_id,
            research_pass_id=pass_id,
            parent_pass_id=parent.pass_id,
        )
        if existing is not None:
            if (
                existing.pass_input_hash != pass_input_hash
                or existing.parent_pass_id != parent.pass_id
            ):
                raise RuntimeError("existing pass id has different prompt/input lineage")
            if existing.status == ResearchPassStatus.TRANSPORT_PENDING.value:
                if existing.submit_count == 1:
                    # The exactly-once claim is consumed.  This plan can only
                    # enter result recovery; prompt_text is deliberately empty
                    # so it cannot reach preparation or a second DOM click.
                    return FollowupPassPlan(
                        scope=scope,
                        research_pass=existing,
                        prompt_text="",
                        prompt_hash=existing.prompt_hash,
                    )
                return TransportPendingDecision(
                    job_id=job_id,
                    requested_pass_name=pass_name,
                    research_status="TRANSPORT_PENDING",
                    reason=str(
                        existing.detail.get("transport_pending_reason")
                        or "bounded browser pass limit reached; research remains incomplete"
                    ),
                )
            if existing.prompt_hash != compiled.prompt_hash:
                if (
                    existing.submit_count != 1
                    or existing.status
                    not in {
                        ResearchPassStatus.RESEARCH_RUNNING.value,
                        ResearchPassStatus.COMPLETE.value,
                    }
                ):
                    raise RuntimeError(
                        "unsubmitted existing pass differs from the current prompt contract"
                    )
                # A transmitted pass is immutable.  Template evolution may
                # change today's compilation, but crash recovery needs only
                # the durable hash to bind an already-visible/captured result;
                # this empty text can never enter PREPARE_AND_SUBMIT because
                # submit_count is already one.
                return FollowupPassPlan(
                    scope=scope,
                    research_pass=existing,
                    prompt_text="",
                    prompt_hash=existing.prompt_hash,
                )
            return FollowupPassPlan(
                scope=scope,
                research_pass=existing,
                prompt_text=compiled.prompt_text,
                prompt_hash=compiled.prompt_hash,
            )
        # A payload can be rejected by the visible browser transport before it
        # is ever submitted (for example, an oversized verifier-repair batch).
        # Preserve that TRANSPORT_PENDING row for audit, but do not let a zero-
        # submit transport plan consume the bounded count of actual follow-ups.
        if followup_count >= self.max_followup_passes:
            reason = (
                f"bounded browser pass limit {self.max_followup_passes} reached; "
                "research remains incomplete"
            )
            self.ledger.create_followup_pass(
                scope=scope,
                pass_id=pass_id,
                pass_name=pass_name,
                parent_pass_id=parent.pass_id,
                prompt_hash=compiled.prompt_hash,
                pass_input_hash=pass_input_hash,
                detail={
                    "transport_pending_reason": reason,
                    "research_status": "TRANSPORT_PENDING",
                    "score_valid": False,
                    "publication_withheld": True,
                },
                status=ResearchPassStatus.TRANSPORT_PENDING,
            )
            return TransportPendingDecision(
                job_id=job_id,
                requested_pass_name=pass_name,
                research_status="TRANSPORT_PENDING",
                reason=reason,
            )
        record = self.ledger.create_followup_pass(
            scope=scope,
            pass_id=pass_id,
            pass_name=pass_name,
            parent_pass_id=parent.pass_id,
            prompt_hash=compiled.prompt_hash,
            pass_input_hash=pass_input_hash,
            detail={
                "compiled_contract_ids": list(compiled.contract_ids),
                "mandatory_question_ids": list(compiled.mandatory_question_ids),
                "unresolved_question_ids": [
                    str(row.get("question_family_id") or "")
                    for row in unresolved_question_state
                ],
                "pass_inputs": normalized_inputs,
                "logical_pass_input_hash": logical_pass_input_hash,
                "resumed_from_transport_pending_pass_id": (
                    resumed_from_transport_pending.pass_id
                    if resumed_from_transport_pending is not None
                    else None
                ),
            },
        )
        return FollowupPassPlan(
            scope=scope,
            research_pass=record,
            prompt_text=compiled.prompt_text,
            prompt_hash=compiled.prompt_hash,
        )

    async def prepare_followup(
        self,
        plan: FollowupPassPlan,
        adapter: ChatGPTWebAdapter,
    ) -> PreparedFollowupPass:
        if self.store.get_job(plan.scope.job_id).old_job_frozen_at is not None:
            raise ScopeApprovalRequired(
                "old diagnostic conversation is frozen; follow-up preparation is forbidden"
            )
        prepared = await adapter.prepare_followup_without_submit(
            browser_session_id=plan.scope.browser_session_id,
            conversation_id=plan.scope.conversation_id,
            job_id=plan.scope.job_id,
            pass_id=plan.research_pass.pass_id,
            parent_pass_id=plan.research_pass.parent_pass_id or "",
            prompt=plan.prompt_text,
            prompt_hash=plan.prompt_hash,
        )
        if prepared.conversation_id != plan.scope.conversation_id:
            raise RuntimeError("follow-up preparation escaped the approved conversation")
        current = self.ledger.get_pass(plan.research_pass.pass_id)
        if (
            current.status == ResearchPassStatus.PREPARED.value
            and current.submit_count == 0
        ):
            updated = current
        else:
            updated = self.ledger.mark_prepared(plan.research_pass.pass_id)
        if updated.prompt_hash != prepared.prompt_hash:
            raise RuntimeError("prepared follow-up prompt differs from durable pass")
        return prepared

    async def submit_followup(
        self,
        plan: FollowupPassPlan,
        adapter: ChatGPTWebAdapter,
    ) -> FollowupSubmitResult:
        if self.store.get_job(plan.scope.job_id).old_job_frozen_at is not None:
            raise ScopeApprovalRequired(
                "old diagnostic conversation is frozen; follow-up submit is forbidden"
            )
        claimed = self.ledger.claim_submit(plan.research_pass.pass_id)
        proof = ScopedFollowupProof(
            job_id=claimed.job_id,
            pass_id=claimed.pass_id,
            parent_pass_id=claimed.parent_pass_id or "",
            approval_scope_id=claimed.approval_scope_id,
            browser_session_id=plan.scope.browser_session_id,
            conversation_id=claimed.conversation_id,
            prompt_hash=claimed.prompt_hash,
            submit_count=claimed.submit_count,
            _capability=_FOLLOWUP_CAPABILITY,
        )
        try:
            inspection = await adapter.submit_once(proof)
            if inspection.state is not BrowserUIState.RESEARCH_RUNNING:
                raise RuntimeError(
                    f"follow-up send did not enter RESEARCH_RUNNING: {inspection.state.value}"
                )
            if inspection.conversation_id != claimed.conversation_id:
                raise RuntimeError("follow-up response moved to another conversation")
            persistence = await adapter.inspect_submitted_turn_persistence(
                conversation_id=claimed.conversation_id,
                job_id=claimed.job_id,
                pass_id=claimed.pass_id,
                parent_pass_id=claimed.parent_pass_id,
            )
            durable = self.ledger.record_server_persistence_observation(
                claimed.pass_id,
                observation=persistence,
            )
            if not persistence.persistence_confirmed:
                raise FollowupSubmitBlocked(
                    "fresh public conversation did not persist the exact "
                    f"follow-up turn: observation_id={persistence.observation_id}"
                )
        except Exception as error:
            current = self.ledger.get_pass(claimed.pass_id)
            if current.status in {
                ResearchPassStatus.SUBMITTING.value,
                ResearchPassStatus.RESEARCH_RUNNING.value,
            }:
                self.ledger.mark_transport_pending(
                    claimed.pass_id,
                    reason=f"{type(error).__name__}: {error}",
                )
            raise
        return FollowupSubmitResult(research_pass=durable, inspection=inspection)

    def complete_followup(
        self,
        pass_id: str,
        *,
        response_hash: str,
        conversation_id: str,
    ) -> ResearchPassRecord:
        current = self.ledger.get_pass(pass_id)
        if conversation_id != current.conversation_id:
            raise RuntimeError("follow-up completion came from another conversation")
        return self.ledger.complete_pass(pass_id, response_hash=response_hash)

    def confirm_transport_pending_result_visible(
        self,
        pass_id: str,
    ) -> ResearchPassRecord:
        """Promote a claimed timeout only after its exact result is visible."""

        return self.ledger.confirm_transport_pending_submit(pass_id)

    async def resume_intercepted_followup_submit(
        self,
        plan: FollowupPassPlan,
        adapter: ChatGPTWebAdapter,
    ) -> FollowupSubmitResult:
        """Continue the existing claim after a proven pre-dispatch UI block."""

        current = self.ledger.get_pass(plan.research_pass.pass_id)
        if (
            current.status != ResearchPassStatus.TRANSPORT_PENDING.value
            or current.submit_count != 1
        ):
            raise FollowupSubmitBlocked(
                "intercepted recovery requires one claimed transport-pending pass"
            )
        reason = str(current.detail.get("transport_pending_reason") or "")
        failure_hash = canonical_hash({"transport_pending_reason": reason})

        # The send click may have reached ChatGPT even when the local browser
        # call timed out before the ledger transition completed.  Reconcile the
        # exact durable user turn first so a process restart can never click the
        # same claimed pass twice.
        existing = await adapter.inspect_submitted_turn_persistence(
            conversation_id=current.conversation_id,
            job_id=current.job_id,
            pass_id=current.pass_id,
            parent_pass_id=current.parent_pass_id,
        )
        if existing.persistence_confirmed:
            running = self.ledger.record_server_persistence_observation(
                current.pass_id,
                observation=existing,
            )
            inspection = await adapter.inspect_state()
            if inspection.conversation_id != current.conversation_id:
                raise FollowupSubmitBlocked(
                    "persisted follow-up recovery moved to another conversation"
                )
            return FollowupSubmitResult(
                research_pass=running,
                inspection=inspection,
            )

        proof = ScopedFollowupProof(
            job_id=current.job_id,
            pass_id=current.pass_id,
            parent_pass_id=current.parent_pass_id or "",
            approval_scope_id=current.approval_scope_id,
            browser_session_id=plan.scope.browser_session_id,
            conversation_id=current.conversation_id,
            prompt_hash=current.prompt_hash,
            submit_count=current.submit_count,
            _capability=_FOLLOWUP_CAPABILITY,
        )
        await adapter.prepare_intercepted_followup_submit_recovery(
            proof,
            transport_pending_reason=reason,
        )
        inspection = await adapter.submit_once(proof)
        if (
            inspection.state is not BrowserUIState.RESEARCH_RUNNING
            or inspection.conversation_id != current.conversation_id
        ):
            raise FollowupSubmitBlocked(
                "intercepted recovery did not prove the exact conversation running"
            )
        persistence = await adapter.inspect_submitted_turn_persistence(
            conversation_id=current.conversation_id,
            job_id=current.job_id,
            pass_id=current.pass_id,
            parent_pass_id=current.parent_pass_id,
        )
        if not persistence.persistence_confirmed:
            self.ledger.record_server_persistence_observation(
                current.pass_id,
                observation=persistence,
            )
            raise FollowupSubmitBlocked(
                "intercepted click produced only optimistic local UI; "
                f"fresh conversation lacks the pass: {persistence.observation_id}"
            )
        self.ledger.confirm_intercepted_submit_dispatched(
            current.pass_id,
            prior_failure_hash=failure_hash,
        )
        running = self.ledger.record_server_persistence_observation(
            current.pass_id,
            observation=persistence,
        )
        return FollowupSubmitResult(research_pass=running, inspection=inspection)

    async def audit_submitted_followup_persistence(
        self,
        plan: FollowupPassPlan,
        adapter: ChatGPTWebAdapter,
    ) -> FollowupPersistenceAuditResult:
        """Re-audit one already-clicked pass without preparing or submitting."""

        current = self.ledger.get_pass(plan.research_pass.pass_id)
        if (
            current.submit_count != 1
            or current.status
            not in {
                ResearchPassStatus.RESEARCH_RUNNING.value,
                ResearchPassStatus.TRANSPORT_PENDING.value,
            }
            or not current.parent_pass_id
        ):
            raise FollowupSubmitBlocked(
                "server-persistence audit requires one claimed unsnapshotted follow-up"
            )
        observation = await adapter.inspect_submitted_turn_persistence(
            conversation_id=current.conversation_id,
            job_id=current.job_id,
            pass_id=current.pass_id,
            parent_pass_id=current.parent_pass_id,
        )
        updated = self.ledger.record_server_persistence_observation(
            current.pass_id,
            observation=observation,
        )
        sealed = False
        if (
            not observation.persistence_confirmed
            and int(
                updated.detail.get(
                    "server_persistence_absence_confirmation_count"
                )
                or 0
            )
            >= 2
        ):
            updated = self.ledger.seal_unpersisted_dispatch(current.pass_id)
            sealed = True
        return FollowupPersistenceAuditResult(
            research_pass=updated,
            observation=observation,
            sealed_unpersisted=sealed,
        )

    def _job_conversation(self, job_id: str) -> str:
        conversation_id = self.store.get_job(job_id).conversation_id
        if not conversation_id:
            raise ScopeApprovalRequired("job has no durable ChatGPT conversation")
        return conversation_id


def scope_conversation(packet: Mapping[str, Any], *, fallback: str) -> str:
    declared = str(packet.get("conversation_id") or "")
    if declared and declared != fallback:
        return declared
    return fallback


def _reject_scope_expansion_inputs(value: Any, path: tuple[str, ...] = ()) -> None:
    """Reject follow-up inputs that explicitly require authority outside the grant."""

    forbidden_true_flags = {
        "requires_new_private_access",
        "requires_private_account",
        "new_authenticated_site",
        "private_site_access",
        "requires_user_judgment",
        "investment_assumption_required",
    }
    if isinstance(value, Mapping):
        for key, nested in value.items():
            normalized = str(key).strip().casefold()
            next_path = (*path, str(key))
            if normalized in forbidden_true_flags and nested is True:
                raise ScopeApprovalRequired(
                    "follow-up requires new approval for " + ".".join(next_path)
                )
            if normalized == "access_scope" and str(nested).strip().upper() not in {
                "PUBLIC",
                "PUBLIC_WEB",
                "CURRENT_CHATGPT_PRO",
            }:
                raise ScopeApprovalRequired(
                    "follow-up access scope is outside the initial public research grant"
                )
            _reject_scope_expansion_inputs(nested, next_path)
    elif isinstance(value, (list, tuple)):
        for index, nested in enumerate(value):
            _reject_scope_expansion_inputs(nested, (*path, str(index)))


__all__ = [
    "FollowupSubmitResult",
    "FollowupPersistenceAuditResult",
    "ProMultiPassResearchOrchestrator",
    "ScopedFollowupProof",
]
