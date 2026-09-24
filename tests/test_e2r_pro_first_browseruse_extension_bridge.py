from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from e2r.pro_first.browser.browseruse_extension_bridge import (
    BROWSERUSE_PACKET_ATTACH_RPC_TIMEOUT_SECONDS,
    BrowserUseBridgeClient,
    BrowserUseBridgeError,
    BrowserUsePage,
    validate_bridge_endpoint,
)
from e2r.pro_first.browser.chatgpt_adapter import PlaywrightChatGPTWebAdapter
from e2r.pro_first.browser.protocol import BrowserUIIncompatible
from e2r.pro_first.browser.worker import ProBrowserWorker
from e2r.pro_first.config import BrowserConnectionMode, ProBrowserConfig
from e2r.pro_first.browser.selector_registry import (
    ATTACH_BUTTON_SELECTORS,
    UPLOAD_MENU_ITEM_SELECTORS,
)


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

    async def test_packet_attach_rpc_budget_exceeds_native_file_chooser_wait(self) -> None:
        client = BrowserUseBridgeClient(
            endpoint="http://127.0.0.1:12345",
            token="x" * 48,
        )
        client.session_id = "BROWSERUSE-test-session"
        client._request = AsyncMock(  # type: ignore[method-assign]
            return_value={
                "value": {"selected": True, "filename": "research_packet.json"},
                "page_url": "https://chatgpt.com/",
            }
        )

        await BrowserUsePage(client).upload_file_via_existing_user_session(
            "/tmp/research_packet.json",
            attach_selectors=("button[aria-label='Attach files']",),
            upload_menu_selectors=("[role='menuitem']:has-text('Upload files')",),
        )

        request = client._request.await_args
        self.assertEqual(
            request.kwargs["timeout_seconds"],
            BROWSERUSE_PACKET_ATTACH_RPC_TIMEOUT_SECONDS,
        )
        self.assertNotIn(
            "request_timeout_seconds",
            request.args[1]["arguments"],
        )
        self.assertEqual(
            request.args[1]["arguments"]["upload_menu_selectors"],
            ["[role='menuitem']:has-text('Upload files')"],
        )

        node = shutil.which("node")
        self.assertIsNotNone(node)
        bridge_path = (
            Path(__file__).parents[1]
            / "src/e2r/pro_first/browser/browseruse_extension_bridge.mjs"
        ).resolve()
        script = f"""
import assert from "node:assert/strict";
import {{ BROWSERUSE_NATIVE_FILE_CHOOSER_TIMEOUT_MS }} from {json.dumps(bridge_path.as_uri())};
assert.equal(BROWSERUSE_NATIVE_FILE_CHOOSER_TIMEOUT_MS, 45000);
assert.ok({BROWSERUSE_PACKET_ATTACH_RPC_TIMEOUT_SECONDS * 1000} > BROWSERUSE_NATIVE_FILE_CHOOSER_TIMEOUT_MS);
"""
        completed = subprocess.run(
            [str(node), "--input-type=module", "--eval", script],
            cwd=Path(__file__).parents[1],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)

    def test_packet_attach_menu_is_state_aware_and_fails_closed(self) -> None:
        node = shutil.which("node")
        self.assertIsNotNone(node)
        bridge_path = (
            Path(__file__).parents[1]
            / "src/e2r/pro_first/browser/browseruse_extension_bridge.mjs"
        ).resolve()
        script = f"""
import assert from "node:assert/strict";
import {{ prepareVisiblePacketUpload, assignPacketThroughBrowserUseFileChooser }} from {json.dumps(bridge_path.as_uri())};

class Locator {{
  constructor({{ present = true, expanded = null, hasPopup = null }} = {{}}) {{
    this.present = present;
    this.expanded = expanded;
    this.hasPopup = hasPopup;
    this.first = this;
    this.clicks = 0;
    this.onClick = null;
  }}
  async count() {{ return this.present ? 1 : 0; }}
  async evaluateAll() {{ return this.present ? 1 : 0; }}
  async evaluate() {{ return this.present; }}
  async getAttribute(name) {{
    if (name === "aria-expanded") return this.expanded;
    if (name === "aria-haspopup") return this.hasPopup;
    return null;
  }}
  async click() {{ this.clicks += 1; if (this.onClick) await this.onClick(); }}
}}
function pageFor(attach, upload) {{
  return {{
    locator(selector) {{
      if (selector === "attach") return attach;
      if (selector === "upload") return upload;
      throw new Error("unexpected selector: " + selector);
    }},
    async waitForTimeout() {{ return; }},
  }};
}}

// An already expanded menu is reused; clicking the toggle again would close it.
const expandedAttach = new Locator({{ expanded: "true" }});
const expandedUpload = new Locator();
const expandedOrder = [];
expandedUpload.onClick = async () => expandedOrder.push("upload-click");
await prepareVisiblePacketUpload({{
  playwright: pageFor(expandedAttach, expandedUpload),
  attachSelectors: ["attach"],
  uploadMenuSelectors: ["upload"],
  beforeChooserTrigger: () => expandedOrder.push("arm-filechooser"),
}});
assert.equal(expandedAttach.clicks, 0);
assert.equal(expandedUpload.clicks, 1);
assert.deepEqual(expandedOrder, ["arm-filechooser", "upload-click"]);

// A collapsed control is opened once, then its visible upload item is selected.
let expanded = "false";
const collapsedAttach = new Locator({{ expanded, hasPopup: "menu" }});
const collapsedOrder = [];
collapsedAttach.onClick = async () => {{ collapsedOrder.push("attach-click"); expanded = "true"; collapsedAttach.expanded = expanded; }};
const collapsedUpload = new Locator();
collapsedUpload.onClick = async () => collapsedOrder.push("upload-click");
await prepareVisiblePacketUpload({{
  playwright: pageFor(collapsedAttach, collapsedUpload),
  attachSelectors: ["attach"],
  uploadMenuSelectors: ["upload"],
  beforeChooserTrigger: () => collapsedOrder.push("arm-filechooser"),
}});
assert.equal(collapsedAttach.clicks, 1);
assert.equal(collapsedUpload.clicks, 1);
assert.deepEqual(collapsedOrder, ["attach-click", "arm-filechooser", "upload-click"]);

// An expanded but unrecognized menu must stop before native chooser selection.
const unknownAttach = new Locator({{ expanded: "true" }});
const missingUpload = new Locator({{ present: false }});
await assert.rejects(
  prepareVisiblePacketUpload({{
    playwright: pageFor(unknownAttach, missingUpload),
    attachSelectors: ["attach"],
    uploadMenuSelectors: ["upload"],
  }}),
  /no recognized visible file-upload action/,
);
assert.equal(unknownAttach.clicks, 0);
assert.equal(missingUpload.clicks, 0);

// A direct-chooser UI variant with no expanded web menu remains supported.
const directAttach = new Locator({{ expanded: "false" }});
const absentUpload = new Locator({{ present: false }});
const directResult = await prepareVisiblePacketUpload({{
  playwright: pageFor(directAttach, absentUpload),
  attachSelectors: ["attach"],
  uploadMenuSelectors: ["upload"],
  beforeChooserTrigger: () => {{ directAttach.beforeArmed = true; }},
}});
assert.deepEqual(directResult, {{ menu_item_selected: false }});
assert.equal(directAttach.clicks, 1);
assert.equal(directAttach.beforeArmed, true);

const selectedFiles = [];
const selected = await assignPacketThroughBrowserUseFileChooser({{
  async setFiles(files, options) {{ selectedFiles.push({{ files, options }}); }},
}}, "C:\\\\fixture\\\\packet.json");
assert.deepEqual(selected, {{
  selected: true,
  filename: "packet.json",
  selection_mode: "browseruse_filechooser_event",
}});
assert.equal(selectedFiles.length, 1);
assert.equal(selectedFiles[0].files, "C:\\\\fixture\\\\packet.json");
assert.equal(selectedFiles[0].options.timeoutMs, 45000);
await assert.rejects(
  assignPacketThroughBrowserUseFileChooser({{}}, "C:\\\\fixture\\\\packet.json"),
  /did not provide a setFiles handle/,
);
"""
        completed = subprocess.run(
            [str(node), "--input-type=module", "--eval", script],
            cwd=Path(__file__).parents[1],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)

    def test_native_file_chooser_diagnostics_ignore_clixml_progress_and_fail_closed(self) -> None:
        node = shutil.which("node")
        self.assertIsNotNone(node)
        bridge_path = (
            Path(__file__).parents[1]
            / "src/e2r/pro_first/browser/browseruse_extension_bridge.mjs"
        ).resolve()
        packet_path = r"C:\Users\fixture-user\packet.json"
        script = f"""
import assert from "node:assert/strict";
import {{ nativeFileDialogScript, parseNativeFileChooserResult }} from {json.dumps(bridge_path.as_uri())};
const packetPath = {json.dumps(packet_path)};
const failurePayload = {{
  status: "FAILED",
  phase: "inspect_dialog_controls",
  error_id: "PatternUnavailable",
  category: "InvalidOperation",
  message: "UI Automation could not inspect the dialog",
}};
const structured = parseNativeFileChooserResult({{
  exitCode: 1,
  stdout: "banner\\nE2R_FILE_CHOOSER_RESULT:" + JSON.stringify(failurePayload) + "\\n",
  stderr: "#< CLIXML <progress>irrelevant host progress</progress>",
  targetPath: packetPath,
}});
assert.deepEqual(structured, {{
  selected: false,
  phase: "inspect_dialog_controls",
  error_id: "PatternUnavailable",
  category: "InvalidOperation",
  message: "UI Automation could not inspect the dialog",
}});
const fallback = parseNativeFileChooserResult({{
  exitCode: 1,
  stdout: "Actual parser error at " + packetPath,
  stderr: "#< CLIXML <progress>irrelevant host progress</progress>",
  targetPath: packetPath,
}});
assert.equal(fallback.selected, false);
assert.equal(fallback.phase, "RESULT_MISSING");
assert.match(fallback.message, /Actual parser error/);
assert.doesNotMatch(fallback.message, /irrelevant host progress|fixture-user|packet\\.json/);
const success = parseNativeFileChooserResult({{
  exitCode: 0,
  stdout: "E2R_FILE_CHOOSER_RESULT:" + JSON.stringify({{status:"SELECTED",phase:"complete"}}),
}});
assert.equal(success.selected, true);
const mismatchedExit = parseNativeFileChooserResult({{
  exitCode: 1,
  stdout: "E2R_FILE_CHOOSER_RESULT:" + JSON.stringify({{status:"SELECTED",phase:"complete"}}),
}});
assert.equal(mismatchedExit.selected, false);
const powershell = nativeFileDialogScript(packetPath);
assert.ok(powershell.includes('$ProgressPreference = "SilentlyContinue"'));
assert.ok(powershell.includes("E2R_FILE_CHOOSER_RESULT:"));
assert.ok(powershell.includes("inspect_dialog_controls"));
assert.ok(!powershell.includes("SendKeys"));
assert.ok(!powershell.includes("cancelPattern.Invoke"));
"""
        completed = subprocess.run(
            [str(node), "--input-type=module", "--eval", script],
            cwd=Path(__file__).parents[1],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)

    async def test_native_file_chooser_inspection_is_a_read_only_bridge_call(self) -> None:
        client = BrowserUseBridgeClient(
            endpoint="http://127.0.0.1:12345",
            token="x" * 48,
        )
        client.session_id = "BROWSERUSE-test-session"
        client.call = AsyncMock(  # type: ignore[method-assign]
            return_value={
                "open": False,
                "chrome_owned_dialog_count": 0,
                "unknown_owner_count": 0,
            }
        )

        result = await BrowserUsePage(client).inspect_native_file_chooser_state()

        self.assertEqual(
            result,
            {
                "open": False,
                "chrome_owned_dialog_count": 0,
                "unknown_owner_count": 0,
            },
        )
        client.call.assert_awaited_once_with("page.inspect_native_file_chooser")

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

    async def test_read_only_evaluate_uses_bounded_timeout_and_translates_python_alias(self) -> None:
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
            if operation in {"locator.evaluate", "locator.evaluate_all", "page.evaluate"}:
                return "div"
            if operation == "locator.click":
                return None
            raise AssertionError(operation)

        client.call = fake_call  # type: ignore[method-assign]
        page = BrowserUsePage(client)

        self.assertEqual(
            await page.locator("div.ProseMirror").evaluate("element => element.tagName.toLowerCase()"),
            "div",
        )
        self.assertEqual(calls[-1][1]["options"], {"timeoutMs": 10_000})

        self.assertEqual(
            await page.locator("div.ProseMirror").evaluate(
                "element => element.tagName.toLowerCase()",
                timeout=8_765,
            ),
            "div",
        )
        self.assertEqual(calls[-1][1]["options"], {"timeoutMs": 8_765})

        self.assertEqual(
            await page.locator("div.ProseMirror").evaluate_all(
                "elements => elements.map(element => element.tagName)",
                timeoutMs=6_543,
            ),
            "div",
        )
        self.assertEqual(calls[-1][1]["options"], {"timeoutMs": 6_543})

        self.assertEqual(
            await page.evaluate("selector => document.querySelector(selector)", "body", timeout=4_321),
            "div",
        )
        self.assertEqual(calls[-1][1]["options"], {"timeoutMs": 4_321})

        await page.locator("button").click(timeout=3_210)
        self.assertEqual(calls[-1][1]["options"], {"timeout": 3_210})

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
            'if (operation === "locator.create") return { value: { handle: await makeLocator(args) } };',
            bridge_source,
        )
        self.assertIn(
            "callReadOnlyLocatorMethod(locator, method, args)",
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

    def test_first_and_last_support_browseruse_methods_and_playwright_properties(
        self,
    ) -> None:
        node = shutil.which("node")
        self.assertIsNotNone(
            node,
            "Node.js is required for the BrowserUse bridge contract test",
        )
        bridge_path = (
            Path(__file__).parents[1]
            / "src/e2r/pro_first/browser/browseruse_extension_bridge.mjs"
        ).resolve()
        script = f"""
import assert from "node:assert/strict";
const {{ resolveBrowserUseLocatorMember, resolveFirstVisibleEnabledLocator, readonlyCallback, evaluateReadOnlyLocator, countReadOnlyLocator, isVisibleReadOnlyLocator, isEnabledReadOnlyLocator, callReadOnlyLocatorMethod, browserUseOptions, wslUncPath, BROWSERUSE_NATIVE_FILE_CHOOSER_TIMEOUT_MS, nativeFileChooserInspectionScript }} = await import({json.dumps(bridge_path.as_uri())});
assert.equal(BROWSERUSE_NATIVE_FILE_CHOOSER_TIMEOUT_MS, 45000);
const nativeChooserInspection = nativeFileChooserInspectionScript();
assert.match(nativeChooserInspection, /AutomationElement\]::RootElement/);
assert.match(nativeChooserInspection, /GetWindowThreadProcessId/);
assert.doesNotMatch(nativeChooserInspection, /SetValue|InvokePattern|SendKeys|SendWait/);
assert.match(nativeChooserInspection, /else\s*\{{\s*\$unknownOwners\s*\+=\s*1\s*\}}/);
assert.equal(wslUncPath("/mnt/c/Users/eorb9/file.json", "Ubuntu-22.04", "win32"), "C:\\\\Users\\\\eorb9\\\\file.json");
assert.equal(wslUncPath("/mnt/z/folder/file.json", "Ubuntu-22.04", "win32"), "Z:\\\\folder\\\\file.json");
assert.equal(wslUncPath("C:\\\\Users\\\\eorb9\\\\file.json", "Ubuntu-22.04", "win32"), "C:\\\\Users\\\\eorb9\\\\file.json");
assert.throws(() => wslUncPath("/mnt/c/file.json", "Ubuntu-22.04", "linux"), /requires Windows/);
const child = {{ count: async () => 1 }};
const browserUse = {{
  called: false,
  first() {{ this.called = true; return child; }},
  last: async function() {{ return child; }}
}};
assert.strictEqual(await resolveBrowserUseLocatorMember(browserUse, "first"), child);
assert.equal(browserUse.called, true);
assert.strictEqual(await resolveBrowserUseLocatorMember(browserUse, "last"), child);
const playwrightStyle = {{ first: child, last: child }};
assert.strictEqual(await resolveBrowserUseLocatorMember(playwrightStyle, "first"), child);
assert.strictEqual(await resolveBrowserUseLocatorMember(playwrightStyle, "last"), child);
await assert.rejects(resolveBrowserUseLocatorMember({{}}, "first"), /did not return a locator/);
const selectorCalls = [];
globalThis.window = {{ getComputedStyle: element => ({{ visibility: element.visibility || "visible" }}) }};
const element = ({{ width = 10, height = 10, visibility = "visible", disabled = false, ariaDisabled = false }} = {{}}) => ({{
  visibility,
  disabled,
  getBoundingClientRect() {{ return {{ width, height }}; }},
  matches(selector) {{ return selector === ":disabled" && disabled; }},
  closest(selector) {{ return selector === '[aria-disabled="true"]' && ariaDisabled ? this : null; }},
  getAttribute(name) {{ return name === "aria-disabled" && ariaDisabled ? "true" : null; }},
}});
const selectorLocator = elements => ({{
  async count() {{ throw new Error("unbounded locator.count must not be used"); }},
  async isVisible() {{ throw new Error("unbounded locator.isVisible must not be used"); }},
  async isEnabled() {{ throw new Error("unbounded locator.isEnabled must not be used"); }},
  async evaluateAll(callback, argument, options) {{ selectorCalls.push(["evaluateAll", options]); return callback(elements, argument); }},
  async evaluate(callback, argument, options) {{ selectorCalls.push(["evaluate", options]); return callback(elements[0], argument); }},
}});
const invisible = selectorLocator([element({{ width: 0, height: 0 }})]);
const attachButton = selectorLocator([element()]);
const rows = {{ "#hidden": invisible, "#attach": attachButton, "#missing": selectorLocator([]) }};
let firstCalls = 0;
const browserUsePage = {{ locator(selector) {{ return {{ first() {{ firstCalls += 1; return rows[selector]; }} }}; }} }};
assert.strictEqual(await resolveFirstVisibleEnabledLocator(browserUsePage, ["#hidden", "#attach"]), attachButton);
assert.equal(firstCalls, 2);
const playwrightPage = {{ locator() {{ return {{ first: attachButton }}; }} }};
assert.strictEqual(await resolveFirstVisibleEnabledLocator(playwrightPage, ["#attach"]), attachButton);
assert.strictEqual(await resolveFirstVisibleEnabledLocator(browserUsePage, ["#missing"]), null);
assert.equal(selectorCalls.length, 9);
assert.ok(selectorCalls.every(([, options]) => options.timeoutMs === 10000));
assert.deepEqual(browserUseOptions({{ timeout: 3210, force: true }}), {{ timeoutMs: 3210, force: true }});
assert.deepEqual(browserUseOptions({{ timeout: 4321, timeoutMs: 7654 }}), {{ timeoutMs: 7654 }});
const tagReader = readonlyCallback("element => element.tagName.toLowerCase()");
assert.equal(tagReader({{ tagName: {{ toLowerCase: () => "div" }} }}), "div");
const evaluateCalls = [];
const evaluationLocator = {{
  async evaluate(...args) {{ evaluateCalls.push(["evaluate", args]); return "DIV"; }},
  async evaluateAll(...args) {{ evaluateCalls.push(["evaluateAll", args]); return ["DIV"]; }}
}};
assert.equal(await evaluateReadOnlyLocator(evaluationLocator, "evaluate", "element => element.tagName.toLowerCase()", null, {{ timeoutMs: 7654 }}), "DIV");
assert.equal(typeof evaluateCalls[0][1][0], "function");
assert.equal(evaluateCalls[0][1][0]({{ tagName: "DIV" }}), "div");
assert.equal(evaluateCalls[0][1][1], null);
assert.deepEqual(evaluateCalls[0][1][2], {{ timeoutMs: 7654 }});
assert.deepEqual(await evaluateReadOnlyLocator(evaluationLocator, "evaluate_all", "elements => elements.map(element => ({{url: element.href, aria_label: element.getAttribute('aria-label')}}))", null, {{ timeoutMs: 4321 }}), ["DIV"]);
assert.deepEqual(evaluateCalls[1][1][2], {{ timeoutMs: 4321 }});
const defaultEvaluationCalls = [];
const defaultEvaluationLocator = {{ async evaluate(...args) {{ defaultEvaluationCalls.push(args); return "DIV"; }} }};
await evaluateReadOnlyLocator(defaultEvaluationLocator, "evaluate", "element => element.tagName.toLowerCase()");
assert.deepEqual(defaultEvaluationCalls[0][2], {{ timeoutMs: 10000 }});
const boundedSelectorCalls = [];
const boundedSelectorLocator = {{
  async evaluateAll(...args) {{ boundedSelectorCalls.push(["evaluateAll", args]); return args[0]([element(), element()], args[1]); }},
  async evaluate(...args) {{ boundedSelectorCalls.push(["evaluate", args]); return args[0](element(), args[1]); }}
}};
assert.equal(await countReadOnlyLocator(boundedSelectorLocator), 2);
assert.equal(await isVisibleReadOnlyLocator(boundedSelectorLocator), true);
assert.equal(await isEnabledReadOnlyLocator(boundedSelectorLocator), true);
assert.deepEqual(boundedSelectorCalls.map(([,args]) => args[2]), [{{timeoutMs:10000}}, {{timeoutMs:10000}}, {{timeoutMs:10000}}]);
assert.equal(await countReadOnlyLocator(boundedSelectorLocator, {{timeout: 4321}}), 2);
assert.deepEqual(boundedSelectorCalls[3][1][2], {{timeoutMs:4321}});
const dispatchedReads = [];
const apiLocator = {{
  async count() {{ throw new Error("unbounded count API called"); }},
  async isVisible() {{ throw new Error("unbounded isVisible API called"); }},
  async isEnabled() {{ throw new Error("unbounded isEnabled API called"); }},
  async evaluateAll(callback, argument, options) {{ dispatchedReads.push(["evaluateAll", options]); return callback([element(), element()], argument); }},
  async evaluate(callback, argument, options) {{ dispatchedReads.push(["evaluate", options]); return callback(element(), argument); }},
  async innerText(options) {{ dispatchedReads.push(["innerText", options]); return "visible text"; }},
  async textContent(options) {{ dispatchedReads.push(["textContent", options]); return "raw text"; }},
  async getAttribute(name, options) {{ dispatchedReads.push(["getAttribute", options]); return name; }},
}};
assert.deepEqual(await callReadOnlyLocatorMethod(apiLocator, "count"), {{handled:true, value:2}});
assert.deepEqual(await callReadOnlyLocatorMethod(apiLocator, "is_visible"), {{handled:true, value:true}});
assert.deepEqual(await callReadOnlyLocatorMethod(apiLocator, "is_enabled"), {{handled:true, value:true}});
assert.deepEqual(await callReadOnlyLocatorMethod(apiLocator, "inner_text"), {{handled:true, value:"visible text"}});
assert.deepEqual(await callReadOnlyLocatorMethod(apiLocator, "text_content"), {{handled:true, value:"raw text"}});
assert.deepEqual(await callReadOnlyLocatorMethod(apiLocator, "get_attribute", {{name:"role"}}), {{handled:true, value:"role"}});
assert.deepEqual(await callReadOnlyLocatorMethod(apiLocator, "click"), {{handled:false, value:null}});
assert.ok(dispatchedReads.every(([,options]) => options.timeoutMs === 10000));
const markerReader = readonlyCallback("(element, needle) => (element.innerText || '').toLowerCase().includes(needle)");
assert.equal(markerReader({{ innerText: "Packet ready" }}, "packet"), true);
const composerSnapshot = readonlyCallback("element => {{ /* E2R_UNPREPARED_RECOVERY_COMPOSER_SNAPSHOT */ return true; }}");
const fileChip = {{innerText:"research_packet.json", getBoundingClientRect:() => ({{width:10,height:10}}), getAttribute:() => ""}};
const composerRoot = {{innerText:"research_packet.json", querySelectorAll:() => [fileChip]}};
const composerSnapshotRoot = {{closest:() => null,parentElement:{{parentElement:{{parentElement:composerRoot}}}}}};
assert.deepEqual(composerSnapshot(composerSnapshotRoot), {{visible_file_signals:["research_packet.json"]}});
assert.throws(() => readonlyCallback("element => element.click()"), /read-only/);
assert.throws(() => readonlyCallback("element => element.id"), /no reviewed read-only callback/);
const activeAdapterCallbacks = [
  "element => element.value ?? ''",
  "([userSelector, requiredMarkers]) => {{ const observedUserTurnCount = 0; return document.querySelectorAll(userSelector); }}",
  "element => (element.innerText || '').trim().slice(-2000)",
  "elements => elements.map(element => ({{url: element.href, aria_label: element.getAttribute('aria-label')}}))",
  "element => {{ const turn = element.closest('[data-message-id], [data-turn-id]'); return turn ? turn.getAttribute('data-message-id') : null; }}",
  "element => element.tagName.toLowerCase() === 'body' || element.matches('section[data-turn]')",
  "element => `assistant-section-${{element.outerHTML.slice(0, 200)}}`",
  "selector => ({{operational_status_texts: [], citation_registry: []}})",
  "element => {{ const visit = node => node.nodeType === Node.TEXT_NODE ? node.nodeValue : ''; return Array.from(element.childNodes).map(visit).join(''); }}",
  "async input => {{ const file = input.files && input.files[0]; return file ? {{name: file.name, text: await file.text()}} : null; }}",
  "element => {{ /* E2R_UNPREPARED_RECOVERY_COMPOSER_SNAPSHOT */ return true; }}",
];
for (const expression of activeAdapterCallbacks) {{
  let callback;
  try {{ callback = readonlyCallback(expression); }} catch (error) {{
    throw new Error(String(expression) + " :: " + error.message);
  }}
  assert.equal(typeof callback, "function", expression);
}}
"""
        result = subprocess.run(
            [str(node), "--input-type=module", "--eval", script],
            cwd=Path(__file__).parents[1],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


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
        self.assertIn(
            '[role="group"] div[tabindex="0"]:has-text("사진 및 파일 추가")',
            UPLOAD_MENU_ITEM_SELECTORS,
        )
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
            self.assertEqual(
                page.upload_file_via_existing_user_session.await_args.kwargs[
                    "upload_menu_selectors"
                ],
                tuple(UPLOAD_MENU_ITEM_SELECTORS),
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
