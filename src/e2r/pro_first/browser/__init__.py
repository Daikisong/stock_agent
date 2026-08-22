"""Playwright DOM-only ChatGPT browser integration."""

from .chatgpt_adapter import PlaywrightChatGPTWebAdapter
from .protocol import BrowserUIState, ChatGPTWebAdapter, PreparedBrowserJob
from .worker import ProBrowserWorker

__all__ = [
    "BrowserUIState",
    "ChatGPTWebAdapter",
    "PlaywrightChatGPTWebAdapter",
    "PreparedBrowserJob",
    "ProBrowserWorker",
]
