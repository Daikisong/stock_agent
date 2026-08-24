"""Read-only preflight for the logged-in visible ChatGPT Pro browser."""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from e2r.pro_first.browser.worker import ProBrowserWorker
from e2r.pro_first.config import load_pro_first_local_config


async def _run(
    config_path: str,
    screenshot: str | None,
    search_probe: str | None,
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
            "visible_ui_only": True,
            "submit_count": 0,
            "upload_count": 0,
        }
    finally:
        await session.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--screenshot")
    parser.add_argument("--search-probe")
    args = parser.parse_args(argv)
    try:
        payload = asyncio.run(_run(args.config, args.screenshot, args.search_probe))
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
