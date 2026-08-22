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
    BrowserCaptureRequest,
    BrowserInspection,
    BrowserResultSnapshot,
    BrowserUIIncompatible,
    BrowserUIState,
    ManualLoginRequired,
    PreparedBrowserJob,
    RawBrowserCapture,
    SubmitAuthorizationRequired,
)
from .selector_registry import (
    ASSISTANT_TURN_SELECTORS,
    ATTACH_BUTTON_SELECTORS,
    CHAT_MODE_ACTIVE_SELECTORS,
    CHAT_MODE_CONTROL_SELECTORS,
    CITATION_SELECTORS,
    DEEP_RESEARCH_ACTIVE_SELECTORS,
    DEEP_RESEARCH_CONTROL_SELECTORS,
    DEEP_RESEARCH_OPTION_SELECTORS,
    EDITOR_SELECTORS,
    FILE_INPUT_SELECTORS,
    LOGIN_INDICATOR_SELECTORS,
    DOWNLOAD_SELECTORS,
    MD_CANDIDATE_SELECTORS,
    PDF_CANDIDATE_SELECTORS,
    PREVIEW_ROOT_SELECTORS,
    PRO_REASONING_ACTIVE_SELECTORS,
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
        self._preexisting_attachment_keys: frozenset[str] = frozenset()
        self._prepared_job_id: str | None = None
        self._prepared_run_id: str | None = None
        self._submit_attempted = False

    async def ensure_logged_in(self) -> BrowserInspection:
        # A newly opened ChatGPT landing page can render the authentication
        # controls a little after ``domcontentloaded``.  Keep this wait finite:
        # login remains a manual user action and is never automated here.
        for attempt in range(9):
            editor = await first_visible(self.page, EDITOR_SELECTORS)
            if editor is not None:
                return await self.inspect_state()
            if await self._manual_login_required():
                raise ManualLoginRequired(
                    "ChatGPT manual login is required; login automation is forbidden"
                )
            if attempt < 8:
                await self.page.wait_for_timeout(250)
        raise BrowserUIIncompatible("ChatGPT prompt editor was not found")

    async def ensure_deep_research_mode(self) -> BrowserInspection:
        """Require the supported Pro research UI before packet preparation.

        The current public UI exposes this as ordinary ``Chat`` mode plus the
        composer reasoning level ``Pro``.  Legacy Deep Research selectors are
        retained for older DOM-contract fixtures and transitional deployments.
        """
        await self.ensure_logged_in()
        if await self._deep_research_ready():
            return await self.inspect_state()

        chat = await first_visible(self.page, CHAT_MODE_CONTROL_SELECTORS)
        if chat is not None and await chat.is_enabled():
            await chat.click()
            await self.page.wait_for_timeout(100)
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
        raise BrowserUIIncompatible(
            "Chat + Pro research mode was not active and no supported legacy "
            "Deep Research control could be activated"
        )

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
        displayed_filename = await self._wait_for_uploaded_filename(path.name)
        if displayed_filename is None:
            raise BrowserUIIncompatible(
                f"uploaded packet filename was not confirmed in the DOM: {path.name}"
            )
        self._uploaded_filename = displayed_filename
        return displayed_filename

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
        uploaded_filename = await self._reuse_matching_uploaded_packet(
            path, packet_hash
        )
        if uploaded_filename is None:
            uploaded_filename = await self.upload_packet(packet_path)
        await self.set_prompt(prompt)
        preexisting = await self.snapshot_attachment_keys()
        send = await self._wait_for_send_ready()
        if send is None:
            raise BrowserUIIncompatible("ChatGPT send button is not ready after packet preparation")
        self._prepared_binding = {
            "browser_session_id": browser_session_id,
            "packet_hash": packet_hash,
            "prompt_hash": prompt_hash,
        }
        self._preexisting_attachment_keys = frozenset(row.stable_key for row in preexisting)
        self._prepared_job_id = self._marker_value(prompt, "E2R_PRO_JOB_ID")
        self._prepared_run_id = self._marker_value(prompt, "E2R_PRO_RUN_ID")
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
        login_required = editor is None and await self._manual_login_required()
        deep_ready = await self._deep_research_ready()
        send = await first_visible(self.page, SEND_SELECTORS)
        stop = await first_visible(self.page, STOP_SELECTORS)
        editor_value = await editor_text(editor) if editor is not None else ""
        body = self.page.locator("body")
        body_text = (await body.inner_text()).lower()
        mock_state = (await body.get_attribute("data-mock-state") or "").upper()
        packet_uploaded = bool(
            self._uploaded_filename and self._uploaded_filename.lower() in body_text
        )
        prompt_ready = bool(editor_value)
        if login_required:
            state = BrowserUIState.LOGIN_REQUIRED
        elif mock_state == "CLARIFICATION" or any(
            token in body_text
            for token in ("before i start, please clarify", "시작하기 전에 확인", "need clarification")
        ):
            state = BrowserUIState.AWAITING_CLARIFICATION
        elif any(token in body_text for token in ("usage limit", "quota", "사용 한도", "한도에 도달")):
            state = BrowserUIState.QUOTA_PENDING
        elif mock_state == "ERROR" or any(
            token in body_text
            for token in ("something went wrong", "network error", "오류가 발생", "다시 시도하세요")
        ):
            state = BrowserUIState.RETRYABLE_ERROR
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
        detail = None
        if state in {
            BrowserUIState.AWAITING_CLARIFICATION,
            BrowserUIState.QUOTA_PENDING,
            BrowserUIState.RETRYABLE_ERROR,
            BrowserUIState.UI_INCOMPATIBLE,
        }:
            detail = (await body.inner_text()).strip()[-2_000:] or state.value
        return BrowserInspection(
            state=state,
            conversation_id=self.conversation_id(),
            editor_ready=editor is not None,
            deep_research_ready=deep_ready,
            packet_uploaded=packet_uploaded,
            prompt_ready=prompt_ready,
            send_ready=await locator_enabled(send),
            stop_visible=stop is not None,
            detail=detail,
        )

    async def inspect_result(self, *, job_id: str, run_id: str) -> BrowserResultSnapshot:
        turns = await self._assistant_turns()
        if not turns:
            return BrowserResultSnapshot(
                conversation_id=self.conversation_id(),
                assistant_turn_id=None,
                report_text="",
                report_hash=canonical_hash({"report_text": "", "attachments": []}),
                has_citations=False,
                has_dossier_marker=False,
                job_marker_matches=False,
                run_marker_matches=False,
                new_attachment_keys=(),
            )
        turn = turns[-1]
        report_text = (await turn.inner_text()).strip()
        turn_id = await self._turn_id(turn)
        has_dossier = (
            "E2R_RESEARCH_DOSSIER_JSON_BEGIN" in report_text
            and "E2R_RESEARCH_DOSSIER_JSON_END" in report_text
        )
        citations = False
        for selector in CITATION_SELECTORS:
            if await turn.locator(selector).count() > 0:
                citations = True
                break
        new_keys = tuple(key for key, _locator in await self._new_md_candidates())
        report_hash = canonical_hash(
            {
                "conversation_id": self.conversation_id(),
                "assistant_turn_id": turn_id,
                "report_text": report_text,
                "attachment_keys": [row.stable_key for row in new_keys],
            }
        )
        return BrowserResultSnapshot(
            conversation_id=self.conversation_id(),
            assistant_turn_id=turn_id,
            report_text=report_text,
            report_hash=report_hash,
            has_citations=citations,
            has_dossier_marker=has_dossier,
            job_marker_matches=f"[[E2R_PRO_JOB_ID:{job_id}]]" in report_text,
            run_marker_matches=f"[[E2R_PRO_RUN_ID:{run_id}]]" in report_text,
            new_attachment_keys=new_keys,
        )

    async def capture_result(self, request: BrowserCaptureRequest) -> RawBrowserCapture:
        snapshot = await self.inspect_result(job_id=request.job_id, run_id=request.run_id)
        if not snapshot.structurally_complete or snapshot.report_hash != request.expected_report_hash:
            raise BrowserUIIncompatible("capture requires the same stable completed assistant result")
        request.staging_directory.mkdir(parents=True, exist_ok=True)
        part_path = request.staging_directory / "pro_report.md.part"
        matching = [
            (key, locator)
            for key, locator in await self._new_md_candidates()
            if key.button_text.strip() == request.expected_filename
        ]
        if matching:
            key, locator = matching[-1]
            download = await self._download_from_candidate(locator)
            suggested = download.suggested_filename
            if suggested.strip() != request.expected_filename:
                raise BrowserUIIncompatible(
                    f"downloaded filename mismatch: expected {request.expected_filename}, got {suggested}"
                )
            await download.save_as(str(part_path))
            if not part_path.is_file() or part_path.stat().st_size == 0:
                raise BrowserUIIncompatible("Playwright download produced an empty MD file")
            source = "DOWNLOAD_MD"
            downloaded_filename = suggested
            attachment_key = key
        else:
            if not snapshot.has_dossier_marker:
                raise BrowserUIIncompatible("no matching new MD and no complete direct report fallback")
            part_path.write_text(snapshot.report_text + "\n", encoding="utf-8")
            source = "DIRECT_REPORT_DOM"
            downloaded_filename = None
            attachment_key = None
        expected_pdf = Path(request.expected_filename).with_suffix(".pdf").name
        matching_pdf = [
            (key, locator)
            for key, locator in await self._new_pdf_candidates()
            if key.button_text.strip() == expected_pdf
        ]
        pdf_part_path = None
        downloaded_pdf_filename = None
        optional_pdf_error = None
        if matching_pdf:
            try:
                _pdf_key, pdf_locator = matching_pdf[-1]
                pdf_download = await self._download_from_candidate(pdf_locator)
                if pdf_download.suggested_filename.strip() != expected_pdf:
                    raise BrowserUIIncompatible("optional PDF filename differs from the expected report")
                pdf_part_path = request.staging_directory / "pro_report.pdf.part"
                await pdf_download.save_as(str(pdf_part_path))
                if not pdf_part_path.read_bytes().startswith(b"%PDF-"):
                    pdf_part_path.unlink(missing_ok=True)
                    raise BrowserUIIncompatible("optional PDF download has no PDF magic header")
                downloaded_pdf_filename = pdf_download.suggested_filename
            except Exception as error:
                optional_pdf_error = f"{type(error).__name__}: {error}"
                pdf_part_path = None
                downloaded_pdf_filename = None
        return RawBrowserCapture(
            conversation_id=snapshot.conversation_id,
            assistant_turn_id=snapshot.assistant_turn_id or "",
            report_md_part_path=part_path,
            source=source,
            downloaded_filename=downloaded_filename,
            attachment_key=attachment_key,
            report_pdf_part_path=pdf_part_path,
            downloaded_pdf_filename=downloaded_pdf_filename,
            optional_pdf_error=optional_pdf_error,
        )

    async def snapshot_attachment_keys(self) -> tuple[AttachmentKey, ...]:
        keys: list[AttachmentKey] = []
        conversation_id = self.conversation_id()
        for selector in (*MD_CANDIDATE_SELECTORS, *PDF_CANDIDATE_SELECTORS):
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

    async def _new_md_candidates(self) -> list[tuple[AttachmentKey, Any]]:
        return await self._new_file_candidates(MD_CANDIDATE_SELECTORS)

    async def _new_pdf_candidates(self) -> list[tuple[AttachmentKey, Any]]:
        return await self._new_file_candidates(PDF_CANDIDATE_SELECTORS)

    async def _new_file_candidates(
        self, selectors: tuple[str, ...]
    ) -> list[tuple[AttachmentKey, Any]]:
        candidates: list[tuple[AttachmentKey, Any]] = []
        seen: set[str] = set()
        for selector in selectors:
            locator = self.page.locator(selector)
            for index in range(await locator.count()):
                item = locator.nth(index)
                if not await item.is_visible():
                    continue
                key = AttachmentKey(
                    self.conversation_id(),
                    await self._turn_id(item),
                    (await item.inner_text()).strip(),
                )
                if key.stable_key in self._preexisting_attachment_keys or key.stable_key in seen:
                    continue
                seen.add(key.stable_key)
                candidates.append((key, item))
        return candidates

    async def _download_from_candidate(self, candidate: Any) -> Any:
        try:
            async with self.page.expect_download(timeout=1_000) as download_info:
                await candidate.click()
            return await download_info.value
        except Exception as direct_error:
            preview = await first_visible(self.page, PREVIEW_ROOT_SELECTORS)
            if preview is None:
                raise BrowserUIIncompatible(
                    "MD candidate produced neither a Playwright download nor a preview"
                ) from direct_error
            download_control = None
            for selector in DOWNLOAD_SELECTORS:
                matches = preview.locator(selector)
                for index in range(await matches.count()):
                    item = matches.nth(index)
                    if not await item.is_visible() or not await item.is_enabled():
                        continue
                    label = " ".join(
                        filter(
                            None,
                            (
                                (await item.inner_text()).strip(),
                                await item.get_attribute("aria-label"),
                                await item.get_attribute("title"),
                            ),
                        )
                    ).lower()
                    if "앱 다운로드" in label or "download app" in label:
                        continue
                    download_control = item
                    break
                if download_control is not None:
                    break
            if download_control is None:
                raise BrowserUIIncompatible("preview has no enabled real download control")
            try:
                async with self.page.expect_download(timeout=10_000) as download_info:
                    await download_control.click()
                return await download_info.value
            except Exception as error:
                raise BrowserUIIncompatible("preview download was not observed by Playwright") from error

    async def _assistant_turns(self) -> list[Any]:
        turns: list[Any] = []
        seen: set[str] = set()
        for selector in ASSISTANT_TURN_SELECTORS:
            locator = self.page.locator(selector)
            for index in range(await locator.count()):
                item = locator.nth(index)
                if not await item.is_visible():
                    continue
                identity = await item.evaluate(
                    "element => element.getAttribute('data-message-id') || element.getAttribute('data-turn-id') || element.outerHTML.slice(0, 200)"
                )
                if identity in seen:
                    continue
                seen.add(identity)
                turns.append(item)
        return turns

    @staticmethod
    async def _turn_id(locator: Any) -> str | None:
        return await locator.evaluate(
            """element => {
                const turn = element.closest('[data-message-id], [data-turn-id]');
                return turn ? (turn.getAttribute('data-message-id') || turn.getAttribute('data-turn-id')) : null;
            }"""
        )

    @staticmethod
    def _marker_value(prompt: str, marker: str) -> str | None:
        match = re.search(rf"\[\[{re.escape(marker)}:([^\]]+)\]\]", prompt)
        return match.group(1) if match else None

    def conversation_id(self) -> str | None:
        match = re.search(r"/c/([^/?#]+)", self.page.url)
        return match.group(1) if match else None

    async def _deep_research_ready(self) -> bool:
        chat_active = await first_visible(self.page, CHAT_MODE_ACTIVE_SELECTORS)
        pro_active = await first_visible(self.page, PRO_REASONING_ACTIVE_SELECTORS)
        if chat_active is not None and pro_active is not None:
            # ``:has-text`` is deliberately followed by an exact text check so
            # a future button such as ``Upgrade to Pro`` cannot satisfy the
            # production readiness gate.
            if " ".join((await pro_active.inner_text()).split()) == "Pro":
                return True
        return await first_visible(self.page, DEEP_RESEARCH_ACTIVE_SELECTORS) is not None

    async def _wait_for_send_ready(self) -> Any | None:
        # ChatGPT can show the uploaded filename before its attachment scan is
        # complete.  During that short interval the visible send button stays
        # disabled, so wait finitely without ever clicking it.
        for attempt in range(300):
            send = await first_visible(self.page, SEND_SELECTORS)
            if await locator_enabled(send):
                return send
            if attempt < 299:
                await self.page.wait_for_timeout(100)
        return None

    async def _wait_for_uploaded_filename(self, filename: str) -> str | None:
        # Current ChatGPT file tiles can expose the name only through their
        # visible accessibility label; older builds rendered it as text.  The
        # public UI may add ``(1)`` after repeated safe preparation attempts.
        path = Path(filename)
        display_pattern = re.compile(
            rf"^{re.escape(path.stem)}(?:\(\d+\))?{re.escape(path.suffix)}$"
        )
        for attempt in range(100):
            label = self.page.get_by_label(display_pattern).first
            if await label.count() and await label.is_visible():
                displayed = (await label.get_attribute("aria-label") or "").strip()
                if display_pattern.fullmatch(displayed):
                    return displayed
            text = self.page.get_by_text(display_pattern).first
            if await text.count() and await text.is_visible():
                displayed = (await text.inner_text()).strip().splitlines()[0]
                if display_pattern.fullmatch(displayed):
                    return displayed
            if attempt < 99:
                await self.page.wait_for_timeout(100)
        return None

    async def _reuse_matching_uploaded_packet(
        self, packet_path: Path, packet_hash: str
    ) -> str | None:
        """Reuse a visible selected file only after exact JSON hash validation."""

        inputs = self.page.locator('input[type="file"]')
        for index in range(await inputs.count()):
            item = inputs.nth(index)
            try:
                selected = await item.evaluate(
                    """async input => {
                        const file = input.files && input.files[0];
                        return file ? {name: file.name, text: await file.text()} : null;
                    }"""
                )
            except Exception:
                continue
            if not selected or str(selected.get("name") or "") != packet_path.name:
                continue
            try:
                payload = json.loads(str(selected.get("text") or ""))
            except json.JSONDecodeError:
                continue
            if canonical_hash(payload) != packet_hash:
                continue
            displayed = await self._wait_for_uploaded_filename(packet_path.name)
            if displayed is not None:
                self._uploaded_filename = displayed
                return displayed
        return None

    async def _manual_login_required(self) -> bool:
        if "/auth/" in self.page.url:
            return True
        if await first_visible(self.page, LOGIN_INDICATOR_SELECTORS) is not None:
            return True
        body = self.page.locator("body")
        try:
            body_text = (await body.inner_text()).lower()
        except Exception:
            return False
        return any(
            marker in body_text
            for marker in (
                "log in",
                "sign up",
                "로그인",
                "회원가입",
            )
        )


__all__ = ["PlaywrightChatGPTWebAdapter"]
