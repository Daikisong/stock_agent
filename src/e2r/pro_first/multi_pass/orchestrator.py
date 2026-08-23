"""Contract-scoped, same-conversation Pro V2 follow-up orchestration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

from ..browser.protocol import (
    BrowserInspection,
    BrowserUIState,
    ChatGPTWebAdapter,
    PreparedFollowupPass,
)
from ..ids import canonical_hash, stable_id
from ..job_store import ProFirstJobStore
from ..research_contracts import ProResearchPromptCompilerV2
from .ledger import ProMultiPassLedger
from .models import (
    FollowupPassPlan,
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
    ) -> ResearchApprovalScope:
        return self.ledger.establish_initial_scope(
            job_id,
            primary_archetype_ids=primary_archetype_ids,
            initial_response_hash=response_hash,
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
                pass_name="COUNTER_SUPERSESSION",
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
        existing = next(
            (
                row
                for row in passes
                if row.pass_name == pass_name and row.pass_input_hash == pass_input_hash
            ),
            None,
        )
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
            pass_id = stable_id(
                "PROPASS",
                {
                    "job_id": job_id,
                    "parent_pass_id": parent.pass_id,
                    "pass_name": pass_name,
                    "pass_input_hash": pass_input_hash,
                },
            )
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
                existing.prompt_hash != compiled.prompt_hash
                or existing.pass_input_hash != pass_input_hash
                or existing.parent_pass_id != parent.pass_id
            ):
                raise RuntimeError("existing pass id has different prompt/input lineage")
            if existing.status == ResearchPassStatus.TRANSPORT_PENDING.value:
                return TransportPendingDecision(
                    job_id=job_id,
                    requested_pass_name=pass_name,
                    research_status="TRANSPORT_PENDING",
                    reason=str(
                        existing.detail.get("transport_pending_reason")
                        or "bounded browser pass limit reached; research remains incomplete"
                    ),
                )
            return FollowupPassPlan(
                scope=scope,
                research_pass=existing,
                prompt_text=compiled.prompt_text,
                prompt_hash=compiled.prompt_hash,
            )
        followup_count = sum(row.pass_name != "INITIAL_FULL_RESEARCH" for row in passes)
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
        updated = self.ledger.mark_prepared(plan.research_pass.pass_id)
        if updated.prompt_hash != prepared.prompt_hash:
            raise RuntimeError("prepared follow-up prompt differs from durable pass")
        return prepared

    async def submit_followup(
        self,
        plan: FollowupPassPlan,
        adapter: ChatGPTWebAdapter,
    ) -> FollowupSubmitResult:
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
        except Exception as error:
            self.ledger.mark_transport_pending(
                claimed.pass_id,
                reason=f"{type(error).__name__}: {error}",
            )
            raise
        running = self.ledger.mark_running(claimed.pass_id)
        return FollowupSubmitResult(research_pass=running, inspection=inspection)

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
    "ProMultiPassResearchOrchestrator",
    "ScopedFollowupProof",
]
