"""Playwright connection lifecycle for logged-in Chrome sessions."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
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
                browser = await playwright.chromium.connect_over_cdp(self.config.cdp_url)
                context = browser.contexts[0] if browser.contexts else await browser.new_context()
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
                page = await context.new_page()
                await page.goto(self.config.chatgpt_url, wait_until="domcontentloaded")
            elif not self._same_origin(page.url, self.config.chatgpt_url):
                await page.goto(self.config.chatgpt_url, wait_until="domcontentloaded")
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

    def _matching_page(self, pages: list[Any]) -> Any | None:
        for page in pages:
            if self._same_origin(page.url, self.config.chatgpt_url):
                return page
        return None

    @staticmethod
    def _origin(url: str) -> str:
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}"

    @classmethod
    def _same_origin(cls, first: str, second: str) -> bool:
        return cls._origin(first) == cls._origin(second)


__all__ = ["BrowserWorkerSession", "ProBrowserWorker"]
