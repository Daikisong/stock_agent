from __future__ import annotations

import asyncio
import socket
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import unittest
from urllib.request import urlopen

from e2r.pro_first.browser.chatgpt_adapter import PlaywrightChatGPTWebAdapter
from e2r.pro_first.browser.mock_chatgpt_app import MockChatGPTServer
from e2r.pro_first.browser.protocol import (
    BrowserUIIncompatible,
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
        self.packet_payload = {"schema_version": "e2r_pro_research_packet_v1"}
        self.packet_path.write_text(
            json.dumps(self.packet_payload), encoding="utf-8"
        )
        self.packet_hash = canonical_hash(self.packet_payload)
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
            packet_hash=self.packet_hash,
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

    async def test_prepare_waits_for_attachment_processing_without_submitting(self) -> None:
        await self.page.evaluate(
            """() => {
                const send = document.querySelector('#composer-submit-button');
                send.disabled = true;
                window.setTimeout(() => { send.disabled = false; }, 250);
            }"""
        )
        prepared = await self.adapter.prepare_without_submit(
            browser_session_id="BROWSER-session",
            packet_path=self.packet_path,
            packet_hash=self.packet_hash,
            prompt=self.prompt,
            prompt_hash=canonical_hash({"prompt": self.prompt}),
        )
        self.assertTrue(prepared.send_ready)
        self.assertEqual(prepared.submit_count, 0)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

    async def test_prepare_restart_reuses_exact_hashed_attachment(self) -> None:
        first = await self.adapter.prepare_without_submit(
            browser_session_id="BROWSER-session",
            packet_path=self.packet_path,
            packet_hash=self.packet_hash,
            prompt=self.prompt,
            prompt_hash=canonical_hash({"prompt": self.prompt}),
        )
        restarted = PlaywrightChatGPTWebAdapter(self.page)
        second = await restarted.prepare_without_submit(
            browser_session_id="BROWSER-session",
            packet_path=self.packet_path,
            packet_hash=self.packet_hash,
            prompt=self.prompt,
            prompt_hash=canonical_hash({"prompt": self.prompt}),
        )
        self.assertEqual(first.uploaded_filename, second.uploaded_filename)
        self.assertEqual(
            await self.page.locator('#attachments button:has-text("research_packet.json")').count(),
            1,
        )
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

    async def test_upload_packet(self) -> None:
        filename = await self.adapter.upload_packet(self.packet_path)
        self.assertEqual(filename, "research_packet.json")
        self.assertTrue(await self.page.get_by_text(filename, exact=False).is_visible())

    async def test_upload_filename_accepts_visible_accessibility_label(self) -> None:
        await self.page.set_content(
            '<html><body><button aria-label="research_packet.json"></button></body></html>'
        )
        self.assertEqual(
            await self.adapter._wait_for_uploaded_filename("research_packet.json"),
            "research_packet.json",
        )

    async def test_upload_filename_accepts_only_numeric_collision_suffix(self) -> None:
        await self.page.set_content(
            '<html><body><button aria-label="research_packet(2).json"></button></body></html>'
        )
        self.assertEqual(
            await self.adapter._wait_for_uploaded_filename("research_packet.json"),
            "research_packet(2).json",
        )

    async def test_prepare_rejects_packet_or_prompt_hash_mismatch(self) -> None:
        with self.assertRaisesRegex(BrowserUIIncompatible, "packet file hash"):
            await self.adapter.prepare_without_submit(
                browser_session_id="BROWSER-session",
                packet_path=self.packet_path,
                packet_hash="f" * 64,
                prompt=self.prompt,
                prompt_hash=canonical_hash({"prompt": self.prompt}),
            )
        with self.assertRaisesRegex(BrowserUIIncompatible, "prompt hash"):
            await self.adapter.prepare_without_submit(
                browser_session_id="BROWSER-session",
                packet_path=self.packet_path,
                packet_hash=self.packet_hash,
                prompt=self.prompt,
                prompt_hash="e" * 64,
            )
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

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

    async def test_current_chat_plus_pro_mode_is_research_ready(self) -> None:
        await self.page.set_content(
            "<html><body>"
            '<button id="chat" role="radio" data-state="on">Chat</button>'
            '<button id="work" role="radio" data-state="off">Work</button>'
            "<form>"
            '<div id="prompt-textarea" class="ProseMirror" '
            'contenteditable="true"></div>'
            '<button id="reasoning" type="button" data-state="closed">Pro</button>'
            '<button id="composer-submit-button" type="submit">Send</button>'
            "</form></body></html>"
        )
        inspection = await self.adapter.ensure_deep_research_mode()
        self.assertTrue(inspection.deep_research_ready)
        self.assertEqual(await self.page.locator("#chat").get_attribute("data-state"), "on")
        self.assertEqual(await self.page.locator("#work").get_attribute("data-state"), "off")

    async def test_chat_plus_light_does_not_pass_as_pro_mode(self) -> None:
        await self.page.set_content(
            "<html><body>"
            '<button role="radio" data-state="on">Chat</button>'
            "<form>"
            '<div id="prompt-textarea" class="ProseMirror" '
            'contenteditable="true"></div>'
            '<button type="button" data-state="closed">Light</button>'
            "</form></body></html>"
        )
        with self.assertRaisesRegex(BrowserUIIncompatible, "Chat \\+ Pro"):
            await self.adapter.ensure_deep_research_mode()
        self.assertFalse((await self.adapter.inspect_state()).deep_research_ready)

    async def test_work_plus_pro_switches_to_chat_before_becoming_ready(self) -> None:
        await self.page.set_content(
            "<html><body>"
            '<button id="chat" role="radio" data-state="off" '
            'onclick="this.dataset.state=\'on\'; '
            'document.querySelector(\'#work\').dataset.state=\'off\'">Chat</button>'
            '<button id="work" role="radio" data-state="on">Work</button>'
            "<form>"
            '<div id="prompt-textarea" class="ProseMirror" '
            'contenteditable="true"></div>'
            '<button type="button" data-state="closed">Pro</button>'
            "</form></body></html>"
        )
        inspection = await self.adapter.ensure_deep_research_mode()
        self.assertTrue(inspection.deep_research_ready)
        self.assertEqual(await self.page.locator("#chat").get_attribute("data-state"), "on")
        self.assertEqual(await self.page.locator("#work").get_attribute("data-state"), "off")

    async def test_manual_login_is_reported_not_automated(self) -> None:
        await self.page.goto(
            f"{self.server.base_url}/auth/login?state=LOGIN_REQUIRED",
            wait_until="domcontentloaded",
        )
        with self.assertRaises(ManualLoginRequired):
            await self.adapter.ensure_logged_in()
        self.assertEqual(await self.page.locator('a[href="/auth/login"]').count(), 1)

    async def test_logged_out_landing_page_is_manual_login_not_ui_breakage(self) -> None:
        await self.page.set_content(
            "<html><body><main><h1>ChatGPT</h1>"
            '<a href="/sign-up">Sign up</a></main></body></html>'
        )
        with self.assertRaises(ManualLoginRequired):
            await self.adapter.ensure_logged_in()
        inspection = await self.adapter.inspect_state()
        self.assertEqual(inspection.state, BrowserUIState.LOGIN_REQUIRED)

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

    def test_package_import_does_not_eagerly_load_posix_research_provider(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "-c",
                (
                    "import sys, e2r.pro_first; "
                    "print('e2r.research_brain.researcher_mode."
                    "collaboration_provider_bridge' in sys.modules)"
                ),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.stdout.strip(), "False")

    def test_worker_resolves_safe_active_port_file_only_in_memory(self) -> None:
        active_port_file = Path(self.temporary_directory.name) / "DevToolsActivePort"
        active_port_file.write_text(
            "9222\n/devtools/browser/12345678-1234-1234-1234-123456789abc\n",
            encoding="utf-8",
        )
        worker = ProBrowserWorker(
            ProBrowserConfig(cdp_active_port_file=active_port_file)
        )
        self.assertEqual(
            worker._resolve_cdp_endpoint(),
            "ws://127.0.0.1:9222/devtools/browser/12345678-1234-1234-1234-123456789abc",
        )
        self.assertNotIn("12345678-1234", worker.config.cdp_url)

    def test_worker_rejects_unsafe_active_port_file_values(self) -> None:
        active_port_file = Path(self.temporary_directory.name) / "DevToolsActivePort"
        worker = ProBrowserWorker(
            ProBrowserConfig(cdp_active_port_file=active_port_file)
        )
        invalid_values = (
            "0\n/devtools/browser/12345678-1234-1234-1234-123456789abc\n",
            "9222\n/devtools/page/12345678-1234-1234-1234-123456789abc\n",
            "9222\n/devtools/browser/../../etc/passwd\n",
            "not-a-port\n/devtools/browser/12345678-1234-1234-1234-123456789abc\n",
        )
        for value in invalid_values:
            with self.subTest(value=value.splitlines()[0]):
                active_port_file.write_text(value, encoding="utf-8")
                with self.assertRaisesRegex(RuntimeError, "invalid"):
                    worker._resolve_cdp_endpoint()


if __name__ == "__main__":
    unittest.main()
