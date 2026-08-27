"""Browser adapter contracts independent of Playwright imports."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Protocol


class BrowserUIState(str, Enum):
    LOGIN_REQUIRED = "LOGIN_REQUIRED"
    READY_FOR_INPUT = "READY_FOR_INPUT"
    DEEP_RESEARCH_MODE_READY = "DEEP_RESEARCH_MODE_READY"
    PACKET_UPLOADED = "PACKET_UPLOADED"
    PROMPT_READY = "PROMPT_READY"
    AWAITING_USER_APPROVAL = "AWAITING_USER_APPROVAL"
    RESEARCH_RUNNING = "RESEARCH_RUNNING"
    AWAITING_CLARIFICATION = "AWAITING_CLARIFICATION"
    RESEARCH_COMPLETE = "RESEARCH_COMPLETE"
    EXPORT_AVAILABLE = "EXPORT_AVAILABLE"
    QUOTA_PENDING = "QUOTA_PENDING"
    RETRYABLE_ERROR = "RETRYABLE_ERROR"
    UI_INCOMPATIBLE = "UI_INCOMPATIBLE"


@dataclass(frozen=True)
class AttachmentKey:
    conversation_id: str | None
    turn_id: str | None
    button_text: str

    @property
    def stable_key(self) -> str:
        return "|".join((self.conversation_id or "", self.turn_id or "", self.button_text))


@dataclass(frozen=True)
class BrowserInspection:
    state: BrowserUIState
    conversation_id: str | None
    editor_ready: bool
    deep_research_ready: bool
    packet_uploaded: bool
    prompt_ready: bool
    send_ready: bool
    stop_visible: bool
    detail: str | None = None
    metadata: Mapping[str, Any] | None = None


@dataclass(frozen=True)
class BrowserSubmittedTurnPersistence:
    """Fresh public-UI evidence that one submitted user turn is durable.

    The observation is intentionally read-only.  It comes from a temporary
    page opened in the same authenticated browser context, never from a
    private ChatGPT endpoint and never from the optimistic DOM that performed
    the send click.
    """

    observation_id: str
    observed_at: str
    conversation_id: str
    job_id: str
    run_id: str | None
    pass_id: str | None
    parent_pass_id: str | None
    persistence_confirmed: bool
    user_turn_id: str | None
    required_markers: tuple[str, ...]
    missing_markers: tuple[str, ...]
    observed_user_turn_count: int
    fresh_page_url: str
    fresh_page_loaded: bool
    detail: str | None = None
    submit_count: int = 0

    def __post_init__(self) -> None:
        if not self.observation_id.strip() or not self.observed_at.strip():
            raise ValueError("server-persistence observation identity is required")
        if not self.conversation_id.strip() or not self.job_id.strip():
            raise ValueError("server-persistence conversation/job identity is required")
        if self.pass_id is None and self.parent_pass_id is not None:
            raise ValueError("parent pass marker requires a follow-up pass marker")
        if self.pass_id is not None and not self.parent_pass_id:
            raise ValueError("follow-up persistence requires the exact parent pass")
        if not self.required_markers:
            raise ValueError("server-persistence observation requires exact markers")
        if self.observed_user_turn_count < 0:
            raise ValueError("observed user-turn count cannot be negative")
        if self.persistence_confirmed:
            if not self.user_turn_id or self.missing_markers:
                raise ValueError(
                    "confirmed persistence requires one exact user turn and no missing marker"
                )
        elif not self.missing_markers:
            raise ValueError("unconfirmed persistence must name missing markers")
        if self.submit_count != 0:
            raise ValueError("server-persistence inspection must never submit")


@dataclass(frozen=True)
class PreparedBrowserJob:
    browser_session_id: str
    conversation_id: str | None
    state: BrowserUIState
    packet_path: Path
    packet_hash: str
    prompt_hash: str
    uploaded_filename: str
    prompt_preview: str
    deep_research_ready: bool
    send_ready: bool
    preexisting_attachment_keys: tuple[AttachmentKey, ...]
    submit_count: int = 0

    def __post_init__(self) -> None:
        if self.state is not BrowserUIState.AWAITING_USER_APPROVAL:
            raise ValueError("prepared browser job must await user approval")
        if self.submit_count != 0:
            raise ValueError("prepare_without_submit must never submit")


@dataclass(frozen=True)
class PreparedFollowupPass:
    browser_session_id: str
    conversation_id: str
    state: BrowserUIState
    job_id: str
    pass_id: str
    parent_pass_id: str
    prompt_hash: str
    prompt_preview: str
    send_ready: bool
    preexisting_attachment_keys: tuple[AttachmentKey, ...]
    submit_count: int = 0

    def __post_init__(self) -> None:
        if self.state is not BrowserUIState.AWAITING_USER_APPROVAL:
            raise ValueError("prepared follow-up must remain unsent")
        if self.submit_count != 0:
            raise ValueError("follow-up preparation must never submit")


@dataclass(frozen=True)
class BrowserResultSnapshot:
    conversation_id: str | None
    assistant_turn_id: str | None
    report_text: str
    report_hash: str
    has_citations: bool
    has_dossier_marker: bool
    job_marker_matches: bool
    run_marker_matches: bool
    new_attachment_keys: tuple[AttachmentKey, ...]
    raw_report_text: str | None = None
    raw_report_hash: str | None = None
    transport_normalization_operations: tuple[str, ...] = ()
    has_repair_delta_marker: bool = False

    @property
    def structurally_complete(self) -> bool:
        return bool(
            self.assistant_turn_id
            and self.report_text.strip()
            and (
                self.has_citations
                or self.has_dossier_marker
                or self.has_repair_delta_marker
            )
            and self.job_marker_matches
            and self.run_marker_matches
            and (
                self.new_attachment_keys
                or self.has_dossier_marker
                or self.has_repair_delta_marker
            )
        )


@dataclass(frozen=True)
class RecoveredBrowserConversation:
    conversation_id: str
    inspection: BrowserInspection
    result: BrowserResultSnapshot
    search_query: str
    result_href: str
    submit_count: int = 0

    def __post_init__(self) -> None:
        if not self.conversation_id.strip():
            raise ValueError("recovered conversation id must be nonempty")
        if not self.result.structurally_complete:
            raise ValueError("recovered conversation must contain a complete result")
        if not self.result.job_marker_matches or not self.result.run_marker_matches:
            raise ValueError("recovered conversation markers must match the durable job")
        if self.submit_count != 0:
            raise ValueError("conversation recovery must never submit")


@dataclass(frozen=True)
class BrowserCaptureRequest:
    job_id: str
    run_id: str
    expected_filename: str
    expected_report_hash: str
    staging_directory: Path
    allow_readable_report_without_dossier: bool = False


@dataclass(frozen=True)
class BrowserJsonAttachmentRequest:
    job_id: str
    run_id: str
    conversation_id: str
    assistant_turn_id: str
    expected_filename: str
    staging_directory: Path


@dataclass(frozen=True)
class RawBrowserJsonAttachment:
    conversation_id: str
    assistant_turn_id: str
    json_part_path: Path
    downloaded_filename: str
    attachment_key: AttachmentKey
    submit_count: int = 0

    def __post_init__(self) -> None:
        if not self.conversation_id or not self.assistant_turn_id:
            raise ValueError("JSON attachment capture identity must be nonempty")
        if not self.downloaded_filename.strip():
            raise ValueError("downloaded JSON filename must be nonempty")
        if self.submit_count != 0:
            raise ValueError("JSON attachment recovery must never submit")


@dataclass(frozen=True)
class RawBrowserCapture:
    conversation_id: str | None
    assistant_turn_id: str
    report_md_part_path: Path
    source: str
    downloaded_filename: str | None
    attachment_key: AttachmentKey | None
    report_pdf_part_path: Path | None = None
    downloaded_pdf_filename: str | None = None
    optional_pdf_error: str | None = None
    raw_report_md_part_path: Path | None = None
    transport_normalization_operations: tuple[str, ...] = ()


class ChatGPTWebAdapter(Protocol):
    async def ensure_logged_in(self) -> BrowserInspection: ...

    async def ensure_deep_research_mode(self) -> BrowserInspection: ...

    async def upload_packet(self, packet_path: str | Path) -> str: ...

    async def set_prompt(self, prompt: str) -> None: ...

    async def prepare_without_submit(
        self,
        *,
        browser_session_id: str,
        packet_path: str | Path,
        packet_hash: str,
        prompt: str,
        prompt_hash: str,
    ) -> PreparedBrowserJob: ...

    async def submit_once(self, approval_proof: Any) -> BrowserInspection: ...

    async def inspect_submitted_turn_persistence(
        self,
        *,
        conversation_id: str,
        job_id: str,
        pass_id: str | None = None,
        parent_pass_id: str | None = None,
    ) -> BrowserSubmittedTurnPersistence: ...

    async def open_exact_conversation_without_submit(
        self,
        *,
        conversation_id: str,
    ) -> BrowserInspection: ...

    async def prepare_intercepted_followup_submit_recovery(
        self,
        approval_proof: Any,
        *,
        transport_pending_reason: str,
    ) -> None: ...

    async def prepare_followup_without_submit(
        self,
        *,
        browser_session_id: str,
        conversation_id: str,
        job_id: str,
        pass_id: str,
        parent_pass_id: str,
        prompt: str,
        prompt_hash: str,
    ) -> PreparedFollowupPass: ...

    async def inspect_state(self) -> BrowserInspection: ...

    async def inspect_result(self, *, job_id: str, run_id: str) -> BrowserResultSnapshot: ...

    async def recover_conversation_without_submit(
        self,
        *,
        job_id: str,
        run_id: str,
        search_terms: tuple[str, ...] = (),
    ) -> RecoveredBrowserConversation: ...

    async def capture_result(self, request: BrowserCaptureRequest) -> RawBrowserCapture: ...

    async def download_json_attachment_without_submit(
        self, request: BrowserJsonAttachmentRequest
    ) -> RawBrowserJsonAttachment: ...


class ManualLoginRequired(RuntimeError):
    pass


class BrowserUIIncompatible(RuntimeError):
    pass


class SubmitAuthorizationRequired(PermissionError):
    pass


__all__ = [
    "AttachmentKey",
    "BrowserInspection",
    "BrowserCaptureRequest",
    "BrowserJsonAttachmentRequest",
    "BrowserResultSnapshot",
    "BrowserSubmittedTurnPersistence",
    "BrowserUIIncompatible",
    "BrowserUIState",
    "ChatGPTWebAdapter",
    "ManualLoginRequired",
    "PreparedBrowserJob",
    "PreparedFollowupPass",
    "RawBrowserCapture",
    "RawBrowserJsonAttachment",
    "RecoveredBrowserConversation",
    "SubmitAuthorizationRequired",
]
