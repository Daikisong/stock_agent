"""ChatGPT DOM adapter using only public, user-visible Playwright actions."""

from __future__ import annotations

import asyncio
import base64
import json
import re
import secrets
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Mapping
from urllib.parse import parse_qs, quote, unquote, urlsplit, urlunsplit

from ..ids import canonical_hash, canonical_json
from .page_helpers import editor_text, first_existing, first_visible, locator_enabled
from .result_transport import normalize_visible_dossier_transport
from .protocol import (
    AttachmentKey,
    BrowserArtifactUnavailable,
    BrowserCaptureRequest,
    BrowserInspection,
    BrowserJsonAttachmentRequest,
    BrowserResultSnapshot,
    BrowserSubmittedTurnPersistence,
    BrowserUIIncompatible,
    BrowserUIState,
    ManualLoginRequired,
    PreparedBrowserJob,
    PreparedFollowupPass,
    RawBrowserCapture,
    RawBrowserJsonAttachment,
    RecoveredBrowserConversation,
    SubmitAuthorizationRequired,
)
from .selector_registry import (
    ASSISTANT_TURN_SELECTORS,
    ATTACH_BUTTON_SELECTORS,
    CHAT_MODE_ACTIVE_SELECTORS,
    CHAT_MODE_CONTROL_SELECTORS,
    CHAT_HISTORY_RESULT_LINK_SELECTORS,
    CHAT_HISTORY_SEARCH_CONTROL_SELECTORS,
    CHAT_HISTORY_SEARCH_INPUT_SELECTORS,
    CITATION_SELECTORS,
    DEEP_RESEARCH_ACTIVE_SELECTORS,
    EDITOR_SELECTORS,
    FILE_INPUT_SELECTORS,
    LOGIN_INDICATOR_SELECTORS,
    DOWNLOAD_SELECTORS,
    JSON_CANDIDATE_SELECTORS,
    MD_CANDIDATE_SELECTORS,
    OPERATIONAL_NOTICE_SELECTORS,
    PDF_CANDIDATE_SELECTORS,
    PREVIEW_CLOSE_SELECTORS,
    PREVIEW_ROOT_SELECTORS,
    PRO_REASONING_ACTIVE_SELECTORS,
    SEND_SELECTORS,
    STOP_SELECTORS,
    USER_TURN_SELECTORS,
    WORK_MODE_ACTIVE_SELECTORS,
)


@dataclass(frozen=True)
class _ResponseBackedDownload:
    """Playwright-download compatible wrapper for ChatGPT's fetched artifact."""

    suggested_filename: str
    content: bytes

    async def save_as(self, destination: str) -> None:
        Path(destination).write_bytes(self.content)


