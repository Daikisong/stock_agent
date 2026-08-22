from __future__ import annotations

import asyncio
import socket
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from urllib.request import urlopen

from e2r.pro_first.browser.chatgpt_adapter import PlaywrightChatGPTWebAdapter
from e2r.pro_first.browser.mock_chatgpt_app import MockChatGPTServer
from e2r.pro_first.browser.protocol import (
    BrowserUIState,
    ManualLoginRequired,
    SubmitAuthorizationRequired,
)
from e2r.pro_first.config import BrowserConnectionMode, ProBrowserConfig
from e2r.pro_first.browser.worker import ProBrowserWorker
from e2r.pro_first.ids import canonical_hash


class ProFirstBrowserAdapterTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.server = MockChatGPTServer()
        self.server.__enter__()
        self.addCleanup(self.server.__exit__, None, None, None)
        self.packet_path = Path(self.temporary_directory.name) / "research_packet.json"
        self.packet_path.write_text('{"schema_version":"e2r_pro_research_packet_v1"}\n', encoding="utf-8")
        self.prompt = (
            "독립적으로 조사하라.\n"
            "[[E2R_PRO_RUN_ID:PRORUN-bbbbbbbbbbbbbbbbbbbbbbbb]]\n"
            "[[E2R_PRO_JOB_ID:PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa]]"
        )

    async def asyncSetUp(self) -> None:
        from playwright.async_api import async_playwright

        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.page = await self.browser.new_page()
        await self.page.goto(
            f"{self.server.base_url}/c/mock-conversation",
            wait_until="domcontentloaded",
        )
        self.adapter = PlaywrightChatGPTWebAdapter(self.page)

    async def asyncTearDown(self) -> None:
        await self.browser.close()
        await self.playwright.stop()

    async def test_prepare_does_not_submit(self) -> None:
        prepared = await self.adapter.prepare_without_submit(
            browser_session_id="BROWSER-session",
            packet_path=self.packet_path,
            packet_hash=canonical_hash({"packet": "fixture"}),
            prompt=self.prompt,
            prompt_hash=canonical_hash({"prompt": self.prompt}),
        )
        submit_count = await self.page.evaluate("window.__submitCount")
        self.assertEqual(submit_count, 0)
        self.assertEqual(prepared.submit_count, 0)
        self.assertEqual(prepared.state, BrowserUIState.AWAITING_USER_APPROVAL)
        self.assertTrue(prepared.deep_research_ready)
        self.assertTrue(prepared.send_ready)
        self.assertEqual(prepared.conversation_id, "mock-conversation")
        self.assertIn(
            "old_result.md",
            {row.button_text for row in prepared.preexisting_attachment_keys},
        )

    async def test_upload_packet(self) -> None:
        filename = await self.adapter.upload_packet(self.packet_path)
        self.assertEqual(filename, "research_packet.json")
        self.assertTrue(await self.page.get_by_text(filename, exact=False).is_visible())

    async def test_set_prompt(self) -> None:
        await self.adapter.set_prompt(self.prompt)
        editor = self.page.locator('#prompt-textarea')
        self.assertEqual((await editor.inner_text()).strip(), self.prompt)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

    async def test_deep_research_mode_uses_visible_dom_control(self) -> None:
        inspection = await self.adapter.ensure_deep_research_mode()
        self.assertTrue(inspection.deep_research_ready)
        self.assertEqual(
            await self.page.locator('#deep-research').get_attribute('aria-pressed'),
            "true",
        )

    async def test_manual_login_is_reported_not_automated(self) -> None:
        await self.page.goto(
            f"{self.server.base_url}/auth/login?state=LOGIN_REQUIRED",
            wait_until="domcontentloaded",
        )
        with self.assertRaises(ManualLoginRequired):
            await self.adapter.ensure_logged_in()
        self.assertEqual(await self.page.locator('a[href="/auth/login"]').count(), 1)

    async def test_submit_path_is_unavailable_before_p5_approval_gate(self) -> None:
        with self.assertRaises(SubmitAuthorizationRequired):
            await self.adapter.submit_once(None)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

    async def test_cdp_worker_attaches_without_closing_logged_in_browser(self) -> None:
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", 0))
            port = probe.getsockname()[1]
        profile = Path(self.temporary_directory.name) / "cdp-profile"
        process = await asyncio.create_subprocess_exec(
            self.playwright.chromium.executable_path,
            f"--remote-debugging-port={port}",
            "--remote-debugging-address=127.0.0.1",
            f"--user-data-dir={profile}",
            "--headless=new",
            "--no-sandbox",
            "about:blank",
            stdout=asyncio.subprocess.DEVNULL,
            stderr=asyncio.subprocess.DEVNULL,
        )
        try:
            endpoint = f"http://127.0.0.1:{port}/json/version"
            for _attempt in range(50):
                try:
                    await asyncio.to_thread(lambda: urlopen(endpoint, timeout=0.2).read())
                    break
                except Exception:
                    await asyncio.sleep(0.1)
            else:
                self.fail("CDP endpoint did not become ready")
            worker = ProBrowserWorker(
                ProBrowserConfig(
                    cdp_url=f"http://127.0.0.1:{port}",
                    chatgpt_url=f"{self.server.base_url}/c/worker-conversation",
                    mock_origin_allowed=True,
                )
            )
            session = await worker.open(job_id="PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa")
            inspection = await session.adapter.ensure_logged_in()
            self.assertTrue(inspection.editor_ready)
            self.assertTrue(session.attached_over_cdp)
            await session.close()
            self.assertIsNone(process.returncode)
        finally:
            if process.returncode is None:
                process.terminate()
                await process.wait()

    def test_browser_config_defaults_to_safe_cdp_attach(self) -> None:
        config = ProBrowserConfig()
        self.assertEqual(config.mode, BrowserConnectionMode.CDP_ATTACH)
        self.assertEqual(config.cdp_url, "http://127.0.0.1:9222")
        self.assertTrue(config.require_manual_login)
        self.assertFalse(config.hidden_api_access)
        with self.assertRaisesRegex(ValueError, "hidden/private"):
            ProBrowserConfig(hidden_api_access=True)
        with self.assertRaisesRegex(ValueError, "loopback-only"):
            ProBrowserConfig(cdp_url="http://remote.example:9222")


if __name__ == "__main__":
    unittest.main()
