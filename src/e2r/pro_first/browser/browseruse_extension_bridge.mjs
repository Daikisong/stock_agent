import crypto from "node:crypto";
import fs from "node:fs";
import http from "node:http";
import net from "node:net";
import os from "node:os";
import path from "node:path";
import { spawn } from "node:child_process";

const MAX_REQUEST_BYTES = 64 * 1024 * 1024;
const MAX_EVENT_ROWS = 2048;
const DEFAULT_READ_ONLY_EVALUATE_TIMEOUT_MS = 10_000;
const CHATGPT_ORIGIN = "https://chatgpt.com";
const PRIVATE_IPV4 = /^(10\.(?:\d{1,3}\.){2}\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.(?:\d{1,3}\.)\d{1,3}|192\.168\.(?:\d{1,3}\.)\d{1,3})$/;
const READ_ONLY_LOCATOR_COUNT_EXPRESSION = "elements => elements.length";
const READ_ONLY_LOCATOR_VISIBLE_EXPRESSION = "element => { const rect = element.getBoundingClientRect(); const style = window.getComputedStyle(element); return rect.width > 0 && rect.height > 0 && style.visibility !== 'hidden' && style.visibility !== 'collapse'; }";
const READ_ONLY_LOCATOR_ENABLED_EXPRESSION = "element => !element.matches(':disabled') && !element.closest('[aria-disabled=\"true\"]')";

function assertPrivateBindHost(host) {
  if (!net.isIP(host)) throw new Error("bridge bind host must be an IP address");
  if (host === "127.0.0.1" || host === "::1") return;
  if (net.isIPv4(host) && PRIVATE_IPV4.test(host) && host.split(".").every(part => Number(part) <= 255)) return;
  throw new Error("bridge bind host must be loopback or RFC1918 private IPv4");
}

function safeOrigin(value) {
  const parsed = new URL(String(value || ""));
  if (parsed.origin !== CHATGPT_ORIGIN) {
    throw new Error("claimed BrowserUse tab must remain on the official ChatGPT origin");
  }
  return parsed.origin;
}

async function tabUrl(tab) {
  return String(typeof tab.url === "function" ? await tab.url() : tab.url || "");
}

async function tabTitle(tab) {
  return String(typeof tab.title === "function" ? await tab.title() : tab.title || "");
}

function jsonRegex(value) {
  if (Array.isArray(value)) return value.map(jsonRegex);
  if (!value || typeof value !== "object") return value;
  if (typeof value.__e2r_regex__ === "string") {
    return new RegExp(value.__e2r_regex__, String(value.flags || ""));
  }
  return Object.fromEntries(Object.entries(value).map(([key, item]) => [key, jsonRegex(item)]));
}

export function browserUseOptions(value = {}) {
  const options = jsonRegex(value || {});
  if (!options || typeof options !== "object" || Array.isArray(options)) return options;
  const timeout = options.timeoutMs ?? options.timeout;
  delete options.timeout;
  if (timeout !== undefined && timeout !== null) options.timeoutMs = timeout;
  return options;
}

function readOnlyEvaluationOptions(value = {}) {
  const options = browserUseOptions(value);
  if (options.timeoutMs === undefined || options.timeoutMs === null) {
    options.timeoutMs = DEFAULT_READ_ONLY_EVALUATE_TIMEOUT_MS;
  }
  return options;
}

