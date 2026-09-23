"""Small authenticated RPC client for the user's claimed BrowserUse tab.

The bridge deliberately exposes only visible-page operations. It does not
create browser contexts, tabs, CDP sessions, or private ChatGPT API clients.
"""

from __future__ import annotations

import asyncio
import json
import re
import time
from dataclasses import dataclass
from typing import Any, Callable, Mapping
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


class BrowserUseBridgeError(RuntimeError):
    """A fail-closed BrowserUse bridge or identity error."""


def validate_bridge_endpoint(endpoint: str) -> str:
    normalized = str(endpoint or "").strip().rstrip("/")
    parsed = urlsplit(normalized)
    if (
        parsed.scheme != "http"
        or not parsed.hostname
        or parsed.username
        or parsed.password
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
        or parsed.port is None
        or not 1 <= parsed.port <= 65_535
    ):
        raise ValueError("BrowserUse bridge must be an authenticated private HTTP endpoint")
    host = parsed.hostname
    if host not in {"127.0.0.1", "localhost", "::1"}:
        parts = host.split(".")
        if len(parts) != 4 or not all(part.isdigit() for part in parts):
            raise ValueError("BrowserUse bridge host must be loopback or a private IPv4 address")
        octets = tuple(int(part) for part in parts)
        if any(part > 255 for part in octets):
            raise ValueError("BrowserUse bridge host is not a valid IPv4 address")
        private = (
            octets[0] == 10
            or (octets[0] == 172 and 16 <= octets[1] <= 31)
            or (octets[0] == 192 and octets[1] == 168)
        )
        if not private:
            raise ValueError("BrowserUse bridge must stay on a private local interface")
    return normalized


