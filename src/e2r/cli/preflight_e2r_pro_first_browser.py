"""Read-only preflight for the logged-in visible ChatGPT Pro browser."""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
import sys

from e2r.pro_first.browser.worker import ProBrowserWorker
from e2r.pro_first.config import load_pro_first_local_config


async def _run(
    config_path: str,
    screenshot: str | None,
    search_probe: str | None,
    job_id: str | None,
    run_id: str | None,
) -> dict:
    config = load_pro_first_local_config(config_path)
    session = await ProBrowserWorker(config.browser).open(job_id="READ_ONLY_PREFLIGHT")
    try:
        inspection = await session.adapter.ensure_logged_in()
        controls = await session.page.locator("button").evaluate_all(
            """elements => elements.map(element => ({
                text: (element.innerText || '').trim(),
                ariaLabel: element.getAttribute('aria-label'),
                role: element.getAttribute('role'),
                dataState: element.getAttribute('data-state'),
                ariaChecked: element.getAttribute('aria-checked')
            })).filter(row => /^(Chat|Work|Pro|Instant|Thinking|Deep research|채팅|작업|심층 리서치)/i.test(row.text || row.ariaLabel || ''))"""
        )
        recovery_controls = await session.page.locator("button,a,input").evaluate_all(
            """elements => elements.map(element => ({
                tag: element.tagName.toLowerCase(),
                text: (element.innerText || '').trim(),
                ariaLabel: element.getAttribute('aria-label'),
                placeholder: element.getAttribute('placeholder'),
                role: element.getAttribute('role'),
                href: element.getAttribute('href')
            })).filter(row => /(검색|search)/i.test(
                [row.text, row.ariaLabel, row.placeholder].filter(Boolean).join(' ')
            ) || /PROJOB-[A-Za-z0-9-]+/.test(row.text)).map(row => ({
                ...row,
                text: row.text.slice(0, 500)
            }))"""
        )
        search_probe_result = None
        if search_probe:
            search_input = session.page.locator(
                'input[placeholder*="검색"]:visible, '
                'input[placeholder*="Search" i]:visible, '
                '[role="dialog"] input:visible'
            ).first
            if not await search_input.count() or not await search_input.is_visible():
                search_control = session.page.locator('button[aria-label="검색"]:visible').first
                if not await search_control.count():
                    search_control = session.page.locator(
                        'button[aria-label*="Search" i]:visible'
                    ).first
                if not await search_control.count():
                    raise RuntimeError("visible ChatGPT history search control was not found")
                await search_control.click(timeout=5_000)
                await session.page.wait_for_timeout(300)
                search_input = session.page.locator(
                    'input[placeholder*="검색"]:visible, '
                    'input[placeholder*="Search" i]:visible, '
                    '[role="dialog"] input:visible'
                ).first
            if not await search_input.count():
                raise RuntimeError("visible ChatGPT history search input was not found")
            await search_input.fill(search_probe, timeout=5_000)
            await session.page.wait_for_timeout(1_000)
            search_probe_result = await session.page.locator(
                '[role="dialog"], [data-radix-portal]'
            ).evaluate_all(
                """(elements, probe) => ({
                    query: probe,
                    matchingLinks: Array.from(document.querySelectorAll('a[href*="/c/"]'))
                        .filter(link => (link.innerText || '').includes(probe))
                        .map(link => ({
                            href: link.getAttribute('href'),
                            text: (link.innerText || '').trim().slice(0, 500)
                        })),
                    matchingTextCount: elements.filter(
                        element => (element.innerText || '').includes(probe)
                    ).length
                })""",
                search_probe,
            )
        composer_diagnostics = await session.page.locator(
            'button, input[type="file"], [contenteditable="true"], textarea'
        ).evaluate_all(
            """async elements => Promise.all(elements.map(async element => {
                const rect = element.getBoundingClientRect();
                const files = [];
                if (element.tagName === 'INPUT' && element.type === 'file') {
                    for (const file of Array.from(element.files || [])) {
                        let rawSha256 = null;
                        let readError = null;
                        try {
                            const buffer = await file.arrayBuffer();
                            const digest = await crypto.subtle.digest('SHA-256', buffer);
                            rawSha256 = Array.from(new Uint8Array(digest))
                                .map(byte => byte.toString(16).padStart(2, '0')).join('');
                        } catch (error) {
                            readError = `${error.name || 'Error'}: ${error.message || error}`;
                        }
                        files.push({
                            name: file.name,
                            size: file.size,
                            type: file.type,
                            rawSha256,
                            readError,
                        });
                    }
                }
                return {
                    tag: element.tagName.toLowerCase(),
                    id: element.id || null,
                    type: element.getAttribute('type'),
                    text: (element.innerText || '').trim().slice(0, 200),
                    ariaLabel: element.getAttribute('aria-label'),
                    dataTestId: element.getAttribute('data-testid'),
                    disabled: element.disabled === true,
                    ariaDisabled: element.getAttribute('aria-disabled'),
                    contentEditable: element.getAttribute('contenteditable'),
                    visible: rect.width > 0 && rect.height > 0,
                    x: Math.round(rect.x),
                    y: Math.round(rect.y),
                    width: Math.round(rect.width),
                    height: Math.round(rect.height),
                    files,
                    editorChars: element.getAttribute('contenteditable') === 'true'
                        ? (element.innerText || '').length
                        : null,
                };
            })).then(rows => rows.filter(
                row => row.visible || row.files.length || row.editorChars
            ))"""
        )
        visible_alerts = await session.page.locator(
            '[role="alert"], [data-sonner-toast], [data-testid*="toast"]'
        ).evaluate_all(
            """elements => elements.map(element => ({
                text: (element.innerText || '').trim().slice(0, 1000),
                ariaLabel: element.getAttribute('aria-label'),
                dataTestId: element.getAttribute('data-testid'),
            })).filter(row => row.text || row.ariaLabel)"""
        )
        result_diagnostics = None
        if job_id and run_id:
            result = await session.adapter.inspect_result(
                job_id=job_id,
                run_id=run_id,
            )
            result_diagnostics = {
                "conversation_id": result.conversation_id,
                "assistant_turn_id": result.assistant_turn_id,
                "report_char_count": len(result.report_text),
                "report_hash": result.report_hash,
                "raw_report_char_count": len(result.raw_report_text or ""),
                "raw_report_hash": result.raw_report_hash,
                "has_citations": result.has_citations,
                "has_dossier_marker": result.has_dossier_marker,
                "has_repair_delta_marker": result.has_repair_delta_marker,
                "job_marker_matches": result.job_marker_matches,
                "run_marker_matches": result.run_marker_matches,
                "new_attachment_count": len(result.new_attachment_keys),
                "structurally_complete": result.structurally_complete,
                "transport_normalization_operations": list(
                    result.transport_normalization_operations
                ),
            }
        if screenshot:
            path = Path(screenshot).expanduser().resolve()
            path.parent.mkdir(parents=True, exist_ok=True)
            await session.page.screenshot(path=str(path), full_page=False)
        try:
            mode = await session.adapter.ensure_deep_research_mode()
        except Exception as error:
            return {
                "schema_version": "e2r_pro_first_browser_preflight_v1",
                "status": "PENDING",
                "attach_ok": True,
                "editor_present": inspection.editor_ready,
                "login_required": False,
                "pro_mode_ready": False,
                "mode_controls": controls,
                "recovery_controls": recovery_controls,
                "search_probe": search_probe_result,
                "composer_diagnostics": composer_diagnostics,
                "visible_alerts": visible_alerts,
                "result_diagnostics": result_diagnostics,
                "error_class": type(error).__name__,
                "error_message": str(error),
                "visible_ui_only": True,
                "submit_count": 0,
                "upload_count": 0,
            }
        return {
            "schema_version": "e2r_pro_first_browser_preflight_v1",
            "status": "PASS",
            "attach_ok": True,
            "editor_present": inspection.editor_ready,
            "login_required": False,
            "pro_mode_ready": mode.deep_research_ready,
            "mode_controls": controls,
            "recovery_controls": recovery_controls,
            "search_probe": search_probe_result,
            "composer_diagnostics": composer_diagnostics,
            "visible_alerts": visible_alerts,
            "result_diagnostics": result_diagnostics,
            "visible_ui_only": True,
            "submit_count": 0,
            "upload_count": 0,
        }
    finally:
        await session.close()


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--screenshot")
    parser.add_argument("--search-probe")
    parser.add_argument("--job-id")
    parser.add_argument("--run-id")
    args = parser.parse_args(argv)
    if bool(args.job_id) != bool(args.run_id):
        parser.error("--job-id and --run-id must be provided together")
    try:
        payload = asyncio.run(
            _run(
                args.config,
                args.screenshot,
                args.search_probe,
                args.job_id,
                args.run_id,
            )
        )
    except Exception as error:
        payload = {
            "schema_version": "e2r_pro_first_browser_preflight_v1",
            "status": "PENDING",
            "attach_ok": False,
            "error_class": type(error).__name__,
            "error_message": str(error),
            "submit_count": 0,
            "upload_count": 0,
        }
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if payload["status"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
