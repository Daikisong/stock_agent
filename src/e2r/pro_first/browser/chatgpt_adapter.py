"""ChatGPT DOM adapter using only public, user-visible Playwright actions."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from ..ids import canonical_hash
from .page_helpers import editor_text, first_existing, first_visible, locator_enabled
from .protocol import (
    AttachmentKey,
    BrowserInspection,
    BrowserUIIncompatible,
    BrowserUIState,
    ManualLoginRequired,
    PreparedBrowserJob,
    SubmitAuthorizationRequired,
)
from .selector_registry import (
    ATTACH_BUTTON_SELECTORS,
    DEEP_RESEARCH_ACTIVE_SELECTORS,
    DEEP_RESEARCH_CONTROL_SELECTORS,
    DEEP_RESEARCH_OPTION_SELECTORS,
    EDITOR_SELECTORS,
    FILE_INPUT_SELECTORS,
    LOGIN_INDICATOR_SELECTORS,
    MD_CANDIDATE_SELECTORS,
    SEND_SELECTORS,
    STOP_SELECTORS,
    TOOLS_BUTTON_SELECTORS,
)


class PlaywrightChatGPTWebAdapter:
    """One adapter for real ChatGPT and the local DOM-contract mock."""

    def __init__(self, page: Any) -> None:
        self.page = page
        self._uploaded_filename: str | None = None
        self._prepared_binding: dict[str, str] | None = None
        self._submit_attempted = False

    async def ensure_logged_in(self) -> BrowserInspection:
        editor = await first_visible(self.page, EDITOR_SELECTORS)
        if editor is not None:
            return await self.inspect_state()
        login = await first_visible(self.page, LOGIN_INDICATOR_SELECTORS)
        if login is not None or "/auth/" in self.page.url:
            raise ManualLoginRequired("ChatGPT manual login is required; login automation is forbidden")
        raise BrowserUIIncompatible("ChatGPT prompt editor was not found")

    async def ensure_deep_research_mode(self) -> BrowserInspection:
        await self.ensure_logged_in()
        if await self._deep_research_ready():
            return await self.inspect_state()

        control = await first_visible(self.page, DEEP_RESEARCH_CONTROL_SELECTORS)
        if control is not None and await control.is_enabled():
            await control.click()
            await self.page.wait_for_timeout(100)
            option = await first_visible(self.page, DEEP_RESEARCH_OPTION_SELECTORS)
            if option is not None and await option.is_enabled():
                await option.click()
                await self.page.wait_for_timeout(100)
            if await self._deep_research_ready():
                return await self.inspect_state()

        tools = await first_visible(self.page, TOOLS_BUTTON_SELECTORS)
        if tools is not None and await tools.is_enabled():
            await tools.click()
            option = await first_visible(self.page, DEEP_RESEARCH_OPTION_SELECTORS)
            if option is not None and await option.is_enabled():
                await option.click()
                await self.page.wait_for_timeout(100)
            if await self._deep_research_ready():
                return await self.inspect_state()
        raise BrowserUIIncompatible("Deep Research mode control was not found or did not activate")

    async def upload_packet(self, packet_path: str | Path) -> str:
        path = Path(packet_path).resolve()
        if not path.is_file():
            raise FileNotFoundError(path)
        file_input = await first_existing(self.page, FILE_INPUT_SELECTORS)
        if file_input is not None:
            await file_input.set_input_files(str(path))
        else:
            attach = await first_visible(self.page, ATTACH_BUTTON_SELECTORS)
            if attach is None or not await attach.is_enabled():
                raise BrowserUIIncompatible("ChatGPT packet attachment control was not found")
            async with self.page.expect_file_chooser() as chooser_info:
                await attach.click()
            chooser = await chooser_info.value
            await chooser.set_files(str(path))
        try:
            await self.page.get_by_text(path.name, exact=False).first.wait_for(
                state="visible", timeout=10_000
            )
        except Exception as error:
            raise BrowserUIIncompatible(
                f"uploaded packet filename was not confirmed in the DOM: {path.name}"
            ) from error
        self._uploaded_filename = path.name
        return path.name

    async def set_prompt(self, prompt: str) -> None:
        if not prompt.strip():
            raise ValueError("prompt must be nonempty")
        editor = await first_visible(self.page, EDITOR_SELECTORS)
        if editor is None:
            raise BrowserUIIncompatible("ChatGPT prompt editor was not found")
        await editor.fill(prompt)
        current = await editor_text(editor)
        required_markers = tuple(
            marker for marker in ("[[E2R_PRO_RUN_ID:", "[[E2R_PRO_JOB_ID:") if marker in prompt
        )
        if not current or any(marker not in current for marker in required_markers):
            raise BrowserUIIncompatible("prompt text was not retained by the ChatGPT editor")

    async def prepare_without_submit(
        self,
        *,
        browser_session_id: str,
        packet_path: str | Path,
        packet_hash: str,
        prompt: str,
        prompt_hash: str,
    ) -> PreparedBrowserJob:
        path = Path(packet_path).resolve()
        try:
            packet_payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise BrowserUIIncompatible("prepared packet must be valid research_packet.json") from error
        if canonical_hash(packet_payload) != packet_hash:
            raise BrowserUIIncompatible("prepared packet file hash differs from durable packet hash")
        if canonical_hash({"prompt": prompt}) != prompt_hash:
            raise BrowserUIIncompatible("prepared prompt hash differs from rendered prompt")
        await self.ensure_logged_in()
        await self.ensure_deep_research_mode()
        uploaded_filename = await self.upload_packet(packet_path)
        await self.set_prompt(prompt)
        preexisting = await self.snapshot_attachment_keys()
        send = await first_visible(self.page, SEND_SELECTORS)
        if not await locator_enabled(send):
            raise BrowserUIIncompatible("ChatGPT send button is not ready after packet preparation")
        self._prepared_binding = {
            "browser_session_id": browser_session_id,
            "packet_hash": packet_hash,
            "prompt_hash": prompt_hash,
        }
        return PreparedBrowserJob(
            browser_session_id=browser_session_id,
            conversation_id=self.conversation_id(),
            state=BrowserUIState.AWAITING_USER_APPROVAL,
            packet_path=path,
            packet_hash=packet_hash,
            prompt_hash=prompt_hash,
            uploaded_filename=uploaded_filename,
            prompt_preview=prompt[:500],
            deep_research_ready=True,
            send_ready=True,
            preexisting_attachment_keys=preexisting,
            submit_count=0,
        )

    async def submit_once(self, approval_proof: Any) -> BrowserInspection:
        from ..approval import ConsumedApprovalProof

        if not isinstance(approval_proof, ConsumedApprovalProof) or not approval_proof.ledger_verified:
            raise SubmitAuthorizationRequired("DOM send requires a consumed durable approval proof")
        if self._submit_attempted:
            raise SubmitAuthorizationRequired("this prepared browser adapter already attempted submit")
        expected = self._prepared_binding
        actual = {
            "browser_session_id": approval_proof.browser_session_id,
            "packet_hash": approval_proof.packet_hash,
            "prompt_hash": approval_proof.prompt_hash,
        }
        if expected is None or expected != actual:
            raise SubmitAuthorizationRequired("approval proof does not match prepared browser content")
        editor = await first_visible(self.page, EDITOR_SELECTORS)
        if editor is None:
            raise BrowserUIIncompatible("prompt editor disappeared before submit")
        current_prompt = await editor_text(editor)
        if f"[[E2R_PRO_JOB_ID:{approval_proof.job_id}]]" not in current_prompt:
            raise SubmitAuthorizationRequired("prepared prompt job marker differs from approval proof")
        if approval_proof.conversation_id != self.conversation_id():
            raise SubmitAuthorizationRequired("conversation changed after approval")
        send = await first_visible(self.page, SEND_SELECTORS)
        if not await locator_enabled(send):
            raise BrowserUIIncompatible("ChatGPT send button is not ready")
        self._submit_attempted = True
        await send.click()
        for _attempt in range(50):
            inspection = await self.inspect_state()
            if inspection.state is BrowserUIState.RESEARCH_RUNNING:
                return inspection
            await self.page.wait_for_timeout(100)
        return await self.inspect_state()

    async def inspect_state(self) -> BrowserInspection:
        editor = await first_visible(self.page, EDITOR_SELECTORS)
        login = await first_visible(self.page, LOGIN_INDICATOR_SELECTORS)
        deep_ready = await self._deep_research_ready()
        send = await first_visible(self.page, SEND_SELECTORS)
        stop = await first_visible(self.page, STOP_SELECTORS)
        editor_value = await editor_text(editor) if editor is not None else ""
        body_text = (await self.page.locator("body").inner_text()).lower()
        packet_uploaded = bool(
            self._uploaded_filename and self._uploaded_filename.lower() in body_text
        )
        prompt_ready = bool(editor_value)
        if editor is None and (login is not None or "/auth/" in self.page.url):
            state = BrowserUIState.LOGIN_REQUIRED
        elif any(token in body_text for token in ("usage limit", "quota", "사용 한도", "한도에 도달")):
            state = BrowserUIState.QUOTA_PENDING
        elif stop is not None:
            state = BrowserUIState.RESEARCH_RUNNING
        elif prompt_ready and packet_uploaded and deep_ready:
            state = BrowserUIState.PROMPT_READY
        elif packet_uploaded:
            state = BrowserUIState.PACKET_UPLOADED
        elif deep_ready:
            state = BrowserUIState.DEEP_RESEARCH_MODE_READY
        elif editor is not None:
            state = BrowserUIState.READY_FOR_INPUT
        else:
            state = BrowserUIState.UI_INCOMPATIBLE
        return BrowserInspection(
            state=state,
            conversation_id=self.conversation_id(),
            editor_ready=editor is not None,
            deep_research_ready=deep_ready,
            packet_uploaded=packet_uploaded,
            prompt_ready=prompt_ready,
            send_ready=await locator_enabled(send),
            stop_visible=stop is not None,
        )

    async def capture_result(self, destination: str | Path) -> Any:
        raise NotImplementedError("P6 owns completion detection and atomic capture")

    async def snapshot_attachment_keys(self) -> tuple[AttachmentKey, ...]:
        keys: list[AttachmentKey] = []
        conversation_id = self.conversation_id()
        for selector in MD_CANDIDATE_SELECTORS:
            locator = self.page.locator(selector)
            for index in range(await locator.count()):
                item = locator.nth(index)
                if not await item.is_visible():
                    continue
                text = (await item.inner_text()).strip()
                turn_id = await item.evaluate(
                    """element => {
                        const turn = element.closest('[data-message-id], [data-turn-id]');
                        return turn ? (turn.getAttribute('data-message-id') || turn.getAttribute('data-turn-id')) : null;
                    }"""
                )
                key = AttachmentKey(conversation_id, turn_id, text)
                if key.stable_key not in {row.stable_key for row in keys}:
                    keys.append(key)
        return tuple(keys)

    def conversation_id(self) -> str | None:
        match = re.search(r"/c/([^/?#]+)", self.page.url)
        return match.group(1) if match else None

    async def _deep_research_ready(self) -> bool:
        return await first_visible(self.page, DEEP_RESEARCH_ACTIVE_SELECTORS) is not None


__all__ = ["PlaywrightChatGPTWebAdapter"]
