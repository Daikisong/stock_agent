"""Playwright DOM-only ChatGPT browser integration."""

from .chatgpt_adapter import PlaywrightChatGPTWebAdapter
from .completion_monitor import BrowserCompletionMonitor, ProCompletionStateService
from .protocol import (
    BrowserCaptureRequest,
    BrowserResultSnapshot,
    BrowserSubmittedTurnPersistence,
    BrowserUIState,
    ChatGPTWebAdapter,
    PreparedBrowserJob,
    PreparedFollowupPass,
    RawBrowserCapture,
)
from .worker import ProBrowserWorker

__all__ = [
    "BrowserCaptureRequest",
    "BrowserCompletionMonitor",
    "BrowserResultSnapshot",
    "BrowserSubmittedTurnPersistence",
    "BrowserUIState",
    "ChatGPTWebAdapter",
    "PlaywrightChatGPTWebAdapter",
    "PreparedBrowserJob",
    "PreparedFollowupPass",
    "ProCompletionStateService",
    "ProBrowserWorker",
    "RawBrowserCapture",
]
