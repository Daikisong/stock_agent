from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from e2r.pro_first.browser.browseruse_extension_bridge import (
    BrowserUseBridgeClient,
    BrowserUseBridgeError,
    BrowserUsePage,
    validate_bridge_endpoint,
)
from e2r.pro_first.browser.chatgpt_adapter import PlaywrightChatGPTWebAdapter
from e2r.pro_first.browser.protocol import BrowserUIIncompatible
from e2r.pro_first.browser.worker import ProBrowserWorker
from e2r.pro_first.config import BrowserConnectionMode, ProBrowserConfig
from e2r.pro_first.browser.selector_registry import ATTACH_BUTTON_SELECTORS


class BrowserUseBridgeEndpointTest(unittest.TestCase):
    def test_private_endpoint_policy(self) -> None:
        for endpoint in (
            "http://127.0.0.1:12345",
            "http://172.23.224.1:12345",
            "http://10.2.3.4:12345",
        ):
            with self.subTest(endpoint=endpoint):
                self.assertEqual(validate_bridge_endpoint(endpoint), endpoint)
        for endpoint in (
            "https://127.0.0.1:12345",
            "http://8.8.8.8:12345",
            "http://172.32.0.1:12345",
            "http://user:secret@127.0.0.1:12345",
        ):
            with self.subTest(endpoint=endpoint):
                with self.assertRaises(ValueError):
                    validate_bridge_endpoint(endpoint)


class BrowserUseBridgeClientTest(unittest.IsolatedAsyncioTestCase):
    async def test_handshake_rejects_a_different_site(self) -> None:
        payload = json.dumps(
            {
                "ok": True,
                "result": {
                    "session_id": "BROWSERUSE-test-session",
                    "url": "https://example.com/",
                    "title": "not ChatGPT",
                },
            }
        ).encode()
        with patch.object(BrowserUseBridgeClient, "_read_response", return_value=payload):
            with self.assertRaisesRegex(BrowserUseBridgeError, "required ChatGPT origin"):
                await BrowserUseBridgeClient.connect(
                    endpoint="http://127.0.0.1:12345",
                    token="x" * 48,
                    job_id="PROJOB-test",
                )

    async def test_nested_locators_are_bound_by_opaque_parent_handle(self) -> None:
        client = BrowserUseBridgeClient(
            endpoint="http://127.0.0.1:12345",
            token="x" * 48,
        )
        client.session_id = "BROWSERUSE-test-session"
        calls: list[tuple[str, dict[str, object]]] = []

        async def fake_call(operation: str, **arguments: object) -> object:
            calls.append((operation, dict(arguments)))
            if operation == "locator.create":
                return {"handle": f"handle-{len(calls)}"}
            if operation == "locator.count":
                return 1
            raise AssertionError(operation)

        client.call = fake_call  # type: ignore[method-assign]
        page = BrowserUsePage(client)
        count = await page.get_by_role("dialog").get_by_text("Attach").first.count()

        self.assertEqual(count, 1)
        self.assertEqual([name for name, _ in calls], [
            "locator.create", "locator.create", "locator.create", "locator.count"
        ])
        self.assertEqual(calls[1][1]["parent_handle"], "handle-1")
        self.assertEqual(calls[2][1]["parent_handle"], "handle-2")
        self.assertEqual(calls[3][1]["handle"], "handle-3")

    async def test_locator_create_consumes_the_rpc_value_envelope(self) -> None:
        client = BrowserUseBridgeClient(
            endpoint="http://127.0.0.1:12345",
            token="x" * 48,
        )
        client.session_id = "BROWSERUSE-test-session"
        with patch.object(
            client,
            "_request",
            new=AsyncMock(
                return_value={
                    "value": {"handle": "opaque-locator-handle"},
                    "page_url": "https://chatgpt.com/",
                }
            ),
        ):
            locator = BrowserUsePage(client).locator('textarea[placeholder="ChatGPT"]')
            self.assertEqual(await locator._id(), "opaque-locator-handle")

        bridge_source = (
            Path(__file__).parents[1]
            / "src/e2r/pro_first/browser/browseruse_extension_bridge.mjs"
        ).read_text(encoding="utf-8")
        self.assertIn(
            'if (operation === "locator.create") return { value: { handle: makeLocator(args) } };',
            bridge_source,
        )

    async def test_locator_create_missing_handle_fails_with_bridge_error(self) -> None:
        client = BrowserUseBridgeClient(
            endpoint="http://127.0.0.1:12345",
            token="x" * 48,
        )
        client.session_id = "BROWSERUSE-test-session"
        client.call = AsyncMock(return_value=None)  # type: ignore[method-assign]

        with self.assertRaisesRegex(
            BrowserUseBridgeError,
            "locator.create response did not include an opaque handle",
        ):
            await BrowserUsePage(client).locator("textarea").count()


