from __future__ import annotations

import json
import unittest

from e2r.pro_first.browser.cdp_existing_page_proxy import ExistingPageCDPProxy


class ExistingPageCDPProxyTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        try:
            from websockets.asyncio.client import connect
            from websockets.asyncio.server import serve
        except ImportError as error:
            self.skipTest(f"websockets optional dependency unavailable: {error}")
        self.connect = connect
        self.received_methods: list[str] = []

        async def upstream_handler(socket) -> None:
            await socket.send(
                json.dumps(
                    {
                        "method": "Target.attachedToTarget",
                        "params": {
                            "sessionId": "NONCHAT-SESSION",
                            "targetInfo": {
                                "targetId": "NONCHAT-PAGE",
                                "type": "page",
                                "url": "https://example.com/",
                            },
                            "waitingForDebugger": False,
                        },
                    }
                )
            )
            await socket.send(
                json.dumps(
                    {
                        "method": "Target.attachedToTarget",
                        "params": {
                            "sessionId": "CHATGPT-SESSION",
                            "targetInfo": {
                                "targetId": "CHATGPT-PAGE",
                                "type": "page",
                                "url": "https://chatgpt.com/",
                            },
                            "waitingForDebugger": False,
                        },
                    }
                )
            )
            async for message in socket:
                request = json.loads(message)
                self.received_methods.append(str(request.get("method") or ""))
                await socket.send(
                    json.dumps(
                        {
                            "id": request["id"],
                            "result": {"product": "Chrome/test"},
                        }
                    )
                )

        self.upstream = await serve(
            upstream_handler,
            "127.0.0.1",
            0,
            ping_interval=None,
        )
        upstream_port = self.upstream.sockets[0].getsockname()[1]
        self.proxy = await ExistingPageCDPProxy.start(
            upstream_endpoint=f"ws://127.0.0.1:{upstream_port}",
            allowed_origin="https://chatgpt.com/",
        )

    async def asyncTearDown(self) -> None:
        await self.proxy.close()
        self.upstream.close()
        await self.upstream.wait_closed()

    async def test_filters_unrelated_pages_and_supplies_root_barrier(self) -> None:
        async with self.connect(
            self.proxy.endpoint,
            ping_interval=None,
        ) as client:
            attached = json.loads(await client.recv())
            self.assertEqual(
                attached["params"]["targetInfo"]["url"],
                "https://chatgpt.com/",
            )

            await client.send(
                json.dumps(
                    {"id": 1, "method": "Target.getTargetInfo"}
                )
            )
            barrier = json.loads(await client.recv())
            self.assertEqual(barrier["id"], 1)
            self.assertEqual(barrier["result"]["targetInfo"]["type"], "browser")

            await client.send(
                json.dumps({"id": 2, "method": "Browser.getVersion"})
            )
            forwarded = json.loads(await client.recv())
            self.assertEqual(forwarded["id"], 2)
            self.assertEqual(forwarded["result"]["product"], "Chrome/test")

        self.assertNotIn("Target.getTargetInfo", self.received_methods)
        self.assertIn("Browser.getVersion", self.received_methods)

    def test_rejects_non_loopback_upstream(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "loopback"):
            ExistingPageCDPProxy._require_loopback(
                "ws://remote.example/devtools/browser/example"
            )


if __name__ == "__main__":
    unittest.main()
