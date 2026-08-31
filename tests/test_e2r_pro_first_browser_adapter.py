from __future__ import annotations

import asyncio
import socket
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
import json
from types import SimpleNamespace
import unittest
from urllib.request import urlopen

from e2r.pro_first.browser.chatgpt_adapter import PlaywrightChatGPTWebAdapter
from e2r.pro_first.browser.mock_chatgpt_app import MockChatGPTServer
from e2r.pro_first.browser.protocol import (
    BrowserArtifactUnavailable,
    BrowserCaptureRequest,
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

    async def test_large_prompt_uses_framework_fill_without_submitting(self) -> None:
        large = self.prompt + "\n" + ("긴 full-thesis 검증 문장\n" * 2_500)
        self.assertGreater(len(large), 50_000)
        self.assertLess(len(large), 60_000)
        await self.adapter.set_prompt(large)
        editor = self.page.locator('#prompt-textarea')
        self.assertEqual((await editor.inner_text()).strip(), large.strip())
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

    async def test_prosemirror_paragraph_rows_reconstruct_exact_prompt(self) -> None:
        prompt = "첫째 줄\n\n둘째 줄\n마지막 줄\n"
        editor = self.page.locator("#prompt-textarea")
        await editor.evaluate(
            """(element, text) => {
                element.replaceChildren();
                const newline = String.fromCharCode(10);
                const normalized = text.endsWith(newline)
                    ? text.slice(0, -1)
                    : text;
                for (const line of normalized.split(newline)) {
                    const paragraph = document.createElement('p');
                    if (line) paragraph.textContent = line;
                    else paragraph.appendChild(document.createElement('br'));
                    element.appendChild(paragraph);
                }
            }""",
            prompt,
        )

        self.assertEqual(
            (await self.adapter._editor_exact_text(editor)).rstrip(),
            prompt.rstrip(),
        )

    async def test_followup_sized_prompt_uses_exact_editor_input(self) -> None:
        followup = self.prompt + "\n" + ("질문별 증분 검증 문장\n" * 700)
        self.assertGreater(len(followup), 8_000)
        self.assertLess(len(followup), 20_000)

        await self.adapter.set_prompt(followup)

        editor = self.page.locator("#prompt-textarea")
        self.assertEqual((await editor.inner_text()).strip(), followup.strip())
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

    async def test_followup_closes_download_preview_before_preparing_composer(
        self,
    ) -> None:
        await self.page.evaluate(
            """() => {
                const send = document.querySelector('#composer-submit-button');
                send.disabled = true;
                const flyout = document.createElement('div');
                flyout.dataset.testid = 'stage-thread-flyout';
                const close = document.createElement('button');
                close.dataset.testid = 'close-button';
                close.setAttribute('aria-label', '닫기');
                close.addEventListener('click', () => {
                    flyout.remove();
                    send.disabled = false;
                });
                flyout.appendChild(close);
                document.body.appendChild(flyout);
            }"""
        )
        prompt = (
            "파일 미리보기 종료 후 후속 조사\n"
            "[[E2R_PRO_RUN_ID:PRORUN-bbbbbbbbbbbbbbbbbbbbbbbb]]\n"
            "[[E2R_PRO_JOB_ID:PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa]]\n"
            "[[E2R_PRO_PASS_ID:PROPASS-cccccccccccccccccccccccc]]\n"
            "[[E2R_PRO_PARENT_PASS_ID:PROPASS-dddddddddddddddddddddddd]]"
        )

        prepared = await self.adapter.prepare_followup_without_submit(
            browser_session_id="BROWSER-session",
            conversation_id="mock-conversation",
            job_id="PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa",
            pass_id="PROPASS-cccccccccccccccccccccccc",
            parent_pass_id="PROPASS-dddddddddddddddddddddddd",
            prompt=prompt,
            prompt_hash=canonical_hash({"prompt": prompt}),
        )

        self.assertTrue(prepared.send_ready)
        self.assertEqual(prepared.submit_count, 0)
        self.assertEqual(
            await self.page.locator(
                '[data-testid="stage-thread-flyout"]'
            ).count(),
            0,
        )
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

    async def test_pro_mode_uses_visible_ordinary_chat_composer(self) -> None:
        inspection = await self.adapter.ensure_deep_research_mode()
        self.assertTrue(inspection.deep_research_ready)
        self.assertEqual(
            await self.page.locator('#reasoning-mode').inner_text(),
            "Pro",
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

    async def test_compact_composer_plus_pro_is_research_ready_without_old_tabs(self) -> None:
        await self.page.set_content(
            "<html><body><form>"
            '<div id="prompt-textarea" class="ProseMirror" '
            'contenteditable="true"></div>'
            '<button type="button">Pro</button>'
            "</form></body></html>"
        )
        inspection = await self.adapter.ensure_deep_research_mode()
        self.assertTrue(inspection.deep_research_ready)

    async def test_reload_waits_for_delayed_pro_control_without_clicking_send(self) -> None:
        await self.page.set_content(
            "<html><body><form>"
            '<div id="prompt-textarea" class="ProseMirror" '
            'contenteditable="true"></div>'
            '<button id="composer-submit-button" type="submit">Send</button>'
            "</form><script>"
            "setTimeout(() => {"
            "  const button = document.createElement('button');"
            "  button.type = 'button';"
            "  button.id = 'delayed-pro';"
            "  button.textContent = 'Pro';"
            "  document.querySelector('form').prepend(button);"
            "}, 500);"
            "</script></body></html>"
        )

        inspection = await self.adapter.ensure_deep_research_mode()

        self.assertTrue(inspection.deep_research_ready)
        self.assertEqual(await self.page.locator("#delayed-pro").inner_text(), "Pro")
        self.assertEqual(await self.page.locator("article").count(), 0)

    async def test_legacy_deep_research_is_not_a_pro_substitute(self) -> None:
        await self.page.set_content(
            "<html><body>"
            '<button data-testid="deep-research-toggle" '
            'aria-pressed="true">Deep research</button>'
            "<form>"
            '<div id="prompt-textarea" class="ProseMirror" '
            'contenteditable="true"></div>'
            '<button type="button">Pro</button>'
            "</form></body></html>"
        )
        with self.assertRaisesRegex(BrowserUIIncompatible, "legacy Deep Research"):
            await self.adapter.ensure_deep_research_mode()

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
        with self.assertRaisesRegex(BrowserUIIncompatible, "Pro mode is not active"):
            await self.adapter.ensure_deep_research_mode()
        self.assertFalse((await self.adapter.inspect_state()).deep_research_ready)

    async def test_report_error_words_do_not_become_retryable_ui_error(self) -> None:
        await self.page.set_content(
            "<html><body><form>"
            '<div id="prompt-textarea" class="ProseMirror" '
            'contenteditable="true"></div>'
            '<button type="button">Pro</button></form>'
            '<article data-message-author-role="assistant">'
            "[[E2R_PRO_JOB_ID:PROJOB-example]] "
            "[[E2R_PRO_RUN_ID:PRORUN-example]] "
            "DART gateway에서 오류가 발생했지만 해당 후보를 제외했다. "
            "E2R_RESEARCH_DOSSIER_JSON_END"
            "</article></body></html>"
        )

        inspection = await self.adapter.inspect_state()

        self.assertEqual(
            inspection.state,
            BrowserUIState.DEEP_RESEARCH_MODE_READY,
        )

    async def test_visible_alert_is_retryable_ui_error(self) -> None:
        await self.page.set_content(
            "<html><body><form>"
            '<div id="prompt-textarea" class="ProseMirror" '
            'contenteditable="true"></div>'
            '<button type="button">Pro</button></form>'
            '<div role="alert">오류가 발생했습니다. 다시 시도하세요.</div>'
            "</body></html>"
        )

        inspection = await self.adapter.inspect_state()

        self.assertEqual(inspection.state, BrowserUIState.RETRYABLE_ERROR)

    async def test_latest_section_thinking_failure_beats_older_completed_turn(
        self,
    ) -> None:
        job_id = "PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa"
        run_id = "PRORUN-bbbbbbbbbbbbbbbbbbbbbbbb"
        await self.page.set_content(
            "<html><body><form>"
            '<div id="prompt-textarea" class="ProseMirror" '
            'contenteditable="true"></div>'
            '<button type="button">Pro</button></form>'
            '<section data-turn="assistant" data-turn-id="old-turn">'
            '<div data-message-author-role="assistant" data-message-id="old-message">'
            f"[[E2R_PRO_JOB_ID:{job_id}]] "
            f"[[E2R_PRO_RUN_ID:{run_id}]] "
            "E2R_RESEARCH_DOSSIER_JSON_BEGIN {} "
            "E2R_RESEARCH_DOSSIER_JSON_END"
            "</div></section>"
            '<section data-turn="assistant" data-turn-id="new-failed-turn">'
            "<button>생각 실패</button>"
            "<p>검색은 수행했지만 최종 dossier를 만들기 전에 실패했습니다.</p>"
            "</section></body></html>"
        )

        inspection = await self.adapter.inspect_state()
        result = await self.adapter.inspect_result(job_id=job_id, run_id=run_id)

        self.assertEqual(inspection.state, BrowserUIState.RETRYABLE_ERROR)
        self.assertIn("생각 실패", inspection.detail or "")
        self.assertEqual(result.assistant_turn_id, "new-failed-turn")
        self.assertIn("최종 dossier", result.report_text)
        self.assertFalse(result.structurally_complete)

    async def test_latest_network_failure_beats_stale_stop_control(self) -> None:
        await self.page.set_content(
            "<html><body><form>"
            '<div id="prompt-textarea" class="ProseMirror" '
            'contenteditable="true"></div>'
            '<button type="button">Pro</button>'
            '<button type="button" aria-label="중지">중지</button>'
            "</form>"
            '<section data-turn="assistant" data-turn-id="network-failed-turn">'
            "<p>A network error occurred. Please check your connection.</p>"
            "<button>다시 시도</button>"
            "</section></body></html>"
        )

        inspection = await self.adapter.inspect_state()

        self.assertEqual(inspection.state, BrowserUIState.RETRYABLE_ERROR)
        self.assertIn("network error", (inspection.detail or "").lower())

    async def test_network_words_without_latest_retry_control_keep_running(
        self,
    ) -> None:
        await self.page.set_content(
            "<html><body><form>"
            '<div id="prompt-textarea" class="ProseMirror" '
            'contenteditable="true"></div>'
            '<button type="button">Pro</button>'
            '<button type="button" aria-label="중지">중지</button>'
            "</form>"
            '<section data-turn="assistant" data-turn-id="research-turn">'
            "<p>The filing describes a historical network error.</p>"
            "</section></body></html>"
        )

        inspection = await self.adapter.inspect_state()

        self.assertEqual(inspection.state, BrowserUIState.RESEARCH_RUNNING)

    async def test_latest_completed_assistant_section_wins_in_document_order(
        self,
    ) -> None:
        job_id = "PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa"
        run_id = "PRORUN-bbbbbbbbbbbbbbbbbbbbbbbb"
        await self.page.set_content(
            "<html><body>"
            '<article data-message-author-role="assistant" '
            'data-message-id="old-message">old completed response</article>'
            '<section data-turn="assistant" data-turn-id="new-turn">'
            '<div data-message-author-role="assistant" data-message-id="new-message">'
            f"[[E2R_PRO_JOB_ID:{job_id}]] "
            f"[[E2R_PRO_RUN_ID:{run_id}]] "
            "E2R_RESEARCH_DOSSIER_JSON_BEGIN {} "
            "E2R_RESEARCH_DOSSIER_JSON_END"
            "</div></section></body></html>"
        )

        result = await self.adapter.inspect_result(job_id=job_id, run_id=run_id)

        self.assertEqual(result.assistant_turn_id, "new-turn")
        self.assertTrue(result.structurally_complete)
        self.assertTrue(result.job_marker_matches)
        self.assertTrue(result.run_marker_matches)

    async def test_attachment_backed_dossier_selects_schema_matched_json(self) -> None:
        job_id = "PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa"
        run_id = "PRORUN-bbbbbbbbbbbbbbbbbbbbbbbb"
        dossier_filename = "generated_dossier.json"
        validation_filename = "generated_validation.json"
        await self.page.set_content(
            "<html><body>"
            '<section data-turn="assistant" data-turn-id="attachment-turn">'
            f"[[E2R_PRO_JOB_ID:{job_id}]] "
            f"[[E2R_PRO_RUN_ID:{run_id}]] "
            "전체 dossier와 validation 결과를 첨부했습니다."
            f'<button class="entity-underline">{validation_filename}</button>'
            f'<button class="entity-underline">{dossier_filename}</button>'
            "</section></body></html>"
        )
        payloads = {
            validation_filename: {
                "schema_version": "e2r_pro_research_dossier_validation_v1",
                "job_id": job_id,
                "run_id": run_id,
                "valid": True,
            },
            dossier_filename: {
                "schema_version": "e2r_pro_research_dossier_v3",
                "job_id": job_id,
                "run_id": run_id,
                "source_documents": [],
                "facts": [],
            },
        }

        class FakeDownload:
            def __init__(self, filename: str) -> None:
                self.suggested_filename = filename

            async def save_as(self, destination: str) -> None:
                Path(destination).write_text(
                    json.dumps(payloads[self.suggested_filename]),
                    encoding="utf-8",
                )

        async def fake_download(candidate: object) -> FakeDownload:
            filename = (await candidate.inner_text()).strip()  # type: ignore[attr-defined]
            return FakeDownload(filename)

        self.adapter._download_from_candidate = fake_download  # type: ignore[method-assign]
        result = await self.adapter.inspect_result(job_id=job_id, run_id=run_id)
        self.assertTrue(result.has_json_attachment_candidate)
        self.assertTrue(result.structurally_complete)
        self.assertFalse(result.has_citations)
        self.assertFalse(result.has_dossier_marker)

        staging = Path(self.temporary_directory.name) / "attachment-backed"
        raw = await self.adapter.capture_result(
            BrowserCaptureRequest(
                job_id=job_id,
                run_id=run_id,
                expected_filename="legacy_expected.md",
                expected_report_hash=result.report_hash,
                staging_directory=staging,
            )
        )
        self.assertEqual(raw.source, "DOWNLOAD_JSON")
        self.assertEqual(raw.downloaded_filename, dossier_filename)
        self.assertEqual(
            json.loads(raw.report_md_part_path.read_text(encoding="utf-8")),
            payloads[dossier_filename],
        )

    async def test_direct_artifact_row_download_closes_stale_preview(self) -> None:
        filename = "generated_dossier.json"
        download_url = (
            f"{self.server.base_url}/download?filename={filename}"
            "&job_id=PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa"
            "&run_id=PRORUN-bbbbbbbbbbbbbbbbbbbbbbbb"
        )
        await self.page.set_content(
            "<html><body>"
            '<div role="dialog" aria-label="generated_dossier.json">'
            '<button data-testid="close-button" aria-label="닫기" '
            "onclick=\"this.parentElement.remove()\"></button>"
            "</div>"
            '<section data-turn="assistant" data-turn-id="artifact-turn">'
            '<div class="group/artifact-row">'
            f'<button class="entity-underline">{filename}</button>'
            f'<a aria-label="파일 다운로드" href="{download_url}" '
            f'download="{filename}">다운로드</a>'
            "</div></section></body></html>"
        )

        candidate = self.page.locator(".entity-underline")
        download = await self.adapter._download_from_candidate(candidate)

        self.assertEqual(download.suggested_filename, filename)
        self.assertEqual(await self.page.locator('[role="dialog"]').count(), 0)

    async def test_direct_artifact_row_accepts_exact_authenticated_fetch(self) -> None:
        filename = "generated_dossier.json"
        self.server.server.download_text = json.dumps({"schema_version": "fetch-test"})  # type: ignore[attr-defined]
        download_url = (
            f"{self.server.base_url}/backend-api/conversation/mock-conversation/"
            f"interpreter/download?filename={filename}"
            f"&sandbox_path=%2Fmnt%2Fdata%2F{filename}"
        )
        await self.page.set_content(
            "<html><body>"
            '<section data-turn="assistant" data-turn-id="artifact-turn">'
            '<div class="group/artifact-row">'
            f'<button class="entity-underline">{filename}</button>'
            '<button aria-label="파일 다운로드">다운로드</button>'
            "</div></section>"
            "<script>"
            "document.querySelector('button[aria-label=\"파일 다운로드\"]')"
            f".addEventListener('click', () => fetch('{download_url}'));"
            "</script></body></html>"
        )

        candidate = self.page.locator(".entity-underline")
        download = await self.adapter._download_from_candidate(candidate)
        destination = Path(self.temporary_directory.name) / filename
        await download.save_as(str(destination))

        self.assertEqual(download.suggested_filename, filename)
        self.assertEqual(
            json.loads(destination.read_text(encoding="utf-8")),
            {"schema_version": "fetch-test"},
        )

    async def test_authenticated_fetch_file_not_found_is_transport_error(self) -> None:
        filename = "missing_dossier.json"
        self.server.server.download_text = json.dumps({  # type: ignore[attr-defined]
            "status": "error",
            "error_code": "file_not_found",
            "error_type": "GetDownloadLinkError",
            "error_message": None,
        })
        download_url = (
            f"{self.server.base_url}/backend-api/conversation/mock-conversation/"
            f"interpreter/download?filename={filename}"
            f"&sandbox_path=%2Fmnt%2Fdata%2F{filename}"
        )
        await self.page.set_content(
            "<html><body><div>"
            f'<button class="entity-underline">{filename}</button>'
            '<button aria-label="파일 다운로드">다운로드</button>'
            "</div><script>"
            "document.querySelector('button[aria-label=\"파일 다운로드\"]')"
            f".addEventListener('click', () => fetch('{download_url}'));"
            "</script></body></html>"
        )

        with self.assertRaisesRegex(
            BrowserArtifactUnavailable,
            "no backing sandbox file",
        ):
            await self.adapter._download_from_candidate(
                self.page.locator(".entity-underline")
            )

    async def test_authenticated_fetch_retry_placeholder_is_transport_error(
        self,
    ) -> None:
        filename = "pending_dossier.json"
        self.server.server.download_text = json.dumps(  # type: ignore[attr-defined]
            {"status": "retry"}
        )
        download_url = (
            f"{self.server.base_url}/backend-api/conversation/mock-conversation/"
            f"interpreter/download?filename={filename}"
            f"&sandbox_path=%2Fmnt%2Fdata%2F{filename}"
        )
        await self.page.set_content(
            "<html><body><div>"
            f'<button class="entity-underline">{filename}</button>'
            '<button aria-label="파일 다운로드">다운로드</button>'
            "</div><script>"
            "document.querySelector('button[aria-label=\"파일 다운로드\"]')"
            f".addEventListener('click', () => fetch('{download_url}'));"
            "</script></body></html>"
        )

        with self.assertRaisesRegex(
            BrowserArtifactUnavailable,
            "retry placeholder",
        ):
            await self.adapter._download_from_candidate(
                self.page.locator(".entity-underline")
            )

    async def test_authenticated_fetch_follows_exact_estuary_manifest(self) -> None:
        filename = "generated_dossier.json"
        file_id = "file_exact_generated_dossier"
        dossier = {
            "schema_version": "e2r_pro_research_dossier_v3",
            "job_id": "PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa",
            "run_id": "PRORUN-bbbbbbbbbbbbbbbbbbbbbbbb",
        }
        self.server.set_estuary_text(json.dumps(dossier))
        manifest_url = (
            f"{self.server.base_url}/backend-api/estuary/content"
            f"?fn={filename}&id={file_id}"
        )
        self.server.set_download_text(
            json.dumps(
                {
                    "status": "success",
                    "file_name": filename,
                    "mime_type": "application/json",
                    "metadata": {"file_id": file_id},
                    "download_url": manifest_url,
                }
            )
        )
        first_url = (
            f"{self.server.base_url}/backend-api/conversation/mock-conversation/"
            f"interpreter/download?filename={filename}"
            f"&sandbox_path=%2Fmnt%2Fdata%2F{filename}"
        )
        await self.page.set_content(
            "<html><body><div>"
            f'<button class="entity-underline">{filename}</button>'
            '<button aria-label="파일 다운로드">다운로드</button>'
            "</div><script>"
            "document.querySelector('button[aria-label=\"파일 다운로드\"]')"
            f".addEventListener('click', () => fetch('{first_url}'));"
            "</script></body></html>"
        )

        download = await self.adapter._download_from_candidate(
            self.page.locator(".entity-underline")
        )
        destination = Path(self.temporary_directory.name) / filename
        await download.save_as(str(destination))

        self.assertEqual(
            json.loads(destination.read_text(encoding="utf-8")),
            dossier,
        )

    async def test_authenticated_fetch_accepts_bound_numeric_collision_manifest(
        self,
    ) -> None:
        visible_filename = "generated_dossier.json"
        manifest_filename = "generated_dossier(2).json"
        file_id = "file_exact_collision_generated_dossier"
        dossier = {
            "schema_version": "e2r_pro_research_dossier_v3",
            "job_id": "PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa",
            "run_id": "PRORUN-bbbbbbbbbbbbbbbbbbbbbbbb",
        }
        self.server.set_estuary_text(json.dumps(dossier))
        manifest_url = (
            f"{self.server.base_url}/backend-api/estuary/content"
            f"?fn={manifest_filename}&id={file_id}"
        )
        self.server.set_download_text(
            json.dumps(
                {
                    "status": "success",
                    "file_name": manifest_filename,
                    "mime_type": "application/json",
                    "metadata": {"file_id": file_id},
                    "download_url": manifest_url,
                }
            )
        )
        first_url = (
            f"{self.server.base_url}/backend-api/conversation/mock-conversation/"
            f"interpreter/download?filename={visible_filename}"
            f"&sandbox_path=%2Fmnt%2Fdata%2F{visible_filename}"
        )
        await self.page.set_content(
            "<html><body><div>"
            f'<button class="entity-underline">{visible_filename}</button>'
            '<button aria-label="파일 다운로드">다운로드</button>'
            "</div><script>"
            "document.querySelector('button[aria-label=\"파일 다운로드\"]')"
            f".addEventListener('click', () => fetch('{first_url}'));"
            "</script></body></html>"
        )

        download = await self.adapter._download_from_candidate(
            self.page.locator(".entity-underline")
        )
        destination = Path(self.temporary_directory.name) / visible_filename
        await download.save_as(str(destination))

        self.assertEqual(download.suggested_filename, visible_filename)
        self.assertEqual(
            json.loads(destination.read_text(encoding="utf-8")),
            dossier,
        )

    async def test_authenticated_fetch_rejects_collision_suffix_on_other_stem(
        self,
    ) -> None:
        visible_filename = "generated_dossier.json"
        manifest_filename = "other_dossier(2).json"
        file_id = "file_wrong_collision_stem"
        self.server.set_download_text(
            json.dumps(
                {
                    "status": "success",
                    "file_name": manifest_filename,
                    "mime_type": "application/json",
                    "metadata": {"file_id": file_id},
                    "download_url": (
                        f"{self.server.base_url}/backend-api/estuary/content"
                        f"?fn={manifest_filename}&id={file_id}"
                    ),
                }
            )
        )
        first_url = (
            f"{self.server.base_url}/backend-api/conversation/mock-conversation/"
            f"interpreter/download?filename={visible_filename}"
            f"&sandbox_path=%2Fmnt%2Fdata%2F{visible_filename}"
        )
        await self.page.set_content(
            "<html><body><div>"
            f'<button class="entity-underline">{visible_filename}</button>'
            '<button aria-label="파일 다운로드">다운로드</button>'
            "</div><script>"
            "document.querySelector('button[aria-label=\"파일 다운로드\"]')"
            f".addEventListener('click', () => fetch('{first_url}'));"
            "</script></body></html>"
        )

        with self.assertRaisesRegex(
            BrowserUIIncompatible,
            "not bound to the exact visible file",
        ):
            await self.adapter._download_from_candidate(
                self.page.locator(".entity-underline")
            )

    async def test_authenticated_fetch_rejects_unbound_estuary_manifest(self) -> None:
        filename = "generated_dossier.json"
        file_id = "file_exact_generated_dossier"
        self.server.set_download_text(
            json.dumps(
                {
                    "status": "success",
                    "file_name": filename,
                    "mime_type": "application/json",
                    "metadata": {"file_id": file_id},
                    "download_url": (
                        f"{self.server.base_url}/backend-api/estuary/content"
                        f"?fn=other.json&id={file_id}"
                    ),
                }
            )
        )
        first_url = (
            f"{self.server.base_url}/backend-api/conversation/mock-conversation/"
            f"interpreter/download?filename={filename}"
            f"&sandbox_path=%2Fmnt%2Fdata%2F{filename}"
        )
        await self.page.set_content(
            "<html><body><div>"
            f'<button class="entity-underline">{filename}</button>'
            '<button aria-label="파일 다운로드">다운로드</button>'
            "</div><script>"
            "document.querySelector('button[aria-label=\"파일 다운로드\"]')"
            f".addEventListener('click', () => fetch('{first_url}'));"
            "</script></body></html>"
        )

        with self.assertRaisesRegex(
            BrowserUIIncompatible,
            "not bound to the exact visible file",
        ):
            await self.adapter._download_from_candidate(
                self.page.locator(".entity-underline")
            )

    async def test_latest_result_uses_atomic_dom_snapshot_not_count_then_nth(
        self,
    ) -> None:
        job_id = "PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa"
        run_id = "PRORUN-bbbbbbbbbbbbbbbbbbbbbbbb"
        await self.page.set_content(
            "<html><body>"
            '<section data-turn="assistant" data-turn-id="atomic-turn">'
            f"[[E2R_PRO_JOB_ID:{job_id}]] "
            f"[[E2R_PRO_RUN_ID:{run_id}]] "
            "E2R_RESEARCH_DOSSIER_JSON_BEGIN {} "
            "E2R_RESEARCH_DOSSIER_JSON_END"
            '<a href="https://example.com/source">source</a>'
            "</section></body></html>"
        )

        async def stale_count_then_nth_path() -> list[object]:
            raise AssertionError("count-then-nth assistant lookup must not run")

        self.adapter._assistant_turns = stale_count_then_nth_path  # type: ignore[method-assign]
        result = await self.adapter.inspect_result(job_id=job_id, run_id=run_id)

        self.assertEqual(result.assistant_turn_id, "atomic-turn")
        self.assertTrue(result.structurally_complete)
        self.assertTrue(result.has_citations)
        self.assertIn("https://example.com/source", result.report_text)

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

    async def test_extension_shadow_body_is_not_treated_as_page_body(self) -> None:
        await self.page.evaluate(
            """() => {
                const host = document.createElement('hypeduck-coupang-badge');
                const shadow = host.attachShadow({mode: 'open'});
                const shadowHtml = document.createElement('html');
                const decoy = document.createElement('body');
                decoy.setAttribute('data-mock-state', 'ERROR');
                decoy.innerText = '로그인 오류가 발생했습니다 decoy-only.json';
                shadowHtml.appendChild(decoy);
                shadow.appendChild(shadowHtml);
                document.documentElement.appendChild(host);
            }"""
        )

        inspection = await self.adapter.inspect_state()

        self.assertNotEqual(inspection.state, BrowserUIState.RETRYABLE_ERROR)
        self.assertFalse(await self.adapter._manual_login_required())
        self.assertFalse(await self.adapter._body_contains_text("decoy-only.json"))

    async def test_history_recovery_opens_exact_marked_result_without_submit(self) -> None:
        job_id = "PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa"
        run_id = "PRORUN-bbbbbbbbbbbbbbbbbbbbbbbb"
        report = "\n".join(
            (
                f"[[E2R_PRO_JOB_ID:{job_id}]]",
                f"[[E2R_PRO_RUN_ID:{run_id}]]",
                "E2R_RESEARCH_DOSSIER_JSON_BEGIN",
                "{}",
                "E2R_RESEARCH_DOSSIER_JSON_END",
            )
        )
        await self.page.set_content(
            "<html><body>"
            '<form><div id="prompt-textarea" class="ProseMirror" '
            'contenteditable="true"></div><button type="button">Pro</button></form>'
            '<input placeholder="채팅 검색" />'
            f'<a id="recovered" href="/c/canonical-conversation">{job_id} 독립 조사 보고서</a>'
            '<section id="conversation-results"></section>'
            '<script>window.__submitCount=0;</script>'
            "</body></html>"
        )
        await self.page.locator("#recovered").evaluate(
            """(link, report) => link.addEventListener('click', event => {
                event.preventDefault();
                history.pushState({}, '', link.getAttribute('href'));
                const turn = document.createElement('article');
                turn.dataset.messageAuthorRole = 'assistant';
                turn.dataset.messageId = 'recovered-final-turn';
                turn.textContent = report;
                document.querySelector('#conversation-results').appendChild(turn);
            })""",
            report,
        )

        recovered = await self.adapter.recover_conversation_without_submit(
            job_id=job_id,
            run_id=run_id,
            search_terms=("검증기업",),
        )

        self.assertEqual(recovered.conversation_id, "canonical-conversation")
        self.assertEqual(recovered.search_query, job_id)
        self.assertTrue(recovered.result.structurally_complete)
        self.assertEqual(recovered.submit_count, 0)
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

    async def test_history_recovery_rejects_wrong_run_marker(self) -> None:
        job_id = "PROJOB-aaaaaaaaaaaaaaaaaaaaaaaa"
        run_id = "PRORUN-bbbbbbbbbbbbbbbbbbbbbbbb"
        wrong_report = "\n".join(
            (
                f"[[E2R_PRO_JOB_ID:{job_id}]]",
                "[[E2R_PRO_RUN_ID:PRORUN-wrongwrongwrongwrongwrong]]",
                "E2R_RESEARCH_DOSSIER_JSON_BEGIN",
                "{}",
                "E2R_RESEARCH_DOSSIER_JSON_END",
            )
        )
        await self.page.set_content(
            "<html><body>"
            '<form><div id="prompt-textarea" class="ProseMirror" '
            'contenteditable="true"></div><button type="button">Pro</button></form>'
            '<input placeholder="채팅 검색" />'
            f'<a id="recovered" href="/c/wrong-conversation">{job_id} 독립 조사 보고서</a>'
            '<section id="conversation-results"></section>'
            '<script>window.__submitCount=0;</script>'
            "</body></html>"
        )
        await self.page.locator("#recovered").evaluate(
            """(link, report) => link.addEventListener('click', event => {
                event.preventDefault();
                history.pushState({}, '', link.getAttribute('href'));
                const turn = document.createElement('article');
                turn.dataset.messageAuthorRole = 'assistant';
                turn.dataset.messageId = 'wrong-final-turn';
                turn.textContent = report;
                document.querySelector('#conversation-results').appendChild(turn);
            })""",
            wrong_report,
        )

        with self.assertRaisesRegex(BrowserUIIncompatible, "job/run markers"):
            await self.adapter.recover_conversation_without_submit(
                job_id=job_id,
                run_id=run_id,
            )
        self.assertEqual(await self.page.evaluate("window.__submitCount"), 0)

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
            f"{self.server.base_url}/c/worker-existing-conversation",
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
            initially_listed = json.loads(
                await asyncio.to_thread(
                    lambda: urlopen(
                        f"http://127.0.0.1:{port}/json/list",
                        timeout=1,
                    ).read()
                )
            )
            existing_target_id = next(
                str(row["id"])
                for row in initially_listed
                if row.get("type") == "page"
                and row.get("url")
                == f"{self.server.base_url}/c/worker-existing-conversation"
            )
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
            self.assertEqual(
                session.page.url,
                f"{self.server.base_url}/c/worker-existing-conversation",
            )
            self.assertEqual(len(session.context.pages), 1)
            await session.close()
            listed = json.loads(
                await asyncio.to_thread(
                    lambda: urlopen(
                        f"http://127.0.0.1:{port}/json/list",
                        timeout=1,
                    ).read()
                )
            )
            retained = next(
                (
                    row
                    for row in listed
                    if row.get("type") == "page"
                    and row.get("url")
                    == f"{self.server.base_url}/c/worker-existing-conversation"
                ),
                None,
            )
            self.assertIsNotNone(
                retained,
                "CDP session cleanup closed the pre-existing user page",
            )
            self.assertEqual(str(retained["id"]), existing_target_id)
            reopened = await worker.open(
                job_id="PROJOB-bbbbbbbbbbbbbbbbbbbbbbbb"
            )
            self.assertEqual(
                reopened.page.url,
                f"{self.server.base_url}/c/worker-existing-conversation",
            )
            await reopened.close()
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

    def test_worker_requires_existing_context_without_creating_one(self) -> None:
        worker = ProBrowserWorker()
        with self.assertRaisesRegex(RuntimeError, "existing browser context"):
            worker._require_existing_context(SimpleNamespace(contexts=[]))

        existing = object()
        self.assertIs(
            worker._require_existing_context(
                SimpleNamespace(contexts=[existing])
            ),
            existing,
        )

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
