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

    async def inspect_state(self) -> BrowserInspection: ...

    async def capture_result(self, destination: str | Path) -> Any: ...


class ManualLoginRequired(RuntimeError):
    pass


class BrowserUIIncompatible(RuntimeError):
    pass


class SubmitAuthorizationRequired(PermissionError):
    pass


__all__ = [
    "AttachmentKey",
    "BrowserInspection",
    "BrowserUIIncompatible",
    "BrowserUIState",
    "ChatGPTWebAdapter",
    "ManualLoginRequired",
    "PreparedBrowserJob",
    "SubmitAuthorizationRequired",
]