class BrowserUseBridgeClient:
    def __init__(
        self,
        *,
        endpoint: str,
        token: str,
        expected_origin: str = "https://chatgpt.com",
        timeout_seconds: float = 30.0,
    ) -> None:
        self.endpoint = validate_bridge_endpoint(endpoint)
        self._token = str(token or "")
        if len(self._token) < 32:
            raise ValueError("BrowserUse bridge token is missing or too short")
        self.expected_origin = expected_origin.rstrip("/")
        self.timeout_seconds = float(timeout_seconds)
        self.session_id: str | None = None
        self.current_url = ""
        self.current_title = ""
        self._closed = False

    @classmethod
    async def connect(
        cls,
        *,
        endpoint: str,
        token: str,
        job_id: str,
        expected_origin: str = "https://chatgpt.com",
        timeout_seconds: float = 30.0,
    ) -> "BrowserUseBridgeClient":
        client = cls(
            endpoint=endpoint,
            token=token,
            expected_origin=expected_origin,
            timeout_seconds=timeout_seconds,
        )
        result = await client._request(
            "/handshake",
            {"job_id": str(job_id)},
        )
        session_id = str(result.get("session_id") or "").strip()
        url = str(result.get("url") or "").strip()
        title = str(result.get("title") or "").strip()
        if not session_id:
            raise BrowserUseBridgeError("BrowserUse handshake returned no bound session identity")
        if _origin(url) != client.expected_origin:
            raise BrowserUseBridgeError("claimed BrowserUse tab is not on the required ChatGPT origin")
        client.session_id = session_id
        client.current_url = url
        client.current_title = title
        return client

    async def call(self, operation: str, **arguments: Any) -> Any:
        if self._closed or not self.session_id:
            raise BrowserUseBridgeError("BrowserUse bridge session is not connected")
        result = await self._request(
            "/rpc",
            {
                "session_id": self.session_id,
                "operation": operation,
                "arguments": _jsonable(arguments),
            },
        )
        page_url = str(result.get("page_url") or "")
        if page_url:
            if _origin(page_url) != self.expected_origin:
                raise BrowserUseBridgeError("claimed BrowserUse tab left the required ChatGPT origin")
            self.current_url = page_url
        return result.get("value")

    async def event_wait(
        self,
        event_name: str,
        *,
        after_sequence: int,
        timeout_seconds: float,
    ) -> Mapping[str, Any]:
        value = await self.call(
            "event.wait",
            event_name=event_name,
            after_sequence=int(after_sequence),
            timeout_ms=max(1, int(timeout_seconds * 1000)),
        )
        if not isinstance(value, Mapping):
            raise BrowserUseBridgeError("BrowserUse event bridge returned a malformed event")
        return value

    async def _request(self, path: str, payload: Mapping[str, Any]) -> Mapping[str, Any]:
        if self._closed:
            raise BrowserUseBridgeError("BrowserUse bridge connection is closed")
        url = self.endpoint + path
        body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        request = Request(url, data=body, headers=headers, method="POST")
        try:
            response_body = await asyncio.to_thread(self._read_response, request)
        except BrowserUseBridgeError:
            raise
        except (HTTPError, URLError, TimeoutError, OSError) as error:
            reason = getattr(error, "reason", None)
            detail = str(reason or error)
            raise BrowserUseBridgeError(
                f"BrowserUse bridge transport failed ({type(error).__name__}: {detail[:240]})"
            ) from error
        try:
            response = json.loads(response_body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise BrowserUseBridgeError("BrowserUse bridge returned invalid JSON") from error
        if not isinstance(response, Mapping):
            raise BrowserUseBridgeError("BrowserUse bridge returned an invalid response envelope")
        if response.get("ok") is not True:
            code = str(response.get("code") or "BRIDGE_ERROR")
            detail = str(response.get("error") or "request failed")[:400]
            if code == "EVENT_TIMEOUT":
                raise TimeoutError(detail)
            raise BrowserUseBridgeError(f"{code}: {detail}")
        result = response.get("result")
        if not isinstance(result, Mapping):
            raise BrowserUseBridgeError("BrowserUse bridge response is missing its result object")
        if result.get("page_url"):
            self.current_url = str(result["page_url"])
        if result.get("title"):
            self.current_title = str(result["title"])
        return result

    def _read_response(self, request: Request) -> bytes:
        with urlopen(request, timeout=self.timeout_seconds) as response:
            payload = response.read(64 * 1024 * 1024 + 1)
        if len(payload) > 64 * 1024 * 1024:
            raise BrowserUseBridgeError("BrowserUse bridge response exceeded the 64 MiB limit")
        return payload

    async def close(self) -> None:
        # Closing the Python client never closes the user's Chrome tab or the
        # shared bridge held by the persistent BrowserUse REPL.
        self._closed = True


class BrowserUsePage:
    """Playwright-shaped read/action facade backed by one claimed extension tab."""

    def __init__(self, client: BrowserUseBridgeClient) -> None:
        self.client = client
        self.context = BrowserUseContext(client)

    @property
    def url(self) -> str:
        return self.client.current_url

    async def goto(self, url: str, **options: Any) -> None:
        await self.client.call("page.goto", url=url, options=_jsonable(options))

    async def reload(self, **options: Any) -> None:
        await self.client.call("page.reload", options=_jsonable(options))

    async def wait_for_timeout(self, milliseconds: int) -> None:
        await self.client.call("page.wait_for_timeout", milliseconds=int(milliseconds))

    async def wait_for_load_state(self, state: str = "load", **options: Any) -> None:
        await self.client.call(
            "page.wait_for_load_state",
            state=state,
            options=_jsonable(options),
        )

    async def evaluate(self, expression: str, argument: Any = None) -> Any:
        return await self.client.call(
            "page.evaluate",
            expression=str(expression),
            argument=_jsonable(argument),
        )

    def locator(self, selector: str) -> "BrowserUseLocator":
        return BrowserUseLocator(self.client, create={"selector": selector})

    def get_by_role(self, role: str, **options: Any) -> "BrowserUseLocator":
        return BrowserUseLocator(
            self.client,
            create={"method": "get_by_role", "value": str(role), "options": _jsonable(options)},
        )

    def get_by_label(self, label: Any, **options: Any) -> "BrowserUseLocator":
        return BrowserUseLocator(
            self.client,
            create={"method": "get_by_label", "value": _jsonable(label), "options": _jsonable(options)},
        )

    def get_by_text(self, text: Any, **options: Any) -> "BrowserUseLocator":
        return BrowserUseLocator(
            self.client,
            create={"method": "get_by_text", "value": _jsonable(text), "options": _jsonable(options)},
        )

    async def upload_file_via_existing_user_session(
        self,
        path: str,
        *,
        attach_selectors: tuple[str, ...],
    ) -> None:
        result = await self.client.call(
            "page.attach_packet",
            path=str(path),
            attach_selectors=list(attach_selectors),
        )
        if not isinstance(result, Mapping) or result.get("selected") is not True:
            raise BrowserUseBridgeError("the visible Chrome file chooser did not select the packet")
        if str(result.get("filename") or "") != str(path).rsplit("/", 1)[-1]:
            raise BrowserUseBridgeError("the visible Chrome file chooser selected a different filename")

    async def wait_for_visible_artifact_response(
        self,
        *,
        expected_url_suffix: str,
        timeout_ms: int,
    ) -> "BrowserUseResponse":
        event = await self.client.call(
            "event.start",
            event_name="response",
        )
        sequence = int(event["sequence"])
        deadline = time.monotonic() + timeout_ms / 1000
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("timed out waiting for the visible artifact response")
            row = await self.client.event_wait(
                "response",
                after_sequence=sequence,
                timeout_seconds=remaining,
            )
            sequence = int(row.get("sequence") or sequence)
            candidate = urlsplit(str(row.get("url") or ""))
            expected = str(expected_url_suffix or "").strip()
            expected_origin = self.client.expected_origin
            suffix_matches = (
                candidate.path.endswith(expected)
                if expected.startswith("/")
                else candidate.path.rsplit("/", 1)[-1] == expected
            )
            if _origin(str(row.get("url") or "")) == expected_origin and suffix_matches:
                return BrowserUseResponse(self.client, str(row["handle"]), row)

    async def wait_for_event(
        self,
        event: str,
        *,
        timeout: int | float = 30_000,
        predicate: Callable[[Any], bool] | None = None,
    ) -> Any:
        started = await self.client.call(
            "event.start",
            event_name=event,
            timeout_ms=max(1, int(float(timeout))),
        )
        return await self._wait_for_event_after(
            event,
            after_sequence=int(started["sequence"]),
            timeout=timeout,
            predicate=predicate,
        )

    async def _wait_for_event_after(
        self,
        event: str,
        *,
        after_sequence: int,
        timeout: int | float,
        predicate: Callable[[Any], bool] | None = None,
    ) -> Any:
        sequence = int(after_sequence)
        deadline = time.monotonic() + float(timeout) / 1000
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError(f"timed out waiting for BrowserUse {event} event")
            row = await self.client.event_wait(
                event,
                after_sequence=sequence,
                timeout_seconds=remaining,
            )
            sequence = int(row.get("sequence") or sequence)
            wrapped = _event_object(self.client, row)
            if predicate is None or predicate(wrapped):
                return wrapped

    def expect_download(self, *, timeout: int | float = 30_000) -> "_BrowserUseEventExpectation":
        return _BrowserUseEventExpectation(self, "download", timeout=timeout)


class BrowserUseContext:
    def __init__(self, client: BrowserUseBridgeClient) -> None:
        self._client = client

    async def wait_for_event(
        self,
        event: str,
        *,
        timeout: int | float = 30_000,
        predicate: Callable[[Any], bool] | None = None,
    ) -> Any:
        return await BrowserUsePage(self._client).wait_for_event(
            event,
            timeout=timeout,
            predicate=predicate,
        )


class BrowserUseLocator:
    def __init__(
        self,
        client: BrowserUseBridgeClient,
        *,
        handle: str | None = None,
        create: Mapping[str, Any] | None = None,
    ) -> None:
        self._client = client
        self._handle = handle
        self._create = dict(create or {})

    async def _id(self) -> str:
        if self._handle is None:
            create = dict(self._create)
            parent = create.pop("parent", None)
            if parent is not None:
                if not isinstance(parent, BrowserUseLocator):
                    raise BrowserUseBridgeError("locator parent is not bound to BrowserUse")
                create["parent_handle"] = await parent._id()
            result = await self._client.call("locator.create", **create)
            self._handle = str(result["handle"])
        return self._handle

    @property
    def first(self) -> "BrowserUseLocator":
        return BrowserUseLocator(self._client, create={"parent": self, "method": "first"})

    @property
    def last(self) -> "BrowserUseLocator":
        return BrowserUseLocator(self._client, create={"parent": self, "method": "last"})

    async def count(self) -> int:
        return int(await self._call("count"))

    def nth(self, index: int) -> "BrowserUseLocator":
        return BrowserUseLocator(
            self._client,
            create={"parent": self, "method": "nth", "index": int(index)},
        )

    def locator(self, selector: str, **options: Any) -> "BrowserUseLocator":
        return BrowserUseLocator(
            self._client,
            create={"parent": self, "method": "locator", "selector": selector, "options": options},
        )

    def get_by_role(self, role: str, **options: Any) -> "BrowserUseLocator":
        return BrowserUseLocator(
            self._client,
            create={"parent": self, "method": "get_by_role", "value": role, "options": _jsonable(options)},
        )

    def get_by_label(self, label: Any, **options: Any) -> "BrowserUseLocator":
        return BrowserUseLocator(
            self._client,
            create={"parent": self, "method": "get_by_label", "value": _jsonable(label), "options": _jsonable(options)},
        )

    def get_by_text(self, text: Any, **options: Any) -> "BrowserUseLocator":
        return BrowserUseLocator(
            self._client,
            create={"parent": self, "method": "get_by_text", "value": _jsonable(text), "options": _jsonable(options)},
        )

    def filter(self, **options: Any) -> "BrowserUseLocator":
        return BrowserUseLocator(
            self._client,
            create={"parent": self, "method": "filter", "options": _jsonable(options)},
        )

    async def is_visible(self, **options: Any) -> bool:
        return bool(await self._call("is_visible", options=_jsonable(options)))

    async def is_enabled(self, **options: Any) -> bool:
        return bool(await self._call("is_enabled", options=_jsonable(options)))

    async def inner_text(self, **options: Any) -> str:
        return str(await self._call("inner_text", options=_jsonable(options)) or "")

    async def text_content(self, **options: Any) -> str | None:
        value = await self._call("text_content", options=_jsonable(options))
        return None if value is None else str(value)

    async def input_value(self, **options: Any) -> str:
        return str(await self._call("input_value", options=_jsonable(options)) or "")

    async def get_attribute(self, name: str, **options: Any) -> str | None:
        value = await self._call("get_attribute", name=name, options=_jsonable(options))
        return None if value is None else str(value)

    async def fill(self, value: str, **options: Any) -> None:
        await self._call("fill", value=str(value), options=_jsonable(options))

    async def click(self, **options: Any) -> None:
        await self._call("click", options=_jsonable(options))

    async def press(self, key: str, **options: Any) -> None:
        await self._call("press", key=str(key), options=_jsonable(options))

    async def wait_for(self, *, state: str = "visible", **options: Any) -> None:
        await self._call("wait_for", state=state, options=_jsonable(options))

    async def evaluate(self, expression: str, argument: Any = None, **options: Any) -> Any:
        return await self._call(
            "evaluate",
            expression=str(expression),
            argument=_jsonable(argument),
            options=_jsonable(options),
        )

    async def evaluate_all(self, expression: str, argument: Any = None, **options: Any) -> Any:
        return await self._call(
            "evaluate_all",
            expression=str(expression),
            argument=_jsonable(argument),
            options=_jsonable(options),
        )

    async def set_input_files(self, *_args: Any, **_kwargs: Any) -> None:
        raise BrowserUseBridgeError(
            "programmatic file assignment is unavailable; use the visible file chooser in the claimed tab"
        )

    async def _call(self, method: str, **arguments: Any) -> Any:
        handle = await self._id()
        return await self._client.call(
            "locator." + method,
            handle=handle,
            **arguments,
        )


class BrowserUseResponse:
    def __init__(self, client: BrowserUseBridgeClient, handle: str, metadata: Mapping[str, Any]) -> None:
        self._client = client
        self._handle = handle
        self.url = str(metadata.get("url") or "")
        self.status = int(metadata.get("status") or 0)

    async def body(self) -> bytes:
        import base64

        value = await self._client.call("response.body", handle=self._handle)
        try:
            return base64.b64decode(str(value or ""), validate=True)
        except ValueError as error:
            raise BrowserUseBridgeError("BrowserUse response body encoding is invalid") from error


class BrowserUseDownload:
    def __init__(self, client: BrowserUseBridgeClient, handle: str, filename: str) -> None:
        self._client = client
        self._handle = handle
        self.suggested_filename = filename

    async def save_as(self, destination: str) -> None:
        await self._client.call(
            "download.save_as",
            handle=self._handle,
            destination=str(destination),
        )


@dataclass
class _BrowserUseEventExpectation:
    page: BrowserUsePage
    event_name: str
    timeout: int | float
    _task: asyncio.Task[Any] | None = None
    _sequence: int | None = None

    async def __aenter__(self) -> "_BrowserUseEventExpectation":
        started = await self.page.client.call(
            "event.start",
            event_name=self.event_name,
            timeout_ms=max(1, int(float(self.timeout))),
        )
        self._sequence = int(started["sequence"])
        self._task = asyncio.create_task(
            self.page._wait_for_event_after(
                self.event_name,
                after_sequence=self._sequence,
                timeout=self.timeout,
            )
        )
        return self

    async def __aexit__(self, exc_type: Any, *_exc: Any) -> None:
        if exc_type is not None and self._task is not None and not self._task.done():
            self._task.cancel()
            await asyncio.gather(self._task, return_exceptions=True)

    @property
    def value(self) -> asyncio.Task[Any]:
        if self._task is None:
            raise BrowserUseBridgeError("BrowserUse event expectation was not started")
        return self._task


def _event_object(client: BrowserUseBridgeClient, row: Mapping[str, Any]) -> Any:
    kind = str(row.get("event_name") or "")
    handle = str(row.get("handle") or "")
    if kind == "download":
        return BrowserUseDownload(client, handle, str(row.get("suggested_filename") or ""))
    if kind == "response":
        return BrowserUseResponse(client, handle, row)
    raise BrowserUseBridgeError(f"unsupported BrowserUse event type: {kind or 'unknown'}")


def _jsonable(value: Any) -> Any:
    if isinstance(value, re.Pattern):
        flags = "".join(
            flag
            for enabled, flag in (
                (bool(value.flags & re.IGNORECASE), "i"),
                (bool(value.flags & re.MULTILINE), "m"),
                (bool(value.flags & re.DOTALL), "s"),
            )
            if enabled
        )
        return {"__e2r_regex__": value.pattern, "flags": flags}
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    raise TypeError(f"unsupported BrowserUse bridge argument: {type(value).__name__}")


def _origin(url: str) -> str:
    parsed = urlsplit(url)
    return f"{parsed.scheme}://{parsed.netloc}" if parsed.scheme and parsed.netloc else ""


__all__ = [
    "BrowserUseBridgeClient",
    "BrowserUseBridgeError",
    "BrowserUseContext",
    "BrowserUseDownload",
    "BrowserUseLocator",
    "BrowserUsePage",
    "BrowserUseResponse",
    "validate_bridge_endpoint",
]
