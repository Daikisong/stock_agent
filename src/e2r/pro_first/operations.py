"""Production packet preparation and logged-in browser shadow operations."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import subprocess
from typing import Any, Mapping

from .browser.worker import BrowserWorkerSession, ProBrowserWorker
from .config import ProFirstLocalConfig
from .ids import canonical_hash, stable_id
from .job_store import ProFirstJobStore
from .models import JobStatus, ProResearchJob, ResearchMode, ScanWindow
from .packet import (
    PACKET_V2_SCHEMA_VERSION,
    PacketBuildInput,
    PacketBundleReceipt,
    ResearchPacketBuilder,
    ResearchPacketV2Builder,
    write_packet_bundle,
)
from .prompt_contract import ProResearchPromptContract, RenderedProPrompt
from .research_contracts import (
    CompiledProResearchPromptV2,
    ProResearchPromptCompilerV2,
)
from .multi_pass.models import INITIAL_PASS_NAME


DEFAULT_RESEARCH_OBJECTIVES = (
    "사업모델과 경제 메커니즘을 원문 근거로 확인한다.",
    "7개 component의 positive evidence와 counter evidence를 함께 확인한다.",
    "실적, FCF, CAPEX, revision, valuation과 주문·가격·공급 조건을 구분한다.",
)
DEFAULT_SOURCE_PREFERENCES = (
    "OPENDART",
    "KIND_KRX",
    "ISSUER_EARNINGS_RELEASE",
    "ISSUER_PRESENTATION",
    "CUSTOMER_OFFICIAL",
    "CONSENSUS_REVISION",
)
DEFAULT_FORBIDDEN_INFERENCES = (
    "확인하지 못한 사실을 ABSENT로 단정하지 않는다.",
    "동일 사실을 여러 기사로 중복 계산하지 않는다.",
    "as_of_date 이후 자료를 사용하지 않는다.",
    "최종 score와 Stage를 결정하지 않는다.",
)


@dataclass
class PreparedBrowserRuntime:
    job: ProResearchJob
    session: BrowserWorkerSession
    packet_bundle: PacketBundleReceipt
    prompt: RenderedProPrompt
    receipt: Mapping[str, Any]

    async def close(self) -> None:
        await self.session.close()


@dataclass(frozen=True)
class BuiltV2JobPacket:
    job: ProResearchJob
    packet_bundle: PacketBundleReceipt
    packet_payload: Mapping[str, Any]
    prompt: CompiledProResearchPromptV2
    initial_pass_id: str
    output_filename: str


@dataclass
class PreparedV2BrowserRuntime:
    job: ProResearchJob
    session: BrowserWorkerSession
    packet_bundle: PacketBundleReceipt
    packet_payload: Mapping[str, Any]
    prompt: CompiledProResearchPromptV2
    initial_pass_id: str
    output_filename: str
    receipt: Mapping[str, Any]

    async def close(self) -> None:
        await self.session.close()


def create_forced_validation_canary(
    store: ProFirstJobStore,
    *,
    symbol: str,
    company_name: str,
    as_of_date: str,
    archetype_ids: tuple[str, ...] = (),
) -> ProResearchJob:
    """Create an explicitly labelled canary; never masquerade it as natural selection."""

    trigger = canonical_hash(
        {
            "selection_mode": ResearchMode.FORCED_VALIDATION_CANARY.value,
            "symbol": symbol,
            "as_of_date": as_of_date,
        }
    )
    candidate = store.create_candidate(
        symbol=symbol,
        company_name=company_name,
        as_of_date=as_of_date,
        scan_window=ScanWindow.MORNING,
        trigger_fingerprint=trigger,
        research_mode=ResearchMode.FORCED_VALIDATION_CANARY,
        selection_receipt={
            "schema_version": "e2r_pro_live_canary_selection_v1",
            "selection_mode": "FORCED_VALIDATION_CANARY",
            "production_candidate": False,
            "test_injected": False,
            "final_score_visible_at_selection": False,
            "final_stage_visible_at_selection": False,
            "trigger_ids": [stable_id("CANARYTRIGGER", {"symbol": symbol, "as_of_date": as_of_date})],
            "reason_codes": ["EXPLICIT_USER_AUTHORIZED_LIVE_VALIDATION"],
        },
    )
    return store.create_job(
        candidate.candidate_id,
        archetype_ids=archetype_ids,
        actor="live-canary-preparer",
    )


def build_job_packet(
    store: ProFirstJobStore,
    *,
    job_id: str,
    runtime_root: str | Path,
    config_hash: str,
    repo_root: str | Path,
) -> tuple[ProResearchJob, PacketBundleReceipt, RenderedProPrompt]:
    job = store.get_job(job_id)
    if job.mode == ResearchMode.DELTA_RESEARCH.value:
        raise ValueError("DELTA_RESEARCH requires an explicit prior-dossier context")
    if job.status == JobStatus.CANDIDATE_SELECTED.value:
        job = store.transition(
            job_id,
            expected_version=job.state_version,
            to_status=JobStatus.PACKET_BUILDING,
            actor="pro-first-packet-builder",
            idempotency_key=f"packet-building:{job_id}",
        )
    if job.status not in {
        JobStatus.PACKET_BUILDING.value,
        JobStatus.PACKET_READY.value,
        JobStatus.BROWSER_PREPARING.value,
        JobStatus.AWAITING_USER_APPROVAL.value,
        JobStatus.USER_ATTENTION_REQUIRED.value,
    }:
        raise ValueError(f"job cannot build/reuse a packet from {job.status}")
    candidate = store.get_candidate(job.candidate_id)
    job_root = Path(runtime_root).expanduser().resolve() / "jobs" / job_id
    packet_path = job_root / "packet/research_packet.json"
    manifest_path = job_root / "packet/packet_manifest.json"
    if job.packet_hash and packet_path.is_file() and manifest_path.is_file():
        payload = json.loads(packet_path.read_text(encoding="utf-8"))
        if canonical_hash(payload) != job.packet_hash:
            raise ValueError("durable packet differs from filesystem packet")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        bundle = PacketBundleReceipt(
            packet_directory=packet_path.parent,
            research_packet_json=packet_path,
            research_packet_markdown=packet_path.with_name("research_packet.md"),
            packet_manifest=manifest_path,
            packet_hash=job.packet_hash,
            manifest_hash=canonical_hash(manifest),
        )
    else:
        selection = dict(candidate.selection_receipt)
        trigger_ids = tuple(str(value) for value in selection.get("trigger_ids") or ())
        reason_codes = tuple(str(value) for value in selection.get("reason_codes") or ())
        trigger_summary = tuple(
            {
                "trigger_id": trigger_id,
                "reason": ", ".join(reason_codes) or "production DEEP_RESEARCH candidate",
            }
            for trigger_id in trigger_ids
        )
        packet = ResearchPacketBuilder().build(
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
                research_objectives=DEFAULT_RESEARCH_OBJECTIVES,
                source_preferences=DEFAULT_SOURCE_PREFERENCES,
                forbidden_inferences=DEFAULT_FORBIDDEN_INFERENCES,
            )
        )
        bundle = write_packet_bundle(
            packet,
            job_root / "packet",
            commit_sha=_git_head(repo_root),
            config_hash=config_hash,
        )
        manifest = json.loads(bundle.packet_manifest.read_text(encoding="utf-8"))
        job = store.record_packet(
            job_id,
            expected_version=job.state_version,
            packet_id=stable_id("PROPACKET", {"job_id": job_id, "packet_hash": packet.packet_hash}),
            packet_hash=packet.packet_hash,
            manifest=manifest,
            actor="pro-first-packet-builder",
            idempotency_key=f"packet-ready:{job_id}:{packet.packet_hash}",
        )
    packet_payload = json.loads(bundle.research_packet_json.read_text(encoding="utf-8"))
    prompt = ProResearchPromptContract().render(
        job_id=job_id,
        run_id=str(packet_payload["run_id"]),
        symbol=job.symbol,
        as_of_date=job.as_of_date,
    )
    return store.get_job(job_id), bundle, prompt


def build_job_packet_v2(
    store: ProFirstJobStore,
    *,
    job_id: str,
    runtime_root: str | Path,
    config_hash: str,
    repo_root: str | Path,
) -> BuiltV2JobPacket:
    """Build one contract-attached V2 packet and its non-circular initial pass."""

    job = store.get_job(job_id)
    if job.mode == ResearchMode.DELTA_RESEARCH.value:
        raise ValueError("DELTA_RESEARCH requires the dedicated V2 delta path")
    if not job.archetype_ids:
        raise ValueError("a Pro V2 job requires one to three candidate contracts")
    if job.status == JobStatus.CANDIDATE_SELECTED.value:
        job = store.transition(
            job_id,
            expected_version=job.state_version,
            to_status=JobStatus.PACKET_BUILDING,
            actor="pro-first-v2-packet-builder",
            idempotency_key=f"v2-packet-building:{job_id}",
        )
    if job.status not in {
        JobStatus.PACKET_BUILDING.value,
        JobStatus.PACKET_READY.value,
        JobStatus.BROWSER_PREPARING.value,
        JobStatus.AWAITING_USER_APPROVAL.value,
        JobStatus.USER_ATTENTION_REQUIRED.value,
    }:
        raise ValueError(f"job cannot build/reuse a V2 packet from {job.status}")
    candidate = store.get_candidate(job.candidate_id)
    job_root = Path(runtime_root).expanduser().resolve() / "jobs" / job_id
    packet_path = job_root / "packet/research_packet.json"
    manifest_path = job_root / "packet/packet_manifest.json"
    if job.packet_hash and packet_path.is_file() and manifest_path.is_file():
        packet_payload = json.loads(packet_path.read_text(encoding="utf-8"))
        if canonical_hash(packet_payload) != job.packet_hash:
            raise ValueError("durable packet differs from filesystem packet")
        if packet_payload.get("schema_version") != PACKET_V2_SCHEMA_VERSION:
            raise ValueError("durable job packet is not ResearchPacketV2")
        _verify_v2_contract_snapshot(packet_payload)
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        bundle = PacketBundleReceipt(
            packet_directory=packet_path.parent,
            research_packet_json=packet_path,
            research_packet_markdown=packet_path.with_name("research_packet.md"),
            packet_manifest=manifest_path,
            packet_hash=job.packet_hash,
            manifest_hash=canonical_hash(manifest),
        )
    else:
        selection = dict(candidate.selection_receipt)
        trigger_ids = tuple(str(value) for value in selection.get("trigger_ids") or ())
        reason_codes = tuple(str(value) for value in selection.get("reason_codes") or ())
        trigger_summary = tuple(
            {
                "trigger_id": trigger_id,
                "reason": ", ".join(reason_codes) or "production DEEP_RESEARCH candidate",
            }
            for trigger_id in trigger_ids
        )
        packet = ResearchPacketV2Builder().build(
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
                research_objectives=DEFAULT_RESEARCH_OBJECTIVES,
                source_preferences=DEFAULT_SOURCE_PREFERENCES,
                forbidden_inferences=DEFAULT_FORBIDDEN_INFERENCES,
            )
        )
        bundle = write_packet_bundle(
            packet,
            job_root / "packet",
            commit_sha=_git_head(repo_root),
            config_hash=config_hash,
        )
        manifest = json.loads(bundle.packet_manifest.read_text(encoding="utf-8"))
        job = store.record_packet(
            job_id,
            expected_version=job.state_version,
            packet_id=stable_id(
                "PROPACKET", {"job_id": job_id, "packet_hash": packet.packet_hash}
            ),
            packet_hash=packet.packet_hash,
            manifest=manifest,
            actor="pro-first-v2-packet-builder",
            idempotency_key=f"v2-packet-ready:{job_id}:{packet.packet_hash}",
        )
        packet_payload = dict(packet.payload)
    initial_pass_id = stable_id(
        "PROPASS",
        {
            "job_id": job_id,
            "run_id": packet_payload["run_id"],
            "pass_name": INITIAL_PASS_NAME,
            "packet_hash": bundle.packet_hash,
            "primary_archetype_ids": list(job.archetype_ids),
        },
    )
    prompt = ProResearchPromptCompilerV2().compile(
        packet=packet_payload,
        primary_archetype_ids=job.archetype_ids,
        pass_name=INITIAL_PASS_NAME,
        conversation_id="PENDING_INITIAL_CONVERSATION",
        research_pass_id=initial_pass_id,
        parent_pass_id=None,
    )
    output_filename = f"E2R_PRO_{job_id}_{job.symbol}_{job.as_of_date}.md"
    return BuiltV2JobPacket(
        job=store.get_job(job_id),
        packet_bundle=bundle,
        packet_payload=packet_payload,
        prompt=prompt,
        initial_pass_id=initial_pass_id,
        output_filename=output_filename,
    )


async def prepare_v2_job_in_logged_in_browser(
    store: ProFirstJobStore,
    *,
    job_id: str,
    config: ProFirstLocalConfig,
    repo_root: str | Path,
    screenshot_path: str | Path | None = None,
) -> PreparedV2BrowserRuntime:
    built = build_job_packet_v2(
        store,
        job_id=job_id,
        runtime_root=config.runtime_root,
        config_hash=config.config_hash,
        repo_root=repo_root,
    )
    job = built.job
    if job.status in {
        JobStatus.PACKET_READY.value,
        JobStatus.USER_ATTENTION_REQUIRED.value,
    }:
        job = store.transition(
            job_id,
            expected_version=job.state_version,
            to_status=JobStatus.BROWSER_PREPARING,
            actor="pro-first-v2-browser-worker",
            idempotency_key=f"v2-browser-preparing:{job_id}:{job.state_version}",
        )
    if job.status != JobStatus.BROWSER_PREPARING.value:
        raise ValueError(f"V2 browser preparation requires BROWSER_PREPARING, got {job.status}")
    try:
        session = await ProBrowserWorker(config.browser).open(job_id=job_id)
    except Exception as error:
        _record_v2_browser_attention(store, job_id, error)
        raise
    try:
        # Initial jobs start a new visible ChatGPT conversation. Follow-ups use
        # the durable /c/<id> page and never call this initial preparation path.
        if session.page.url.rstrip("/") != config.browser.chatgpt_url.rstrip("/"):
            await session.page.goto(
                config.browser.chatgpt_url,
                wait_until="domcontentloaded",
            )
        prepared = await session.adapter.prepare_without_submit(
            browser_session_id=session.browser_session_id,
            packet_path=built.packet_bundle.research_packet_json,
            packet_hash=built.packet_bundle.packet_hash,
            prompt=built.prompt.prompt_text,
            prompt_hash=built.prompt.prompt_hash,
        )
        job = store.record_browser_prepared(
            job_id,
            expected_version=job.state_version,
            browser_session_id=prepared.browser_session_id,
            conversation_id=prepared.conversation_id,
            adapter_name="PlaywrightChatGPTWebAdapterV2",
            packet_hash=prepared.packet_hash,
            prompt_hash=prepared.prompt_hash,
            state={
                "state": prepared.state.value,
                "uploaded_filename": prepared.uploaded_filename,
                "send_ready": prepared.send_ready,
                "deep_research_ready": prepared.deep_research_ready,
                "submit_count": 0,
                "initial_pass_id": built.initial_pass_id,
                "packet_schema_version": PACKET_V2_SCHEMA_VERSION,
            },
            actor="pro-first-v2-browser-worker",
            idempotency_key=f"v2-browser-prepared:{job_id}:{prepared.prompt_hash}",
        )
        if screenshot_path:
            destination = Path(screenshot_path).expanduser().resolve()
            destination.parent.mkdir(parents=True, exist_ok=True)
            await session.page.screenshot(path=str(destination), full_page=False)
        receipt = {
            "schema_version": "e2r_pro_first_v2_live_prepare_receipt_v1",
            "status": "CHATGPT_PRO_V2_PREPARED_AWAITING_APPROVAL",
            "job_id": job_id,
            "selection_mode": job.mode,
            "browser_session_id": prepared.browser_session_id,
            "conversation_id": prepared.conversation_id,
            "packet_hash": prepared.packet_hash,
            "prompt_hash": prepared.prompt_hash,
            "initial_pass_id": built.initial_pass_id,
            "contract_ids": list(
                built.packet_payload["research_contract_snapshot"]["contract_ids"]
            ),
            "mandatory_question_count": len(built.prompt.mandatory_question_ids),
            "deep_research_ready": prepared.deep_research_ready,
            "send_ready": prepared.send_ready,
            "submit_count": 0,
            "screenshot_runtime_only": bool(screenshot_path),
        }
        return PreparedV2BrowserRuntime(
            job=job,
            session=session,
            packet_bundle=built.packet_bundle,
            packet_payload=built.packet_payload,
            prompt=built.prompt,
            initial_pass_id=built.initial_pass_id,
            output_filename=built.output_filename,
            receipt=receipt,
        )
    except Exception as error:
        await session.close()
        _record_v2_browser_attention(store, job_id, error)
        raise


async def recover_submitted_v2_job_in_logged_in_browser(
    store: ProFirstJobStore,
    *,
    job_id: str,
    config: ProFirstLocalConfig,
    repo_root: str | Path,
    search_terms: tuple[str, ...] = (),
    screenshot_path: str | Path | None = None,
) -> PreparedV2BrowserRuntime:
    """Recover one already-submitted V2 job without any browser submit action."""

    del repo_root  # Existing packet lineage is verified from the durable bundle.
    job = store.get_job(job_id)
    captured_downstream_resume = (
        job.capture_count == 1
        and job.status
        in {
            JobStatus.USER_ATTENTION_REQUIRED.value,
            JobStatus.CAPTURE_COMPLETE.value,
            JobStatus.IMPORTING.value,
            JobStatus.DOSSIER_IMPORTED.value,
            JobStatus.VERIFYING_SOURCES.value,
            JobStatus.GAP_ADJUDICATION.value,
        }
    )
    if job.status not in {
        JobStatus.RESEARCH_RUNNING.value,
        JobStatus.RESULT_DETECTED.value,
    } and not captured_downstream_resume:
        raise ValueError(
            "submitted V2 recovery requires RESEARCH_RUNNING, RESULT_DETECTED, "
            "or one captured downstream resume state, "
            f"got {job.status}"
        )
    if job.submit_count != 1:
        raise ValueError("submitted V2 recovery requires exactly one prior submit")
    if not job.packet_hash or not job.approval_prompt_hash:
        raise ValueError("submitted V2 recovery requires durable packet and prompt hashes")
    job_root = config.runtime_root / "jobs" / job_id
    packet_path = job_root / "packet/research_packet.json"
    manifest_path = job_root / "packet/packet_manifest.json"
    if not packet_path.is_file() or not manifest_path.is_file():
        raise FileNotFoundError("submitted V2 packet bundle is incomplete")
    packet_payload = json.loads(packet_path.read_text(encoding="utf-8"))
    if packet_payload.get("schema_version") != PACKET_V2_SCHEMA_VERSION:
        raise ValueError("submitted job packet is not ResearchPacketV2")
    if canonical_hash(packet_payload) != job.packet_hash:
        raise ValueError("submitted V2 packet differs from the durable packet hash")
    _verify_v2_contract_snapshot(packet_payload)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bundle = PacketBundleReceipt(
        packet_directory=packet_path.parent,
        research_packet_json=packet_path,
        research_packet_markdown=packet_path.with_name("research_packet.md"),
        packet_manifest=manifest_path,
        packet_hash=job.packet_hash,
        manifest_hash=canonical_hash(manifest),
    )
    initial_pass_id = stable_id(
        "PROPASS",
        {
            "job_id": job_id,
            "run_id": packet_payload["run_id"],
            "pass_name": INITIAL_PASS_NAME,
            "packet_hash": bundle.packet_hash,
            "primary_archetype_ids": list(job.archetype_ids),
        },
    )
    prompt = ProResearchPromptCompilerV2().compile(
        packet=packet_payload,
        primary_archetype_ids=job.archetype_ids,
        pass_name=INITIAL_PASS_NAME,
        conversation_id="PENDING_INITIAL_CONVERSATION",
        research_pass_id=initial_pass_id,
        parent_pass_id=None,
    )
    if prompt.prompt_hash != job.approval_prompt_hash:
        raise ValueError("recompiled initial prompt differs from the approved prompt hash")
    output_filename = f"E2R_PRO_{job_id}_{job.symbol}_{job.as_of_date}.md"
    session = await ProBrowserWorker(config.browser).open(job_id=job_id)
    try:
        recovered = await session.adapter.recover_conversation_without_submit(
            job_id=job_id,
            run_id=str(packet_payload["run_id"]),
            search_terms=tuple(
                dict.fromkeys(
                    value.strip()
                    for value in (*search_terms, job.company_name, job.symbol)
                    if value and value.strip()
                )
            ),
        )
        if captured_downstream_resume:
            if recovered.conversation_id != job.conversation_id:
                raise ValueError(
                    "captured import retry recovered a different conversation"
                )
            rebound = job
        else:
            rebound = store.rebind_recovered_conversation(
                job_id,
                expected_version=job.state_version,
                conversation_id=recovered.conversation_id,
                run_id=str(packet_payload["run_id"]),
                report_hash=recovered.result.report_hash,
                job_marker_matches=recovered.result.job_marker_matches,
                run_marker_matches=recovered.result.run_marker_matches,
                actor="pro-first-v2-browser-history-recovery",
                idempotency_key=(
                    f"v2-conversation-recovered:{job_id}:"
                    f"{recovered.conversation_id}:{recovered.result.report_hash}"
                ),
            )
        if screenshot_path:
            destination = Path(screenshot_path).expanduser().resolve()
            destination.parent.mkdir(parents=True, exist_ok=True)
            await session.page.screenshot(path=str(destination), full_page=False)
        receipt = {
            "schema_version": "e2r_pro_first_v2_recovery_receipt_v1",
            "status": (
                "CAPTURED_CHAT_REATTACHED_FOR_IMPORT_WITHOUT_RESUBMIT"
                if captured_downstream_resume
                else "SUBMITTED_CHAT_RECOVERED_WITHOUT_RESUBMIT"
            ),
            "job_id": job_id,
            "run_id": packet_payload["run_id"],
            "conversation_id": recovered.conversation_id,
            "search_query": recovered.search_query,
            "result_href": recovered.result_href,
            "report_hash": recovered.result.report_hash,
            "job_marker_matches": recovered.result.job_marker_matches,
            "run_marker_matches": recovered.result.run_marker_matches,
            "structurally_complete": recovered.result.structurally_complete,
            "submit_count": rebound.submit_count,
            "capture_count": rebound.capture_count,
            "capture_reused": captured_downstream_resume,
            "recovery_submit_count": recovered.submit_count,
            "screenshot_runtime_only": bool(screenshot_path),
        }
        return PreparedV2BrowserRuntime(
            job=rebound,
            session=session,
            packet_bundle=bundle,
            packet_payload=packet_payload,
            prompt=prompt,
            initial_pass_id=initial_pass_id,
            output_filename=output_filename,
            receipt=receipt,
        )
    except Exception:
        await session.close()
        raise


def _verify_v2_contract_snapshot(packet_payload: Mapping[str, Any]) -> None:
    snapshot = packet_payload.get("research_contract_snapshot")
    if not isinstance(snapshot, Mapping):
        raise ValueError("ResearchPacketV2 lacks a contract snapshot")
    declared_hash = str(snapshot.get("snapshot_hash") or "")
    unsigned = {key: value for key, value in snapshot.items() if key != "snapshot_hash"}
    if declared_hash != canonical_hash(unsigned):
        raise ValueError("ResearchPacketV2 contract snapshot hash mismatch")
    contract_ids = [
        str(row.get("archetype_id") or "")
        for row in snapshot.get("contracts") or ()
        if isinstance(row, Mapping)
    ]
    if contract_ids != list(snapshot.get("contract_ids") or ()):
        raise ValueError("ResearchPacketV2 contract roster differs from attached contracts")


def _record_v2_browser_attention(
    store: ProFirstJobStore,
    job_id: str,
    error: Exception,
) -> None:
    current = store.get_job(job_id)
    if current.status == JobStatus.BROWSER_PREPARING.value:
        store.transition(
            job_id,
            expected_version=current.state_version,
            to_status=JobStatus.USER_ATTENTION_REQUIRED,
            actor="pro-first-v2-browser-worker",
            idempotency_key=f"v2-browser-attention:{job_id}:{current.state_version}",
            payload={
                "automatic_login_allowed": False,
                "automatic_resubmit_allowed": False,
                "submit_count": current.submit_count,
            },
            updates={
                "last_error_class": type(error).__name__,
                "last_error_message": str(error),
            },
        )


async def prepare_job_in_logged_in_browser(
    store: ProFirstJobStore,
    *,
    job_id: str,
    config: ProFirstLocalConfig,
    repo_root: str | Path,
    screenshot_path: str | Path | None = None,
) -> PreparedBrowserRuntime:
    job, bundle, prompt = build_job_packet(
        store,
        job_id=job_id,
        runtime_root=config.runtime_root,
        config_hash=config.config_hash,
        repo_root=repo_root,
    )
    if job.status in {
        JobStatus.PACKET_READY.value,
        JobStatus.USER_ATTENTION_REQUIRED.value,
    }:
        job = store.transition(
            job_id,
            expected_version=job.state_version,
            to_status=JobStatus.BROWSER_PREPARING,
            actor="pro-first-browser-worker",
            idempotency_key=f"browser-preparing:{job_id}:{job.state_version}",
        )
    if job.status != JobStatus.BROWSER_PREPARING.value:
        raise ValueError(f"browser preparation requires BROWSER_PREPARING, got {job.status}")
    try:
        session = await ProBrowserWorker(config.browser).open(job_id=job_id)
    except Exception as error:
        current = store.get_job(job_id)
        if current.status == JobStatus.BROWSER_PREPARING.value:
            store.transition(
                job_id,
                expected_version=current.state_version,
                to_status=JobStatus.USER_ATTENTION_REQUIRED,
                actor="pro-first-browser-worker",
                idempotency_key=f"browser-attention:{job_id}:{current.state_version}",
                payload={"automatic_login_allowed": False, "automatic_resubmit_allowed": False},
                updates={
                    "last_error_class": type(error).__name__,
                    "last_error_message": str(error),
                },
            )
        raise
    try:
        prepared = await session.adapter.prepare_without_submit(
            browser_session_id=session.browser_session_id,
            packet_path=bundle.research_packet_json,
            packet_hash=bundle.packet_hash,
            prompt=prompt.text,
            prompt_hash=prompt.prompt_hash,
        )
        job = store.record_browser_prepared(
            job_id,
            expected_version=job.state_version,
            browser_session_id=prepared.browser_session_id,
            conversation_id=prepared.conversation_id,
            adapter_name="PlaywrightChatGPTWebAdapter",
            packet_hash=prepared.packet_hash,
            prompt_hash=prepared.prompt_hash,
            state={
                "state": prepared.state.value,
                "uploaded_filename": prepared.uploaded_filename,
                "send_ready": prepared.send_ready,
                "deep_research_ready": prepared.deep_research_ready,
                "submit_count": 0,
            },
            actor="pro-first-browser-worker",
            idempotency_key=f"browser-prepared:{job_id}:{prepared.prompt_hash}",
        )
        if screenshot_path:
            destination = Path(screenshot_path).expanduser().resolve()
            destination.parent.mkdir(parents=True, exist_ok=True)
            await session.page.screenshot(path=str(destination), full_page=False)
        receipt = {
            "schema_version": "e2r_pro_first_live_shadow_receipt_v1",
            "status": "CHATGPT_WEB_SHADOW_COMPATIBILITY_PASS",
            "job_id": job_id,
            "selection_mode": job.mode,
            "browser_session_id": prepared.browser_session_id,
            "conversation_id": prepared.conversation_id,
            "packet_hash": prepared.packet_hash,
            "prompt_hash": prepared.prompt_hash,
            "deep_research_ready": prepared.deep_research_ready,
            "send_ready": prepared.send_ready,
            "submit_count": 0,
            "screenshot_runtime_only": bool(screenshot_path),
        }
        return PreparedBrowserRuntime(
            job=job,
            session=session,
            packet_bundle=bundle,
            prompt=prompt,
            receipt=receipt,
        )
    except Exception as error:
        await session.close()
        current = store.get_job(job_id)
        if current.status == JobStatus.BROWSER_PREPARING.value:
            store.transition(
                job_id,
                expected_version=current.state_version,
                to_status=JobStatus.USER_ATTENTION_REQUIRED,
                actor="pro-first-browser-worker",
                idempotency_key=(
                    f"browser-prepare-attention:{job_id}:{current.state_version}"
                ),
                payload={
                    "automatic_login_allowed": False,
                    "automatic_resubmit_allowed": False,
                    "submit_count": current.submit_count,
                },
                updates={
                    "last_error_class": type(error).__name__,
                    "last_error_message": str(error),
                },
            )
        raise


def _git_head(repo_root: str | Path) -> str:
    # A Windows browser worker can read a WSL repository through UNC while
    # Windows Git rejects the same worktree as ``dubious ownership``.  The
    # launching trusted process may therefore pass the already-resolved source
    # revision explicitly.  It is data only: accept a full hexadecimal object
    # id and never a ref name or command fragment.
    supplied = os.environ.get("E2R_SOURCE_COMMIT_SHA", "").strip().lower()
    if supplied:
        if re.fullmatch(r"[0-9a-f]{40,64}", supplied) is None:
            raise ValueError("E2R_SOURCE_COMMIT_SHA must be a full hexadecimal object id")
        return supplied
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=Path(repo_root).resolve(),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    ).stdout.strip()


__all__ = [
    "BuiltV2JobPacket",
    "PreparedBrowserRuntime",
    "PreparedV2BrowserRuntime",
    "build_job_packet",
    "build_job_packet_v2",
    "create_forced_validation_canary",
    "prepare_job_in_logged_in_browser",
    "prepare_v2_job_in_logged_in_browser",
    "recover_submitted_v2_job_in_logged_in_browser",
]
