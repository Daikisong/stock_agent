"""Playwright DOM-only ChatGPT browser integration."""

from .chatgpt_adapter import PlaywrightChatGPTWebAdapter
from .completion_monitor import BrowserCompletionMonitor, ProCompletionStateService
from .protocol import (
    BrowserCaptureRequest,
    BrowserResultSnapshot,
    BrowserUIState,
    ChatGPTWebAdapter,
    PreparedBrowserJob,
    RawBrowserCapture,
)
from .worker import ProBrowserWorker

__all__ = [
    "BrowserCaptureRequest",
    "BrowserCompletionMonitor",
    "BrowserResultSnapshot",
    "BrowserUIState",
    "ChatGPTWebAdapter",
    "PlaywrightChatGPTWebAdapter",
    "PreparedBrowserJob",
    "ProCompletionStateService",
    "ProBrowserWorker",
    "RawBrowserCapture",
]
