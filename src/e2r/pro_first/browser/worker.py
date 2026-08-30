"""Playwright connection lifecycle for logged-in Chrome sessions."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any
from urllib.parse import urlparse

from ..config import BrowserConnectionMode, ProBrowserConfig
from ..ids import stable_id
from .chatgpt_adapter import PlaywrightChatGPTWebAdapter


@dataclass
class BrowserWorkerSession:
    browser_session_id: str
    page: Any
    adapter: PlaywrightChatGPTWebAdapter
    playwright: Any
    browser: Any | None
    context: Any
    attached_over_cdp: bool

    async def close(self) -> None:
        if not self.attached_over_cdp:
            await self.context.close()
        await self.playwright.stop()


class ProBrowserWorker:
    def __init__(self, config: ProBrowserConfig | None = None) -> None:
        self.config = config or ProBrowserConfig()

    async def open(self, *, job_id: str) -> BrowserWorkerSession:
        try:
            from playwright.async_api import async_playwright
        except ImportError as error:
            raise RuntimeError(
                "Playwright optional dependency is required: install project[pro-first]"
            ) from error
        playwright = await async_playwright().start()
        browser: Any | None = None
        attached = self.config.mode is BrowserConnectionMode.CDP_ATTACH
        try:
            if attached:
                browser = await playwright.chromium.connect_over_cdp(
                    self._resolve_cdp_endpoint()
                )
                context = self._require_existing_context(browser)
            else:
                profile = Path(self.config.persistent_profile_path or "").resolve()
                profile.mkdir(parents=True, exist_ok=True)
                context = await playwright.chromium.launch_persistent_context(
                    user_data_dir=str(profile),
                    channel="chrome",
                    headless=False,
                )
            page = self._matching_page(context.pages)
            if page is None:
                raise RuntimeError(
                    "an existing ChatGPT tab is required; the worker will not "
                    "open a new browser tab or window"
                )
            browser_session_id = stable_id(
                "BROWSER",
                {
                    "job_id": job_id,
                    "mode": self.config.mode.value,
                    "chatgpt_origin": self._origin(self.config.chatgpt_url),
                },
            )
            return BrowserWorkerSession(
                browser_session_id=browser_session_id,
                page=page,
                adapter=PlaywrightChatGPTWebAdapter(page),
                playwright=playwright,
                browser=browser,
                context=context,
                attached_over_cdp=attached,
            )
        except Exception:
            await playwright.stop()
            raise

    def _resolve_cdp_endpoint(self) -> str:
        """Resolve Chrome's ephemeral CDP capability without persisting it.

        Chrome 151 can return 404 for the historical ``/json/version`` HTTP
        discovery route while still publishing its loopback WebSocket path in
        ``DevToolsActivePort``.  The second line is therefore read only at
        connection time and is never copied into configuration or receipts.
        """

        active_port_file = self.config.cdp_active_port_file
        if active_port_file is None:
            return self.config.cdp_url
        try:
            lines = active_port_file.read_text(encoding="utf-8").splitlines()
        except OSError as error:
            raise RuntimeError("Chrome DevToolsActivePort is unavailable") from error
        if len(lines) < 2 or not lines[0].isdigit():
            raise RuntimeError("Chrome DevToolsActivePort has an invalid format")
        port = int(lines[0])
        path = lines[1]
        if not 1 <= port <= 65_535:
            raise RuntimeError("Chrome DevToolsActivePort has an invalid port")
        if re.fullmatch(r"/devtools/browser/[A-Za-z0-9_-]{16,128}", path) is None:
            raise RuntimeError("Chrome DevToolsActivePort has an invalid browser path")
        return f"ws://127.0.0.1:{port}{path}"

    def _matching_page(self, pages: list[Any]) -> Any | None:
        for page in reversed(pages):
            if self._same_origin(page.url, self.config.chatgpt_url):
                return page
        return None

    @staticmethod
    def _require_existing_context(browser: Any) -> Any:
        contexts = tuple(browser.contexts)
        if not contexts:
            raise RuntimeError(
                "an existing browser context is required; the worker will not "
                "open a new browser context, tab, or window"
            )
        return contexts[0]

    @staticmethod
    def _origin(url: str) -> str:
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}"

    @classmethod
    def _same_origin(cls, first: str, second: str) -> bool:
        return cls._origin(first) == cls._origin(second)


__all__ = ["BrowserWorkerSession", "ProBrowserWorker"]
