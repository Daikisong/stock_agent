"""Local DOM-contract mock driven by the production Playwright adapter."""

from __future__ import annotations

from contextlib import AbstractContextManager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import threading
from urllib.parse import parse_qs, urlparse


def render_mock_chatgpt(state: str = "READY_FOR_INPUT") -> str:
    login = state == "LOGIN_REQUIRED"
    composer = "" if login else """
      <main>
        <div data-message-id="old-turn"><button class="entity-underline">old_result.md</button></div>
        <button id="deep-research" data-testid="deep-research-toggle" aria-label="Deep research" aria-pressed="false">Deep research</button>
        <input id="packet-input" type="file" hidden>
        <div id="attachments"></div>
        <form id="composer-form">
          <div id="prompt-textarea" class="ProseMirror" contenteditable="true"></div>
          <button id="composer-submit-button" type="button" aria-label="Send">Send</button>
          <button data-testid="stop-button" type="button" hidden>Stop</button>
        </form>
      </main>
    """
    login_markup = '<a href="/auth/login">Log in</a>' if login else ""
    return f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>E2R Mock ChatGPT</title></head>
<body data-mock-state="{state}">
  {login_markup}
  {composer}
  <script>
    window.__submitCount = 0;
    const deep = document.querySelector('#deep-research');
    if (deep) deep.addEventListener('click', () => deep.setAttribute('aria-pressed', 'true'));
    const input = document.querySelector('#packet-input');
    if (input) input.addEventListener('change', () => {{
      const button = document.createElement('button');
      button.type = 'button';
      button.dataset.testid = 'behavior-btn-attachment';
      button.textContent = input.files[0].name;
      document.querySelector('#attachments').appendChild(button);
    }});
    const send = document.querySelector('#composer-submit-button');
    if (send) send.addEventListener('click', () => {{
      window.__submitCount += 1;
      document.body.dataset.mockState = 'RUNNING';
      document.querySelector('[data-testid="stop-button"]').hidden = false;
    }});
  </script>
</body>
</html>"""


class _MockHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        state = parse_qs(urlparse(self.path).query).get("state", ["READY_FOR_INPUT"])[0]
        body = render_mock_chatgpt(state).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, _format: str, *_args: object) -> None:
        return


class MockChatGPTServer(AbstractContextManager["MockChatGPTServer"]):
    def __init__(self) -> None:
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), _MockHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    @property
    def base_url(self) -> str:
        return f"http://127.0.0.1:{self.server.server_port}"

    def __enter__(self) -> "MockChatGPTServer":
        self.thread.start()
        return self

    def __exit__(self, *_args: object) -> None:
        self.server.shutdown()
        self.thread.join(timeout=5)
        self.server.server_close()


__all__ = ["MockChatGPTServer", "render_mock_chatgpt"]
