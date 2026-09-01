"""Fresh-blind ResearchPacketV3 and same-conversation pass orchestration."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..approval import ExactlyOnceSubmitCoordinator, SubmitResult
from ..browser.protocol import ChatGPTWebAdapter, PreparedBrowserJob
from ..browser.worker import BrowserWorkerSession, ProBrowserWorker
from ..config import ProFirstLocalConfig
from ..ids import canonical_hash, canonical_json, stable_id
from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob
from ..multi_pass import (
    ARTIFACT_REEXPORT_PASS_NAME,
    FollowupPassPlan,
    ProMultiPassLedger,
    ProMultiPassResearchOrchestrator,
    ResearchApprovalScope,
    ResearchPassStatus,
)
from ..multi_pass.models import (
    COUNTER_SUPERSESSION_PASS_NAME,
    INITIAL_PASS_NAME,
)
from ..operations import (
    DEFAULT_FORBIDDEN_INFERENCES,
    DEFAULT_RESEARCH_OBJECTIVES,
    DEFAULT_SOURCE_PREFERENCES,
)
from ..packet import (
    PACKET_V3_SCHEMA_VERSION,
    PacketBuildInput,
    PacketBundleReceipt,
    ResearchPacketV3Builder,
    write_packet_bundle,
)
from ..repair import CompactRepairPromptCompilerV3
from ..repair.models_v3 import CompiledCompactRepairPromptV3
from ..research_contracts import (
    CompiledProResearchPromptV3,
    ProResearchPromptCompilerV3,
)
from .boundary import (
    FreshBlindLeakageAudit,
    FreshSessionBoundary,
    FreshSessionBoundaryError,
    FreshSessionRerunRequired,
    assert_fresh_prompt_has_no_old_answers,
    audit_fresh_blind_payload,
    write_runtime_json_once,
)


_GAP_PASS_NAMES = frozenset(
    {"PUBLIC_GAP_CLOSURE", COUNTER_SUPERSESSION_PASS_NAME}
)
_NON_REPAIR_V3_FOLLOWUPS = frozenset(
    (*_GAP_PASS_NAMES, "SATURATION_AUDIT", ARTIFACT_REEXPORT_PASS_NAME)
)
_MAX_FOLLOWUP_PROMPT_CHARS = 100_000
# Repeated inline-contract new-chat submissions, including one at 50,856
# characters through framework-owned input, cleared the visible composer
# without a durable user turn.  Live initial transport therefore uses a short
# envelope whose complete protocol/contracts/schema live in the hash-bound
# packet.  The full V3 compiler still supports larger offline audit snapshots.
_MAX_LIVE_INITIAL_PROMPT_CHARS = 10_000


@dataclass(frozen=True)
class BuiltFreshV3JobPacket:
    boundary: FreshSessionBoundary
    job: ProResearchJob
    packet_bundle: PacketBundleReceipt
    packet_payload: Mapping[str, Any]
    prompt: CompiledProResearchPromptV3
    initial_pass_id: str
    output_filename: str
    packet_leakage_audit: FreshBlindLeakageAudit
    prompt_leakage_receipt: Mapping[str, Any]


@dataclass(frozen=True)
class PreparedFreshV3Initial:
    job: ProResearchJob
    prepared: PreparedBrowserJob
    receipt: Mapping[str, Any]


@dataclass
class PreparedFreshV3BrowserRuntime:
    built: BuiltFreshV3JobPacket
    prepared: PreparedFreshV3Initial
    session: BrowserWorkerSession

    async def close(self) -> None:
        await self.session.close()


@dataclass(frozen=True)
class FreshInitialSubmitResult:
    submit_result: SubmitResult
    receipt: Mapping[str, Any]


@dataclass(frozen=True)
class CompiledFreshFollowupV3:
    pass_name: str
    prompt_text: str
    prompt_hash: str
    pass_input_hash: str
    research_pass_id: str
    parent_pass_id: str
    context_hash: str


class FreshSessionOrchestratorV3:
    """Orchestrate a blind initial pass and a bounded same-chat tail.

    The initial pass must start at ChatGPT's new-chat route.  Only after the
    first DOM click produces a canonical conversation ID may the initial user
    approval be expanded to bounded public-gap, one semantic repair, and one
    saturation pass in that exact conversation.
    """

    def __init__(
        self,
        store: ProFirstJobStore,
        boundary: FreshSessionBoundary,
        *,
        initial_compiler: ProResearchPromptCompilerV3 | None = None,
        repair_compiler: CompactRepairPromptCompilerV3 | None = None,
        ledger: ProMultiPassLedger | None = None,
    ) -> None:
        self.store = store
        self.boundary = boundary
        self.initial_compiler = initial_compiler or ProResearchPromptCompilerV3()
        self.repair_compiler = repair_compiler or CompactRepairPromptCompilerV3()
        self.ledger = ledger or ProMultiPassLedger(store)
        self.followup_transport = ProMultiPassResearchOrchestrator(
            store,
            ledger=self.ledger,
        )
        if self.boundary.fresh_job_id == self.boundary.old_job_id:
            raise FreshSessionBoundaryError("fresh orchestrator reused the old job")

    def build_initial_packet(
        self,
        *,
        commit_sha: str,
        config_hash: str,
        business_snapshot: Mapping[str, Any] | None = None,
        structured_financial_snapshot: Mapping[str, Any] | None = None,
        revision_valuation_snapshot: Mapping[str, Any] | None = None,
        research_objectives: Sequence[str] = DEFAULT_RESEARCH_OBJECTIVES,
        source_preferences: Sequence[str] = DEFAULT_SOURCE_PREFERENCES,
        forbidden_inferences: Sequence[str] = DEFAULT_FORBIDDEN_INFERENCES,
    ) -> BuiltFreshV3JobPacket:
        job = self.store.get_job(self.boundary.fresh_job_id)
        if job.status == JobStatus.CANDIDATE_SELECTED.value:
            job = self.store.transition(
                job.job_id,
                expected_version=job.state_version,
                to_status=JobStatus.PACKET_BUILDING,
                actor="v2.1-fresh-v3-packet-builder",
                idempotency_key=f"fresh-v3-packet-building:{job.job_id}",
            )
        allowed = {
            JobStatus.PACKET_BUILDING.value,
            JobStatus.PACKET_READY.value,
            JobStatus.BROWSER_PREPARING.value,
            JobStatus.AWAITING_USER_APPROVAL.value,
            # Recovery may only reuse the hash-bound durable packet below;
            # it may not build a replacement while the job needs attention.
            JobStatus.USER_ATTENTION_REQUIRED.value,
            # A submitted-run recovery only recompiles and hash-checks the
            # already durable packet/prompt.  It must never create a packet in
            # any of these states.
            JobStatus.RESEARCH_RUNNING.value,
            JobStatus.RESULT_DETECTED.value,
            JobStatus.CAPTURING_ARTIFACTS.value,
            JobStatus.CAPTURE_COMPLETE.value,
            JobStatus.IMPORTING.value,
            JobStatus.DOSSIER_IMPORTED.value,
            JobStatus.VERIFYING_SOURCES.value,
            JobStatus.GAP_ADJUDICATION.value,
        }
        if job.status not in allowed:
            raise ValueError(f"fresh V3 packet cannot build/reuse from {job.status}")
        packet_path = self.boundary.fresh_job_root / "packet/research_packet.json"
        manifest_path = self.boundary.fresh_job_root / "packet/packet_manifest.json"
        if job.packet_hash and packet_path.is_file() and manifest_path.is_file():
            packet_payload = json.loads(packet_path.read_text(encoding="utf-8"))
            if packet_payload.get("schema_version") != PACKET_V3_SCHEMA_VERSION:
                raise FreshSessionBoundaryError(
                    "durable fresh job packet is not ResearchPacketV3"
                )
            if canonical_hash(packet_payload) != job.packet_hash:
                raise FreshSessionBoundaryError(
                    "durable fresh packet differs from its database hash"
                )
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            bundle = PacketBundleReceipt(
                packet_directory=packet_path.parent,
                research_packet_json=packet_path,
                research_packet_markdown=packet_path.with_name(
                    "research_packet.md"
                ),
                packet_manifest=manifest_path,
                packet_hash=job.packet_hash,
                manifest_hash=canonical_hash(manifest),
            )
        else:
            if job.status not in {
                JobStatus.PACKET_BUILDING.value,
                JobStatus.PACKET_READY.value,
            }:
                raise FreshSessionBoundaryError(
                    "submitted fresh recovery requires the existing hash-bound packet"
                )
            candidate = self.store.get_candidate(job.candidate_id)
            selection = dict(candidate.selection_receipt)
            trigger_ids = tuple(
                str(value) for value in selection.get("trigger_ids") or ()
            )
            reasons = tuple(
                str(value) for value in selection.get("reason_codes") or ()
            )
            trigger_summary = tuple(
                {
                    "trigger_id": trigger_id,
                    "reason": ", ".join(reasons)
                    or "fresh blind Pro validation",
                }
                for trigger_id in trigger_ids
            )
            packet = ResearchPacketV3Builder().build(
                PacketBuildInput(
                    job_id=job.job_id,
                    symbol=job.symbol,
                    company_name=job.company_name,
                    aliases=(job.company_name, job.symbol),
                    as_of_date=job.as_of_date,
                    latest_trading_snapshot_date=job.as_of_date,
                    research_mode=job.mode,
                    trigger_summary=trigger_summary,
                    candidate_archetypes=job.archetype_ids,
                    business_snapshot=dict(business_snapshot or {}),
                    structured_financial_snapshot=dict(
                        structured_financial_snapshot or {}
                    ),
                    revision_valuation_snapshot=dict(
                        revision_valuation_snapshot or {}
                    ),
                    research_objectives=tuple(research_objectives),
                    source_preferences=tuple(source_preferences),
                    forbidden_inferences=tuple(forbidden_inferences),
                )
            )
            packet_payload = dict(packet.payload)
            if packet_payload["run_id"] == self.boundary.old_run_id:
                raise FreshSessionBoundaryError("fresh packet reused the old run ID")
            packet_audit = audit_fresh_blind_payload(
                packet_payload,
                self.boundary.leakage_manifest,
            )
            if not packet_audit.passed:
                raise FreshSessionBoundaryError(
                    "fresh ResearchPacketV3 contains old-run answer leakage"
                )
            bundle = write_packet_bundle(
                packet,
                self.boundary.fresh_job_root / "packet",
                commit_sha=commit_sha,
                config_hash=config_hash,
            )
            manifest = json.loads(
                bundle.packet_manifest.read_text(encoding="utf-8")
            )
            job = self.store.record_packet(
                job.job_id,
                expected_version=job.state_version,
                packet_id=stable_id(
                    "PROPACKET",
                    {"job_id": job.job_id, "packet_hash": packet.packet_hash},
                ),
                packet_hash=packet.packet_hash,
                manifest=manifest,
                actor="v2.1-fresh-v3-packet-builder",
                idempotency_key=(
                    f"fresh-v3-packet-ready:{job.job_id}:{packet.packet_hash}"
                ),
            )

        packet_audit = audit_fresh_blind_payload(
            packet_payload,
            self.boundary.leakage_manifest,
        )
        if not packet_audit.passed:
            raise FreshSessionBoundaryError(
                "reused fresh ResearchPacketV3 fails the blind leakage audit"
            )
        initial_pass_id = stable_id(
            "PROPASS",
            {
                "job_id": job.job_id,
                "run_id": packet_payload["run_id"],
                "pass_name": INITIAL_PASS_NAME,
                "packet_hash": bundle.packet_hash,
                "fresh_session_id": self.boundary.fresh_session_id,
            },
        )
        if initial_pass_id in set(
            self.boundary.leakage_manifest.old_research_pass_ids
        ):
            raise FreshSessionBoundaryError("fresh initial pass reused an old pass ID")
        contract_prompt = self.initial_compiler.compile(
            packet=packet_payload,
            primary_archetype_ids=job.archetype_ids,
            conversation_id="PENDING_NEW_CONVERSATION",
            research_pass_id=initial_pass_id,
            parent_pass_id=None,
        )
        prompt = self.initial_compiler.compile_transport_envelope(
            packet=packet_payload,
            primary_archetype_ids=job.archetype_ids,
            conversation_id="PENDING_NEW_CONVERSATION",
            research_pass_id=initial_pass_id,
            parent_pass_id=None,
        )
        if (
            prompt.primary_archetype_ids != contract_prompt.primary_archetype_ids
            or prompt.contract_ids != contract_prompt.contract_ids
            or prompt.mandatory_question_ids
            != contract_prompt.mandatory_question_ids
            or prompt.dossier_schema_hash
            != contract_prompt.dossier_schema_hash
        ):
            raise FreshSessionBoundaryError(
                "attachment-backed transport envelope differs from the compiled V3 contract"
            )
        prompt_audit = assert_fresh_prompt_has_no_old_answers(
            prompt.prompt_text,
            self.boundary.leakage_manifest,
        )
        audit_root = self.boundary.fresh_job_root / "fresh_session"
        write_runtime_json_once(
            audit_root / "fresh_blind_packet_audit.json",
            packet_audit.to_dict(),
        )
        write_runtime_json_once(
            audit_root / "fresh_initial_prompt_leakage_audit.json",
            prompt_audit,
        )
        write_runtime_json_once(
            audit_root / "initial_prompt_v3_receipt.json",
            {
                **prompt.to_receipt(),
                "delivery_mode": "ATTACHMENT_BACKED_TRANSPORT_ENVELOPE",
                "compiled_contract_prompt_hash": contract_prompt.prompt_hash,
                "compiled_contract_prompt_char_count": len(
                    contract_prompt.prompt_text
                ),
                "initial_protocol_hash": packet_payload[
                    "initial_research_protocol"
                ]["protocol_hash"],
                "contract_snapshot_hash": packet_payload[
                    "research_contract_snapshot"
                ]["snapshot_hash"],
                "dossier_output_schema_hash": packet_payload[
                    "dossier_output_schema_hash"
                ],
            },
        )
        write_runtime_json_once(
            audit_root / "initial_prompt_v3_contract_receipt.json",
            {
                **contract_prompt.to_receipt(),
                "delivery_mode": "HASH_BOUND_RESEARCH_PACKET_FIELDS",
                "packet_field_paths": [
                    "initial_research_protocol.instructions_markdown",
                    "research_contract_snapshot.contracts",
                    "dossier_output_schema",
                ],
                "transport_prompt_hash": prompt.prompt_hash,
                "transport_prompt_char_count": len(prompt.prompt_text),
            },
        )
        return BuiltFreshV3JobPacket(
            boundary=self.boundary,
            job=self.store.get_job(job.job_id),
            packet_bundle=bundle,
            packet_payload=packet_payload,
            prompt=prompt,
            initial_pass_id=initial_pass_id,
            output_filename=(
                f"E2R_PRO_V3_{job.job_id}_{job.symbol}_{job.as_of_date}.md"
            ),
            packet_leakage_audit=packet_audit,
            prompt_leakage_receipt=prompt_audit,
        )

    def load_initial_packet_for_submitted_recovery(
        self,
        *,
        commit_sha: str,
        config_hash: str,
    ) -> BuiltFreshV3JobPacket:
        """Load the exact submitted packet and prompt receipts without recompiling.

        A post-submit recovery can run after the common prompt template has been
        improved. Recompiling in that situation would compare a new prompt with
        the immutable prompt that was actually submitted and fail before import.
        This loader verifies the durable artifacts instead. The receipt-only
        prompt text is a length-preserving placeholder and must never be sent to
        a browser.
        """

        job = self.store.get_job(self.boundary.fresh_job_id)
        if job.submit_count != 1 or not job.packet_hash:
            raise FreshSessionBoundaryError(
                "submitted recovery requires one exact submit and a durable packet"
            )
        packet_root = self.boundary.fresh_job_root / "packet"
        packet_path = packet_root / "research_packet.json"
        packet_markdown_path = packet_root / "research_packet.md"
        manifest_path = packet_root / "packet_manifest.json"
        required_paths = (packet_path, packet_markdown_path, manifest_path)
        if any(not path.is_file() for path in required_paths):
            raise FreshSessionBoundaryError(
                "submitted recovery requires the complete immutable packet bundle"
            )
        packet_payload = json.loads(packet_path.read_text(encoding="utf-8"))
        if (
            packet_payload.get("schema_version") != PACKET_V3_SCHEMA_VERSION
            or canonical_hash(packet_payload) != job.packet_hash
        ):
            raise FreshSessionBoundaryError(
                "submitted recovery packet differs from the durable job"
            )
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if (
            str(manifest.get("packet_hash") or "") != job.packet_hash
            or str(manifest.get("job_id") or "") != job.job_id
            or str(manifest.get("run_id") or "")
            != str(packet_payload.get("run_id") or "")
            or str(manifest.get("commit_sha") or "") != str(commit_sha)
            or str(manifest.get("config_hash") or "") != str(config_hash)
        ):
            raise FreshSessionBoundaryError(
                "submitted recovery packet manifest identity differs"
            )
        bundle = PacketBundleReceipt(
            packet_directory=packet_root,
            research_packet_json=packet_path,
            research_packet_markdown=packet_markdown_path,
            packet_manifest=manifest_path,
            packet_hash=job.packet_hash,
            manifest_hash=canonical_hash(manifest),
        )

        packet_audit = audit_fresh_blind_payload(
            packet_payload,
            self.boundary.leakage_manifest,
        )
        packet_audit_path = (
            self.boundary.fresh_job_root
            / "fresh_session/fresh_blind_packet_audit.json"
        )
        prompt_audit_path = (
            self.boundary.fresh_job_root
            / "fresh_session/fresh_initial_prompt_leakage_audit.json"
        )
        prompt_receipt_path = (
            self.boundary.fresh_job_root
            / "fresh_session/initial_prompt_v3_receipt.json"
        )
        if any(
            not path.is_file()
            for path in (packet_audit_path, prompt_audit_path, prompt_receipt_path)
        ):
            raise FreshSessionBoundaryError(
                "submitted recovery requires immutable initial prompt receipts"
            )
        stored_packet_audit = json.loads(
            packet_audit_path.read_text(encoding="utf-8")
        )
        if not packet_audit.passed or stored_packet_audit != packet_audit.to_dict():
            raise FreshSessionBoundaryError(
                "submitted recovery packet leakage receipt differs"
            )
        prompt_audit = json.loads(prompt_audit_path.read_text(encoding="utf-8"))
        prompt_receipt = json.loads(
            prompt_receipt_path.read_text(encoding="utf-8")
        )
        prompt_hash = str(prompt_receipt.get("prompt_hash") or "")
        prompt_char_count = int(prompt_receipt.get("prompt_char_count") or 0)
        mandatory_question_ids = tuple(
            str(value)
            for value in prompt_receipt.get("mandatory_question_ids") or ()
        )
        if (
            prompt_receipt.get("schema_version")
            != "e2r_compiled_pro_research_prompt_v3"
            or prompt_receipt.get("pass_name") != INITIAL_PASS_NAME
            or tuple(prompt_receipt.get("primary_archetype_ids") or ())
            != job.archetype_ids
            or len(mandatory_question_ids)
            != int(prompt_receipt.get("mandatory_question_count") or -1)
            or len(mandatory_question_ids) != len(set(mandatory_question_ids))
            or not mandatory_question_ids
            or prompt_char_count <= 0
            or not prompt_hash
            or job.approval_prompt_hash != prompt_hash
            or prompt_receipt.get("score_authority") is not False
            or prompt_receipt.get("stage_authority") is not False
        ):
            raise FreshSessionBoundaryError(
                "submitted recovery initial prompt receipt differs from the durable job"
            )
        unsigned_prompt_audit = dict(prompt_audit)
        stored_prompt_audit_hash = str(
            unsigned_prompt_audit.pop("receipt_hash", "")
        )
        if (
            canonical_hash(unsigned_prompt_audit) != stored_prompt_audit_hash
            or prompt_audit.get("status") != "PASS"
            or prompt_audit.get("prompt_hash") != prompt_hash
            or prompt_audit.get("score_authority") is not False
            or prompt_audit.get("stage_authority") is not False
        ):
            raise FreshSessionBoundaryError(
                "submitted recovery initial prompt leakage receipt differs"
            )

        initial_pass_id = stable_id(
            "PROPASS",
            {
                "job_id": job.job_id,
                "run_id": packet_payload["run_id"],
                "pass_name": INITIAL_PASS_NAME,
                "packet_hash": bundle.packet_hash,
                "fresh_session_id": self.boundary.fresh_session_id,
            },
        )
        browser_state = self.store.get_browser_session_state(job.job_id) or {}
        durable_initial_pass_id = str(
            (browser_state.get("state") or {}).get("initial_pass_id") or ""
        )
        if durable_initial_pass_id != initial_pass_id:
            raise FreshSessionBoundaryError(
                "submitted recovery initial pass identity differs"
            )
        prompt = CompiledProResearchPromptV3(
            pass_name=INITIAL_PASS_NAME,
            primary_archetype_ids=job.archetype_ids,
            contract_ids=tuple(
                str(value) for value in prompt_receipt.get("contract_ids") or ()
            ),
            mandatory_question_ids=mandatory_question_ids,
            prompt_text=" " * prompt_char_count,
            prompt_hash=prompt_hash,
            dossier_schema_hash=str(
                prompt_receipt.get("dossier_schema_hash") or ""
            ),
        )
        return BuiltFreshV3JobPacket(
            boundary=self.boundary,
            job=job,
            packet_bundle=bundle,
            packet_payload=packet_payload,
            prompt=prompt,
            initial_pass_id=initial_pass_id,
            output_filename=(
                f"E2R_PRO_V3_{job.job_id}_{job.symbol}_{job.as_of_date}.md"
            ),
            packet_leakage_audit=packet_audit,
            prompt_leakage_receipt=prompt_audit,
        )

    async def prepare_initial_with_adapter(
        self,
        built: BuiltFreshV3JobPacket,
        adapter: ChatGPTWebAdapter,
        *,
        browser_session_id: str,
    ) -> PreparedFreshV3Initial:
        job = self._ensure_browser_preparing(built.job.job_id)
        if job.status != JobStatus.BROWSER_PREPARING.value:
            raise ValueError(
                "fresh initial preparation requires BROWSER_PREPARING, "
                f"got {job.status}"
            )
        try:
            inspection = await adapter.ensure_logged_in()
            if inspection.conversation_id is not None:
                raise FreshSessionBoundaryError(
                    "fresh initial preparation must start on the new-chat route"
                )
            prepared = await adapter.prepare_without_submit(
                browser_session_id=browser_session_id,
                packet_path=built.packet_bundle.research_packet_json,
                packet_hash=built.packet_bundle.packet_hash,
                prompt=built.prompt.prompt_text,
                prompt_hash=built.prompt.prompt_hash,
            )
            if prepared.conversation_id is not None:
                raise FreshSessionBoundaryError(
                    "fresh packet was prepared inside an existing conversation"
                )
        except Exception as error:
            self._record_browser_attention(built.job.job_id, error)
            raise
        job = self.store.record_browser_prepared(
            job.job_id,
            expected_version=job.state_version,
            browser_session_id=prepared.browser_session_id,
            conversation_id=None,
            adapter_name="PlaywrightChatGPTWebAdapterV3Fresh",
            packet_hash=prepared.packet_hash,
            prompt_hash=prepared.prompt_hash,
            state={
                "state": prepared.state.value,
                "uploaded_filename": prepared.uploaded_filename,
                "send_ready": prepared.send_ready,
                "pro_mode_ready": prepared.deep_research_ready,
                "legacy_deep_research_allowed": False,
                "new_chat_route_verified": True,
                "initial_pass_id": built.initial_pass_id,
                "packet_schema_version": PACKET_V3_SCHEMA_VERSION,
                "submit_count": 0,
            },
            actor="v2.1-fresh-v3-browser-worker",
            idempotency_key=(
                f"fresh-v3-browser-prepared:{job.job_id}:{prepared.prompt_hash}"
            ),
        )
        unsigned = {
            "schema_version": "e2r_pro_fresh_v3_prepare_receipt_v1",
            "status": "FRESH_NEW_CHAT_PREPARED_AWAITING_APPROVAL",
            "fresh_session_id": self.boundary.fresh_session_id,
            "job_id": job.job_id,
            "run_id": built.packet_payload["run_id"],
            "initial_pass_id": built.initial_pass_id,
            "old_conversation_id": self.boundary.old_conversation_id,
            "prepared_conversation_id": None,
            "new_chat_route_verified": True,
            "packet_hash": prepared.packet_hash,
            "prompt_hash": prepared.prompt_hash,
            "submit_count": 0,
            "score_authority": False,
            "stage_authority": False,
        }
        receipt = {**unsigned, "receipt_hash": canonical_hash(unsigned)}
        write_runtime_json_once(
            self.boundary.fresh_job_root
            / "fresh_session/fresh_v3_prepare_receipt.json",
            receipt,
        )
        return PreparedFreshV3Initial(job=job, prepared=prepared, receipt=receipt)

    async def prepare_initial_in_logged_in_browser(
        self,
        built: BuiltFreshV3JobPacket,
        *,
        config: ProFirstLocalConfig,
    ) -> PreparedFreshV3BrowserRuntime:
        if len(built.prompt.prompt_text) > _MAX_LIVE_INITIAL_PROMPT_CHARS:
            raise FreshSessionBoundaryError(
                "fresh initial prompt exceeds the 59,800 character "
                "public-composer safety boundary"
            )
        self._ensure_browser_preparing(built.job.job_id)
        try:
            session = await ProBrowserWorker(config.browser).open(
                job_id=built.job.job_id
            )
        except Exception as error:
            self._record_browser_attention(built.job.job_id, error)
            raise
        try:
            current_conversation = session.adapter.conversation_id()
            if (
                self.boundary.predecessor_required
                and current_conversation
                not in {None, self.boundary.old_conversation_id}
            ):
                raise FreshSessionBoundaryError(
                    "matched ChatGPT tab is unrelated to the frozen E2R conversation"
                )
            await session.page.goto(
                config.browser.chatgpt_url,
                wait_until="domcontentloaded",
            )
            if session.adapter.conversation_id() is not None:
                raise FreshSessionBoundaryError(
                    "browser did not reach a clean ChatGPT new-chat route"
                )
            prepared = await self.prepare_initial_with_adapter(
                built,
                session.adapter,
                browser_session_id=session.browser_session_id,
            )
            return PreparedFreshV3BrowserRuntime(
                built=built,
                prepared=prepared,
                session=session,
            )
        except Exception:
            await session.close()
            raise

    async def recover_prepared_initial_in_logged_in_browser(
        self,
        built: BuiltFreshV3JobPacket,
        *,
        config: ProFirstLocalConfig,
    ) -> PreparedFreshV3BrowserRuntime:
        """Adopt an exact intact new-chat draft after preparation timed out."""

        job = self._ensure_browser_preparing(built.job.job_id)
        if job.submit_count != 0 or job.conversation_id is not None:
            raise FreshSessionBoundaryError(
                "prepared-draft recovery is allowed only before the first submit"
            )
        try:
            session = await ProBrowserWorker(config.browser).open(job_id=job.job_id)
        except Exception as error:
            self._record_browser_attention(job.job_id, error)
            raise
        try:
            if session.adapter.conversation_id() is not None:
                raise FreshSessionBoundaryError(
                    "prepared-draft recovery left the original new-chat route"
                )
            prepared = await session.adapter.recover_initial_prepared_without_mutation(
                browser_session_id=session.browser_session_id,
                packet_path=built.packet_bundle.research_packet_json,
                packet_hash=built.packet_bundle.packet_hash,
                prompt=built.prompt.prompt_text,
                prompt_hash=built.prompt.prompt_hash,
            )
            job = self.store.record_browser_prepared(
                job.job_id,
                expected_version=job.state_version,
                browser_session_id=prepared.browser_session_id,
                conversation_id=None,
                adapter_name="PlaywrightChatGPTWebAdapterV3FreshRecoveredDraft",
                packet_hash=prepared.packet_hash,
                prompt_hash=prepared.prompt_hash,
                state={
                    "state": prepared.state.value,
                    "uploaded_filename": prepared.uploaded_filename,
                    "send_ready": prepared.send_ready,
                    "pro_mode_ready": prepared.deep_research_ready,
                    "legacy_deep_research_allowed": False,
                    "new_chat_route_verified": True,
                    "initial_pass_id": built.initial_pass_id,
                    "packet_schema_version": PACKET_V3_SCHEMA_VERSION,
                    "prepared_draft_recovered_without_upload_or_input": True,
                    "submit_count": 0,
                },
                actor="v2.1-fresh-v3-browser-draft-recovery",
                idempotency_key=(
                    f"fresh-v3-browser-draft-recovered:{job.job_id}:"
                    f"{prepared.prompt_hash}"
                ),
            )
            unsigned = {
                "schema_version": "e2r_pro_fresh_v3_prepare_receipt_v1",
                "status": "FRESH_NEW_CHAT_DRAFT_RECOVERED_AWAITING_APPROVAL",
                "fresh_session_id": self.boundary.fresh_session_id,
                "job_id": job.job_id,
                "run_id": built.packet_payload["run_id"],
                "initial_pass_id": built.initial_pass_id,
                "old_conversation_id": self.boundary.old_conversation_id,
                "prepared_conversation_id": None,
                "new_chat_route_verified": True,
                "prepared_draft_recovered_without_upload_or_input": True,
                "packet_hash_verified_in_browser": True,
                "prompt_hash_verified_in_browser": True,
                "packet_hash": prepared.packet_hash,
                "prompt_hash": prepared.prompt_hash,
                "submit_count": 0,
                "score_authority": False,
                "stage_authority": False,
            }
            receipt = {**unsigned, "receipt_hash": canonical_hash(unsigned)}
            write_runtime_json_once(
                self.boundary.fresh_job_root
                / "fresh_session/fresh_v3_prepare_receipt.json",
                receipt,
            )
            return PreparedFreshV3BrowserRuntime(
                built=built,
                prepared=PreparedFreshV3Initial(
                    job=job,
                    prepared=prepared,
                    receipt=receipt,
                ),
                session=session,
            )
        except Exception as error:
            await session.close()
            self._record_browser_attention(job.job_id, error)
            raise

    async def submit_initial_once(
        self,
        adapter: ChatGPTWebAdapter,
    ) -> FreshInitialSubmitResult:
        result = await ExactlyOnceSubmitCoordinator(self.store).submit(
            self.boundary.fresh_job_id,
            adapter,
            actor="v2.1-fresh-v3-browser-worker",
        )
        conversation_id = result.inspection.conversation_id
        passed = bool(
            conversation_id
            and conversation_id != self.boundary.old_conversation_id
        )
        unsigned = {
            "schema_version": "e2r_pro_fresh_initial_submit_receipt_v1",
            "status": (
                "FRESH_CONVERSATION_CONFIRMED"
                if passed
                else "DIAGNOSTIC_ONLY_NEW_CONVERSATION_REQUIRED"
            ),
            "fresh_session_id": self.boundary.fresh_session_id,
            "job_id": result.job.job_id,
            "old_conversation_id": self.boundary.old_conversation_id,
            "new_conversation_id": conversation_id,
            "new_conversation": passed,
            "submit_count": result.job.submit_count,
            "automatic_resubmit_allowed": False,
            "same_conversation_followups_allowed": passed,
            "score_authority": False,
            "stage_authority": False,
        }
        receipt = {**unsigned, "receipt_hash": canonical_hash(unsigned)}
        name = (
            "fresh_initial_submit_receipt.json"
            if passed
            else "fresh_initial_submit_failure_receipt.json"
        )
        write_runtime_json_once(
            self.boundary.fresh_job_root / "fresh_session" / name,
            receipt,
        )
        if not passed:
            raise FreshSessionRerunRequired(
                "fresh submit did not create a distinct conversation; seal this "
                "run and start another fresh_session_id"
            )
        return FreshInitialSubmitResult(submit_result=result, receipt=receipt)

    def establish_followup_scope(
        self,
        built: BuiltFreshV3JobPacket,
        *,
        initial_response_hash: str,
    ) -> ResearchApprovalScope:
        job = self.store.get_job(built.job.job_id)
        if (
            not job.conversation_id
            or job.conversation_id == self.boundary.old_conversation_id
        ):
            raise FreshSessionRerunRequired(
                "a distinct fresh conversation is required before follow-up scope"
            )
        return self.ledger.establish_initial_scope(
            job.job_id,
            primary_archetype_ids=job.archetype_ids,
            initial_response_hash=initial_response_hash,
            initial_pass_id=built.initial_pass_id,
        )

    def seal_failed_run_for_new_conversation(
        self,
        *,
        reason: str,
    ) -> ProResearchJob:
        """Make the current canary diagnostic-only before a fresh successor."""

        job = self.store.get_job(self.boundary.fresh_job_id)
        frozen = self.store.seal_fresh_efficiency_failure(
            job.job_id,
            expected_version=job.state_version,
            reason=reason,
            actor="v2.1-fresh-efficiency-gate",
            idempotency_key=f"fresh-efficiency-failed:{job.job_id}",
        )
        unsigned = {
            "schema_version": "e2r_pro_fresh_efficiency_failure_receipt_v1",
            "status": "FRESH_SESSION_DIAGNOSTIC_ONLY",
            "job_id": frozen.job_id,
            "run_id": self.build_packet_run_id(),
            "conversation_id": frozen.conversation_id,
            "reason": reason.strip(),
            "new_conversation_required": True,
            "automatic_resubmit_allowed": False,
            "score_authority": False,
            "stage_authority": False,
            "publication_withheld": True,
        }
        write_runtime_json_once(
            self.boundary.fresh_job_root
            / "fresh_session/fresh_efficiency_failure_receipt.json",
            {**unsigned, "receipt_hash": canonical_hash(unsigned)},
        )
        return frozen

    def build_packet_run_id(self) -> str:
        packet_path = self.boundary.fresh_job_root / "packet/research_packet.json"
        if not packet_path.is_file():
            raise FreshSessionBoundaryError("fresh packet is not available")
        payload = json.loads(packet_path.read_text(encoding="utf-8"))
        return str(payload.get("run_id") or "")

    def plan_compact_repair(
        self,
        built: BuiltFreshV3JobPacket,
        *,
        dossier: Mapping[str, Any],
        rejection_classifications: Sequence[Mapping[str, Any]],
        verification_rows: Sequence[Mapping[str, Any]],
        job_root: str | Path,
    ) -> tuple[FollowupPassPlan, CompiledCompactRepairPromptV3]:
        scope, parent = self._scope_and_completed_parent(built, "VERIFIER_REPAIR")
        transport_replacement_root_input_hash = canonical_hash(
            {
                "pass_name": "VERIFIER_REPAIR",
                "dossier_hash": canonical_hash(dossier),
                "rejection_classifications": list(rejection_classifications),
                "verification_rows": list(verification_rows),
            }
        )
        repairs = tuple(
            row
            for row in self.ledger.list_passes(built.job.job_id)
            if row.pass_name == "VERIFIER_REPAIR"
        )
        unpersisted_same_context = tuple(
            row
            for row in repairs
            if row.status == ResearchPassStatus.FAILED_HARD.value
            and str(row.detail.get("failure_domain") or "") == "TRANSPORT"
            and (
                row.pass_input_hash == transport_replacement_root_input_hash
                or str(
                    row.detail.get("transport_failure_root_input_hash") or ""
                )
                == transport_replacement_root_input_hash
            )
        )
        if len(unpersisted_same_context) >= 2:
            raise FreshSessionBoundaryError(
                "same compact repair context failed server persistence twice; "
                "automatic repetition is blocked"
            )
        transport_persistence_feedback: Mapping[str, Any] | None = None
        if unpersisted_same_context:
            failed_transport = unpersisted_same_context[-1]
            transport_persistence_feedback = {
                "supersedes_unpersisted_pass_id": failed_transport.pass_id,
                "failure_class": str(
                    failed_transport.detail.get("failure_class")
                    or "CHATGPT_SUBMITTED_TURN_NOT_SERVER_PERSISTED"
                ),
                "server_persistence_failure_evidence_hash": str(
                    failed_transport.detail.get(
                        "server_persistence_failure_evidence_hash"
                    )
                    or ""
                ),
                "replacement_ordinal": 1,
                "instruction": (
                    "This is a new exactly-once compact repair pass replacing "
                    "a prior turn that never persisted in the public "
                    "conversation. Preserve the same verifier-repair scope."
                ),
            }
        logical_input_hash = (
            canonical_hash(
                {
                    "pass_name": "VERIFIER_REPAIR",
                    "root_logical_input_hash": (
                        transport_replacement_root_input_hash
                    ),
                    "transport_persistence_feedback": (
                        transport_persistence_feedback
                    ),
                }
            )
            if transport_persistence_feedback is not None
            else transport_replacement_root_input_hash
        )
        pass_id = stable_id(
            "PROPASS",
            {
                "job_id": built.job.job_id,
                "parent_pass_id": parent.pass_id,
                "pass_name": "VERIFIER_REPAIR",
                "logical_input_hash": logical_input_hash,
            },
        )
        existing = next((row for row in repairs if row.pass_id == pass_id), None)
        if existing is None:
            repair_pass_ordinal = 1 + max(
                (
                    int(row.detail.get("repair_pass_ordinal") or 1)
                    for row in repairs
                ),
                default=0,
            )
        else:
            repair_pass_ordinal = int(
                existing.detail.get("repair_pass_ordinal") or 1
            )
        active = tuple(
            row
            for row in self.ledger.list_passes(built.job.job_id)
            if row.status
            not in {
                ResearchPassStatus.COMPLETE.value,
                ResearchPassStatus.FAILED_HARD.value,
            }
        )
        if active and all(row.pass_id != pass_id for row in active):
            raise FreshSessionBoundaryError(
                "another fresh follow-up is still incomplete"
            )
        compiled = self.repair_compiler.compile(
            dossier=dossier,
            rejection_classifications=rejection_classifications,
            verification_rows=verification_rows,
            job_root=job_root,
            research_pass_id=pass_id,
            parent_pass_id=parent.pass_id,
            repair_pass_ordinal=repair_pass_ordinal,
        )
        if existing is None:
            record = self.ledger.create_followup_pass(
                scope=scope,
                pass_id=pass_id,
                pass_name="VERIFIER_REPAIR",
                parent_pass_id=parent.pass_id,
                prompt_hash=compiled.prompt_hash,
                pass_input_hash=logical_input_hash,
                detail={
                    "fresh_v3_followup": True,
                    "repair_pass_ordinal": repair_pass_ordinal,
                    "candidate_ids": list(compiled.candidate_ids),
                    "prompt_char_count": compiled.prompt_char_count,
                    "full_dossier_reoutput_requested_count": 0,
                    "local_normalizable_sent_to_pro_count": 0,
                    "source_representation_sent_to_pro_count": 0,
                    "transport_replacement_root_input_hash": (
                        transport_replacement_root_input_hash
                        if unpersisted_same_context
                        else None
                    ),
                    "supersedes_unpersisted_pass_id": (
                        unpersisted_same_context[-1].pass_id
                        if unpersisted_same_context
                        else None
                    ),
                    "transport_persistence_feedback": (
                        transport_persistence_feedback
                    ),
                },
            )
        else:
            record = existing
            if (
                record.prompt_hash != compiled.prompt_hash
                or record.pass_input_hash != logical_input_hash
                or record.parent_pass_id != parent.pass_id
            ):
                raise FreshSessionBoundaryError(
                    "existing compact repair has different immutable lineage"
                )
        return (
            FollowupPassPlan(
                scope=scope,
                research_pass=record,
                prompt_text=(
                    "" if record.submit_count == 1 else compiled.prompt_text
                ),
                prompt_hash=record.prompt_hash,
            ),
            compiled,
        )

    def plan_v3_followup(
        self,
        built: BuiltFreshV3JobPacket,
        *,
        pass_name: str,
        latest_dossier_digest: Mapping[str, Any],
        unresolved_question_state: Sequence[Mapping[str, Any]] = (),
        pass_inputs: Mapping[str, Any] | None = None,
    ) -> tuple[FollowupPassPlan, CompiledFreshFollowupV3]:
        if pass_name not in _NON_REPAIR_V3_FOLLOWUPS:
            raise ValueError(f"unsupported fresh V3 follow-up: {pass_name}")
        scope, parent = self._scope_and_completed_parent(built, pass_name)
        existing_passes = self.ledger.list_passes(built.job.job_id)
        prior = tuple(
            row for row in existing_passes if row.pass_name == pass_name
        )
        context = {
            "latest_dossier_digest": dict(latest_dossier_digest),
            "unresolved_question_state": list(unresolved_question_state),
            "pass_inputs": dict(pass_inputs or {}),
        }
        _reject_full_dossier_followup_context(context)
        logical_input_hash = canonical_hash(
            {"pass_name": pass_name, "context": context}
        )
        provider_failure_root_input_hash = logical_input_hash
        failed_same_context = tuple(
            row
            for row in prior
            if row.status == ResearchPassStatus.FAILED_HARD.value
            and str(row.detail.get("failure_domain") or "PROVIDER")
            == "PROVIDER"
            and (
                row.pass_input_hash == provider_failure_root_input_hash
                or str(
                    row.detail.get("provider_failure_root_input_hash") or ""
                )
                == provider_failure_root_input_hash
            )
        )
        if len(failed_same_context) >= 2:
            raise FreshSessionBoundaryError(
                "same fresh V3 context failed twice at the provider; "
                "automatic repetition is blocked"
            )
        if failed_same_context:
            failed = failed_same_context[-1]
            context["pass_inputs"] = {
                **dict(context.get("pass_inputs") or {}),
                "provider_failure_feedback": {
                    "supersedes_failed_pass_id": failed.pass_id,
                    "failure_class": str(
                        failed.detail.get("failure_class")
                        or "CHATGPT_VISIBLE_RESPONSE_FAILURE"
                    ),
                    "failure_reason": str(
                        failed.detail.get("failure_reason")
                        or "visible assistant turn failed before dossier output"
                    ),
                    "failed_visible_response_hash": str(
                        failed.response_hash or ""
                    ),
                    "retry_ordinal": 1,
                    "instruction": (
                        "Do not repeat already completed routes. Use the "
                        "failure feedback, finish the requested structured "
                        "dossier, and preserve unresolved evidence as pending."
                    ),
                },
            }
            logical_input_hash = canonical_hash(
                {"pass_name": pass_name, "context": context}
            )
        transport_replacement_root_input_hash = logical_input_hash
        unpersisted_same_context = tuple(
            row
            for row in prior
            if row.status == ResearchPassStatus.FAILED_HARD.value
            and str(row.detail.get("failure_domain") or "") == "TRANSPORT"
            and (
                row.pass_input_hash == transport_replacement_root_input_hash
                or str(
                    row.detail.get("transport_failure_root_input_hash") or ""
                )
                == transport_replacement_root_input_hash
            )
        )
        if len(unpersisted_same_context) >= 2:
            raise FreshSessionBoundaryError(
                "same fresh V3 context failed server persistence twice; "
                "automatic repetition is blocked"
            )
        if unpersisted_same_context:
            failed_transport = unpersisted_same_context[-1]
            context["pass_inputs"] = {
                **dict(context.get("pass_inputs") or {}),
                "transport_persistence_feedback": {
                    "supersedes_unpersisted_pass_id": failed_transport.pass_id,
                    "failure_class": str(
                        failed_transport.detail.get("failure_class")
                        or "CHATGPT_SUBMITTED_TURN_NOT_SERVER_PERSISTED"
                    ),
                    "server_persistence_failure_evidence_hash": str(
                        failed_transport.detail.get(
                            "server_persistence_failure_evidence_hash"
                        )
                        or ""
                    ),
                    "replacement_ordinal": 1,
                    "instruction": (
                        "This is a new exactly-once pass replacing a prior "
                        "turn that never persisted in the public conversation. "
                        "Preserve the same research scope and structured output."
                    ),
                },
            }
            logical_input_hash = canonical_hash(
                {"pass_name": pass_name, "context": context}
            )
        pass_id = stable_id(
            "PROPASS",
            {
                "job_id": built.job.job_id,
                "parent_pass_id": parent.pass_id,
                "pass_name": pass_name,
                "logical_input_hash": logical_input_hash,
            },
        )
        active = tuple(
            row
            for row in existing_passes
            if row.status
            not in {
                ResearchPassStatus.COMPLETE.value,
                ResearchPassStatus.FAILED_HARD.value,
            }
        )
        if active and all(row.pass_id != pass_id for row in active):
            raise FreshSessionBoundaryError(
                "another fresh follow-up is still incomplete"
            )
        compiled = _compile_fresh_followup_v3(
            packet=built.packet_payload,
            scope=scope,
            pass_name=pass_name,
            research_pass_id=pass_id,
            parent_pass_id=parent.pass_id,
            context=context,
        )
        existing = next((row for row in prior if row.pass_id == pass_id), None)
        if existing is None:
            record = self.ledger.create_followup_pass(
                scope=scope,
                pass_id=pass_id,
                pass_name=pass_name,
                parent_pass_id=parent.pass_id,
                prompt_hash=compiled.prompt_hash,
                pass_input_hash=logical_input_hash,
                detail={
                    "fresh_v3_followup": True,
                    "context_hash": compiled.context_hash,
                    "research_gap_context_hash": str(
                        (context.get("pass_inputs") or {}).get(
                            "research_gap_context_hash"
                        )
                        or ""
                    ),
                    "saturation_blocker_identity_hash": str(
                        (context.get("pass_inputs") or {}).get(
                            "saturation_blocker_identity_hash"
                        )
                        or ""
                    ),
                    "question_family_ids": list(
                        (context.get("pass_inputs") or {}).get(
                            "question_family_ids"
                        )
                        or ()
                    ),
                    "question_context_hashes": dict(
                        (context.get("pass_inputs") or {}).get(
                            "question_context_hashes"
                        )
                        or {}
                    ),
                    "question_progress_hashes": dict(
                        (context.get("pass_inputs") or {}).get(
                            "question_progress_hashes"
                        )
                        or {}
                    ),
                    "question_stable_gap_hashes": dict(
                        (context.get("pass_inputs") or {}).get(
                            "question_stable_gap_hashes"
                        )
                        or {}
                    ),
                    "prompt_char_count": len(compiled.prompt_text),
                    "provider_failure_root_input_hash": (
                        provider_failure_root_input_hash
                        if failed_same_context
                        else None
                    ),
                    "supersedes_failed_pass_id": (
                        failed_same_context[-1].pass_id
                        if failed_same_context
                        else None
                    ),
                    "transport_replacement_root_input_hash": (
                        transport_replacement_root_input_hash
                        if unpersisted_same_context
                        else None
                    ),
                    "supersedes_unpersisted_pass_id": (
                        unpersisted_same_context[-1].pass_id
                        if unpersisted_same_context
                        else None
                    ),
                    "score_authority": False,
                    "stage_authority": False,
                },
            )
        else:
            record = existing
            if (
                record.prompt_hash != compiled.prompt_hash
                or record.pass_input_hash != logical_input_hash
                or record.parent_pass_id != parent.pass_id
            ):
                raise FreshSessionBoundaryError(
                    "existing fresh V3 follow-up has different immutable lineage"
                )
        return (
            FollowupPassPlan(
                scope=scope,
                research_pass=record,
                prompt_text=(
                    "" if record.submit_count == 1 else compiled.prompt_text
                ),
                prompt_hash=record.prompt_hash,
            ),
            compiled,
        )

    async def prepare_followup(
        self,
        plan: FollowupPassPlan,
        adapter: ChatGPTWebAdapter,
    ):
        return await self.followup_transport.prepare_followup(plan, adapter)

    async def submit_followup(
        self,
        plan: FollowupPassPlan,
        adapter: ChatGPTWebAdapter,
    ):
        return await self.followup_transport.submit_followup(plan, adapter)

    async def resume_intercepted_followup_submit(
        self,
        plan: FollowupPassPlan,
        adapter: ChatGPTWebAdapter,
    ):
        """Expose the shared proven-pre-dispatch recovery to fresh V3."""

        return await self.followup_transport.resume_intercepted_followup_submit(
            plan,
            adapter,
        )

    async def audit_submitted_followup_persistence(
        self,
        plan: FollowupPassPlan,
        adapter: ChatGPTWebAdapter,
    ):
        """Expose the shared fresh public-UI persistence audit."""

        return await self.followup_transport.audit_submitted_followup_persistence(
            plan,
            adapter,
        )

    def complete_followup(
        self,
        pass_id: str,
        *,
        response_hash: str,
        conversation_id: str,
    ):
        return self.followup_transport.complete_followup(
            pass_id,
            response_hash=response_hash,
            conversation_id=conversation_id,
        )

    def confirm_transport_pending_result_visible(self, pass_id: str):
        """Expose the shared exactly-once recovery path to fresh V3 runners."""

        return self.followup_transport.confirm_transport_pending_result_visible(
            pass_id
        )

    def _scope_and_completed_parent(
        self,
        built: BuiltFreshV3JobPacket,
        pass_name: str,
    ):
        job = self.store.get_job(built.job.job_id)
        if (
            not job.conversation_id
            or job.conversation_id == self.boundary.old_conversation_id
        ):
            raise FreshSessionRerunRequired(
                "bounded follow-up requires the distinct fresh conversation"
            )
        scope = self.ledger.require_authorized_scope(
            job.job_id,
            target_id=job.symbol,
            as_of_date=job.as_of_date,
            primary_archetype_ids=job.archetype_ids,
            pass_name=pass_name,
            conversation_id=job.conversation_id,
        )
        passes = self.ledger.list_passes(job.job_id)
        completed = tuple(
            row
            for row in passes
            if row.status == ResearchPassStatus.COMPLETE.value
            and row.pass_name != ARTIFACT_REEXPORT_PASS_NAME
        )
        if not completed:
            raise FreshSessionBoundaryError("fresh follow-up has no completed parent")
        return scope, completed[-1]

    def _ensure_browser_preparing(self, job_id: str) -> ProResearchJob:
        job = self.store.get_job(job_id)
        if job.status in {
            JobStatus.PACKET_READY.value,
            JobStatus.USER_ATTENTION_REQUIRED.value,
        }:
            job = self.store.transition(
                job.job_id,
                expected_version=job.state_version,
                to_status=JobStatus.BROWSER_PREPARING,
                actor="v2.1-fresh-v3-browser-worker",
                idempotency_key=(
                    f"fresh-v3-browser-preparing:{job.job_id}:{job.state_version}"
                ),
            )
        return job

    def _record_browser_attention(self, job_id: str, error: Exception) -> None:
        current = self.store.get_job(job_id)
        if current.status != JobStatus.BROWSER_PREPARING.value:
            return
        self.store.transition(
            job_id,
            expected_version=current.state_version,
            to_status=JobStatus.USER_ATTENTION_REQUIRED,
            actor="v2.1-fresh-v3-browser-worker",
            idempotency_key=(
                f"fresh-v3-browser-attention:{job_id}:{current.state_version}"
            ),
            payload={
                "automatic_login_allowed": False,
                "automatic_resubmit_allowed": False,
                "new_chat_route_required": True,
                "submit_count": current.submit_count,
            },
            updates={
                "last_error_class": type(error).__name__,
                "last_error_message": str(error),
            },
        )


def _compile_fresh_followup_v3(
    *,
    packet: Mapping[str, Any],
    scope: ResearchApprovalScope,
    pass_name: str,
    research_pass_id: str,
    parent_pass_id: str,
    context: Mapping[str, Any],
) -> CompiledFreshFollowupV3:
    context_hash = canonical_hash(context)
    if pass_name == ARTIFACT_REEXPORT_PASS_NAME:
        expected_artifact = str(
            (context.get("pass_inputs") or {}).get(
                "expected_artifact_filename"
            )
            or "ResearchDossierV3.json"
        )
        initial_pass_id = str(
            (context.get("pass_inputs") or {}).get(
                "initial_research_pass_id"
            )
            or scope.initial_pass_id
        )
        objective = (
            "직전 연구의 링크가 가리키는 sandbox 파일이 실제로 존재하지 않았다. "
            "웹 검색, 새 자료 수집, 새 사실 판단은 전부 금지한다. 직전 연구에서 이미 "
            "완료한 ResearchDossierV3만 실제 파일로 다시 내보내라."
        )
        output_instruction = (
            f"직전 전체 dossier를 `{expected_artifact}`에 UTF-8 JSON으로 실제 저장하고, "
            "그 파일을 즉시 다시 열어 JSON parse와 packet의 dossier_output_schema 검증을 "
            "통과시켜라. 파일이 존재하고 byte_count>0임을 확인하기 전에는 sandbox 링크를 "
            "출력하지 마라. dossier 내부 research_pass_id는 원래 initial pass "
            f"`{initial_pass_id}`를 유지하고 parent_pass_id는 원래 값 `NONE`을 유지하라. "
            "이번 ARTIFACT_REEXPORT pass id로 dossier 내부 연구 계보를 바꾸지 마라. "
            "최종 응답 맨 앞에는 위 job/run/pass/parent marker를 각각 정확히 한 번 출력하라. "
            "실제 파일 링크와 schema validation 결과, sha256, byte_count를 함께 출력하라. "
            "파일 저장이 불가능할 때만 전체 JSON을 "
            "E2R_RESEARCH_DOSSIER_JSON_BEGIN/END 사이에 직접 출력하라."
        )
    elif pass_name == "SATURATION_AUDIT":
        objective = (
            "최신 question closure와 source-lineage digest를 감사하라. 공개적으로 더 "
            "조사 가능한 material gap이 남았으면 COMPLETE로 만들지 말고 정확한 "
            "nonterminal 상태를 유지하라. 새 score나 Stage를 제안하지 마라."
        )
    elif pass_name == "PUBLIC_GAP_CLOSURE":
        objective = (
            "아래에 열거된 material public gap만 official-first로 조사하고, 실제로 "
            "연 source와 exact excerpt를 새 atomic fact/route receipt로 연결하라. "
            "unresolved_question_state의 missing_core_source_roles는 deterministic "
            "검문 결과다. 그 role은 verifier-eligible CURRENT/OPEN/RESOLVED fact로만 "
            "닫힌다. HISTORICAL_ONLY 또는 SUPERSEDED fact는 과거 맥락일 뿐 현재 "
            "source role을 충족하지 않는다. 과거 경고·위험만 찾았으면 as_of_date까지의 "
            "후속 유지·해제·대체 상태를 더 조사하고, 현재 근거를 못 찾으면 attempted "
            "route와 gap을 남겨라. 오래된 fact 하나로 required role satisfied, gap "
            "RESOLVED, blocks_full_thesis=false를 선언하지 마라."
        )
        output_instruction = ""
    else:
        objective = (
            "아래에 열거된 counterfact의 current/resolved/superseded 상태만 공개 "
            "근거로 닫고 기존 accepted fact를 삭제하지 마라."
        )
        output_instruction = ""
    if pass_name != ARTIFACT_REEXPORT_PASS_NAME:
        output_instruction = (
            "최종 응답 맨 앞에 위 job/run/pass/parent marker를 각각 정확히 한 번 "
            "출력하고, `E2R_RESEARCH_DOSSIER_JSON_BEGIN/END` 사이에 "
            "ResearchDossierV3 **delta JSON** 하나를 출력하라. 이전 전체 dossier를 "
            "반복하지 말고 이번 pass의 새 source/fact/route와 실제로 갱신한 question/gap만 "
            "배열에 넣어라. schema의 나머지 필수 배열·객체는 빈 값으로 유지해도 되며, "
            "deterministic merger가 이전 append-only ledger와 합친다. "
            "issuer_scoped=false인 새 fact의 subject는 source 원문에 실제로 연속 등장하는 "
            "가장 짧은 주체 표현을 그대로 복사하고, 여러 위치의 회사·시설·거래 이름을 "
            "합성하지 마라. 새 fact의 canonical source는 후속 verifier가 로그인·개인 "
            "cookie·JavaScript challenge 없이 다시 받을 수 있는 공개 representation이어야 "
            "한다. 401/403·로그인·anti-bot으로 재수집할 수 없으면 official 원문·filing·issuer "
            "data·공개 mirror를 사용하고, 대체 표현도 없으면 fact 대신 attempted route와 "
            "source gap을 남겨라."
        )
    prompt = "\n".join(
        (
            f"[[E2R_PRO_RUN_ID:{packet.get('run_id')}]]",
            f"[[E2R_PRO_JOB_ID:{packet.get('job_id')}]]",
            f"[[E2R_PRO_PASS_ID:{research_pass_id}]]",
            f"[[E2R_PRO_PARENT_PASS_ID:{parent_pass_id}]]",
            "",
            f"# E2R Pro Fresh V3 {pass_name}",
            "",
            f"- conversation_id: `{scope.conversation_id}`",
            f"- target_id: `{scope.target_id}`",
            f"- as_of_date: `{scope.as_of_date}`",
            "- same_conversation_scope_required: `true`",
            "- score_authority: `false`",
            "- stage_authority: `false`",
            "",
            objective,
            "",
            "초기 V3의 one fact/one predicate/one source/one exact excerpt 계약과 "
            "verifier_preflight를 그대로 지켜라. 기존 accepted fact는 append-only다.",
            output_instruction,
            "",
            "## Compact deterministic context",
            "",
            "```json",
            canonical_json(context),
            "```",
            "",
        )
    )
    if len(prompt) > _MAX_FOLLOWUP_PROMPT_CHARS:
        raise FreshSessionBoundaryError(
            "fresh V3 follow-up exceeds 100,000 chars; compact the digest first"
        )
    prompt_hash = canonical_hash({"prompt": prompt})
    return CompiledFreshFollowupV3(
        pass_name=pass_name,
        prompt_text=prompt,
        prompt_hash=prompt_hash,
        pass_input_hash=canonical_hash({"pass_name": pass_name, "context": context}),
        research_pass_id=research_pass_id,
        parent_pass_id=parent_pass_id,
        context_hash=context_hash,
    )


def _reject_full_dossier_followup_context(value: Any, path: tuple[str, ...] = ()) -> None:
    forbidden = {
        "source_documents",
        "material_facts",
        "counterfacts",
        "resolution_facts",
        "derived_metrics",
    }
    if isinstance(value, Mapping):
        for key, child in value.items():
            normalized = str(key).strip().casefold().replace("-", "_")
            if normalized in forbidden:
                raise FreshSessionBoundaryError(
                    "fresh follow-up context must be a compact digest, not a full "
                    f"dossier: {'/'.join((*path, str(key)))}"
                )
            _reject_full_dossier_followup_context(child, (*path, str(key)))
    elif isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        for index, child in enumerate(value):
            _reject_full_dossier_followup_context(child, (*path, str(index)))


__all__ = [
    "BuiltFreshV3JobPacket",
    "CompiledFreshFollowupV3",
    "FreshInitialSubmitResult",
    "FreshSessionOrchestratorV3",
    "PreparedFreshV3BrowserRuntime",
    "PreparedFreshV3Initial",
]
