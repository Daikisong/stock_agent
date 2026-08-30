"""Loopback CDP compatibility proxy scoped to an existing ChatGPT page.

Chrome can expose unrelated user pages through one browser-level CDP socket.
Playwright initializes every exposed page before returning from
``connect_over_cdp``; one unrelated, unresponsive page can therefore block the
single ChatGPT page that E2R actually needs.  This proxy leaves every browser
target open but hides non-ChatGPT page targets from the attached Playwright
client.

Chrome 151 also leaves Playwright's root ``Target.getTargetInfo`` barrier
unanswered.  Playwright does not consume that response value, so the proxy
supplies the protocol-shaped synchronization response locally.  All other CDP
traffic is forwarded byte-for-byte.
"""

from __future__ import annotations

import asyncio
import ipaddress
import json
from typing import Any, Mapping
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen


class ExistingPageCDPProxy:
    """Expose only an already-open page on one allowed origin to Playwright."""

    _INTERNAL_COMMAND_ID_BASE = 2_000_000_000

    def __init__(
        self,
        *,
        upstream_url: str,
        allowed_origin: str,
        server: Any,
        connect: Any,
    ) -> None:
        self.upstream_url = upstream_url
        self.allowed_origin = allowed_origin
        self._server = server
        self._connect = connect
        self._client_active = False
        self._client_guard = asyncio.Lock()
        socket = tuple(server.sockets)[0]
        port = int(socket.getsockname()[1])
        self.endpoint = f"ws://127.0.0.1:{port}"

    @classmethod
    async def start(
        cls,
        *,
        upstream_endpoint: str,
        allowed_origin: str,
    ) -> "ExistingPageCDPProxy":
        try:
            from websockets.asyncio.client import connect
            from websockets.asyncio.server import serve
        except ImportError as error:
            raise RuntimeError(
                "websockets optional dependency is required: install project[pro-first]"
            ) from error

        normalized_origin = cls._origin(allowed_origin)
        await cls._activate_single_existing_page(
            upstream_endpoint,
            allowed_origin=normalized_origin,
        )
        upstream_url = await cls._resolve_upstream_websocket(upstream_endpoint)
        holder: dict[str, ExistingPageCDPProxy] = {}

        async def handler(client: Any) -> None:
            await holder["proxy"]._handle_client(client)

        server = await serve(
            handler,
            "127.0.0.1",
            0,
            max_size=None,
            ping_interval=None,
        )
        proxy = cls(
            upstream_url=upstream_url,
            allowed_origin=normalized_origin,
            server=server,
            connect=connect,
        )
        holder["proxy"] = proxy
        return proxy

    async def close(self) -> None:
        self._server.close()
        await self._server.wait_closed()

    async def _handle_client(self, client: Any) -> None:
        async with self._client_guard:
            if self._client_active:
                await client.close(
                    code=1013,
                    reason="E2R CDP proxy permits one Playwright client",
                )
                return
            self._client_active = True
        try:
            async with self._connect(
                self.upstream_url,
                max_size=None,
                ping_interval=None,
            ) as upstream:
                await self._forward(client=client, upstream=upstream)
        finally:
            async with self._client_guard:
                self._client_active = False

    async def _forward(self, *, client: Any, upstream: Any) -> None:
        client_send_lock = asyncio.Lock()
        upstream_send_lock = asyncio.Lock()
        hidden_sessions: set[str] = set()
        internal_command_ids: set[int] = set()
        next_internal_id = self._INTERNAL_COMMAND_ID_BASE

        async def send_client(message: str | bytes) -> None:
            async with client_send_lock:
                await client.send(message)

        async def send_upstream(message: str | bytes) -> None:
            async with upstream_send_lock:
                await upstream.send(message)

        async def client_to_upstream() -> None:
            async for message in client:
                request = self._json_object(message)
                if self._is_root_target_info_barrier(request):
                    await send_client(
                        json.dumps(
                            {
                                "id": request["id"],
                                "result": {
                                    "targetInfo": {
                                        "targetId": "E2R-BROWSER-ROOT",
                                        "type": "browser",
                                        "title": "",
                                        "url": "",
                                        "attached": True,
                                        "canAccessOpener": False,
                                    }
                                },
                            },
                            separators=(",", ":"),
                        )
                    )
                    continue
                await send_upstream(message)

        async def upstream_to_client() -> None:
            nonlocal next_internal_id
            async for message in upstream:
                response = self._json_object(message)
                if response is None:
                    await send_client(message)
                    continue
                method = str(response.get("method") or "")
                params = response.get("params")
                params = params if isinstance(params, Mapping) else {}
                if method == "Target.attachedToTarget":
                    target = params.get("targetInfo")
                    target = target if isinstance(target, Mapping) else {}
                    hidden = self._hide_target(target)
                    if hidden:
                        session_id = str(params.get("sessionId") or "")
                        if session_id:
                            hidden_sessions.add(session_id)
                            if params.get("waitingForDebugger") is True:
                                next_internal_id += 1
                                internal_command_ids.add(next_internal_id)
                                await send_upstream(
                                    json.dumps(
                                        {
                                            "id": next_internal_id,
                                            "method": "Runtime.runIfWaitingForDebugger",
                                            "sessionId": session_id,
                                        },
                                        separators=(",", ":"),
                                    )
                                )
                        continue
                if method == "Target.detachedFromTarget":
                    session_id = str(params.get("sessionId") or "")
                    if session_id in hidden_sessions:
                        hidden_sessions.discard(session_id)
                        continue
                response_id = response.get("id")
                if isinstance(response_id, int) and response_id in internal_command_ids:
                    internal_command_ids.discard(response_id)
                    continue
                if str(response.get("sessionId") or "") in hidden_sessions:
                    continue
                await send_client(message)

        tasks = {
            asyncio.create_task(client_to_upstream()),
            asyncio.create_task(upstream_to_client()),
        }
        done, pending = await asyncio.wait(
            tasks,
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()
        await asyncio.gather(*done, *pending, return_exceptions=True)

    def _hide_target(self, target: Mapping[str, Any]) -> bool:
        target_type = str(target.get("type") or "")
        target_url = str(target.get("url") or "")
        if target_type == "browser_ui":
            return True
        if target_type in {
            "page",
            "iframe",
            "service_worker",
            "shared_worker",
            "worker",
        }:
            return self._origin(target_url) != self.allowed_origin
        return False

    @staticmethod
    def _is_root_target_info_barrier(
        request: Mapping[str, Any] | None,
    ) -> bool:
        if request is None or request.get("method") != "Target.getTargetInfo":
            return False
        if request.get("sessionId"):
            return False
        params = request.get("params")
        return not isinstance(params, Mapping) or not params.get("targetId")

    @staticmethod
    def _json_object(message: Any) -> Mapping[str, Any] | None:
        if not isinstance(message, str):
            return None
        try:
            value = json.loads(message)
        except json.JSONDecodeError:
            return None
        return value if isinstance(value, Mapping) else None

    @classmethod
    async def _resolve_upstream_websocket(cls, endpoint: str) -> str:
        parsed = urlparse(endpoint)
        if parsed.scheme in {"ws", "wss"}:
            cls._require_loopback(endpoint)
            return endpoint
        if parsed.scheme not in {"http", "https"}:
            raise RuntimeError("CDP endpoint must use http(s) or ws(s)")
        cls._require_loopback(endpoint)
        version_url = endpoint.rstrip("/") + "/json/version"

        def fetch() -> str:
            with urlopen(version_url, timeout=5) as response:
                payload = json.load(response)
            websocket_url = str(payload.get("webSocketDebuggerUrl") or "")
            if not websocket_url:
                raise RuntimeError("CDP /json/version omitted webSocketDebuggerUrl")
            return websocket_url

        websocket_url = await asyncio.to_thread(fetch)
        cls._require_loopback(websocket_url)
        return websocket_url

    @classmethod
    async def _activate_single_existing_page(
        cls,
        endpoint: str,
        *,
        allowed_origin: str,
    ) -> None:
        """Wake one existing allowed tab without creating a browser target.

        Chrome can freeze a background renderer under Memory Saver.  In that
        state the browser CDP socket responds, but Playwright waits forever for
        the existing page's initialization commands.  Chrome's loopback
        ``/json/activate`` command only foregrounds an already listed target;
        it never opens a tab, window, context, or conversation.
        """

        parsed = urlparse(endpoint)
        if parsed.scheme not in {"http", "https"}:
            return
        cls._require_loopback(endpoint)
        base = endpoint.rstrip("/")

        def activate() -> None:
            with urlopen(base + "/json/list", timeout=5) as response:
                rows = json.load(response)
            matches = [
                row
                for row in rows
                if isinstance(row, Mapping)
                and row.get("type") == "page"
                and cls._origin(str(row.get("url") or "")) == allowed_origin
                and str(row.get("id") or "").strip()
            ]
            if len(matches) != 1:
                return
            target_id = str(matches[0]["id"])
            request = Request(
                base + "/json/activate/" + quote(target_id, safe=""),
                method="PUT",
            )
            with urlopen(request, timeout=5) as response:
                response.read()

        await asyncio.to_thread(activate)
        await asyncio.sleep(0.25)

    @staticmethod
    def _require_loopback(url: str) -> None:
        host = urlparse(url).hostname or ""
        if host.casefold() == "localhost":
            return
        try:
            if ipaddress.ip_address(host).is_loopback:
                return
        except ValueError:
            pass
        raise RuntimeError("CDP compatibility proxy requires a loopback endpoint")

    @staticmethod
    def _origin(url: str) -> str:
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return ""
        return f"{parsed.scheme.casefold()}://{parsed.netloc.casefold()}"


__all__ = ["ExistingPageCDPProxy"]