class BrowserUseWorkerIntegrationTest(unittest.IsolatedAsyncioTestCase):
    async def test_worker_uses_only_handed_off_exact_browseruse_session(self) -> None:
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            job_id = "PROJOB-0123456789abcdef01234567"
            handoff_directory = root / ".cache" / "e2r" / "browseruse"
            handoff_directory.mkdir(parents=True)
            handoff_path = handoff_directory / f"{job_id}.json"
            handoff_path.write_text(
                json.dumps(
                    {
                        "job_id": job_id,
                        "session_id": "BROWSERUSE-exact-claimed-tab",
                        "endpoint": "http://172.23.224.1:12345",
                        "token": "x" * 48,
                    }
                ),
                encoding="utf-8",
            )
            handoff_path.chmod(0o600)
            client = SimpleNamespace(
                session_id="BROWSERUSE-exact-claimed-tab",
                current_url="https://chatgpt.com/library",
                current_title="ChatGPT - Library",
                close=AsyncMock(),
            )
            config = ProBrowserConfig(mode=BrowserConnectionMode.BROWSER_USE_EXTENSION)
            with (
                patch("pathlib.Path.home", return_value=root),
                patch(
                    "e2r.pro_first.browser.worker.BrowserUseBridgeClient.connect",
                    new=AsyncMock(return_value=client),
                ) as connect,
            ):
                session = await ProBrowserWorker(config).open(job_id=job_id)
                connect.assert_awaited_once_with(
                    endpoint="http://172.23.224.1:12345",
                    token="x" * 48,
                    job_id=job_id,
                    expected_origin="https://chatgpt.com",
                )
                self.assertEqual(session.page.url, "https://chatgpt.com/library")
                self.assertNotIn("BROWSERUSE-exact-claimed-tab", session.browser_session_id)
                await session.close()
                client.close.assert_awaited_once()


class BrowserUsePacketUploadTest(unittest.IsolatedAsyncioTestCase):
    async def test_packet_uses_visible_session_upload_and_exact_file_hash(self) -> None:
        with TemporaryDirectory() as temporary_directory:
            packet_path = Path(temporary_directory) / "research_packet.json"
            payload = {"schema_version": "e2r_pro_research_packet_v1", "facts": []}
            packet_path.write_text(json.dumps(payload), encoding="utf-8")

            class Locator:
                def __init__(self, *, present: bool, text: str = "") -> None:
                    self.present = present
                    self.text = text
                    self.first = self

                async def count(self) -> int:
                    return int(self.present)

                async def is_visible(self) -> bool:
                    return self.present

                async def get_attribute(self, name: str) -> str | None:
                    return self.text if name == "aria-label" else None

                async def inner_text(self) -> str:
                    return self.text

            class SelectedFile:
                def __init__(self, selected_text: str) -> None:
                    self.selected_text = selected_text

                async def evaluate(self, _expression: str) -> dict[str, str]:
                    return {"name": packet_path.name, "text": self.selected_text}

            class FileInputs:
                def __init__(self, selected_text: str) -> None:
                    self.selected_text = selected_text

                async def count(self) -> int:
                    return 1

                def nth(self, _index: int) -> SelectedFile:
                    return SelectedFile(self.selected_text)

            class FakeBrowserUsePage:
                def __init__(self, selected_text: str) -> None:
                    self.upload_file_via_existing_user_session = AsyncMock()
                    self.selected_text = selected_text

                def get_by_label(self, _pattern: object) -> Locator:
                    return Locator(present=False)

                def get_by_text(self, _pattern: object) -> Locator:
                    return Locator(present=True, text=packet_path.name)

                def locator(self, selector: str) -> object:
                    if selector == 'input[type="file"]':
                        return FileInputs(self.selected_text)
                    raise AssertionError(selector)

                async def wait_for_timeout(self, _milliseconds: int) -> None:
                    return None

            page = FakeBrowserUsePage(json.dumps(payload))
            filename = await PlaywrightChatGPTWebAdapter(page).upload_packet(packet_path)

            self.assertEqual(filename, packet_path.name)
            page.upload_file_via_existing_user_session.assert_awaited_once()
            self.assertEqual(
                page.upload_file_via_existing_user_session.await_args.kwargs["attach_selectors"],
                tuple(ATTACH_BUTTON_SELECTORS),
            )

            different_file_page = FakeBrowserUsePage(json.dumps({"different": True}))
            with self.assertRaisesRegex(BrowserUIIncompatible, "exact BrowserUse packet file/hash"):
                await PlaywrightChatGPTWebAdapter(different_file_page).upload_packet(packet_path)

    async def test_worker_refuses_handoff_for_a_different_tab_identity(self) -> None:
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            job_id = "PROJOB-fedcba9876543210fedcba98"
            handoff_directory = root / ".cache" / "e2r" / "browseruse"
            handoff_directory.mkdir(parents=True)
            handoff_path = handoff_directory / f"{job_id}.json"
            handoff_path.write_text(
                json.dumps(
                    {
                        "job_id": job_id,
                        "session_id": "BROWSERUSE-expected-tab",
                        "endpoint": "http://127.0.0.1:12345",
                        "token": "x" * 48,
                    }
                ),
                encoding="utf-8",
            )
            handoff_path.chmod(0o600)
            client = SimpleNamespace(
                session_id="BROWSERUSE-other-tab",
                close=AsyncMock(),
            )
            with (
                patch("pathlib.Path.home", return_value=root),
                patch(
                    "e2r.pro_first.browser.worker.BrowserUseBridgeClient.connect",
                    new=AsyncMock(return_value=client),
                ),
            ):
                with self.assertRaisesRegex(RuntimeError, "differs from the exact claimed tab"):
                    await ProBrowserWorker(
                        ProBrowserConfig(mode=BrowserConnectionMode.BROWSER_USE_EXTENSION)
                    ).open(job_id=job_id)
                client.close.assert_awaited_once()


if __name__ == "__main__":
    unittest.main()