class PlaywrightChatGPTWebAdapter:
    """One adapter for real ChatGPT and the local DOM-contract mock."""

    def __init__(
        self,
        page: Any,
        *,
        server_persistence_max_polls: int = 1_200,
        server_persistence_poll_interval_ms: int = 100,
    ) -> None:
        if server_persistence_max_polls < 1:
            raise ValueError("server-persistence poll bound must be positive")
        if server_persistence_poll_interval_ms < 1:
            raise ValueError("server-persistence poll interval must be positive")
        self.page = page
        self._server_persistence_max_polls = server_persistence_max_polls
        self._server_persistence_poll_interval_ms = (
            server_persistence_poll_interval_ms
        )
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
        """Require the supported ordinary Chat composer with Pro selected.

        The public UI calls this ``Pro``.  It is deliberately distinct from
        the legacy ``Deep research`` tool.  The method name remains stable for
        the browser protocol, but this implementation never activates that
        legacy tool.
        """
        await self.ensure_logged_in()
        if await self._deep_research_ready():
            return await self.inspect_state()

        chat = await first_visible(self.page, CHAT_MODE_CONTROL_SELECTORS)
        if chat is not None and await chat.is_enabled():
            await chat.click()

        # After a report-preview close the exact conversation is reloaded.
        # The editor commonly appears before the reasoning selector, so one
        # immediate probe can misclassify a healthy Pro conversation as Light.
        # Wait finitely for the public Pro control; never click or infer Pro.
        for attempt in range(50):
            if await self._deep_research_ready():
                return await self.inspect_state()
            if await first_visible(self.page, DEEP_RESEARCH_ACTIVE_SELECTORS) is not None:
                break
            if attempt < 49:
                await self.page.wait_for_timeout(100)

        raise BrowserUIIncompatible(
            "ordinary Chat composer + Pro mode is not active; legacy Deep "
            "Research is not an accepted substitute"
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
        # Directly replacing ProseMirror children can make the public DOM look
        # correct while leaving ChatGPT's framework-owned editor state empty.
        # The send button then clears the composer without a durable user turn.
        # Use Playwright's public framework input path and fail before approval
        # if it cannot finish; there is no synthetic-DOM fallback.
        await editor.fill(prompt, timeout=120_000)
        current = await editor_text(editor)
        reconstructed = await self._editor_exact_text(editor)
        raw_text_content = (await editor.text_content()) or ""
        # Chromium represents leading contenteditable spaces as NBSP so they
        # survive HTML whitespace collapsing.  Canonicalize only that browser
        # representation; all other characters and line boundaries must still
        # match the compiled prompt exactly.
        browser_canonical = reconstructed.replace("\u00a0", " ")
        expected = prompt.rstrip()
        retained_dom_text = next(
            (
                candidate
                for candidate in (
                    reconstructed,
                    browser_canonical,
                    current,
                    raw_text_content,
                )
                if candidate.rstrip() == expected
            ),
            reconstructed,
        )
        required_markers = tuple(
            marker for marker in ("[[E2R_PRO_RUN_ID:", "[[E2R_PRO_JOB_ID:") if marker in prompt
        )
        retained_exactly = retained_dom_text.rstrip() == expected
        if (
            not retained_dom_text
            or not retained_exactly
            or any(marker not in retained_dom_text for marker in required_markers)
        ):
            def first_difference(candidate: str) -> int | None:
                for index, (expected_char, actual_char) in enumerate(
                    zip(expected, candidate.rstrip(), strict=False)
                ):
                    if expected_char != actual_char:
                        return index
                if len(expected) != len(candidate.rstrip()):
                    return min(len(expected), len(candidate.rstrip()))
                return None

            missing_markers = [
                marker
                for marker in required_markers
                if marker not in retained_dom_text
            ]
            raise BrowserUIIncompatible(
                "prompt text was not retained by the ChatGPT editor: "
                f"expected_chars={len(prompt.strip())}, "
                f"retained_dom_chars={len(retained_dom_text)}, "
                f"rendered_chars={len(current)}, "
                "candidate_diagnostics="
                f"reconstructed(chars={len(reconstructed)},newlines={reconstructed.count(chr(10))},first_difference={first_difference(reconstructed)}),"
                f"browser_canonical(chars={len(browser_canonical)},newlines={browser_canonical.count(chr(10))},first_difference={first_difference(browser_canonical)}),"
                f"rendered(chars={len(current)},newlines={current.count(chr(10))},first_difference={first_difference(current)}),"
                f"text_content(chars={len(raw_text_content)},newlines={raw_text_content.count(chr(10))},first_difference={first_difference(raw_text_content)}),"
                f"expected(newlines={expected.count(chr(10))}); "
                f"missing_marker_prefixes={missing_markers}"
            )

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
            "authorization_kind": "INITIAL_USER_APPROVAL",
            "browser_session_id": browser_session_id,
            "packet_hash": packet_hash,
            "prompt_hash": prompt_hash,
        }
        self._preexisting_attachment_keys = frozenset(row.stable_key for row in preexisting)
        self._prepared_job_id = self._marker_value(prompt, "E2R_PRO_JOB_ID")
        self._prepared_run_id = self._marker_value(prompt, "E2R_PRO_RUN_ID")
        self._submit_attempted = False
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

    async def recover_initial_prepared_without_mutation(
        self,
        *,
        browser_session_id: str,
        packet_path: str | Path,
        packet_hash: str,
        prompt: str,
        prompt_hash: str,
    ) -> PreparedBrowserJob:
        """Adopt an intact failed-preparation draft without upload or input.

        ChatGPT can keep the selected packet and full composer text after a
        transient attachment toast while the finite preparation wait expires.
        Recovery is allowed only when both browser-local contents hash back to
        the exact durable packet and prompt.  This method never calls file
        upload, editor fill, or send.
        """

        path = Path(packet_path).resolve()
        packet_payload = json.loads(path.read_text(encoding="utf-8"))
        if canonical_hash(packet_payload) != packet_hash:
            raise BrowserUIIncompatible("recovered packet file differs from durable hash")
        if canonical_hash({"prompt": prompt}) != prompt_hash:
            raise BrowserUIIncompatible("recovered prompt differs from durable hash")
        await self.ensure_logged_in()
        if self.conversation_id() is not None:
            raise BrowserUIIncompatible(
                "prepared initial recovery requires the unchanged new-chat route"
            )
        await self.ensure_deep_research_mode()
        uploaded_filename = await self._selected_packet_filename_if_hash_matches(
            path,
            packet_hash,
        )
        if uploaded_filename is None:
            raise BrowserUIIncompatible(
                "prepared initial recovery found no exact selected packet; re-upload is forbidden"
            )
        self._uploaded_filename = uploaded_filename
        editor = await first_visible(self.page, EDITOR_SELECTORS)
        if editor is None:
            raise BrowserUIIncompatible("prepared initial recovery found no editor")
        retained = await self._editor_exact_text(editor)
        if retained.rstrip() != prompt.rstrip():
            raise BrowserUIIncompatible(
                "prepared initial recovery editor differs from the exact durable prompt"
            )
        preexisting = await self.snapshot_attachment_keys()
        send = await self._wait_for_send_ready()
        if send is None:
            raise BrowserUIIncompatible(
                "prepared initial recovery send button remains unavailable"
            )
        self._prepared_binding = {
            "authorization_kind": "INITIAL_USER_APPROVAL",
            "browser_session_id": browser_session_id,
            "packet_hash": packet_hash,
            "prompt_hash": prompt_hash,
        }
        self._preexisting_attachment_keys = frozenset(
            row.stable_key for row in preexisting
        )
        self._prepared_job_id = self._marker_value(prompt, "E2R_PRO_JOB_ID")
        self._prepared_run_id = self._marker_value(prompt, "E2R_PRO_RUN_ID")
        self._submit_attempted = False
        return PreparedBrowserJob(
            browser_session_id=browser_session_id,
            conversation_id=None,
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

    async def prepare_followup_without_submit(
        self,
        *,
        browser_session_id: str,
        conversation_id: str,
        job_id: str,
        pass_id: str,
        parent_pass_id: str,
        prompt: str,
        prompt_hash: str,
    ) -> PreparedFollowupPass:
        if canonical_hash({"prompt": prompt}) != prompt_hash:
            raise BrowserUIIncompatible("follow-up prompt differs from durable compiled hash")
        await self.ensure_logged_in()
        if self.conversation_id() != conversation_id:
            raise BrowserUIIncompatible("follow-up must reuse the approved ChatGPT conversation")
        preview_reloaded = await self._dismiss_visible_file_preview()
        if preview_reloaded and self.conversation_id() != conversation_id:
            raise BrowserUIIncompatible(
                "file-preview reload left the approved ChatGPT conversation"
            )
        await self.ensure_deep_research_mode()
        await self.set_prompt(prompt)
        current = await first_visible(self.page, EDITOR_SELECTORS)
        current_prompt = await editor_text(current) if current is not None else ""
        required = (
            f"[[E2R_PRO_JOB_ID:{job_id}]]",
            f"[[E2R_PRO_PASS_ID:{pass_id}]]",
            f"[[E2R_PRO_PARENT_PASS_ID:{parent_pass_id}]]",
        )
        if any(marker not in current_prompt for marker in required):
            raise BrowserUIIncompatible("follow-up prompt lineage markers were not retained")
        preexisting = await self.snapshot_attachment_keys()
        send = await self._wait_for_send_ready()
        if send is None:
            raise BrowserUIIncompatible("ChatGPT send button is not ready for follow-up")
        self._prepared_binding = {
            "authorization_kind": "SCOPED_FOLLOWUP",
            "browser_session_id": browser_session_id,
            "conversation_id": conversation_id,
            "job_id": job_id,
            "pass_id": pass_id,
            "parent_pass_id": parent_pass_id,
            "prompt_hash": prompt_hash,
        }
        self._preexisting_attachment_keys = frozenset(
            row.stable_key for row in preexisting
        )
        self._prepared_job_id = job_id
        self._prepared_run_id = self._marker_value(prompt, "E2R_PRO_RUN_ID")
        self._submit_attempted = False
        return PreparedFollowupPass(
            browser_session_id=browser_session_id,
            conversation_id=conversation_id,
            state=BrowserUIState.AWAITING_USER_APPROVAL,
            job_id=job_id,
            pass_id=pass_id,
            parent_pass_id=parent_pass_id,
            prompt_hash=prompt_hash,
            prompt_preview=prompt[:500],
            send_ready=True,
            preexisting_attachment_keys=preexisting,
            submit_count=0,
        )

    async def _dismiss_visible_file_preview(
        self,
        *,
        reload_after_close: bool = True,
    ) -> bool:
        """Return from a downloaded report preview to a fresh same-chat composer."""

        close = await first_visible(self.page, PREVIEW_CLOSE_SELECTORS)
        if close is None:
            return False
        await close.click()
        for attempt in range(50):
            if await first_visible(self.page, PREVIEW_CLOSE_SELECTORS) is None:
                # The public ChatGPT UI can leave the React composer disabled
                # after its file flyout disappears.  Reload this exact URL once
                # before inserting the next durable prompt; this neither opens
                # a new conversation nor clicks send.
                if reload_after_close:
                    await self.page.reload(wait_until="domcontentloaded")
                return True
            if attempt < 49:
                await self.page.wait_for_timeout(100)
        raise BrowserUIIncompatible(
            "ChatGPT file preview remained visible after its close control was clicked"
        )

    async def submit_once(self, approval_proof: Any) -> BrowserInspection:
        from ..approval import ConsumedApprovalProof
        from ..multi_pass.orchestrator import ScopedFollowupProof

        if not isinstance(
            approval_proof, (ConsumedApprovalProof, ScopedFollowupProof)
        ) or not approval_proof.ledger_verified:
            raise SubmitAuthorizationRequired("DOM send requires a consumed durable approval proof")
        if self._submit_attempted:
            raise SubmitAuthorizationRequired("this prepared browser adapter already attempted submit")
        expected = self._prepared_binding
        if isinstance(approval_proof, ConsumedApprovalProof):
            actual = {
                "authorization_kind": "INITIAL_USER_APPROVAL",
                "browser_session_id": approval_proof.browser_session_id,
                "packet_hash": approval_proof.packet_hash,
                "prompt_hash": approval_proof.prompt_hash,
            }
        else:
            actual = {
                "authorization_kind": "SCOPED_FOLLOWUP",
                "browser_session_id": approval_proof.browser_session_id,
                "conversation_id": approval_proof.conversation_id,
                "job_id": approval_proof.job_id,
                "pass_id": approval_proof.pass_id,
                "parent_pass_id": approval_proof.parent_pass_id,
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
        if isinstance(approval_proof, ScopedFollowupProof) and (
            f"[[E2R_PRO_PASS_ID:{approval_proof.pass_id}]]" not in current_prompt
            or f"[[E2R_PRO_PARENT_PASS_ID:{approval_proof.parent_pass_id}]]"
            not in current_prompt
        ):
            raise SubmitAuthorizationRequired("prepared follow-up lineage differs from durable pass")
        if approval_proof.conversation_id != self.conversation_id():
            raise SubmitAuthorizationRequired("conversation changed after approval")
        send = await first_visible(self.page, SEND_SELECTORS)
        if not await locator_enabled(send):
            raise BrowserUIIncompatible("ChatGPT send button is not ready")
        self._submit_attempted = True
        try:
            # The exact enabled send control is already bound to a consumed
            # durable proof above.  ChatGPT can continuously animate this
            # button, causing Playwright's coordinate click to wait for
            # "stable" until timeout before dispatch.  Native click avoids
            # that pre-dispatch-only wait without adding a second send path.
            await send.evaluate("element => element.click()")
        except Exception:
            # ChatGPT can start a same-page navigation after the DOM click and
            # keep Playwright waiting until its click timeout even though the
            # prompt is already visibly running.  Inspect once after that
            # single click; never click again.  If the visible state does not
            # prove submission, preserve the exception for recovery-only
            # handling by the durable submit_count=1 ledger.
            inspection = await self.inspect_state()
            if (
                inspection.state is BrowserUIState.RESEARCH_RUNNING
                and inspection.conversation_id == approval_proof.conversation_id
            ):
                return inspection
            raise
        for _attempt in range(50):
            inspection = await self.inspect_state()
            if inspection.state is BrowserUIState.RESEARCH_RUNNING:
                return inspection
            await self.page.wait_for_timeout(100)
        return await self.inspect_state()

    async def inspect_submitted_turn_persistence(
        self,
        *,
        conversation_id: str,
        job_id: str,
        run_id: str | None = None,
        pass_id: str | None = None,
        parent_pass_id: str | None = None,
    ) -> BrowserSubmittedTurnPersistence:
        """Verify one send through a fresh public conversation page.

        ChatGPT may optimistically add the user turn and stop control to the
        page that performed ``send.click()`` even when the turn never reaches
        the durable conversation.  A second page in the same authenticated
        browser context is therefore the authority for dispatch persistence.
        This method only navigates and reads the visible public UI; it never
        calls a private endpoint, edits the composer, or submits anything.
        """

        if not conversation_id.strip() or not job_id.strip():
            raise ValueError("server-persistence inspection requires conversation/job")
        if pass_id is None and parent_pass_id is not None:
            raise ValueError("parent pass requires a follow-up pass")
        if pass_id is not None and not str(parent_pass_id or "").strip():
            raise ValueError("follow-up persistence requires the exact parent pass")
        source_url = urlsplit(str(self.page.url or ""))
        if source_url.scheme not in {"http", "https"} or not source_url.netloc:
            raise BrowserUIIncompatible(
                "fresh persistence inspection requires a public browser origin"
            )
        fresh_url = urlunsplit(
            (
                source_url.scheme,
                source_url.netloc,
                # Recovery IDs may carry the audited ``WEB:`` namespace.
                # Keep the colon path-safe while still escaping slashes and
                # query/fragment delimiters.
                f"/c/{quote(conversation_id, safe=':')}",
                "",
                "",
            )
        )
        prepared_run_id = (
            self._prepared_run_id
            if self._prepared_job_id == job_id and self._prepared_run_id
            else None
        )
        if run_id and prepared_run_id and run_id != prepared_run_id:
            raise ValueError("explicit run differs from the prepared browser run")
        run_id = str(run_id or prepared_run_id or "").strip() or None
        required = [f"[[E2R_PRO_JOB_ID:{job_id}]]"]
        if run_id:
            required.append(f"[[E2R_PRO_RUN_ID:{run_id}]]")
        if pass_id is not None:
            required.extend(
                (
                    f"[[E2R_PRO_PASS_ID:{pass_id}]]",
                    f"[[E2R_PRO_PARENT_PASS_ID:{parent_pass_id}]]",
                )
            )
        required_markers = tuple(required)
        missing_markers = required_markers
        user_turn_id: str | None = None
        observed_user_turn_count = 0
        fresh_page_loaded = False
        detail: str | None = None
        inspection_page = self.page
        observed_url = fresh_url
        try:
            user_selector = ", ".join(USER_TURN_SELECTORS)
            optimistic_snapshot: Mapping[str, Any] = {}
            optimistic_poll_limit = min(
                self._server_persistence_max_polls,
                300,
            )
            for attempt in range(optimistic_poll_limit):
                optimistic_snapshot = await self._user_turn_marker_snapshot(
                    selector=user_selector,
                    required_markers=required_markers,
                )
                observed_user_turn_count = max(
                    observed_user_turn_count,
                    int(
                        optimistic_snapshot.get("observedUserTurnCount") or 0
                    ),
                )
                missing_markers = tuple(
                    optimistic_snapshot.get("missingMarkers") or ()
                )
                if optimistic_snapshot.get("markerMatched") is True:
                    break
                if attempt + 1 < optimistic_poll_limit:
                    await inspection_page.wait_for_timeout(
                        self._server_persistence_poll_interval_ms
                    )
            if optimistic_snapshot.get("markerMatched") is not True:
                detail = (
                    "optimistic public conversation did not render one user "
                    "turn with all exact submission markers; same-tab refresh "
                    "was skipped to avoid cancelling an in-flight submit"
                )
            else:
                # Refresh the exact durable conversation in the already
                # attached public tab only after the guarded click has rendered
                # the exact local user turn.  Navigating a large new-chat
                # submission before that point can cancel its in-flight public
                # request.  The settle interval lets the browser finish the
                # turn's persistence callback without opening another tab.
                await inspection_page.wait_for_timeout(
                    max(1_000, self._server_persistence_poll_interval_ms * 10)
                )
                await inspection_page.goto(
                    fresh_url,
                    wait_until="domcontentloaded",
                    timeout=60_000,
                )
                observed_url = str(inspection_page.url or fresh_url)
                fresh_page_loaded = bool(
                    urlsplit(observed_url).path.rstrip("/")
                    == f"/c/{conversation_id}".rstrip("/")
                )
                for attempt in range(self._server_persistence_max_polls):
                    snapshot = await self._user_turn_marker_snapshot(
                        selector=user_selector,
                        required_markers=required_markers,
                    )
                    observed_user_turn_count = max(
                        observed_user_turn_count,
                        int(snapshot.get("observedUserTurnCount") or 0),
                    )
                    user_turn_id = (
                        str(snapshot.get("userTurnId") or "").strip() or None
                    )
                    if user_turn_id:
                        missing_markers = ()
                        break
                    missing_markers = tuple(
                        snapshot.get("missingMarkers") or ()
                    )
                    if attempt + 1 < self._server_persistence_max_polls:
                        await inspection_page.wait_for_timeout(
                            self._server_persistence_poll_interval_ms
                        )
                if user_turn_id is None:
                    detail = (
                        "fresh public conversation did not contain one user "
                        "turn with all exact submission markers"
                    )
        except Exception as error:
            detail = f"{type(error).__name__}: {error}"
            missing_markers = required_markers
        return BrowserSubmittedTurnPersistence(
            observation_id=f"PROSERVERVIEW-{secrets.token_hex(12)}",
            observed_at=datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            conversation_id=conversation_id,
            job_id=job_id,
            run_id=run_id,
            pass_id=pass_id,
            parent_pass_id=parent_pass_id,
            persistence_confirmed=user_turn_id is not None,
            user_turn_id=user_turn_id,
            required_markers=required_markers,
            missing_markers=missing_markers,
            observed_user_turn_count=observed_user_turn_count,
            fresh_page_url=observed_url,
            fresh_page_loaded=fresh_page_loaded,
            detail=detail,
            submit_count=0,
        )

    async def open_exact_conversation_without_submit(
        self,
        *,
        conversation_id: str,
    ) -> BrowserInspection:
        """Navigate the current public tab to one durable conversation.

        A user may leave the attached logged-in tab on Library or another
        public ChatGPT surface.  Requiring the composer before navigating
        makes that harmless state look like a login failure.  The durable
        conversation id is already ledger-bound, so opening its normal
        ``/c/...`` URL is narrower and safer than history-search heuristics.
        This method only navigates; it never edits or submits the composer.
        """

        if not conversation_id.strip():
            raise ValueError("exact conversation navigation requires an id")
        source_url = urlsplit(str(self.page.url or ""))
        if source_url.scheme not in {"http", "https"} or not source_url.netloc:
            raise BrowserUIIncompatible(
                "exact conversation navigation requires a public browser origin"
            )
        exact_url = urlunsplit(
            (
                source_url.scheme,
                source_url.netloc,
                f"/c/{quote(conversation_id, safe=':')}",
                "",
                "",
            )
        )
        await self.page.goto(
            exact_url,
            wait_until="domcontentloaded",
            timeout=60_000,
        )
        inspection = await self.ensure_logged_in()
        if inspection.conversation_id != conversation_id:
            raise BrowserUIIncompatible(
                "public exact conversation URL did not retain the durable id"
            )
        return inspection

    async def prepare_intercepted_followup_submit_recovery(
        self,
        approval_proof: Any,
        *,
        transport_pending_reason: str,
    ) -> None:
        """Prepare one claimed send whose first click never reached the button.

        This is narrower than a retry.  The durable claim already exists, the
        exact prompt must still be in the composer, no user turn may contain
        the pass marker, and Playwright's prior error must prove that the
        global-search modal intercepted every click before dispatch.  This
        method never clicks send; the durable multi-pass coordinator must call
        the adapter's sole ``submit_once`` boundary after this preflight.
        """

        from ..multi_pass.orchestrator import ScopedFollowupProof

        if (
            not isinstance(approval_proof, ScopedFollowupProof)
            or not approval_proof.ledger_verified
        ):
            raise SubmitAuthorizationRequired(
                "intercepted follow-up recovery requires the durable scoped proof"
            )
        modal_interception = all(
            token in transport_pending_reason
            for token in (
                "Locator.click: Timeout",
                "modal-global-search",
                "intercepts pointer events",
            )
        )
        unstable_send_pre_dispatch = all(
            token in transport_pending_reason
            for token in (
                "Locator.click: Timeout",
                "composer-submit-button",
                "waiting for element to be visible, enabled and stable",
            )
        )
        if not (modal_interception or unstable_send_pre_dispatch):
            raise SubmitAuthorizationRequired(
                "transport evidence does not prove a supported pre-dispatch click failure"
            )
        if self._submit_attempted:
            raise SubmitAuthorizationRequired(
                "this browser adapter already attempted the recovered click"
            )
        await self.ensure_logged_in()
        if self.conversation_id() != approval_proof.conversation_id:
            raise SubmitAuthorizationRequired(
                "conversation changed before intercepted send recovery"
            )
        editor = await first_visible(self.page, EDITOR_SELECTORS)
        if editor is None:
            raise BrowserUIIncompatible(
                "intercepted send recovery requires the preserved prompt editor"
            )
        current_prompt = await editor_text(editor)
        required_markers = (
            f"[[E2R_PRO_JOB_ID:{approval_proof.job_id}]]",
            f"[[E2R_PRO_PASS_ID:{approval_proof.pass_id}]]",
            f"[[E2R_PRO_PARENT_PASS_ID:{approval_proof.parent_pass_id}]]",
        )
        if any(marker not in current_prompt for marker in required_markers):
            raise SubmitAuthorizationRequired(
                "preserved composer does not contain the exact claimed pass"
            )
        # ChatGPT's contenteditable DOM normalizes newlines and list spacing,
        # so text read back from the composer is not byte-identical to the
        # compiled prompt even immediately after ``set_prompt``.  The normal
        # submit boundary therefore binds the compiled hash before insertion
        # and verifies the three exact lineage markers after insertion.  This
        # recovery uses that same boundary plus the stronger absence of an
        # already-sent user turn below.
        pass_marker = required_markers[1]
        user_turns = self.page.locator(", ".join(USER_TURN_SELECTORS))
        for index in range(await user_turns.count()):
            turn = user_turns.nth(index)
            if pass_marker in str(await turn.inner_text() or ""):
                raise SubmitAuthorizationRequired(
                    "claimed pass already exists as a visible user turn"
                )

        modal = await first_visible(
            self.page,
            ('[role="dialog"][data-testid="modal-global-search"]',),
        )
        if modal is not None:
            await modal.press("Escape")
            await self.page.wait_for_timeout(200)
            if await first_visible(
                self.page,
                ('[role="dialog"][data-testid="modal-global-search"]',),
            ) is not None:
                raise BrowserUIIncompatible(
                    "global search modal remained visible after Escape"
                )
        # Recovery proves that the first Playwright click never reached the
        # button, but it does not gain a second DOM submit surface.  Rebind the
        # already-verified visible composer to the durable scoped proof, then
        # enter the same guarded ``submit_once`` boundary used by normal sends.
        self._prepared_binding = {
            "authorization_kind": "SCOPED_FOLLOWUP",
            "browser_session_id": approval_proof.browser_session_id,
            "conversation_id": approval_proof.conversation_id,
            "job_id": approval_proof.job_id,
            "pass_id": approval_proof.pass_id,
            "parent_pass_id": approval_proof.parent_pass_id,
            "prompt_hash": approval_proof.prompt_hash,
        }

    async def inspect_state(self) -> BrowserInspection:
        editor = await first_visible(self.page, EDITOR_SELECTORS)
        login_required = editor is None and await self._manual_login_required()
        deep_ready = await self._deep_research_ready()
        send = await first_visible(self.page, SEND_SELECTORS)
        stop = await first_visible(self.page, STOP_SELECTORS)
        editor_value = await editor_text(editor) if editor is not None else ""
        body = self._main_document_body()
        mock_state = (await body.get_attribute("data-mock-state") or "").upper()
        operational_notice_text = await self._operational_notice_text()
        (
            latest_dossier_complete,
            latest_clarification_visible,
            latest_failure_visible,
            latest_clarification_detail,
        ) = await self._latest_assistant_state_flags()
        packet_uploaded = bool(
            self._uploaded_filename
            and await self._body_contains_text(self._uploaded_filename)
        )
        prompt_ready = bool(editor_value)
        if login_required:
            state = BrowserUIState.LOGIN_REQUIRED
        elif mock_state == "CLARIFICATION" or (
            not latest_dossier_complete
            and latest_clarification_visible
        ):
            state = BrowserUIState.AWAITING_CLARIFICATION
        elif mock_state == "QUOTA" or any(
            token in operational_notice_text
            for token in ("usage limit", "quota", "사용 한도", "한도에 도달")
        ):
            state = BrowserUIState.QUOTA_PENDING
        elif stop is not None:
            # A stale upload/network toast can remain visible after the one
            # authorized send has already started.  The visible stop control
            # is stronger current-state evidence that research is running.
            state = BrowserUIState.RESEARCH_RUNNING
        elif latest_failure_visible:
            state = BrowserUIState.RETRYABLE_ERROR
        elif mock_state == "ERROR" or any(
            token in operational_notice_text
            for token in ("something went wrong", "network error", "오류가 발생", "다시 시도하세요")
        ):
            state = BrowserUIState.RETRYABLE_ERROR
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
        if state is BrowserUIState.AWAITING_CLARIFICATION:
            detail = latest_clarification_detail or state.value
        elif state in {
            BrowserUIState.QUOTA_PENDING,
            BrowserUIState.RETRYABLE_ERROR,
        }:
            detail = (
                operational_notice_text.strip()
                or latest_clarification_detail
                or await self._body_tail_text()
                or state.value
            )
        elif state is BrowserUIState.UI_INCOMPATIBLE:
            detail = await self._body_tail_text() or state.value
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

    async def _body_contains_text(self, value: str) -> bool:
        """Match a small token locally without transferring the whole chat."""

        body = self._main_document_body()
        return bool(
            await body.evaluate(
                """(element, needle) =>
                    (element.innerText || '').toLowerCase().includes(needle)
                """,
                value.lower(),
            )
        )

    async def _user_turn_marker_snapshot(
        self,
        *,
        selector: str,
        required_markers: tuple[str, ...],
    ) -> Mapping[str, Any]:
        """Inspect exact public user-turn markers in one DOM task."""

        return await self.page.evaluate(
            r"""([userSelector, requiredMarkers]) => {
                const matches = Array.from(
                    document.querySelectorAll(userSelector)
                );
                const turns = [];
                const seen = new Set();
                for (const match of matches) {
                    const turn = match.closest(
                        'section[data-turn="user"], '
                        + 'article[data-turn="user"]'
                    ) || match;
                    if (seen.has(turn)) continue;
                    seen.add(turn);
                    turns.push(turn);
                }
                let bestMissing = [...requiredMarkers];
                for (const turn of turns) {
                    const text = turn.textContent || '';
                    const missing = requiredMarkers.filter(
                        marker => !text.includes(marker)
                    );
                    if (missing.length < bestMissing.length) {
                        bestMissing = missing;
                    }
                    if (missing.length) continue;
                    const identified = turn.closest(
                        '[data-message-id], [data-turn-id]'
                    ) || turn.querySelector(
                        '[data-message-id], [data-turn-id]'
                    );
                    const turnId = identified && (
                        identified.getAttribute('data-message-id')
                        || identified.getAttribute('data-turn-id')
                    );
                    return {
                        observedUserTurnCount: turns.length,
                        missingMarkers: [],
                        markerMatched: true,
                        userTurnId: turnId || null
                    };
                }
                return {
                    observedUserTurnCount: turns.length,
                    missingMarkers: bestMissing,
                    markerMatched: false,
                    userTurnId: null
                };
            }""",
            [selector, list(required_markers)],
        )

    async def _body_tail_text(self) -> str:
        """Return only bounded diagnostic text from an incompatible page."""

        body = self._main_document_body()
        return str(
            await body.evaluate(
                """element => (element.innerText || '').trim().slice(-2000)"""
            )
            or ""
        )

    async def _operational_notice_text(self) -> str:
        """Return visible error/quota UI text, excluding conversation prose."""

        values: list[str] = []
        seen: set[str] = set()
        for selector in OPERATIONAL_NOTICE_SELECTORS:
            matches = self.page.locator(selector)
            for index in range(await matches.count()):
                item = matches.nth(index)
                if not await item.is_visible():
                    continue
                text = " ".join(
                    value.strip()
                    for value in (
                        await item.inner_text(),
                        str(await item.get_attribute("aria-label") or ""),
                        str(await item.get_attribute("title") or ""),
                    )
                    if value and value.strip()
                ).lower()
                if text and text not in seen:
                    seen.add(text)
                    values.append(text)
        return "\n".join(values)

    async def _latest_assistant_state_flags(
        self,
    ) -> tuple[bool, bool, bool, str]:
        """Inspect the newest assistant turn without transferring full prose."""

        snapshot = await self._latest_assistant_turn_snapshot()
        if snapshot is None:
            return False, False, False, ""
        raw = str(snapshot.get("raw_text") or "").strip()
        text = raw.lower()
        clarification = any(
            token in text
            for token in (
                "before i start, please clarify",
                "시작하기 전에 확인",
                "need clarification",
            )
        )
        controls = {
            str(value).strip().lower()
            for value in snapshot.get("button_texts") or ()
        }
        visible_failure = any(
            token in controls or text.startswith(token)
            for token in (
                "생각 실패",
                "thinking failed",
                "조사 실패",
                "research failed",
            )
        )
        return (
            "e2r_research_dossier_json_end" in text,
            clarification,
            visible_failure,
            raw[-2000:] if clarification or visible_failure else "",
        )

    async def inspect_result(self, *, job_id: str, run_id: str) -> BrowserResultSnapshot:
        snapshot = await self._latest_assistant_turn_snapshot()
        if snapshot is None:
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
        raw_report_text = str(snapshot.get("raw_text") or "").strip()
        normalization = normalize_visible_dossier_transport(raw_report_text)
        report_text = normalization.normalized_text
        citation_registry = tuple(snapshot.get("citation_registry") or ())
        transport_operations = list(normalization.operations)
        if citation_registry:
            report_text = "\n".join(
                (
                    report_text,
                    "",
                    "E2R_VISIBLE_CITATION_REGISTRY_BEGIN",
                    *(canonical_json(row) for row in citation_registry),
                    "E2R_VISIBLE_CITATION_REGISTRY_END",
                )
            )
            transport_operations.append("APPEND_VISIBLE_CITATION_HREF_REGISTRY")
        turn_id = str(snapshot.get("turn_id") or "").strip() or None
        has_dossier = (
            "E2R_RESEARCH_DOSSIER_JSON_BEGIN" in report_text
            and "E2R_RESEARCH_DOSSIER_JSON_END" in report_text
        )
        has_repair_delta = (
            "E2R_REPAIR_DELTA_JSON_BEGIN" in report_text
            and "E2R_REPAIR_DELTA_JSON_END" in report_text
        )
        citations = bool(snapshot.get("has_citations"))
        new_attachment_rows: list[tuple[AttachmentKey, Any]] = []
        for selectors in (
            MD_CANDIDATE_SELECTORS,
            PDF_CANDIDATE_SELECTORS,
            JSON_CANDIDATE_SELECTORS,
        ):
            new_attachment_rows.extend(
                await self._new_file_candidates(
                    selectors,
                    assistant_turn_id=turn_id,
                )
            )
        new_keys = tuple(key for key, _locator in new_attachment_rows)
        report_hash = canonical_hash(
            {
                "conversation_id": self.conversation_id(),
                "assistant_turn_id": turn_id,
                "report_text": report_text,
                "raw_report_hash": (
                    normalization.raw_hash if normalization.applied else None
                ),
                "transport_normalization_operations": transport_operations,
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
            raw_report_text=(normalization.raw_text if transport_operations else None),
            raw_report_hash=(normalization.raw_hash if transport_operations else None),
            transport_normalization_operations=tuple(transport_operations),
            has_repair_delta_marker=has_repair_delta,
        )

    async def recover_conversation_without_submit(
        self,
        *,
        job_id: str,
        run_id: str,
        search_terms: tuple[str, ...] = (),
    ) -> RecoveredBrowserConversation:
        """Recover a completed submitted job through visible chat history only.

        This path exists specifically for a closed tab or restarted browser.
        It never prepares the composer, uploads a packet, or invokes send.
        Search snippets are only routing hints; exact durable job/run markers
        in the opened assistant result are required before recovery succeeds.
        """

        await self.ensure_logged_in()
        current = await self.inspect_result(job_id=job_id, run_id=run_id)
        if current.structurally_complete and self.conversation_id():
            return RecoveredBrowserConversation(
                conversation_id=str(self.conversation_id()),
                inspection=await self.inspect_state(),
                result=current,
                search_query="CURRENT_PAGE",
                result_href=self.page.url,
            )

        queries = tuple(
            dict.fromkeys(
                value.strip()
                for value in (job_id, *search_terms)
                if value and value.strip()
            )
        )
        for query in queries:
            search_input = await first_visible(
                self.page, CHAT_HISTORY_SEARCH_INPUT_SELECTORS
            )
            if search_input is None:
                control = await first_visible(
                    self.page, CHAT_HISTORY_SEARCH_CONTROL_SELECTORS
                )
                if control is None or not await control.is_enabled():
                    raise BrowserUIIncompatible(
                        "visible ChatGPT history search control was not found"
                    )
                await control.click()
                await self.page.wait_for_timeout(300)
                search_input = await first_visible(
                    self.page, CHAT_HISTORY_SEARCH_INPUT_SELECTORS
                )
            if search_input is None:
                raise BrowserUIIncompatible(
                    "visible ChatGPT history search input was not found"
                )
            await search_input.fill(query)

            match = None
            for attempt in range(60):
                for selector in CHAT_HISTORY_RESULT_LINK_SELECTORS:
                    links = self.page.locator(selector)
                    for index in range(await links.count()):
                        link = links.nth(index)
                        if not await link.is_visible():
                            continue
                        snippet = (await link.inner_text()).strip()
                        if job_id in snippet:
                            match = link
                            break
                    if match is not None:
                        break
                if match is not None:
                    break
                if attempt < 59:
                    await self.page.wait_for_timeout(100)
            if match is None:
                continue

            result_href = str(await match.get_attribute("href") or "")
            await match.click()
            for attempt in range(120):
                result = await self.inspect_result(job_id=job_id, run_id=run_id)
                conversation_id = self.conversation_id()
                if result.structurally_complete and conversation_id:
                    return RecoveredBrowserConversation(
                        conversation_id=conversation_id,
                        inspection=await self.inspect_state(),
                        result=result,
                        search_query=query,
                        result_href=result_href,
                    )
                if attempt < 119:
                    await self.page.wait_for_timeout(100)
            raise BrowserUIIncompatible(
                "history result opened but exact job/run markers did not validate"
            )
        raise BrowserUIIncompatible(
            "submitted ChatGPT conversation was not found in visible history search"
        )

    async def capture_result(self, request: BrowserCaptureRequest) -> RawBrowserCapture:
        snapshot = await self.inspect_result(job_id=request.job_id, run_id=request.run_id)
        readable_override = bool(
            request.allow_readable_report_without_dossier
            and snapshot.assistant_turn_id
            and snapshot.report_text.strip()
            and snapshot.has_citations
            and snapshot.job_marker_matches
            and snapshot.run_marker_matches
        )
        if (
            not (snapshot.structurally_complete or readable_override)
            or snapshot.report_hash != request.expected_report_hash
        ):
            raise BrowserUIIncompatible("capture requires the same stable completed assistant result")
        request.staging_directory.mkdir(parents=True, exist_ok=True)
        part_path = request.staging_directory / "pro_report.md.part"
        raw_part_path: Path | None = None
        transport_operations: tuple[str, ...] = ()
        expected_basename = Path(request.expected_filename).name
        if expected_basename != request.expected_filename:
            raise BrowserUIIncompatible(
                "primary report attachment filename must be one safe basename"
            )
        expected_suffix = Path(request.expected_filename).suffix.casefold()
        if expected_suffix == ".json":
            primary_candidates = await self._new_json_candidates(
                assistant_turn_id=snapshot.assistant_turn_id,
            )
        elif expected_suffix == ".md":
            primary_candidates = await self._new_md_candidates(
                assistant_turn_id=snapshot.assistant_turn_id,
            )
        else:
            raise BrowserUIIncompatible(
                "primary report attachment must use a .md or .json filename"
            )
        matching = [
            (key, locator)
            for key, locator in primary_candidates
            if key.button_text.strip() == request.expected_filename
        ]
        selected_filename = request.expected_filename
        selected_suffix = expected_suffix
        schema_matched_json_candidates: list[tuple[AttachmentKey, Any]] = []
        if not matching and expected_suffix == ".md":
            schema_matched_json_candidates = await self._new_json_candidates(
                assistant_turn_id=snapshot.assistant_turn_id,
            )
        if matching:
            key, locator = matching[-1]
            download = await self._download_from_candidate(locator)
            suggested = download.suggested_filename
            if suggested.strip() != selected_filename:
                raise BrowserUIIncompatible(
                    f"downloaded filename mismatch: expected {selected_filename}, got {suggested}"
                )
            await download.save_as(str(part_path))
            if not part_path.is_file() or part_path.stat().st_size == 0:
                raise BrowserUIIncompatible(
                    "Playwright download produced an empty report attachment"
                )
            try:
                downloaded_text = part_path.read_text(encoding="utf-8-sig")
            except UnicodeDecodeError as error:
                part_path.unlink(missing_ok=True)
                raise BrowserUIIncompatible(
                    "downloaded report attachment is not UTF-8 text"
                ) from error
            if selected_suffix == ".json":
                try:
                    downloaded_json = json.loads(downloaded_text)
                except json.JSONDecodeError as error:
                    part_path.unlink(missing_ok=True)
                    raise BrowserUIIncompatible(
                        "downloaded JSON report is not valid JSON"
                    ) from error
                if not isinstance(downloaded_json, dict):
                    part_path.unlink(missing_ok=True)
                    raise BrowserUIIncompatible(
                        "downloaded JSON report must be a JSON object"
                    )
                if (
                    str(downloaded_json.get("job_id") or "") != request.job_id
                    or str(downloaded_json.get("run_id") or "") != request.run_id
                ):
                    part_path.unlink(missing_ok=True)
                    raise BrowserUIIncompatible(
                        "downloaded JSON report job/run identity differs from the capture request"
                    )
                source = "DOWNLOAD_JSON"
            else:
                downloaded_normalization = normalize_visible_dossier_transport(
                    downloaded_text
                )
                if downloaded_normalization.applied:
                    raw_part_path = request.staging_directory / "pro_report.raw.md.part"
                    part_path.replace(raw_part_path)
                    part_path.write_bytes(
                        downloaded_normalization.normalized_text.encode("utf-8")
                    )
                    transport_operations = downloaded_normalization.operations
                    source = "DOWNLOAD_MD_NORMALIZED"
                else:
                    source = "DOWNLOAD_MD"
            downloaded_filename = suggested
            attachment_key = key
        elif schema_matched_json_candidates:
            (
                key,
                selected_filename,
                downloaded_json,
            ) = await self._download_schema_matched_dossier_json(
                candidates=schema_matched_json_candidates,
                assistant_turn_id=snapshot.assistant_turn_id,
                part_path=part_path,
                job_id=request.job_id,
                run_id=request.run_id,
            )
            selected_suffix = ".json"
            source = "DOWNLOAD_JSON"
            downloaded_filename = selected_filename
            attachment_key = key
        else:
            if not (
                snapshot.has_dossier_marker
                or snapshot.has_repair_delta_marker
                or readable_override
            ):
                raise BrowserUIIncompatible(
                    "no matching new report attachment and no complete direct report fallback"
                )
            part_path.write_bytes((snapshot.report_text + "\n").encode("utf-8"))
            if snapshot.transport_normalization_operations:
                if snapshot.raw_report_text is None:
                    raise BrowserUIIncompatible(
                        "normalized visible result is missing its immutable raw report"
                    )
                raw_part_path = request.staging_directory / "pro_report.raw.md.part"
                raw_part_path.write_bytes(
                    (snapshot.raw_report_text + "\n").encode("utf-8")
                )
                transport_operations = snapshot.transport_normalization_operations
                source = "DIRECT_REPORT_DOM_NORMALIZED"
            else:
                source = "DIRECT_REPORT_DOM"
            downloaded_filename = None
            attachment_key = None
        expected_pdf = Path(selected_filename).with_suffix(".pdf").name
        matching_pdf = [
            (key, locator)
            for key, locator in await self._new_pdf_candidates(
                assistant_turn_id=snapshot.assistant_turn_id,
            )
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
            raw_report_md_part_path=raw_part_path,
            transport_normalization_operations=transport_operations,
        )

    async def _download_schema_matched_dossier_json(
        self,
        *,
        candidates: list[tuple[AttachmentKey, Any]],
        assistant_turn_id: str | None,
        part_path: Path,
        job_id: str,
        run_id: str,
    ) -> tuple[AttachmentKey, str, dict[str, Any]]:
        """Select a generated dossier by content, never by a filename guess.

        A Pro response can expose both the dossier and a validation receipt as
        JSON attachments.  Each candidate is downloaded through the visible UI
        and remains non-authoritative until its canonical dossier schema and
        exact durable job/run identity match.  No composer or send action is
        involved.
        """

        candidate_keys = tuple(key for key, _locator in candidates)
        schema_identity_mismatch_seen = False
        for index, expected_key in enumerate(candidate_keys):
            current_candidates = await self._new_json_candidates(
                assistant_turn_id=assistant_turn_id,
            )
            current = next(
                (
                    (key, locator)
                    for key, locator in current_candidates
                    if key.stable_key == expected_key.stable_key
                ),
                None,
            )
            if current is None:
                raise BrowserUIIncompatible(
                    "JSON attachment candidate changed during schema-bound capture"
                )
            key, locator = current
            download = await self._download_from_candidate(locator)
            suggested = str(download.suggested_filename or "").strip()
            if (
                Path(suggested).name != suggested
                or not suggested.casefold().endswith(".json")
                or suggested != key.button_text.strip()
            ):
                raise BrowserUIIncompatible(
                    "downloaded JSON candidate filename differs from its visible attachment"
                )
            candidate_path = part_path.with_name(
                f"{part_path.name}.candidate-{index}.json"
            )
            await download.save_as(str(candidate_path))
            try:
                payload = json.loads(candidate_path.read_text(encoding="utf-8-sig"))
            except (UnicodeDecodeError, json.JSONDecodeError):
                candidate_path.unlink(missing_ok=True)
                payload = None
            if isinstance(payload, dict) and (
                payload.get("schema_version") == "e2r_pro_research_dossier_v3"
            ):
                if (
                    str(payload.get("job_id") or "") == job_id
                    and str(payload.get("run_id") or "") == run_id
                ):
                    candidate_path.replace(part_path)
                    return key, suggested, payload
                schema_identity_mismatch_seen = True
            candidate_path.unlink(missing_ok=True)
            if await first_visible(self.page, PREVIEW_CLOSE_SELECTORS) is not None:
                await self._dismiss_visible_file_preview()
        if schema_identity_mismatch_seen:
            raise BrowserUIIncompatible(
                "downloaded JSON report job/run identity differs from the capture request"
            )
        raise BrowserUIIncompatible(
            "no generated JSON attachment matched the ResearchDossierV3 schema and exact job/run identity"
        )

    async def download_json_attachment_without_submit(
        self,
        request: BrowserJsonAttachmentRequest,
    ) -> RawBrowserJsonAttachment:
        """Download one exact visible JSON artifact without touching composer/send.

        The durable capture already binds the conversation and assistant turn.
        A JSON link elsewhere in the report (for example a schema URL) or in an
        older turn therefore cannot be mistaken for the requested dossier.
        """

        current_conversation = self.conversation_id()
        if current_conversation != request.conversation_id:
            raise BrowserUIIncompatible(
                "visible conversation differs from JSON attachment recovery identity"
            )
        expected = Path(request.expected_filename).name
        if expected != request.expected_filename or not expected.casefold().endswith(
            ".json"
        ):
            raise BrowserUIIncompatible(
                "expected JSON attachment filename must be one safe basename"
            )
        matching = [
            (key, locator)
            for key, locator in await self._new_json_candidates(
                assistant_turn_id=request.assistant_turn_id,
            )
            if key.button_text == expected
            and key.conversation_id == request.conversation_id
            and key.turn_id == request.assistant_turn_id
        ]
        if len(matching) != 1:
            raise BrowserUIIncompatible(
                "exactly one same-turn JSON dossier attachment is required"
            )
        key, locator = matching[0]
        request.staging_directory.mkdir(parents=True, exist_ok=True)
        part_path = request.staging_directory / "expanded_research_dossier.json.part"
        download = await self._download_from_candidate(locator)
        suggested = str(download.suggested_filename or "").strip()
        if suggested != expected:
            raise BrowserUIIncompatible(
                f"downloaded JSON filename mismatch: expected {expected}, got {suggested}"
            )
        await download.save_as(str(part_path))
        if not part_path.is_file() or part_path.stat().st_size == 0:
            raise BrowserUIIncompatible(
                "Playwright download produced an empty JSON dossier"
            )
        try:
            payload = json.loads(part_path.read_text(encoding="utf-8-sig"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            part_path.unlink(missing_ok=True)
            raise BrowserUIIncompatible(
                "downloaded JSON dossier is not a UTF-8 JSON document"
            ) from error
        if not isinstance(payload, dict):
            part_path.unlink(missing_ok=True)
            raise BrowserUIIncompatible(
                "downloaded JSON dossier must be a JSON object"
            )
        return RawBrowserJsonAttachment(
            conversation_id=request.conversation_id,
            assistant_turn_id=request.assistant_turn_id,
            json_part_path=part_path,
            downloaded_filename=suggested,
            attachment_key=key,
        )

    @staticmethod
    async def _visible_citation_registry(turn: Any) -> tuple[dict[str, str], ...]:
        rows = await turn.locator("a[href]").evaluate_all(
            r"""elements => elements.map(element => ({
                url: element.href || element.getAttribute('href') || '',
                text: (element.innerText || '').trim(),
                aria_label: element.getAttribute('aria-label') || '',
                title: element.getAttribute('title') || ''
            })).filter(row => /^https?:\/\//i.test(row.url))"""
        )
        registry: list[dict[str, str]] = []
        seen: set[tuple[str, str, str, str]] = set()
        for row in rows:
            normalized = {
                key: " ".join(str(row.get(key) or "").split())
                for key in ("url", "text", "aria_label", "title")
            }
            key = tuple(normalized[name] for name in ("url", "text", "aria_label", "title"))
            if key in seen:
                continue
            seen.add(key)
            registry.append(normalized)
        return tuple(registry)

    async def snapshot_attachment_keys(self) -> tuple[AttachmentKey, ...]:
        keys: list[AttachmentKey] = []
        conversation_id = self.conversation_id()
        for selector in (
            *MD_CANDIDATE_SELECTORS,
            *PDF_CANDIDATE_SELECTORS,
            *JSON_CANDIDATE_SELECTORS,
        ):
            locator = self.page.locator(selector)
            for index in range(await locator.count()):
                item = locator.nth(index)
                if not await item.is_visible():
                    continue
                text = await self._attachment_candidate_name(item)
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

    async def _new_md_candidates(
        self,
        *,
        assistant_turn_id: str | None = None,
    ) -> list[tuple[AttachmentKey, Any]]:
        return await self._new_file_candidates(
            MD_CANDIDATE_SELECTORS,
            assistant_turn_id=assistant_turn_id,
        )

    async def _new_pdf_candidates(
        self,
        *,
        assistant_turn_id: str | None = None,
    ) -> list[tuple[AttachmentKey, Any]]:
        return await self._new_file_candidates(
            PDF_CANDIDATE_SELECTORS,
            assistant_turn_id=assistant_turn_id,
        )

    async def _new_json_candidates(
        self,
        *,
        assistant_turn_id: str | None = None,
    ) -> list[tuple[AttachmentKey, Any]]:
        return await self._new_file_candidates(
            JSON_CANDIDATE_SELECTORS,
            assistant_turn_id=assistant_turn_id,
        )

    async def _new_file_candidates(
        self,
        selectors: tuple[str, ...],
        *,
        assistant_turn_id: str | None = None,
    ) -> list[tuple[AttachmentKey, Any]]:
        candidates: list[tuple[AttachmentKey, Any]] = []
        seen: set[str] = set()
        for selector in selectors:
            locator = self.page.locator(selector)
            for index in range(await locator.count()):
                item = locator.nth(index)
                if not await item.is_visible():
                    continue
                turn_id = await self._turn_id(item)
                if assistant_turn_id is not None and turn_id != assistant_turn_id:
                    continue
                key = AttachmentKey(
                    self.conversation_id(),
                    turn_id,
                    await self._attachment_candidate_name(item),
                )
                if key.stable_key in self._preexisting_attachment_keys or key.stable_key in seen:
                    continue
                seen.add(key.stable_key)
                candidates.append((key, item))
        return candidates

    @staticmethod
    async def _attachment_candidate_name(candidate: Any) -> str:
        values = [
            await candidate.get_attribute("aria-label"),
            await candidate.get_attribute("title"),
            await candidate.get_attribute("download"),
            (await candidate.inner_text()).strip(),
        ]
        for value in values:
            for line in str(value or "").splitlines():
                normalized = line.strip()
                if re.search(r"\.(?:md|pdf|json)$", normalized, re.IGNORECASE):
                    return normalized
        return str(values[-1] or "").strip()

    async def _download_from_candidate(self, candidate: Any) -> Any:
        # A prior interrupted capture can leave the same file's fullscreen
        # preview over the conversation.  Close only a filename-labelled file
        # preview here and keep the exact public conversation loaded.
        if await first_visible(self.page, PREVIEW_CLOSE_SELECTORS) is not None:
            await self._dismiss_visible_file_preview(reload_after_close=False)

        # Current ChatGPT artifact rows expose two different controls: the
        # filename opens a preview, while a sibling aria-labelled control
        # performs the actual download.  Bind that control to the candidate's
        # *nearest* containing row so a neighbouring validation JSON (or an
        # unrelated old turn) cannot be downloaded by mistake.
        direct_control = await self._direct_download_control(candidate)
        if direct_control is not None:
            try:
                return await self._click_direct_download_or_capture_fetch(
                    control=direct_control,
                    candidate=candidate,
                )
            except Exception as error:
                if isinstance(error, BrowserUIIncompatible):
                    raise
                raise BrowserUIIncompatible(
                    "artifact-row direct download was not observed by Playwright"
                ) from error

        try:
            async with self.page.expect_download(timeout=1_000) as download_info:
                await candidate.click()
            return await download_info.value
        except Exception as direct_error:
            download_control = None
            preview_seen = False
            for attempt in range(50):
                for preview_selector in PREVIEW_ROOT_SELECTORS:
                    previews = self.page.locator(preview_selector)
                    for preview_index in range(await previews.count()):
                        preview = previews.nth(preview_index)
                        if not await preview.is_visible():
                            continue
                        preview_seen = True
                        for selector in DOWNLOAD_SELECTORS:
                            matches = preview.locator(selector)
                            for index in range(await matches.count()):
                                item = matches.nth(index)
                                if (
                                    not await item.is_visible()
                                    or not await item.is_enabled()
                                ):
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
                                if (
                                    "앱 다운로드" in label
                                    or "download app" in label
                                ):
                                    continue
                                download_control = item
                                break
                            if download_control is not None:
                                break
                        if download_control is not None:
                            break
                    if download_control is not None:
                        break
                if download_control is not None:
                    break
                if attempt < 49:
                    await self.page.wait_for_timeout(100)
            if download_control is None:
                if not preview_seen:
                    raise BrowserUIIncompatible(
                        "file candidate produced neither a Playwright download nor a preview"
                    ) from direct_error
                raise BrowserUIIncompatible("preview has no enabled real download control")
            try:
                async with self.page.expect_download(timeout=10_000) as download_info:
                    await download_control.click()
                return await download_info.value
            except Exception as error:
                raise BrowserUIIncompatible("preview download was not observed by Playwright") from error

    async def _direct_download_control(self, candidate: Any) -> Any | None:
        """Find one download control scoped to the candidate's nearest row."""

        labelled_download = (
            './/button[contains(@aria-label, "파일 다운로드") '
            'or contains(translate(@aria-label, '
            '"ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), '
            '"download file")] '
            '| .//a[contains(@aria-label, "파일 다운로드") '
            'or contains(translate(@aria-label, '
            '"ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), '
            '"download file")]'
        )
        container = candidate.locator(
            "xpath=ancestor::*[" + labelled_download + "][1]"
        )
        if await container.count() != 1:
            return None
        # ``ancestor::*`` can otherwise escape an artifact row and bind a
        # candidate to a stale preview's download control through BODY.  That
        # is especially dangerous when an MD preview is still mounted while
        # the next PDF attachment is selected.  A direct control is accepted
        # only from a local row-like container, never from the whole page or
        # the whole assistant turn.
        if await container.evaluate(
            """element => {
                const tag = element.tagName.toLowerCase();
                return tag === 'html' || tag === 'body'
                    || element.matches(
                        'article, section[data-turn], '
                        + '[data-message-author-role], [data-message-id], [data-turn-id]'
                    );
            }"""
        ):
            return None
        controls = container.locator("xpath=" + labelled_download)
        enabled: list[Any] = []
        for index in range(await controls.count()):
            item = controls.nth(index)
            if await item.is_visible() and await item.is_enabled():
                enabled.append(item)
        if len(enabled) != 1:
            return None
        control = enabled[0]
        expected_filename = await self._attachment_candidate_name(candidate)
        control_download = str(
            await control.get_attribute("download") or ""
        ).strip()
        if control_download and control_download != expected_filename:
            return None

        # The local container may have several attachment rows but only one
        # visible download control.  Refuse that ambiguous binding as well.
        # The broad locator is intentionally de-duplicated by the browser and
        # direct controls are excluded from the filename roster.
        visible_filenames: set[str] = set()
        row_items = container.locator(
            'button, a, [data-testid*="behavior-btn"], .entity-underline'
        )
        for index in range(await row_items.count()):
            item = row_items.nth(index)
            if not await item.is_visible():
                continue
            aria_label = str(
                await item.get_attribute("aria-label") or ""
            ).casefold()
            if "파일 다운로드" in aria_label or "download file" in aria_label:
                continue
            filename = await self._attachment_candidate_name(item)
            if re.search(r"\.(?:md|pdf|json)$", filename, re.IGNORECASE):
                visible_filenames.add(filename)
        if visible_filenames != {expected_filename}:
            return None
        return control

    async def _click_direct_download_or_capture_fetch(
        self,
        *,
        control: Any,
        candidate: Any,
    ) -> Any:
        """Capture either a browser download or ChatGPT's authenticated fetch.

        The current public UI downloads generated artifacts with ``fetch`` and
        therefore emits a normal network response instead of Playwright's
        ``download`` event.  Both paths still start with the user-visible file
        card control.  The response path is accepted only when its sandbox
        basename exactly matches this candidate in this conversation.
        """

        expected_filename = await self._attachment_candidate_name(candidate)
        if Path(expected_filename).name != expected_filename:
            raise BrowserUIIncompatible(
                "artifact-row candidate filename must be one safe basename"
            )

        def url_matches(url: str) -> bool:
            parsed = urlsplit(url)
            page_origin = urlsplit(str(self.page.url or ""))
            if (
                parsed.scheme.casefold() != page_origin.scheme.casefold()
                or parsed.netloc.casefold() != page_origin.netloc.casefold()
                or not parsed.path.endswith("/interpreter/download")
            ):
                return False
            values = parse_qs(parsed.query).get("sandbox_path", ())
            return len(values) == 1 and PurePosixPath(
                unquote(str(values[0]))
            ).name == expected_filename

        def response_matches(response: Any) -> bool:
            return url_matches(str(response.url or ""))

        cdp_session = None
        cdp_queue: asyncio.Queue[Mapping[str, Any]] | None = None
        try:
            cdp_session = await self.page.context.new_cdp_session(self.page)
            cdp_queue = asyncio.Queue()

            def observe_cdp_response(params: Mapping[str, Any]) -> None:
                response = params.get("response")
                if not isinstance(response, Mapping):
                    return
                if url_matches(str(response.get("url") or "")):
                    cdp_queue.put_nowait(params)

            cdp_session.on("Network.responseReceived", observe_cdp_response)
            await cdp_session.send("Network.enable")
        except Exception:
            if cdp_session is not None:
                try:
                    await cdp_session.detach()
                except Exception:
                    pass
            cdp_session = None
            cdp_queue = None

        download_task = asyncio.create_task(
            self.page.wait_for_event("download", timeout=10_000)
        )
        response_task = asyncio.create_task(
            self.page.wait_for_event(
                "response",
                predicate=response_matches,
                timeout=10_000,
            )
        )
        cdp_task = (
            asyncio.create_task(asyncio.wait_for(cdp_queue.get(), timeout=10))
            if cdp_queue is not None
            else None
        )
        tasks = {download_task, response_task}
        if cdp_task is not None:
            tasks.add(cdp_task)
        try:
            # ChatGPT renders this control inside a hover-only wrapper.  A
            # coordinate click can make React replace the hovered node between
            # hit-testing and dispatch, producing no request and no error.
            # Dispatch the native click on the already exact, enabled control.
            await control.evaluate("element => element.click()")
            done, _pending = await asyncio.wait(
                tasks,
                return_when=asyncio.FIRST_COMPLETED,
            )
            successful = [
                task for task in done if not task.cancelled() and task.exception() is None
            ]
            if not successful:
                # The first waiter can fail before the other succeeds.  Keep
                # the shared ten-second boundary rather than treating one
                # missing transport surface as the final result.
                done, _pending = await asyncio.wait(tasks)
                successful = [
                    task
                    for task in done
                    if not task.cancelled() and task.exception() is None
                ]
            # CDP publishes ``Network.responseReceived`` before the response
            # body is always readable.  Give the normal Playwright download
            # or response surface a short chance to finish before asking CDP
            # for the body.  This removes a scheduler-dependent race without
            # weakening the exact URL/filename checks below.
            if (
                cdp_task is not None
                and cdp_task in successful
                and download_task not in successful
                and response_task not in successful
            ):
                primary_pending = {
                    task
                    for task in (download_task, response_task)
                    if not task.done()
                }
                if primary_pending:
                    primary_done, _still_pending = await asyncio.wait(
                        primary_pending,
                        timeout=0.25,
                        return_when=asyncio.FIRST_COMPLETED,
                    )
                    successful.extend(
                        task
                        for task in primary_done
                        if not task.cancelled() and task.exception() is None
                    )
            if download_task in successful:
                return download_task.result()
            if response_task in successful:
                response = response_task.result()
                return await self._validated_response_download(
                    expected_filename=expected_filename,
                    status=int(response.status),
                    content=await response.body(),
                )
            if cdp_task is not None and cdp_task in successful:
                if cdp_session is None:
                    raise BrowserUIIncompatible(
                        "artifact CDP response lost its observing session"
                    )
                params = cdp_task.result()
                response = params.get("response")
                if not isinstance(response, Mapping):
                    raise BrowserUIIncompatible(
                        "artifact CDP response metadata is malformed"
                    )
                try:
                    body_result = await cdp_session.send(
                        "Network.getResponseBody",
                        {"requestId": str(params.get("requestId") or "")},
                    )
                except Exception as cdp_body_error:
                    # On some Chromium/Python schedules the CDP event wins the
                    # race but getResponseBody is still premature.  Wait for
                    # the already-armed public response/download observers;
                    # do not click again and do not accept a different URL.
                    primary_pending = {
                        task
                        for task in (download_task, response_task)
                        if not task.done()
                    }
                    if primary_pending:
                        await asyncio.wait(primary_pending)
                    if (
                        not download_task.cancelled()
                        and download_task.exception() is None
                    ):
                        return download_task.result()
                    if (
                        not response_task.cancelled()
                        and response_task.exception() is None
                    ):
                        fallback_response = response_task.result()
                        return await self._validated_response_download(
                            expected_filename=expected_filename,
                            status=int(fallback_response.status),
                            content=await fallback_response.body(),
                        )
                    raise BrowserUIIncompatible(
                        "artifact fetch body was unavailable on every observed transport"
                    ) from cdp_body_error
                raw_body = str(body_result.get("body") or "")
                content = (
                    base64.b64decode(raw_body)
                    if body_result.get("base64Encoded") is True
                    else raw_body.encode("utf-8")
                )
                return await self._validated_response_download(
                    expected_filename=expected_filename,
                    status=int(response.get("status") or 0),
                    content=content,
                )
            raise BrowserUIIncompatible(
                "artifact-row direct control produced neither a download nor an exact artifact fetch"
            )
        finally:
            for task in tasks:
                if not task.done():
                    task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
            if cdp_session is not None:
                try:
                    await cdp_session.detach()
                except Exception:
                    pass

    async def _validated_response_download(
        self,
        *,
        expected_filename: str,
        status: int,
        content: bytes,
        allow_download_manifest: bool = True,
    ) -> _ResponseBackedDownload:
        if status != 200:
            raise BrowserUIIncompatible(
                "artifact fetch response did not return HTTP 200"
            )
        if not content:
            raise BrowserUIIncompatible(
                "artifact fetch response returned an empty body"
            )
        try:
            error_payload = json.loads(content.decode("utf-8-sig"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            error_payload = None
        if (
            isinstance(error_payload, Mapping)
            and error_payload.get("status") == "error"
            and error_payload.get("error_code") == "file_not_found"
        ):
            raise BrowserArtifactUnavailable(
                "visible ChatGPT artifact has no backing sandbox file: "
                f"{expected_filename}"
            )
        if (
            allow_download_manifest
            and isinstance(error_payload, Mapping)
            and error_payload.get("status") == "success"
            and isinstance(error_payload.get("download_url"), str)
        ):
            manifest_filename = str(error_payload.get("file_name") or "")
            metadata = error_payload.get("metadata")
            file_id = (
                str(metadata.get("file_id") or "")
                if isinstance(metadata, Mapping)
                else ""
            )
            download_url = str(error_payload["download_url"])
            parsed = urlsplit(download_url)
            page_origin = urlsplit(str(self.page.url or ""))
            query = parse_qs(parsed.query)
            if (
                manifest_filename != expected_filename
                or parsed.scheme.casefold() != page_origin.scheme.casefold()
                or parsed.netloc.casefold() != page_origin.netloc.casefold()
                or parsed.path != "/backend-api/estuary/content"
                or query.get("fn") != [expected_filename]
                or not file_id
                or query.get("id") != [file_id]
            ):
                raise BrowserUIIncompatible(
                    "artifact download manifest is not bound to the exact visible file"
                )
            response = await self.page.context.request.get(
                download_url,
                timeout=10_000,
            )
            return await self._validated_response_download(
                expected_filename=expected_filename,
                status=int(response.status),
                content=await response.body(),
                allow_download_manifest=False,
            )
        if (
            not allow_download_manifest
            and isinstance(error_payload, Mapping)
            and error_payload.get("status") == "success"
            and "download_url" in error_payload
        ):
            raise BrowserUIIncompatible(
                "artifact content endpoint returned another download manifest"
            )
        return _ResponseBackedDownload(
            suggested_filename=expected_filename,
            content=content,
        )

    async def _assistant_turns(self) -> list[Any]:
        """Return unique assistant turns in document order.

        ChatGPT can render both a top-level assistant section and a nested
        message-role element for one completed response.  Concatenating one
        selector at a time can place an older nested response after the newest
        top-level thinking card.  The CSS union keeps DOM order, and nested
        matches are normalized to their top-level assistant section.
        """

        turns: list[Any] = []
        seen: set[str] = set()
        locator = self.page.locator(", ".join(ASSISTANT_TURN_SELECTORS))
        for index in range(await locator.count()):
            item = locator.nth(index)
            if not await item.is_visible():
                continue
            section = item.locator(
                "xpath=ancestor-or-self::section[@data-turn='assistant'][1]"
            )
            if await section.count():
                item = section
            identity = await item.evaluate(
                r"""element => {
                    const direct = element.getAttribute('data-message-id')
                        || element.getAttribute('data-turn-id');
                    if (direct) return direct;
                    if (element.matches('section[data-turn="assistant"]')) {
                        return `assistant-section-${Array.from(
                            document.querySelectorAll(
                                'section[data-turn="assistant"]'
                            )
                        ).indexOf(element)}`;
                    }
                    return element.getAttribute('data-testid')
                        || element.outerHTML.slice(0, 200);
                }"""
            )
            if identity in seen:
                continue
            seen.add(identity)
            turns.append(item)
        return turns

    async def _latest_assistant_turn_snapshot(
        self,
    ) -> Mapping[str, Any] | None:
        """Read the newest assistant turn in one atomic browser evaluation.

        ChatGPT can replace the hydrated conversation DOM while a response is
        finishing.  A ``count()`` followed by ``nth(index)`` can therefore
        point past the newly rendered list and wait for a node that will never
        exist.  This helper resolves the ordered turn, its identity, visible
        text, controls, and citations inside one JavaScript task.  A bounded
        retry only covers a full document navigation that destroys that task's
        execution context; it never submits or clicks anything.
        """

        selector = ", ".join(ASSISTANT_TURN_SELECTORS)
        last_error: Exception | None = None
        for attempt in range(10):
            try:
                snapshot = await self.page.evaluate(
                    r"""selector => {
                        const matches = Array.from(
                            document.querySelectorAll(selector)
                        );
                        const turns = [];
                        const seen = new Set();
                        for (const match of matches) {
                            const turn = match.closest(
                                'section[data-turn="assistant"]'
                            ) || match;
                            if (seen.has(turn)) continue;
                            seen.add(turn);
                            const style = window.getComputedStyle(turn);
                            const visible = turn.isConnected
                                && style.display !== 'none'
                                && style.visibility !== 'hidden'
                                && (turn.getClientRects().length > 0
                                    || turn.offsetWidth > 0
                                    || turn.offsetHeight > 0);
                            if (visible) turns.push(turn);
                        }
                        const element = turns.at(-1);
                        if (!element) return null;
                        const identified = element.closest(
                            '[data-message-id], [data-turn-id]'
                        ) || element.querySelector(
                            '[data-message-id], [data-turn-id]'
                        );
                        const anchors = Array.from(
                            element.querySelectorAll('a[href]')
                        ).map(node => ({
                            url: node.href || node.getAttribute('href') || '',
                            text: (node.innerText || '').trim(),
                            aria_label: node.getAttribute('aria-label') || '',
                            title: node.getAttribute('title') || ''
                        })).filter(row => /^https?:\/\//i.test(row.url));
                        const buttonTexts = Array.from(
                            element.querySelectorAll('button')
                        ).map(node => (node.innerText || '').trim());
                        const labelledCitation = Boolean(
                            element.querySelector(
                                '[data-testid*="citation"], '
                                + '[data-testid*="source"]'
                            )
                        ) || buttonTexts.some(value => {
                            const text = value.toLowerCase();
                            return text === 'sources' || text === '출처';
                        });
                        return {
                            raw_text: (element.innerText || '').trim(),
                            turn_id: identified
                                ? (identified.getAttribute('data-message-id')
                                    || identified.getAttribute('data-turn-id'))
                                : null,
                            button_texts: buttonTexts,
                            citation_registry: anchors,
                            has_citations: anchors.length > 0 || labelledCitation
                        };
                    }""",
                    selector,
                )
                if snapshot is None:
                    return None
                registry: list[dict[str, str]] = []
                seen_registry: set[tuple[str, str, str, str]] = set()
                for row in snapshot.get("citation_registry") or ():
                    normalized = {
                        key: " ".join(str(row.get(key) or "").split())
                        for key in ("url", "text", "aria_label", "title")
                    }
                    identity = tuple(
                        normalized[key]
                        for key in ("url", "text", "aria_label", "title")
                    )
                    if identity in seen_registry:
                        continue
                    seen_registry.add(identity)
                    registry.append(normalized)
                return {
                    **snapshot,
                    "citation_registry": tuple(registry),
                }
            except Exception as error:
                last_error = error
                if attempt < 9:
                    await self.page.wait_for_timeout(100)
        raise BrowserUIIncompatible(
            "assistant turn DOM remained unstable during atomic snapshot"
        ) from last_error

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
        chat_control = await first_visible(self.page, CHAT_MODE_CONTROL_SELECTORS)
        work_active = await first_visible(self.page, WORK_MODE_ACTIVE_SELECTORS)
        pro_active = await first_visible(self.page, PRO_REASONING_ACTIVE_SELECTORS)
        editor = await first_visible(self.page, EDITOR_SELECTORS)
        legacy_deep_research = await first_visible(
            self.page, DEEP_RESEARCH_ACTIVE_SELECTORS
        )
        if (
            editor is not None
            and pro_active is not None
            and (chat_control is None or chat_active is not None)
            and work_active is None
            and legacy_deep_research is None
        ):
            # ``:has-text`` is deliberately followed by an exact text check so
            # a future button such as ``Upgrade to Pro`` cannot satisfy the
            # production readiness gate.  ``chat_active`` may be absent in the
            # current compact composer; when it exists, the Work exclusion
            # above makes the old two-tab UI equally strict.
            if " ".join((await pro_active.inner_text()).split()) == "Pro":
                return True
        return False

    async def _wait_for_send_ready(self) -> Any | None:
        # ChatGPT can show the uploaded filename before its attachment scan is
        # complete.  During that short interval the visible send button stays
        # disabled, so wait finitely without ever clicking it.
        for attempt in range(1_200):
            send = await first_visible(self.page, SEND_SELECTORS)
            if await locator_enabled(send):
                return send
            if attempt < 1_199:
                await self.page.wait_for_timeout(100)
        return None

    @staticmethod
    async def _editor_exact_text(editor: Any) -> str:
        """Reconstruct the located ProseMirror DOM with exact line boundaries."""

        return await editor.evaluate(
            r"""
            element => {
                const visit = node => {
                    if (node.nodeType === Node.TEXT_NODE) {
                        return node.nodeValue || '';
                    }
                    if (node.nodeType !== Node.ELEMENT_NODE) return '';
                    if (node.tagName === 'BR') return '\n';
                    return Array.from(node.childNodes).map(visit).join('');
                };
                const rows = Array.from(element.childNodes);
                if (
                    rows.length
                    && rows.some(
                        child => child.nodeType === Node.ELEMENT_NODE
                            && (child.tagName === 'P' || child.tagName === 'DIV')
                    )
                    && rows.every(
                        child => child.nodeType === Node.TEXT_NODE
                            || (
                                child.nodeType === Node.ELEMENT_NODE
                                && (child.tagName === 'P' || child.tagName === 'DIV')
                            )
                    )
                ) {
                    return rows.map(row => {
                        // ``innerText`` applies layout whitespace collapsing
                        // and can silently remove indentation from JSON or
                        // Markdown.  ProseMirror already expresses line
                        // boundaries as top-level blocks, so preserve every
                        // character inside a row with ``textContent`` and add
                        // exactly one newline only between rows.
                        const text = row.textContent || '';
                        return text.endsWith('\n') ? text.slice(0, -1) : text;
                    }).join('\n');
                }
                return Array.from(element.childNodes).map(visit).join('');
            }
            """
        )

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

        selected_name = await self._selected_packet_filename_if_hash_matches(
            packet_path,
            packet_hash,
        )
        if selected_name is None:
            return None
        displayed = await self._wait_for_uploaded_filename(packet_path.name)
        if displayed is not None:
            self._uploaded_filename = displayed
            return displayed
        return None

    async def _selected_packet_filename_if_hash_matches(
        self,
        packet_path: Path,
        packet_hash: str,
    ) -> str | None:
        """Read the browser-selected File and require the exact JSON hash."""

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
            return str(selected.get("name") or "")
        return None

    async def _manual_login_required(self) -> bool:
        if "/auth/" in self.page.url:
            return True
        if await first_visible(self.page, LOGIN_INDICATOR_SELECTORS) is not None:
            return True
        body = self._main_document_body()
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

    def _main_document_body(self) -> Any:
        """Select the page body without piercing extension shadow roots.

        Playwright CSS locators pierce open shadow DOM by default. Browser
        extensions can inject a custom element containing another complete
        ``html > body`` tree, so even that CSS selector can violate strict
        mode. Absolute XPath stays in the top-level document tree and selects
        only the operational ChatGPT body.
        """

        return self.page.locator("xpath=/html/body")


__all__ = ["PlaywrightChatGPTWebAdapter"]
