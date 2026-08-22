"""Production packet preparation and logged-in browser shadow operations."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import subprocess
from typing import Any, Mapping

from .browser.worker import BrowserWorkerSession, ProBrowserWorker
from .config import ProFirstLocalConfig
from .ids import canonical_hash, stable_id
from .job_store import ProFirstJobStore
from .models import JobStatus, ProResearchJob, ResearchMode, ScanWindow
from .packet import PacketBuildInput, PacketBundleReceipt, ResearchPacketBuilder, write_packet_bundle
from .prompt_contract import ProResearchPromptContract, RenderedProPrompt


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
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=Path(repo_root).resolve(),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    ).stdout.strip()


__all__ = [
    "PreparedBrowserRuntime",
    "build_job_packet",
    "create_forced_validation_canary",
    "prepare_job_in_logged_in_browser",
]