function assertReadOnlyDomExpression(expression) {
  const source = String(expression || "");
  if (source.length > 100_000) throw new Error("DOM inspection expression exceeds the size bound");
  const forbidden = /(?:\bfetch\s*\(|\bXMLHttpRequest\b|\bWebSocket\b|\bEventSource\b|\bWorker\b|\bindexedDB\b|\bcaches\b|\blocalStorage\b|\bsessionStorage\b|document\.cookie|\bchrome\.|window\.open\s*\(|location\.(?:assign|replace)\s*\(|history\.(?:pushState|replaceState)\s*\(|\.dispatchEvent\s*\(|\.setAttribute\s*\(|\.removeChild\s*\(|\.appendChild\s*\(|\.remove\s*\(|\.click\s*\(|\.submit\s*\(|requestSubmit\s*\(|\.focus\s*\(|\.blur\s*\(|\.innerHTML\s*=|\.textContent\s*=|\.value\s*=|\beval\s*\()/i;
  if (forbidden.test(source)) {
    throw new Error("DOM bridge permits read-only public-page inspection only");
  }
}

export function readonlyCallback(expression) {
  const source = String(expression || "").trim();
  assertReadOnlyDomExpression(source);
  const callbacks = [
    {
      matches: value => value === READ_ONLY_LOCATOR_COUNT_EXPRESSION,
      callback: elements => elements.length,
    },
    {
      matches: value => value === READ_ONLY_LOCATOR_VISIBLE_EXPRESSION,
      callback: element => {
        const rect = element.getBoundingClientRect();
        const style = window.getComputedStyle(element);
        return rect.width > 0
          && rect.height > 0
          && style.visibility !== "hidden"
          && style.visibility !== "collapse";
      },
    },
    {
      matches: value => value === READ_ONLY_LOCATOR_ENABLED_EXPRESSION,
      callback: element => !element.matches(":disabled") && !element.closest('[aria-disabled="true"]'),
    },
    {
      matches: value => /^element\s*=>\s*element\.tagName\.toLowerCase\(\)$/.test(value),
      callback: element => element.tagName.toLowerCase(),
    },
    {
      matches: value => /element\.value\s*\?\?/.test(value),
      callback: element => element.value ?? "",
    },
    {
      matches: value => value.includes("includes(needle)") && value.includes("element.innerText"),
      callback: (element, needle) => (element.innerText || "").toLowerCase().includes(needle),
    },
    {
      matches: value => value.includes("requiredMarkers") && value.includes("observedUserTurnCount"),
      callback: ([userSelector, requiredMarkers]) => {
        const matches = Array.from(document.querySelectorAll(userSelector));
        const turns = [];
        const seen = new Set();
        for (const match of matches) {
          const turn = match.closest('section[data-turn="user"], article[data-turn="user"]') || match;
          if (seen.has(turn)) continue;
          seen.add(turn);
          turns.push(turn);
        }
        let bestMissing = [...requiredMarkers];
        for (const turn of turns) {
          const text = turn.textContent || "";
          const missing = requiredMarkers.filter(marker => !text.includes(marker));
          if (missing.length < bestMissing.length) bestMissing = missing;
          if (missing.length) continue;
          const identified = turn.closest("[data-message-id], [data-turn-id]")
            || turn.querySelector("[data-message-id], [data-turn-id]");
          const turnId = identified && (
            identified.getAttribute("data-message-id") || identified.getAttribute("data-turn-id")
          );
          return {
            observedUserTurnCount: turns.length,
            missingMarkers: [],
            markerMatched: true,
            userTurnId: turnId || null,
          };
        }
        return {
          observedUserTurnCount: turns.length,
          missingMarkers: bestMissing,
          markerMatched: false,
          userTurnId: null,
        };
      },
    },
    {
      matches: value => value.includes("slice(-2000)") && value.includes("element.innerText"),
      callback: element => (element.innerText || "").trim().slice(-2000),
    },
    {
      matches: value => value.includes("aria_label") && value.includes("elements.map(element => ({"),
      callback: elements => elements.map(element => ({
        url: element.href || element.getAttribute("href") || "",
        text: (element.innerText || "").trim(),
        aria_label: element.getAttribute("aria-label") || "",
        title: element.getAttribute("title") || "",
      })).filter(row => /^https?:\/\//i.test(row.url)),
    },
    {
      matches: value => value.includes("element.closest('[data-message-id], [data-turn-id]')"),
      callback: element => {
        const turn = element.closest("[data-message-id], [data-turn-id]");
        return turn ? (turn.getAttribute("data-message-id") || turn.getAttribute("data-turn-id")) : null;
      },
    },
    {
      matches: value => value.includes("element.matches(") && value.includes("section[data-turn]"),
      callback: element => {
        const tag = element.tagName.toLowerCase();
        return tag === "html" || tag === "body" || element.matches(
          "article, section[data-turn], [data-message-author-role], [data-message-id], [data-turn-id]",
        );
      },
    },
    {
      matches: value => value.includes("assistant-section-") && value.includes("outerHTML.slice(0, 200)"),
      callback: element => {
        const direct = element.getAttribute("data-message-id") || element.getAttribute("data-turn-id");
        if (direct) return direct;
        if (element.matches('section[data-turn="assistant"]')) {
          return `assistant-section-${Array.from(
            document.querySelectorAll('section[data-turn="assistant"]'),
          ).indexOf(element)}`;
        }
        return element.getAttribute("data-testid") || element.outerHTML.slice(0, 200);
      },
    },
    {
      matches: value => value.includes("operational_status_texts") && value.includes("citation_registry"),
      callback: selector => {
        const matches = Array.from(document.querySelectorAll(selector));
        const turns = [];
        const seen = new Set();
        for (const match of matches) {
          const turn = match.closest('section[data-turn="assistant"]') || match;
          if (seen.has(turn)) continue;
          seen.add(turn);
          const style = window.getComputedStyle(turn);
          const visible = turn.isConnected
            && style.display !== "none"
            && style.visibility !== "hidden"
            && (turn.getClientRects().length > 0 || turn.offsetWidth > 0 || turn.offsetHeight > 0);
          if (visible) turns.push(turn);
        }
        const element = turns.at(-1);
        if (!element) return null;
        const identified = element.closest("[data-message-id], [data-turn-id]")
          || element.querySelector("[data-message-id], [data-turn-id]");
        const anchors = Array.from(element.querySelectorAll("a[href]")).map(node => ({
          url: node.href || node.getAttribute("href") || "",
          text: (node.innerText || "").trim(),
          aria_label: node.getAttribute("aria-label") || "",
          title: node.getAttribute("title") || "",
        })).filter(row => /^https?:\/\//i.test(row.url));
        const buttonTexts = Array.from(element.querySelectorAll("button"))
          .map(node => (node.innerText || "").trim());
        const operationalStatusTexts = Array.from(
          element.querySelectorAll("[data-streaming-response-status] .select-none"),
        ).map(node => (node.innerText || "").trim()).filter(Boolean);
        const labelledCitation = Boolean(element.querySelector(
          '[data-testid*="citation"], [data-testid*="source"]',
        )) || buttonTexts.some(value => {
          const text = value.toLowerCase();
          return text === "sources" || text === "출처";
        });
        return {
          raw_text: (element.innerText || "").trim(),
          turn_id: identified
            ? (identified.getAttribute("data-message-id") || identified.getAttribute("data-turn-id"))
            : null,
          button_texts: buttonTexts,
          operational_status_texts: operationalStatusTexts,
          citation_registry: anchors,
          has_citations: anchors.length > 0 || labelledCitation,
        };
      },
    },
    {
      matches: value => value.includes("Node.TEXT_NODE") && value.includes("element.childNodes"),
      callback: element => {
        const visit = node => {
          if (node.nodeType === Node.TEXT_NODE) return node.nodeValue || "";
          if (node.nodeType !== Node.ELEMENT_NODE) return "";
          if (node.tagName === "BR") return "\n";
          return Array.from(node.childNodes).map(visit).join("");
        };
        const rows = Array.from(element.childNodes);
        if (
          rows.length
          && rows.some(child => child.nodeType === Node.ELEMENT_NODE && (child.tagName === "P" || child.tagName === "DIV"))
          && rows.every(child => child.nodeType === Node.TEXT_NODE || (
            child.nodeType === Node.ELEMENT_NODE && (child.tagName === "P" || child.tagName === "DIV")
          ))
        ) {
          return rows.map(row => {
            const text = row.textContent || "";
            return text.endsWith("\n") ? text.slice(0, -1) : text;
          }).join("\n");
        }
        return Array.from(element.childNodes).map(visit).join("");
      },
    },
    {
      matches: value => value.includes("input.files") && value.includes("await file.text()"),
      callback: async input => {
        const file = input.files && input.files[0];
        return file ? { name: file.name, text: await file.text() } : null;
      },
    },
  ];
  const match = callbacks.find(candidate => candidate.matches(source));
  if (!match) throw new Error("DOM bridge has no reviewed read-only callback for this expression");
  return match.callback;
}

export async function evaluateReadOnlyLocator(locator, method, expression, argument, options = {}) {
  if (!locator || !["evaluate", "evaluate_all"].includes(method)) {
    throw new Error("read-only BrowserUse locator evaluation received an invalid locator or method");
  }
  const methodName = method === "evaluate" ? "evaluate" : "evaluateAll";
  return simplify(await locator[methodName](
    readonlyCallback(expression),
    jsonRegex(argument),
    readOnlyEvaluationOptions(options),
  ));
}

export async function countReadOnlyLocator(locator, options = {}) {
  const count = await evaluateReadOnlyLocator(
    locator,
    "evaluate_all",
    READ_ONLY_LOCATOR_COUNT_EXPRESSION,
    null,
    options,
  );
  return Number(count) || 0;
}

export async function isVisibleReadOnlyLocator(locator, options = {}) {
  return Boolean(await evaluateReadOnlyLocator(
    locator,
    "evaluate",
    READ_ONLY_LOCATOR_VISIBLE_EXPRESSION,
    null,
    options,
  ));
}

export async function isEnabledReadOnlyLocator(locator, options = {}) {
  return Boolean(await evaluateReadOnlyLocator(
    locator,
    "evaluate",
    READ_ONLY_LOCATOR_ENABLED_EXPRESSION,
    null,
    options,
  ));
}

export async function callReadOnlyLocatorMethod(locator, method, args = {}) {
  const options = browserUseOptions(args.options || {});
  if (method === "count") {
    return { handled: true, value: await countReadOnlyLocator(locator, options) };
  }
  if (method === "is_visible") {
    return { handled: true, value: await isVisibleReadOnlyLocator(locator, options) };
  }
  if (method === "is_enabled") {
    return { handled: true, value: await isEnabledReadOnlyLocator(locator, options) };
  }
  if (method === "inner_text") {
    return { handled: true, value: await locator.innerText(readOnlyEvaluationOptions(options)) };
  }
  if (method === "text_content") {
    return { handled: true, value: await locator.textContent(readOnlyEvaluationOptions(options)) };
  }
  if (method === "get_attribute") {
    return {
      handled: true,
      value: await locator.getAttribute(String(args.name), readOnlyEvaluationOptions(options)),
    };
  }
  if (method === "input_value") {
    return {
      handled: true,
      value: await evaluateReadOnlyLocator(
        locator,
        "evaluate",
        "element => element.value ?? ''",
        null,
        options,
      ),
    };
  }
  if (method === "evaluate" || method === "evaluate_all") {
    return {
      handled: true,
      value: await evaluateReadOnlyLocator(
        locator,
        method,
        String(args.expression || ""),
        args.argument,
        options,
      ),
    };
  }
  return { handled: false, value: null };
}

function simplify(value) {
  if (value === undefined) return null;
  if (value === null || typeof value === "string" || typeof value === "number" || typeof value === "boolean") return value;
  if (Array.isArray(value)) return value.map(simplify);
  if (typeof value === "object") {
    return Object.fromEntries(Object.entries(value).map(([key, item]) => [key, simplify(item)]));
  }
  return String(value);
}

export async function resolveBrowserUseLocatorMember(base, memberName) {
  if (!base || !["first", "last"].includes(memberName)) {
    throw new Error("unsupported BrowserUse locator member");
  }
  const member = base[memberName];
  const locator = await (typeof member === "function" ? member.call(base) : member);
  if (!locator || typeof locator.count !== "function") {
    throw new Error(`BrowserUse locator ${memberName} did not return a locator`);
  }
  return locator;
}

export async function resolveFirstVisibleEnabledLocator(playwright, selectors) {
  for (const selector of selectors || []) {
    const base = playwright.locator(String(selector));
    const candidate = await resolveBrowserUseLocatorMember(base, "first");
    if (
      await countReadOnlyLocator(candidate)
      && await isVisibleReadOnlyLocator(candidate)
      && await isEnabledReadOnlyLocator(candidate)
    ) {
      return candidate;
    }
  }
  return null;
}

export function wslUncPath(value, distroName, platform = os.platform()) {
  const normalized = String(value || "");
  if (/^[a-zA-Z]:\\/.test(normalized) || normalized.startsWith("\\\\")) return normalized;
  if (!normalized.startsWith("/")) throw new Error("packet path must be an absolute WSL or Windows path");
  if (platform !== "win32") throw new Error("native file chooser bridge requires Windows BrowserUse runtime");
  const mountedDrive = normalized.match(/^\/mnt\/([a-zA-Z])(?:\/(.*))?$/);
  if (mountedDrive) {
    const tail = (mountedDrive[2] || "").replaceAll("/", "\\");
    return mountedDrive[1].toUpperCase() + ":\\" + tail;
  }
  return `\\\\wsl.localhost\\${distroName}${normalized.replaceAll("/", "\\")}`;
}

function powerShellEncoded(script) {
  return Buffer.from(script, "utf16le").toString("base64");
}

function runWsl(distroName, arguments_, input = "") {
  return new Promise((resolve, reject) => {
    const child = spawn("wsl.exe", ["-d", distroName, "--", ...arguments_], {
      windowsHide: true,
      stdio: ["pipe", "pipe", "pipe"],
    });
    let stdout = "";
    let stderr = "";
    child.stdout.setEncoding("utf8");
    child.stderr.setEncoding("utf8");
    child.stdout.on("data", data => { stdout = (stdout + data).slice(-3000); });
    child.stderr.on("data", data => { stderr = (stderr + data).slice(-3000); });
    child.once("error", reject);
    child.once("close", code => {
      if (code !== 0) {
        reject(new Error(`WSL bridge handoff failed (exit=${code}; ${(stderr || stdout).replace(/[\r\n]+/g, " ").slice(0, 300)})`));
      } else resolve(stdout.trim());
    });
    child.stdin.end(input);
  });
}

async function persistPrivateHandoff({ distroName, linuxHome, jobId, sessionId, endpoint, token }) {
  if (!/^[A-Za-z0-9_-]{1,96}$/.test(jobId)) throw new Error("unsafe BrowserUse bridge job identity");
  if (!/^\/(?:home\/[A-Za-z0-9_.-]+|root)$/.test(linuxHome)) throw new Error("unsafe WSL handoff home path");
  const directory = `${linuxHome}/.cache/e2r/browseruse`;
  const file = `${directory}/${jobId}.json`;
  const script = [
    "set -eu",
    "umask 077",
    `mkdir -p '${directory}'`,
    `chmod 700 '${directory}'`,
    `test ! -e '${file}' || { echo "handoff already exists" >&2; exit 73; }`,
    `cat > '${file}'`,
    `chmod 600 '${file}'`,
    `printf '%s' '${file}'`,
  ].join("\n");
  const handoff = JSON.stringify({ job_id: jobId, session_id: sessionId, endpoint, token });
  return await runWsl(distroName, ["bash", "-lc", script], handoff);
}

async function removePrivateHandoff({ distroName, jobId, sessionId, linuxHome }) {
  const file = `${linuxHome}/.cache/e2r/browseruse/${jobId}.json`;
  const script = [
    "set -eu",
    `python3 -c 'import json,pathlib,sys; p=pathlib.Path(sys.argv[1]); d=json.loads(p.read_text()) if p.is_file() and not p.is_symlink() else {}; p.unlink() if d.get("session_id")==sys.argv[2] else None' '${file}' '${sessionId}'`,
  ].join("\n");
  await runWsl(distroName, ["bash", "-lc", script]);
}

async function resolveWslHome(distroName) {
  const home = await runWsl(
    distroName,
    ["bash", "-lc", 'getent passwd "$(id -u)" | cut -d: -f6'],
  );
  if (!/^\/(?:home\/[A-Za-z0-9_.-]+|root)$/.test(home)) {
    throw new Error("could not resolve a safe Linux user home for the BrowserUse handoff");
  }
  return home;
}

async function resolveWslGateway(distroName) {
  const routes = await runWsl(distroName, ["bash", "-lc", "ip -o route show default"]);
  const match = routes.match(/\bdefault\s+via\s+([0-9.]+)\b/);
  if (!match) throw new Error("could not resolve the Windows private gateway from the active WSL route");
  assertPrivateBindHost(match[1]);
  return match[1];
}

function nativeFileDialogScript(targetPath) {
  const targetB64 = Buffer.from(targetPath, "utf8").toString("base64");
  return `
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
Add-Type -TypeDefinition @'
using System;
using System.Runtime.InteropServices;
public static class E2RWindowApi {
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern IntPtr GetWindow(IntPtr hWnd, uint uCmd);
  [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint processId);
}
'@
$targetPath = [System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("${targetB64}"))
if (-not (Test-Path -LiteralPath $targetPath -PathType Leaf)) { throw "Selected packet is not visible to Windows" }
$deadline = [DateTime]::UtcNow.AddSeconds(45)
$matchedDialog = $false
while ([DateTime]::UtcNow -lt $deadline) {
  $handle = [E2RWindowApi]::GetForegroundWindow()
  if ($handle -ne [IntPtr]::Zero) {
    $dialog = [System.Windows.Automation.AutomationElement]::FromHandle($handle)
    if ($null -ne $dialog) {
      $title = [string]$dialog.Current.Name
      if ($title -match "^(Open|Open File|열기|파일 열기)$") {
        $owner = [E2RWindowApi]::GetWindow($handle, 4)
        [uint32]$ownerPid = 0
        [void][E2RWindowApi]::GetWindowThreadProcessId($owner, [ref]$ownerPid)
        $ownerName = ""
        if ($ownerPid -gt 0) { $ownerName = (Get-Process -Id $ownerPid -ErrorAction Stop).ProcessName }
        if ($ownerName -ne "chrome") { throw "Foreground file chooser is not owned by the existing Chrome process" }
        $matchedDialog = $true
        $scope = [System.Windows.Automation.TreeScope]::Descendants
        $editCondition = New-Object System.Windows.Automation.PropertyCondition(
          [System.Windows.Automation.AutomationElement]::ControlTypeProperty,
          [System.Windows.Automation.ControlType]::Edit
        )
        $edits = $dialog.FindAll($scope, $editCondition)
        $fileEdit = $null
        foreach ($edit in $edits) {
          if ($edit.Current.AutomationId -eq "1001" -or $edit.Current.Name -match "File name|파일 이름") { $fileEdit = $edit; break }
        }
        if ($null -eq $fileEdit -and $edits.Count -eq 1) { $fileEdit = $edits.Item(0) }
        $buttonCondition = New-Object System.Windows.Automation.PropertyCondition(
          [System.Windows.Automation.AutomationElement]::ControlTypeProperty,
          [System.Windows.Automation.ControlType]::Button
        )
        $buttons = $dialog.FindAll($scope, $buttonCondition)
        $openButton = $null
        $cancelButton = $null
        foreach ($button in $buttons) {
          if ($button.Current.Name -match "^(Open|열기)$") { $openButton = $button }
          if ($button.Current.Name -match "^(Cancel|취소)$") { $cancelButton = $button }
        }
        if ($null -eq $fileEdit -or $null -eq $openButton) {
          if ($null -ne $cancelButton) {
            $cancelPattern = $cancelButton.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern)
            $cancelPattern.Invoke()
          }
          throw "Chrome file chooser controls did not match the expected Open dialog"
        }
        $valuePattern = $fileEdit.GetCurrentPattern([System.Windows.Automation.ValuePattern]::Pattern)
        $valuePattern.SetValue($targetPath)
        $openPattern = $openButton.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern)
        $openPattern.Invoke()
        Write-Output "E2R_FILE_CHOOSER_SELECTED"
        exit 0
      }
    }
  }
  Start-Sleep -Milliseconds 100
}
if ($matchedDialog) { throw "Chrome file chooser timed out before selecting the packet" }
throw "No Chrome-owned Open dialog appeared; no global keystrokes were sent"
`;
}

function validatePacketPathForWindowsChooser({ pathValue, distroName }) {
  const targetPath = wslUncPath(pathValue, distroName);
  let stat;
  try {
    stat = fs.statSync(targetPath);
  } catch {
    throw new Error("packet file is not readable from the Windows file chooser");
  }
  if (!stat.isFile() || stat.size < 1 || stat.size > 32 * 1024 * 1024) {
    throw new Error("packet file must be a nonempty regular JSON file under 32 MiB");
  }
  if (path.extname(targetPath).toLowerCase() !== ".json") {
    throw new Error("BrowserUse packet attachment must be a JSON file");
  }
  return targetPath;
}

async function selectThroughVisibleWindowsDialog({ targetPath, distroName }) {
  const encoded = powerShellEncoded(nativeFileDialogScript(targetPath));
  const child = spawn(
    "powershell.exe",
    ["-NoLogo", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-EncodedCommand", encoded],
    { windowsHide: true, stdio: ["ignore", "pipe", "pipe"] },
  );
  let stdout = "";
  let stderr = "";
  child.stdout.setEncoding("utf8");
  child.stderr.setEncoding("utf8");
  child.stdout.on("data", data => { stdout = (stdout + data).slice(-2000); });
  child.stderr.on("data", data => { stderr = (stderr + data).slice(-2000); });
  const exitCode = new Promise((resolve, reject) => {
    child.once("error", reject);
    child.once("close", code => resolve(code));
  });
  return {
    targetPath,
    child,
    completion: exitCode.then(code => {
      if (code !== 0 || !stdout.includes("E2R_FILE_CHOOSER_SELECTED")) {
        const detail = (stderr || stdout).replace(/[\r\n]+/g, " ").slice(0, 350);
        throw new Error(`existing Chrome file chooser did not select the packet (exit=${code}; ${detail})`);
      }
      return true;
    }),
  };
}

export async function startBrowserUseExtensionBridge({
  tab,
  jobId,
  host = "",
  port = 0,
  distroName = "Ubuntu-22.04",
}) {
  if (!tab || !tab.playwright || !tab.id) throw new Error("an exact claimed BrowserUse tab is required");
  if (!String(jobId || "").trim()) throw new Error("bridge job identity is required");
  const bindHost = String(host || await resolveWslGateway(distroName));
  assertPrivateBindHost(bindHost);
  safeOrigin(await tabUrl(tab));
  if (!Number.isInteger(port) || port < 0 || port > 65_535) throw new Error("invalid BrowserUse bridge port");

  const token = crypto.randomBytes(32).toString("base64url");
  const sessionId = "BROWSERUSE-" + crypto.createHash("sha256")
    .update(`${token}\n${jobId}\n${tab.id}`)
    .digest("hex")
    .slice(0, 32);
  const linuxHome = await resolveWslHome(distroName);
  const locators = new Map();
  const downloads = new Map();
  const events = new Map();
  const requestQueue = [];
  let queueWake = null;
  let eventSequence = 0;
  let closed = false;
  let activeDownloadWaiter = null;

  const enqueueRequest = request => new Promise(resolve => {
    requestQueue.push({ request, resolve });
    if (queueWake) {
      const wake = queueWake;
      queueWake = null;
      wake();
    }
  });

  const nextRequest = async () => {
    if (requestQueue.length) return requestQueue.shift();
    return await new Promise(resolve => {
      queueWake = () => {
        queueWake = null;
        resolve(requestQueue.shift() || null);
      };
    });
  };

  const publishDownload = async download => {
    const handle = crypto.randomUUID();
    const filenameValue = download?.suggestedFilename;
    const filename = typeof filenameValue === "function"
      ? await filenameValue.call(download)
      : filenameValue;
    downloads.set(handle, download);
    const row = {
      sequence: ++eventSequence,
      event_name: "download",
      handle,
      suggested_filename: String(filename || ""),
    };
    events.set(row.sequence, row);
    while (events.size > MAX_EVENT_ROWS) {
      const oldest = Math.min(...events.keys());
      const expired = events.get(oldest);
      if (expired) downloads.delete(expired.handle);
      events.delete(oldest);
    }
    if (activeDownloadWaiter) {
      activeDownloadWaiter.row = row;
      activeDownloadWaiter.done = true;
    }
    return row;
  };

  const findHandle = (map, handle, kind) => {
    const value = map.get(String(handle || ""));
    if (!value) throw new Error(`${kind} handle is no longer available`);
    return value;
  };

  const makeLocator = async args => {
    const { parent_handle: parentHandle, method, selector, value, options = {}, index } = args;
    const base = parentHandle ? findHandle(locators, parentHandle, "locator") : null;
    let locator;
    if (!method) {
      if (base) throw new Error("root locator cannot have a parent");
      if (typeof selector !== "string" || selector.length > 4_000) throw new Error("invalid visible locator selector");
      locator = tab.playwright.locator(selector);
    } else if (method === "first") locator = await resolveBrowserUseLocatorMember(base, "first");
    else if (method === "last") locator = await resolveBrowserUseLocatorMember(base, "last");
    else if (method === "nth") locator = base.nth(Number(index));
    else if (method === "locator") locator = base.locator(String(selector), jsonRegex(options));
    else if (method === "get_by_role") locator = base.getByRole(String(value), jsonRegex(options));
    else if (method === "get_by_label") locator = (base || tab.playwright).getByLabel(jsonRegex(value), jsonRegex(options));
    else if (method === "get_by_text") locator = (base || tab.playwright).getByText(jsonRegex(value), jsonRegex(options));
    else if (method === "filter") {
      const converted = jsonRegex(options);
      if (Object.hasOwn(converted, "has_text")) {
        converted.hasText = converted.has_text;
        delete converted.has_text;
      }
      locator = base.filter(converted);
    } else throw new Error(`unsupported BrowserUse locator constructor: ${method}`);
    const handle = crypto.randomUUID();
    locators.set(handle, locator);
    return handle;
  };

  const callLocator = async ({ handle, method, ...args }) => {
    const locator = findHandle(locators, handle, "locator");
    const readOnly = await callReadOnlyLocatorMethod(locator, method, args);
    if (readOnly.handled) return readOnly.value;
    const options = browserUseOptions(args.options || {});
    if (method === "fill") return await locator.fill(String(args.value), options);
    if (method === "click") return await locator.click(options);
    if (method === "press") return await locator.press(String(args.key), options);
    if (method === "wait_for") return await locator.waitFor({ state: String(args.state || "visible"), ...options });
    throw new Error(`unsupported BrowserUse locator method: ${method}`);
  };

  const attachPacket = async ({ filePath, attachSelectors }) => {
    const attach = await resolveFirstVisibleEnabledLocator(tab.playwright, attachSelectors);
    if (!attach) throw new Error("visible attachment button was not found in the claimed ChatGPT tab");
    const targetPath = validatePacketPathForWindowsChooser({ pathValue: filePath, distroName });
    await attach.click();
    const dialog = await selectThroughVisibleWindowsDialog({ targetPath, distroName });
    try {
      await dialog.completion;
      return { selected: true, filename: path.basename(dialog.targetPath) };
    } catch (error) {
      try { dialog.child.kill(); } catch {}
      throw error;
    }
  };

  const dispatch = async (operation, args) => {
    if (operation === "locator.create") return { value: { handle: await makeLocator(args) } };
    if (operation.startsWith("locator.")) {
      return { value: await callLocator({ ...args, method: operation.slice("locator.".length) }) };
    }
    if (operation === "page.goto") {
      const requested = new URL(String(args.url || ""));
      if (requested.origin !== CHATGPT_ORIGIN) throw new Error("navigation outside ChatGPT is forbidden");
      await tab.goto(requested.href, browserUseOptions(args.options || {}));
      return { value: null };
    }
    if (operation === "page.reload") {
      await tab.reload(browserUseOptions(args.options || {}));
      return { value: null };
    }
    if (operation === "page.wait_for_timeout") {
      const ms = Math.max(0, Math.min(120_000, Number(args.milliseconds) || 0));
      await tab.playwright.waitForTimeout(ms);
      return { value: null };
    }
    if (operation === "page.wait_for_load_state") {
      await tab.playwright.waitForLoadState(String(args.state || "load"), browserUseOptions(args.options || {}));
      return { value: null };
    }
    if (operation === "page.evaluate") {
      const expression = String(args.expression || "");
      assertReadOnlyDomExpression(expression);
      return { value: simplify(await tab.playwright.evaluate(
        readonlyCallback(expression),
        jsonRegex(args.argument),
        readOnlyEvaluationOptions(args.options || {}),
      )) };
    }
    if (operation === "page.attach_packet") {
      return { value: await attachPacket({ filePath: args.path, attachSelectors: args.attach_selectors }) };
    }
    if (operation === "event.start") {
      const eventName = String(args.event_name || "");
      if (eventName !== "download") {
        throw Object.assign(
          new Error("BrowserUse extension exposes download events only; response-body interception is unavailable"),
          { code: "CAPABILITY_UNAVAILABLE" },
        );
      }
      if (activeDownloadWaiter && !activeDownloadWaiter.done) {
        throw Object.assign(new Error("a BrowserUse download waiter is already armed"), { code: "EVENT_WAITER_BUSY" });
      }
      const timeoutMs = Math.max(1, Math.min(120_000, Number(args.timeout_ms) || 30_000));
      const waiter = { sequence: eventSequence, done: false, row: null, error: null };
      // Arm inside the active Node REPL dispatch turn so this exact
      // extension capability remains usable while the Python pipeline runs.
      waiter.promise = tab.playwright.waitForEvent("download", { timeout: timeoutMs })
        .then(download => publishDownload(download).then(row => { waiter.row = row; waiter.done = true; }))
        .catch(error => { waiter.error = error; waiter.done = true; });
      activeDownloadWaiter = waiter;
      return { value: { sequence: waiter.sequence } };
    }
    if (operation === "event.wait") {
      const eventName = String(args.event_name || "");
      if (eventName !== "download") {
        throw Object.assign(new Error("BrowserUse extension does not expose response events"), { code: "CAPABILITY_UNAVAILABLE" });
      }
      const afterSequence = Number(args.after_sequence) || 0;
      const cached = [...events.values()].find(row => row.event_name === eventName && row.sequence > afterSequence);
      if (cached) return { value: cached };
      const waiter = activeDownloadWaiter;
      if (!waiter || waiter.sequence !== afterSequence) {
        throw Object.assign(new Error("no exact BrowserUse download waiter is armed"), { code: "EVENT_WAITER_MISSING" });
      }
      await waiter.promise;
      if (waiter.error) {
        const error = new Error(String(waiter.error?.message || waiter.error || "BrowserUse download wait failed"));
        error.code = /timeout|timed out/i.test(error.message) ? "EVENT_TIMEOUT" : "BROWSERUSE_EVENT_FAILED";
        throw error;
      }
      if (!waiter.row || waiter.row.sequence <= afterSequence) {
        throw Object.assign(new Error("BrowserUse download event was not observed"), { code: "EVENT_TIMEOUT" });
      }
      return { value: waiter.row };
    }
    if (operation === "response.body") throw Object.assign(new Error("BrowserUse response-body capture is unavailable"), { code: "CAPABILITY_UNAVAILABLE" });
    if (operation === "download.save_as") {
      const download = findHandle(downloads, args.handle, "download");
      const destination = wslUncPath(args.destination, distroName);
      if (!path.isAbsolute(destination) && !/^\\\\/.test(destination)) throw new Error("download destination must be absolute");
      if (typeof download.saveAs === "function") await download.saveAs(destination);
      else if (typeof download.save_as === "function") await download.save_as(destination);
      else if (typeof download.path === "function") {
        const sourcePath = await download.path();
        if (!sourcePath) throw new Error("BrowserUse download has no readable local path");
        fs.copyFileSync(sourcePath, destination);
      } else throw new Error("BrowserUse download object has no supported save operation");
      return { value: true };
    }
    throw new Error(`unsupported BrowserUse bridge operation: ${operation}`);
  };

  const processRpcRequest = async ({ route, payload }) => {
    let value;
    if (route === "/handshake") {
      if (String(payload.job_id || "") !== String(jobId)) throw Object.assign(new Error("job identity does not match this claimed BrowserUse bridge"), { code: "JOB_MISMATCH" });
      const currentUrl = await tabUrl(tab);
      safeOrigin(currentUrl);
      value = { session_id: sessionId, url: currentUrl, title: await tabTitle(tab) };
    } else {
      if (String(payload.session_id || "") !== sessionId) throw Object.assign(new Error("session identity does not match the exact claimed tab"), { code: "SESSION_MISMATCH" });
      safeOrigin(await tabUrl(tab));
      const result = await dispatch(String(payload.operation || ""), payload.arguments || {});
      const currentUrl = await tabUrl(tab);
      safeOrigin(currentUrl);
      value = { ...result, page_url: currentUrl, title: await tabTitle(tab) };
    }
    return { ok: true, result: value };
  };

  const server = http.createServer(async (request, response) => {
    if (request.method !== "POST" || !["/handshake", "/rpc"].includes(request.url)) {
      response.writeHead(404).end();
      return;
    }
    const authorization = String(request.headers.authorization || "");
    const suppliedToken = authorization.startsWith("Bearer ") ? authorization.slice(7) : "";
    const supplied = Buffer.from(suppliedToken);
    const expected = Buffer.from(token);
    if (supplied.length !== expected.length || !crypto.timingSafeEqual(supplied, expected)) {
      response.writeHead(401).end(JSON.stringify({ ok: false, code: "AUTH_FAILED", error: "bridge token mismatch" }));
      return;
    }
    const chunks = [];
    let bytes = 0;
    try {
      for await (const chunk of request) {
        bytes += chunk.length;
        if (bytes > MAX_REQUEST_BYTES) throw Object.assign(new Error("RPC request exceeds the size limit"), { code: "REQUEST_TOO_LARGE" });
        chunks.push(chunk);
      }
      const payload = JSON.parse(Buffer.concat(chunks).toString("utf8"));
      const envelope = await enqueueRequest({ route: request.url, payload });
      response.writeHead(200, { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" });
      response.end(JSON.stringify(envelope));
    } catch (error) {
      const code = String(error?.code || "BRIDGE_OPERATION_FAILED");
      const detail = String(error?.message || error || "unknown bridge error").replace(/[\r\n]+/g, " ").slice(0, 500);
      response.writeHead(200, { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" });
      response.end(JSON.stringify({ ok: false, code, error: detail }));
    }
  });
  server.requestTimeout = 120_000;
  server.headersTimeout = 30_000;
  server.keepAliveTimeout = 5_000;
  await new Promise((resolve, reject) => {
    server.once("error", reject);
    server.listen(port, bindHost, resolve);
  });
  const address = server.address();
  if (!address || typeof address === "string") throw new Error("BrowserUse bridge did not bind a TCP endpoint");
  const endpoint = `http://${bindHost}:${address.port}`;
  let handoffPath;
  try {
    handoffPath = await persistPrivateHandoff({
      distroName,
      linuxHome,
      jobId: String(jobId),
      sessionId,
      endpoint,
      token,
    });
  } catch (error) {
    closed = true;
    await new Promise(resolve => server.close(resolve));
    throw error;
  }
  let activeService = false;
  let cleanupPromise = null;
  const serviceRequests = async () => {
    if (activeService) throw new Error("BrowserUse bridge request service is already active");
    activeService = true;
    try {
      while (!closed) {
        const item = await nextRequest();
        if (!item) break;
        try {
          item.resolve(await processRpcRequest(item.request));
        } catch (error) {
          item.resolve({
            ok: false,
            code: String(error?.code || "BRIDGE_OPERATION_FAILED"),
            error: String(error?.message || error || "unknown bridge error").replace(/[\r\n]+/g, " ").slice(0, 500),
          });
        }
      }
    } finally {
      activeService = false;
    }
  };
  const cleanup = async () => {
    if (cleanupPromise) return await cleanupPromise;
    cleanupPromise = (async () => {
      closed = true;
      if (queueWake) {
        const wake = queueWake;
        queueWake = null;
        wake();
      }
      for (const pending of requestQueue.splice(0)) {
        pending.resolve({ ok: false, code: "BRIDGE_CLOSED", error: "BrowserUse bridge is shutting down" });
      }
      await new Promise(resolve => server.close(resolve));
      await removePrivateHandoff({ distroName, linuxHome, jobId: String(jobId), sessionId });
    })();
    return await cleanupPromise;
  };
  return {
    endpoint,
    handoffPath,
    async runUntil(work) {
      if (closed) throw new Error("BrowserUse bridge is closed");
      const service = serviceRequests();
      try {
        return await (typeof work === "function" ? work() : work);
      } finally {
        closed = true;
        if (queueWake) {
          const wake = queueWake;
          queueWake = null;
          wake();
        }
        await service;
        await cleanup();
      }
    },
    async close() {
      await cleanup();
    },
  };
}
